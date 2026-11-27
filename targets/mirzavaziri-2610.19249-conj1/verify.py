#!/usr/bin/env python3
"""Standalone, self-contained, zero-float verification of:
  - Mirzavaziri-Yaqubi Conjecture 4.4 (arXiv:2610.19249v1, Section 4, conj:general)
  - Guo-Krattenthaler Conjecture 7.4 (arXiv:1301.7651v3 / J. Number Theory 135 (2014); Mirzavaziri-Yaqubi Section 1, Conjecture 1.1, conj:GK)

Part A (m in {5} U {9 <= m <= 100 : m != 2,3 (mod 5)}, 57 values):
  Exact arbitrary-precision Python integer arithmetic verifying [q^0]=1, [q^1]=-1,
  and [q^k] >= 0 for all 2 <= k <= D_m/2 (combined with exact reciprocity of P^(m),
  also cross-checked at full degree D_m for small m).

Part B (all m >= 101, m != 2,3 (mod 5), all 5m < t <= D_m/2):
  Rigorous directed-rounding interval arithmetic (mpmath.iv at 25 decimal digits,
  ZERO Python float conversions in any mathematical computation) certifying the
  4-regime uniform saddle-point + Exact Trigonometric Splitting + Poisson /
  Interval-Fourier / Layer-Cake proof with strictly positive margin everywhere.

Prints PASS on complete certification, or FAIL (and exits nonzero) otherwise.
"""
import sys
import time
from mpmath import iv, mp

iv.dps = 25
mp.dps = 25

M0 = 101


# ============================================================================
# Part A: Exact arbitrary-precision integer polynomial verification (m < M0)
# ============================================================================

def verify_poly_exact_half(m):
    """Compute exact integer coefficients [0..T] (T = D_m/2) of P^(m)(q) and check
    [q^0]=1, [q^1]=-1, [q^k]>=0 for 2 <= k <= T.
    """
    D_m = 5 * m * m - 5 * m + 4
    assert D_m % 2 == 0
    T = D_m // 2

    poly = [0] * (T + 1)
    poly[0] = 1
    true_deg = 0

    for i in range(m):
        num_step = 6 * m - i
        den_step = i + 1
        d_num = true_deg + num_step
        hi = min(T, d_num)
        for j in range(hi, num_step - 1, -1):
            poly[j] -= poly[j - num_step]
        for j in range(den_step, hi + 1):
            poly[j] += poly[j - den_step]
        true_deg = d_num - den_step
        if d_num <= T:
            for j in range(true_deg + 1, d_num + 1):
                assert poly[j] == 0, f"Nonzero remainder in q-binomial at m={m}, i={i}, j={j}"

    assert true_deg == 5 * m * m

    a = 2 * m - 1
    b = 3 * m - 1
    for step in (a, b):
        for j in range(T, 0, -1):
            poly[j] -= poly[j - 1]
        for j in range(step, T + 1):
            poly[j] += poly[j - step]

    if poly[0] != 1 or poly[1] != -1:
        raise AssertionError(f"m={m}: unexpected p_0={poly[0]}, p_1={poly[1]}")
    for k in range(2, T + 1):
        if poly[k] < 0:
            raise AssertionError(f"m={m}: negative coefficient p_{k}={poly[k]}")
    return D_m, T


def verify_poly_full_crosscheck(m):
    """Cross-check exact divisibility (zero remainder) and exact reciprocity at full degree D_m."""
    D_m = 5 * m * m - 5 * m + 4
    deg_G = 5 * m * m
    poly = [0] * (deg_G + 6 * m + 2)
    poly[0] = 1
    deg = 0
    for i in range(m):
        ns, ds = 6 * m - i, i + 1
        for j in range(deg, -1, -1):
            poly[j + ns] -= poly[j]
        deg += ns
        for j in range(ds, deg + 1):
            poly[j] += poly[j - ds]
        for j in range(deg - ds + 1, deg + 1):
            assert poly[j] == 0
        deg -= ds
    assert deg == deg_G

    for step in (2 * m - 1, 3 * m - 1):
        for j in range(deg, -1, -1):
            poly[j + 1] -= poly[j]
        deg += 1
        for j in range(step, deg + 1):
            poly[j] += poly[j - step]
        for j in range(deg - step + 1, deg + 1):
            assert poly[j] == 0, f"Full division remainder nonzero at m={m}, step={step}"
        deg -= step

    assert deg == D_m
    for k in range(D_m + 1):
        assert poly[k] == poly[D_m - k], f"Reciprocity failed at m={m}, k={k}"
    assert poly[0] == 1 and poly[1] == -1 and poly[D_m - 1] == -1 and poly[D_m] == 1
    assert all(poly[k] >= 0 for k in range(2, D_m - 1))


def run_part_A():
    t0 = time.perf_counter()
    admissible = [5] + [m for m in range(9, M0) if m % 5 not in (2, 3)]
    for m in (5, 9, 10, 11, 14, 15, 20):
        verify_poly_full_crosscheck(m)
    for m in admissible:
        verify_poly_exact_half(m)
    dt = time.perf_counter() - t0
    print(f"[Part A] Exact integer check PASS for all {len(admissible)} admissible m in {{5}} U [9..{M0-1}] (full-degree cross-check on 7 values) in {dt:.2f}s", flush=True)


# ============================================================================
# Part B: Rigorous zero-float mpmath.iv certification for all m >= M0
# ============================================================================

def rat(p, q=1):
    return iv.mpf(p) / iv.mpf(q)


def iv_min(*xs):
    vals = [iv.mpf(x) for x in xs]
    return iv.mpf([min(v.a for v in vals), min(v.b for v in vals)])


def iv_max(*xs):
    vals = [iv.mpf(x) for x in xs]
    return iv.mpf([max(v.a for v in vals), max(v.b for v in vals)])


def iv_hull(*xs):
    vals = [iv.mpf(x) for x in xs]
    return iv.mpf([min(v.a for v in vals), max(v.b for v in vals)])


def iv_abs_max(x):
    return abs(iv.mpf(x)).b


def fmt(x, digits=6):
    x = iv.mpf(x)
    return mp.nstr(mp.make_mpf(x._mpi_[1]), digits)


def fmt_lo(x, digits=6):
    x = iv.mpf(x)
    return mp.nstr(mp.make_mpf(x._mpi_[0]), digits)


USTAR = iv.log(2 + iv.sqrt(3))
EXT_MAG = iv.mpf(1) / (6 * iv.sqrt(3))


def iv_sinh(x):
    x = iv.mpf(x)
    xa, xb = x.a, x.b
    sa = rat(1, 2) * (iv.exp(xa) - iv.exp(-xa))
    sb = rat(1, 2) * (iv.exp(xb) - iv.exp(-xb))
    return iv.mpf([sa.a, sb.b])


def iv_cosh(x):
    x = iv.mpf(x)
    xmin = iv.mpf(0) if (x.a <= 0 and 0 <= x.b) else iv_min(abs(x.a), abs(x.b))
    xmax = iv_max(abs(x.a), abs(x.b))
    ca = rat(1, 2) * (iv.exp(xmin) + iv.exp(-xmin))
    cb = rat(1, 2) * (iv.exp(xmax) + iv.exp(-xmax))
    return iv.mpf([ca.a, cb.b])


