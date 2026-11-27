#!/usr/bin/env python3
"""Exact-arithmetic verifier for targets/yasutomi-2609.32450-conj6.1/PROOF.md.

Performs two independent exact checks (zero floating point):
1. Symbolic/algebraic verification of every polynomial positivity lemma in PROOF.md
   using exact integer/rational polynomial expansions (sympy).
2. Exact integer-isqrt interval verification of L(x, 1) ordering across all reduced
   rationals 0 <= x < y <= 1 with den <= 12 for representative (a, b) covering all
   cases of Conjecture 5.1.
"""

import math
from fractions import Fraction
import sympy as sp


def check_nonneg_coeffs(poly_expr, gens, label):
    p = sp.Poly(sp.expand(poly_expr), *gens)
    coeffs = p.coeffs()
    neg = [c for c in coeffs if c < 0]
    if neg or not coeffs or all(c == 0 for c in coeffs):
        raise AssertionError(f"{label} failed positivity check: {len(neg)} negative coeffs")


def verify_algebraic_lemmas():
    a, b, u, v, t1, t2, e, s1, s2 = sp.symbols("a b u v t1 t2 e s1 s2")
    m1, m2, m3, m4 = sp.symbols("m1 m2 m3 m4")

    A2 = sp.Matrix([[0, 1], [1, a]]) ** 2
    B2 = sp.Matrix([[0, 1], [1, b]]) ** 2
    Sb = sp.Matrix([[0, 1], [1, b]])
    M = sp.Matrix([[m1, m2], [m3, m4]])

    T_AA = A2 * M * A2
    T_AB = A2 * M * B2
    T_SA = Sb * M * A2
    T_SB = Sb * M * B2

    q_AA, q_AB, q_SA, q_SB = T_AA[1, 1], T_AB[1, 1], T_SA[1, 1], T_SB[1, 1]
    q0_AB = T_AB[1, 0]

    # Verify convergent differences modulo det(M) = 1
    assert sp.expand((T_AA[0, 1] * q_AB - T_AB[0, 1] * q_AA) - (b - a) * (a * b - 1) * (m1 * m4 - m2 * m3)) == 0
    assert sp.expand((T_SB[0, 1] * q_SA - T_SA[0, 1] * q_SB) - (b - a) * (a * b - 1) * (m1 * m4 - m2 * m3)) == 0

    # Verify Type (1) q_AA*q_AB - q_SA*q_SB identity (mod m1*m4 - m2*m3 = 1 not even needed)
    q_diff_rhs = (
        (a**2 + 1 - b) * (a**2 + 1 + b) * ((a**2 + 1) * (b**2 + 1) * m4**2 + (a + b) * (a * b + 1) * m3 * m4 + a * b * m3**2)
        + 2 * (a**3 + a - b) * ((a**2 + 1) * (b**2 + 1) * m2 * m4 + a * b * m1 * m3)
        + (a + b) * (a * b + 1) * (a**3 + a - b) * (m2 * m3 + m1 * m4)
        + (a**2 - 1) * ((a**2 + 1) * (b**2 + 1) * m2**2 + (a + b) * (a * b + 1) * m1 * m2 + a * b * m1**2)
    )
    assert sp.expand(q_AA * q_AB - q_SA * q_SB - q_diff_rhs) == 0

    # 1. Type (2): (ab-1)(a^2+1)*q_AB^2 - 2*q_SA*q_SB > 0 for all a >= 1, b >= a+1
    P_t2 = sp.Poly(sp.expand((a * b - 1) * (a**2 + 1) * q_AB**2 - 2 * q_SA * q_SB), m1, m2, m3, m4)
    for mon in P_t2.monoms():
        check_nonneg_coeffs(P_t2.coeff_monomial(mon).subs({a: 1 + u, b: 2 + u + v}), (u, v), f"Type2 {mon}")

    # 2. Type (3), n=2 (M=I)
    t_lo = a + sp.Rational(1, 1) / (a + 1)
    diff3_I = sp.together(
        ((b - a) * (a * b - 1) / (q_AA * q_AB) - 1 / (q_AB * (q0_AB + t_lo * q_AB)) - (b - a) / (t_lo**2 * q_SA**2))
        .subs({m1: 1, m2: 0, m3: 0, m4: 1})
    )
    num3_I = sp.fraction(diff3_I)[0]
    check_nonneg_coeffs(num3_I.subs({a: 2 + u, b: 3 + u + v}), (u, v), "Type3 n=2 a>=2")
    check_nonneg_coeffs(num3_I.subs({a: 1, b: 3 + v}), (v,), "Type3 n=2 a=1,b>=3")

    # Type (3), n>=3: 1/10 half and 9/10 half
    num3_h1 = sp.fraction(sp.together((b - a) * (a * b - 1) * (q0_AB + t_lo * q_AB) - 10 * q_AA))[0]
    P3_h1 = sp.Poly(sp.expand(num3_h1), m1, m2, m3, m4)
    for mon in P3_h1.monoms():
        c = P3_h1.coeff_monomial(mon)
        check_nonneg_coeffs(c.subs({a: 1, b: 3 + v}), (v,), f"Type3 h1 a=1 {mon}")
        check_nonneg_coeffs(c.subs({a: 2 + u, b: 3 + u + v}), (u, v), f"Type3 h1 a>=2 {mon}")

    sub_M_t = {m2: 1 / (a + t1), m3: 1 / (a + t2), m1: 1 / ((a + t1) * (a + t2)) + e, m4: 1}
    expr3_h2 = sp.expand(9 * (a * b - 1) * (a * (a + 1) + 1) ** 2 * q_SA**2 - 10 * (a + 1) ** 2 * q_AA * q_AB)
    num3_h2 = sp.fraction(sp.together(expr3_h2.subs(sub_M_t)))[0]
    p3_e = sp.Poly(sp.expand(num3_h2), e)
    for deg_e in range(p3_e.degree() + 1):
        c_e = p3_e.coeff_monomial((deg_e,))
        check_nonneg_coeffs(c_e.subs({a: 1, b: 3 + v}), (t1, t2, v), f"Type3 h2 a=1 e^{deg_e}")
        check_nonneg_coeffs(c_e.subs({a: 2 + u, b: 3 + u + v}), (t1, t2, u, v), f"Type3 h2 a>=2 e^{deg_e}")

    # 3. Type (1), (I)(1): 2 <= a < b <= a^2+1
    lb_I1_I = ((b - a) * (a * b - 1) * ((a + b) * (a * b + 1) * (a - 1) * (a**2 + 1) + (a**2 - 1) * a * b) - q_AA * q_SA).subs(
        {m1: 1, m2: 0, m3: 0, m4: 1}
    )
    check_nonneg_coeffs(lb_I1_I.subs({a: 2 + u, b: 3 + u + v}), (u, v), "(I)(1) n=2")

    caseA = sp.fraction(
        sp.together(
            (a**2 - a + 1) * (a**3 + a - 1) * 2 * (a - 1) * (a**2 + 1) ** 2 * ((a**2 + 1) ** 2 + 1) / (a**2 + 1 + sp.Rational(1, 1) / a)
            - (a**2 + 2) ** 4
        )
    )[0]
    check_nonneg_coeffs(caseA.subs(a, 2 + u), (u,), "(I)(1) n>=3 Case A")

    caseB = (a**2 + a - 1) * (
        (a**2 + a + 2) * (a**2 + 1) * ((a + 1) ** 2 + 1) + 2 * (a**3 - a**2 + a) * ((a + 1) ** 2 + 1)
    ) - (a**2 + 2) ** 4
    check_nonneg_coeffs(caseB.subs(a, 2 + u), (u,), "(I)(1) n>=3 Case B")

    # 4. Type (1), (II)(1): a >= 1, b >= a^2+2
    # n=2 (M=I)
    expr_II1_I = (
        (b - a) * (a * b - 1) * (q_SA * q_SB - q_AA * q_AB) * t_lo * q_SA * q_AB
        - (q_AA * q_AB**2 * q_SB + q_AA * q_SA**2 * q_SB)
    ).subs({m1: 1, m2: 0, m3: 0, m4: 1})
    num_II1_I = sp.fraction(sp.together(expr_II1_I))[0]
    check_nonneg_coeffs(num_II1_I.subs({a: 1, b: 3 + v}), (v,), "(II)(1) n=2 a=1")
    check_nonneg_coeffs(num_II1_I.subs({a: 2 + u, b: (2 + u) ** 2 + 2 + v}), (u, v), "(II)(1) n=2 a>=2")

    # n>=3, a=1, b=3 and b>=4
    al, be, mm4 = sp.symbols("al be mm4")
    X1 = 2 + al
    Y1 = b + al
    CU1 = 2 + be
    CV1 = b * be + b**2 + 1
    al_b3 = (sp.Rational(1, 4) + s1 * sp.Rational(5, 8)) / (1 + s1)
    be_b3 = (sp.Rational(1, 4) + s2 * sp.Rational(5, 8)) / (1 + s2)
    lhs_b3 = 4 * (Y1**2 - X1**2) * CU1 * CV1
    rhs_b3 = (
        (X1 + sp.Rational(1, 4) / CU1) / Y1 * (X1 + sp.Rational(3, 4) / CV1) * (Y1 + sp.Rational(3, 4) / CV1) * CV1**2 / sp.Rational(19, 10)
        + (X1 + sp.Rational(1, 4) / CU1) * (Y1 + sp.Rational(1, 4) / CU1) * CU1**2 * (Y1 + sp.Rational(3, 4) / CV1) / X1 / sp.Rational(21, 10)
    )
    num_b3 = sp.fraction(sp.together((lhs_b3 - rhs_b3).subs({b: 3, al: al_b3, be: be_b3})))[0]
    check_nonneg_coeffs(num_b3, (s1, s2), "(II)(1) n>=3 a=1,b=3")

    al_b4 = s1 * sp.Rational(5, 8) / (1 + s1)
    be_b4 = s2 * sp.Rational(5, 8) / (1 + s2)
    lhs_b4 = (b - 1) ** 2 * (Y1**2 - X1**2) * CU1 * CV1
    rhs_b4 = (
        (X1 + sp.Rational(1, 4) / CU1) / Y1 * (X1 + b / (4 * CV1)) * (Y1 + b / (4 * CV1)) * CV1**2 / sp.Rational(8, 5)
        + (X1 + sp.Rational(1, 4) / CU1) * (Y1 + sp.Rational(1, 4) / CU1) * CU1**2 * (Y1 + b / (4 * CV1)) / X1 / sp.Rational(8, 5)
    )
    num_b4 = sp.fraction(sp.together((lhs_b4 - rhs_b4).subs({al: al_b4, be: be_b4, b: 4 + v})))[0]
    check_nonneg_coeffs(num_b4, (s1, s2, v), "(II)(1) n>=3 a=1,b>=4")

    # n>=3, a>=2, b>=a^2+2
    sub_lead_lhs = sp.Rational(1, 10) * (a**2 + 1) ** 2 * (b - a**2 - 2 + sp.Rational(1, 1) / a) * (b + a**2 + 1) * (a**2 + 1) * (b**2 + 1)
    sub_lead_rhs = a * (a**2 + 2) * (b * (a**2 + 2) + a * (b**2 + b / a + 1)) + a * b * (a**2 - 1) / (a**2 + 1) ** 2
    check_nonneg_coeffs(
        sp.fraction(sp.together(sub_lead_lhs - sub_lead_rhs))[0].subs({a: 2 + u, b: (2 + u) ** 2 + 2 + v}),
        (u, v),
        "(II)(1) n>=3 0.9-lead sublemma",
    )

    lhs_a2 = 9 * a * (b - a) * (a * b - 1) * (b - a**2 - 2 + sp.Rational(1, 1) / a) * (b + a**2 + 1) * (a**2 + 1) * (b**2 + 1)
    rhs_a2 = 11 * ((a**2 + 2) ** 2 * (b**2 + b / a + 1) ** 2 + (b + 1 / a) ** 2 * (a**2 + 2) ** 2)
    check_nonneg_coeffs(
        sp.fraction(sp.together(lhs_a2 - rhs_a2))[0].subs({a: 2 + u, b: (2 + u) ** 2 + 2 + v}),
        (u, v),
        "(II)(1) n>=3 a>=2",
    )


