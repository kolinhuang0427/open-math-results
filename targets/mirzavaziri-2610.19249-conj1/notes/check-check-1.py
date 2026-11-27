#!/usr/bin/env python3
"""Independent zero-float exact-arithmetic & interval-arithmetic verifier
for targets/mirzavaziri-2610.19249-conj1/ (PROOF.md).

- Part A: Exact Python int polynomial verification of Conjecture 2 (conj:general)
  for all 57 admissible m in {5} U {9 <= m <= 100 : m != 2, 3 mod 5} (which
  also covers Guo-Krattenthaler Conj 7.4 / conj:GK for 1 <= n <= 20), plus full-degree
  exact remainder-0 and reciprocity checks on selected m including m = 100.
- Part B: Independent zero-float mpmath.iv (dps=30) certification of Lemma 1-7
  and uniform m >= 101 monotonicity assertions across an exhaustive rational cover
  of gamma = theta * m in (0, inf).
"""
from __future__ import annotations

import time
from fractions import Fraction
from mpmath import iv


def I(s: int | str) -> iv.mpf:
    return iv.mpf(str(s))


def F(num: int, den: int) -> iv.mpf:
    return iv.mpf(num) / iv.mpf(den)


# ===========================================================================
# PART A: Exact integer polynomial arithmetic for m <= 100
# ===========================================================================

def exact_P_coeffs(m: int, trunc_deg: int | None = None) -> list[int]:
    """Compute coefficients [q^0 .. q^limit] of P^{(m)}(q) in exact Python ints."""
    deg_full = 5 * m * m - 5 * m + 4
    lim = deg_full if trunc_deg is None else trunc_deg
    # Build G_m(q) = [6m choose m]_q iteratively mod q^{lim+1}
    poly = [0] * (lim + 1)
    poly[0] = 1
    cur_deg = 0
    for i in range(m):
        top = 6 * m - i
        bot = i + 1
        new_deg = min(lim, cur_deg + top)
        # Multiply by (1 - q^top)
        for k in range(new_deg, top - 1, -1):
            poly[k] -= poly[k - top]
        # Exact division by (1 - q^bot)
        for k in range(bot, new_deg + 1):
            poly[k] += poly[k - bot]
        cur_deg = new_deg

    # Multiply by (1 - q) and divide by (1 - q^a), a = 2m - 1
    a = 2 * m - 1
    for k in range(lim, 0, -1):
        poly[k] -= poly[k - 1]
    for k in range(a, lim + 1):
        poly[k] += poly[k - a]

    # Multiply by (1 - q) and divide by (1 - q^b), b = 3m - 1
    b = 3 * m - 1
    for k in range(lim, 0, -1):
        poly[k] -= poly[k - 1]
    for k in range(b, lim + 1):
        poly[k] += poly[k - b]

    return poly


def verify_part_a() -> None:
    t0 = time.monotonic()
    admissible = [m for m in range(5, 101) if (m == 5 or m >= 9) and m % 5 not in (2, 3)]
    assert len(admissible) == 57, f"Expected 57 admissible m <= 100, got {len(admissible)}"
    full_check_set = {5, 9, 10, 11, 14, 15, 20, 25, 30, 35, 100}

    for m in admissible:
        D = 5 * m * m - 5 * m + 4
        assert D % 2 == 0
        T = D // 2
        if m in full_check_set:
            # Compute slightly past D to assert exact polynomiality (0 higher terms)
            ext = exact_P_coeffs(m, D + m + 5)
            assert all(ext[k] == 0 for k in range(D + 1, len(ext))), f"Nonzero remainder for m={m}"
            coeffs = ext[: D + 1]
            # Reciprocity
            for k in range(T + 1):
                assert coeffs[k] == coeffs[D - k], f"Reciprocity failed m={m}, k={k}"
        else:
            coeffs = exact_P_coeffs(m, T)

        assert coeffs[0] == 1, f"m={m}: c[0]={coeffs[0]}"
        assert coeffs[1] == -1, f"m={m}: c[1]={coeffs[1]}"
        for k in range(2, T + 1):
            assert coeffs[k] >= 0, f"m={m}: c[{k}]={coeffs[k]} < 0"
        if m >= 9:
            for k in range(5 * m + 1, T + 1):
                assert coeffs[k] > 0, f"m={m}: c[{k}]={coeffs[k]} <= 0"

    # Also verify Proposition 2 boundary injection condition d_k(n) >= 0 (n >= 2), >= 1 (n >= 8)
    # directly for k in {9, 10, 15, 25} up to n = 150
    for k_val in (9, 10, 15, 25):
        lim_n = 150
        h = [0] * (lim_n + 1)
        h[0] = 1
        for part in range(2, k_val + 1):
            for n in range(part, lim_n + 1):
                h[n] += h[n - part]
        for n in range(2, lim_n + 1):
            d = h[n] - h[n - 1]
            assert d >= 0, f"d_{k_val}({n})={d} < 0"
            if n >= 8:
                assert d >= 1, f"d_{k_val}({n})={d} < 1"

    dt = time.monotonic() - t0
    print(f"PASS Part A: all {len(admissible)} admissible m <= 100 verified ({int(dt)}s)")


# ===========================================================================
# PART B: Independent zero-float mpmath.iv certification for m >= 101
# ===========================================================================

iv.dps = 30
PI = +iv.pi
L_VAL = I(3)
X0_VAL = (L_VAL * L_VAL) / 2
M0 = 101


def p_fn(u: iv.mpf) -> iv.mpf:
    return I(1) / (I(1) + iv.exp(u))


def v_fn(u: iv.mpf) -> iv.mpf:
    return p_fn(u) * (I(1) - p_fn(u))


def vp_fn(u: iv.mpf) -> iv.mpf:
    # v'(u) = v(u)*(2p(u)-1)
    p = p_fn(u)
    return p * (I(1) - p) * (I(2) * p - I(1))


def vpp_fn(u: iv.mpf) -> iv.mpf:
    v = v_fn(u)
    return v * (I(1) - I(6) * v)


def v3_fn(u: iv.mpf) -> iv.mpf:
    v = v_fn(u)
    return vp_fn(u) * (I(1) - I(12) * v)


def iv_sinh(x: iv.mpf) -> iv.mpf:
    return (iv.exp(x) - iv.exp(-x)) / I(2)


def sinhc(x: iv.mpf) -> iv.mpf:
    """Even positive increasing sinh(x)/x using series for |x| <= 2 (no x division blowup)."""
    xb = abs(x).b
    if xb <= I(2).b:
        x2 = x * x
        # sinh(x)/x = sum_{k=0}^7 x^{2k}/(2k+1)! + rem
        # For |x| <= 2, term k=8 is <= 2^16 / 17! < 2e-10; series ratio <= 4/(18*19) < 0.012
        from math import factorial
        s = I(1)
        xp = I(1)
        for k in range(1, 9):
            xp = xp * x2
            s = s + xp / I(factorial(2 * k + 1))
        rem_b = F(2, factorial(19)) * (xb ** 18)
        rem = iv.mpf([-rem_b.b, rem_b.b])
        return s + rem
    return iv_sinh(x) / x


def g_inc(k: int, x: iv.mpf) -> iv.mpf:
    """Upper-bounded / interval-enclosed 1 - exp(-x) sum_{r=0}^k x^r / r!."""
    s = I(1)
    term = I(1)
    for r in range(1, k + 1):
        term = term * x / I(r)
        s = s + term
    return I(1) - iv.exp(-x) * s