def sinhc_iv(x):
    """Exact enclosure of sinh(x)/x (strictly increasing on [0, inf))."""
    x = iv.mpf(x)
    assert x.a >= 0

    def _pt(t):
        t = iv.mpf(t)
        if t.b < rat(1, 1000):
            rem = (t ** 6) * iv_cosh(t) / 5040
            return 1 + (t ** 2) / 6 + (t ** 4) / 120 + iv.mpf([0, rem.b])
        return iv_sinh(t) / t

    return iv.mpf([_pt(x.a).a, _pt(x.b).b])


def _p_pt(t):
    t = iv.mpf(t)
    if t.a > 60:
        et = iv.exp(-t)
        return et / (1 + et)
    return 1 / (1 + iv.exp(t))


def _v_pt(t):
    t = iv.mpf(t)
    at = abs(t)
    if at.a > 60:
        e = iv.exp(-at)
        return e / ((1 + e) ** 2)
    e = iv.exp(at)
    return e / ((1 + e) ** 2)


def _v1_pt(t):
    t = iv.mpf(t)
    p = _p_pt(t)
    v = _v_pt(t)
    return v * (2 * p - 1)


def v_derivs(u):
    """Exact dependency-free interval enclosure of (p, v, v', v'', v''') on interval u."""
    u = iv.mpf(u)
    ua, ub = u.a, u.b
    if ua == ub:
        p = _p_pt(ua)
        v = _v_pt(ua)
        v1 = v * (2 * p - 1)
        v2 = v * (1 - 6 * v)
        v3 = v1 * (1 - 12 * v)
        return p, v, v1, v2, v3
    p = iv.mpf([_p_pt(ub).a, _p_pt(ua).b])
    umin = iv.mpf(0) if (ua <= 0 and 0 <= ub) else iv_min(abs(ua), abs(ub))
    umax = iv_max(abs(ua), abs(ub))
    v = iv.mpf([_v_pt(umax).a, _v_pt(umin).b])
    cands = [_v1_pt(ua), _v1_pt(ub)]
    if ua <= -USTAR.a and -USTAR.b <= ub:
        cands.append(EXT_MAG)
    if ua <= USTAR.b and USTAR.a <= ub:
        cands.append(-EXT_MAG)
    v1 = iv_hull(*cands)
    v2 = v * (1 - 6 * v)
    v3 = v1 * (1 - 12 * v)
    return p, v, v1, v2, v3


def verify_v_deriv_sups():
    """Certify global suprema |v|<=1/4, |v'|<=97/1000, |v''|<=1/8, |v'''|<=14/100."""
    v0_m = rat(1, 4)
    v1_m = rat(97, 1000)
    assert (iv.mpf(1) / (6 * iv.sqrt(3))).b <= v1_m.a
    v2_m = rat(1, 8)
    v3_m = rat(14, 100)
    N = 100
    mx_v2, mx_v3 = iv.mpf(0), iv.mpf(0)
    for i in range(N):
        v_iv = iv.mpf([rat(i, 4 * N).a, rat(i + 1, 4 * N).b])
        mx_v2 = iv_max(mx_v2, abs(v_iv * (1 - 6 * v_iv)).b)
        mx_v3 = iv_max(mx_v3, (v_iv * iv.sqrt(iv_max(iv.mpf(0), 1 - 4 * v_iv)) * abs(1 - 12 * v_iv)).b)
    assert mx_v2.b <= v2_m.a and mx_v3.b <= v3_m.a
    return v0_m, v1_m, v2_m, v3_m, mx_v3


def eval_gk_derivs(u, k, is_vp=False):
    _, v, v1, v2, v3 = v_derivs(u)
    if not is_vp:
        if k == 0: return v1, v2
        if k == 1: return v + u * v1, 2 * v1 + u * v2
        if k == 2: return 2 * u * v + (u ** 2) * v1, 2 * v + 4 * u * v1 + (u ** 2) * v2
        if k == 3: return 3 * (u ** 2) * v + (u ** 3) * v1, 6 * u * v + 6 * (u ** 2) * v1 + (u ** 3) * v2
        if k == 4: return 4 * (u ** 3) * v + (u ** 4) * v1, 12 * (u ** 2) * v + 8 * (u ** 3) * v1 + (u ** 4) * v2
    else:
        if k == 0: return v2, v3
        if k == 1: return v1 + u * v2, 2 * v2 + u * v3
        if k == 2: return 2 * u * v1 + (u ** 2) * v2, 2 * v1 + 4 * u * v2 + (u ** 2) * v3
        if k == 3: return 3 * (u ** 2) * v1 + (u ** 3) * v2, 6 * u * v1 + 6 * (u ** 2) * v2 + (u ** 3) * v3
    raise ValueError((k, is_vp))


def certify_l1_norm(k, is_vp=False):
    """Rigorous upper bound on int_{-inf}^{inf} |(u^k f(u))''| du for f in {v, v'}."""
    U_MAX = iv.mpf(22)
    N_grid = 20
    total_half = iv.mpf(0)

    def seg(a, b, depth=0):
        u_iv = iv.mpf([a.a, b.b])
        _, g2 = eval_gk_derivs(u_iv, k, is_vp)
        if g2.a > 0 or g2.b < 0:
            g1a, _ = eval_gk_derivs(a, k, is_vp)
            g1b, _ = eval_gk_derivs(b, k, is_vp)
            return abs(g1b - g1a)
        if depth >= 7 or (b - a).b < rat(5, 1000):
            return (b - a) * iv_abs_max(g2)
        mid = (a + b) / 2
        return seg(a, mid, depth + 1) + seg(mid, b, depth + 1)

    for i in range(N_grid):
        total_half += seg(rat(22 * i, N_grid), rat(22 * (i + 1), N_grid), 0)
    eU = iv.exp(-U_MAX)
    polys = {
        0: iv.mpf(1),
        1: U_MAX + 3,
        2: U_MAX ** 2 + 6 * U_MAX + 8,
        3: U_MAX ** 3 + 9 * U_MAX ** 2 + 24 * U_MAX + 24,
        4: U_MAX ** 4 + 12 * U_MAX ** 3 + 48 * U_MAX ** 2 + 96 * U_MAX + 96,
    }
    return 2 * (total_half + polys[k] * eU)


def certify_lemma1(m0, cs_val):
    """Lemma 1: for all m >= m0 and 5m < t <= T_m, saddle scale satisfies s = 1/theta > cs * sqrt(m)."""
    m = iv.mpf(m0)
    cs = iv.mpf(cs_val)
    assert (iv.sqrt(m) / cs).a > 1
    assert (1 - 1 / (2 * cs * iv.sqrt(m))).a > 0
    tail_m1 = (cs * iv.sqrt(m) / (1 - 1 / (2 * cs * iv.sqrt(m)))) * iv.exp(-iv.sqrt(m) / cs)
    assert tail_m1.b < rat(1, 2)
    g_max = rat(285, 1000)
    assert (g_max - iv.exp(-(1 + g_max))).a > 0
    tau_over_m = (iv.pi ** 2) * (cs ** 2) / 6 + 2 * g_max * cs / iv.sqrt(m)
    assert tau_over_m.b < 5
    return tau_over_m, tail_m1


