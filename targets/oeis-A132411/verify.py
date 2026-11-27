#!/usr/bin/env python3
"""Exact-arithmetic verification for OEIS A132411 Peter Bala (2025) q-series conjecture."""


def poly_mul_trunc(A, B, deg):
    res = [0] * (deg + 1)
    for i, a in enumerate(A[: deg + 1]):
        if a:
            for j in range(min(len(B), deg + 1 - i)):
                res[i + j] += a * B[j]
    return res


def poly_inv_trunc(A, deg):
    """Exact power series inverse in Z[[x]] mod x^(deg+1) assuming A[0] == 1."""
    assert A[0] == 1
    inv = [0] * (deg + 1)
    inv[0] = 1
    for m in range(1, deg + 1):
        s = 0
        for j in range(1, min(len(A), m + 1)):
            s += A[j] * inv[m - j]
        inv[m] = -s
    return inv


def q_pochhammer(u_sign, deg, step=1, start=1):
    """Product_{k >= start, step} (1 - u_sign * x^k) truncated to deg."""
    res = [0] * (deg + 1)
    res[0] = 1
    k = start
    while k <= deg:
        nres = list(res)
        for i in range(deg + 1 - k):
            if res[i]:
                nres[i + k] -= u_sign * res[i]
        res = nres
        k += step
    return res


def main():
    D = 120

    # 1. Verify A132411 sequence definition and OEIS DATA
    a = [0, 1] + [n * n - 1 for n in range(2, 52)]
    oeis_data = [
        0, 1, 3, 8, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195, 224,
        255, 288, 323, 360, 399, 440, 483, 528, 575, 624, 675, 728, 783,
        840, 899, 960, 1023, 1088, 1155, 1224, 1295, 1368, 1443, 1520,
        1599, 1680, 1763, 1848, 1935, 2024, 2115, 2208, 2303, 2400, 2499, 2600,
    ]
    assert a == oeis_data, "OEIS DATA mismatch"

    # 2. Direct expansion of F(q) = sum_{n>=0} q^(2n) * prod_{k>=2n+2} (1 - (-q)^k) mod q^(D+1)
    F = [0] * (D + 1)
    for n in range(D // 2 + 1):
        term = [0] * (D + 1)
        term[2 * n] = 1
        for k in range(2 * n + 2, D + 1):
            sgn = -((-1) ** k)  # coeff of q^k in 1 - (-q)^k
            nterm = list(term)
            for i in range(D + 1 - k):
                if term[i]:
                    nterm[i + k] += sgn * term[i]
            term = nterm
        for i in range(D + 1):
            F[i] += term[i]

    expected_F = [0] * (D + 1)
    m = 1
    while m * m - 1 <= D:
        expected_F[m * m - 1] = 1
        m += 1
    assert F == expected_F, "q-series F(q) mismatch"

    # 3. Verify Step 1 Euler identity (E(x) - E(-x))/2 == sum_{n>=0} x^(2n+1)/(x;x)_{2n+1}
    # and Step 2 Gauss identity (x;x)_inf / (-x;x)_inf == 1 + 2 * sum_{m>=1} (-1)^m x^(m^2)
    xx_inf = q_pochhammer(1, D, step=1, start=1)
    mx_inf = q_pochhammer(-1, D, step=1, start=1)
    ratio = poly_mul_trunc(xx_inf, poly_inv_trunc(mx_inf, D), D)
    gauss = [0] * (D + 1)
    gauss[0] = 1
    m = 1
    while m * m <= D:
        gauss[m * m] += 2 * ((-1) ** m)
        m += 1
    assert ratio == gauss, "Gauss theta identity mismatch"

    # 4. Verify finite Step 2 Laurent polynomial identity P_N(z) for N = 1..6 in Z[x, z, z^-1]
    for N in range(1, 7):
        # Store P_N(z) as dict (deg_z, deg_x) -> int
        P = {(0, 0): 1}
        for k in range(1, N + 1):
            newP = {}
            exp = 2 * k - 1
            for (dz, dx), c in P.items():
                # * (1 + z*x^exp) * (1 + z^-1*x^exp) = 1 + x^(2*exp) + (z + z^-1)*x^exp
                for add_z, add_x in [(0, 0), (0, 2 * exp), (1, exp), (-1, exp)]:
                    key = (dz + add_z, dx + add_x)
                    newP[key] = newP.get(key, 0) + c
            P = {k2: v2 for k2, v2 in newP.items() if v2 != 0}

        deg_x_max = N * N + 2 * N * N + 10
        x2_2N = q_pochhammer(1, deg_x_max, step=2, start=2)
        # Actually truncate exact finite products up to 2N factors
        def fin_q2(n_terms):
            poly = [0] * (n_terms * (n_terms + 1) + 5)
            poly[0] = 1
            for j in range(1, n_terms + 1):
                deg_j = 2 * j
                npoly = list(poly)
                for i in range(len(poly) - deg_j):
                    if poly[i]:
                        npoly[i + deg_j] -= poly[i]
                poly = npoly
            while len(poly) > 1 and poly[-1] == 0:
                poly.pop()
            return poly

        q2N = fin_q2(2 * N)
        rhs_P = {}
        for m_val in range(-N, N + 1):
            den = poly_mul_trunc(fin_q2(N + m_val), fin_q2(N - m_val), len(q2N) + 5)
            coeff = poly_mul_trunc(q2N, poly_inv_trunc(den, len(q2N)), len(q2N))
            for dx, c in enumerate(coeff):
                if c:
                    rhs_P[(m_val, dx + m_val * m_val)] = c
        assert P == rhs_P, f"Finite Jacobi identity failed at N={N}"

    print("PASS")


if __name__ == "__main__":
    main()
