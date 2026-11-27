#!/usr/bin/env python3
"""
Independent exact-arithmetic verifier for targets/oeis-A392058/
directly from live OEIS A392058 rev. 6 and A233335 rev. 20 definitions
and PROOF.md without reading verify.py or author notes. Zero floats.
"""
from __future__ import annotations

from math import comb, factorial
import sympy as sp


def series_inv_mod(q: list[sp.Rational], N: int) -> list[sp.Rational]:
    assert q[0] == 1
    inv = [sp.Rational(0)] * (N + 1)
    inv[0] = sp.Rational(1)
    for n in range(1, N + 1):
        inv[n] = -sum(q[j] * inv[n - j] for j in range(1, min(n, len(q) - 1) + 1))
    return inv


def series_mul_mod(a: list[sp.Rational], b: list[sp.Rational], N: int) -> list[sp.Rational]:
    out = [sp.Rational(0)] * (N + 1)
    for i, ai in enumerate(a):
        if ai == 0 or i > N:
            continue
        for j in range(min(len(b), N + 1 - i)):
            out[i + j] += ai * b[j]
    return out


def series_compose_mod(f: list[sp.Rational], g: list[sp.Rational], N: int) -> list[sp.Rational]:
    """Compute f(g(u)) mod u^(N+1), assuming g[0] == 0."""
    assert g[0] == 0
    res = [sp.Rational(0)] * (N + 1)
    g_pow = [sp.Rational(0)] * (N + 1)
    g_pow[0] = sp.Rational(1)
    for k, fk in enumerate(f):
        if fk != 0:
            for j in range(N + 1):
                res[j] += fk * g_pow[j]
        if k < len(f) - 1:
            g_pow = series_mul_mod(g_pow, g, N)
    return res


def compute_A233335_from_oeis_def(M: int) -> list[int]:
    """
    Solve E(int_0^x dt/E(t)) = exp(x) with E(0) = 1 uniquely term-by-term
    (PROOF.md Section 3 uniqueness recursion).
    """
    E = [sp.Rational(0)] * (M + 1)
    E[0] = sp.Rational(1)
    exp_c = [sp.Rational(1, factorial(k)) for k in range(M + 1)]
    for m in range(1, M + 1):
        # Compute Phi_E(u) = int_0^u dt/E(t) up to u^m (depends only on E[0..m-1])
        inv_E = series_inv_mod(E[:m], m - 1)
        Phi = [sp.Rational(0)] + [inv_E[j - 1] / j for j in range(1, m + 1)]
        # Temporarily set E[m] = 0, evaluate [u^m] E(Phi(u)), and note coefficient of E[m] in [u^m] E(Phi(u)) is Phi[1]^m = 1
        E_tmp = E[:]
        E_tmp[m] = sp.Rational(0)
        comp = series_compose_mod(E_tmp, Phi, m)
        E[m] = exp_c[m] - comp[m]
        # Double check
        E_chk = E[:]
        comp_chk = series_compose_mod(E_chk, Phi, m)
        assert comp_chk[m] == exp_c[m]
    return [int(E[k] * factorial(k)) for k in range(M + 1)]