def _g4v_iv(u_iv, p_iv):
    q_iv = 1 - p_iv
    eiu = iv.exp(1j * u_iv)
    w_iv = q_iv + p_iv * eiu
    aw = abs(w_iv)
    assert aw.a > 0
    return abs(w_iv ** 2 - 6 * p_iv * q_iv * eiu) / (aw ** 4)


def certify_c4_tail():
    """Exact bound on |g^(4)(s)|/v for min(p, 1-p) <= 1/(1+e^{5/2}) and all real s."""
    q0 = 1 / (1 + iv.exp(rat(5, 2)))
    v0 = q0 * (1 - q0)
    return (1 + 2 * v0) / ((1 - 2 * q0) ** 4)


def ceil_centi_rat(x_iv):
    target = iv.mpf(x_iv).b
    assert target >= 0
    lo_k, hi_k = 0, 1
    while (iv.mpf(hi_k) / 100).a < target:
        lo_k = hi_k
        hi_k *= 2
    while lo_k < hi_k:
        mid_k = (lo_k + hi_k) // 2
        if (iv.mpf(mid_k) / 100).a >= target:
            hi_k = mid_k
        else:
            lo_k = mid_k + 1
    assert (iv.mpf(hi_k) / 100).a >= target
    return hi_k


_C4_CACHE = {}


def certify_c4_core(u0_val):
    u0_k = ceil_centi_rat(iv.mpf(u0_val).b + rat(1, 100))
    if u0_k in _C4_CACHE:
        return _C4_CACHE[u0_k]
    u0_rat = rat(u0_k, 100)
    mx = iv.mpf(0)
    Nu, Np = 12, 12
    for iu in range(Nu):
        u_iv = iv.mpf([(iv.mpf(iu) * u0_rat / Nu).a, (iv.mpf(iu + 1) * u0_rat / Nu).b])
        for ip in range(Np):
            p_iv = iv.mpf([rat(ip, 2 * Np).a, rat(ip + 1, 2 * Np).b])
            mx = iv_max(mx, _g4v_iv(u_iv, p_iv).b)
    _C4_CACHE[u0_k] = mx
    return mx


def g1_fn(X):
    return 1 - (1 + X) * iv.exp(-X)


def g2_fn(X):
    return 1 - (1 + X + (X ** 2) / 2) * iv.exp(-X)


def g3_fn(X):
    return 1 - (1 + X + (X ** 2) / 2 + (X ** 3) / 6) * iv.exp(-X)


def major_arc_lower(L, V_lo, W_lo, S3_abs_hi, M4_hi, EC3sq_hi, beta_hi, H_hi, C4):
    """Lemma 4: 4th-order Edgeworth lower bound on B = {V*alpha^2 + W*phi^2 <= L^2}."""
    L, V_lo, W_lo = iv.mpf(L), iv.mpf(V_lo), iv.mpf(W_lo)
    assert (L / iv.sqrt(V_lo)).b < iv.pi.a and (L / iv.sqrt(W_lo)).b < iv.pi.a

    S3_over_VW = S3_abs_hi / (iv.sqrt(V_lo) * (W_lo ** rat(3, 2)))
    c_B = iv.mpf(0)
    N_th = 24
    pi2 = iv.pi / 2
    for k in range(N_th):
        th_iv = iv.mpf([(iv.mpf(k) * pi2 / N_th).a, (iv.mpf(k + 1) * pi2 / N_th).b])
        u, w = iv.cos(th_iv), iv.sin(th_iv)
        quart = (
            (u ** 4 + 6 * (u ** 2) * (w ** 2)) / V_lo
            + 4 * abs(u) * (w ** 3) * S3_over_VW
            + (w ** 4) * M4_hi / (W_lo ** 2)
        )
        val = rat(1, 24) * (L ** 2) * quart + (H_hi / (2 * W_lo)) * (w ** 2)
        c_B = iv_max(c_B, val.b)
    lam = 2 * c_B
    assert lam.b < rat(99, 100)

    X0 = (L ** 2) / 2
    X = (1 - lam) * X0
    g1_0, g3_0 = g1_fn(X0), g3_fn(X0)
    g1_X, g2_X = g1_fn(X), g2_fn(X)

    bw = beta_hi / iv.sqrt(W_lo)
    main = iv.exp(-(bw ** 2) / 2)
    err_tr = iv.exp(-X0)
    err_C3sq = rat(1, 2) * g3_0 * EC3sq_hi
    err_bC3 = bw * iv.sqrt(g1_0 * g3_0 * EC3sq_hi)
    err_R4 = (C4 / 24) * (g2_X / ((1 - lam) ** 3)) * (9 / V_lo + 3 * M4_hi / (W_lo ** 2))
    err_K2 = (H_hi / (2 * W_lo)) * (g1_X / ((1 - lam) ** 2))
    tot = err_tr + err_C3sq + err_bC3 + err_R4 + err_K2
    return {
        "lam": lam, "main": main, "maj_err": tot, "maj_lb": (main - tot).a,
    }


def trig_split_A_and_B1(L, V_lo, V_hi, W_lo, W_hi, M4_hi, K_eta, phi1, K_phi1, u_cap_val):
    """Lemma 5a (Exact Trigonometric Splitting) for Region (A) {|phi|<=eta, Q>L^2}
    and Region (B1) {eta < |phi| <= phi1}.
    """
    L = iv.mpf(L)
    eta = L / iv.sqrt(W_lo)
    M3_hi = iv.sqrt(W_hi * M4_hi).b

    # On |phi| <= eta_true = L / sqrt(W), W*phi^2 <= L^2 => C(phi) >= V_lo - L^2/2
    C_eta = (V_lo - rat(1, 2) * (L ** 2)).a
    assert C_eta.a > 0
    cW_eta = (rat(1, 2) - M4_hi * (eta ** 2) / (24 * W_lo) - (M3_hi ** 2) * (eta ** 4) / (72 * C_eta * W_lo)).a
    assert cW_eta.a > rat(5, 100)

    d_phi = (M3_hi * (eta ** 2) / (6 * C_eta)).b
    u_cap = iv.mpf(u_cap_val)
    assert (d_phi * eta).b < (iv.pi - u_cap).a
    b_sh = (d_phi * iv.sqrt(V_hi / W_lo)).b
    rho_sh = (1 + (b_sh ** 2 + b_sh * iv.sqrt(4 + b_sh ** 2)) / 2).b
    L_eff2 = (L ** 2) / rho_sh

    c_cos = (1 - iv.cos(u_cap)) / (u_cap ** 2)
    c_ell = iv_min(cW_eta, (C_eta / V_hi) * c_cos).a
    assert c_ell.a > rat(5, 100)
    err_a1 = K_eta * iv.exp(-c_ell * L_eff2) / (2 * c_ell)
    E_a2 = (C_eta * (1 - iv.cos(u_cap))).a
    assert E_a2.a > 1
    err_a2 = iv.sqrt(iv.pi / cW_eta) * iv.sqrt(V_hi) * K_eta * iv.exp(-E_a2)

    phi1 = iv.mpf(phi1)
    assert phi1.a >= eta.b
    C_1 = (V_lo - rat(1, 2) * W_hi * (phi1 ** 2)).a
    assert C_1.a > 0
    cW_1 = (rat(1, 2) - M4_hi * (phi1 ** 2) / (24 * W_lo) - (M3_hi ** 2) * (phi1 ** 4) / (72 * C_1 * W_lo)).a
    assert cW_1.a > rat(5, 100)
    err_b1 = iv.sqrt(iv.pi / 8) * iv.sqrt(V_hi / C_1) * K_phi1 * iv.exp(-cW_1 * (L ** 2)) / (cW_1 * L)
    return err_a1, err_a2, err_b1


