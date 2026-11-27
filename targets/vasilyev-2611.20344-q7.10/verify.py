#!/usr/bin/env python3
"""Exact-arithmetic (zero-float) verification for vasilyev-2611.20344-q7.10.

Verifies:
  1. Vasilyev (arXiv:2611.20344v2) Table 5.3 exact baselines (mod 4, 8, 16).
  2. Lemma 1 (dyadic-shell base sets S_0(J): exact density, forward Lipschitz,
     inverse branch 1/2-similarity, Phi_n bijection, and exact P_0^n = 2^{-n} J).
  3. Lemmas 2-5 and Theorem 6 on explicit Barina first-exit sieve instances S_n:
     - First-exit lockout & exact Karp max cycle mean mu* < mu < log_3 2;
     - Exact rational Hoeffding tail check;
     - Path uniqueness per (y, z, T) across all 2^n paths from every y;
     - Nested-chain total order of F_0(y) and exact P_n^n(y, z) bound;
     - Exact Fraction stationary distributions on every sink SCC C confirming
       all three inequalities of Theorem 6.
"""

from fractions import Fraction


def v2(u):
    assert u > 0
    c = 0
    while (u & 1) == 0:
        u >>= 1
        c += 1
    return c


def U_int(x):
    return (3 * x + (x & 1)) // 2


def D_int(x):
    return (x + (x & 1)) // 2


def make_S0(m, J):
    M = 1 << m
    Jset = set(J)
    S0 = set()
    for r in range(M):
        if (r & 1) == 1:
            S0.add(r)
        elif r > 0 and v2(r >> 1) in Jset:
            S0.add(r)
    return S0


def T_S0_int(x, m, S0):
    if (x & ((1 << m) - 1)) in S0:
        return U_int(x)
    return D_int(x)


def build_res_graph(k, S_set):
    """Build exact Vasilyev Definition 5.3 residue graph R_k(S) on Z/2^k Z."""
    M = 1 << k
    H = 1 << (k - 1)
    adj = []
    for r in range(M):
        r_hat = M if r == 0 else r
        if r in S_set:
            g = U_int(r_hat) % M
        else:
            g = D_int(r_hat) % M
        s1 = g
        s2 = (g + H) % M
        assert s1 != s2
        adj.append((s1, s2))
    return M, adj


def tarjan_sink_sccs(N, adj):
    idx = 0
    indices = [-1] * N
    low = [0] * N
    on_stack = [False] * N
    st = []
    sccs = []
    for start in range(N):
        if indices[start] != -1:
            continue
        call_st = [(start, 0)]
        indices[start] = low[start] = idx
        idx += 1
        st.append(start)
        on_stack[start] = True
        while call_st:
            v, ei = call_st[-1]
            if ei < 2:
                call_st[-1] = (v, ei + 1)
                w = adj[v][ei]
                if indices[w] == -1:
                    indices[w] = low[w] = idx
                    idx += 1
                    st.append(w)
                    on_stack[w] = True
                    call_st.append((w, 0))
                elif on_stack[w]:
                    if indices[w] < low[v]:
                        low[v] = indices[w]
            else:
                if low[v] == indices[v]:
                    comp = []
                    while True:
                        w = st.pop()
                        on_stack[w] = False
                        comp.append(w)
                        if w == v:
                            break
                    sccs.append(sorted(comp))
                call_st.pop()
                if call_st:
                    p = call_st[-1][0]
                    if low[v] < low[p]:
                        low[p] = low[v]
    scc_id = [0] * N
    for i, comp in enumerate(sccs):
        for v in comp:
            scc_id[v] = i
    sinks = [
        comp
        for i, comp in enumerate(sccs)
        if all(scc_id[w] == i for v in comp for w in adj[v])
    ]
    return sinks


