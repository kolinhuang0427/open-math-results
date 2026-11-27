#!/usr/bin/env python3
"""Exact-rational verification of a counterexample to Ivanov (2026) Conjecture 6 (conj:fleanverts).

Constructs an explicit primitive 13-polytope P = {x in R^13 : A x <= b} with 24 facets
(hence not an affine 13-cube, which has 26 facets) and 8704 > 8192 = 2^13 vertices.

Uses only Python standard library exact arithmetic (fractions.Fraction); zero floating point.
"""

from fractions import Fraction
import itertools
import time


def det3(M):
    return (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )


def solve3(M, rhs):
    d = det3(M)
    if d == 0:
        return None
    cols = []
    for col in range(3):
        Mc = [row[:] for row in M]
        for r in range(3):
            Mc[r][col] = rhs[r]
        cols.append(Fraction(det3(Mc), d))
    return tuple(cols)


def exact_rank(mat, ncols):
    """Exact Gaussian elimination rank over Q for a list of Fraction/int rows."""
    rows = [[Fraction(x) for x in row] for row in mat]
    rank = 0
    for c in range(ncols):
        piv = None
        for r in range(rank, len(rows)):
            if rows[r][c] != 0:
                piv = r
                break
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        pv = rows[rank][c]
        for r in range(rank + 1, len(rows)):
            if rows[r][c] != 0:
                fac = rows[r][c] / pv
                for j in range(c, ncols):
                    rows[r][j] -= fac * rows[rank][j]
        rank += 1
    return rank


def main():
    t0 = time.time()
    d = 13
    k = 10  # d = 3 + k, n = 4 + 2k = 24 facets

    # Build A (24 x 13) and b (24,) with small integer entries.
    # Coordinates: (x1, x2, x3, y0, ..., y9)
    A = []
    b = []

    # 4 simplex facets in (x1, x2, x3)
    A.append([1, 0, 0] + [0] * k); b.append(100)
    A.append([0, 1, 0] + [0] * k); b.append(100)
    A.append([0, 0, 1] + [0] * k); b.append(100)
    A.append([-1, -1, -1] + [0] * k); b.append(100)

    # 2k = 20 lifted facets for t_j = -j (j = 0..9):
    #   y_j <= 1
    #   -y_j + x1 + x2 - j * x3 <= 119 + j^2
    # Eliminating y_j yields the 3D slice x1 + x2 - j * x3 <= 120 + j^2.
    for j in range(k):
        r1 = [0] * d
        r1[3 + j] = 1
        A.append(r1); b.append(1)

        r2 = [0] * d
        r2[0] = 1
        r2[1] = 1
        r2[2] = -j
        r2[3 + j] = -1
        A.append(r2); b.append(119 + j * j)

    n = len(A)
    assert n == 24

    # 1. Verify origin 0 is strictly interior: A @ 0 < b.
    for i in range(n):
        assert b[i] > 0, f"Origin not strictly interior at row {i}"

    # 2. Verify positive spanning (boundedness of P) via explicit strictly positive mu: sum mu_i A[i] = 0.
    # sum_{j=0..9} (e_{3+j} + (-e_{3+j} + e1 + e2 - j e3)) = 10 e1 + 10 e2 - 45 e3.
    # Add 1*e1 + 1*e2 + 56*e3 + 11*(-e1-e2-e3) = 0.
    mu = [1, 1, 56, 11] + [1] * (2 * k)
    assert all(m > 0 for m in mu)
    for c in range(d):
        s = sum(mu[i] * A[i][c] for i in range(n))
        assert s == 0, f"Positive dependence failed at coord {c}: {s}"

    # 3. Verify primitivity (omitting any single halfspace leaves an unbounded ray r_i):
    # Check A[i] . r_i > 0 and A[m] . r_i <= 0 for all m != i.
    rays = [
        [1, -1, 0] + [0] * k,           # omit x1 <= 100
        [-1, 1, 0] + [0] * k,           # omit x2 <= 100
        [-1, -1, 2] + [0] * k,          # omit x3 <= 100
        [-10, 0, -1] + [0] * k,         # omit -x1-x2-x3 <= 100
    ]
    for j in range(k):
        rp = [0] * d; rp[3 + j] = 1
        rn = [0] * d; rn[3 + j] = -1
        rays.append(rp)                 # omit y_j <= 1
        rays.append(rn)                 # omit -y_j + ... <= 119 + j^2

    for i in range(n):
        ri = rays[i]
        for m in range(n):
            dot = sum(A[m][c] * ri[c] for c in range(d))
            if m == i:
                assert dot > 0, f"Ray {i} failed dot > 0 on row {i}: {dot}"
            else:
                assert dot <= 0, f"Ray {i} violated row {m}: {dot}"

    # 4. Compute ALL exact vertices of the 3D projection P_x = {x in R^3 : A3 x <= b3}.
    A3 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [-1, -1, -1],
    ] + [[1, 1, -j] for j in range(k)]
    b3 = [100, 100, 100, 100] + [120 + j * j for j in range(k)]

    px_verts = set()
    for idx_triple in itertools.combinations(range(len(A3)), 3):
        M = [A3[idx] for idx in idx_triple]
        rhs = [b3[idx] for idx in idx_triple]
        pt = solve3(M, rhs)
        if pt is None:
            continue
        # Check feasibility against all 14 3D inequalities
        if all(A3[m][0] * pt[0] + A3[m][1] * pt[1] + A3[m][2] * pt[2] <= b3[m] for m in range(len(A3))):
            px_verts.add(pt)

    assert len(px_verts) == 24, f"Expected 24 vertices in P_x, got {len(px_verts)}"

    # 5. Lift each vertex x of P_x to exact vertices of P in Q^13 and verify EVERY vertex!
    p_verts = set()
    for x in sorted(px_verts):
        choices = []
        for j in range(k):
            s_val = x[0] + x[1] - j * x[2]
            c_j = 120 + j * j
            upper = Fraction(1)
            lower = s_val - (119 + j * j)
            if s_val == c_j:
                assert lower == upper
                choices.append((upper,))
            else:
                assert lower < upper
                choices.append((upper, lower))
        for y_tup in itertools.product(*choices):
            v = x + y_tup
            # Check exact feasibility A v <= b and collect active rows
            active_rows = []
            for m in range(n):
                val = sum(A[m][c] * v[c] for c in range(d))
                assert val <= b[m], f"Vertex {v} violated row {m}: {val} > {b[m]}"
                if val == b[m]:
                    active_rows.append(A[m])
            assert len(active_rows) >= d, f"Too few active rows at {v}: {len(active_rows)}"
            # Check exact rank of active rows (for speed, note structure or check exact_rank on a subset)
            # Check full exact rank on ALL 8704 vertices!
            rk = exact_rank(active_rows, d)
            assert rk == d, f"Rank {rk} < {d} at {v}"
            p_verts.add(v)

    assert len(p_verts) > 2 ** d, f"Expected > {2**d} vertices, got {len(p_verts)}"
    print(f"PASS (d={d}, facets={n}, vertices={len(p_verts)} > 2^{d}={2**d}; P_x vertices={len(px_verts)}; {time.time()-t0:.2f}s)")


if __name__ == "__main__":
    main()