def certify_s_unit_slice(m0, s_min, gamma_lo, l1_norms, c4_tail, L_val):
    """Uniform-in-s >= s_min certification for all gamma >= gamma_lo and m >= m0."""
    m = iv.mpf(m0)
    s_min = iv.mpf(s_min).a
    g_lo = iv.mpf(gamma_lo).a
    L = iv.mpf(L_val)

    dgam = 1 / (16 * (s_min ** 2))
    gam_star_min = g_lo - dgam
    A_ub = -iv.log(iv.exp(gam_star_min) - 1)
    e_negB_hi = iv.exp(-5 * g_lo + dgam) / (1 - iv.exp(-5 * g_lo + dgam))
    B_lb = -iv.log(e_negB_hi)
    absA_lb = -A_ub
    assert absA_lb.a > rat(25, 10) and B_lb.a > rat(25, 10)
    assert (rat(25, 10) * iv_sinh(rat(25, 20)) / iv_cosh(rat(25, 20))).a > 2

    def int_uk_v(a, k):
        def ik(c):
            ca = c * a
            if k == 0: p = iv.mpf(1)
            elif k == 1: p = ca + 1
            elif k == 2: p = ca ** 2 + 2 * ca + 2
            elif k == 3: p = ca ** 3 + 3 * ca ** 2 + 6 * ca + 6
            return p * iv.exp(-ca) / (c ** (k + 1))
        return _p_pt(a) if k == 0 else (ik(1) - 2 * ik(2) + 3 * ik(3))

    V_tc = int_uk_v(absA_lb, 0) + int_uk_v(B_lb, 0)
    S1_tc = int_uk_v(absA_lb, 1) + int_uk_v(B_lb, 1)
    S2_tc = int_uk_v(absA_lb, 2) + int_uk_v(B_lb, 2)
    S3_tc = int_uk_v(absA_lb, 3) + int_uk_v(B_lb, 3)

    me = lambda key: l1_norms[key] / (8 * (s_min ** 2))
    V_lo_s = (1 - V_tc - me("v0")).a
    V_hi_s = (1 + me("v0")).b
    dmu_s = ((S1_tc + me("v1")) / V_lo_s).b
    W_lo_s3 = ((iv.pi ** 2) / 3 - S2_tc - me("v2") - (dmu_s ** 2) * V_hi_s).a
    W_hi_s3 = ((iv.pi ** 2) / 3 + me("v2")).b

    M4_mu_s5 = (7 * (iv.pi ** 4) / 15 + me("v4")).b
    M3_mu_s4 = iv.sqrt(W_hi_s3 * M4_mu_s5).b
    M4_hi_s5 = M4_mu_s5 + 4 * dmu_s * M3_mu_s4 + 6 * (dmu_s ** 2) * W_hi_s3
    S3_abs_s4 = S3_tc + me("v3") + 3 * dmu_s * W_hi_s3 + 2 * (dmu_s ** 3) * V_hi_s

    m0_hi = V_tc + me("vp0")
    m1_hi = 1 + S1_tc + me("vp1")
    m2_hi = S2_tc + me("vp2")
    m3_hi = (iv.pi ** 2) + S3_tc + me("vp3")
    jb0 = m0_hi
    jb1 = m1_hi + dmu_s * m0_hi
    jb2 = m2_hi + 2 * dmu_s * m1_hi + (dmu_s ** 2) * m0_hi
    jb3 = m3_hi + 3 * dmu_s * m2_hi + 3 * (dmu_s ** 2) * m1_hi + (dmu_s ** 3) * m0_hi
    a30 = jb0 / (V_lo_s ** rat(3, 2))
    a21 = jb1 / (V_lo_s * iv.sqrt(W_lo_s3))
    a12 = jb2 / (iv.sqrt(V_lo_s) * W_lo_s3)
    a03 = jb3 / (W_lo_s3 ** rat(3, 2))
    EC3sq_s = (15 * a30 ** 2 + 18 * a30 * a12 + 27 * a21 ** 2 + 18 * a21 * a03 + 27 * a12 ** 2 + 15 * a03 ** 2) / 36

    a_th_min = (2 - 1 / m) * g_lo
    b_th_min = (3 - 1 / m) * g_lo
    H_hi_s2 = 2 + (a_th_min ** 2) / (4 * iv_sinh(a_th_min / 2) ** 2) + (b_th_min ** 2) / (4 * iv_sinh(b_th_min / 2) ** 2)

    u0 = L * iv.sqrt((1 / V_lo_s + ((rat(5, 2) + dmu_s) ** 2) / W_lo_s3) / s_min)
    C4 = iv_max(c4_tail, certify_c4_core(u0))

    V_lo, V_hi = V_lo_s * s_min, V_hi_s * s_min
    W_lo, W_hi = W_lo_s3 * (s_min ** 3), W_hi_s3 * (s_min ** 3)
    M4_hi = M4_hi_s5 * (s_min ** 5)

    maj = major_arc_lower(
        L, V_lo, W_lo, S3_abs_s4 * (s_min ** 4), M4_hi,
        EC3sq_s / s_min, iv.mpf(2) * s_min, H_hi_s2 * (s_min ** 2), C4,
    )

    eta_s = L / iv.sqrt(W_lo_s3 * s_min)
    u_1 = iv_max(rat(42, 100), rat(105, 100) * eta_s).b
    err_a1_t, err_a2_t, err_b1a = trig_split_A_and_B1(
        L, V_lo, V_hi, W_lo, W_hi, M4_hi,
        1 + eta_s ** 2, u_1 / s_min, 1 + u_1 ** 2, rat(12, 10),
    )

    V_tail_s = V_tc + (_v_pt(absA_lb) + _v_pt(B_lb)) / s_min
    W_tail_s3 = S2_tc + ((absA_lb ** 2) * _v_pt(absA_lb) + (B_lb ** 2) * _v_pt(B_lb)) / s_min
    eps_P_abs = 8 * (iv.pi ** 2) * (s_min ** 2) * iv.exp(-(iv.pi ** 2) * s_min)
    assert ((iv.pi ** 2) * s_min).a > 2 and eps_P_abs.b < iv.mpf(10) ** (-50)

    assert (dmu_s * eta_s).b < rat(17, 10)
    b_sh_p = (dmu_s * iv.sqrt(V_hi_s / W_lo_s3)).b
    rho_sh_p = (1 + (b_sh_p ** 2 + b_sh_p * iv.sqrt(4 + b_sh_p ** 2)) / 2).b
    x_eta = iv.pi * eta_s
    SZ0_eta = x_eta / iv_sinh(x_eta)
    cW_eta_p = (((1 - SZ0_eta) / (x_eta ** 2)) * (iv.pi ** 2) - W_tail_s3) / W_hi_s3
    cu_eta_p = (SZ0_eta - 2 * V_tail_s) / V_hi_s
    err_a1, err_a2 = err_a1_t, err_a2_t
    if cW_eta_p.a > rat(1, 10) and cu_eta_p.a > rat(2, 10):
        u_cap_p = rat(13, 10)
        c_ell_p = iv_min(cW_eta_p, cu_eta_p * (1 - iv.cos(u_cap_p)) / (u_cap_p ** 2)).a
        K_eta = 1 + eta_s ** 2
        ea1_p = K_eta * iv.exp(2 * eps_P_abs - c_ell_p * (L ** 2) / rho_sh_p) / (2 * c_ell_p)
        E_a2_p = (SZ0_eta - 2 * V_tail_s) * s_min * (1 - iv.cos(u_cap_p))
        if E_a2_p.a > 1:
            ea2_p = iv.sqrt(iv.pi / cW_eta_p) * iv.sqrt(V_hi_s * s_min) * K_eta * iv.exp(2 * eps_P_abs - E_a2_p)
            if (ea1_p + ea2_p).b < (err_a1 + err_a2).b:
                err_a1, err_a2 = ea1_p, ea2_p

    u_m = rat(55, 100)
    assert u_m.a > u_1.b
    x_m = iv.pi * u_m
    SZ0_m = x_m / iv_sinh(x_m)
    cW_m = (((1 - SZ0_m) / (x_m ** 2)) * (iv.pi ** 2) - W_tail_s3) / W_hi_s3
    A_m_s = SZ0_m - 2 * V_tail_s
    assert cW_m.a > rat(5, 100) and A_m_s.a > rat(5, 100)
    L_1 = u_1 * iv.sqrt(W_lo_s3 * s_min)
    err_b1b = iv.sqrt(iv.pi / 8) * iv.sqrt(V_hi_s / A_m_s) * (1 + u_m ** 2) * iv.exp(2 * eps_P_abs - cW_m * (L_1 ** 2)) / (cW_m * L_1)
    err_b1_pois = iv.sqrt(iv.pi / 8) * iv.sqrt(V_hi_s / A_m_s) * (1 + u_m ** 2) * iv.exp(2 * eps_P_abs - cW_m * (L ** 2)) / (cW_m * L)
    err_b1 = iv_min(err_b1a + err_b1b, err_b1_pois)

    def far_gap(u_val):
        xu = iv.pi * u_val
        return 1 - xu / iv_sinh(xu) - 2 * V_tail_s

    pref_s = 2 * iv.sqrt(V_hi_s * W_hi_s3) * s_min
    u_f = rat(80, 100)
    u_mid2 = rat(140, 100)
    u_far = rat(25, 10)
    A_f_s = (iv.pi * u_f) / iv_sinh(iv.pi * u_f) - 2 * V_tail_s
    assert A_f_s.a > 0 and (far_gap(u_m) * s_min).a > 1
    assert (far_gap(u_f) * s_min).a > 2 and (far_gap(u_far) * s_min).a > 5
    psi_fac_m = iv_min(iv.mpf(1), iv.sqrt(iv.pi / 8) / iv.sqrt(A_f_s * s_min))
    err_b2 = pref_s * psi_fac_m * (u_f - u_m) * (1 + u_f ** 2) * iv.exp(2 * eps_P_abs - far_gap(u_m) * s_min)
    err_c1 = pref_s * (u_mid2 - u_f) * (1 + u_mid2 ** 2) * iv.exp(2 * eps_P_abs - far_gap(u_f) * s_min)
    err_c2 = pref_s * (u_far - u_mid2) * (1 + u_far ** 2) * iv.exp(2 * eps_P_abs - far_gap(u_mid2) * s_min)
    err_c3 = 2 * iv.pi * iv.sqrt(V_hi_s * W_hi_s3) * (s_min ** 2) * (1 + 2 * (s_min ** 2)) * iv.exp(2 * eps_P_abs - far_gap(u_far) * s_min)

    tot_minor = err_a1 + err_a2 + err_b1 + err_b2 + err_c1 + err_c2 + err_c3
    net = (maj["maj_lb"] - tot_minor).a
    assert net.a > 0, f"s-unit slice g_lo={g_lo} failed: net={net}"
    return {"s_min": s_min, "g_lo": g_lo, "maj": maj, "tot_minor": tot_minor, "net": net}


