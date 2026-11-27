#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for Navarra-Qureshi-Rinaldo arXiv:2511.22346v1 Conjecture 2.3.

Built strictly from primary source definitions (HILBERT_Series_NEW.tex) without reading verify.py.
Uses exact integer and sympy polynomial/Groebner-basis arithmetic (zero floats).
"""

from __future__ import annotations

from collections import deque
import itertools
import sys
import sympy as sp


def build_counterexample() -> list[tuple[int, int]]:
    # 10 unit cells [(x,y), (x+1,y+1)]
    return [
        (1, 2), (1, 3),
        (2, 1), (2, 3), (2, 4),
        (3, 1), (3, 2), (3, 4),
        (4, 2), (4, 3),
    ]


def check_weakly_connected(cells: set[tuple[int, int]]) -> bool:
    verts = {c: {(c[0] + dx, c[1] + dy) for dx in (0, 1) for dy in (0, 1)} for c in cells}
    start = next(iter(cells))
    seen = {start}
    q = deque([start])
    while q:
        cur = q.popleft()
        for nxt in cells:
            if nxt not in seen and (verts[cur] & verts[nxt]):
                seen.add(nxt)
                q.append(nxt)
    return len(seen) == len(cells)


def all_inner_intervals(cells: set[tuple[int, int]]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    """Return all proper intervals [a, b] in N^2 whose cells are all in `cells`."""
    xs = sorted({v[0] for c in cells for v in (c, (c[0] + 1, c[1] + 1))})
    ys = sorted({v[1] for c in cells for v in (c, (c[0] + 1, c[1] + 1))})
    intervals = []
    for i1, x1 in enumerate(xs):
        for x2 in xs[i1 + 1 :]:
            for j1, y1 in enumerate(ys):
                for y2 in ys[j1 + 1 :]:
                    ok = True
                    for x in range(x1, x2):
                        for y in range(y1, y2):
                            if (x, y) not in cells:
                                ok = False
                                break
                        if not ok:
                            break
                    if ok:
                        intervals.append(((x1, y1), (x2, y2)))
    return intervals


def switching_rook_polynomial(
    cells_list: list[tuple[int, int]],
    intervals: list[tuple[tuple[int, int], tuple[int, int]]],
) -> tuple[int, list[int]]:
    """Compute exact switching rook polynomial [1, r~_1, ..., r~_r] and rook number from primary definitions."""
    cells = set(cells_list)
    n = len(cells_list)

    # Two cells A, B are in attacking position iff they belong to a common row or column of P
    # i.e., either (a_y == b_y and all cells between them horizontally are in P)
    # or (a_x == b_x and all cells between them vertically are in P).
    attacking = [[False] * n for _ in range(n)]
    for i, c1 in enumerate(cells_list):
        for j, c2 in enumerate(cells_list):
            if i == j:
                attacking[i][j] = True
            elif c1[1] == c2[1]:
                lo, hi = min(c1[0], c2[0]), max(c1[0], c2[0])
                if all((x, c1[1]) in cells for x in range(lo, hi + 1)):
                    attacking[i][j] = True
            elif c1[0] == c2[0]:
                lo, hi = min(c1[1], c2[1]), max(c1[1], c2[1])
                if all((c1[0], y) in cells for y in range(lo, hi + 1)):
                    attacking[i][j] = True

    # Find all switching pairs {c1, c2} <-> {d1, d2} from proper inner intervals [a, b] with >= 2x2 cells
    # Corner cells of [a, b] with a=(x1,y1), b=(x2,y2) (x2 >= x1+2, y2 >= y1+2):
    # diagonal corner cells: (x1, y1) and (x2-1, y2-1)
    # anti-diagonal corner cells: (x1, y2-1) and (x2-1, y1)
    cell_idx = {c: i for i, c in enumerate(cells_list)}
    switches: dict[tuple[int, int], list[tuple[int, int]]] = {}
    for (x1, y1), (x2, y2) in intervals:
        if x2 - x1 >= 2 and y2 - y1 >= 2:
            d1 = cell_idx[(x1, y1)]
            d2 = cell_idx[(x2 - 1, y2 - 1)]
            a1 = cell_idx[(x1, y2 - 1)]
            a2 = cell_idx[(x2 - 1, y1)]
            p_diag = (min(d1, d2), max(d1, d2))
            p_anti = (min(a1, a2), max(a1, a2))
            switches.setdefault(p_diag, []).append(p_anti)
            switches.setdefault(p_anti, []).append(p_diag)

    # Enumerate k-rook configurations by level
    coeffs = [1]
    k = 1
    while True:
        confs: list[tuple[int, ...]] = []
        for comb in itertools.combinations(range(n), k):
            ok = True
            for u in range(k):
                for v in range(u + 1, k):
                    if attacking[comb[u]][comb[v]]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                confs.append(comb)
        if not confs:
            break
        conf_set = set(confs)
        seen = set()
        num_classes = 0
        for start in confs:
            if start in seen:
                continue
            num_classes += 1
            seen.add(start)
            dq = deque([start])
            while dq:
                cur = dq.popleft()
                cur_set = set(cur)
                for u in range(k):
                    for v in range(u + 1, k):
                        pair = (cur[u], cur[v])
                        if pair in switches:
                            for sw in switches[pair]:
                                if sw[0] not in cur_set and sw[1] not in cur_set:
                                    nxt = tuple(sorted((cur_set - {pair[0], pair[1]}) | {sw[0], sw[1]}))
                                    if nxt in conf_set and nxt not in seen:
                                        seen.add(nxt)
                                        dq.append(nxt)
        coeffs.append(num_classes)
        k += 1

    return len(coeffs) - 1, coeffs


def hilbert_series_monomial_ideal(monomial_exps: list[tuple[int, ...]], num_vars: int) -> tuple[int, list[int]]:
    """Compute exact Krull dimension d and h-polynomial of S / <monomial_exps> by inclusion-exclusion / Mayer-Vietoris.

    Actually, simple recursive splitting on variables (Taylor/Eliahou-Kervaire/pivot splitting):
    Let M be a monomial ideal in K[x_1, ..., x_n] generated by monomials G.
    Minimize G to minimal generators (all squarefree here? Let's verify!).
    For squarefree monomial ideal I:
      HP(S/I; t) = sum_{F in simplicial complex Delta} t^{|F|} / (1 - t)^{|F|}?
      Wait: if I is NOT squarefree, or for general monomial ideal:
      Pick a variable x_i appearing in some generator (not pure power? No, any variable appearing in >=1 generator!).
      Actually we have exact short exact sequence:
        0 -> (S / (I : x_i))(-1) -> S / I -> S / (I + (x_i)) -> 0
      which works for ANY monomial ideal (squarefree or not)!!
      Wait: if I is minimally generated by a single monomial or empty:
        - If 1 in I: num = 0
        - If G is empty: HP(S; t) = 1 / (1 - t)^num_vars, so numerator over (1-t)^num_vars is 1.
        - Otherwise pick variable x_i appearing in the most generators of G (or a non-pure-power generator),
          and compute numerator P(t) over (1-t)^num_vars via:
            P(I) = P(I + (x_i)) + t * P(I : x_i) !!
      WAIT: check the degree/exactness of that recurrence:
      0 -> (S/(I:x_i))(-1) --(*x_i)--> S/I --> S/(I+(x_i)) -> 0 is exact for ANY homogeneous ideal I and variable x_i!
      And HP((S/(I:x_i))(-1); t) = t * HP(S/(I:x_i); t)!
      So over common denominator (1-t)^num_vars,
        N(I; t) = N(I + (x_i); t) + t * N(I : x_i; t)!
      Wait: when I = (x_{i_1}^{a_1}, ..., x_{i_r}^{a_r}) has only univariate generators (or empty),
      S/I is a tensor product of K[x_j]/(x_j^{a_j}) and free variables:
        HP(S/I; t) = (prod_{j in pure} (1 - t^{a_j}) / (1 - t)) * (1 / (1 - t)^{num_vars - |pure|})
                   = prod_{j in pure} (1 - t^{a_j}) / (1 - t)^{num_vars} !!
      Once we get N(I; t) such that HP(S/I; t) = N(I; t) / (1 - t)^{num_vars}, simply divide out all factors of (1 - t)
      from N(I; t) until h(1) != 0! The remaining denominator power d IS the exact Krull dimension, and h(t) IS the exact h-polynomial!
    """

    def minimize(gens: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
        # Remove duplicates and multiples
        uniq = sorted(set(gens), key=lambda m: (sum(m), m))
        res: list[tuple[int, ...]] = []
        for g in uniq:
            if any(all(a <= b for a, b in zip(h, g)) for h in res):
                continue
            res.append(g)
        return res

    def poly_add(a: list[int], b: list[int]) -> list[int]:
        L = max(len(a), len(b))
        out = [0] * L
        for i, v in enumerate(a):
            out[i] += v
        for i, v in enumerate(b):
            out[i] += v
        while len(out) > 1 and out[-1] == 0:
            out.pop()
        return out

    def poly_mul(a: list[int], b: list[int]) -> list[int]:
        out = [0] * (len(a) + len(b) - 1)
        for i, va in enumerate(a):
            for j, vb in enumerate(b):
                out[i + j] += va * vb
        while len(out) > 1 and out[-1] == 0:
            out.pop()
        return out

    def compute_num(gens: list[tuple[int, ...]]) -> list[int]:
        gens = minimize(gens)
        if not gens:
            return [1]
        if any(sum(g) == 0 for g in gens):
            return [0]
        # Check if all generators are univariate powers
        non_univ = [g for g in gens if sum(1 for e in g if e > 0) > 1]
        if not non_univ:
            num = [1]
            for g in gens:
                # single nonzero entry
                exp = max(g)
                # multiply by (1 - t^exp)
                fac = [1] + [0] * (exp - 1) + [-1]
                num = poly_mul(num, fac)
            return num
        # Pick variable appearing in the most non-univariate generators
        counts = [sum(1 for g in non_univ if g[v] > 0) for v in range(num_vars)]
        pivot = max(range(num_vars), key=lambda v: counts[v])
        assert counts[pivot] > 0

        # I + (x_pivot): add e_pivot, i.e. drop generators divisible by x_pivot and add unit vector
        unit = tuple(1 if v == pivot else 0 for v in range(num_vars))
        gens_plus = [g for g in gens if g[pivot] == 0] + [unit]

        # I : x_pivot: decrement exponent of pivot if > 0
        gens_colon = []
        for g in gens:
            if g[pivot] > 0:
                gl = list(g)
                gl[pivot] -= 1
                gens_colon.append(tuple(gl))
            else:
                gens_colon.append(g)

        p_plus = compute_num(gens_plus)
        p_colon = compute_num(gens_colon)
        return poly_add(p_plus, [0] + p_colon)

    num = compute_num(monomial_exps)
    assert any(c != 0 for c in num)
    d = num_vars
    # Divide num(t) by (1 - t) while num(1) == 0
    while sum(num) == 0:
        # Synthetic division of num(t) by (t - 1), then negate
        # Actually num(t) = (1 - t) * q(t) => q_0 = num_0, q_k = num_k + q_{k-1}
        q = []
        running = 0
        for c in num[:-1]:
            running += c
            q.append(running)
        assert running + num[-1] == 0
        num = q
        d -= 1
    while len(num) > 1 and num[-1] == 0:
        num.pop()
    return d, num


def run_all_checks() -> None:
    cells_list = build_counterexample()
    cells = set(cells_list)
    assert len(cells) == 10
    assert check_weakly_connected(cells), "Not weakly connected"

    # Vertex set V(P)
    verts = sorted({(c[0] + dx, c[1] + dy) for c in cells for dx in (0, 1) for dy in (0, 1)})
    assert len(verts) == 21
    print(f"Verified |P|={len(cells)}, weakly connected=True, |V(P)|={len(verts)}")

    # Inner intervals
    intervals = all_inner_intervals(cells)
    print(f"Found {len(intervals)} proper inner intervals.")
    assert len(intervals) == 18
    for (x1, y1), (x2, y2) in intervals:
        assert x2 - x1 < 2 or y2 - y1 < 2, "Unexpected 2x2 block"

    # Check prime ideal Z = {2,3,4}^2 containment from COUNTEREXAMPLE.md
    Z = {(x, y) for x in (2, 3, 4) for y in (2, 3, 4)}
    assert Z.issubset(set(verts)) and len(Z) == 9
    for a, b in intervals:
        c = (a[0], b[1])
        d = (b[0], a[1])
        assert (a in Z or b in Z) and (c in Z or d in Z), f"Interval {[a,b]} not in prime ideal!"
    print("Verified elementary proof: I_P subset of 12-dim prime ideal p = (x_v : v in {2,3,4}^2) => dim K[P] >= 12 => h_1 <= 9 < 10 = r~_1(P).")

    # Compute exact switching rook polynomial
    rook_num, sw_rook = switching_rook_polynomial(cells_list, intervals)
    print(f"Switching rook polynomial: {sw_rook}, rook number = {rook_num}")
    assert sw_rook == [1, 10, 37, 62, 46, 12, 1]
    assert rook_num == 6

    # Compute exact Groebner basis of I_P under grevlex over Q (sympy)
    # Note: generators are pure-difference binomials m1 - m2; verify reduced GB has only +/-1 coefficients
    # so in_grevlex(I_P) is identical over EVERY field K!
    var_syms = [sp.Symbol(f"x_{v[0]}_{v[1]}") for v in verts]
    v_to_idx = {v: i for i, v in enumerate(verts)}
    gens = []
    for a, b in intervals:
        c = (a[0], b[1])
        d = (b[0], a[1])
        gens.append(var_syms[v_to_idx[a]] * var_syms[v_to_idx[b]] - var_syms[v_to_idx[c]] * var_syms[v_to_idx[d]])

    # Primary source variable order (HILBERT_Series_NEW.tex line 658) or standard grevlex:
    # Hilbert series & dim are independent of term order! Use grevlex over Q.
    gb = sp.groebner(gens, *var_syms, order="grevlex", domain=sp.QQ)
    lead_exps: list[tuple[int, ...]] = []
    for poly in gb.polys:
        coeffs = poly.coeffs()
        assert all(c in (1, -1) for c in coeffs), f"Non-unit coefficient in GB: {coeffs}"
        lead_exps.append(tuple(int(e) for e in poly.LM(order="grevlex").exponents))
    print(f"Reduced grevlex Groebner basis has {len(lead_exps)} elements (all coefficients in {{+1, -1}}, field-independent!).")

    dim_KP, h_poly = hilbert_series_monomial_ideal(lead_exps, len(verts))
    print(f"Exact dim K[P] = {dim_KP}, h_K[P](t) = {h_poly}")
    assert dim_KP == 12
    assert h_poly == [1, 9, 27, 25, -16, -33, -11, -1]
    assert h_poly != sw_rook

    print("PASS")


if __name__ == "__main__":
    try:
        run_all_checks()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
