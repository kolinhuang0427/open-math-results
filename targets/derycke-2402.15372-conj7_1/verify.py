"""Exact-arithmetic verification script for PROOF.md (Conjecture 6.1 / conj:ITCCTIsymmetry).

Zero floating-point operations and zero '/' true-division operators anywhere.
All polynomial and combinatorial arithmetic is performed exactly over Z.
"""

from __future__ import annotations

from itertools import combinations_with_replacement
from math import comb
import sys
import time
from sympy import Poly, symbols


# ---------------------------------------------------------------------------
# Pure integer univariate polynomials in Z[q]: dict[int, int]
# and bivariate polynomials in Z[q, t] or Z[q, u]: dict[tuple[int, int], int]
# ---------------------------------------------------------------------------

PolyQ = dict[int, int]
Poly2 = dict[tuple[int, int], int]
PolyXY = dict[tuple[int, int], Poly2]


def q_add(a: PolyQ, b: PolyQ) -> PolyQ:
    res = dict(a)
    for deg, coeff in b.items():
        val = res.get(deg, 0) + coeff
        if val:
            res[deg] = val
        else:
            res.pop(deg, None)
    return res


def q_mul(a: PolyQ, b: PolyQ) -> PolyQ:
    if not a or not b:
        return {}
    res: PolyQ = {}
    for da, ca in a.items():
        for db, cb in b.items():
            d = da + db
            res[d] = res.get(d, 0) + ca * cb
    return {d: c for d, c in res.items() if c}


def q_shift(a: PolyQ, shift: int) -> PolyQ:
    if not a or shift == 0:
        return dict(a)
    return {d + shift: c for d, c in a.items()}


_Q_BINOM_CACHE: dict[tuple[int, int], PolyQ] = {}


def q_binom(m: int, k: int) -> PolyQ:
    """Exact q-binomial coefficient [m choose k]_q in Z[q] via q-Pascal recurrence."""
    if k < 0 or k > m:
        return {}
    if k == 0 or k == m:
        return {0: 1}
    key = (m, k)
    cached = _Q_BINOM_CACHE.get(key)
    if cached is not None:
        return cached
    res = q_add(q_binom(m - 1, k), q_shift(q_binom(m - 1, k - 1), m - k))
    _Q_BINOM_CACHE[key] = res
    return res


def q_trinom(m: int, k1: int, k2: int, k3: int) -> PolyQ:
    """Exact q-trinomial coefficient [m choose k1, k2, k3]_q in Z[q]."""
    if k1 < 0 or k2 < 0 or k3 < 0 or k1 + k2 + k3 != m:
        return {}
    return q_mul(q_binom(m, k1), q_binom(m - k1, k2))


def p2_add(a: Poly2, b: Poly2) -> Poly2:
    res = dict(a)
    for key, coeff in b.items():
        val = res.get(key, 0) + coeff
        if val:
            res[key] = val
        else:
            res.pop(key, None)
    return res


def p2_add_inplace(acc: Poly2, poly: Poly2, shift0: int = 0, shift1: int = 0) -> None:
    for (d0, d1), coeff in poly.items():
        key = (d0 + shift0, d1 + shift1)
        val = acc.get(key, 0) + coeff
        if val:
            acc[key] = val
        else:
            acc.pop(key, None)


def p2_add_qpoly(acc: Poly2, qpoly: PolyQ, shift0: int = 0, shift1: int = 0) -> None:
    for dq, coeff in qpoly.items():
        key = (dq + shift0, shift1)
        val = acc.get(key, 0) + coeff
        if val:
            acc[key] = val
        else:
            acc.pop(key, None)


def p2_mul(a: Poly2, b: Poly2) -> Poly2:
    if not a or not b:
        return {}
    res: Poly2 = {}
    for (a0, a1), ca in a.items():
        for (b0, b1), cb in b.items():
            key = (a0 + b0, a1 + b1)
            res[key] = res.get(key, 0) + ca * cb
    return {k: v for k, v in res.items() if v}


def p2_shift(a: Poly2, s0: int = 0, s1: int = 0) -> Poly2:
    if not a or (s0 == 0 and s1 == 0):
        return dict(a)
    return {(d0 + s0, d1 + s1): c for (d0, d1), c in a.items()}


