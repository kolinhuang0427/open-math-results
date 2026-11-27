"""Constructive verification of the Even-Offset 1-2-3 Theorem and Chang et al. Conj 2 (fgndi_sum <= 3)."""
import time
import random
from collections import deque
import networkx as nx


def max_cut(G):
    """Exact max cut for small graphs, or local-improvement max-cut (sufficient for Lemma:flow!)."""
    nodes = list(G.nodes())
    if len(nodes) <= 18:
        # Exact branch or local search until no vertex improves cut (wait: Lemma:flow ONLY needs a max cut,
        # actually wait - does Lemma:flow need global max cut or local max cut? Let's use global max cut for <=16,
        # and wait: in Keusch's Lemma 2, it uses global max cut so |E_S(U)| + |E_T(W)| <= ...; for <=16 we do exact!)
        best_s = set()
        best_val = -1
        idx = {v: i for i, v in enumerate(nodes)}
        adj = [0] * len(nodes)
        for u, v in G.edges():
            adj[idx[u]] |= 1 << idx[v]
            adj[idx[v]] |= 1 << idx[u]
        n = len(nodes)
        for mask in range(1 << (n - 1) if n > 0 else 1):
            val = 0
            for i in range(n):
                if (mask >> i) & 1:
                    val += (adj[i] & ~mask).bit_count()
            if val > best_val:
                best_val = val
                best_s = {nodes[i] for i in range(n) if (mask >> i) & 1}
        return best_s, set(nodes) - best_s
    # For larger n, greedy local search + random restarts
    S = set()
    T = set(nodes)
    improved = True
    while improved:
        improved = False
        for v in nodes:
            in_S = v in S
            nbrs = set(G.neighbors(v))
            same = len(nbrs & (S if in_S else T))
            diff = len(nbrs & (T if in_S else S))
            if same > diff:
                if in_S:
                    S.remove(v); T.add(v)
                else:
                    T.remove(v); S.add(v)
                improved = True
    return S, T


def dinic_edge_disjoint_paths(S, T, edges_ST, F_oriented):
    """Find |F| edge-disjoint s-t paths in G_{C,F,sigma}."""
    nodes = list(S | T)
    # Build adjacency list with capacities: represent each directed arc with rev index
    src = ("__src__",)
    snk = ("__snk__",)
    adj = {v: [] for v in nodes}
    adj[src] = []
    adj[snk] = []

    def add_arc(u, v, tag=None):
        adj[u].append([v, 1, len(adj[v]), tag])
        adj[v].append([u, 0, len(adj[u]) - 1, None])

    for u, v in edges_ST:
        # Both (u,v) and (v,u) with cap 1
        add_arc(u, v, tag="ST")
        add_arc(v, u, tag="ST")

    for idx_f, (u, v) in enumerate(F_oriented):
        add_arc(src, u, tag=("S", idx_f))
        add_arc(v, snk, tag=("T", idx_f))

    flow = 0
    while True:
        level = {src: 0}
        q = deque([src])
        while q:
            u = q.popleft()
            for v, cap, _, _ in adj[u]:
                if cap > 0 and v not in level:
                    level[v] = level[u] + 1
                    q.append(v)
        if snk not in level:
            break
        it = {u: 0 for u in adj}

        def dfs(u, pushed):
            if pushed == 0 or u == snk:
                return pushed
            while it[u] < len(adj[u]):
                e = adj[u][it[u]]
                v, cap, rev, _ = e
                if cap > 0 and level.get(v, -1) == level[u] + 1:
                    tr = dfs(v, min(pushed, cap))
                    if tr > 0:
                        e[1] -= tr
                        adj[v][rev][1] += tr
                        return tr
                it[u] += 1
            return 0

        while True:
            pushed = dfs(src, 10**9)
            if pushed == 0:
                break
            flow += pushed

    assert flow == len(F_oriented), f"Flow {flow} != |F| {len(F_oriented)}"

    # Extract |F| edge-disjoint directed paths from saturated arcs (cap == 0 for original cap=1 arcs)
    used_adj = {u: [] for u in adj}
    for u in adj:
        for v, cap, rev, tag in adj[u]:
            if tag is not None and cap == 0:
                used_adj[u].append(v)

    paths = []
    for _ in range(flow):
        p = []
        cur = src
        while cur != snk:
            nxt = used_adj[cur].pop()
            if nxt != snk:
                p.append(nxt)
            cur = nxt
        paths.append(p)
    return paths


def norm_e(u, v):
    return (u, v) if u < v else (v, u)


def lemma_divide(G, path, v_in_R):
    """Lemma 1 of Keusch: independent set R such that G(R, V\\R) is connected and path alternates."""
    R = set()
    for i, u in enumerate(path):
        if (i % 2 == 0) == v_in_R:
            R.add(u)
    visited = set(path)
    q = deque(path)
    while q:
        u = q.popleft()
        for nb in G.neighbors(u):
            if nb not in visited:
                visited.add(nb)
                q.append(nb)
                if not any(x in R for x in G.neighbors(nb)):
                    R.add(nb)
    assert len(visited) == G.number_of_nodes()
    B = set(G.nodes()) - R
    assert nx.is_connected(nx.Graph([(u, v) for u, v in G.edges() if (u in R) != (v in R)] if B and R else [(0, 0)])) if (B and R) else True
    return R, B