def verify_all() -> None:
    # 1. Compute A(n, k) directly from A392058 recurrence for 0 <= n + k <= Dmax
    Dmax = 22
    A: dict[tuple[int, int], int] = {}
    for s in range(Dmax + 1):
        for n in range(s + 1):
            k = s - n
            if n == 0:
                A[(0, k)] = 1
            else:
                A[(n, k)] = A[(n - 1, k + 1)] + sum(
                    comb(k + 1, j) * A[(n - 1, j)] * A[(k - j, 0)]
                    for j in range(k + 1)
                )

    # Match live OEIS A392058 %S downward antidiagonals (n+k = 0..8, 45 terms)
    antidiags = [A[(n, s - n)] for s in range(9) for n in range(s + 1)]
    oeis_392058 = [
        1, 1, 2, 1, 5, 7, 1, 17, 31, 38, 1, 83, 178, 254, 292,
        1, 578, 1330, 2099, 2683, 2975,
        1, 5474, 12748, 21338, 29425, 35375, 38350,
        1, 66932, 153136, 263870, 382966, 489383, 566083, 604433,
        1, 1014002, 2249503, 3913556, 5865952, 7837136, 9538360, 10747226, 11351659,
    ]
    assert antidiags == oeis_392058

    # 2. Compute A233335 from its live OEIS functional equation and match live OEIS %S (0..21)
    M_233 = 22
    a233 = compute_A233335_from_oeis_def(M_233)
    oeis_233335 = [
        1, 1, 2, 7, 38, 292, 2975, 38350, 604433, 11351659, 249042701, 6283114723,
        179995680530, 5794486077958, 207806806310354, 8241414107222095,
        359171801820266717, 17107537203463252273, 886296777786378900077,
        49732564234138336160086, 3011177123882906437153214, 196063383282648338166793297,
    ]
    assert a233[:len(oeis_233335)] == oeis_233335

    # Verify conjecture A(n, 0) == A233335(n + 1) for 0 <= n <= 21
    for n in range(22):
        assert A[(n, 0)] == a233[n + 1], f"Mismatch at n={n}: {A[(n,0)]} != {a233[n+1]}"

    # 3. Verify intermediate PDE / method-of-characteristics steps on truncated series (total deg <= 10)
    x, y = sp.symbols("x y")
    Tdeg = 10

    def trunc_poly(expr: sp.Expr) -> sp.Expr:
        p = sp.Poly(sp.expand(expr), x, y)
        return sum(coef * x**i * y**j for (i, j), coef in p.terms() if i + j <= Tdeg)

    V_y = sp.Integer(1) + sum(sp.Rational(A[(m - 1, 0)], factorial(m)) * y**m for m in range(1, Tdeg + 2))
    G_xy = sum(
        sp.Rational(A[(n, k)], factorial(n) * factorial(k)) * x**n * y**k
        for n in range(Tdeg + 1)
        for k in range(Tdeg + 1 - n)
    )
    W_xy = trunc_poly(V_y * G_xy)

    # Check H_n(y) = d_y(V(y)*H_{n-1}(y)) mod y^(Tdeg+1-n)
    for n in range(1, Tdeg):
        H_n = sum(sp.Rational(A[(n, k)], factorial(k)) * y**k for k in range(Tdeg + 1 - n))
        H_prev = sum(sp.Rational(A[(n - 1, k)], factorial(k)) * y**k for k in range(Tdeg + 2 - n))
        rhs = sp.diff(V_y * H_prev, y)
        p = sp.Poly(sp.expand(H_n - rhs), y)
        for (deg,), coef in p.terms():
            assert deg > Tdeg - n or coef == 0

    # Check transport PDE: d_x W == V(y) d_y W up to total deg Tdeg - 1
    pde_diff = sp.Poly(sp.expand(sp.diff(W_xy, x) - V_y * sp.diff(W_xy, y)), x, y)
    for (i, j), coef in pde_diff.terms():
        assert i + j >= Tdeg or coef == 0

    # Check V(Phi(u)) == exp(u) mod u^(M_233)
    V_coeffs = [sp.Rational(1)] + [sp.Rational(A[(m - 1, 0)], factorial(m)) for m in range(1, M_233)]
    inv_V = series_inv_mod(V_coeffs, M_233 - 1)
    Phi = [sp.Rational(0)] + [inv_V[j - 1] / j for j in range(1, M_233)]
    V_of_Phi = series_compose_mod(V_coeffs, Phi, M_233 - 1)
    exp_coeffs = [sp.Rational(1, factorial(k)) for k in range(M_233)]
    assert V_of_Phi == exp_coeffs

    print(f"PASS verify_all: A392058 (45 terms), A233335 (22 terms), A(n,0)=A233335(n+1) (0..21), PDE & V(Phi(u))=e^u exact")


def main() -> None:
    verify_all()
    print("PASS")


if __name__ == "__main__":
    main()