def xy_add(a: PolyXY, b: PolyXY) -> PolyXY:
    res = dict(a)
    for deg_xy, p2 in b.items():
        if deg_xy in res:
            merged = p2_add(res[deg_xy], p2)
            if merged:
                res[deg_xy] = merged
            else:
                res.pop(deg_xy)
        else:
            if p2:
                res[deg_xy] = dict(p2)
    return res


def xy_mul(a: PolyXY, b: PolyXY) -> PolyXY:
    if not a or not b:
        return {}
    res: PolyXY = {}
    for (xa, ya), pa in a.items():
        for (xb, yb), pb in b.items():
            prod = p2_mul(pa, pb)
            if not prod:
                continue
            key = (xa + xb, ya + yb)
            if key in res:
                merged = p2_add(res[key], prod)
                if merged:
                    res[key] = merged
                else:
                    res.pop(key)
            else:
                res[key] = prod
    return res


# ---------------------------------------------------------------------------
# Propositions 1.1 and 2.1 cell formulas
# ---------------------------------------------------------------------------

def cell_cti_polys(n: int, d: int) -> dict[int, Poly2]:
    """Compute F_{n, d, r}^{CTI}(q, t) for 1 <= r <= n + d via Proposition 1.1."""
    result: dict[int, Poly2] = {r: {} for r in range(1, n + d + 1)}

    def dfs(
        step: int,
        rem_p: int,
        rem_q: int,
        prev_p: int,
        prev_q: int,
        q_poly: PolyQ,
        q_shift_acc: int,
        t_shift_acc: int,
        r_first: int,
    ) -> None:
        if rem_p == 0 and rem_q == 0:
            p2_add_qpoly(result[r_first], q_poly, shift0=q_shift_acc, shift1=t_shift_acc)
            return
        if rem_p == 0:
            # For i >= 2, p_i >= 1 is required, so no further step is possible.
            return
        min_p = 0 if step == 1 else 1
        for p_i in range(min_p, rem_p + 1):
            for q_i in range(0, rem_q + 1):
                if step == 1:
                    if p_i + q_i == 0:
                        continue
                    r_val = p_i + q_i
                    step_poly = q_binom(r_val, q_i)
                else:
                    r_val = r_first
                    f1 = q_binom(p_i + prev_p + prev_q - 1, p_i)
                    f2 = q_binom(p_i + q_i - 1, q_i)
                    step_poly = q_mul(f1, f2)
                if not step_poly:
                    continue
                next_poly = q_mul(q_poly, step_poly)
                if not next_poly:
                    continue
                dfs(
                    step + 1,
                    rem_p - p_i,
                    rem_q - q_i,
                    p_i,
                    q_i,
                    next_poly,
                    q_shift_acc + p_i * (p_i - 1) // 2,
                    t_shift_acc + (step - 1) * (p_i + q_i),
                    r_val,
                )

    dfs(1, n, d, 0, 0, {0: 1}, 0, 0, 0)
    return result


def cell_itc_polys(n: int, d: int) -> dict[int, Poly2]:
    """Compute F_{n, d, r}^{ITC}(q, t) for 1 <= r <= n + d via Proposition 2.1."""
    result: dict[int, Poly2] = {r: {} for r in range(1, n + d + 1)}

    def dfs(
        step: int,
        rem_a: int,
        rem_b: int,
        prev_a: int,
        q_poly: PolyQ,
        q_shift_acc: int,
        t_shift_acc: int,
        r_first: int,
    ) -> None:
        if rem_a == 0 and rem_b == 0:
            p2_add_qpoly(result[r_first], q_poly, shift0=q_shift_acc, shift1=t_shift_acc)
            return
        if step > 1 and prev_a == 0:
            # In ITC, a_1, ..., a_{k-1} >= 1; a_k = 0 is only allowed at the last step.
            return
        min_a = 1 if step == 1 else 0
        for a_i in range(min_a, rem_a + 1):
            for b_i in range(0, rem_b + 1):
                if a_i + b_i == 0:
                    continue
                if step > 1 and a_i == 0 and rem_a > 0:
                    # a_i = 0 is only valid when this is the final step k (rem_a == 0).
                    continue
                r_val = a_i + b_i if step == 1 else r_first
                step_poly = q_trinom(a_i + b_i + prev_a - 1, a_i, b_i, prev_a - 1)
                if not step_poly:
                    continue
                next_poly = q_mul(q_poly, step_poly)
                if not next_poly:
                    continue
                dfs(
                    step + 1,
                    rem_a - a_i,
                    rem_b - b_i,
                    a_i,
                    next_poly,
                    q_shift_acc + a_i * (a_i - 1) // 2,
                    t_shift_acc + (step - 1) * (a_i + b_i),
                    r_val,
                )

    dfs(1, n, d, 1, {0: 1}, 0, 0, 0)
    return result


