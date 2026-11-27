#!/usr/bin/env python3
"""
Independent exact-arithmetic verifier for targets/oeis-A176126/
directly from live OEIS A176126 rev. 18, A127276 rev. 33, A127275, A001788,
and PROOF.md without reading verify.py or author notes. Zero floats.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb
import sympy as sp


def verify_lemma1_hankel() -> None:
    """Independently verify Lemma 1 (A127276(n) = det(M_n) = 2^n - n(n+1)2^{n-2})."""
    x, t, z = sp.symbols("x t z")

    # 1. Power series of (sqrt(1 - 4x) - x)/(1 - 4x) vs b_m
    M_ser = 18
    ser = sp.Poly(sp.series((sp.sqrt(1 - 4 * x) - x) / (1 - 4 * x), x, 0, M_ser + 1).removeO(), x)
    b = [int(ser.coeff_monomial(x**m)) for m in range(M_ser + 1)]
    assert b[0] == 1
    for m in range(1, M_ser + 1):
        assert b[m] == comb(2 * m, m) - 4 ** (m - 1)

    # 2. Polynomial recurrence P_k(t(z)) == z^k + z^{-k} in Z[z, z^{-1}]
    P_polys = [sp.Integer(1), t - 2, t**2 - 4 * t + 2]
    for k in range(3, 12):
        P_polys.append(sp.expand((t - 2) * P_polys[-1] - P_polys[-2]))
    tz = z + 2 + z**-1
    for k in range(1, len(P_polys)):
        assert sp.expand(P_polys[k].subs(t, tz) - (z**k + z**-k)) == 0
        assert P_polys[k].subs(t, 4) == 2
        assert P_polys[k].subs(t, 0) == 2 * ((-1) ** k)

    # 3. Direct Hankel matrix M_n = (b_{i+j}), decomposition C_n - 1/4 vv^T + 1/4 e0 e0^T,
    #    quadratic forms v^T C_n^{-1} v = 2n+1, e0^T C_n^{-1} e0 = 2n+1, v^T C_n^{-1} e0 = (-1)^n,
    #    and det(M_n) = 2^n - n(n+1)2^{n-2} for n = 0..8.
    for n in range(9):
        M_mat = sp.Matrix(n + 1, n + 1, lambda i, j: b[i + j])
        C_mat = sp.Matrix(n + 1, n + 1, lambda i, j: comb(2 * (i + j), i + j))
        v_vec = sp.Matrix(n + 1, 1, lambda i, _: 4**i)
        e0_vec = sp.Matrix(n + 1, 1, lambda i, _: 1 if i == 0 else 0)
        assert M_mat == C_mat - sp.Rational(1, 4) * (v_vec * v_vec.T) + sp.Rational(1, 4) * (e0_vec * e0_vec.T)

        # P C_n P^T = diag(1, 2, ..., 2)
        P_mat = sp.zeros(n + 1, n + 1)
        for k in range(n + 1):
            poly = sp.Poly(P_polys[k], t)
            for i in range(k + 1):
                P_mat[k, i] = poly.coeff_monomial(t**i)
        diag_expected = sp.diag(*([1] + [2] * n))
        assert P_mat * C_mat * P_mat.T == diag_expected
        assert C_mat.det() == 2**n

        C_inv = C_mat.inv()
        assert (v_vec.T * C_inv * v_vec)[0, 0] == 2 * n + 1
        assert (e0_vec.T * C_inv * e0_vec)[0, 0] == 2 * n + 1
        assert (v_vec.T * C_inv * e0_vec)[0, 0] == (-1) ** n

        expected = (2**n - (n * (n + 1) * (2**n)) // 4) if n >= 1 else 1
        assert M_mat.det() == expected

    print("PASS verify_lemma1_hankel: b_m, P_k(t(z))=z^k+z^{-k}, P C_n P^T, and det(M_n) verified for n=0..8")


def verify_fraction_reduction_and_gf() -> None:
    def a_formula(n: int) -> int:
        if n % 4 in (0, 3):
            return (n * (n + 1) - 4) // 4
        return (n * (n + 1) - 4) // 2

    oeis_prefix = [
        -1, -1, 1, 2, 4, 13, 19, 13, 17, 43, 53, 32, 38, 89, 103, 59, 67, 151, 169, 94,
        104, 229, 251, 137, 149, 323, 349, 188, 202, 433, 463, 247, 263, 559, 593, 314,
        332, 701, 739, 389, 409, 859, 901, 472, 494, 1033, 1079, 563, 587, 1223, 1273,
        662, 688, 1429, 1483, 769, 797, 1651, 1709, 884, 914, 1889, 1951, 1007, 1039,
        2143, 2209, 1138, 1172, 2413, 2483, 1277, 1313, 2699, 2773, 1424, 1462, 3001,
        3079, 1579,
    ]

    # 1. Reduced numerator check for n = 1..150 + OEIS %S prefix (n = 0..79)
    a_seq = [-1]
    assert a_formula(0) == -1
    for n in range(1, 151):
        num_127276 = 2**n - n * (n + 1) * (2**n) // 4 if n == 1 else 2**n - n * (n + 1) * (2 ** (n - 2))
        den_001788 = n * (n + 1) * (2**n) // 4 if n == 1 else n * (n + 1) * (2 ** (n - 2))
        frac = Fraction(-num_127276, den_001788)
        assert frac.numerator == a_formula(n)
        a_seq.append(frac.numerator)
    assert a_seq[:len(oeis_prefix)] == oeis_prefix

    # Check %C comment fractions -1/1, 1/3, 2/3, 4/5, 13/15, 19/21, 13/14, 17/18, 43/45, 53/55, 32/33, 38/39
    comment_fracs = [
        (-1, 1), (1, 3), (2, 3), (4, 5), (13, 15), (19, 21),
        (13, 14), (17, 18), (43, 45), (53, 55), (32, 33), (38, 39),
    ]
    for n, (num, den) in enumerate(comment_fracs, start=1):
        val = Fraction(n * (n + 1) - 4, n * (n + 1))
        assert (val.numerator, val.denominator) == (num, den)

    # 2. Check finite difference a(n) - 3a(n-4) + 3a(n-8) - a(n-12) == 0 for 12 <= n <= 150
    for n in range(12, 151):
        assert a_seq[n] - 3 * a_seq[n - 4] + 3 * a_seq[n - 8] - a_seq[n - 12] == 0

    # 3. Exact polynomial identities in Z[x]
    x = sp.Symbol("x")
    N_factored = (x**4 - x**3 + 3 * x**2 - x + 1) * (x**4 - x**3 - 2 * x**2 - x + 1)
    N_exp = 1 - 2 * x + 2 * x**2 - 3 * x**3 - 2 * x**4 - 3 * x**5 + 2 * x**6 - 2 * x**7 + x**8
    assert sp.expand(N_factored - N_exp) == 0

    P_expected = -1 - x + x**2 + 2 * x**3 + 7 * x**4 + 16 * x**5 + 16 * x**6 + 7 * x**7 + 2 * x**8 + x**9 - x**10 - x**11
    assert sp.expand(-(1 + x) ** 3 * N_exp - P_expected) == 0
    assert sp.expand((1 - x**4) ** 3 + (x - 1) ** 3 * (x + 1) ** 3 * (x**2 + 1) ** 3) == 0

    D_exp = -1 + 3 * x - 6 * x**2 + 10 * x**3 - 12 * x**4 + 12 * x**5 - 10 * x**6 + 6 * x**7 - 3 * x**8 + x**9
    assert sp.expand((x - 1) ** 3 * (x**2 + 1) ** 3 - D_exp) == 0

    # Verify (1 - x^4)^3 * sum a_n x^n == P(x) up to x^150
    for n in range(151):
        coeff = a_seq[n]
        if n >= 4:
            coeff -= 3 * a_seq[n - 4]
        if n >= 8:
            coeff += 3 * a_seq[n - 8]
        if n >= 12:
            coeff -= a_seq[n - 12]
        assert coeff == sp.Poly(P_expected, x).coeff_monomial(x**n)

    # 4. Verify D(x)*A(x) == N(x) identically up to x^150 (exact integer convolution) + SymPy series to x^20,
    #    and Mathar 9-term recurrence for n = 9..150
    D_coeffs = [-1, 3, -6, 10, -12, 12, -10, 6, -3, 1]
    N_coeffs = [1, -2, 2, -3, -2, -3, 2, -2, 1]
    for n in range(151):
        conv = sum(D_coeffs[j] * a_seq[n - j] for j in range(min(n, 9) + 1))
        expected_n = N_coeffs[n] if n < len(N_coeffs) else 0
        assert conv == expected_n, f"D(x)A(x) != N(x) at x^{n}: {conv} != {expected_n}"

    ser_gf = sp.Poly(sp.series(N_factored / ((x - 1) ** 3 * (x**2 + 1) ** 3), x, 0, 21).removeO(), x)
    assert [int(ser_gf.coeff_monomial(x**n)) for n in range(21)] == a_seq[:21]

    for n in range(9, 151):
        rhs = (
            3 * a_seq[n - 1]
            - 6 * a_seq[n - 2]
            + 10 * a_seq[n - 3]
            - 12 * a_seq[n - 4]
            + 12 * a_seq[n - 5]
            - 10 * a_seq[n - 6]
            + 6 * a_seq[n - 7]
            - 3 * a_seq[n - 8]
            + a_seq[n - 9]
        )
        assert a_seq[n] == rhs

    print("PASS verify_fraction_reduction_and_gf: Fraction reductions, OEIS %S (0..79), GF & 9-term recurrence (9..150)")


def main() -> None:
    verify_lemma1_hankel()
    verify_fraction_reduction_and_gf()
    print("PASS")


if __name__ == "__main__":
    main()
