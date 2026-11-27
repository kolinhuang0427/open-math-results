#!/usr/bin/env python3
"""Exact symbolic/integer verifier for the counterexample G = C_6 to arXiv:2310.16929v1 Conjecture 3.2."""

import itertools
import sympy as sp


def build_cycle_6():
    n = 6
    adj = {i: {(i - 1) % 6, (i + 1) % 6} for i in range(n)}
    return n, adj


def build_token_graph(n, adj, k):
    """Build F_k(G) from the k-subset symmetric-difference definition."""
    if k == 0:
        return [()], [[0]]
    subsets = list(itertools.combinations(range(n), k))
    idx = {s: i for i, s in enumerate(subsets)}
    m = len(subsets)
    L = [[0] * m for _ in range(m)]
    for i, A in enumerate(subsets):
        A_set = set(A)
        deg = 0
        for u in A:
            for v in adj[u]:
                if v not in A_set:
                    B = tuple(sorted((A_set - {u}) | {v}))
                    j = idx[B]
                    L[i][j] -= 1
                    deg += 1
        L[i][i] = deg
    return subsets, L


def main():
    n, adj = build_cycle_6()
    x = sp.Symbol("x")

    polys = {}
    sizes = {0: 1, 1: 6, 2: 15, 3: 20}
    for k in range(4):
        subs, L_int = build_token_graph(n, adj, k)
        assert len(subs) == sizes[k]
        L_mat = sp.Matrix(L_int)
        assert L_mat.is_symmetric()
        # Verify row sums are 0 (Laplacian property)
        for row in L_int:
            assert sum(row) == 0
        polys[k] = sp.Poly(L_mat.charpoly(x).as_expr(), x, domain="ZZ")

    # Verify spectral inclusion P_0 | P_1 | P_2 | P_3 in Z[x]
    quot = {}
    for k in range(1, 4):
        q, r = sp.div(polys[k], polys[k - 1], x, domain="ZZ")
        assert r.is_zero, f"P_{k-1} does not divide P_{k}!"
        quot[k] = sp.Poly(q, x, domain="ZZ")

    # Verify exact quotient polynomials against COUNTEREXAMPLE.md
    expected_Q1 = sp.Poly((x - 1) ** 2 * (x - 3) ** 2 * (x - 4), x, domain="ZZ")
    expected_Q2 = sp.Poly(
        (x - 2) * (x - 5) ** 2 * (x ** 2 - 10 * x + 20) * (x ** 2 - 7 * x + 8) ** 2,
        x,
        domain="ZZ",
    )
    expected_Q3 = sp.Poly((x - 4) ** 2 * (x - 6) * (x ** 2 - 10 * x + 12), x, domain="ZZ")

    assert quot[1] == expected_Q1
    assert quot[2] == expected_Q2
    assert quot[3] == expected_Q3

    # Exact root extraction (with multiplicities) via sympy.real_roots (exact CRootOf, zero floats)
    roots1 = sp.real_roots(quot[1])
    roots2 = sp.real_roots(quot[2])
    roots3 = sp.real_roots(quot[3])

    assert len(roots1) == quot[1].degree()
    assert len(roots2) == quot[2].degree()
    assert len(roots3) == quot[3].degree()

    a1 = roots1[0]
    a2 = roots2[0]
    a3 = roots3[0]

    assert sp.simplify(a1 - 1) == 0
    assert sp.simplify(a2 - (7 - sp.sqrt(17)) / 2) == 0
    assert sp.simplify(a3 - (5 - sp.sqrt(13))) == 0

    # Exact integer/algebraic check that alpha_3(C_6) < alpha_2(C_6)
    assert 9 * 17 < 13 * 13  # 153 < 169
    assert a3 < a2

    print("PASS: C_6 refutes Conjecture 3.2: alpha_1=1, alpha_2=(7-sqrt(17))/2, alpha_3=5-sqrt(13) < alpha_2.")


if __name__ == "__main__":
    main()
