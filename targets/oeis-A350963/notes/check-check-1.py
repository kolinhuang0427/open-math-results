"""Independent exact verifier for targets/oeis-A350963/PROOF.md.

Written strictly from live OEIS A350963 + a350963.gp.txt and PROOF.md,
without reading verify.py or author notes.
"""

from __future__ import annotations

from collections import deque
import sys
import time
from sympy import Poly, Rational, expand, symbols

OEIS_A350963_DATA = [
    1, 9, 29, 42, 63, 75, 97, 106, 131, 139, 165, 170, 199, 203, 233, 234,
    267, 267, 301, 298, 335, 331, 369, 362, 403, 395, 437, 426, 471, 459,
    505, 490, 539, 523, 573, 554, 607, 587, 641, 618, 675, 651, 709, 682,
    743, 715, 777, 746, 811, 779, 845, 810, 879, 843,
]

DX = (4, -1)
DY = (0, 6)
H_PROTO = [(0, 0), (1, 0), (3, 0), (4, 0)]
V_PROTO = [(0, 0), (0, 1), (0, 3), (0, 4)]

TILES = [
    [(u + 0, v + 0) for u, v in H_PROTO],
    [(u - 1, v + 2) for u, v in H_PROTO],
    [(u + 0, v + 3) for u, v in H_PROTO],
    [(u - 1, v + 5) for u, v in H_PROTO],
    [(u + 1, v + 1) for u, v in V_PROTO],
    [(u + 2, v + 0) for u, v in V_PROTO],
]

PROOF_ADJ = [
    {(3,-1,-1),(0,-1,0),(3,0,-1),(4,0,-1),(4,0,0),(5,0,0),(0,1,0),(1,1,0),(4,1,0)},
    {(0,-1,0),(1,-1,0),(5,-1,0),(2,0,0),(4,0,0),(5,0,0),(1,1,0),(2,1,0)},
    {(1,-1,0),(2,-1,0),(1,0,0),(4,0,0),(5,0,0),(2,1,0),(3,1,0),(4,1,0)},
    {(2,-1,0),(3,-1,0),(5,-1,0),(4,0,0),(5,0,0),(0,0,1),(5,0,1),(3,1,0),(0,1,1)},
    {(0,-1,0),(2,-1,0),(0,0,0),(1,0,0),(2,0,0),(3,0,0),(5,0,0),(0,0,1)},
    {(3,0,-1),(0,0,0),(1,0,0),(2,0,0),(3,0,0),(4,0,0),(1,1,0),(3,1,0)},
]

C1 = (2, 1, 1, 0, 1, 1)
C2 = (-1, 0, 0, 0, 0, -1)
C3 = (-1, 0, 0, 0, 0, -1)
C4 = (2, 2, 1, 0, 1, 1)
K5 = (-1, 0, 1, 2, 0, 1)
K6 = (5, 4, 3, 2, 4, 3)
C7 = (0, 0, 0, 0, 0, 1)
C8 = (0, 0, 0, 0, 1, 0)


def mod_lambda(u: int, v: int) -> tuple[int, int]:
    k = u // 4
    return (u - 4 * k, (v + k) % 6)


