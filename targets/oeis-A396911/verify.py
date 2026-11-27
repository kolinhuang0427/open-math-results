#!/usr/bin/env python3
"""
Certified verification script for PROOF.md (OEIS A396911: Sean A. Irvine's conjecture
a(n) <= (3/2) n^2 for all n >= 0, plus monotonicity & Fibonacci differences).

Uses 100% certified mpmath.iv interval arithmetic (dps=50) and exact Python integers
(ZERO floating-point arithmetic in any certification step!) to verify:
  1. Proposition 1 (Base Case 0 <= n <= 460):
     - Exact walk a(0..460), certifying EVERY nearest-neighbor inequality
       D^2(k, a(n)) < D^2(k, j) for ALL unvisited j >= 0 via certified radial cutoffs
       and exact integer fixed-point angular pruning (zero floats!).
     - Strict monotonicity, Fibonacci differences F_2, F_4, ..., F_16, a(460) = 280542,
       a(459) = 279555 = a(460) - F_16.
     - Exact integer bound 2 * a(n) <= 3 * n^2 for all 0 <= n <= 460.
     - Certified sign checks f_16(279555) < 0 < f_16(280542) (certifying k*_16 < a(460) < k*_16 + F_16).
     - Certified inequality 460 > phi^18 / (4*pi).
  2. Every numerical constant inequality used in Lemmas 1-4 and Theorem 1 (certified in mpmath.iv!).
  3. Cross-check of Lemma 1(1)-(2) (best-approximation gap) exhaustively for m = 3..14,
     and cross-check of a(0..460) against OEIS data prefix.
"""

import signal
import time
import mpmath as mp
from mpmath import iv

# OEIS A396911 data prefix (n = 0..50) verbatim from OEIS rev 48
OEIS_DATA_51 = [
    0, 1, 4, 9, 17, 30, 43, 64, 85, 106, 127, 161, 195, 229, 263, 297, 331,
    386, 441, 496, 551, 606, 661, 716, 771, 826, 881, 970, 1059, 1148, 1237,
    1326, 1415, 1504, 1593, 1682, 1771, 1860, 1949, 2038, 2127, 2216, 2305,
    2449, 2593, 2737, 2881, 3025, 3169, 3313, 3457,
]


def iv_floor_int(x) -> int:
    """Exact certified floor of an mpmath.mpf lower endpoint."""
    # x is an mp.mpf; mp.floor(x) is exact integer mpf, verify via interval comparison
    m = int(mp.floor(x))
    assert iv.mpf(m) <= x and x < iv.mpf(m + 1)
    return m


def iv_ceil_int(x) -> int:
    """Exact certified ceiling of an mpmath.mpf upper endpoint."""
    m = int(mp.ceil(x))
    assert iv.mpf(m - 1) < x and x <= iv.mpf(m)
    return m


