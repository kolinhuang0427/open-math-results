#!/usr/bin/env python3
"""Exact-arithmetic verification for OEIS A187430 Irwin (2017) conjecture."""

import math


def bivar_add(A, B, sign=1):
    res = {}
    for k, v in A.items():
        res[k] = res.get(k, 0) + v
    for k, v in B.items():
        res[k] = res.get(k, 0) + sign * v
    return {k: v for k, v in res.items() if v != 0}


def bivar_mul(A, B):
    res = {}
    for (i1, j1), v1 in A.items():
        for (i2, j2), v2 in B.items():
            key = (i1 + i2, j1 + j2)
            res[key] = res.get(key, 0) + v1 * v2
    return {k: v for k, v in res.items() if v != 0}


def bivar_pow(A, e):
    res = {(0, 0): 1}
    base = dict(A)
    while e > 0:
        if e & 1:
            res = bivar_mul(res, base)
        e >>= 1
        if e:
            base = bivar_mul(base, base)
    return res


def series_mul(A, B, deg):
    res = [0] * (deg + 1)
    for i, a in enumerate(A[: deg + 1]):
        if a:
            for j in range(min(len(B), deg + 1 - i)):
                res[i + j] += a * B[j]
    return res


def series_pow(A, e, deg):
    res = [0] * (deg + 1)
    res[0] = 1
    base = list(A[: deg + 1]) + [0] * max(0, deg + 1 - len(A))
    while e > 0:
        if e & 1:
            res = series_mul(res, base, deg)
        e >>= 1
        if e:
            base = series_mul(base, base, deg)
    return res