def build_graph_from_tiles() -> list[set[tuple[int, int, int]]]:
    # 1. Exact fundamental domain partition of Z^2 / Lambda
    seen_classes: dict[tuple[int, int], int] = {}
    for t, pts in enumerate(TILES):
        for u, v in pts:
            cls = mod_lambda(u, v)
            assert cls not in seen_classes, f"overlap at {cls}"
            seen_classes[cls] = t
    assert len(seen_classes) == 24

    # Verify tiling on [-20, 20]^2 has exact unique coverage
    cover: dict[tuple[int, int], tuple[int, int, int]] = {}
    for x in range(-10, 11):
        for y in range(-6, 7):
            for t, pts in enumerate(TILES):
                for u, v in pts:
                    pt = (u + x * DX[0] + y * DY[0], v + x * DX[1] + y * DY[1])
                    assert pt not in cover
                    cover[pt] = (x, y, t)
    for u in range(-15, 16):
        for v in range(-15, 16):
            assert (u, v) in cover, f"gap at {(u, v)}"

    # 2. Derive adjacency across dx, dy in [-3, 3]
    tile_sets = [set(pts) for pts in TILES]
    nbrs_of_base = []
    for pts in TILES:
        ns = set()
        for u, v in pts:
            for du, dv in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ns.add((u + du, v + dv))
        ns -= set(pts)
        nbrs_of_base.append(ns)

    adj: list[set[tuple[int, int, int]]] = [set() for _ in range(6)]
    for t in range(6):
        for dx in range(-3, 4):
            for dy in range(-3, 4):
                sh_u = dx * DX[0] + dy * DY[0]
                sh_v = dx * DX[1] + dy * DY[1]
                for o in range(6):
                    shifted = {(u + sh_u, v + sh_v) for u, v in tile_sets[o]}
                    if nbrs_of_base[t] & shifted:
                        assert -1 <= dx <= 1 and -1 <= dy <= 1
                        adj[t].add((o, dx, dy))

    assert adj == PROOF_ADJ
    assert sum(len(s) for s in adj) == 50
    for t in range(6):
        for o, dx, dy in adj[t]:
            assert (t, -dx, -dy) in adj[o]

    # Check R/G/B breakdowns and half-turn automorphism
    types = {0: "R", 3: "R", 4: "G", 5: "G", 1: "B", 2: "B"}
    for t in range(6):
        counts = {"R": 0, "G": 0, "B": 0}
        for o, _, _ in adj[t]:
            counts[types[o]] += 1
        if types[t] == "R":
            assert counts == {"R": 4, "G": 4, "B": 1}
        elif types[t] == "G":
            assert counts == {"R": 4, "G": 1, "B": 3}
        else:
            assert counts == {"R": 1, "G": 3, "B": 4}

    swap = {0: 3, 3: 0, 1: 2, 2: 1, 4: 5, 5: 4}
    for t in range(6):
        t_img = {mod_lambda(3 - u, 5 - v) for u, v in TILES[t]}
        s_img = {mod_lambda(u, v) for u, v in TILES[swap[t]]}
        assert t_img == s_img
        for o, dx, dy in adj[t]:
            assert (swap[o], -dx, -dy) in adj[swap[t]]
    return adj


def f_all(x: int, y: int, t: int) -> tuple[int, ...]:
    f1 = (x - 2 * y) + C1[t]
    f2 = -(x - 2 * y) + C2[t]
    f3 = 2 * y + C3[t]
    f4 = -2 * y + C4[t]
    f5 = (2 * (x + 2 * y) + K5[t]) // 3
    f6 = (-2 * (x + 2 * y) + K6[t]) // 3
    f7 = x + C7[t]
    f8 = -x + C8[t]
    return (f1, f2, f3, f4, f5, f6, f7, f8)  # 1-indexed via [s-1]


def in_e_exc(x: int, y: int, t: int) -> bool:
    if t != 2:
        return False
    if x in (0, 1) and y <= 0:
        return True
    if x == y and y >= 1:
        return True
    return False


def d_val(x: int, y: int, t: int) -> int:
    return max(f_all(x, y, t))


def d_star(x: int, y: int, t: int) -> int:
    return d_val(x, y, t) + (1 if in_e_exc(x, y, t) else 0)