def verify_base_case_iv():
    """Certify Proposition 1 (0 <= n <= 460) with pure mpmath.iv + exact integer pruning."""
    t0 = time.time()
    iv.dps = 50
    mp.mp.dps = 50

    THETA_IV = iv.pi * (3 - iv.sqrt(5))
    PHI_IV = (1 + iv.sqrt(5)) / 2

    F = [0, 1]
    while len(F) < 25:
        F.append(F[-1] + F[-2])
    FIB_SET = set(F[1:])

    # Fixed-point integer scaling for 100% float-free certified angular pruning:
    # For each d >= 1, store S_INT[d] = floor(sin^2(d*theta/2).a * SCALE_S) <= sin^2(d*theta/2) * SCALE_S.
    SCALE_S = 10 ** 18
    SCALE_C = 10 ** 6
    SCALE_B = SCALE_S * SCALE_C  # 10 ** 24

    sin2_iv = [iv.mpf(0)]
    sin2_int = [0]

    def ensure_sin2(max_d: int):
        while len(sin2_iv) <= max_d:
            d = len(sin2_iv)
            val = iv.sin(d * THETA_IV / 2) ** 2
            sin2_iv.append(val)
            lb = iv_floor_int((val * SCALE_S).a)
            assert lb >= 0
            assert iv.mpf(lb) <= (val * SCALE_S).a
            sin2_int.append(lb)

    def dist2_iv(k1: int, k2: int):
        r1 = iv.sqrt(k1)
        r2 = iv.sqrt(k2)
        d = abs(k2 - k1)
        ensure_sin2(d)
        return (r2 - r1) ** 2 + 4 * r1 * r2 * sin2_iv[d]

    visited = {0}
    a = [0]
    k = 0
    min_gap = None
    min_gap_n = None
    max_num = 0
    max_den = 1
    max_n = 0

    N_BASE = 460
    # Track expected Fibonacci candidate order for fast initial upper bound (no floats!)
    fib_idx = 2  # F_2 = 1

    for n in range(1, N_BASE + 1):
        # Pick an unvisited witness j_guess to obtain a certified upper bound B = D^2(k, j_guess).b
        guess_cands = []
        for idx in range(max(1, fib_idx - 1), min(len(F), fib_idx + 3)):
            if k + F[idx] not in visited:
                guess_cands.append(k + F[idx])
        if n <= 6:
            for j in range(1, k + 15):
                if j not in visited:
                    guess_cands.append(j)
        best_guess_iv = None
        for j in guess_cands:
            v = dist2_iv(k, j)
            if best_guess_iv is None or v.b < best_guess_iv.b:
                best_guess_iv = v
        assert best_guess_iv is not None

        # Certified upper bound B_ub >= D^2(k, j_guess)
        # Use slightly widened B_wide to guarantee at least 2 candidates survive for strict gap check
        B_wide = (best_guess_iv.b * iv.mpf("1.5") + iv.mpf("1.5")).b
        rk_iv = iv.sqrt(k)
        sB_iv = iv.sqrt(B_wide)

        # Any integer j > j_hi has sqrt(j) > sqrt(k) + sqrt(B_wide) => (sqrt(j)-sqrt(k))^2 > B_wide
        j_hi = iv_ceil_int(((rk_iv + sB_iv) ** 2).b)
        if rk_iv.a > sB_iv.b:
            j_lo = max(0, iv_floor_int(((rk_iv - sB_iv) ** 2).a))
        else:
            j_lo = 0

        # Certified check on the radial window endpoints:
        assert ((iv.sqrt(j_hi + 1) - rk_iv) ** 2).a > B_wide
        if j_lo > 0:
            assert ((rk_iv - iv.sqrt(j_lo - 1)) ** 2).a > B_wide

        max_d = max(k - j_lo, j_hi - k)
        ensure_sin2(max_d)

        # Exact integer angular pruning:
        # For every j in [j_lo, j_hi], D^2(k, j) >= 4*sqrt(j_lo * k) * sin^2(|j-k|*theta/2).
        # If c_int * sin2_int[d] > b_int, then 4*sqrt(j_lo*k)*sin^2(d*theta/2) > B_wide rigorously!
        C_iv = 4 * iv.sqrt(j_lo) * rk_iv
        c_int = iv_floor_int((C_iv * SCALE_C).a)
        b_int = iv_ceil_int((iv.mpf(B_wide) * SCALE_B).b)
        assert iv.mpf(c_int) <= (C_iv * SCALE_C).a
        assert iv.mpf(b_int) >= (iv.mpf(B_wide) * SCALE_B).b

        cands = []
        if c_int == 0:
            for j in range(j_lo, j_hi + 1):
                if j != k and j not in visited:
                    cands.append(j)
        else:
            # Threshold on sin2_int[d]: survive iff c_int * sin2_int[d] <= b_int <=> sin2_int[d] <= b_int // c_int
            s_thresh = b_int // c_int
            for d in range(1, max_d + 1):
                if sin2_int[d] <= s_thresh:
                    jm = k - d
                    if jm >= j_lo and jm not in visited:
                        cands.append(jm)
                    jp = k + d
                    if jp <= j_hi and jp not in visited:
                        cands.append(jp)

        assert len(cands) >= 2, f"Expected >=2 unpruned candidates at n={n}"
        scored = [(dist2_iv(k, j), j) for j in cands]
        scored.sort(key=lambda pair: pair[0].a)
        best_iv, best_j = scored[0]
        second_iv, second_j = scored[1]

        # Strict certified separation: best_iv.b < second_iv.a <= all other scored[i][0].a
        # AND best_iv.b <= B_wide < all pruned indices!
        assert best_iv.b <= B_wide, f"best_iv.b > B_wide at n={n}"
        gap = second_iv.a - best_iv.b
        assert gap > 0, f"Certified gap failed at n={n}: best={best_j} vs second={second_j}"
        for other_iv, _ in scored[1:]:
            assert other_iv.a > best_iv.b

        if min_gap is None or gap < min_gap:
            min_gap = gap
            min_gap_n = (n, k, best_j, second_j)

        diff = best_j - k
        assert diff > 0, f"Non-increasing step at n={n}: {k} -> {best_j}"
        assert diff in FIB_SET, f"Non-Fibonacci step at n={n}: {diff}"
        if n >= 2:
            assert diff >= a[-1] - a[-2], f"Non-monotone Fibonacci jump at n={n}"
        while F[fib_idx] < diff:
            fib_idx += 1

        k = best_j
        visited.add(k)
        a.append(k)

        # Exact integer check of Irvine's conjecture: a(n) <= (3/2) * n^2
        assert 2 * k <= 3 * n * n, f"Conjecture failed at n={n}: a(n)={k}"
        if k * max_den > max_num * (n * n):
            max_num, max_den, max_n = k, n * n, n

    # Check OEIS prefix verbatim
    assert a[:len(OEIS_DATA_51)] == OEIS_DATA_51, "Mismatch with OEIS A396911 data prefix"
    assert a[460] == 280542 and a[459] == 279555 and a[460] - a[459] == F[16] == 987

    # Certified sign checks for f_16(279555) < 0 < f_16(280542)
    def f16_iv(kv: int):
        d1 = (iv.sqrt(kv + F[16]) - iv.sqrt(kv)) ** 2 + 4 * iv.sqrt(kv * (kv + F[16])) * (iv.sin(iv.pi * PHI_IV ** (-16)) ** 2)
        d2 = (iv.sqrt(kv + F[17]) - iv.sqrt(kv)) ** 2 + 4 * iv.sqrt(kv * (kv + F[17])) * (iv.sin(iv.pi * PHI_IV ** (-17)) ** 2)
        return d1 - d2

    v_lo = f16_iv(279555)
    v_hi = f16_iv(280542)
    assert v_lo.b < 0, f"f_16(279555) not certified < 0: {v_lo}"
    assert v_hi.a > 0, f"f_16(280542) not certified > 0: {v_hi}"

    # Certified inequality 460 > phi^18 / (4*pi)
    n16_asymp = (PHI_IV ** 18) / (4 * iv.pi)
    assert iv.mpf(460) > n16_asymp.b

    print(f"[OK] Proposition 1 (0 <= n <= 460) certified in pure mpmath.iv + exact int ({time.time() - t0:.2f}s):")
    print(f"     a(460)={a[460]}, a(459)={a[459]}, diff={a[460]-a[459]}=F_16, min gap={mp.nstr(mp.mpf(min_gap.a), 6)} at n={min_gap_n[0]}")
    print(f"     max a(n)/n^2 on 1..460: {max_num}/{max_den} = {mp.nstr(mp.mpf(max_num)/max_den, 8)} at n={max_n}")
    print(f"     f_16(279555) < 0 < f_16(280542) certified; 460 > phi^18/(4*pi) = {mp.nstr(mp.mpf(n16_asymp.b), 8)} certified.")
    return a


