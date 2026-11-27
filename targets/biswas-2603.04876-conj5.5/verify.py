#!/usr/bin/env python3
"""Exact-arithmetic verifier for Conjecture 5.5 of Biswas-Mandal-Saha (arXiv:2603.04876v1).

Verifies:
  1. Every step of the constructive proof in PROOF.md (Dirac simplicial vertex s,
     clique tree T rooted at the simplicial maximal clique R = N_G[s], greedy
     bottom-up clique cover B_1,...,B_r and maximum induced matching M,
     root-clique adjustment C_r = {u_r, x} when B_r = R and R cap X = empty,
     pigeonhole vertex x* in X giving im(G - N_G[x*]) <= r - ceil(r/(n-2r)),
     and Saha-Sengupta witness A = {x*} U A' with |A| <= r - ceil(r/(n-2r)) + 1) across:
     - ALL 352 connected chordal graphs on n = 3..7 (every simplicial root R = N_G[s]!),
     - Paths P_3..P_25 (every simplicial root),
     - Adversarial wing/core graphs and the 14-vertex MIS-in-X counterexample tree,
     - 1,500+ random connected chordal graphs on n = 8..20 (general PEO, trees, dense).
  2. Exact equality against brute-force im(G) and v(G) on all n = 3..7 graphs and
     sampled n = 8..10 graphs.
  3. Realizability of every lattice point (r, v) in A(n) by the connected chordal
     constructions of Theorem 3.5 (arXiv:2603.04876v1) for all n = 3..11.

Exact integer/set arithmetic only. Prints PASS or FAIL.
"""
import itertools
import math
import random
import signal
import sys
import time
from collections import deque
import networkx as nx

TIMEOUT_SECONDS = 120


def _timeout_handler(signum, frame):
    print("FAIL: timeout exceeded")
    sys.exit(1)


signal.signal(signal.SIGALRM, _timeout_handler)
signal.alarm(TIMEOUT_SECONDS)


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def exact_im(adj_bits, n):
    """Exact induced matching number via branch-and-bound on bitmasks."""
    edges = []
    for u in range(n):
        m = adj_bits[u] >> (u + 1)
        v = u + 1
        while m:
            lsb = m & -m
            idx = lsb.bit_length() - 1
            edges.append((u, v + idx))
            m ^= lsb
    if not edges:
        return 0
    # Conflict mask for each edge: two edges conflict iff they share a vertex or have an edge between them
    ne = len(edges)
    # Use vertex-based recursion (much faster for dense chordal graphs)
    best = [0]

    # Precompute closed neighborhood mask of each edge
    edge_nclosed = []
    for u, v in edges:
        edge_nclosed.append(adj_bits[u] | adj_bits[v] | (1 << u) | (1 << v))

    # Build vertex -> incident edges
    # Standard branch-and-bound on edges
    edge_compat = [0] * ne
    for i in range(ne):
        ui, vi = edges[i]
        nc_i = edge_nclosed[i]
        mask = 0
        for j in range(i + 1, ne):
            uj, vj = edges[j]
            if not (nc_i & ((1 << uj) | (1 << vj))):
                mask |= (1 << j)
        edge_compat[i] = mask

    def bt(cand_mask, cur):
        if cur > best[0]:
            best[0] = cur
        if cur + cand_mask.bit_count() <= best[0]:
            return
        # Upper bound by remaining vertices / 2? Simple bitcount is fast for n <= 12
        m = cand_mask
        while m:
            if cur + m.bit_count() <= best[0]:
                return
            lsb = m & -m
            i = lsb.bit_length() - 1
            m ^= lsb
            bt(m & edge_compat[i], cur + 1)

    bt((1 << ne) - 1, 0)
    return best[0]


