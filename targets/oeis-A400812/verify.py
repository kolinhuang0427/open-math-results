"""
Exact verification script for OEIS A400812:
  Number of star triples in the level-n Spectre supertile.
Zero floating-point arithmetic is used anywhere: all planar coordinates lie in
Z[zeta_12] (represented as exact 4-tuples of ints) and all algebraic/GF identities
are proved over QQ with SymPy.
"""

from collections import Counter, defaultdict
import sympy as sp

# ---------------------------------------------------------------------------
# 1. Exact Spectre (S8/S9) substitution data from Smith-Myers-Kaplan-Goodman-Strauss
#    (arXiv:2305.17743, Section 4-5, Fig. 5 / Fig. 6, 00_macros.tex & fig_hexsubsts.tex)
# ---------------------------------------------------------------------------
NAMES = ["Gamma", "Delta", "Theta", "Lambda", "Xi", "Pi", "Sigma", "Phi", "Psi"]

# Counterclockwise edge labels of each level-0 marked hexagon (0=rot 0 .. 5=rot 300)
HEX_EDGES = {
    "Gamma":  ["a-", "a+", "g-", "d-", "b+", "b-"],
    "Delta":  ["g+", "b+", "e-", "a+", "g-", "z-"],
    "Theta":  ["g+", "b+", "t+", "b+", "et", "b-"],
    "Lambda": ["g+", "b+", "e-", "a+", "t-", "b-"],
    "Xi":     ["a-", "e+", "t+", "b+", "et", "b-"],
    "Pi":     ["a-", "e+", "e-", "a+", "t-", "b-"],
    "Sigma":  ["z+", "b+", "e-", "a+", "g-", "d+"],
    "Phi":    ["g+", "b+", "e-", "e+", "et", "b-"],
    "Psi":    ["a-", "e+", "e-", "e+", "et", "b-"],
}

# Supertiles: (child_name, rot60_k, hx, hy) and boundary mark points in centered vcoords
SUPERTILE_DEFS = {
    "Gamma": {
        "children": [("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Phi", 2, 0, 1), ("Xi", 1, 1, 1), ("Pi", 4, 0, -1), ("Delta", 5, 1, -1), ("Theta", 0, 2, -1)],
        "marks": [(2, 4), (-2, 2), (-4, 0), (-2, -4), (8, -8), (8, 0)],
    },
    "Delta": {
        "children": [("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Phi", 2, 0, 1), ("Pi", 1, 1, 1), ("Xi", 4, 0, -1), ("Delta", 5, 1, -1), ("Phi", 0, 2, -1), ("Xi", 5, 2, -2)],
        "marks": [(6, 2), (-2, 2), (-4, -2), (4, -10), (8, -8), (8, -2)],
    },
    "Theta": {
        "children": [("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Phi", 2, 0, 1), ("Pi", 1, 1, 1), ("Psi", 4, 0, -1), ("Delta", 5, 1, -1), ("Phi", 0, 2, -1), ("Pi", 5, 2, -2)],
        "marks": [(6, 2), (-2, 2), (-4, 0), (2, -8), (6, -10), (8, -2)],
    },
    "Lambda": {
        "children": [("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Phi", 2, 0, 1), ("Pi", 1, 1, 1), ("Psi", 4, 0, -1), ("Delta", 5, 1, -1), ("Phi", 0, 2, -1), ("Xi", 5, 2, -2)],
        "marks": [(6, 2), (-2, 2), (-4, 0), (4, -10), (8, -8), (8, -2)],
    },
    "Xi": {
        "children": [("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Phi", 2, 0, 1), ("Psi", 1, 1, 1), ("Psi", 4, 0, -1), ("Delta", 5, 1, -1), ("Phi", 0, 2, -1), ("Pi", 5, 2, -2)],
        "marks": [(2, 4), (-2, 2), (-4, 0), (2, -8), (6, -10), (8, -2)],
    },
    "Pi": {
        "children": [("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Phi", 2, 0, 1), ("Psi", 1, 1, 1), ("Psi", 4, 0, -1), ("Delta", 5, 1, -1), ("Phi", 0, 2, -1), ("Xi", 5, 2, -2)],
        "marks": [(2, 4), (-2, 2), (-4, 0), (4, -10), (8, -8), (8, -2)],
    },
    "Sigma": {
        "children": [("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Lambda", 2, 0, 1), ("Pi", 1, 1, 1), ("Xi", 4, 0, -1), ("Delta", 5, 1, -1), ("Phi", 0, 2, -1), ("Xi", 5, 2, -2)],
        "marks": [(6, 2), (0, 4), (-4, -2), (4, -10), (8, -8), (8, -2)],
    },
    "Phi": {
        "children": [("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Phi", 2, 0, 1), ("Pi", 1, 1, 1), ("Psi", 4, 0, -1), ("Delta", 5, 1, -1), ("Phi", 0, 2, -1), ("Psi", 5, 2, -2)],
        "marks": [(6, 2), (-2, 2), (-4, 0), (2, -8), (8, -8), (8, -2)],
    },
    "Psi": {
        "children": [("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Phi", 2, 0, 1), ("Psi", 1, 1, 1), ("Psi", 4, 0, -1), ("Delta", 5, 1, -1), ("Phi", 0, 2, -1), ("Psi", 5, 2, -2)],
        "marks": [(2, 4), (-2, 2), (-4, 0), (2, -8), (8, -8), (8, -2)],
    },
}