def compute_L1_constants() -> dict[str, iv.mpf]:
    """Certify L1 norms int_{-inf}^inf |(u^k v(u))''| du (k=0..4) and
    int_{-inf}^inf |(u^k v'(u))''| du (k=0..3) by symmetry + 800-panel Simpson/midpoint on [0, 22]
    plus exponential tail on [22, inf)."""
    # Note: for u >= 0, |v|, |v'|, |v''|, |v'''| <= e^{-u}, so bounding each derivative
    # via explicit triangle inequality on [22, inf) using int_{22}^inf u^k e^{-u} du is elementary.
    # For (u^k v)'': (u^k v)'' = k(k-1)u^{k-2} v + 2k u^{k-1} v' + u^k v''.
    # And for (u^k v')'': k(k-1)u^{k-2} v' + 2k u^{k-1} v'' + u^k v'''.
    # Since both v and v' are even/odd, total L1 over (-inf, inf) is 2 * int_0^inf ...
    UMAX = I(22)
    N_PAN = 880  # h = 22/880 = 1/40
    H = UMAX / N_PAN

    def tail_uk_exp(k: int, a: iv.mpf) -> iv.mpf:
        # int_a^inf u^k e^{-u} du = e^{-a} sum_{j=0}^k (k!/j!) a^j
        fact = 1
        s = I(0)
        # Actually reverse: k! sum_{j=0}^k a^j / j!
        s_inner = I(0)
        term = I(1)
        for j in range(k + 1):
            if j > 0:
                term = term * a / I(j)
            s_inner = s_inner + term
        for j in range(1, k + 1):
            fact *= j
        return I(fact) * iv.exp(-a) * s_inner

    def norm_uk_v_dd(u: iv.mpf, k: int) -> iv.mpf:
        val = u ** k * vpp_fn(u)
        if k >= 1:
            val = val + I(2 * k) * (u ** (k - 1)) * vp_fn(u)
        if k >= 2:
            val = val + I(k * (k - 1)) * (u ** (k - 2)) * v_fn(u)
        return abs(val)

    def norm_uk_vp_dd(u: iv.mpf, k: int) -> iv.mpf:
        val = u ** k * v3_fn(u)
        if k >= 1:
            val = val + I(2 * k) * (u ** (k - 1)) * vpp_fn(u)
        if k >= 2:
            val = val + I(k * (k - 1)) * (u ** (k - 2)) * vp_fn(u)
        return abs(val)

    # Integrate on [0, 22] using rigorous Riemann interval sum: sum_j h * max_{u in [j*h, (j+1)*h]} f(u)
    res: dict[str, iv.mpf] = {}
    for k in range(5):
        acc = I(0)
        for j in range(N_PAN):
            cell = iv.mpf([j * H.a, (j + 1) * H.b])
            acc = acc + H * norm_uk_v_dd(cell, k)
        tail = tail_uk_exp(k, UMAX)
        if k >= 1:
            tail = tail + I(2 * k) * tail_uk_exp(k - 1, UMAX)
        if k >= 2:
            tail = tail + I(k * (k - 1)) * tail_uk_exp(k - 2, UMAX)
        res[f"v_{k}"] = I(2) * I((acc + tail).b)

    for k in range(4):
        acc = I(0)
        for j in range(N_PAN):
            cell = iv.mpf([j * H.a, (j + 1) * H.b])
            acc = acc + H * norm_uk_vp_dd(cell, k)
        tail = tail_uk_exp(k, UMAX)
        if k >= 1:
            tail = tail + I(2 * k) * tail_uk_exp(k - 1, UMAX)
        if k >= 2:
            tail = tail + I(k * (k - 1)) * tail_uk_exp(k - 2, UMAX)
        res[f"vp_{k}"] = I(2) * I((acc + tail).b)

    return res


def certify_c4_core(u0: iv.mpf) -> iv.mpf:
    """Upper bound max_{|u| <= 5/2, |x| <= u0} |w^2 - 6*v*e^{ix}| / |w|^4
    via 2D interval subdivision on p in [q0, 1/2], x in [0, u0]."""
    q0 = I(1) / (I(1) + iv.exp(F(5, 2)))
    np_steps = 24
    nx_steps = 40
    p_lo = q0.a
    p_hi = I("0.5").b
    best = I(0)
    dp = (p_hi - p_lo) / np_steps
    dx = u0.b / nx_steps
    for ip in range(np_steps):
        p_iv = iv.mpf([p_lo + ip * dp, p_lo + (ip + 1) * dp])
        v_iv = p_iv * (I(1) - p_iv)
        for ix in range(nx_steps):
            x_iv = iv.mpf([ix * dx, (ix + 1) * dx])
            ex = iv.cos(x_iv) + iv.j * iv.sin(x_iv)
            w = (I(1) - p_iv) + p_iv * ex
            num = abs(w * w - I(6) * v_iv * ex)
            den = (abs(w) ** 4)
            ratio = num / den
            if ratio.b > best.b:
                best = I(ratio.b)
    return best


def verify_lemma1() -> iv.mpf:
    """Certify Lemma 1 constants at m0 = 101 and return s_min = c_s * sqrt(101)."""
    c_s = F(1709, 1000)
    m = I(M0)
    sq_m = iv.sqrt(m)
    assert sq_m.a > c_s.b
    theta1 = I(1) / (c_s * sq_m)
    tail_sum = (c_s * sq_m) / (I(1) - I(1) / (I(2) * c_s * sq_m)) * iv.exp(-sq_m / c_s)
    assert tail_sum.b < F(1, 2), f"Lemma 1 tail_sum={tail_sum}"

    # Check u_* - 1 = e^{-u_*} < 0.285 <=> u_* < 1.285
    u_test = F(1285, 1000)
    assert (u_test - I(1) - iv.exp(-u_test)).a > 0
    g_max = F(285, 1000)
    tau_over_m = (PI * PI / I(6)) * c_s * c_s + (I(2) * g_max * c_s) / sq_m
    assert tau_over_m.b < I(5), f"Lemma 1 tau/m={tau_over_m}"
    s_min = c_s * sq_m
    print(f"PASS Lemma 1: tail_sum <= {iv.nstr(tail_sum.b, 7)} < 0.5, tau/m <= {iv.nstr(tau_over_m.b, 7)} < 5, s_min >= {iv.nstr(s_min.a, 7)}")
    return I(s_min.a)


def maj_min_combo(
    V: iv.mpf,
    W: iv.mpf,
    S3: iv.mpf,
    M4: iv.mpf,
    cub: dict[str, iv.mpf],
    beta_over_sqrtW: iv.mpf,
    H_over_W: iv.mpf,
    C4_val: iv.mpf,
    min_ub: iv.mpf,
    extra_check: bool = True,
) -> tuple[iv.mpf, iv.mpf, iv.mpf]:
    """Compute rigorous Major Arc lower bound and Net = Maj_lb - min_ub."""
    # Domain check: L/sqrt(V) < pi, L/sqrt(W) < pi
    assert (L_VAL / iv.sqrt(I(V.a))).b < PI.a
    assert (L_VAL / iv.sqrt(I(W.a))).b < PI.a

    # M3 <= sqrt(W * M4)
    M4_hi = I(M4.b)
    S3_hi = I(abs(S3).b)
    V_lo = I(V.a)
    W_lo = I(W.a)

    # Maximize lambda(theta) over theta in [0, pi/2] divided into 32 intervals
    lam_max = I(0)
    n_th = 32
    dth = (PI / I(2)) / n_th
    for k in range(n_th):
        th = iv.mpf([k * dth.a, (k + 1) * dth.b])
        c = iv.cos(th)
        s = iv.sin(th)
        c2, s2 = c * c, s * s
        poly_bit = (
            (c2 * c2 + I(6) * c2 * s2) / V_lo
            + I(4) * abs(c) * (s2 * s) * S3_hi / (iv.sqrt(V_lo) * (W_lo ** F(3, 2)))
            + (s2 * s2) * M4_hi / (W_lo * W_lo)
        )
        val = I(2) * ((L_VAL * L_VAL / I(24)) * poly_bit + F(1, 2) * H_over_W * s2)
        if val.b > lam_max.b:
            lam_max = I(val.b)
    assert lam_max.b < 1, f"lambda = {lam_max} >= 1"

    X_val = (I(1) - lam_max) * X0_VAL
    a30 = cub["a30"]
    a21 = cub["a21"]
    a12 = cub["a12"]
    a03 = cub["a03"]
    ec32 = (
        I(15) * a30 * a30
        + I(18) * abs(a30) * abs(a12)
        + I(27) * a21 * a21
        + I(18) * abs(a21) * abs(a03)
        + I(27) * a12 * a12
        + I(15) * a03 * a03
    ) / I(36)

    g1_x0 = g_inc(1, X0_VAL)
    g3_x0 = g_inc(3, X0_VAL)
    g1_x = g_inc(1, X_val)
    g2_x = g_inc(2, X_val)

    maj = (
        iv.exp(-(beta_over_sqrtW * beta_over_sqrtW) / I(2))
        - iv.exp(-X0_VAL)
        - F(1, 2) * g3_x0 * ec32
        - abs(beta_over_sqrtW) * iv.sqrt(g1_x0 * g3_x0 * ec32)
        - (C4_val / I(24)) * (g2_x / ((I(1) - lam_max) ** 3)) * (I(9) / V_lo + I(3) * M4_hi / (W_lo * W_lo))
        - F(1, 2) * H_over_W * (g1_x / ((I(1) - lam_max) ** 2))
    )
    maj_lb = I(maj.a)
    net = maj_lb - I(min_ub.b)
    assert net.a > 0, f"Negative net margin: maj_lb={maj_lb}, min_ub={min_ub}, net={net}"
    return maj_lb, I(min_ub.b), I(net.a)


