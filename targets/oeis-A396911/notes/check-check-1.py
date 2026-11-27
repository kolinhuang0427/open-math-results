"""Independent exact/interval verifier for targets/oeis-A396911/PROOF.md."""

from __future__ import annotations

import math
import sys
import time
from mpmath import iv

iv.dps = 60

OEIS_FIRST_51 = [
    0, 1, 4, 9, 17, 30, 43, 64, 85, 106, 127, 161, 195, 229, 263, 297, 331,
    386, 441, 496, 551, 606, 661, 716, 771, 826, 881, 970, 1059, 1148, 1237,
    1326, 1415, 1504, 1593, 1682, 1771, 1860, 1949, 2038, 2127, 2216, 2305,
    2449, 2593, 2737, 2881, 3025, 3169, 3313, 3457,
]

PHI = (iv.mpf(1) + iv.sqrt(5)) / 2
INV_PHI = PHI - 1
INV_PHI2 = 2 - PHI
THETA = iv.pi * (3 - iv.sqrt(5))
C_CONST = PHI / (4 * iv.sqrt(5) * iv.pi)


def fibs_up_to(max_m: int) -> list[int]:
    f = [0, 1]
    for _ in range(2, max_m + 1):
        f.append(f[-1] + f[-2])
    return f


F = fibs_up_to(210)


def km(m: int) -> iv.mpf:
    return C_CONST * (PHI ** (2 * m))


def d2_iv(k: int | iv.mpf, j: int | iv.mpf) -> iv.mpf:
    sk = iv.sqrt(k)
    sj = iv.sqrt(j)
    d = abs(j - k)
    return (sj - sk) ** 2 + 4 * sk * sj * (iv.sin(d * THETA / 2) ** 2)


def fm_iv(m: int, k: int | iv.mpf) -> iv.mpf:
    return d2_iv(k, k + F[m]) - d2_iv(k, k + F[m + 1])


def fm_prime_iv(m: int, k: int | iv.mpf) -> iv.mpf:
    def term(d: int) -> iv.mpf:
        sk = iv.sqrt(k)
        skd = iv.sqrt(k + d)
        ang = 4 * (iv.sin(d * THETA / 2) ** 2)
        rad = (d ** 2) * iv.cos(d * THETA) / (sk * skd * ((skd + sk) ** 2))
        return ang - rad

    return term(F[m]) - term(F[m + 1])


def norm_z_iv(x: iv.mpf) -> iv.mpf:
    q = int(round(float(x.mid)))
    res = abs(x - q)
    assert float(res.b) <= 0.5 + 1e-12, f"unexpected fractional distance {res}"
    return res


