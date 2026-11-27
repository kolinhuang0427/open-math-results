"""Exact-arithmetic verification for OEIS A178072 D-finite recurrence.

Verifies:
1. Algebraic equation (2x + x^3) A(x)^2 - (1 + x)^2 A(x) + 1 = 0, radical G.f.,
   and binomial formula match published OEIS A178072 data (n = 0..33).
2. Exact 1st-order ODE A_1(x) A'(x) + A_0(x) A(x) == R_1(x) up to x^55.
3. Exact 2nd-order ODE P_2(x) A''(x) + P_1(x) A'(x) + P_0(x) A(x) == R_2(x) (deg R_2 = 5) up to x^55.
4. Mathar's conjectured 7-term recurrence holds identically for n = 7..60 (and at n = 6 with a(-1) = 0).
"""

from fractions import Fraction
from math import comb, factorial


PUBLISHED_A178072 = [
    1, 0, -1, -1, -1, -1, 1, 8, 23, 45, 55, -14, -317, -1095, -2459, -3574,
    -681, 16124, 64605, 159483, 260869, 134374, -906919, -4228769,
    -11317061, -20327731, -15742753, 52640154, 293447719, 847451759,
    1648865921, 1636313816, -2986606297, -21074495982,
]


def binom_ext(n: int, k: int) -> int:
    if k < 0:
        return 0
    if n >= 0:
        return comb(n, k) if k <= n else 0
    num = 1
    for i in range(k):
        num *= n - i
    return num // factorial(k)


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

    # 1. Compute A(x) from (1+x)^2 A = 1 + (2x + x^3) A^2
    a = [0] * (max_n + 1)
    a[0] = 1
    for n in range(1, max_n + 1):
        rhs = 2 * sum(a[k] * a[n - 1 - k] for k in range(n))
        if n >= 3:
            rhs += sum(a[k] * a[n - 3 - k] for k in range(n - 2))
        lhs_prev = 2 * a[n - 1] + (a[n - 2] if n >= 2 else 0)
        a[n] = rhs - lhs_prev

    assert a[: len(PUBLISHED_A178072)] == PUBLISHED_A178072

    # Cross-check OEIS binomial formula for n = 0..25
    for n in range(26):
        s = Fraction(0)
        for k in range(n // 2 + 1):
            c1 = Fraction(comb(n - k, k), n - 2 * k + 1)
            inner = sum(
                comb(k, i)
                * binom_ext(n - k - i - 1, n - 2 * k - i)
                * (2 ** (n - 2 * k - i))
                * ((-1) ** (k - i))
                for i in range(min(k, n - 2 * k) + 1)
            )
            s += c1 * inner
        assert s == a[n], f"Binomial sum mismatch at n={n}"

    # 2. Check radical G.f. ((1+x)^2 + sqrt(1 - 4x + 6x^2 + x^4)) * A(x) == 2
    delta = [Fraction(0)] * (max_n + 1)
    delta[0], delta[1], delta[2], delta[4] = Fraction(1), Fraction(-4), Fraction(6), Fraction(1)
    y = [Fraction(0)] * (max_n + 1)
    y[0] = Fraction(1)
    for m in range(1, max_n + 1):
        conv = sum(y[j] * y[m - j] for j in range(1, m))
        y[m] = (delta[m] - conv) / 2
    r_plus_y = [
        (Fraction(1) if m in (0, 2) else Fraction(2) if m == 1 else Fraction(0)) + y[m]
        for m in range(max_n + 1)
    ]
    a_frac = [Fraction(x) for x in a]
    prod_rad = poly_mul_trunc(r_plus_y, a_frac, max_n)
    assert prod_rad == [Fraction(2)] + [Fraction(0)] * max_n

    # 3. Check 1st-order ODE up to x^(max_n - 1)
    deg1 = max_n - 1
    a_d1 = [Fraction(n) * a_frac[n] for n in range(1, max_n + 1)]
    a1 = [Fraction(0), Fraction(2), Fraction(-8), Fraction(13), Fraction(-4), Fraction(8), Fraction(0), Fraction(1)]
    a0 = [Fraction(2), Fraction(-4), Fraction(3), Fraction(-10), Fraction(10), Fraction(0), Fraction(1)]
    r1_exp = [Fraction(2), Fraction(-4), Fraction(-3), Fraction(2), Fraction(-1)] + [Fraction(0)] * (deg1 - 4)
    lhs1 = [
        u + v
        for u, v in zip(
            poly_mul_trunc(a1, a_d1, deg1),
            poly_mul_trunc(a0, a_frac, deg1),
        )
    ]
    assert lhs1 == r1_exp

    # 4. Check 2nd-order ODE up to x^(max_n - 2)
    deg2 = max_n - 2
    a_d2 = [Fraction(n * (n - 1)) * a_frac[n] for n in range(2, max_n + 1)]
    p2 = [Fraction(0), Fraction(0), Fraction(2), Fraction(2), Fraction(-27), Fraction(61), Fraction(-12), Fraction(40), Fraction(1), Fraction(5)]
    p1 = [Fraction(0), Fraction(4), Fraction(8), Fraction(-90), Fraction(236), Fraction(-96), Fraction(282), Fraction(8), Fraction(44)]
    p0 = [Fraction(0), Fraction(4), Fraction(-30), Fraction(12), Fraction(-150), Fraction(240), Fraction(6), Fraction(34)]
    r2_exp = [Fraction(0), Fraction(4), Fraction(-42), Fraction(-36), Fraction(34), Fraction(-24)] + [Fraction(0)] * (deg2 - 5)
    t2 = poly_mul_trunc(p2, a_d2, deg2)
    t1 = poly_mul_trunc(p1, a_d1, deg2)
    t0 = poly_mul_trunc(p0, a_frac, deg2)
    lhs2 = [t2[k] + t1[k] + t0[k] for k in range(deg2 + 1)]
    assert lhs2 == r2_exp

    # 5. Check Mathar's 7-term recurrence for n = 6..max_n
    for n in range(6, max_n + 1):
        val = (
            2 * n * (n + 1) * a[n]
            + 2 * n * (n + 1) * a[n - 1]
            - 3 * (3 * n - 1) * (3 * n - 4) * a[n - 2]
            + (61 * n * n - 191 * n + 36) * a[n - 3]
            + 6 * (-2 * n * n + 2 * n - 1) * a[n - 4]
            + 2 * (5 * n - 1) * (4 * n - 15) * a[n - 5]
            + n * (n - 5) * a[n - 6]
            + (5 * n - 1) * (n - 6) * (a[n - 7] if n >= 7 else 0)
        )
        assert val == 0, f"Mathar recurrence failed at n={n}"

    print(f"PASS: verified OEIS A178072 G.f., ODEs, and Mathar recurrence for n=7..{max_n}.")


if __name__ == "__main__":
    main()
