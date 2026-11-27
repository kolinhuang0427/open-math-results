#!/usr/bin/env python3
"""
Independent exact-arithmetic verifier for targets/oeis-A383410/
directly from live OEIS A383410 rev. 6 and A005649 rev. 123 definitions
and PROOF.md without reading verify.py or author notes. Zero floats.
"""
from __future__ import annotations

from math import comb, factorial
import sympy as sp


def verify_symbolic_pde() -> None:
    x, y = sp.symbols("x y")
    D = 1 + sp.exp(-y) - sp.exp(x)
    U_tilde = D ** (-2)
    assert sp.simplify(U_tilde.subs(x, 0) - sp.exp(2 * y)) == 0
    assert sp.simplify(sp.diff(U_tilde, x) - sp.exp(x + y) * sp.diff(U_tilde, y)) == 0
    F_closed = sp.exp(-y) * U_tilde
    assert sp.simplify(F_closed.subs(y, 0) - 1 / (2 - sp.exp(x)) ** 2) == 0
    print("PASS verify_symbolic_pde: U_tilde PDE and y=0 specialization exact")


def verify_array_and_egf() -> None:
    # 1. Compute A(n, k) directly from A383410 recurrence for 0 <= n + k <= Dmax
    Dmax = 20
    A: dict[tuple[int, int], int] = {}
    for s in range(Dmax + 1):
        for n in range(s + 1):
            k = s - n
            if n == 0:
                A[(0, k)] = 1
            else:
                A[(n, k)] = sum(
                    comb(n - 1, i) * comb(k + 1, j) * A[(i, j)]
                    for i in range(n)
                    for j in range(k + 2)
                )

    # Match live OEIS A383410 %S downward antidiagonals (55 terms, n+k = 0..9)
    antidiags = [A[(n, s - n)] for s in range(10) for n in range(s + 1)]
    oeis_383410 = [
        1, 1, 2, 1, 4, 8, 1, 8, 22, 44, 1, 16, 62, 154, 308, 1, 32, 178, 554, 1306, 2612,
        1, 64, 518, 2038, 5690, 12994, 25988, 1, 128, 1522, 7634, 25366, 66338, 148282, 296564,
        1, 256, 4502, 29014, 115298, 346366, 867002, 1908274, 3816548,
        1, 512, 13378, 111554, 532726, 1844042, 5179798, 12564434, 27333706, 54667412,
    ]
    assert antidiags == oeis_383410

    # 2. Verify A005649 = [x^n/n!] (2 - e^x)^(-2) for n = 0..20 and match live OEIS %S (0..19)
    x = sp.Symbol("x")
    N_egf = 20
    exp_x = sum(x**k / factorial(k) for k in range(N_egf + 1))
    # Compute (2 - exp_x)^{-2} mod x^(N_egf+1) via exact series inversion:
    # Let q = 2 - exp_x = 1 - sum_{k>=1} x^k/k!
    # Square q^2 mod x^(N_egf+1) and invert
    q_coeffs = [sp.Rational(1)] + [-sp.Rational(1, factorial(k)) for k in range(1, N_egf + 1)]
    q2 = [sp.Rational(0)] * (N_egf + 1)
    for i in range(N_egf + 1):
        for j in range(N_egf + 1 - i):
            q2[i + j] += q_coeffs[i] * q_coeffs[j]
    inv_q2 = [sp.Rational(0)] * (N_egf + 1)
    inv_q2[0] = sp.Rational(1)
    for n in range(1, N_egf + 1):
        inv_q2[n] = -sum(q2[j] * inv_q2[n - j] for j in range(1, n + 1))
    a005649 = [int(inv_q2[n] * factorial(n)) for n in range(N_egf + 1)]

    oeis_005649 = [
        1, 2, 8, 44, 308, 2612, 25988, 296564, 3816548, 54667412, 862440068,
        14857100084, 277474957988, 5584100659412, 120462266974148,
        2772968936479604, 67843210855558628, 1757952715142990612,
        48093560991292628228, 1385244691781856307124,
    ]
    assert a005649[:len(oeis_005649)] == oeis_005649
    for n in range(Dmax + 1):
        assert A[(n, 0)] == a005649[n], f"A({n},0)={A[(n,0)]} != A005649({n})={a005649[n]}"

    # 3. Verify bivariate EGF F(x, y) == e^{-y}/(1 + e^{-y} - e^x)^2 and PDE up to total degree 10
    y = sp.Symbol("y")
    Tdeg = 10
    F_from_A = sum(
        sp.Rational(A[(n, k)], factorial(n) * factorial(k)) * (x**n) * (y**k)
        for n in range(Tdeg + 1)
        for k in range(Tdeg + 1 - n)
    )
    # Build U_tilde = D^{-2} by Neumann series since 1 - D = e^x - e^{-y} has zero constant term!
    one_minus_D = sp.expand(
        sum(x**n / factorial(n) for n in range(1, Tdeg + 1))
        - sum(((-y) ** k) / factorial(k) for k in range(1, Tdeg + 1))
    )
    # D^{-2} = (1 - w)^{-2} = sum_{m>=0} (m+1) w^m mod (x,y)^{Tdeg+1}
    U_tilde_poly = sp.Integer(0)
    w_pow = sp.Integer(1)
    for m in range(Tdeg + 1):
        U_tilde_poly = sp.expand(U_tilde_poly + (m + 1) * w_pow)
        w_pow_next = sp.expand(w_pow * one_minus_D)
        # Drop terms of total degree > Tdeg
        p = sp.Poly(w_pow_next, x, y)
        w_pow = sum(coef * x**i * y**j for (i, j), coef in p.terms() if i + j <= Tdeg)

    exp_my = sum(((-y) ** k) / factorial(k) for k in range(Tdeg + 1))
    F_closed_poly = sp.Poly(sp.expand(exp_my * U_tilde_poly), x, y)
    F_closed_trunc = sum(coef * x**i * y**j for (i, j), coef in F_closed_poly.terms() if i + j <= Tdeg)
    assert sp.expand(F_from_A - F_closed_trunc) == 0

    print(f"PASS verify_array_and_egf: A(n,k) antidiags (55 terms), A005649 (0..20), bivariate EGF mod deg {Tdeg+1}")


def main() -> None:
    verify_symbolic_pde()
    verify_array_and_egf()
    print("PASS")


if __name__ == "__main__":
    main()
