#!/usr/bin/env python3
"""Exact pure-Python verifier for the counterexample to arXiv:2303.08771v1 Conjecture 3."""

from collections import deque


def build_graph():
    A = [0, 1, 2, 3]
    B = [4, 5, 6]
    C = [7, 8]
    edges = []
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            edges.append((A[i], A[j]))
    for a in A:
        for b in B:
            edges.append((a, b))
    for b in B:
        for c in C:
            edges.append((b, c))
    return 9, edges


def compute_col_number(n, edges):
    """Exact col(G) = 1 + max_{H <= G, H != empty} delta(H)."""
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    max_min_deg = 0
    for mask in range(1, 1 << n):
        verts = [v for v in range(n) if (mask >> v) & 1]
        min_d = min(sum(1 for w in adj[v] if (mask >> w) & 1) for v in verts)
        if min_d > max_min_deg:
            max_min_deg = min_d
    return max_min_deg + 1


def is_forest_multigraph(n, edge_list):
    """Check if multigraph on n vertices (possibly with parallel edges, no self-loops) is acyclic."""
    parent = list(range(n))

    def find(x):
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


def is_strongly_woody_via_contraction(n, edges, edge_colors):
    """Verify woody in G AND in G/e (keeping parallel edges) for every edge e."""
    k = max(edge_colors) + 1
    # Check G itself
    for c in range(k):
        ce = [edges[i] for i in range(len(edges)) if edge_colors[i] == c]
        if not is_forest_multigraph(n, ce):
            return False
    # Check every contraction G/e
    for e_idx, (eu, ev) in enumerate(edges):
        for c in range(k):
            contracted = []
            for j, (u, v) in enumerate(edges):
                if j == e_idx or edge_colors[j] != c:
                    continue
                nu = eu if u == ev else u
                nv = eu if v == ev else v
                contracted.append((nu, nv))
            if not is_forest_multigraph(n, contracted):
                return False
    return True


def is_strongly_woody_via_induced_trees(n, edges, edge_colors):
    """Verify every color class is a forest whose connected components are induced trees in G."""
    k = max(edge_colors) + 1
    edge_set = {tuple(sorted(e)) for e in edges}
    for c in range(k):
        adj = [[] for _ in range(n)]
        ce = [edges[i] for i in range(len(edges)) if edge_colors[i] == c]
        if not is_forest_multigraph(n, ce):
            return False
        for u, v in ce:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n
        for start in range(n):
            if not visited[start]:
                comp = []
                q = deque([start])
                visited[start] = True
                while q:
                    cur = q.popleft()
                    comp.append(cur)
                    for nxt in adj[cur]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            q.append(nxt)
                # Count edges of G induced on comp: must equal len(comp) - 1
                induced_edges = 0
                for i in range(len(comp)):
                    for j in range(i + 1, len(comp)):
                        if tuple(sorted((comp[i], comp[j]))) in edge_set:
                            induced_edges += 1
                if induced_edges != len(comp) - 1:
                    return False
    return True


def enumerate_all_valid_color_classes(n, edges):
    """Enumerate all nonempty bitmasks of E(G) that form a valid strongly woody color class."""
    m = len(edges)
    edge_to_bit = {tuple(sorted(e)): (1 << i) for i, e in enumerate(edges)}
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    # First find all vertex subsets S (|S| >= 2) whose induced subgraph G[S] is a tree.
    # By the induced-tree characterization, every component (>= 2 vertices) of a valid color class
    # must have V(T) = S where G[S] is an induced tree, and E(T) = E(G[S]).
    induced_trees = []  # (vertex_mask, edge_mask)
    for vmask in range(1, 1 << n):
        verts = [v for v in range(n) if (vmask >> v) & 1]
        if len(verts) < 2:
            continue
        emask = 0
        ecnt = 0
        for i in range(len(verts)):
            for j in range(i + 1, len(verts)):
                pair = tuple(sorted((verts[i], verts[j])))
                if pair in edge_to_bit:
                    emask |= edge_to_bit[pair]
                    ecnt += 1
        if ecnt != len(verts) - 1:
            continue
        # Check connectedness of G[verts]
        seen = {verts[0]}
        stack = [verts[0]]
        while stack:
            cur = stack.pop()
            for nxt in adj[cur]:
                if ((vmask >> nxt) & 1) and nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        if len(seen) == len(verts):
            induced_trees.append((vmask, emask))

    # Build all valid color classes = vertex-disjoint unions of induced trees
    valid_classes = set()

    def build(idx, v_used, e_mask):
        if e_mask:
            valid_classes.add(e_mask)
        for i in range(idx, len(induced_trees)):
            vm, em = induced_trees[i]
            if not (v_used & vm):
                build(i + 1, v_used | vm, e_mask | em)

    build(0, 0, 0)
    return sorted(valid_classes)