def exact_v_number(adj_bits, n):
    """Exact v(G) = min |A| over independent A such that N_G(A) is a vertex cover."""
    all_edges = []
    for u in range(n):
        for v in range(u + 1, n):
            if (adj_bits[u] >> v) & 1:
                all_edges.append((u, v))
    if not all_edges:
        return 0

    def is_vc(mask):
        for u, v in all_edges:
            if not (((mask >> u) & 1) or ((mask >> v) & 1)):
                return False
        return True

    # Iterative deepening on size k = 1, 2, ...
    verts = list(range(n))
    for k in range(1, n + 1):
        found = [False]

        def bt(start, rem, forbidden, n_mask):
            if rem == 0:
                if is_vc(n_mask):
                    found[0] = True
                return
            for i in range(start, n - rem + 1):
                if (forbidden >> i) & 1:
                    continue
                bt(i + 1, rem - 1, forbidden | adj_bits[i] | (1 << i), n_mask | adj_bits[i])
                if found[0]:
                    return

        bt(0, k, 0, 0)
        if found[0]:
            return k
    raise AssertionError("No v-set found")


def is_chordal_and_simplicial_peo(adj_sets, verts):
    """Compute a simplicial PEO (v_0, v_1, ..., v_{n-1}) where v_i is simplicial in G[v_i..]."""
    rem = set(verts)
    peo = []
    while rem:
        found = None
        for v in rem:
            nbrs = adj_sets[v] & rem
            # Check nbrs is a clique
            ok = True
            nbr_list = list(nbrs)
            for i in range(len(nbr_list)):
                u = nbr_list[i]
                for j in range(i + 1, len(nbr_list)):
                    if nbr_list[j] not in adj_sets[u]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                found = v
                break
        if found is None:
            return None
        peo.append(found)
        rem.remove(found)
    return peo


def build_clique_tree(adj_sets, verts):
    """Construct clique tree inductively by simplicial elimination (Lemma 2 of PROOF.md)."""
    peo = is_chordal_and_simplicial_peo(adj_sets, verts)
    assert peo is not None, "Graph is not chordal"
    # Build backwards from peo[-1] down to peo[0]
    cliques = [frozenset([peo[-1]])]
    tree_adj = {0: set()}
    present = {peo[-1]}

    for s in reversed(peo[:-1]):
        nbrs = adj_sets[s] & present
        present.add(s)
        # Find a maximal clique B of G[present\{s}] containing nbrs
        target = None
        for idx, B in enumerate(cliques):
            if nbrs <= B:
                target = idx
                break
        assert target is not None, "Neighborhood clique not contained in any maximal clique"
        if nbrs == cliques[target]:
            cliques[target] = cliques[target] | {s}
        else:
            new_idx = len(cliques)
            cliques.append(frozenset(nbrs | {s}))
            tree_adj[new_idx] = {target}
            tree_adj[target].add(new_idx)

    # Verify clique tree axioms!
    k = len(cliques)
    # 1. Tree check: connected and k-1 edges
    edge_cnt = sum(len(ns) for ns in tree_adj.values()) // 2
    assert edge_cnt == k - 1
    seen = {0}
    q = deque([0])
    while q:
        u = q.popleft()
        for w in tree_adj[u]:
            if w not in seen:
                seen.add(w)
                q.append(w)
    assert len(seen) == k
    # 2. Every tree edge has nonempty intersection (for connected graph)
    for u in range(k):
        for w in tree_adj[u]:
            assert len(cliques[u] & cliques[w]) >= 1
    # 3. Every clique is a genuine clique and maximal, and T_v is connected for every v
    for B in cliques:
        Bl = list(B)
        for i in range(len(Bl)):
            for j in range(i + 1, len(Bl)):
                assert Bl[j] in adj_sets[Bl[i]]
    for v in verts:
        tv = {idx for idx, B in enumerate(cliques) if v in B}
        assert len(tv) >= 1
        start = next(iter(tv))
        vis = {start}
        dq = deque([start])
        while dq:
            u = dq.popleft()
            for w in tree_adj[u]:
                if w in tv and w not in vis:
                    vis.add(w)
                    dq.append(w)
        assert vis == tv, f"T_{v} is not connected"
    return cliques, tree_adj


