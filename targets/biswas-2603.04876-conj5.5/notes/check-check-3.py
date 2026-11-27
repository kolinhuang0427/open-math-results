"""Independent exact-arithmetic verifier for targets/biswas-2603.04876-conj5.5/."""

from collections import deque
import itertools
import random
import signal

signal.alarm(50)


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def is_connected(n: int, adj: list[set[int]]) -> bool:
    if n == 0:
        return True
    seen = {0}
    q = deque([0])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)
    return len(seen) == n


def is_clique(adj: list[set[int]], verts: set[int] | list[int]) -> bool:
    vs = list(verts)
    for i in range(len(vs)):
        u = vs[i]
        for j in range(i + 1, len(vs)):
            if vs[j] not in adj[u]:
                return False
    return True


def simplicial_vertices(n: int, adj: list[set[int]]) -> list[int]:
    return [v for v in range(n) if is_clique(adj, adj[v])]


def is_chordal(n: int, adj: list[set[int]]) -> bool:
    """Exact PEO check via Maximum Cardinality Search (Tarjan-Yannakakis)."""
    # Compute MCS order, then verify every vertex's earlier neighbors form a clique.
    placed = [False] * n
    weight = [0] * n
    order = []
    for _ in range(n):
        best = -1
        for v in range(n):
            if not placed[v] and (best == -1 or weight[v] > weight[best]):
                best = v
        placed[best] = True
        order.append(best)
        for u in adj[best]:
            if not placed[u]:
                weight[u] += 1
    pos = {v: i for i, v in enumerate(order)}
    for i, v in enumerate(order):
        earlier = [u for u in adj[v] if pos[u] < i]
        if not is_clique(adj, earlier):
            return False
    return True


def edges_list(n: int, adj: list[set[int]]) -> list[tuple[int, int]]:
    return [(u, v) for u in range(n) for v in adj[u] if u < v]


def induced_matching_number(n: int, adj: list[set[int]], allowed: set[int] | None = None) -> int:
    """Exact im(G[allowed]) via branch-and-bound on edge sets."""
    if allowed is None:
        allowed = set(range(n))
    es = [(u, v) for u in allowed for v in adj[u] if u < v and v in allowed]
    if not es:
        return 0
    # Two edges are compatible in an induced matching iff they are at distance >= 2
    # (no shared endpoint and no cross-edge between endpoints).
    m = len(es)
    compat = [0] * m
    for i, (u1, v1) in enumerate(es):
        mask = 0
        for j in range(i + 1, m):
            u2, v2 = es[j]
            if (
                u1 != u2 and u1 != v2 and v1 != u2 and v1 != v2
                and u2 not in adj[u1] and v2 not in adj[u1]
                and u2 not in adj[v1] and v2 not in adj[v1]
            ):
                mask |= 1 << j
        compat[i] = mask

    best = 0

    def dfs(avail_mask: int, count: int) -> None:
        nonlocal best
        if count + avail_mask.bit_count() <= best:
            return
        if avail_mask == 0:
            if count > best:
                best = count
            return
        lsb = avail_mask & -avail_mask
        i = lsb.bit_length() - 1
        rest = avail_mask ^ lsb
        # Pick edge i
        dfs(rest & compat[i], count + 1)
        # Skip edge i
        dfs(rest, count)

    dfs((1 << m) - 1, 0)
    return best


def v_number(n: int, adj: list[set[int]]) -> int:
    """Exact v(G) directly from Definition 2.4: min |A| for A independent with N_G(A) a vertex cover."""
    es = edges_list(n, adj)
    if not es:
        return 0
    adj_mask = [0] * n
    for u in range(n):
        m = 0
        for v in adj[u]:
            m |= 1 << v
        adj_mask[u] = m

    # Search independent sets by increasing cardinality k = 1, 2, ...
    for k in range(1, n + 1):
        for comb_a in itertools.combinations(range(n), k):
            a_mask = 0
            na_mask = 0
            indep = True
            for u in comb_a:
                if adj_mask[u] & a_mask:
                    indep = False
                    break
                a_mask |= 1 << u
                na_mask |= adj_mask[u]
            if not indep:
                continue
            # Check N_G(A) is a vertex cover of G
            if all(((na_mask >> u) & 1) or ((na_mask >> v) & 1) for u, v in es):
                return k
    raise AssertionError("No vertex-cover neighborhood found")


