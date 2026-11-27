#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A045742 (Mathar 2022 D-finite recurrence).

Written directly from live OEIS A045742 (rev. 20) definitions and PROOF.md
without reading verify.py or author notes. Zero floating-point arithmetic.
"""

from __future__ import annotations

from math import comb
import sys
import sympy as sp


OEIS_DATA = [
    0, 1, 13, 141, 1456, 14778, 149031, 1499773, 15089932, 151927854,
    1531242362, 15451614738, 156114597744, 1579223536788, 15993825704427,
    162159485143581, 1645827425223220, 16720488433727910, 170023231905932790,
]


def a_formula(n: int) -> int:
    if n <= 2:
        return 0
    total = sum(k * comb(n + k - 2, k) * comb(3 * n - 3, n - 2 - k) for k in range(1, n - 1))
    assert total % (n - 1) == 0
    return total // (n - 1)


def poly_mul_trunc(p: list[int], q: list[int], deg: int) -> list[int]:
    out = [0] * (deg + 1)
    for i, pi in enumerate(p):
        if pi == 0 or i > deg:
            continue
        for j, qj in enumerate(q):
            if i + j > deg:
                break
            out[i + j] += pi * qj
    return out


def main() -> int:
    # 1. Check OEIS formula against all 19 live OEIS A045742 data terms (offset 2 -> n = 2..20)
    N = 45
    a_vals = [a_formula(n) for n in range(N + 1)]  # a[0]=a[1]=a[2]=0, a[2..20] == OEIS_DATA
    assert a_vals[2 : 2 + len(OEIS_DATA)] == OEIS_DATA, "Formula disagrees with live OEIS A045742 data"
    print(f"[1/4] Closed-form sum matches all {len(OEIS_DATA)} live OEIS A045742 terms (n=2..20).")

    # 2. Step 1: Verify t(x) = x*(1+t)^3/(1-t), y(x) = x*t^2*(1+t)/(1-4t+t^2), and 6x6 resultant
    # Solve t(1-t) = x(1+t)^3 mod x^{N+1}
    t_ser = [0] * (N + 1)
    for _ in range(N + 1):
        t2 = poly_mul_trunc(t_ser, t_ser, N)
        t3 = poly_mul_trunc(t2, t_ser, N)
        # (1+t)^3 = 1 + 3t + 3t^2 + t^3
        one_pt3 = [1 if m == 0 else 0 for m in range(N + 1)]
        for m in range(N + 1):
            one_pt3[m] = (1 if m == 0 else 0) + 3 * t_ser[m] + 3 * t2[m] + t3[m]
        for m in range(1, N + 1):
            t_ser[m] = one_pt3[m - 1] + t2[m]

    # Verify x t^2 (1+t) == y * (1 - 4t + t^2) mod x^{N+1}
    t2 = poly_mul_trunc(t_ser, t_ser, N)
    t3 = poly_mul_trunc(t2, t_ser, N)
    lhs_y = [0] + [t2[m - 1] + t3[m - 1] for m in range(1, N + 1)]
    den_t = [(1 if m == 0 else 0) - 4 * t_ser[m] + t2[m] for m in range(N + 1)]
    rhs_y = poly_mul_trunc(a_vals, den_t, N)
    assert lhs_y == rhs_y, "Step 1 y(x) identity mismatch"

    x, y, t_sym = sp.symbols("x y t_sym")
    E1 = x * (1 + t_sym) ** 3 - t_sym * (1 - t_sym)
    E2 = y * (1 - 4 * t_sym + t_sym**2) - x * t_sym**2 * (1 + t_sym)
    res_expr = sp.expand(sp.resultant(E1, E2, t_sym))
    P_expr = x**4 - 27 * x**3 * y + 108 * x**2 * y**3 + 108 * x**2 * y**2 + 13 * x**2 * y - x * y - y**3 - y**2
    assert sp.expand(res_expr - 2 * x * P_expr) == 0, "6x6 Sylvester resultant mismatch"
    print("[2/4] Step 1 series identity and 6x6 Sylvester resultant Res_t(E1,E2) = 2x P(x,y) verified.")

    # 3. Step 2: Exact Z[x,y] division Q(x,y) = P(x,y)*R(x,y) and order-3 ODE
    Px = sp.diff(P_expr, x)
    Py = sp.diff(P_expr, y)
    N1 = -Px
    N2 = sp.expand((Py * sp.diff(N1, x) + N1 * sp.diff(N1, y)) * Py - 1 * N1 * (Py * sp.diff(Py, x) + N1 * sp.diff(Py, y)))
    N3 = sp.expand((Py * sp.diff(N2, x) + N1 * sp.diff(N2, y)) * Py - 3 * N2 * (Py * sp.diff(Py, x) + N1 * sp.diff(Py, y)))

    p_inhom = 2544 * x**3
    p0 = 7632 * x**3
    p1 = 24 * x**2 * (4554 * x**2 + 2594 * x - 947)
    p2 = x**2 * (1018008 * x**3 - 180144 * x**2 + 13344 * x - 947)
    p3 = x**3 * (4554 * x - 523) * (108 * x**2 - 1)

    R_xy, rx, ry = sp.polys.rings.ring("x y", sp.ZZ)
    Py_r = R_xy.from_expr(Py)
    Q_r = (
        Py_r**5 * (R_xy.from_expr(p_inhom) + R_xy.from_expr(p0) * ry)
        + Py_r**4 * R_xy.from_expr(p1) * R_xy.from_expr(N1)
        + Py_r**2 * R_xy.from_expr(p2) * R_xy.from_expr(N2)
        + R_xy.from_expr(p3) * R_xy.from_expr(N3)
    )
    P_r = R_xy.from_expr(P_expr)
    quo, rem = Q_r.div(P_r)
    assert rem == 0, "Q(x,y) is not divisible by P(x,y) in Z[x,y]"
    assert quo * P_r == Q_r

    # Direct series check of the order-3 ODE up to x^{N-3}
    def poly_c(expr: sp.Expr, cap: int) -> list[int]:
        p = sp.Poly(sp.expand(expr), x)
        arr = [0] * (cap + 1)
        for (pw,), v in p.terms():
            if pw <= cap:
                arr[pw] = int(v)
        return arr

    yp = [m * a_vals[m] for m in range(1, N + 1)] + [0]
    ypp = [m * yp[m] for m in range(1, N + 1)] + [0]
    yppp = [m * ypp[m] for m in range(1, N + 1)] + [0]
    M_ode = N - 3
    t0 = poly_mul_trunc(poly_c(p0, M_ode), a_vals, M_ode)
    t1 = poly_mul_trunc(poly_c(p1, M_ode), yp, M_ode)
    t2 = poly_mul_trunc(poly_c(p2, M_ode), ypp, M_ode)
    t3 = poly_mul_trunc(poly_c(p3, M_ode), yppp, M_ode)
    pi_c = poly_c(p_inhom, M_ode)
    for m in range(M_ode + 1):
        assert pi_c[m] + t0[m] + t1[m] + t2[m] + t3[m] == 0, f"ODE failed at x^{m}"
    print("[3/4] Step 2 exact Z[x,y] division Q = P*R and order-3 ODE verified.")

    # 4. Step 3: Extract C_0(n)..C_3(n) symbolically and check recurrence up to n=150
    n_sym = sp.Symbol("n")
    C_from_ode = [sp.Integer(0)] * 4
    for k_ord, pk_expr in enumerate((p0, p1, p2, p3)):
        pk_poly = sp.Poly(sp.expand(pk_expr), x)
        for (d,), coeff in pk_poly.terms():
            j = d - k_ord
            assert 0 <= j <= 3, f"Out-of-range shift j={j} in p_{k_ord}"
            falling = sp.Integer(1)
            m_sym = n_sym - j
            for i in range(k_ord):
                falling *= (m_sym - i)
            C_from_ode[j] += int(coeff) * falling

    C_mathar = [
        n_sym * (n_sym - 1) * (523 * n_sym - 1993),
        -6 * (n_sym - 1) * (759 * n_sym**2 - 6019 * n_sym + 12790),
        -12 * (n_sym - 2) * (4707 * n_sym**2 - 17937 * n_sym + 6260),
        72 * (3 * n_sym - 10) * (759 * n_sym - 2224) * (3 * n_sym - 11),
    ]
    for j in range(4):
        assert sp.expand(C_from_ode[j] - C_mathar[j]) == 0, f"C_{j}(n) mismatch"

    N_REC = 150
    a_ext = [a_formula(n) for n in range(N_REC + 1)]
    for n in range(5, N_REC + 1):
        s = sum(int(C_mathar[j].subs(n_sym, n)) * a_ext[n - j] for j in range(4))
        assert s == 0, f"Mathar recurrence failed at n={n}"
    print(f"[4/4] Step 3 symbolic Z[n] coefficient match and recurrence verified for 5 <= n <= {N_REC}.")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