def saha_sengupta_v_set(adj_sets, verts):
    """Construct independent A <= verts with N(A) a vertex cover and |A| <= im(G[verts])."""
    rem = set(verts)
    A = set()
    while True:
        # Remove isolated vertices in G[rem]
        non_iso = {v for v in rem if adj_sets[v] & rem}
        if not non_iso:
            break
        peo = is_chordal_and_simplicial_peo(adj_sets, non_iso)
        assert peo is not None
        s = peo[0]
        u = next(iter(adj_sets[s] & non_iso))
        A.add(u)
        rem = non_iso - (adj_sets[u] | {u})
    return A


def verify_proof_on_graph(G_nx, check_all_roots=False, check_exact_invariants=False):
    """Run and verify every lemma of PROOF.md on a connected chordal graph G_nx."""
    n = G_nx.number_of_nodes()
    assert n >= 3 and nx.is_connected(G_nx)
    mapping = {node: idx for idx, node in enumerate(G_nx.nodes())}
    adj_sets = [set() for _ in range(n)]
    adj_bits = [0] * n
    edges_all = []
    for u0, v0 in G_nx.edges():
        u, v = mapping[u0], mapping[v0]
        if u == v:
            continue
        adj_sets[u].add(v)
        adj_sets[v].add(u)
        adj_bits[u] |= (1 << v)
        adj_bits[v] |= (1 << u)
        edges_all.append((min(u, v), max(u, v)))

    verts = list(range(n))
    cliques, tree_adj = build_clique_tree(adj_sets, verts)
    num_cliques = len(cliques)

    # Precompute T_v for each vertex v, and find all simplicial vertices and their unique maximal cliques R = N_G[s]
    Tv = [{idx for idx, B in enumerate(cliques) if v in B} for v in range(n)]
    simplicial_roots = []
    seen_roots = set()
    for s in range(n):
        if len(Tv[s]) == 1:
            r_idx = next(iter(Tv[s]))
            # Verify directly that s is simplicial and cliques[r_idx] == N_G[s]
            assert cliques[r_idx] == (adj_sets[s] | {s}), "Unique clique of s must equal N_G[s]"
            if r_idx not in seen_roots:
                seen_roots.add(r_idx)
                simplicial_roots.append((r_idx, s))
    assert len(simplicial_roots) >= 1, "Chordal graph must have at least one simplicial vertex"

    roots_to_test = simplicial_roots if check_all_roots else [simplicial_roots[0]]
    exact_r = exact_im(adj_bits, n) if check_exact_invariants else None
    exact_v = exact_v_number(adj_bits, n) if check_exact_invariants else None

    subcase_b2_hits = 0

    for root, root_s in roots_to_test:
        # BFS from root to get depth and parent
        depth = [-1] * num_cliques
        parent = [-1] * num_cliques
        depth[root] = 0
        q = deque([root])
        while q:
            u = q.popleft()
            for w in tree_adj[u]:
                if depth[w] == -1:
                    depth[w] = depth[u] + 1
                    parent[w] = u
                    q.append(w)

        # Greedy bottom-up clique cover & induced matching (Lemma 3 of PROOF.md)
        alive = set(range(n))
        B_indices = []
        M_edges = []
        while True:
            alive_edges = [
                (u, v) for (u, v) in edges_all if u in alive and v in alive
            ]
            if not alive_edges:
                break
            best_edge = None
            best_top = -1
            best_depth = -1
            for u, v in alive_edges:
                te = Tv[u] | Tv[v]
                top_node = min(te, key=lambda idx: depth[idx])
                if depth[top_node] > best_depth:
                    best_depth = depth[top_node]
                    best_top = top_node
                    best_edge = (u, v)
            B_indices.append(best_top)
            M_edges.append(best_edge)
            alive -= set(cliques[best_top])

        r = len(M_edges)
        assert 1 <= r < n / 2
        if exact_r is not None:
            assert r == exact_r, f"Greedy r={r} != exact im={exact_r}"

        # Verify M_edges is an induced matching
        VM = set()
        for u, v in M_edges:
            VM.add(u)
            VM.add(v)
        assert len(VM) == 2 * r
        for i in range(r):
            ui, vi = M_edges[i]
            for j in range(i + 1, r):
                uj, vj = M_edges[j]
                assert uj not in adj_sets[ui] and vj not in adj_sets[ui]
                assert uj not in adj_sets[vi] and vj not in adj_sets[vi]

        # Verify union of B_indices is a vertex cover of G
        cover_B = set()
        for idx in B_indices:
            cover_B |= set(cliques[idx])
        for u, v in edges_all:
            assert u in cover_B or v in cover_B

        X = set(range(n)) - VM
        m = n - 2 * r
        assert len(X) == m and m >= 1
        bound = r - ceil_div(r, m) + 1

        # Verify Lemma 4 uniformly for ALL r >= 1:
        # Every non-root B_i intersects X via B_i cap parent(B_i);
        # if B_r == root and root cap X == empty, then root == e_r == {u_r, root_s}
        # with root_s a degree-1 leaf, and C_r = {u_r, x} for any x in N_G(u_r) \ {root_s} <= X.
        C_cliques = [set(cliques[idx]) for idx in B_indices]
        for i in range(r - 1):
            assert B_indices[i] != root, "Root chosen before last step!"
            p_inter = cliques[B_indices[i]] & cliques[parent[B_indices[i]]]
            assert len(p_inter) >= 1 and (p_inter <= X), "B_i cap parent(B_i) must lie inside X!"

        if B_indices[-1] != root:
            p_inter = cliques[B_indices[-1]] & cliques[parent[B_indices[-1]]]
            assert len(p_inter) >= 1 and (p_inter <= X), "Non-root B_r cap parent(B_r) must lie inside X!"
        elif not (C_cliques[-1] & X):
            subcase_b2_hits += 1
            ur, vr = M_edges[-1]
            assert C_cliques[-1] == {ur, vr}, "Root disjoint from X must equal e_r"
            assert root_s in {ur, vr}, "Simplicial vertex s must belong to root R = N_G[s]"
            other = vr if root_s == ur else ur
            # Verify root_s is a degree-1 leaf whose sole neighbor is `other`
            assert adj_sets[root_s] == {other}, "Simplicial root vertex s must have degree 1"
            cand_x = adj_sets[other] - {root_s}
            assert len(cand_x) >= 1, "Connectedness (n>=3) forces other to have a neighbor outside {ur, vr}"
            assert cand_x <= X, "Every neighbor of other outside e_r must lie in X"
            x = next(iter(cand_x))
            C_cliques[-1] = {other, x}
        else:
            assert len(C_cliques[-1] & X) >= 1

        # Verify C_cliques are all cliques, intersect X, and cover all edges of G
        cover_C = set()
        for C in C_cliques:
            assert len(C & X) >= 1
            Cl = list(C)
            for a in range(len(Cl)):
                for b in range(a + 1, len(Cl)):
                    assert Cl[b] in adj_sets[Cl[a]]
            cover_C |= C
        for u, v in edges_all:
            assert u in cover_C or v in cover_C

        # Pigeonhole vertex x* in X belonging to max number of C_i
        counts = {x: sum(1 for C in C_cliques if x in C) for x in X}
        x_star = max(X, key=lambda x: counts[x])
        t = counts[x_star]
        assert t >= ceil_div(r, m)

        # Construct G' = G - N_G[x*] and verify witness A = {x*} U A'
        rem_verts = [v for v in range(n) if v != x_star and v not in adj_sets[x_star]]
        A_prime = saha_sengupta_v_set(adj_sets, rem_verts)
        assert len(A_prime) <= r - t
        A = {x_star} | A_prime

        # Independent check of im(G - N[x*]) <= r - ceil(r/m) for small n
        if check_exact_invariants:
            if rem_verts:
                sub_map = {v: i for i, v in enumerate(rem_verts)}
                sub_bits = [0] * len(rem_verts)
                for v in rem_verts:
                    iv = sub_map[v]
                    for w in adj_sets[v]:
                        if w in sub_map:
                            sub_bits[iv] |= (1 << sub_map[w])
                im_sub = exact_im(sub_bits, len(rem_verts))
            else:
                im_sub = 0
            assert im_sub <= r - t <= r - ceil_div(r, m)

        # Verify A is independent and N_G(A) is a vertex cover of G
        for a in A:
            assert not (adj_sets[a] & A), "Witness A is not independent!"
        NA = set()
        for a in A:
            NA |= adj_sets[a]
        for u, v in edges_all:
            assert u in NA or v in NA, "N_G(A) is not a vertex cover!"
        assert len(A) <= bound, f"|A|={len(A)} > bound={bound}"

        if exact_v is not None:
            assert 1 <= exact_v <= bound

    return subcase_b2_hits