def main():
    # 1. Exact bivariate kernel factorization in Z[y, u] (Step 2):
    # (1-y)^2 (1-y+y^2)^2 u^2 - y(1-y)^4 (u^4+u^3+u+1)
    #   == ((1-y) u^2 - y u - y(1-y)) * (1-y)^2 * (-y(1-y) u^2 - y u + (1-y))
    one = {(0, 0): 1}
    y = {(1, 0): 1}
    u = {(0, 1): 1}
    one_m_y = bivar_add(one, y, sign=-1)
    q_y = bivar_add(bivar_add(one, y, sign=-1), bivar_pow(y, 2))
    u_sum = bivar_add(bivar_add(bivar_pow(u, 4), bivar_pow(u, 3)), bivar_add(u, one))

    lhs_biv = bivar_add(
        bivar_mul(bivar_mul(bivar_pow(one_m_y, 2), bivar_pow(q_y, 2)), bivar_pow(u, 2)),
        bivar_mul(bivar_mul(y, bivar_pow(one_m_y, 4)), u_sum),
        sign=-1,
    )
    m_cl = bivar_add(
        bivar_mul(one_m_y, bivar_pow(u, 2)),
        bivar_add(bivar_mul(y, u), bivar_mul(y, one_m_y)),
        sign=-1,
    )
    q_cl = bivar_add(
        bivar_add(one_m_y, bivar_mul(y, u), sign=-1),
        bivar_mul(bivar_mul(y, one_m_y), bivar_pow(u, 2)),
        sign=-1,
    )
    rhs_biv = bivar_mul(m_cl, bivar_mul(bivar_pow(one_m_y, 2), q_cl))
    assert bivar_add(lhs_biv, rhs_biv, sign=-1) == {}, "Kernel factorization failed"

    # 2. Exact Catalan-to-u(x) polynomial identity in Z[x, C] modulo (x*C^2 - C + 1) (Step 3):
    # (1-x)^2 (1-C) C^2 + x (C^2 - C + 1)^2 == (-x^2*C^2 + x*C^2 - x*C + x + C^2) * (x*C^2 - C + 1) ?
    # Compute remainder modulo (x*C^2 - C + 1) in Z[C][x] by replacing x*C^2 -> C - 1!
    # Or directly check in Z[x, C] by dividing out (x*C^2 - C + 1) as a linear poly in x? No, deg_x is 2!
    # Here (x, C) stored as (deg_x, deg_C). Eliminate x*C^2 -> C - 1? Better: check in Z[C, x] where we reduce deg_x via C^2*x = C-1?
    # Even simpler: check directly on exact Catalan series AND explicitly verify the polynomial quotient:
    # (1-x)^2*(1-C)*C^2 + x*(C^2-C+1)^2 == (x*C^2 - C + 1) * (-C^2*x + C^2*... wait let us divide in Z[C][x]!)
    # Expressing P(x, C) = p0(C) + p1(C)*x + p2(C)*x^2:
    # P = (1 - 2x + x^2)*(C^2 - C^3) + x*(C^2 - C + 1)^2
    #   = (C^2 - C^3) + x*((C^2 - C + 1)^2 - 2*(C^2 - C^3)) + x^2*(C^2 - C^3).
    # Note C^2 * P_coeff: multiply by C^4 to reduce x^2*C^4 = (C-1)^2 and x*C^2 = C-1!
    # Even cleaner: divide C^2 * P(x, C) by (x*C^2 - (C - 1)) in Z[C][x] cleanly:
    x_v = {(1, 0): 1}
    c_v = {(0, 1): 1}
    one_m_x = bivar_add(one, x_v, sign=-1)
    one_m_c = bivar_add(one, c_v, sign=-1)
    c2mc1 = bivar_add(bivar_add(bivar_pow(c_v, 2), c_v, sign=-1), one)
    p_xc = bivar_add(
        bivar_mul(bivar_pow(one_m_x, 2), bivar_mul(one_m_c, bivar_pow(c_v, 2))),
        bivar_mul(x_v, bivar_pow(c2mc1, 2)),
    )
    # In Z[x, C], (x*C^2 - C + 1) divides p_xc? Let's verify quotient in Z[x, C] directly!
    #Wait: p_xc = (x*C^2 - C + 1) * Q(x, C) iff Q exists in Z[x, C]? Let's test if C^2 divides p0, etc.:
    # p0(C) = (1-C)*C^2 = -(C-1)*C^2. So Q(0, C) = -C^2!
    # p2(C) = (1-C)*C^2. So Q_2 * C^2 = (1-C)*C^2 => Q_2 = 1-C!
    # Wait: P = (x*C^2 - C + 1) * (-C^2 + (1-C)*x + ...)? Let us check Q = -C^2 + (1-C)*x:
    # (-C^2 + (1-C)*x)*(x*C^2 - C + 1) = (1-C)*C^2 * x^2 + (-C^4 + (1-C)*(1-C)) * x + C^2*(C-1)!
    # Check x-coeff of P: (C^2-C+1)^2 - 2*(C^2-C^3) = C^4 - 2C^3 + 3C^2 - 2C + 1 - 2C^2 + 2C^3 = C^4 + C^2 - 2C + 1!
    # Wait: (-C^4 + (1-C)^2) = -C^4 + C^2 - 2C + 1 != C^4 + C^2 - 2C + 1 unless we check C^4 term!
    # Oh! Multiply (1-x)^2*(1-C)*C^2 + x*(C^2-C+1)^2 -> wait: why was C^4 coeff +1? Because +x*(C^2-C+1)^2 has +C^4*x, which uses +C^2*(x*C^2) = +C^2*(C-1) + ...!
    # Wait: Q = C^2 - 2*C^2? No, Q = (x*C^2 - C + 1) * ... wait: (x*C^2 - C + 1) * (x*(1-C) + C^2) has C^4*x, const term -C^2*(C-1) != +C^2*(C-1)!
    # In Z[x, C], (1-x)^2*(1-C)*C^2 + x*(C^2-C+1)^2 = (x*C^2 - C + 1)*(C^2*x + C^2 - 2*C*x + x)??
    # Check with symp-free explicit quotient: (x*C^2 - C + 1)*(x*(1-C) + C^2) vs (x*C^2 - C + 1)*(x*(1-C) - C^2 + 2*x*C^2?):
    # Actually: P mod (x*C^2 - C + 1) in Z[C][x] is 0 iff C^4*P(x=(C-1)/C^2) == 0, AND because deg_x(P)=2:
    # C^2 * P = (x*C^2 - C + 1) * ((1-C)*C^2*x + (C^4 - C^2 + 2*C - 1 + ...)) — wait check exact quotient of C^2*P by (x*C^2 - (C-1)):
    # At x^2: C^4*(1-C)*x^2 -> quotient term C^2*(1-C)*x, remainder (C-1)*C^2*(1-C)*x = -C^2*(C-1)^2*x.
    # Total x coeff: C^2*(C^4 + C^2 - 2C + 1) - C^2*(C^2 - 2C + 1) = C^6!
    # Quotient term C^4, remainder C^4*(C-1) = C^5 - C^4? Wait: C^2 * p0 = C^4*(1-C) = -C^5 + C^4! Sums to ZERO!
    # So C^2 * P == (x*C^2 - C + 1) * (C^2*(1-C)*x + C^4), i.e. P == (x*C^2 - C + 1) * ((1-C)*x + C^2) ?? No, sign! Wait:
    # Let's check ((1-C)*x + C^2) * (x*C^2 - C + 1)? No, (C^2*(1-C)*x + C^4) = C^2 * ((1-C)*x + C^2) had +C^4(1-C) wrong sign!
    # Wait: p0 = C^2*(1-C) = -C^3 + C^2, so C^2*p0 = -C^5 + C^4 = -C^4*(C-1) = +(C^4)*(-(C-1))! YES! Wait: check (x*C^2 - C + 1)*(C^2*(1-C)*x + C^4):
    # x^2 coeff: C^4*(1-C).
    # x^1 coeff: -(C-1)*C^2*(1-C) + C^6 = C^2*(C-1)^2 + C^6 = C^6 + C^4 - 2C^3 + C^2 != C^2*(C^4 + C^2 - 2C + 1)!
    # Aha! C^2*(1-C)^2 has +C^4 - 2C^3 + C^2, whereas C^2*(C^4+C^2-2C+1) = C^6 + C^4 - 2C^3 + C^2! THEY ARE EQUAL!!
    # So P(x, C) == (x*C^2 - C + 1) * (C^2 + (1-C)*x) ? Wait: no, we divided by C^2! Check (C^2 + (1-C)*x)*(x*C^2 - C + 1):
    # const: C^2*(1-C), x^2: C^2*(1-C), x^1: C^4 + (1-C)^2 = C^4 + C^2 - 2C + 1!!
    # BINGO!! P(x, C) == (x*C^2 - C + 1) * (C^2 + (1-C)*x) IDENTICALLY IN Z[x, C]!
    q_xc = bivar_add(bivar_pow(c_v, 2), bivar_mul(one_m_c, x_v))
    prod_xc = bivar_mul(
        bivar_add(bivar_mul(x_v, bivar_pow(c_v, 2)), bivar_add(one, c_v, sign=-1)),
        q_xc,
    )
    assert bivar_add(p_xc, prod_xc, sign=-1) == {}, "Catalan u(x) identity failed"

    # 3. Compute a(0..N) directly from the primary nonnegative walk definition:
    N = 30
    dp = {0: 1}
    a = [1]
    for _ in range(1, N + 1):
        ndp = {}
        for h, cnt in dp.items():
            for step in (-2, -1, 1, 2):
                nh = h + step
                if nh >= 0:
                    ndp[nh] = ndp.get(nh, 0) + cnt
        dp = ndp
        a.append(dp.get(0, 0))

    oeis_data = [
        1, 0, 2, 2, 11, 24, 93, 272, 971, 3194, 11293, 39148, 139687,
        497756, 1798002, 6517194, 23807731, 87336870, 322082967,
        1192381270, 4431889344, 16527495396, 61831374003, 231973133544,
        872598922407, 3290312724374, 12434632908623, 47089829065940,
        178672856753641,
    ]
    assert a[: len(oeis_data)] == oeis_data, "OEIS DATA mismatch"

    # 4. Verify y(t) = t * A(t) satisfies t*(1 - y + y^2)^2 == y*(1 - y)^2 mod t^(N+1):
    deg_t = N
    y_ser = [0] + a[:deg_t]
    one_m_y_ser = [1] + [-c for c in y_ser[1:]]
    y2_ser = series_pow(y_ser, 2, deg_t)
    q_ser = [one_m_y_ser[i] + y2_ser[i] for i in range(deg_t + 1)]
    lhs_t = [0] + series_pow(q_ser, 2, deg_t)[:deg_t]  # t * (1 - y + y^2)^2
    rhs_t = series_mul(y_ser, series_pow(one_m_y_ser, 2, deg_t), deg_t)
    assert lhs_t == rhs_t, "Functional equation for y(t) = t*A(t) failed"

    # 5. Direct exact-integer series check of Irwin's identity up to x^N:
    # C_n = sum_{k=0}^{n-1} C_k C_{n-1-k}
    cat = [1]
    for n in range(1, N + 1):
        cat.append(sum(cat[k] * cat[n - 1 - k] for k in range(n)))
    assert cat[5] == 42 and cat[10] == 16796

    irwin = [0] * (N + 1)
    irwin[0] = 1
    for n in range(N):
        sign = 1 if (n % 2 == 0) else -1
        coeff_base = a[n] * sign
        for k in range(N - n):
            # [x^(n+1+k)] (-1)^n a(n) x^(n+1) / (1-x)^(2n+2)
            irwin[n + 1 + k] += coeff_base * math.comb(2 * n + 1 + k, k)
    assert irwin == cat, "Irwin identity mismatch"

    print("PASS")


if __name__ == "__main__":
    main()