def maximal_cliques_bron_kerbosch(n: int, adj: list[set[int]]) -> list[frozenset[int]]:
    cliques = []

    def bk(R: set[int], P: set[int], X: set[int]) -> None:
        if not P and not X:
            cliques.append(frozenset(R))
            return
        u = next(iter(P | X))
        for v in list(P - adj[u]):
            bk(R | {v}, P & adj[v], X & adj[v])
            P.remove(v)
            X.add(v)

    bk(set(), set(range(n)), set())
    return cliques


def build_clique_tree(n: int, adj: list[set[int]]) -> tuple[list[frozenset[int]], dict[int, set[int]]]:
    """Construct clique tree following PROOF.md Lemma 3 and assert axioms (1) and (2)."""
    verts = sorted(range(n))
    if n == 1:
        cliques = [frozenset({0})]
        return cliques, {0: set()}

    def helper(active: set[int]) -> tuple[list[frozenset[int]], dict[int, set[int]]]:
        if len(active) == 1:
            v = next(iter(active))
            return [frozenset({v})], {0: set()}
        # Find simplicial vertex s in G[active]
        s = None
        for v in sorted(active):
            nbrs = adj[v] & active
            if is_clique(adj, nbrs):
                s = v
                break
        assert s is not None
        sub_active = active - {s}
        cliques_p, tree_p = helper(sub_active)
        nbrs = frozenset(adj[s] & sub_active)
        assert len(nbrs) >= 1
        # Find maximal clique B0 in cliques_p containing nbrs
        b0_idx = next(i for i, b in enumerate(cliques_p) if nbrs <= b)
        b0 = cliques_p[b0_idx]
        if nbrs == b0:
            new_cliques = cliques_p[:]
            new_cliques[b0_idx] = b0 | {s}
            new_tree = {i: set(ns) for i, ns in tree_p.items()}
        else:
            new_cliques = cliques_p + [nbrs | {s}]
            new_idx = len(new_cliques) - 1
            new_tree = {i: set(ns) for i, ns in tree_p.items()}
            new_tree[b0_idx].add(new_idx)
            new_tree[new_idx] = {b0_idx}
        return new_cliques, new_tree

    cliques, tree = helper(set(verts))
    assert set(cliques) == set(maximal_cliques_bron_kerbosch(n, adj))
    # Verify clique tree axioms (1) & (2)
    for u, nbrs in tree.items():
        for w in nbrs:
            assert cliques[u] & cliques[w], "Tree edge intersection empty"
    for v in range(n):
        tv = {i for i, c in enumerate(cliques) if v in c}
        assert tv
        start = next(iter(tv))
        seen = {start}
        q = deque([start])
        while q:
            cur = q.popleft()
            for nb in tree[cur]:
                if nb in tv and nb not in seen:
                    seen.add(nb)
                    q.append(nb)
        assert seen == tv, f"T_{v} not connected"
    return cliques, tree


