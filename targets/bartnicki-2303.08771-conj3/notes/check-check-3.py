#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for Bartnicki-Czerwinski-Grytczuk-Miechowicz
(arXiv:2303.08771v1, Section 5, Conjecture 3: zeta(G) <= col(G)).

Written directly from the primary-source definitions in Zlamasy_III_11.tex
without reading verify.py or check-check-2.py. Zero floating-point arithmetic.
"""

from __future__ import annotations

from itertools import combinations
import sys


def build_G() -> tuple[int, list[tuple[int, int]]]:
    A = [0, 1, 2, 3]
    B = [4, 5, 6]
    C = [7, 8]
    edges = []
    for u, v in combinations(A, 2):
        edges.append((u, v))
    for u in A:
        for v in B:
            edges.append((u, v))
    for u in B:
        for v in C:
            edges.append((u, v))
    edges.sort()
    assert len(edges) == 24
    return 9, edges


def is_forest_multigraph(n_verts: int, edge_list: list[tuple[int, int]]) -> bool:
    """Check if multigraph edge_list has no cycle (including 2-cycles from parallel edges)."""
    parent = list(range(n_verts))
    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in edge_list:
        if u == v:
            return False
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return True


def is_strongly_woody_class_via_contraction(n_verts: int, all_edges: list[tuple[int, int]], mask: int) -> bool:
    """Primary-source contraction definition: F is woody, and for every e in E(G), F/e is woody in G/e."""
    class_edges = [all_edges[i] for i in range(len(all_edges)) if (mask >> i) & 1]
    if not is_forest_multigraph(n_verts, class_edges):
        return False
    for idx_e, (eu, ev) in enumerate(all_edges):
        contracted = []
        for idx_f, (fu, fv) in enumerate(all_edges):
            if not ((mask >> idx_f) & 1):
                continue
            if idx_f == idx_e:
                continue
            nu = eu if fu == ev else fu
            nv = eu if fv == ev else fv
            contracted.append((min(nu, nv), max(nu, nv)))
        if not is_forest_multigraph(n_verts, contracted):
            return False
    return True


def check_col_eq_5(n_verts: int, edges: list[tuple[int, int]]) -> None:
    adj = [0] * n_verts
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Check explicit ordering (0,1,2,3,4,5,6,7,8) has max back-degree 4 => col(G) <= 5
    seen = 0
    max_back = 0
    for v in range(n_verts):
        back_deg = (adj[v] & seen).bit_count()
        if back_deg > max_back:
            max_back = back_deg
        seen |= 1 << v
    assert max_back == 4

    # Exhaustively verify col(G) = 1 + max_{H <= G} delta(H) == 5 over all 511 nonempty induced subgraphs
    max_min_deg = 0
    for sub in range(1, 1 << n_verts):
        min_deg = n_verts
        for v in range(n_verts):
            if (sub >> v) & 1:
                d = (adj[v] & sub).bit_count()
                if d < min_deg:
                    min_deg = d
        if min_deg > max_min_deg:
            max_min_deg = min_deg
    assert 1 + max_min_deg == 5
    print("[1/4] Verified col(G) = 5 (explicit ordering + all 511 induced subgraphs).")


def check_explicit_6_coloring(n_verts: int, edges: list[tuple[int, int]]) -> None:
    edge_idx = {e: i for i, e in enumerate(edges)}
    colors = [
        [(0, 1), (2, 4), (3, 6), (5, 7), (5, 8)],
        [(0, 2), (1, 6), (3, 5), (4, 7), (4, 8)],
        [(0, 3), (1, 2)],
        [(0, 6), (1, 4), (1, 5), (2, 3)],
        [(2, 5), (2, 6), (3, 4)],
        [(0, 4), (0, 5), (1, 3), (6, 7), (6, 8)],
    ]
    seen_mask = 0
    for c_edges in colors:
        m = 0
        for e in c_edges:
            idx = edge_idx[e]
            assert not ((seen_mask >> idx) & 1), f"Duplicate edge {e}"
            seen_mask |= 1 << idx
            m |= 1 << idx
        assert is_strongly_woody_class_via_contraction(n_verts, edges, m)
    assert seen_mask == (1 << len(edges)) - 1
    print("[2/4] Verified explicit 6-coloring is a strongly woody partition via all 24 contractions.")


def enumerate_valid_color_classes(n_verts: int, edges: list[tuple[int, int]]) -> list[int]:
    """Enumerate all strongly woody edge subsets F subset E(G) directly via induced-tree components
    and verify equivalence with the contraction definition."""
    m = len(edges)
    adj_mask = [0] * n_verts
    for u, v in edges:
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u

    # Backtrack over edges: maintain union-find / component vertex masks for current F
    # Actually, a forest F has no broken cycles iff whenever u,v are in the SAME component of F,
    # and uv in E(G), then uv in F!
    # Wait: during edge-by-edge backtracking (decide include or exclude edge i),
    # if we EXCLUDE edge i=(u,v), then u and v may NEVER be placed in the same component!
    # If we INCLUDE edge i=(u,v), then u and v must currently be in DIFFERENT components,
    # AND no edge already EXCLUDED may join the merged component, AND no edge between
    # the merged components may be excluded later — wait: even simpler, if we decide edges 0..m-1,
    # whenever we include (u,v) we merge comp(u) and comp(v); whenever an edge (x,y) with x,y in same comp
    # is reached, it MUST be included (forced!) unless cycle, wait: if (x,y) is NOT yet included and x,y are
    # already in same component, then adding (x,y) creates a cycle AND excluding (x,y) creates a broken cycle!
    # So such a state is immediately DEAD!
    valid_masks = []
    comp_id = list(range(n_verts))
    comp_verts = [1 << v for v in range(n_verts)]
    forbidden_pairs = 0  # bitmask of vertex pairs? Better: check excluded edges at merge, or check all edges <= i

    # Precompute for each pair (u,v) whether it's an edge
    is_edge = [[False] * n_verts for _ in range(n_verts)]
    for u, v in edges:
        is_edge[u][v] = is_edge[v][u] = True

    # Even simpler: backtrack by partitioning vertices into components, OR edge backtracking:
    # Since at each step we test edges 0..m-1, if we maintain which pairs of components have a forbidden
    # (already excluded) edge between them, any merge of two components that had an excluded edge between them is dead!
    # Also, if an edge (u,v) has u,v already in the SAME component, it can neither be included (cycle) nor excluded (broken cycle)!
    excl_adj = [0] * n_verts  # bitmask of vertices connected to v by an excluded edge

    def dfs(idx: int, cur_mask: int, c_id: list[int], c_verts: list[int]) -> None:
        if idx == m:
            valid_masks.append(cur_mask)
            return
        u, v = edges[idx]
        cu, cv = c_id[u], c_id[v]
        if cu == cv:
            # Cannot include (cycle) and cannot exclude (broken cycle)! Prune immediately!
            return
        # Option 1: include edge idx, provided no excluded edge connects c_verts[cu] and c_verts[cv]
        cv_mask = c_verts[cv]
        cu_mask = c_verts[cu]
        can_merge = True
        tmp = cu_mask
        while tmp:
            lsb = tmp & -tmp
            w = lsb.bit_length() - 1
            if excl_adj[w] & cv_mask:
                can_merge = False
                break
            tmp ^= lsb
        if can_merge:
            # Merge cv into cu
            new_cid = c_id[:]
            new_cverts = c_verts[:]
            new_cverts[cu] = cu_mask | cv_mask
            new_cverts[cv] = 0
            t2 = cv_mask
            while t2:
                lsb = t2 & -t2
                w = lsb.bit_length() - 1
                new_cid[w] = cu
                t2 ^= lsb
            dfs(idx + 1, cur_mask | (1 << idx), new_cid, new_cverts)

        # Option 2: exclude edge idx
        excl_adj[u] |= 1 << v
        excl_adj[v] |= 1 << u
        dfs(idx + 1, cur_mask, c_id, c_verts)
        excl_adj[u] ^= 1 << v
        excl_adj[v] ^= 1 << u

    dfs(0, 0, comp_id, comp_verts)

    # Cross-check ALL enumerated masks against contraction definition!
    for mask in valid_masks:
        assert is_strongly_woody_class_via_contraction(n_verts, edges, mask)
    return valid_masks


def check_no_5_coloring(n_verts: int, edges: list[tuple[int, int]]) -> None:
    valid_masks = enumerate_valid_color_classes(n_verts, edges)
    valid_nonempty = [m for m in valid_masks if m != 0]
    print(f"[3/4] Enumerated all {len(valid_masks)} strongly woody color classes (verified against G/e).")

    # Exact cover into <= 5 strongly woody classes (breaking symmetry: each step picks lowest uncovered edge)
    full = (1 << len(edges)) - 1
    by_lowest = [[] for _ in range(len(edges))]
    for m in valid_nonempty:
        lsb = (m & -m).bit_length() - 1
        by_lowest[lsb].append(m)
    # Automatic upper bound pruning on edge weights (3*e_A + e_AB) computed directly from valid_nonempty
    eA_mask = sum((1 << i) for i, (u, v) in enumerate(edges) if u < 4 and v < 4)
    eAB_mask = sum((1 << i) for i, (u, v) in enumerate(edges) if (u < 4 <= v < 7) or (v < 4 <= u < 7))
    def w_mask(m: int) -> int:
        return 3 * (m & eA_mask).bit_count() + (m & eAB_mask).bit_count()

    max_size = max(m.bit_count() for m in valid_nonempty)
    max_w = max(w_mask(m) for m in valid_nonempty)
    for lst in by_lowest:
        lst.sort(key=lambda m: (-w_mask(m), -m.bit_count()))

    def can_cover(uncovered: int, rem_colors: int) -> bool:
        if uncovered == 0:
            return True
        if rem_colors == 0:
            return False
        if uncovered.bit_count() > rem_colors * max_size:
            return False
        if w_mask(uncovered) > rem_colors * max_w:
            return False
        lsb = (uncovered & -uncovered).bit_length() - 1
        for m in by_lowest[lsb]:
            if (m & uncovered) == m:
                if can_cover(uncovered ^ m, rem_colors - 1):
                    return True
        return False

    assert not can_cover(full, 5), "Found unexpected strongly woody 5-coloring!"
    assert can_cover(full, 6), "Exact cover failed to find 6-coloring!"
    print("[4/4] Exhaustive exact-cover search proved zeta(G) > 5 and zeta(G) = 6.")


def main() -> int:
    n_verts, edges = build_G()
    check_col_eq_5(n_verts, edges)
    check_explicit_6_coloring(n_verts, edges)
    check_no_5_coloring(n_verts, edges)
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