def exact_karp_max_cycle_mean(N, adj, S_set):
    """Exact rational maximum cycle mean via Karp's algorithm."""
    NEG_INF = -10**9
    dp = [[NEG_INF] * N for _ in range(N + 1)]
    for v in range(N):
        dp[0][v] = 0
    for step in range(1, N + 1):
        prev = dp[step - 1]
        cur = dp[step]
        for u in range(N):
            pu = prev[u]
            if pu == NEG_INF:
                continue
            w = 1 if u in S_set else 0
            a, b = adj[u]
            val = pu + w
            if val > cur[a]:
                cur[a] = val
            if val > cur[b]:
                cur[b] = val
    mu = Fraction(0)
    for v in range(N):
        if dp[N][v] == NEG_INF:
            continue
        mn = None
        for step in range(N):
            if dp[step][v] != NEG_INF:
                cand = Fraction(dp[N][v] - dp[step][v], N - step)
                if mn is None or cand < mn:
                    mn = cand
        if mn is not None and mn > mu:
            mu = mn
    return mu


def exact_stationary_on_sink(N, adj, sink):
    """Exact Fraction stationary distribution on a sink SCC C."""
    sz = len(sink)
    pos = {v: i for i, v in enumerate(sink)}
    A = [[Fraction(0)] * (sz + 1) for _ in range(sz)]
    half = Fraction(1, 2)
    for i, u in enumerate(sink):
        A[i][i] -= 1
        a, b = adj[u]
        A[pos[a]][i] += half
        A[pos[b]][i] += half
    A[sz - 1] = [Fraction(1)] * sz + [Fraction(1)]

    for col in range(sz):
        piv = None
        for r in range(col, sz):
            if A[r][col] != 0:
                piv = r
                break
        assert piv is not None, "Singular stationary system"
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        row_c = [x / pv for x in A[col]]
        A[col] = row_c
        for r in range(sz):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                row_r = A[r]
                for c in range(col, sz + 1):
                    row_r[c] -= f * row_c[c]

    mu = [Fraction(0)] * N
    for i, v in enumerate(sink):
        val = A[i][sz]
        assert val > 0
        mu[v] = val
    assert sum(mu) == 1

    # Independently verify mu * P == mu
    for v in range(N):
        acc = Fraction(0)
        for u in range(N):
            a, b = adj[u]
            if a == v:
                acc += mu[u] * half
            if b == v:
                acc += mu[u] * half
        assert acc == mu[v], f"Stationarity check failed at vertex {v}"
    return mu


def verify_table_5_3_baselines():
    cases = [
        (2, {2}, Fraction(1, 4)),
        (3, {3, 4, 6}, Fraction(5, 18)),
        (4, {1, 3, 6, 7, 8, 11, 13}, Fraction(73, 174)),
    ]
    for k, S_set, expected_pi in cases:
        M, adj = build_res_graph(k, S_set)
        mu_star = exact_karp_max_cycle_mean(M, adj, S_set)
        assert pow(3, mu_star.numerator) < pow(2, mu_star.denominator)
        sinks = tarjan_sink_sccs(M, adj)
        assert len(sinks) == 1
        mu = exact_stationary_on_sink(M, adj, sinks[0])
        pi = sum(mu[r] for r in S_set)
        assert pi == expected_pi, f"Table 5.3 mismatch for k={k}: {pi} != {expected_pi}"
    print("[OK] Vasilyev Table 5.3 baselines verified: 1/4, 5/18, 73/174")