def verify_proof_constants_iv():
    """Certify EVERY numerical constant inequality used in Lemmas 1-4 and Theorem 1 via mpmath.iv."""
    iv.dps = 50
    phi = (1 + iv.sqrt(5)) / 2
    s5 = iv.sqrt(5)
    pi = iv.pi
    c = phi / (4 * s5 * pi)
    K16 = c * (phi ** 32)
    K17 = c * (phi ** 34)

    F = [0, 1]
    while len(F) < 25:
        F.append(F[-1] + F[-2])

    # Lemma 2(2) constants
    assert ((4 + 3 * iv.sqrt(2)) / 4).b < iv.mpf("2.07")
    assert iv.mpf("2.61") < (iv.mpf(F[18]) / F[17]) ** 2
    assert iv.mpf("2.61") < (iv.mpf(F[17]) / F[16]) ** 2
    assert (phi ** 16).a > iv.mpf("2206")
    assert (phi ** (-32)).b < iv.mpf("2.1e-7")
    assert (pi ** 2 / 3).b < iv.mpf("4")
    # x_m and x_{m+1} bounds for m >= 16:
    assert iv.mpf("7.76") < ((1 - phi ** (-32)) * 4 * pi / phi).a
    assert ((1 + phi ** (-32)) * 4 * pi / phi).b < iv.mpf("7.77")
    assert iv.mpf("12.56") < ((1 - phi ** (-34)) * 4 * pi).a
    assert ((1 + phi ** (-34)) * 4 * pi).b < iv.mpf("12.57")
    assert (iv.mpf("12.57") * phi ** (-16)).b < iv.mpf("0.0057")
    assert (1 - 6 * phi ** (-16)).a > iv.mpf("0.997")
    assert (iv.mpf("0.997") * K16).a > iv.mpf(F[17])
    # f_m(K_m) > 0 constants:
    assert 776 + 1256 == 2 * 1016
    err_Km = (phi / 2) * (iv.mpf("12.57") ** 2) + (phi / 8) * (iv.mpf("7.77") ** 2) + 6 / phi + 5 * phi
    assert err_Km.b < iv.mpf("153")
    assert (iv.mpf("10.16") * (phi ** 16)).a > iv.mpf("153")
    # f_m((1 - 6*phi^{-m}) K_m) < 0 constants:
    u_lo = iv.mpf("0.997")
    assert (iv.mpf("7.77") / u_lo).b < iv.mpf("7.80")
    assert (iv.mpf("12.57") / u_lo).b < iv.mpf("12.61")
    assert (iv.mpf("6") / (u_lo ** 2)).b < iv.mpf("6.04")
    assert (phi * iv.mpf("12.57")).b < iv.mpf("21")
    assert (iv.mpf("6.04") * iv.mpf("21")).b < iv.mpf("128")
    assert ((1 / phi) / (2 * u_lo) * (iv.mpf("7.80") ** 2)).b < iv.mpf("19")
    assert (6 / (phi * u_lo)).b < iv.mpf("4")
    assert ((1 / phi) / 8 * (iv.mpf("12.61") ** 2)).b < iv.mpf("13")
    assert (5 * phi ** (-3)).b < iv.mpf("2")
    assert 2 * 1200 - (777 + 1257) == 2 * 183
    assert (iv.mpf("1.83") * (phi ** 16)).a > iv.mpf("166")

    # Lemma 3(2) constants (m >= 17)
    assert (iv.mpf(F[17]) / K16).b < iv.mpf("0.0057")
    assert (iv.mpf(F[17]) / (iv.mpf("0.997") * K16)).b < iv.mpf("0.00572")
    assert ((iv.mpf("1.0057") ** 2) * (iv.mpf("1.00572") ** iv.mpf("1.5"))).b < iv.mpf("1.021")
    assert (1 - 2 * pi ** 2 * phi ** (-34)).a > iv.mpf("0.99999")
    assert (iv.mpf("0.99998") / iv.mpf("1.021")).a > iv.mpf("0.979")
    assert (iv.mpf("0.997") ** 2) > iv.mpf("0.994")
    assert (iv.mpf("1.00001") / iv.mpf("0.994")).b < iv.mpf("1.007")
    assert (iv.mpf("0.9999") * phi + iv.mpf("0.979") * (phi ** 2) - iv.mpf("1.007")).a > iv.mpf("3.16")
    assert (iv.mpf("3.16") * iv.mpf("0.99999") / phi).a > iv.mpf("1.95")

    # Lemma 4 constants (m >= 17)
    assert (iv.mpf(F[18]) / (iv.mpf("0.997") * K16)).b < iv.mpf("0.00926")
    assert (iv.mpf(F[19]) / (iv.mpf("0.997") * K16)).b < iv.mpf("0.0150")
    assert (phi / iv.mpf("0.997") + iv.mpf("0.997") / phi).b < (iv.mpf("1.0023") * s5).a
    assert (iv.mpf("1.003") * iv.mpf("1.0023") * pi).b < iv.mpf("3.161")
    assert ((1 - iv.mpf("1e-5")) / iv.mpf("1.008")).a > iv.mpf("0.992")
    assert (iv.mpf("0.992") * (pi / s5) * (phi ** 3)).a > iv.mpf("5.90")
    assert (phi ** (-15)).b < iv.mpf("0.00074")
    assert (1 - (pi ** 2 / 3) * phi ** (-30)).a > iv.mpf("0.99999")
    assert (iv.mpf("0.99") * iv.mpf("0.99999")).a > iv.mpf("0.989")
    assert (iv.mpf("0.989") * iv.mpf("0.997") * (pi / s5) * (phi ** 3)).a > iv.mpf("5.86")
    assert (iv.mpf("0.984") * iv.mpf("0.99999")).a > iv.mpf("0.983")
    assert ((1 - iv.mpf("1e-5")) / iv.mpf("1.005")).a > iv.mpf("0.995")
    assert (iv.mpf("0.983") * (pi / s5) * 2 * (phi ** 2)).a > iv.mpf("7.23")
    assert (iv.mpf("1.004") / (phi ** 2)).b < iv.mpf("0.39")
    assert (iv.mpf("0.99") / phi).a > iv.mpf("0.61")

    # Theorem 1 Part 2 constants (m >= 17)
    assert (6 * phi / (4 * pi)).b < iv.mpf("0.773")
    assert (iv.mpf(F[16]) / F[17]) < iv.mpf("0.62")
    assert (phi ** 17 / (4 * pi)).a > iv.mpf("284.1")
    assert (iv.mpf("1.40") / iv.mpf("284.1")).b < iv.mpf("0.005")
    assert (iv.mpf(F[16]) / K16).b < iv.mpf("0.0036")
    assert (iv.mpf("1.001") * iv.mpf("0.994")) > iv.mpf("0.9949")
    assert (iv.mpf("0.9949") - iv.mpf("1.004") / (phi ** 2)).a > iv.mpf("0.6114")
    assert (iv.mpf("0.6114") * phi).a > iv.mpf("0.989")
    assert (iv.mpf("1.001") ** 2) < iv.mpf("1.0021")
    assert (pi / s5).b < iv.mpf("1.405")
    assert (iv.mpf("1.0021") / iv.mpf("0.989") * iv.mpf("1.405")).b < iv.mpf("1.43")

    print("[OK] All analytical constant inequalities in Lemmas 2-4 and Theorem 1 certified in mpmath.iv.")


