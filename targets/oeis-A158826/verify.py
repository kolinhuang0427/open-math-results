#!/usr/bin/env python3
"""Exact integer polynomial verifier for OEIS A158826 Mathar recurrence proof."""

import math
import sys


def poly_add(p, q):
    n = max(len(p), len(q))
    res = [0] * n
    for i, v in enumerate(p):
        res[i] += v
    for i, v in enumerate(q):
        res[i] += v
    while res and res[-1] == 0:
        res.pop()
    return res


def poly_mul(p, q):
    if not p or not q:
        return []
    res = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a == 0:
            continue
        for j, b in enumerate(q):
            res[i + j] += a * b
    while res and res[-1] == 0:
        res.pop()
    return res


def poly_pow(p, e):
    res = [1]
    base = p
    while e > 0:
        if e & 1:
            res = poly_mul(res, base)
        e >>= 1
        if e:
            base = poly_mul(base, base)
    return res


def poly_diff(p):
    return [i * p[i] for i in range(1, len(p))]


def poly_compose(outer, inner):
    """Evaluate outer(inner(y)) in Z[y]."""
    res = []
    for c in reversed(outer):
        res = poly_mul(res, inner)
        if c != 0:
            res = poly_add(res, [c])
    return res


def series_comp(A, B, deg):
    """Compose power series A(B(x)) mod x^(deg+1) with B[0] == 0."""
    res = [0] * (deg + 1)
    Bpow = [0] * (deg + 1)
    Bpow[0] = 1
    for k in range(1, min(len(A), deg + 1)):
        nxt = [0] * (deg + 1)
        for i in range(deg + 1):
            if Bpow[i] == 0:
                continue
            for j in range(1, min(len(B), deg + 1 - i)):
                nxt[i + j] += Bpow[i] * B[j]
        Bpow = nxt
        ak = A[k]
        if ak:
            for i in range(deg + 1):
                res[i] += ak * Bpow[i]
    return res


