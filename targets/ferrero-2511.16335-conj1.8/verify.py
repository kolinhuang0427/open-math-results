"""Exact verifier for the counterexample to Conjecture 1.8 of Ferrero et al. (arXiv:2511.16335v1)."""

from itertools import combinations
import networkx as nx


def build_c6_blowup(sizes):
    """Return C_6[sizes[0]*K_1, ..., sizes[5]*K_1]."""
    assert len(sizes) == 6 and all(r >= 2 for r in sizes)
    G = nx.Graph()
    parts = []
    vid = 0
    for r in sizes:
        part = list(range(vid, vid + r))
        parts.append(part)
        G.add_nodes_from(part)
        vid += r
    for i in range(6):
        j = (i + 1) % 6
        for u in parts[i]:
            for v in parts[j]:
                G.add_edge(u, v)
    return G


def standard_prop_time(G, B):
    """Return exact standard zero forcing propagation time, or None if B is not forcing."""
    n = G.number_of_nodes()
    blue = set(B)
    rounds = 0
    while len(blue) < n:
        newly_forced = set()
        for u in blue:
            white_nbrs = [w for w in G.neighbors(u) if w not in blue]
            if len(white_nbrs) == 1:
                newly_forced.add(white_nbrs[0])
        if not newly_forced:
            return None
        blue |= newly_forced
        rounds += 1
    return rounds


def verify_exhaustive(G, name):
    """Exhaustively check all 2^n subsets of G."""
    nodes = list(G.nodes())
    n = len(nodes)
    assert nx.is_connected(G), f"{name}: G not connected"
    assert not nx.is_connected(nx.complement(G)) is False, f"{name}: complement disconnected (would be a join)"
    # Explicit check: G is not complete and complement is connected -> not a standard fast join
    assert G.number_of_edges() < n * (n - 1) // 2, f"{name}: G is complete"
    assert nx.is_connected(nx.complement(G)), f"{name}: complement is disconnected"

    forcing_pts = {}
    for r in range(n + 1):
        for comb in combinations(nodes, r):
            key = frozenset(comb)
            pt = standard_prop_time(G, key)
            if pt is not None:
                forcing_pts[key] = pt

    minimal = [
        (key, pt)
        for key, pt in forcing_pts.items()
        if all((key - {v}) not in forcing_pts for v in key)
    ]
    assert len(minimal) > 0, f"{name}: no minimal forcing sets"
    pt_bar = max(pt for _, pt in minimal)
    pt_ul = min(pt for _, pt in minimal)
    sizes = set(len(key) for key, _ in minimal)
    print(f"{name}: n={n}, m={G.number_of_edges()}, minimal_count={len(minimal)}, sizes={sizes}, PTul={pt_ul}, PTbar={pt_bar}, comp_connected=True")
    assert pt_bar == 1, f"{name}: expected PTbar == 1, got {pt_bar}"


def main():
    G12 = nx.circulant_graph(12, [1, 5])
    B12 = build_c6_blowup([2, 2, 2, 2, 2, 2])
    assert nx.is_isomorphic(G12, B12), "Circ(12, {1, 5}) should be isomorphic to C_6[2K_1]"
    verify_exhaustive(G12, "Circ(12, {1, 5}) ~= C_6[2K_1]")

    # Also exhaustively verify an asymmetric 13-vertex instance C_6[3K_1, 2K_1, ...]
    G13 = build_c6_blowup([3, 2, 2, 2, 2, 2])
    verify_exhaustive(G13, "C_6[3K_1, 2K_1^5]")
    print("PASS")


if __name__ == "__main__":
    main()
