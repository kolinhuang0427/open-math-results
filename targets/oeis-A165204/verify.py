"""Exact-arithmetic verification for OEIS A165204 Hankel transform conjecture.

Verifies (with zero floats):
1. A165203(x) = (1+x)*c(x)^3/(1-x*c(x)^3) matches radical form and published OEIS A165203 data.
2. Exact Hankel determinants H_n = det(b_{i+j})_{0<=i,j<=n} match published OEIS A165204 data,
   period-3 Fibonacci closed form, Colin Barker's G.f., and 4-term recurrence for n = 0..35.
3. Exact J-fraction coefficients (alpha_j, beta_j) of A165203 match the closed-form Fibonacci
   formulas for j = 0..32, and Heilermann diagonalization U_n H_n U_n^T = diag(1, beta_1, ...) holds
   for n = 0..16.
4. Period-3 Fibonacci sequence matches Barker's G.f. (1 - 8x + 2x^2 - x^3)/(1 - 3x + 8x^2 - 3x^3 + x^4)
   and 4-term recurrence up to n = 100.
"""

from fractions import Fraction
from math import comb


PUBLISHED_A165203 = [
    1, 5, 20, 81, 332, 1372, 5702, 23793, 99576, 417664, 1754866, 7383204,
    31096466, 131084954, 552969854, 2334012425, 9856336324, 41639407776,
    175971686398, 743888534968, 3145439344550, 13302946909338, 56272308538682,
]

PUBLISHED_A165204 = [
    1, -5, -21, -21, 89, 377, 377, -1597, -6765, -6765, 28657, 121393,
    121393, -514229, -2178309, -2178309, 9227465, 39088169, 39088169,
    -165580141, -701408733, -701408733, 2971215073, 12586269025,
    12586269025, -53316291173, -225851433717, -225851433717,
]


def poly_mul_trunc(p: list[Fraction], q: list[Fraction], deg: int) -> list[Fraction]:
    res = [Fraction(0)] * (deg + 1)
    for i, a in enumerate(p):
        if a == 0 or i > deg:
            continue
        for j, b in enumerate(q):
            if i + j > deg:
                break
            res[i + j] += a * b
    return res


def series_inv_trunc(p: list[Fraction], deg: int) -> list[Fraction]:
    res = [Fraction(0)] * (deg + 1)
    inv0 = Fraction(1) / p[0]
    res[0] = inv0
    for m in range(1, deg + 1):
        res[m] = -sum(p[j] * res[m - j] for j in range(1, min(m + 1, len(p)))) * inv0
    return res


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


def fib_list(max_idx: int) -> list[int]:
    f = [0, 1]
    while len(f) <= max_idx:
        f.append(f[-1] + f[-2])
    return f


def h_period3(n: int, fibs: list[int]) -> int:
    k, r = divmod(n, 3)
    if r == 0:
        return ((-1) ** k) * fibs[6 * k + 2]
    if r == 1:
        return ((-1) ** (k + 1)) * fibs[6 * k + 5]
    return ((-1) ** (k + 1)) * fibs[6 * k + 8]


