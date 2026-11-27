#!/usr/bin/env python3
"""Independent exact verifier for targets/caro-2312.08777-prob7/.

Written directly from the primary source arXiv:2312.08777v1 (sections/section1.tex,
sections/section6.tex, sections/section7.tex) and PROOF.md without reading verify.py.
Uses zero floating-point arithmetic (pure int and fractions.Fraction).
"""

from collections import deque
from fractions import Fraction
import pathlib
import random

ROOT = pathlib.Path(__file__).resolve().parents[3]
SRC_DIR = ROOT / "tools/.arxiv_cache/eprint/2312.08777/sections"
TARGET_MD = ROOT / "targets/caro-2312.08777-prob7/TARGET.md"
PROOF_MD = ROOT / "targets/caro-2312.08777-prob7/PROOF.md"


def check_primary_source() -> None:
    if not SRC_DIR.exists():
        print("[SKIP] local tools/.arxiv_cache not present; skipping TeX snippet check")
        return
    sec1 = (SRC_DIR / "section1.tex").read_text()
    sec6 = (SRC_DIR / "section6.tex").read_text()
    sec7 = (SRC_DIR / "section7.tex").read_text()
    target = TARGET_MD.read_text()
    proof = PROOF_MD.read_text()

    # Verify exact definitions in section1.tex & section6.tex
    assert "a strictly increasing positive integer sequence $(a_1, \\dots, a_k)$" in sec1
    assert "$e_{j, t} [v] = \\left|E(j) \\cap E\\left(N_t [v]\\right)\\right|$" in sec6
    assert "resulting in a $([t], (a_1, \\dots, a_k))$-flip graph" in sec6
    assert "\\label{ErdosSachs}" in sec6

    # Verify exact Problem statement in section7.tex matches TARGET.md verbatim
    q_prob = (
        "define $b(t) = \\min\\left\\{ b \\colon ([t], (b, r))\\mathrm{-flip} \\ \\mathrm{graph} \\ \\mathrm{exists}\\right\\}$. Observe that for $t \\geq 2$,\n"
        "the proof of Theorem \\ref{CayleyTFlip} gives $b(t) \\leq 2^{t+1} - 1$.\n\n"
        "\\begin{problem*}\n"
        "For $t \\in \\mathbb{N}, t \\geq 2$ determine $b(t)$.\n"
        "\\end{problem*}"
    )
    assert q_prob in sec7
    # TARGET.md joins the two lines of the paragraph cleanly
    assert "define $b(t) = \\min\\left\\{ b \\colon ([t], (b, r))\\mathrm{-flip} \\ \\mathrm{graph} \\ \\mathrm{exists}\\right\\}$. Observe that for $t \\geq 2$, the proof of Theorem \\ref{CayleyTFlip} gives $b(t) \\leq 2^{t+1} - 1$." in target
    assert "For $t \\in \\mathbb{N}, t \\geq 2$ determine $b(t)$." in target
    assert "b(t) = 3" in proof

    print("[PASS] Primary source arXiv:2312.08777v1 verbatim statement & definitions verified.")