def random_connected_chordal(n, rng, density_mode=0):
    """Generate a random connected chordal graph via PEO construction."""
    G = nx.Graph()
    G.add_node(0)
    cliques = [{0}]
    for v in range(1, n):
        base = rng.choice(cliques)
        if density_mode == 0:
            sz = rng.randint(1, len(base))
        elif density_mode == 1:
            sz = 1  # tree
        else:
            sz = len(base) if rng.random() < 0.7 else rng.randint(1, len(base))
        nbrs = set(rng.sample(list(base), sz))
        G.add_node(v)
        for u in nbrs:
            G.add_edge(u, v)
        if nbrs == base:
            base.add(v)
        else:
            cliques.append(nbrs | {v})
    return G


def build_thm35_graph(n, r, v):
    """Construct connected chordal graph of Theorem 3.5 (arXiv:2603.04876v1) for (r,v) in A(n)."""
    G = nx.Graph()
    if n - 2 * r >= r:
        # Case I: tree on n vertices
        # Vertices: x_1..x_v, y_1..y_r, z_1..z_r, w_1..w_{n-2r-v}
        G.add_nodes_from(range(n))
        x = list(range(0, v))
        y = list(range(v, v + r))
        z = list(range(v + r, v + 2 * r))
        w = list(range(v + 2 * r, n))
        for i in range(1, v):
            G.add_edge(x[0], x[i])
        for i in range(r - v + 1):
            G.add_edge(x[0], y[i])
        for i in range(1, v):
            G.add_edge(x[i], y[r - v + i])
        for i in range(r):
            G.add_edge(y[i], z[i])
        for wi in w:
            G.add_edge(x[0], wi)
    else:
        # Case II: K_q + pendant leaves on x_1 + pendant P_2's
        m = n - 2 * r
        t1 = r - v + 1
        assert t1 >= ceil_div(r, m) and t1 <= r
        t = [t1] + [0] * (m - 1)
        rem = r - t1
        idx = 1
        while rem > 0:
            add = min(t1, rem)
            t[idx] = add
            rem -= add
            idx += 1
        G.add_nodes_from(range(n))
        cur = m
        q = sum(1 for ti in t if ti > 0)
        for i in range(q):
            for j in range(i + 1, q):
                G.add_edge(i, j)
        for i in range(q, m):
            G.add_edge(0, i)
        for i in range(m):
            for _ in range(t[i]):
                yi, zi = cur, cur + 1
                cur += 2
                G.add_edge(i, yi)
                G.add_edge(yi, zi)
        assert cur == n
    return G