# ---------------------------------------------------------------------------
# Suite 1: Direct Abelian sandpile verification on S_{n, d} (n + d <= 7)
# ---------------------------------------------------------------------------

def run_suite_1() -> int:
    """Enumerate R_dec(S_{n, d}) via Dhar's burning test + CTI/ITC parallel toppling."""
    configs_checked = 0
    for total in range(1, 8):
        for n in range(1, total + 1):
            d = total - n
            direct_cti: dict[int, Poly2] = {r: {} for r in range(1, total + 1)}
            direct_itc: dict[int, Poly2] = {r: {} for r in range(1, total + 1)}
            recurrent_count = 0
            base_level_offset = n * d + n * (n - 1) // 2

            for a in combinations_with_replacement(range(total - 1, -1, -1), n):
                sum_a = sum(a)
                for b in combinations_with_replacement(range(n, -1, -1), d):
                    # Dhar's burning test via CTI parallel toppling after sink s topples
                    va = [x + 1 for x in a]
                    wb = [y + 1 for y in b]
                    toppled_v = [0] * n
                    toppled_w = [0] * d
                    cti_rounds: list[tuple[int, int]] = []

                    while True:
                        p_idx = [i for i in range(n) if va[i] >= total]
                        p_cnt = len(p_idx)
                        if p_cnt:
                            for i in range(n):
                                va[i] += p_cnt
                            for i in p_idx:
                                va[i] -= total + 1
                                toppled_v[i] += 1
                            for j in range(d):
                                wb[j] += p_cnt

                        q_idx = [j for j in range(d) if wb[j] >= n + 1]
                        q_cnt = len(q_idx)
                        if q_cnt:
                            for j in q_idx:
                                wb[j] -= n + 1
                                toppled_w[j] += 1
                            for i in range(n):
                                va[i] += q_cnt

                        if p_cnt == 0 and q_cnt == 0:
                            break
                        cti_rounds.append((p_cnt, q_cnt))

                    if not (all(t >= 1 for t in toppled_v) and all(t >= 1 for t in toppled_w)):
                        continue

                    # Verify Dhar's burning invariant: each vertex toppled exactly once and returned to (a, b)
                    if not (all(t == 1 for t in toppled_v) and all(t == 1 for t in toppled_w)):
                        raise AssertionError(f"Vertex toppled more than once in burning test for {(n, d)}: {a}, {b}")
                    if tuple(va) != a or tuple(wb) != b:
                        raise AssertionError(f"Burning test did not return to initial config for {(n, d)}: {a}, {b}")

                    recurrent_count += 1
                    configs_checked += 1

                    # ITC parallel toppling after sink s topples
                    va2 = [x + 1 for x in a]
                    wb2 = [y + 1 for y in b]
                    toppled_v2 = [0] * n
                    toppled_w2 = [0] * d
                    itc_rounds: list[tuple[int, int]] = []

                    while True:
                        q_idx = [j for j in range(d) if wb2[j] >= n + 1]
                        b_cnt = len(q_idx)
                        if b_cnt:
                            for j in q_idx:
                                wb2[j] -= n + 1
                                toppled_w2[j] += 1
                            for i in range(n):
                                va2[i] += b_cnt

                        p_idx = [i for i in range(n) if va2[i] >= total]
                        a_cnt = len(p_idx)
                        if a_cnt:
                            for i in range(n):
                                va2[i] += a_cnt
                            for i in p_idx:
                                va2[i] -= total + 1
                                toppled_v2[i] += 1
                            for j in range(d):
                                wb2[j] += a_cnt

                        if b_cnt == 0 and a_cnt == 0:
                            break
                        itc_rounds.append((b_cnt, a_cnt))

                    if not (all(t == 1 for t in toppled_v2) and all(t == 1 for t in toppled_w2)):
                        raise AssertionError(f"ITC did not topple every vertex once for {(n, d)}: {a}, {b}")
                    if tuple(va2) != a or tuple(wb2) != b:
                        raise AssertionError(f"ITC did not return to initial config for {(n, d)}: {a}, {b}")

                    level = sum_a + sum(b) - base_level_offset
                    if level < 0:
                        raise AssertionError(f"Negative level {level} for {(n, d)}: {a}, {b}")

                    r_cti = cti_rounds[0][0] + cti_rounds[0][1]
                    wtopple_cti = sum(idx * (p + q) for idx, (p, q) in enumerate(cti_rounds, 1))
                    t_exp_cti = wtopple_cti - total
                    key_cti = (level, t_exp_cti)
                    direct_cti[r_cti][key_cti] = direct_cti[r_cti].get(key_cti, 0) + 1

                    r_itc = itc_rounds[0][0] + itc_rounds[0][1]
                    wtopple_itc = sum(idx * (b_i + a_i) for idx, (b_i, a_i) in enumerate(itc_rounds, 1))
                    t_exp_itc = wtopple_itc - total
                    key_itc = (level, t_exp_itc)
                    direct_itc[r_itc][key_itc] = direct_itc[r_itc].get(key_itc, 0) + 1

            # Verify exact count formula: (1 / (n + 1)) * C(2n + d, n) * C(n + d, d)
            num = comb(2 * n + d, n) * comb(n + d, d)
            if num % (n + 1) != 0:
                raise AssertionError(f"Count formula not divisible by n+1 for {(n, d)}")
            expected_count = num // (n + 1)
            if recurrent_count != expected_count:
                raise AssertionError(
                    f"Recurrent count mismatch for {(n, d)}: got {recurrent_count}, expected {expected_count}"
                )

            # Verify refined equality and cell formulas
            prop1 = cell_cti_polys(n, d)
            prop2 = cell_itc_polys(n, d)
            total_cti: Poly2 = {}
            total_itc: Poly2 = {}
            for r in range(1, total + 1):
                if direct_cti[r] != direct_itc[r]:
                    raise AssertionError(f"Direct CTI != ITC for {(n, d)}, r={r}")
                if direct_cti[r] != prop1[r]:
                    raise AssertionError(f"Direct CTI != Prop 1.1 for {(n, d)}, r={r}")
                if direct_itc[r] != prop2[r]:
                    raise AssertionError(f"Direct ITC != Prop 2.1 for {(n, d)}, r={r}")
                p2_add_inplace(total_cti, direct_cti[r])
                p2_add_inplace(total_itc, direct_itc[r])
            if total_cti != total_itc:
                raise AssertionError(f"Total F_CTI != F_ITC for {(n, d)}")

    return configs_checked


