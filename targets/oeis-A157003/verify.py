"""Exact-arithmetic verification for OEIS A157003 D-finite recurrence.

Verifies (with zero floats):
1. Riordan sum and quadratic equation x(1-x^2) A(x)^2 - A(x) + 1 = 0 match published OEIS A157003 data (n = 0..27).
2. Radical G.f. (1 - 2x(1-x^2)A(x))^2 == 1 - 4x + 4x^3 up to x^50.
3. First-order ODE x(1 - 4x - x^2 + 8x^3 - 4x^5)A'(x) + (1 - 2x - 3x^2 + 8x^3 - 6x^5)A(x) == 1 - 3x^2
   holds identically up to x^50.
4. Kotesovec's recurrence (n >= 5) and Mathar's 6-term recurrence (n >= 6) hold up to n = 60.
"""

from fractions import Fraction
from math import comb


PUBLISHED_A157003 = [
    1, 1, 2, 4, 10, 27, 78, 234, 722, 2274, 7280, 23617, 77466, 256481,
    856016, 2876940, 9728090, 33072228, 112974592, 387580856, 1334821448,
    4613225722, 15994465796, 55615889745, 193904367362, 677709772035,
    2374027931492, 8333765738127,
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

    # 1. Compute from A(x) = 1 + x(1-x^2) A(x)^2 and cross-check Riordan sum
    a = [0] * (max_n + 1)
    a[0] = 1
    for n in range(1, max_n + 1):
        rhs = sum(a[k] * a[n - 1 - k] for k in range(n))
        if n >= 3:
            rhs -= sum(a[k] * a[n - 3 - k] for k in range(n - 2))
        a[n] = rhs

        # Riordan sum: Sum_{k=0..n, n-k even} (-1)^((n-k)//2) C(k, (n-k)//2) C_k
        riordan = 0
        for k in range(n + 1):
            if (n - k) % 2 == 0:
                j = (n - k) // 2
                if j <= k:
                    riordan += ((-1) ** j) * comb(k, j) * (comb(2 * k, k) // (k + 1))
        assert a[n] == riordan, f"Riordan mismatch at n={n}"

    assert a[: len(PUBLISHED_A157003)] == PUBLISHED_A157003

    # 2. Verify (1 - 2x(1-x^2)A(x))^2 == 1 - 4x + 4x^3 up to x^50
    deg = 50
    a_frac = [Fraction(x) for x in a]
    p2a = poly_mul_trunc([Fraction(0), Fraction(2), Fraction(0), Fraction(-2)], a_frac, deg)
    y = [(Fraction(1) if m == 0 else Fraction(0)) - p2a[m] for m in range(deg + 1)]
    expected_delta = [Fraction(1), Fraction(-4), Fraction(0), Fraction(4)] + [Fraction(0)] * (deg - 3)
    assert poly_mul_trunc(y, y, deg) == expected_delta

    # 3. Verify 1st-order ODE up to x^50
    a_deriv = [Fraction(n) * a_frac[n] for n in range(1, deg + 2)]
    p1 = [Fraction(0), Fraction(1), Fraction(-4), Fraction(-1), Fraction(8), Fraction(0), Fraction(-4)]
    p0 = [Fraction(1), Fraction(-2), Fraction(-3), Fraction(8), Fraction(0), Fraction(-6)]
    lhs_ode = [
        u + v
        for u, v in zip(
            poly_mul_trunc(p1, a_deriv, deg),
            poly_mul_trunc(p0, a_frac, deg),
        )
    ]
    expected_rhs = [Fraction(1), Fraction(0), Fraction(-3)] + [Fraction(0)] * (deg - 2)
    assert lhs_ode == expected_rhs

    # 4. Verify Kotesovec (n >= 5) and Mathar (n >= 6) recurrences up to n = 60
    for n in range(3, max_n + 1):
        kot = (
            (n + 1) * a[n]
            - 2 * (2 * n - 1) * a[n - 1]
            - (n + 1) * a[n - 2]
            + 8 * (n - 2) * a[n - 3]
            - 2 * (2 * n - 7) * (a[n - 5] if n >= 5 else 0)
        )
        assert kot == 0, f"Kotesovec recurrence failed at n={n}"
    for n in range(5, max_n + 1):
        mat = (
            (n + 1) * a[n]
            + (n + 2) * a[n - 1]
            + (-21 * n + 29) * a[n - 2]
            + (3 * n - 16) * a[n - 3]
            + 40 * (n - 3) * a[n - 4]
            + 2 * (-2 * n + 7) * a[n - 5]
            + 10 * (-2 * n + 9) * (a[n - 6] if n >= 6 else 0)
        )
        assert mat == 0, f"Mathar recurrence failed at n={n}"

    print(f"PASS: verified OEIS A157003 G.f., ODE, and Mathar recurrence for n=6..{max_n}.")


if __name__ == "__main__":
    main()