def opp(e):
    return "et" if e == "et" else e[:-1] + ("-" if e[-1] == "+" else "+")


def rot60(u, v, k):
    for _ in range(k % 6):
        u, v = -v, u + v
    return u, v


def hex_center(hx, hy):
    return (4 * hx + 2 * hy, -2 * hx + 2 * hy)


def build_supertile_templates():
    # Expected CW edge-word label sequences for matching each side to HEX_EDGES[name][0..5]
    expected_side_labels = {
        "a+": ["e-", "et", "b+"],
        "a-": ["b-", "et", "e+"],
        "b+": ["a+", "e-"],
        "b-": ["e+", "a-"],
        "d+": ["t+", "e+", "a-", "b-", "t-"],
        "d-": ["t+", "b+", "a+", "e-", "t-"],
        "e+": ["e-", "et", "e+", "e-"],
        "e-": ["e+", "e-", "et", "e+"],
        "et": ["e+", "e-", "et", "e+", "e-"],
        "g+": ["b-", "et", "e+", "e-", "t-"],
        "g-": ["t+", "e+", "e-", "et", "b+"],
        "t+": ["e+", "e-", "et", "e+", "e-", "t-"],
        "t-": ["t+", "e+", "e-", "et", "e+", "e-"],
        "z+": ["a+", "e-", "t-"],
        "z-": ["t+", "e+", "a-"],
    }
    templates = {}
    for name in NAMES:
        d = SUPERTILE_DEFS[name]
        children = d["children"]
        marks = set(d["marks"])
        ccw_edges = {}
        rev_ccw = {}
        for ci, (cname, rotk, hx, hy) in enumerate(children):
            cx, cy = hex_center(hx, hy)
            for s in range(6):
                p0 = rot60(-2, 2, s + rotk)
                p1 = rot60(-2, 0, s + rotk)
                a = (cx + p0[0], cy + p0[1])
                b = (cx + p1[0], cy + p1[1])
                ccw_edges[(ci, s)] = (a, b, HEX_EDGES[cname][s])
                rev_ccw[(a, b)] = (ci, s)

        # Verify every interior edge pair satisfies opp matching
        for (ci, si), (a, b, lab) in ccw_edges.items():
            if (b, a) in rev_ccw:
                cj, sj = rev_ccw[(b, a)]
                assert lab == opp(ccw_edges[(cj, sj)][2]), (name, ci, si, cj, sj)

        bdry = {a: (b, ci, s, lab) for (ci, s), (a, b, lab) in ccw_edges.items() if (b, a) not in rev_ccw}
        cur = sorted(marks)[0]
        cycle = []
        for _ in range(len(bdry)):
            nxt, ci, s, lab = bdry[cur]
            cycle.append((cur, nxt, ci, s, lab))
            cur = nxt
        assert cur == sorted(marks)[0]

        sides = []
        cs = []
        for item in cycle:
            if item[0] in marks and cs:
                sides.append(cs)
                cs = []
            cs.append(item)
        if cs:
            sides.append(cs)
        assert len(sides) == 6

        side_words_ccw = [[x[4] for x in sd] for sd in sides]
        # Match against reversed(HEX_EDGES[name]); each CCW side word equals the reverse of expected_side_labels
        rev_he = list(reversed(HEX_EDGES[name]))
        matches = [
            k for k in range(6)
            if all(side_words_ccw[j] == list(reversed(expected_side_labels[rev_he[(k + j) % 6]])) for j in range(6))
        ]
        assert len(matches) == 1, (name, matches, side_words_ccw)
        k_shift = matches[0]
        side_ccw = [None] * 6
        for j in range(6):
            edge_idx = 5 - ((k_shift + j) % 6)
            side_ccw[edge_idx] = sides[j]
        for i in range(6):
            assert side_ccw[i][0][0] == side_ccw[(i + 1) % 6][-1][1]

        templates[name] = {
            "children": [c for c, _, _, _ in children],
            "side_ccw": side_ccw,
            "rev_ccw": rev_ccw,
            "ccw_edges": ccw_edges,
        }
    return templates


# ---------------------------------------------------------------------------
# 2. Exact Z[zeta_12] Spectre polygon and geometric verification
# ---------------------------------------------------------------------------
def z_add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def z_sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])