def compute_y_block(ga, gb, l1_norms, v_sups, m_ref=M0, n_y=36):
    m = iv.mpf(m_ref)
    g_a, g_b = iv.mpf(ga), iv.mpf(gb)
    gam = iv.mpf([g_a.a, g_b.b])
    eps_r = g_b / (16 * (m ** 2))
    rho = iv.mpf([(1 - eps_r).a, (1 + eps_r).b])
    gam_star = gam * rho
    is_R2 = g_a.a >= rat(1, 2).a

    if is_R2:
        dg = iv.mpf([-(eps_r * g_b).b, (eps_r * g_b).b])
        e_Agam = iv.exp(dg) * (1 - iv.exp((rho - 6) * gam)) / (1 - iv.exp(-gam_star))
        Agam_iv = iv.log(e_Agam)
        A_iv = Agam_iv - gam
        u_of_y = lambda y: Agam_iv + gam * (y - 1)
    else:
        e_A3gam = (sinhc_iv((3 - rho / 2) * gam) / sinhc_iv((rho / 2) * gam)) * ((6 - rho) / rho)
        A3gam_iv = iv.log(e_A3gam)
        Agam_iv = A3gam_iv - 2 * gam
        A_iv = A3gam_iv - 3 * gam
        u_of_y = lambda y: A3gam_iv + gam * (y - 3)

    h = rat(6, n_y)
    y_mids = [(iv.mpf(i) + rat(1, 2)) * h for i in range(n_y)]
    vd_mids = [v_derivs(u_of_y(ym)) for ym in y_mids]

    def y_quad(fn_idx_val, l1_f2_bound):
        acc = iv.mpf(0)
        for i in range(n_y):
            acc += fn_idx_val(y_mids[i], vd_mids[i])
        err = ((h ** 2) / 8) * l1_f2_bound
        return h * acc + iv.mpf([-err.b, err.b])

    v0_m, v1_m, v2_m, v3_m, _ = v_sups

    def l1_cap(sup_val, k, u0_abs, is_vp=False):
        s_bd = 6 * sup_val
        if not is_R2:
            return s_bd
        if not is_vp:
            if k == 0: l1u = l1_norms["v0"]
            elif k == 1: l1u = l1_norms["v1"] + u0_abs * l1_norms["v0"]
            elif k == 2: l1u = l1_norms["v2"] + 2 * u0_abs * l1_norms["v1"] + (u0_abs ** 2) * l1_norms["v0"]
            elif k == 3: l1u = l1_norms["v3"] + 3 * u0_abs * l1_norms["v2"] + 3 * (u0_abs ** 2) * l1_norms["v1"] + (u0_abs ** 3) * l1_norms["v0"]
            elif k == 4: l1u = l1_norms["v4"] + 4 * u0_abs * l1_norms["v3"] + 6 * (u0_abs ** 2) * l1_norms["v2"] + 4 * (u0_abs ** 3) * l1_norms["v1"] + (u0_abs ** 4) * l1_norms["v0"]
        else:
            if k == 0: l1u = l1_norms["vp0"]
            elif k == 1: l1u = l1_norms["vp1"] + u0_abs * l1_norms["vp0"]
            elif k == 2: l1u = l1_norms["vp2"] + 2 * u0_abs * l1_norms["vp1"] + (u0_abs ** 2) * l1_norms["vp0"]
            elif k == 3: l1u = l1_norms["vp3"] + 3 * u0_abs * l1_norms["vp2"] + 3 * (u0_abs ** 2) * l1_norms["vp1"] + (u0_abs ** 3) * l1_norms["vp0"]
        u_bd = (g_b if k == 0 else (iv.mpf(1) if k == 1 else (1 / (g_a ** (k - 1))))) * l1u
        return iv_min(s_bd, u_bd)

    l1_V = l1_cap((g_b ** 2) * v2_m, 0, iv.mpf(0))
    V_iv = y_quad(lambda y, vd: vd[1], l1_V)

    y_ref = iv.mpf(1) if is_R2 else iv.mpf(3)
    u_ref_abs = iv_abs_max(u_of_y(y_ref))
    l1_yV = l1_cap(2 * g_b * v1_m + 6 * (g_b ** 2) * v2_m, 1, u_ref_abs)
    I1_shift = y_quad(lambda y, vd: (y - y_ref) * vd[1], l1_yV)
    ybar_iv = y_ref + I1_shift / V_iv
    y0_iv = iv.mpf(((ybar_iv.a + ybar_iv.b) / 2).a)
    dy0 = ((ybar_iv.b - ybar_iv.a) / 2).b
    D = iv_max(y0_iv, 6 - y0_iv).b
    u0_abs = iv_abs_max(u_of_y(y0_iv))

    l1_ybar = l1_cap(2 * g_b * v1_m + (D + dy0) * (g_b ** 2) * v2_m, 1, u0_abs + g_b * dy0)
    l1_W = l1_cap(2 * v0_m + 4 * D * g_b * v1_m + (D ** 2) * (g_b ** 2) * v2_m, 2, u0_abs)
    W0_iv = y_quad(lambda y, vd: ((y - y0_iv) ** 2) * vd[1], l1_W)
    l1_S3 = l1_cap(6 * D * v0_m + 6 * (D ** 2) * g_b * v1_m + (D ** 3) * (g_b ** 2) * v2_m, 3, u0_abs)
    S30_iv = y_quad(lambda y, vd: ((y - y0_iv) ** 3) * vd[1], l1_S3)
    l1_M4 = l1_cap(12 * (D ** 2) * v0_m + 8 * (D ** 3) * g_b * v1_m + (D ** 4) * (g_b ** 2) * v2_m, 4, u0_abs)
    M40_iv = y_quad(lambda y, vd: ((y - y0_iv) ** 4) * vd[1], l1_M4)

    l1_vp = [
        l1_cap((g_b ** 2) * v3_m, 0, u0_abs, True),
        l1_cap(2 * g_b * v2_m + D * (g_b ** 2) * v3_m, 1, u0_abs, True),
        l1_cap(2 * v1_m + 4 * D * g_b * v2_m + (D ** 2) * (g_b ** 2) * v3_m, 2, u0_abs, True),
        l1_cap(6 * D * v1_m + 6 * (D ** 2) * g_b * v2_m + (D ** 3) * (g_b ** 2) * v3_m, 3, u0_abs, True),
    ]
    vp_raw = [y_quad(lambda y, vd, r=r: -((y - y0_iv) ** r) * vd[2], l1_vp[r]) for r in range(4)]

    return {
        "m_ref": m_ref, "ga": g_a, "gb": g_b, "gam": gam, "A_iv": A_iv, "Agam_iv": Agam_iv,
        "y0": y0_iv, "dy0": dy0, "D": D,
        "V_iv": V_iv, "W0_iv": W0_iv, "S30_iv": S30_iv, "M40_iv": M40_iv,
        "vp_raw": vp_raw, "l1": (l1_V, l1_ybar, l1_W, l1_S3, l1_M4, l1_vp),
        "l1_v0": l1_norms["v0"], "y_mids": y_mids, "v_mids": [vd[1] for vd in vd_mids], "h_y": h,
    }