def check_lemmas_and_thm1(n: int, adj: list[set[int]], test_all_roots: bool = True) -> tuple[int, int]:
    assert is_connected(n, adj) and is_chordal(n, adj)
    simps = simplicial_vertices(n, adj)
    assert simps, "Lemma 1 failed: no simplicial vertex"
    if len(edges_list(n, adj)) < n * (n - 1) // 2:
        assert any(v not in adj[u] and u != v for u in simps for v in simps), "Lemma 1 failed: no nonadj simplicial pair"

    r = induced_matching_number(n, adj)
    v_num = v_number(n, adj)
    assert 1 <= r < n / 2
    assert v_num <= r, "Lemma 2 failed: v(G) > im(G)"
    assert 1 <= v_num <= r - ceil_div(r, n - 2 * r) + 1, "Theorem 1 failed: v(G) > bound"

    cliques, tree = build_clique_tree(n, adj)
    es = edges_list(n, adj)

    roots_to_check = simps if test_all_roots else [simps[0]]
    for s in roots_to_check:
        R_set = frozenset({s}) | adj[s]
        R_idx = cliques.index(R_set)
        # BFS depths and parents from R_idx
        depth = {R_idx: 0}
        parent = {R_idx: None}
        q = deque([R_idx])
        while q:
            cur = q.popleft()
            for nb in tree[cur]:
                if nb not in depth:
                    depth[nb] = depth[cur] + 1
                    parent[nb] = cur
                    q.append(nb)

        # Lemma 4 greedy loop
        rem_verts = set(range(n))
        M_edges = []
        B_indices = []
        while True:
            rem_edges = [(u, v) for (u, v) in es if u in rem_verts and v in rem_verts]
            if not rem_edges:
                break
            best_edge = None
            best_top = None
            best_d = -1
            for u, v in rem_edges:
                te = [i for i, c in enumerate(cliques) if u in c or v in c]
                top_idx = min(te, key=lambda idx: depth[idx])
                if depth[top_idx] > best_d:
                    best_d = depth[top_idx]
                    best_top = top_idx
                    best_edge = (u, v)
            M_edges.append(best_edge)
            B_indices.append(best_top)
            rem_verts -= cliques[best_top]

        assert len(M_edges) == r
        assert all(idx != R_idx for idx in B_indices[:-1])
        # Verify M_edges is an induced matching
        v_M = {x for e in M_edges for x in e}
        assert len(v_M) == 2 * r
        for i in range(r):
            for j in range(i + 1, r):
                u1, v1 = M_edges[i]
                u2, v2 = M_edges[j]
                assert not ({u1, v1} & {u2, v2})
                assert u2 not in adj[u1] and v2 not in adj[u1]
                assert u2 not in adj[v1] and v2 not in adj[v1]

        # Lemma 5 clique cover C_1..C_r hitting X
        X = set(range(n)) - v_M
        assert len(X) == n - 2 * r
        C_cliques = []
        for idx in B_indices:
            if idx != R_idx:
                C_cliques.append(cliques[idx])
            else:
                if cliques[R_idx] & X:
                    C_cliques.append(cliques[R_idx])
                else:
                    # Subcase B2
                    e_r = M_edges[-1]
                    assert cliques[R_idx] == frozenset(e_r)
                    u_r = e_r[0] if e_r[1] == s else e_r[1]
                    x_nbr = next(w for w in adj[u_r] if w != s)
                    assert x_nbr in X
                    C_cliques.append(frozenset({u_r, x_nbr}))

        assert len(C_cliques) == r
        cov = set().union(*C_cliques)
        assert all(u in cov or v in cov for u, v in es)
        assert all(C & X for C in C_cliques)

        # Theorem 1 pigeonhole vertex x*
        hits = {x: sum(1 for C in C_cliques if x in C) for x in X}
        x_star = max(hits, key=lambda x: hits[x])
        assert hits[x_star] >= ceil_div(r, n - 2 * r)
        allowed_after = set(range(n)) - ({x_star} | adj[x_star])
        im_after = induced_matching_number(n, adj, allowed_after)
        assert im_after <= r - ceil_div(r, n - 2 * r)

    return r, v_num


