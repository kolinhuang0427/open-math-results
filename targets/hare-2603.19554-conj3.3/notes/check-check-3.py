#!/usr/bin/env python3
"""Independent verifier for Hare-Hichri (arXiv:2603.19554v1) Conjecture 3.3 (conj:1).

Written solely from the primary source v6.tex and PROOF.md without reading verify.py or notes/.
Part 1: Pure Python arbitrary-precision integer fixed-point interval arithmetic
        (SCALE = 2^140, zero floats) for all 4 <= d <= 499 and all k >= 1.
Part 2: Rigorous mpmath.iv (iv.dps = 50) verification of all analytic lemmas and
        constants in Section 3 for d >= 500, plus full-k spot checks at d in {500, 501, 600, 1000}.
"""

from __future__ import annotations

import sys
import mpmath as mp
from mpmath import iv

iv.dps = 50

# =============================================================================
# Part 1: Pure integer fixed-point interval arithmetic (ZERO floats)
# =============================================================================
BITS = 140
S = 1 << BITS
ROUCHE_BITS = 40  # radius r = 2^(ROUCHE_BITS - BITS) = 2^-100
R_INT = 1 << ROUCHE_BITS

# Exact integer brackets for ln(2) and 2*pi at precision 2^140
# Computed from integer series in pure int arithmetic (no floats!)
def int_atan_recip(m: int, shift_bits: int) -> int:
    """Compute floor(2^shift_bits * atan(1/m)) and return (lo, hi) within +-2."""
    # Machin / Taylor series: atan(1/m) = sum_{k>=0} (-1)^k / ((2k+1) m^(2k+1))
    scale = 1 << shift_bits
    term = scale // m
    acc_lo = 0
    acc_hi = 0
    k = 0
    m2 = m * m
    while term > 0:
        d = 2 * k + 1
        q = term // d
        if k % 2 == 0:
            acc_lo += q
            acc_hi += q + 1
        else:
            acc_lo -= q + 1
            acc_hi -= q
        term = term // m2
        k += 1
    return acc_lo, acc_hi

def compute_pi_ln2_brackets() -> tuple[tuple[int, int], tuple[int, int]]:
    guard = 16
    sh = BITS + guard
    # pi = 16*atan(1/5) - 4*atan(1/239)
    a5_lo, a5_hi = int_atan_recip(5, sh)
    a239_lo, a239_hi = int_atan_recip(239, sh)
    pi_lo = (16 * a5_lo - 4 * a239_hi) >> guard
    pi_hi = ((16 * a5_hi - 4 * a239_lo) >> guard) + 1
    # ln(2) = 2 * sum_{k>=0} 1 / ((2k+1) * 3^(2k+1))
    scale = 1 << sh
    term = scale // 3
    ln2_lo = 0
    ln2_hi = 0
    k = 0
    while term > 0:
        d = 2 * k + 1
        q = term // d
        ln2_lo += 2 * q
        ln2_hi += 2 * (q + 1)
        term = term // 9
        k += 1
    return (pi_lo, pi_hi), (ln2_lo >> guard, (ln2_hi >> guard) + 1)

PI_IV, LN2_IV = compute_pi_ln2_brackets()
TWO_PI_IV = (2 * PI_IV[0], 2 * PI_IV[1])

def isqrt_ceil(n: int) -> int:
    if n <= 0:
        return 0
    r = int(n).bit_length()
    x = 1 << ((r + 1) // 2)
    while True:
        y = (x + n // x) >> 1
        if y >= x:
            break
        x = y
    if x * x < n:
        x += 1
    return x

def isqrt_floor(n: int) -> int:
    if n <= 0:
        return 0
    import math
    return math.isqrt(n)

def iv_mul(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    al, ah = a
    bl, bh = b
    prods = (al * bl, al * bh, ah * bl, ah * bh)
    lo = min(prods) // S
    hi = (max(prods) + S - 1) // S
    return (lo, hi)

def iv_add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])

def iv_sub(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] - b[1], a[1] - b[0])

