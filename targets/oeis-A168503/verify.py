"""Exact-arithmetic verification for OEIS A168503 D-finite recurrence.

Verifies (with zero floats):
1. Periodic continued fraction 1/(1 - x/(1 - 2x/(1 - 3x*A(x)))) and quadratic equation
   3x(1-x)A(x)^2 - A(x) + 1 - 2x = 0 match published OEIS A168503 data (n = 0..21).
2. Radical G.f. (1 - 6x(1-x)A(x))^2 == 1 - 12x + 36x^2 - 24x^3 up to x^50.
3. First-order ODE x(1-13x+48x^2-60x^3+24x^4)A'(x) + (1-8x+18x^2-24x^3+12x^4)A(x) == 1 - 6x + 6x^2
   holds identically up to x^50.
4. Mathar's conjectured 4-term recurrence holds identically for n = 4..60 (and n = 3 with a(-1)=0).
"""

from fractions import Fraction


PUBLISHED_A168503 = [
    1, 1, 3, 15, 87, 531, 3339, 21483, 140859, 938331, 6334875, 43257483,
    298276587, 2074128363, 14529077163, 102432060459, 726280074027,
    5175707802795, 37051160719275, 266319772644267, 1921345252699563,
    13907901060055467,
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


def series_inv_trunc(p: list[Fraction], max_deg: int) -> list[Fraction]:
    res = [Fraction(0)] * (max_deg + 1)
    inv0 = Fraction(1) / p[0]
    res[0] = inv0
    for m in range(1, max_deg + 1):
        res[m] = -sum(p[j] * res[m - j] for j in range(1, min(m + 1, len(p)))) * inv0
    return res


def main() -> None:
    max_n = 60

    # 1. Compute via 3x(1-x)A^2 - A + 1 - 2x = 0 and verify CF T(A) == A
    a = [0] * (max_n + 1)
    a[0] = 1
    for n in range(1, max_n + 1):
        rhs = (-2 if n == 1 else 0) + 3 * sum(a[k] * a[n - 1 - k] for k in range(n))
        if n >= 2:
            rhs -= 3 * sum(a[k] * a[n - 2 - k] for k in range(n - 1))
        a[n] = rhs

    assert a[: len(PUBLISHED_A168503)] == PUBLISHED_A168503

    # Verify CF fixed point directly up to x^50
    deg = 50
    a_frac = [Fraction(x) for x in a[: deg + 1]]
    d1 = [Fraction(1)] + [-3 * a_frac[m - 1] for m in range(1, deg + 1)]
    d2 = [Fraction(1)] + [-2 * series_inv_trunc(d1, deg)[m - 1] for m in range(1, deg + 1)]
    d3 = [Fraction(1)] + [-series_inv_trunc(d2, deg)[m - 1] for m in range(1, deg + 1)]
    assert series_inv_trunc(d3, deg) == a_frac

    # 2. Verify (1 - 6x(1-x)A(x))^2 == 1 - 12x + 36x^2 - 24x^3 up to x^50
    p6 = poly_mul_trunc([Fraction(0), Fraction(6), Fraction(-6)], a_frac, deg)
    y = [(Fraction(1) if m == 0 else Fraction(0)) - p6[m] for m in range(deg + 1)]
    expected_delta = [Fraction(1), Fraction(-12), Fraction(36), Fraction(-24)] + [Fraction(0)] * (deg - 3)
    assert poly_mul_trunc(y, y, deg) == expected_delta

    # 3. Verify 1st-order ODE up to x^50
    a_full = [Fraction(x) for x in a]
    a_deriv = [Fraction(n) * a_full[n] for n in range(1, deg + 2)]
    p1 = [Fraction(0), Fraction(1), Fraction(-13), Fraction(48), Fraction(-60), Fraction(24)]
    p0 = [Fraction(1), Fraction(-8), Fraction(18), Fraction(-24), Fraction(12)]
    lhs_ode = [
        u + v
        for u, v in zip(
            poly_mul_trunc(p1, a_deriv, deg),
            poly_mul_trunc(p0, a_full, deg),
        )
    ]
    expected_rhs = [Fraction(1), Fraction(-6), Fraction(6)] + [Fraction(0)] * (deg - 2)
    assert lhs_ode == expected_rhs

    # 4. Verify Mathar's recurrence for n = 3..60
    for n in range(3, max_n + 1):
        val = (
            (n + 1) * a[n]
            + (-13 * n + 5) * a[n - 1]
            + 6 * (8 * n - 13) * a[n - 2]
            + 12 * (-5 * n + 13) * a[n - 3]
            + 12 * (2 * n - 7) * (a[n - 4] if n >= 4 else 0)
        )
        assert val == 0, f"Mathar recurrence failed at n={n}"

    print(f"PASS: verified OEIS A168503 CF, ODE, and Mathar recurrence for n=4..{max_n}.")


if __name__ == "__main__":
    main()
