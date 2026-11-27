#!/usr/bin/env python3
"""
Independent exact-arithmetic verifier for targets/oeis-A168503/
directly from live OEIS A168503 rev. 20 definitions and PROOF.md
without reading verify.py or author notes. Zero floats.
"""
from __future__ import annotations

import sympy as sp


def verify_symbolic() -> None:
    x, u, u1, u2, A_sym = sp.symbols("x u u1 u2 A")

    # 1. Continued fraction operator T(u) and x-adic contraction T(u1) - T(u2)
    T_cf = 1 / (1 - x / (1 - 2 * x / (1 - 3 * x * u)))
    T_rat = (1 - 2 * x - 3 * x * u) / (1 - 3 * x - 3 * x * (1 - x) * u)
    assert sp.simplify(T_cf - T_rat) == 0

    denom1 = 1 - 3 * x - 3 * x * (1 - x) * u1
    denom2 = 1 - 3 * x - 3 * x * (1 - x) * u2
    diff_T = T_rat.subs(u, u1) - T_rat.subs(u, u2)
    assert sp.simplify(diff_T - 6 * x**3 * (u1 - u2) / (denom1 * denom2)) == 0

    # 2. Fixed-point quadratic and completing the square
    quad = 3 * x * (1 - x) * A_sym**2 - A_sym + (1 - 2 * x)
    assert sp.simplify((1 - 3 * x - 3 * x * (1 - x) * A_sym) * A_sym - (1 - 2 * x - 3 * x * A_sym) + quad) == 0
    Delta = 1 - 12 * x + 36 * x**2 - 24 * x**3
    assert sp.expand(1 - 12 * x * (1 - x) * (1 - 2 * x) - Delta) == 0
    assert sp.expand(12 * x * (1 - x) * quad - ((1 - 6 * x * (1 - x) * A_sym) ** 2 - Delta)) == 0

    # 3. ODE polynomial reductions and coefficient extraction equivalence
    dDelta = sp.diff(Delta, x)
    assert sp.expand(dDelta - (-12 + 72 * x - 72 * x**2)) == 0
    assert sp.expand(Delta * (x - x**2) - (x - 13 * x**2 + 48 * x**3 - 60 * x**4 + 24 * x**5)) == 0
    assert sp.expand(Delta * (1 - 2 * x) - (-6 + 36 * x - 36 * x**2) * (x - x**2) - (1 - 8 * x + 18 * x**2 - 24 * x**3 + 12 * x**4)) == 0
    assert sp.expand(-sp.Rational(1, 12) * dDelta - (1 - 6 * x + 6 * x**2)) == 0

    n, a0, a1, a2, a3, a4 = sp.symbols("n a0 a1 a2 a3 a4")
    lhs_ode = (
        n * a0 - 13 * (n - 1) * a1 + 48 * (n - 2) * a2 - 60 * (n - 3) * a3 + 24 * (n - 4) * a4
        + a0 - 8 * a1 + 18 * a2 - 24 * a3 + 12 * a4
    )
    mathar = (
        (n + 1) * a0
        + (-13 * n + 5) * a1
        + 6 * (8 * n - 13) * a2
        + 12 * (-5 * n + 13) * a3
        + 12 * (2 * n - 7) * a4
    )
    assert sp.expand(lhs_ode - mathar) == 0
    print("PASS verify_symbolic: T(u), contraction, quadratic, ODE reductions, and Mathar coefficients exact")


def poly_inv_mod(q: list[int], N: int) -> list[int]:
    """Invert power series q with q[0] == 1 modulo x^(N+1) in Z[[x]]."""
    assert q[0] == 1
    inv = [0] * (N + 1)
    inv[0] = 1
    for n in range(1, N + 1):
        s = 0
        for j in range(1, min(n, len(q) - 1) + 1):
            s += q[j] * inv[n - j]
        inv[n] = -s
    return inv


def poly_mul_mod(a: list[int], b: list[int], N: int) -> list[int]:
    out = [0] * (N + 1)
    for i, ai in enumerate(a):
        if ai == 0 or i > N:
            continue
        for j in range(min(len(b), N + 1 - i)):
            out[i + j] += ai * b[j]
    return out


