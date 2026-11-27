#!/usr/bin/env python3
"""Exact integer/polynomial verification for gullerud-2201.08490-conj5.4 (Conj 5.4 at n=8)."""

from math import comb


def poly_add(a, b):
    n = max(len(a), len(b))
    res = [0] * n
    for i, c in enumerate(a):
        res[i] += c
    for i, c in enumerate(b):
        res[i] += c
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res


def poly_sub(a, b):
    return poly_add(a, [-c for c in b])


def poly_mul(a, b):
    res = [0] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        for j, cb in enumerate(b):
            res[i + j] += ca * cb
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res


def poly_eval(p, x):
    acc = 0
    for c in reversed(p):
        acc = acc * x + c
    return acc


def poly_det(mat):
    """Bareiss-free fraction-free exact determinant over Z[lambda] via Laplace expansion for n<=9."""
    n = len(mat)
    if n == 1:
        return mat[0][0]
    if n == 2:
        return poly_sub(poly_mul(mat[0][0], mat[1][1]), poly_mul(mat[0][1], mat[1][0]))
    total = [0]
    for j in range(n):
        if mat[0][j] == [0]:
            continue
        sub = [row[:j] + row[j + 1 :] for row in mat[1:]]
        term = poly_mul(mat[0][j], poly_det(sub))
        if j % 2 == 1:
            term = [-c for c in term]
        total = poly_add(total, term)
    return total


def f_char_det(n):
    """Compute f_n(lambda) = det(A_n - lambda I_n) directly from Definition 2.6."""
    mat = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append([0, -1])  # -lambda
            elif abs(i - j) == 1:
                row.append([1])
            else:
                row.append([0])
        mat.append(row)
    return poly_det(mat)


def f_recurrence(n_max):
    polys = [[1], [0, -1], [-1, 0, 1]]
    for n in range(3, n_max + 1):
        nxt = poly_sub(poly_mul([0, -1], polys[n - 1]), polys[n - 2])
        polys.append(nxt)
    return polys


def f_binomial(n):
    coeffs = [0] * (n + 1)
    for i in range(n // 2 + 1):
        sign = -1 if ((n + i) % 2 == 1) else 1
        coeffs[n - 2 * i] += sign * comb(n - i, i)
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    return coeffs


def main():
    # 1. Verify f_n(lambda) definitions agree: det(A_n - lambda I), recurrence, and Pascal binomial sum.
    polys = f_recurrence(30)
    for n in range(1, 9):
        assert f_char_det(n) == polys[n], f"det mismatch at n={n}"
    for n in range(1, 31):
        assert f_binomial(n) == polys[n], f"binomial mismatch at n={n}"

    # 2. Verify n=8, F_9 = 34 factorization: f_8(lambda) - 34 = (lambda^2 + 1) * P(lambda^2).
    fib = [0, 1]
    for _ in range(500):
        fib.append(fib[-1] + fib[-2])
    assert fib[9] == 34

    f8 = polys[8]
    assert f8 == [1, 0, -10, 0, 15, 0, -7, 0, 1]
    f8_minus_34 = poly_sub(f8, [34])
    P_z = [-33, 23, -8, 1]  # z^3 - 8z^2 + 23z - 33
    P_lam2 = [P_z[0], 0, P_z[1], 0, P_z[2], 0, P_z[3]]
    assert poly_mul([1, 0, 1], P_lam2) == f8_minus_34

    # 3. Verify P'(z) = 3z^2 - 16z + 23 has negative discriminant and P(4) < 0 < P(5).
    disc_P_prime = (-16) ** 2 - 4 * 3 * 23
    assert disc_P_prime == -20 < 0
    assert poly_eval(P_z, 4) == -5 < 0
    assert poly_eval(P_z, 5) == 7 > 0

    # 4. Verify Vieta elimination polynomial Q(z) and polynomial division + Bezout identity.
    # (-z^2 + 13z - 8)^2 * z - 132*(z+1)^2
    inner = [-8, 13, -1]
    Q_z = poly_sub(poly_mul([0, 1], poly_mul(inner, inner)), poly_mul([132], poly_mul([1, 1], [1, 1])))
    assert Q_z == [-132, -200, -340, 185, -26, 1]

    q_z = [18, -18, 1]  # z^2 - 18z + 18
    R_z = [462, -1208, 251]  # 251z^2 - 1208z + 462
    assert poly_add(poly_mul(q_z, P_z), R_z) == Q_z

    A_z = [13858805, -92031911]
    B_z = [2309921, -1223855, 366661]
    assert poly_add(poly_mul(A_z, P_z), poly_mul(B_z, R_z)) == [609842937]

    # Check the algebraic elimination step symbolically via exact bivariate polynomial arithmetic
    # in (z0, w) where z0 is a root of P, w = |z1|, s = 2*Re(z1) = 8 - z0, z0*w^2 = 33:
    # Check that (2*z0 + (z0 - 1)*(4 - z0/2)) * 2 == (-z0^2 + 13*z0 - 8).
    lhs = poly_add([0, 4], poly_mul([-1, 1], [8, -1]))  # 2*(2z0 + (z0-1)*(8-z0)/2) = 4z0 + (z0-1)(8-z0)
    assert lhs == [-8, 13, -1]

    print("PASS: gullerud-2201.08490-conj5.4 (Conj 5.4 at n=8) verified exactly.")


if __name__ == "__main__":
    main()
