"""Independent exact verifier for targets/petyuk-2210.14762-conj1/COUNTEREXAMPLE.md.

Written strictly from arXiv:2210.14762v2 (simplified_de_Bruijn_graphs__4_.tex)
and COUNTEREXAMPLE.md, without reading verify.py or author notes.
"""

from __future__ import annotations

import itertools
import random
import sys


TABLE_F: dict[tuple[int, int], tuple[int, int, int]] = {
    (0, 0): (1, 2, 2),
    (0, 1): (0, 0, 0),
    (0, 2): (1, 1, 1),
    (1, 0): (1, 2, 1),
    (1, 1): (1, 1, 1),
    (1, 2): (2, 1, 2),
    (2, 0): (2, 0, 2),
    (2, 1): (2, 2, 2),
    (2, 2): (0, 2, 0),
}


def f_val(d1: int, d2: int, d3: int) -> int:
    return TABLE_F[(d1, d2)][d3]


def color_vertex(x: tuple[int, int, int, int]) -> int:
    d1 = (x[1] - x[0]) % 3
    d2 = (x[2] - x[1]) % 3
    d3 = (x[3] - x[2]) % 3
    return (x[0] + f_val(d1, d2, d3)) % 3


def build_s43() -> tuple[list[tuple[int, int, int, int]], set[tuple[tuple[int, ...], tuple[int, ...]]], dict]:
    vertices = list(itertools.product((0, 1, 2), repeat=4))
    assert len(vertices) == 81
    edges: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    adj: dict[tuple[int, ...], set[tuple[int, ...]]] = {v: set() for v in vertices}
    for x in vertices:
        for x5 in (0, 1, 2):
            y = (x[1], x[2], x[3], x5)
            if x == y:  # loop removed in S(4,3)
                continue
            u, v = (x, y) if x < y else (y, x)
            edges.add((u, v))
            adj[x].add(y)
            adj[y].add(x)
    assert len(edges) == 237
    return vertices, edges, adj


def check_coloring_and_diff_condition(
    vertices: list[tuple[int, int, int, int]],
    edges: set[tuple[tuple[int, ...], tuple[int, ...]]],
    adj: dict,
) -> dict[tuple[int, ...], int]:
    colors = {v: color_vertex(v) for v in vertices}
    for u, v in edges:
        assert colors[u] != colors[v], f"improper edge {u}--{v}"

    # Verify triangle 0010 - 0100 - 1001
    t = [(0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 1)]
    for a, b in itertools.combinations(t, 2):
        assert b in adj[a]

    # Verify all 80 nonzero tuples (d1,d2,d3,d4)
    for d1, d2, d3, d4 in itertools.product((0, 1, 2), repeat=4):
        if (d1, d2, d3, d4) == (0, 0, 0, 0):
            continue
        assert f_val(d1, d2, d3) != (d1 + f_val(d2, d3, d4)) % 3

    classes = [[v for v in vertices if colors[v] == i] for i in (0, 1, 2)]
    assert [len(c) for c in classes] == [27, 27, 27]
    return colors


def build_representing_word(
    classes: list[list[tuple[int, int, int, int]]],
    adj: dict,
) -> list[tuple[int, int, int, int]]:
    A0, A1, A2 = classes

    def make_list(X: list, Y: list, p0: list) -> list[list]:
        perms = [p0]
        X_set = set(X)
        for y in Y:
            nx = [x for x in X if x in adj[y]]
            assert len(nx) < len(X), f"y={y} adjacent to all of X"
            rest_x = [x for x in X if x not in adj[y]]
            rest_y = [z for z in Y if z != y]
            perms.append(nx + [y] + rest_x + rest_y)
        assert len(perms) == 28
        return perms

    L01 = make_list(A0, A1, A0 + A1)
    L20 = make_list(A2, A0, A2 + list(reversed(A0)))
    L12 = make_list(A1, A2, list(reversed(A1)) + list(reversed(A2)))

    w: list[tuple[int, int, int, int]] = []
    for t in range(28):
        w.extend(L01[t])
        w.extend(L20[t])
        w.extend(L12[t])
    assert len(w) == 4536
    return w


def verify_word_represents(
    w: list[tuple[int, int, int, int]],
    vertices: list[tuple[int, int, int, int]],
    edges: set[tuple[tuple[int, ...], tuple[int, ...]]],
) -> None:
    positions: dict[tuple[int, int, int, int], list[int]] = {v: [] for v in vertices}
    for idx, v in enumerate(w):
        positions[v].append(idx)

    # Check exact alternation for ALL 3240 unordered pairs {u, v}
    pair_count = 0
    for u, v in itertools.combinations(vertices, 2):
        pair_count += 1
        pu = positions[u]
        pv = positions[v]
        # Merge sorted position lists to check alternation directly
        i = j = 0
        merged_who: list[int] = []
        while i < len(pu) and j < len(pv):
            if pu[i] < pv[j]:
                merged_who.append(0)
                i += 1
            else:
                merged_who.append(1)
                j += 1
        while i < len(pu):
            merged_who.append(0)
            i += 1
        while j < len(pv):
            merged_who.append(1)
            j += 1
        alternates = len(merged_who) >= 2 and all(
            merged_who[k] != merged_who[k + 1] for k in range(len(merged_who) - 1)
        )
        edge = (u, v) if u < v else (v, u)
        is_edge = edge in edges
        assert alternates == is_edge, f"word mismatch on pair {u}, {v}: alt={alternates}, edge={is_edge}"
    assert pair_count == 3240


def main() -> int:
    vertices, edges, adj = build_s43()
    colors = check_coloring_and_diff_condition(vertices, edges, adj)
    print("S(4,3) (81 vertices, 237 edges), triangle, 80 nonzero tuples, & 3-coloring (27/27/27): OK")

    classes_lex = [[v for v in vertices if colors[v] == i] for i in (0, 1, 2)]
    w_lex = build_representing_word(classes_lex, adj)
    verify_word_represents(w_lex, vertices, edges)
    print("Explicit representing word (len=4536, M=28, lex order) across all 3240 pairs: OK")

    # Also test an arbitrary shuffled ordering of each color class (claim: "ordered arbitrarily")
    rng = random.Random(221014762)
    classes_shuf = [list(c) for c in classes_lex]
    for c in classes_shuf:
        rng.shuffle(c)
    w_shuf = build_representing_word(classes_shuf, adj)
    verify_word_represents(w_shuf, vertices, edges)
    print("Explicit representing word (arbitrary shuffled class order) across all 3240 pairs: OK")

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
