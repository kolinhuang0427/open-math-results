#!/usr/bin/env python3
"""
Independent exact-arithmetic verifier for targets/oeis-A157002/
directly from live OEIS A157002 rev. 15 definitions and PROOF.md
without reading verify.py or author notes. Zero floats.
"""
from __future__ import annotations

from math import comb
import sympy as sp


def verify_symbolic() -> None:
    x, A_sym = sp.symbols("x A")
    Delta = 1 - 4 * x + 4 * x**3
    P = x * (1 + x)

    # 1. Quadratic equation x(1+x)A^2 - A + (1-x) = 0 <=> (1 - 2x(1+x)A)^2 = Delta(x)
    quad = P * A_sym**2 - A_sym + (1 - x)
    sq_id = sp.expand(4 * P * quad - ((1 - 2 * P * A_sym) ** 2 - Delta))
    assert sq_id == 0

    # 2. ODE polynomial coefficients
    dDelta = sp.diff(Delta, x)
    dP = sp.diff(P, x)
    assert sp.expand(Delta * P - (x - 3 * x**2 - 4 * x**3 + 4 * x**4 + 4 * x**5)) == 0
    assert sp.expand(Delta * dP - sp.Rational(1, 2) * dDelta * P - (1 - 6 * x**2 - 2 * x**3 + 2 * x**4)) == 0
    assert sp.expand(-sp.Rational(1, 4) * dDelta - (1 - 3 * x**2)) == 0

    # 3. Coefficient extraction identity
    n, a0, a1, a2, a3, a4 = sp.symbols("n a0 a1 a2 a3 a4")
    lhs_ode = (
        n * a0 - 3 * (n - 1) * a1 - 4 * (n - 2) * a2 + 4 * (n - 3) * a3 + 4 * (n - 4) * a4
        + a0 - 6 * a2 - 2 * a3 + 2 * a4
    )
    mathar = (
        (n + 1) * a0
        + 3 * (-n + 1) * a1
        + 2 * (-2 * n + 1) * a2
        + 2 * (2 * n - 7) * a3
        + 2 * (2 * n - 7) * a4
    )
    assert sp.expand(lhs_ode - mathar) == 0
    print("PASS verify_symbolic: algebraic equation, ODE polynomials, and coefficient identity exact")


def verify_series_and_recurrence() -> None:
    Nmax = 80
    catalan = [comb(2 * k, k) // (k + 1) for k in range(Nmax + 1)]

    # 1. Compute (1 - x) * c(x(1 - x^2)) directly via exact integer polynomial convolution
    # First c(u) = sum_{k=0}^{Nmax} catalan[k] * u^k where u = x - x^3
    riordan = [0] * (Nmax + 1)
    # Build powers u^k truncated to deg <= Nmax
    u_pow = [1]  # u^0
    for k in range(Nmax + 1):
        # Contribute catalan[k] * (1 - x) * u^k
        for j, coef in enumerate(u_pow):
            if coef == 0:
                continue
            riordan[j] += catalan[k] * coef
            if j + 1 <= Nmax:
                riordan[j + 1] -= catalan[k] * coef
        # Next u^{k+1} = (x - x^3) * u_pow truncated to Nmax
        nxt = [0] * (min(len(u_pow) + 3, Nmax + 1))
        for j, coef in enumerate(u_pow):
            if j + 1 <= Nmax:
                nxt[j + 1] += coef
            if j + 3 <= Nmax:
                nxt[j + 3] -= coef
        u_pow = nxt

    # 2. Cross-check against OEIS explicit formula sum_{k=0..n} (-1)^floor((n-k+1)/2) C(k, floor((n-k)/2)) C_k
    for n in range(Nmax + 1):
        oeis_f = sum(
            ((-1) ** ((n - k + 1) // 2)) * comb(k, (n - k) // 2) * catalan[k]
            for k in range(n + 1)
            if (n - k) // 2 <= k
        )
        # Note for (1-x) * sum C_k x^k (1-x^2)^k, let's check both formulas match!
        assert riordan[n] == oeis_f, f"Riordan vs OEIS formula mismatch at n={n}: {riordan[n]} != {oeis_f}"

    # 3. Match live OEIS %S prefix (0..27)
    oeis_prefix = [
        1, 0, 1, 2, 6, 17, 51, 156, 488, 1552, 5006, 16337, 53849, 179015, 599535, 2020924,
        6851150, 23344138, 79902364, 274606264, 947240592, 3278404274, 11381240074,
        39621423949, 138288477617, 483805404673, 1696318159457, 5959737806635,
    ]
    assert riordan[:len(oeis_prefix)] == oeis_prefix

    # 4. SymPy series of radical G.f. (1 - sqrt(1 - 4x(1-x^2)))/(2x(1+x)) to x^20
    x = sp.Symbol("x")
    ser = sp.Poly(sp.series((1 - sp.sqrt(1 - 4 * x * (1 - x**2))) / (2 * x * (1 + x)), x, 0, 21).removeO(), x)
    assert [int(ser.coeff_monomial(x**k)) for k in range(21)] == riordan[:21]

    # 5. Formal power series ODE at every [x^n] for 0 <= n <= Nmax
    rhs_ode = {0: 1, 2: -3}
    for n in range(Nmax + 1):
        lhs = (n + 1) * riordan[n]
        if n >= 1:
            lhs += 3 * (-n + 1) * riordan[n - 1]
        if n >= 2:
            lhs += 2 * (-2 * n + 1) * riordan[n - 2]
        if n >= 3:
            lhs += 2 * (2 * n - 7) * riordan[n - 3]
        if n >= 4:
            lhs += 2 * (2 * n - 7) * riordan[n - 4]
        assert lhs == rhs_ode.get(n, 0), f"ODE mismatch at n={n}: {lhs}"

    # 6. Mathar recurrence for n >= 4 (and n=3 with a(-1)=0)
    assert 4 * riordan[3] + 3 * (-2) * riordan[2] + 2 * (-5) * riordan[1] + 2 * (-1) * riordan[0] == 0
    for n in range(4, Nmax + 1):
        val = (
            (n + 1) * riordan[n]
            + 3 * (-n + 1) * riordan[n - 1]
            + 2 * (-2 * n + 1) * riordan[n - 2]
            + 2 * (2 * n - 7) * riordan[n - 3]
            + 2 * (2 * n - 7) * riordan[n - 4]
        )
        assert val == 0, f"Mathar recurrence failed at n={n}"

    print("PASS verify_series_and_recurrence: Riordan vs OEIS formula (n<=80), %S (0..27), GF (0..20), ODE/Mathar (n<=80)")


def main() -> None:
    verify_symbolic()
    verify_series_and_recurrence()
    print("PASS")


if __name__ == "__main__":
    main()