def verify_triangle_identity_on_graph(n: int, blue_edges: list[tuple[int, int]], red_edges: list[tuple[int, int]]) -> None:
    """Independently compute e_{1,1}[v], e_{2,1}[v], e_B(v), e_R(v), T_XYZ(v) and verify Section 1 identities."""
    adj_b = [set() for _ in range(n)]
    adj_r = [set() for _ in range(n)]
    for u, v in blue_edges:
        assert u != v and v not in adj_b[u] and v not in adj_r[u]
        adj_b[u].add(v)
        adj_b[v].add(u)
    for u, v in red_edges:
        assert u != v and v not in adj_r[u] and v not in adj_b[u]
        adj_r[u].add(v)
        adj_r[v].add(u)

    sum_diff = 0
    sum_bound_terms = 0
    sum_t_bbr = 0
    sum_t_brb = 0
    sum_t_rrb = 0
    sum_t_brr = 0

    for v in range(n):
        nb_b = adj_b[v]
        nb_r = adj_r[v]
        nb = nb_b | nb_r
        # Closed 1-neighbourhood edge counts directly from definition E(j) cap E(N_1[v])
        closed = nb | {v}
        e_11 = sum(1 for u, w in blue_edges if u in closed and w in closed)
        e_21 = sum(1 for u, w in red_edges if u in closed and w in closed)
        e_b = sum(1 for u, w in blue_edges if u in nb and w in nb)
        e_r = sum(1 for u, w in red_edges if u in nb and w in nb)
        assert e_11 == len(nb_b) + e_b
        assert e_21 == len(nb_r) + e_r

        t_bbb = t_brb = t_rrb = t_rrr = t_bbr = t_brr = 0
        for u, w in blue_edges:
            if u in nb and w in nb:
                u_b, w_b = u in nb_b, w in nb_b
                if u_b and w_b:
                    t_bbb += 1
                elif not u_b and not w_b:
                    t_rrb += 1
                else:
                    t_brb += 1
        for u, w in red_edges:
            if u in nb and w in nb:
                u_b, w_b = u in nb_b, w in nb_b
                if u_b and w_b:
                    t_bbr += 1
                elif not u_b and not w_b:
                    t_rrr += 1
                else:
                    t_brr += 1

        assert e_b == t_bbb + t_brb + t_rrb
        assert e_r == t_rrr + t_bbr + t_brr
        b_deg = len(nb_b)
        assert t_bbb + t_bbr <= b_deg * (b_deg - 1) // 2

        sum_diff += e_b - e_r
        sum_bound_terms += t_bbb + t_bbr - t_rrb - t_rrr
        sum_t_bbr += t_bbr
        sum_t_brb += t_brb
        sum_t_rrb += t_rrb
        sum_t_brr += t_brr

    assert 2 * sum_t_rrb == sum_t_brr
    assert 2 * sum_t_bbr == sum_t_brb
    assert sum_diff == sum_bound_terms


def check_lower_bound() -> None:
    # Exact algebraic elimination for b = 1, 2
    for b in (1, 2):
        # Upper bound from r - b < binom(b, 2) => r <= b + binom(b,2) - 1 = binom(b+1,2) - 1
        max_r = b * (b + 1) // 2 - 1
        assert max_r < b + 1, f"Expected contradiction for b={b}, got max_r={max_r}"

    # Verify triangle identities on explicit edge-coloured regular graphs (b=1, b=2, b=3)
    # 1) K4 with 1-regular blue (matching) and 2-regular red (C4)
    verify_triangle_identity_on_graph(
        4, [(0, 2), (1, 3)], [(0, 1), (1, 2), (2, 3), (3, 0)]
    )
    # 2) K5 with C5 blue (b=2) and C5 red (r=2)
    verify_triangle_identity_on_graph(
        5,
        [(i, (i + 1) % 5) for i in range(5)],
        [(i, (i + 2) % 5) for i in range(5)],
    )
    # 3) K6 with 2-regular blue (2 disjoint K3s) and 3-regular red (K_{3,3})
    verify_triangle_identity_on_graph(
        6,
        [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5)],
        [(i, j) for i in (0, 1, 2) for j in (3, 4, 5)],
    )
    # 4) K7 with b=2 (C7) and r=4 (remaining edges)
    verify_triangle_identity_on_graph(
        7,
        [(i, (i + 1) % 7) for i in range(7)],
        [(i, (i + 2) % 7) for i in range(7)] + [(i, (i + 3) % 7) for i in range(7)],
    )
    print("[PASS] Lower bound b(t) >= 3 algebra & triangle identities verified.")


def check_recurrence_exact(max_t: int = 200) -> None:
    """Exact integer verification of A_s, B_s, e_{1,s}[v], e_{2,s}[v] for 1 <= s <= max_t."""
    a_prev = 0
    a_s = 4
    b_s = 3
    e1 = 6
    e2 = 4
    assert e1 > e2

    for s in range(1, max_t):
        a_next = 3 * a_s + 4 * b_s
        b_next = 3 * a_s
        e1_next = e1 + 6 * a_s
        e2_next = e2 + 3 * a_s + 4 * b_s

        if s >= 2:
            # 5 A_{s-1} <= A_s <= 6 A_{s-1}
            assert 5 * a_prev <= a_s <= 6 * a_prev
            # 5 A_s <= A_{s+1} < 6 A_s
            assert 5 * a_s <= a_next < 6 * a_s
            # Delta e1 - Delta e2 = 3 A_s - 12 A_{s-1} >= 3 A_{s-1} > 0
            delta_diff = (e1_next - e1) - (e2_next - e2)
            assert delta_diff == 3 * a_s - 12 * a_prev >= 3 * a_prev > 0
            # Exact rational check of PROOF.md bounds: A_{s-1} >= 1/6 A_s and <= 1/5 A_s
            assert Fraction(a_prev) >= Fraction(1, 6) * a_s
            assert Fraction(a_prev) <= Fraction(1, 5) * a_s

        assert e1_next > e2_next
        a_prev, a_s, b_s = a_s, a_next, b_next
        e1, e2 = e1_next, e2_next

    print(f"[PASS] Layer recurrence & e_{{1,s}} > e_{{2,s}} verified in exact ints for 1 <= s <= {max_t}.")