def main():
    # 1. Verify P3(y) = F(F(F(y))) where F(t) = t*(1 - t) = [0, 1, -1]
    F = [0, 1, -1]
    P2 = poly_compose(F, F)
    P3 = poly_compose(F, P2)
    expected_P3 = [0, 1, -3, 6, -9, 10, -8, 4, -1]
    if P3 != expected_P3:
        print("FAIL: P3 mismatch")
        sys.exit(1)

    # 2. Verify univariate polynomial identity U(y) == 0 in Z[y]
    P3_1 = poly_diff(P3)
    P3_2 = poly_diff(P3_1)
    P3_3 = poly_diff(P3_2)

    # N3 = 3*P3_2^2 - P3_1*P3_3
    N3 = poly_add(
        poly_mul([3], poly_mul(P3_2, P3_2)),
        poly_mul([-1], poly_mul(P3_1, P3_3)),
    )
    # N4 = N3'*P3_1 - 5*N3*P3_2
    N4 = poly_add(
        poly_mul(poly_diff(N3), P3_1),
        poly_mul([-5], poly_mul(N3, P3_2)),
    )

    c0 = [-29 * 120, 16 * 120]
    c1 = [29 * 240, -16 * 240]
    c2 = [24 * 18577, -24 * 101872, 24 * 96256]
    c3 = [-24 * 14637, 24 * 156290, -24 * 503584, 24 * 446464]
    c4 = poly_mul([-4, 16], [-10521, 127080, -460672, 458752])
    c5 = poly_mul(
        poly_pow([-1, 4], 2),
        poly_mul([-9, 16], poly_mul([-3, 16], [-39, 256])),
    )

    c0_y = poly_compose(c0, P3)
    c1_y = poly_compose(c1, P3)
    c2_y = poly_compose(c2, P3)
    c3_y = poly_compose(c3, P3)
    c4_y = poly_compose(c4, P3)
    c5_y = poly_compose(c5, P3)

    P3_1_2 = poly_pow(P3_1, 2)
    P3_1_4 = poly_pow(P3_1, 4)
    P3_1_6 = poly_pow(P3_1, 6)
    P3_1_7 = poly_pow(P3_1, 7)

    U = []
    U = poly_add(U, poly_mul(c0_y, P3_1_7))
    U = poly_add(U, poly_mul(c1_y, poly_mul([0, 1], P3_1_7)))
    U = poly_add(U, poly_mul(c2_y, P3_1_6))
    U = poly_add(U, poly_mul(c3_y, poly_mul([-1], poly_mul(P3_2, P3_1_4))))
    U = poly_add(U, poly_mul(c4_y, poly_mul(N3, P3_1_2)))
    U = poly_add(U, poly_mul(c5_y, N4))

    if U != []:
        print("FAIL: U(y) != 0, degree =", len(U) - 1)
        sys.exit(1)

    # 3. Verify [x^(n-4)] extraction from -(c1*y + c2*y' + c3*y'' + c4*y''' + c5*y'''')
    # matches Mathar's degree-4 recurrence polynomials at 6 points n = 10..15
    cs = [c1, c2, c3, c4, c5]

    def extracted_coeffs(n):
        res = [0] * 6
        for d, cpoly in enumerate(cs, 1):
            deriv_ord = d - 1
            for r, coef in enumerate(cpoly):
                if coef == 0:
                    continue
                j = r + 4 - deriv_ord
                ff = 1
                for s in range(1, deriv_ord + 1):
                    ff *= (n - 4 - r + s)
                res[j] -= coef * ff
        return res

    def mathar_coeffs(n):
        return [
            1053 * n * (n - 1) * (n - 2) * (n - 3),
            -36 * (n - 1) * (n - 2) * (n - 3) * (634 * n - 1367),
            24 * (n - 2) * (n - 3) * (7966 * n**2 - 43500 * n + 61181),
            -8 * (n - 3) * (96128 * n**3 - 957424 * n**2 + 3221878 * n - 3665189),
            16 * (91904 * n**4 - 1446528 * n**3 + 8575792 * n**2 - 22703688 * n + 22652013),
            -256 * (8 * n - 35) * (8 * n - 41) * (8 * n - 39) * (8 * n - 37),
        ]

    for n in range(10, 16):
        if extracted_coeffs(n) != mathar_coeffs(n):
            print(f"FAIL: recurrence polynomial mismatch at n={n}")
            sys.exit(1)

    # 4. Compute a(n) from f(f(f(x))), check P3(y) == x mod x^(N+1), check OEIS DATA & recurrence
    N = 60
    f = [0] + [math.comb(2 * m, m) // (m + 1) for m in range(N)]
    f2 = series_comp(f, f, N)
    y = series_comp(f, f2, N)

    expected_data = [
        0, 1, 3, 12, 54, 260, 1310, 6824, 36478, 199094, 1105478, 6227712,
        35520498, 204773400, 1191572004, 6990859416, 41313818217,
        245735825082, 1470125583756, 8840948601024, 53417237877396,
        324123222435804, 1974317194619712,
    ]
    if y[:len(expected_data)] != expected_data:
        print("FAIL: OEIS A158826 DATA mismatch")
        sys.exit(1)

    # Check P3(y(x)) == x mod x^(N+1)
    P3_val = [0] * (N + 1)
    ypow = [0] * (N + 1)
    ypow[0] = 1
    for deg_y, coef in enumerate(P3):
        if deg_y > 0:
            nxt = [0] * (N + 1)
            for i in range(N + 1):
                if ypow[i] == 0:
                    continue
                for j in range(1, N + 1 - i):
                    nxt[i + j] += ypow[i] * y[j]
            ypow = nxt
        if coef:
            for i in range(N + 1):
                P3_val[i] += coef * ypow[i]
    if P3_val[1] != 1 or any(P3_val[k] != 0 for k in range(N + 1) if k != 1):
        print("FAIL: P3(y(x)) != x")
        sys.exit(1)

    for n in range(6, N + 1):
        mc = mathar_coeffs(n)
        lhs = sum(mc[j] * y[n - j] for j in range(6))
        if lhs != 0:
            print(f"FAIL: Mathar recurrence failed at n={n}: lhs={lhs}")
            sys.exit(1)

    print("PASS")


if __name__ == "__main__":
    main()