def canon_graph(n: int, adj: list[set[int]]) -> tuple[tuple[int, int], ...]:
    """Exact canonical edge-tuple using 2-step vertex-invariant tie refinement."""
    degs = [len(adj[v]) for v in range(n)]
    sigs = [
        (
            degs[v],
            tuple(sorted(degs[u] for u in adj[v])),
            tuple(sorted(len(adj[u] & adj[v]) for u in adj[v])),
        )
        for v in range(n)
    ]
    buckets: dict[tuple, list[int]] = {}
    for v in range(n):
        buckets.setdefault(sigs[v], []).append(v)
    sorted_keys = sorted(buckets)
    groups = [buckets[k] for k in sorted_keys]
    edges = edges_list(n, adj)
    best: tuple[tuple[int, int], ...] | None = None
    for prod in itertools.product(*(itertools.permutations(g) for g in groups)):
        mapping = {}
        pos = 0
        for g in prod:
            for v in g:
                mapping[v] = pos
                pos += 1
        cand = tuple(sorted((min(mapping[u], mapping[w]), max(mapping[u], mapping[w])) for u, w in edges))
        if best is None or cand < best:
            best = cand
    assert best is not None
    return best


def aut_size(n: int, adj: list[set[int]]) -> int:
    degs = [len(adj[v]) for v in range(n)]
    sigs = [(degs[v], tuple(sorted(degs[u] for u in adj[v]))) for v in range(n)]
    buckets: dict[tuple, list[int]] = {}
    for v in range(n):
        buckets.setdefault(sigs[v], []).append(v)
    groups = list(buckets.values())
    cnt = 0
    for prod in itertools.product(*(itertools.permutations(g) for g in groups)):
        perm = [0] * n
        for orig_g, p_g in zip(groups, prod):
            for ov, nv in zip(orig_g, p_g):
                perm[ov] = nv
        if all(all(perm[w] in adj[perm[u]] for w in adj[u]) for u in range(n)):
            cnt += 1
    return cnt