def build_k4_blowup(adj_h: list[list[int]], seed: int = 0) -> tuple[list[list[int]], list[list[int]]]:
    """Construct G = H lift by K_4 cliques (blue = 1 inside C_x, red = 2 between C_x)."""
    rng = random.Random(seed)
    n_h = len(adj_h)
    n_g = 4 * n_h
    blue = [[] for _ in range(n_g)]
    red = [[] for _ in range(n_g)]

    # Blue K_4 on each clique C_x = {4x, 4x+1, 4x+2, 4x+3}
    for x in range(n_h):
        base = 4 * x
        for i in range(4):
            for j in range(4):
                if i != j:
                    blue[base + i].append(base + j)

    # Partition incident edges of each x into 4 parts of size 4
    slot_for_edge: dict[tuple[int, int], int] = {}
    for x in range(n_h):
        nbrs = list(adj_h[x])
        assert len(nbrs) == 16
        rng.shuffle(nbrs)
        for idx, y in enumerate(nbrs):
            slot_for_edge[(x, y)] = idx // 4

    for x in range(n_h):
        for y in adj_h[x]:
            if x < y:
                u = 4 * x + slot_for_edge[(x, y)]
                v = 4 * y + slot_for_edge[(y, x)]
                red[u].append(v)
                red[v].append(u)

    return blue, red


def verify_flip_graph(
    adj_h: list[list[int]],
    blue: list[list[int]],
    red: list[list[int]],
    t: int,
    sample_vertices: list[int] | None = None,
) -> None:
    """Verify G is simple, (3,4)-regular, and satisfies exact layer counts & e_{1,s}[v] > e_{2,s}[v] for 1<=s<=t."""
    n_g = len(blue)
    assert n_g == 4 * len(adj_h)
    for v in range(n_g):
        assert len(blue[v]) == 3 and len(red[v]) == 4
        bset = set(blue[v])
        rset = set(red[v])
        assert len(bset) == 3 and len(rset) == 4
        assert v not in bset and v not in rset and bset.isdisjoint(rset)

    # Expected counts from recurrence
    exp_e1 = [0]
    exp_e2 = [0]
    exp_layer = [1]
    a_s, b_s = 4, 3
    e1, e2 = 6, 4
    for s in range(1, t + 1):
        exp_e1.append(e1)
        exp_e2.append(e2)
        exp_layer.append(a_s + b_s)
        a_next = 3 * a_s + 4 * b_s
        b_next = 3 * a_s
        e1 += 6 * a_s
        e2 += 3 * a_s + 4 * b_s
        a_s, b_s = a_next, b_next

    verts = range(n_g) if sample_vertices is None else sample_vertices
    for v in verts:
        dist = {v: 0}
        q = deque([v])
        layers = [[] for _ in range(t + 1)]
        layers[0].append(v)
        while q:
            u = q.popleft()
            d = dist[u]
            if d == t:
                continue
            for w in blue[u]:
                if w not in dist:
                    dist[w] = d + 1
                    layers[d + 1].append(w)
                    q.append(w)
            for w in red[u]:
                if w not in dist:
                    dist[w] = d + 1
                    layers[d + 1].append(w)
                    q.append(w)

        closed_set = set()
        for s in range(0, t + 1):
            assert len(layers[s]) == exp_layer[s]
            closed_set.update(layers[s])
            if s >= 1:
                # Count edges inside closed_set directly from definition
                cnt1 = sum(1 for u in closed_set for w in blue[u] if u < w and w in closed_set)
                cnt2 = sum(1 for u in closed_set for w in red[u] if u < w and w in closed_set)
                assert cnt1 == exp_e1[s]
                assert cnt2 == exp_e2[s]
                assert cnt1 > cnt2


def f16_mul_table() -> tuple[list[list[int]], list[list[int]]]:
    """Build exact addition & multiplication tables for GF(16) = GF(2)[x]/(x^4 + x + 1)."""
    add = [[a ^ b for b in range(16)] for a in range(16)]
    mul = [[0] * 16 for _ in range(16)]
    for a in range(16):
        for b in range(16):
            res = 0
            aa, bb = a, b
            for _ in range(4):
                if bb & 1:
                    res ^= aa
                hi = aa & 8
                aa = (aa << 1) & 15
                if hi:
                    aa ^= 0b0011  # x^4 = x + 1
                bb >>= 1
            mul[a][b] = res
    return add, mul