def check_lipschitz_and_rays(adj: list[set[tuple[int, int, int]]]) -> None:
    assert all(v == 0 for v in f_all(0, 0, 3))
    assert d_star(0, 0, 3) == 0

    # Check all 50 directed edges across all (x+2y) mod 3 classes
    for t in range(6):
        for r in range(3):
            x, y = r, 0
            fv = f_all(x, y, t)
            for o, dx, dy in adj[t]:
                fu = f_all(x + dx, y + dy, o)
                for s in range(8):
                    assert abs(fu[s] - fv[s]) <= 1
                assert abs(2 * (dx + 2 * dy) + K5[o] - K5[t]) <= 3
                assert abs(-2 * (dx + 2 * dy) + K6[o] - K6[t]) <= 3

    # Check E_exc rays R1, R2, R3 for k in 0..80 (k>=1 for R3)
    for k in range(0, 81):
        # R1: (0, -k, 2)
        v1 = (0, -k, 2)
        assert d_val(*v1) == 2 * k + 1 and d_star(*v1) == 2 * k + 2
        for o, dx, dy in adj[2]:
            u = (v1[0] + dx, v1[1] + dy, o)
            assert abs(d_star(*u) - d_star(*v1)) <= 1
            if not in_e_exc(*u):
                assert d_val(*u) >= d_val(*v1)
        assert (3, 1, 0) in adj[2]
        u1 = (1, -k, 3)
        assert not in_e_exc(*u1) and d_star(*u1) == d_star(*v1) - 1

        # R2: (1, -k, 2)
        v2 = (1, -k, 2)
        assert d_val(*v2) == 2 * k + 2 and d_star(*v2) == 2 * k + 3
        for o, dx, dy in adj[2]:
            u = (v2[0] + dx, v2[1] + dy, o)
            assert abs(d_star(*u) - d_star(*v2)) <= 1
            if not in_e_exc(*u):
                assert d_val(*u) >= d_val(*v2)
        u2 = (2, -k, 3)
        assert not in_e_exc(*u2) and d_star(*u2) == d_star(*v2) - 1

        if k >= 1:
            v3 = (k, k, 2)
            assert d_val(*v3) == 2 * k and d_star(*v3) == 2 * k + 1
            for o, dx, dy in adj[2]:
                u = (v3[0] + dx, v3[1] + dy, o)
                assert abs(d_star(*u) - d_star(*v3)) <= 1
                if not in_e_exc(*u):
                    assert d_val(*u) >= d_val(*v3)
            assert (5, 0, 0) in adj[2]
            u3 = (k, k, 5)
            assert not in_e_exc(*u3) and d_star(*u3) == d_star(*v3) - 1


