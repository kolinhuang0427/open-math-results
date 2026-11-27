#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for Ballantine-Beck-Merca (arXiv:2408.13346v1)
Conjectural Table of Minimal Periods for e_2 p_4(n) mod m (Section 1, lines 93-97).

Written directly from the primary-source definition in main.tex without reading verify.py.
Uses pure Python int arithmetic (zero floats).
"""

from __future__ import annotations

import sys


def brute_e2p4(n: int) -> int:
    """Brute-force sum of e_2(lambda) over all partitions lambda of n into 4 parts."""
    if n < 4:
        return 0
    total = 0
    for a in range(1, n + 1):
        for b in range(a, n - a + 1):
            for c in range(b, n - a - b + 1):
                d = n - a - b - c
                if d >= c:
                    total += a * b + a * c + a * d + b * c + b * d + c * d
    return total


def dp_e2p4_upto(N: int) -> list[int]:
    """Exact partition DP computing e_2 p_4(n) for 0 <= n <= N from the definition."""
    # State dp[k][s] = [count_of_partitions, sum_of_e1, sum_of_e2] for k parts summing to s.
    cnt = [[0] * (N + 1) for _ in range(5)]
    se1 = [[0] * (N + 1) for _ in range(5)]
    se2 = [[0] * (N + 1) for _ in range(5)]
    cnt[0][0] = 1

    for v in range(1, N + 1):
        # Process k from 4 down to 0 and multiplicities r = 1 .. 4-k
        for k in range(3, -1, -1):
            for s in range(0, N + 1 - v):
                c0 = cnt[k][s]
                if c0 == 0:
                    continue
                e1_0 = se1[k][s]
                e2_0 = se2[k][s]
                max_r = min(4 - k, (N - s) // v)
                for r in range(1, max_r + 1):
                    nk = k + r
                    ns = s + r * v
                    comb_r2 = (r * (r - 1)) // 2
                    cnt[nk][ns] += c0
                    se1[nk][ns] += e1_0 + r * v * c0
                    se2[nk][ns] += e2_0 + r * v * e1_0 + comb_r2 * v * v * c0
    return se2[4]


def main() -> int:
    MAX_N = 1400
    e2 = dp_e2p4_upto(MAX_N)

    # 1. Cross-check DP against brute-force partition enumeration for n = 0..40
    for n in range(41):
        assert e2[n] == brute_e2p4(n), f"DP vs brute mismatch at n={n}"
    print("[1/4] Direct partition DP matches brute-force enumeration for n = 0..40.")

    # 2. Check exact numerical counterexamples in COUNTEREXAMPLE.md
    assert e2[0] == 0
    assert e2[4] == 6
    assert e2[5] == 9 and e2[51] == 770034
    assert e2[2] == 0 and e2[6] == 25
    assert e2[1150] == 4204006824112 and e2[1150] % 10 == 2 != e2[0] % 10
    assert e2[1154] == 4277582023120 and e2[1154] % 10 == 0 != e2[4] % 10
    assert e2[1246] == 6275602376628 and e2[1246] % 18 == 6 != e2[0] % 18
    assert e2[1250] == 6376921776108 and e2[1250] % 18 == 0 != e2[4] % 18
    print("[2/4] Exact values at n=0,2,4,5,6,51,1150,1154,1246,1250 verified.")

    # 3. Independently verify the order-22 linear recurrence from main.tex lines 90-91
    # y(n+22) = -y(n) - y(n+1) + 3y(n+3) + 6y(n+4) + 3y(n+5) - 3y(n+6) - 12y(n+7)
    #           - 12y(n+8) - 2y(n+9) + 10y(n+10) + 18y(n+11) + 10y(n+12) - 2y(n+13)
    #           - 12y(n+14) - 12y(n+15) - 3y(n+16) + 3y(n+17) + 6y(n+18) + 3y(n+19) - y(n+21)
    # Note: first prove e2p4(n) has rational GF with denominator D(q) = (1-q)^6(1+q)^4(1+q^2)^3(1+q+q^2)^3
    # directly from parameterization a=t4+t3+t2+t1, b=t4+t3+t2, c=t4+t3, d=t4 (t4>=1, t1,t2,t3>=0):
    # Check that D(q) matches the recurrence polynomial and check e2[0..1400] satisfies it!
    import sympy as sp
    q = sp.Symbol("q")
    D_fac = (1 - q)**6 * (1 + q)**4 * (1 + q**2)**3 * (1 + q + q**2)**3
    D_exp = sp.expand(D_fac)
    # Recurrence polynomial R(q) = 1 + q - 3q^3 - ... + q^22 (reversed coefficients of y(n+22) - RHS = 0)
    coeffs_lhs = [1, 1, 0, -3, -6, -3, 3, 12, 12, 2, -10, -18, -10, 2, 12, 12, 3, -3, -6, -3, 0, 1, 1]
    R_poly = sum(c * q**i for i, c in enumerate(coeffs_lhs))
    assert sp.expand(D_exp - R_poly) == 0, "D(q) does not match order-22 recurrence!"
    # Independently derive the numerator N(q) = D(q) * sum_{n>=0} e2[n] q^n directly from
    # symbolic 4-part generating function:
    # For parts d=t4>=1, c=t4+t3, b=t4+t3+t2, a=t4+t3+t2+t1 with sum t1+2t2+3t3+4t4:
    # Use SymPy formal power series differentiation on 1 / ((1-z1 q)(1-z2 q^2)(1-z3 q^3)(1-z4 q^4))
    t1, t2, t3, t4 = sp.symbols("t1 t2 t3 t4")
    # Actually e_2(a, b, c, d) in terms of t_j (differentiate 1/((1-x1 q)(1-x2 q^2)(1-x3 q^3)(1-x4 q^4))):
    # d = t4, c = t4+t3, b = t4+t3+t2, a = t4+t3+t2+t1
    x1, x2, x3, x4 = sp.symbols("x1 x2 x3 x4")
    # Sum_{t4>=1, t1,t2,t3>=0} x1^t1 x2^t2 x3^t3 x4^t4 * q^{t1+2t2+3t3+4t4} = (x4 q^4) / ((1-x1 q)(1-x2 q^2)(1-x3 q^3)(1-x4 q^4))
    # Part values: d = x4*d_x4, c = x4*d_x4 + x3*d_x3, etc.
    def op_mul_var(expr, v):
        return sp.together(v * sp.diff(expr, v))

    G0 = (x4 * q**4) / ((1 - x1 * q) * (1 - x2 * q**2) * (1 - x3 * q**3) * (1 - x4 * q**4))
    # Apply linear differential operators corresponding to d, c, b, a:
    # Since operators commute? Wait: x_i*d_{x_i} commute with each other!
    def apply_d(e): return op_mul_var(e, x4)
    def apply_c(e): return op_mul_var(e, x4) + op_mul_var(e, x3)
    def apply_b(e): return op_mul_var(e, x4) + op_mul_var(e, x3) + op_mul_var(e, x2)
    def apply_a(e): return op_mul_var(e, x4) + op_mul_var(e, x3) + op_mul_var(e, x2) + op_mul_var(e, x1)

    G_e2 = (
        apply_a(apply_b(G0)) + apply_a(apply_c(G0)) + apply_a(apply_d(G0))
        + apply_b(apply_c(G0)) + apply_b(apply_d(G0)) + apply_c(apply_d(G0))
    )
    G_e2_sub = sp.cancel(G_e2.subs({x1: 1, x2: 1, x3: 1, x4: 1}))
    num, den = sp.fraction(G_e2_sub)
    # Check that den divides D_exp (so D(q) * G_e2 is a polynomial!)
    quo_den, rem_den = sp.poly(D_exp, q).div(sp.poly(den, q))
    assert rem_den.is_zero, "Derived denominator does not divide D(q)"
    N_poly = sp.poly(sp.expand(num * quo_den.as_expr()), q)
    assert N_poly.degree() < 22, f"deg N_poly = {N_poly.degree()} >= 22"
    # Verify exact series expansion up to n=MAX_N satisfies D_exp * G == N_poly (hence order-22 recurrence for ALL n >= 22!)
    for n in range(22, MAX_N + 1):
        val = sum(coeffs_lhs[j] * e2[n - j] for j in range(23))
        assert val == 0, f"Recurrence failed at n={n}"
    for n in range(22):
        val = sum(coeffs_lhs[j] * e2[n - j] for j in range(n + 1))
        assert val == int(N_poly.coeff_monomial(q**n)), f"Initial term mismatch at n={n}"
    print("[3/4] Symbolically proved exact rational GF N(q)/D(q) and order-22 recurrence for all n >= 22.")

    # 4. Verify pure periodicity and exact minimal periods modulo 10 and 18 via 22-state transition
    def minimal_period_mod(m: int, bound: int = 3000) -> int:
        # Since constant term of D(q) is 1 and deg 22 term is 1 (GL_22(Z) companion matrix),
        # sequence mod m is purely periodic from n=0; period divides any T where state_T == state_0.
        seq = [v % m for v in e2[:22]]
        # Use recurrence directly mod m up to bound
        state0 = tuple(seq)
        cur = list(seq)
        # Step forward using recurrence: e2(n) = -sum_{j=1}^{22} coeffs_lhs[j] * e2(n-j) mod m
        # Wait: coeffs_lhs[0] == 1, so y[n] = -sum_{j=1}^{22} coeffs_lhs[j]*y[n-j]
        for step in range(1, bound + 1):
            nxt = (-sum(coeffs_lhs[j] * cur[-j] for j in range(1, 23))) % m
            cur.append(nxt)
            if step <= MAX_N - 21:
                assert nxt == e2[21 + step] % m
            if tuple(cur[-22:]) == state0:
                return step
        raise AssertionError(f"Period mod {m} exceeded {bound}")

    per_10 = minimal_period_mod(10)
    per_18 = minimal_period_mod(18)
    assert per_10 == 1200 and per_10 != 1150
    assert per_18 == 1296 and per_18 != 1246
    # Verify non-periodicity of 1150 mod 10 and 1246 mod 18
    assert e2[1150] % 10 != e2[0] % 10
    assert e2[1246] % 18 != e2[0] % 18
    print(f"[4/4] Exact minimal periods verified: per(10) = {per_10} != 1150, per(18) = {per_18} != 1246.")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
