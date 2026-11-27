"""Exact-arithmetic verifier for the rank-10 counterexample to Navarra et al. (2025), Conjecture 2.3."""

from itertools import combinations
from math import comb
import sympy as sp

CELLS = [
    (1, 2), (1, 3),
    (2, 1), (2, 3), (2, 4),
    (3, 1), (3, 2), (3, 4),
    (4, 2), (4, 3),
]
Z_SET = {(x, y) for x in (2, 3, 4) for y in (2, 3, 4)}


def is_inner(x1, y1, x2, y2, pset):
    return x1 < x2 and y1 < y2 and all(
        (x, y) in pset for x in range(x1, x2) for y in range(y1, y2)
    )


def poly_add(a, b):
    r = [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
         for i in range(max(len(a), len(b)))]
    while r and r[-1] == 0:
        r.pop()
    return r


def poly_shift(a, s):
    return [0] * s + a if a else []


def div_by_1mt(p):
    q = [0] * (len(p) - 1)
    q[0] = p[0]
    for i in range(1, len(q)):
        q[i] = p[i] + q[i - 1]
    return q


def min_gens(ms):
    ms = sorted(set(ms), key=lambda m: (sum(m), m))
    out = []
    for m in ms:
        if sum(m) == 0:
            return [m]
        if not any(all(m[i] >= g[i] for i in range(len(m))) for g in out):
            out.append(m)
    return out


def hilb_num(ms):
    ms = min_gens(ms)
    if ms and sum(ms[0]) == 0:
        return []
    deg1 = sum(1 for m in ms if sum(m) == 1)
    high = [m for m in ms if sum(m) > 1]
    if not high:
        p = [1]
        for _ in range(deg1):
            p = poly_add(p, [-x for x in poly_shift(p, 1)])
        return p
    nv = len(high[0])
    best_v = max(range(nv), key=lambda v: sum(1 for m in high if m[v] > 0))
    xv = tuple(1 if i == best_v else 0 for i in range(nv))
    j_add = hilb_num(ms + [xv])
    j_col = hilb_num([
        tuple(m[i] - (1 if i == best_v and m[i] > 0 else 0) for i in range(nv))
        for m in ms
    ])
    return poly_add(j_add, poly_shift(j_col, 1))


def switching_rook_poly(cells):
    pset = set(cells)
    n = len(cells)

    def non_attacking(c1, c2):
        if c1[0] == c2[0]:
            y1, y2 = min(c1[1], c2[1]), max(c1[1], c2[1])
            return not all((c1[0], y) in pset for y in range(y1, y2 + 1))
        if c1[1] == c2[1]:
            x1, x2 = min(c1[0], c2[0]), max(c1[0], c2[0])
            return not all((x, c1[1]) in pset for x in range(x1, x2 + 1))
        return True

    # No 2x2 sub-block => check switches directly via inner intervals
    switches = []
    for i in range(n):
        for j in range(i + 1, n):
            c1, c2 = cells[i], cells[j]
            if c1[0] != c2[0] and c1[1] != c2[1]:
                x1, x2 = min(c1[0], c2[0]), max(c1[0], c2[0])
                y1, y2 = min(c1[1], c2[1]), max(c1[1], c2[1])
                if all((x, y) in pset for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)):
                    switches.append((c1, c2, (c1[0], c2[1]), (c2[0], c1[1])))

    coeffs = [1]
    for k in range(1, n + 1):
        confs = []
        for sub in combinations(cells, k):
            if all(non_attacking(sub[a], sub[b]) for a in range(k) for b in range(a + 1, k)):
                confs.append(frozenset(sub))
        if not confs:
            break
        conf_set = set(confs)
        seen = set()
        comps = 0
        for c in confs:
            if c in seen:
                continue
            comps += 1
            stack = [c]
            seen.add(c)
            while stack:
                cur = stack.pop()
                for a, b, c_, d_ in switches:
                    if a in cur and b in cur:
                        nxt = (cur - {a, b}) | {c_, d_}
                        if nxt in conf_set and nxt not in seen:
                            seen.add(nxt)
                            stack.append(nxt)
        coeffs.append(comps)
    return coeffs


def main():
    pset = set(CELLS)
    assert len(pset) == 10
    verts = sorted({(x + dx, y + dy) for (x, y) in CELLS for dx in (0, 1) for dy in (0, 1)})
    assert len(verts) == 21
    assert Z_SET.issubset(set(verts)) and len(Z_SET) == 9

    intervals = [
        ((x1, y1), (x2, y2), (x1, y2), (x2, y1))
        for (x1, y1) in verts
        for (x2, y2) in verts
        if is_inner(x1, y1, x2, y2, pset)
    ]
    assert len(intervals) == 18

    # 1. Elementary prime-ideal check: I_P subset (x_v : v in Z_SET)
    for a, b, c, d in intervals:
        assert (a in Z_SET or b in Z_SET) and (c in Z_SET or d in Z_SET), (a, b, c, d)

    # 2. Exact Groebner basis & h-polynomial check
    vars_map = {v: sp.Symbol(f"x_{v[0]}_{v[1]}") for v in verts}
    var_list = [vars_map[v] for v in verts]
    gens = [vars_map[a] * vars_map[b] - vars_map[c] * vars_map[d] for a, b, c, d in intervals]
    G = sp.groebner(gens, *var_list, order="grevlex")
    # Confirm every GB polynomial is pure-difference binomial (char-independent)
    for p in G:
        terms = sp.Poly(p, *var_list).terms()
        assert len(terms) == 2 and sorted([t[1] for t in terms]) == [-1, 1]

    lms = [tuple(sp.Poly(sp.LM(p, *var_list, order="grevlex"), *var_list).monoms()[0]) for p in G]
    K = hilb_num(lms)
    dim = len(verts)
    while K and sum(K) == 0:
        K = div_by_1mt(K)
        dim -= 1

    assert dim == 12
    assert K == [1, 9, 27, 25, -16, -33, -11, -1], K

    # 3. Switching rook polynomial check
    sw_rook = switching_rook_poly(CELLS)
    assert sw_rook == [1, 10, 37, 62, 46, 12, 1], sw_rook
    assert K != sw_rook
    assert K[1] == 9 and sw_rook[1] == 10

    print(f"dim K[P] = {dim}")
    print(f"h_poly   = {K}")
    print(f"sw_rook  = {sw_rook}")
    print("PASS")


if __name__ == "__main__":
    main()