# ---------------------------------------------------------------------------
# Suite 2: Propositions 1.1 & 2.1 cell-formula comparison (n + d <= 10)
# ---------------------------------------------------------------------------

def run_suite_2() -> dict[tuple[int, int, int], Poly2]:
    """Compare Prop 1.1 and Prop 2.1 for all n >= 1, d >= 0, n + d <= 10, 1 <= r <= n + d."""
    stored: dict[tuple[int, int, int], Poly2] = {}
    for total in range(1, 11):
        for n in range(1, total + 1):
            d = total - n
            c1 = cell_cti_polys(n, d)
            c2 = cell_itc_polys(n, d)
            for r in range(1, total + 1):
                if c1[r] != c2[r]:
                    raise AssertionError(f"Prop 1.1 != Prop 2.1 for (n={n}, d={d}, r={r})")
                stored[(n, d, r)] = c1[r]
    return stored


# ---------------------------------------------------------------------------
# Suite 3: Generating-function identity P~_r(X, Y) = P_r(X, Y)
# ---------------------------------------------------------------------------

def pi_poly_xy(r: int) -> PolyXY:
    """Compute Pi_r(X, Y) = sum_{a=0}^r q^{C(a, 2)} [r choose a]_q X^a Y^{r - a}."""
    res: PolyXY = {}
    for a in range(r + 1):
        qp = q_shift(q_binom(r, a), a * (a - 1) // 2)
        if qp:
            res[(a, r - a)] = {(dq, 0): c for dq, c in qp.items()}
    return res


def run_suite_3(cell_table: dict[tuple[int, int, int], Poly2]) -> int:
    """Verify P~_r^{(N)} = P_r^{(N)} for 1 <= r <= 6, r <= N <= 9 and match F_{n, d, r}."""
    max_deg = 9

    # 1. Compute H(n, d, a) in Z[q, t] for 1 <= a <= max_deg - 1, 0 <= n + d <= max_deg - 1
    H: dict[tuple[int, int, int], Poly2] = {}
    max_h_deg = max_deg - 1  # up to 8
    for a in range(1, max_h_deg + 1):
        for d in range(0, max_h_deg + 1):
            qp = q_binom(d + a - 1, d)
            H[(0, d, a)] = {(dq, 0): c for dq, c in qp.items()}
    for n in range(1, max_h_deg + 1):
        for d in range(0, max_h_deg - n + 1):
            for a in range(1, max_h_deg + 1):
                acc: Poly2 = {}
                for m in range(1, n + 1):
                    q_tri_base = m * (m - 1) // 2
                    for b in range(0, d + 1):
                        q_coeff = q_shift(q_trinom(m + b + a - 1, m, b, a - 1), q_tri_base)
                        if not q_coeff:
                            continue
                        sub = H[(n - m, d - b, m)]
                        if not sub:
                            continue
                        t_pow = (n - m) + (d - b)
                        q_as_p2 = {(dq, 0): c for dq, c in q_coeff.items()}
                        p2_add_inplace(acc, p2_mul(q_as_p2, sub), shift0=0, shift1=t_pow)
                H[(n, d, a)] = acc

    # Form P_r^{(N)}(X, Y) for 1 <= r <= 6, r <= N <= 9
    P_homog: dict[tuple[int, int], PolyXY] = {}
    for r in range(1, 7):
        for N in range(r, max_deg + 1):
            M = N - r
            poly_xy: PolyXY = {}
            for a in range(0, r + 1):
                q_front = q_shift(q_binom(r, a), a * (a - 1) // 2)
                if not q_front:
                    continue
                q_front_p2 = {(dq, 0): c for dq, c in q_front.items()}
                if a == 0:
                    if M == 0:
                        poly_xy = xy_add(poly_xy, {(0, r): q_front_p2})
                else:
                    for n_sub in range(0, M + 1):
                        d_sub = M - n_sub
                        h_val = H[(n_sub, d_sub, a)]
                        if not h_val:
                            continue
                        term = p2_mul(q_front_p2, h_val)
                        if term:
                            poly_xy = xy_add(poly_xy, {(a + n_sub, (r - a) + d_sub): term})
            P_homog[(r, N)] = poly_xy

    # 2. Compute K_{r, r'}(X, Y) and G~_r^{(M)}(X, Y) for 1 <= r <= max_h_deg, 0 <= M <= max_h_deg
    K_cache: dict[tuple[int, int], PolyXY] = {}
    for r in range(1, max_h_deg + 1):
        for rp in range(1, max_h_deg + 1):
            k_xy: PolyXY = {}
            for p in range(1, rp + 1):
                qp = q_shift(q_mul(q_binom(p + r - 1, p), q_binom(rp - 1, p - 1)), p * (p - 1) // 2)
                if qp:
                    k_xy[(p, rp - p)] = {(dq, 0): c for dq, c in qp.items()}
            K_cache[(r, rp)] = k_xy

    G_tilde: dict[tuple[int, int], PolyXY] = {}
    for r in range(1, max_h_deg + 1):
        G_tilde[(r, 0)] = {(0, 0): {(0, 0): 1}}
    for M in range(1, max_h_deg + 1):
        for r in range(1, max_h_deg + 1):
            acc_xy: PolyXY = {}
            for rp in range(1, M + 1):
                g_sub = G_tilde[(rp, M - rp)]
                if not g_sub:
                    continue
                t_pow = M - rp
                g_shifted = {deg_xy: p2_shift(p2, s1=t_pow) for deg_xy, p2 in g_sub.items()}
                prod = xy_mul(K_cache[(r, rp)], g_shifted)
                acc_xy = xy_add(acc_xy, prod)
            G_tilde[(r, M)] = acc_xy

    # Form P~_r^{(N)}(X, Y) and compare with P_r^{(N)}(X, Y) and F_{n, d, r}
    checks = 0
    for r in range(1, 7):
        pi_r = pi_poly_xy(r)
        for N in range(r, max_deg + 1):
            p_tilde = xy_mul(pi_r, G_tilde[(r, N - r)])
            p_itc = P_homog[(r, N)]
            if p_tilde != p_itc:
                raise AssertionError(f"P~_r^(N) != P_r^(N) for r={r}, N={N}")
            checks += 1

            # Verify t^{-r} P_r(tx, ty) = y^r + sum_{n >= 1, d >= 0} F_{n, d, r} x^n y^d
            if N == r:
                if p_itc.get((0, r)) != {(0, 0): 1}:
                    raise AssertionError(f"[X^0 Y^r] P_r^(r) != 1 for r={r}")
            else:
                if (0, N) in p_itc:
                    raise AssertionError(f"Unexpected [X^0 Y^{N}] term in P_{r}^({N})")

            for n in range(1, N + 1):
                d = N - n
                coeff_p = p2_shift(p_itc.get((n, d), {}), s1=N - r)
                coeff_tilde = p2_shift(p_tilde.get((n, d), {}), s1=N - r)
                expected_f = cell_table[(n, d, r)]
                if coeff_p != expected_f or coeff_tilde != expected_f:
                    raise AssertionError(
                        f"t^(-r) P_r(tx, ty) mismatch with F_{{(n={n}, d={d}, r={r})}}"
                    )

    return checks


# ---------------------------------------------------------------------------
# Suite 4: Lemma 4.2 (Heine's 3rd transformation coefficient identity in Z[q, a, b])
# ---------------------------------------------------------------------------

def run_suite_4() -> int:
    """Verify cleared-denominator Lemma 4.2 identically in Z[q, a, b] for 0 <= N <= 6."""
    q, a, b = symbols("q a b")
    checked = 0
    for N in range(0, 7):
        # LHS * (q; q)_N (q^2; q)_N q^{2N} = q^{2N} (a; q)_N (b; q)_N
        lhs = Poly(q ** (2 * N), q, a, b, domain="ZZ")
        for i in range(N):
            lhs = lhs * Poly(1 - a * q**i, q, a, b, domain="ZZ") * Poly(1 - b * q**i, q, a, b, domain="ZZ")

        rhs = Poly(0, q, a, b, domain="ZZ")
        for j in range(N + 1):
            # [N choose j]_q in Z[q]
            qb_dict = q_binom(N, j)
            qb_expr = sum(c * q**dq for dq, c in qb_dict.items())
            term = Poly(qb_expr, q, a, b, domain="ZZ")
            # (q^2; q)_N / (q^2; q)_j = prod_{i=j}^{N-1} (1 - q^{i+2})
            for i in range(j, N):
                term = term * Poly(1 - q ** (i + 2), q, a, b, domain="ZZ")
            # q^{2(N-j)} (ab/q^2; q)_{N-j} = prod_{i=0}^{N-j-1} (q^2 - a*b*q^i)
            for i in range(N - j):
                term = term * Poly(q**2 - a * b * q**i, q, a, b, domain="ZZ")
            # prod_{i=0}^{j-1} (a - q^{i+2})(b - q^{i+2})
            for i in range(j):
                term = term * Poly(a - q ** (i + 2), q, a, b, domain="ZZ") * Poly(b - q ** (i + 2), q, a, b, domain="ZZ")
            rhs = rhs + term

        if lhs != rhs:
            raise AssertionError(f"Lemma 4.2 polynomial identity failed at N={N}")
        checked += 1
    return checked


# ---------------------------------------------------------------------------
# Suite 5: Lemma 4.3 (symmetry in Z[q, u]) & Theorem 4.4 telescoping q-binomial
# ---------------------------------------------------------------------------

def q_pochhammer_neg_u(m: int) -> Poly2:
    """Compute (-u; q)_m = prod_{j=0}^{m-1} (1 + u q^j) in Z[q, u] as (deg_q, deg_u) -> coeff."""
    res: Poly2 = {(0, 0): 1}
    for j in range(m):
        factor: Poly2 = {(0, 0): 1, (j, 1): 1}
        res = p2_mul(res, factor)
    return res


def k_u_poly(r: int, rp: int) -> Poly2:
    """Compute K_u(r, r') in Z[q, u]."""
    res: Poly2 = {}
    for p in range(1, rp + 1):
        qp = q_shift(q_mul(q_binom(p + r - 1, p), q_binom(rp - 1, p - 1)), p * (p - 1) // 2)
        p2_add_qpoly(res, qp, shift0=0, shift1=p)
    return res


def run_suite_5() -> tuple[int, int]:
    """Verify Lemma 4.3 for 1 <= r, r' <= 8 and Theorem 4.4 telescoping identity for 1 <= a, m, r' <= 8."""
    neg_u_cache = {m: q_pochhammer_neg_u(m) for m in range(1, 9)}
    sym_pairs = 0
    for r in range(1, 9):
        neg_u_r = neg_u_cache[r]
        for rp in range(1, 9):
            neg_u_rp = neg_u_cache[rp]
            lhs = p2_mul(neg_u_r, k_u_poly(r, rp))

            rhs_sum: Poly2 = {}
            for a in range(1, r + 1):
                qp = q_shift(q_mul(q_binom(r, a), q_binom(rp + a - 1, rp)), a * (a - 1) // 2)
                p2_add_qpoly(rhs_sum, qp, shift0=0, shift1=a)
            rhs = p2_mul(neg_u_rp, rhs_sum)

            if lhs != rhs:
                raise AssertionError(f"Lemma 4.3 symmetry identity failed for r={r}, r'={rp}")
            sym_pairs += 1

    # Telescoping q-binomial identity in Theorem 4.4:
    # [r' + a - 1 choose r']_q [r' choose m]_q == [m + a - 1 choose m]_q [m + a + k - 1 choose k]_q
    # with k = r' - m >= 0, for 1 <= a, m, r' <= 8, m <= r'.
    telescoping_checks = 0
    for a in range(1, 9):
        for rp in range(1, 9):
            for m in range(1, rp + 1):
                k = rp - m
                lhs_q = q_mul(q_binom(rp + a - 1, rp), q_binom(rp, m))
                rhs_q = q_mul(q_binom(m + a - 1, m), q_binom(m + a + k - 1, k))
                if lhs_q != rhs_q:
                    raise AssertionError(f"Telescoping q-binomial failed for a={a}, m={m}, r'={rp}")
                telescoping_checks += 1

    return sym_pairs, telescoping_checks


def main() -> int:
    t0 = time.monotonic_ns()

    s1 = run_suite_1()
    print(f"[Suite 1] Direct sandpile CTI/ITC + Dhar + Prop 1.1/2.1 (n+d <= 7): {s1} recurrent configs OK")

    cell_table = run_suite_2()
    print(f"[Suite 2] Prop 1.1 == Prop 2.1 cell comparison (n+d <= 10): {len(cell_table)} (n, d, r) triples OK")

    s3 = run_suite_3(cell_table)
    print(f"[Suite 3] Generating functions P~_r^(N) == P_r^(N) (1 <= r <= 6, r <= N <= 9): {s3} checks OK")

    s4 = run_suite_4()
    print(f"[Suite 4] Lemma 4.2 Heine 3rd transformation in Z[q, a, b] (0 <= N <= 6): {s4} checks OK")

    s5_sym, s5_tel = run_suite_5()
    print(
        f"[Suite 5] Lemma 4.3 in Z[q, u] ({s5_sym} pairs) + Theorem 4.4 telescoping ({s5_tel} triples) OK"
    )

    elapsed_ms = (time.monotonic_ns() - t0) // 1_000_000
    print(f"All 5 suites verified with 100% exact arithmetic (elapsed ~{elapsed_ms} ms).")
    print("PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        print("FAIL")
        raise SystemExit(1)
