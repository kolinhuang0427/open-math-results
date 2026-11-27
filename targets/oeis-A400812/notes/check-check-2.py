#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/oeis-A400812/PROOF.md.

Zero floating-point arithmetic anywhere: uses exact Z[zeta_12] integer tuples,
exact Q(sqrt(3)) sign/norm tests, exact Fraction Krylov linear algebra, and exact
sympy rational polynomial arithmetic, derived directly from arXiv:2305.17743
(00_macros.tex, 04_hexagons.tex, 05_hexsubst.tex, fig_hexsubsts.tex).
"""

from collections import deque
from fractions import Fraction
import sympy as sp

# ---------------------------------------------------------------------------
# 1. Exact Z[zeta_12] arithmetic: basis (1, z, z^2, z^3) with z^4 = z^2 - 1
# ---------------------------------------------------------------------------

def zadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])

def zsub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])

def zmul_z(a):
    return (-a[3], a[0], a[1] + a[3], a[2])

Z = [(1, 0, 0, 0)]
for _ in range(11):
    Z.append(zmul_z(Z[-1]))

def zrot(a, k):
    for _ in range(k % 12):
        a = zmul_z(a)
    return a

def zconj(a):
    # Complex conjugation (reflection across x-axis): z -> z^11 = z - z^3, z^2 -> 1 - z^2, z^3 -> -z^3
    return (a[0] + a[2], a[1], -a[2], -a[1] - a[3])

def to_2cart_qsqrt3(p):
    # 2*p = ((2*c0 + c2) + c1*sqrt(3), (c1 + 2*c3) + c2*sqrt(3))
    c0, c1, c2, c3 = p
    return ((2 * c0 + c2, c1), (c1 + 2 * c3, c2))

def q3_add(u, v):
    return (u[0] + v[0], u[1] + v[1])

def q3_sub(u, v):
    return (u[0] - v[0], u[1] - v[1])

def q3_mul(u, v):
    return (u[0] * v[0] + 3 * u[1] * v[1], u[0] * v[1] + u[1] * v[0])

def q3_sign(u):
    a, b = u
    if a == 0 and b == 0:
        return 0
    if a >= 0 and b >= 0:
        return 1
    if a <= 0 and b <= 0:
        return -1
    if a > 0 and b < 0:
        return 1 if a * a > 3 * b * b else (-1 if a * a < 3 * b * b else 0)
    return -1 if a * a > 3 * b * b else (1 if a * a < 3 * b * b else 0)

def z_sqnorm_qsqrt3(p):
    x, y = to_2cart_qsqrt3(p)
    n4 = q3_add(q3_mul(x, x), q3_mul(y, y))
    assert n4[0] % 4 == 0 and n4[1] % 4 == 0
    return (n4[0] // 4, n4[1] // 4)

def poly_cross2(a, b, c):
    ax, ay = to_2cart_qsqrt3(a)
    bx, by = to_2cart_qsqrt3(b)
    cx, cy = to_2cart_qsqrt3(c)
    return q3_sub(q3_mul(q3_sub(bx, ax), q3_sub(cy, ay)),
                  q3_mul(q3_sub(by, ay), q3_sub(cx, ax)))

# ---------------------------------------------------------------------------
# 2. Primary definitions from 00_macros.tex & fig_hexsubsts.tex (arXiv:2305.17743)
# ---------------------------------------------------------------------------

NAMES = ["Gamma", "Delta", "Theta", "Lambda", "Xi", "Pi", "Sigma", "Phi", "Psi"]
NON_GAMMA = [nm for nm in NAMES if nm != "Gamma"]

HEX_LABELS = {
    "Gamma":  ("alphaminus", "alphaplus", "gammaminus", "deltaminus", "betaplus", "betaminus"),
    "Delta":  ("gammaplus", "betaplus", "epsilonminus", "alphaplus", "gammaminus", "zetaminus"),
    "Theta":  ("gammaplus", "betaplus", "thetaplus", "betaplus", "eta", "betaminus"),
    "Lambda": ("gammaplus", "betaplus", "epsilonminus", "alphaplus", "thetaminus", "betaminus"),
    "Xi":     ("alphaminus", "epsilonplus", "thetaplus", "betaplus", "eta", "betaminus"),
    "Pi":     ("alphaminus", "epsilonplus", "epsilonminus", "alphaplus", "thetaminus", "betaminus"),
    "Sigma":  ("zetaplus", "betaplus", "epsilonminus", "alphaplus", "gammaminus", "deltaplus"),
    "Phi":    ("gammaplus", "betaplus", "epsilonminus", "epsilonplus", "eta", "betaminus"),
    "Psi":    ("alphaminus", "epsilonplus", "epsilonminus", "epsilonplus", "eta", "betaminus"),
}

def opp_label(lbl):
    if lbl == "eta":
        return "eta"
    if lbl.endswith("plus"):
        return lbl[:-4] + "minus"
    if lbl.endswith("minus"):
        return lbl[:-5] + "plus"
    raise ValueError(lbl)

SUPERTILE_CHILDS = {
    "Gamma": [
        ("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Phi", 2, 0, 1),
        ("Xi", 1, 1, 1), ("Pi", 4, 0, -1), ("Delta", 5, 1, -1), ("Theta", 0, 2, -1),
    ],
    "Delta": [
        ("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Phi", 2, 0, 1), ("Pi", 1, 1, 1),
        ("Xi", 4, 0, -1), ("Delta", 5, 1, -1), ("Phi", 0, 2, -1), ("Xi", 5, 2, -2),
    ],
    "Theta": [
        ("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Phi", 2, 0, 1), ("Pi", 1, 1, 1),
        ("Psi", 4, 0, -1), ("Delta", 5, 1, -1), ("Phi", 0, 2, -1), ("Pi", 5, 2, -2),
    ],
    "Lambda": [
        ("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Phi", 2, 0, 1), ("Pi", 1, 1, 1),
        ("Psi", 4, 0, -1), ("Delta", 5, 1, -1), ("Phi", 0, 2, -1), ("Xi", 5, 2, -2),
    ],
    "Xi": [
        ("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Phi", 2, 0, 1), ("Psi", 1, 1, 1),
        ("Psi", 4, 0, -1), ("Delta", 5, 1, -1), ("Phi", 0, 2, -1), ("Pi", 5, 2, -2),
    ],
    "Pi": [
        ("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Phi", 2, 0, 1), ("Psi", 1, 1, 1),
        ("Psi", 4, 0, -1), ("Delta", 5, 1, -1), ("Phi", 0, 2, -1), ("Xi", 5, 2, -2),
    ],
    "Sigma": [
        ("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Lambda", 2, 0, 1), ("Pi", 1, 1, 1),
        ("Xi", 4, 0, -1), ("Delta", 5, 1, -1), ("Phi", 0, 2, -1), ("Xi", 5, 2, -2),
    ],
    "Phi": [
        ("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Phi", 2, 0, 1), ("Pi", 1, 1, 1),
        ("Psi", 4, 0, -1), ("Delta", 5, 1, -1), ("Phi", 0, 2, -1), ("Psi", 5, 2, -2),
    ],
    "Psi": [
        ("Gamma", 0, 0, 0), ("Sigma", 1, 1, 0), ("Phi", 2, 0, 1), ("Psi", 1, 1, 1),
        ("Psi", 4, 0, -1), ("Delta", 5, 1, -1), ("Phi", 0, 2, -1), ("Psi", 5, 2, -2),
    ],
}

SUPERTILE_MARKS = {
    "Gamma":  [(4, 4), (0, 2), (-2, 0), (0, -4), (10, -8), (10, 0)],
    "Delta":  [(8, 2), (0, 2), (-2, -2), (6, -10), (10, -8), (10, -2)],
    "Theta":  [(8, 2), (0, 2), (-2, 0), (4, -8), (8, -10), (10, -2)],
    "Lambda": [(8, 2), (0, 2), (-2, 0), (6, -10), (10, -8), (10, -2)],
    "Xi":     [(4, 4), (0, 2), (-2, 0), (4, -8), (8, -10), (10, -2)],
    "Pi":     [(4, 4), (0, 2), (-2, 0), (6, -10), (10, -8), (10, -2)],
    "Sigma":  [(8, 2), (2, 4), (-2, -2), (6, -10), (10, -8), (10, -2)],
    "Phi":    [(8, 2), (0, 2), (-2, 0), (4, -8), (10, -8), (10, -2)],
    "Psi":    [(4, 4), (0, 2), (-2, 0), (4, -8), (10, -8), (10, -2)],
}

def hex_center(hx, hy):
    return (4 * hx + 2 * hy + 2, 2 * hy - 2 * hx)

def lat_rot60(vx, vy, steps):
    for _ in range(steps % 6):
        vx, vy = -vy, vx + vy
    return (vx, vy)

HEX_VERTS0 = [(-2, 2), (-2, 0), (0, -2), (2, -2), (2, 0), (0, 2)]

def build_templates():
    templates = {}
    for name in NAMES:
        children = SUPERTILE_CHILDS[name]
        marks = SUPERTILE_MARKS[name]
        dir_edges = {}
        vert_to_inc = {}
        for ci, (cname, rsteps, hx, hy) in enumerate(children):
            cx, cy = hex_center(hx, hy)
            verts = [(cx + rx, cy + ry) for vx, vy in HEX_VERTS0 for rx, ry in [lat_rot60(vx, vy, rsteps)]]
            for s in range(6):
                u, v = verts[s], verts[(s + 1) % 6]
                lbl = HEX_LABELS[cname][s]
                assert (u, v) not in dir_edges
                dir_edges[(u, v)] = (ci, s, lbl)
                vert_to_inc.setdefault(u, []).append((ci, s, (s - 1) % 6))

        seams = []
        seen_seams = set()
        bnext = {}
        for (u, v), (ci, si, lbl) in dir_edges.items():
            if (v, u) in dir_edges:
                cj, sj, lbl2 = dir_edges[(v, u)]
                assert lbl == opp_label(lbl2)
                key = tuple(sorted([(ci, si), (cj, sj)]))
                if key not in seen_seams:
                    seen_seams.add(key)
                    seams.append(((ci, si), (cj, sj)))
            else:
                bnext[u] = (v, ci, si, lbl)

        bdy_verts = set(bnext.keys())
        tri_verts = []
        for v, incs in vert_to_inc.items():
            if v not in bdy_verts:
                assert len(incs) == 3
                # Sort CCW around v in T(X): edge direction (rsteps + s) % 6 increases CCW
                incs_sorted = sorted(incs, key=lambda x: (children[x[0]][1] + x[1]) % 6)
                # Verify consecutive pairs share an edge in T(X):
                # In T(X), child k's outgoing side s goes away from v, and child (k+1)'s incoming side s_in comes INTO v along the same geometric segment!
                for k in range(3):
                    c_a, _, s_in_a = incs_sorted[k]
                    c_b, s_out_b, _ = incs_sorted[(k + 1) % 3]
                    # Check edge equality in dir_edges:
                    assert ((c_a, s_in_a), (c_b, s_out_b)) in seen_seams or ((c_b, s_out_b), (c_a, s_in_a)) in seen_seams
                # Notice: in T_bar(X) (children reflected once), CCW order around v reverses!
                # And each child corner in T(X) was (in_side=s_in, out_side=s_out).
                tri_verts.append(tuple((ci, s_in, s_out) for ci, s_out, s_in in incs_sorted))
            else:
                assert len(incs) <= 2

        curr = marks[0]
        walk = []
        for _ in range(len(bnext)):
            v, ci, si, lbl = bnext[curr]
            walk.append((curr, v, ci, si, lbl))
            curr = v
        assert curr == marks[0]
        midxs = [k for k, step in enumerate(walk) if step[0] in marks]
        assert [walk[k][0] for k in midxs] == marks

        side_decomps = [None] * 6
        corner_is_single_child = [None] * 6  # at start of canonical side s (between side s-1 and s): (True, ci, s_prev_child) or (False,)
        for m_i in range(6):
            side_orig = (6 - m_i) % 6
            a, b = midxs[m_i], midxs[(m_i + 1) % 6]
            seg = walk[a:b] if a < b else walk[a:] + walk[:b]
            side_decomps[side_orig] = [(x[2], x[3]) for x in reversed(seg)]
            # In walk (T(X)), vertex walk[b % len(walk)][0] is end of walk[b-1] (= first edge of canonical side_orig in T_bar)
            # and start of walk[b % len(walk)] (= last edge of canonical (side_orig - 1)%6 in T_bar)!
            step_before = walk[(b - 1) % len(walk)]
            step_after = walk[b % len(walk)]
            corner_is_single_child[side_orig] = (step_before[2] == step_after[2])

        templates[name] = {
            "children": children,
            "seams": seams,
            "tri_verts": tri_verts,
            "side_decomps": side_decomps,
            "corner_is_single_child": corner_is_single_child,
        }
    return templates

TEMPLATES = build_templates()

# ---------------------------------------------------------------------------
# 3. Exact Z[zeta_12] polygons for standard W and Gamma_0 (Mystic)
# ---------------------------------------------------------------------------

d_W = [0, 3, 5, 2, 4, 4, 6, 9, 7, 10, 8, 11, 1, 10]
W_VERTS = [(0, 0, 0, 0)]
for dk in d_W[:-1]:
    W_VERTS.append(zadd(W_VERTS[-1], Z[dk]))
assert zadd(W_VERTS[-1], Z[d_W[-1]]) == (0, 0, 0, 0)

B_rel = [(0, 0, 0, 0)]
for dk in d_W[:-1]:
    B_rel.append(zadd(B_rel[-1], Z[(dk + 1) % 12]))
shift_B = zsub(W_VERTS[1], B_rel[11])
B_VERTS = [zadd(p, shift_B) for p in B_rel]
for k in range(5):
    assert B_VERTS[(11 - k) % 14] == W_VERTS[1 + k]

GAMMA_VERTS = (
    [W_VERTS[i] for i in [9, 10, 11, 12, 13, 0, 1]] +
    [B_VERTS[i % 14] for i in [12, 13, 0, 1, 2, 3, 4, 5, 6]] +
    [W_VERTS[i] for i in [5, 6, 7, 8]]
)
GAMMA_CORNER_IDX = [0, 3, 6, 8, 14, 17]

SIGMA_SPUR = zadd(W_VERTS[11], zadd(Z[5], Z[3]))
SIGMA_MID = zadd(W_VERTS[11], Z[5])

TILE0_CORNERS_W_IDX = {
    "Delta":  [9, 11, 0, 2, 5, 7],
    "Theta":  [9, 11, 0, 1, 4, 6],
    "Lambda": [9, 11, 0, 2, 5, 6],
    "Xi":     [9, 12, 0, 1, 4, 6],
    "Pi":     [9, 12, 0, 2, 5, 6],
    "Phi":    [9, 11, 0, 2, 4, 6],
    "Psi":    [9, 12, 0, 2, 4, 6],
}

def get_tile0_spec(name):
    if name == "Gamma":
        corners = [GAMMA_VERTS[i] for i in GAMMA_CORNER_IDX]
        paths = []
        for s in range(6):
            a = GAMMA_CORNER_IDX[s]
            b = GAMMA_CORNER_IDX[(s + 1) % 6]
            pts = GAMMA_VERTS[a : b + 1] if a < b else GAMMA_VERTS[a:] + GAMMA_VERTS[: b + 1]
            paths.append(pts)
        return ([("even", W_VERTS), ("odd", B_VERTS)], corners, paths)
    if name == "Sigma":
        corners = [SIGMA_SPUR, W_VERTS[11], W_VERTS[0], W_VERTS[2], W_VERTS[5], W_VERTS[7]]
        paths = [
            [SIGMA_SPUR, SIGMA_MID, W_VERTS[11]],
            [W_VERTS[11], W_VERTS[12], W_VERTS[13], W_VERTS[0]],
            [W_VERTS[0], W_VERTS[1], W_VERTS[2]],
            [W_VERTS[2], W_VERTS[3], W_VERTS[4], W_VERTS[5]],
            [W_VERTS[5], W_VERTS[6], W_VERTS[7]],
            [W_VERTS[7], W_VERTS[8], W_VERTS[9], W_VERTS[10], W_VERTS[11], SIGMA_MID, SIGMA_SPUR],
        ]
        return ([("even", W_VERTS)], corners, paths)
    cidxs = TILE0_CORNERS_W_IDX[name]
    corners = [W_VERTS[i] for i in cidxs]
    paths = []
    for s in range(6):
        a, b = cidxs[s], cidxs[(s + 1) % 6]
        pts = W_VERTS[a : b + 1] if a < b else W_VERTS[a:] + W_VERTS[: b + 1]
        paths.append(pts)
    return ([("even", W_VERTS)], corners, paths)

TILE0_SPECS = {nm: get_tile0_spec(nm) for nm in NAMES}

# 134 compatible side pairs S
S_PAIRS = []
for i1, y in enumerate(NAMES):
    for s1 in range(6):
        l1 = HEX_LABELS[y][s1]
        for i2 in range(i1, len(NAMES)):
            z = NAMES[i2]
            s2_start = s1 if i2 == i1 else 0
            for s2 in range(s2_start, 6):
                if HEX_LABELS[z][s2] == opp_label(l1):
                    S_PAIRS.append(((y, s1), (z, s2)))
assert len(S_PAIRS) == 134
S_INDEX = {pair: idx for idx, pair in enumerate(S_PAIRS)}

def norm_pair(a, b):
    ka = (NAMES.index(a[0]), a[1])
    kb = (NAMES.index(b[0]), b[1])
    return (a, b) if ka <= kb else (b, a)

def apply_xform(pt, refl, r, t):
    if refl:
        pt = zconj(pt)
    return zadd(zrot(pt, r), t)

def compose_xform(outer_refl, outer_r, outer_t, inner_refl, inner_r, inner_t):
    if not outer_refl:
        return (inner_refl, (outer_r + inner_r) % 12, zadd(zrot(inner_t, outer_r), outer_t))
    return (not inner_refl, (outer_r - inner_r) % 12, zadd(zrot(zconj(inner_t), outer_r), outer_t))

def find_glue_xform(path_target, path_src, src_refl):
    rev_t = list(reversed(path_target))
    src0 = [zconj(p) if src_refl else p for p in path_src]
    if len(rev_t) != len(src0):
        return None
    dt = zsub(rev_t[1], rev_t[0])
    ds = zsub(src0[1], src0[0])
    for r in range(12):
        if zrot(ds, r) == dt:
            t = zsub(rev_t[0], zrot(src0[0], r))
            if all(zadd(zrot(p, r), t) == q for p, q in zip(src0, rev_t)):
                return (r, t)
    return None

def polys_overlap(poly1, poly2):
    def pip(pt, poly):
        px, py = to_2cart_qsqrt3(pt)
        inside = False
        n = len(poly)
        for i in range(n):
            ax, ay = to_2cart_qsqrt3(poly[i])
            bx, by = to_2cart_qsqrt3(poly[(i + 1) % n])
            ay_s, by_s = q3_sign(q3_sub(ay, py)), q3_sign(q3_sub(by, py))
            if ay_s == 0 and by_s == 0:
                continue
            if (ay_s > 0) != (by_s > 0):
                dx = q3_sub(bx, ax)
                dy = q3_sub(by, ay)
                lhs = q3_mul(q3_sub(ax, px), dy)
                rhs = q3_mul(q3_sub(ay, py), dx)
                diff = q3_sub(lhs, rhs)
                if dy[0] != 0 or dy[1] != 0:
                    s_diff = q3_sign(diff) * q3_sign(dy)
                    if s_diff > 0:
                        inside = not inside
                    elif s_diff == 0:
                        return False
        return inside

    def seg_cross_strict(a1, a2, b1, b2):
        s1 = q3_sign(poly_cross2(a1, a2, b1))
        s2 = q3_sign(poly_cross2(a1, a2, b2))
        s3 = q3_sign(poly_cross2(b1, b2, a1))
        s4 = q3_sign(poly_cross2(b1, b2, a2))
        return s1 * s2 < 0 and s3 * s4 < 0

    n1, n2 = len(poly1), len(poly2)
    for i in range(n1):
        a1, a2 = poly1[i], poly1[(i + 1) % n1]
        for j in range(n2):
            b1, b2 = poly2[j], poly2[(j + 1) % n2]
            if seg_cross_strict(a1, a2, b1, b2):
                return True
    bset2 = set(poly2)
    for v in poly1:
        if v not in bset2 and not any(
            q3_sign(poly_cross2(poly2[j], poly2[(j + 1) % n2], v)) == 0
            and q3_sign(q3_sub(
                z_sqnorm_qsqrt3(zsub(poly2[(j + 1) % n2], poly2[j])),
                q3_add(z_sqnorm_qsqrt3(zsub(v, poly2[j])), z_sqnorm_qsqrt3(zsub(poly2[(j + 1) % n2], v)))
            )) >= 0
            for j in range(n2)
        ):
            if pip(v, poly2):
                return True
    return False

print("[1] Checking all 134 compatible edge pairs S in Z[zeta_12]...")
for (y, s1), (z, s2) in S_PAIRS:
    polys_y, _, paths_y = TILE0_SPECS[y]
    polys_z, _, paths_z = TILE0_SPECS[z]
    xf = find_glue_xform(paths_y[s1], paths_z[s2], False)
    assert xf is not None, f"Edge mismatch on {((y, s1), (z, s2))}"
    r, t = xf
    for _, py in polys_y:
        for _, pz in polys_z:
            pz_t = [apply_xform(p, False, r, t) for p in pz]
            assert not polys_overlap(py, pz_t), f"Overlap on {((y, s1), (z, s2))}"
print("    PASS: 134/134 compatible seams glue congruently without overlap.")

# ---------------------------------------------------------------------------
# 4. Lemma 3.1 (Period-2 Boundary Stabilization) & Lemma 3.2 (V_45)
# ---------------------------------------------------------------------------

def refl_corner(c):
    return (c[0], c[2], c[1])

def refl_tup(tup):
    return tuple(refl_corner(c) for c in reversed(tup))

def refl_side_data(sdata):
    return {
        "start": refl_tup(sdata["end"]),
        "end": refl_tup(sdata["start"]),
        "pieces": [refl_tup(p) for p in reversed(sdata["pieces"])],
    }

def canon_tri_with_chirality(tri, parity):
    """Canonicalize 3-corner vertex to even-chirality (unreflected) CCW form.
    If parity == 1 (currently in reflected level), reflect once to even-chirality."""
    if parity == 1:
        tri = tuple(refl_corner(c) for c in reversed(tri))
    return min(tri[k:] + tri[:k] for k in range(3))

def check_lemmas_and_build_transfer():
    sides = {0: {}}
    for x in NAMES:
        sides[0][x] = [
            {"start": ((x, (s - 1) % 6, s),), "end": ((x, s, (s + 1) % 6),), "pieces": []}
            for s in range(6)
        ]

    V_inside = {0: {x: set() for x in NAMES}}
    corners_table = {}
    corners_table[0] = {x: [(sides[0][x][s]["start"], sides[0][x][s]["end"]) for s in range(6)] for x in NAMES}

    V_raw_level = {0: set()}
    V_even_level = {0: set()}

    for n in range(1, 7):
        sides[n] = {}
        corners_table[n] = {}
        V_inside[n] = {}
        v_raw = set()
        v_even = set()

        for x in NAMES:
            tpl = TEMPLATES[x]
            ch = tpl["children"]
            sides[n][x] = []
            corners_table[n][x] = []

            # Build macro-corners[0..5] of X_n:
            # Corner s sits between side (s-1)%6 and side s of X_n.
            macro_c = []
            for s in range(6):
                ci_prev, si_prev = tpl["side_decomps"][(s - 1) % 6][-1]
                ci_next, si_next = tpl["side_decomps"][s][0]
                pc_prev = refl_side_data(sides[n - 1][ch[ci_prev][0]][si_prev])
                pc_next = refl_side_data(sides[n - 1][ch[ci_next][0]][si_next])
                if tpl["corner_is_single_child"][s]:
                    assert pc_prev["end"] == pc_next["start"]
                    ctup = pc_next["start"]
                else:
                    ctup = pc_prev["end"] + pc_next["start"]
                assert 1 <= len(ctup) <= 2, f"Macro corner deg {len(ctup)} > 2 at n={n}, {x}, s={s}"
                macro_c.append(ctup)

            # Macro sides of X_n: children in T_bar(X) are reflected once relative to level n-1!
            for s in range(6):
                decomp = tpl["side_decomps"][s]
                pcs = [refl_side_data(sides[n - 1][ch[ci][0]][si]) for ci, si in decomp]
                st = macro_c[s]
                en = macro_c[(s + 1) % 6]
                iv = []
                for idx, pc in enumerate(pcs):
                    iv.extend(pc["pieces"])
                    if idx + 1 < len(pcs):
                        ci_a, _ = decomp[idx]
                        ci_b, _ = decomp[idx + 1]
                        if ci_a == ci_b:
                            # Same child hexagon: single shared vertex corner!
                            assert pc["end"] == pcs[idx + 1]["start"]
                            iv.append(pc["end"])
                        else:
                            iv.append(pc["end"] + pcs[idx + 1]["start"])
                for v in iv:
                    assert 1 <= len(v) <= 2, f"Boundary vertex degree {len(v)} > 2 at n={n}, {x}, s={s}"
                sides[n][x].append({"start": st, "end": en, "pieces": iv})
                corners_table[n][x].append((st, en))

            # Collect interior 3-hex vertices of X_n (in X_n's local orientation = T_bar(X)):
            vx = set()
            for yc, _, _, _ in ch:
                for tri in V_inside[n - 1][yc]:
                    rtri = tuple(refl_corner(c) for c in reversed(tri))
                    vx.add(min(rtri[k:] + rtri[:k] for k in range(3)))
            for tri in tpl["tri_verts"]:
                cs = []
                for ci, s_in, s_out in reversed(tri):
                    ctup = refl_tup(sides[n - 1][ch[ci][0]][s_out]["start"])
                    assert len(ctup) == 1, f"Macro interior vertex child corner deg {len(ctup)} != 1"
                    cs.append(ctup[0])
                vx.add(min(tuple(cs[k:] + cs[:k]) for k in range(3)))
            for (ci, si), (cj, sj) in tpl["seams"]:
                s1 = refl_side_data(sides[n - 1][ch[ci][0]][si])
                s2 = refl_side_data(sides[n - 1][ch[cj][0]][sj])
                p1 = s1["pieces"]
                p2 = list(reversed(s2["pieces"]))
                assert len(p1) == len(p2), f"Seam piece mismatch at n={n}: {len(p1)} vs {len(p2)}"
                for v1, v2 in zip(p1, p2):
                    deg = len(v1) + len(v2)
                    assert 2 <= deg <= 3, f"Interior seam deg={deg} at n={n}"
                    if deg == 3:
                        combined = tuple(reversed(v1)) + tuple(reversed(v2))
                        vx.add(min(combined[k:] + combined[:k] for k in range(3)))

            V_inside[n][x] = vx
            v_raw |= vx
            for tri in vx:
                v_even.add(canon_tri_with_chirality(tri, n % 2))

        V_raw_level[n] = v_raw
        V_even_level[n] = v_even

    # Verify Lemma 3.1: corners(4) == corners(2) and corners(5) == corners(3)
    assert corners_table[4] == corners_table[2], "Lemma 3.1 corners(4) != corners(2)"
    assert corners_table[5] == corners_table[3], "Lemma 3.1 corners(5) != corners(3)"
    assert corners_table[6] == corners_table[4], "Lemma 3.1 corners(6) != corners(4)"
    print("[2] PASS Lemma 3.1: max boundary degree <= 2; corners(4)==corners(2) and corners(5)==corners(3).")

    # Verify Lemma 3.2: |V_even(4)| = |V_even(5)| = |V_even(6)| = 45 (and check V_raw sizes too!)
    for n in range(1, 7):
        print(f"    n={n}: |V_even|={len(V_even_level[n])}, |V_raw|={len(V_raw_level[n])}")
    assert len(V_even_level[4]) == 45 and len(V_even_level[5]) == 45 and len(V_even_level[6]) == 45

    V_45 = sorted(V_even_level[4])
    for tri in V_45:
        gamma_cnt = sum(1 for c in tri if c[0] == "Gamma")
        assert gamma_cnt <= 1, f"Gamma appears {gamma_cnt} times in {tri}"

    # Verify Gamma never meets another Gamma along an edge or vertex:
    # Check Gamma boundary appearances in X_1 (for all X in NAMES)
    gamma_bdy_sides = set()
    for x in NAMES:
        ch = TEMPLATES[x]["children"]
        for s in range(6):
            for ci, si in TEMPLATES[x]["side_decomps"][s]:
                if ch[ci][0] == "Gamma":
                    gamma_bdy_sides.add(HEX_LABELS["Gamma"][si])
    # Check no label and its opposite both appear in gamma_bdy_sides
    for lbl in gamma_bdy_sides:
        assert opp_label(lbl) not in gamma_bdy_sides, f"Gamma boundary {lbl} and opp both occur!"
    print(f"[3] PASS Lemma 3.2: |V(4)|=|V(5)|=|V(6)|=45; max Gamma=1; Gamma bdy labels={sorted(gamma_bdy_sides)} (no opposite pairs).")

    return sides, V_45

SIDES, V_45 = check_lemmas_and_build_transfer()

# ---------------------------------------------------------------------------
# 5. Theorem 3.3: Z[zeta_12] Realization of all 45 configs in V_45 & Direct Tilings Delta_3, Delta_4
# ---------------------------------------------------------------------------

def is_star_triple_polys(p1, p2, p3):
    """Given 3 Spectre 14-gons, check if there is a common boundary point P such that
    rotation by +120 or -120 around P cycles (p1, p2, p3)."""
    s1, s2, s3 = set(p1), set(p2), set(p3)
    common = s1 & s2 & s3
    if not common:
        return None
    for P in common:
        # Check if rotating p1 around P by 120 deg (Z[4]) gives p2 (as a set of vertices and ordered polygon)
        rot_p1 = set(zadd(zrot(zsub(v, P), 4), P) for v in p1)
        if rot_p1 == s2:
            rot_p2 = set(zadd(zrot(zsub(v, P), 4), P) for v in p2)
            if rot_p2 == s3:
                return P
        elif rot_p1 == s3:
            rot_p3 = set(zadd(zrot(zsub(v, P), 4), P) for v in p3)
            if rot_p3 == s2:
                return P
    return None

def star_triple_type_from_vertex_distances(P, poly):
    # Max |v - P|^2 over vertices v of poly using exact Z[sqrt(3)] comparison:
    best = (0, 0)
    for v in poly:
        d2 = z_sqnorm_qsqrt3(zsub(v, P))
        if q3_sign(q3_sub(d2, best)) > 0:
            best = d2
    return best

print("[4] Testing Z[zeta_12] realization of all 45 interior 3-hexagon vertices in V_45...")
L_CORNER = ("eps_p_eps_m", 1, 2)  # incoming side 1 (eps+), outgoing side 2 (eps-) for Pi, Psi
S_CORNER = ("eps_m_eps_p", 2, 3)  # incoming side 2 (eps-), outgoing side 3 (eps+) for Phi

def classify_tri_expected(tri):
    # Check if all 3 corners are Pi/Psi at (1, 2) or all 3 are Phi at (2, 3)
    if all(c[0] in ("Pi", "Psi") and (c[1], c[2]) == (1, 2) for c in tri):
        return "L"
    if all(c[0] == "Phi" and (c[1], c[2]) == (2, 3) for c in tri):
        return "S"
    return None

v45_L_cnt = 0
v45_S_cnt = 0
for tri in V_45:
    # Build the 3 even-chirality tiles around the common vertex P=(0,0,0,0)!
    # Each c = (tile_name, in_s, out_s) has out_s = (in_s + 1) % 6 (since even chirality!).
    # Place c0 at (0,0,0,0) with its corner (in_s, out_s) shifted to origin (0,0,0,0).
    # Then glue c1's in_s against c0's out_s, and glue c2's in_s against c1's out_s!
    # Verify c2's out_s glues cleanly back onto c0's in_s!
    tri_cw = list(reversed(tri))
    placed_spectres = []
    specs0 = [TILE0_SPECS[c[0]] for c in tri_cw]
    # Place tile 0:
    polys0, corners0, paths0 = specs0[0]
    t0 = zsub((0, 0, 0, 0), corners0[tri_cw[0][2]])  # out_s index IS the vertex between in_s and out_s!
    xforms = [(0, t0)]
    for ch_type, pv in polys0:
        placed_spectres.append((ch_type, [apply_xform(p, False, 0, t0) for p in pv]))

    # Glue tile 1 (in_s = tri_cw[1][1]) onto tile 0's out_s (= tri_cw[0][2]):
    for idx in (1, 2):
        prev_r, prev_t = xforms[idx - 1]
        prev_out_s = tri_cw[idx - 1][2]
        prev_path = [apply_xform(p, False, prev_r, prev_t) for p in specs0[idx - 1][2][prev_out_s]]
        cur_in_s = tri_cw[idx][1]
        xf = find_glue_xform(prev_path, specs0[idx][2][cur_in_s], False)
        assert xf is not None, f"Failed to glue {tri} at step {idx}"
        xforms.append(xf)
        for ch_type, pv in specs0[idx][0]:
            placed_spectres.append((ch_type, [apply_xform(p, False, xf[0], xf[1]) for p in pv]))

    # Check closure: tile 2's out_s matches tile 0's in_s reversed!
    r2, t2 = xforms[2]
    p2_out = [apply_xform(p, False, r2, t2) for p in specs0[2][2][tri_cw[2][2]]]
    p0_in = [apply_xform(p, False, 0, t0) for p in specs0[0][2][tri_cw[0][1]]]
    assert p2_out == list(reversed(p0_in)), f"Cycle failed to close on {tri}"
    # Check pairwise non-overlap among the placed Spectres
    for a in range(len(placed_spectres)):
        for b in range(a + 1, len(placed_spectres)):
            assert not polys_overlap(placed_spectres[a][1], placed_spectres[b][1]), f"Overlap in {tri}"

    # Check ALL 3-element subsets of placed_spectres for a 120-deg star triple
    even_only = [p for ch_t, p in placed_spectres if ch_t == "even"]
    odd_only = [p for ch_t, p in placed_spectres if ch_t == "odd"]
    found_stars = []
    from itertools import combinations
    for grp in (even_only, odd_only):
        for p1, p2, p3 in combinations(grp, 3):
            P = is_star_triple_polys(p1, p2, p3)
            if P is not None:
                d2 = star_triple_type_from_vertex_distances(P, p1)
                found_stars.append((P, d2))

    exp = classify_tri_expected(tri)
    if exp == "L":
        assert len(found_stars) == 1 and found_stars[0][1] == (10, 5), f"L mismatch: {tri}, {found_stars}"
        v45_L_cnt += 1
    elif exp == "S":
        assert len(found_stars) == 1 and found_stars[0][1] == (10, 3), f"S mismatch: {tri}, {found_stars}"
        v45_S_cnt += 1
    else:
        assert len(found_stars) == 0, f"Unexpected star triple in {tri}: {found_stars}"

assert v45_L_cnt == 3 and v45_S_cnt == 1
print(f"    PASS Theorem 3.3 (V_45): {v45_L_cnt} L-configs (R_L^2 = 10+5*sqrt(3)), {v45_S_cnt} S-config (R_S^2 = 10+3*sqrt(3)), {45 - v45_L_cnt - v45_S_cnt}/45 have 0 star triples.")

# ---------------------------------------------------------------------------
# 6. Full Z[zeta_12] construction of Delta_0..Delta_4 (up to 4401 Spectres!)
#    and direct exhaustive star-triple count on Delta_3 (559) and Delta_4 (4401)
# ---------------------------------------------------------------------------

def build_supertile_geom(max_n=4):
    """Build exact level-n supertile specs in Z[zeta_12]:
    returns geom[n][name] = (side_paths_6, tile_xforms)
    where tile_xforms is list of (level0_tile_name, refl, r, t) OR list of Spectre (parity, refl, r, t)."""
    geom = {0: {}}
    for nm in NAMES:
        _, _, paths = TILE0_SPECS[nm]
        # Store each level-n Spectre directly as (is_odd_tile, refl, r, t) relative to W_VERTS (or B_VERTS for odd)
        # Wait: B_VERTS is rotated+translated W_VERTS (with odd rotation!), so BOTH even and odd Spectres are rigid images of W_VERTS!
        # Let's represent every Spectre as (refl, r, t) acting on W_VERTS!
        # Check B_VERTS relative to W_VERTS: B_VERTS[k] = W_VERTS[k] rotated by +1 (30 deg) + shift_B!
        if nm == "Gamma":
            sp_list = [(False, 0, (0, 0, 0, 0)), (False, 1, shift_B)]
        else:
            sp_list = [(False, 0, (0, 0, 0, 0))]
        geom[0][nm] = (paths, sp_list)

    for n in range(1, max_n + 1):
        geom[n] = {}
        for x in NAMES:
            tpl = TEMPLATES[x]
            ch = tpl["children"]
            # Build children placement in T_bar(X) by BFS across TEMPLATES[x]["seams"]!
            # Child 0 placed with refl=True, r=0, t=(0,0,0,0).
            adj = {ci: [] for ci in range(len(ch))}
            for (ci, si), (cj, sj) in tpl["seams"]:
                adj[ci].append((si, cj, sj))
                adj[cj].append((sj, ci, si))

            placed_ch = {0: (True, 0, (0, 0, 0, 0))}
            q = deque([0])
            while q:
                ci = q.popleft()
                crefl, cr, ct = placed_ch[ci]
                c_paths, _ = geom[n - 1][ch[ci][0]]
                for si, cj, sj in adj[ci]:
                    path_i = [apply_xform(p, crefl, cr, ct) for p in c_paths[si]]
                    # Note: when children are reflected once (crefl=True), path_i runs in reflected CCW order!
                    # Wait: in T_bar(X), side si of child ci (with crefl=True) runs OPPOSITE to side sj of child cj (with crefl=True)!
                    # Wait: apply_xform(p, True, cr, ct) transforms p_0, p_1, ..., p_k to reflected points P_0, ..., P_k,
                    # which traverses the boundary CLOCKWISE on the reflected tile!
                    # Since BOTH child ci and child cj are reflected, P_0 -> ... -> P_k on ci runs OPPOSITE to Q_0 -> ... -> Q_k on cj!
                    # So find_glue_xform(path_i, cj_paths[sj], src_refl=True) matches reversed(path_i) to Q_0 -> ... -> Q_k!
                    cj_paths, _ = geom[n - 1][ch[cj][0]]
                    xf = find_glue_xform(path_i, cj_paths[sj], True)
                    assert xf is not None, f"Failed seam BFS at n={n} in {x}: ({ci},{si})->({cj},{sj})"
                    new_xf = (True, xf[0], xf[1])
                    if cj in placed_ch:
                        assert placed_ch[cj] == new_xf, f"Cycle holonomy mismatch at n={n} in {x}!"
                    else:
                        placed_ch[cj] = new_xf
                        q.append(cj)
            assert len(placed_ch) == len(ch)

            # Extract the 6 canonical CCW outer side_paths of X_n!
            # In T_bar(X), side s visits side_decomps[s] in order (ci, c_side),
            # where on reflected child ci (crefl=True), c_side runs backwards from end to start!
            out_paths = []
            for s in range(6):
                pts = []
                for idx, (ci, c_side) in enumerate(tpl["side_decomps"][s]):
                    crefl, cr, ct = placed_ch[ci]
                    c_paths, _ = geom[n - 1][ch[ci][0]]
                    seg = [apply_xform(p, crefl, cr, ct) for p in reversed(c_paths[c_side])]
                    if idx == 0:
                        pts.extend(seg)
                    else:
                        assert pts[-1] == seg[0], f"Boundary continuity break at n={n}, {x}, s={s}"
                        pts.extend(seg[1:])
                out_paths.append(pts)

            # Verify side paths form closed loop!
            for s in range(6):
                assert out_paths[s][-1] == out_paths[(s + 1) % 6][0]

            # Assemble Spectres if n <= 4 and x == "Delta" (or needed for Delta_4)
            spectres = []
            for ci in range(len(ch)):
                crefl, cr, ct = placed_ch[ci]
                _, c_sp = geom[n - 1][ch[ci][0]]
                for sp_refl, sp_r, sp_t in c_sp:
                    spectres.append(compose_xform(crefl, cr, ct, sp_refl, sp_r, sp_t))
            geom[n][x] = (out_paths, spectres)
    return geom

def count_direct_star_triples(spectres):
    # Transform W_VERTS for all spectres and verify distinct tiles (no duplicates / no overlap? Check vertex-bucket fast!)
    polys = []
    vert_to_tiles = {}
    edge_mid_check = set()
    for tid, (refl, r, t) in enumerate(spectres):
        poly = tuple(apply_xform(v, refl, r, t) for v in W_VERTS)
        polys.append(poly)
        for v in poly:
            vert_to_tiles.setdefault(v, []).append(tid)
        # Quick edge-interior parity check: no midpoint coincides with wrong orientation
        for k in range(14):
            a, b = poly[k], poly[(k + 1) % 14]
            mid2 = zadd(a, b)
            edge_mid_check.add(mid2)

    # Check every vertex shared by >= 3 tiles (and check pairwise 120-deg triples among tiles sharing P)
    # Wait: could a star triple share a boundary point P that is NOT a vertex of all 3 tiles?
    # Note: in a vertex-to-vertex Tile(1,1) tiling (collinear edge midpoint included as vertex W_5!),
    # any common boundary point P of 3 tiles rotated by 120 deg around P MUST map boundary to boundary.
    # For completeness, also check midpoints of edges (2*P in Z[zeta_12]) just in case!
    found = set()
    cnt_L = 0
    cnt_S = 0
    for P, tids in vert_to_tiles.items():
        if len(tids) < 3:
            continue
        from itertools import combinations
        for i1, i2, i3 in combinations(tids, 3):
            key = tuple(sorted((i1, i2, i3)))
            if key in found:
                continue
            p1, p2, p3 = polys[i1], polys[i2], polys[i3]
            if is_star_triple_polys(p1, p2, p3) is not None:
                found.add(key)
                d2 = star_triple_type_from_vertex_distances(P, p1)
                if d2 == (10, 5):
                    cnt_L += 1
                elif d2 == (10, 3):
                    cnt_S += 1
                else:
                    raise AssertionError(f"Unknown star triple d2={d2}")
    # Also verify no edge midpoint is shared by 3 tiles!
    mid_to_tiles = {}
    for tid, poly in enumerate(polys):
        for k in range(14):
            m = zadd(poly[k], poly[(k + 1) % 14])
            mid_to_tiles.setdefault(m, []).append(tid)
    assert all(len(v) <= 2 for v in mid_to_tiles.values())
    return len(polys), cnt_L, cnt_S

print("[5] Constructing exact Z[zeta_12] Spectre patches Delta_0..Delta_4...")
GEOM = build_supertile_geom(4)
for n, exp_tiles, exp_L, exp_S in [(0, 1, 0, 0), (1, 9, 0, 0), (2, 71, 0, 0), (3, 559, 18, 10), (4, 4401, 236, 136)]:
    n_tiles, cL, cS = count_direct_star_triples(GEOM[n]["Delta"][1])
    assert (n_tiles, cL, cS) == (exp_tiles, exp_L, exp_S), f"Delta_{n}: got {(n_tiles, cL, cS)}"
    print(f"    Delta_{n}: {n_tiles:4d} Spectres -> {cL} major (L) + {cS} minor (S) = {cL + cS} star triples (PASS)")

# ---------------------------------------------------------------------------
# 7. Exact Combinatorial Star Triple Counter vs Section 4 Transfer Matrix
# ---------------------------------------------------------------------------

def is_L_tri(tri):
    return all(c[0] in ("Pi", "Psi") and (c[1], c[2]) == (1, 2) for c in tri)

def is_S_tri(tri):
    return all(c[0] == "Phi" and (c[1], c[2]) == (2, 3) for c in tri)

def count_tri_type(tri):
    # Note: tri is already normalized (even chirality) OR raw (if odd level, reflected once!).
    # Wait: check whether reflecting swaps (1,2) <-> (2,1) and (2,3) <-> (3,2)!
    # So we normalize chirality to even before checking is_L_tri / is_S_tri!
    return (1 if is_L_tri(tri) else 0, 1 if is_S_tri(tri) else 0)

def compute_exact_v_and_transfer():
    # Compute exact state vector v_n^(L), v_n^(S) for n=0..6 directly from combinatorial definitions,
    # AND independently build the 143x143 matrix A and period-2 offsets b_even, b_odd!
    def check_tri_parity(tri, parity):
        return count_tri_type(canon_tri_with_chirality(tri, parity))

    # Exact direct counts for n=0..6:
    # interior[n][X] = (cnt_L, cnt_S) strictly inside X_n
    # seam[n][s_idx] = (cnt_L, cnt_S) strictly along interior of glued pair ((Y_n, s1), (Z_n, s2))
    interior = {0: {x: (0, 0) for x in NAMES}}
    seam_counts = {0: [(0, 0) for _ in range(134)]}

    for n in range(1, 7):
        interior[n] = {}
        for x in NAMES:
            tpl = TEMPLATES[x]
            ch = tpl["children"]
            cL, cS = 0, 0
            # 1) Children:
            for yc, _, _, _ in ch:
                dL, dS = interior[n - 1][yc]
                cL += dL
                cS += dS
            # 2) Interior seams of X_1:
            for (ci, si), (cj, sj) in tpl["seams"]:
                pair = norm_pair((ch[ci][0], si), (ch[cj][0], sj))
                dL, dS = seam_counts[n - 1][S_INDEX[pair]]
                cL += dL
                cS += dS
            # 3) 3-child interior macro-vertices of X_1:
            for tri in tpl["tri_verts"]:
                # In T_bar(X) (level n parity = n%2, but here we compute vertex directly at level n-1 pieces!):
                # Wait: sides[n-1][ch[ci][0]][s_out]["start"] has (n-1)%2 chirality!
                # Reflected to T_bar(X) gives level n chirality!
                cs = [refl_tup(SIDES[n - 1][ch[ci][0]][s_out]["start"])[0] for ci, _, s_out in reversed(tri)]
                dL, dS = check_tri_parity(tuple(cs), n % 2)
                cL += dL
                cS += dS
            interior[n][x] = (cL, cS)

        seam_counts[n] = []
        for (y, s1), (z, s2) in S_PAIRS:
            # Glue side s1 of Y_n against side s2 of Z_n!
            # Each macro-side at level n is formed from level-(n-1) reflected children in side_decomps!
            # Wait: along ((Y_n, s1), (Z_n, s2)), BOTH Y_n and Z_n are at level n (so both have pieces in SIDES[n]!).
            # Even better: SIDES[n][y][s1]["pieces"] vs reversed(SIDES[n][z][s2]["pieces"])!
            p1 = SIDES[n][y][s1]["pieces"]
            p2 = list(reversed(SIDES[n][z][s2]["pieces"]))
            assert len(p1) == len(p2)
            sL, sS = 0, 0
            for v1, v2 in zip(p1, p2):
                if len(v1) + len(v2) == 3:
                    combined = tuple(reversed(v1)) + tuple(reversed(v2))
                    dL, dS = check_tri_parity(combined, n % 2)
                    sL += dL
                    sS += dS
            seam_counts[n].append((sL, sS))

    # Now build the 143x143 linear matrix A directly from child & seam decompositions!
    # State vector ordering: 0..8 = NAMES, 9..142 = S_PAIRS
    dim = 9 + 134
    assert dim == 143
    A = [[0] * dim for _ in range(dim)]
    for xi, x in enumerate(NAMES):
        tpl = TEMPLATES[x]
        ch = tpl["children"]
        for yc, _, _, _ in ch:
            yi = NAMES.index(yc)
            A[xi][yi] += 1
        for (ci, si), (cj, sj) in tpl["seams"]:
            pair = norm_pair((ch[ci][0], si), (ch[cj][0], sj))
            A[xi][9 + S_INDEX[pair]] += 1

    # Seam transition rows in A:
    # Along seam ((Y_{n+1}, s1), (Z_{n+1}, s2)), Y's boundary decomposes into child sides side_decomps[s1]
    # and Z's boundary (reversed) decomposes into reversed(side_decomps[s2])!
    # Wait: how do the child sides along Y_{n+1} match child sides along Z_{n+1}?
    # At n=0, a child side at level 1 has length 1 (one child hexagon). Wait: at level n >= 1,
    # a child side (U_n, su) has the SAME number of level-0 edges? WAIT A SECOND!
    # Does a child side along (Y_{n+1}, s1) ALWAYS align 1-to-1 with a child side along (Z_{n+1}, s2),
    # OR can 1 child side of Y_{n+1} span MULTIPLE child sides of Z_{n+1}?!
    # TEST THAT CAREFULLY! Look at Delta side 0 (len 5) vs Theta side 0 (len 5) vs Pi side 2 (len 4):
    # What about Gamma side 3 (deltaminus, len 5 children: [Pi.4, De.2, De.3, Th.1, Th.2])
    # vs Sigma side 5 (deltaplus, len 5 children: [La.4, Ga.5, Ga.0, Xi.1, Xi.2])?!
    # CHECK THEIR LEVEL-n EDGE LENGTHS!
    # Wait: Gamma side 3 has Pi.4(theta-) + De.2(eps-) + De.3(alpha+) + Th.1(beta+) + Th.2(theta+).
    # Reversed Sigma side 5 has Xi.2(theta+) + Xi.1(eps+) + Ga.0(alpha-) + Ga.5(beta-) + La.4(theta-)!
    # Notice EACH PAIR OF OPPOSITE CHILDREN HAS OPPOSITE EDGE LABELS:
    # Pi.4(theta-) <-> Xi.2(theta+), De.2(eps-) <-> Xi.1(eps+), De.3(alpha+) <-> Ga.0(alpha-),
    # Th.1(beta+) <-> Ga.5(beta-), Th.2(theta+) <-> La.4(theta-)!!
    #Wait: is THAT true for ALL 134 compatible seams?! Let's ASSERT IT RIGHT HERE!
    for sidx, ((y, s1), (z, s2)) in enumerate(S_PAIRS):
        d1 = TEMPLATES[y]["side_decomps"][s1]
        d2 = list(reversed(TEMPLATES[z]["side_decomps"][s2]))
        assert len(d1) == len(d2), f"Seam {(y,s1),(z,s2)} child lengths differ: {len(d1)} vs {len(d2)}"
        ch_y = TEMPLATES[y]["children"]
        ch_z = TEMPLATES[z]["children"]
        for (ci, csi), (cj, csj) in zip(d1, d2):
            yc = ch_y[ci][0]
            zc = ch_z[cj][0]
            assert HEX_LABELS[yc][csi] == opp_label(HEX_LABELS[zc][csj])
            pair = norm_pair((yc, csi), (zc, csj))
            A[9 + sidx][9 + S_INDEX[pair]] += 1

    # Helper to extract v_n^(L) and v_n^(S) vectors
    def get_v(n, kind):
        idx = 0 if kind == "L" else 1
        vec = [interior[n][x][idx] for x in NAMES] + [seam_counts[n][i][idx] for i in range(134)]
        return vec

    def mat_vec(M, v):
        return [sum(row[j] * v[j] for j in range(len(v))) for row in M]

    def vec_sub(u, v):
        return [a - b for a, b in zip(u, v)]

    # Verify Lemma 4.1 / Period-2 offset stabilization: b_n = v_{n+1} - A v_n!
    # PROOF.md L76-77: b_2 == b_4 and b_3 == b_5!
    for kind in ("L", "S"):
        v = {n: get_v(n, kind) for n in range(7)}
        b = {n: vec_sub(v[n + 1], mat_vec(A, v[n])) for n in range(6)}
        assert b[2] == b[4], f"{kind}: b_2 != b_4"
        assert b[3] == b[5], f"{kind}: b_3 != b_5"
    print("[6] PASS Transfer Matrix A (143x143) & period-2 offsets: b_2==b_4 and b_3==b_5 for both L and S.")
    return interior, seam_counts, A, get_v

INTERIOR, SEAM_COUNTS, A_MAT, get_v = compute_exact_v_and_transfer()

# Check Delta_0..Delta_6 against live OEIS A400813 (major L) & A400814 (minor S) & A400812!
OEIS_A400813 = [0, 0, 0, 18, 236, 2276, 19708, 162758, 1313592, 10478312, 83073496, 656484378,
                5178861028, 40817016588, 321537782164, 2532249895438, 19939700510704,
                156999075362384, 1236111026206512, 9732135350734498, 76622014769266780, 603248400978233780]
OEIS_A400814 = [0, 0, 0, 10, 136, 1328, 11560, 95706, 773392, 6173216, 48958800, 386964842,
                3052977048, 24063187664, 189564085880, 1492922081978, 11755814461984,
                92562073764672, 728776698150560, 5737803681571274, 45174297357440680, 355659305760169840]
OEIS_A400812 = [0, 0, 0, 28, 372, 3604, 31268, 258464, 2086984, 16651528, 132032296, 1043449220]
OEIS_A057080 = [1, 9, 71, 559, 4401, 34649, 272791, 2147679, 16908641, 133121449, 1048062951,
                8251382159, 64962994321, 511452572409, 4026657584951, 31701808107199,
                249587807272641, 1965000650073929, 15470417393318791, 121798338496476399]
OEIS_A099919 = [0, 2, 10, 44, 188, 798, 3382, 14328, 60696, 257114, 1089154, 4613732,
                19544084, 82790070, 350704366, 1485607536, 6293134512, 26658145586,
                112925716858, 478361013020, 2026369768940]

for n in range(7):
    for x in NON_GAMMA:
        cL, cS = INTERIOR[n][x]
        assert cL == OEIS_A400813[n] and cS == OEIS_A400814[n], f"n={n}, {x}: got {(cL, cS)}"
print("[7] PASS Combinatorial counts n=0..6 match OEIS A400813, A400814, A400812 identically across all 8 non-Gamma X!")

# ---------------------------------------------------------------------------
# 8. Reachable 60-dim subspace, Krylov minimal poly q(z), and exact Rational GFs
# ---------------------------------------------------------------------------

# Reachable indices from rows 1..8 (NON_GAMMA)
reach = set(range(1, 9))
q = deque(range(1, 9))
while q:
    r = q.popleft()
    for c in range(143):
        if A_MAT[r][c] != 0 and c not in reach:
            reach.add(c)
            q.append(c)
reach = sorted(reach)
assert len(reach) == 60, f"Expected 60 reachable states, got {len(reach)}"
r_pos = {orig: idx for idx, orig in enumerate(reach)}
A_r = [[A_MAT[r][c] for c in reach] for r in reach]

# Compute A_r^2
def mat_mul(M1, M2):
    n = len(M1)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if M1[i][k] == 0:
                continue
            aik = M1[i][k]
            for j in range(n):
                res[i][j] += aik * M2[k][j]
    return res

A_r2 = mat_mul(A_r, A_r)

def vec_mat(v, M):
    n = len(v)
    return [sum(v[i] * M[i][j] for i in range(n)) for j in range(n)]

# Compute exact minimal annihilating polynomial of A_r^2 on e_i^T over Q via exact Fraction RREF!
def krylov_min_poly(M, row_idx):
    n = len(M)
    v = [Fraction(1 if j == row_idx else 0) for j in range(n)]
    vecs = [v]
    # RREF basis of vecs[0..k]
    pivots = {}  # col -> (rref_vec, coeff_comb_in_basis)
    basis_combs = []
    for k in range(n + 1):
        cur = list(vecs[-1])
        comb = [Fraction(0)] * (k + 1)
        comb[k] = Fraction(1)
        for pcol in sorted(pivots.keys()):
            if cur[pcol] != 0:
                pvec, pcomb = pivots[pcol]
                factor = cur[pcol]
                for j in range(n):
                    cur[j] -= factor * pvec[j]
                for j in range(len(pcomb)):
                    comb[j] -= factor * pcomb[j]
        # Find first nonzero entry in cur
        nz = next((j for j in range(n) if cur[j] != 0), None)
        if nz is None:
            # Linear dependence found: sum_{j=0..k} comb[j] v M^j == 0!
            # Normalize monic (divide by comb[k])
            assert comb[k] == 1
            return comb
        inv = Fraction(1) / cur[nz]
        pivots[nz] = ([c * inv for c in cur], [c * inv for c in comb])
        # Compute next Krylov vector v * M^(k+1)
        nxt = [sum(vecs[-1][i] * Fraction(M[i][j]) for i in range(n)) for j in range(n)]
        vecs.append(nxt)
    raise AssertionError("No dependence found")

# Expected q(z) = z(z - 1)(z^2 - 62z + 1)(z^2 - 18z + 1)
z_sym = sp.Symbol("z")
q_expected_expr = sp.expand(z_sym * (z_sym - 1) * (z_sym**2 - 62 * z_sym + 1) * (z_sym**2 - 18 * z_sym + 1))
q_expected_coeffs = [int(sp.Poly(q_expected_expr, z_sym).nth(d)) for d in range(7)]

for x in NON_GAMMA:
    xi = NAMES.index(x)
    mp = krylov_min_poly(A_r2, r_pos[xi])
    assert [int(c) for c in mp] == q_expected_coeffs, f"Krylov mismatch for {x}: {mp}"
print(f"[8] PASS Reachable dim = {len(reach)}; Krylov min poly of A_r^2 on e_X^T is q(z) for all 8 non-Gamma X.")

# Exact rational GF computation using sympy from period-2 offset recurrence!
# Since v_{n+1} = A_r v_n + b_even (n>=2 even), A_r v_n + b_odd (n>=3 odd):
# v_{2m+2} satisfies v_{2m+4} - v_{2m+2} = A_r^{2m} (v_4 - v_2), so (1-y) Q_rev(y) * sum_{m>=0} X_{2m+2} y^m is poly of deg <= 6!
x_sym, y_sym = sp.symbols("x y")
Q_rev_y = (1 - y_sym) * (1 - 62 * y_sym + y_sym**2) * (1 - 18 * y_sym + y_sym**2)
ann_y = sp.expand((1 - y_sym) * Q_rev_y)

def mat_vec_int(M, v):
    return [sum(row[j] * v[j] for j in range(len(v))) for row in M]

def compute_gf(kind):
    v = {n: [get_v(n, kind)[idx] for idx in reach] for n in range(7)}
    b_even = [v[3][i] - mat_vec_int(A_r, v[2])[i] for i in range(60)]
    b_odd  = [v[4][i] - mat_vec_int(A_r, v[3])[i] for i in range(60)]
    # Generate v[n] up to n = 22 using EXACT matrix recurrence!
    for n in range(6, 22):
        b = b_even if n % 2 == 0 else b_odd
        av = mat_vec_int(A_r, v[n])
        v[n + 1] = [av[i] + b[i] for i in range(60)]

    # Verify for each X in NON_GAMMA that (1-y)*Q_rev(y) annihilates both even (2m+2) and odd (2m+3) sequences for m >= 7:
    gfs = set()
    for nm in NON_GAMMA:
        ri = r_pos[NAMES.index(nm)]
        even_seq = [v[2 * m + 2][ri] for m in range(10)]  # n = 2, 4, ..., 20
        odd_seq  = [v[2 * m + 3][ri] for m in range(10)]  # n = 3, 5, ..., 21
        ann_poly = sp.Poly(ann_y, y_sym)
        ann_c = [int(ann_poly.nth(d)) for d in range(8)]
        # Verify m=7,8,9 give exact 0 when convolved with ann_c:
        for seq in (even_seq, odd_seq):
            for m in range(7, 10):
                val = sum(ann_c[d] * seq[m - d] for d in range(8))
                assert val == 0, f"Annihilation failed at m={m} for {nm} ({kind}): val={val}"
        num_even = sum(sum(ann_c[d] * even_seq[m - d] for d in range(m + 1)) * y_sym**m for m in range(7))
        num_odd  = sum(sum(ann_c[d] * odd_seq[m - d]  for d in range(m + 1)) * y_sym**m for m in range(7))
        gf_even = sp.cancel(num_even / ann_y).subs(y_sym, x_sym**2) * x_sym**2
        gf_odd  = sp.cancel(num_odd  / ann_y).subs(y_sym, x_sym**2) * x_sym**3
        # Add n=0, 1 terms (both 0)
        gf_tot = sp.factor(sp.cancel(v[0][ri] + v[1][ri] * x_sym + gf_even + gf_odd))
        gfs.add(gf_tot)
    assert len(gfs) == 1
    gf = next(iter(gfs))
    return gf, v

GL_gf, vL_seq = compute_gf("L")
GS_gf, vS_seq = compute_gf("S")
G_gf = sp.factor(sp.cancel(GL_gf + GS_gf))

den_exp = (1 - x_sym) * (1 - 8 * x_sym + x_sym**2) * (1 - 4 * x_sym - x_sym**2)
assert sp.simplify(GL_gf - 2 * x_sym**3 * (9 + x_sym) / den_exp) == 0, f"GL mismatch: {GL_gf}"
assert sp.simplify(GS_gf - 2 * x_sym**3 * (5 + 3 * x_sym) / den_exp) == 0, f"GS mismatch: {GS_gf}"
assert sp.simplify(G_gf  - 4 * x_sym**3 * (7 + 2 * x_sym) / den_exp) == 0, f"G mismatch: {G_gf}"
print(f"[9] PASS Exact Rational GFs: G_L={GL_gf}, G_S={GS_gf}, G={G_gf}")

# Check expanded denominator and order-5 recurrence + OEIS terms n=0..21!
assert sp.expand(den_exp) == 1 - 13 * x_sym + 44 * x_sym**2 - 28 * x_sym**3 - 5 * x_sym**4 + x_sym**5
a_vals = [0, 0, 0, 28, 372]
for n in range(5, 22):
    a_vals.append(13 * a_vals[n - 1] - 44 * a_vals[n - 2] + 28 * a_vals[n - 3] + 5 * a_vals[n - 4] - a_vals[n - 5])

ri_delta = r_pos[NAMES.index("Delta")]
for n in range(22):
    assert vL_seq[n][ri_delta] == OEIS_A400813[n], f"A400813 mismatch at n={n}"
    assert vS_seq[n][ri_delta] == OEIS_A400814[n], f"A400814 mismatch at n={n}"
    assert a_vals[n] == OEIS_A400813[n] + OEIS_A400814[n]
for n in range(len(OEIS_A400812)):
    assert a_vals[n] == OEIS_A400812[n]
print("[10] PASS Exact recurrence matches all 22 terms of A400813 & A400814 and all 12 terms of A400812.")

# ---------------------------------------------------------------------------
# 9. Section 5: Tile count matrix, A057080-Fibonacci identity, and limit
# ---------------------------------------------------------------------------

# Verify child tile counts from TEMPLATES directly:
for x in NAMES:
    ch = TEMPLATES[x]["children"]
    g_cnt = sum(1 for c in ch if c[0] == "Gamma")
    ng_cnt = sum(1 for c in ch if c[0] != "Gamma")
    if x == "Gamma":
        assert (g_cnt, ng_cnt) == (1, 6)
    else:
        assert (g_cnt, ng_cnt) == (1, 7)

# Verify exact rational GF identity in Section 5:
lhs_gf = (x_sym * (1 + x_sym) / (1 - 8 * x_sym + x_sym**2)
          - sp.Rational(1, 2) * ((1 + x_sym) / (1 - 4 * x_sym - x_sym**2) - 1 - 3 * x_sym / (1 - x_sym)))
assert sp.simplify(lhs_gf - G_gf) == 0

# Verify numerical A057080 and A099919 identity for n=1..19:
F = [0, 1]
for _ in range(70):
    F.append(F[-1] + F[-2])

g_cnt, t_cnt = 2, 1
assert t_cnt == OEIS_A057080[0]
for n in range(1, 20):
    t_prev = t_cnt
    g_cnt, t_cnt = g_cnt + 6 * t_cnt, g_cnt + 7 * t_cnt
    assert t_cnt == OEIS_A057080[n]
    assert (F[3 * n + 2] - 1) // 2 == OEIS_A099919[n]
    assert a_vals[n] == t_prev - (F[3 * n + 2] - 3) // 2
    assert a_vals[n] == t_prev - OEIS_A099919[n] + 1

# Verify exact algebraic limit in Section 5:
lam_plus = 4 + sp.sqrt(15)
assert sp.simplify(lam_plus**2 - 8 * lam_plus + 1) == 0
assert sp.simplify(1 / lam_plus - (4 - sp.sqrt(15))) == 0
print("[11] PASS Section 5: M_tile=[[1,6],[1,7]], exact A057080-Fibonacci GF & sequence identity, and limit 4-sqrt(15).")
print("PASS")
