"""Independent exact verifier for targets/oeis-A125790/PROOF.md.

Written strictly from live OEIS A125790 (rev 47) and PROOF.md,
without reading verify.py.
"""

from __future__ import annotations

import math
import sys
from sympy import Poly, Rational, binomial, expand, factor, symbols

# Verbatim OEIS A125790 example rows (first entries for n = 0..8)
OEIS_ROWS = {
    0: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    2: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169],
    3: [1, 10, 35, 84, 165, 286, 455, 680, 969, 1330, 1771, 2300],
    4: [1, 36, 201, 656, 1625, 3396, 6321, 10816, 17361, 26500, 38841],
    5: [1, 202, 1827, 8148, 25509, 64350, 140231, 274856, 497097],
    6: [1, 1828, 27337, 167568, 664665, 2026564, 5174449, 11622976],
    7: [1, 27338, 692003, 5866452, 29559717, 109082974, 326603719],
    8: [1, 692004, 30251721, 356855440, 2290267225, 10243585092],
}


def compute_T(max_n: int, max_k_top: int) -> dict[tuple[int, int], int]:
    """Exact array T(n,k) by OEIS A125790 recurrence."""
    need_k = {max_n: max_k_top}
    for n in range(max_n - 1, -1, -1):
        need_k[n] = 2 * need_k[n + 1]
    T: dict[tuple[int, int], int] = {}
    for k in range(need_k[0] + 1):
        T[(0, k)] = 1
    for n in range(1, max_n + 1):
        T[(n, 0)] = 1
        for k in range(1, need_k[n] + 1):
            T[(n, k)] = T[(n, k - 1)] + T[(n - 1, 2 * k)]
    return T


def main() -> int:
    # 1. Exact table T(n,k) up to n=10, k=40 (needs T(0, 40 * 2^10) = 40960)
    max_n = 10
    max_k = 40
    T = compute_T(max_n, max_k)
    for n, row in OEIS_ROWS.items():
        for k, val in enumerate(row):
            assert T[(n, k)] == val, f"OEIS mismatch at ({n}, {k})"

    # 2. Construct P_n(t) via Step 1 polynomial difference equation & check all properties
    t, x = symbols("t x")
    P: list[Poly] = [Poly(1, t, domain="QQ")]
    for n in range(1, max_n + 1):
        # Solve f(t) - f(t-1) == P_{n-1}(2t) with deg f <= n and f(0) = 1
        coeffs = symbols(f"a1:{n + 1}")
        f_expr = Rational(1) + sum(coeffs[r - 1] * (t ** r) for r in range(1, n + 1))
        diff_poly = Poly(expand(f_expr - f_expr.subs(t, t - 1) - P[n - 1].as_expr().subs(t, 2 * t)), t)
        from sympy import solve
        sol = solve(diff_poly.all_coeffs(), coeffs)
        assert isinstance(sol, dict) and len(sol) == n
        pn_expr = expand(f_expr.subs(sol))
        pn = Poly(pn_expr, t, domain="QQ")
        P.append(pn)
        assert pn.degree() <= n
        assert pn.eval(0) == 1
        assert pn.eval(-1) == 0
        for k in range(0, max_k + 1):
            assert pn.eval(k) == T[(n, k)], f"P_{n}({k}) != T({n},{k})"
        # Check (n+1)-th backward difference vanishes at i = n..25
        for i in range(n, 26):
            bd = sum(math.comb(n + 1, j) * ((-1) ** j) * pn.eval(i - j) for j in range(n + 2))
            assert bd == 0

    print("OEIS table (0<=n<=8), Step 1 P_n(t) & P_n(-1)=0, and backward differences (1<=n<=10): OK")

    # 3. Verify Kurkov's exact GF up to x^40 for every row 1 <= n <= 10
    for n in range(1, max_n + 1):
        num_terms = []
        for i in range(n):
            coeff = sum(
                math.comb(n + 1, j) * T[(n, i - j)] * ((-1) ** j)
                for j in range(i + 1)
            )
            num_terms.append(coeff * (x ** i))
        num_poly = sum(num_terms)
        # Multiply (num_poly) / (1 - x)^(n+1) by computing exact series via 1/(1-x)^(n+1) = sum_{m>=0} binom(m+n, n) x^m
        series = [0] * (max_k + 1)
        for i in range(n):
            ci = sum(math.comb(n + 1, j) * T[(n, i - j)] * ((-1) ** j) for j in range(i + 1))
            for k in range(i, max_k + 1):
                series[k] += ci * math.comb((k - i) + n, n)
        for k in range(max_k + 1):
            assert series[k] == T[(n, k)], f"GF mismatch at row {n}, k={k}"

    print(f"Kurkov row GF verified against T(n, 0..{max_k}) for all 1 <= n <= {max_n}: OK")

    # 4. Check Step 1 isomorphism nabla: V_n -> W_{n-1} directly via exact matrix det/rank
    from sympy import Matrix
    for n in range(1, max_n + 1):
        mat = []
        for r in range(1, n + 1):
            img = Poly(expand(t**r - (t - 1) ** r), t, domain="QQ")
            assert img.degree() == r - 1
            # Coefficients in basis 1, t, ..., t^{n-1}
            row_coeffs = [img.nth(d) for d in range(n)]
            mat.append(row_coeffs)
        M = Matrix(mat)
        assert M.rows == M.cols == n and M.det() != 0

    print("Step 1 isomorphism nabla: V_n -> W_{n-1} (dim n, det != 0 for 1<=n<=10): OK")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
