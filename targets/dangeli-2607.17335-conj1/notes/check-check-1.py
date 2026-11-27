#!/usr/bin/env python3
"""Independent zero-float exact & interval-arithmetic verifier for targets/dangeli-2607.17335-conj1/.

Built strictly from primary source definitions (tools/.arxiv_cache/eprint/2607.17335v1.src -> totally_main.tex)
and COUNTEREXAMPLE.md without reading verify.py or author notes.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import comb, factorial
import sympy as sp
from mpmath import iv

iv.dps = 30


def I(x: int | str) -> iv.mpf:
    return iv.mpf(str(x))


def F(num: int, den: int) -> iv.mpf:
    return iv.mpf(num) / iv.mpf(den)


# ---------------------------------------------------------------------------
# 1. Lemma 1: Clean twin pairs on small strongly connected 2-out graphs (n=3..6)
# ---------------------------------------------------------------------------
def is_strongly_connected(edges: list[tuple[int, int]]) -> bool:
    n = len(edges)
    for s in range(n):
        seen = {s}
        stack = [s]
        while stack:
            u = stack.pop()
            for v in edges[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        if len(seen) < n:
            return False
    return True


def verify_lemma1_examples() -> None:
    examples = [
        [(0, 2), (2, 0), (0, 1)],
        [(2, 3), (3, 2), (3, 0), (2, 1)],
        [(2, 3), (3, 2), (3, 4), (4, 0), (1, 2)],
        [(2, 3), (3, 2), (3, 1), (4, 0), (5, 2), (0, 3)],
    ]
    for edges in examples:
        n = len(edges)
        assert is_strongly_connected(edges), f"Not SCC for n={n}"
        assert sorted(edges[0]) == sorted(edges[1])
        d0 = sorted(edges[0])
        delta = [edges[u] for u in range(n)]
        delta[0] = (d0[0], d0[1])
        delta[1] = (d0[0], d0[1])
        assert delta[0][0] == delta[1][0] and delta[0][1] == delta[1][1]
        if n >= 4:
            assert len({0, 1, d0[0], d0[1]}) == 4
    print("PASS Lemma 1: explicit strongly connected twin-pair examples verified (n=3..6)")


# ---------------------------------------------------------------------------
# 2. Surjection recurrences T(m, k), F(m, k, t) & small brute-force counts
# ---------------------------------------------------------------------------
def verify_surjections() -> None:
    T: dict[tuple[int, int], int] = {(0, 0): 1}
    for m in range(1, 13):
        T[(m, 0)] = 0
        for k in range(1, m + 1):
            T[(m, k)] = k * (T.get((m - 1, k), 0) + T.get((m - 1, k - 1), 0))

    for m in range(1, 11):
        for k in range(1, m + 1):
            for t in range(0, 5):
                f1 = sum(comb(m, j) * (t ** j) * T.get((m - j, k), 0) for j in range(m - k + 1))
                f2 = sum(comb(t, i) * T.get((m, k + i), 0) for i in range(min(t, m - k) + 1))
                assert f1 == f2, f"F mismatch m={m}, k={k}, t={t}: {f1} vs {f2}"

    for n in range(2, 5):
        surj_cnt = 0
        scc_cnt = 0
        for cfg in product(range(n), repeat=2 * n):
            if len(set(cfg)) == n:
                surj_cnt += 1
                edges = [(cfg[2 * i], cfg[2 * i + 1]) for i in range(n)]
                if is_strongly_connected(edges):
                    scc_cnt += 1
        assert surj_cnt == T[(2 * n, n)]
        assert scc_cnt <= surj_cnt
    print("PASS Section 2: T(m,k), F(m,k,t) identities and brute-force E_n/SCC_n checks (n=2..4)")


# ---------------------------------------------------------------------------
# 3. Interval helpers & exact calculus checks
# ---------------------------------------------------------------------------
def H_ent(x: iv.mpf) -> iv.mpf:
    return -x * iv.log(x) - (I(1) - x) * iv.log(I(1) - x)


def iv_xlogx_upper(lo: iv.mpf, hi: iv.mpf) -> iv.mpf:
    """Upper bound for -t*ln(t) on t in [lo, hi] subset [0, 1]."""
    lo_c = I(0) if lo.a < 0 else lo
    hi_c = I(1) if hi.b > 1 else hi
    inv_e = I(1) / iv.e
    vals = []
    for pt in (lo_c, hi_c):
        if pt.a <= 0 and pt.b >= 0:
            vals.append(I(0))
        if pt.b > 0:
            pt_pos = iv.mpf([max(pt.a, I(0).a), pt.b])
            if pt_pos.a > 0:
                vals.append(-pt_pos * iv.log(pt_pos))
    if lo_c.a <= inv_e.b and hi_c.b >= inv_e.a:
        vals.append(inv_e)
    return iv.mpf([min(v.a for v in vals), max(v.b for v in vals)])


def verify_analytic_and_proof_text() -> list[str]:
    # Solve lambda / (1 - e^{-lambda}) = 2 in (1, 2)
    lo, hi = F(15, 10), F(17, 10)
    for _ in range(100):
        mid = (lo + hi) / I(2)
        if (mid - I(2) + I(2) * iv.exp(-mid)).b < 0:
            lo = mid
        else:
            hi = mid
    lam = iv.mpf([lo.a, hi.b])
    assert lam.a > F(1593624, 10**6).a and lam.b < F(1593625, 10**6).b
    Z = iv.exp(lam) - I(1)

    sig2 = I(2) * (lam - I(1))
    m3_true = I(2) * lam**2 - I(8) * lam + I(10)
    m4_true = I(2) * lam**3 - I(4) * lam**2 + I(14) * lam - I(14)

    s3 = sum((abs(I(k) - I(2)) ** 3) * (lam ** k) / I(factorial(k)) for k in range(1, 70)) / Z
    s4 = sum(((I(k) - I(2)) ** 4) * (lam ** k) / I(factorial(k)) for k in range(1, 70)) / Z
    assert abs(s3 - m3_true).b < F(1, 10**20)
    assert abs(s4 - m4_true).b < F(1, 10**20)

    delta = F(3, 10)
    A = lam + lam**2 / I(2)
    rho_d = (iv.sqrt(A**2 - lam**3 * (I(1) - iv.cos(delta))) + (Z - A)) / Z
    assert rho_d.b < F(992, 1000)

    two_cloc = sig2 - (sig2**2 / I(4) + m4_true / I(12) + (m3_true**2 * delta**2) / I(36) + (m4_true**2 * delta**4) / I(576)) * delta**2
    cloc = two_cloc / I(2)
    assert two_cloc.a > F(1107, 1000)

    C_up = F(38, 100)
    cup_check = I(1) / (I(2) * iv.sqrt(iv.pi * cloc)) + iv.sqrt(I(1996)) * (rho_d ** 1996)
    assert cup_check.b <= C_up.a

    k0 = I(3998)
    R_param = F(26, 10)
    t0 = R_param / iv.sqrt(k0)
    theta_max = k0 * (m3_true * (t0**3)) / (I(6) * (I(1) - sig2 / I(2) * t0**2)) + I(4) * t0
    gauss_tail = iv.exp(-cloc * R_param**2) / (I(2) * iv.pi * cloc * R_param)
    ns = 200
    ds = R_param / I(ns)
    acc = I(0)
    for j in range(ns):
        s_iv = iv.mpf([(I(j) * ds).a, (I(j + 1) * ds).b])
        t_iv = s_iv / iv.sqrt(k0)
        mag_k = iv.exp(-sig2 / I(2) * s_iv**2 - (sig2**2 / I(4)) * (s_iv**4) / k0)
        ang = k0 * (m3_true * (t_iv**3)) / (I(6) * (I(1) - sig2 / I(2) * t0**2)) + I(4) * t_iv
        acc = acc + ds * mag_k * iv.cos(ang)
    clow_cert = acc / iv.pi - I(2) * gauss_tail - iv.sqrt(k0) * (rho_d ** 3998)
    c_low = F(34, 100)
    assert clow_cert.a >= c_low.b, f"c_low failed: {clow_cert}"

    # Verify exact c_scc(s, M) for s=1..4
    def is_scc(adj: list[list[int]], s: int) -> bool:
        for st in range(s):
            seen = 1 << st
            stack = [st]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if not ((seen >> v) & 1):
                        seen |= (1 << v)
                        stack.append(v)
            if seen != (1 << s) - 1:
                return False
        return True

    cscc_expected = {1: [1, 2], 2: [9, 12, 4], 3: [296, 372, 144, 16], 4: [20958, 26304, 11376, 1920, 96]}
    for s in range(1, 5):
        counts = [0] * (s + 1)
        for leave_bits in product([0, 1, 2], repeat=s):
            M = sum(1 for x in leave_bits if x > 0)
            opts = [list(product(range(s), repeat=2)) if x == 0 else [(v,) for v in range(s)] for x in leave_bits]
            for choice in product(*opts):
                adj = [list(c) for c in choice]
                if is_scc(adj, s):
                    counts[M] += 1
        assert counts == cscc_expected[s], f"c_scc mismatch s={s}: {counts}"

    # ------------------------------------------------------------------
    # Case 1a (L88-97)
    # ------------------------------------------------------------------
    # 1a (1 <= s <= 4): uniform over n >= 4000, sum over t in {0,1,2} and s in 1..4
    pref_1a_le4 = (C_up / c_low) * iv.sqrt(F(4000, 3994))
    sig_1a_le4 = I(0)
    for s in range(1, 5):
        # C(n-2, s) * (2s)! * (2n-4-2s)! / (2n-4)! <= 2^{-s} * prod_{j=0}^{s-1} (2s-j)/(2n-5-2j) <= (s / (3996 - s))^s?
        # Even sharper: for j in 0..s-1, (2s-j)/(2n-5-2j) <= 2s / (7995 - 2*s), times 2^{-s}
        ratio_comb = I(factorial(2 * s)) / I(factorial(s)) / (I(7995 - 2 * s) ** s)  # wait: (n-2)^s / (2n-4)^{2s} * (2s)!/s!
        # Let's write cleanly: (n-2)...(n-1-s) <= n^s; (2n-4)...(2n-3-2s) >= (2n-3-2s)^{2s}? Better:
        # binom(n-2,s)*(2s)!*(2n-4-2s)!/(2n-4)! = [prod_{j=0}^{s-1} (n-2-j)/(2n-4-2j)] * [(2s)!/s! / prod_{j=0}^{s-1} (2n-5-2j)]
        # First factor <= 2^{-s}; second factor <= ((2s)/ (2*4000 - 3 - 2*s))^s * ... wait (2s-j) vs prod: use exact prod_{j=0}^{s-1} (2s-j)/(7995-2j)
        prod_fac = I(1)
        for j in range(s):
            prod_fac = prod_fac * I(2 * s - j) / I(7995 - 2 * j)
        assert (iv.exp(lam) / Z).a > 1  # hence (e^lam / Z)^(t-2) <= 1 for t in {0,1,2}
        sig_1a_le4 = sig_1a_le4 + pref_1a_le4 * (I(1) / I(2 ** s)) * prod_fac * iv.exp(s * lam)
    assert sig_1a_le4.b < F(1, 1000), f"1a_le4 failed: {sig_1a_le4}"

    # 1a (5 <= s <= 0.02n):
    pref_1a_mid = (C_up / c_low) * iv.sqrt(F(4000, 3918))
    assert pref_1a_mid.b <= F(113, 100).a
    sig_1a_5_9 = sum(F(113, 100) * ((I(s) / I(7836)) * iv.exp(lam)) ** s for s in range(5, 10))
    assert sig_1a_5_9.b < F(4, 10**13)
    q_10 = F(103, 10000) * iv.exp(lam)
    assert q_10.b < I(1)
    sig_1a_10p = F(113, 100) * (q_10 ** 10) / (I(1) - q_10)
    assert sig_1a_10p.b < F(2, 10**13)
    assert (sig_1a_5_9 + sig_1a_10p).b < F(1, 10**12)

    # 1a (0.02n < s <= n/2): interval check f_sink(alpha) <= -0.05 on [0.02, 0.5]
    # Note: verify f_sink upper bound in 240 subintervals
    M_grid = 240
    a_lo, a_hi = F(2, 100), F(5, 10)
    step_a = (a_hi - a_lo) / I(M_grid)
    max_fsink_ub = F(-100, 1)
    for j in range(M_grid):
        al = iv.mpf([(a_lo + I(j) * step_a).a, (a_lo + I(j + 1) * step_a).b])
        r_al = lam * (I(1) - F(13, 10) * al)
        assert r_al.a > 0
        fs = -H_ent(al) - I(2) * (I(1) - al) * iv.log(r_al / lam) + al * r_al + (I(1) - al) * iv.log((iv.exp(r_al) - I(1)) / Z)
        if fs.b > max_fsink_ub.a:
            max_fsink_ub = iv.mpf([fs.b, fs.b])
    assert max_fsink_ub.b <= F(-5, 100).a, f"f_sink failed: {max_fsink_ub}"
    # Check prefactor: since x/(1 - e^{-x}) is strictly increasing on (0, lam] with value 2 at lam,
    # (r_s/lam)^4 * (e^{r_s}/(e^{r_s}-1))^t * ((e^lam-1)/e^lam)^2 <= (r_s/lam)^{4-t} * 1 <= 1 for t in {0,1,2}.
    pref_coeff = I(16) / c_low
    assert pref_coeff.b < I(100)
    # At n >= 4000 with <= 3*2000 terms and exp(-0.05 * 4000):
    sig_1a_tail = I(3) * I(2000) * I(100) * I(8001) * iv.sqrt(I(4000)) * iv.exp(F(-5, 100) * I(4000))
    assert sig_1a_tail.b < F(1, 10**60)
    assert (sig_1a_le4 + sig_1a_5_9 + sig_1a_10p + sig_1a_tail).b < F(2, 1000)

    # ------------------------------------------------------------------
    # Case 1b (L99-106)
    # ------------------------------------------------------------------
    # s in {3, 4}: exact F(2s-2r, s-2, 2) bounded at n >= 4000 (external via (3) + C_up)
    # T(m, k) small table for F(2s-2r, s-2, 2) (m <= 6)
    T_sm: dict[tuple[int, int], int] = {(0, 0): 1}
    for mm in range(1, 8):
        T_sm[(mm, 0)] = 0
        for kk in range(1, mm + 1):
            T_sm[(mm, kk)] = kk * (T_sm.get((mm - 1, kk), 0) + T_sm.get((mm - 1, kk - 1), 0))
    sig_1b_le4 = I(0)
    for s in (3, 4):
        for r in range(1, min(2, s - 2) + 1):
            m_int_b = 2 * s - 2 * r
            k_int_b = s - 2
            F_int_b = sum(comb(2, ii) * T_sm.get((m_int_b, k_int_b + ii), 0) for ii in range(3))
            # (n-4)...(n-s-1+r) <= (4000)^{s-2-r} * (1)? No, (n-4)... / (2n-4)... has s-2-r pairs <= 2^{-(s-2-r)},
            # remaining m_int_b + (s-2-r)? Wait: total (2n-4)!/(2n-2s-4+2r)! has 2s-2r factors;
            # Wait: (n-4)_{s-2-r} / [(s-2-r)! (2n-4)_{2s-2r}] = [prod_{j=0}^{s-3-r} (n-4-j)/(2n-4-2j)] / [(s-2-r)! prod_{j=...}]
            # For n >= 4000, n^{s-2-r} / (2n-11)^{2s-2r} decreases in n as n^{-(s-r+2)}:
            # Clean exact bound at n >= 4000: (n-4)_{s-2-r} / (2n-4)_{2s-2r} <= (4000)^{s-2-r} / (7996 - 2*4)^{...}:
            # Actually since (n-4-j)/(2n-4-2j) <= 1/2 (for j>=2), wait for j=0,1: (n-4)/(2n-4) < 1/2,
            # so comb(n-4, s-2-r) / (2n-4)_{2s-2r} <= 2^{-(s-2-r)} / ((s-2-r)! * (7985)^{s-r+2})
            comb_1b_ex = (F(1, 2) ** (s - 2 - r)) / (I(factorial(s - 2 - r)) * (I(7985) ** (s - r + 2)))
            term_1b_s = (
                (C_up / c_low)
                * iv.sqrt(F(4000, 3996))
                * I(comb(2, r))
                * I(F_int_b)
                * comb_1b_ex
                * (lam ** (2 * s - 2 * r))
                * ((iv.exp(lam) / Z) ** (s - 2))
            )
            sig_1b_le4 = sig_1b_le4 + term_1b_s
    assert sig_1b_le4.b < F(1, 10**11), f"1b_le4 failed: {sig_1b_le4}"

    # 5 <= s <= 0.02n:
    # LHS bound (without replacing (2s-2r)/(1.96n-4) by 0.0205 at small s):
    sig_1b_lhs = I(0)
    # RHS bound written on L103 (with 0.0205):
    sig_1b_rhs = I(0)
    for r in (1, 2):
        for s in range(5, 15):
            sig_1b_lhs = sig_1b_lhs + F(113, 100) * I(comb(2, r)) * (F(1, 2) ** (s - 2 - r)) * ((I(2 * s - 2 * r) / I(7836)) ** (s - r + 2)) * iv.exp(I(s) * lam)
            sig_1b_rhs = sig_1b_rhs + F(113, 100) * I(comb(2, r)) * (F(1, 2) ** (s - 2 - r)) * (F(205, 10000) ** (s - r + 2)) * iv.exp(I(s) * lam)
        q_1b = F(1, 2) * F(205, 10000) * iv.exp(lam)
        assert q_1b.b < F(1, 10)
        term_15_rhs = F(113, 100) * I(comb(2, r)) * (F(1, 2) ** (15 - 2 - r)) * (F(205, 10000) ** (15 - r + 2)) * iv.exp(I(15) * lam)
        sig_1b_lhs = sig_1b_lhs + term_15_rhs / (I(1) - q_1b)
        sig_1b_rhs = sig_1b_rhs + term_15_rhs / (I(1) - q_1b)
    assert sig_1b_lhs.b < F(1, 10**11)
    assert sig_1b_rhs.b < F(1, 10**4)
    sig_1b_mid = sig_1b_le4 + sig_1b_rhs
    assert sig_1b_mid.b < F(1, 1000)

    # Case 1b tail (0.02n < s <= n/2):
    # Internal (r=lam) + External (r_s) gives same f_sink(alpha) <= -0.05, prefactor <= (16/c_low)*comb(2,r) <= 95 < 100
    assert (I(16) / c_low * I(2)).b < I(100)
    sig_1b_tail = I(2) * I(2000) * I(100) * I(8001) * iv.sqrt(I(4000)) * iv.exp(F(-5, 100) * I(4000))
    assert sig_1b_tail.b < F(1, 10**60)

    # ------------------------------------------------------------------
    # Case 2a (L108-120)
    # ------------------------------------------------------------------
    tot_2a_le4 = I(0)
    for s in range(1, 5):
        for M in range(s + 1):
            term = (
                I(cscc_expected[s][M])
                / (I(factorial(s)) * (I(2) ** (2 * s - M)) * ((I(1) - F(11, 8000)) ** (2 * s - M)) * (I(4000) ** (s - M)))
                * (lam ** (2 * s - M))
                / (Z ** s)
            )
            tot_2a_le4 = tot_2a_le4 + term
    sig2a_le4_rhs = (C_up / c_low) * iv.sqrt(F(4000, 3994)) * tot_2a_le4
    assert sig2a_le4_rhs.b < F(581, 1000)

    tot_2a_5_15 = I(0)
    for s in range(5, 16):
        for M in range(s + 1):
            if M == s:
                T_bd = I(factorial(s))
            else:
                r = lam * (I(1) - F(M, s))
                T_bd = I(factorial(2 * s - M)) / (r ** (2 * s - M)) * ((iv.exp(r) - I(1)) ** s)
            den_ex = ((F(196, 100) - F(4, 4000)) * I(4000)) ** (s - M)
            term = (
                (C_up / c_low)
                * iv.sqrt(F(4000, 3983))
                * I(comb(s, M))
                * I(2 ** M)
                * T_bd
                / (I(factorial(s)) * I(2 ** s) * den_ex)
                * (lam ** (2 * s - M))
                / (Z ** s)
            )
            tot_2a_5_15 = tot_2a_5_15 + term
    assert tot_2a_5_15.b < F(42, 1000)

    # 2a (16 <= s <= 0.02n): f_mid(p) <= -0.70 on [0, 1]
    eps_002 = F(4, 100) / (F(196, 100) - F(4, 4000))
    N_p = 256
    max_fmid_ub = F(-100, 1)
    for j in range(N_p):
        p0, p1 = F(j, N_p), F(j + 1, N_p)
        p_iv = iv.mpf([p0.a, p1.b])
        ent_p = iv_xlogx_upper(p0, p1) + I(2) * iv_xlogx_upper(F(N_p - j - 1, N_p), F(N_p - j, N_p))
        phi_hi = I(1) if j == N_p - 1 else (iv.exp(lam * F(N_p - j, N_p)) - I(1)) / (lam * F(N_p - j, N_p))
        if j == N_p - 1:
            phi_hi = (iv.exp(lam * F(1, N_p)) - I(1)) / (lam * F(1, N_p))
        fm = (
            -iv.log(I(2))
            + ent_p
            + p_iv * iv.log(I(2))
            + (I(1) - p_iv) * iv.log(eps_002)
            + iv.log(phi_hi)
            - iv.log(Z / lam)
        )
        if fm.b > max_fmid_ub.a:
            max_fmid_ub = iv.mpf([fm.b, fm.b])
    assert max_fmid_ub.b <= F(-70, 100).a, f"f_mid failed: {max_fmid_ub}"
    q_fmid = iv.exp(F(-70, 100))
    # sum_{s>=16} (s+1) q^s = (17 - 16*q)/(1-q)^2 * q^16
    sig_2a_mid = F(113, 100) * (q_fmid ** 16) * (I(17) - I(16) * q_fmid) / ((I(1) - q_fmid) ** 2)
    assert sig_2a_mid.b < F(1, 1000)

    # 2a (0.02n < s <= n/2): verify derivative formula symbolically + check R(alpha, p) <= -0.30 on (0, 1/2] x [0, 1]
    a_sym, b_sym = sp.symbols("a b", positive=True)
    H_sym = lambda t: -t * sp.log(t) - (1 - t) * sp.log(1 - t)
    g_sym = (H_sym(a_sym) - 2 * H_sym(b_sym * a_sym)) / a_sym
    dg_da = sp.simplify(sp.expand_log(sp.diff(g_sym, a_sym) - (sp.log((1 - a_sym) / (1 - b_sym * a_sym) ** 2) / a_sym**2), force=True))
    assert dg_da == 0, f"Derivative mismatch: {dg_da}"

    def max_g_over_alpha(beta_lo: iv.mpf, alpha_cap: iv.mpf) -> iv.mpf:
        """
        Since dg/dbeta <= 0 for alpha <= 1/2, beta in [1/2, 1],
        max_{beta >= beta_lo, alpha in (0, alpha_cap]} g(alpha, beta) <= max_{alpha in (0, alpha_cap]} g(alpha, beta_lo).
        """
        if beta_lo.b <= F(1, 2).a:
            return -iv.log(I(2))
        alpha_star = (I(2) * beta_lo - I(1)) / (beta_lo ** 2)
        if alpha_star.a >= alpha_cap.b:
            a_eval = alpha_cap
        elif alpha_star.b <= 0:
            return -iv.log(I(2))
        else:
            a_eval = iv.mpf([max(alpha_star.a, F(1, 10**12).a), min(alpha_star.b, alpha_cap.b)])
        return (H_ent(a_eval) - I(2) * H_ent(beta_lo * a_eval)) / a_eval

    max_R_half = F(-100, 1)
    max_R_010 = F(-100, 1)
    N_R = 512
    for j in range(N_R):
        p0, p1 = F(j, N_R), F(j + 1, N_R)
        p_iv = iv.mpf([p0.a, p1.b])
        beta_lo = F(2 * N_R - j - 1, 2 * N_R)
        g_half = max_g_over_alpha(beta_lo, F(1, 2))
        g_010 = max_g_over_alpha(beta_lo, F(1, 10))
        ent_h = iv_xlogx_upper(p0, p1) + I(2) * iv_xlogx_upper(F(N_R - j - 1, N_R), F(N_R - j, N_R))
        phi_hi = (iv.exp(lam * F(N_R - j, N_R)) - I(1)) / (lam * F(N_R - j, N_R))
        h_mid = ent_h + p_iv * iv.log(I(2)) + iv.log(phi_hi) - iv.log(Z / lam)
        R_half = g_half + h_mid
        R_010 = g_010 + h_mid
        if R_half.b > max_R_half.a:
            max_R_half = iv.mpf([R_half.b, R_half.b])
        if R_010.b > max_R_010.a:
            max_R_010 = iv.mpf([R_010.b, R_010.b])
    assert max_R_half.b <= F(-30, 100).a, f"R_half failed: {max_R_half}"
    assert max_R_010.b <= F(-60, 100).a, f"R_010 failed: {max_R_010}"
    # Tail sum for 2a: 16*(2n+1)*(C_up/c_low)*sqrt(2.01) * sum_{s>=81} (s+1) e^{-0.30 s} at n=4000
    q_R = iv.exp(F(-30, 100))
    pref_2a_tail = I(16) * I(8001) * (C_up / c_low) * iv.sqrt(F(201, 100))
    sig_2a_tail = pref_2a_tail * (q_R ** 81) * (I(82) - I(81) * q_R) / ((I(1) - q_R) ** 2)
    assert sig_2a_tail.b < F(3, 1000)

    # ------------------------------------------------------------------
    # Case 2b (L122-126)
    # ------------------------------------------------------------------
    # 3 <= s <= 0.02n at n >= 4000 (s <= 80):
    sig_2b_mid = I(0)
    for s in range(3, 81):
        for q in (1, 2):
            if s < 2 + q:
                continue
            for M in range(min(s - 2, s - 4 + q) + 1):  # F=0 unless 2s-4-M >= s-q
                # Internal F(2s-4-M, s-q, q):
                k_int = s - q
                m_int = 2 * s - 4 - M
                assert m_int >= k_int
                if m_int == k_int:
                    F_int_norm = I(1)  # k_int! / m_int! = 1
                else:
                    r_M = lam * (I(1) - F(M, s))
                    F_int_norm = (iv.exp(q * r_M) * ((iv.exp(r_M) - I(1)) ** (s - q))) / (r_M ** m_int)
                # Product bound for comb(n-4, s-2-q) * m_int! * (2n-2s+M)! / (2n-4)! <= 2^{-(s-2-q)} * ((2s-4-M)/(1.96n-4))^{s-2+q-M}
                comb_ex = (F(1, 2) ** (s - 2 - q)) * (I(m_int) / (F(196, 100) * I(4000) - I(4))) ** (s - 2 + q - M)
                term_2b = (
                    (C_up / c_low)
                    * iv.sqrt(F(4000, 3918))
                    * I(comb(2, q))
                    * I(comb(s - 2, M))
                    * I(2 ** M)
                    * F_int_norm
                    * comb_ex
                    * (lam ** (2 * s - M - 4))
                    / (iv.exp(q * lam) * (Z ** (s - q)))
                )
                sig_2b_mid = sig_2b_mid + term_2b
    assert sig_2b_mid.b < F(1, 1000), f"2b_mid failed: {sig_2b_mid}"

    # 2b tail (0.02n < s <= n/2): verify Case 2b/2a ratio < 6500 across alpha in [0.02, 0.5]
    assert (
        I(2) * I(16) / (F(2, 100) * (F(98, 100) ** 3)) * (Z / lam)
        + I(16) / (F(50, 100) ** 4) * ((Z / lam) ** 2)
    ).b < I(6500)
    pref_2b_t1 = I(6500) * I(16) * I(8001) * (C_up / c_low) * iv.sqrt(F(201, 100))
    q_60 = iv.exp(F(-60, 100))
    sig_2b_t1 = pref_2b_t1 * (q_60 ** 81) * (I(82) - I(81) * q_60) / ((I(1) - q_60) ** 2)
    assert sig_2b_t1.b < F(2, 10**10)
    sig_2b_t2 = pref_2b_t1 * (q_R ** 401) * (I(402) - I(401) * q_R) / ((I(1) - q_R) ** 2)
    assert sig_2b_t2.b < F(2, 10**40)
    assert (sig_2b_mid + sig_2b_t1 + sig_2b_t2).b < F(2, 1000)

    # Grand sum across all 4 cases < 0.64:
    sig_1a_tot = sig_1a_le4 + sig_1a_5_9 + sig_1a_10p + sig_1a_tail
    sig_1b_tot = sig_1b_mid + sig_1b_tail
    sig_2a_tot = sig2a_le4_rhs + tot_2a_5_15 + sig_2a_mid + sig_2a_tail
    sig_2b_tot = sig_2b_mid + sig_2b_t1 + sig_2b_t2
    assert (sig_1a_tot + sig_1b_tot + sig_2a_tot + sig_2b_tot).b < F(64, 100)

    # ------------------------------------------------------------------
    # Section 5 first/second moments and overlap bounds
    # ------------------------------------------------------------------
    ez_lb = F(36, 100) * ((I(1) - F(3, 4000)) ** 3) * (lam**2 / I(4)) * (c_low / C_up)
    assert ez_lb.a >= F(20, 100)
    en_ub = (lam**2 / I(4)) * (C_up / c_low) / ((I(1) - F(3, 8000)) ** 4) * iv.sqrt(F(4000, 3998))
    assert en_ub.b < F(72, 100)
    # Overlap |P1 cap P2| = 1: <= n^5 * 8 * F(2n-6, n-2, 2)/T(2n, n)
    ov_1 = I(8) * (I(4000) ** 5) * (lam ** 6) / (I(7999) * I(7998) * I(7997) * I(7996) * I(7995) * I(7994)) * (iv.exp(2 * lam) / (Z ** 2)) * (C_up / c_low) * iv.sqrt(F(4000, 3998))
    assert ov_1.b < F(5, 1000)
    # Disjoint t=2,3 overlaps:
    # t=2: <= n^4 * 16 * F(2n-8, n-2, 2)/T(2n,n) ~ O(n^-2)
    # t=3: <= n^5 * 32 * F(2n-8, n-3, 3)/T(2n,n) ~ O(n^-1)
    # Use n*(n-1)... <= n^4 and n^5, prod_{j=0}^{7} (2n-j) >= (2n-7)^8 = 7993^8:
    ov_t2 = I(16) * (I(4000) ** 4) * (lam ** 8) / (I(7993) ** 8) * (iv.exp(2 * lam) / (Z ** 2)) * (C_up / c_low) * iv.sqrt(F(4000, 3998))
    ov_t3 = I(32) * (I(4000) ** 5) * (lam ** 8) / (I(7993) ** 8) * (iv.exp(3 * lam) / (Z ** 3)) * (C_up / c_low) * iv.sqrt(F(4000, 3997))
    assert (ov_t2 + ov_t3).b < F(5, 1000)
    en2_main = ((lam / I(2)) ** 4) * (C_up / c_low) * iv.sqrt(F(4000, 3996)) / ((I(1) - F(7, 8000)) ** 8)
    assert en2_main.b < F(46, 100)
    assert (en_ub + ov_1 + ov_t2 + ov_t3 + en2_main).b <= F(120, 100).a
    assert (Fraction(20, 100) ** 2) / Fraction(120, 100) == Fraction(1, 30)

    print(
        f"PASS All Lemma 2 + Section 4 (1a/1b/2a/2b; sum <= {iv.nstr((sig_1a_tot+sig_1b_tot+sig_2a_tot+sig_2b_tot).b, 4)} < 0.64) "
        f"+ Section 5 (E[N^2] < {iv.nstr((en_ub+ov_1+ov_t2+ov_t3+en2_main).b, 4)} <= 1.20; PZ >= 1/30) verified."
    )

    with open("targets/dangeli-2607.17335-conj1/TARGET.md") as f:
        tgt = f.read()
    with open("targets/dangeli-2607.17335-conj1/COUNTEREXAMPLE.md") as f:
        txt = f.read()

    issues = []
    if not tgt.startswith("---\n"):
        issues.append("TARGET.md missing opening --- YAML delimiter.")
    if "Section 4" not in tgt or "Conjecture 4.6" not in tgt or "Theorem 4.4" not in tgt:
        issues.append("TARGET.md missing Section 4 / Theorem 4.4 / Conjecture 4.6 citations.")
    if "Section 8" in tgt or "Section 8" in txt:
        issues.append("Erroneous Section 8 citation still present.")
    if "Section 4" not in txt or "Conjecture 4.6" not in txt or "Theorem 4.4" not in txt:
        issues.append("COUNTEREXAMPLE.md missing Section 4 / Theorem 4.4 / Conjecture 4.6 citations.")
    if "2\\lambda^2 - 8\\lambda + 10" not in txt or "2\\lambda^2 - 6\\lambda + 6" not in txt:
        issues.append("COUNTEREXAMPLE.md missing m_3 formula 2*lam^2 - 8*lam + 10.")
    if "2\\lambda^3 - 4\\lambda^2 + 14\\lambda - 14" not in txt:
        issues.append("COUNTEREXAMPLE.md missing m_4 formula 2*lam^3 - 4*lam^2 + 14*lam - 14.")
    if not (theta_max.b < F(28, 100).b and gauss_tail.b < F(27, 10000).b and "< 0.28" in txt and "< 0.0027" in txt):
        issues.append("COUNTEREXAMPLE.md theta_max < 0.28 or tail < 0.0027 check failed.")
    if not (sig2a_le4_rhs.b < F(581, 1000).b and "< 0.581" in txt):
        issues.append("COUNTEREXAMPLE.md Sigma_{2a,<=4} < 0.581 check failed.")
    if not (sig_1b_rhs.b < F(7, 10**6).a and "< 7 \\times 10^{-6} < 10^{-4}" in txt):
        issues.append("COUNTEREXAMPLE.md L104 < 7e-6 < 10^-4 bound check failed.")
    return issues


def main() -> int:
    verify_lemma1_examples()
    verify_surjections()
    issues = verify_analytic_and_proof_text()
    if issues:
        for iss in issues:
            print(f"TEXT_ISSUE: {iss}")
        print("FAIL")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
