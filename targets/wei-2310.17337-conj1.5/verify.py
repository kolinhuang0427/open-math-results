#!/usr/bin/env python3
"""Exact integer/rational verifier for counterexample to Wei-Zhang-Zhao Conjecture 1.5 (arXiv:2310.17337v1)."""

from fractions import Fraction
from itertools import combinations, permutations


def build_truncated_tetrahedron():
    n = 12
    edges = [
        # Four triangles
        (0, 1), (0, 2), (1, 2),
        (3, 4), (3, 5), (4, 5),
        (6, 7), (6, 8), (7, 8),
        (9, 10), (9, 11), (10, 11),
        # Six matching edges
        (0, 3), (1, 6), (2, 9),
        (4, 7), (5, 10), (8, 11),
    ]
    return n, edges


def verify():
    n, edges = build_truncated_tetrahedron()
    k = 8

    # 1. Check simple graph
    edge_set = set()
    adj = {v: set() for v in range(n)}
    for u, v in edges:
        assert 0 <= u < n and 0 <= v < n and u != v, "Invalid edge endpoint or self-loop"
        e = (min(u, v), max(u, v))
        assert e not in edge_set, f"Duplicate edge {e}"
        edge_set.add(e)
        adj[u].add(v)
        adj[v].add(u)

    m = len(edge_set)
    assert m == 18, f"Expected m=18, got {m}"

    # 2. Check connectivity via BFS
    seen = {0}
    queue = [0]
    while queue:
        u = queue.pop()
        for w in adj[u]:
            if w not in seen:
                seen.add(w)
                queue.append(w)
    assert len(seen) == n, "Graph is not connected"

    # 3. Check G is not isomorphic to C_8
    assert n != k or m != k, "Graph is isomorphic to C_k"

    # 4. Check for every vertex v, G - N[v] contains a C_8
    for v in range(n):
        closed_nb = {v} | adj[v]
        rem = sorted(set(range(n)) - closed_nb)
        assert len(rem) >= k, f"Remaining vertices < {k} after removing N[{v}]"
        found_c8 = None
        # Since len(rem) == 8, check all cyclic orderings fixing rem[0]
        if len(rem) == k:
            r0 = rem[0]
            for p in permutations(rem[1:]):
                cyc = (r0,) + p
                if all(cyc[(i + 1) % k] in adj[cyc[i]] for i in range(k)):
                    found_c8 = cyc
                    break
        assert found_c8 is not None, f"No C_8 found in G - N[{v}]"

    # 5. Exhaustively verify exact iota(G, C_8) == 2
    # Enumerate all 8-vertex subsets that span a C_8
    c8_vertex_sets = []
    for sub in combinations(range(n), k):
        s0 = sub[0]
        for p in permutations(sub[1:]):
            cyc = (s0,) + p
            if all(cyc[(i + 1) % k] in adj[cyc[i]] for i in range(k)):
                c8_vertex_sets.append(set(sub))
                break

    assert len(c8_vertex_sets) > 0, "Graph has no C_8"

    # Confirm no size-1 isolating set
    for v in range(n):
        cnb = {v} | adj[v]
        if all(len(c & cnb) > 0 for c in c8_vertex_sets):
            raise AssertionError(f"Singleton {{{v}}} is a C_8-isolating set!")

    # Confirm a size-2 isolating set exists (e.g., {0, 4})
    witness_d = {0, 4}
    cnb_d = set()
    for v in witness_d:
        cnb_d |= {v} | adj[v]
    assert all(len(c & cnb_d) > 0 for c in c8_vertex_sets), "Witness D={0,4} failed"

    iota = 2
    bound = Fraction(m + 1, k + 2)
    assert Fraction(iota) > bound, f"iota={iota} does not exceed bound {bound}"

    print(f"G: truncated tetrahedron (n={n}, m={m}), k={k}")
    print(f"Exact iota(G, C_{k}) = {iota}")
    print(f"Conjecture bound (m+1)/(k+2) = {bound}")
    print(f"Counterexample check: {iota} > {bound} -> PASS")


if __name__ == "__main__":
    verify()