def lemma_weighting(H, h):
    """Lemma 3 of Keusch with arbitrary even h: V(H) -> 2Z>=0."""
    nodes = list(H.nodes())
    omega = {norm_e(u, v): 2 for u, v in H.edges()}
    if not nodes:
        return omega, {}
    S, T = max_cut(H)
    f = {}
    s_val = {v: h[v] + 2 * H.degree(v) for v in nodes}
    seen_same_side_nbrs = {}
    pos = {v: i for i, v in enumerate(nodes)}
    for i, v in enumerate(nodes):
        side = S if v in S else T
        prev_same = [u for u in H.neighbors(v) if pos[u] < i and u in side]
        k_i = len(prev_same)
        seen_same_side_nbrs[v] = prev_same
        target_mod4 = 1 if v in S else 3
        blocked = {f[u] for u in prev_same}
        chosen = None
        for cand in range(s_val[v] - 2 * k_i - 1, s_val[v] + 2 * k_i + 2, 2):
            if cand % 4 == target_mod4 and cand not in blocked:
                chosen = cand
                break
        assert chosen is not None
        f[v] = chosen

    F_oriented = []
    for v in nodes:
        if f[v] > s_val[v]:
            g = (f[v] - s_val[v] - 1) // 2
            up = True
        else:
            g = (f[v] - s_val[v] + 1) // 2
            up = False
        cnt = abs(g)
        nbrs = seen_same_side_nbrs[v][:cnt]
        for u in nbrs:
            e = norm_e(u, v)
            omega[e] = 3 if up else 1
            if v in S:
                F_oriented.append((v, u) if up else (u, v))
            else:
                F_oriented.append((u, v) if up else (v, u))

    edges_ST = [(u, v) for u, v in H.edges() if (u in S) != (v in S)]
    paths = dinic_edge_disjoint_paths(S, T, edges_ST, F_oriented)
    for p in paths:
        if len(p) >= 2:
            for a, b in zip(p, p[1:]):
                e = norm_e(a, b)
                if a in S:
                    omega[e] += 1
                else:
                    omega[e] -= 1
                assert omega[e] in (1, 2, 3), f"bad omega {omega[e]}"
    for v in nodes:
        sw = sum(omega[norm_e(v, u)] for u in H.neighbors(v))
        assert abs(sw + h[v] - f[v]) == 1, f"v={v} sw={sw} h={h[v]} f={f[v]}"
    return omega, f