def z_mul_z(a):
    c0, c1, c2, c3 = a
    return (-c3, c0, c1 + c3, c2)


def z_rot30(a, k):
    for _ in range(k % 12):
        a = z_mul_z(a)
    return a


def norm2_times4(a):
    """Exact 4*|a|^2 = (A, B) representing A + B*sqrt(3) in Z[sqrt(3)]."""
    c0, c1, c2, c3 = a
    x0, x1 = 2 * c0 + c2, c1
    y0, y1 = 2 * c3 + c1, c2
    return (x0 * x0 + 3 * x1 * x1 + y0 * y0 + 3 * y1 * y1, 2 * (x0 * x1 + y0 * y1))


def seg_sig(dlist):
    return (len(dlist), tuple((dlist[t + 1] - dlist[t]) % 12 for t in range(len(dlist) - 1)))


def transform_poly(dirs_k_list, rot_k=0):
    return [(3 - d + rot_k) % 12 for d in reversed(dirs_k_list)]


def poly_from_dirs(dlist, start=(0, 0, 0, 0)):
    pts = [start]
    for d in dlist[:-1]:
        pts.append(z_add(pts[-1], z_rot30((1, 0, 0, 0), d)))
    assert z_add(pts[-1], z_rot30((1, 0, 0, 0), dlist[-1])) == start
    return pts


def build_canonical_tiles():
    # Tile A (even) & Tile B (odd) edge directions from 00_macros.tex, in reflected+rot270 frame
    b_dirs = transform_poly([6, 9, 7, 10, 0, 0, 2, 11, 1, 4, 6, 3, 5, 8])
    a_dirs_raw = transform_poly([6, 9, 11, 11, 1, 10, 0, 3, 5, 2, 4, 7, 5, 8])
    idx0 = next(i for i in range(14) if a_dirs_raw[i] == 0 and a_dirs_raw[(i + 1) % 14] == 3)
    a_dirs_0 = a_dirs_raw[idx0:] + a_dirs_raw[:idx0]
    w_poly = poly_from_dirs(a_dirs_0)

    a_dirs_in_mystic = [(d - 2) % 12 for d in a_dirs_0]
    b_pts = poly_from_dirs(b_dirs)
    ib, ia = next(
        (ib_, ia_) for ib_ in range(14) for ia_ in range(14)
        if [b_dirs[(ib_ + t) % 14] for t in range(4)] == [(a_dirs_in_mystic[(ia_ + 3 - t) % 14] + 6) % 12 for t in range(4)]
    )
    a_raw = poly_from_dirs(a_dirs_in_mystic)
    shift_a = z_sub(b_pts[(ib + 4) % 14], a_raw[ia])
    a_pts_m = [z_add(p, shift_a) for p in a_raw]
    for t in range(5):
        assert b_pts[(ib + t) % 14] == a_pts_m[(ia + 4 - t) % 14]

    mystic_pts, mystic_dirs = [], []
    k = (ib + 4) % 14
    while k != ib:
        mystic_pts.append(b_pts[k])
        mystic_dirs.append(b_dirs[k])
        k = (k + 1) % 14
    k = (ia + 4) % 14
    while k != ia:
        mystic_pts.append(a_pts_m[k])
        mystic_dirs.append(a_dirs_in_mystic[k])
        k = (k + 1) % 14
    assert len(mystic_pts) == 20

    g_start = next(
        st for st in range(20)
        if (
            seg_sig([mystic_dirs[(st + t) % 20] for t in range(3)]) == (3, (10, 3))
            and seg_sig([mystic_dirs[(st + 3 + t) % 20] for t in range(3)]) == (3, (9, 2))
            and seg_sig([mystic_dirs[(st + 6 + t) % 20] for t in range(2)]) == (2, (2,))
            and seg_sig([mystic_dirs[(st + 14 + t) % 20] for t in range(3)]) == (3, (2, 9))
            and seg_sig([mystic_dirs[(st + 17 + t) % 20] for t in range(3)]) == (3, (3, 10))
        )
    )
    d_minus = [mystic_dirs[(g_start + 8 + t) % 20] for t in range(6)]
    assert seg_sig([9, 7, 10, 8, 5, 3]) == seg_sig([(d + 6) % 12 for d in reversed(d_minus)])

    dot_indices = {
        "Phi":    [9, 11, 0, 2, 4, 6],
        "Pi":     [9, 12, 0, 2, 5, 6],
        "Psi":    [9, 12, 0, 2, 4, 6],
        "Delta":  [9, 11, 0, 2, 5, 7],
        "Lambda": [9, 11, 0, 2, 5, 6],
        "Theta":  [9, 11, 0, 1, 4, 6],
        "Xi":     [9, 12, 0, 1, 4, 6],
    }
    p_q = z_add(w_poly[11], z_rot30((1, 0, 0, 0), 5))
    p_spur = z_add(p_q, z_rot30((1, 0, 0, 0), 3))

    tiles = {nm: {"corners": [w_poly[idx] for idx in idxs], "spectres": [w_poly], "parities": [0]} for nm, idxs in dot_indices.items()}
    tiles["Sigma"] = {"corners": [p_spur, w_poly[11], w_poly[0], w_poly[2], w_poly[5], w_poly[7]], "spectres": [w_poly], "parities": [0]}
    tiles["Gamma"] = {"corners": [mystic_pts[(g_start + off) % 20] for off in (0, 3, 6, 8, 14, 17)], "spectres": [b_pts, a_pts_m], "parities": [1, 0]}

    # Check every pair of opposite labels has congruent chord vectors
    for t1 in NAMES:
        for s1 in range(6):
            l1 = HEX_EDGES[t1][s1]
            v1 = z_sub(tiles[t1]["corners"][(s1 + 1) % 6], tiles[t1]["corners"][s1])
            ol = opp(l1)
            for t2 in NAMES:
                for s2 in range(6):
                    if HEX_EDGES[t2][s2] == ol:
                        v2 = z_sub(tiles[t2]["corners"][s2], tiles[t2]["corners"][(s2 + 1) % 6])
                        assert any(z_rot30(v2, r) == v1 for r in range(12)), (t1, s1, l1, t2, s2, ol)
    return tiles


