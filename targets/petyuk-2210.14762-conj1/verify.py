"""Exact independent verifier for targets/petyuk-2210.14762-conj1/COUNTEREXAMPLE.md."""
import itertools

F_TABLE = {
    (0, 0, 0): 1, (0, 0, 1): 2, (0, 0, 2): 2,
    (0, 1, 0): 0, (0, 1, 1): 0, (0, 1, 2): 0,
    (0, 2, 0): 1, (0, 2, 1): 1, (0, 2, 2): 1,
    (1, 0, 0): 1, (1, 0, 1): 2, (1, 0, 2): 1,
    (1, 1, 0): 1, (1, 1, 1): 1, (1, 1, 2): 1,
    (1, 2, 0): 2, (1, 2, 1): 1, (1, 2, 2): 2,
    (2, 0, 0): 2, (2, 0, 1): 0, (2, 0, 2): 2,
    (2, 1, 0): 2, (2, 1, 1): 2, (2, 1, 2): 2,
    (2, 2, 0): 0, (2, 2, 1): 2, (2, 2, 2): 0,
}


def build_s43():
    verts = list(itertools.product(range(3), repeat=4))
    idx = {v: i for i, v in enumerate(verts)}
    adj = [set() for _ in range(len(verts))]
    for i, v in enumerate(verts):
        for a in range(3):
            u = v[1:] + (a,)
            j = idx[u]
            if i != j:
                adj[i].add(j)
                adj[j].add(i)
    return verts, adj


def color_s43(v):
    d1 = (v[1] - v[0]) % 3
    d2 = (v[2] - v[1]) % 3
    d3 = (v[3] - v[2]) % 3
    return (v[0] + F_TABLE[(d1, d2, d3)]) % 3


def bipartite_perms(X, Y, adj, flip_X=False, flip_Y=False):
    X0 = list(reversed(X)) if flip_X else list(X)
    Y0 = list(reversed(Y)) if flip_Y else list(Y)
    perms = [X0 + Y0]
    for y in Y:
        nx = [x for x in X if y in adj[x]]
        nonx = [x for x in X if y not in adj[x]]
        if nonx:
            perms.append(nx + [y] + nonx + [y2 for y2 in Y if y2 != y])
    return perms


def main():
    verts, adj = build_s43()
    n_verts = len(verts)
    n_edges = sum(len(a) for a in adj) // 2
    assert n_verts == 81 and n_edges == 237

    # 1. Verify exact proper 3-coloring
    colors = [color_s43(v) for v in verts]
    assert all(c in (0, 1, 2) for c in colors)
    for u in range(n_verts):
        for v in adj[u]:
            assert colors[u] != colors[v], f"Color conflict on edge {verts[u]}-{verts[v]}"

    # Also verify all 80 nonzero 4-tuples of first differences
    for d1, d2, d3, d4 in itertools.product(range(3), repeat=4):
        if (d1, d2, d3, d4) == (0, 0, 0, 0):
            continue
        assert F_TABLE[(d1, d2, d3)] != (d1 + F_TABLE[(d2, d3, d4)]) % 3

    # 2. Construct explicit representing word and verify literally from Definition 1
    A0 = [i for i in range(n_verts) if colors[i] == 0]
    A1 = [i for i in range(n_verts) if colors[i] == 1]
    A2 = [i for i in range(n_verts) if colors[i] == 2]
    assert len(A0) == 27 and len(A1) == 27 and len(A2) == 27

    p01 = bipartite_perms(A0, A1, adj, flip_X=False, flip_Y=False)
    p20 = bipartite_perms(A2, A0, adj, flip_X=False, flip_Y=True)
    p12 = bipartite_perms(A1, A2, adj, flip_X=True, flip_Y=True)
    M = max(len(p01), len(p20), len(p12))
    while len(p01) < M: p01.append(p01[0])
    while len(p20) < M: p20.append(p20[0])
    while len(p12) < M: p12.append(p12[0])

    word = []
    for t in range(M):
        word.extend(p01[t])
        word.extend(p20[t])
        word.extend(p12[t])

    pos = [[] for _ in range(n_verts)]
    for idx_pos, letter in enumerate(word):
        pos[letter].append(idx_pos)

    for u in range(n_verts):
        for v in range(u + 1, n_verts):
            pu, pv = pos[u], pos[v]
            i = j = 0
            merged = []
            while i < len(pu) and j < len(pv):
                if pu[i] < pv[j]:
                    merged.append(0)
                    i += 1
                else:
                    merged.append(1)
                    j += 1
            while i < len(pu):
                merged.append(0)
                i += 1
            while j < len(pv):
                merged.append(1)
                j += 1
            alternates = all(merged[r] != merged[r + 1] for r in range(len(merged) - 1))
            adjacent = (v in adj[u])
            assert alternates == adjacent, (
                f"Word mismatch on ({verts[u]}, {verts[v]}): "
                f"adjacent={adjacent}, alternates={alternates}"
            )

    print(
        f"S(4,3) (|V|={n_verts}, |E|={n_edges}): 3-coloring (27/27/27) and "
        f"explicit representing word (len={len(word)}, M={M}) verified on all "
        f"{n_verts * (n_verts - 1) // 2} pairs: PASS"
    )


if __name__ == "__main__":
    main()