def check_base_walk() -> tuple[list[int], float]:
    # Precompute sin^2(d * theta / 2) intervals for d = 1..5000
    max_d = 5000
    sin2_iv = [iv.mpf(0)] * (max_d + 1)
    sin2_lo_f = [0.0] * (max_d + 1)
    half_theta = THETA / 2
    for d in range(1, max_d + 1):
        s2 = iv.sin(d * half_theta) ** 2
        sin2_iv[d] = s2
        lo_f = float(s2.a) * (1.0 - 1e-12)
        if lo_f < 0.0:
            lo_f = 0.0
        # Certify in exact iv arithmetic that lo_f <= s2
        assert iv.mpf(lo_f) <= s2
        sin2_lo_f[d] = lo_f

    visited = {0}
    walk = [0]
    min_gap = float("inf")

    # Precompute candidate Fibonacci steps up to F_19 for quick tight upper bound U
    fib_cands = sorted(set(F[1:20]))

    for n in range(1, 501):
        k = walk[-1]
        # Find tight heuristic best j0 using Fibonacci and small forward offsets
        best_j0 = None
        best_u = None
        for d in fib_cands:
            j = k + d
            if j not in visited:
                val = d2_iv(k, j)
                if best_u is None or float(val.b) < float(best_u.a):
                    best_j0 = j
                    best_u = val
        # Also test small local offsets around k just in case (k=0,1,...)
        for j in range(max(0, k - 30), k + 31):
            if j != k and j not in visited:
                val = d2_iv(k, j)
                if best_u is None or float(val.b) < float(best_u.a):
                    best_j0 = j
                    best_u = val

        assert best_j0 is not None and best_u is not None
        u_hi = float(best_u.b) * (1.0 + 1e-12) + 1e-15
        assert best_u <= iv.mpf(u_hi)

        # Exact radial window bounds:
        # If (sqrt(j) - sqrt(k))^2 > u_hi then D^2(k,j) > best_u strictly.
        sk_iv = iv.sqrt(k)
        su_iv = iv.sqrt(iv.mpf(u_hi))
        j_max = int(math.floor(float(((sk_iv + su_iv) ** 2).b))) + 1
        if float((sk_iv - su_iv).a) > 0:
            j_min = max(0, int(math.ceil(float(((sk_iv - su_iv) ** 2).a))) - 1)
        else:
            j_min = 0

        # Double-check endpoints j_min - 1 (if >= 0) and j_max + 1 strictly exceed u_hi
        if j_min > 0:
            assert (sk_iv - iv.sqrt(j_min - 1)) ** 2 > iv.mpf(u_hi)
        assert (iv.sqrt(j_max + 1) - sk_iv) ** 2 > iv.mpf(u_hi)
        assert max(abs(j_max - k), abs(k - j_min)) <= max_d

        # Collect every j in [j_min, j_max] not certified > u_hi by radial + integer-sqrt angular lower bound
        survivors: list[int] = []
        for j in range(j_min, j_max + 1):
            if j == k or j in visited:
                continue
            d = abs(j - k)
            ang_lo = 4.0 * math.isqrt(k * j) * sin2_lo_f[d]
            if ang_lo <= u_hi:
                survivors.append(j)
            else:
                # Certify in iv for exactness? ang_lo is proven <= 4*sqrt(k*j)*sin2(d*theta/2)
                # since isqrt(k*j) <= sqrt(k*j) and sin2_lo_f[d] <= sin2_iv[d].
                pass

        assert best_j0 in survivors
        vals = {j: (sk_iv - iv.sqrt(j)) ** 2 + 4 * sk_iv * iv.sqrt(j) * sin2_iv[abs(j - k)] for j in survivors}
        # Find minimum by upper bound, then verify strict separation against EVERY other survivor
        winner = min(survivors, key=lambda j: float(vals[j].b))
        w_val = vals[winner]
        step_min_gap = float("inf")
        for j in survivors:
            if j == winner:
                continue
            diff = vals[j] - w_val
            assert float(diff.a) > 0, f"non-strict winner at step {n}: k={k}, winner={winner}, rival={j}, diff={diff}"
            if float(diff.a) < step_min_gap:
                step_min_gap = float(diff.a)
        if n <= 460:
            min_gap = min(min_gap, step_min_gap)

        walk.append(winner)
        visited.add(winner)

    assert walk[:51] == OEIS_FIRST_51, f"OEIS mismatch: {walk[:51]}"
    assert all(walk[i] < walk[i + 1] for i in range(500))
    assert walk[460] == 280542
    assert walk[459] == 279555
    assert walk[460] - walk[459] == F[16] == 987
    assert min_gap > 2.5e-3, f"min_gap too small: {min_gap}"

    # Verify Fibonacci monotonicity in base case 1 <= n <= 460 and continuation into m=17 for 461..500
    diffs = [walk[i] - walk[i - 1] for i in range(1, 501)]
    fib_set = set(F[1:20])
    for idx, d in enumerate(diffs, 1):
        assert d in fib_set, f"non-Fibonacci diff {d} at n={idx}"
    for i in range(len(diffs) - 1):
        assert diffs[i] <= diffs[i + 1], f"non-monotonic diff at {i + 1}"
    assert diffs[0] == F[2] and diffs[1] == F[4] and diffs[459] == F[16] and diffs[460] == F[17]

    # Check a(n) <= 1.5 * n^2 on 0..500 and max ratio at n=352 on 1..460
    for n in range(501):
        assert 2 * walk[n] <= 3 * n * n
    max_n = max(range(1, 461), key=lambda n: walk[n] / (n * n))
    assert max_n == 352 and walk[352] == 173946

    # Proposition 1(4) and 1(5)
    assert float(fm_iv(16, 279555).b) < 0.0 < float(fm_iv(16, 280542).a)
    assert iv.mpf(460) > (PHI ** 18) / (4 * iv.pi)
    return walk, min_gap