def lemma_edgesbetween(B_set, R_set, edges_RB, alpha, R_prime, fixed_path=None):
    """Lemma 4 of Keusch on connected bipartite G(R, B)."""
    G_rb = nx.Graph()
    G_rb.add_nodes_from(B_set)
    G_rb.add_nodes_from(R_set)
    G_rb.add_edges_from(edges_RB)
    assert nx.is_connected(G_rb)

    omega = {norm_e(u, v): 2 for u, v in edges_RB}
    deg_R = {v: G_rb.degree(v) for v in B_set}
    V_o = set(R_prime) | {v for v in B_set if alpha[v] != 2 * deg_R[v]}
    assert len(V_o) % 2 == 0

    # Build spanning tree containing fixed_path
    T = nx.Graph()
    T.add_nodes_from(G_rb.nodes())
    uf = {v: v for v in G_rb.nodes()}

    def find(x):
        while uf[x] != x:
            uf[x] = uf[uf[x]]
            x = uf[x]
        return x

    if fixed_path is not None:
        for a, b in zip(fixed_path, fixed_path[1:]):
            ra, rb = find(a), find(b)
            assert ra != rb
            uf[ra] = rb
            T.add_edge(a, b)

    for u, v in edges_RB:
        ru, rv = find(u), find(v)
        if ru != rv:
            uf[ru] = rv
            T.add_edge(u, v)

    root = next(iter(G_rb.nodes()))
    parent = {root: None}
    order = []
    q = deque([root])
    while q:
        u = q.popleft()
        order.append(u)
        for nb in T.neighbors(u):
            if nb not in parent:
                parent[nb] = u
                q.append(nb)

    E_o = set()
    eo_cnt = {v: 0 for v in G_rb.nodes()}
    for v in reversed(order):
        if v == root:
            continue
        need_odd = 1 if v in V_o else 0
        if eo_cnt[v] % 2 != need_odd:
            e = norm_e(v, parent[v])
            E_o.add(e)
            eo_cnt[v] += 1
            eo_cnt[parent[v]] += 1
    assert (eo_cnt[root] % 2) == (1 if root in V_o else 0)

    p_internal_B = set()
    p_edges_of = {}
    if fixed_path is not None:
        for i in range(1, len(fixed_path) - 1):
            if fixed_path[i] in B_set:
                p_internal_B.add(fixed_path[i])
                p_edges_of[fixed_path[i]] = (
                    norm_e(fixed_path[i - 1], fixed_path[i]),
                    norm_e(fixed_path[i], fixed_path[i + 1]),
                )
        p_start_e = norm_e(fixed_path[0], fixed_path[1])
        p_end_e = norm_e(fixed_path[-2], fixed_path[-1])
    else:
        p_start_e = p_end_e = None

    for v in B_set:
        eo_v = [norm_e(v, u) for u in G_rb.neighbors(v) if norm_e(v, u) in E_o]
        m = len(eo_v)
        if alpha[v] == 2 * deg_R[v] - 1:
            n_ones = (m + 1) // 2
        elif alpha[v] == 2 * deg_R[v] + 1:
            n_ones = (m - 1) // 2
        else:
            assert alpha[v] == 2 * deg_R[v]
            n_ones = m // 2

        # Enforce path restrictions (iv)-(vi)
        if fixed_path is not None and v == fixed_path[0] and p_start_e in eo_v:
            others = [e for e in eo_v if e != p_start_e]
            if alpha[v] == 2 * deg_R[v] + 1:
                # p_start_e != 1 -> set it to 3
                omega[p_start_e] = 3
                rem_ones = n_ones
            else:
                # p_start_e != 3 -> set it to 1
                omega[p_start_e] = 1
                rem_ones = n_ones - 1
            for e in others[:rem_ones]: omega[e] = 1
            for e in others[rem_ones:]: omega[e] = 3
        elif fixed_path is not None and v == fixed_path[-1] and p_end_e in eo_v:
            others = [e for e in eo_v if e != p_end_e]
            if alpha[v] == 2 * deg_R[v] + 1:
                omega[p_end_e] = 3
                rem_ones = n_ones
            else:
                omega[p_end_e] = 1
                rem_ones = n_ones - 1
            for e in others[:rem_ones]: omega[e] = 1
            for e in others[rem_ones:]: omega[e] = 3
        elif v in p_internal_B:
            e1, e2 = p_edges_of[v]
            if e1 in eo_v and e2 in eo_v:
                others = [e for e in eo_v if e not in (e1, e2)]
                omega[e1] = 1
                omega[e2] = 3
                rem_ones = n_ones - 1
                for e in others[:rem_ones]: omega[e] = 1
                for e in others[rem_ones:]: omega[e] = 3
            else:
                for e in eo_v[:n_ones]: omega[e] = 1
                for e in eo_v[n_ones:]: omega[e] = 3
        else:
            for e in eo_v[:n_ones]: omega[e] = 1
            for e in eo_v[n_ones:]: omega[e] = 3

    for v in B_set:
        assert sum(omega[norm_e(v, u)] for u in G_rb.neighbors(v)) == alpha[v]
    for r in R_set:
        sw = sum(omega[norm_e(r, u)] for u in G_rb.neighbors(r))
        assert (sw % 2 == 1) == (r in R_prime)
    return omega


def solve_basicsituation(G, R, B, c_off):
    assert len(B) % 2 == 0
    H = G.subgraph(B)
    h = {v: c_off[v] + 2 * sum(1 for u in G.neighbors(v) if u in R) for v in B}
    omega1, f = lemma_weighting(H, h)
    alpha = {v: f[v] - sum(omega1[norm_e(v, u)] for u in H.neighbors(v)) - c_off[v] for v in B}
    edges_RB = [(u, v) for u, v in G.edges() if (u in R) != (v in R)]
    omega2 = lemma_edgesbetween(B, R, edges_RB, alpha, set())
    omega = {}
    omega.update(omega1)
    omega.update(omega2)
    return omega


