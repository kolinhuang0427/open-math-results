#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A024199 (Peter Bala, Nov 15 2016).

Verifies directly from OEIS A024199 rev. 80 and PROOF.md using pure Python
int/Fraction arithmetic (zero floating-point operations).
"""

from __future__ import annotations

from fractions import Fraction
import math
import sys

OEIS_DATA = [
    0,
    1,
    2,
    13,
    76,
    789,
    7734,
    110937,
    1528920,
    28018665,
    497895210,
    11110528485,
    241792844580,
    6361055257725,
    163842638377950,
    4964894559637425,
    147721447995130800,
    5066706567801827025,
    171002070002301095250,
    6548719685561840296125,
    247199273204273879989500,
]


def odd_df_m(m: int) -> Fraction:
    """Exact odd double factorial (2m - 1)!! for any integer m."""
    if m == 0:
        return Fraction(1)
    if m > 0:
        prod = 1
        for j in range(1, m + 1):
            prod *= 2 * j - 1
        return Fraction(prod)
    # m = -r <= -1, r >= 1: (-1)^r / (2r - 1)!!
    r = -m
    denom = 1
    for j in range(1, r + 1):
        denom *= 2 * j - 1
    sign = -1 if (r % 2 == 1) else 1
    return Fraction(sign, denom)


def a_def(n: int) -> int:
    """OEIS NAME definition: a(n) = (2n-1)!! * sum_{k=0..n-1} (-1)^k / (2k+1)."""
    if n == 0:
        return 0
    pref = odd_df_m(n)
    total = Fraction(0)
    for k in range(n):
        sign = 1 if (k % 2 == 0) else -1
        total += Fraction(sign, 2 * k + 1)
    res = pref * total
    assert res.denominator == 1, f"a({n}) is not an integer: {res}"
    return res.numerator


def T_term(n: int, k: int) -> Fraction:
    sign = 1 if ((n - k + 1) % 2 == 0) else -1
    return Fraction(sign * math.factorial(k)) * odd_df_m(n - k - 1)


def b_bala(n: int) -> Fraction:
    if n == 0:
        return Fraction(0)
    return Fraction(1, 2) * sum((T_term(n, k) for k in range(2 * n)), Fraction(0))


def series_mul(p: list[Fraction], q: list[Fraction], deg: int) -> list[Fraction]:
    out = [Fraction(0)] * (deg + 1)
    for i in range(min(len(p), deg + 1)):
        if p[i] == 0:
            continue
        for j in range(min(len(q), deg + 1 - i)):
            out[i + j] += p[i] * q[j]
    return out


def series_diff(p: list[Fraction]) -> list[Fraction]:
    return [Fraction(k) * p[k] for k in range(1, len(p))]


def main() -> int:
    # 1. Primary DATA & Sloane recurrence verification
    a_vals = [a_def(n) for n in range(51)]
    assert a_vals[: len(OEIS_DATA)] == OEIS_DATA, "Mismatch against OEIS A024199 DATA"
    for n in range(1, 50):
        assert a_vals[n + 1] == 2 * a_vals[n] + (2 * n - 1) ** 2 * a_vals[n - 1]

    # 2. Lemma 1: (2m-1)*(2m-3)!! == (2m-1)!! for m in [-40, 40]
    for m in range(-40, 41):
        assert Fraction(2 * m - 1) * odd_df_m(m - 1) == odd_df_m(m), f"Lemma 1 failed at m={m}"

    # 3. Lemma 2: a(n) - (2n-1)*a(n-1) == (-1)^{n-1}*(2n-3)!! for n in [1, 50]
    for n in range(1, 51):
        lhs = Fraction(a_vals[n] - (2 * n - 1) * a_vals[n - 1])
        rhs = Fraction(-1 if (n - 1) % 2 else 1) * odd_df_m(n - 1)
        assert lhs == rhs, f"Lemma 2 failed at n={n}"

    # 4. Theorem 1: row identities, boundary cancellations, and b(n) == a(n)
    assert T_term(1, 0) == 1 and T_term(1, 1) == 1 and b_bala(1) == 1
    for n in range(2, 31):
        for k in range(2 * n - 2):
            tnk = T_term(n, k)
            tn1k = T_term(n - 1, k)
            tnkp1 = T_term(n, k + 1)
            assert tnk == Fraction(-(2 * n - 2 * k - 3)) * tn1k
            assert tnkp1 == Fraction(k + 1) * tn1k
            assert tnk - Fraction(2 * n - 1) * tn1k == Fraction(2) * (tnk - tnkp1)

        assert T_term(n, 0) == Fraction(-1 if (n - 1) % 2 else 1) * odd_df_m(n - 1)
        expected_top = Fraction(2 ** (n - 1) * math.factorial(n - 1))
        assert T_term(n, 2 * n - 2) == expected_top
        assert T_term(n, 2 * n - 1) == expected_top

    for n in range(1, 51):
        bn = b_bala(n)
        assert bn == Fraction(a_vals[n]), f"Bala sum mismatch at n={n}: {bn} vs {a_vals[n]}"

    # 5. Theorem 2: Formal power series EGF verification up to x^40
    deg = 40
    Y = [Fraction(a_vals[n], math.factorial(n)) for n in range(deg + 1)]
    Yp = series_diff(Y)  # degree deg - 1 = 39
    # ODE: (1 - 2x) Y'(x) - Y(x) = (1 + 2x)^{-1/2} in Q[[x]] mod x^40
    ode_lhs = [Fraction(0)] * deg
    for k in range(deg):
        ode_lhs[k] = Yp[k] - (Fraction(2) * Yp[k - 1] if k >= 1 else Fraction(0)) - Y[k]

    # (1 + 2x)^{-1/2} = sum_{m>=0} (-1)^m * (2m-1)!! / m! * x^m
    inv_sqrt_1p2x = [
        Fraction(-1 if m % 2 else 1) * odd_df_m(m) / Fraction(math.factorial(m))
        for m in range(deg)
    ]
    assert ode_lhs == inv_sqrt_1p2x, "ODE verification in Q[[x]] failed"

    # Explicit RHS: (1/2) * arcsin(2x) * (1 - 2x)^{-1/2} mod x^41
    inv_sqrt_1m2x = [odd_df_m(m) / Fraction(math.factorial(m)) for m in range(deg + 1)]
    half_arcsin_2x = [Fraction(0)] * (deg + 1)
    for m in range((deg - 1) // 2 + 1):
        d = 2 * m + 1
        # [x^{2m+1}] (1/2)*arcsin(2x) = 1/2 * (2m)! / (4^m (m!)^2 (2m+1)) * 2^{2m+1}
        # = (2m)! / ((m!)^2 * (2m+1)) = binom(2m, m) / (2m+1)
        coeff = Fraction(math.comb(2 * m, m), 2 * m + 1)
        half_arcsin_2x[d] = coeff
    egf_rhs = series_mul(half_arcsin_2x, inv_sqrt_1m2x, deg)
    assert Y == egf_rhs, "EGF series mismatch mod x^41"

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