def iv_abs(a: tuple[int, int]) -> tuple[int, int]:
    al, ah = a
    if al >= 0:
        return (al, ah)
    if ah <= 0:
        return (-ah, -al)
    return (0, max(-al, ah))

def c_mul_exact_scaled(z1: tuple[int, int], z2: tuple[int, int]) -> tuple[int, int]:
    """Multiply two point-centers scaled by S, rounding to nearest int."""
    x1, y1 = z1
    x2, y2 = z2
    return ((x1 * x2 - y1 * y2) // S, (x1 * y2 + y1 * x2) // S)

def c_iv_mul(z1: tuple[tuple[int, int], tuple[int, int]],
             z2: tuple[tuple[int, int], tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    x1, y1 = z1
    x2, y2 = z2
    re = iv_sub(iv_mul(x1, x2), iv_mul(y1, y2))
    im = iv_add(iv_mul(x1, y2), iv_mul(y1, x2))
    return (re, im)

def c_iv_norm2(z: tuple[tuple[int, int], tuple[int, int]]) -> tuple[int, int]:
    x, y = z
    ax = iv_abs(x)
    ay = iv_abs(y)
    lo = (ax[0] * ax[0] + ay[0] * ay[0]) // S
    hi = (ax[1] * ax[1] + ay[1] * ay[1] + S - 1) // S
    return (lo, hi)

def c_iv_abs(z: tuple[tuple[int, int], tuple[int, int]]) -> tuple[int, int]:
    x, y = z
    ax = iv_abs(x)
    ay = iv_abs(y)
    lo = isqrt_floor(ax[0] * ax[0] + ay[0] * ay[0])
    hi = isqrt_ceil(ax[1] * ax[1] + ay[1] * ay[1])
    return (lo, hi)

def find_initial_z0(d: int) -> tuple[int, int]:
    """Pure integer Taylor series for exp((ln 2 + 2*pi*i)/d) at scale S."""
    re = ((LN2_IV[0] + LN2_IV[1]) // 2) // d
    im = ((TWO_PI_IV[0] + TWO_PI_IV[1]) // 2) // d
    # exp(z) = sum_{j=0}^{30} z^j / j!
    sum_re, sum_im = S, 0
    term_re, term_im = S, 0
    for j in range(1, 35):
        nr = (term_re * re - term_im * im) // (S * j)
        ni = (term_re * im + term_im * re) // (S * j)
        term_re, term_im = nr, ni
        sum_re += term_re
        sum_im += term_im
        if abs(term_re) <= 1 and abs(term_im) <= 1:
            break
    return (sum_re, sum_im)

def newton_refine_gamma(d: int, z0: tuple[int, int]) -> tuple[int, int]:
    """Refine root z_* of z^d - z - 1 = 0 using pure integer arithmetic."""
    zr, zi = z0
    for _ in range(10):
        # Compute z^{d-1} via binary exponentiation at scale S
        pr, pi = S, 0
        br, bi = zr, zi
        e = d - 1
        while e > 0:
            if e & 1:
                pr, pi = (pr * br - pi * bi) // S, (pr * bi + pi * br) // S
            e >>= 1
            if e > 0:
                br, bi = (br * br - bi * bi) // S, (2 * br * bi) // S
        # z^d = z^{d-1} * z
        zdr = (pr * zr - pi * zi) // S
        zdi = (pr * zi + pi * zr) // S
        fr, fi = zdr - zr - S, zdi - zi
        dpr, dpi = d * pr - S, d * pi
        den = (dpr * dpr + dpi * dpi) // S
        if den == 0:
            break
        # step = f / df
        sr = (fr * dpr + fi * dpi) // den
        si = (fi * dpr - fr * dpi) // den
        zr -= sr
        zi -= si
        if abs(sr) <= 2 and abs(si) <= 2:
            break
    return (zr, zi)

def certify_beta(d: int) -> tuple[int, int]:
    """Certify beta_d in (b_lo, b_hi) by pure integer bisection and P_d sign checks."""
    lo = S + 1
    hi = 2 * S
    for _ in range(125):
        mid = (lo + hi) >> 1
        if mid == lo or mid == hi:
            break
        # P_d(mid/S) = (mid/S)^d - mid/S - 1
        p_iv = (mid, mid)
        acc = (S, S)
        base = p_iv
        e = d
        while e > 0:
            if e & 1:
                acc = iv_mul(acc, base)
            e >>= 1
            if e > 0:
                base = iv_mul(base, base)
        val = iv_sub(iv_sub(acc, p_iv), (S, S))
        if val[1] < 0:
            lo = mid
        elif val[0] > 0:
            hi = mid
        else:
            break
    # Final rigorous check: P_d(lo) < 0 and P_d(hi) > 0
    def eval_Pd_real(pt: int) -> tuple[int, int]:
        acc = (S, S)
        base = (pt, pt)
        e = d
        while e > 0:
            if e & 1:
                acc = iv_mul(acc, base)
            e >>= 1
            if e > 0:
                base = iv_mul(base, base)
        return iv_sub(iv_sub(acc, (pt, pt)), (S, S))

    assert eval_Pd_real(lo)[1] < 0, f"beta_d lower check failed at d={d}"
    assert eval_Pd_real(hi)[0] > 0, f"beta_d upper check failed at d={d}"
    assert hi > lo > S
    return (lo, hi)

def certify_gamma_rouche(d: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Certify unique root gamma_d in |z - z_*| < r = 2^-100, Im(gamma_d) > 0."""
    z_init = find_initial_z0(d)
    zr, zi = newton_refine_gamma(d, z_init)
    assert zi > R_INT, f"Im(z_*) <= r at d={d}"

    z_pt = ((zr, zr), (zi, zi))
    # Compute z_*^{d-1} in complex interval arithmetic
    zm1 = ((S, S), (0, 0))
    base = z_pt
    e = d - 1
    while e > 0:
        if e & 1:
            zm1 = c_iv_mul(zm1, base)
        e >>= 1
        if e > 0:
            base = c_iv_mul(base, base)
    zd = c_iv_mul(zm1, z_pt)
    f_val = (iv_sub(iv_sub(zd[0], z_pt[0]), (S, S)), iv_sub(zd[1], z_pt[1]))
    df_val = (iv_sub((d * zm1[0][0], d * zm1[0][1]), (S, S)), (d * zm1[1][0], d * zm1[1][1]))

    abs_f_hi = c_iv_abs(f_val)[1]
    abs_df_lo = c_iv_abs(df_val)[0]
    abs_z_hi = c_iv_abs(z_pt)[1]

    # Upper bound on (|z_*| + r)^{d-2}
    r_plus = abs_z_hi + R_INT
    pow_up = (S, S)
    base_up = (r_plus, r_plus)
    e2 = d - 2
    while e2 > 0:
        if e2 & 1:
            pow_up = iv_mul(pow_up, base_up)
        e2 >>= 1
        if e2 > 0:
            base_up = iv_mul(base_up, base_up)

    # Check |P'(z_*)| * r > |P(z_*)| + d*(d-1)/2 * r^2 * (|z_*|+r)^{d-2}
    r_iv = (R_INT, R_INT)
    lhs = iv_mul((abs_df_lo, abs_df_lo), r_iv)[0]
    r2 = iv_mul(r_iv, r_iv)
    rem_hi = ((d * (d - 1)) // 2) * iv_mul(r2, pow_up)[1]
    rhs = abs_f_hi + rem_hi
    assert lhs > rhs, f"Rouche check failed at d={d}: {lhs} <= {rhs}"

    # Return complex interval [zr - R_INT, zr + R_INT] + i [zi - R_INT, zi + R_INT]
    return ((zr - R_INT, zr + R_INT), (zi - R_INT, zi + R_INT))

def verify_small_d_exact() -> None:
    print("[Part 1] Exact integer fixed-point verification for 4 <= d <= 499 (zero floats)...", flush=True)
    max_akiyama_steps = 0
    solomyak_checks = 0
    closed_form_checks = 0
    greedy_checks = 0

    for d in range(4, 500):
        beta_iv = certify_beta(d)
        gamma_iv = certify_gamma_rouche(d)
        abs_gamma_iv = c_iv_abs(gamma_iv)
        assert abs_gamma_iv[0] > S, f"|gamma_d| <= 1 at d={d}"

        # Track q = beta_d^k, c = gamma_d^k, |c|^2 = |gamma_d|^{2k}
        q_iv = beta_iv
        c_iv = gamma_iv
        k = 1
        while True:
            # Check Solomyak criterion: |c|^2 > (3 + sqrt(5))/2
            # i.e. 2*s - 3 > 0 and (2*s - 3)^2 > 5 where s = |c|^2_lo / S
            c_norm2_lo = c_iv_norm2(c_iv)[0]
            lhs_lin = 2 * c_norm2_lo - 3 * S
            if lhs_lin > 0 and lhs_lin * lhs_lin > 5 * S * S:
                solomyak_checks += 1
                break

            abs_c_iv = c_iv_abs(c_iv)
            c_lo_m1 = abs_c_iv[0] - S
            assert c_lo_m1 > 0, f"|c| <= 1 at d={d}, k={k}"

            # Try closed-form Akiyama block (Section 1.4) whenever q < 2
            settled = False
            if q_iv[1] < 2 * S:
                # Find m0 >= 2 minimal with q^{m0-1}(q-1) >= 1
                qm1_iv = iv_sub(q_iv, (S, S))
                m0 = 2
                prod_iv = qm1_iv  # q^{m0-2} * (q-1)
                found_m0 = False
                while m0 <= 10000:
                    if prod_iv[1] < S:
                        next_prod = iv_mul(prod_iv, q_iv)
                        if next_prod[0] >= S:
                            found_m0 = True
                            break
                        prod_iv = next_prod
                        m0 += 1
                    else:
                        break
                if found_m0:
                    # Compute c^{m0-2} via binary exponentiation
                    c_pow_m0m2 = ((S, S), (0, 0))
                    base_c = c_iv
                    e_c = m0 - 2
                    while e_c > 0:
                        if e_c & 1:
                            c_pow_m0m2 = c_iv_mul(c_pow_m0m2, base_c)
                        e_c >>= 1
                        if e_c > 0:
                            base_c = c_iv_mul(base_c, base_c)
                    c_pow_m0m1 = c_iv_mul(c_pow_m0m2, c_iv)
                    c_m1 = (iv_sub(c_iv[0], (S, S)), c_iv[1])
                    inner = c_iv_mul(c_pow_m0m1, c_m1)
                    inner = (iv_sub(inner[0], (S, S)), inner[1])
                    # F(c)_lo = (|c|_lo - 1) * |c|_{lo}^{m0-2} * |c^{m0-1}(c-1) - 1|_lo
                    abs_inner_lo = c_iv_abs(inner)[0]
                    abs_cm2_lo = c_iv_abs(c_pow_m0m2)[0]
                    f1 = iv_mul((c_lo_m1, c_lo_m1), (abs_cm2_lo, abs_cm2_lo))[0]
                    f2 = iv_mul((f1, f1), (abs_inner_lo, abs_inner_lo))[0]
                    if f2 > S:
                        closed_form_checks += 1
                        settled = True

            if not settled:
                # Direct greedy orbit simulation for Akiyama's criterion
                fl_lo = q_iv[0] // S
                fl_hi = q_iv[1] // S
                assert fl_lo == fl_hi, f"Ambiguous floor(q) at d={d}, k={k}"
                floor_q = fl_lo
                x_iv = (S, S)
                sx_iv = ((S, S), (0, 0))
                ok = False
                for step in range(1, 50):
                    qx = iv_mul(q_iv, x_iv)
                    d_lo = qx[0] // S
                    d_hi = qx[1] // S
                    assert d_lo == d_hi, f"Ambiguous greedy digit at d={d}, k={k}, step={step}"
                    dig = d_lo
                    x_iv = iv_sub(qx, (dig * S, dig * S))
                    csx = c_iv_mul(c_iv, sx_iv)
                    sx_iv = (iv_sub(csx[0], (dig * S, dig * S)), csx[1])
                    sx_abs_lo = c_iv_abs(sx_iv)[0]
                    # Check |sigma(x_n)| * (|c| - 1) > floor(q)
                    if iv_mul((sx_abs_lo, sx_abs_lo), (c_lo_m1, c_lo_m1))[0] > floor_q * S:
                        ok = True
                        if step > max_akiyama_steps:
                            max_akiyama_steps = step
                        break
                assert ok, f"Akiyama criterion failed at d={d}, k={k}"
                greedy_checks += 1

            k += 1
            assert k <= 500, f"Too many k iterations at d={d}"
            q_iv = iv_mul(q_iv, beta_iv)
            c_iv = c_iv_mul(c_iv, gamma_iv)

    print(
        f"  Part 1 PASS: 4 <= d <= 499 (496 degrees): "
        f"{solomyak_checks} Solomyak cutoffs, {closed_form_checks} closed-form blocks, "
        f"{greedy_checks} greedy orbits (max step={max_akiyama_steps}).",
        flush=True,
    )


# =============================================================================
# Part 2: Rigorous mpmath.iv verification for analytic d >= 500
# =============================================================================
def verify_analytic_d_ge_500() -> None:
    print("[Part 2] Rigorous mpmath.iv verification of Section 3 (d >= 500)...", flush=True)
    d_min = iv.mpf(500)
    ln2 = iv.log(2)
    pi = iv.pi
    theta0 = (1 + iv.sqrt(5)) / 2

    # --- Lemma 3.1 ---
    # u = ln(2)/d + 1/d^2 <= ln(2)/500 + 1/250000 < 0.0014
    u_max = ln2 / 500 + iv.mpf(1) / 250000
    assert u_max < iv.mpf("0.0014")
    # Check 1 - (ln2 + 1/500)^2 / 2 > 0.75
    rem_31 = 1 - (ln2 + iv.mpf(1) / 500) ** 2 / 2
    assert rem_31 > iv.mpf("0.758") > iv.mpf("0.75")
    # Check 2 + 1.5/d > 2 + u = 2 + ln2/d + 1/d^2 for all d >= 500
    # Equivalent: 1.5 > ln2 + 1/d, true since ln2 + 1/500 < 0.70 < 1.5
    assert ln2 + iv.mpf(1) / 500 < iv.mpf("1.5")

    # --- Lemma 3.2 ---
    two_1_500 = iv.exp(ln2 / 500)
    assert two_1_500 < iv.mpf("1.0014")
    assert iv.mpf(10) / two_1_500 > iv.mpf("9.98")
    zeta_abs_coeff = iv.sqrt(ln2**2 + 4 * pi**2)
    assert zeta_abs_coeff < iv.mpf("6.322")
    assert zeta_abs_coeff / 500 < iv.mpf("0.0127")
    assert zeta_abs_coeff * iv.exp(iv.mpf("0.0127")) < iv.mpf("6.41")
    # Check 2*(e^{5/d} - 1 - 5/d) < 0.06/d on d >= 500
    # Wait: d*(e^{5/d} - 1 - 5/d) = 25/(2d) + ... is strictly decreasing in d!
    # Check directly at d = 500:
    y0 = iv.mpf(5) / 500
    err_tail_500 = 2 * 500 * (iv.exp(y0) - 1 - y0)
    assert err_tail_500 < iv.mpf("0.06")
    assert (iv.mpf("6.41") + iv.mpf("0.01") + iv.mpf("0.06")).b < iv.mpf("9.98").a
    assert 641 + 1 + 6 == 648 < 998
    # Im(z0) > 6.28/d > 5/d^2
    assert 500 * iv.sin(2 * pi / 500) > iv.mpf("6.28")
    # x = 5/(2^{1/d} d^2) < 2e-5 since 2^{1/d} > 1 and d >= 500; x + x^2 <= 5*(1 + 2e-5)/d^2 < 5.01/d^2
    assert 5 * 50000 == 500 * 500
    x_max = iv.mpf(1) / 50000
    assert 5 * (1 + x_max) < iv.mpf("5.01")
    # arcsin(x) < 5.01/d^2: since sin is strictly increasing on [0, pi/2] and arcsin(x)/x increases on (0,1),
    # checking sin(5.01 / 500^2) > x_max certifies arcsin(x) < 5.01 / d^2 for all d >= 500.
    assert iv.sin(iv.mpf(501) / (100 * 500 * 500)) > x_max

    # --- Completion of Proof for d >= 500 ---
    # ln |gamma_d| >= (ln2 - 5.01/500)/d > 0.683/d
    c_gam = ln2 - iv.mpf("5.01") / 500
    assert c_gam > iv.mpf("0.683")
    t_max = iv.log(theta0) / iv.mpf("0.683")
    assert t_max < iv.mpf("0.705")

    ln_q_max = iv.mpf("0.705") * (ln2 + iv.mpf(1) / 500)
    assert ln_q_max < iv.mpf("0.491") < ln2
    assert iv.exp(iv.mpf("0.491")) < iv.mpf("1.635") < 2

    # (|c| - 1)/(q - 1) > 1 - (6.01*0.705/500 + 6.01/(500*ln2)) > 1 - 0.0259 = 0.9741
    gap_ratio = iv.mpf("6.01") * iv.mpf("0.705") / 500 + iv.mpf("6.01") / (500 * ln2)
    assert gap_ratio < iv.mpf("0.0259")
    assert 10000 - 259 == 9741

    # Case A (0 < t <= 0.5):
    # Check max over d >= 500 of 6.01*0.5/d + 6.01*ln(d/ln2)/(d*ln2) < 0.1227
    # Since ln(d/ln2)/d decreases for d > e*ln2 (~1.88), max on d >= 500 is at d = 500!
    caseA_exp = iv.mpf("6.01") * iv.mpf("0.5") / 500 + iv.mpf("6.01") * iv.log(500 / ln2) / (500 * ln2)
    assert caseA_exp < iv.mpf("0.1227")
    assert iv.exp(-iv.mpf("0.1227")) > iv.mpf("0.8845")

    assert 501 * 2 == 1002  # 5.01 / 500 == 0.01002
    half_phi_max = pi / 2 + iv.mpf("0.00251")
    assert iv.sin(half_phi_max) / half_phi_max > iv.mpf("0.635")
    assert iv.mpf("0.635") * (2 * pi - iv.mpf("0.01002")) > iv.mpf("3.98")
    assert ln2 + iv.mpf(1) / 500 < iv.mpf("0.6952")
    assert iv.mpf("0.6952") * iv.exp(iv.mpf("0.3476")) < iv.mpf("0.985")
    assert iv.mpf("3.98") / iv.mpf("0.985") > iv.mpf("4.04")
    F_A_lb = iv.mpf("0.9741") / theta0 * iv.mpf("0.8845") * (iv.mpf("0.8845") * iv.mpf("4.04") - 1)
    assert F_A_lb > iv.mpf("1.36") > 1

    # Case B (0.5 < t <= 0.705):
    s2 = iv.sqrt(2)
    assert 2 * s2 * (s2 - 1) > iv.mpf("1.17") > 1
    caseB_exp = 3 * iv.mpf("6.01") * iv.mpf("0.705") / 500
    assert caseB_exp < iv.mpf("0.0255")
    assert iv.exp(-iv.mpf("0.0255")) > iv.mpf("0.9748")
    assert iv.exp(iv.mpf("0.5") * iv.mpf("0.683")) > iv.mpf("1.407")
    phi_B_lo = iv.mpf("0.5") * (2 * pi - iv.mpf("0.01002"))
    phi_B_hi = iv.mpf("0.705") * (2 * pi + iv.mpf("0.01002"))
    assert phi_B_lo > iv.mpf("3.1365") and phi_B_hi < iv.mpf("4.4368")
    assert iv.cos(iv.mpf("4.4368")) < iv.mpf("-0.272")
    c_m1_B = iv.sqrt(iv.mpf("1.407") ** 2 + 1 + 2 * iv.mpf("1.407") * iv.mpf("0.272"))
    assert c_m1_B > iv.mpf("1.935")
    assert iv.exp(iv.mpf("0.491")) - 1 < iv.mpf("0.634")
    assert iv.mpf("1.935") / iv.mpf("0.634") > iv.mpf("3.05")
    F_B_lb = iv.mpf("0.9741") / theta0 * iv.mpf("0.9748") * (iv.mpf("0.9748") * iv.mpf("3.05") - 1)
    assert F_B_lb > iv.mpf("1.15") > 1

    # Spot-check actual roots & all k for d in {500, 501, 600, 1000} using mpmath.iv
    for d in (500, 501, 600, 1000):
        # Bracket beta_d
        b_lo = iv.mpf(2) ** (iv.mpf(1) / d)
        b_hi = 1 + ln2 / d + iv.mpf(1) / (d * d)
        assert (b_lo ** d - b_lo - 1).b < 0
        assert (b_hi ** d - b_hi - 1).a > 0
        # Bracket gamma_d in Lemma 3.2 disk |z - z0| < 5/d^2
        z0 = iv.exp(iv.mpc(ln2, 2 * pi) / d)
        # Newton in mp.mpc to get center, then certify in iv with radius 2^-60
        mp.mp.dps = 50
        zc = mp.exp((mp.log(2) + 2j * mp.pi) / d)
        for _ in range(12):
            zc = zc - (zc**d - zc - 1) / (d * zc**(d - 1) - 1)
        r_disk = iv.mpf(2) ** (-60)
        z_iv = iv.mpc(iv.mpf(zc.real) + iv.mpf([-r_disk.a, r_disk.b]),
                      iv.mpf(zc.imag) + iv.mpf([-r_disk.a, r_disk.b]))
        # Verify Rouché at center zc
        z_pt = iv.mpc(iv.mpf(zc.real), iv.mpf(zc.imag))
        f_pt = z_pt**d - z_pt - 1
        df_pt = d * z_pt**(d - 1) - 1
        rem_iv = (d * (d - 1) / 2) * r_disk**2 * (abs(z_pt) + r_disk) ** (d - 2)
        assert (abs(df_pt) * r_disk).a > (abs(f_pt) + rem_iv).b
        assert iv.mpf(zc.imag).a > r_disk.b
        # Also verify gamma_d is inside Lemma 3.2 disk |z - z0| < 5/d^2
        assert (abs(z_iv - z0)).b < iv.mpf(5) / (d * d)
        # Tighten beta_d bracket inside [b_lo, b_hi] via exact interval bisection
        blo, bhi = b_lo.a, b_hi.b
        for _ in range(70):
            mid = (blo + bhi) / 2
            mid_iv = iv.mpf(mid)
            val = mid_iv**d - mid_iv - 1
            if val.b < 0:
                blo = mid
            elif val.a > 0:
                bhi = mid
            else:
                break
        beta_d = iv.mpf([blo, bhi])
        assert (beta_d**d - beta_d - 1).a <= 0 <= (beta_d**d - beta_d - 1).b
        k = 1
        while True:
            ck = z_iv**k
            if (abs(ck)).a > theta0.b:
                break
            qk = beta_d**k
            assert qk.b < 2
            m0 = 2
            while (qk**(m0 - 1) * (qk - 1)).a < 1:
                assert (qk**(m0 - 2) * (qk - 1)).b < 1
                m0 += 1
            F_val = (abs(ck) - 1) * abs(ck**(2 * m0 - 2) * (1 - ck**(-1) - ck**(-m0)))
            assert F_val.a > 1, f"F(c) <= 1 at d={d}, k={k}"
            k += 1

    print("  Part 2 PASS: All Section 3 inequalities and spot checks (d=500,501,600,1000) verified.", flush=True)


def main() -> int:
    verify_small_d_exact()
    verify_analytic_d_ge_500()
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
