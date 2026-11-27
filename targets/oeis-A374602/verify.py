#!/usr/bin/env python3
"""Zero-float exact verification script for OEIS A374602, A377290, and A377291."""

from math import isqrt


def is_square(n: int) -> bool:
    r = isqrt(n)
    return r * r == n


def a000037(n: int) -> int:
    """n-th nonsquare positive integer (n >= 1): d = n + floor(sqrt(n) + 1/2)."""
    # floor(sqrt(n) + 1/2) == m iff (2m - 1)^2 < 4n < (2m + 1)^2, i.e. m^2 - m < n <= m^2 + m.
    m = isqrt(n)
    if n > m * m + m:
        m += 1
    return n + m


def sqrt_mod_all(d: int, m: int):
    """Exact pure-integer enumeration of all r in [0, m-1] with r^2 == d (mod m)."""
    target = d % m
    return [r for r in range(m) if (r * r) % m == target]


def pell_z_sqrt_d(d: int):
    """Fundamental solution (u1, v1) > 0 to u^2 - d*v^2 = 1 via CF of sqrt(d)."""
    a0 = isqrt(d)
    m, q, a = 0, 1, a0
    p_prev, p = 1, a0
    q_prev, q_cur = 0, 1
    while p * p - d * q_cur * q_cur != 1:
        m = q * a - m
        q = (d - m * m) // q
        a = (a0 + m) // q
        p_prev, p = p, a * p + p_prev
        q_prev, q_cur = q_cur, a * q_cur + q_prev
    return p, q_cur


def fundamental_unit_Od(d: int):
    """Smallest norm-+1 unit eps0 = (A1 + B1*sqrt(d))/2 > 1 in O_d."""
    u1, v1 = pell_z_sqrt_d(d)
    if d % 4 != 1:
        return 2 * u1, 2 * v1, u1, v1

    # For d = 1 (mod 4), check CF of (1 + sqrt(d))/2 for smallest A^2 - d*B^2 = 4.
    sd = isqrt(d)
    P, Q = 1, 2
    p0, p1 = 1, (1 + sd) // 2
    q0, q1 = 0, 1
    while True:
        A = 2 * p1 - q1
        B = q1
        if A * A - d * B * B == 4:
            return A, B, u1, v1
        ak = (P + sd) // Q
        P = ak * Q - P
        Q = (d - P * P) // Q
        ak_next = (P + sd) // Q
        p0, p1 = p1, ak_next * p1 + p0
        q0, q1 = q1, ak_next * q1 + q0