def main() -> None:
    max_n = 35
    max_m = 2 * max_n

    # 1. Compute A165203 = (1+x)*c(x)^3 / (1 - x*c(x)^3)
    c = [Fraction(comb(2 * m, m), m + 1) for m in range(max_m + 1)]
    c3 = poly_mul_trunc(poly_mul_trunc(c, c, max_m), c, max_m)
    num_a = poly_mul_trunc([Fraction(1), Fraction(1)], c3, max_m)
    den_a = [Fraction(1)] + [-c3[m - 1] for m in range(1, max_m + 1)]
    b = poly_mul_trunc(num_a, series_inv_trunc(den_a, max_m), max_m)

    assert [int(x) for x in b[: len(PUBLISHED_A165203)]] == PUBLISHED_A165203

    # Verify radical form 2x(1-4x-x^2)*A(x) == (1+x)*((1-x)*sqrt(1-4x) + 5x - 1)
    sqrt14x = [Fraction(1)] + [Fraction(-2 * comb(2 * (m - 1), m - 1), m) for m in range(1, max_m + 2)]
    lhs_rad = poly_mul_trunc([Fraction(0), Fraction(2), Fraction(-8), Fraction(-2)], b, max_m)
    inner = [
        ((sqrt14x[m] - (sqrt14x[m - 1] if m >= 1 else 0)) + (Fraction(5) if m == 1 else Fraction(-1) if m == 0 else Fraction(0)))
        for m in range(max_m + 1)
    ]
    rhs_rad = poly_mul_trunc([Fraction(1), Fraction(1)], inner, max_m)
    assert lhs_rad == rhs_rad

    # 2. Verify exact Hankel determinants up to n = 35 against period-3 Fibonacci and OEIS data
    fibs = fib_list(700)
    h_vals = []
    for n in range(max_n + 1):
        h_n = det_exact([[b[i + j] for j in range(n + 1)] for i in range(n + 1)])
        assert h_n.denominator == 1
        val = h_n.numerator
        assert val == h_period3(n, fibs), f"Hankel mismatch at n={n}"
        h_vals.append(val)
    assert h_vals[: len(PUBLISHED_A165204)] == PUBLISHED_A165204

    # 3. Verify J-fraction coefficients (alpha_j, beta_j) and Heilermann orthogonal polynomials
    alphas_pred = [Fraction(5)]
    betas_pred = [None]
    for k in range(12):
        u_k = Fraction(fibs[6 * k + 2], 2 * fibs[6 * k + 5])
        if k == 0:
            betas_pred.append(Fraction(-5))
        else:
            betas_pred.append(Fraction(-fibs[6 * k + 5], fibs[6 * k + 2]))
            alphas_pred.append(Fraction(4))
        alphas_pred.append(-2 * u_k - 1)
        betas_pred.append(-4 * u_k * (u_k + 2))
        alphas_pred.append(2 * u_k + 3)
        betas_pred.append(Fraction(1) / (2 * (u_k + 2)))

    cur = list(b)
    for j in range(33):
        inv = series_inv_trunc(cur, len(cur) - 1)
        al = -inv[1]
        be = -inv[2]
        assert al == alphas_pred[j], f"alpha_{j} mismatch"
        assert be == betas_pred[j + 1], f"beta_{j+1} mismatch"
        cur = [-inv[m] / be for m in range(2, len(inv))]

    # Verify U_n H_n U_n^T = diag(1, beta_1, beta_1*beta_2, ...) for n = 16
    n_ortho = 16
    p_rows = [[Fraction(1)], [-alphas_pred[0], Fraction(1)]]
    for k in range(1, n_ortho):
        # p_{k+1}(t) = (t - alpha_k) p_k(t) - beta_k p_{k-1}(t)
        prev1, prev2 = p_rows[k], p_rows[k - 1]
        nxt = [Fraction(0)] * (k + 2)
        for i, coeff in enumerate(prev1):
            nxt[i + 1] += coeff
            nxt[i] -= alphas_pred[k] * coeff
        for i, coeff in enumerate(prev2):
            nxt[i] -= betas_pred[k] * coeff
        p_rows.append(nxt)

    prod_beta = [Fraction(1)]
    for k in range(1, n_ortho + 1):
        prod_beta.append(prod_beta[-1] * betas_pred[k])
    for k in range(n_ortho + 1):
        for l in range(n_ortho + 1):
            val = sum(
                p_rows[k][i] * b[i + j] * p_rows[l][j]
                for i in range(k + 1)
                for j in range(l + 1)
            )
            assert val == (prod_beta[k] if k == l else Fraction(0))

    # 4. Verify period-3 Fibonacci sequence satisfies Barker's G.f. and recurrence up to n = 100
    h_long = [h_period3(n, fibs) for n in range(101)]
    num_gf = [1, -8, 2, -1]
    den_gf = [1, -3, 8, -3, 1]
    for n in range(101):
        conv = sum(den_gf[j] * h_long[n - j] for j in range(min(5, n + 1)))
        expected = num_gf[n] if n < 4 else 0
        assert conv == expected, f"Barker GF mismatch at n={n}"
        if n >= 4:
            assert h_long[n] == 3 * h_long[n - 1] - 8 * h_long[n - 2] + 3 * h_long[n - 3] - h_long[n - 4]

    print("PASS: verified OEIS A165204 Hankel determinants (n=0..35), J-fraction (j=0..32), and Barker G.f. (n=0..100).")


if __name__ == "__main__":
    main()
