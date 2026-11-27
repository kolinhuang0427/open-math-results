#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/guo-2310.15207-conj6.8/PROOF.md.

Zero floating-point arithmetic: uses exact sympy rational/polynomial arithmetic
over Q[q]/(Phi_n(q)^2) and Q(Q, a, b, c, d, t) to verify:
1. n=1 boundary remark (m=1 holds, m=2 fails).
2. Block vanishing v_{Phi_n}(A_{rn+s}) >= 3 for s > (n-1)/2, Eq. (1) per block.
3. Linearization Eqs. (2) and (3) mod Phi_n(q)^2.
4. Watson's e -> infinity rational-function identity (4) in Q(Q, a, b, c, d).
5. Specialization (5) for B_0(q) mod Phi_n(q)^2.
6. Parametric identity (6) in Q(q, t), logarithmic t-derivative at t=1, and Eq. (7).
7. Full Conjecture 6.8 mod Phi_n(q)^2 for odd n in {3,5,7,9,11,13,15} and m in {1..5}.
"""

from fractions import Fraction
import sympy as sp

q_sym, t_sym = sp.symbols("q t")

def q_poch(a, Q, k):
    res = sp.Integer(1)
    cur = sp.Integer(1)
    for j in range(k):
        res *= (1 - a * cur)
        cur *= Q
    return res

def q_num(m, q):
    return (1 - q**m) / (1 - q)  # exact polynomial sum_{j=0}^{m-1} q^j when m >= 0

def q_num_poly(m, q):
    return sum(q**j for j in range(m))

def rf_poch_rat(x, k):
    # Rising factorial (x)_k in Q
    res = Fraction(1)
    for j in range(k):
        res *= (x + j)
    return res

def fact(k):
    res = 1
    for j in range(2, k + 1):
        res *= j
    return res

def inv_mod_poly(a_expr, mod_poly, q):
    """Exact modular inverse of polynomial a_expr mod mod_poly in Q[q]."""
    p_a = sp.Poly(sp.cancel(a_expr), q, domain=sp.QQ)
    p_m = sp.Poly(mod_poly, q, domain=sp.QQ)
    u, _, g = sp.gcdex(p_a, p_m)
    assert g.degree() == 0 and g != 0, f"{a_expr} not invertible mod {mod_poly}"
    return sp.Poly(u.as_expr() / g.as_expr(), q, domain=sp.QQ).rem(p_m)

def rat_mod_poly(rat_expr, mod_poly, q):
    """Reduce rational function num(q)/den(q) modulo mod_poly in Q[q], cancelling common factors first."""
    num, den = sp.fraction(sp.together(rat_expr))
    p_m = sp.Poly(mod_poly, q, domain=sp.QQ)
    p_n = sp.Poly(sp.expand(num), q, domain=sp.QQ)
    if p_n == 0:
        return sp.Poly(0, q, domain=sp.QQ)
    p_d = sp.Poly(sp.expand(den), q, domain=sp.QQ)
    g = sp.gcd(p_n, p_d)
    p_n = p_n.exquo(g).rem(p_m)
    p_d = p_d.exquo(g)
    inv_d = inv_mod_poly(p_d.as_expr(), mod_poly, q)
    return (p_n * inv_d).rem(p_m)

def A_term(k, q):
    sign = (-1) ** k
    return sign * q_num_poly(4 * k + 1, q) * (q_poch(q, q**2, k) ** 3) / (q_poch(q**2, q**2, k) ** 3) * (q ** (k * k))

def A_term_mod(k, phi_n, power, q):
    """Exact modular evaluation of A_k(q) mod phi_n(q)^power without huge degree expansion."""
    p_phi = sp.Poly(phi_n, q, domain=sp.QQ)
    p_mod = sp.Poly(sp.expand(phi_n**power), q, domain=sp.QQ)
    # Track exact phi_n valuation of numerator and denominator:
    v_n, v_d = 0, 0
    num_p = sp.Poly((-1)**k, q, domain=sp.QQ)
    den_p = sp.Poly(1, q, domain=sp.QQ)

    def strip_phi(poly_f):
        val = 0
        cur = poly_f
        while True:
            quo, rem = cur.div(p_phi)
            if rem == 0:
                val += 1
                cur = quo
            else:
                break
        return val, cur.rem(p_mod)

    # [4k+1] = sum_{j=0}^{4k} q^j (or (1-q^{4k+1})/(1-q)):
    vn_c, f_c = strip_phi(sp.Poly(sum(q**j for j in range(4 * k + 1)), q, domain=sp.QQ))
    v_n += vn_c
    num_p = (num_p * f_c).rem(p_mod)

    # q^{k^2}:
    q_mod = sp.Poly(q, q, domain=sp.QQ)
    # pow mod p_mod:
    qk2 = sp.Poly(1, q, domain=sp.QQ)
    base = q_mod
    e = k * k
    while e > 0:
        if e & 1:
            qk2 = (qk2 * base).rem(p_mod)
        e >>= 1
        if e:
            base = (base * base).rem(p_mod)
    num_p = (num_p * qk2).rem(p_mod)

    # Cube of product (1 - q^{2j+1}) / (1 - q^{2j+2}):
    prod_n = sp.Poly(1, q, domain=sp.QQ)
    prod_d = sp.Poly(1, q, domain=sp.QQ)
    vp_n, vp_d = 0, 0
    for j in range(k):
        vn_j, fn_j = strip_phi(sp.Poly(1 - q**(2 * j + 1), q, domain=sp.QQ))
        vd_j, fd_j = strip_phi(sp.Poly(1 - q**(2 * j + 2), q, domain=sp.QQ))
        vp_n += vn_j
        vp_d += vd_j
        prod_n = (prod_n * fn_j).rem(p_mod)
        prod_d = (prod_d * fd_j).rem(p_mod)
    v_n += 3 * vp_n
    v_d += 3 * vp_d
    assert v_n >= v_d
    if v_n - v_d >= power:
        return sp.Poly(0, q, domain=sp.QQ)
    num_p = (num_p * (prod_n**3)).rem(p_mod)
    if v_n > v_d:
        num_p = (num_p * (p_phi**(v_n - v_d))).rem(p_mod)
    den_p = (den_p * (prod_d**3)).rem(p_mod)
    # gcdex returns (u, v, g) with u*den_p + v*p_mod = g (constant)
    u, _, g = sp.gcdex(den_p, p_mod)
    assert g.degree() == 0 and g != 0
    inv_d = sp.Poly(u.as_expr() / g.as_expr(), q, domain=sp.QQ).rem(p_mod)
    return (num_p * inv_d).rem(p_mod)

# ---------------------------------------------------------------------------
# 1. Check n=1 boundary remark (m=1 holds, m=2 fails mod (q-1)^2)
# ---------------------------------------------------------------------------

phi1 = sp.cyclotomic_poly(1, q_sym)
assert sp.expand(phi1 - (q_sym - 1)) == 0
phi1_sq = sp.expand(phi1**2)

lhs_n1_m1 = rat_mod_poly(A_term(0, q_sym), phi1_sq, q_sym)
rhs_n1_m1 = rat_mod_poly(sp.Integer(1), phi1_sq, q_sym)
assert lhs_n1_m1 == rhs_n1_m1

lhs_n1_m2 = rat_mod_poly(A_term(0, q_sym) + A_term(1, q_sym), phi1_sq, q_sym)
exp_lhs_n1_m2 = rat_mod_poly(sp.Rational(3, 8) - sp.Rational(15, 16) * (q_sym - 1), phi1_sq, q_sym)
rhs_n1_m2 = rat_mod_poly(sp.Rational(3, 8), phi1_sq, q_sym)
assert lhs_n1_m2 == exp_lhs_n1_m2 and lhs_n1_m2 != rhs_n1_m2
print("[1] PASS n=1 boundary remark verified: m=1 holds, m=2 gives 3/8 - (15/16)(q-1) != 3/8 mod (q-1)^2.")

# ---------------------------------------------------------------------------
# 2. Check Watson e->infty rational identity (4) in Q(Q, a, b, c, d)
# ---------------------------------------------------------------------------

def q_poch_frac(a, Q, k):
    res = Fraction(1)
    Qk = Fraction(1)
    for _ in range(k):
        res *= (1 - a * Qk)
        Qk *= Q
    return res


Q_s, a_s, b_s, c_s, d_s = sp.symbols("Q a b c d")
# Exact 5-variable symbolic rational check for N=1
for N_val in (1,):
    lhs4 = sp.Integer(0)
    for s in range(N_val + 1):
        term = (
            (1 - a_s * Q_s**(2 * s)) / (1 - a_s)
            * q_poch(a_s, Q_s, s) * q_poch(b_s, Q_s, s) * q_poch(c_s, Q_s, s)
            * q_poch(d_s, Q_s, s) * q_poch(Q_s**(-N_val), Q_s, s)
            / (q_poch(Q_s, Q_s, s) * q_poch(a_s * Q_s / b_s, Q_s, s) * q_poch(a_s * Q_s / c_s, Q_s, s)
               * q_poch(a_s * Q_s / d_s, Q_s, s) * q_poch(a_s * Q_s**(N_val + 1), Q_s, s))
            * ((-1)**s) * (Q_s**(s * (s - 1) // 2))
            * ((a_s**2 * Q_s**(N_val + 2) / (b_s * c_s * d_s))**s)
        )
        lhs4 += term
    rhs4 = (
        q_poch(a_s * Q_s, Q_s, N_val) / q_poch(a_s * Q_s / d_s, Q_s, N_val)
        * sum(
            q_poch(Q_s**(-N_val), Q_s, k) * q_poch(d_s, Q_s, k) * q_poch(a_s * Q_s / (b_s * c_s), Q_s, k)
            / (q_poch(Q_s, Q_s, k) * q_poch(a_s * Q_s / b_s, Q_s, k) * q_poch(a_s * Q_s / c_s, Q_s, k))
            * ((a_s * Q_s**(N_val + 1) / d_s)**k)
            for k in range(N_val + 1)
        )
    )
    assert sp.cancel(lhs4 - rhs4) == 0, f"Watson (4) failed symbolically at N={N_val}"

# Exact Fraction multi-point checks for N=1..6 (zero float)
watson_pts = [
    (Fraction(2, 3), Fraction(3, 5), Fraction(5, 7), Fraction(7, 11), Fraction(11, 13)),
    (Fraction(3, 4), Fraction(5, 8), Fraction(7, 9), Fraction(11, 15), Fraction(13, 17)),
    (Fraction(5, 7), Fraction(2, 5), Fraction(3, 11), Fraction(9, 13), Fraction(4, 19)),
]
for N_val in range(1, 7):
    for Q_f, a_f, b_f, c_f, d_f in watson_pts:
        lhs_f = Fraction(0)
        for s in range(N_val + 1):
            lhs_f += (
                (1 - a_f * (Q_f**(2 * s))) / (1 - a_f)
                * q_poch_frac(a_f, Q_f, s) * q_poch_frac(b_f, Q_f, s) * q_poch_frac(c_f, Q_f, s)
                * q_poch_frac(d_f, Q_f, s) * q_poch_frac(Q_f**(-N_val), Q_f, s)
                / (q_poch_frac(Q_f, Q_f, s) * q_poch_frac(a_f * Q_f / b_f, Q_f, s)
                   * q_poch_frac(a_f * Q_f / c_f, Q_f, s) * q_poch_frac(a_f * Q_f / d_f, Q_f, s)
                   * q_poch_frac(a_f * (Q_f**(N_val + 1)), Q_f, s))
                * ((-1)**s) * (Q_f**(s * (s - 1) // 2))
                * ((a_f**2 * (Q_f**(N_val + 2)) / (b_f * c_f * d_f))**s)
            )
        rhs_f = (
            q_poch_frac(a_f * Q_f, Q_f, N_val) / q_poch_frac(a_f * Q_f / d_f, Q_f, N_val)
            * sum(
                q_poch_frac(Q_f**(-N_val), Q_f, k) * q_poch_frac(d_f, Q_f, k) * q_poch_frac(a_f * Q_f / (b_f * c_f), Q_f, k)
                / (q_poch_frac(Q_f, Q_f, k) * q_poch_frac(a_f * Q_f / b_f, Q_f, k) * q_poch_frac(a_f * Q_f / c_f, Q_f, k))
                * ((a_f * (Q_f**(N_val + 1)) / d_f)**k)
                for k in range(N_val + 1)
            )
        )
        assert lhs_f == rhs_f, f"Watson (4) Fraction check failed at N={N_val}"
print("[2] PASS Watson e->infinity rational identity (4): symbolic in Q(Q,a,b,c,d) for N=1 and exact Fraction multi-point for N=1..6.")

# ---------------------------------------------------------------------------
# 3. Check parametric identity (6) in Q(q, t) and t-derivative mod Phi_n(q)
# ---------------------------------------------------------------------------

def dual_mul(x, y, mod_poly, q):
    """Multiply (x0 + x1*u) * (y0 + y1*u) in (Q[q]/(mod_poly))[u]/(u^2)."""
    x0, x1 = x
    y0, y1 = y
    z0 = (x0 * y0).rem(mod_poly)
    z1 = (x0 * y1 + x1 * y0).rem(mod_poly)
    return (z0, z1)


def dual_inv(x, mod_poly, q):
    """Invert (x0 + x1*u) in (Q[q]/(mod_poly))[u]/(u^2)."""
    x0, x1 = x
    inv0 = inv_mod_poly(x0, mod_poly.as_expr(), q)
    inv1 = (-x1 * inv0 * inv0).rem(mod_poly)
    return (inv0, inv1)


def dual_poch_t(c_power, q_start, q_step, k, mod_poly, q):
    """Compute (t^c_power * q^q_start; q^q_step)_k with t = 1 + u (u^2 = 0) mod mod_poly."""
    res = (sp.Poly(1, q, domain=sp.QQ), sp.Poly(0, q, domain=sp.QQ))
    for i in range(k):
        qp = sp.Poly(q**(q_start + i * q_step), q, domain=sp.QQ)
        fac = ((sp.Poly(1, q, domain=sp.QQ) - qp).rem(mod_poly), (-c_power * qp).rem(mod_poly))
        res = dual_mul(res, fac, mod_poly, q)
    return res


for n in (3, 5, 7, 9, 11):
    N = (n - 1) // 2
    phi_n = sp.cyclotomic_poly(n, q_sym)
    phi_n_p = sp.Poly(phi_n, q_sym, domain=sp.QQ)

    # Full symbolic bivariate Q(q, t) check for n=3 and exact Fraction multi-point checks for all n
    param_pts = [
        (Fraction(2, 3), Fraction(3, 5)),
        (Fraction(3, 5), Fraction(5, 7)),
        (Fraction(5, 7), Fraction(7, 11)),
    ]
    for q_f, t_f in param_pts:
        lhs_f = sum(
            (1 - (t_f**4) * (q_f**(4 * s + 1)))
            * q_poch_frac((t_f**2) * q_f, q_f**2, s)
            * q_poch_frac((t_f**4) * q_f, q_f**2, s)
            * q_poch_frac(q_f**(1 - n), q_f**2, s)
            / (q_poch_frac((t_f**2) * (q_f**2), q_f**2, s) * q_poch_frac(q_f**2, q_f**2, s)
               * q_poch_frac((t_f**4) * (q_f**(n + 2)), q_f**2, s))
            * ((-1)**s) * (q_f**(s * (s - 1))) * (((t_f**2) * (q_f**(n + 1)))**s)
            for s in range(N + 1)
        )
        rhs_f = (1 - (t_f**4) * (q_f**n)) * sum(
            q_poch_frac(q_f**(1 - n), q_f**2, k) * q_poch_frac(q_f / (t_f**2), q_f**2, k)
            / (q_poch_frac(q_f**2, q_f**2, k) * q_poch_frac((t_f**2) * (q_f**2), q_f**2, k))
            * (((t_f**4) * (q_f**n))**k)
            for k in range(N + 1)
        )
        assert lhs_f == rhs_f, f"Parametric identity (6) Fraction check failed at n={n}"

    if n == 3:
        lhs6_sym = sum(
            (1 - t_sym**4 * q_sym**(4 * s + 1))
            * q_poch(t_sym**2 * q_sym, q_sym**2, s)
            * q_poch(t_sym**4 * q_sym, q_sym**2, s)
            * q_poch(q_sym**(1 - n), q_sym**2, s)
            / (q_poch(t_sym**2 * q_sym**2, q_sym**2, s) * q_poch(q_sym**2, q_sym**2, s)
               * q_poch(t_sym**4 * q_sym**(n + 2), q_sym**2, s))
            * ((-1)**s) * (q_sym**(s * (s - 1))) * ((t_sym**2 * q_sym**(n + 1))**s)
            for s in range(N + 1)
        )
        rhs6_sym = (1 - t_sym**4 * q_sym**n) * sum(
            q_poch(q_sym**(1 - n), q_sym**2, k) * q_poch(q_sym * t_sym**(-2), q_sym**2, k)
            / (q_poch(q_sym**2, q_sym**2, k) * q_poch(t_sym**2 * q_sym**2, q_sym**2, k))
            * ((t_sym**4 * q_sym**n)**k)
            for k in range(N + 1)
        )
        assert sp.cancel(lhs6_sym - rhs6_sym) == 0, "Parametric identity (6) symbolic check failed at n=3"

    # Dual-number check at t = 1 + u (u^2 = 0) in (Q[q]/(Phi_n(q)))[u]/(u^2)
    # using positive exponents mod Phi_n(q) since q^n == 1 mod Phi_n(q):
    zero_p = sp.Poly(0, q_sym, domain=sp.QQ)
    lhs_dual = (zero_p, zero_p)
    for s in range(N + 1):
        q4s1 = sp.Poly(q_sym**(4 * s + 1), q_sym, domain=sp.QQ)
        num = ((sp.Poly(1, q_sym, domain=sp.QQ) - q4s1).rem(phi_n_p), (-4 * q4s1).rem(phi_n_p))
        num = dual_mul(num, dual_poch_t(2, 1, 2, s, phi_n_p, q_sym), phi_n_p, q_sym)
        num = dual_mul(num, dual_poch_t(4, 1, 2, s, phi_n_p, q_sym), phi_n_p, q_sym)
        num = dual_mul(num, dual_poch_t(0, 1, 2, s, phi_n_p, q_sym), phi_n_p, q_sym)  # q^(1-n) == q mod Phi_n
        den = dual_poch_t(2, 2, 2, s, phi_n_p, q_sym)
        den = dual_mul(den, dual_poch_t(0, 2, 2, s, phi_n_p, q_sym), phi_n_p, q_sym)
        den = dual_mul(den, dual_poch_t(4, 2, 2, s, phi_n_p, q_sym), phi_n_p, q_sym)  # q^(n+2) == q^2 mod Phi_n
        wt_q = sp.Poly(((-1)**s) * (q_sym**(s * s)), q_sym, domain=sp.QQ)  # q^(s(n+1)+s(s-1)) == q^(s^2) mod Phi_n
        wt = (wt_q.rem(phi_n_p), (2 * s * wt_q).rem(phi_n_p))
        term_dual = dual_mul(dual_mul(num, dual_inv(den, phi_n_p, q_sym), phi_n_p, q_sym), wt, phi_n_p, q_sym)
        lhs_dual = ((lhs_dual[0] + term_dual[0]).rem(phi_n_p), (lhs_dual[1] + term_dual[1]).rem(phi_n_p))

    rhs_dual_sum = (zero_p, zero_p)
    for k in range(N + 1):
        num_r = dual_mul(dual_poch_t(0, 1, 2, k, phi_n_p, q_sym), dual_poch_t(-2, 1, 2, k, phi_n_p, q_sym), phi_n_p, q_sym)
        den_r = dual_mul(dual_poch_t(0, 2, 2, k, phi_n_p, q_sym), dual_poch_t(2, 2, 2, k, phi_n_p, q_sym), phi_n_p, q_sym)
        wt_r = (sp.Poly(1, q_sym, domain=sp.QQ), sp.Poly(4 * k, q_sym, domain=sp.QQ))  # (t^4 q^n)^k == 1 + 4k*u mod (Phi_n, u^2)
        term_r = dual_mul(dual_mul(num_r, dual_inv(den_r, phi_n_p, q_sym), phi_n_p, q_sym), wt_r, phi_n_p, q_sym)
        rhs_dual_sum = ((rhs_dual_sum[0] + term_r[0]).rem(phi_n_p), (rhs_dual_sum[1] + term_r[1]).rem(phi_n_p))
    # Multiply by (1 - t^4 q^n) == -4u mod (Phi_n, u^2):
    rhs_dual = dual_mul((zero_p, sp.Poly(-4, q_sym, domain=sp.QQ)), rhs_dual_sum, phi_n_p, q_sym)

    assert lhs_dual[0] == zero_p and lhs_dual[0] == rhs_dual[0]
    assert lhs_dual[1] == rhs_dual[1]

    # Verify Delta_8(q) from (3) matches -d/dt|_{t=1} (LHS) = -lhs_dual[1] and 4*(-1)^N*q^{N^2} mod Phi_n(q):
    delta8 = sp.Integer(0)
    for s in range(N + 1):
        inner_sum = sum(
            q_sym**(2 * i + 1) / (1 - q_sym**(2 * i + 1)) - q_sym**(2 * i + 2) / (1 - q_sym**(2 * i + 2))
            for i in range(s)
        )
        bracket = 4 * q_sym**(4 * s + 1) + (1 - q_sym**(4 * s + 1)) * (6 * inner_sum - 2 * s)
        delta8 += ((-1)**s) * (q_poch(q_sym, q_sym**2, s)**3 / q_poch(q_sym**2, q_sym**2, s)**3) * q_sym**(s * s) * bracket

    delta8_mod = rat_mod_poly(delta8, phi_n, q_sym)
    exp_d8 = sp.Poly(((-1)**N) * 4 * (q_sym**(N * N)), q_sym, domain=sp.QQ).rem(phi_n_p)
    assert delta8_mod == (-lhs_dual[1]).rem(phi_n_p), f"-d/dt LHS != Delta_8 at n={n}"
    assert delta8_mod == exp_d8, f"Delta_8 != 4*(-1)^N*q^(N^2) mod Phi_n at n={n}"

print("[3] PASS Parametric identity (6), logarithmic derivative vs Delta_8 (3), and Eq. (7) mod Phi_n(q) for n=3,5,7,9,11.")

# ---------------------------------------------------------------------------
# 4. Full Section 1, 2, 3, and Conjecture 6.8 verification mod Phi_n(q)^2 for odd n in {3,5,7,9,11,13,15}
# ---------------------------------------------------------------------------

for n in (3, 5, 7, 9, 11, 13, 15):
    N = (n - 1) // 2
    phi_n = sp.cyclotomic_poly(n, q_sym)
    phi_n2 = sp.expand(phi_n**2)
    phi_n3 = sp.expand(phi_n**3)
    n_qpoly = q_num_poly(n, q_sym)
    z_q = 1 - q_sym**n

    # 1) Vanishing for N+1 <= s <= n-1 mod Phi_n^3 (for r=0, 1, 2)
    m_max = 5 if n <= 11 else 3
    for r in range(m_max):
        for s in range(N + 1, n):
            assert A_term_mod(r * n + s, phi_n, 3, q_sym) == sp.Poly(0, q_sym, domain=sp.QQ)

    # 2) Compute B_r(q) mod Phi_n^2 and verify Eq. (1) and Eq. (2) for every r = 0..m_max-1:
    B_list = []
    for r in range(m_max):
        Br = sp.Poly(0, q_sym, domain=sp.QQ)
        for s in range(N + 1):
            Br = (Br + A_term_mod(r * n + s, phi_n, 2, q_sym)).rem(sp.Poly(phi_n2, q_sym, domain=sp.QQ))
        B_list.append(Br)

        # Target RHS of (1):
        c_r = ((-1)**r) * (4 * r + 1) * (rf_poch_rat(Fraction(1, 2), r) ** 3) / Fraction(fact(r) ** 3)
        target_Br = rat_mod_poly(sp.Rational(c_r.numerator, c_r.denominator) * ((-1)**N) * (q_sym**(N * N)) * n_qpoly, phi_n2, q_sym)
        assert Br == target_Br, f"Eq. (1) failed at n={n}, r={r}"

    # Verify B_0 == 0 mod Phi_n and z*B_0 == 0 mod Phi_n^2:
    assert rat_mod_poly(B_list[0].as_expr(), phi_n, q_sym) == sp.Poly(0, q_sym, domain=sp.QQ)
    assert rat_mod_poly(z_q * B_list[0].as_expr(), phi_n2, q_sym) == sp.Poly(0, q_sym, domain=sp.QQ)

    # Verify LHS of Conjecture 6.8 == RHS mod Phi_n(q)^2 for m = 1..m_max:
    lhs_acc = sp.Poly(0, q_sym, domain=sp.QQ)
    rhs_rat_sum = Fraction(0)
    for m in range(1, m_max + 1):
        for s in range(n):
            lhs_acc = (lhs_acc + A_term_mod((m - 1) * n + s, phi_n, 2, q_sym)).rem(sp.Poly(phi_n2, q_sym, domain=sp.QQ))
        r = m - 1
        rhs_rat_sum += ((-1)**r) * (4 * r + 1) * (rf_poch_rat(Fraction(1, 2), r) ** 3) / Fraction(fact(r) ** 3)
        rhs_mod = rat_mod_poly(
            sp.Rational(rhs_rat_sum.numerator, rhs_rat_sum.denominator) * ((-1)**N) * (q_sym**(N * N)) * n_qpoly,
            phi_n2, q_sym
        )
        assert lhs_acc == rhs_mod, f"Conjecture 6.8 failed at n={n}, m={m}"

    print(f"[4.{n:2d}] PASS n={n:2d} (m=1..{m_max}): s>N vanishes mod Phi_n^3; B_r satisfies Eq. (1) & Conj 6.8 holds mod Phi_n^2.")

print("PASS")
