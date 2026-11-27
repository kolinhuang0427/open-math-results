#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for Marberg-Morales-Yu (arXiv:2611.19371v1) Conjecture 3.8 (iG-conj).

Written directly from involution_pipe_dream_shifted_rpp_arxiv_v1.tex and PROOF.md without reading verify.py or notes/.
Uses pure Python int and SymPy ZZ[u_1,u_2,v] / ZZ[beta,x_1..x_n] polynomial arithmetic (zero floats).
"""

from __future__ import annotations

from collections import defaultdict
from itertools import product
import sys
import sympy as sp

u1, u2, v = sp.symbols("u1 u2 v")
beta = sp.Symbol("beta")

EMPTY = None


def flip_state(e):
    return EMPTY if e is EMPTY else (e[1], e[0])


def sort2(a: int, b: int) -> tuple[int, int]:
    return (a, b) if a >= b else (b, a)


def min_max(a: int, b: int) -> tuple[int, int]:
    return (a, b) if a <= b else (b, a)


def W_weight(u_p, v_p, W, S, E, N):
    """Off-diagonal folded bulk vertex weight."""
    if W is EMPTY and S is EMPTY and E is EMPTY and N is EMPTY:
        return u_p * v_p - 1
    if S is EMPTY and N is EMPTY and W is not EMPTY and W == E:
        return sp.Integer(1)
    if W is EMPTY and E is EMPTY and S is not EMPTY and S == N:
        return sp.Integer(1)
    if S is EMPTY and E is EMPTY and W is not EMPTY and W == N:
        return u_p * v_p
    if W is EMPTY and N is EMPTY and S is not EMPTY and S == E:
        return sp.Integer(1)
    if W is not EMPTY and S is not EMPTY and E is not EMPTY and N is not EMPTY:
        w1, n2 = W
        s1, e2 = S
        e1, s2 = E
        n1, w2 = N
        if min_max(w1, s1) == (e1, n1) and min_max(w2, s2) == (e2, n2):
            return sp.Integer(1)
    return sp.Integer(0)


def K_weight(u_p, W, S):
    """Diagonal boundary vertex weight."""
    if W is EMPTY and S is EMPTY:
        return u_p - 1
    if S is EMPTY and W is not EMPTY and W[0] == W[1]:
        return u_p
    if W is EMPTY and S is not EMPTY and S[0] == S[1]:
        return sp.Integer(1)
    if W is not EMPTY and S is not EMPTY:
        w1, n1 = W
        s1, e1 = S
        if min_max(w1, s1) == (e1, n1):
            return sp.Integer(1)
    return sp.Integer(0)


def R_weight(u1_p, u2_p, W1, W2, E1, E2):
    """Horizontal folded 0-Hecke R-matrix."""
    if W1 is EMPTY and W2 is EMPTY and E1 is EMPTY and E2 is EMPTY:
        return u2_p
    if W2 is EMPTY and W1 is not EMPTY:
        if E1 == W1 and E2 is EMPTY:
            return u2_p
        if E1 is EMPTY and E2 == W1:
            return u1_p - u2_p
        return sp.Integer(0)
    if W1 is EMPTY and W2 is not EMPTY:
        if E1 is EMPTY and E2 == W2:
            return u1_p
        return sp.Integer(0)
    if W1 is not EMPTY and W2 is not EMPTY and E1 is not EMPTY and E2 is not EMPTY:
        a1, b1 = W1
        a2, b2 = W2
        ap1, bp1 = E1
        ap2, bp2 = E2
        res = sp.Integer(0)
        if (ap1, ap2) == (a1, a2) and (b1, b2) == (bp1, bp2):
            res += u2_p
        if (ap1, ap2) == sort2(a1, a2) and (b1, b2) == sort2(bp1, bp2):
            res += u1_p - u2_p
        return res
    return sp.Integer(0)


def RV_weight(u1_p, u2_p, N1, N2, S1, S2):
    return R_weight(u1_p, u2_p, flip_state(N1), flip_state(N2), flip_state(S1), flip_state(S2))


def verify_bulk_ybe() -> None:
    print("[1/3] Checking Horizontal & Vertical Bulk YBE (Lemma 2)...", flush=True)
    # Build states for n=2 (all pairs in {1,2}^2 plus EMPTY) + representative 3-color states for k=3
    states_n2 = [EMPTY] + list(product([1, 2], repeat=2))
    # Index non-zero R and W transitions to evaluate YBE rapidly
    def verify_states(states):
        for W1, W2, S in product(states, repeat=3):
            k_in = (W1 is not EMPTY) + (W2 is not EMPTY) + (S is not EMPTY)
            # Compute LHS dict over (E1, E2, N)
            lhs = defaultdict(lambda: sp.Integer(0))
            for m1 in states:
                for m2 in states:
                    rw = R_weight(u1, u2, W1, W2, m1, m2)
                    if rw == 0:
                        continue
                    for c in states:
                        for E2 in states:
                            w2w = W_weight(u2, v, m2, S, E2, c)
                            if w2w == 0:
                                continue
                            for E1 in states:
                                for N in states:
                                    w1w = W_weight(u1, v, m1, c, E1, N)
                                    if w1w != 0:
                                        lhs[(E1, E2, N)] += rw * w1w * w2w
            rhs = defaultdict(lambda: sp.Integer(0))
            for m1 in states:
                for c in states:
                    for N in states:
                        w2w = W_weight(u2, v, W1, c, m1, N)
                        if w2w == 0:
                            continue
                        for m2 in states:
                            w1w = W_weight(u1, v, W2, S, m2, c)
                            if w1w == 0:
                                continue
                            for E1 in states:
                                for E2 in states:
                                    rw = R_weight(u1, u2, m1, m2, E1, E2)
                                    if rw != 0:
                                        rhs[(E1, E2, N)] += w2w * w1w * rw
            all_keys = set(lhs.keys()) | set(rhs.keys())
            for key in all_keys:
                assert sp.expand(lhs[key] - rhs[key]) == 0, f"Horiz YBE mismatch at {(W1,W2,S)}->{key}"

    verify_states(states_n2)
    # Also test 3 distinct incoming colors (1,2),(2,3),(3,1) and permutation at k=3
    states_k3 = [EMPTY, (1, 3), (2, 1), (3, 2), (1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (3, 1)]
    for W1, W2, S in [((1, 2), (2, 3), (3, 1)), ((3, 2), (1, 3), (2, 1))]:
        lhs = defaultdict(lambda: sp.Integer(0))
        for m1 in states_k3:
            for m2 in states_k3:
                rw = R_weight(u1, u2, W1, W2, m1, m2)
                if rw == 0:
                    continue
                for c in states_k3:
                    for E2 in states_k3:
                        w2w = W_weight(u2, v, m2, S, E2, c)
                        if w2w == 0:
                            continue
                        for E1 in states_k3:
                            for N in states_k3:
                                w1w = W_weight(u1, v, m1, c, E1, N)
                                if w1w != 0:
                                    lhs[(E1, E2, N)] += rw * w1w * w2w
        rhs = defaultdict(lambda: sp.Integer(0))
        for m1 in states_k3:
            for c in states_k3:
                for N in states_k3:
                    w2w = W_weight(u2, v, W1, c, m1, N)
                    if w2w == 0:
                        continue
                    for m2 in states_k3:
                        w1w = W_weight(u1, v, W2, S, m2, c)
                        if w1w == 0:
                            continue
                        for E1 in states_k3:
                            for E2 in states_k3:
                                rw = R_weight(u1, u2, m1, m2, E1, E2)
                                if rw != 0:
                                    rhs[(E1, E2, N)] += w2w * w1w * rw
        for key in set(lhs.keys()) | set(rhs.keys()):
            assert sp.expand(lhs[key] - rhs[key]) == 0

    # Vertical YBE for n=2
    for N1, N2, W in product(states_n2, repeat=3):
        lhs = defaultdict(lambda: sp.Integer(0))
        for m1 in states_n2:
            for m2 in states_n2:
                rw = RV_weight(u1, u2, N1, N2, m1, m2)
                if rw == 0:
                    continue
                for c in states_n2:
                    for S1 in states_n2:
                        w1w = W_weight(v, u1, W, S1, c, m1)
                        if w1w == 0:
                            continue
                        for S2 in states_n2:
                            for E in states_n2:
                                w2w = W_weight(v, u2, c, S2, E, m2)
                                if w2w != 0:
                                    lhs[(S1, S2, E)] += rw * w1w * w2w
        rhs = defaultdict(lambda: sp.Integer(0))
        for m1 in states_n2:
            for c in states_n2:
                w2w = W_weight(v, u2, W, m1, c, N1)
                if w2w == 0:
                    continue
                for m2 in states_n2:
                    for E in states_n2:
                        w1w = W_weight(v, u1, c, m2, E, N2)
                        if w1w == 0:
                            continue
                        for S1 in states_n2:
                            for S2 in states_n2:
                                rw = RV_weight(u1, u2, m1, m2, S1, S2)
                                if rw != 0:
                                    rhs[(S1, S2, E)] += w2w * w1w * rw
        for key in set(lhs.keys()) | set(rhs.keys()):
            assert sp.expand(lhs[key] - rhs[key]) == 0


def T_triangle(u1_p, u2_p, W1, W2, S1, S2, states):
    tot = sp.Integer(0)
    for c in states:
        k1 = K_weight(u1_p, W1, c)
        if k1 == 0:
            continue
        for d in states:
            w21 = W_weight(u2_p, u1_p, W2, S1, d, c)
            if w21 == 0:
                continue
            k2 = K_weight(u2_p, d, S2)
            if k2 != 0:
                tot += k1 * w21 * k2
    return tot


def verify_reflection_eq() -> None:
    print("[2/3] Checking 2x2 Diagonal Reflection Equation (Lemma 3)...", flush=True)
    states_n2 = [EMPTY] + list(product([1, 2], repeat=2))
    for W1, W2, S1, S2 in product(states_n2, repeat=4):
        lhs = sp.Integer(0)
        for m1 in states_n2:
            for m2 in states_n2:
                rw = R_weight(u1, u2, W1, W2, m1, m2)
                if rw != 0:
                    lhs += rw * T_triangle(u1, u2, m1, m2, S1, S2, states_n2)
        rhs = sp.Integer(0)
        for n1 in states_n2:
            for n2 in states_n2:
                rw = RV_weight(u1, u2, n1, n2, S1, S2)
                if rw != 0:
                    rhs += T_triangle(u2, u1, W1, W2, n1, n2, states_n2) * rw
        assert sp.expand(lhs - rhs) == 0, f"Reflection eq failed at {(W1,W2,S1,S2)}"

    # Also test 4-wire distinct-color case k=4 with colors {1,2,3,4}
    states_k4 = list(product([1, 2, 3, 4], repeat=2))
    W1, W2, S1, S2 = (2, 4), (4, 1), (1, 3), (3, 2)
    lhs = sp.Integer(0)
    for m1 in states_k4:
        for m2 in states_k4:
            rw = R_weight(u1, u2, W1, W2, m1, m2)
            if rw != 0:
                lhs += rw * T_triangle(u1, u2, m1, m2, S1, S2, states_k4)
    rhs = sp.Integer(0)
    for n1 in states_k4:
        for n2 in states_k4:
            rw = RV_weight(u1, u2, n1, n2, S1, S2)
            if rw != 0:
                rhs += T_triangle(u2, u1, W1, W2, n1, n2, states_k4) * rw
    assert sp.expand(lhs - rhs) == 0


def demazure_prod(p: tuple[int, ...], i_1based: int) -> tuple[int, ...]:
    idx = i_1based - 1
    lst = list(p)
    if lst[idx] < lst[idx + 1]:
        lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
    return tuple(lst)


def perm_compose_0hecke_s_left(i: int, z: tuple[int, ...]) -> tuple[int, ...]:
    """Compute s_i o z where (u v)(k) = u(v(k)) => s_i swaps values i and i+1 if needed."""
    pos_i = z.index(i)
    pos_ip1 = z.index(i + 1)
    if pos_i < pos_ip1:
        lst = list(z)
        lst[pos_i], lst[pos_ip1] = lst[pos_ip1], lst[pos_i]
        return tuple(lst)
    return z


def s_circ_z_circ_s(i: int, z: tuple[int, ...]) -> tuple[int, ...]:
    return demazure_prod(perm_compose_0hecke_s_left(i, z), i)


def inv_length(z: tuple[int, ...]) -> int:
    n = len(z)
    ell = sum(1 for i in range(n) for j in range(i + 1, n) if z[i] > z[j])
    cyc = sum(1 for i in range(n) if z[i] > i + 1)
    return (ell + cyc) // 2


def enumerate_sym_k_bpds(n: int) -> dict[tuple[int, ...], list[dict]]:
    """Enumerate all symmetric square K-theoretic BPDs (no bump tiles) on [n]x[n], grouped by kpi."""
    # Each tile is represented by (kind, in_W, in_S, out_E, out_N) or simply tile code:
    # 'B': (0,0)->(0,0), 'H': (1,0)->(1,0), 'V': (0,1)->(0,1), 'J': (1,0)->(0,1), 'C': (0,1)->(1,0), 'P': (1,1)->(1,1)
    TILES = {
        "B": (0, 0, 0, 0),
        "H": (1, 0, 1, 0),
        "V": (0, 1, 0, 1),
        "J": (1, 0, 0, 1),
        "C": (0, 1, 1, 0),
        "P": (1, 1, 1, 1),
    }
    TRANSPOSE = {"B": "B", "H": "V", "V": "H", "J": "J", "C": "C", "P": "P"}

    # Build grid cell-by-cell in row-major order, imposing E_{j,i} = TRANSPOSE[E_{i,j}] and symmetric edges:
    # West boundary (col 0) = 0; North boundary (row 0) = 0; South boundary (row n-1) = 1; East boundary (col n-1) = 1.
    grid = [[None] * n for _ in range(n)]
    north_in = [[0] * n for _ in range(n + 1)]
    west_in = [[0] * (n + 1) for _ in range(n)]
    # Symmetry forces S[n-1][c] == 1 and E[r][n-1] == 1 automatically if E[j][i] = T(E[i][j])!
    results: dict[tuple[int, ...], list[dict]] = defaultdict(list)

    cells = [(r, c) for r in range(n) for c in range(n)]

    def backtrack(idx: int) -> None:
        if idx == n * n:
            # Propagate Demazure pipe labels from south (1..n) to east
            east_out = [None] * n
            north_label = [[0] * n for _ in range(n + 1)]
            west_label = [[0] * (n + 1) for _ in range(n)]
            for c in range(n):
                north_label[n][c] = c + 1
            for r in range(n - 1, -1, -1):
                for c in range(n):
                    t = grid[r][c]
                    wl = west_label[r][c]
                    sl = north_label[r + 1][c]
                    if t == "B":
                        el, nl = 0, 0
                    elif t == "H":
                        el, nl = wl, 0
                    elif t == "V":
                        el, nl = 0, sl
                    elif t == "J":
                        el, nl = 0, wl
                    elif t == "C":
                        el, nl = sl, 0
                    else:  # P
                        el, nl = min(wl, sl), max(wl, sl)
                    west_label[r][c + 1] = el
                    north_label[r][c] = nl
            z = tuple(west_label[r][n] for r in range(n))
            # Check involution: because E = E^T, z is automatically in I_n!
            assert all(z[z[k] - 1] == k + 1 for k in range(n))
            # Lower triangle cells (i >= j, 1-based): record blank and upturn (J)
            blanks = [(r + 1, c + 1) for r in range(n) for c in range(r + 1) if grid[r][c] == "B"]
            upturns = [(r + 1, c + 1) for r in range(n) for c in range(r + 1) if grid[r][c] == "J"]
            results[z].append({"blanks": blanks, "upturns": upturns, "grid": [row[:] for row in grid]})
            return

        r, c = cells[idx]
        w_req = west_in[r][c]
        n_req = north_in[r][c]
        allowed = [TRANSPOSE[grid[c][r]]] if r > c else (["B", "J", "C", "P"] if r == c else list(TILES.keys()))
        for t in allowed:
            wt, st, et, nt = TILES[t]
            if wt != w_req or nt != n_req:
                continue
            if r == n - 1 and st != 1:
                continue
            if c == n - 1 and et != 1:
                continue
            grid[r][c] = t
            west_in[r][c + 1] = et
            north_in[r + 1][c] = st
            backtrack(idx + 1)

    backtrack(0)
    return results


def verify_conjecture_small_n() -> None:
    print("[3/3] Checking iG-conj & iG-conj-cor exhaustively for n = 1, 2, 3, 4...", flush=True)
    for n in range(1, 5):
        xs = sp.symbols(f"x1:{n+1}")
        by_z = enumerate_sym_k_bpds(n)
        # Generate all involutions I_n
        from itertools import permutations

        invols = [p for p in permutations(range(1, n + 1)) if all(p[p[k] - 1] == k + 1 for k in range(n))]
        assert set(by_z.keys()) <= set(invols)

        # Compute R_z from kInvBPD(z)
        def oplus(i: int, j: int):
            if i == j:
                return xs[i - 1]
            return xs[i - 1] + xs[j - 1] + beta * xs[i - 1] * xs[j - 1]

        R_z = {}
        for z in invols:
            ell_z = inv_length(z)
            poly = sp.Integer(0)
            for D in by_z[z]:
                term = beta ** (len(D["blanks"]) - ell_z)
                for i, j in D["blanks"]:
                    term *= oplus(i, j)
                for i, j in D["upturns"]:
                    term *= 1 + beta * oplus(i, j)
                poly += term
            R_z[z] = sp.expand(poly)

        # Compute exact iG_z from Definition 2.7 (dominant w_0^(n) + isobaric divided differences)
        w0 = tuple(range(n, 0, -1))
        iD_w0 = [(i, j) for i in range(1, n + 1) for j in range(1, i + 1) if w0[i - 1] > j and w0[j - 1] > i]
        iG_w0 = sp.Integer(1)
        for i, j in iD_w0:
            iG_w0 *= oplus(i, j)
        iG = {w0: sp.expand(iG_w0)}
        assert len(by_z[w0]) == 1, f"Lemma 5 uniqueness failed at n={n}"
        assert R_z[w0] == iG[w0], f"Base case w0 failed at n={n}"

        def bpartial(i: int, f):
            fi = f.subs({xs[i - 1]: xs[i], xs[i]: xs[i - 1]}, simultaneous=True)
            num = sp.Poly(f - fi, xs)
            den = sp.Poly(xs[i - 1] - xs[i], xs)
            q_poly, rem = sp.div(num, den)
            assert rem.is_zero
            return sp.expand(-beta * f + (1 + beta * xs[i - 1]) * q_poly.as_expr())

        # Downward BFS by inv_length from w0
        by_len = defaultdict(list)
        for z in invols:
            by_len[inv_length(z)].append(z)
        max_len = max(by_len.keys())
        for L in range(max_len - 1, -1, -1):
            for z in by_len[L]:
                found = False
                for i in range(1, n):
                    zp = s_circ_z_circ_s(i, z)
                    if zp != z:
                        assert inv_length(zp) == L + 1
                        val = bpartial(i, iG[zp])
                        if z in iG:
                            assert sp.expand(iG[z] - val) == 0
                        else:
                            iG[z] = val
                        found = True
                assert found

        for z in invols:
            assert sp.expand(R_z[z] - iG[z]) == 0, f"iG-conj failed at n={n}, z={z}"

        # Also check Proposition 7.1 (beta=1 sum over all z in I_n)
        sum_R = sp.expand(sum(R_z[z].subs(beta, 1) for z in invols))
        sum_G = sp.expand(sum(iG[z].subs(beta, 1) for z in invols))
        assert sp.expand(sum_R - sum_G) == 0


def main() -> int:
    verify_bulk_ybe()
    verify_reflection_eq()
    verify_conjecture_small_n()
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