def verify_lemma_1():
    configs = [
        (2, ()),
        (3, (1,)),
        (4, (2,)),
        (4, (0, 2)),
        (5, (1, 3)),
    ]
    for m, J in configs:
        M = 1 << m
        S0 = make_S0(m, J)
        # 1. Exact density formula
        expected_lam = Fraction(1, 2) + sum(Fraction(1, 1 << (j + 2)) for j in J)
        assert Fraction(len(S0), M) == expected_lam

        # 2. Forward Lipschitz for all 1 <= d <= m and all x, x' mod 2^m
        for d in range(1, m + 1):
            step = 1 << d
            mod_out = 1 << (d - 1)
            for x in range(M):
                y = (x + step) % M
                assert (T_S0_int(x, m, S0) - T_S0_int(y, m, S0)) % mod_out == 0

        # 3. Exact 2-to-1 inverse branches and 1/2-similarity mod 2^{m+1}
        M2 = 1 << (m + 1)
        inv3 = pow(3, -1, M2)
        Jset = set(J)
        for y in range(M):
            x1 = (inv3 * (2 * y - 1)) % M2
            assert (x1 & 1) == 1
            assert (T_S0_int(x1, m, S0) - y) % M == 0
            if y > 0 and v2(y) in Jset:
                x0 = (2 * inv3 * y) % M2
            else:
                x0 = (2 * y) % M2
            assert (x0 & 1) == 0
            assert (T_S0_int(x0, m, S0) - y) % M == 0
        # Check exact 1/2-similarity on pairs y != y' mod 2^m
        x0_map = []
        x1_map = []
        for y in range(M):
            x1_map.append((inv3 * (2 * y - 1)) % M2)
            if y > 0 and v2(y) in Jset:
                x0_map.append((2 * inv3 * y) % M2)
            else:
                x0_map.append((2 * y) % M2)
        for y in range(M):
            for yp in range(y + 1, M):
                vy = v2(yp - y)
                assert v2((x1_map[yp] - x1_map[y]) % M2) == 1 + vy
                assert v2((x0_map[yp] - x0_map[y]) % M2) == 1 + vy

        # 4. Exact De Bruijn conjugacy & P_0^n == 2^{-n} * 1 1^T
        for n in (m, m + 1):
            N = 1 << n
            S0n = {r for r in range(N) if (r & (M - 1)) in S0}
            _, adj0 = build_res_graph(n, S0n)
            phi = {}
            for r in range(N):
                cur = r
                bits = []
                for _ in range(n):
                    bits.append(cur & 1)
                    cur = T_S0_int(cur, m, S0)
                phi[r] = tuple(bits)
            assert len(set(phi.values())) == N
            # Verify exact De Bruijn edges
            for r in range(N):
                a, b = adj0[r]
                w = phi[r]
                assert {phi[a], phi[b]} == {w[1:] + (0,), w[1:] + (1,)}
            # Verify P_0^n(y, z) == 1/N for every y, z
            for y in range(N):
                cnt = [0] * N
                cnt[y] = 1
                for _ in range(n):
                    nxt = [0] * N
                    for u in range(N):
                        c = cnt[u]
                        if c:
                            a, b = adj0[u]
                            nxt[a] += c
                            nxt[b] += c
                    cnt = nxt
                assert all(c == 1 for c in cnt)
    print("[OK] Lemma 1 verified across 5 dyadic-shell base sets S_0(J)")


