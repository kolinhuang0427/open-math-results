#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A108449 (Mathar 2022 D-finite recurrence).

Written directly from live OEIS A108449 (rev. 13) NAME/FORMULA definitions and PROOF.md
without reading verify.py or author notes. Zero floating-point arithmetic.
"""

from __future__ import annotations

import sys
import sympy as sp


OEIS_DATA = [
    1, 0, 4, 32, 252, 2112, 18484, 166976, 1545548, 14583808,
    139774180, 1356966240, 13316740764, 131890671680, 1316627340564,
    13234192747648, 133829733962732, 1360586260341248, 13898403178004420,
    142578916276009632,
]


def count_paths_dp(max_n: int) -> list[int]:
    """Direct exact DP from the OEIS A108449 NAME definition (steps u=(2,1), U=(1,2), d=(1,-1))."""
    # Track primitive paths by up-step count n <= max_n:
    # A path with up-step count n from (0,0) to (3n,0) staying in Y >= 0.
    # For DP by total steps or up-steps: state (n_used, height) where height <= 2*max_n.
    # First count all paths staying strictly Y > 0 except at start/end?
    # Even more direct: DP over step-by-step prefix from (0, 0) using total X+Y = 3*n_used:
    # Wait: d=(1,-1) decreases Y by 1 and increases X by 1 (preserves X+Y = 3*n_used).
    # So we can iterate up-step count? Better: iterate total steps? Max steps <= 3*max_n.
    # To avoid tracking pyramids dynamically in DP, track exact state:
    # Step-by-step DP for primitive paths of up-step count n:
    # Wait: a path has X+Y = 3*n_used. At Y=0, starting a primitive path means either:
    #  - count all paths from (0,0) to (3n,0) in Y>=0 via DP over (x_plus_y_div3, y):
    # Actually, step-by-step over X from 0 to 3*max_n: state is height y (0 <= y <= 2*max_n).
    # For pyramid-free directly from NAME:
    # A pyramid starts on Y=0 and is u^p d^p or U^p d^{2p}.
    # In any path, returns to Y=0 partition it into primitive excursions; an excursion is a pyramid iff
    # it has the form u^p d^p or U^p d^{2p}!
    # So first DP counts primitive excursions of each up-step count n (1 <= n <= max_n) directly
    # by forbidding intermediate Y=0: start with u (y=1, n=1) or U (y=2, n=1), propagate in y >= 1!
    # Wait: to be 100% independent of Step 1's formula K(x) = xA(1+A), propagate (n_up, y) step by step!
    max_steps = 3 * max_n
    # prim[n] = number of primitive excursions with n up-steps
    # DP: cur[(n_up, y)] for y >= 1
    from collections import defaultdict
    cur = defaultdict(int)
    cur[(1, 1)] += 1  # step u
    cur[(1, 2)] += 1  # step U
    prim = [0] * (max_n + 1)
    while cur:
        nxt = defaultdict(int)
        for (nu, y), cnt in cur.items():
            # Step d=(1,-1)
            if y == 1:
                prim[nu] += cnt
            else:
                nxt[(nu, y - 1)] += cnt
            # Step u=(2,1), U=(1,2)
            if nu + 1 <= max_n:
                nxt[(nu + 1, y + 1)] += cnt
                nxt[(nu + 1, y + 2)] += cnt
        cur = nxt

    # Remove the 2 pyramids u^n d^n and U^n d^{2n} for each n >= 1
    prim_free = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        prim_free[n] = prim[n] - 2

    # Concatenate arbitrary sequence of primitive pyramid-free excursions
    a = [0] * (max_n + 1)
    a[0] = 1
    for n in range(1, max_n + 1):
        a[n] = sum(prim_free[k] * a[n - k] for k in range(1, n + 1))
    return a


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
    # 1. Direct lattice-path DP check against live OEIS A108449 data
    dp_vals = count_paths_dp(len(OEIS_DATA) - 1)
    assert dp_vals == OEIS_DATA, f"DP mismatch: {dp_vals} vs {OEIS_DATA}"
    print(f"[1/4] Direct lattice-path DP matches all {len(OEIS_DATA)} live OEIS A108449 terms.")

    # 2. Step 1 & Step 2: OGF and 5x5 Sylvester resultant Res_A(E1, E2) == x^2 * P(x, y)
    N = 45
    # Solve A = 1 + x*A^2 + x*A^3 iteratively mod x^{N+1}
    A = [0] * (N + 1)
    A[0] = 1
    for _ in range(N + 1):
        A2 = poly_mul_trunc(A, A, N)
        A3 = poly_mul_trunc(A2, A, N)
        for m in range(1, N + 1):
            A[m] = A2[m - 1] + A3[m - 1]
    # Verify A = 1 + x A^2 + x A^3
    A2 = poly_mul_trunc(A, A, N)
    A3 = poly_mul_trunc(A2, A, N)
    assert A[0] == 1 and all(A[m] == A2[m - 1] + A3[m - 1] for m in range(1, N + 1))

    # K_free = x A(1+A) - 2x/(1-x)
    A_plus_A2 = [A[m] + A2[m] for m in range(N + 1)]
    K_free = [0] + [A_plus_A2[m - 1] - 2 for m in range(1, N + 1)]
    assert K_free[0] == 0 and K_free[1] == 0
    y_vals = [0] * (N + 1)
    y_vals[0] = 1
    for m in range(1, N + 1):
        y_vals[m] = sum(K_free[k] * y_vals[m - k] for k in range(1, m + 1))
    assert y_vals[: len(OEIS_DATA)] == OEIS_DATA

    # Symbolic resultant Res_A(E1, E2) in Z[x, y]
    x, y, A_sym = sp.symbols("x y A_sym")
    E1 = x * A_sym**3 + x * A_sym**2 - A_sym + 1
    E2 = y * (1 + x - x * (1 - x) * A_sym * (1 + A_sym)) - (1 - x)
    res_expr = sp.expand(sp.resultant(E1, E2, A_sym))
    P_expr = (
        (-1 + 3 * x - 3 * x**2 + x**3)
        + (1 + 3 * x - 9 * x**2 + 5 * x**3) * y
        + (-5 * x - x**2 + 5 * x**3 + x**4) * y**2
        + (-x + 9 * x**2 - 3 * x**3 + 3 * x**4) * y**3
    )
    assert sp.expand(res_expr - x**2 * P_expr) == 0, "Resultant mismatch"
    print("[2/4] Step 1 OGF and Step 2 5x5 Sylvester resultant Res_A(E1,E2) = x^2 P(x,y) verified.")

    # 3. Step 3: Exact Z[x,y] division Q(x,y) = P(x,y)*R(x,y) and ODE on y(x)
    Px = sp.diff(P_expr, x)
    Py = sp.diff(P_expr, y)
    N1 = -Px
    N2 = sp.expand((Py * sp.diff(N1, x) + N1 * sp.diff(N1, y)) * Py - 1 * N1 * (Py * sp.diff(Py, x) + N1 * sp.diff(Py, y)))
    N3 = sp.expand((Py * sp.diff(N2, x) + N1 * sp.diff(N2, y)) * Py - 3 * N2 * (Py * sp.diff(Py, x) + N1 * sp.diff(Py, y)))

    p_inhom = 342 * x**7 + 3006 * x**6 + 4452 * x**5 - 67380 * x**4 + 25086 * x**3 + 168166 * x**2 - 42504 * x
    p0 = 2 * x * (513 * x**6 + 5481 * x**5 + 16074 * x**4 - 252882 * x**3 - 265431 * x**2 - 43423 * x + 21252)
    p1 = 2 * x * (1296 * x**8 + 12681 * x**7 + 27666 * x**6 - 46737 * x**5 + 20532 * x**4 + 373095 * x**3 - 369686 * x**2 + 76017 * x - 3696)
    p2 = x**2 * (x - 1) * (3033 * x**7 + 36747 * x**6 + 74775 * x**5 - 270837 * x**4 + 65427 * x**3 - 72523 * x**2 - 21731 * x + 2773)
    p3 = 2 * x**3 * (x - 1)**2 * (87 * x + 431) * (x**2 + 11 * x - 1) * (3 * x**3 - 3 * x**2 + 9 * x - 1)

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
    def poly_coeffs_list(expr: sp.Expr, deg_cap: int) -> list[int]:
        p = sp.Poly(sp.expand(expr), x)
        arr = [0] * (deg_cap + 1)
        for (pw,), v in p.terms():
            if pw <= deg_cap:
                arr[pw] = int(v)
        return arr

    yp = [m * y_vals[m] for m in range(1, N + 1)] + [0]
    ypp = [m * yp[m] for m in range(1, N + 1)] + [0]
    yppp = [m * ypp[m] for m in range(1, N + 1)] + [0]
    M_ode = N - 3
    pi_c = poly_coeffs_list(p_inhom, M_ode)
    p0_c = poly_coeffs_list(p0, M_ode)
    p1_c = poly_coeffs_list(p1, M_ode)
    p2_c = poly_coeffs_list(p2, M_ode)
    p3_c = poly_coeffs_list(p3, M_ode)
    t0 = poly_mul_trunc(p0_c, y_vals, M_ode)
    t1 = poly_mul_trunc(p1_c, yp, M_ode)
    t2 = poly_mul_trunc(p2_c, ypp, M_ode)
    t3 = poly_mul_trunc(p3_c, yppp, M_ode)
    for m in range(M_ode + 1):
        assert pi_c[m] + t0[m] + t1[m] + t2[m] + t3[m] == 0, f"ODE failed at x^{m}"
    print("[3/4] Step 3 exact Z[x,y] division Q = P*R and order-3 ODE verified.")

    # 4. Step 4: Extract C_0(n)..C_8(n) symbolically from p0..p3 and check recurrence up to n=100
    n_sym = sp.Symbol("n")
    C_from_ode = [sp.Integer(0)] * 9
    for k_ord, pk_expr in enumerate((p0, p1, p2, p3)):
        pk_poly = sp.Poly(sp.expand(pk_expr), x)
        for (d,), coeff in pk_poly.terms():
            j = d - k_ord
            assert 0 <= j <= 8, f"Out-of-range shift j={j} in p_{k_ord}"
            falling = sp.Integer(1)
            m_sym = n_sym - j
            for i in range(k_ord):
                falling *= (m_sym - i)
            C_from_ode[j] += int(coeff) * falling

    C_mathar = [
        n_sym * (2 * n_sym + 1) * (431 * n_sym - 2895),
        2 * (-9395 * n_sym**3 + 68622 * n_sym**2 - 64084 * n_sym + 26109),
        2 * (59288 * n_sym**3 - 508196 * n_sym**2 + 1044822 * n_sym - 574587),
        2 * (-94965 * n_sym**3 + 1070605 * n_sym**2 - 3607435 * n_sym + 3485484),
        4 * (29036 * n_sym**3 - 351474 * n_sym**2 + 1402336 * n_sym - 1970505),
        6 * (-6703 * n_sym**3 + 63052 * n_sym**2 - 99178 * n_sym - 237177),
        6 * (1012 * n_sym**3 - 14914 * n_sym**2 + 74580 * n_sym - 127341),
        6 * (1127 * n_sym**3 - 21429 * n_sym**2 + 135199 * n_sym - 282762),
        9 * (29 * n_sym - 165) * (2 * n_sym - 15) * (n_sym - 8),
    ]
    for j in range(9):
        assert sp.expand(C_from_ode[j] - C_mathar[j]) == 0, f"C_{j}(n) mismatch"

    # Extend y_vals to N_REC = 100 directly from K_free and verify recurrence for 8 <= n <= 100
    N_REC = 100
    A_ext = [0] * (N_REC + 1)
    A_ext[0] = 1
    for _ in range(N_REC + 1):
        A2_e = poly_mul_trunc(A_ext, A_ext, N_REC)
        A3_e = poly_mul_trunc(A2_e, A_ext, N_REC)
        for m in range(1, N_REC + 1):
            A_ext[m] = A2_e[m - 1] + A3_e[m - 1]
    A2_e = poly_mul_trunc(A_ext, A_ext, N_REC)
    K_free_e = [0] + [A_ext[m - 1] + A2_e[m - 1] - 2 for m in range(1, N_REC + 1)]
    y_ext = [0] * (N_REC + 1)
    y_ext[0] = 1
    for m in range(1, N_REC + 1):
        y_ext[m] = sum(K_free_e[k] * y_ext[m - k] for k in range(1, m + 1))

    for n in range(8, N_REC + 1):
        s = sum(int(C_mathar[j].subs(n_sym, n)) * y_ext[n - j] for j in range(9))
        assert s == 0, f"Mathar recurrence failed at n={n}"

    print(f"[4/4] Step 4 symbolic Z[n] coefficient match and recurrence verified for 8 <= n <= {N_REC}.")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