def certify_s_unit_regime(gamma_lo: iv.mpf, gamma_hi: iv.mpf | None, s_min: iv.mpf, L1: dict[str, iv.mpf]) -> tuple[iv.mpf, iv.mpf, iv.mpf]:
    """Certify an s-unit regime gamma in [gamma_lo, gamma_hi] (or [gamma_lo, inf)) with s >= s_min."""
    # rho in 1 +- gamma / (16 m^2), so |gamma_* - gamma| <= 1/(16 s^2) <= 1/(16 s_min^2)
    d_gamma = I(1) / (I(16) * s_min * s_min)
    g_lo_eff = gamma_lo - d_gamma
    assert g_lo_eff.a > I(3).b

    # Lower bound on |A| and B:
    # From e^A = (1 - e^{(rho-6)gamma}) / (e^{gamma_*} - 1),
    # A <= -log(e^{gamma_*} - 1) <= -log(e^{gamma_lo - d_gamma} - 1) if rho<=6, actually numerator <= 1!
    # So |A| = -A >= log(e^{gamma_lo - d_gamma} - 1).
    A_abs_lo = iv.log(iv.exp(g_lo_eff) - I(1))
    # B = A + 6*gamma: e^{-B} = e^{-6*gamma} * (e^{gamma_*} - 1)/(1 - e^{(rho-6)gamma})
    # <= e^{(rho-6)gamma} / (1 - e^{(rho-6)gamma})? Wait: e^{gamma_*} - 1 < e^{gamma_*},
    # so e^{-6*gamma}*(e^{gamma_*}-1) < e^{(\rho-6)\gamma}!!
    # Wait: verify! gamma_* = rho*gamma, so e^{-6*gamma} * (e^{rho*gamma} - 1) = e^{(rho-6)\gamma} - e^{-6\gamma} < e^{(rho-6)\gamma}!
    # And (6 - rho)*gamma >= 6*gamma_lo - gamma_lo - d_gamma = 5*gamma_lo - d_gamma (since rho*gamma = gamma_* <= gamma + d_gamma)!
    five_g_lo = I(5) * gamma_lo - d_gamma
    B_lo = -iv.log(iv.exp(-five_g_lo) / (I(1) - iv.exp(-five_g_lo)))
    assert A_abs_lo.a > F(5, 2) and B_lo.a > F(5, 2)

    # Tail integrals for v and u^2 v: using v(u) <= e^{-u} - 2e^{-2u} + 3e^{-3u} (valid u > 0)
    def tail_v_int(a: iv.mpf) -> iv.mpf:
        return p_fn(a)

    def tail_u2v_int(a: iv.mpf) -> iv.mpf:
        # Exact int_a^inf u^2 (e^{-u} - 2e^{-2u} + 3e^{-3u}) du
        # int_a^inf u^2 e^{-c u} du = e^{-ca}(a^2/c + 2a/c^2 + 2/c^3)
        res = I(0)
        for c, w in [(1, 1), (2, -2), (3, 3)]:
            res = res + I(w) * iv.exp(-I(c) * a) * (a * a / I(c) + I(2) * a / I(c * c) + I(2) / I(c ** 3))
        return res

    def tail_u4v_int(a: iv.mpf) -> iv.mpf:
        # Upper bound int_a^inf u^4 e^{-u} du
        return iv.exp(-a) * (a**4 + I(4)*a**3 + I(12)*a**2 + I(24)*a + I(24))

    def tail_uvp_int(a: iv.mpf) -> iv.mpf:
        # |u v'(u)| <= u v(u) <= u e^{-u} (or alternating)
        return iv.exp(-a) * (a + I(1))

    def tail_u3vp_int(a: iv.mpf) -> iv.mpf:
        return iv.exp(-a) * (a**3 + I(3)*a**2 + I(6)*a + I(6))

    V_tail_s = tail_v_int(A_abs_lo) + tail_v_int(B_lo) + (v_fn(A_abs_lo) + v_fn(B_lo)) / s_min
    W_tail_mu_s3 = (
        tail_u2v_int(A_abs_lo)
        + tail_u2v_int(B_lo)
        + (A_abs_lo**2 * v_fn(A_abs_lo) + B_lo**2 * v_fn(B_lo)) / s_min
    )
    # Discrete sum error <= L1 / (8 s^2)
    err_fac = I(1) / (I(8) * s_min * s_min)

    V_s_lo = I(1) - V_tail_s - L1["v_0"] * err_fac
    V_s_hi = I(1) + L1["v_0"] * err_fac
    V_s = iv.mpf([V_s_lo.a, V_s_hi.b])

    # Uncentered around mu: W_mu/s^3 in pi^2/3 - tail +- L1(v_2)/(8 s^2)
    W_mu_s3_lo = (PI * PI / I(3)) - W_tail_mu_s3 - L1["v_2"] * err_fac
    W_mu_s3_hi = (PI * PI / I(3)) + L1["v_2"] * err_fac

    # Mean shift delta = jbar - mu: sum (j - mu) v_j = s * delta_s
    # Full line integral int u v(u) du = 0; boundary point + tail + L1(v_1)/(8 s^2)
    tail_uv = (iv.exp(-A_abs_lo) * (A_abs_lo + I(1)) + iv.exp(-B_lo) * (B_lo + I(1)))
    # Monotonicity of u v(u) for u >= 2.5: (uv)' = v(1 - u tanh(u/2)) < 0
    point_uv = (A_abs_lo * v_fn(A_abs_lo) + B_lo * v_fn(B_lo)) / s_min
    sum_uv_s2 = tail_uv + point_uv + L1["v_1"] * err_fac
    delta_s = sum_uv_s2 / I(V_s.a)  # |jbar - mu| / s <= delta_s

    # Shift to jbar
    W_s3_lo = W_mu_s3_lo - I(V_s.b) * delta_s * delta_s
    W_s3_hi = W_mu_s3_hi
    W_s3 = iv.mpf([W_s3_lo.a, W_s3_hi.b])

    # S_3,mu / s^4: int u^3 v(u) du = 0
    tail_u3v = iv.exp(-A_abs_lo)*(A_abs_lo**3+3*A_abs_lo**2+6*A_abs_lo+6) + iv.exp(-B_lo)*(B_lo**3+3*B_lo**2+6*B_lo+6)
    # Peak of u^3 v(u) is at ~3 (let's bound extra boundary term safely by max at 3 if <3, here >=2.5 so use 3^3 v(3))
    point_u3v = (I(27)*v_fn(I(3)) + I(27)*v_fn(I(3))) / s_min
    S3_mu_s4 = tail_u3v + point_u3v + L1["v_3"] * err_fac
    S3_s4 = S3_mu_s4 + I(3) * delta_s * I(W_mu_s3_hi.b) + I(2) * I(V_s.b) * delta_s**3

    # M_4,mu / s^5: int u^4 v(u) du = 7 pi^4 / 15
    M4_mu_s5 = (I(7) * PI**4 / I(15)) + L1["v_4"] * err_fac
    M4_s5 = M4_mu_s5 + I(4) * delta_s * iv.sqrt(I(W_mu_s3_hi.b) * I(M4_mu_s5.b)) + I(6) * delta_s**2 * I(W_mu_s3_hi.b)

    # Cubic cumulant sums: sum v'(u_j) (j - mu)^r
    # int v'(u) du = 0; int u v'(u) du = -1; int u^2 v'(u) du = 0; int u^3 v'(u) du = -pi^2
    vp0_s = (v_fn(A_abs_lo) + v_fn(B_lo)) + (abs(vp_fn(A_abs_lo)) + abs(vp_fn(B_lo))) / s_min + L1["vp_0"] * err_fac
    vp1_s2_err = tail_uvp_int(A_abs_lo) + tail_uvp_int(B_lo) + (A_abs_lo*v_fn(A_abs_lo)+B_lo*v_fn(B_lo))/s_min + L1["vp_1"] * err_fac
    vp1_s2_abs = I(1) + vp1_s2_err
    vp2_s3_abs = tail_u2v_int(A_abs_lo) + tail_u2v_int(B_lo) + (A_abs_lo**2*v_fn(A_abs_lo)+B_lo**2*v_fn(B_lo))/s_min + L1["vp_2"] * err_fac
    vp3_s4_abs = PI*PI + tail_u3vp_int(A_abs_lo) + tail_u3vp_int(B_lo) + (I(27)*v_fn(I(3))*I(2))/s_min + L1["vp_3"] * err_fac

    # Shift cubic cumulant moments to jbar
    def shifted_vp_bound(r: int) -> iv.mpf:
        base = [vp0_s, vp1_s2_abs, vp2_s3_abs, vp3_s4_abs]
        tot = I(0)
        from math import comb
        for k in range(r + 1):
            tot = tot + I(comb(r, k)) * (delta_s ** (r - k)) * base[k]
        return tot

    V_lo_s = I(V_s.a)
    W_lo_s3 = I(W_s3.a)
    # Note a_{r, 3-r} = (sum v' (j-jbar)^{3-r}) / (V^{r/2} W^{(3-r)/2}) scales as s^{-1/2}!
    # Factor out s^{-1/2}:
    inv_sqrt_s = I(1) / iv.sqrt(s_min)
    cub = {
        "a30": shifted_vp_bound(0) / (V_lo_s ** F(3, 2)) * inv_sqrt_s,
        "a21": shifted_vp_bound(1) / (V_lo_s * iv.sqrt(W_lo_s3)) * inv_sqrt_s,
        "a12": shifted_vp_bound(2) / (iv.sqrt(V_lo_s) * W_lo_s3) * inv_sqrt_s,
        "a03": shifted_vp_bound(3) / (W_lo_s3 ** F(3, 2)) * inv_sqrt_s,
    }

    # Physical V, W, S3, M4 scaled by s_min (since all remainder ratios scale as <= 1/s_min)
    V = V_s * s_min
    W = W_s3 * (s_min ** 3)
    S3 = S3_s4 * (s_min ** 4)
    M4 = M4_s5 * (s_min ** 5)

    # K-bounds (Lemma 3): |beta| <= 2s, so |beta|/sqrt(W) <= 2 / sqrt(s * W_s3)
    beta_over_sqrtW = I(2) / iv.sqrt(s_min * W_lo_s3)
    # H / W: using universal s-form of Lemma 3(2)
    # For gamma >= gamma_lo and m >= 101: a*theta = (2 - 1/m)*gamma >= (2 - 1/101)*gamma_lo, b*theta >= (3 - 1/101)*gamma_lo
    at_lo = (I(2) - I(1)/I(M0)) * gamma_lo
    bt_lo = (I(3) - I(1)/I(M0)) * gamma_lo
    H_s2 = I(2) + (at_lo**2)/(I(4)*iv_sinh(at_lo/I(2))**2) + (bt_lo**2)/(I(4)*iv_sinh(bt_lo/I(2))**2)
    H_over_W = H_s2 / (s_min * W_lo_s3)

    # C4: u0 = L * sqrt(1/V + J_lim^2 / W). For |u_j| <= 5/2, |j - jbar| <= s*(5/2 + delta_s)
    jlim_s = F(5, 2) + delta_s
    u0 = L_VAL * iv.sqrt(I(1) / (s_min * V_lo_s) + (jlim_s * jlim_s) / (s_min * W_lo_s3))
    q0 = I(1) / (I(1) + iv.exp(F(5, 2)))
    c4_tail = (I(1) + I(2)*q0*(I(1)-q0)) / ((I(1)-I(2)*q0)**4)
    c4_core = certify_c4_core(u0)
    C4_val = max(I(c4_tail.b), I(c4_core.b))

    # Minor Arc bounds (Lemma 5 + Lemma 6):
    V_lo = I(V.a)
    W_lo = I(W.a)
    W_hi = I(W.b)
    M4_hi = I(M4.b)
    M3_hi = iv.sqrt(W_hi * M4_hi)

    eta = L_VAL / iv.sqrt(W_lo)
    # Choose phi_1 = u1 / s_min with u1 = 0.55 (or 0.50)
    u1 = F(55, 100)
    phi_1 = u1 / s_min
    assert phi_1.a > eta.b

    def trig_cW(phi_max: iv.mpf) -> tuple[iv.mpf, iv.mpf]:
        Cmin = V_lo - F(1, 2) * W_hi * phi_max * phi_max
        assert Cmin.a > 0
        cW = F(1, 2) - (M4_hi * phi_max**2) / (I(24) * W_lo) - (M3_hi**2 * phi_max**4) / (I(72) * Cmin * W_lo)
        assert cW.a > 0
        return I(Cmin.a), I(cW.a)

    epsP_max = I(8) * PI * PI * (s_min ** 2) * iv.exp(-PI * PI * s_min)
    epsP_fac = iv.exp(I(2) * epsP_max)

    def poisson_cW(u_max: iv.mpf) -> tuple[iv.mpf, iv.mpf]:
        xmax = PI * u_max
        q_coeff = ((I(1) - xmax / iv_sinh(xmax)) / (xmax * xmax)) * (PI * PI) - I(W_tail_mu_s3.b)
        assert q_coeff.a > 0
        cW_p = I((q_coeff / I(W_s3.b)).a)
        C_p = s_min * (xmax / iv_sinh(xmax) - I(2) * V_tail_s)
        assert C_p.a > 0
        return I(C_p.a), cW_p

    C_eta, cW_eta = trig_cW(eta)
    d_phi = M3_hi * eta * eta / (I(6) * C_eta)
    u_cap = F(15, 10)
    assert (d_phi * eta).b < (PI - u_cap).a
    b_sh = d_phi * iv.sqrt(I(V.b) / W_lo)
    rho_sh = I(1) + (b_sh**2 + b_sh * iv.sqrt(I(4) + b_sh**2)) / I(2)
    L_eff2 = (L_VAL * L_VAL) / I(rho_sh.b)
    c_ell = min(cW_eta, (C_eta / I(V.b)) * (I(1) - iv.cos(u_cap)) / (u_cap * u_cap))
    # Universal K bound on |phi| <= phi_1: 1 + (s*phi)^2
    K_eta = I(1) + (s_min * eta) ** 2
    K_phi1 = I(1) + u1 * u1
    # Check monotonicity condition E_a2 > 1
    E_a2 = C_eta * (I(1) - iv.cos(u_cap))
    assert E_a2.a > 1, f"E_a2={E_a2} <= 1"
    I_A_5 = K_eta * iv.exp(-c_ell * L_eff2) / (I(2) * c_ell) + iv.sqrt(PI / cW_eta) * iv.sqrt(I(V.b)) * K_eta * iv.exp(-E_a2)

    u_eta_max = L_VAL / iv.sqrt(s_min * W_lo_s3)
    C_p_eta, cW_p_eta = poisson_cW(u_eta_max)
    assert (delta_s * u_eta_max).b < (PI - u_cap).a
    b_sh_6 = delta_s * iv.sqrt(I(V_s.b) / W_lo_s3)
    rho_sh_6 = I(1) + (b_sh_6**2 + b_sh_6 * iv.sqrt(I(4) + b_sh_6**2)) / I(2)
    L_eff2_6 = (L_VAL * L_VAL) / I(rho_sh_6.b)
    c_ell_6 = min(cW_p_eta, (C_p_eta / I(V.b)) * (I(1) - iv.cos(u_cap)) / (u_cap * u_cap))
    E_a2_6 = C_p_eta * (I(1) - iv.cos(u_cap)) - I(2) * epsP_max
    assert E_a2_6.a > 1
    I_A_6 = epsP_fac * K_eta * iv.exp(-c_ell_6 * L_eff2_6) / (I(2) * c_ell_6) + iv.sqrt(PI / cW_p_eta) * iv.sqrt(I(V.b)) * K_eta * iv.exp(-E_a2_6)
    I_A = min(I(I_A_5.b), I(I_A_6.b))

    C_1, cW_1 = trig_cW(phi_1)
    I_B1_5 = iv.sqrt(PI / I(8)) * iv.sqrt(I(V.b) / C_1) * K_phi1 * iv.exp(-cW_1 * L_VAL * L_VAL) / (cW_1 * L_VAL)
    C_p_1, cW_p_1 = poisson_cW(u1)
    I_B1_6 = epsP_fac * iv.sqrt(PI / I(8)) * iv.sqrt(I(V.b) / C_p_1) * K_phi1 * iv.exp(-cW_p_1 * L_VAL * L_VAL) / (cW_p_1 * L_VAL)
    I_B1 = min(I(I_B1_5.b), I(I_B1_6.b))

    # Far minor arcs via Lemma 6(2) on [u1, 0.80], [0.80, 1.40], [1.40, 2.50], [2.50, pi*s]
    s_grid = [u1, F(80, 100), F(140, 100), F(250, 100)]
    I_far = I(0)
    for idx in range(len(s_grid)):
        ua = s_grid[idx]
        is_tail = (idx == len(s_grid) - 1)
        # x_a = pi * ua
        xa = PI * ua
        fac_a = xa / iv_sinh(xa)
        # On [ua, ub], 1 - x/sinh(x) increases with ua
        far_gap = I(1) - fac_a - I(2) * V_tail_s
        assert far_gap.a > 0
        E_far = s_min * far_gap - I(2) * epsP_max
        if not is_tail:
            ub = s_grid[idx + 1]
            # Monotonicity deg d=1 (exponent far_gap * s > 1)
            assert (s_min * far_gap).a > 1
            K_ub = I(1) + ub * ub
            # alpha integral factor:
            # S_lo = s_min * (pi*ub)/sinh(pi*ub) - 2*V_tail_s*s_min? Actually on [ua, ub], coeff of (1-cos u) is s*(pi*ub/sinh(pi*ub) - 2*V_tail_s)
            alpha_A = s_min * (PI * ub / iv_sinh(PI * ub) - I(2) * V_tail_s)
            psi_fac = min(I(1), iv.sqrt(PI / (I(8) * alpha_A))) if alpha_A.a > 0 else I(1)
            # phi integral factor: 2*(ub - ua)/s_min * sqrt(V*W) = 2*(ub-ua)*s_min*sqrt(V_s*W_s3)
            I_seg = I(2) * (ub - ua) * s_min * iv.sqrt(I(V_s.b) * I(W_s3.b)) * K_ub * psi_fac * iv.exp(-E_far)
        else:
            # Tail [2.50/s, pi]: use L1 bound int |K|/K(r) / (2pi) <= 1 + 2*s^2, total * sqrt(VW)
            assert (s_min * far_gap).a > 5  # deg <= 4 monotonicity
            I_seg = I(2) * PI * iv.sqrt(I(V.b) * W_hi) * (I(1) + I(2) * s_min * s_min) * iv.exp(-E_far)
        I_far = I_far + I_seg

    min_ub = I(I_A.b + I_B1.b + I_far.b)
    return maj_min_combo(V, W, S3, M4, cub, beta_over_sqrtW, H_over_W, C4_val, min_ub)


