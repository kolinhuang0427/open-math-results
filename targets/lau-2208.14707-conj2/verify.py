"""Exact integer verification of the counterexample (G, H) = (K_4, K_2) to arXiv:2208.14707v1 Conjecture 2."""

import itertools
import sys


def chromatic_number(n: int, edges: set[tuple[int, int]]) -> int:
    """Exact chromatic number by backtracking/brute force for small n."""
    for c in range(1, n + 1):
        for col in itertools.product(range(c), repeat=n):
            if all(col[u] != col[v] for u, v in edges):
                return c
    raise AssertionError("Unreachable")


def shortest_odd_cycle_length(n: int, edges: set[tuple[int, int]]) -> int:
    """Exact shortest odd cycle length via BFS from each vertex."""
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    best = None
    for s in range(n):
        dist = [-1] * n
        parent = [-1] * n
        dist[s] = 0
        q = [s]
        for u in q:
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
                elif v != parent[u] and (dist[u] + dist[v] + 1) % 2 == 1:
                    cyc_len = dist[u] + dist[v] + 1
                    if best is None or cyc_len < best:
                        best = cyc_len
    assert best is not None
    return best


def main() -> int:
    # 1. Define G = K_4 and H = K_2
    nG = 4
    edgesG = {(u, v) for u in range(nG) for v in range(u + 1, nG)}
    nH = 2
    edgesH = {(0, 1)}

    chi_G = chromatic_number(nG, edgesG)
    chi_H = chromatic_number(nH, edgesH)
    assert chi_G == 4, f"Expected chi(K_4)=4, got {chi_G}"
    assert chi_H == 2, f"Expected chi(K_2)=2, got {chi_H}"

    odd_len = shortest_odd_cycle_length(nG, edgesG)
    assert odd_len == 3 and odd_len % 2 == 1
    k = (odd_len - 1) // 2
    assert k == 1 and k >= 1

    # 2. Construct lexicographic product G[H] directly from the primary definition
    verts = [(u, up) for u in range(nG) for up in range(nH)]
    v_idx = {v: i for i, v in enumerate(verts)}
    edgesGH = set()
    for i, (u, up) in enumerate(verts):
        for j in range(i + 1, len(verts)):
            v, vp = verts[j]
            adj_in_G = (min(u, v), max(u, v)) in edgesG
            adj_in_H = (u == v) and ((min(up, vp), max(up, vp)) in edgesH)
            if adj_in_G or adj_in_H:
                edgesGH.add((i, j))

    # Verify G[H] is K_8 (all 28 pairs adjacent), forcing chi_la(G[H]) >= chi(G[H]) = 8
    nGH = len(verts)
    assert nGH == 8
    assert len(edgesGH) == nGH * (nGH - 1) // 2 == 28
    chi_GH = chromatic_number(nGH, edgesGH)
    assert chi_GH == 8

    # 3. Verify explicit local antimagic bijection f: E(G[H]) -> {1, ..., 28}
    sorted_edges = sorted(edgesGH)
    f = {e: idx for idx, e in enumerate(sorted_edges, start=1)}
    assert set(f.values()) == set(range(1, 29))

    sums = [0] * nGH
    for (i, j), val in f.items():
        sums[i] += val
        sums[j] += val

    assert sums == [28, 64, 90, 108, 120, 128, 134, 140], f"Unexpected sums: {sums}"
    assert len(set(sums)) == 8
    for i, j in edgesGH:
        assert sums[i] != sums[j]

    # Since chi(G[H]) = 8 <= chi_la(G[H]) <= 8, we have chi_la(G[H]) = 8
    chi_la_GH = 8
    lhs_cond = (chi_la_GH == chi_G * chi_H)
    assert lhs_cond is True

    # 4. Compute RHS of Conjecture 2 using exact integer ceiling
    ceil_chiH_k = (chi_H + k - 1) // k
    rhs_val = 2 * chi_H + ceil_chiH_k
    assert rhs_val == 6
    assert chi_G * chi_H == 8
    rhs_cond = (chi_G * chi_H == rhs_val)
    assert rhs_cond is False

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