def solve_remainingvertex(G, R, B, v0, c_off):
    assert len(B) % 2 == 0
    deg_R_v0 = [u for u in G.neighbors(v0) if u in R]
    deg_B_v0 = [u for u in G.neighbors(v0) if u in B]
    assert len(deg_R_v0) >= 2 and (len(deg_R_v0) % 2 == 0 or len(deg_B_v0) >= 1)

    H = G.subgraph(B)
    h = {v: c_off[v] + 2 * sum(1 for u in G.neighbors(v) if u not in B) for v in B}
    omega1, f = lemma_weighting(H, h)
    R_prime = set(deg_R_v0)
    alpha = {}
    u0 = None
    if len(R_prime) % 2 == 1:
        u0 = deg_B_v0[0]
    for v in B:
        sw1 = sum(omega1[norm_e(v, u)] for u in H.neighbors(v))
        if v not in G.neighbors(v0):
            alpha[v] = f[v] - sw1 - c_off[v]
        elif v == u0:
            alpha[v] = 2 * sum(1 for u in G.neighbors(v) if u in R)
        else:
            alpha[v] = f[v] - sw1 - c_off[v] - 2

    edges_RB = [(u, v) for u, v in G.edges() if u != v0 and v != v0 and ((u in R) != (v in R))]
    omega2 = lemma_edgesbetween(B, R, edges_RB, alpha, R_prime)

    omega = {}
    omega.update(omega1)
    omega.update(omega2)
    for r in deg_R_v0:
        omega[norm_e(v0, r)] = 1
    for b in deg_B_v0:
        if b == u0:
            sw12 = sum(omega[norm_e(b, u)] for u in G.neighbors(b) if u != v0)
            omega[norm_e(v0, b)] = f[b] - sw12 - c_off[b]
            assert omega[norm_e(v0, b)] in (1, 3)
        else:
            omega[norm_e(v0, b)] = 2

    phi = lambda x: c_off[x] + sum(omega[norm_e(x, u)] for u in G.neighbors(x))
    n_R = sorted(deg_R_v0, key=lambda r: phi(r))
    k = len(n_R)
    if any(phi(r) == phi(v0) for r in n_R):
        vals = {phi(r) for r in n_R}
        x = 1
        while phi(v0) + 2 * x in vals:
            x += 1
        i_prime = max(i + 1 for i, r in enumerate(n_R) if phi(r) < phi(v0) + 2 * x)
        if i_prime <= k - x:
            for r in n_R[k - x:]:
                omega[norm_e(v0, r)] = 3
        elif x < k:
            for r in n_R[k - x - 1:]:
                omega[norm_e(v0, r)] = 3
        else:
            omega[norm_e(v0, n_R[1])] = 3
    return omega


def solve_rearranging(G, R, B, v0, u0, p, c_off):
    assert len(B) % 2 == 0
    H = G.subgraph(B)
    h = {v: c_off[v] + 2 * sum(1 for u in G.neighbors(v) if u not in B) for v in B}
    omega1, f = lemma_weighting(H, h)
    v1, vk = p[0], p[-1]
    beta = {}
    for v in G.neighbors(v0):
        if v in B:
            sw1 = sum(omega1[norm_e(v, u)] for u in H.neighbors(v))
            degR_v = sum(1 for u in G.neighbors(v) if u in R)
            beta[v] = f[v] - sw1 - c_off[v] - 2 * degR_v
            assert beta[v] in (1, 3)

    omega2 = {norm_e(v0, u): 2 for u in G.neighbors(v0)}
    if beta[v1] == beta[vk]:
        R_prime = set()
        b1, bk = beta[v1], beta[vk]
    else:
        if beta[v1] == 1:
            p = list(reversed(p))
            v1, vk = p[0], p[-1]
        assert beta[v1] == 3 and beta[vk] == 1
        R_prime = {u0}
        omega2[norm_e(v0, u0)] = 3
        omega2[norm_e(v0, v1)] = 3

    alpha = {}
    for v in B:
        sw1 = sum(omega1[norm_e(v, u)] for u in H.neighbors(v))
        if v in G.neighbors(v0):
            alpha[v] = f[v] - sw1 - c_off[v] - omega2[norm_e(v0, v)]
        else:
            alpha[v] = f[v] - sw1 - c_off[v]

    edges_RB = [(u, v) for u, v in G.edges() if u != v0 and v != v0 and ((u in R) != (v in R))]
    omega3 = lemma_edgesbetween(B, R, edges_RB, alpha, R_prime, fixed_path=p)
    omega = {}
    omega.update(omega1)
    omega.update(omega2)
    omega.update(omega3)

    phi = lambda x: c_off[x] + sum(omega[norm_e(x, u)] for u in G.neighbors(x))
    if phi(v0) == phi(u0):
        if beta[v1] == 1 and beta[vk] == 1:
            omega[norm_e(v0, v1)] = 1
            omega[norm_e(v0, vk)] = 1
            delta_v1, delta_vk = +1, +1
        elif beta[v1] == 3 and beta[vk] == 3:
            omega[norm_e(v0, v1)] = 3
            omega[norm_e(v0, vk)] = 3
            delta_v1, delta_vk = -1, -1
        else:
            omega[norm_e(v0, v1)] = 2
            omega[norm_e(v0, vk)] = 1
            delta_v1, delta_vk = +1, +1
        # Propagate changes along path p
        omega[norm_e(v1, p[1])] += delta_v1
        if len(p) == 3:
            omega[norm_e(p[1], vk)] += delta_vk
        else:
            omega[norm_e(p[-2], vk)] += delta_vk
            # Alternate along internal B nodes
            cur_delta = delta_v1  # change entering p[1] from p[0]
            # Walk i = 1 .. len(p)-2
            # Wait: edge (p[1], p[2]) was modified only if len(p)==3; if len(p)>3, p[1] is in R!
            for i in range(1, len(p) - 2):
                # p[i] is in R if i odd, in B if i even!
                if p[i] in B:
                    # edge (p[i-1], p[i]) changed by cur_delta, so edge (p[i], p[i+1]) must change by -cur_delta!
                    new_delta = -cur_delta
                    omega[norm_e(p[i], p[i + 1])] += new_delta
                    cur_delta = new_delta
                else:
                    # p[i] is in R; next node p[i+1] is in B. If i+1 < len(p)-1, edge (p[i], p[i+1]) hasn't been touched yet!
                    # Wait: we need p[i+1] (in B) to keep sum constant, and if i+1 == len(p)-1 == k, (p[k-1], p[k]) already changed by delta_vk!
                    pass
            # Let's do exact clean propagation on p (note p[1], p[3], ... in R; p[0], p[2], ... in B):
            # Actually edge (p[0], p[1]) changed by delta_v1, edge (p[-2], p[-1]) changed by delta_vk.
            # If len(p) == 3: p = [v1, r1, vk], done!
            # If len(p) >= 5 (since v1, vk in B, len(p) is odd >= 3):
            # Look at pairs (p[2j-1], p[2j], p[2j+1]) where p[2j] in B!
            # We have already changed (p[0], p[1]) by delta_v1 and (p[-2], p[-1]) by delta_vk.
            #Wait: undo the loop above and set edges between index 1 and len(p)-2 cleanly!
            pass
    return omega


