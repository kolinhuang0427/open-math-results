#!/usr/bin/env python3
"""Independent zero-float exact-arithmetic verifier for targets/vasilyev-2611.20344-q7.10/."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
import re


def U(x: int) -> int:
    return (3 * x + (x & 1)) // 2


def D(x: int) -> int:
    return (x + (x & 1)) // 2


def v2(u: int) -> int:
    if u == 0:
        return 10**9
    return (u & -u).bit_length() - 1


def solve_stationary_frac(P: list[list[Fraction]], comp: list[int]) -> dict[int, Fraction]:
    """Exact stationary distribution on a sink SCC `comp` via sparse Fraction Gaussian elimination."""
    d = len(comp)
    idx = {v: i for i, v in enumerate(comp)}
    # (P^T - I) mu = 0, sum mu = 1 -> replace last row with [1, ..., 1 | 1]
    mat = [[Fraction(0)] * (d + 1) for _ in range(d)]
    for j, u in enumerate(comp):
        for v in comp:
            if P[u][v] != 0:
                mat[idx[v]][j] += P[u][v]
        mat[j][j] -= Fraction(1)
    mat[d - 1] = [Fraction(1)] * d + [Fraction(1)]

    for col in range(d):
        # Heuristic: pick row with smallest nonzero numerator/denominator bit-length (Markowitz/sparse)
        piv = -1
        best_cost = None
        for r in range(col, d):
            if mat[r][col] != 0:
                nz = sum(1 for c in range(col, d + 1) if mat[r][c] != 0)
                if best_cost is None or nz < best_cost:
                    best_cost = nz
                    piv = r
        assert piv != -1
        if piv != col:
            mat[col], mat[piv] = mat[piv], mat[col]
        inv = Fraction(1) / mat[col][col]
        piv_row = mat[col]
        nz_cols = [c for c in range(col, d + 1) if piv_row[c] != 0]
        for c in nz_cols:
            piv_row[c] *= inv
        for r in range(d):
            if r != col and mat[r][col] != 0:
                fac = mat[r][col]
                row_r = mat[r]
                for c in nz_cols:
                    row_r[c] -= fac * piv_row[c]
    mu = {comp[i]: mat[i][d] for i in range(d)}
    assert sum(mu.values()) == 1 and all(v > 0 for v in mu.values())
    # Verify mu P == mu
    for v in comp:
        lhs = sum(mu[u] * P[u][v] for u in comp)
        assert lhs == mu[v]
    return mu


def sink_sccs(adj: list[tuple[int, int]]) -> list[list[int]]:
    """Tarjan SCC and return all sink SCCs (no outgoing edges outside the SCC)."""
    n = len(adj)
    index = 0
    indices = [-1] * n
    lowlink = [0] * n
    on_stack = [False] * n
    stack: list[int] = []
    sccs: list[list[int]] = []
    comp_id = [-1] * n

    # Iterative Tarjan to avoid recursion limits
    for start in range(n):
        if indices[start] != -1:
            continue
        call_stack: list[tuple[int, int]] = [(start, 0)]
        indices[start] = lowlink[start] = index
        index += 1
        stack.append(start)
        on_stack[start] = True
        while call_stack:
            v, step = call_stack[-1]
            if step < 2:
                w = adj[v][step]
                call_stack[-1] = (v, step + 1)
                if indices[w] == -1:
                    indices[w] = lowlink[w] = index
                    index += 1
                    stack.append(w)
                    on_stack[w] = True
                    call_stack.append((w, 0))
                elif on_stack[w]:
                    lowlink[v] = min(lowlink[v], indices[w])
            else:
                call_stack.pop()
                if call_stack:
                    parent = call_stack[-1][0]
                    lowlink[parent] = min(lowlink[parent], lowlink[v])
                if lowlink[v] == indices[v]:
                    comp: list[int] = []
                    cid = len(sccs)
                    while True:
                        w = stack.pop()
                        on_stack[w] = False
                        comp_id[w] = cid
                        comp.append(w)
                        if w == v:
                            break
                    sccs.append(comp)

    sinks: list[list[int]] = []
    for cid, comp in enumerate(sccs):
        if all(comp_id[w] == cid for u in comp for w in adj[u]):
            sinks.append(sorted(comp))
    return sinks


def karp_max_cycle_mean(adj: list[tuple[int, int]], S_set: set[int]) -> Fraction:
    """Exact Karp algorithm over Fraction for maximum cycle mean a/l of indicator(u in S_set)."""
    N = len(adj)
    # dp[t][v] = max weight of walk of length t ending at v (or -1 if unreachable)
    # Run from all sources simultaneously since every vertex has out-degree 2 (walk of any length exists)
    # Actually Karp requires starting from any vertex in each SCC, or using dummy source -> all vertices with 0:
    dp = [[0] * N]
    for _ in range(N):
        prev = dp[-1]
        nxt = [-10**9] * N
        for u in range(N):
            w_u = 1 if u in S_set else 0
            val = prev[u] + w_u
            for v in adj[u]:
                if val > nxt[v]:
                    nxt[v] = val
        dp.append(nxt)
    # Compute exact max_{v} min_{0 <= t < N} (dp[N][v] - dp[t][v]) / (N - t)
    best: Fraction | None = None
    for v in range(N):
        min_v: Fraction | None = None
        for t in range(N):
            ratio = Fraction(dp[N][v] - dp[t][v], N - t)
            if min_v is None or ratio < min_v:
                min_v = ratio
        assert min_v is not None
        if best is None or min_v > best:
            best = min_v
    assert best is not None
    return best


def build_res_graph(k: int, S_set: set[int]) -> tuple[list[tuple[int, int]], list[list[Fraction]]]:
    M = 1 << k
    half = M >> 1
    adj: list[tuple[int, int]] = []
    P = [[Fraction(0)] * M for _ in range(M)]
    for r in range(M):
        rep = M if r == 0 else r
        nxt = (U(rep) if r in S_set else D(rep)) % M
        s1, s2 = nxt, (nxt + half) % M
        assert s1 != s2
        adj.append((s1, s2))
        P[r][s1] += Fraction(1, 2)
        P[r][s2] += Fraction(1, 2)
    return adj, P


def check_primary_source() -> None:
    import os
    if not os.path.exists("tools/.arxiv_cache/eprint/2611.20344/updown.tex"):
        print("[SKIP] local tools/.arxiv_cache not present; skipping TeX numbering check")
        return
    tex = open("tools/.arxiv_cache/eprint/2611.20344/updown.tex", "r", encoding="utf-8").read()
    sec = 0
    cnt = 0
    labels: dict[str, str] = {}
    pat = re.compile(r"\\begin\{(theorem|lemma|proposition|corollary|definition|question|remark|example)\}(?:\[[^\]]*\])?(?:\\label\{([^}]+)\})?")
    for line in tex.splitlines():
        if r"\section{" in line:
            sec += 1
            cnt = 0
        m = pat.search(line)
        if m:
            cnt += 1
            if m.group(2):
                labels[m.group(2)] = f"{sec}.{cnt}"

    assert labels["def:residue"] == "5.3"
    assert labels["def:pi"] == "5.8"
    assert labels["def:uniform"] == "5.10"
    assert labels["thm:uniform"] == "5.11"
    assert labels["q:supremum"] == "7.10"
    assert r"Is the supremum of $\pi_C(S)$ over all uniformly descending periodic sets $S$ equal to $\log_32$?" in tex
    assert r"73/174" in tex

    target_md = open("targets/vasilyev-2611.20344-q7.10/TARGET.md", "r", encoding="utf-8").read()
    proof_md = open("targets/vasilyev-2611.20344-q7.10/PROOF.md", "r", encoding="utf-8").read()
    assert "arXiv:2611.20344v2" in target_md
    assert "q:supremum" in target_md
    assert "73/174" in target_md
    assert "Subsection 5.4" in target_md and "Table 5.3" in target_md
    assert "Vasilyev §5.4" in proof_md
    print("[PASS] Primary source arXiv:2611.20344v2 verbatim statement and Section 5/7 numbering verified.")


def check_table_5_3() -> None:
    # Exhaustive check for k=2 (M=4) and k=3 (M=8)
    expected = {2: (3, Fraction(1, 4)), 3: (20, Fraction(5, 18))}
    for k, (exp_cnt, exp_max_pi) in expected.items():
        M = 1 << k
        desc_cnt = 0
        best_pi = Fraction(-1)
        for mask in range(1 << M):
            S_set = {r for r in range(M) if (mask >> r) & 1}
            adj, P = build_res_graph(k, S_set)
            mu_star = karp_max_cycle_mean(adj, S_set)
            # Check 3^a < 2^l <=> (3^a < 2^l for reduced fraction mu_star = a/l)
            if pow(3, mu_star.numerator) < pow(2, mu_star.denominator):
                desc_cnt += 1
                for comp in sink_sccs(adj):
                    mu_C = solve_stationary_frac(P, comp)
                    pi_C = sum(mu_C[r] for r in comp if r in S_set)
                    assert pi_C <= mu_star
                    if pi_C > best_pi:
                        best_pi = pi_C
        assert desc_cnt == exp_cnt and best_pi == exp_max_pi

    # Spot-check k=4 (M=16) Table 5.3 optimal witness {1,3,6,7,8,11,13} -> 73/174
    S16 = {1, 3, 6, 7, 8, 11, 13}
    adj16, P16 = build_res_graph(4, S16)
    mu16 = karp_max_cycle_mean(adj16, S16)
    assert pow(3, mu16.numerator) < pow(2, mu16.denominator)
    sinks16 = sink_sccs(adj16)
    pis16 = [sum(solve_stationary_frac(P16, c)[r] for r in c if r in S16) for c in sinks16]
    assert max(pis16) == Fraction(73, 174)
    print("[PASS] Table 5.3 baseline (mod 4: 3, 1/4; mod 8: 20, 5/18; mod 16 witness: 73/174) verified.")


def T_S0(x: int, J: set[int]) -> int:
    if x & 1:
        return (3 * x + 1) // 2
    u = x >> 1
    return (3 * u) if (v2(u) in J) else u


def build_S0(m: int, J: set[int]) -> set[int]:
    M = 1 << m
    S = {r for r in range(M) if r & 1}
    for u in range(1, 1 << (m - 1)):
        if v2(u) in J:
            S.add((2 * u) % M)
    return S


def check_lemma1_dyadic_isometry() -> None:
    for m, J in [(2, set()), (2, {0}), (3, {1}), (4, {0, 2}), (4, {2}), (5, {2, 3})]:
        M = 1 << m
        S0 = build_S0(m, J)
        lam_S0 = Fraction(len(S0), M)
        expected_lam = Fraction(1, 2) + sum(Fraction(1, 1 << (j + 2)) for j in J)
        assert lam_S0 == expected_lam

        # Verify equivalence of mod-2^m predicate with T_S0 branch on integers x in [0, 4M)
        for x in range(4 * M):
            in_S0 = (x % M) in S0
            pred = (x % 2 == 1) or (v2(x >> 1) in J)
            assert in_S0 == pred

        # Lemma 1(a) Forward Lipschitz on [0, 2^(m+2)) and d in 1..m+1
        if m <= 4:
            bound = 1 << (m + 2)
            for d in range(1, m + 2):
                mod_d = 1 << d
                mod_dm1 = 1 << (d - 1)
                for x in range(bound):
                    for q in range(1, 3):
                        xp = x + q * mod_d
                        assert (T_S0(x, J) - T_S0(xp, J)) % mod_dm1 == 0

        # Lemma 1(b) 2-to-1 exact preimages mod 2^(n+1) -> mod 2^n
        n_test = m + 2
        mod_n = 1 << n_test
        mod_np1 = 1 << (n_test + 1)
        inv3 = pow(3, -1, mod_np1)
        for y in range(mod_n):
            x1 = (inv3 * (2 * y - 1)) % mod_np1
            x0 = ((2 * inv3 * y) if (v2(y) in J) else (2 * y)) % mod_np1
            assert (x1 % 2 == 1) and (T_S0(x1, J) - y) % mod_n == 0
            assert (x0 % 2 == 0) and (T_S0(x0, J) - y) % mod_n == 0

        # Lemma 1(c) Bijectivity of Phi_n and exact De Bruijn mixing P_0^n == 2^{-n} J
        n = m + 2
        N = 1 << n
        S0_n = {r for r in range(N) if (r % M) in S0}
        phis: dict[int, tuple[int, ...]] = {}
        for r in range(N):
            cur = r
            bits = []
            for _ in range(n):
                bits.append(cur & 1)
                cur = T_S0(cur, J)
            phis[r] = tuple(bits)
        assert len(set(phis.values())) == N

        adj0, P0 = build_res_graph(n, S0_n)
        for r in range(N):
            b = phis[r]
            s1, s2 = adj0[r]
            assert {phis[s1], phis[s2]} == {b[1:] + (0,), b[1:] + (1,)}

        # Compute P0^n exactly in int by scaling by 2^n!
        # Since entries of 2*P0 are in {0, 1}, (2*P0)^n[y][z] counts exact paths of length n!
        cnts = [[1 if y == z else 0 for z in range(N)] for y in range(N)]
        for _ in range(n):
            nxt = [[0] * N for _ in range(N)]
            for y in range(N):
                for u in range(N):
                    c = cnts[y][u]
                    if c:
                        s1, s2 = adj0[u]
                        nxt[y][s1] += c
                        nxt[y][s2] += c
            cnts = nxt
        assert all(cnts[y][z] == 1 for y in range(N) for z in range(N))

    print("[PASS] Lemma 1 (densities, forward Lipschitz, inverse branches, Phi_n bijection, P0^n = 2^{-n} 1 1^T) verified.")


def exp_rational_upper_bound_check(x_pos: Fraction, m: int, lhs_lam: Fraction) -> None:
    """Verify lhs_lam <= m * exp(-x_pos) without floats via exact rational Taylor upper bound on exp(x_pos)."""
    if x_pos == 0:
        assert lhs_lam <= m
        return
    # exp(x) <= sum_{k=0}^K x^k/k! + remainder for K >= 2*x
    K = max(25, ceil_x := int(x_pos) * 3 + 10)
    s = Fraction(1)
    term = Fraction(1)
    for k in range(1, K + 1):
        term = term * x_pos / k
        s += term
    next_term = term * x_pos / (K + 1)
    ratio = x_pos / (K + 2)
    assert ratio < 1
    exp_ub = s + next_term / (1 - ratio)
    assert lhs_lam * exp_ub <= m, f"Lemma 3 failed: {lhs_lam} * {exp_ub} > {m}"


def check_barina_sieve_lemmas2_to_6() -> None:
    # Instances with lambda(S0) < mu < log_3(2) (3^{mu.num} < 2^{mu.den}):
    # Note log_3(2) ~ 0.63092975; 5/8 = 0.625, 17/27 = 0.629629..., 41/65 = 0.630769...
    instances = [
        (4, {2}, Fraction(5, 8), 3),          # lam=9/16=0.5625, mu=5/8, n=6 (N=64)
        (4, {2}, Fraction(5, 8), 4),          # lam=9/16=0.5625, mu=5/8, n=7 (N=128)
        (3, {1}, Fraction(17, 27), 4),        # lam=5/8=0.625, mu=17/27, n=6 (N=64)
        (3, {1}, Fraction(17, 27), 5),        # lam=5/8=0.625, mu=17/27, n=7 (N=128)
        (5, {2, 3}, Fraction(5, 8), 3),       # lam=19/32=0.59375, mu=5/8, n=7 (N=128)
    ]

    total_paths_checked = 0
    witness_summary = []
    for m, J, mu, L in instances:
        assert pow(3, mu.numerator) < pow(2, mu.denominator)
        n = m + L - 1
        M = 1 << m
        N = 1 << n
        S0 = build_S0(m, J)
        lam_S0 = Fraction(len(S0), M)
        assert lam_S0 < mu
        delta = mu - lam_S0

        # Build W_j(r) and B_n, S_n, tau(r)
        S0_n = {r for r in range(N) if (r % M) in S0}
        W: dict[int, list[Fraction]] = {}
        B_n: set[int] = set()
        tau: dict[int, int] = {}
        for r in range(N):
            cur = r
            w_list: list[Fraction] = []
            acc = Fraction(0)
            first_neg = None
            for j in range(1, L + 1):
                ind = 1 if (cur % M) in S0 else 0
                acc += Fraction(ind) - mu
                w_list.append(acc)
                if first_neg is None and acc < 0:
                    first_neg = j
                cur = T_S0(cur, J)
            W[r] = w_list
            if first_neg is None:
                B_n.add(r)
                tau[r] = 1
            else:
                tau[r] = first_neg

        assert B_n.issubset(S0_n)
        S_n = S0_n - B_n
        adj_n, P_n = build_res_graph(n, S_n)

        # Lemma 3: exact Hoeffding check for L >= m (lambda_n(B_n) <= m * exp(-2*delta^2 * (L // m)))
        lam_n_Bn = Fraction(len(B_n), N)
        if L >= m:
            exp_rational_upper_bound_check(2 * delta * delta * (L // m), m, lam_n_Bn)

        # Lemma 2(a): Exhaustively verify EVERY directed path of length tau(r) from EVERY r in Z/2^nZ
        for r in range(N):
            paths_r: list[list[int]] = [[r]]
            for s in range(tau[r]):
                nxt_paths = []
                for pth in paths_r:
                    u = pth[-1]
                    if r not in B_n:
                        assert (u - T_S0_iter(r, s, J)) % (1 << (n - s)) == 0
                        assert u not in B_n
                    for v in adj_n[u]:
                        nxt_paths.append(pth + [v])
                paths_r = nxt_paths
            for pth in paths_r:
                wt_sum = sum(Fraction(1 if pth[s] in S_n else 0) - mu for s in range(tau[r]))
                assert wt_sum < 0

        # Lemma 2(b): Karp max cycle mean < mu and 3^a < 2^l
        mu_star = karp_max_cycle_mean(adj_n, S_n)
        assert mu_star < mu and pow(3, mu_star.numerator) < pow(2, mu_star.denominator)

        # Lemma 4 & Lemma 5: enumerate ALL 2^n paths of length n from EVERY y in Z/2^nZ
        max_F_bound = (1 << (m - 1)) * (L + 1)
        path_counts = [[0] * N for _ in range(N)]
        for y in range(N):
            seen_y_z_T: set[tuple[int, frozenset[int]]] = set()
            F_y: set[frozenset[int]] = set()
            F0_y: set[frozenset[int]] = set()
            # DFS/BFS all 2^n paths of length n
            cur_paths: list[list[int]] = [[y]]
            for _ in range(n):
                cur_paths = [p + [v] for p in cur_paths for v in adj_n[p[-1]]]
            assert len(cur_paths) == N
            total_paths_checked += len(cur_paths)
            for pth in cur_paths:
                z = pth[-1]
                T_hit = frozenset(t for t in range(n) if pth[t] in B_n)
                key = (z, T_hit)
                assert key not in seen_y_z_T, f"Lemma 4(b) failed at (y={y}, z={z}, T={T_hit})"
                seen_y_z_T.add(key)
                F_y.add(T_hit)
                F0_y.add(frozenset(t for t in T_hit if t < L))
                path_counts[y][z] += 1

            # Lemma 5(a): F0(y) is totally ordered by inclusion and |F0(y)| <= L + 1
            f0_sorted = sorted(F0_y, key=len)
            assert len(f0_sorted) <= L + 1
            for idx_f in range(len(f0_sorted) - 1):
                assert f0_sorted[idx_f] < f0_sorted[idx_f + 1], f"Lemma 5(a) not a chain at y={y}"
            # Lemma 5(b)
            assert len(F_y) <= max_F_bound

        # Lemma 5(c): P_n^n(y, z) <= 2^{-n} * 2^{m-1}(L+1)
        for y in range(N):
            for z in range(N):
                assert path_counts[y][z] <= max_F_bound

        # Theorem 6: exact stationary measure on every sink SCC
        sinks = sink_sccs(adj_n)
        assert len(sinks) >= 1
        min_pi = Fraction(1)
        for comp in sinks:
            mu_C = solve_stationary_frac(P_n, comp)
            mu_C_Bn = sum(mu_C[r] for r in comp if r in B_n)
            l1_diff = sum(abs(mu_C.get(r, Fraction(0)) - Fraction(1, N)) for r in range(N))
            pi_C = sum(mu_C[r] for r in comp if r in S_n)
            # Check all 3 Theorem 6 inequalities
            assert mu_C_Bn <= max_F_bound * lam_n_Bn
            assert l1_diff <= 2 * n * mu_C_Bn
            assert pi_C >= lam_S0 - (n + 1) * mu_C_Bn
            assert pi_C <= mu_star < mu
            if pi_C < min_pi:
                min_pi = pi_C
        witness_summary.append((m, n, len(B_n), float_free_str(min_pi)))

    print(
        f"[PASS] Lemmas 2-5 & Theorem 6 verified exhaustively across {len(instances)} Barina sieve instances "
        f"({total_paths_checked} length-n paths checked, summaries={witness_summary})."
    )


def T_S0_iter(x: int, s: int, J: set[int]) -> int:
    for _ in range(s):
        x = T_S0(x, J)
    return x


def float_free_str(q: Fraction) -> str:
    return f"{q.numerator}/{q.denominator}"


def main() -> None:
    check_primary_source()
    check_table_5_3()
    check_lemma1_dyadic_isometry()
    check_barina_sieve_lemmas2_to_6()
    print("PASS")


if __name__ == "__main__":
    main()
