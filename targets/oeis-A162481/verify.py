"""Exact-arithmetic verification for OEIS A162481 D-finite recurrence.

Verifies (with zero floats):
1. Binomial formula Sum_{k=0..n} C(n+2k+2, n-k)*C_k and quadratic recurrence A(x) = 1/(1-x)^3 + x*A(x)^2
   match published OEIS A162481 data (n = 0..23).
2. Radical G.f. (1 - 2x A(x))^2 == (1 - 7x + 3x^2 - x^3)/(1-x)^3 up to x^50.
3. First-order ODE x(1 - 8x + 10x^2 - 4x^3 + x^4) A'(x) + (1 - 6x + 14x^2 - 4x^3 + x^4) A(x) == 1 + 2x
   holds identically up to x^50.
4. Mathar's conjectured 4-term recurrence holds for all n = 4..60 (and n=2, 3 with a(<0)=0).
"""

from fractions import Fraction
from math import comb


PUBLISHED_A162481 = [
    1, 4, 14, 54, 235, 1119, 5658, 29800, 161621, 896198, 5056824,
    28938519, 167548937, 979653821, 5776252440, 34305807512,
    205039491091, 1232333298174, 7443336041318, 45157243590384,
    275051410542141, 1681362181696823, 10311616254855422, 63428758470722109,
]


def poly_mul_trunc(p: list[Fraction], q: list[Fraction], max_deg: int) -> list[Fraction]:
    res = [Fraction(0)] * (max_deg + 1)
    for i, a in enumerate(p):
        if a == 0 or i > max_deg:
            continue
        for j, b in enumerate(q):
            if i + j > max_deg:
                break
            res[i + j] += a * b
    return res


def main() -> None:
    max_n = 60

    # 1. Compute via A(x) = 1/(1-x)^3 + x A(x)^2 and cross-check binomial formula
    a = [0] * (max_n + 1)
    a[0] = 1
    for n in range(1, max_n + 1):
        a[n] = comb(n + 2, 2) + sum(a[k] * a[n - 1 - k] for k in range(n))
        binom_val = sum(comb(n + 2 * k + 2, n - k) * (comb(2 * k, k) // (k + 1)) for k in range(n + 1))
        assert a[n] == binom_val, f"Binomial mismatch at n={n}"

    assert a[: len(PUBLISHED_A162481)] == PUBLISHED_A162481

    # 2. Verify (1-x)^3 * (1 - 2x A(x))^2 == 1 - 7x + 3x^2 - x^3 up to x^50
    deg = 50
    a_frac = [Fraction(x) for x in a]
    z = [Fraction(1)] + [-2 * a_frac[n - 1] for n in range(1, deg + 1)]
    r_poly = [Fraction(1), Fraction(-3), Fraction(3), Fraction(-1)]
    lhs_sq = poly_mul_trunc(r_poly, poly_mul_trunc(z, z, deg), deg)
    expected_q = [Fraction(1), Fraction(-7), Fraction(3), Fraction(-1)] + [Fraction(0)] * (deg - 3)
    assert lhs_sq == expected_q

    # 3. Verify 1st-order ODE up to x^50
    a_deriv = [Fraction(n) * a_frac[n] for n in range(1, deg + 2)]
    p1 = [Fraction(0), Fraction(1), Fraction(-8), Fraction(10), Fraction(-4), Fraction(1)]
    p0 = [Fraction(1), Fraction(-6), Fraction(14), Fraction(-4), Fraction(1)]
    lhs_ode = [
        u + v
        for u, v in zip(
            poly_mul_trunc(p1, a_deriv, deg),
            poly_mul_trunc(p0, a_frac, deg),
        )
    ]
    expected_rhs = [Fraction(1), Fraction(2)] + [Fraction(0)] * (deg - 1)
    assert lhs_ode == expected_rhs

    # 4. Verify Mathar's recurrence for n = 2..60
    for n in range(2, max_n + 1):
        val = (
            (n + 1) * a[n]
            + 2 * (1 - 4 * n) * a[n - 1]
            + 2 * (5 * n - 3) * a[n - 2]
            + 4 * (2 - n) * (a[n - 3] if n >= 3 else 0)
            + (n - 3) * (a[n - 4] if n >= 4 else 0)
        )
        assert val == 0, f"Mathar recurrence failed at n={n}"

    print(f"PASS: verified OEIS A162481 G.f., ODE, and Mathar recurrence for n=4..{max_n}.")


if __name__ == "__main__":
    main()