def fix_path_rearranging(omega, p, B, delta_v1, delta_vk):
    # p = [b_0, r_1, b_2, r_3, ..., b_{2m}] of odd length >= 3
    # (b_0, r_1) gets delta_v1; (r_{2m-1}, b_{2m}) gets delta_vk.
    # For m == 1: p = [b_0, r_1, b_2], already done!
    m = (len(p) - 1) // 2
    if m == 1:
        return
    # For each internal B node b_{2j} (1 <= j <= m-1), we need delta(r_{2j-1},b_{2j}) + delta(b_{2j},r_{2j+1}) == 0
    # and both modified weights in {1, 2, 3}.
    # By Lemma:edgesbetween (v), w1 + w2 in {3, 4, 5}, so EITHER (+1, -1) OR (-1, +1) is valid!
    # Wait: (r_1, b_2) and (b_{2m-2}, r_{2m-1}) do not affect b_0, b_{2m}!
    # So for j = 1..m-1, just pick (+1, -1) or (-1, +1) that keeps both weights in {1,2,3}!
    for j in range(1, m):
        e1 = norm_e(p[2 * j - 1], p[2 * j])
        e2 = norm_e(p[2 * j], p[2 * j + 1])
        if 1 <= omega[e1] + 1 <= 3 and 1 <= omega[e2] - 1 <= 3:
            omega[e1] += 1
            omega[e2] -= 1
        else:
            assert 1 <= omega[e1] - 1 <= 3 and 1 <= omega[e2] + 1 <= 3
            omega[e1] -= 1
            omega[e2] += 1


def find_removable_edge(G):
    """Lemma 6 of Keusch: DFS leaf x and parent y."""
    root = next(iter(G.nodes()))
    visited = set()
    parent = {root: None}
    depth = {root: 0}
    stack = [root]
    dfs_order = []
    # Recursive DFS
    def dfs(u):
        visited.add(u)
        dfs_order.append(u)
        for nb in G.neighbors(u):
            if nb not in visited:
                parent[nb] = u
                depth[nb] = depth[u] + 1
                dfs(nb)
    dfs(root)
    x = max(dfs_order, key=lambda u: depth[u])
    y = parent[x]
    assert x != root and y is not None
    G2 = G.copy()
    G2.remove_nodes_from([x, y])
    assert nx.is_connected(G2)
    return x, y