def prove_no_5_coloring_exhaustively(n, edges):
    """Exact exhaustive proof that E(G) cannot be partitioned into <= 5 valid color classes."""
    m = len(edges)
    full_mask = (1 << m) - 1
    valid_classes = enumerate_all_valid_color_classes(n, edges)

    # Also verify Claim 2 (3*e_A + e_AB <= 6) across every valid color class
    mask_A = sum((1 << i) for i, (u, v) in enumerate(edges) if u < 4 and v < 4)
    mask_AB = sum((1 << i) for i, (u, v) in enumerate(edges) if (u < 4 and 4 <= v < 7))
    for em in valid_classes:
        eA = (em & mask_A).bit_count()
        eAB = (em & mask_AB).bit_count()
        assert 3 * eA + eAB <= 6, f"Bound failed on {bin(em)}: eA={eA}, eAB={eAB}"

    # Group valid classes by their tightest uncovered edge (exact cover with <= 5 classes)
    by_lowest_edge = [[] for _ in range(m)]
    for em in valid_classes:
        lsb = (em & -em).bit_length() - 1
        by_lowest_edge[lsb].append(em)

    def can_cover(uncovered_mask, colors_left):
        if uncovered_mask == 0:
            return True
        if colors_left == 0:
            return False
        rem_w = 3 * (uncovered_mask & mask_A).bit_count() + (uncovered_mask & mask_AB).bit_count()
        if rem_w > 6 * colors_left:
            return False
        if uncovered_mask.bit_count() > 6 * colors_left:
            return False
        e_bit = (uncovered_mask & -uncovered_mask).bit_length() - 1
        for em in by_lowest_edge[e_bit]:
            if (em & uncovered_mask) == em:
                if can_cover(uncovered_mask ^ em, colors_left - 1):
                    return True
        return False

    return not can_cover(full_mask, 5)


def main():
    n, edges = build_graph()
    assert n == 9 and len(edges) == 24
    assert len(set(edges)) == 24

    col = compute_col_number(n, edges)
    assert col == 5, f"Expected col(G)=5, got {col}"

    # Verify explicit 6-coloring
    color_classes = [
        [(0, 1), (2, 4), (3, 6), (5, 7), (5, 8)],
        [(0, 2), (1, 6), (3, 5), (4, 7), (4, 8)],
        [(0, 3), (1, 2)],
        [(0, 6), (1, 4), (1, 5), (2, 3)],
        [(2, 5), (2, 6), (3, 4)],
        [(0, 4), (0, 5), (1, 3), (6, 7), (6, 8)],
    ]
    edge_to_idx = {e: i for i, e in enumerate(edges)}
    edge_colors = [-1] * len(edges)
    for c_idx, cls in enumerate(color_classes):
        for e in cls:
            idx = edge_to_idx[tuple(sorted(e))]
            assert edge_colors[idx] == -1, f"Duplicate edge {e}"
            edge_colors[idx] = c_idx
    assert all(c != -1 for c in edge_colors), "Uncolored edge"
    assert is_strongly_woody_via_contraction(n, edges, edge_colors), "6-coloring failed contraction check"
    assert is_strongly_woody_via_induced_trees(n, edges, edge_colors), "6-coloring failed induced-tree check"

    # Exhaustively verify zeta(G) > 5
    ok_no_5 = prove_no_5_coloring_exhaustively(n, edges)
    assert ok_no_5, "Found unexpected 5-coloring!"

    print("PASS: G(4,3,2) has n=9, m=24, col(G)=5, and zeta(G)=6 > col(G).")


if __name__ == "__main__":
    main()
