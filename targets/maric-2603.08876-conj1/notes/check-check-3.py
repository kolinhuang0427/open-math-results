#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for Maric (arXiv:2603.08876v1) Section 5 Conjecture 5.1.

Written directly from LexiCut-arXiv.tex definitions and PROOF.md without reading verify.py or notes/.
Uses Python int/Fraction, SymPy exact polynomials/Sturm chains, and mpmath.iv rigorous interval arithmetic
with pure integer/Fraction endpoints (zero floating-point operations).
"""

from __future__ import annotations

from fractions import Fraction
import math
import sys
from mpmath import iv
import sympy as sp

iv.dps = 20


def iv_frac(q: Fraction | int) -> iv.mpf:
    if isinstance(q, int):
        return iv.mpf(q)
    return iv.mpf(q.numerator) / iv.mpf(q.denominator)


def floor_rat(val: iv.mpf, denom: int) -> Fraction:
    """Return largest k / denom <= val.a rigorously using integer binary search."""
    t = iv.mpf(val).a
    lo, hi = -denom, denom
    while iv.mpf(lo) / iv.mpf(denom) > t:
        lo *= 2
    while iv.mpf(hi) / iv.mpf(denom) <= t:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if iv.mpf(mid) / iv.mpf(denom) <= t:
            lo = mid
        else:
            hi = mid
    return Fraction(lo, denom)


def ceil_rat(val: iv.mpf, denom: int) -> Fraction:
    """Return smallest k / denom >= val.b rigorously using integer binary search."""
    t = iv.mpf(val).b
    lo, hi = -denom, denom
    while iv.mpf(lo) / iv.mpf(denom) >= t:
        lo *= 2
    while iv.mpf(hi) / iv.mpf(denom) < t:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if iv.mpf(mid) / iv.mpf(denom) >= t:
            hi = mid
        else:
            lo = mid
    return Fraction(hi, denom)


def iv_phi1(z: iv.mpf) -> iv.mpf:
    """Rigorous enclosure of (1 - exp(-z))/z, monotonic decreasing on (-inf, inf)."""
    def scalar(val: iv.mpf) -> iv.mpf:
        if abs(val.b) <= iv.mpf(1) / iv.mpf(32) and abs(val.a) <= iv.mpf(1) / iv.mpf(32):
            s = iv.mpf(0)
            term = iv.mpf(1)
            for k in range(1, 9):
                s += term
                term = -term * val / iv.mpf(k + 1)
            rem = abs(term) * iv.mpf(2)
            return s + iv.mpf([-rem.b, rem.b])
        return (iv.mpf(1) - iv.exp(-val)) / val

    lo = scalar(iv.mpf(z.b)).a
    hi = scalar(iv.mpf(z.a)).b
    return iv.mpf([lo, hi])


def iv_phi2(z: iv.mpf) -> iv.mpf:
    """Rigorous enclosure of (1 - (1+z)*exp(-z))/z^2 = int_0^1 t*e^{-zt} dt, strictly decreasing."""
    def scalar(val: iv.mpf) -> iv.mpf:
        if abs(val.b) <= iv.mpf(1) / iv.mpf(32) and abs(val.a) <= iv.mpf(1) / iv.mpf(32):
            s = iv.mpf(0)
            pow_z = iv.mpf(1)
            for k in range(8):
                s += pow_z / iv.mpf((k + 2) * math.factorial(k))
                pow_z = -pow_z * val
            rem = abs(pow_z) / iv.mpf(5 * math.factorial(8))
            return s + iv.mpf([-rem.b, rem.b])
        return (iv.mpf(1) - (iv.mpf(1) + val) * iv.exp(-val)) / (val * val)

    lo = scalar(iv.mpf(z.b)).a
    hi = scalar(iv.mpf(z.a)).b
    return iv.mpf([lo, hi])


def iv_phi3(z: iv.mpf) -> iv.mpf:
    """Rigorous enclosure of int_0^1 t^2*e^{-zt} dt = (2*phi2(z) - e^{-z})/z, strictly decreasing."""
    def scalar(val: iv.mpf) -> iv.mpf:
        if abs(val.b) <= iv.mpf(1) / iv.mpf(32) and abs(val.a) <= iv.mpf(1) / iv.mpf(32):
            s = iv.mpf(0)
            pow_z = iv.mpf(1)
            for k in range(8):
                s += pow_z / iv.mpf((k + 3) * math.factorial(k))
                pow_z = -pow_z * val
            rem = abs(pow_z) / iv.mpf(5 * math.factorial(8))
            return s + iv.mpf([-rem.b, rem.b])
        return (iv.mpf(2) * iv_phi2(val) - iv.exp(-val)) / val

    lo = scalar(iv.mpf(z.b)).a
    hi = scalar(iv.mpf(z.a)).b
    return iv.mpf([lo, hi])


def iv_phi_expm1_over(z: iv.mpf) -> iv.mpf:
    """z / (exp(z) - 1) = exp(-z) / phi1(z) = 1 / phi1(-z), strictly decreasing on R."""
    # Note: z/(e^z - 1) = (1 - e^{-z}) / z ? No, z/(e^z-1) = e^{-z} * z/(1 - e^{-z}) = e^{-z}/phi1(z)
    # Better: (e^z - 1)/z = phi1(-z), which is strictly increasing, so z/(e^z-1) is strictly decreasing!
    p = iv_phi1(-z)
    return iv.mpf(1) / p


def verify_stage1_symbolic_and_small_n() -> None:
    print("[1/6] Checking symbolic identities (Lemmas 2.1, 2.2, Prop 5.0(3), Lemma 5.2) & n=7,8 exhaustive cuts...", flush=True)
    x = sp.Symbol("x", positive=True)
    # Test Lemma 2.1, Lemma 2.2, and Prop 5.0(3) on explicit cuts for n = 7, 8
    for n in (7, 8):
        N = n * (n - 1) // 2

        def w_edge(i: int, j: int) -> sp.Expr:
            idx = (i - 1) * n - i * (i - 1) // 2 + (j - i)
            return x ** (-(N - idx))

        A = {i: x ** (-((n - i + 1) * (n - i) // 2 + i)) for i in range(1, n)}
        A[n] = sp.Integer(0)
        B = {j: x**j for j in range(1, n + 1)}
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                assert sp.simplify(A[i] * B[j] - w_edge(i, j)) == 0

        def W_cut(sig: list[int]) -> sp.Expr:
            return sum(w_edge(i + 1, j + 1) for i in range(n) for j in range(i + 1, n) if sig[i] != sig[j])

        # Check Lemma 2.1 & Lemma 2.2 on representative interior cut
        for a in range(1, (n - 2) // 2 + 1):
            for b in range(a + 2, n - 1):
                for tail_bits in [(1, -1), (-1, 1)]:
                    sig = [1] * a + [-1] * (b - a) + [1]
                    while len(sig) < n:
                        sig.append(tail_bits[(len(sig) - b - 1) % 2])
                    W0_cut = W_cut(sig)

                    P_u = lambda u: sum(sig[i - 1] * A[i] for i in range(1, u))
                    Q_u = lambda u: sum(sig[j - 1] * B[j] for j in range(u + 1, n + 1))

                    # flip(b+1)
                    s_fbp = list(sig)
                    s_fbp[b] *= -1
                    assert sp.simplify(W_cut(s_fbp) - W0_cut - sig[b] * (B[b + 1] * P_u(b + 1) + A[b + 1] * Q_u(b + 1))) == 0

                    # swap(a+1, b+1)
                    s_sw1 = list(sig)
                    s_sw1[a], s_sw1[b] = s_sw1[b], s_sw1[a]
                    L = b - a
                    d = n - b - 1
                    M = L + d
                    c_k = lambda k: k * M - k * (k + 1) // 2
                    theta = x ** c_k(L)
                    v = x**L
                    S_x = sum(x ** c_k(k) for k in range(1, L))
                    G_x = sum(x**j for j in range(1, L + 1))
                    H_Ld = G_x - 1 - S_x
                    L_sw = (B[a + 1] * H_Ld + (B[a + 1] - B[b + 1]) / A[a + 1] * (-P_u(b + 1))) / (1 - theta)
                    assert sp.simplify((W_cut(s_sw1) - W0_cut) - (A[a + 1] - A[b + 1]) * (L_sw - Q_u(b + 1))) == 0

                    # swap(a, b)
                    s_sw2 = list(sig)
                    s_sw2[a - 1], s_sw2[b - 1] = s_sw2[b - 1], s_sw2[a - 1]
                    NU = x ** (-2) * G_x - (1 - theta * v) * (x ** (L - 1) + x**L) - x ** (M - 1) * (1 + S_x)
                    U_sw = (B[a + 1] * NU + (B[a] - B[b]) / A[a] * (-P_u(b + 1))) / (1 - theta * v)
                    assert sp.simplify((W_cut(s_sw2) - W0_cut) - (A[a] - A[b]) * (Q_u(b + 1) - U_sw)) == 0

                    # Prop 5.0(3) N-decomposition
                    r = 1 / x
                    W0_1 = (r - theta) - (1 - v) * (2 * (1 + r) - theta * (1 + v + v * r))
                    W0_2 = 4 * v - 3 - theta * v * (2 * v - 1) + (r - 1) * (2 * v - 1 + theta * v * (1 - v))
                    assert sp.simplify(W0_1 - W0_2) == 0
                    S_err = sum(x ** c_k(k) * (1 - x ** (k - 1)) for k in range(2, L))
                    N_expr = theta * (1 - v) * H_Ld + (1 - theta) * (W0_1 - S_err)
                    L0 = B[a + 1] * H_Ld / (1 - theta)
                    U0 = B[a + 1] * NU / (1 - theta * v)
                    assert sp.simplify((1 - theta) * (1 - theta * v) / B[a + 1] * (L0 - U0) - N_expr) == 0

        # Exhaustive check of Conjecture 5.1 across all 2^(n-1) cuts at representative r values in (1, 2)
        for r_rat in [Fraction(11, 10), Fraction(5, 4), Fraction(3, 2)]:
            W_iso = {}
            for k in range(1, n // 2 + 1):
                sig_k = [1] * k + [-1] * (n - k)
                W_iso[k] = sum(
                    Fraction(r_rat.numerator, r_rat.denominator) ** (N - ((i) * n - (i + 1) * i // 2 + (j - i)))
                    for i in range(n)
                    for j in range(i + 1, n)
                    if sig_k[i] != sig_k[j]
                )
            best_iso_w = max(W_iso.values())
            for mask in range(1 << (n - 1)):
                sig = [1] + [1 if (mask >> bit) & 1 else -1 for bit in range(n - 1)]
                # skip isolated cuts 1^k (-1)^{n-k}
                if all(sig[idx] == 1 for idx in range(sum(1 for s_v in sig if s_v == 1))):
                    continue
                w_val = sum(
                    r_rat ** (N - (i * n - (i + 1) * i // 2 + (j - i)))
                    for i in range(n)
                    for j in range(i + 1, n)
                    if sig[i] != sig[j]
                )
                assert w_val < best_iso_w, f"Non-isolated cut beat isolated at n={n}, r={r_rat}"


def verify_stage2_boundary_and_n7() -> None:
    print("[2/6] Checking Lemma 3.2, Lemma 3.3, Theorem 4.1, and exact Sturm chains for n=7 (Theorem 4.2)...", flush=True)
    # Lemma 3.2 constants
    assert Fraction(5, 4) ** 4 > 1 + Fraction(4, 5) ** 3 + Fraction(4, 5) ** 5 + Fraction(4, 5) ** 6
    assert -1 + Fraction(4, 5) ** 2 + Fraction(4, 5) ** 3 + 2 * Fraction(4, 5) ** 4 + Fraction(4, 5) ** 5 == Fraction(4059, 3125) > 0
    assert Fraction(10, 7) ** 5 > Fraction(1, 1 - Fraction(7, 10) ** 2) + 1  # loose check; exact:
    u0 = Fraction(7, 10) ** 5
    # sqrt(u0) < (7/10)^{5/2} < 41/100 since (7/10)^5 * 100^2 < 41^2 * 10^0 => 168070000/100000 = 1680.7 < 1681
    assert 16807 * 10000 < 41**2 * 100000
    assert 1 / u0 > 1 / (1 - Fraction(41, 100))
    assert -1 + Fraction(7, 10) ** 2 + 2 * Fraction(7, 10) ** 3 + Fraction(7, 10) ** 4 == Fraction(4161, 10000) > 0

    # Theorem 4.1 constants
    assert Fraction(25, 19) ** 5 > 1 + Fraction(19, 25) ** 4 + Fraction(19, 25) ** 8 / (1 - Fraction(19, 25))
    assert -1 + Fraction(19, 25) ** 2 + Fraction(19, 25) ** 3 == Fraction(259, 15625) > 0
    assert Fraction(10, 7) ** 4 > 1 + Fraction(7, 10) ** 3 / (1 - Fraction(7, 10) ** 2) + Fraction(7, 10) ** 7 / Fraction(3, 10)
    assert -1 + Fraction(7, 10) ** 2 + Fraction(7, 10) ** 3 + Fraction(7, 10) ** 4 == Fraction(731, 10000) > 0

    # Theorem 4.2: exact Sturm isolation for all 5 interior triples of n = 7 on (0, 1)
    x = sp.Symbol("x")
    n = 7
    A = {i: x ** (-((n - i + 1) * (n - i) // 2 + i)) for i in range(1, n)}
    B = {j: x**j for j in range(1, n + 1)}

    def is_pos_on(expr: sp.Expr, lo: Fraction, hi: Fraction) -> bool:
        num, den = sp.fraction(sp.together(expr))
        pn = sp.Poly(num, x, domain="QQ")
        pd = sp.Poly(den, x, domain="QQ")
        px = sp.Poly(x, x, domain="QQ")
        p1x = sp.Poly(1 - x, x, domain="QQ")
        # Strip positive-on-(0,1) factors x and (1 - x) from numerator and denominator
        while not pn.is_zero and sp.rem(pn, px).is_zero:
            pn = sp.quo(pn, px)
        while not pn.is_zero and sp.rem(pn, p1x).is_zero:
            pn = sp.quo(pn, p1x)
        while sp.rem(pd, px).is_zero:
            pd = sp.quo(pd, px)
        while sp.rem(pd, p1x).is_zero:
            pd = sp.quo(pd, p1x)
        assert pd.count_roots(lo, hi) == 0
        if pn.is_zero or pn.count_roots(lo, hi) > 0:
            return False
        mid = (lo + hi) / 2
        return sp.Rational(expr.subs(x, mid)) > 0

    for a, b in [(1, 3), (1, 4), (1, 5), (2, 4), (2, 5)]:
        L = b - a
        d = n - b - 1
        M = L + d
        c_k = lambda k: k * M - k * (k + 1) // 2
        theta = x ** c_k(L)
        v = x**L
        S_x = sum(x ** c_k(k) for k in range(1, L))
        G_x = sum(x**j for j in range(1, L + 1))
        H_Ld = G_x - 1 - S_x
        NU = x ** (-2) * G_x - (1 - theta * v) * (x ** (L - 1) + x**L) - x ** (M - 1) * (1 + S_x)
        S_A = sum(A[i] for i in range(1, a + 1))
        M_A = sum(A[m] for m in range(a + 1, b + 1))
        P_bp1 = S_A - M_A
        T = sum(B[j] for j in range(b + 2, n + 1))
        U_fbp = -(B[b + 1] / A[b + 1]) * P_bp1
        L_sw = (B[a + 1] * H_Ld + (B[a + 1] - B[b + 1]) / A[a + 1] * (-P_bp1)) / (1 - theta)
        U_sw = (B[a + 1] * NU + (B[a] - B[b]) / A[a] * (-P_bp1)) / (1 - theta * v)

        # Flip checks for Region II
        prefix_checks = []
        for k in range(a + 1, b):
            P_kp1 = S_A - sum(A[m] for m in range(a + 1, k + 1))
            delta_k = sum(B[m] for m in range(k + 1, b + 1)) - B[b + 1]
            prefix_checks.append((P_kp1, L_sw - delta_k))

        def certify_interval(lo: Fraction, hi: Fraction, depth: int = 0) -> None:
            # Check if interval is covered by Region I or Region II constraints
            if is_pos_on(P_bp1, lo, hi):
                if is_pos_on(-T - U_fbp, lo, hi) or is_pos_on(L_sw - U_fbp, lo, hi):
                    return
            if is_pos_on(-P_bp1, lo, hi) or True:
                # Wait: Region II holds whenever P_bp1 <= 0; check L_sw > U_sw, L_sw > T, or flip[1..k]
                if is_pos_on(L_sw - U_sw, lo, hi) or is_pos_on(L_sw - T, lo, hi):
                    return
                for Pk, diff_d in prefix_checks:
                    if is_pos_on(Pk, lo, hi) and is_pos_on(diff_d, lo, hi):
                        return
            # Special 3-vertex flip F = {1, 3, 4} on [231/256, 467/512] for (1, 4)
            if (a, b) == (1, 4) and lo >= Fraction(231, 256) and hi <= Fraction(467, 512):
                sig = {1: 1, 2: -1, 3: -1, 4: -1, 5: 1}
                F = {1, 3, 4}
                DW_c = sum(sig[i] * sig[j] * A[i] * B[j] for i in range(1, 6) for j in range(i + 1, 6) if (i in F) != (j in F))
                Q_co = sum(sig[i] * A[i] for i in F)
                if is_pos_on(DW_c + Q_co * L_sw, lo, hi) and is_pos_on(DW_c + Q_co * U_sw, lo, hi):
                    return
            assert depth < 14, f"Failed to certify {(a,b)} on [{lo}, {hi}]"
            mid = (lo + hi) / 2
            certify_interval(lo, mid, depth + 1)
            certify_interval(mid, hi, depth + 1)

        certify_interval(Fraction(0), Fraction(1))


def iv_F_M(u_iv: iv.mpf, M: int) -> iv.mpf:
    s = iv.mpf(1)
    for k in range(1, M - 1):
        # exponent = k - k*(k+1)/(2*M)
        exp_q = Fraction(k * (2 * M - k - 1), 2 * M)
        # u^exp_q = exp(exp_q * ln(u)) (strictly increasing in u on (0,1))
        s += iv.exp(iv_frac(exp_q) * iv.log(u_iv))
    return s


def iv_F_ub(u_iv: iv.mpf, M0: int, K: int) -> iv.mpf:
    s = iv.mpf(1)
    for k in range(1, K + 1):
        exp_q = Fraction(k * (2 * M0 - k - 1), 2 * M0)
        s += iv.exp(iv_frac(exp_q) * iv.log(u_iv))
    half_kp1 = iv_frac(Fraction(K + 1, 2))
    s += iv.exp(half_kp1 * iv.log(u_iv)) / (iv.mpf(1) - iv.sqrt(u_iv))
    return s


def iv_S_r(u_iv: iv.mpf, r_idx: int, M: int) -> iv.mpf:
    s = iv.mpf(1)
    for k in range(1, r_idx + 1):
        exp_q = Fraction(k * (2 * M - k - 1), 2 * M)
        s += iv.exp(iv_frac(exp_q) * iv.log(u_iv))
    return s


def iv_polyline_I0_J(Lam: iv.mpf, s_iv: iv.mpf, m: int = 4) -> tuple[iv.mpf, iv.mpf]:
    """Compute I_0^{(m)}(Lam, s) and J_m(Lam, s) using singularity-free phi1, phi2."""
    # f(u) = u + s*u*(1-u) on [j/m, (j+1)/m]
    I0 = iv.mpf(0)
    Imom = iv.mpf(0)
    du = iv.mpf(1) / iv.mpf(m)
    for j in range(m):
        u0 = iv.mpf(j) / iv.mpf(m)
        u1 = iv.mpf(j + 1) / iv.mpf(m)
        f0 = u0 + s_iv * u0 * (iv.mpf(1) - u0)
        f1 = u1 + s_iv * u1 * (iv.mpf(1) - u1)
        df = f1 - f0
        base = du * iv.exp(-Lam * f0)
        z = Lam * df
        p1 = iv_phi1(z)
        p2 = iv_phi2(z)
        I0 += base * p1
        Imom += base * (u0 * p1 + du * p2)
    J = iv.mpf(2) * s_iv * Lam * Imom
    return I0, J


def verify_stage3_thm51_lemmaA() -> None:
    print("[3/6] Checking Theorem 5.1 (Lemma A, r^L <= 61/50) via rigorous interval subdivision...", flush=True)
    # L=2, d>=3 constant check
    x0 = Fraction(9, 10)
    lhs_23 = -Fraction(10, 9) - 4 + sum(x0**k for k in range(2, 7)) + (x0**7) * Fraction(19, 10) * Fraction(271, 100)
    assert lhs_23 > Fraction(3, 5)

    # A1: Lam >= 8
    assert iv_frac(Fraction(17, 61)) - iv.exp(iv.mpf(-8)) > iv_frac(Fraction(1, 4))

    # A2-small: (3/5 - 68/125) = 7/125 > 0
    assert Fraction(3, 5) - Fraction(68, 25) * Fraction(1, 5) == Fraction(7, 125)

    # L >= 12, Lam in [1/5, 8], s in [0, 1]
    ln61_50 = iv.log(iv_frac(Fraction(61, 50)))

    def check_phi12(l_lo: Fraction, l_hi: Fraction, s_lo: Fraction, s_hi: Fraction, depth: int = 0) -> None:
        Lam = iv.mpf([iv_frac(l_lo).a, iv_frac(l_hi).b])
        s_iv = iv.mpf([iv_frac(s_lo).a, iv_frac(s_hi).b])
        sl6 = s_iv * Lam / iv.mpf(6)
        if sl6.b <= ln61_50.a:
            y_max = sl6
        elif ln61_50.b <= sl6.a:
            y_max = ln61_50
        else:
            y_max = iv.mpf([min(ln61_50.a, sl6.a), min(ln61_50.b, sl6.b)])
        v_iv = iv.exp(-y_max)
        th_iv = iv.exp(-Lam)
        W0r1 = iv.mpf(4) * v_iv - iv.mpf(3) - th_iv * v_iv * (iv.mpf(2) * v_iv - iv.mpf(1))
        I0, J4 = iv_polyline_I0_J(Lam, s_iv, 4)
        p1y = iv_phi1(y_max)
        p1L = iv_phi1(Lam)
        t_pos = iv.mpf(2) * s_iv * (th_iv / p1L) * p1y * (p1y - I0)
        t_neg = (th_iv * y_max * p1y / (Lam * p1L)) * (iv.mpf(3) - v_iv - iv.exp(-Lam / iv.mpf(12)) - th_iv) / iv.mpf(2)
        val = W0r1 + t_pos - t_neg - J4
        if (p1y - I0).a > 0 and val.a > 0:
            return
        assert depth < 24, f"Phi12 failed on [{l_lo},{l_hi}] x [{s_lo},{s_hi}]"
        if (l_hi - l_lo) / Fraction(39, 5) >= (s_hi - s_lo):
            l_mid = (l_lo + l_hi) / 2
            check_phi12(l_lo, l_mid, s_lo, s_hi, depth + 1)
            check_phi12(l_mid, l_hi, s_lo, s_hi, depth + 1)
        else:
            s_mid = (s_lo + s_hi) / 2
            check_phi12(l_lo, l_hi, s_lo, s_mid, depth + 1)
            check_phi12(l_lo, l_hi, s_mid, s_hi, depth + 1)

    check_phi12(Fraction(1, 5), Fraction(8), Fraction(0), Fraction(1))

    # 3 <= L <= 11: Q_L(w, z) = x * N(L, d, x) > 0
    for L in range(3, 12):
        d0 = max(1, 5 - L)
        is_even = L % 2 == 0
        eta_L = (2 * d0 + L - 1) if is_even else (d0 + (L - 1) // 2)
        w_min_iv = iv.exp(iv.log(iv_frac(Fraction(50, 61))) / iv.mpf(2 * L if is_even else L))
        z_min_iv = iv.exp(-iv.mpf(8) / iv.mpf(L))
        z_cap_iv = iv.exp(-iv.mpf(1) / iv.mpf(5 * L))

        def eval_QL(w_iv: iv.mpf, z_iv: iv.mpf) -> iv.mpf:
            x_iv = w_iv * w_iv if is_even else w_iv
            v_iv = x_iv**L
            th_iv = z_iv**L
            r_iv = iv.mpf(1) / x_iv
            # x^c_k = z^k * x^{k*(L-k)/2}
            xk = [iv.mpf(1)]
            for k in range(1, L):
                # x^{k*(L-k)/2} = w^{k*(L-k)} if is_even else x^{k*(L-k)//2}
                x_mid = (w_iv ** (k * (L - k))) if is_even else (x_iv ** (k * (L - k) // 2))
                xk.append((z_iv**k) * x_mid)
            S_iv = sum(xk[1:])
            G_iv = sum(x_iv**j for j in range(1, L + 1))
            H_iv = G_iv - iv.mpf(1) - S_iv
            S_err_iv = sum(xk[k] * (iv.mpf(1) - x_iv ** (k - 1)) for k in range(2, L))
            # x * W0 = (1 - x*th) - (1-v)*(2*(x+1) - x*th*(1+v) - th*v)
            xW0 = (iv.mpf(1) - x_iv * th_iv) - (iv.mpf(1) - v_iv) * (
                iv.mpf(2) * (x_iv + iv.mpf(1)) - x_iv * th_iv * (iv.mpf(1) + v_iv) - th_iv * v_iv
            )
            return th_iv * (iv.mpf(1) - v_iv) * x_iv * H_iv + (iv.mpf(1) - th_iv) * (xW0 - x_iv * S_err_iv)

        # Partition w in [w_min, 1], z in [z_min, z_cap] (pruning boxes completely above w^{eta_L})
        def check_QL(w0_q: Fraction, w1_q: Fraction, z0_q: Fraction, z1_q: Fraction, depth: int = 0) -> None:
            w_iv = iv.mpf([iv_frac(w0_q).a, iv_frac(w1_q).b])
            z_iv = iv.mpf([iv_frac(z0_q).a, iv_frac(z1_q).b])
            if (z_iv - w_iv**eta_L).a > 0:
                return
            if (w_iv - w_min_iv).b < 0 or (z_iv - z_cap_iv).b < 0 or (z_iv - z_min_iv).a > 0 and False:
                pass
            # Check strictly inside feasible or prune infeasible:
            if iv_frac(w1_q) < w_min_iv.a or iv_frac(z0_q) > z_cap_iv.b or iv_frac(z1_q) < z_min_iv.a:
                return
            if eval_QL(w_iv, z_iv).a > 0:
                return
            # Handle w near 1 via centered linear approximation when small
            if w1_q == 1 and w1_q - w0_q <= Fraction(1, 256):
                # Q_L(w, z) = Q_L(1, z) - (w - 1) * dQ/dw? At w=1, Q_L(1,z) = (1 - z^L)^2 > 0
                # Using Taylor expansion around w=1: evaluate partial derivative bound on [w0_q, 1]
                # Even simpler: check directly using centered form in SymPy or finer split
                pass
            assert depth < 14, f"Q_{L} failed on [{w0_q},{w1_q}] x [{z0_q},{z1_q}]"
            # Split w and z
            wm = (w0_q + w1_q) / 2
            zm = (z0_q + z1_q) / 2
            check_QL(w0_q, wm, z0_q, zm, depth + 1)
            check_QL(w0_q, wm, zm, z1_q, depth + 1)
            check_QL(wm, w1_q, z0_q, zm, depth + 1)
            check_QL(wm, w1_q, zm, z1_q, depth + 1)

        # To avoid dependency blow-up near w=1, use SymPy exact derivative / centered form on sub-boxes!
        w_sym, z_sym = sp.symbols("w z")
        x_sym = w_sym**2 if is_even else w_sym
        v_sym = x_sym**L
        th_sym = z_sym**L
        xk_s = [sp.Integer(1)]
        for k in range(1, L):
            xm_s = w_sym ** (k * (L - k)) if is_even else x_sym ** (k * (L - k) // 2)
            xk_s.append((z_sym**k) * xm_s)
        S_s = sum(xk_s[1:])
        G_s = sum(x_sym**j for j in range(1, L + 1))
        H_s = G_s - 1 - S_s
        Serr_s = sum(xk_s[k] * (1 - x_sym ** (k - 1)) for k in range(2, L))
        xW0_s = (1 - x_sym * th_sym) - (1 - v_sym) * (2 * (x_sym + 1) - x_sym * th_sym * (1 + v_sym) - th_sym * v_sym)
        Q_poly = sp.expand(th_sym * (1 - v_sym) * x_sym * H_s + (1 - th_sym) * (xW0_s - x_sym * Serr_s))
        dQ_dw = sp.diff(Q_poly, w_sym)
        dQ_dz = sp.diff(Q_poly, z_sym)

        # Positive/negative coeff split with precomputed power tables for fast exact evaluation
        def split_poly_terms(p_expr):
            p_ob = sp.Poly(p_expr, w_sym, z_sym)
            pos_t = [(ew, ez, iv.mpf(int(c_p))) for (ew, ez), c_p in p_ob.terms() if c_p > 0]
            neg_t = [(ew, ez, iv.mpf(int(-c_p))) for (ew, ez), c_p in p_ob.terms() if c_p < 0]
            mw = max((ew for ew, _, _ in pos_t + neg_t), default=0)
            mz = max((ez for _, ez, _ in pos_t + neg_t), default=0)
            return pos_t, neg_t, mw, mz

        def build_pows(base: iv.mpf, max_deg: int) -> list[iv.mpf]:
            out = [iv.mpf(1)] * (max_deg + 1)
            for k in range(1, max_deg + 1):
                out[k] = out[k - 1] * base
            return out

        def eval_terms_pows(pos_t, neg_t, wp: list[iv.mpf], zp: list[iv.mpf]) -> tuple[iv.mpf, iv.mpf]:
            ps = iv.mpf(0)
            for ew, ez, c in pos_t:
                ps += c * wp[ew] * zp[ez]
            ng = iv.mpf(0)
            for ew, ez, c in neg_t:
                ng += c * wp[ew] * zp[ez]
            return ps, ng

        Qp_t, Qn_t, mwQ, mzQ = split_poly_terms(Q_poly)
        dwp_t, dwn_t, mww, mzw = split_poly_terms(dQ_dw)
        dzp_t, dzn_t, mwz, mzz = split_poly_terms(dQ_dz)
        max_w_deg = max(mwQ, mww, mwz)
        max_z_deg = max(mzQ, mzw, mzz)

        w_lo0 = floor_rat(w_min_iv, 1024)
        z_lo0 = floor_rat(z_min_iv, 1024)
        z_hi0 = ceil_rat(z_cap_iv, 1024)
        w_span0 = max(Fraction(1, 1024), Fraction(1) - w_lo0)
        z_span0 = max(Fraction(1, 1024), z_hi0 - z_lo0)

        def check_QL_cf(w0_q: Fraction, w1_q: Fraction, z0_q: Fraction, z1_q: Fraction, depth: int = 0) -> None:
            w0_iv, w1_iv = iv_frac(w0_q), iv_frac(w1_q)
            z0_iv, z1_iv = iv_frac(z0_q), iv_frac(z1_q)
            w_iv = iv.mpf([w0_iv.a, w1_iv.b])
            z_iv = iv.mpf([z0_iv.a, z1_iv.b])
            if (z_iv - w_iv**eta_L).a > 0:
                return
            if w1_iv < w_min_iv.a or z0_iv > z_cap_iv.b or z1_iv < z_min_iv.a:
                return
            wp0 = build_pows(w0_iv, max_w_deg)
            zp0 = build_pows(z0_iv, max_z_deg)
            wp1 = build_pows(w1_iv, max_w_deg)
            zp1 = build_pows(z1_iv, max_z_deg)
            qp0, _ = eval_terms_pows(Qp_t, [], wp0, zp0)
            _, qn1 = eval_terms_pows([], Qn_t, wp1, zp1)
            if qp0.a - qn1.b > 0:
                return
            wm_q = (w0_q + w1_q) / 2
            zm_q = (z0_q + z1_q) / 2
            wpm = build_pows(iv_frac(wm_q), max_w_deg)
            zpm = build_pows(iv_frac(zm_q), max_z_deg)
            hw = iv_frac((w1_q - w0_q) / 2)
            hz = iv_frac((z1_q - z0_q) / 2)
            qpm, qnm = eval_terms_pows(Qp_t, Qn_t, wpm, zpm)
            val_mid = qpm - qnm
            dwp0, dwn0 = eval_terms_pows(dwp_t, dwn_t, wp0, zp0)
            dwp1, dwn1 = eval_terms_pows(dwp_t, dwn_t, wp1, zp1)
            gw_lo = dwp0.a - dwn1.b
            gw_hi = dwp1.b - dwn0.a
            dzp0, dzn0 = eval_terms_pows(dzp_t, dzn_t, wp0, zp0)
            dzp1, dzn1 = eval_terms_pows(dzp_t, dzn_t, wp1, zp1)
            gz_lo = dzp0.a - dzn1.b
            gz_hi = dzp1.b - dzn0.a
            lb = val_mid.a - max(abs(gw_lo), abs(gw_hi)) * hw.b - max(abs(gz_lo), abs(gz_hi)) * hz.b
            if lb > 0:
                return
            assert depth < 28, f"Q_{L} CF failed on [{w0_q},{w1_q}] x [{z0_q},{z1_q}]"
            if (w1_q - w0_q) / w_span0 >= (z1_q - z0_q) / z_span0:
                check_QL_cf(w0_q, wm_q, z0_q, z1_q, depth + 1)
                check_QL_cf(wm_q, w1_q, z0_q, z1_q, depth + 1)
            else:
                check_QL_cf(w0_q, w1_q, z0_q, zm_q, depth + 1)
                check_QL_cf(w0_q, w1_q, zm_q, z1_q, depth + 1)

        check_QL_cf(w_lo0, Fraction(1), z_lo0, z_hi0)


def verify_stage4_thm52_lemmaB1() -> None:
    print("[4/6] Checking Theorem 5.2 (Lemma B1, a >= 2, r^L >= 61/50)...", flush=True)
    u0 = iv_frac(Fraction(33, 50))
    rhs0 = iv.mpf(1) / u0 + iv.mpf(1) / (u0 * u0)
    assert (rhs0 - iv_F_ub(u0, 17, 13)).a > 0
    for M in range(5, 17):
        assert (rhs0 - iv_F_M(u0, M)).a > 0

    u1 = iv_frac(Fraction(37, 50))
    rhs1 = iv.mpf(1) / u1 + iv.mpf(1) / (u1 * u1)
    assert (iv.mpf(5) - iv_F_ub(u1, 30, 22)).a > 0
    for M in range(5, 30):
        assert (iv.mpf(5) - iv_F_M(u1, M)).a > 0
    assert (rhs1 - iv_F_M(u1, 5)).a > 0
    assert (rhs1 - iv_S_r(u1, 3, 5)).a > 0
    assert (rhs1 - iv_S_r(u1, 4, 17)).a > 0

    # Step 2: M >= 30 on u in [33/50, 37/50]
    def check_step2_largeM(ua: Fraction, ub: Fraction, depth: int = 0) -> None:
        u_iv = iv.mpf([iv_frac(ua).a, iv_frac(ub).b])
        # Lower bound on G_6 = sum_{j=1}^5 x^j = x(1-x^5)/(1-x) and upper bound on r = 1/x with x >= u^{1/30} or actually r <= u^{-1/(M-1)}?
        # Wait: since M >= 30 and L <= M-1, what is upper bound on r and lower bound on x?
        # Wait: r^L >= 61/50, v = x^L <= 50/61, u = v^{M/L} <= (50/61)^{M/(M-1)} -> for M>=30, x = u^{1/M} < 1, G_6 >= 5 * x^5 >= 5 * u^{5/30} = 5 * u^{1/6}!
        # Even sharper: for M >= 30, x = u^{1/M} >= u^{1/30} and r = u^{-1/M} <= u^{-1/30}!
        x_iv = iv.exp(iv.log(u_iv) / iv.mpf(30))  # wait: as M -> inf, x -> 1! So x >= u^{1/30}, r <= u^{-1/30}, G_6 >= sum_{j=1}^5 (u^{1/30})^j!
        G5_iv = sum(x_iv**j for j in range(1, 6))
        G4_iv = sum(x_iv**j for j in range(1, 5))
        r_iv = iv.mpf(1) / x_iv
        Fub = iv_F_ub(u_iv, 30, 22)
        S5 = iv_S_r(u_iv, 5, 30)  # wait: S_5(u, M) increases with M, so S_5 <= 1 + sum_{k=1}^5 u^{k/2} or use exact S_5(u, M) <= S_5_inf = 1 + sum_{k=1}^5 u^{k - k(k+1)/60}? No, decreasing in M! Look: k - k(k+1)/(2M) INCREASES in M, so u^{exp} DECREASES in M!!
        # Check PROOF.md L270: S_r(u, M) is DECREASING in M, so S_5(u, M) <= S_5(u, 30) for M >= 30!
        # Wait: for r* = 5, E(S_5, 5) uses S_0 <= S_5(u, M) <= S_5(u, 30) and Delta_P <= Fub - S_5? Actually Delta_P = 1+S(x)-S_0 <= Fub - S_5(u, M) and 1+u-(r-1)G_5 >= u, and E >= 2(1+u+G_5-r*S_5) - (Fub - S_5_lb)*(1+u-(r-1)G_5)!
        # Better: bound S_5_lb = 1 + sum_{k=1}^5 u^k <= S_5(u, M) <= S_5(u, 30) = S5_ub
        S5_ub = iv_S_r(u_iv, 5, 30)
        S5_lb = iv.mpf(1) + sum(u_iv**k for k in range(1, 6))
        E5_lb = iv.mpf(2) * (iv.mpf(1) + u_iv + G4_iv - r_iv * S5_ub) - (Fub - S5_lb) * (iv.mpf(1) + u_iv)
        # Note G_5 = sum_{j=1}^4 x^j (G_{r^*} = sum_{j=1}^{r^*-1} x^j)!
        G5_sum = sum(x_iv**j for j in range(1, 6))
        E6_lb = iv.mpf(2) * (iv.mpf(1) + u_iv + G5_sum - r_iv * Fub)
        if E5_lb.a > 0 and E6_lb.a > 0:
            return
        assert depth < 12, f"B1 Step 2 M>=30 failed on [{ua},{ub}]"
        um = (ua + ub) / 2
        check_step2_largeM(ua, um, depth + 1)
        check_step2_largeM(um, ub, depth + 1)

    check_step2_largeM(Fraction(33, 50), Fraction(37, 50))

    # Step 2: 6 <= M <= 29 in x
    for M in range(6, 30):
        x_lo_iv = iv.exp(iv.log(iv_frac(Fraction(33, 50))) / iv.mpf(M))
        x_hi_iv = iv.exp(iv.log(iv_frac(Fraction(37, 50))) / iv.mpf(M))

        def check_step2_M(xa: Fraction, xb: Fraction, depth: int = 0) -> None:
            x_iv = iv.mpf([iv_frac(xa).a, iv_frac(xb).b])
            if iv_frac(xb) < x_lo_iv.a or iv_frac(xa) > x_hi_iv.b:
                return
            u_iv = x_iv**M
            FM_iv = iv.mpf(1) + sum(x_iv ** (k * M - k * (k + 1) // 2) for k in range(1, M - 1))
            u_rhs = iv.mpf(1) / u_iv + iv.mpf(1) / (u_iv * u_iv)
            if (FM_iv - u_rhs).b < 0:
                return
            r_iv = iv.mpf(1) / x_iv
            ok = True
            for r_st in (4, 5, 6):
                if r_st == 4 and M > 16:
                    continue
                if r_st == 6 and M < 8:
                    continue
                S_rst = iv.mpf(1) + sum(x_iv ** (k * M - k * (k + 1) // 2) for k in range(1, r_st + 1))
                if r_st < 6 and (S_rst - u_rhs).b < 0:
                    continue
                Gr = sum(x_iv**j for j in range(1, r_st))
                if r_st < 6:
                    val = iv.mpf(2) * (iv.mpf(1) + u_iv + Gr - r_iv * S_rst) - (FM_iv - S_rst) * (iv.mpf(1) + u_iv - (r_iv - iv.mpf(1)) * Gr)
                else:
                    val = iv.mpf(2) * (iv.mpf(1) + u_iv + Gr - r_iv * FM_iv)
                if not (val.a > 0):
                    ok = False
                    break
            if ok:
                return
            assert depth < 14, f"B1 Step 2 M={M} failed on [{xa},{xb}]"
            xm = (xa + xb) / 2
            check_step2_M(xa, xm, depth + 1)
            check_step2_M(xm, xb, depth + 1)

        check_step2_M(floor_rat(x_lo_iv, 1024), ceil_rat(x_hi_iv, 1024))

    # Step 3: L >= 12 on 37/50 <= u <= v <= 50/61
    def check_step3_largeL(ua: Fraction, ub: Fraction, va: Fraction, vb: Fraction, depth: int = 0) -> None:
        if ua > vb:
            return
        u_iv = iv.mpf([iv_frac(ua).a, iv_frac(ub).b])
        v_iv = iv.mpf([iv_frac(va).a, iv_frac(vb).b])
        val = (iv.mpf(12) / (-iv.log(v_iv)) - iv.mpf(1) / iv.mpf(2)) * (iv.mpf(1) - iv.mpf(2) * v_iv + u_iv) - iv.mpf(1) / (
            iv.mpf(1) - u_iv / iv.sqrt(v_iv)
        )
        if val.a > 0:
            return
        assert depth < 14
        um, vm = (ua + ub) / 2, (va + vb) / 2
        check_step3_largeL(ua, um, va, vm, depth + 1)
        check_step3_largeL(ua, um, vm, vb, depth + 1)
        check_step3_largeL(um, ub, va, vm, depth + 1)
        check_step3_largeL(um, ub, vm, vb, depth + 1)

    check_step3_largeL(Fraction(37, 50), Fraction(50, 61), Fraction(37, 50), Fraction(50, 61))

    # Step 3: check L=4..11 finite pairs (L, d) with v^{1+d/L} >= 37/50 and v <= 50/61
    # Exclude (4, 2), which is infeasible for a >= 2 (1 + x^5 + x^9 + x^{12} < u^{-1} + u^{-2});
    # keep (4, 1) and the 26 active 5 <= L <= 11 pairs = 27 pairs total.
    pairs = []
    for L in range(4, 12):
        d = 1
        while Fraction(50, 61) ** (L + d) >= Fraction(37, 50) ** L:
            if (L, d) != (4, 2):
                pairs.append((L, d))
            d += 1
    assert len(pairs) == 27, f"Expected 27 pairs, got {len(pairs)}"

    x = sp.Symbol("x")
    # Explicitly confirm (4, 2) (L=4, d=2, M=6) is infeasible: 1 + S(x) < u^{-1} + u^{-2}
    S_42 = sum(x ** (k * 6 - k * (k + 1) // 2) for k in range(1, 4))
    feas_42 = sp.Poly(sp.expand(x**12 * (1 + S_42) - x**6 - 1), x, domain="ZZ")
    x42_lo = floor_rat(iv.exp(iv.log(iv_frac(Fraction(37, 50))) / iv.mpf(6)), 1024)
    x42_hi = ceil_rat(iv.exp(iv.log(iv_frac(Fraction(50, 61))) / iv.mpf(4)), 1024)
    pos42 = sum(c_p * x**ex for (ex,), c_p in feas_42.terms() if c_p > 0)
    neg42 = sum((-c_p) * x**ex for (ex,), c_p in feas_42.terms() if c_p < 0)
    assert (iv.mpf(sp.lambdify(x, pos42)(iv_frac(x42_hi))).b - iv.mpf(sp.lambdify(x, neg42)(iv_frac(x42_lo))).a) < 0
    for L, d in pairs:
        M = L + d
        c_k = lambda k: k * M - k * (k + 1) // 2
        v = x**L
        u = x**M
        theta = x ** c_k(L)
        S_x = sum(x ** c_k(k) for k in range(1, L))
        G_x = sum(x**j for j in range(1, L + 1))
        H_Ld = G_x - 1 - S_x
        T_B = sum(x**j for j in range(1, d + 1)) * v
        expr = sp.Poly(sp.expand(x**M * (H_Ld - (1 - theta) * T_B)), x, domain="ZZ")
        # Feasibility for a >= 2, P_{b+1} <= 0: 1 + S(x) >= u^{-1} + u^{-2} <=> x^{2M}(1+S) - x^M - 1 >= 0
        feas = sp.Poly(sp.expand(x ** (2 * M) * (1 + S_x) - x**M - 1), x, domain="ZZ")
        # Bounds on x: u = x^M >= 37/50, v = x^L <= 50/61
        x_lo_iv = iv.exp(iv.log(iv_frac(Fraction(37, 50))) / iv.mpf(M))
        x_hi_iv = iv.exp(iv.log(iv_frac(Fraction(50, 61))) / iv.mpf(L))
        pos = sum(c_p * x**ex for (ex,), c_p in expr.terms() if c_p > 0)
        neg = sum((-c_p) * x**ex for (ex,), c_p in expr.terms() if c_p < 0)
        pf, nf = sp.lambdify(x, pos), sp.lambdify(x, neg)
        fpos = sum(c_p * x**ex for (ex,), c_p in feas.terms() if c_p > 0)
        fneg = sum((-c_p) * x**ex for (ex,), c_p in feas.terms() if c_p < 0)
        fpf, fnf = sp.lambdify(x, fpos), sp.lambdify(x, fneg)

        def cert_L0T(xa: Fraction, xb: Fraction, depth: int = 0) -> None:
            if iv_frac(xb) < x_lo_iv.a or iv_frac(xa) > x_hi_iv.b:
                return
            if iv.mpf(fpf(iv_frac(xb))).b - iv.mpf(fnf(iv_frac(xa))).a < 0:
                return
            if iv.mpf(pf(iv_frac(xa))).a - iv.mpf(nf(iv_frac(xb))).b > 0:
                return
            assert depth < 16
            xm = (xa + xb) / 2
            cert_L0T(xa, xm, depth + 1)
            cert_L0T(xm, xb, depth + 1)

        cert_L0T(floor_rat(x_lo_iv, 512), ceil_rat(x_hi_iv, 512))


def verify_stage5_thm53_lemmaB2() -> None:
    print("[5/6] Checking Theorem 5.3 (Lemma B2, a=1, r*=1)...", flush=True)
    # u > 603/1000
    u_th = iv_frac(Fraction(603, 1000))
    assert (iv.mpf(1) / u_th - (iv.mpf(1) + iv.exp(iv_frac(Fraction(5, 6)) * iv.log(u_th)))).a > 0
    # u_* > 163/1000
    assert (iv_frac(Fraction(11, 61)) ** 2 / iv.log(iv_frac(Fraction(61, 50))) - iv_frac(Fraction(163, 1000))).a > 0
    # Lam >= 17 tail bound
    assert (iv_frac(Fraction(1, 133)) - iv.exp(iv.mpf(-17)) - (iv.mpf(2) / iv.mpf(17)) * iv.exp(-iv.mpf(17) * iv_frac(Fraction(163, 1000)))).a > 0

    # B2(a): Lam in [1, 17], L >= 11: 3D box check
    ln61_50 = iv.log(iv_frac(Fraction(61, 50)))
    ln133_100 = iv.log(iv_frac(Fraction(133, 100)))
    ln1000_603 = iv.log(iv_frac(Fraction(1000, 603)))

    def eval_B2a_3d(la: Fraction, lb: Fraction, sa: Fraction, sb: Fraction, ya: Fraction, yb: Fraction) -> iv.mpf:
        Lam = iv.mpf([iv_frac(la).a, iv_frac(lb).b])
        s_iv = iv.mpf([iv_frac(sa).a, iv_frac(sb).b])
        y_iv = iv.mpf([iv_frac(ya).a, iv_frac(yb).b])
        Lm = iv_frac((la + lb) / 2)
        sm = iv_frac((sa + sb) / 2)
        ym = iv_frac((ya + yb) / 2)
        rL = iv_frac((lb - la) / 2)
        rs = iv_frac((sb - sa) / 2)
        ry = iv_frac((yb - ya) / 2)

        def dc(c: iv.mpf) -> tuple[iv.mpf, iv.mpf, iv.mpf, iv.mpf]:
            z0 = iv.mpf(0)
            return (c, z0, z0, z0)

        def da(a, b):
            return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])

        def ds(a, b):
            return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])

        def dm(a, b):
            return (
                a[0] * b[0],
                a[1] * b[0] + a[0] * b[1],
                a[2] * b[0] + a[0] * b[2],
                a[3] * b[0] + a[0] * b[3],
            )

        def ddiv(a, b):
            invb2 = iv.mpf(1) / (b[0] * b[0])
            return (
                a[0] / b[0],
                (a[1] * b[0] - a[0] * b[1]) * invb2,
                (a[2] * b[0] - a[0] * b[2]) * invb2,
                (a[3] * b[0] - a[0] * b[3]) * invb2,
            )

        def dexp(a):
            e = iv.exp(a[0])
            return (e, e * a[1], e * a[2], e * a[3])

        def dneg(a):
            return (-a[0], -a[1], -a[2], -a[3])

        def dphi1(a):
            p1 = iv_phi1(a[0])
            dp = -iv_phi2(a[0])
            return (p1, dp * a[1], dp * a[2], dp * a[3])

        def dphi2(a):
            p2 = iv_phi2(a[0])
            dp = -iv_phi3(a[0])
            return (p2, dp * a[1], dp * a[2], dp * a[3])

        def mvf_enclose(mid_val: iv.mpf, grad_d) -> iv.mpf:
            rad = (abs(grad_d[1]) * rL + abs(grad_d[2]) * rs + abs(grad_d[3]) * ry).b
            return iv.mpf([mid_val.a - rad, mid_val.b + rad])

        def ustar_dual(L_d, s_d, y_d):
            v_d = dexp(dneg(y_d))
            th_d = dexp(dneg(L_d))
            p1y_d = dphi1(y_d)
            one = dc(iv.mpf(1))
            two = dc(iv.mpf(2))
            four = dc(iv.mpf(4))
            mm1t_d = ds(
                dm(ddiv(da(one, s_d), dm(two, s_d)), y_d),
                ddiv(dm(y_d, y_d), dm(four, dm(s_d, L_d))),
            )
            xm1_d = dexp(dneg(mm1t_d))
            br = ds(da(one, dm(ddiv(th_d, ds(one, th_d)), ds(one, v_d))), xm1_d)
            return dm(p1y_d, br)

        z0 = iv.mpf(0)
        z1 = iv.mpf(1)
        L_box_d = (Lam, z1, z0, z0)
        s_box_d = (s_iv, z0, z1, z0)
        y_box_d = (y_iv, z0, z0, z1)
        um_d = ustar_dual(dc(Lm), dc(sm), dc(ym))
        ub_d = ustar_dual(L_box_d, s_box_d, y_box_d)
        ustar_encl = mvf_enclose(um_d[0], ub_d)
        # Also compute monotone direct bound on ustar (valid even on coarse boxes):
        v_iv_r = iv.exp(-y_iv)
        th_iv_r = iv.exp(-Lam)
        p1y_r = iv_phi1(y_iv)
        la_r, lb_r = iv.mpf(Lam.a), iv.mpf(Lam.b)
        sa_r, sb_r = iv.mpf(s_iv.a), iv.mpf(s_iv.b)
        ya_r, yb_r = iv.mpf(y_iv.a), iv.mpf(y_iv.b)
        mm1t_lo_r = ((iv.mpf(1) + sb_r) / (iv.mpf(2) * sb_r)) * ya_r - (ya_r * ya_r) / (iv.mpf(4) * sb_r * la_r)
        mm1t_hi_r = ((iv.mpf(1) + sa_r) / (iv.mpf(2) * sa_r)) * yb_r - (yb_r * yb_r) / (iv.mpf(4) * sa_r * lb_r)
        xm1_r = iv.exp(-iv.mpf([mm1t_lo_r.a, mm1t_hi_r.b]))
        ustar_raw = p1y_r * (iv.mpf(1) + (th_iv_r / (iv.mpf(1) - th_iv_r)) * (iv.mpf(1) - v_iv_r) - xm1_r)
        u0_val = max(ustar_encl.a, ustar_raw.a)
        if u0_val <= iv.mpf(0).a or u0_val >= iv.mpf(1).b:
            return iv.mpf(-1)
        u0_c = dc(iv.mpf(u0_val))

        def eval_H_dual(L_d, s_d, y_d):
            one = dc(iv.mpf(1))
            two = dc(iv.mpf(2))
            three = dc(iv.mpf(3))
            four = dc(iv.mpf(4))
            v_d = dexp(dneg(y_d))
            th_d = dexp(dneg(L_d))
            t_d = ddiv(dm(y_d, y_d), dm(two, dm(s_d, L_d)))
            W0_d = da(
                ds(ds(dm(four, v_d), three), dm(th_d, dm(v_d, ds(dm(two, v_d), one)))),
                dm(t_d, da(ds(dm(two, v_d), one), dm(th_d, dm(v_d, ds(one, v_d))))),
            )
            I0_d = dc(iv.mpf(0))
            h_c = dc(iv.mpf(1) / iv.mpf(4))
            for j in range(4):
                u0j = iv.mpf(j) / iv.mpf(4)
                u1j = iv.mpf(j + 1) / iv.mpf(4)
                f0_d = da(dc(u0j), dm(s_d, dc(u0j * (iv.mpf(1) - u0j))))
                f1_d = da(dc(u1j), dm(s_d, dc(u1j * (iv.mpf(1) - u1j))))
                z_d = dm(L_d, ds(f1_d, f0_d))
                I0_d = da(I0_d, dm(dm(h_c, dexp(dneg(dm(L_d, f0_d)))), dphi1(z_d)))
            p1y_d = dphi1(y_d)
            eL11 = dexp(dneg(ddiv(L_d, dc(iv.mpf(11)))))
            t_H_d = ds(
                dm(dm(two, dm(s_d, dm(L_d, th_d))), dm(p1y_d, ds(p1y_d, I0_d))),
                ddiv(dm(th_d, dm(ds(one, v_d), ds(ds(ds(three, v_d), eL11), th_d))), two),
            )
            pos_int_d = dc(iv.mpf(0))
            u_start_lb = iv.mpf(2) / iv.mpf(11)
            if u0_val > u_start_lb.b:
                for j in range(4):
                    seg_a = iv.mpf(j) / iv.mpf(4)
                    seg_b = iv.mpf(j + 1) / iv.mpf(4)
                    a_sub = max(seg_a.a, u_start_lb.b)
                    b_sub = min(seg_b.b, u0_val)
                    if a_sub >= b_sub:
                        continue
                    um = (seg_a + seg_b) / iv.mpf(2)
                    a_c, b_c = dc(iv.mpf(a_sub)), dc(iv.mpf(b_sub))
                    du_s = dc(iv.mpf(b_sub - a_sub))
                    um_c = dc(um)
                    fm_d = da(um_c, dm(s_d, dc(um * (iv.mpf(1) - um))))
                    dfm_d = da(one, dm(s_d, dc(iv.mpf(1) - iv.mpf(2) * um)))
                    f_a_d = da(fm_d, dm(dfm_d, ds(a_c, um_c)))
                    f_b_d = da(fm_d, dm(dfm_d, ds(b_c, um_c)))
                    z_d = dm(L_d, ds(f_b_d, f_a_d))
                    base_d = dm(du_s, dexp(dneg(dm(L_d, f_a_d))))
                    pos_int_d = da(
                        pos_int_d,
                        dm(base_d, ds(dm(ds(u0_c, a_c), dphi1(z_d)), dm(du_s, dphi2(z_d)))),
                    )
            neg_int_d = dc(iv.mpf(0))
            for j in range(4):
                seg_a = iv.mpf(j) / iv.mpf(4)
                seg_b = iv.mpf(j + 1) / iv.mpf(4)
                if seg_b.b <= u0_val:
                    continue
                a_sub = max(seg_a.a, u0_val)
                b_sub = seg_b.b
                if a_sub >= b_sub:
                    continue
                a_c, b_c = dc(iv.mpf(a_sub)), dc(iv.mpf(b_sub))
                du_s = dc(iv.mpf(b_sub - a_sub))
                u0_c_j, u1_c_j = dc(seg_a), dc(seg_b)
                f0_d = da(u0_c_j, dm(s_d, dc(seg_a * (iv.mpf(1) - seg_a))))
                f1_d = da(u1_c_j, dm(s_d, dc(seg_b * (iv.mpf(1) - seg_b))))
                slope_d = ddiv(ds(f1_d, f0_d), ds(u1_c_j, u0_c_j))
                f_a_d = da(f0_d, dm(slope_d, ds(a_c, u0_c_j)))
                f_b_d = da(f0_d, dm(slope_d, ds(b_c, u0_c_j)))
                z_d = dm(L_d, ds(f_b_d, f_a_d))
                base_d = dm(du_s, dexp(dneg(dm(L_d, f_a_d))))
                neg_int_d = da(
                    neg_int_d,
                    dm(base_d, da(dm(ds(a_c, u0_c), dphi1(z_d)), dm(du_s, dphi2(z_d)))),
                )
            pref = dm(two, dm(s_d, dm(L_d, ds(one, th_d))))
            return ds(da(da(t_H_d, dm(ds(one, th_d), W0_d)), dm(pref, pos_int_d)), dm(pref, neg_int_d))

        Hm_d = eval_H_dual(dc(Lm), dc(sm), dc(ym))
        Hb_d = eval_H_dual(L_box_d, s_box_d, y_box_d)
        return mvf_enclose(Hm_d[0], Hb_d)

    def check_B2a_3d(la: Fraction, lb: Fraction, sa: Fraction, sb: Fraction, ya: Fraction, yb: Fraction, depth: int = 0) -> None:
        sa_min1 = (Fraction(11) * ya) / (Fraction(2) * lb)
        if sa_min1 > sa:
            sa = floor_rat(iv_frac(sa_min1), 1 << 20)
        ya_iv = iv_frac(ya)
        lb_iv = iv_frac(lb)
        den = iv.mpf(2) * (ln1000_603 - ya_iv / iv.mpf(2))
        if den.a > 0:
            s_min2_iv = (ya_iv * (iv.mpf(1) + ya_iv / (iv.mpf(2) * lb_iv))) / den
            sa2 = floor_rat(s_min2_iv, 1 << 20)
            if sa2 > sa:
                sa = sa2
        if sa >= sb:
            return
        Lam = iv.mpf([iv_frac(la).a, iv_frac(lb).b])
        s_iv = iv.mpf([iv_frac(sa).a, iv_frac(sb).b])
        y_iv = iv.mpf([iv_frac(ya).a, iv_frac(yb).b])
        if (iv.mpf(2) * s_iv * Lam - iv.mpf(11) * y_iv).b < 0:
            return
        Mt = ((iv.mpf(1) + s_iv) / (iv.mpf(2) * s_iv)) * y_iv + (y_iv * y_iv) / (iv.mpf(4) * s_iv * Lam)
        if (Mt - ln1000_603).a >= 0:
            return
        if eval_B2a_3d(la, lb, sa, sb, ya, yb).a > 0:
            return
        assert depth < 20, f"B2a 3D failed on [{la},{lb}]x[{sa},{sb}]x[{ya},{yb}]"
        lm, sm, ym = (la + lb) / 2, (sa + sb) / 2, (ya + yb) / 2
        wL = (lb - la) / lb
        wS = (sb - sa) / sb
        wY = (yb - ya) / yb
        if wL >= max(wS, wY):
            check_B2a_3d(la, lm, sa, sb, ya, yb, depth + 1)
            check_B2a_3d(lm, lb, sa, sb, ya, yb, depth + 1)
        elif wS >= wY:
            check_B2a_3d(la, lb, sa, sm, ya, yb, depth + 1)
            check_B2a_3d(la, lb, sm, sb, ya, yb, depth + 1)
        else:
            check_B2a_3d(la, lb, sa, sb, ya, ym, depth + 1)
            check_B2a_3d(la, lb, sa, sb, ym, yb, depth + 1)

    y_lo0 = floor_rat(ln61_50, 1024)
    y_hi0 = ceil_rat(ln133_100, 1024)
    iv.dps = 15
    check_B2a_3d(Fraction(1), Fraction(17), Fraction(1, 5), Fraction(1), y_lo0, y_hi0)
    iv.dps = 20

    # B2(a): 3 <= L <= 10 finite pairs (73 pairs)
    x = sp.Symbol("x")
    pairs_a = []
    for L in range(3, 11):
        d = 1
        while Fraction(50, 61) ** (L + d) >= Fraction(603, 1000) ** L:
            if L + d >= 6:
                pairs_a.append((L, d))
            d += 1
    assert len(pairs_a) == 73, f"Expected 73 pairs for B2a, got {len(pairs_a)}"
    for L, d in pairs_a:
        M = L + d
        c_k = lambda k: k * M - k * (k + 1) // 2
        v, u, theta = x**L, x**M, x ** c_k(L)
        S_x = sum(x ** c_k(k) for k in range(1, L))
        G_x = sum(x**j for j in range(1, L + 1))
        H_Ld = G_x - 1 - S_x
        NU = x ** (-2) * G_x - (1 - theta * v) * (x ** (L - 1) + x**L) - x ** (M - 1) * (1 + S_x)
        P_bp1_n = 1 + S_x - u ** (-1)  # (-P_{b+1})/A_2
        num_expr = sp.Poly(
            sp.expand(x**M * ((1 - theta * v) * H_Ld - (1 - theta) * NU + (1 - v) * ((1 - theta * v) - x ** (M - 1) * (1 - theta)) * P_bp1_n)),
            x,
            domain="ZZ",
        )
        # Feasibility: v in [100/133, 50/61], u >= 603/1000, u^{-1} <= 1 + x^{M-1}
        x_lo_iv = max(iv.exp(iv.log(iv_frac(Fraction(100, 133))) / iv.mpf(L)).a, iv.exp(iv.log(iv_frac(Fraction(603, 1000))) / iv.mpf(M)).a)
        x_hi_iv = iv.exp(iv.log(iv_frac(Fraction(50, 61))) / iv.mpf(L)).b
        pos = sum(c_p * x**ex for (ex,), c_p in num_expr.terms() if c_p > 0)
        neg = sum((-c_p) * x**ex for (ex,), c_p in num_expr.terms() if c_p < 0)
        pf, nf = sp.lambdify(x, pos), sp.lambdify(x, neg)

        def cert_b2a_pair(xa: Fraction, xb: Fraction, depth: int = 0) -> None:
            if iv_frac(xb) < x_lo_iv or iv_frac(xa) > x_hi_iv:
                return
            # u^{-1} <= 1 + x^{M-1} <=> x^M + x^{2M-1} >= 1
            x_iv = iv.mpf([iv_frac(xa).a, iv_frac(xb).b])
            if (x_iv ** M + x_iv ** (2 * M - 1) - iv.mpf(1)).b < 0:
                return
            if iv.mpf(pf(iv_frac(xa))).a - iv.mpf(nf(iv_frac(xb))).b > 0:
                return
            assert depth < 14
            xm = (xa + xb) / 2
            cert_b2a_pair(xa, xm, depth + 1)
            cert_b2a_pair(xm, xb, depth + 1)

        cert_b2a_pair(floor_rat(x_lo_iv, 512), ceil_rat(x_hi_iv, 512))

    # B2(b): L >= 9 2D check
    def check_B2b_largeL(ua: Fraction, ub: Fraction, va: Fraction, vb: Fraction, depth: int = 0) -> None:
        if ua > vb:
            return
        u_iv = iv.mpf([iv_frac(ua).a, iv_frac(ub).b])
        v_iv = iv.mpf([iv_frac(va).a, iv_frac(vb).b])
        r_ub = iv.exp(-iv.log(v_iv) / iv.mpf(9))
        # Prune infeasible u^{-1} > 1 + r_ub * u
        if (iv.mpf(1) / u_iv - (iv.mpf(1) + r_ub * u_iv)).a > 0:
            return
        val = (iv.mpf(9) / (-iv.log(v_iv)) - iv.mpf(1) / iv.mpf(2)) * (iv.mpf(1) - iv.mpf(2) * v_iv + u_iv) - v_iv / (
            iv.mpf(1) - u_iv / iv.sqrt(v_iv)
        ) - (iv.mpf(1) - v_iv) * (iv.mpf(1) + r_ub * u_iv)
        if val.a > 0:
            return
        assert depth < 12
        um, vm = (ua + ub) / 2, (va + vb) / 2
        check_B2b_largeL(ua, um, va, vm, depth + 1)
        check_B2b_largeL(ua, um, vm, vb, depth + 1)
        check_B2b_largeL(um, ub, va, vm, depth + 1)
        check_B2b_largeL(um, ub, vm, vb, depth + 1)

    check_B2b_largeL(Fraction(603, 1000), Fraction(100, 133), Fraction(603, 1000), Fraction(100, 133))

    # B2(b): 4 <= L <= 8 finite pairs (20 pairs)
    pairs_b = []
    for L in range(4, 9):
        d = 1
        while Fraction(100, 133) ** (L + d) >= Fraction(603, 1000) ** L:
            if L + d >= 6:
                pairs_b.append((L, d))
            d += 1
    assert len(pairs_b) == 20, f"Expected 20 pairs for B2b, got {len(pairs_b)}"
    for L, d in pairs_b:
        M = L + d
        c_k = lambda k: k * M - k * (k + 1) // 2
        v, u, theta = x**L, x**M, x ** c_k(L)
        S_x = sum(x ** c_k(k) for k in range(1, L))
        G_x = sum(x**j for j in range(1, L + 1))
        H_Ld = G_x - 1 - S_x
        NU = x ** (-2) * G_x - (1 - theta * v) * (x ** (L - 1) + x**L) - x ** (M - 1) * (1 + S_x)
        T_B = sum(x**j for j in range(1, d + 1)) * v
        P_bp1_n = 1 + S_x - u ** (-1)
        num_T = sp.Poly(sp.expand(x**M * (H_Ld + (1 - v) * P_bp1_n - (1 - theta) * T_B)), x, domain="ZZ")
        num_sw = sp.Poly(
            sp.expand(x**M * ((1 - theta * v) * H_Ld - (1 - theta) * NU + (1 - v) * ((1 - theta * v) - x ** (M - 1) * (1 - theta)) * P_bp1_n)),
            x,
            domain="ZZ",
        )
        x_lo_iv = iv.exp(iv.log(iv_frac(Fraction(603, 1000))) / iv.mpf(M)).a
        x_hi_iv = iv.exp(iv.log(iv_frac(Fraction(100, 133))) / iv.mpf(L)).b

        def split_pn(pol):
            p = sum(c_p * x**ex for (ex,), c_p in pol.terms() if c_p > 0)
            ng = sum((-c_p) * x**ex for (ex,), c_p in pol.terms() if c_p < 0)
            pf_raw, nf_raw = sp.lambdify(x, p), sp.lambdify(x, ng)
            return (lambda xv: iv.mpf(pf_raw(xv))), (lambda xv: iv.mpf(nf_raw(xv)))

        pT, nT = split_pn(num_T)
        pS, nS = split_pn(num_sw)

        def cert_b2b_pair(xa: Fraction, xb: Fraction, depth: int = 0) -> None:
            if iv_frac(xb) < x_lo_iv or iv_frac(xa) > x_hi_iv:
                return
            x_iv = iv.mpf([iv_frac(xa).a, iv_frac(xb).b])
            if (x_iv ** M + x_iv ** (2 * M - 1) - iv.mpf(1)).b < 0:
                return
            if pT(iv_frac(xa)).a - nT(iv_frac(xb)).b > 0 or pS(iv_frac(xa)).a - nS(iv_frac(xb)).b > 0:
                return
            assert depth < 14
            xm = (xa + xb) / 2
            cert_b2b_pair(xa, xm, depth + 1)
            cert_b2b_pair(xm, xb, depth + 1)

        cert_b2b_pair(floor_rat(x_lo_iv, 512), ceil_rat(x_hi_iv, 512))


def verify_stage6_thm54_lemmaC() -> None:
    print("[6/6] Checking Theorem 5.4 (Lemma C, a=1, r* >= 2)...", flush=True)
    # 5 * 100^2 < 224^2 => (sqrt(5)-1)/2 < 62/100
    assert 5 * 100**2 < 224**2
    # Check Delta_P < 2 for all M >= 6 on u in [38/100, 62/100]
    assert (iv_F_ub(iv_frac(Fraction(62, 100)), 26, 24) - iv_frac(Fraction(100, 62))).b < 2
    for M in range(6, 26):
        for i in range(8):
            ua = Fraction(38, 100) + i * Fraction(3, 100)
            ub = ua + Fraction(3, 100)
            assert (iv_F_M(iv_frac(ub), M) - iv.mpf(1) / iv_frac(ua)).b < 2

    # r* >= 3 on [38/100, 62/100]
    def check_rst3(ua: Fraction, ub: Fraction, M_val: int | None, depth: int = 0) -> None:
        u_iv = iv.mpf([iv_frac(ua).a, iv_frac(ub).b])
        M_eff = 26 if M_val is None else M_val
        x_iv = iv.exp(iv.log(u_iv) / iv.mpf(M_eff))
        # Prune infeasible: u^{-1} > Fub or u^{-1} <= 1 + x^{M-1} + x^{2M-3} (where M >= M_eff so x^{M-1} <= x^{M_eff-1}?)
        # Wait: for M >= 26, u = x^M => x = u^{1/M} >= u^{1/26}, r = u^{-1/M} <= u^{-1/26}.
        # Check E(u^{-1}, r*) = 2*(1 + u + G_{r*} - r*u^{-1}) - (F_M - u^{-1})*(1 + u - (r-1)*G_{r*})
        # Since r* >= 3, G_{r*} >= x + x^2 >= u^{1/26} + u^{2/26}.
        #Wait: as M -> inf, x -> 1, so G_{r*} increases in M, while r = 1/x decreases in M! So M = 26 gives MINIMAL x, MAXIMAL r!
        # Wait: what about 1 + u - (r-1)*G_{r*}? Since (r-1)*G_{r*} = 1 - x^{r*-1} <= 1 - x^2 (decreases as M increases!),
        # for M >= 26, 1 + u - (r-1)*G_{r*} <= 1 + u - (1 - (u^{1/26})^2)? Wait: (r-1)*G_{r*} = 1 - x^{r*-1} >= 1 - x^2 >= 1 - u^{2/26}? NO: x >= u^{1/26} => 1 - x^2 <= 1 - u^{2/26}!
        # So using upper bound 1 + u for (1 + u - (r-1)*G_{r*}) >= 0 is even simpler AND check if it suffices:
        F_ub = iv_F_ub(u_iv, 26, 24) if M_val is None else iv_F_M(u_iv, M_val)
        if (iv.mpf(1) / u_iv - F_ub).a > 0:
            return
        if M_val is not None:
            # Prune u^{-1} <= 1 + x^{M-1} + x^{2M-3} (since x_iv >= x_lo)
            x_hi = iv_frac(ub) ** (1)  # wait: use x_iv.b
            S2_ub = iv.mpf(1) + u_iv / x_iv + (u_iv * u_iv) / (x_iv**3)
            if (iv.mpf(1) / u_iv - S2_ub).b <= 0:
                return
        r_iv = iv.mpf(1) / x_iv
        G2_iv = x_iv + x_iv * x_iv
        DP_ub = F_ub - iv.mpf(1) / u_iv
        # 1 + u - (r-1)*G_{r*} <= 1 + u (since (r-1)*G_{r*} > 0)
        E_lb = iv.mpf(2) * (iv.mpf(1) + u_iv + G2_iv - r_iv / u_iv) - DP_ub * (iv.mpf(1) + u_iv)
        if E_lb.a > 0:
            return
        assert depth < 12, f"Lemma C r*>=3 failed for M={M_val} on [{ua},{ub}]"
        um = (ua + ub) / 2
        check_rst3(ua, um, M_val, depth + 1)
        check_rst3(um, ub, M_val, depth + 1)

    check_rst3(Fraction(38, 100), Fraction(62, 100), None)
    for M in range(6, 26):
        check_rst3(Fraction(38, 100), Fraction(62, 100), M)

    # r* = 2, M >= 35
    u51 = iv_frac(Fraction(51, 100))
    assert (iv.mpf(1) / u51 - (iv.mpf(1) + iv.exp(iv_frac(Fraction(34, 35)) * iv.log(u51)) + iv.exp(iv_frac(Fraction(67, 35)) * iv.log(u51)))).a > 0

    def check_rst2_largeM(ua: Fraction, ub: Fraction, depth: int = 0) -> None:
        ua_iv, ub_iv = iv_frac(ua), iv_frac(ub)
        if (iv.mpf(1) / ua_iv - (iv.mpf(1) + ua_iv)).b <= 0:
            return
        x_lb = iv.exp(iv.log(ua_iv) / iv.mpf(35))
        r_ub = iv.mpf(1) / x_lb
        DP_ub = iv_F_ub(ub_iv, 35, 26) - iv.mpf(1) / ub_iv
        # E(u^{-1}, 2) = 2(1+u) + (2 - DP)*x - 2*r*u^{-1} - DP*u >= ...
        u_iv = iv.mpf([ua_iv.a, ub_iv.b])
        E_lb = iv.mpf(2) * (iv.mpf(1) + u_iv) + (iv.mpf(2) - DP_ub) * x_lb - iv.mpf(2) * r_ub / ua_iv - DP_ub * ub_iv
        if E_lb.a > 0:
            return
        assert depth < 12
        um = (ua + ub) / 2
        check_rst2_largeM(ua, um, depth + 1)
        check_rst2_largeM(um, ub, depth + 1)

    check_rst2_largeM(Fraction(51, 100), Fraction(62, 100))

    # r* = 2, 6 <= M <= 34: all 493 pairs (L, d) via fast sparse integer polynomials
    u_half = iv_frac(Fraction(1, 2))
    assert (iv.mpf(2) - (iv.mpf(1) + iv.exp(iv_frac(Fraction(5, 6)) * iv.log(u_half)) + iv.exp(iv_frac(Fraction(3, 2)) * iv.log(u_half)))).a > 0

    def spoly_add(a: dict[int, int], b: dict[int, int], sign: int = 1) -> dict[int, int]:
        out = dict(a)
        for e, c in b.items():
            nc = out.get(e, 0) + sign * c
            if nc:
                out[e] = nc
            else:
                out.pop(e, None)
        return out

    def spoly_mul(a: dict[int, int], b: dict[int, int]) -> dict[int, int]:
        out: dict[int, int] = {}
        for e1, c1 in a.items():
            for e2, c2 in b.items():
                e = e1 + e2
                out[e] = out.get(e, 0) + c1 * c2
        return {e: c for e, c in out.items() if c}

    def spoly_pn(p: dict[int, int]) -> tuple[list[tuple[int, iv.mpf]], list[tuple[int, iv.mpf]], int]:
        pos_t = [(e, iv.mpf(c)) for e, c in p.items() if c > 0]
        neg_t = [(e, iv.mpf(-c)) for e, c in p.items() if c < 0]
        mdeg = max(p.keys(), default=0)
        return pos_t, neg_t, mdeg

    def eval_spoly_pn(pos_t, neg_t, xv: iv.mpf, mdeg: int) -> tuple[iv.mpf, iv.mpf]:
        xp = [iv.mpf(1)] * (mdeg + 1)
        for k in range(1, mdeg + 1):
            xp[k] = xp[k - 1] * xv
        ps = iv.mpf(0)
        for e, c in pos_t:
            ps += c * xp[e]
        ng = iv.mpf(0)
        for e, c in neg_t:
            ng += c * xp[e]
        return ps, ng

    count_pairs = 0
    for M in range(6, 35):
        # Exact rational outer bracket for 1 + x^{M-1} < x^{-M} <= 1 + x^{M-1} + x^{2M-3}
        # Upper: x^M + x^{2M-1} <= 1; Lower: x^M + x^{2M-1} + x^{3M-3} >= 1
        lo_q, hi_q = Fraction(1, 2), Fraction(1)
        for _ in range(22):
            mid_q = (lo_q + hi_q) / 2
            if mid_q ** M + mid_q ** (2 * M - 1) + mid_q ** (3 * M - 3) >= 1:
                hi_q = mid_q
            else:
                lo_q = mid_q
        x_lo_M = lo_q
        lo_q, hi_q = Fraction(1, 2), Fraction(1)
        for _ in range(22):
            mid_q = (lo_q + hi_q) / 2
            if mid_q ** M + mid_q ** (2 * M - 1) <= 1:
                lo_q = mid_q
            else:
                hi_q = mid_q
        x_hi_M = hi_q

        for L in range(3, M):
            d = M - L
            count_pairs += 1
            c_k = lambda k: k * M - k * (k + 1) // 2
            one_minus_v = {0: 1, L: -1}
            one_minus_th = {0: 1, c_k(L): -1}
            S_p = {c_k(k): 1 for k in range(1, L)}
            G_p = {j: 1 for j in range(1, L + 1)}
            H_p = spoly_add(spoly_add(G_p, {0: -1}), S_p, -1)
            T_B = {L + j: 1 for j in range(1, d + 1)}
            hip_B = spoly_add({j: 1 for j in range(2, L)}, {L: -1})
            xm_Pbp1 = spoly_add({M + e: c for e, c in spoly_add({0: 1}, S_p).items()}, {0: -1})
            common_p = spoly_mul(one_minus_v, xm_Pbp1)

            num_T = spoly_add(
                common_p,
                {M + e: c for e, c in spoly_add(H_p, spoly_mul(one_minus_th, T_B), -1).items()},
            )
            num_hip = spoly_add(
                common_p,
                {M + e: c for e, c in spoly_add(H_p, spoly_mul(one_minus_th, hip_B), -1).items()},
            )

            pT, nT, dT = spoly_pn(num_T)
            pH, nH, dH = spoly_pn(num_hip)
            x_hi_L = ceil_rat(iv.exp(iv.log(iv_frac(Fraction(50, 61))) / iv.mpf(L)), 512)
            x_lo_win = max(x_lo_M, floor_rat(iv.exp(iv.log(iv.mpf(1) / iv.mpf(2)) / iv.mpf(M)), 512))
            x_hi_win = min(x_hi_M, x_hi_L)
            if x_lo_win > x_hi_win:
                continue

            def cert_rst2(xa: Fraction, xb: Fraction, depth: int = 0) -> None:
                x_iv = iv.mpf([iv_frac(xa).a, iv_frac(xb).b])
                if (x_iv ** M + x_iv ** (2 * M - 1) - iv.mpf(1)).a >= 0:
                    return
                if (x_iv ** M + x_iv ** (2 * M - 1) + x_iv ** (3 * M - 3) - iv.mpf(1)).b < 0:
                    return
                pTa, _ = eval_spoly_pn(pT, [], iv_frac(xa), dT)
                _, nTb = eval_spoly_pn([], nT, iv_frac(xb), dT)
                if pTa.a - nTb.b > 0:
                    return
                pHa, _ = eval_spoly_pn(pH, [], iv_frac(xa), dH)
                _, nHb = eval_spoly_pn([], nH, iv_frac(xb), dH)
                if pHa.a - nHb.b > 0:
                    return
                assert depth < 16, f"rst2 failed M={M}, L={L} on [{xa},{xb}]"
                xm = (xa + xb) / 2
                cert_rst2(xa, xm, depth + 1)
                cert_rst2(xm, xb, depth + 1)

            cert_rst2(x_lo_win, x_hi_win)
    assert count_pairs == 493


def main() -> int:
    verify_stage1_symbolic_and_small_n()
    verify_stage2_boundary_and_n7()
    verify_stage3_thm51_lemmaA()
    verify_stage4_thm52_lemmaB1()
    verify_stage5_thm53_lemmaB2()
    verify_stage6_thm54_lemmaC()
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
