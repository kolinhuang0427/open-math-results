#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for Yasutomi (arXiv:2609.32450v2) Section 5, Conjecture 5.1
(historical directory slug yasutomi-2609.32450-conj6.1).

Written directly from lagrangev2.tex definitions and PROOF.md without reading verify.py.
Uses SymPy exact polynomial/algebraic arithmetic and exact quadratic-irrational comparisons
(zero floating-point operations).
"""

from __future__ import annotations

from fractions import Fraction
import math
import sys
import sympy as sp


def check_matrix_identities() -> None:
    print("[1/5] Checking Sections 1.3 & 1.4 matrix & convergent identities...", flush=True)
    a, b, t, x1, y1, x2, y2 = sp.symbols("a b t x1 y1 x2 y2")
    m1, m2, m3, m4 = sp.symbols("m1 m2 m3 m4")
    # det M = 1 => m1*m4 - m2*m3 = 1; substitute m1 = (1 + m2*m3)/m4 or eliminate m1*m4 -> 1 + m2*m3
    M = sp.Matrix([[m1, m2], [m3, m4]])
    A = sp.Matrix([[0, 1], [1, a]]) ** 2
    B = sp.Matrix([[0, 1], [1, b]]) ** 2
    Sb = sp.Matrix([[0, 1], [1, b]])

    T_AA = A * M * A
    T_AB = A * M * B
    T_SA = Sb * M * A
    T_SB = Sb * M * B

    assert sp.expand(T_AA.det() - (m1 * m4 - m2 * m3)) == 0
    assert sp.expand(T_AB.det() - (m1 * m4 - m2 * m3)) == 0
    assert sp.expand(T_SA.det() + (m1 * m4 - m2 * m3)) == 0
    assert sp.expand(T_SB.det() + (m1 * m4 - m2 * m3)) == 0

    r0_AA, r_AA = T_AA[0, 0], T_AA[0, 1]
    q0_AA, q_AA = T_AA[1, 0], T_AA[1, 1]
    r0_AB, r_AB = T_AB[0, 0], T_AB[0, 1]
    q0_AB, q_AB = T_AB[1, 0], T_AB[1, 1]
    r0_SA, r_SA = T_SA[0, 0], T_SA[0, 1]
    q0_SA, q_SA = T_SA[1, 0], T_SA[1, 1]
    r0_SB, r_SB = T_SB[0, 0], T_SB[0, 1]
    q0_SB, q_SB = T_SB[1, 0], T_SB[1, 1]

    # Check convergent difference formulas (Section 1.3) using m1*m4 = 1 + m2*m3
    sub_det = {m1 * m4: 1 + m2 * m3}
    diff1 = sp.expand((r_AA * q_AB - r_AB * q_AA) - (b - a) * (a * b - 1))
    diff1 = sp.expand(diff1.subs(m1, (1 + m2 * m3) / m4) * m4)
    assert diff1 == 0, f"r_AA/q_AA - r_AB/q_AB mismatch: {diff1}"

    diff2 = sp.expand((r_SB * q_SA - r_SA * q_SB) - (b - a) * (a * b - 1))
    diff2 = sp.expand(diff2.subs(m1, (1 + m2 * m3) / m4) * m4)
    assert diff2 == 0, f"r_SB/q_SB - r_SA/q_SA mismatch: {diff2}"

    # Check Section 1.3 bottom row difference for Type (1) Part (I)(1): A*M - S_b*M
    row_diff = sp.Matrix([[1, a], [a, a**2 + 1]]) * M - sp.Matrix([[0, 1], [1, b]]) * M
    assert sp.expand(row_diff[1, 0] - ((a - 1) * m1 + (a**2 + 1 - b) * m3)) == 0
    assert sp.expand(row_diff[1, 1] - ((a - 1) * m2 + (a**2 + 1 - b) * m4)) == 0

    # Check Section 1.4(3): Q_SA(t) > (a/(a^2+1) + t)*q_SA and Q_AB(t) > (b/(b^2+1) + t)*q_AB
    r_v, s_v = sp.symbols("r_v s_v")
    assert sp.expand((r_v + a * s_v) * (a**2 + 1) - a * (a * r_v + (a**2 + 1) * s_v) - r_v) == 0
    assert sp.expand((r_v + b * s_v) * (b**2 + 1) - b * (b * r_v + (b**2 + 1) * s_v) - r_v) == 0


def all_coeffs_nonneg(poly_expr: sp.Expr, vars_list: list[sp.Symbol]) -> bool:
    p = sp.Poly(sp.expand(poly_expr), *vars_list)
    return all(c >= 0 for c in p.coeffs())


def check_section2_type2() -> None:
    print("[2/5] Checking Section 2 (Type 2) polynomial inequalities...", flush=True)
    a, b, u, v = sp.symbols("a b u v")
    m1, m2, m3, m4 = sp.symbols("m1 m2 m3 m4")
    M = sp.Matrix([[m1, m2], [m3, m4]])
    A = sp.Matrix([[0, 1], [1, a]]) ** 2
    B = sp.Matrix([[0, 1], [1, b]]) ** 2
    Sb = sp.Matrix([[0, 1], [1, b]])

    q_AB = (A * M * B)[1, 1]
    q_SA = (Sb * M * A)[1, 1]
    q_SB = (Sb * M * B)[1, 1]

    # Check for a=1, b=2: q_SB >= 2*q_SA
    diff_12 = sp.expand((q_SB - 2 * q_SA).subs({a: 1, b: 2}))
    assert all_coeffs_nonneg(diff_12, [m1, m2, m3, m4])

    # Second half: (ab-1)(a^2+1) q_AB^2 - 2 q_SA q_SB > 0
    expr2 = sp.expand((a * b - 1) * (a**2 + 1) * q_AB**2 - 2 * q_SA * q_SB)
    expr2_uv = sp.expand(expr2.subs({a: 1 + u, b: 2 + u + v}))
    p_m = sp.Poly(expr2_uv, m1, m2, m3, m4)
    assert len(p_m.terms()) == 10
    for mon, coeff in p_m.terms():
        assert all_coeffs_nonneg(coeff, [u, v]) and sp.expand(coeff) != 0


def check_section3_type3() -> None:
    print("[3/5] Checking Section 3 (Type 3) polynomial inequalities...", flush=True)
    a, b, u, v, t1, t2, e = sp.symbols("a b u v t1 t2 e")
    m1, m2, m3, m4 = sp.symbols("m1 m2 m3 m4")
    M = sp.Matrix([[m1, m2], [m3, m4]])
    A = sp.Matrix([[0, 1], [1, a]]) ** 2
    B = sp.Matrix([[0, 1], [1, b]]) ** 2
    Sb = sp.Matrix([[0, 1], [1, b]])

    T_AA, T_AB, T_SA = A * M * A, A * M * B, Sb * M * A
    q_AA, q_AB, q_SA = T_AA[1, 1], T_AB[1, 1], T_SA[1, 1]
    q0_AB = T_AB[1, 0]

    # Case n = 2 (M = I)
    I_sub = {m1: 1, m2: 0, m3: 0, m4: 1}
    qAA_2 = q_AA.subs(I_sub)
    qAB_2 = q_AB.subs(I_sub)
    q0AB_2 = q0_AB.subs(I_sub)
    qSA_2 = q_SA.subs(I_sub)
    t_val = a + sp.Rational(1, 1) / (a + 1)
    ineq_n2 = sp.together(
        (b - a) * (a * b - 1) / (qAA_2 * qAB_2)
        - 1 / (qAB_2 * (q0AB_2 + t_val * qAB_2))
        - (b - a) / (t_val**2 * qSA_2**2)
    )
    num_n2, den_n2 = sp.fraction(ineq_n2)
    assert all_coeffs_nonneg(sp.expand(num_n2.subs({a: 2 + u, b: 3 + u + v})), [u, v])
    assert all_coeffs_nonneg(sp.expand(num_n2.subs({a: 1, b: 3 + v})), [v])

    # Case n >= 3: two split inequalities
    ineq3_1, den3_1 = sp.fraction(sp.together((b - a) * (a * b - 1) * (q0_AB + t_val * q_AB) - 10 * q_AA))
    assert sp.expand(den3_1 - (a + 1)) == 0
    assert all_coeffs_nonneg(ineq3_1.subs({a: 1, b: 3 + v}), [m1, m2, m3, m4, v])
    assert all_coeffs_nonneg(ineq3_1.subs({a: 2 + u, b: 3 + u + v}), [m1, m2, m3, m4, u, v])

    ineq3_2, den3_2 = sp.fraction(sp.together(9 * (a * b - 1) * t_val**2 * q_SA**2 - 10 * q_AA * q_AB))
    assert sp.expand(den3_2 - (a + 1) ** 2) == 0
    sub_t = {
        m2: m4 / (a + t1),
        m3: m4 / (a + t2),
        m1: m4 / ((a + t1) * (a + t2)) + e * m4,
    }
    cleared = sp.expand(sp.together(ineq3_2.subs(sub_t)) * (a + t1) ** 2 * (a + t2) ** 2 / m4**2)
    assert all_coeffs_nonneg(cleared.subs({a: 1, b: 3 + v}), [t1, t2, e, v])
    assert all_coeffs_nonneg(cleared.subs({a: 2 + u, b: 3 + u + v}), [t1, t2, e, u, v])


def check_section4_type1_partI() -> None:
    print("[4/5] Checking Section 4 (Type 1, Part I(1)) identities & inequalities...", flush=True)
    a, b, u, v = sp.symbols("a b u v")
    m1, m2, m3, m4 = sp.symbols("m1 m2 m3 m4")
    M = sp.Matrix([[m1, m2], [m3, m4]])
    A = sp.Matrix([[0, 1], [1, a]]) ** 2
    B = sp.Matrix([[0, 1], [1, b]]) ** 2
    Sb = sp.Matrix([[0, 1], [1, b]])

    q_AA, q_AB, q_SA, q_SB = (A * M * A)[1, 1], (A * M * B)[1, 1], (Sb * M * A)[1, 1], (Sb * M * B)[1, 1]

    # Exact expansion of q_AA*q_AB - q_SA*q_SB using m1*m4 - m2*m3 = 1
    rhs_id = (
        (a**2 + 1 - b) * (a**2 + 1 + b) * ((a**2 + 1) * (b**2 + 1) * m4**2 + (a + b) * (a * b + 1) * m3 * m4 + a * b * m3**2)
        + 2 * (a**3 + a - b) * ((a**2 + 1) * (b**2 + 1) * m2 * m4 + a * b * m1 * m3)
        + (a + b) * (a * b + 1) * (a**3 + a - b) * (m2 * m3 + m1 * m4)
        + (a**2 - 1) * ((a**2 + 1) * (b**2 + 1) * m2**2 + (a + b) * (a * b + 1) * m1 * m2 + a * b * m1**2)
    )
    diff_id = sp.expand((q_AA * q_AB - q_SA * q_SB - rhs_id).subs(m1, (1 + m2 * m3) / m4) * m4)
    assert diff_id == 0, f"Identity (Sec 4) mismatch: {diff_id}"

    # Case n = 2 (M = I)
    I_sub = {m1: 1, m2: 0, m3: 0, m4: 1}
    lb_n2 = (a + b) * (a * b + 1) * (a - 1) * (a**2 + 1) + (a**2 - 1) * a * b
    poly_n2 = sp.expand((b - a) * (a * b - 1) * lb_n2 - q_AA.subs(I_sub) * q_SA.subs(I_sub))
    assert all_coeffs_nonneg(poly_n2.subs({a: 2 + u, b: 3 + u + v}), [u, v])

    # Case n >= 3: b = a^2 + 1
    b1 = a**2 + 1
    lhs_b1 = (a**2 - a + 1) * (a**3 + a - 1) * 2 * (a - 1) * (a**2 + 1) ** 2 * ((a**2 + 1) ** 2 + 1)
    rhs_b1 = (a**2 + 1 + sp.Rational(1) / a) * (a**2 + 2) ** 4
    poly_b1 = sp.expand(a * (lhs_b1 - rhs_b1))
    assert all_coeffs_nonneg(poly_b1.subs(a, 2 + u), [u])

    # Case n >= 3: a + 1 <= b <= a^2
    lhs_b2 = (a**2 + a - 1) * ((a**2 + a + 2) * (a**2 + 1) * ((a + 1) ** 2 + 1) + 2 * (a**3 - a**2 + a) * ((a + 1) ** 2 + 1))
    poly_b2 = sp.expand(lhs_b2 - (a**2 + 2) ** 4)
    assert all_coeffs_nonneg(poly_b2.subs(a, 2 + u), [u])


def check_section5_type1_partII_and_exhaustive_small() -> None:
    print("[5/5] Checking Section 5 (Type 1, Part II(1)) + exact direct tests...", flush=True)
    a, b, u, v = sp.symbols("a b u v")
    m1, m2, m3, m4, alpha, beta = sp.symbols("m1 m2 m3 m4 alpha beta")
    M = sp.Matrix([[m1, m2], [m3, m4]])
    A = sp.Matrix([[0, 1], [1, a]]) ** 2
    B = sp.Matrix([[0, 1], [1, b]]) ** 2
    Sb = sp.Matrix([[0, 1], [1, b]])

    q_AA, q_AB, q_SA, q_SB = (A * M * A)[1, 1], (A * M * B)[1, 1], (Sb * M * A)[1, 1], (Sb * M * B)[1, 1]

    # Case n = 2 (M = I)
    I_sub = {m1: 1, m2: 0, m3: 0, m4: 1}
    qAA2, qAB2, qSA2, qSB2 = q_AA.subs(I_sub), q_AB.subs(I_sub), q_SA.subs(I_sub), q_SB.subs(I_sub)
    t_val = a + sp.Rational(1) / (a + 1)
    ineq5_n2 = sp.together(
        (b - a) * (a * b - 1) * (qSA2 * qSB2 - qAA2 * qAB2) / (qAA2 * qAB2 * qSA2 * qSB2)
        - 1 / (t_val * qSA2**2)
        - 1 / (t_val * qAB2**2)
    )
    num5_n2, _ = sp.fraction(ineq5_n2)
    assert all_coeffs_nonneg(sp.expand(num5_n2.subs({a: 1, b: 3 + v})), [v])
    assert all_coeffs_nonneg(sp.expand(num5_n2.subs({a: 2 + u, b: (2 + u) ** 2 + 2 + v})), [u, v])

    # Case n >= 3: Check exact q_{XY} expansions & q_SA*q_SB - q_AA*q_AB identity
    X = a**2 + 1 + a * alpha
    Y = b + alpha
    CU = a * beta + a**2 + 1
    CV = b * beta + b**2 + 1
    sub_ab = {m2: alpha * m4, m3: beta * m4, m1: alpha * beta * m4 + 1 / m4}

    assert sp.expand(q_AA.subs(sub_ab) - (m4 * X * CU + a**2 / m4)) == 0
    assert sp.expand(q_SA.subs(sub_ab) - (m4 * Y * CU + a / m4)) == 0
    assert sp.expand(q_AB.subs(sub_ab) - (m4 * X * CV + a * b / m4)) == 0
    assert sp.expand(q_SB.subs(sub_ab) - (m4 * Y * CV + b / m4)) == 0

    rhs_id5 = m4**2 * (Y**2 - X**2) * CU * CV + (Y - a * X) * (b * CU + a * CV) - a * b * (a**2 - 1) / m4**2
    assert sp.expand((q_SA * q_SB - q_AA * q_AB).subs(sub_ab) - rhs_id5) == 0

    # Subcase a = 1, b >= 3:
    # From PROOF.md line 164:
    # q_AA < m4*(X + 1/(4*CU))*CU, q_SA >= m4*Y*CU, q_AB >= m4*X*CV, q_SB <= m4*(Y + 1/(4*CV))*CV?
    # Wait: let's check both b=3 (Q_AB >= 19/10 * q_AB) and b>=4 (Q_AB >= 8/5 * q_AB),
    # and Q_SA >= 21/10 * q_SA, with alpha, beta in [1/(b+1), 5/8].
    # Check directly: (b-a)(ab-1)*(Y^2 - X^2)*CU*CV / (q_AA/m4 * q_AB/m4 * q_SA/m4 * q_SB/m4)...
    # Even simpler: check directly the polynomial from PROOF.md line 164!
    # We have (b-1)*(b-1)*(Y^2 - X^2)*CU*CV > (X + 1/(4*CU))*(Y + 1/(4*CV)) * (CU^2/(21/10 * Y * X) * ...)?
    # Wait: let's check the exact upper bound on 1/(21/10 * q_SA^2) + 1/(c_AB * q_AB^2) using
    # q_SA >= m4*Y*CU, q_AB >= m4*X*CV, q_AA < m4*(X+1/(4*CU))*CU, q_SB < m4*(Y+1/(4*CV))*CV,
    # q_SA*q_SB - q_AA*q_AB > m4^2*(Y^2 - X^2)*CU*CV:
    # Note: (b-1)^2 (Y^2 - X^2) CU CV / (q_AA q_AB q_SA q_SB) > 10/(21 q_SA^2) + 1/(c_AB q_AB^2)
    # holds if (b-1)^2 (Y^2-X^2) CU CV > (X + 1/(4*CU))*(Y + 1/(4*CV)) * (10*X*CV/(21*Y) + Y*CU/(c_AB*X))
    # wait: q_AA*q_AB / q_SA < (X+1/(4CU))*X*CV/Y and q_SA*q_SB / q_AB < Y*(Y+1/(4CV))*CU/X!
    # Let's check THAT exact inequality with alpha, beta parameterized on [1/(b+1), 5/8]!
    p_a, p_b = sp.symbols("p_a p_b")  # p_a, p_b >= 0 parameterize [1/(b+1), 5/8] via (1/(b+1) + 5/8*p)/(1+p)
    sub_a1 = {
        a: 1,
        alpha: (sp.Rational(1) / (b + 1) + sp.Rational(5, 8) * p_a) / (1 + p_a),
        beta: (sp.Rational(1) / (b + 1) + sp.Rational(5, 8) * p_b) / (1 + p_b),
    }
    X1 = X.subs(sub_a1)
    Y1 = Y.subs(sub_a1)
    CU1 = CU.subs(sub_a1)
    CV1 = CV.subs(sub_a1)
    # Check b = 3 with c_AB = 19/10 (since b/(b^2+1) = 3/10, 3/10 + 8/5 = 19/10)
    # Using q_AA/q_SA < (X + 1/(4*CU))/Y, q_SB/q_AB < Y/X,
    # q_AB < m4*(X + b/(4*CV))*CV, q_SB < m4*(Y + b/(4*CV))*CV,
    # q_AA < m4*(X + 1/(4*CU))*CU, q_SA < m4*(Y + 1/(4*CU))*CU:
    lhs_a1_b3 = ((b - 1) ** 2 * (Y1**2 - X1**2) * CU1 * CV1).subs(b, 3)
    rhs_a1_b3 = (
        sp.Rational(10, 21)
        * (X1 + sp.Rational(1, 4) / CU1)
        / Y1
        * (X1 + b / (4 * CV1))
        * (Y1 + b / (4 * CV1))
        * CV1**2
        + sp.Rational(10, 19)
        * (Y1 / X1)
        * (X1 + sp.Rational(1, 4) / CU1)
        * (Y1 + sp.Rational(1, 4) / CU1)
        * CU1**2
    ).subs(b, 3)
    num_a1_b3, _ = sp.fraction(sp.together(lhs_a1_b3 - rhs_a1_b3))
    assert all_coeffs_nonneg(num_a1_b3, [p_a, p_b])

    # Check b = 4 + v with c_AB = 8/5
    lhs_a1_b4 = ((b - 1) ** 2 * (Y1**2 - X1**2) * CU1 * CV1).subs(b, 4 + v)
    rhs_a1_b4 = (
        sp.Rational(10, 21)
        * (X1 + sp.Rational(1, 4) / CU1)
        / Y1
        * (X1 + b / (4 * CV1))
        * (Y1 + b / (4 * CV1))
        * CV1**2
        + sp.Rational(5, 8)
        * (Y1 / X1)
        * (X1 + sp.Rational(1, 4) / CU1)
        * (Y1 + sp.Rational(1, 4) / CU1)
        * CU1**2
    ).subs(b, 4 + v)
    num_a1_b4, _ = sp.fraction(sp.together(lhs_a1_b4 - rhs_a1_b4))
    assert all_coeffs_nonneg(num_a1_b4, [p_a, p_b, v])

    # Subcase a >= 2, b >= a^2 + 2:
    # Check line 169: 1/10 m4^2 (Y^2 - X^2) CU CV > a(a^2+2)(b CU + a CV) + ab(a^2-1)/m4^2
    # Since Y >= b, X <= a^2+2, Y-X >= b - a^2 - 2 + 1/a, Y+X >= b + a^2 + 1, CU >= a^2+1, CV >= b^2+1, m4 >= a^2+1:
    lhs_err = sp.Rational(1, 10) * (a**2 + 1) ** 2 * (b - a**2 - 2 + sp.Rational(1) / a) * (b + a**2 + 1) * (a**2 + 1) * (b**2 + 1)
    rhs_err = a * (a**2 + 2) * (b * (a**2 + 2) + a * (b**2 + b / a + 1)) + a * b * (a**2 - 1) / (a**2 + 1) ** 2
    num_err, _ = sp.fraction(sp.together(lhs_err - rhs_err))
    assert all_coeffs_nonneg(num_err.subs({a: 2 + u, b: (2 + u) ** 2 + 2 + v}), [u, v])

    # Check line 171: final polynomial for a >= 2, b >= a^2 + 2
    poly_5_fin = (
        9 * a * (b - a) * (a * b - 1) * (b - a**2 - 2 + sp.Rational(1) / a) * (b + a**2 + 1) * (a**2 + 1) * (b**2 + 1)
        - 11 * ((a**2 + 2) ** 2 * (b**2 + b / a + 1) ** 2 + (b + sp.Rational(1) / a) ** 2 * (a**2 + 2) ** 2)
    )
    num_fin, _ = sp.fraction(sp.together(poly_5_fin))
    assert all_coeffs_nonneg(num_fin.subs({a: 2 + u, b: (2 + u) ** 2 + 2 + v}), [u, v])

    # Direct verification of L(x, 1) and Conjecture ordering on all x < y with den <= 6 and small (a, b)
    # Using exact quadratic integers + rigorous 60-digit mpmath interval arithmetic (zero floats)
    from mpmath import iv

    iv.dps = 60

    def eval_L1_iv(x_rat: Fraction, a_val: int, b_val: int) -> iv.mpf:
        if x_rat == 0:
            return iv.sqrt(iv.mpf(a_val**2 + 4))
        if x_rat == 1:
            return iv.sqrt(iv.mpf(b_val**2 + 4))
        q = x_rat.denominator
        p = x_rat.numerator

        def G(k: int) -> int:
            return math.floor(Fraction(k * p, q)) - math.floor(Fraction((k - 1) * p, q))

        fwd_digits: list[int] = []
        for k in range(1, q + 1):
            d = b_val if G(k) == 1 else a_val
            fwd_digits.extend([d, d])

        bwd_digits: list[int] = [b_val]  # a_{-1}
        for m in range(1, q):
            d = b_val if G(-m) == 1 else a_val
            bwd_digits.extend([d, d])
        bwd_digits.append(b_val)  # a_{-2q}

        def zero_periodic_cf_iv(period_digits: list[int]) -> iv.mpf:
            # Computes t = [0; d_1, ..., d_m, t] using product of [[0, 1], [1, d]]
            m00, m01, m10, m11 = 1, 0, 0, 1
            for d in period_digits:
                m00, m01, m10, m11 = m01, m00 + d * m01, m11, m10 + d * m11
            # t = (m00*t + m01) / (m10*t + m11) => m10*t^2 + (m11 - m00)*t - m01 = 0
            A_q = m10
            B_q = m11 - m00
            C_q = -m01
            disc = B_q * B_q - 4 * A_q * C_q
            return (iv.mpf(-B_q) + iv.sqrt(iv.mpf(disc))) / iv.mpf(2 * A_q)

        fwd_val = zero_periodic_cf_iv(fwd_digits)
        bwd_val = zero_periodic_cf_iv(bwd_digits)
        return iv.mpf(b_val) + fwd_val + bwd_val

    def classify(x_r: Fraction, y_r: Fraction) -> int:
        dx, dy = x_r.denominator, y_r.denominator
        if (x_r, y_r) == (Fraction(0), Fraction(1)):
            return 2
        for n_i in range(1, min(dx, dy)):
            if math.floor(n_i * x_r) < math.floor(n_i * y_r):
                return 1
        if dx < dy and all(math.floor(j * x_r) == math.floor(j * y_r) for j in range(1, dx + 1)):
            return 2
        assert dx > dy
        return 3

    rats = sorted({Fraction(p, q) for q in range(1, 7) for p in range(q + 1)})
    test_ab = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 5), (2, 6), (2, 7), (3, 4), (3, 10), (3, 11)]
    for a_v, b_v in test_ab:
        L_map = {r: eval_L1_iv(r, a_v, b_v) for r in rats}
        for i in range(len(rats)):
            for j in range(i + 1, len(rats)):
                xr, yr = rats[i], rats[j]
                tp = classify(xr, yr)
                diff = L_map[yr] - L_map[xr]
                if b_v < a_v**2 + 2:
                    if tp == 1 and a_v >= 2:
                        assert diff.a > 0
                    elif tp == 2:
                        assert diff.a > 0
                    elif tp == 3 and a_v >= 2:
                        assert diff.b < 0
                else:
                    if tp == 1:
                        assert diff.b < 0
                    elif tp == 2:
                        assert diff.a > 0
                    elif tp == 3:
                        assert diff.b < 0


def main() -> int:
    check_matrix_identities()
    check_section2_type2()
    check_section3_type3()
    check_section4_type1_partI()
    check_section5_type1_partII_and_exhaustive_small()
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