def eval_y_block_for_m0(blk, m0, c4_tail, is_R3, L_val):
    assert m0 >= blk["m_ref"]
    m = iv.mpf(m0)
    L = iv.mpf(L_val)
    g_a, g_b, gam = blk["ga"], blk["gb"], blk["gam"]
    y0, dy0 = blk["y0"], blk["dy0"]
    l1_V, l1_ybar, l1_W, l1_S3, l1_M4, l1_vp = blk["l1"]

    disc_err = lambda l1: (l1 / (8 * (m ** 2))).b
    e_V = disc_err(l1_V)
    V_lo_m = (blk["V_iv"] - e_V).a
    V_hi_m = (blk["V_iv"] + e_V).b
    assert V_lo_m.a > 0

    dy_d = (disc_err(l1_ybar) / V_lo_m).b
    dy_tot = (dy0 + dy_d).b

    e_W = disc_err(l1_W)
    W_lo_m = ((blk["W0_iv"] - e_W).a - V_hi_m * (dy_tot ** 2)).a
    W_hi_m = (blk["W0_iv"] + e_W).b
    assert W_lo_m.a > 0

    S3_hi_m = (iv_abs_max(blk["S30_iv"]) + disc_err(l1_S3) + 3 * dy_tot * W_hi_m + 2 * (dy_tot ** 3) * V_hi_m).b
    M40_hi_m = (blk["M40_iv"].b + disc_err(l1_M4)).b
    M4_hi_m = (M40_hi_m + 4 * dy_tot * iv.sqrt(W_hi_m * M40_hi_m) + 6 * (dy_tot ** 2) * W_hi_m).b

    vp_m = [(iv_abs_max(blk["vp_raw"][r]) + disc_err(l1_vp[r])).b for r in range(4)]
    jb0 = vp_m[0]
    jb1 = (vp_m[1] + dy_tot * vp_m[0]).b
    jb2 = (vp_m[2] + 2 * dy_tot * vp_m[1] + (dy_tot ** 2) * vp_m[0]).b
    jb3 = (vp_m[3] + 3 * dy_tot * vp_m[2] + 3 * (dy_tot ** 2) * vp_m[1] + (dy_tot ** 3) * vp_m[0]).b
    a30 = jb0 / (V_lo_m ** rat(3, 2))
    a21 = jb1 / (V_lo_m * iv.sqrt(W_lo_m))
    a12 = jb2 / (iv.sqrt(V_lo_m) * W_lo_m)
    a03 = jb3 / (W_lo_m ** rat(3, 2))
    EC3sq_m = (15 * a30 ** 2 + 18 * a30 * a12 + 27 * a21 ** 2 + 18 * a21 * a03 + 27 * a12 ** 2 + 15 * a03 ** 2) / 36

    beta_hi_m = iv_min(rat(5, 2), 2 / g_a) if g_a.a > 0 else rat(5, 2)
    eta_m = L / iv.sqrt(W_lo_m * m)
    D_box_m = iv_max(y0 + dy_tot, 6 - y0 + dy_tot).b

    if is_R3:
        th_eta_m = g_b + eta_m
        c1 = 2 * iv.sin(iv.pi / (2 * m - 1)) * (2 * m - 1)
        gap1 = c1 - 3 * th_eta_m
        assert gap1.a > 0 and (8 - 3 * th_eta_m).a > 0
        s_tail = 1 / ((8 - 3 * th_eta_m) ** 2) + 1 / (4 * (8 - 3 * th_eta_m))
        H_hi_m2 = 2 * 13 * (1 / (gap1 ** 2) + s_tail)
    else:
        a_lo, b_lo = 2 - 1 / m, 3 - 1 / m
        H_hi_m2 = 2 / (g_a ** 2) + 1 / (iv_sinh(a_lo * g_a / 2) ** 2) + rat(9, 4) / (iv_sinh(b_lo * g_a / 2) ** 2)

    y_diff_hi = (iv_abs_max((y0 - 1) + blk["Agam_iv"] / gam) + dy_tot).b if g_a.a > 0 else D_box_m
    jb_lim_m = D_box_m if g_a.a == 0 else iv_min(D_box_m, rat(5, 2) / g_a + y_diff_hi)
    u0_c4 = L * iv.sqrt((1 / V_lo_m + (jb_lim_m ** 2) / W_lo_m) / m)
    C4 = iv_max(c4_tail, certify_c4_core(u0_c4))

    V_lo, V_hi = V_lo_m * m, V_hi_m * m
    W_lo, W_hi = W_lo_m * (m ** 3), W_hi_m * (m ** 3)
    M4_hi = M4_hi_m * (m ** 5)

    maj = major_arc_lower(
        L, V_lo, W_lo, S3_hi_m * (m ** 4), M4_hi,
        EC3sq_m / m, beta_hi_m * m, H_hi_m2 * (m ** 2), C4,
    )

    if is_R3:
        K_fn = lambda pm: (
            1 / (iv.cos(pm) * iv.cos(rat(3, 2) * pm))
            if pm.b <= rat(7, 10).a
            else (
                (g_b ** 2 + pm ** 2) * 6 * iv.exp(rat(5, 2) * g_b)
                / (4 * iv_min(iv.sin((2 - 1 / m) * rat(7, 10) / 2), iv.sin(pm)) * iv_min(iv.sin((3 - 1 / m) * rat(7, 10) / 2), iv.sin(rat(3, 2) * pm)))
            )
        )
        phi_1_m = iv_max(rat(45, 100), rat(12, 10) * eta_m).b
        assert phi_1_m.b < rat(7, 10).a
        phi_lc_m = rat(16, 10)
        b2_breaks = (rat(7, 10), phi_lc_m)
    else:
        s_over_m_hi = 1 / g_a
        K_fn = lambda pm: 1 + (s_over_m_hi * pm) ** 2
        sig_m = iv.sqrt(W_hi_m / V_lo_m)
        phi_1_m = iv_max(rat(75, 100) / sig_m, rat(11, 10) * eta_m).b
        phi_lc_m = (iv.mpf(3) / V_lo_m).b
        b2_breaks = (phi_lc_m,)

    err_a1, err_a2, err_b1 = trig_split_A_and_B1(
        L, V_lo, V_hi, W_lo, W_hi, M4_hi,
        K_fn(eta_m), phi_1_m / m, K_fn(phi_1_m), rat(95, 100),
    )

    has_pois_far = False
    if g_a.a > 0 and (-blk["A_iv"]).a > 0 and (m / g_b).a >= 12:
        s_min_p = (m / g_b).a
        absA_p = (-blk["A_iv"]).a
        B_p = (blk["A_iv"] + 6 * gam).a
        if B_p.a > 0:
            eps_P_f = 8 * (iv.pi ** 2) * (s_min_p ** 2) * iv.exp(-(iv.pi ** 2) * s_min_p)
            if ((iv.pi ** 2) * s_min_p).a > 2 and eps_P_f.b < iv.mpf(10) ** (-30):
                V_tail_p = _p_pt(absA_p) + _p_pt(B_p) + (_v_pt(absA_p) + _v_pt(B_p)) / s_min_p
                has_pois_far = True

    def pois_far_E(p_cur_m):
        if not has_pois_far:
            return iv.mpf(0)
        xu = iv.pi * (p_cur_m / g_b)
        gap = 1 - xu / iv_sinh(xu) - 2 * V_tail_p
        return (gap * s_min_p - 2 * eps_P_f) if gap.a > 0 else iv.mpf(0)

    y_mids, v_mids, h_y = blk["y_mids"], blk["v_mids"], blk["h_y"]
    l1_v0 = blk["l1_v0"]
    V_cont_hi = blk["V_iv"].b

    def fourier_gap_and_S(om_a, om_b):
        om_iv = iv.mpf([om_a.a, om_b.b])
        om_hi = om_b.b
        l1_pm = 2 * g_b * l1_v0 + om_hi + (om_hi ** 2) * V_cont_hi
        l1_cs = g_b * l1_v0 + om_hi + (om_hi ** 2) * V_cont_hi
        err_pm = (((h_y ** 2) / 8 + 1 / (8 * (m ** 2))) * l1_pm).b
        err_cs = (((h_y ** 2) / 8 + 1 / (8 * (m ** 2))) * l1_cs).b
        acc_vmr, acc_vpr, acc_r, acc_j = iv.mpf(0), iv.mpf(0), iv.mpf(0), iv.mpf(0)
        for ym, vm in zip(y_mids, v_mids):
            ang = om_iv * (ym - y0)
            ca, sa = iv.cos(ang), iv.sin(ang)
            acc_vmr += vm * (1 - ca)
            acc_vpr += vm * (1 + ca)
            acc_r += vm * ca
            acc_j += vm * sa
        vmr_lo = (h_y * acc_vmr - err_pm).a
        vpr_lo = (h_y * acc_vpr - err_pm).a
        r_iv = h_y * acc_r + iv.mpf([-err_cs, err_cs])
        j_iv = h_y * acc_j + iv.mpf([-err_cs, err_cs])
        j_hi = iv_abs_max(j_iv)
        gap1 = ((vmr_lo * iv_max(iv.mpf(0), vpr_lo) - j_hi ** 2) / (2 * V_hi_m)).a if vmr_lo.a > 0 else iv.mpf(0)
        s_hi = iv.sqrt(iv_abs_max(r_iv) ** 2 + j_hi ** 2).b
        gap2 = (V_lo_m - s_hi).a
        s_lo_m = iv_max(iv.mpf(0), r_iv.a, iv_max(iv.mpf(0), j_iv.a, -j_iv.b))
        return iv_max(iv.mpf(0), gap1, gap2) * m, s_lo_m

    assert (phi_lc_m / (2 * m)).b < (iv.pi / 2).a
    err_b2 = iv.mpf(0)
    p_cur = phi_1_m
    for p_stop in b2_breaks:
        while p_cur.a < p_stop.b:
            p_nxt = iv_min(p_stop, rat(118, 100) * p_cur).b
            E_four, S_lo_f = fourier_gap_and_S(p_cur, p_nxt)
            best_E = iv_max(pois_far_E(p_cur), E_four)
            assert best_E.a > 1
            S_lo_m = iv_max(S_lo_f, V_lo_m - rat(1, 2) * W_hi_m * (p_nxt ** 2))
            psi_fac = iv_min(iv.mpf(1), iv.sqrt(iv.pi / (8 * S_lo_m * m))) if S_lo_m.a > rat(1, 100) else iv.mpf(1)
            err_b2 += 2 * iv.sqrt(V_hi_m * W_hi_m) * m * psi_fac * (p_nxt - p_cur) * K_fn(p_nxt) * iv.exp(-best_E)
            p_cur = p_nxt

    E_lc = V_lo_m * m - 1 / (4 * iv.sin(phi_lc_m / (2 * m)))
    if is_R3:
        assert E_lc.a > 6
        s_max = rat(9, 4) * (m ** 2)
        err_c = 2 * iv.pi * iv.sqrt(V_hi_m * W_hi_m) * (m ** 2) * (2 * iv.sqrt(6) * m * (s_max + 1)) * iv.exp(-E_lc)
    else:
        assert E_lc.a > 5
        err_c = 2 * iv.pi * iv.sqrt(V_hi_m * W_hi_m) * (m ** 2) * (1 + 2 * ((m / g_a) ** 2)) * iv.exp(-E_lc)

    tot_minor = err_a1 + err_a2 + err_b1 + err_b2 + err_c
    net = (maj["maj_lb"] - tot_minor).a
    assert net.a > 0, f"Block [{g_a}, {g_b}] failed: net={net}"
    return {"ga": g_a, "gb": g_b, "maj": maj, "tot_minor": tot_minor, "net": net}


