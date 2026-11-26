#!/usr/bin/env python3
"""Exact verification of R. J. Mathar's conjecture on OEIS A100691 and A193641.

Verifies:
1. Part 1 (OEIS sequence reading): A193641(n) matches brute-force enumeration
   for 1 <= n <= 8, satisfies b(m) = 2*b(m-1) + b(m-3) for m >= 3 via the
   proven 3-state (U, V, W) recurrence, and b(n+2) - 3 matches the OEIS A100691
   generating function (1+z^2)(1+z+z^2)/((1-z)(1-2z-z^3)) symbolically.
2. Part 2 (combinatorial SAW reading): Exact DFS enumeration of n-step
   self-avoiding paths from (0,0) on the triangular lattice strip Z x {0,1}
   for 0 <= n <= 12 matches the symbolic column transfer-matrix generating
   function (1 + z^2 - z^3 + z^5) / ((1 - z)^2 (1 - 2z - z^3)), which equals
   A193641(n+2) - 3 for 1 <= n <= 4 and differs starting at n = 5 (160 vs 158).
"""

import signal
import sys
from collections import defaultdict
from itertools import product
import sympy as sp


def _timeout_handler(signum, frame):
    raise TimeoutError("verify.py exceeded 60s time limit")


signal.signal(signal.SIGALRM, _timeout_handler)
signal.alarm(60)


def brute_a193641(n):
    if n == 0:
        return 1
    cnt = 0
    for x in product((-1, 0, 1), repeat=n):
        ok_all = True
        for i in range(n):
            if x[i] == 0:
                continue
            ok_i = (i > 0 and x[i - 1] + x[i] == 0) or (i + 1 < n and x[i] + x[i + 1] == 0)
            if not ok_i:
                ok_all = False
                break
        if ok_all:
            cnt += 1
    return cnt


def uvw_a193641(n_max):
    U = [0] * (n_max + 1)
    V = [0] * (n_max + 1)
    W = [0] * (n_max + 1)
    U[0], V[0], W[0] = 1, 0, 0
    for n in range(n_max):
        U[n + 1] = U[n] + V[n]
        W[n + 1] = 2 * U[n] + V[n]
        V[n + 1] = V[n] + W[n]
    return [U[n] + V[n] for n in range(n_max + 1)]