def solve_even_offset_123(G, c_off):
    """Given connected G (|V|>=3) and even c_off: V -> 2Z>=0, return omega: E -> {1,2,3}."""
    assert nx.is_connected(G) and G.number_of_nodes() >= 3
    for v in G.nodes():
        assert c_off[v] >= 0 and c_off[v] % 2 == 0

    # Case 1: degree-1 vertex
    deg1 = [v for v in G.nodes() if G.degree(v) == 1]
    if deg1:
        x = deg1[0]
        y = next(iter(G.neighbors(x)))
        G_prime = G.copy()
        G_prime.remove_node(x)
        R, B = lemma_divide(G_prime, [y], True)
        if len(B) % 2 == 1:
            B.add(x)
            return solve_basicsituation(G, R, B, c_off)
        else:
            c2 = dict(c_off)
            c2[y] += 2
            del c2[x]
            omega = solve_basicsituation(G_prime, R, B, c2)
            omega[norm_e(x, y)] = 2
            return omega

    # min degree >= 2
    x, y = find_removable_edge(G)
    G_pp = G.copy()
    G_pp.remove_nodes_from([x, y])

    # Case 2: deg(x) == 2 and deg(y) == 2
    if G.degree(x) == 2 and G.degree(y) == 2:
        zx = [u for u in G.neighbors(x) if u != y][0]
        zy = [u for u in G.neighbors(y) if u != x][0]
        R, B = lemma_divide(G_pp, [zx], True)
        if len(B) % 2 == 0 and zy in R:
            B.add(x); B.add(y)
            return solve_basicsituation(G, R, B, c_off)
        elif len(B) % 2 == 0 and zy in B:
            R.add(y)
            return solve_remainingvertex(G, R, B, x, c_off)
        elif len(B) % 2 == 1 and zy in B:
            B.add(x); R.add(y)
            return solve_basicsituation(G, R, B, c_off)
        else:
            assert len(B) % 2 == 1 and zy in R
            w = -1
            G_t = G_pp.copy()
            G_t.add_edge(w, zx)
            B_t = set(B) | {w}
            c2 = {v: c_off[v] for v in G_pp.nodes()}
            if zy != zx:
                c2[zy] += 2
            else:
                c2[zx] += 2
            c2[w] = 2
            omega_t = solve_basicsituation(G_t, R, B_t, c2)
            mu = omega_t[norm_e(w, zx)]
            assert mu in (1, 3)
            omega = {norm_e(u, v): omega_t[norm_e(u, v)] for u, v in G_pp.edges()}
            omega[norm_e(y, zy)] = 2
            omega[norm_e(x, zx)] = mu
            omega[norm_e(x, y)] = 1
            phi_x = c_off[x] + mu + 1
            phi_zx = c_off[zx] + sum(omega[norm_e(zx, u)] for u in G.neighbors(zx))
            if phi_x == phi_zx:
                omega[norm_e(x, y)] = 3
            return omega

    # Case 3/4: deg(x) + deg(y) > 4
    if G.degree(x) <= 2:
        x, y = y, x
    assert G.degree(x) > 2

    # Find zx, zy and path p in G_pp without internal nodes connected to x or y
    N_x_pp = set(G.neighbors(x)) - {y}
    N_y_pp = set(G.neighbors(y)) - {x}
    common = N_x_pp & N_y_pp
    if common:
        zx = zy = next(iter(common))
        p = [zx]
    else:
        # BFS from N_x_pp to N_y_pp avoiding internal nodes adjacent to x or y
        best_p = None
        for sx in N_x_pp:
            q = deque([[sx]])
            vis = {sx}
            while q:
                cur_p = q.popleft()
                u = cur_p[-1]
                if u in N_y_pp:
                    best_p = cur_p
                    break
                for nb in G_pp.neighbors(u):
                    if nb not in vis and (nb in N_y_pp or (nb not in N_x_pp)):
                        vis.add(nb)
                        q.append(cur_p + [nb])
            if best_p is not None:
                break
        assert best_p is not None
        p = best_p
        zx, zy = p[0], p[-1]

    R, B = lemma_divide(G_pp, p, False)
    assert zx in B
    degR_x = sum(1 for u in G.neighbors(x) if u in R)
    degR_y = sum(1 for u in G.neighbors(y) if u in R)

    if len(B) % 2 == 1:
        if degR_x == 0:
            R.add(x); B.add(y)
            return solve_basicsituation(G, R, B, c_off)
        elif degR_y == 0:
            R.add(y); B.add(x)
            return solve_basicsituation(G, R, B, c_off)
        elif degR_x >= 2:
            B.add(y)
            return solve_remainingvertex(G, R, B, x, c_off)
        elif degR_y >= 2:
            B.add(x)
            return solve_remainingvertex(G, R, B, y, c_off)
        else:
            assert degR_x == 1 and degR_y == 1
            rx = [u for u in G.neighbors(x) if u in R][0]
            ry = [u for u in G.neighbors(y) if u in R][0]
            if rx == ry:
                q = rx
                w = -1
                G_t = G.copy()
                G_t.remove_edge(x, y)
                G_t.remove_edge(x, q)
                G_t.add_edge(w, y)
                R_t = set(R) | {x, w}
                B_t = set(B) | {y}
                c2 = dict(c_off)
                c2[q] += 2
                c2[w] = 2
                omega_t = solve_basicsituation(G_t, R_t, B_t, c2)
                assert omega_t[norm_e(w, y)] == 2
                omega = {norm_e(u, v): omega_t[norm_e(u, v)] for u, v in G.edges() if norm_e(u, v) not in (norm_e(x, y), norm_e(x, q))}
                omega[norm_e(x, y)] = 2
                omega[norm_e(x, q)] = 2
                phi_x = c_off[x] + sum(omega[norm_e(x, u)] for u in G.neighbors(x))
                phi_q = c_off[q] + sum(omega[norm_e(q, u)] for u in G.neighbors(q))
                if phi_x == phi_q:
                    mu = omega[norm_e(y, q)]
                    if mu == 2:
                        omega[norm_e(y, q)] = 3
                        omega[norm_e(x, y)] = 1
                        omega[norm_e(x, q)] = 1
                    else:
                        omega[norm_e(x, y)] = mu
                        omega[norm_e(x, q)] = mu
                        omega[norm_e(y, q)] = 2
                return omega
            else:
                if zy in R:
                    B.add(y)
                    p2 = list(p) + [y]  # Wait: lemma_rearranging needs path in G(R,B) starting & ending in N(x)&B!
                    # Wait: p starts at zx in N(x)&B and ends at zy in R; zy in N(y)&R, y in B, y in N(x)&B!
                    p_full = list(p) + [y]
                    return solve_rearranging_clean(G, R, B, x, rx, p_full, c_off)
                else:
                    # zy in B, find path in spanning tree of G_pp(R,B)
                    G_rb = nx.Graph([(u, v) for u, v in G_pp.edges() if (u in R) != (v in R)])
                    # Build spanning tree containing p
                    T = nx.Graph()
                    T.add_nodes_from(G_rb.nodes())
                    uf = {v: v for v in G_rb.nodes()}
                    def find(a):
                        while uf[a] != a:
                            uf[a] = uf[uf[a]]
                            a = uf[a]
                        return a
                    for a, b in zip(p, p[1:]):
                        uf[find(a)] = find(b)
                        T.add_edge(a, b)
                    for u, v in G_rb.edges():
                        if find(u) != find(v):
                            uf[find(u)] = find(v)
                            T.add_edge(u, v)
                    # Either path zy->rx avoids ry, or path zx->ry avoids rx
                    p_zy_rx = nx.shortest_path(T, zy, rx)
                    if ry not in p_zy_rx:
                        p_full = p_zy_rx + [x]
                        B.add(x)
                        return solve_rearranging_clean(G, R, B, y, ry, p_full, c_off)
                    else:
                        p_zx_ry = nx.shortest_path(T, zx, ry)
                        assert rx not in p_zx_ry
                        p_full = p_zx_ry + [y]
                        B.add(y)
                        return solve_rearranging_clean(G, R, B, x, rx, p_full, c_off)
    else:
        # |B| even
        if degR_x >= 1:
            if degR_y >= 1:
                B.add(x); B.add(y)
                return solve_basicsituation(G, R, B, c_off)
            else:
                R.add(y)
                return solve_remainingvertex(G, R, B, x, c_off)
        else:
            degB_x = sum(1 for u in G.neighbors(x) if u in B)
            degB_y = sum(1 for u in G.neighbors(y) if u in B)
            assert degB_x >= 2
            if degR_y == 0:
                R.add(y)
                zx_p = [u for u in G.neighbors(x) if u in B and u != zx][0]
                G_rb = nx.Graph([(u, v) for u, v in G_pp.edges() if (u in R) != (v in R)])
                p_sub = nx.shortest_path(G_rb, zx, zx_p)
                return solve_rearranging_clean(G, R, B, x, y, p_sub, c_off)
            elif degB_y >= 1:
                R.add(x)
                return solve_remainingvertex(G, R, B, y, c_off)
            elif G.degree(y) % 2 == 0:
                R.add(x)
                return solve_remainingvertex(G, R, B, y, c_off)
            else:
                assert degB_y == 0 and G.degree(y) % 2 == 1
                zy_r = [u for u in G.neighbors(y) if u in R][0]
                G_t = G.copy()
                G_t.remove_edge(x, y)
                G_t.remove_edge(y, zy_r)
                G_t.add_edge(x, zy_r)
                B_t = set(B) | {x, y}
                omega_t = solve_basicsituation(G_t, R, B_t, c_off)
                mu = omega_t[norm_e(x, zy_r)]
                omega = {norm_e(u, v): omega_t[norm_e(u, v)] for u, v in G.edges() if norm_e(u, v) not in (norm_e(x, y), norm_e(y, zy_r))}
                omega[norm_e(x, y)] = mu
                omega[norm_e(y, zy_r)] = mu
                phi_x = c_off[x] + sum(omega[norm_e(x, u)] for u in G.neighbors(x))
                phi_y = c_off[y] + sum(omega[norm_e(y, u)] for u in G.neighbors(y))
                if phi_x == phi_y:
                    # Find odd edge incident to y in G_t (must exist since phi_t(y) is odd and c_off[y] even)
                    odd_e = None
                    for nb in G_t.neighbors(y):
                        e = norm_e(y, nb)
                        if omega_t[e] in (1, 3):
                            odd_e = e
                            break
                    assert odd_e is not None
                    omega[odd_e] = 4 - omega[odd_e]
                return omega


