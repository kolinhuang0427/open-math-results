"""Exact-arithmetic verification for OEIS A157002 D-finite recurrence.

Verifies (with zero floats):
1. Riordan array sum Sum_{k=0..n} (-1)^floor((n-k+1)/2) C(k, floor((n-k)/2)) C_k and quadratic
   equation x(1+x) A(x)^2 - A(x) + 1 - x = 0 match published OEIS A157002 data (n = 0..27).
2. Radical G.f. (1 - 2x(1+x)A(x))^2 == 1 - 4x + 4x^3 holds up to x^50.
3. First-order ODE x(1 - 3x - 4x^2 + 4x^3 + 4x^4) A'(x) + (1 - 6x^2 - 2x^3 + 2x^4) A(x) == 1 - 3x^2
   holds identically up to x^50.
4. Mathar's conjectured 4-term recurrence holds identically for n = 4..60 (and n = 3 with a(-1)=0).
"""

from fractions import Fraction
from math import comb


PUBLISHED_A157002 = [
    1, 0, 1, 2, 6, 17, 51, 156, 488, 1552, 5006, 16337, 53849, 179015,
    599535, 2020924, 6851150, 23344138, 79902364, 274606264, 947240592,
    3278404274, 11381240074, 39621423949, 138288477617, 483805404673,
    1696318159457, 5959737806635,
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

    # 1. Compute via A(x) = 1 - x + x(1+x) A(x)^2 and cross-check Riordan sum
    a = [0] * (max_n + 1)
    a[0] = 1
    for n in range(1, max_n + 1):
        rhs = (-1 if n == 1 else 0) + sum(a[k] * a[n - 1 - k] for k in range(n))
        if n >= 2:
            rhs += sum(a[k] * a[n - 2 - k] for k in range(n - 1))
        a[n] = rhs

        # Verify against [x^n] (1 - x) c(x(1-x^2)) = [x^n] sum_{k>=0} C_k x^k (1-x)(1-x^2)^k
        # Wait: signed binomial sum in OEIS A157002:
        # Note (1-x) = 1 - x, and (1-x^2)^k has (-1)^j C(k, j) x^{2j}, so coeff of x^{n-k} in (1-x)(1-x^2)^k:
        riordan_val = 0
        for k in range(n + 1):
            d = n - k
            ck = comb(2 * k, k) // (k + 1)
            if d % 2 == 0:
                j = d // 2
                if j <= k:
                    riordan_val += ((-1) ** j) * comb(k, j) * ck
            else:
                j = (d - 1) // 2
                if j <= k:
                    riordan_val += ((-1) ** (j + 1)) * comb(k, j) * ck
        assert a[n] == riordan_val, f"Riordan mismatch at n={n}"

    assert a[: len(PUBLISHED_A157002)] == PUBLISHED_A157002

    # 2. Verify (1 - 2x(1+x)A(x))^2 == 1 - 4x + 4x^3 up to x^50
    deg = 50
    a_frac = [Fraction(x) for x in a]
    p2a = poly_mul_trunc([Fraction(0), Fraction(2), Fraction(2)], a_frac, deg)
    y = [(Fraction(1) if m == 0 else Fraction(0)) - p2a[m] for m in range(deg + 1)]
    expected_delta = [Fraction(1), Fraction(-4), Fraction(0), Fraction(4)] + [Fraction(0)] * (deg - 3)
    assert poly_mul_trunc(y, y, deg) == expected_delta

    # 3. Verify 1st-order ODE up to x^50
    a_deriv = [Fraction(n) * a_frac[n] for n in range(1, deg + 2)]
    p1 = [Fraction(0), Fraction(1), Fraction(-3), Fraction(-4), Fraction(4), Fraction(4)]
    p0 = [Fraction(1), Fraction(0), Fraction(-6), Fraction(-2), Fraction(2)]
    lhs_ode = [
        u + v
        for u, v in zip(
            poly_mul_trunc(p1, a_deriv, deg),
            poly_mul_trunc(p0, a_frac, deg),
        )
    ]
    expected_rhs = [Fraction(1), Fraction(0), Fraction(-3)] + [Fraction(0)] * (deg - 2)
    assert lhs_ode == expected_rhs

    # 4. Verify Mathar's recurrence for n = 3..60
    for n in range(3, max_n + 1):
        val = (
            (n + 1) * a[n]
            + 3 * (-n + 1) * a[n - 1]
            + 2 * (-2 * n + 1) * a[n - 2]
            + 2 * (2 * n - 7) * a[n - 3]
            + 2 * (2 * n - 7) * (a[n - 4] if n >= 4 else 0)
        )
        assert val == 0, f"Mathar recurrence failed at n={n}"

    print(f"PASS: verified OEIS A157002 G.f., ODE, and Mathar recurrence for n=4..{max_n}.")


if __name__ == "__main__":
    main()