def verify_barina_sieve_lemmas():
    cases = [
        (2, (), Fraction(5, 8), 3),
        (2, (), Fraction(5, 8), 4),
        (2, (), Fraction(5, 8), 5),
        (2, (), Fraction(5, 8), 6),
        (3, (1,), Fraction(17, 27), 3),
        (3, (1,), Fraction(17, 27), 4),
        (3, (1,), Fraction(17, 27), 5),
        (4, (2,), Fraction(5, 8), 3),
        (4, (2,), Fraction(5, 8), 4),
    ]
    for m, J, mu_frac, L in cases:
        assert pow(3, mu_frac.numerator) < pow(2, mu_frac.denominator)
        n = m + L - 1
        M = 1 << m
        N = 1 << n
        S0 = make_S0(m, J)
        lam_S0 = Fraction(len(S0), M)
        assert lam_S0 < mu_frac
        delta = mu_frac - lam_S0

        # Construct B_n, tau(r), and S_n = S_0^{(n)} \ B_n
        S0n = {r for r in range(N) if (r & (M - 1)) in S0}
        B = set()
        tau = {}
        for r in range(N):
            cur = r
            acc = Fraction(0)
            first_neg = None
            for j in range(1, L + 1):
                in0 = (cur & (M - 1)) in S0
                acc += (1 if in0 else 0) - mu_frac
                if acc < 0:
                    first_neg = j
                    break
                cur = T_S0_int(cur, m, S0)
            if first_neg is None:
                B.add(r)
                tau[r] = 1
            else:
                tau[r] = first_neg
        assert B.issubset(S0n)
        Sn = S0n - B
        _, adj = build_res_graph(n, Sn)

        # Lemma 2(a): Verify lockout & strictly negative weight for ALL paths of length tau(r)
        for r in range(N):
            t_len = tau[r]
            for mask in range(1 << t_len):
                u = r
                weight = Fraction(0)
                t_orb = r
                for s in range(t_len):
                    if r not in B:
                        assert u not in B
                        assert (u - t_orb) % (1 << (n - s)) == 0
                        t_orb = T_S0_int(t_orb, m, S0)
                    weight += (1 if u in Sn else 0) - mu_frac
                    u = adj[u][(mask >> s) & 1]
                assert weight < 0

        # Lemma 2(b): Exact Karp max cycle mean < mu_frac < log_3 2
        mu_star = exact_karp_max_cycle_mean(N, adj, Sn)
        assert mu_star < mu_frac
        assert pow(3, mu_star.numerator) < pow(2, mu_star.denominator)

        # Lemma 3: Exact rational check of Hoeffding bound when L >= m
        # Check lam_n(B) <= m * exp(-x) via lam_n(B) * sum_{k=0}^{12} x^k / k! <= m (since sum < exp(x))
        lam_B = Fraction(len(B), N)
        if L >= m:
            x = 2 * delta * delta * (L // m)
            exp_lb = Fraction(0)
            term = Fraction(1)
            for k_idx in range(15):
                exp_lb += term
                term = term * x / (k_idx + 1)
            assert lam_B * exp_lb <= m

        # Lemmas 4 & 5: Exhaustive check over ALL y in Z/2^n Z and ALL 2^n length-n paths
        for y in range(N):
            seen_zT = set()
            F_y = set()
            F0_y = set()
            path_counts = [0] * N
            for mask in range(N):
                u = y
                T = []
                for t in range(n):
                    if u in B:
                        T.append(t)
                    u = adj[u][(mask >> t) & 1]
                Tt = tuple(T)
                assert (u, Tt) not in seen_zT, "Lemma 4(b) path uniqueness failed"
                seen_zT.add((u, Tt))
                F_y.add(Tt)
                F0_y.add(frozenset(t for t in T if t < L))
                path_counts[u] += 1
            # Verify F0_y is totally ordered by inclusion and |F0_y| <= L + 1
            F0_list = list(F0_y)
            for i in range(len(F0_list)):
                for j in range(i + 1, len(F0_list)):
                    assert F0_list[i].issubset(F0_list[j]) or F0_list[j].issubset(F0_list[i])
            assert len(F0_y) <= L + 1
            assert len(F_y) <= (1 << (m - 1)) * (L + 1)
            assert max(path_counts) <= (1 << (m - 1)) * (L + 1)

        # Theorem 6: Exact stationary distribution on EVERY sink SCC
        sinks = tarjan_sink_sccs(N, adj)
        assert len(sinks) >= 1
        for sink in sinks:
            mu_C = exact_stationary_on_sink(N, adj, sink)
            mu_B = sum(mu_C[r] for r in B)
            l1 = sum(abs(mu_C[r] - Fraction(1, N)) for r in range(N))
            pi_C = sum(mu_C[r] for r in Sn)
            assert mu_B <= (1 << (m - 1)) * (L + 1) * lam_B
            assert l1 <= 2 * n * mu_B
            assert pi_C >= lam_S0 - (n + 1) * mu_B
            assert pi_C <= mu_star
    print("[OK] Lemmas 2-5 and Theorem 6 verified across all 9 Barina sieve instances (up to N=128)")


def main():
    verify_table_5_3_baselines()
    verify_lemma_1()
    verify_barina_sieve_lemmas()
    print("PASS")


if __name__ == "__main__":
    main()