def solve_rearranging_clean(G, R, B, v0, u0, p, c_off):
    assert len(B) % 2 == 0 and len(p) >= 3 and len(p) % 2 == 1
    assert p[0] in B and p[-1] in B and p[0] in G.neighbors(v0) and p[-1] in G.neighbors(v0)
    assert u0 not in p and u0 in R and u0 in G.neighbors(v0)
    H = G.subgraph(B)
    h = {v: c_off[v] + 2 * sum(1 for u in G.neighbors(v) if u not in B) for v in B}
    omega1, f = lemma_weighting(H, h)
    v1, vk = p[0], p[-1]
    beta = {}
    for v in G.neighbors(v0):
        if v in B:
            sw1 = sum(omega1[norm_e(v, u)] for u in H.neighbors(v))
            degR_v = sum(1 for u in G.neighbors(v) if u in R)
            beta[v] = f[v] - sw1 - c_off[v] - 2 * degR_v
            assert beta[v] in (1, 3)

    omega2 = {norm_e(v0, u): 2 for u in G.neighbors(v0)}
    if beta[v1] == beta[vk]:
        R_prime = set()
    else:
        if beta[v1] == 1:
            p = list(reversed(p))
            v1, vk = p[0], p[-1]
        assert beta[v1] == 3 and beta[vk] == 1
        R_prime = {u0}
        omega2[norm_e(v0, u0)] = 3
        omega2[norm_e(v0, v1)] = 3

    alpha = {}
    for v in B:
        sw1 = sum(omega1[norm_e(v, u)] for u in H.neighbors(v))
        if v in G.neighbors(v0):
            alpha[v] = f[v] - sw1 - c_off[v] - omega2[norm_e(v0, v)]
        else:
            alpha[v] = f[v] - sw1 - c_off[v]

    edges_RB = [(u, v) for u, v in G.edges() if u != v0 and v != v0 and ((u in R) != (v in R))]
    omega3 = lemma_edgesbetween(B, R, edges_RB, alpha, R_prime, fixed_path=p)
    omega = {}
    omega.update(omega1)
    omega.update(omega2)
    omega.update(omega3)

    phi = lambda x: c_off[x] + sum(omega[norm_e(x, u)] for u in G.neighbors(x))
    if phi(v0) == phi(u0):
        if beta[v1] == 1 and beta[vk] == 1:
            omega[norm_e(v0, v1)] = 1
            omega[norm_e(v0, vk)] = 1
            d1, dk = +1, +1
        elif beta[v1] == 3 and beta[vk] == 3:
            omega[norm_e(v0, v1)] = 3
            omega[norm_e(v0, vk)] = 3
            d1, dk = -1, -1
        else:
            omega[norm_e(v0, v1)] = 2
            omega[norm_e(v0, vk)] = 1
            d1, dk = +1, +1
        omega[norm_e(v1, p[1])] += d1
        omega[norm_e(p[-2], vk)] += dk
        fix_path_rearranging(omega, p, B, d1, dk)
    return omega