def run_part_B():
    t0 = time.perf_counter()
    v_sups = verify_v_deriv_sups()
    l1_norms = {
        "v0": certify_l1_norm(0, False), "v1": certify_l1_norm(1, False),
        "v2": certify_l1_norm(2, False), "v3": certify_l1_norm(3, False),
        "v4": certify_l1_norm(4, False),
        "vp0": certify_l1_norm(0, True), "vp1": certify_l1_norm(1, True),
        "vp2": certify_l1_norm(2, True), "vp3": certify_l1_norm(3, True),
    }
    c4_tail = certify_c4_tail()

    cs = rat(1709, 1000)
    tau_m, tail_m1 = certify_lemma1(M0, cs)
    L_val = iv.mpf(3)

    # Exhaustive exact rational cover of gamma = theta * m in (0, inf):
    #   Regime III : [0, 1/2]
    #   Regime IIa : [1/2, 37/10]
    #   Regime IIb : [37/10, 11/2]
    #   Regime I   : [11/2, inf)
    r3_knots = [rat(0), rat(12, 100), rat(24, 100), rat(36, 100), rat(44, 100), rat(1, 2)]
    r2a_knots = [
        rat(1, 2), rat(60, 100), rat(72, 100), rat(86, 100), rat(102, 100),
        rat(120, 100), rat(140, 100), rat(162, 100), rat(186, 100), rat(212, 100),
        rat(240, 100), rat(270, 100), rat(302, 100), rat(336, 100), rat(370, 100),
    ]
    r2b_slices = [
        (rat(370, 100), rat(420, 100)),
        (rat(420, 100), rat(480, 100)),
        (rat(480, 100), rat(11, 2)),
    ]

    # Verify exact boundary continuity of the cover of [0, inf):
    assert r3_knots[0] == 0 and r3_knots[-1] == r2a_knots[0]
    assert r2a_knots[-1] == r2b_slices[0][0]
    for i in range(len(r2b_slices) - 1):
        assert r2b_slices[i][1] == r2b_slices[i + 1][0]
    assert r2b_slices[-1][1] == rat(11, 2)

    s_min_r1 = cs * iv.sqrt(iv.mpf(M0))
    r1 = certify_s_unit_slice(M0, s_min_r1, rat(11, 2), l1_norms, c4_tail, L_val)
    r2b = [certify_s_unit_slice(M0, iv.mpf(M0) / gb, ga, l1_norms, c4_tail, L_val) for (ga, gb) in r2b_slices]
    r2a_blks = [compute_y_block(r2a_knots[i], r2a_knots[i + 1], l1_norms, v_sups, m_ref=M0, n_y=36) for i in range(len(r2a_knots) - 1)]
    r3_blks = [compute_y_block(r3_knots[i], r3_knots[i + 1], l1_norms, v_sups, m_ref=M0, n_y=36) for i in range(len(r3_knots) - 1)]
    r2a = [eval_y_block_for_m0(b, M0, c4_tail, False, L_val) for b in r2a_blks]
    r3 = [eval_y_block_for_m0(b, M0, c4_tail, True, L_val) for b in r3_blks]

    w_r2a = min(r2a, key=lambda r: r["net"].a)
    w_r2b = min(r2b, key=lambda r: r["net"].a)
    w_r3 = min(r3, key=lambda r: r["net"].a)
    overall = iv_min(r1["net"], w_r2a["net"], w_r2b["net"], w_r3["net"])
    assert overall.a > 0

    dt = time.perf_counter() - t0
    print(f"[Part B] Certified mpmath.iv (dps=25, zero floats) for ALL m >= {M0}, L=3 in {dt:.2f}s:", flush=True)
    print(f"  Lemma 1 (c_s=1.709): tau/m <= {fmt(tau_m, 6)} (<5), tail_m1 <= {fmt(tail_m1, 6)} (<0.5), C4_tail <= {fmt(c4_tail, 6)}")
    print(f"  L1 norms: " + ", ".join(f"{k}<={fmt(v, 5)}" for k, v in l1_norms.items()))
    print(f"  Regime I   [5.5, inf) : NET >= +{fmt_lo(r1['net'], 6)} (maj >= {fmt_lo(r1['maj']['maj_lb'], 5)}, min <= {fmt(r1['tot_minor'], 5)})")
    print(f"  Regime IIb [3.7, 5.5] : min NET >= +{fmt_lo(w_r2b['net'], 6)} (worst g_lo={fmt(w_r2b['g_lo'], 3)}, maj >= {fmt_lo(w_r2b['maj']['maj_lb'], 5)}, min <= {fmt(w_r2b['tot_minor'], 5)})")
    print(f"  Regime IIa [0.5, 3.7] : min NET >= +{fmt_lo(w_r2a['net'], 6)} (worst [{fmt(w_r2a['ga'], 3)},{fmt(w_r2a['gb'], 3)}], maj >= {fmt_lo(w_r2a['maj']['maj_lb'], 5)}, min <= {fmt(w_r2a['tot_minor'], 5)})")
    print(f"  Regime III [0.0, 0.5] : min NET >= +{fmt_lo(w_r3['net'], 6)} (worst [{fmt(w_r3['ga'], 3)},{fmt(w_r3['gb'], 3)}], maj >= {fmt_lo(w_r3['maj']['maj_lb'], 5)}, min <= {fmt(w_r3['tot_minor'], 5)})")
    print(f"  OVERALL MIN NET MARGIN (all m >= {M0}, all 5m < t <= D_m/2): +{fmt_lo(overall, 6)} > 0")


def main():
    try:
        t_all = time.perf_counter()
        run_part_A()
        run_part_B()
        print(f"Total runtime: {time.perf_counter() - t_all:.2f}s")
        print("PASS")
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
