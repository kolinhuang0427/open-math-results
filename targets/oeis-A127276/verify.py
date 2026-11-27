"""Exact-arithmetic verification for OEIS A127276 Hankel transform conjecture.

Verifies:
1. Power series expansion of (sqrt(1-4x)-x)/(1-4x) matches b_m = C(2m,m) - 4^(m-1) + [m=0]/4.
2. Exact integer Hankel determinants det(b_{i+j})_{0<=i,j<=n} match published OEIS A127276 data
   and Mathar's formula 2^n - n*(n+1)*2^(n-2) for n = 0..25.
3. G.f. -(4x-1)(x-1)/(2x-1)^3 agrees with 2^n - n*(n+1)*2^(n-2) up to n = 40.
4. Laurent-Chebyshev diagonalization P C_n P^T = diag(1, 2, ..., 2) and bilinear forms
   v^T C_n^{-1} v = 2n+1, e_0^T C_n^{-1} e_0 = 2n+1, v^T C_n^{-1} e_0 = (-1)^n up to n = 20.
"""

from fractions import Fraction
from math import comb


PUBLISHED_A127276 = [
    1, 1, -2, -16, -64, -208, -608, -1664, -4352, -11008, -27136,
    -65536, -155648, -364544, -843776, -1933312, -4390912, -9895936,
    -22151168, -49283072, -109051904, -240123904, -526385152,
    -1149239296, -2499805184, -5419040768,
]


def det_exact(matrix: list[list[Fraction]]) -> Fraction:
    n = len(matrix)
    a = [[Fraction(val) for val in row] for row in matrix]
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
            factor = a[r][i] * inv
            if factor != 0:
                for c in range(i, n):
                    a[r][c] -= factor * a[i][c]
    return det


def chebyshev_monic_rows(max_n: int) -> list[list[Fraction]]:
    p = [[Fraction(1)]]
    if max_n >= 1:
        p.append([Fraction(-2), Fraction(1)])
    if max_n >= 2:
        p.append([Fraction(2), Fraction(-4), Fraction(1)])
    for k in range(3, max_n + 1):
        prev1, prev2 = p[k - 1], p[k - 2]
        cur = [Fraction(0)] * (k + 1)
        for i, coeff in enumerate(prev1):
            cur[i + 1] += coeff
            cur[i] -= 2 * coeff
        for i, coeff in enumerate(prev2):
            cur[i] -= coeff
        p.append(cur)
    return p


def gf_series(max_n: int) -> list[Fraction]:
    # -(4x - 1)(x - 1) / (2x - 1)^3 = (1 - 5x + 4x^2) / (1 - 2x)^3
    num = [Fraction(1), Fraction(-5), Fraction(4)]
    # Coefficients of (1 - 2x)^(-3) = sum C(m+2, 2) 2^m x^m
    inv_cubed = [Fraction(comb(m + 2, 2) * (2 ** m)) for m in range(max_n + 1)]
    res = []
    for n in range(max_n + 1):
        val = Fraction(0)
        for j, c in enumerate(num):
            if n - j >= 0:
                val += c * inv_cubed[n - j]
        res.append(val)
    return res


def main() -> None:
    max_n = 25

    # 1. Verify (sqrt(1-4x) - x)/(1-4x) series coefficients up to 2*max_n
    max_m = 2 * max_n
    # Compute sqrt(1 - 4x) via s(x)^2 = 1 - 4x in Q[[x]]
    sqrt_s = [Fraction(0)] * (max_m + 1)
    sqrt_s[0] = Fraction(1)
    for m in range(1, max_m + 1):
        rhs = Fraction(-4) if m == 1 else Fraction(0)
        conv = sum(sqrt_s[j] * sqrt_s[m - j] for j in range(1, m))
        sqrt_s[m] = (rhs - conv) / 2
    # Divide (sqrt(1-4x) - x) by (1 - 4x)
    num_b = [sqrt_s[m] - (Fraction(1) if m == 1 else Fraction(0)) for m in range(max_m + 1)]
    b = []
    acc = Fraction(0)
    for m in range(max_m + 1):
        acc = 4 * acc + num_b[m]
        b.append(acc)
        expected_b = Fraction(1) if m == 0 else Fraction(comb(2 * m, m) - 4 ** (m - 1))
        assert b[m] == expected_b, f"A127275 mismatch at m={m}"

    # 2. Verify exact Hankel determinants against published OEIS data and closed form
    for n in range(max_n + 1):
        hankel = [[b[i + j] for j in range(n + 1)] for i in range(n + 1)]
        val = det_exact(hankel)
        closed = Fraction(2 ** n) - Fraction(n * (n + 1)) * (Fraction(2) ** (n - 2))
        assert val == closed, f"Hankel mismatch at n={n}: {val} != {closed}"
        assert val == PUBLISHED_A127276[n], f"OEIS mismatch at n={n}"

    # 3. Verify generating function expansion up to n = 40
    gf = gf_series(40)
    for n in range(41):
        closed = Fraction(2 ** n) - Fraction(n * (n + 1)) * (Fraction(2) ** (n - 2))
        assert gf[n] == closed, f"GF mismatch at n={n}"

    # 4. Verify Laurent-Chebyshev diagonalization and bilinear forms up to n = 20
    p_rows = chebyshev_monic_rows(20)
    c_full = [[Fraction(comb(2 * (i + j), i + j)) for j in range(21)] for i in range(21)]
    for k in range(21):
        for l in range(21):
            entry = sum(
                p_rows[k][i] * c_full[i][j] * p_rows[l][j]
                for i in range(k + 1)
                for j in range(l + 1)
            )
            expected = (Fraction(1) if k == 0 else Fraction(2)) if k == l else Fraction(0)
            assert entry == expected, f"Orthogonality mismatch at k={k}, l={l}"
    for n in range(21):
        d = [Fraction(1) if k == 0 else Fraction(2) for k in range(n + 1)]
        p4 = [sum(p_rows[k][i] * (4 ** i) for i in range(k + 1)) for k in range(n + 1)]
        p0 = [p_rows[k][0] for k in range(n + 1)]
        assert sum(p4[k] * p4[k] / d[k] for k in range(n + 1)) == 2 * n + 1
        assert sum(p0[k] * p0[k] / d[k] for k in range(n + 1)) == 2 * n + 1
        assert sum(p4[k] * p0[k] / d[k] for k in range(n + 1)) == (-1) ** n

    print("PASS: verified OEIS A127276 Hankel determinants (n=0..25), GF (n=0..40), and Chebyshev diagonalization.")


if __name__ == "__main__":
    main()
