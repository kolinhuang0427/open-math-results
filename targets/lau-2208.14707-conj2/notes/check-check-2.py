"""Independent exact-arithmetic verifier for targets/lau-2208.14707-conj2/."""

from collections import deque
from itertools import product
import sys


def complete_graph(n: int):
    verts = list(range(n))
    edges = {(i, j) for i in range(n) for j in range(i + 1, n)}
    return verts, edges


def is_connected(verts, edges) -> bool:
    adj = {v: set() for v in verts}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    seen = {verts[0]}
    q = deque([verts[0]])
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return len(seen) == len(verts)


def shortest_odd_cycle(verts, edges) -> int:
    adj = {v: set() for v in verts}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    best = None
    for s in verts:
        dist = {s: 0}
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    q.append(v)
                elif dist[v] % 2 == dist[u] % 2:
                    cyc = dist[u] + dist[v] + 1
                    if best is None or cyc < best:
                        best = cyc
    assert best is not None
    return best


def chromatic_number(verts, edges) -> int:
    """Exact chromatic number via backtracking with symmetry breaking & pruning."""
    n = len(verts)
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    def can_color(t: int) -> bool:
        cols = [-1] * n

        def dfs(idx: int, max_used: int) -> bool:
            if idx == n:
                return True
            forbidden = {cols[nb] for nb in adj[idx] if cols[nb] != -1}
            limit = min(t, max_used + 2)
            for c in range(limit):
                if c not in forbidden:
                    cols[idx] = c
                    if dfs(idx + 1, max(max_used, c)):
                        return True
                    cols[idx] = -1
            return False

        return dfs(0, -1)

    for t in range(1, n + 1):
        if can_color(t):
            return t
    return n


def lex_product(G, H):
    vg, eg = G
    vh, eh = H
    verts = [(u, up) for u in vg for up in vh]
    edges = set()
    for i in range(len(verts)):
        u, up = verts[i]
        for j in range(i + 1, len(verts)):
            v, vp = verts[j]
            adj_g = (min(u, v), max(u, v)) in eg
            adj_h = (u == v) and ((min(up, vp), max(up, vp)) in eh)
            if adj_g or adj_h:
                edges.add((i, j))
    return verts, edges


def main():
    G = complete_graph(4)
    H = complete_graph(2)
    assert is_connected(*G) and is_connected(*H)

    girth_odd = shortest_odd_cycle(*G)
    assert girth_odd == 3
    k = (girth_odd - 1) // 2
    assert 2 * k + 1 == girth_odd and k == 1

    chi_G = chromatic_number(*G)
    chi_H = chromatic_number(*H)
    assert chi_G == 4 and chi_H == 2

    GH_verts, GH_edges = lex_product(G, H)
    assert len(GH_verts) == 8
    assert len(GH_edges) == 28  # K_8

    # Lower bound: any local antimagic labeling induces a proper vertex coloring
    chi_GH = chromatic_number(GH_verts, GH_edges)
    assert chi_GH == 8

    # Explicit edge labeling f: E(K_8) -> {1, ..., 28} from COUNTEREXAMPLE.md
    f = {}
    for i in range(8):
        for j in range(i + 1, 8):
            assert (i, j) in GH_edges
            label = 1 + sum(7 - a for a in range(i)) + (j - i - 1)
            f[(i, j)] = label

    assert sorted(f.values()) == list(range(1, 29))

    # Compute vertex sums f^+(v)
    sums = [0] * 8
    for (i, j), val in f.items():
        sums[i] += val
        sums[j] += val
    assert sums == [28, 64, 90, 108, 120, 128, 134, 140]

    # Verify proper local antimagic condition: f^+(u) != f^+(v) for all uv in E(G[H])
    for i, j in GH_edges:
        assert sums[i] != sums[j]

    # Hence chi_la(G[H]) == 8 == chi(G) * chi(H)
    chi_la_GH = len(set(sums))
    assert chi_la_GH == 8 == chi_G * chi_H

    # Check RHS: 2*chi(H) + ceil(chi(H)/k)
    ceil_term = (chi_H + k - 1) // k
    rhs = 2 * chi_H + ceil_term
    assert rhs == 6
    assert chi_G * chi_H != rhs

    print(f"PASS (G=K4, H=K2: k={k}, chi(G)*chi(H)=chi_la(G[H])={chi_la_GH} != 2*chi(H)+ceil(chi(H)/k)={rhs})")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