def count_star_triples_in_spectre_list(spectres):
    pt_to_tiles = defaultdict(list)
    for ti, poly in enumerate(spectres):
        for p in poly:
            pt_to_tiles[(2 * p[0], 2 * p[1], 2 * p[2], 2 * p[3])].append(ti)
        for idx in range(14):
            p0, p1 = poly[idx], poly[(idx + 1) % 14]
            pt_to_tiles[(p0[0] + p1[0], p0[1] + p1[1], p0[2] + p1[2], p0[3] + p1[3])].append(ti)

    by_r2 = Counter()
    for p2, tlist in pt_to_tiles.items():
        if len(tlist) < 3:
            continue
        local_map = {frozenset((2 * q[0], 2 * q[1], 2 * q[2], 2 * q[3]) for q in spectres[ti]): ti for ti in tlist}
        used = set()
        for ti in tlist:
            if ti in used:
                continue
            r120 = frozenset(z_add(p2, z_rot30(z_sub((2 * q[0], 2 * q[1], 2 * q[2], 2 * q[3]), p2), 4)) for q in spectres[ti])
            r240 = frozenset(z_add(p2, z_rot30(z_sub((2 * q[0], 2 * q[1], 2 * q[2], 2 * q[3]), p2), 8)) for q in spectres[ti])
            if r120 in local_map and r240 in local_map:
                t1, t2 = local_map[r120], local_map[r240]
                if len({ti, t1, t2}) == 3:
                    used.update({ti, t1, t2})
                    # Exact max 4*R^2 in Z[sqrt(3)] (comparing exact values since B > 0)
                    cand_r2 = [
                        norm2_times4(z_sub((2 * q[0], 2 * q[1], 2 * q[2], 2 * q[3]), p2))
                        for idx_t in (ti, t1, t2)
                        for q in spectres[idx_t]
                    ]
                    # Compare exact a1 + b1*sqrt(3) > a2 + b2*sqrt(3) via algebraic sign in Z[sqrt(3)]
                    best = cand_r2[0]
                    for ab in cand_r2[1:]:
                        da, db = ab[0] - best[0], ab[1] - best[1]
                        if (da >= 0 and db >= 0 and (da > 0 or db > 0)) or (da > 0 and db < 0 and da * da > 3 * db * db) or (da < 0 and db > 0 and 3 * db * db > da * da):
                            best = ab
                    assert best[0] % 4 == 0 and best[1] % 4 == 0
                    by_r2[(best[0] // 4, best[1] // 4)] += 1
    return by_r2


# ---------------------------------------------------------------------------
# 3. Combinatorial substitution & period-2 corner / 45-vertex-type checks
# ---------------------------------------------------------------------------
def is_l_triple(triple):
    return len(triple) == 3 and all(x[0] in ("Pi", "Psi") and (x[1], x[2]) == ("e+", "e-") for x in triple)


def is_s_triple(triple):
    return len(triple) == 3 and all(x[0] == "Phi" and (x[1], x[2]) == ("e-", "e+") for x in triple)


def init_comb_state():
    st = {}
    for name in NAMES:
        he = HEX_EDGES[name]
        sides = [[((name, he[(i - 1) % 6], he[i]),), ((name, he[i], he[(i + 1) % 6]),)] for i in range(6)]
        st[name] = {"sides": sides, "L": 0, "S": 0, "types": Counter()}
    return st


def step_comb(templates, prev_state, is_level1):
    nxt = {}
    for name in NAMES:
        d = templates[name]
        children = d["children"]
        ch_sides = []
        l_cnt, s_cnt = 0, 0
        types = Counter()
        for cname in children:
            ps = prev_state[cname]
            l_cnt += ps["L"]
            s_cnt += ps["S"]
            types += ps["types"]
            ch_sides.append([list(sd) if is_level1 else list(reversed(sd)) for sd in ps["sides"]])

        parent = {}

        def find(x):
            while parent.get(x, x) != x:
                parent[x] = parent.get(parent[x], parent[x])
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx

        grid_to_key = {}
        for (ci, s), (a, b, _) in d["ccw_edges"].items():
            for pt, k in [(a, ("mv", ci, s)), (b, ("mv", ci, (s + 1) % 6))]:
                if pt in grid_to_key:
                    union(grid_to_key[pt], k)
                else:
                    grid_to_key[pt] = k

        for (ci, si), (a, b, _) in d["ccw_edges"].items():
            if (b, a) in d["rev_ccw"]:
                cj, sj = d["rev_ccw"][(b, a)]
                if (ci, si) < (cj, sj):
                    l1 = len(ch_sides[ci][si])
                    assert l1 == len(ch_sides[cj][sj])
                    for k in range(1, l1 - 1):
                        union(("iv", ci, si, k), ("iv", cj, sj, l1 - 1 - k))

        verts_corners = defaultdict(list)
        seen_mv = set()
        for ci in range(len(children)):
            for s in range(6):
                sd = ch_sides[ci][s]
                if (ci, s) not in seen_mv:
                    seen_mv.add((ci, s))
                    verts_corners[find(("mv", ci, s))].extend(sd[0])
                for k in range(1, len(sd) - 1):
                    verts_corners[find(("iv", ci, s, k))].extend(sd[k])

        bdry_roots = set()
        new_sides = []
        for macro_i in range(6):
            sd_vertices = []
            pieces = d["side_ccw"][macro_i]
            for pi, (_a, _b, ci, s, _lab) in enumerate(pieces):
                cs = ch_sides[ci][s]
                l_side = len(cs)
                rng = range(0, l_side) if pi == len(pieces) - 1 else range(0, l_side - 1)
                for k in rng:
                    if k == 0:
                        r = find(("mv", ci, s))
                    elif k == l_side - 1:
                        r = find(("mv", ci, (s + 1) % 6))
                    else:
                        r = find(("iv", ci, s, k))
                    bdry_roots.add(r)
                    v_tup = tuple(verts_corners[r])
                    assert 1 <= len(v_tup) <= 2
                    sd_vertices.append(v_tup)
            new_sides.append(sd_vertices)

        for r, cs in verts_corners.items():
            if r not in bdry_roots:
                t = tuple(sorted(cs))
                assert len(t) == 3
                types[t] += 1
                if is_l_triple(t):
                    l_cnt += 1
                elif is_s_triple(t):
                    s_cnt += 1
        nxt[name] = {"sides": new_sides, "L": l_cnt, "S": s_cnt, "types": types}
    return nxt


def verify_all():
    templates = build_supertile_templates()
    tiles = build_canonical_tiles()

    # Run combinatorial states n=0..6
    states = [init_comb_state()]
    for n in range(1, 7):
        states.append(step_comb(templates, states[-1], is_level1=(n == 1)))

    # 1. Verify period-2 boundary corner stabilization for n=4,5,6 (=> holds for all n >= 2)
    for n in (4, 5, 6):
        c_n = {nm: [(sd[0], sd[-1]) for sd in states[n][nm]["sides"]] for nm in NAMES}
        c_prev = {nm: [(sd[0], sd[-1]) for sd in states[n - 2][nm]["sides"]] for nm in NAMES}
        assert c_n == c_prev, f"Corner periodicity failed at n={n}"

    # Verify Gamma never contains Gamma in any 3-hex vertex type, nor on sides opposite Gamma's edges
    all45 = set()
    for nm in NAMES:
        all45.update(states[4][nm]["types"].keys())
    all_n5 = set()
    all_n6 = set()
    for nm in NAMES:
        all_n5.update(states[5][nm]["types"].keys())
        all_n6.update(states[6][nm]["types"].keys())
    assert len(all45) == 45 and all_n5 == all45 and all_n6 == all45
    assert all(sum(1 for x in t if x[0] == "Gamma") <= 1 for t in all45)
    # Verify Gamma only occurs on boundary sides in {a-, b-, g+, z-, d+}, never on their opposites {a+, b+, g-, z+, d-}
    for nm in NAMES:
        for i in range(6):
            if HEX_EDGES[nm][i] in ("a+", "b+", "g-", "z+", "d-"):
                assert all(templates[nm]["children"][ci] != "Gamma" for _, _, ci, _, _ in templates[nm]["side_ccw"][i])

    # 2. Exhaustively check ALL 45 3-hex vertex configurations in exact Z[zeta_12]
    star_types = []
    for t3 in sorted(all45):
        options = []
        for nm, e1, e2 in t3:
            he = HEX_EDGES[nm]
            idxs = [i for i in range(6) if he[i] == e1 and he[(i + 1) % 6] == e2]
            assert len(idxs) == 1
            options.append((nm, idxs[0]))
        glued = False
        for perm in ((0, 1, 2), (0, 2, 1)):
            if all(HEX_EDGES[options[perm[k]][0]][(options[perm[k]][1] + 1) % 6] == opp(HEX_EDGES[options[perm[(k + 1) % 3]][0]][options[perm[(k + 1) % 3]][1]]) for k in range(3)):
                nm0, i0 = options[perm[0]]
                nm1, i1 = options[perm[1]]
                nm2, i2 = options[perm[2]]
                c0, c1, c2 = tiles[nm0]["corners"], tiles[nm1]["corners"], tiles[nm2]["corners"]
                v_pt = c0[(i0 + 1) % 6]
                vec0 = z_sub(c0[(i0 + 2) % 6], v_pt)
                r1 = next(r for r in range(12) if z_rot30(z_sub(c1[i1], c1[(i1 + 1) % 6]), r) == vec0)
                t1 = z_sub(v_pt, z_rot30(c1[(i1 + 1) % 6], r1))
                p1_end = z_add(z_rot30(c1[(i1 + 2) % 6], r1), t1)
                r2 = next(r for r in range(12) if z_rot30(z_sub(c2[i2], c2[(i2 + 1) % 6]), r) == z_sub(p1_end, v_pt))
                t2 = z_sub(v_pt, z_rot30(c2[(i2 + 1) % 6], r2))
                spectres = []
                for nm_k, r_k, tr_k in ((nm0, 0, (0, 0, 0, 0)), (nm1, r1, t1), (nm2, r2, t2)):
                    for sp_poly in tiles[nm_k]["spectres"]:
                        spectres.append([z_add(z_rot30(p, r_k), tr_k) for p in sp_poly])
                by_r2 = count_star_triples_in_spectre_list(spectres)
                if by_r2:
                    star_types.append((t3, dict(by_r2)))
                glued = True
                break
        assert glued

    assert len(star_types) == 4
    for t3, br in star_types:
        if is_l_triple(t3):
            assert br == {(40, 20): 1}  # 4*R_L^2 = 40 + 20*sqrt(3)
        else:
            assert is_s_triple(t3) and br == {(40, 12): 1}  # 4*R_S^2 = 40 + 12*sqrt(3)

    # 3. Build explicit geometric Delta_3 (559 Spectres) and Delta_4 (4401 Spectres) patches in Z[zeta_12]
    patches = {nm: {"types": [nm], "adjs": [], "sides": [[(0, s)] for s in range(6)]} for nm in NAMES}
    for lvl in range(1, 5):
        nxt_p = {}
        for nm in NAMES:
            d = templates[nm]
            types, adjs, ch_sides = [], [], []
            for cname in d["children"]:
                off = len(types)
                cp = patches[cname]
                types.extend(cp["types"])
                for h1, s1, h2, s2 in cp["adjs"]:
                    adjs.append((off + h1, s1, off + h2, s2))
                if lvl == 1:
                    ch_sides.append([[(off + h, s) for h, s in sd] for sd in cp["sides"]])
                else:
                    ch_sides.append([[(off + h, s) for h, s in reversed(sd)] for sd in cp["sides"]])
            for (ci, si), (a, b, _) in d["ccw_edges"].items():
                if (b, a) in d["rev_ccw"]:
                    cj, sj = d["rev_ccw"][(b, a)]
                    if (ci, si) < (cj, sj):
                        for (h1, hs1), (h2, hs2) in zip(ch_sides[ci][si], reversed(ch_sides[cj][sj])):
                            adjs.append((h1, hs1, h2, hs2))
            new_sides = []
            for macro_i in range(6):
                sd = []
                for _, _, ci, s, _ in d["side_ccw"][macro_i]:
                    sd.extend(ch_sides[ci][s])
                new_sides.append(sd)
            nxt_p[nm] = {"types": types, "adjs": adjs, "sides": new_sides}
        patches = nxt_p
        if lvl in (3, 4):
            dp = patches["Delta"]
            adj_map = defaultdict(list)
            for h1, s1, h2, s2 in dp["adjs"]:
                adj_map[h1].append((s1, h2, s2))
                adj_map[h2].append((s2, h1, s1))
            placed = {0: (0, (0, 0, 0, 0))}
            q = [0]
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                ru, tu = placed[u]
                cu = tiles[dp["types"][u]]["corners"]
                for su, v, sv in adj_map[u]:
                    p0 = z_add(z_rot30(cu[su], ru), tu)
                    p1 = z_add(z_rot30(cu[(su + 1) % 6], ru), tu)
                    cv = tiles[dp["types"][v]]["corners"]
                    rv = next(r for r in range(12) if z_rot30(z_sub(cv[sv], cv[(sv + 1) % 6]), r) == z_sub(p1, p0))
                    tv = z_sub(p0, z_rot30(cv[(sv + 1) % 6], rv))
                    if v in placed:
                        assert placed[v] == (rv, tv)
                    else:
                        placed[v] = (rv, tv)
                        q.append(v)
            assert len(placed) == len(dp["types"])
            spectres = []
            for h, htype in enumerate(dp["types"]):
                rh, th = placed[h]
                for sp_poly in tiles[htype]["spectres"]:
                    spectres.append([z_add(z_rot30(p, rh), th) for p in sp_poly])
            by_r2 = count_star_triples_in_spectre_list(spectres)
            if lvl == 3:
                assert len(spectres) == 559 and dict(by_r2) == {(40, 20): 18, (40, 12): 10}
            else:
                assert len(spectres) == 4401 and dict(by_r2) == {(40, 20): 236, (40, 12): 136}

    # 4. Exact transfer matrix A and minimal polynomial / rational GF proof
    all_seams = []
    seam_idx = {}
    for i, X in enumerate(NAMES):
        for s1 in range(6):
            e1 = HEX_EDGES[X][s1]
            for j, Y in enumerate(NAMES):
                for s2 in range(6):
                    if HEX_EDGES[Y][s2] == opp(e1) and (i, s1) <= (j, s2):
                        seam_idx[((X, s1), (Y, s2))] = len(all_seams)
                        all_seams.append(((X, s1), (Y, s2)))
    assert len(all_seams) == 134

    def canon_seam(X, s1, Y, s2):
        i, j = NAMES.index(X), NAMES.index(Y)
        return ((X, s1), (Y, s2)) if (i, s1) <= (j, s2) else ((Y, s2), (X, s1))

    dim = len(NAMES) + len(all_seams)
    A = sp.zeros(dim, dim)
    for xi, X in enumerate(NAMES):
        d = templates[X]
        for cname in d["children"]:
            A[xi, NAMES.index(cname)] += 1
        for (ci, si), (a, b, _) in d["ccw_edges"].items():
            if (b, a) in d["rev_ccw"]:
                cj, sj = d["rev_ccw"][(b, a)]
                if (ci, si) < (cj, sj):
                    cs = canon_seam(d["children"][ci], si, d["children"][cj], sj)
                    A[xi, len(NAMES) + seam_idx[cs]] += 1

    for si_idx, ((X, s1), (Y, s2)) in enumerate(all_seams):
        row = len(NAMES) + si_idx
        px = templates[X]["side_ccw"][s1]
        py = list(reversed(templates[Y]["side_ccw"][s2]))
        assert len(px) == len(py)
        for p in range(len(px)):
            _, _, ci, si, _ = px[p]
            _, _, cj, sj, _ = py[p]
            cs = canon_seam(templates[X]["children"][ci], si, templates[Y]["children"][cj], sj)
            A[row, len(NAMES) + seam_idx[cs]] += 1

    def state_vecs(st):
        vL = [st[X]["L"] for X in NAMES]
        vS = [st[X]["S"] for X in NAMES]
        for (X, s1), (Y, s2) in all_seams:
            sd1 = st[X]["sides"][s1]
            sd2 = list(reversed(st[Y]["sides"][s2]))
            lc, sc = 0, 0
            for k in range(1, len(sd1) - 1):
                t = tuple(sorted(sd1[k] + sd2[k]))
                if is_l_triple(t):
                    lc += 1
                elif is_s_triple(t):
                    sc += 1
            vL.append(lc)
            vS.append(sc)
        return sp.Matrix(vL), sp.Matrix(vS)

    vecs = [state_vecs(st) for st in states]
    bLs = [vecs[n + 1][0] - A * vecs[n][0] for n in range(1, 6)]
    bSs = [vecs[n + 1][1] - A * vecs[n][1] for n in range(1, 6)]
    assert bLs[1] == bLs[3] and bLs[2] == bLs[4]
    assert bSs[1] == bSs[3] and bSs[2] == bSs[4]

    # Restrict to states reachable from the 8 non-Gamma supertiles
    reachable = set()
    frontier = set(range(1, 9))
    while frontier:
        nf = set()
        for r in frontier:
            reachable.add(r)
            for c in range(dim):
                if A[r, c] != 0 and c not in reachable:
                    nf.add(c)
        frontier = nf
    r_list = sorted(reachable)
    idx_map = {r: k for k, r in enumerate(r_list)}
    Ar = sp.Matrix(len(r_list), len(r_list), lambda i, j: A[r_list[i], r_list[j]])
    Ar2 = Ar * Ar

    def find_row_minpoly(mat, row_idx):
        m = mat.rows
        e = sp.zeros(1, m)
        e[0, row_idx] = 1
        rows = [e]
        for _ in range(1, m + 2):
            rows.append(rows[-1] * mat)
            ns = sp.Matrix([list(v) for v in rows]).T.nullspace()
            if ns:
                c = ns[0]
                return [ci / c[-1] for ci in c]
        raise AssertionError("No annihilating polynomial found")

    x, z = sp.Symbol("x"), sp.Symbol("z")
    expected_gf_L = 2 * x**3 * (9 + x) / ((1 - x) * (1 - 8 * x + x**2) * (1 - 4 * x - x**2))
    expected_gf_S = 2 * x**3 * (5 + 3 * x) / ((1 - x) * (1 - 8 * x + x**2) * (1 - 4 * x - x**2))
    expected_gf_tot = 4 * x**3 * (7 + 2 * x) / ((1 - x) * (1 - 8 * x + x**2) * (1 - 4 * x - x**2))

    # Check ALL 8 non-Gamma supertiles share the exact same GF_L, GF_S, GF_tot!
    for r_orig in range(1, 9):
        ri = idx_map[r_orig]
        q_coeffs = find_row_minpoly(Ar2, ri)
        q_poly = sum(c * z**k for k, c in enumerate(q_coeffs))
        deg_q = len(q_coeffs) - 1
        assert sp.factor(q_poly) == z * (z - 1) * (z**2 - 62 * z + 1) * (z**2 - 18 * z + 1)
        q_rev = sp.expand(z**deg_q * q_poly.subs(z, 1 / z))
        d_y = sp.Poly((1 - z) * q_rev, z)
        denom_x = sp.expand((1 - x**2) * q_rev.subs(z, x**2))

        for exp_gf, v2, b_ev, b_od in (
            (expected_gf_L, vecs[2][0][r_list, :], bLs[1][r_list, :], bLs[2][r_list, :]),
            (expected_gf_S, vecs[2][1][r_list, :], bSs[1][r_list, :], bSs[2][r_list, :]),
        ):
            v = v2
            vals = [0, 0, int(v[ri])]
            for n in range(2, 2 * deg_q + 4):
                v = Ar * v + (b_ev if n % 2 == 0 else b_od)
                vals.append(int(v[ri]))
            num_ev = sum(sum(d_y.nth(k) * vals[2 + 2 * (m - k)] for k in range(m + 1)) * z**m for m in range(deg_q + 1))
            num_od = sum(sum(d_y.nth(k) * vals[3 + 2 * (m - k)] for k in range(m + 1)) * z**m for m in range(deg_q + 1))
            gf = (x**2 * num_ev.subs(z, x**2) + x**3 * num_od.subs(z, x**2)) / denom_x
            assert sp.simplify(gf - exp_gf) == 0

    # 5. Verify OEIS A400812 data, recurrence, A057080/Fibonacci identity, and asymptotic limit
    oeis_data = [0, 0, 0, 28, 372, 3604, 31268, 258464, 2086984, 16651528, 132032296, 1043449220]
    series_terms = sp.series(expected_gf_tot, x, 0, 31)
    a_seq = [int(series_terms.coeff(x, n)) for n in range(31)]
    assert a_seq[:len(oeis_data)] == oeis_data
    for n in range(5, 31):
        assert a_seq[n] == 13 * a_seq[n - 1] - 44 * a_seq[n - 2] + 28 * a_seq[n - 3] + 5 * a_seq[n - 4] - a_seq[n - 5]

    # Identity: a(n) = A057080(n-1) - (F(3n+2)-3)/2 = A057080(n-1) - A099919(n) + 1 for n >= 1
    # A057080(n) from substitution matrix [[1, 6], [1, 7]] with initial (Gamma=2, Delta=1)
    g, t = 2, 1
    t_seq = [t]
    for _ in range(30):
        g, t = g + 6 * t, g + 7 * t
        t_seq.append(t)
    assert t_seq[:6] == [1, 9, 71, 559, 4401, 34649]

    fib = [0, 1]
    while len(fib) < 100:
        fib.append(fib[-1] + fib[-2])
    for n in range(1, 31):
        assert a_seq[n] == t_seq[n - 1] - (fib[3 * n + 2] - 3) // 2

    gf_t_prev = x * (1 + x) / (1 - 8 * x + x**2)
    gf_fib_term = ((1 + x) / (1 - 4 * x - x**2) - 1 - 3 * x / (1 - x)) / 2
    assert sp.simplify(gf_t_prev - gf_fib_term - expected_gf_tot) == 0

    print("PASS")


if __name__ == "__main__":
    verify_all()