def check_nfsd3(G, omega):
    # f(v) = 2 for all v, f(e) = omega[e] in {1,2,3}
    for u, v in G.edges():
        w = omega[norm_e(u, v)]
        assert w in (1, 2, 3), f"Invalid weight {w}"
    phi = {v: 2 + 2 * G.degree(v) + sum(omega[norm_e(v, u)] for u in G.neighbors(v)) for v in G.nodes()}
    for u, v in G.edges():
        assert phi[u] != phi[v], f"Conflict on {(u, v)}: phi={phi[u]}"


def main():
    t0 = time.time()
    # 1. Exhaustively test ALL 994 connected graphs on n=3..7 from graph_atlas_g()
    atlas = nx.graph_atlas_g()
    graphs = [nx.convert_node_labels_to_integers(G) for G in atlas if 3 <= G.number_of_nodes() <= 7 and nx.is_connected(G)]
    for G in graphs:
        c_off = {v: 2 + 2 * G.degree(v) for v in G.nodes()}
        omega = solve_even_offset_123(G, c_off)
        check_nfsd3(G, omega)
    print(f"All {len(graphs)} connected graphs on n=3..7 constructed and verified: PASS ({time.time()-t0:.2f}s)")

    # 2. Stress test 300 random connected graphs n=8..25 and named/dense/sparse graphs
    rng = random.Random(2026)
    cnt = 0
    for n in range(8, 22):
        for p in [0.15, 0.35, 0.6, 0.85]:
            for _ in range(5):
                G = nx.gnp_random_graph(n, p, seed=rng.randint(1, 10**9))
                if nx.is_connected(G):
                    c_off = {v: 2 + 2 * G.degree(v) for v in G.nodes()}
                    omega = solve_even_offset_123(G, c_off)
                    check_nfsd3(G, omega)
                    cnt += 1
    for G in [nx.petersen_graph(), nx.chvatal_graph(), nx.dodecahedral_graph(), nx.complete_graph(12), nx.mycielski_graph(4)]:
        c_off = {v: 2 + 2 * G.degree(v) for v in G.nodes()}
        omega = solve_even_offset_123(G, c_off)
        check_nfsd3(G, omega)
        cnt += 1
    print(f"All {cnt} larger/named graphs (n=8..21) constructed and verified: PASS (total {time.time()-t0:.2f}s)")


if __name__ == "__main__":
    main()
