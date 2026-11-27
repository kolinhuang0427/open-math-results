#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/oeis-A208425/.

Verifies strictly from OEIS A208425 (rev 60), FormalConjectures/OEIS/208425.lean,
and PROOF.md:
  - Both definitions of a(n) (GF vs binomial sum) + live OEIS A208425 data
  - Every intermediate lemma (Lemmas 1-5), exact rational polynomials (Lemma 5),
    polynomial congruence in F_p[X] (Lemma 4), Z[X] divisibility & 3-orbit
    cancellation (Lemma 3), harmonic/geometric congruences (Lemma 2)
  - Full target supercongruence conjecture_2 for all primes p == 1 (mod 3), p < 1000.
Pure exact integer / Fraction arithmetic; zero floats.
"""

from __future__ import annotations

import math
import signal
import sys
import time
from fractions import Fraction


def _alarm_handler(signum: int, frame: object) -> None:
    raise TimeoutError("Verification script exceeded 60s timeout")


# ---------------------------------------------------------------------------
# Exact polynomial arithmetic over Z, Q (Fraction), and F_p
# Polynomials are lists [c_0, c_1, ...] with trailing zeros stripped.
# ---------------------------------------------------------------------------

def poly_trim(p: list[int | Fraction], zero: int | Fraction = 0) -> list[int | Fraction]:
    out = list(p)
    while out and out[-1] == zero:
        out.pop()
    return out


def poly_add(p: list, q: list) -> list:
    n = max(len(p), len(q))
    res = [(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)]
    return poly_trim(res)


def poly_sub(p: list, q: list) -> list:
    n = max(len(p), len(q))
    res = [(p[i] if i < len(p) else 0) - (q[i] if i < len(q) else 0) for i in range(n)]
    return poly_trim(res)


def poly_mul(p: list, q: list) -> list:
    if not p or not q:
        return []
    res = [0 * p[0]] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a == 0:
            continue
        for j, b in enumerate(q):
            res[i + j] += a * b
    return poly_trim(res)


def poly_pow(p: list, e: int) -> list:
    res = [1]
    base = list(p)
    while e > 0:
        if e & 1:
            res = poly_mul(res, base)
        e >>= 1
        if e:
            base = poly_mul(base, base)
    return res


def poly_eval(p: list, x: int | Fraction) -> int | Fraction:
    acc = 0 * x
    for c in reversed(p):
        acc = acc * x + c
    return acc


def poly_int_from_zero(p: list[Fraction]) -> list[Fraction]:
    return poly_trim([Fraction(0)] + [c / (i + 1) for i, c in enumerate(p)], Fraction(0))


def poly_divmod_monic(num: list, mod_poly: list) -> tuple[list, list]:
    """Exact polynomial division in Z[X] or Q[X] by a monic polynomial."""
    assert mod_poly[-1] == 1
    rem = list(num)
    deg_m = len(mod_poly) - 1
    quo = [0 * num[0]] * max(0, len(num) - deg_m) if num else []
    for i in range(len(num) - 1, deg_m - 1, -1):
        c = rem[i]
        if c != 0:
            quo[i - deg_m] = c
            for j in range(deg_m + 1):
                rem[i - deg_m + j] -= c * mod_poly[j]
    return poly_trim(quo), poly_trim(rem)


def poly_mod_p(p: list, prime: int) -> list[int]:
    out = []
    for c in p:
        if isinstance(c, Fraction):
            assert c.denominator % prime != 0, f"Denominator divisible by {prime}: {c}"
            val = (c.numerator * pow(c.denominator, -1, prime)) % prime
        else:
            val = c % prime
        out.append(val)
    return poly_trim(out, 0)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def a_binomial(n: int) -> int:
    return sum(math.comb(n, k) * math.comb(n - k, k) * math.comb(n + k, k) for k in range(n + 1))


def a_gf_coeffs(max_n: int) -> list[int]:
    """Exact series expansion of sum_{m>=0} (3m)!/m!^3 * x^{2m}/(1-x)^{3m+1} up to x^{max_n}."""
    coeffs = [0] * (max_n + 1)
    for m in range(max_n // 2 + 1):
        pref = math.factorial(3 * m) // (math.factorial(m) ** 3)
        for j in range(2 * m, max_n + 1):
            d = j - 2 * m
            coeffs[j] += pref * math.comb(d + 3 * m, 3 * m)
    return coeffs


def harmonic_mod_p(m: int, p: int) -> int:
    return sum(pow(j, -1, p) for j in range(1, m + 1)) % p


def verify_oeis_definitions() -> None:
    # Live OEIS A208425 rev 60 full DATA field (24 terms, a(0)..a(23))
    oeis_data = [
        1, 1, 7, 25, 151, 751, 4411, 24697, 146455, 862351,
        5195257, 31392967, 191815339, 1177508515, 7276161907, 45154764025,
        281492498455, 1761076827895, 11055132835705, 69600761349175,
        439370198255401, 2780265190892641, 17631718101804517, 112038660509078695,
    ]
    gf = a_gf_coeffs(24)
    for j in range(25):
        assert gf[j] == a_binomial(j), f"Def equivalence failed at j={j}"
    assert gf[:24] == oeis_data, f"OEIS mismatch: {gf[:24]}"


def verify_lemma1(p: int, direct_sum_limit: int = 250) -> None:
    n = (p - 1) // 6
    p2 = p * p
    # Exact hockey-stick sum
    hs_sum = sum(
        math.comb(3 * k, k) * math.comb(2 * k, k) * math.comb(p + k, 3 * k + 1)
        for k in range(3 * n + 1)
    )
    if p <= direct_sum_limit:
        direct_sum = sum(a_binomial(j) for j in range(p))
        assert direct_sum == hs_sum, f"Hockey-stick mismatch at p={p}"

    # Check t_{2n} == C(4n, 2n) (mod p^2)
    t_2n = math.comb(6 * n, 2 * n) * math.comb(4 * n, 2 * n) * math.comb(p + 2 * n, p)
    assert (t_2n - math.comb(4 * n, 2 * n)) % p2 == 0

    # Check F(1) = 0 mod p iff sum a(j) == C(4n, 2n) mod p^2
    f1 = sum(
        (math.comb(2 * k, k) * pow(3 * k + 1, -1, p)) % p
        for k in range(3 * n + 1) if k != 2 * n
    ) % p
    lhs = hs_sum % p2
    rhs = math.comb(4 * n, 2 * n) % p2
    assert ((lhs - rhs) % p2 == 0) == (f1 == 0)
    assert f1 == 0, f"F(1) != 0 at p={p}"


def verify_lemma2(p: int) -> None:
    n = (p - 1) // 6
    p2 = p * p
    # (a) Harmonic identity
    hn = harmonic_mod_p(n, p)
    h2n = harmonic_mod_p(2 * n, p)
    h3n = harmonic_mod_p(3 * n, p)
    assert (hn - h2n - h3n) % p == 0, f"Lemma 2(a) failed at p={p}"

    # (b) Exact [x^{p-1}] identity + A_0 == A_1 (mod p) + sum_{k=0}^{p-1} C(2k,k) == 1 (mod p^2)
    exact_alt = sum(math.comb(2 * p, 6 * n - 3 * j) for j in range(2 * n + 1)) - sum(
        math.comb(2 * p, 6 * n - 3 * j - 1) for j in range(2 * n)
    )
    sum_central = sum(math.comb(2 * k, k) for k in range(p))
    assert sum_central == exact_alt, f"Lemma 2(b) exact [x^(p-1)] identity failed at p={p}"

    a_cls = [0, 0, 0]
    for t in range(1, 6 * n + 1):
        sign = -1 if (t & 1) else 1
        a_cls[t % 3] = (a_cls[t % 3] + sign * pow(t, -1, p)) % p
    assert a_cls[0] == a_cls[1], f"A_0 != A_1 at p={p}"
    assert (a_cls[0] - a_cls[2]) % p == 0, f"A_0 != A_2 at p={p}"
    assert sum_central % p2 == 1, f"Lemma 2(b) failed at p={p}"


def verify_lemma3(p: int, full_orbit_check: bool) -> None:
    n = (p - 1) // 6
    p2 = p * p
    # (a) Sum_{i=0}^{2n-1} 1 / ((2i+1) C(2i, i)) == 0 (mod p)
    s_a = sum(pow((2 * i + 1) * math.comb(2 * i, i), -1, p) for i in range(2 * n)) % p
    assert s_a == 0, f"Lemma 3(a) failed at p={p}"

    if full_orbit_check:
        # Check Phi(X) | L_poly(X) in Z[X]
        phi_poly = [1, -1, 1]  # 1 - X + X^2
        # L_poly(X) = (1 - X^p - (1-X)^p) / p in Z[X]
        l_num = [0] * (p + 1)
        l_num[0] = 1
        l_num[p] -= 1
        # subtract (1-X)^p
        for j in range(p + 1):
            l_num[j] -= ((-1) ** j) * math.comb(p, j)
        assert all(c % p == 0 for c in l_num)
        l_poly = [c // p for c in l_num]
        _, rem = poly_divmod_monic(l_poly, phi_poly)
        assert rem == [], f"Phi(X) does not divide L_poly(X) in Z[X] at p={p}: rem={rem}"

        # Check P(t) polynomial and integral
        u_int = [0, 1, -1]  # t - t^2
        p_poly = [0]
        u_pow = [1]
        for _ in range(2 * n):
            p_poly = poly_add(p_poly, u_pow)
            u_pow = poly_mul(u_pow, u_int)
        int_p_mod_p = sum(
            (c * pow(k + 1, -1, p)) % p for k, c in enumerate(p_poly)
        ) % p
        assert int_p_mod_p == s_a == 0

        # Check roots of Phi in F_p and 3-orbit cancellation across ALL x in F_p
        roots = [x for x in range(p) if (x * x - x + 1) % p == 0]
        assert len(roots) == 2
        zeta, zeta_inv = roots[0], roots[1]
        assert (zeta * zeta_inv) % p == 1
        l_fp = poly_mod_p(l_poly, p)
        p_fp = poly_mod_p(p_poly, p)
        for z in (0, 1, zeta, zeta_inv):
            assert poly_eval(l_fp, z) % p == 0

        seen = {0, 1, zeta, zeta_inv}
        u_elems = set(range(p)) - seen
        total_pl = 0
        for x in sorted(u_elems):
            if x in seen:
                continue
            y = pow((1 - x) % p, -1, p)
            z = ((x - 1) * pow(x, -1, p)) % p
            orbit = {x, y, z}
            assert len(orbit) == 3 and orbit <= u_elems
            seen |= orbit
            px = poly_eval(p_fp, x) % p
            py = poly_eval(p_fp, y) % p
            pz = poly_eval(p_fp, z) % p
            assert py == (((1 - x) ** 2) * px) % p
            assert pz == ((x ** 2) * px) % p
            lx = poly_eval(l_fp, x) % p
            ly = poly_eval(l_fp, y) % p
            lz = poly_eval(l_fp, z) % p
            assert ly == (-lx * pow((1 - x) % p, -1, p)) % p
            assert lz == (-lx * pow(x, -1, p)) % p
            orbit_sum = (px * lx + py * ly + pz * lz) % p
            assert orbit_sum == 0, f"3-orbit cancellation failed at p={p}, orbit={orbit}"
            total_pl = (total_pl + orbit_sum) % p
        assert seen == set(range(p)) and total_pl == 0

    # (b) Adamchuk congruence: sum_{k=0}^{4n} C(2k,k) == 1 (mod p^2)
    adam = sum(math.comb(2 * k, k) for k in range(4 * n + 1)) % p2
    assert adam == 1, f"Adamchuk congruence failed at p={p}: {adam}"


def verify_lemma4_and_5(p: int) -> None:
    n = (p - 1) // 6
    u_q = [Fraction(0), Fraction(1), Fraction(-1)]
    # Q_{4n+1}(X) = int_0^X u(t)^{4n} dt in Q[X]
    u4n = poly_pow(u_q, 4 * n)
    q4n1 = poly_int_from_zero(u4n)

    # Lemma 5: exact rational identity 2 Q_{4n+1}(X) == Q_{4n+1}(1) * (1 + (2X-1) * sum_{k=0}^{4n} C(2k,k) u(X)^k)
    q_at_1 = poly_eval(q4n1, Fraction(1))
    assert q_at_1 == Fraction(math.factorial(4 * n) ** 2, math.factorial(8 * n + 1))
    sum_poly: list[Fraction] = []
    u_k = [Fraction(1)]
    for k in range(4 * n + 1):
        c_k = Fraction(math.comb(2 * k, k))
        term = [c_k * v for v in u_k]
        sum_poly = poly_add(sum_poly, term)
        u_k = poly_mul(u_k, u_q)
    lhs_l5 = [2 * c for c in q4n1]
    rhs_inner = poly_add([Fraction(1)], poly_mul([Fraction(-1), Fraction(2)], sum_poly))
    rhs_l5 = [q_at_1 * c for c in rhs_inner]
    assert lhs_l5 == rhs_l5, f"Lemma 5 exact Q[X] identity failed at p={p}"

    # Lemma 4(a): p Q_{4n+1}(1) == C(4n, 2n) mod p^2
    c4n2n = math.comb(4 * n, 2 * n)
    diff_4a = Fraction(p) * q_at_1 - Fraction(c4n2n)
    assert diff_4a.denominator % p != 0 and diff_4a.numerator % (p * p) == 0

    # Q_tilde(X) in Z_(p)[X]
    xp_term = [Fraction(0)] * p + [Fraction(c4n2n, p)]
    q_tilde = poly_sub(q4n1, xp_term)
    # Check all denominators prime to p
    for c in q_tilde:
        assert c.denominator % p != 0, f"Q_tilde denominator divisible by p={p}: {c}"
    qt_at_1 = poly_eval(q_tilde, Fraction(1))
    assert qt_at_1.denominator % p != 0 and qt_at_1.numerator % p == 0

    # Lemma 4(b): H(u(X)) == A(X) in F_p[X]
    # H(X) = sum_{0<=k<=3n, k!=2n} 3*C(2k,k)/(3k+1) * X^{k+4n+1} mod p
    h_fp = [0] * (7 * n + 2)
    for k in range(3 * n + 1):
        if k == 2 * n:
            continue
        h_fp[k + 4 * n + 1] = (3 * math.comb(2 * k, k) * pow(3 * k + 1, -1, p)) % p
    h_fp = poly_trim(h_fp, 0)
    # Compose H(u(X)) mod p
    u_int = [0, 1, -1]
    hu_fp: list[int] = []
    u_pow_mod = [1]
    for d in range(len(h_fp)):
        if d > 0:
            u_pow_mod = poly_mod_p(poly_mul(u_pow_mod, u_int), p)
        if h_fp[d] != 0:
            scaled = [(h_fp[d] * c) % p for c in u_pow_mod]
            hu_fp = poly_mod_p(poly_add(hu_fp, scaled), p)

    # R(X) = (u(X)^p - X^p + X^{2p}) / p in Z[X]
    u_p = poly_pow(u_int, p)
    r_num = list(u_p)
    r_num[p] -= 1
    r_num[2 * p] += 1
    assert all(c % p == 0 for c in r_num)
    r_poly = [c // p for c in r_num]

    # A(X) = (1 - 2X^p) * Q_tilde(X) - C(4n,2n) * R(X)
    qt_fp = poly_mod_p(q_tilde, p)
    one_minus_2xp = [0] * (p + 1)
    one_minus_2xp[0] = 1
    one_minus_2xp[p] = (-2) % p
    r_fp = poly_mod_p(r_poly, p)
    a_fp = poly_mod_p(
        poly_sub(poly_mul(one_minus_2xp, qt_fp), [c4n2n * v for v in r_fp]),
        p,
    )
    assert hu_fp == a_fp, f"Lemma 4(b) H(u(X)) != A(X) mod {p}"

    # Completion mod Phi(X): check 2*Q_tilde(X) mod Phi(X) lies in p*Z_{(p)}[X]
    phi_q = [Fraction(1), Fraction(-1), Fraction(1)]
    _, rem_qt = poly_divmod_monic([Fraction(2) * c for c in q_tilde], phi_q)
    for c in rem_qt:
        assert c.denominator % p != 0 and c.numerator % p == 0


def main() -> int:
    signal.signal(signal.SIGALRM, _alarm_handler)
    signal.alarm(60)
    t0 = time.monotonic()

    verify_oeis_definitions()
    print("OEIS A208425 rev 60 definitions (GF == trinomial sum, all 24 live OEIS DATA terms): PASS")

    primes_1000 = [p for p in range(7, 1000) if p % 3 == 1 and is_prime(p)]
    primes_500 = [p for p in primes_1000 if p < 500]
    primes_l5 = [p for p in primes_1000 if p <= 43]

    for p in primes_500:
        verify_lemma1(p, direct_sum_limit=250)
        verify_lemma2(p)
        verify_lemma3(p, full_orbit_check=(p <= 200))
    print(f"Lemmas 1, 2, 3 (incl. full 3-orbit F_p check for p<=200, direct sum p<=250) on {len(primes_500)} primes p<500: PASS")

    for p in primes_l5:
        verify_lemma4_and_5(p)
    print(f"Lemmas 4 & 5 (exact Q[X] telescoping, F_p[X] ODE match, mod Phi(X) reduction) on {primes_l5}: PASS")

    # Full target conjecture_2 exact check up to p < 1000 using exact integer hockey-stick identity
    for p in primes_1000:
        n = (p - 1) // 6
        p2 = p * p
        lhs = sum(
            math.comb(3 * k, k) * math.comb(2 * k, k) * math.comb(p + k, 3 * k + 1)
            for k in range(3 * n + 1)
        ) % p2
        rhs = math.comb(2 * (p - 1) // 3, (p - 1) // 3) % p2
        assert lhs == rhs, f"conjecture_2 failed at p={p}"
    print(f"Target conjecture_2 verified across all {len(primes_1000)} primes p == 1 (mod 3), p < 1000: PASS")

    elapsed = time.monotonic() - t0
    print(f"PASS (all checks passed in {elapsed:.3f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
