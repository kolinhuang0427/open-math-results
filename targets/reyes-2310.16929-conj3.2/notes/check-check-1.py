#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/reyes-2310.16929-conj3.2/.

Directly constructs F_k(C_6) for k = 0, 1, 2, 3 from primary source definitions
(symmetric difference of k-subsets), computes exact integer Laplacian matrices L = D - A
and characteristic polynomials P_k(x) in Z[x], verifies exact divisibility and factorizations,
and proves alpha_3(C_6) < alpha_2(C_6) via exact algebraic roots (zero floats).
"""

import itertools
import sympy as sp


def token_laplacian(n: int, edges: set[tuple[int, int]], k: int) -> sp.Matrix:
    """Exact integer Laplacian L = D - A of the k-token graph F_k(G)."""
    if k == 0:
        return sp.Matrix([[0]])
    verts = list(itertools.combinations(range(n), k))
    m = len(verts)
    L = sp.zeros(m, m)
    for i in range(m):
        si = set(verts[i])
        deg = 0
        for j in range(i + 1, m):
            sj = set(verts[j])
            sym_diff = si ^ sj
            if len(sym_diff) == 2:
                u, v = tuple(sorted(sym_diff))
                if (u, v) in edges:
                    L[i, j] = -1
                    L[j, i] = -1
                    deg += 1
        # Wait: deg for i must count ALL j != i, not just j > i!
    # Recompute degrees cleanly from off-diagonal entries:
    for i in range(m):
        L[i, i] = -sum(L[i, j] for j in range(m) if j != i)
    return L


def main() -> None:
    n = 6
    c6_edges = {tuple(sorted((i, (i + 1) % 6))) for i in range(6)}
    x = sp.Symbol("x")

    P = []
    for k in range(4):
        L_k = token_laplacian(n, c6_edges, k)
        # Verify Laplacian row sums are 0 and symmetric
        assert L_k == L_k.T
        for i in range(L_k.rows):
            assert sum(L_k[i, j] for j in range(L_k.cols)) == 0
        P_k = sp.Poly(sp.Matrix(L_k).charpoly(x).as_expr(), x, domain="ZZ")
        P.append(P_k)

    # Expected exact P_0, P_1, P_2, P_3 from COUNTEREXAMPLE.md
    exp_P0 = sp.Poly(x, x, domain="ZZ")
    exp_P1 = sp.Poly(x * (x - 1) ** 2 * (x - 3) ** 2 * (x - 4), x, domain="ZZ")
    exp_P2 = sp.Poly(
        x * (x - 1) ** 2 * (x - 2) * (x - 3) ** 2 * (x - 4) * (x - 5) ** 2 * (x**2 - 10 * x + 20) * (x**2 - 7 * x + 8) ** 2,
        x,
        domain="ZZ",
    )
    exp_P3 = sp.Poly(
        x
        * (x - 1) ** 2
        * (x - 2)
        * (x - 3) ** 2
        * (x - 4) ** 3
        * (x - 5) ** 2
        * (x - 6)
        * (x**2 - 10 * x + 12)
        * (x**2 - 10 * x + 20)
        * (x**2 - 7 * x + 8) ** 2,
        x,
        domain="ZZ",
    )
    assert P == [exp_P0, exp_P1, exp_P2, exp_P3], f"Charpoly mismatch: {P}"

    # Verify exact divisibility P_0 | P_1 | P_2 | P_3 and quotients Q_1, Q_2, Q_3
    Q1, r1 = sp.div(P[1], P[0])
    Q2, r2 = sp.div(P[2], P[1])
    Q3, r3 = sp.div(P[3], P[2])
    assert r1 == 0 and r2 == 0 and r3 == 0
    assert Q1 == sp.Poly((x - 1) ** 2 * (x - 3) ** 2 * (x - 4), x, domain="ZZ")
    assert Q2 == sp.Poly((x - 2) * (x - 5) ** 2 * (x**2 - 10 * x + 20) * (x**2 - 7 * x + 8) ** 2, x, domain="ZZ")
    assert Q3 == sp.Poly((x - 4) ** 2 * (x - 6) * (x**2 - 10 * x + 12), x, domain="ZZ")

    # Exact algebraic minima alpha_1, alpha_2, alpha_3 via sympy.real_roots (CRootOf)
    roots_Q1 = sp.real_roots(Q1)
    roots_Q2 = sp.real_roots(Q2)
    roots_Q3 = sp.real_roots(Q3)
    alpha1 = min(roots_Q1)
    alpha2 = min(roots_Q2)
    alpha3 = min(roots_Q3)

    assert sp.simplify(alpha1 - 1) == 0
    assert sp.simplify(alpha2 - (7 - sp.sqrt(17)) / 2) == 0
    assert sp.simplify(alpha3 - (5 - sp.sqrt(13))) == 0
    assert alpha3 < alpha2
    # Also check exact integer chain: 9*17 = 153 < 169 = 13^2
    assert 9 * 17 < 13 * 13

    print(f"alpha_1(C_6) = {alpha1}")
    print(f"alpha_2(C_6) = {alpha2} = {(7 - sp.sqrt(17)) / 2}")
    print(f"alpha_3(C_6) = {alpha3} = {5 - sp.sqrt(13)}")
    print(f"Strict inequality alpha_3(C_6) < alpha_2(C_6): {alpha3 < alpha2}")
    print("PASS")


if __name__ == "__main__":
    main()