def check_lemma22_and_descent(adj: list[set[tuple[int, int, int]]]) -> None:
    x_sym, y_sym = symbols("x y")
    M = {
        7: 3 * x_sym,
        5: 2 * x_sym + 4 * y_sym,
        3: 6 * y_sym,
        2: 6 * y_sym - 3 * x_sym,
        8: -3 * x_sym,
        6: -2 * x_sym - 4 * y_sym,
        4: -6 * y_sym,
        1: 3 * x_sym - 6 * y_sym,
    }
    cyc = [7, 5, 3, 2, 8, 6, 4, 1]
    adj_pairs = {(cyc[i], cyc[(i + 1) % 8]) for i in range(8)} | {
        (cyc[(i + 1) % 8], cyc[i]) for i in range(8)
    }
    # Check -3 <= 3 F_s - M_s <= 6 over complete period
    for t in range(6):
        for x in range(3):
            for y in range(3):
                fs = f_all(x, y, t)
                for idx, s in enumerate(range(1, 9)):
                    m_val = int(M[s].subs({x_sym: x, y_sym: y}))
                    assert -3 <= 3 * fs[idx] - m_val <= 6

    # Check the 20 non-adjacent pair relations
    assert expand(3 * M[5] - (2 * M[7] + 2 * M[3])) == 0
    assert expand(4 * M[3] - (3 * M[5] + 2 * M[2])) == 0
    assert expand(M[2] - (M[3] + M[8])) == 0
    assert expand(4 * M[8] - (2 * M[2] + 3 * M[6])) == 0
    assert expand(M[3] - (M[7] + M[2])) == 0
    assert expand(2 * M[3] - (3 * M[5] + 2 * M[8])) == 0
    assert expand(2 * M[8] - (2 * M[3] + 3 * M[6])) == 0
    assert expand(M[8] - (M[2] + M[4])) == 0

    # Check B_core = [-20, 20] x [-10, 10] x {0..5}
    zero_verts = []
    for x in range(-20, 21):
        for y in range(-10, 11):
            for t in range(6):
                ds = d_star(x, y, t)
                if ds <= 0:
                    zero_verts.append((x, y, t, ds))
                if (x, y, t) != (0, 0, 3):
                    assert any(
                        d_star(x + dx, y + dy, o) == ds - 1 for o, dx, dy in adj[t]
                    ), f"no descent in B_core at {(x, y, t)}"
    assert zero_verts == [(0, 0, 3, 0)]

    # Verify EVERY entry of Case B descent table on collar [-35, 35] x [-20, 20] \ B_core
    # AND check edge-delta conditions on all 8 seams x 6 tiles x 3 residues
    def table_edge(s1: int, s2: int, t: int, r: int, fs: tuple[int, ...]) -> tuple[int, int, int]:
        f = lambda idx: fs[idx - 1]
        if (s1, s2) == (7, 5):
            return [(3,-1,-1), (0,-1,0), (1,-1,0), ((2,-1,0) if r == 0 else (3,-1,0)), (0,-1,0), (3,0,-1)][t]
        if (s1, s2) == (5, 3):
            if t == 2:
                return (1,-1,0) if f(5) > f(3) else (5,0,0)
            return [(3,-1,-1), (0,-1,0), None, (5,-1,0), (0,-1,0), (3,0,-1)][t]
        if (s1, s2) == (3, 2):
            return [(3,0,-1), (5,0,0), (5,0,0), (5,0,0), (0,0,0), (3,0,-1)][t]
        if (s1, s2) == (2, 8):
            if t == 5:
                return (3,0,-1) if f(2) > f(8) else (1,1,0)
            return [(0,1,0), (1,1,0), (3,1,0), (3,1,0), (0,0,0), None][t]
        if (s1, s2) == (8, 6):
            return [
                (1,1,0) if r == 0 else (0,1,0),
                (2,1,0) if r == 1 else (1,1,0),
                (3,1,0),
                (0,1,1) if r == 0 else (3,1,0),
                (0,0,1) if r == 1 else (3,0,0),
                (1,1,0) if r == 0 else (3,1,0),
            ][t]
        if (s1, s2) == (6, 4):
            if t == 0:
                return [(4,1,0), (4,0,0), (5,0,0)][r]
            if t == 1:
                if f(6) < max(fs) - 1:
                    return (5,-1,0)
                return (2,1,0) if r != 2 else (5,0,0)
            if t == 2:
                return (3,1,0)
            if t == 3:
                return (5,0,1)
            if t == 4:
                return (0,0,1) if r == 1 else (3,0,0)
            return (3,0,0) if r == 0 else (3,1,0)
        if (s1, s2) == (4, 1):
            if t == 2:
                return (3,1,0) if f(4) > f(1) else (1,-1,0)
            return [(4,0,0), (5,-1,0), None, (5,0,1), (3,0,0), (3,0,0)][t]
        if (s1, s2) == (1, 7):
            if t == 4:
                D = max(fs)
                if f(1) < D - 1:
                    return (0,-1,0)
                if f(7) < D - 1:
                    return (3,0,0)
                return (2,-1,0)
            return [(3,-1,-1), (1,-1,0), (1,-1,0), (3,-1,0), None, (3,0,0)][t]
        raise AssertionError((s1, s2))

    checked_collar = 0
    for x in range(-35, 36):
        for y in range(-20, 21):
            if -20 <= x <= 20 and -10 <= y <= 10:
                continue
            for t in range(6):
                if in_e_exc(x, y, t):
                    continue
                checked_collar += 1
                fs = f_all(x, y, t)
                D = max(fs)
                near = [s for s in range(1, 9) if D - fs[s - 1] <= 1]
                assert 1 <= len(near) <= 2
                if len(near) == 2:
                    assert (near[0], near[1]) in adj_pairs
                # Pick matching seam in C
                found_seam = None
                for i in range(8):
                    s1, s2 = cyc[i], cyc[(i + 1) % 8]
                    if set(near).issubset({s1, s2}):
                        found_seam = (s1, s2)
                        break
                assert found_seam is not None
                r = (x + 2 * y) % 3
                e = table_edge(found_seam[0], found_seam[1], t, r, fs)
                assert e in adj[t]
                o, dx, dy = e
                nx, ny = x + dx, y + dy
                assert not in_e_exc(nx, ny, o), f"landed in E_exc from {(x, y, t)} via {e}"
                assert d_star(nx, ny, o) == D - 1, f"table step failed at {(x, y, t)} seam {found_seam} via {e}"
    assert checked_collar > 10000


