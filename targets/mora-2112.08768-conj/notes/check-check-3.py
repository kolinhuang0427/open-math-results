"""Independent exact-arithmetic verifier for targets/mora-2112.08768-conj/.

Derived directly from Mora, Souto-Salorio & Tarrio-Tobar arXiv:2112.08768v1
(Section 1 & Section 3, Conjecture 21) and targets/mora-2112.08768-conj/COUNTEREXAMPLE.md
without reading verify.py or author notes. Zero floating-point arithmetic is used anywhere.

Checks:
1. Graph BFS shortest-path distances match L1 Manhattan distance on P_3 x P_3 x P_4.
2. Primary counterexample (n1, n2, n3, k) = (3, 3, 4, 13):
   - alpha_m = 12 <= 13 < 15 = alpha_M; conjectured min(32, 34) = 32;
   - Explicit 30-vertex witness S = F_edge U F_int = V \\ M has exact minimum resolving count 14 >= k+1 = 14
     across all C(36, 2) = 630 pairs (minimum attained at (0,0,1),(0,1,0) with 12 in F_edge, 2 in F_int).
3. Further counterexamples (3, 3, 5, 15), (3, 4, 4, 15), (4, 4, 4, 17):
   - alpha_m <= k < alpha_M, conjectured value > |S|, and exhaustive verification across all vertex pairs
     confirming S is (k+1)-resolving of size 2*alpha_m + 6 < 4k - 2*alpha_m + 4.
"""

from __future__ import annotations

from collections import deque
from itertools import combinations


def alpha_m(n1: int, n2: int, n3: int) -> int:
    return 2 * (n1 + n2 + n3) - 8


def alpha_M(n1: int, n2: int, n3: int) -> int:
    return min(n1 * (n2 + n3 - 2), n2 * (n1 + n3 - 2), n3 * (n1 + n2 - 2))


def conjectured_dim(n1: int, n2: int, n3: int, k: int) -> int:
    am = alpha_m(n1, n2, n3)
    return min(4 * k - 2 * am + 4, n1 * n2 * n3 - (n1 - 2) * (n2 - 2) * (n3 - 2))


def grid_vertices(n1: int, n2: int, n3: int) -> list[tuple[int, int, int]]:
    return [(x1, x2, x3) for x1 in range(n1) for x2 in range(n2) for x3 in range(n3)]


def dist(u: tuple[int, int, int], v: tuple[int, int, int]) -> int:
    return abs(u[0] - v[0]) + abs(u[1] - v[1]) + abs(u[2] - v[2])


def verify_bfs_matches_l1(n1: int, n2: int, n3: int) -> None:
    verts = grid_vertices(n1, n2, n3)
    vset = set(verts)
    for src in verts:
        seen = {src: 0}
        dq = deque([src])
        while dq:
            cur = dq.popleft()
            d = seen[cur]
            for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                nxt = (cur[0] + dx, cur[1] + dy, cur[2] + dz)
                if nxt in vset and nxt not in seen:
                    seen[nxt] = d + 1
                    dq.append(nxt)
        assert len(seen) == len(verts)
        for dst in verts:
            assert seen[dst] == dist(src, dst)


def build_witness(n1: int, n2: int, n3: int) -> tuple[set[tuple[int, int, int]], set[tuple[int, int, int]], set[tuple[int, int, int]]]:
    verts = grid_vertices(n1, n2, n3)
    f_edge = {
        (x1, x2, x3)
        for (x1, x2, x3) in verts
        if (x1 in (0, n1 - 1)) + (x2 in (0, n2 - 1)) + (x3 in (0, n3 - 1)) >= 2
    }
    f_int = {
        (0, 1, 1),
        (n1 - 1, 1, 1),
        (1, 0, 1),
        (1, n2 - 1, 1),
        (1, 1, 0),
        (1, 1, n3 - 1),
    }
    assert f_edge.isdisjoint(f_int)
    s_set = f_edge | f_int
    return s_set, f_edge, f_int


def min_resolving_count(verts: list[tuple[int, int, int]], s_list: list[tuple[int, int, int]]) -> tuple[int, tuple]:
    min_cnt = len(s_list) + 1
    min_pair = None
    for u, v in combinations(verts, 2):
        cnt = sum(1 for z in s_list if dist(z, u) != dist(z, v))
        if cnt < min_cnt:
            min_cnt = cnt
            min_pair = (u, v)
        if dist(u, v) % 2 == 1:
            assert cnt == len(s_list)
    assert min_pair is not None
    return min_cnt, min_pair


def main() -> None:
    verify_bfs_matches_l1(3, 3, 4)
    print("BFS == L1 distance on P_3 x P_3 x P_4: OK")

    # Primary counterexample: (3, 3, 4, 13)
    verts_334 = grid_vertices(3, 3, 4)
    am = alpha_m(3, 3, 4)
    aM = alpha_M(3, 3, 4)
    assert am == 12 and aM == 15 and am <= 13 < aM
    conj = conjectured_dim(3, 3, 4, 13)
    assert conj == 32

    s_334, fe_334, fi_334 = build_witness(3, 3, 4)
    assert len(fe_334) == 24 and len(fi_334) == 6 and len(s_334) == 30
    expected_M = {(0, 1, 2), (2, 1, 2), (1, 0, 2), (1, 2, 2), (1, 1, 1), (1, 1, 2)}
    assert set(verts_334) - s_334 == expected_M

    min_c, min_p = min_resolving_count(verts_334, sorted(s_334))
    assert min_c == 14, f"Expected min resolving count 14, got {min_c}"
    # Verify explicit attainment at (0,0,1), (0,1,0)
    u0, v0 = (0, 0, 1), (0, 1, 0)
    c_edge = sum(1 for z in fe_334 if dist(z, u0) != dist(z, v0))
    c_int = sum(1 for z in fi_334 if dist(z, u0) != dist(z, v0))
    assert c_edge == 12 and c_int == 2 and c_edge + c_int == 14
    assert len(s_334) < conj
    print(f"(3,3,4,13): alpha_m={am} <= 13 < alpha_M={aM}, |S|={len(s_334)} < conj={conj}, min_res={min_c} >= 14 (min pair {min_p}): OK")

    # Further counterexamples: (3,3,5,15), (3,4,4,15), (4,4,4,17)
    extras = [
        (3, 3, 5, 15, 14, 18, 34, 36),
        (3, 4, 4, 15, 14, 18, 34, 36),
        (4, 4, 4, 17, 16, 24, 38, 40),
    ]
    for n1, n2, n3, k, exp_am, exp_aM, exp_s, exp_conj in extras:
        am_v = alpha_m(n1, n2, n3)
        aM_v = alpha_M(n1, n2, n3)
        assert am_v == exp_am and aM_v == exp_aM and am_v <= k < aM_v
        conj_v = conjectured_dim(n1, n2, n3, k)
        assert conj_v == exp_conj
        s_v, _, _ = build_witness(n1, n2, n3)
        assert len(s_v) == exp_s and len(s_v) == 2 * am_v + 6
        verts_v = grid_vertices(n1, n2, n3)
        mc, _ = min_resolving_count(verts_v, sorted(s_v))
        assert mc >= k + 1, f"Failed (k+1)-resolving at {(n1,n2,n3,k)}: min_res={mc}"
        assert len(s_v) < conj_v
        print(f"{(n1,n2,n3,k)}: alpha_m={am_v} <= {k} < alpha_M={aM_v}, |S|={len(s_v)} < conj={conj_v}, min_res={mc} >= {k+1}: OK")

    print("PASS")


if __name__ == "__main__":
    main()
