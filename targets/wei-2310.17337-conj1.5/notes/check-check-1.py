"""Independent exact-arithmetic verifier for targets/wei-2310.17337-conj1.5/.

Written strictly from arXiv:2310.17337v1 (Section 1, Conjecture 1.5)
and COUNTEREXAMPLE.md, without reading the finder's verify.py or notes/.
"""

from fractions import Fraction
from itertools import combinations


def closed_neighborhood(adj: dict[int, set[int]], D: set[int]) -> set[int]:
    closed = set(D)
    for v in D:
        closed.update(adj[v])
    return closed


def is_connected(vertices: set[int], adj: dict[int, set[int]]) -> bool:
    if not vertices:
        return False
    start = next(iter(vertices))
    seen = {start}
    stack = [start]
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w in vertices and w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == len(vertices)


def find_ck_subgraph(vertices: set[int], adj: dict[int, set[int]], k: int) -> list[int] | None:
    """Return a k-cycle (list of k vertices) in induced subgraph G[vertices], or None."""
    if len(vertices) < k:
        return None
    sub_adj = {u: sorted(adj[u] & vertices) for u in sorted(vertices)}
    ordered = sorted(vertices)
    # To avoid duplicate cycle traversals, require start to be the minimum vertex in the cycle
    for start in ordered:
        # Need at least 2 neighbors >= start
        cands = [w for w in sub_adj[start] if w > start]
        if len(cands) < 2:
            continue
        path = [start]
        used = {start}

        def dfs(curr: int) -> list[int] | None:
            if len(path) == k:
                if start in sub_adj[curr]:
                    return list(path)
                return None
            # Symmetry breaking on direction: path[1] < path[-1] enforced at end or via min neighbor
            for nxt in sub_adj[curr]:
                if nxt > start and nxt not in used:
                    if len(path) == 1 or True:
                        used.add(nxt)
                        path.append(nxt)
                        res = dfs(nxt)
                        if res is not None:
                            return res
                        path.pop()
                        used.remove(nxt)
            return None

        res = dfs(start)
        if res is not None:
            return res
    return None


def exact_isolation_number_upto(
    vertices: set[int], adj: dict[int, set[int]], k: int, max_d: int
) -> tuple[int | None, dict[int, list[int]]]:
    """Check if any D with |D| <= max_d is C_k-isolating; return smallest |D| and witnesses."""
    witnesses_for_singletons: dict[int, list[int]] = {}
    for size in range(max_d + 1):
        for D_tuple in combinations(sorted(vertices), size):
            D = set(D_tuple)
            rem = vertices - closed_neighborhood(adj, D)
            cyc = find_ck_subgraph(rem, adj, k)
            if cyc is None:
                return size, witnesses_for_singletons
            if size == 1:
                witnesses_for_singletons[D_tuple[0]] = cyc
    return None, witnesses_for_singletons


def build_truncated_tetrahedron() -> tuple[set[int], dict[int, set[int]]]:
    vertices = set(range(12))
    raw_edges = [
        # T0, T1, T2, T3
        (0, 1), (1, 2), (2, 0),
        (3, 4), (4, 5), (5, 3),
        (6, 7), (7, 8), (8, 6),
        (9, 10), (10, 11), (11, 9),
        # 6 matching edges
        (0, 3), (1, 6), (2, 9), (4, 7), (5, 10), (8, 11),
    ]
    adj: dict[int, set[int]] = {v: set() for v in vertices}
    for u, v in raw_edges:
        assert u != v, "Self-loop detected"
        assert v not in adj[u], f"Duplicate edge {(u, v)}"
        adj[u].add(v)
        adj[v].add(u)
    return vertices, adj


def build_gp(n_ring: int, step: int) -> tuple[set[int], dict[int, set[int]]]:
    vertices = set(range(2 * n_ring))
    adj: dict[int, set[int]] = {v: set() for v in vertices}
    for i in range(n_ring):
        edges = [
            (i, (i + 1) % n_ring),
            (i, n_ring + i),
            (n_ring + i, n_ring + ((i + step) % n_ring)),
        ]
        for u, v in edges:
            assert u != v
            adj[u].add(v)
            adj[v].add(u)
    return vertices, adj


def verify_counterexample(
    name: str,
    vertices: set[int],
    adj: dict[int, set[int]],
    k: int,
    expected_n: int,
    expected_m: int,
    expected_iota: int,
) -> bool:
    n = len(vertices)
    m = sum(len(adj[v]) for v in vertices) // 2
    assert n == expected_n, f"{name}: expected n={expected_n}, got {n}"
    assert m == expected_m, f"{name}: expected m={expected_m}, got {m}"
    assert is_connected(vertices, adj), f"{name}: graph is not connected"
    assert not (n == k and all(len(adj[v]) == 2 for v in vertices)), f"{name}: isomorphic to C_{k}"

    iota, singleton_witnesses = exact_isolation_number_upto(vertices, adj, k, expected_iota)
    assert iota == expected_iota, f"{name}: expected iota={expected_iota}, got {iota}"
    assert len(singleton_witnesses) == n, f"{name}: missing singleton witness"

    lhs = Fraction(iota, 1)
    rhs = Fraction(m + 1, k + 2)
    print(f"{name}: n={n}, m={m}, k={k}, iota(G,C_{k})={lhs}, (m+1)/(k+2)={rhs}, diff={lhs - rhs}")
    return lhs > rhs


def main() -> None:
    # 1. Primary counterexample: Truncated tetrahedron, k = 8
    V, adj = build_truncated_tetrahedron()
    assert all(len(adj[v]) == 3 for v in V), "Truncated tetrahedron should be 3-regular"

    # Check explicit witness for v = 0 in COUNTEREXAMPLE.md: (4, 5, 10, 9, 11, 8, 6, 7, 4)
    explicit_cyc = [4, 5, 10, 9, 11, 8, 6, 7]
    rem0 = V - closed_neighborhood(adj, {0})
    assert rem0 == set(explicit_cyc), f"Unexpected V \\ N[0]: {rem0}"
    for i in range(8):
        u, v = explicit_cyc[i], explicit_cyc[(i + 1) % 8]
        assert v in adj[u], f"Missing cycle edge {(u, v)}"

    # Check explicit isolating set D = {0, 4}
    rem04 = V - closed_neighborhood(adj, {0, 4})
    assert len(rem04) == 5 and find_ck_subgraph(rem04, adj, 8) is None

    ok_main = verify_counterexample("TruncatedTetrahedron", V, adj, k=8, expected_n=12, expected_m=18, expected_iota=2)

    # 2. Secondary counterexamples mentioned in COUNTEREXAMPLE.md
    V9, adj9 = build_gp(9, 2)
    ok_gp9 = verify_counterexample("GP(9,2)", V9, adj9, k=14, expected_n=18, expected_m=27, expected_iota=2)

    V11, adj11 = build_gp(11, 2)
    ok_gp11 = verify_counterexample("GP(11,2)", V11, adj11, k=18, expected_n=22, expected_m=33, expected_iota=2)

    if ok_main and ok_gp9 and ok_gp11:
        print("PASS")
    else:
        print("FAIL")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