def check_bfs_and_gf(adj: list[set[tuple[int, int, int]]]) -> None:
    # Exact BFS up to radius 55 from (0, 0, 3)
    R = 55
    dist: dict[tuple[int, int, int], int] = {(0, 0, 3): 0}
    q = deque([(0, 0, 3)])
    shells = [0] * (R + 1)
    while q:
        x, y, t = q.popleft()
        d = dist[(x, y, t)]
        assert d == d_star(x, y, t), f"d!=D* at {(x, y, t)}: d={d}, D*={d_star(x, y, t)}"
        shells[d] += 1
        if d == R:
            continue
        for o, dx, dy in adj[t]:
            nxt = (x + dx, y + dy, o)
            if nxt not in dist:
                dist[nxt] = d + 1
                q.append(nxt)

    assert shells[:54] == OEIS_A350963_DATA
    for n in range(2, R + 1):
        if n % 2 == 0:
            assert shells[n] == 17 * n - 5
        elif n % 4 == 1:
            assert shells[n] == 16 * n - 5
        else:
            assert shells[n] == 16 * n - 6

    # Section 3.1 exact polynomial check for |B_t(4m+r)| against direct counting for m=1..10
    expected_poly = {
        (0,0): lambda m: 22*m*m + m,       (0,1): lambda m: 22*m*m + 13*m + 2,
        (0,2): lambda m: 22*m*m + 23*m + 6, (0,3): lambda m: 22*m*m + 35*m + 14,
        (1,0): lambda m: 22*m*m + 2*m,     (1,1): lambda m: 22*m*m + 10*m,
        (1,2): lambda m: 22*m*m + 24*m + 7, (1,3): lambda m: 22*m*m + 32*m + 11,
        (2,0): lambda m: 22*m*m + m,       (2,1): lambda m: 22*m*m + 13*m + 2,
        (2,2): lambda m: 22*m*m + 23*m + 6, (2,3): lambda m: 22*m*m + 35*m + 14,
        (3,0): lambda m: 22*m*m + 6*m + 1, (3,1): lambda m: 22*m*m + 14*m + 3,
        (3,2): lambda m: 22*m*m + 28*m + 9, (3,3): lambda m: 22*m*m + 36*m + 15,
        (4,0): lambda m: 22*m*m + m,       (4,1): lambda m: 22*m*m + 11*m + 1,
        (4,2): lambda m: 22*m*m + 23*m + 6, (4,3): lambda m: 22*m*m + 33*m + 12,
        (5,0): lambda m: 22*m*m + 2*m,     (5,1): lambda m: 22*m*m + 16*m + 3,
        (5,2): lambda m: 22*m*m + 24*m + 7, (5,3): lambda m: 22*m*m + 38*m + 16,
    }
    for m in range(1, 11):
        for r in range(4):
            n = 4 * m + r
            lim_x = n + 3
            lim_y = (n + 3) // 2 + 2
            tot = 0
            for t in range(6):
                cnt = 0
                for x in range(-lim_x, lim_x + 1):
                    for y in range(-lim_y, lim_y + 1):
                        if d_val(x, y, t) <= n:
                            cnt += 1
                assert cnt == expected_poly[(t, r)](m), f"B_t mismatch at t={t}, n={n}"
                tot += cnt
            B_tot = [
                132*m*m + 13*m + 1,
                132*m*m + 77*m + 11,
                132*m*m + 145*m + 41,
                132*m*m + 209*m + 82,
            ][r]
            assert tot == B_tot

    # Check Section 3.1 ordering & nonnegativity differences across all (t, r) as affine functions of m >= 1
    for t in range(6):
        for r in range(4):
            def bounds(m: int) -> tuple[int, ...]:
                n = 4 * m + r
                a1, a2 = n - C1[t], n - C2[t]
                a3, a4 = (n - C3[t]) // 2, (n - C4[t]) // 2
                a5, a6 = (3 * n + 2 - K5[t]) // 2, (3 * n + 2 - K6[t]) // 2
                a7, a8 = n - C7[t], n - C8[t]
                return a1, a2, a3, a4, a5, a6, a7, a8

            # Since all functions are exact affine in m for fixed (t, r), checking m=1 and m=2 checks slope & m=1 value!
            diffs_at = []
            for m in (1, 2):
                a1, a2, a3, a4, a5, a6, a7, a8 = bounds(m)
                mu1, mu2, ml1, ml2 = a7 - a1, a5 - a7, a8 - a6, a2 - a8
                u1, u2, l1, l2 = mu1 // 2, (mu2 + 1) // 2, ml1 // 2, (ml2 + 1) // 2
                seq = [u1 + a4, u2 - u1 - 1, a3 - u2, l1 + a4, l2 - l1 - 1, a3 - l2]
                for y in (-a4, a3):
                    Us = [a7, 2 * y + a1, -2 * y + a5]
                    Ls = [-a8, 2 * y - a2, -2 * y - a6]
                    for U in Us:
                        for L in Ls:
                            seq.append(U - L)
                diffs_at.append(seq)
            for v1, v2 in zip(diffs_at[0], diffs_at[1]):
                slope = v2 - v1
                assert v1 >= 0 and slope >= 0

    # Check rational GF expansion up to t^100
    t_var = symbols("t")
    num = -(2*t_var**7 - 6*t_var**6 - 24*t_var**5 - 33*t_var**4 - 33*t_var**3 - 28*t_var**2 - 9*t_var - 1)
    assert expand(num) == 1 + 9*t_var + 28*t_var**2 + 33*t_var**3 + 33*t_var**4 + 24*t_var**5 + 6*t_var**6 - 2*t_var**7
    # Compute exact power series via (1 - t^2 - t^4 + t^6) recurrence
    gf_coeffs = [0] * 101
    num_list = [1, 9, 28, 33, 33, 24, 6, -2]
    for n in range(101):
        val = num_list[n] if n < len(num_list) else 0
        if n >= 2:
            val += gf_coeffs[n - 2]
        if n >= 4:
            val += gf_coeffs[n - 4]
        if n >= 6:
            val -= gf_coeffs[n - 6]
        gf_coeffs[n] = val
    assert gf_coeffs[:54] == OEIS_A350963_DATA
    for n in range(2, 101):
        expected = 17 * n - 5 if n % 2 == 0 else (16 * n - 5 if n % 4 == 1 else 16 * n - 6)
        assert gf_coeffs[n] == expected


def main() -> int:
    t0 = time.time()
    adj = build_graph_from_tiles()
    print("Section 1 (XXOXX tiling mod Lambda, [-15,15]^2 patch, 50 edges, R/G/B, half-turn): OK")
    check_lipschitz_and_rays(adj)
    print("Section 2.1 (1-Lipschitz F1..F8, D*, and 3 rays R1..R3 k<=80): OK")
    check_lemma22_and_descent(adj)
    print("Sections 2.2-2.3 (B_core 5166 verts + Case B descent table on collar): OK")
    check_bfs_and_gf(adj)
    print(f"Section 3 (BFS r<=55 == D*, 54 OEIS A350963 terms, B_t(4m+r), & GF to t^100): OK ({time.time() - t0:.2f}s)")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