def multiplier_gamma(d: int):
    """Compute gamma = (Ar + Br*sqrt(d))/2 and coset count t_coset."""
    A1, B1, u1, v1 = fundamental_unit_Od(d)
    if d % 4 == 1:
        if A1 % d == 2 % d:
            r, Ar, Br = 1, A1, B1
        else:
            r, Ar, Br = 2, A1 * A1 - 2, A1 * B1
        assert Ar % d == 2 % d
    else:
        if u1 % d == 1:
            r, Ar, Br = 1, 2 * u1, 2 * v1
        else:
            r, Ar, Br = 2, 2 * (2 * u1 * u1 - 1), 2 * (2 * u1 * v1)
        assert (Ar // 2) % d == 1
    assert Ar * Ar - d * Br * Br == 4
    s = 1 if (A1 == 2 * u1 and B1 == 2 * v1) else 3
    t_coset = 6 if (r == 2 and s == 3) else (3 if s == 3 else r)
    return A1, B1, Ar, Br, r, s, t_coset


def pqa_primitive_neg_m(d: int, m: int):
    """Exact PQa algorithm for primitive solutions (G, q) of G^2 - d*q^2 = -m."""
    sd = isqrt(d)
    sols = []
    for r in sqrt_mod_all(d, m):
        r0 = r - m if r > m // 2 else r
        P, Q = r0, m
        p2, p1 = 0, 1
        q2, q1 = 1, 0
        seen_reduced = {}
        while True:
            if Q > 0:
                a = (P + sd) // Q
            else:
                a = -1 - ((P + sd) // (-Q))
            pk = a * p1 + p2
            qk = a * q1 + q2
            P_next = a * Q - P
            Q_next = (d - P_next * P_next) // Q
            Gk = m * pk - r0 * qk
            if Gk * Gk - d * qk * qk == -m:
                if qk >= 0:
                    sols.append((Gk, qk))
                if qk <= 0:
                    sols.append((-Gk, -qk))
            # Reduced check without floats: Q_next > 0, 0 < P_next <= sd,
            # (sd - P_next) < Q_next <= (sd + P_next) -> integer equivalent since sqrt(d) irrational
            if (
                Q_next > 0
                and 0 < P_next <= sd
                and (sd - P_next) < Q_next <= (sd + P_next)
            ):
                st = (P_next, Q_next)
                seen_reduced[st] = seen_reduced.get(st, 0) + 1
                if seen_reduced[st] >= 3:
                    break
            p2, p1 = p1, pk
            q2, q1 = q1, qk
            P, Q = P_next, Q_next
    return sols


def solve_row_exact(d: int):
    """Finite-time exact algorithm computing Ar and sorted W_0 orbit seeds (Y, b, c, X)."""
    A1, B1, Ar, Br, r, s, t_coset = multiplier_gamma(d)

    eps_pows = [(2, 0)]
    Ac, Bc = A1, B1
    for _ in range(t_coset - 1):
        eps_pows.append((Ac, Bc))
        Ac, Bc = (A1 * Ac + d * B1 * Bc) // 2, (B1 * Ac + A1 * Bc) // 2

    valid_M = sorted({c * (d - c) for c in range(1, d)})
    W0 = set()
    for M in valid_M:
        for g in range(1, isqrt(M) + 1):
            if M % (g * g) != 0:
                continue
            m = M // (g * g)
            for Gk, qk in pqa_primitive_neg_m(d, m):
                for sgn in (1, -1):
                    X0, Y0 = sgn * g * Gk, g * qk
                    for Ae, Be in eps_pows:
                        numX = Ae * X0 + d * Be * Y0
                        numY = Be * X0 + Ae * Y0
                        if numX % 2 != 0 or numY % 2 != 0:
                            continue
                        Xc, Yc = numX // 2, numY // 2
                        if Yc <= 0:
                            continue
                        c = Xc % d
                        if c == 0 or (Xc * Xc - d * Yc * Yc) != -c * (d - c):
                            continue
                        # Normalize into W_0 (minimal X >= d+1, Y >= 1 under T_gamma^{\pm 1})
                        xx, yy = Xc, Yc
                        while xx < d + 1:
                            xx, yy = (Ar * xx + d * Br * yy) // 2, (Br * xx + Ar * yy) // 2
                        while True:
                            xp = (Ar * xx - d * Br * yy) // 2
                            yp = (Ar * yy - Br * xx) // 2
                            if xp >= d + 1 and yp >= 1:
                                xx, yy = xp, yp
                            else:
                                break
                        W0.add((yy, xx // d, xx % d, xx))
    return Ar, Br, sorted(W0)


def generate_terms_from_seeds(d: int, Ar: int, Br: int, seeds, periods: int):
    """Generate exact terms for `periods` full periods via T_gamma and check linear recurrence."""
    p = len(seeds)
    # Track each orbit via T_gamma and simultaneously check Y_{m+2} = Ar*Y_{m+1} - Y_m
    rows = []
    cur = list(seeds)
    for m in range(periods):
        rows.append(cur)
        nxt = []
        for Y, b, c, X in cur:
            Xn = (Ar * X + d * Br * Y) // 2
            Yn = (Br * X + Ar * Y) // 2
            assert Xn % d == c and Xn >= d + 1
            assert Yn * Yn == (d - c) * (Xn // d) ** 2 + c * ((Xn // d) + 1) ** 2
            nxt.append((Yn, Xn // d, c, Xn))
        cur = nxt

    for m in range(periods - 2):
        for j in range(p):
            y0, y1, y2 = rows[m][j][0], rows[m + 1][j][0], rows[m + 2][j][0]
            assert y2 == Ar * y1 - y0

    flat = [item for block in rows for item in block]
    # Verify strict global monotonicity of Y across all periods
    for idx in range(len(flat) - 1):
        assert flat[idx][0] < flat[idx + 1][0], f"Non-increasing at d={d}, idx={idx}"
    return flat


def brute_force_row(d: int, count: int):
    """Direct exhaustive enumeration from t = isqrt(d) + 1."""
    res = []
    t = isqrt(d) + 1
    while len(res) < count:
        b = isqrt((t * t) // d)
        num = t * t - d * b * b
        if num % (2 * b + 1) == 0:
            c = num // (2 * b + 1)
            if 1 <= c < d:
                res.append((t, b, c, d * b + c))
        t += 1
    return res


def main():
    # 1. Exact OEIS DATA vectors for A377290(1..67), A377291(1..46), A374602 antidiagonals, and 20 EXAMPLE rows
    oeis_A377290 = [
        1, 2, 2, 6, 4, 4, 14, 10, 8, 10, 6, 8, 14, 16, 34, 10, 8, 34, 8, 12,
        22, 22, 32, 18, 18, 30, 14, 18, 16, 12, 38, 22, 28, 26, 42, 20, 74, 36,
        14, 54, 12, 16, 34, 38, 54, 26, 58, 50, 24, 36, 102, 46, 32, 78, 14,
        22, 38, 46, 118, 22, 30, 68, 36, 32, 130, 74, 34,
    ]
    oeis_A377291 = [
        6, 14, 7, 98, 16, 34, 1442, 398, 194, 119, 30, 62, 4354, 1154, 115598,
        322, 23, 155234, 48, 98, 10402, 2702, 64514, 727, 482, 3040, 1154,
        2114, 70, 142, 21314, 5474, 2498, 1442, 16793602, 674, 48497294,
        158402, 47, 48670, 96, 194, 39202, 9998, 1684802, 2599,
    ]
    oeis_A374602_examples = {
        1: [5, 29, 169, 985, 5741, 33461, 195025, 1136689, 6625109],
        2: [3, 11, 41, 153, 571, 2131, 7953, 29681, 110771],
        3: [5, 13, 34, 89, 233, 610, 1597, 4181, 10946],
        4: [3, 7, 18, 29, 69, 178, 287, 683, 1762],
        5: [4, 5, 11, 28, 62, 79, 175, 446, 988],
        6: [10, 11, 23, 58, 338, 373, 781, 1970, 11482],
        7: [4, 5, 13, 14, 25, 62, 111, 148, 185],
        8: [7, 8, 13, 32, 57, 139, 158, 259, 638],
        9: [6, 22, 39, 69, 82, 125, 306, 543, 1142],
        10: [4, 5, 7, 17, 30, 43, 53, 76, 185],
        11: [9, 11, 14, 19, 46, 81, 267, 329, 418],
        12: [6, 10, 21, 23, 30, 39, 94, 165, 362],
        13: [25, 27, 34, 41, 98, 171, 260, 1649, 1779],
        14: [6, 13, 15, 18, 21, 50, 87, 132, 198],
        15: [5, 7, 8, 9, 11, 31, 34, 37, 56],
        16: [10, 26, 68, 125, 159, 178, 197, 466, 807],
        17: [6, 9, 12, 13, 14, 33, 57, 86, 134],
        18: [5, 7, 8, 17, 18, 19, 31, 64, 77],
        19: [16, 19, 27, 28, 29, 68, 117, 176, 764],
        20: [6, 9, 11, 14, 36, 39, 57, 58, 59],
    }
    oeis_A374602_antidiags = [
        5, 29, 3, 169, 11, 5, 985, 41, 13, 3, 5741, 153, 34, 7, 4, 33461, 571,
        89, 18, 5, 10, 195025, 2131, 233, 29, 11, 11, 4, 1136689, 7953, 610,
        69, 28, 23, 5, 7, 6625109, 29681, 1597, 178, 62, 58, 13, 8, 6,
        38613965, 110771, 4181, 287, 79, 338, 14, 13, 22, 4,
    ]

    # 2. Verify algorithm on n = 1..67 against A377290, A377291, linear recurrence, and c-periodicity
    row_cache = {}
    for n in range(1, len(oeis_A377290) + 1):
        d = a000037(n)
        assert not is_square(d)
        Ar, Br, seeds = solve_row_exact(d)
        p = len(seeds)
        assert p == oeis_A377290[n - 1], f"p mismatch at n={n}: {p} vs {oeis_A377290[n-1]}"
        if n <= len(oeis_A377291):
            assert Ar == oeis_A377291[n - 1], f"Ar mismatch at n={n}: {Ar} vs {oeis_A377291[n-1]}"
        flat = generate_terms_from_seeds(d, Ar, Br, seeds, periods=max(4, (12 + p - 1) // p))
        # Check exact c-periodicity from k=1 across all 4 periods
        cs = [x[2] for x in flat]
        assert cs[:p] == cs[p:2 * p] == cs[2 * p:3 * p] == cs[3 * p:4 * p]
        row_cache[n] = [x[0] for x in flat]

        # Direct brute-force cross-check on early terms (first min(2*p, 18) terms for n <= 20,
        # skipping full 2*p where gamma > 1000 so brute force stays fast while matching all EXAMPLE terms)
        if n <= 20:
            check_len = min(len(flat), 2 * p) if Ar <= 400 else min(len(flat), 12)
            bf = brute_force_row(d, check_len)
            assert flat[:len(bf)] == bf, f"BF mismatch at n={n}, d={d}"

    # 3. Verify all 20 OEIS EXAMPLE rows and all 55 antidiagonal DATA terms
    for n, expected in oeis_A374602_examples.items():
        assert row_cache[n][:len(expected)] == expected, f"EXAMPLE mismatch row {n}"

    anti = []
    for diag in range(1, 11):
        for r_idx in range(1, diag + 1):
            c_idx = diag - r_idx + 1
            anti.append(row_cache[r_idx][c_idx - 1])
    assert anti == oeis_A374602_antidiags

    # 4. Verify non-squarefree d with f >= 5 (d = 75 = 5^2*3, d = 147 = 7^2*3, d = 242 = 11^2*2)
    for d in (75, 147, 242):
        Ar, Br, seeds = solve_row_exact(d)
        flat = generate_terms_from_seeds(d, Ar, Br, seeds, periods=3)
        bf = brute_force_row(d, 15)
        assert flat[:15] == bf, f"Non-squarefree BF mismatch at d={d}"

    print("PASS")


if __name__ == "__main__":
    main()