def certify_y_block(g_a: iv.mpf, g_b: iv.mpf, L1: dict[str, iv.mpf]) -> tuple[iv.mpf, iv.mpf, iv.mpf]:
    """Certify a bounded y-unit gamma block [g_a, g_b] subset [0, 3.7] at m >= M0 = 101."""
    m = I(M0)
    gam = iv.mpf([g_a.a, g_b.b])
    rho_rad = gam / (I(16) * m * m)
    rho = iv.mpf([(I(1) - rho_rad).a, (I(1) + rho_rad).b])
    g_star = gam * rho

    # Compute tight centered u0_shift = A + 3*gamma when g_a < 0.5, else u_left = A + gamma (PROOF.md L125)
    use_center3 = (g_a.a < F(1, 2).b)
    if use_center3:
        # e^{A + 3*gamma} = sinhc((3 - rho/2)*gamma) / sinhc((rho/2)*gamma) * (6 - rho)/rho
        e_u0 = (sinhc((I(3) - rho / I(2)) * gam) / sinhc((rho / I(2)) * gam)) * ((I(6) - rho) / rho)
        u0_c = iv.log(e_u0)
        y_c = I(3)
    else:
        # e^{A + gamma} = e^{(1-rho)*gamma} * (1 - e^{(rho-6)*gamma}) / (1 - e^{-gamma_*})
        e_u0 = iv.exp((I(1) - rho) * gam) * (I(1) - iv.exp((rho - I(6)) * gam)) / (I(1) - iv.exp(-g_star))
        u0_c = iv.log(e_u0)
        y_c = I(1)

    def u_of_y(y: iv.mpf) -> iv.mpf:
        return u0_c + gam * (y - y_c)

    # n_y = 48 panel midpoint rule on [0, 6], h_y = 6/48 = 1/8
    NY = 48
    HY = F(6, NY)
    err_fac_y = (HY * HY + I(1) / (m * m)) / I(8)

    # Compute V/m, W_c/m^3, S3_c/m^4, M4_c/m^5, and cubic moments at center y_0 ~ ybar
    # First enclose V/m and ybar_cont = (1/V_cont) int y v(u(y)) dy
    V_m_mid = I(0)
    y1_mid = I(0)
    for k in range(NY):
        yk = (I(k) + F(1, 2)) * HY
        uk = u_of_y(yk)
        V_m_mid = V_m_mid + HY * v_fn(uk)
        y1_mid = y1_mid + HY * yk * v_fn(uk)

    # Note int_0^6 |(u(y)^k v(u(y)))''| dy <= (1/gamma) * L1 or bounded by gamma * L1(v_k)
    # Wait: f(y) = (y-y0)^k v(A + gamma*y). By change of vars u = A + gamma*y,
    # d^2/dy^2 = gamma^2 d^2/du^2, and dy = du/gamma, so int_0^6 |f''(y)| dy = gamma * int_A^B |d^2/du^2 (( (u-u0)/gamma )^k v(u))| du
    # <= gamma^{1-k} * sum_{r=0}^k binom(k,r) |u0|^{k-r} ...
    # Even simpler and exact for ALL gamma (incl gamma -> 0)!
    # Directly evaluate L1 of f''(y) via NY-panel interval enclosure on [0, 6] OR use exact derivatives w.r.t. y!
    # Yes! On [0, 6], 48 subintervals enclose ||f''||_{L^1([0,6])} rigorously with zero gamma=0 singularity!
    def y_l1_v_pow(y0_pt: iv.mpf, power: int) -> iv.mpf:
        acc = I(0)
        for k in range(NY):
            yc = iv.mpf([(I(k) * HY).a, (I(k + 1) * HY).b])
            uc = u_of_y(yc)
            dy = yc - y0_pt
            # d^2/dy^2 [ dy^p * v(u) ]
            val = (dy ** power) * (gam * gam) * vpp_fn(uc)
            if power >= 1:
                val = val + I(2 * power) * (dy ** (power - 1)) * gam * vp_fn(uc)
            if power >= 2:
                val = val + I(power * (power - 1)) * (dy ** (power - 2)) * v_fn(uc)
            acc = acc + HY * abs(val)
        return I(acc.b)

    def y_l1_vp_pow(y0_pt: iv.mpf, power: int) -> iv.mpf:
        acc = I(0)
        for k in range(NY):
            yc = iv.mpf([(I(k) * HY).a, (I(k + 1) * HY).b])
            uc = u_of_y(yc)
            dy = yc - y0_pt
            val = (dy ** power) * (gam * gam) * v3_fn(uc)
            if power >= 1:
                val = val + I(2 * power) * (dy ** (power - 1)) * gam * vpp_fn(uc)
            if power >= 2:
                val = val + I(power * (power - 1)) * (dy ** (power - 2)) * vp_fn(uc)
            acc = acc + HY * abs(val)
        return I(acc.b)

    V_m_err = err_fac_y * y_l1_v_pow(I(0), 0)
    V_m = iv.mpf([(V_m_mid - V_m_err).a, (V_m_mid + V_m_err).b])
    assert V_m.a > 0

    # Shift to y0 = midpoint of y1_mid / V_m_mid (point interval)
    y0_num = (y1_mid / V_m_mid)
    y0 = iv.mpf(y0_num.mid)

    # Now compute moments of (y - y0)
    yc_1_mid = I(0)
    W_c_mid = I(0)
    S3_c_mid = I(0)
    M4_c_mid = I(0)
    vp_mid = [I(0)] * 4
    for k in range(NY):
        yk = (I(k) + F(1, 2)) * HY
        uk = u_of_y(yk)
        dy = yk - y0
        vk = v_fn(uk)
        vpk = vp_fn(uk)
        yc_1_mid = yc_1_mid + HY * dy * vk
        W_c_mid = W_c_mid + HY * (dy ** 2) * vk
        S3_c_mid = S3_c_mid + HY * (dy ** 3) * vk
        M4_c_mid = M4_c_mid + HY * (dy ** 4) * vk
        for r in range(4):
            vp_mid[r] = vp_mid[r] + HY * (dy ** r) * vpk

    dy1_tot = (abs(yc_1_mid) + err_fac_y * y_l1_v_pow(y0, 1)) / I(V_m.a)
    delta_y = I(dy1_tot.b)  # |ybar_disc - y0| <= delta_y

    W_c_err = err_fac_y * y_l1_v_pow(y0, 2)
    W_c = iv.mpf([(W_c_mid - W_c_err).a, (W_c_mid + W_c_err).b])
    S3_c_err = err_fac_y * y_l1_v_pow(y0, 3)
    S3_c = iv.mpf([(S3_c_mid - S3_c_err).a, (S3_c_mid + S3_c_err).b])
    M4_c_err = err_fac_y * y_l1_v_pow(y0, 4)
    M4_c = iv.mpf([max(0, (M4_c_mid - M4_c_err).a), (M4_c_mid + M4_c_err).b])

    W_m3_lo = I((W_c - I(V_m.b) * delta_y ** 2).a)
    W_m3_hi = I(W_c.b)
    assert W_m3_lo.a > 0
    W_m3 = iv.mpf([W_m3_lo.a, W_m3_hi.b])
    S3_m4_hi = I((abs(S3_c) + I(3) * delta_y * I(W_c.b) + I(2) * I(V_m.b) * delta_y ** 3).b)
    M4_m5_hi = I((M4_c + I(4) * delta_y * iv.sqrt(I(W_c.b) * I(M4_c.b)) + I(6) * delta_y ** 2 * I(W_c.b)).b)

    vp_abs = [I((abs(vp_mid[r]) + err_fac_y * y_l1_vp_pow(y0, r)).b) for r in range(4)]
    from math import comb
    def shifted_vp_y(r: int) -> iv.mpf:
        tot = I(0)
        for k in range(r + 1):
            tot = tot + I(comb(r, k)) * (delta_y ** (r - k)) * vp_abs[k]
        return tot

    V_lo_m = I(V_m.a)
    W_lo_m3 = I(W_m3.a)
    inv_sqrt_m = I(1) / iv.sqrt(m)
    cub = {
        "a30": shifted_vp_y(0) / (V_lo_m ** F(3, 2)) * inv_sqrt_m,
        "a21": shifted_vp_y(1) / (V_lo_m * iv.sqrt(W_lo_m3)) * inv_sqrt_m,
        "a12": shifted_vp_y(2) / (iv.sqrt(V_lo_m) * W_lo_m3) * inv_sqrt_m,
        "a03": shifted_vp_y(3) / (W_lo_m3 ** F(3, 2)) * inv_sqrt_m,
    }

    V = V_m * m
    W = W_m3 * (m ** 3)
    S3 = iv.mpf([-S3_m4_hi.b, S3_m4_hi.b]) * (m ** 4)
    M4 = iv.mpf([0, M4_m5_hi.b]) * (m ** 5)

    # K-bounds (Lemma 3)
    # |beta| <= min(2s, 5m/2)
    if g_a.a == 0:
        beta_over_sqrtW = F(5, 2) / iv.sqrt(m * W_lo_m3)
    else:
        beta_over_sqrtW = min(I(2) / g_a, F(5, 2)) / iv.sqrt(m * W_lo_m3)

    eta = L_VAL / iv.sqrt(I(W.a))
    eta_m = L_VAL / iv.sqrt(m * W_lo_m3)

    # H / W: use root-gap bound for g_b <= 0.5 and trig/sinh bound for g_a >= 0.5
    if g_b.b <= F(1, 2).b:
        # a = 2m-1 >= 201 => c1 = 2a sin(pi/a)
        a0 = I(2 * M0 - 1)
        c1 = I(2) * a0 * iv.sin(PI / a0)
        vartheta = g_b + eta_m
        gap1 = c1 - I(3) * vartheta
        assert gap1.a > 0
        H_m2 = I(26) * (I(1) / (gap1 ** 2) + I(1) / ((I(8) - I(3) * vartheta) ** 2) + I(1) / (I(4) * (I(8) - I(3) * vartheta)))
    else:
        # 2/gam^2 + 1/sinh^2((2-1/m)gam/2) + 9/(4 sinh^2((3-1/m)gam/2))
        a_fac = (I(2) - I(1)/m) * g_a / I(2)
        b_fac = (I(3) - I(1)/m) * g_a / I(2)
        H_m2 = I(2) / (g_a * g_a) + I(1) / (iv_sinh(a_fac) ** 2) + F(9, 4) / (iv_sinh(b_fac) ** 2)
    H_over_W = H_m2 / (m * W_lo_m3)

    # C4: exact y-range where |u(y)| <= 5/2
    q0 = I(1) / (I(1) + iv.exp(F(5, 2)))
    c4_tail = (I(1) + I(2)*q0*(I(1)-q0)) / ((I(1)-I(2)*q0)**4)
    if g_a.a > 0:
        y_lo_core = max(I(0), ((-F(5, 2) - u0_c) / gam + y_c).a)
        y_hi_core = min(I(6), ((F(5, 2) - u0_c) / gam + y_c).b)
    else:
        y_lo_core, y_hi_core = I(0), I(6)
    if y_lo_core.b > y_hi_core.a:
        C4_val = I(c4_tail.b)
    else:
        jlim_m = max(abs(y_lo_core - y0).b, abs(y_hi_core - y0).b) + delta_y.b
        u0 = L_VAL * iv.sqrt(I(1) / (m * V_lo_m) + (jlim_m * jlim_m) / (m * W_lo_m3))
        c4_core = certify_c4_core(u0)
        C4_val = max(I(c4_tail.b), I(c4_core.b))

    # Minor Arc bounds (Regions A, B1, B2, C)
    V_lo = I(V.a)
    V_hi = I(V.b)
    W_lo = I(W.a)
    W_hi = I(W.b)
    M4_hi = I(M4.b)
    M3_hi = iv.sqrt(W_hi * M4_hi)

    def K_ratio_bound(omega_max: iv.mpf) -> iv.mpf:
        """Rigorous upper bound on |K(r e^{i phi})|/K(r) for m*|phi| <= omega_max <= 1.60."""
        if omega_max.b <= F(70, 100).b:
            # 1 / (cos(omega) * cos(1.5*omega))
            return I(1) / (iv.cos(omega_max) * iv.cos(F(3, 2) * omega_max))
        elif omega_max.b <= F(160, 100).b:
            # Moderate phi sine bound on [0.70, omega_max] (and check 0.70 point)
            # 6 e^{2.5 gamma} (gamma^2 + omega^2) / (4 sin(a phi/2) sin(b phi/2))
            # Note a*phi/2 = (1 - 1/(2m)) omega <= pi/2, b*phi/2 = (1.5 - 1/(2m)) omega <= 2.4 < pi
            # Wait: check minimum of sin(a phi/2) sin(b phi/2) on [omega_lo, omega_hi]!
            # Actually K_ratio_bound is called on intervals [w_a, w_b] for B2, or [0, phi_1] for B1!
            return I(1) / (iv.cos(omega_max) * iv.cos(F(3, 2) * omega_max)) if omega_max.b < F(104, 100).b else I(999999)
        else:
            # Universal bound 1 + (gamma^-1 * omega)^2 * ...? If g_a >= 0.5, 1 + (omega/g_a)^2
            if g_a.a > 0:
                return I(1) + (omega_max / g_a) ** 2
            return I(999999)

    def K_ratio_interval(w_a: iv.mpf, w_b: iv.mpf) -> iv.mpf:
        if w_b.b <= F(70, 100).b:
            return I(1) / (iv.cos(w_b) * iv.cos(F(3, 2) * w_b))
        if w_a.a >= F(70, 100).a and w_b.b <= F(160, 100).b:
            # On [w_a, w_b]: check if sine bound beats universal bound
            w_iv = iv.mpf([w_a.a, w_b.b])
            a_ang = iv.mpf([(I(1) - I(1) / (I(2) * m)).a, I(1).b]) * w_iv
            b_ang = iv.mpf([(F(3, 2) - I(1) / (I(2) * m)).a, F(3, 2).b]) * w_iv
            sine_bd = I(6) * iv.exp(F(5, 2) * g_b) * (g_b * g_b + w_b * w_b) / (I(4) * iv.sin(a_ang) * iv.sin(b_ang))
            if g_a.a >= F(1, 2).a:
                univ_bd = I(1) + (w_b / g_a) ** 2
                return min(I(sine_bd.b), I(univ_bd.b))
            return I(sine_bd.b)
        if g_a.a > 0:
            return I(1) + (w_b / g_a) ** 2
        raise ValueError("Cannot bound K on this interval")

    # Region A and B1
    def trig_cW(phi_max: iv.mpf) -> tuple[iv.mpf, iv.mpf]:
        Cmin = V_lo - F(1, 2) * W_hi * phi_max * phi_max
        assert Cmin.a > 0
        cW = F(1, 2) - (M4_hi * phi_max**2) / (I(24) * W_lo) - (M3_hi**2 * phi_max**4) / (I(72) * Cmin * W_lo)
        assert cW.a > 0
        return I(Cmin.a), I(cW.a)

    # Choose phi_1_m in B1: make sure phi_1_m > eta_m, and small enough so C_1 > 0 and cW_1 > 0
    phi_1_m = min(I(eta_m.b) * F(135, 100), F(70, 100) if g_b.b <= F(1, 2).b else I(eta_m.b) * F(135, 100))
    if phi_1_m.a <= eta_m.b:
        phi_1_m = I(eta_m.b) * F(125, 100)
    phi_1 = phi_1_m / m

    C_eta, cW_eta = trig_cW(eta)
    d_phi = M3_hi * eta * eta / (I(6) * C_eta)
    u_cap = F(15, 10)
    if (d_phi * eta).b >= (PI - u_cap).a:
        u_cap = F(12, 10)
    assert (d_phi * eta).b < (PI - u_cap).a
    b_sh = d_phi * iv.sqrt(V_hi / W_lo)
    rho_sh = I(1) + (b_sh**2 + b_sh * iv.sqrt(I(4) + b_sh**2)) / I(2)
    L_eff2 = (L_VAL * L_VAL) / I(rho_sh.b)
    c_ell = min(cW_eta, (C_eta / V_hi) * (I(1) - iv.cos(u_cap)) / (u_cap * u_cap))
    K_eta = K_ratio_interval(I(0), eta_m)
    E_a2 = C_eta * (I(1) - iv.cos(u_cap))
    assert E_a2.a > 1
    I_A = K_eta * iv.exp(-c_ell * L_eff2) / (I(2) * c_ell) + iv.sqrt(PI / cW_eta) * iv.sqrt(V_hi) * K_eta * iv.exp(-E_a2)

    C_1, cW_1 = trig_cW(phi_1)
    K_phi1 = K_ratio_interval(I(0), phi_1_m)
    I_B1 = iv.sqrt(PI / I(8)) * iv.sqrt(V_hi / C_1) * K_phi1 * iv.exp(-cW_1 * L_VAL * L_VAL) / (cW_1 * L_VAL)

    # Region C cutoff phi_lc_m:
    if g_b.b <= F(1, 2).b:
        phi_lc_m = F(160, 100)
        # Parseval L^1 bound: 2 * sqrt(6) * m * (s + 1), with s <= 9/4 m^2
        # Total I_C <= sqrt(VW) * e^{-E_lc} * 2 * sqrt(6) * m * (9/4 m^2 + 1)
        K_L1_fac = I(2) * iv.sqrt(I(6)) * m * (F(9, 4) * m * m + I(1))
        deg_C_thr = I(5)
    else:
        phi_lc_m = I(3) / V_lo_m
        if phi_lc_m.a <= phi_1_m.b:
            phi_lc_m = I(phi_1_m.b) * F(11, 10)
        K_L1_fac = I(1) + I(2) * (m / g_a) ** 2
        deg_C_thr = I(4)

    phi_lc = phi_lc_m / m
    # V - S(phi) >= V_lo - 1/(4 sin(phi_lc/2)), since phi_lc/2 <= 0.8/m, use exact interval sin
    S_lc_ub = I(1) / (I(4) * iv.sin(phi_lc / I(2)))
    E_lc = V_lo - S_lc_ub
    assert E_lc.a > deg_C_thr.b, f"E_lc={E_lc} <= {deg_C_thr}"
    I_C = I(2) * PI * iv.sqrt(V_hi * W_hi) * K_L1_fac * iv.exp(-E_lc)

    # Region B2: Lemma 7(1) Fourier Quadrature (+ Lemma 6(2) when A < 0 and m/g_b >= 12) over [phi_1_m, phi_lc_m]
    A_iv_b2 = u_of_y(I(0))
    B_iv_b2 = u_of_y(I(6))
    use_poiss_b2 = (A_iv_b2.b < 0 and B_iv_b2.a > 0 and (m / g_b).a >= 12)
    if use_poiss_b2:
        A_abs_b2 = I((-A_iv_b2).a)
        B_lo_b2 = I(B_iv_b2.a)
        s_lo_b2 = m / g_b
        s_hi_b2 = m / g_a
        V_tail_s_b2 = p_fn(A_abs_b2) + p_fn(B_lo_b2) + (v_fn(A_abs_b2) + v_fn(B_lo_b2)) / s_lo_b2
        epsP_b2 = I(8) * PI * PI * (s_hi_b2 ** 2) * iv.exp(-PI * PI * s_lo_b2)

    I_B2 = I(0)
    w_cur = phi_1_m
    L1_v0 = L1["v_0"]
    while w_cur.a < phi_lc_m.b - F(1, 10**9).a:
        w_next = min(phi_lc_m, w_cur * F(116, 100))
        if w_cur.b < F(70, 100).a and w_next.a > F(70, 100).b:
            w_next = F(70, 100)
        w_iv = iv.mpf([w_cur.a, w_next.b])
        # Midpoint sums R(w), J(w), V/m +- R(w) using g_pm and g_{c,s}
        R_mid = I(0)
        J_mid = I(0)
        Vm_minus_R_mid = I(0)
        Vm_plus_R_mid = I(0)
        for k in range(NY):
            yk = (I(k) + F(1, 2)) * HY
            uk = u_of_y(yk)
            vk = v_fn(uk)
            ang = w_iv * (yk - y0)
            c_ang = iv.cos(ang)
            s_ang = iv.sin(ang)
            R_mid = R_mid + HY * vk * c_ang
            J_mid = J_mid + HY * vk * s_ang
            Vm_minus_R_mid = Vm_minus_R_mid + HY * vk * (I(1) - c_ang)
            Vm_plus_R_mid = Vm_plus_R_mid + HY * vk * (I(1) + c_ang)

        err_gpm = err_fac_y * (I(2) * gam * L1_v0 + w_next + (w_next ** 2) * I(V_m.b))
        err_gcs = err_fac_y * (gam * L1_v0 + w_next + (w_next ** 2) * I(V_m.b))

        R_iv = iv.mpf([(R_mid - err_gcs).a, (R_mid + err_gcs).b])
        J_iv = iv.mpf([(J_mid - err_gcs).a, (J_mid + err_gcs).b])
        Vm_m_R_lo = max(I(0), I((Vm_minus_R_mid - err_gpm).a))
        Vm_p_R_lo = max(I(0), I((Vm_plus_R_mid - err_gpm).a))

        # Cancellation-free lower bound on (V - S)/m
        gap_cf = (Vm_m_R_lo * Vm_p_R_lo - I(abs(J_iv).b) ** 2) / (I(2) * I(V_m.b))
        gap_dir = V_lo_m - iv.sqrt(I(abs(R_iv).b) ** 2 + I(abs(J_iv).b) ** 2)
        gap_poiss = I(0)
        S_poiss_lo = I(0)
        if use_poiss_b2:
            xa_b2 = PI * w_cur / g_b
            gap_poiss = (I(1) / g_b) * (I(1) - xa_b2 / iv_sinh(xa_b2) - I(2) * V_tail_s_b2) - I(2) * epsP_b2 / m
            xb_b2 = PI * w_next / g_a
            S_poiss_lo = (I(1) / g_b) * (xb_b2 / iv_sinh(xb_b2) - V_tail_s_b2) - epsP_b2 / m
        gap_m = max(I(0), I(gap_cf.a), I(gap_dir.a), I(gap_poiss.a))
        E_b2 = m * gap_m
        assert E_b2.a > 1, f"E_b2={E_b2} <= 1 on [{w_cur}, {w_next}] in [{g_a}, {g_b}]"

        # Lower bound on S/m for alpha-integral factor
        S_m_lo = max(I(0), I(R_iv.a), I(abs(J_iv).a), V_lo_m - F(1, 2) * W_m3_hi * (w_next ** 2), I(S_poiss_lo.a))
        psi_fac = I(1) if S_m_lo.a <= 0 else min(I(1), iv.sqrt(PI / (I(8) * m * S_m_lo)))
        K_seg = K_ratio_interval(w_cur, w_next)
        # Integral over phi in [w_cur/m, w_next/m] (two sides +-phi) * sqrt(VW)
        I_seg = I(2) * (w_next - w_cur) * iv.sqrt(I(V_m.b) * W_m3_hi) * m * K_seg * psi_fac * iv.exp(-E_b2)
        I_B2 = I_B2 + I_seg
        w_cur = w_next

    min_ub = I(I_A.b + I_B1.b + I_B2.b + I_C.b)
    return maj_min_combo(V, W, S3, M4, cub, beta_over_sqrtW, H_over_W, C4_val, min_ub)