def verify_lemma1_exhaustively():
    """Exhaustively check Lemma 1(1)-(2) in mpmath.iv for m = 3..14."""
    iv.dps = 50
    phi = (1 + iv.sqrt(5)) / 2
    alpha = phi ** (-2)
    F = [0, 1]
    while len(F) < 20:
        F.append(F[-1] + F[-2])

    checked = 0
    for m in range(3, 15):
        # Lemma 1(1): |F_m * phi^{-2} - F_{m-2} - (-1)^m * phi^{-m}| == 0
        lhs = F[m] * alpha - F[m - 2]
        rhs = ((-1) ** m) * (phi ** (-m))
        assert (lhs - rhs).a <= 0 <= (lhs - rhs).b
        # Lemma 1(2): for all 1 <= d < F_{m+1}, d not in {F_{m-1}, F_m}: ||d*phi^{-2}||_Z >= phi^{-(m-2)}
        lb = phi ** (-(m - 2))
        for d in range(1, F[m + 1]):
            if d == F[m - 1] or d == F[m]:
                continue
            val = d * alpha
            q = int(mp.nint(val.mid))
            dist = abs(val - q)
            # Tight equality can occur at d = F_{m-2} (where dist = phi^{-(m-2)}); check dist.b >= lb.a
            # and for d != F_{m-2} check strict dist.a > lb.b!
            if d == F[m - 2]:
                assert dist.b >= lb.a and dist.a <= lb.b
            else:
                assert dist.a > lb.b, f"Lemma 1(2) failed at m={m}, d={d}"
            checked += 1

    print(f"[OK] Lemma 1(1)-(2) exhaustively verified in mpmath.iv for m=3..14 ({checked} non-Fibonacci values).")


def main():
    signal.alarm(60)
    t_start = time.time()
    print("Verifying PROOF.md for OEIS A396911 (Sean A. Irvine's conjecture a(n) <= (3/2) n^2)...")
    verify_lemma1_exhaustively()
    verify_proof_constants_iv()
    verify_base_case_iv()
    print(f"All certified checks completed in {time.time() - t_start:.2f}s.")
    print("PASS")


if __name__ == "__main__":
    main()