def saw_dfs(n_max):
    def neighbors(x, y):
        if y == 0:
            return ((x - 1, 0), (x + 1, 0), (x, 1), (x - 1, 1))
        return ((x - 1, 1), (x + 1, 1), (x, 0), (x + 1, 0))

    counts = [0] * (n_max + 1)

    def dfs(x, y, depth, visited):
        counts[depth] += 1
        if depth == n_max:
            return
        for nx, ny in neighbors(x, y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                dfs(nx, ny, depth + 1, visited)
                visited.remove((nx, ny))

    dfs(0, 0, 0, {(0, 0)})
    return counts


def saw_transfer_matrix_gf(z):
    def step_col(state, is_x0):
        phase, s_seen, t_seen, E_in, pairs = state
        b, d, te = E_in
        res = []
        s_choices = (0,) if is_x0 else (None,)
        t_choices = (None,) if t_seen else ((None, 1) if is_x0 else (None, 0, 1))
        for s_pos in s_choices:
            for t_pos in t_choices:
                for vert in (0, 1):
                    for b2 in (0, 1):
                        for d2 in (0, 1):
                            for te2 in (0, 1):
                                d_v0 = b + d + vert + b2 + (1 if s_pos == 0 else 0) + (1 if t_pos == 0 else 0)
                                d_v1 = te + vert + d2 + te2 + (1 if s_pos == 1 else 0) + (1 if t_pos == 1 else 0)
                                if d_v0 not in (0, 2) or d_v1 not in (0, 2):
                                    continue
                                any_here = b or d or te or vert or b2 or d2 or te2 or (s_pos is not None) or (t_pos is not None)
                                if phase == "done" and any_here:
                                    continue
                                adj = defaultdict(list)
                                for u, v in pairs:
                                    adj[u].append(v)
                                    adj[v].append(u)
                                if b:
                                    adj["L0"].append("v0")
                                    adj["v0"].append("L0")
                                if d:
                                    adj["L1"].append("v0")
                                    adj["v0"].append("L1")
                                if te:
                                    adj["L2"].append("v1")
                                    adj["v1"].append("L2")
                                if vert:
                                    adj["v0"].append("v1")
                                    adj["v1"].append("v0")
                                if b2:
                                    adj["v0"].append("R0")
                                    adj["R0"].append("v0")
                                if d2:
                                    adj["v1"].append("R1")
                                    adj["R1"].append("v1")
                                if te2:
                                    adj["v1"].append("R2")
                                    adj["R2"].append("v1")
                                if s_pos is not None:
                                    vn = f"v{s_pos}"
                                    adj["s"].append(vn)
                                    adj[vn].append("s")
                                if t_pos is not None:
                                    vn = f"v{t_pos}"
                                    adj["t"].append(vn)
                                    adj[vn].append("t")
                                deg1 = [k for k, nbrs in adj.items() if len(nbrs) == 1]
                                visited_nodes = set()
                                new_pairs = []
                                closed_st = False
                                bad = False
                                for start in deg1:
                                    if start in visited_nodes:
                                        continue
                                    cur = start
                                    prev = None
                                    visited_nodes.add(cur)
                                    while True:
                                        nxt_list = [x for x in adj[cur] if x != prev]
                                        if not nxt_list:
                                            break
                                        nxt = nxt_list[0]
                                        if nxt in visited_nodes:
                                            bad = True
                                            break
                                        visited_nodes.add(nxt)
                                        prev, cur = cur, nxt
                                    if bad:
                                        break
                                    if {start, cur} == {"s", "t"}:
                                        closed_st = True
                                    else:
                                        new_pairs.append((start, cur))
                                if bad or len(visited_nodes) != len(adj):
                                    continue
                                new_s = s_seen or (s_pos is not None)
                                new_t = t_seen or (t_pos is not None)
                                new_E_out = (b2, d2, te2)
                                if closed_st:
                                    if new_pairs or any(new_E_out):
                                        continue
                                    new_phase = "done"
                                elif new_pairs or any(new_E_out):
                                    new_phase = "active"
                                else:
                                    new_phase = phase
                                rel = {"R0": "L0", "R1": "L1", "R2": "L2", "s": "s", "t": "t"}
                                canon_pairs = tuple(sorted(tuple(sorted((rel[u], rel[v]))) for u, v in new_pairs))
                                res.append(((new_phase, new_s, new_t, new_E_out, canon_pairs), vert + b2 + d2 + te2))
        return res

    init = ("before", False, False, (0, 0, 0), ())
    left_states = {init}
    q = [init]
    while q:
        st = q.pop()
        for nst, _ in step_col(st, is_x0=False):
            if nst not in left_states:
                left_states.add(nst)
                q.append(nst)
    right_states = set()
    q2 = []
    for st in left_states:
        for nst, _ in step_col(st, is_x0=True):
            if nst not in right_states:
                right_states.add(nst)
                q2.append(nst)
    while q2:
        st = q2.pop()
        for nst, _ in step_col(st, is_x0=False):
            if nst not in right_states:
                right_states.add(nst)
                q2.append(nst)

    L_list = sorted(left_states)
    L_idx = {s: i for i, s in enumerate(L_list)}
    R_list = sorted(right_states)
    R_idx = {s: i for i, s in enumerate(R_list)}

    ML = sp.zeros(len(L_list), len(L_list))
    for st in L_list:
        i = L_idx[st]
        for nst, w in step_col(st, is_x0=False):
            if st[0] == "before" and nst[0] == "before":
                continue
            ML[L_idx[nst], i] += z**w
    from sympy.polys.matrices import DomainMatrix
    K = sp.QQ.frac_field(z)

    def solve_rat_sys(A_expr, b_expr):
        dm_A = DomainMatrix.from_Matrix(A_expr).convert_to(K)
        dm_b = DomainMatrix.from_Matrix(b_expr).convert_to(K)
        dm_x = dm_A.lu_solve(dm_b)
        return dm_x.to_Matrix()

    e_init = sp.zeros(len(L_list), 1)
    e_init[L_idx[init], 0] = 1
    v_L = solve_rat_sys(sp.eye(len(L_list)) - ML, e_init)

    M0 = sp.zeros(len(R_list), len(L_list))
    for st in L_list:
        i = L_idx[st]
        for nst, w in step_col(st, is_x0=True):
            M0[R_idx[nst], i] += z**w
    v_0 = M0 * v_L

    MR = sp.zeros(len(R_list), len(R_list))
    for st in R_list:
        i = R_idx[st]
        for nst, w in step_col(st, is_x0=False):
            if st[0] == "done" and nst[0] == "done":
                continue
            MR[R_idx[nst], i] += z**w
    v_R = solve_rat_sys(sp.eye(len(R_list)) - MR, v_0)

    return sp.cancel(1 + sum(v_R[R_idx[st], 0] for st in R_list if st[0] == "done"))


def taylor_coeffs(num_poly, den_poly, z, n_max):
    """Exact integer series expansion of num_poly / den_poly up to z^n_max."""
    p_num = sp.Poly(num_poly, z)
    p_den = sp.Poly(den_poly, z)
    d0 = int(p_den.coeff_monomial(1))
    assert d0 in (1, -1)
    sign = d0
    deg_d = p_den.degree()
    den_coeffs = [int(p_den.coeff_monomial(z**k)) * sign for k in range(deg_d + 1)]
    out = []
    for n in range(n_max + 1):
        rhs = int(p_num.coeff_monomial(z**n)) * sign
        for k in range(1, min(n, deg_d) + 1):
            rhs -= den_coeffs[k] * out[n - k]
        out.append(rhs)
    return out


def main():
    # 1. Check A193641 brute force vs (U, V, W) automaton vs linear recurrence
    b_uvw = uvw_a193641(25)
    for n in range(9):
        assert brute_a193641(n) == b_uvw[n], f"A193641 mismatch at n={n}"
    for m in range(3, 26):
        assert b_uvw[m] == 2 * b_uvw[m - 1] + b_uvw[m - 3], f"Recurrence failed at m={m}"

    # 2. Check OEIS A100691 GF == 1 + sum_{n>=1} (A193641(n+2) - 3) z^n
    z = sp.Symbol("z")
    gf_oeis = (1 + z**2) * (1 + z + z**2) / ((1 - z) * (1 - 2 * z - z**3))
    a_oeis = taylor_coeffs((1 + z**2) * (1 + z + z**2), (1 - z) * (1 - 2 * z - z**3), z, 23)
    for n in range(1, 24):
        assert a_oeis[n] == b_uvw[n + 2] - 3, f"OEIS vs A193641(n+2)-3 mismatch at n={n}"

    # 3. Check exact SAW GF via transfer matrix vs exact DFS for 0 <= n <= 12
    gf_saw = saw_transfer_matrix_gf(z)
    gf_saw_expected = (1 + z**2 - z**3 + z**5) / ((1 - z) ** 2 * (1 - 2 * z - z**3))
    assert sp.simplify(gf_saw - gf_saw_expected) == 0, f"Unexpected SAW GF: {gf_saw}"

    s_exact = taylor_coeffs(1 + z**2 - z**3 + z**5, (1 - z) ** 2 * (1 - 2 * z - z**3), z, 12)
    s_dfs = saw_dfs(12)
    assert s_exact == s_dfs, f"DFS vs transfer matrix mismatch: {s_dfs} vs {s_exact}"

    # 4. Check exact difference F_SAW - G_OEIS
    diff_gf = sp.factor(gf_saw_expected - gf_oeis)
    assert sp.simplify(diff_gf - 2 * z**5 / ((1 - z) ** 2 * (1 - 2 * z - z**3))) == 0
    assert s_dfs[5] == 160 and a_oeis[5] == 158

    print("PASS")
    print(f"A193641(0..8) checked against brute force: {b_uvw[:9]}")
    print(f"A100691 OEIS series(0..8): {a_oeis[:9]}")
    print(f"Exact SAW Zx{{0,1}} series(0..8): {s_dfs[:9]}")
    print(f"First SAW vs OEIS discrepancy at n=5: s(5)={s_dfs[5]} vs A193641(7)-3={a_oeis[5]}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
