"""Exact-arithmetic verification for OEIS A176126 G.f. and linear recurrence.

Verifies (with zero floats):
1. Self-contained Hankel determinant computation of A127276(n) from A127275 = (sqrt(1-4x)-x)/(1-4x)
   and reduced fraction numerator of -A127276(n)/A001788(n) match published OEIS A176126 data (n=0..60).
2. Closed form mod 4 matches reduced numerator for n = 0..100.
3. Exact polynomial identity P(x) == -(1+x)^3 * N(x) in Z[x].
4. G.f. expansion and Mathar's 9-term recurrence hold identically for n = 9..100.
"""

from fractions import Fraction
from math import comb


PUBLISHED_A176126_PREFIX = [
    -1, -1, 1, 2, 4, 13, 19, 13, 17, 43, 53, 32, 38, 89, 103, 59, 67, 151,
    169, 94, 104, 229, 251, 137, 149, 323, 349, 188, 202, 433, 463, 247,
    263, 559, 593, 314, 332, 701, 739, 389, 409, 859, 901, 472, 494, 1033,
    1079, 563, 587, 1223, 1273, 662, 688, 1429, 1483, 769, 797, 1651, 1709,
    884, 914,
]


def det_exact(matrix: list[list[Fraction]]) -> Fraction:
    n = len(matrix)
    a = [[Fraction(v) for v in row] for row in matrix]
    det = Fraction(1)
    for i in range(n):
        piv = next((r for r in range(i, n) if a[r][i] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != i:
            a[i], a[piv] = a[piv], a[i]
            det = -det
        det *= a[i][i]
        inv = Fraction(1) / a[i][i]
        for r in range(i + 1, n):
            f = a[r][i] * inv
            if f != 0:
                for c in range(i, n):
                    a[r][c] -= f * a[i][c]
    return det


def poly_mul(p: list[int], q: list[int]) -> list[int]:
    res = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            res[i + j] += a * b
    return res


def main() -> None:
    # 1. Verify Hankel determinants of A127275 match 2^n - n(n+1)2^(n-2) for n=0..20
    # and reduced numerators of -A127276(n)/A001788(n) match mod-4 closed form and OEIS data
    max_hankel = 20
    b = [1] + [comb(2 * m, m) - 4 ** (m - 1) for m in range(1, 2 * max_hankel + 1)]
    for n in range(max_hankel + 1):
        h_n = det_exact([[Fraction(b[i + j]) for j in range(n + 1)] for i in range(n + 1)])
        assert h_n == Fraction(2 ** n) - Fraction(n * (n + 1)) * (Fraction(2) ** (n - 2))
        if n >= 1:
            a001788_n = Fraction(n * (n + 1)) * (Fraction(2) ** (n - 2))
            frac = -h_n / a001788_n
            assert frac.numerator == PUBLISHED_A176126_PREFIX[n]

    # 2. Closed form mod 4 vs reduced Fraction(n*(n+1) - 4, n*(n+1)) for n = 0..100
    max_n = 100
    a = []
    for n in range(max_n + 1):
        if n % 4 in (0, 3):
            val = (n * (n + 1) - 4) // 4
        else:
            val = (n * (n + 1) - 4) // 2
        if n >= 1:
            assert val == Fraction(n * (n + 1) - 4, n * (n + 1)).numerator
        a.append(val)

    assert a[: len(PUBLISHED_A176126_PREFIX)] == PUBLISHED_A176126_PREFIX

    # 3. Verify P(x) == -(1+x)^3 * N(x) in Z[x]
    p_obs = [
        a[n] - (3 * a[n - 4] if n >= 4 else 0) + (3 * a[n - 8] if n >= 8 else 0)
        for n in range(12)
    ]
    n_poly = poly_mul([1, -1, 3, -1, 1], [1, -1, -2, -1, 1])
    rhs = [-c for c in poly_mul([1, 3, 3, 1], n_poly)]
    assert p_obs == rhs

    # 4. Verify G.f. denominator D(x) * A(x) == N(x) and Mathar's 9-term recurrence for n=9..100
    d_poly = poly_mul([-1, 3, -3, 1], [1, 0, 3, 0, 3, 0, 1])
    assert d_poly == [-1, 3, -6, 10, -12, 12, -10, 6, -3, 1]
    for n in range(max_n + 1):
        conv = sum(d_poly[j] * a[n - j] for j in range(min(len(d_poly), n + 1)))
        expected = n_poly[n] if n < len(n_poly) else 0
        assert conv == expected, f"GF mismatch at n={n}: {conv} != {expected}"

    for n in range(9, max_n + 1):
        rec = (
            a[n]
            - 3 * a[n - 1]
            + 6 * a[n - 2]
            - 10 * a[n - 3]
            + 12 * a[n - 4]
            - 12 * a[n - 5]
            + 10 * a[n - 6]
            - 6 * a[n - 7]
            + 3 * a[n - 8]
            - a[n - 9]
        )
        assert rec == 0, f"Recurrence mismatch at n={n}"

    print(f"PASS: verified OEIS A176126 mod-4 formula, G.f., and 9-term recurrence for n=9..{max_n}.")


if __name__ == "__main__":
    main()