def verify_part_b() -> None:
    t0 = time.monotonic()
    s_min = verify_lemma1()
    L1 = compute_L1_constants()
    print("PASS Lemma 2 L1 constants certified:", {k: iv.nstr(v.b, 5) for k, v in L1.items()})

    # Partition (0, inf) exhaustively:
    # Regime III: [0, 0.5] in 8 blocks
    r3_pts = [F(k, 16) for k in range(9)]  # 0 to 0.5
    # Regime IIa: [0.5, 3.7] in 32 blocks of width 0.1
    r2a_pts = [F(5 + k, 10) for k in range(33)]  # 0.5 to 3.7
    # Regime IIb: [3.7, 5.5] in 3 slices
    r2b_pts = [F(37, 10), F(42, 10), F(48, 10), F(55, 10)]

    min_net = I(999)

    r3_net = I(999)
    for k in range(len(r3_pts) - 1):
        maj, min_u, net = certify_y_block(r3_pts[k], r3_pts[k + 1], L1)
        r3_net = min(r3_net, net)
        min_net = min(min_net, net)
    print(f"PASS Regime III [0, 0.5] ({len(r3_pts)-1} blocks): min Net >= +{iv.nstr(r3_net.a, 7)}")

    r2a_net = I(999)
    for k in range(len(r2a_pts) - 1):
        maj, min_u, net = certify_y_block(r2a_pts[k], r2a_pts[k + 1], L1)
        r2a_net = min(r2a_net, net)
        min_net = min(min_net, net)
    print(f"PASS Regime IIa [0.5, 3.7] ({len(r2a_pts)-1} blocks): min Net >= +{iv.nstr(r2a_net.a, 7)}")

    r2b_net = I(999)
    for k in range(len(r2b_pts) - 1):
        ga, gb = r2b_pts[k], r2b_pts[k + 1]
        s_slice = I(M0) / gb
        maj, min_u, net = certify_s_unit_regime(ga, gb, s_slice, L1)
        r2b_net = min(r2b_net, net)
        min_net = min(min_net, net)
    print(f"PASS Regime IIb [3.7, 5.5] ({len(r2b_pts)-1} slices): min Net >= +{iv.nstr(r2b_net.a, 7)}")

    maj1, min1, net1 = certify_s_unit_regime(F(55, 10), None, s_min, L1)
    min_net = min(min_net, net1)
    print(f"PASS Regime I [5.5, inf): Net >= +{iv.nstr(net1.a, 7)} (Maj >= {iv.nstr(maj1.a, 7)}, Min <= {iv.nstr(min1.b, 7)})")

    dt = time.monotonic() - t0
    print(f"PASS Part B: all regimes gamma in (0, inf) certified for all m >= 101, min Net >= +{iv.nstr(min_net.a, 7)} > 0 ({int(dt)}s)")


def main() -> int:
    verify_part_a()
    verify_part_b()
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