def verify_series_and_recurrence() -> None:
    Nmax = 80
    # 1. Exact x-adic fixed-point iteration T^m(1) mod x^(Nmax+1); each step increases precision by >= 3
    u = [1] + [0] * Nmax
    for _ in range(30):
        # num = 1 - 2x - 3x*u
        num = [0] * (Nmax + 1)
        num[0] = 1
        num[1] = -2
        for k in range(Nmax):
            num[k + 1] -= 3 * u[k]
        # den = 1 - 3x - 3x(1-x)*u = 1 - 3x - 3x*u + 3x^2*u
        den = [0] * (Nmax + 1)
        den[0] = 1
        den[1] = -3
        for k in range(Nmax):
            den[k + 1] -= 3 * u[k]
        for k in range(Nmax - 1):
            den[k + 2] += 3 * u[k]
        u = poly_mul_mod(num, poly_inv_mod(den, Nmax), Nmax)
    # Confirm exact fixed point T(u) == u mod x^(Nmax+1)
    num = [1, -2] + [0] * (Nmax - 1)
    den = [1, -3] + [0] * (Nmax - 1)
    for k in range(Nmax):
        num[k + 1] -= 3 * u[k]
        den[k + 1] -= 3 * u[k]
    for k in range(Nmax - 1):
        den[k + 2] += 3 * u[k]
    assert poly_mul_mod(num, poly_inv_mod(den, Nmax), Nmax) == u

    # 2. Match live OEIS %S prefix (n = 0..21)
    oeis_prefix = [
        1, 1, 3, 15, 87, 531, 3339, 21483, 140859, 938331, 6334875, 43257483,
        298276587, 2074128363, 14529077163, 102432060459, 726280074027,
        5175707802795, 37051160719275, 266319772644267, 1921345252699563,
        13907901060055467,
    ]
    assert u[:len(oeis_prefix)] == oeis_prefix

    # 3. Match SymPy radical G.f. (1 - sqrt(1 - 12x + 36x^2 - 24x^3))/(6x(1-x)) to x^20
    x = sp.Symbol("x")
    ser = sp.Poly(sp.series((1 - sp.sqrt(1 - 12 * x + 36 * x**2 - 24 * x**3)) / (6 * x * (1 - x)), x, 0, 21).removeO(), x)
    assert [int(ser.coeff_monomial(x**k)) for k in range(21)] == u[:21]

    # 4. Formal ODE at every [x^n] for 0 <= n <= Nmax
    rhs_ode = {0: 1, 1: -6, 2: 6}
    for n in range(Nmax + 1):
        lhs = (n + 1) * u[n]
        if n >= 1:
            lhs += (-13 * n + 5) * u[n - 1]
        if n >= 2:
            lhs += 6 * (8 * n - 13) * u[n - 2]
        if n >= 3:
            lhs += 12 * (-5 * n + 13) * u[n - 3]
        if n >= 4:
            lhs += 12 * (2 * n - 7) * u[n - 4]
        assert lhs == rhs_ode.get(n, 0), f"ODE mismatch at n={n}: {lhs}"

    # 5. Boundary n=3 (a(-1)=0) and Mathar recurrence for 4 <= n <= Nmax
    assert 4 * u[3] + (-39 + 5) * u[2] + 6 * 11 * u[1] + 12 * (-2) * u[0] == 0
    for n in range(4, Nmax + 1):
        val = (
            (n + 1) * u[n]
            + (-13 * n + 5) * u[n - 1]
            + 6 * (8 * n - 13) * u[n - 2]
            + 12 * (-5 * n + 13) * u[n - 3]
            + 12 * (2 * n - 7) * u[n - 4]
        )
        assert val == 0, f"Mathar recurrence failed at n={n}"

    print("PASS verify_series_and_recurrence: fixed point T(u)=u (n<=80), %S (0..21), GF (0..20), ODE/Mathar (n<=80)")


def main() -> None:
    verify_symbolic()
    verify_series_and_recurrence()
    print("PASS")


if __name__ == "__main__":
    main()