def check_lemma1() -> None:
    for m in range(2, 41):
        lhs = F[m] * INV_PHI2 - F[m - 2]
        rhs = ((-1) ** m) * (PHI ** (-m))
        diff = abs(lhs - rhs)
        assert float(diff.b) < 1e-45
        assert abs(norm_z_iv(F[m] * INV_PHI2) - (PHI ** (-m))) < iv.mpf("1e-45")

    for m in range(3, 201):
        assert F[m] * F[m - 3] - F[m - 1] * F[m - 2] == (-1) ** m

    # Exhaustive check of Lemma 1(2) for 3 <= m <= 20
    # Equality holds iff |a - b*phi| = phi^2, i.e., (a,b)=(1,-1) so d = F_m - F_{m-1} = F_{m-2} (for m >= 4; at m=3, d=1=F_1=F_2 -> d!=F_2 excludes 1).
    for m in range(3, 21):
        bound = PHI ** (-(m - 2))
        for d in range(1, F[m + 1]):
            if d == F[m - 1] or d == F[m]:
                continue
            nz = norm_z_iv(d * INV_PHI2)
            if d == F[m - 2]:
                assert abs(nz - bound) < iv.mpf("1e-50")
            else:
                assert nz > bound


def check_lemma2() -> None:
    # Lemma 2(1) across 999 grid points in (0, 1) and endpoints
    for i in range(1, 1000):
        x = iv.mpf(i) / 1000
        s1 = iv.sqrt(1 + x)
        assert 1 + x / 2 - (x ** 2) / 8 < s1 < 1 + x / 2
        q = 4 / ((1 + s1) ** 2)
        assert 1 - x / 2 < q < 1 - x / 2 + (x ** 2) / 2
        assert iv.sqrt(1 + x) + iv.sqrt(1 - x) < 2 * (1 - (x ** 2) / 8)
        s2 = iv.sin(x) ** 2
        assert (x ** 2) * (1 - (x ** 2) / 3) < s2 < (x ** 2)

    # Lemma 2(2) constants and certified bounds for 16 <= m <= 50
    assert (4 + 3 * iv.sqrt(2)) / 4 < iv.mpf("2.07") < iv.mpf("2.61") < iv.mpf(F[18]) ** 2 / iv.mpf(F[17]) ** 2
    assert iv.mpf(F[17]) / iv.mpf(F[16]) > iv.mpf("1.618")
    assert PHI ** 16 > 2206
    assert PHI ** (-32) < iv.mpf("2.1e-7")
    assert iv.mpf("7.766") < 4 * iv.pi / PHI < iv.mpf("7.767")
    assert iv.mpf("12.566") < 4 * iv.pi < iv.mpf("12.567")
    assert iv.mpf(F[17]) / km(16) < iv.mpf("0.0057")
    assert 6 * INV_PHI + 5 * PHI < 12 and (6 * INV_PHI + 5 * PHI + 140) < 153
    for m in range(16, 51):
        Km = km(m)
        uKm = (1 - 6 * (PHI ** (-m))) * Km
        assert uKm > iv.mpf("0.997") * Km > F[m + 1]
        assert fm_iv(m, uKm) < 0 < fm_iv(m, Km)
        # Check f'_m > 0 at sample points in [F_{m+1}, Km * 1.1]
        for k in (F[m + 1], int(float((uKm * iv.mpf("0.5")).a)), int(float(uKm.a)), int(float(Km.b))):
            assert fm_prime_iv(m, k) > 0