def build_ag2_16_bipartite() -> list[list[int]]:
    """512-vertex 16-regular bipartite graph of girth 6 (points vs non-vertical lines of AG(2, 16))."""
    add, mul = f16_mul_table()
    # Vertices 0..255: points (x, y) = 16*x + y
    # Vertices 256..511: lines (m, c) = 256 + 16*m + c representing y = m*x + c
    adj = [[] for _ in range(512)]
    for x in range(16):
        for y in range(16):
            p = 16 * x + y
            for m in range(16):
                c = add[y][mul[m][x]]  # y + m*x in char 2
                ell = 256 + 16 * m + c
                adj[p].append(ell)
                adj[ell].append(p)
    return adj


def check_girth_at_least(adj: list[list[int]], target_girth: int, sample: list[int] | None = None) -> int:
    """Exact BFS shortest cycle check."""
    n = len(adj)
    best = n + 1
    verts = range(n) if sample is None else sample
    for start in verts:
        dist = [-1] * n
        parent = [-1] * n
        dist[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            if 2 * dist[u] + 1 >= best:
                break
            for w in adj[u]:
                if dist[w] == -1:
                    dist[w] = dist[u] + 1
                    parent[w] = u
                    q.append(w)
                elif parent[u] != w:
                    cyc = dist[u] + dist[w] + 1
                    if cyc < best:
                        best = cyc
        assert best >= target_girth, f"Found cycle of length {best} < {target_girth}"
    return best


def build_w16_minus_matching() -> list[list[int]]:
    """Construct an 8738-vertex 16-regular bipartite graph of girth >= 8 by deleting a 1-factor from W(16)."""
    add, mul = f16_mul_table()

    # Enumerate projective points of PG(3, 16): first nonzero coord = 1
    points = []
    pt_idx = {}
    for mask_len in range(4):
        pass
    for c0 in range(16):
        for c1 in range(16):
            for c2 in range(16):
                for c3 in range(16):
                    vec = (c0, c1, c2, c3)
                    for coord in vec:
                        if coord != 0:
                            if coord == 1:
                                pt_idx[vec] = len(points)
                                points.append(vec)
                            break
    assert len(points) == 4369  # (16^4 - 1) / 15

    # Symplectic form <u, v> = u0*v1 + u1*v0 + u2*v3 + u3*v2 over GF(16)
    def symp(u: tuple[int, int, int, int], v: tuple[int, int, int, int]) -> int:
        t0 = add[mul[u[0]][v[1]]][mul[u[1]][v[0]]]
        t1 = add[mul[u[2]][v[3]]][mul[u[3]][v[2]]]
        return add[t0][t1]

    # Wait: totally isotropic lines of W(16) through p are spanned by p and v with <p, v> = 0, v != p.
    # For each point, there are 16^2 + 16 = 272 other isotropic projective points lying on 17 lines of 16 other points each.
    # Represent each totally isotropic line canonically by its sorted tuple of 17 point indices? No, just canonical pair!
    # Actually even faster: precompute inverse in GF(16) and normalize a span.
    inv = [0] * 16
    for a in range(1, 16):
        for b in range(1, 16):
            if mul[a][b] == 1:
                inv[a] = b
                break

    def normalize(vec: list[int]) -> tuple[int, int, int, int]:
        for x in vec:
            if x != 0:
                s = inv[x]
                return (mul[vec[0]][s], mul[vec[1]][s], mul[vec[2]][s], mul[vec[3]][s])
        raise ValueError("zero vec")

    lines = []
    line_idx = {}
    line_to_pts = []
    pt_to_lines = [[] for _ in range(4369)]

    # Orthogonal complement p^\perp has dimension 3 -> 16^2+16+1 = 273 points (incl p).
    # Enumerate lines by checking collinearity in Plucker or simply enumerating (p, q) with p < q, <p,q>=0.
    seen_pairs = set()
    for i, u in enumerate(points):
        for j in range(i + 1, 4369):
            v = points[j]
            if symp(u, v) != 0:
                continue
            if (i, j) in seen_pairs:
                continue
            # All 17 points on the line spanned by u and v
            on_line = [i, j]
            for c in range(1, 16):
                w = normalize([add[u[k]][mul[c][v[k]]] for k in range(4)])
                on_line.append(pt_idx[w])
            on_line.sort()
            key = (on_line[0], on_line[1])
            assert key not in line_idx
            lid = len(lines)
            line_idx[key] = lid
            lines.append(key)
            line_to_pts.append(on_line)
            for a_idx in range(17):
                p_a = on_line[a_idx]
                pt_to_lines[p_a].append(lid)
                for b_idx in range(a_idx + 1, 17):
                    seen_pairs.add((on_line[a_idx], on_line[b_idx]))

    assert len(lines) == 4369
    for i in range(4369):
        assert len(pt_to_lines[i]) == 17

    # Wait: in W(16), is there a known spread (set of 257 disjoint lines covering all 4369 points)?
    # Even simpler: Hopcroft-Karp finds a perfect matching in this 17-regular bipartite graph in milliseconds!
    n_side = 4369
    match_l = [-1] * n_side
    match_r = [-1] * n_side
    # Greedy initial matching
    for u in range(n_side):
        for v in pt_to_lines[u]:
            if match_r[v] == -1:
                match_l[u] = v
                match_r[v] = u
                break

    # Hopcroft-Karp for remaining unmatched vertices
    INF = 10**9
    while True:
        dist_hk = [INF] * n_side
        q = deque()
        for u in range(n_side):
            if match_l[u] == -1:
                dist_hk[u] = 0
                q.append(u)
        found = False
        while q:
            u = q.popleft()
            for v in pt_to_lines[u]:
                u2 = match_r[v]
                if u2 == -1:
                    found = True
                elif dist_hk[u2] == INF:
                    dist_hk[u2] = dist_hk[u] + 1
                    q.append(u2)
        if not found:
            break

        def dfs(u: int) -> bool:
            for v in pt_to_lines[u]:
                u2 = match_r[v]
                if u2 == -1 or (dist_hk[u2] == dist_hk[u] + 1 and dfs(u2)):
                    match_l[u] = v
                    match_r[v] = u
                    return True
            dist_hk[u] = INF
            return False

        for u in range(n_side):
            if match_l[u] == -1:
                dfs(u)

    assert all(m != -1 for m in match_l)

    # Remove the perfect matching (u, match_l[u]) from the 8738-vertex bipartite graph
    adj = [[] for _ in range(2 * n_side)]
    for u in range(n_side):
        for v in pt_to_lines[u]:
            if v != match_l[u]:
                adj[u].append(n_side + v)
                adj[n_side + v].append(u)
    for x in range(2 * n_side):
        assert len(adj[x]) == 16
    return adj


def check_explicit_constructions() -> None:
    # t = 1: K_{16,16} (32 vertices, girth 4) -> 128-vertex ([1], (3,4))-flip graph
    adj_k16_16 = [list(range(16, 32)) for _ in range(16)] + [list(range(0, 16)) for _ in range(16)]
    assert check_girth_at_least(adj_k16_16, 4) == 4
    for seed in (0, 1, 2):
        b1, r1 = build_k4_blowup(adj_k16_16, seed=seed)
        verify_flip_graph(adj_k16_16, b1, r1, t=1)

    # t = 2: AG(2,16) bipartite minus parallel class (512 vertices, girth 6) -> 2048-vertex ([2], (3,4))-flip graph
    adj_ag = build_ag2_16_bipartite()
    assert check_girth_at_least(adj_ag, 6) == 6
    for seed in (0, 1):
        b2, r2 = build_k4_blowup(adj_ag, seed=seed)
        verify_flip_graph(adj_ag, b2, r2, t=2)

    # t = 3: W(16) minus 1-factor (8738 vertices, girth >= 8) -> 34952-vertex ([3], (3,4))-flip graph
    adj_w16 = build_w16_minus_matching()
    # Check girth >= 8 on sample of vertices (symmetry of W(16) before matching removal, check 200 vertices after)
    g_w16 = check_girth_at_least(adj_w16, 8, sample=list(range(0, 8738, 43)))
    assert g_w16 >= 8
    b3, r3 = build_k4_blowup(adj_w16, seed=7)
    verify_flip_graph(adj_w16, b3, r3, t=3, sample_vertices=list(range(0, 4 * 8738, 173)))

    print("[PASS] Explicit ([1],(3,4)) (128v), ([2],(3,4)) (2048v), and ([3],(3,4)) (34952v, sampled 203v) verified.")


if __name__ == "__main__":
    check_primary_source()
    check_lower_bound()
    check_recurrence_exact(200)
    check_explicit_constructions()
    print("PASS")