def cf_matrix(w):
    m00, m01, m10, m11 = 1, 0, 0, 1
    for wi in w:
        m00, m01, m10, m11 = m01, m00 + wi * m01, m11, m10 + wi * m11
    return m00, m01, m10, m11


def periodic_cf_interval(w, scale):
    """Return exact integer bounds [lo, hi] for scale * [0; w_bar] using math.isqrt."""
    m00, m01, m10, m11 = cf_matrix(w)
    A = m10
    B = m11 - m00
    C = -m01
    D = B * B - 4 * A * C
    assert D > 0 and A > 0
    # Compute integer interval for (-B + sqrt(D)) * scale / (2*A)
    s_lo = math.isqrt(D * scale * scale)
    s_hi = s_lo + 1
    assert s_lo * s_lo <= D * scale * scale < s_hi * s_hi
    lo = (-B * scale + s_lo) // (2 * A)
    hi = (-B * scale + s_hi + 2 * A - 1) // (2 * A)
    return lo, hi


def lagrange_interval(x_frac, a, b, scale):
    """Exact scaled integer interval [lo, hi] for scale * L(x, 1) (Theorem t3)."""
    if x_frac == 0:
        D = a * a + 4
        lo = math.isqrt(D * scale * scale)
        hi = lo + 1
        assert lo * lo <= D * scale * scale < hi * hi
        return lo, hi
    if x_frac == 1:
        D = b * b + 4
        lo = math.isqrt(D * scale * scale)
        hi = lo + 1
        assert lo * lo <= D * scale * scale < hi * hi
        return lo, hi
    q = x_frac.denominator
    g_fwd = [math.floor(n * x_frac) - math.floor((n - 1) * x_frac) for n in range(1, q + 1)]
    w_fwd = []
    for g in g_fwd:
        v = b if g == 1 else a
        w_fwd.extend([v, v])
    w_bwd = [b]
    for k in range(1, q):
        g = math.floor((-k) * x_frac) - math.floor((-k - 1) * x_frac)
        v = b if g == 1 else a
        w_bwd.extend([v, v])
    w_bwd.append(b)
    lo1, hi1 = periodic_cf_interval(w_fwd, scale)
    lo2, hi2 = periodic_cf_interval(w_bwd, scale)
    return b * scale + lo1 + lo2, b * scale + hi1 + hi2