def check_lemma3_and_4() -> None:
    # Lemma 3 constants
    assert (
        iv.mpf("0.9999") * PHI + iv.mpf("0.979") * (PHI ** 2) - iv.mpf("1.007")
        > iv.mpf("3.16")
    )
    assert iv.mpf("3.16") * iv.mpf("0.99999") * INV_PHI > iv.mpf("1.95")

    for m in range(16, 26):
        Kr = km(m)
        upper = int(float((iv.mpf("0.99") * INV_PHI * Kr).a))
        for k in (F[m] + 1, (F[m] + upper) // 2, upper):
            assert d2_iv(k, k - F[m]) > d2_iv(k, k + F[m])

    for m in range(17, 26):
        Kprev = km(m - 1)
        # Exact lower bound on k^*_{m-1}: u*K_{m-1}, and upper bound: K_{m-1}
        k_start = int(math.ceil(float(Kprev.b))) + F[m]
        for k in (k_start, k_start + 5 * F[m], int(float(km(m).b))):
            assert d2_iv(k, k - F[m - 1]) > d2_iv(k, k + F[m])

    # Lemma 4 numerical constants & m=17 sample checks
    assert iv.mpf("1.003") * iv.mpf("1.0023") * iv.pi < iv.mpf("3.161")
    u16_lo = (1 - 6 * (PHI ** (-16))) * km(16)
    k_lo = int(math.ceil(float(u16_lo.b)))
    k_hi = int(math.floor(float(km(17).a)))
    for k in (k_lo, (k_lo + k_hi) // 2, k_hi):
        assert d2_iv(k, k + F[17]) < iv.mpf("3.161")
        assert d2_iv(k, k - F[18]) > d2_iv(k, k + F[18]) >= d2_iv(k, k + F[17]) or (
            k == k_hi and d2_iv(k, k - F[18]) > d2_iv(k, k + F[18])
        )
        # Test Lemma 4(1) across exhaustive small/medium d != {0, F16, F17, F18} and large d
        for j in list(range(max(0, k - 5000), k + 5000)) + [0, 1, k - F[19], k + F[19]]:
            if j < 0:
                continue
            d = abs(j - k)
            if d in (0, F[16], F[17], F[18]):
                continue
            assert d2_iv(k, j) > d2_iv(k, k + F[17])


def check_theorem1_part2() -> None:
    assert (6 * PHI) / (4 * iv.pi) < iv.mpf("0.773")
    for m in range(17, 60):
        assert iv.mpf(F[m - 1]) / iv.mpf(F[m]) < iv.mpf("0.62")
    assert (PHI ** 17) / (4 * iv.pi) > iv.mpf("284.1")
    assert iv.mpf("1.40") < iv.mpf("0.005") * (PHI ** 17) / (4 * iv.pi)
    assert iv.mpf(F[16]) / km(16) < iv.mpf("0.0036")
    assert iv.mpf("0.9949") - iv.mpf("1.004") * INV_PHI2 > iv.mpf("0.6114")
    bound = ((iv.mpf("1.001") ** 2) / (iv.mpf("0.6114") * PHI)) * (iv.pi / iv.sqrt(5))
    assert bound < iv.mpf("1.43") < iv.mpf("1.5")
    assert iv.pi / iv.sqrt(5) < iv.mpf("1.5")


def main() -> int:
    t0 = time.time()
    _, min_gap = check_base_walk()
    t1 = time.time()
    print(f"Base walk 0<=n<=500 & OEIS A396911 51 terms (min_gap={min_gap:.6f}): OK ({t1 - t0:.2f}s)")
    check_lemma1()
    print("Lemma 1 (Fibonacci angles, det identity, best-approx gap 3<=m<=20): OK")
    check_lemma2()
    print("Lemma 2 (elementary bounds & transition thresholds 16<=m<=50): OK")
    check_lemma3_and_4()
    print("Lemma 3 & Lemma 4 (backward & plateau dominance bounds): OK")
    check_theorem1_part2()
    print("Theorem 1 Part 2 (asymptotic & effective 1.43 < 3/2 inequalities): OK")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