def main():
    t0 = time.time()

    # 1. Exhaustive check on ALL connected chordal graphs on n = 3..7 (every simplicial root R = N_G[s] tested!)
    atlas_chordal = [
        G for G in nx.graph_atlas_g()
        if 3 <= G.number_of_nodes() <= 7 and nx.is_connected(G) and nx.is_chordal(G)
    ]
    assert len(atlas_chordal) == 352, f"Expected 352 connected chordal graphs on n=3..7, got {len(atlas_chordal)}"
    b2_atlas = 0
    for G in atlas_chordal:
        b2_atlas += verify_proof_on_graph(G, check_all_roots=True, check_exact_invariants=True)
    assert b2_atlas > 0, "Expected Subcase B2 to be exercised on n=3..7!"

    # 2. Explicit paths P_3..P_25 (every simplicial root; stress-tests Subcase B2 directly!)
    b2_paths = 0
    for n in range(3, 26):
        P = nx.path_graph(n)
        b2_paths += verify_proof_on_graph(P, check_all_roots=True, check_exact_invariants=(n <= 12))
    assert b2_paths > 0, "Expected Subcase B2 to be exercised on paths!"

    # 3. Specific adversarial tree (n=14, r=5, where MIS-in-X fails across all max IMs)
    T14 = nx.Graph()
    T14.add_edges_from([
        (0, 1), (0, 2), (0, 4), (0, 10), (1, 6), (1, 8),
        (2, 3), (4, 5), (4, 12), (4, 13), (6, 7), (8, 9), (10, 11),
    ])
    verify_proof_on_graph(T14, check_all_roots=True, check_exact_invariants=True)

    # 4. Random PEO chordal graphs + trees + dense chordal graphs on n = 8..20
    rng = random.Random(20260305)
    random_tested = 0
    b2_random = 0
    for n in range(8, 21):
        count = 150 if n <= 12 else 100
        for idx in range(count):
            G = random_connected_chordal(n, rng, density_mode=idx % 3)
            b2_random += verify_proof_on_graph(
                G, check_all_roots=(n <= 10), check_exact_invariants=(n <= 10)
            )
            random_tested += 1

    # 5. Verify Theorem 3.5 realizability AND run our constructive proof on every (r, v) in A(n) for n = 3..11,
    #    plus high-r tight extremal graphs up to n = 30.
    realized_pts = 0
    b2_extremal = 0
    for n in range(3, 12):
        for r in range(1, (n + 1) // 2):
            m = n - 2 * r
            vmax = r - ceil_div(r, m) + 1
            for v in range(1, vmax + 1):
                G = build_thm35_graph(n, r, v)
                assert G.number_of_nodes() == n and nx.is_connected(G) and nx.is_chordal(G)
                adj_bits = [0] * n
                for u, w in G.edges():
                    adj_bits[u] |= (1 << w)
                    adj_bits[w] |= (1 << u)
                assert exact_im(adj_bits, n) == r
                assert exact_v_number(adj_bits, n) == v
                b2_extremal += verify_proof_on_graph(G, check_all_roots=True, check_exact_invariants=True)
                realized_pts += 1

    # Also test tight Case-II extremal graphs for larger n = 12..30
    large_extremal = 0
    for n in range(12, 31):
        for r in range(n // 3 + 1, (n + 1) // 2):
            m = n - 2 * r
            vmax = r - ceil_div(r, m) + 1
            G = build_thm35_graph(n, r, vmax)
            assert G.number_of_nodes() == n and nx.is_connected(G) and nx.is_chordal(G)
            b2_extremal += verify_proof_on_graph(G, check_all_roots=False, check_exact_invariants=False)
            large_extremal += 1

    elapsed = time.time() - t0
    print(
        f"PASS: verified constructive proof on all {len(atlas_chordal)} connected chordal graphs (n=3..7, all simplicial roots; "
        f"{b2_atlas} Subcase B2 hits), paths P_3..P_25 ({b2_paths} B2 hits), adversarial 14-vertex tree, "
        f"{random_tested} random chordal/tree/dense graphs (n=8..20; {b2_random} B2 hits), Theorem 3.5 realizability "
        f"for all {realized_pts} lattice points (n=3..11), and {large_extremal} tight extremal graphs (n=12..30; "
        f"{b2_extremal} extremal B2 hits) in {elapsed:.2f}s."
    )


if __name__ == "__main__":
    main()
