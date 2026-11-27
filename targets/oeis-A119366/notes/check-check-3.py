#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A119366 (Mathar 2025 D-finite recurrence).

Written directly from live OEIS A119366 (rev. 7) definitions and PROOF.md
without reading verify.py or author notes. Zero floating-point arithmetic.
"""

from __future__ import annotations

from math import comb
import sys
import sympy as sp


OEIS_DATA = [
    0, 1, 1, 1, 2, 11, 51, 177, 519, 1513, 5042, 18866, 71270, 257974,
    905425, 3193737, 11578842, 42930441, 159998493, 593445318,
    2194106568, 8138471667, 30399156174, 114219616809, 430344635913,
    1622777285682, 6125465491551,
]


def a_barry(n: int) -> int:
    if n == 0:
        return 0
    total = sum(comb(n, 3 * k + 1) * comb(n, 3 * k) for k in range(n // 3 + 1))
    assert total % n == 0
    return total // n


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
    # 1. Check Barry's formula against all 27 live OEIS A119366 data terms
    N_SERIES = 40
    a_vals = [a_barry(n) for n in range(N_SERIES + 1)]
    assert a_vals[: len(OEIS_DATA)] == OEIS_DATA, "Barry formula disagrees with live OEIS A119366 data"
    print(f"[1/4] Barry formula matches all {len(OEIS_DATA)} live OEIS A119366 terms.")

    # 2. Check Step 1: u_j = x * P_j(u_j) and algebraic / sqrt identity in Q(omega)[[x]]
    # Represent elements of Z[omega] as pairs (a, b) meaning a + b*omega with omega^2 = -1 - omega.
    def zom_mul(u: tuple[int, int], v: tuple[int, int]) -> tuple[int, int]:
        a, b = u
        c, d = v
        # (a + b w)(c + d w) = ac + (ad + bc)w + bd(-1 - w)
        return (a * c - b * d, a * d + b * c - b * d)

    def zom_add(u: tuple[int, int], v: tuple[int, int]) -> tuple[int, int]:
        return (u[0] + v[0], u[1] + v[1])

    def series_mul_zom(p: list[tuple[int, int]], q: list[tuple[int, int]], deg: int) -> list[tuple[int, int]]:
        out = [(0, 0)] * (deg + 1)
        for i in range(deg + 1):
            if p[i] == (0, 0):
                continue
            for j in range(deg + 1 - i):
                if q[j] != (0, 0):
                    out[i + j] = zom_add(out[i + j], zom_mul(p[i], q[j]))
        return out

    # Compute u_j(x) mod x^{N_SERIES+1} for j=0,1,2 from u_j = x * (w^j + (1+w^j)*u_j + u_j^2)
    w_pows = [(1, 0), (0, 1), (-1, -1)]
    u_series = []
    for j in range(3):
        wj = w_pows[j]
        one_plus_wj = zom_add((1, 0), wj)
        u = [(0, 0)] * (N_SERIES + 1)
        for _ in range(N_SERIES + 1):
            u2 = series_mul_zom(u, u, N_SERIES)
            nxt = [(0, 0)] * (N_SERIES + 1)
            nxt[1] = wj
            for m in range(2, N_SERIES + 1):
                nxt[m] = zom_add(zom_mul(one_plus_wj, u[m - 1]), u2[m - 1])
            u = nxt
        u_series.append(u)

    # Check y(x) = (u_0 + w^2 u_1 + w u_2) / 3
    for n in range(N_SERIES + 1):
        val = zom_add(u_series[0][n], zom_add(zom_mul(w_pows[2], u_series[1][n]), zom_mul(w_pows[1], u_series[2][n])))
        assert val[1] == 0 and val[0] == 3 * a_vals[n], f"Step 1 u_j trisection mismatch at n={n}"

    # Check (2x u_j + x(1+w^j) - 1)^2 == Delta_j(x)
    Delta_coeffs = [
        [(1, 0), (-4, 0), (0, 0)],
        [(1, 0), (-2, -2), (0, -3)],  # 1 + 2*w^2 x - 3*w x^2 since w^2 = -1-w
        [(1, 0), (0, 2), (3, 3)],     # 1 + 2*w x - 3*w^2 x^2
    ]
    for j in range(3):
        one_plus_wj = zom_add((1, 0), w_pows[j])
        lhs = [(-1, 0)] + [zom_add(zom_mul((2, 0), u_series[j][m - 1]), one_plus_wj if m == 1 else (0, 0)) for m in range(1, N_SERIES + 1)]
        lhs2 = series_mul_zom(lhs, lhs, N_SERIES)
        for m in range(N_SERIES + 1):
            exp_c = Delta_coeffs[j][m] if m <= 2 else (0, 0)
            assert lhs2[m] == exp_c, f"Delta_{j} identity mismatch at x^{m}"
    print(f"[2/4] Step 1 roots-of-unity trisection and Delta_j identities verified up to x^{N_SERIES}.")

    # 3. Step 2: Symbolic polynomial identity sum_{k=0}^4 p_k N_k (2x D)^{4-k} == 0 for D = Delta_0, Delta_1
    x, w = sp.symbols("x w")
    p0 = 12 * x * (9216 * x**4 - 453 * x**3 + 9541 * x**2 - 2253 * x - 1233)
    p1 = 6 * x * (179010 * x**7 - 513666 * x**6 - 153168 * x**5 + 43362 * x**4 - 15265 * x**3 - 12783 * x**2 + 4719 * x + 1233)
    p2 = 9 * x**2 * (232380 * x**7 - 519261 * x**6 - 237531 * x**5 - 117585 * x**4 - 12395 * x**3 + 8342 * x**2 + 1550 * x - 822)
    p3 = x**3 * (774306 * x**7 - 1378881 * x**6 - 664443 * x**5 - 871557 * x**4 + 173836 * x**3 - 1287 * x**2 - 9879 * x - 175)
    p4 = x**4 * (4 * x - 1) * (x**2 + x + 1) * (9 * x**2 - 3 * x + 1) * (1779 * x**2 - 3450 * x - 881)
    ps = [p0, p1, p2, p3, p4]

    for j, D_expr in [(0, 1 - 4 * x), (1, 1 + 2 * (-1 - w) * x - 3 * w * x**2)]:
        Dp = sp.diff(D_expr, x)
        Ns = [sp.Integer(1)]
        for k in range(4):
            Nk = Ns[-1]
            N_next = sp.expand(2 * x * D_expr * sp.diff(Nk, x) - (2 * (k + 1) * D_expr + (2 * k - 1) * x * Dp) * Nk)
            Ns.append(N_next)
        tot = sp.Integer(0)
        for k in range(5):
            tot += ps[k] * Ns[k] * (2 * x * D_expr) ** (4 - k)
        tot = sp.expand(tot)
        if j == 0:
            assert tot == 0, "Annihilator check failed for Delta_0"
        else:
            # Reduce modulo w^2 + w + 1
            _, rem = sp.poly(tot, w).div(sp.poly(w**2 + w + 1, w))
            assert rem.is_zero, f"Annihilator check failed for Delta_1: rem={rem}"

    # Also check L(y(x)) == -1/2 * p_0(x) directly on a_vals[0..N_SERIES]
    def poly_c(expr: sp.Expr, cap: int) -> list[int]:
        p = sp.Poly(sp.expand(expr), x)
        arr = [0] * (cap + 1)
        for (pw,), v in p.terms():
            if pw <= cap:
                arr[pw] = int(v)
        return arr

    M_ode = N_SERIES - 4
    y_d = [a_vals[:]]
    for _ in range(4):
        prev = y_d[-1]
        y_d.append([m * prev[m] for m in range(1, len(prev))] + [0])

    lhs_ode = [0] * (M_ode + 1)
    for k in range(5):
        pk_c = poly_c(ps[k], M_ode)
        prod_k = poly_mul_trunc(pk_c, y_d[k], M_ode)
        for m in range(M_ode + 1):
            lhs_ode[m] += prod_k[m]
    rhs_ode = poly_c(sp.expand(-p0 / 2), M_ode)
    assert lhs_ode == rhs_ode, "Direct ODE L(y) = -p0/2 check failed on series coefficients"
    print("[3/4] Step 2 exact polynomial annihilator (Delta_0, Delta_1) and order-4 ODE verified.")

    # 4. Step 3: Extract C_0(n)..C_7(n) from p_0..p_4 and verify Mathar's recurrence for 7 <= n <= 120
    n_sym = sp.Symbol("n")
    C_from_ode = [sp.Integer(0)] * 8
    for k_ord, pk_expr in enumerate(ps):
        pk_poly = sp.Poly(sp.expand(pk_expr), x)
        for (d,), coeff in pk_poly.terms():
            j = d - k_ord
            assert 0 <= j <= 7, f"Out-of-range shift j={j} in p_{k_ord}"
            falling = sp.Integer(1)
            m_sym = n_sym - j
            for i in range(k_ord):
                falling *= (m_sym - i)
            C_from_ode[j] += int(coeff) * falling

    C_mathar = [
        n_sym * (881 * n_sym - 4580) * (n_sym - 2) * (n_sym + 1),
        -3 * n_sym * (612 * n_sym**3 - 2827 * n_sym**2 - 2988 * n_sym + 10135),
        3 * (-3088 * n_sym**4 + 42803 * n_sym**3 - 190361 * n_sym**2 + 313702 * n_sym - 167988),
        43042 * n_sym**4 - 600920 * n_sym**3 + 2924411 * n_sym**2 - 5860777 * n_sym + 4115562,
        3 * (-38600 * n_sym**4 + 558681 * n_sym**3 - 2904370 * n_sym**2 + 6389913 * n_sym - 4965528),
        3 * (-14776 * n_sym**4 + 162695 * n_sym**3 - 434711 * n_sym**2 - 415064 * n_sym + 1878084),
        -9 * (n_sym - 6) * (10835 * n_sym**3 - 106831 * n_sym**2 + 290611 * n_sym - 173519),
        54 * (n_sym - 6) * (n_sym - 7) * (593 * n_sym - 1429) * (2 * n_sym - 13),
    ]
    for j in range(8):
        assert sp.expand(C_from_ode[j] - C_mathar[j]) == 0, f"C_{j}(n) mismatch"

    N_REC = 120
    a_ext = [a_barry(n) for n in range(N_REC + 1)]
    for n in range(7, N_REC + 1):
        s = sum(int(C_mathar[j].subs(n_sym, n)) * a_ext[n - j] for j in range(8))
        assert s == 0, f"Mathar recurrence failed at n={n}"
    print(f"[4/4] Step 3 symbolic Z[n] coefficient match and recurrence verified for 7 <= n <= {N_REC}.")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