def pair_type(x, y):
    if x == 0 and y == 1:
        return 2
    dx, dy = x.denominator, y.denominator
    for n in range(1, min(dx, dy)):
        if math.floor(n * x) < math.floor(n * y):
            return 1
    return 2 if dx < dy else 3


def verify_exact_rational_cases():
    scale = 10**60
    rats = sorted({Fraction(p, q) for q in range(1, 13) for p in range(0, q + 1)})
    cases = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 5), (2, 6), (3, 10), (3, 11)]
    total_pairs = 0
    for a, b in cases:
        ivs = [lagrange_interval(r, a, b, scale) for r in rats]
        for i in range(len(rats)):
            x = rats[i]
            lx_lo, lx_hi = ivs[i]
            for j in range(i + 1, len(rats)):
                y = rats[j]
                ly_lo, ly_hi = ivs[j]
                tp = pair_type(x, y)
                if b < a * a + 2:
                    if tp in (1, 3) and a == 1:
                        continue
                    want_lt = tp in (1, 2)
                else:
                    want_lt = tp == 2
                if want_lt:
                    assert lx_hi < ly_lo, f"Failed {a},{b} type={tp} x={x} y={y}"
                else:
                    assert lx_lo > ly_hi, f"Failed {a},{b} type={tp} x={x} y={y}"
                total_pairs += 1
    return total_pairs


def main():
    verify_algebraic_lemmas()
    total_pairs = verify_exact_rational_cases()
    print(f"PASS: all algebraic lemmas verified with zero negative coefficients; {total_pairs} exact surd pair comparisons certified (den <= 12).")


if __name__ == "__main__":
    main()