def enumerate_connected_chordal(max_n: int) -> dict[int, list[list[set[int]]]]:
    """Enumerate all non-isomorphic connected chordal graphs on n=3..max_n via clique attachment + exact n<=6 cross-check."""
    p3 = [{1}, {0, 2}, {1}]
    k3 = [{1, 2}, {0, 2}, {0, 1}]
    res: dict[int, list[list[set[int]]]] = {3: [p3, k3]}
    for n in range(4, max_n + 1):
        seen: set[tuple[tuple[int, int], ...]] = set()
        graphs: list[list[set[int]]] = []
        for adj_prev in res[n - 1]:
            for k in range(1, n):
                for sub in itertools.combinations(range(n - 1), k):
                    if is_clique(adj_prev, sub):
                        adj_new = [set(s) for s in adj_prev] + [set(sub)]
                        for u in sub:
                            adj_new[u].add(n - 1)
                        key = canon_graph(n, adj_new)
                        if key not in seen:
                            seen.add(key)
                            graphs.append(adj_new)
        res[n] = graphs

    # Cross-check completeness on n=3..6 by brute-forcing all 2^C(n,2) graphs and comparing labeled counts
    fact = 1
    for n in range(3, min(max_n, 6) + 1):
        if n == 3:
            fact = 6
        else:
            fact *= n
        pairs = list(itertools.combinations(range(n), 2))
        labeled_brute = 0
        for mask in range(1 << len(pairs)):
            adj = [set() for _ in range(n)]
            for idx, (u, v) in enumerate(pairs):
                if (mask >> idx) & 1:
                    adj[u].add(v)
                    adj[v].add(u)
            if is_connected(n, adj) and is_chordal(n, adj):
                labeled_brute += 1
        labeled_orb = sum(fact // aut_size(n, g) for g in res[n])
        assert labeled_orb == labeled_brute, f"n={n}: orb {labeled_orb} != brute {labeled_brute}"
    return res


def construct_reverse_witness(n: int, r: int, v: int) -> list[set[int]]:
    """Construct exact PROOF.md Part 2 Case I / Case II connected chordal graph."""
    m = n - 2 * r
    assert 1 <= r < n / 2 and 1 <= v <= r - ceil_div(r, m) + 1
    adj = [set() for _ in range(n)]

    def add_e(u: int, w: int) -> None:
        adj[u].add(w)
        adj[w].add(u)

    if m >= r:
        # Case I: x_1..x_v (0..v-1), y_1..y_r (v..v+r-1), z_1..z_r (v+r..v+2r-1), w_1..w_{m-v}
        x = list(range(0, v))
        y = list(range(v, v + r))
        z = list(range(v + r, v + 2 * r))
        w = list(range(v + 2 * r, n))
        assert len(w) == m - v
        for i in range(1, v):
            add_e(x[0], x[i])
        for j in range(r - v + 1):
            add_e(x[0], y[j])
        for i in range(1, v):
            add_e(x[i], y[r - v + i])
        for j in range(r):
            add_e(y[j], z[j])
        for wk in w:
            add_e(x[0], wk)
    else:
        # Case II: m < r
        t1 = r - v + 1
        ts = [t1]
        rem = r - t1
        for _ in range(m - 1):
            take = min(t1, rem)
            ts.append(take)
            rem -= take
        assert rem == 0
        pos_ts = [t for t in ts if t > 0]
        q = len(pos_ts)
        x = list(range(m))
        for i in range(q):
            for j in range(i + 1, q):
                add_e(x[i], x[j])
        for i in range(q, m):
            add_e(x[0], x[i])
        cur = m
        for i, ti in enumerate(pos_ts):
            for _ in range(ti):
                y_ij, z_ij = cur, cur + 1
                cur += 2
                add_e(x[i], y_ij)
                add_e(y_ij, z_ij)
        assert cur == n
    return adj


def main() -> None:
    # 1. Exhaustive n=3..7 connected chordal graphs: verify Lemmas 1-5, Theorem 1, and RV_chordal(n) == A(n)
    all_chordal = enumerate_connected_chordal(7)
    counts = {n: len(gs) for n, gs in all_chordal.items()}
    for n, gs in all_chordal.items():
        observed = set()
        expected = {
            (r, v)
            for r in range(1, (n + 1) // 2)
            for v in range(1, r - ceil_div(r, n - 2 * r) + 2)
        }
        for adj in gs:
            r, v_num = check_lemmas_and_thm1(n, adj, test_all_roots=True)
            observed.add((r, v_num))
        assert observed == expected, f"n={n}: observed {observed} != expected {expected}"
    print(f"Exhaustive n=3..7 PASS: checked {sum(counts.values())} non-isomorphic connected chordal graphs {counts}; RV_chordal(n)==A(n) exact.")

    # 2. Reverse inclusion Part 2 for n=3..11 (42 lattice points)
    total_pts = 0
    for n in range(3, 12):
        for r in range(1, (n + 1) // 2):
            for v in range(1, r - ceil_div(r, n - 2 * r) + 2):
                adj = construct_reverse_witness(n, r, v)
                assert is_connected(n, adj) and is_chordal(n, adj)
                assert induced_matching_number(n, adj) == r
                assert v_number(n, adj) == v
                total_pts += 1
    print(f"Part 2 PASS: constructed and verified exact (im, v) for all {total_pts} lattice points in A(3..11).")

    # 3. Stress test larger random chordal graphs (n=8..14)
    rng = random.Random(202603)
    tested_large = 0
    for n in range(8, 15):
        for _ in range(12):
            adj = [set() for _ in range(n)]
            # Build connected chordal graph by simplicial attachment
            for v_new in range(1, n):
                # Pick random existing vertex and subset of its clique neighbors
                base = rng.randrange(v_new)
                cands = [u for u in adj[base] if u < v_new]
                # Make sure chosen attachment set is a clique
                clique_set = [base]
                rng.shuffle(cands)
                for u in cands:
                    if all(u in adj[w] for w in clique_set) and rng.random() < 0.5:
                        clique_set.append(u)
                for w in clique_set:
                    adj[v_new].add(w)
                    adj[w].add(v_new)
            check_lemmas_and_thm1(n, adj, test_all_roots=False)
            tested_large += 1
    print(f"Large Stress PASS: {tested_large} connected chordal graphs on n=8..14 verified against Lemmas 1-5 & Thm 1.")
    print("PASS")


if __name__ == "__main__":
    main()
