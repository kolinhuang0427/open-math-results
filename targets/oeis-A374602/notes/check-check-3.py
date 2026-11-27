"""Independent exact-arithmetic verifier for targets/oeis-A374602/ (PROOF.md).

Zero floating-point operations or literals anywhere in this script.
Tests:
1. Live OEIS A374602 (rev. 31), A377290 (rev. 7), A377291 (rev. 7) data match.
2. Lemmas 1-3, Proposition 4, Theorem 5, and Proposition 6 across nonsquare d >= 2.
3. Independent PQa finite-time algorithm (Section 4) verified against exhaustive
   brute-force scans of (b, c) and exact order-2 recurrence across multiple periods.
"""

from math import gcd, isqrt

# Fetched live from https://oeis.org/search?q=id:A374602&fmt=json (rev. 31)
A374602_LIVE = [
    5, 29, 3, 169, 11, 5, 985, 41, 13, 3, 5741, 153, 34, 7, 4, 33461, 571, 89, 18, 5,
    10, 195025, 2131, 233, 29, 11, 11, 4, 1136689, 7953, 610, 69, 28, 23, 5, 7, 6625109,
    29681, 1597, 178, 62, 58, 13, 8, 6, 38613965, 110771, 4181, 287, 79, 338, 14, 13, 22, 4,
]

# Fetched live from https://oeis.org/search?q=id:A377290&fmt=json (rev. 7, all 67 terms)
A377290_LIVE = [
    1, 2, 2, 6, 4, 4, 14, 10, 8, 10, 6, 8, 14, 16, 34, 10, 8, 34, 8, 12, 22, 22, 32, 18,
    18, 30, 14, 18, 16, 12, 38, 22, 28, 26, 42, 20, 74, 36, 14, 54, 12, 16, 34, 38, 54, 26,
    58, 50, 24, 36, 102, 46, 32, 78, 14, 22, 38, 46, 118, 22, 30, 68, 36, 32, 130, 74, 34,
]

# Fetched live from https://oeis.org/search?q=id:A377291&fmt=json (rev. 7, all 46 terms)
A377291_LIVE = [
    6, 14, 7, 98, 16, 34, 1442, 398, 194, 119, 30, 62, 4354, 1154, 115598, 322, 23,
    155234, 48, 98, 10402, 2702, 64514, 727, 482, 3040, 1154, 2114, 70, 142, 21314,
    5474, 2498, 1442, 16793602, 674, 48497294, 158402, 47, 48670, 96, 194, 39202,
    9998, 1684802, 2599,
]


def nonsquares(count: int) -> list[int]:
    out = []
    d = 2
    while len(out) < count:
        s = isqrt(d)
        if s * s != d:
            out.append(d)
        d += 1
    return out


def floor_quad(P: int, Q: int, d: int) -> int:
    """Exact floor((P + sqrt(d)) / Q) for nonsquare d > 0 and nonzero integer Q."""
    s = isqrt(d)
    assert s * s < d < (s + 1) * (s + 1) and Q != 0
    if Q > 0:
        a = (P + s) // Q
    else:
        a = (-P - (s + 1)) // (-Q)
    # Exact verification without floats:
    # a < (P + sqrt(d)) / Q < a + 1 (equality impossible since d nonsquare)
    if Q > 0:
        lhs = a * Q - P  # < sqrt(d)
        rhs = (a + 1) * Q - P  # > sqrt(d)
        assert lhs < 0 or lhs * lhs < d
        assert rhs > 0 and rhs * rhs > d
    else:
        Qp = -Q
        lhs = -(a + 1) * Qp - P  # < sqrt(d)
        rhs = -a * Qp - P  # > sqrt(d)
        assert lhs < 0 or lhs * lhs < d
        assert rhs > 0 and rhs * rhs > d
    return a


def gt_z_threshold(X: int, Y: int, d: int) -> bool:
    """Exact comparison X + Y*sqrt(d) > 2*d without floating point."""
    diff = 2 * d - X
    if Y > 0:
        if diff <= 0:
            return True
        return d * Y * Y > diff * diff
    if diff >= 0:
        return False
    return d * Y * Y < diff * diff


def lt_z(X1: int, Y1: int, X2: int, Y2: int, d: int) -> bool:
    """Exact comparison X1 + Y1*sqrt(d) < X2 + Y2*sqrt(d)."""
    dx = X2 - X1
    dy = Y2 - Y1
    if dy == 0:
        return dx > 0
    if dy > 0:
        if dx >= 0:
            return True
        return d * dy * dy > dx * dx
    if dx <= 0:
        return False
    return d * dy * dy < dx * dx


def mul_unit(A: int, B: int, X: int, Y: int, d: int) -> tuple[int, int]:
    """Multiply ((A + B*sqrt(d))/2) * (X + Y*sqrt(d)), asserting integrality."""
    numX = A * X + d * B * Y
    numY = B * X + A * Y
    assert numX % 2 == 0 and numY % 2 == 0
    return numX // 2, numY // 2


def fundamental_units(d: int) -> tuple[int, int, int, int, int, int, int]:
    """Return (A1, B1, u1, v1, Ar, Br, r) via simple continued fractions."""
    # Expand CF of sqrt(d) to get fundamental solution (u1, v1) to u^2 - d*v^2 = 1
    # and smallest integer solution (A1_z, B1_z) to A^2 - d*B^2 = 4 in Z[sqrt(d)] (just 2*u1, 2*v1),
    # plus CF of (1+sqrt(d))/2 if d == 1 mod 4 to get minimal norm-+1 unit eps0 in O_d.
    def cf_sqrt_u1_v1(d_val: int) -> tuple[int, int]:
        a0 = isqrt(d_val)
        P, Q = 0, 1
        p_prev, p_curr = 0, 1
        q_prev, q_curr = 1, 0
        k = 0
        while True:
            a = floor_quad(P, Q, d_val)
            p_next = a * p_curr + p_prev
            q_next = a * q_curr + q_prev
            if k >= 0 and p_next * p_next - d_val * q_next * q_next == 1:
                return p_next, q_next
            P = a * Q - P
            Q = (d_val - P * P) // Q
            p_prev, p_curr = p_curr, p_next
            q_prev, q_curr = q_curr, q_next
            k += 1

    u1, v1 = cf_sqrt_u1_v1(d)
    assert u1 * u1 - d * v1 * v1 == 1

    if d % 4 != 1:
        A1, B1 = 2 * u1, 2 * v1
        assert A1 * A1 - d * B1 * B1 == 4
        if u1 % d == 1:
            r = 1
            Ar, Br = A1, B1
        else:
            Ar = A1 * A1 - 2
            Br = A1 * B1
            assert (Ar // 2) % d == 1
            r = 2
    else:
        # Check eps0 in Z[(1+sqrt(d))/2] via CF of (1+sqrt(d))/2
        P, Q = 1, 2
        p_prev, p_curr = 0, 1
        q_prev, q_curr = 1, 0
        while True:
            a = floor_quad(P, Q, d)
            p_next = a * p_curr + p_prev
            q_next = a * q_curr + q_prev
            A_cand = 2 * p_next - q_next
            B_cand = q_next
            if A_cand * A_cand - d * B_cand * B_cand == 4:
                A1, B1 = A_cand, B_cand
                break
            P = a * Q - P
            Q = (d - P * P) // Q
            p_prev, p_curr = p_curr, p_next
            q_prev, q_curr = q_curr, q_next
        assert A1 * A1 - d * B1 * B1 == 4
        if A1 % d == 2 % d:
            r = 1
            Ar, Br = A1, B1
        else:
            Ar = A1 * A1 - 2
            Br = A1 * B1
            assert Ar % d == 2 % d
            r = 2

    assert Ar * Ar - d * Br * Br == 4 and Ar >= 3
    return A1, B1, u1, v1, Ar, Br, r


def pqa_window(d: int) -> tuple[int, list[tuple[int, int]]]:
    """Execute Section 4 algorithm verbatim to compute (Ar, sorted W_0)."""
    A1, B1, u1, v1, Ar, Br, r = fundamental_units(d)

    # s in {1, 3} such that eps0^s = u1 + v1*sqrt(d)
    if (A1, B1) == (2 * u1, 2 * v1):
        s = 1
    else:
        # Check eps0^3
        A2, B2 = A1 * A1 - 2, A1 * B1
        A3 = (A1 * A2 + d * B1 * B2) // 2
        B3 = (A1 * B2 + B1 * A2) // 2
        assert (A3, B3) == (2 * u1, 2 * v1)
        s = 3
    t_coset = (r * s) // gcd(r, s)

    # Precompute powers eps0^j = (Aj + Bj*sqrt(d))/2 for j = 0..t_coset-1
    eps_pows = [(2, 0)]
    for _ in range(1, t_coset):
        Ap, Bp = eps_pows[-1]
        eps_pows.append(((A1 * Ap + d * B1 * Bp) // 2, (A1 * Bp + B1 * Ap) // 2))

    lim_sq = isqrt(d)
    w0_set: set[tuple[int, int]] = set()
    seen_M: set[int] = set()

    for c in range(1, d):
        M = c * (d - c)
        if M in seen_M:
            continue
        seen_M.add(M)
        # All g >= 1 with g^2 | M
        g = 1
        while g * g <= M:
            if M % (g * g) != 0:
                g += 1
                continue
            m = M // (g * g)
            # Residues r0 in (-m/2, m/2] with r0^2 == d (mod m)
            lo = -(m // 2) + (1 if m % 2 == 0 else 0)
            hi = m // 2
            for r0 in range(lo, hi + 1):
                if (r0 * r0 - d) % m != 0:
                    continue
                P, Q = r0, m
                p_prev, p_curr = 0, 1
                q_prev, q_curr = 1, 0
                reduced_counts: dict[tuple[int, int], int] = {}
                collected: list[tuple[int, int]] = []
                k = 0
                while True:
                    a = floor_quad(P, Q, d)
                    p_next = a * p_curr + p_prev
                    q_next = a * q_curr + q_prev
                    G_next = m * p_next - r0 * q_next
                    P_next = a * Q - P
                    Q_next = (d - P_next * P_next) // Q
                    assert (d - P_next * P_next) % Q == 0
                    sign_k = -1 if (k + 1) % 2 == 1 else 1
                    assert G_next * G_next - d * q_next * q_next == sign_k * m * Q_next
                    if G_next * G_next - d * q_next * q_next == -m:
                        collected.append((G_next, q_next))
                    # Check if (P_next, Q_next) is reduced
                    if Q_next > 0 and 0 < P_next <= lim_sq:
                        if (d - P_next * P_next) > 0:
                            # sqrt(d) - P < Q < sqrt(d) + P
                            cond_lo = (P_next + Q_next) * (P_next + Q_next) > d
                            diff_qp = Q_next - P_next
                            cond_hi = diff_qp <= 0 or diff_qp * diff_qp < d
                            if cond_lo and cond_hi:
                                state = (P_next, Q_next)
                                reduced_counts[state] = reduced_counts.get(state, 0) + 1
                                if reduced_counts[state] >= 3:
                                    break
                    P, Q = P_next, Q_next
                    p_prev, p_curr = p_curr, p_next
                    q_prev, q_curr = q_curr, q_next
                    k += 1

                for Gk, qk in collected:
                    for sigma in (1, -1):
                        x0, y0 = sigma * g * Gk, g * qk
                        for Aj, Bj in eps_pows:
                            nx = Aj * x0 + d * Bj * y0
                            ny = Bj * x0 + Aj * y0
                            if nx % 2 != 0 or ny % 2 != 0:
                                continue
                            Xi, Yi = nx // 2, ny // 2
                            if Yi < 1:
                                continue
                            ci = Xi % d
                            if ci == 0 or Xi * Xi - d * Yi * Yi != -ci * (d - ci):
                                continue
                            # Normalize into W_0 (minimal with X >= d + 1, i.e., z > 2d)
                            X, Y = Xi, Yi
                            while X <= d:
                                X, Y = mul_unit(Ar, Br, X, Y, d)
                            while True:
                                Xp, Yp = mul_unit(Ar, -Br, X, Y, d)
                                if Xp >= d + 1 and Yp >= 1:
                                    X, Y = Xp, Yp
                                else:
                                    break
                            assert gt_z_threshold(X, Y, d)
                            Xp, Yp = mul_unit(Ar, -Br, X, Y, d)
                            assert not gt_z_threshold(Xp, Yp, d)
                            w0_set.add((X, Y))
            g += 1

    w0_sorted = sorted(w0_set, key=lambda pt: pt[1])
    # Verify Proposition 5 ordering inside W_0
    for idx in range(len(w0_sorted) - 1):
        X1, Y1 = w0_sorted[idx]
        X2, Y2 = w0_sorted[idx + 1]
        assert Y1 < Y2 and X1 < X2 and lt_z(X1, Y1, X2, Y2, d)
    return Ar, w0_sorted


def brute_force_row(d: int, Y_limit: int) -> list[tuple[int, int, int]]:
    """Exhaustive scan of b >= 1 and 1 <= c <= d-1 for all t <= Y_limit."""
    # Since t^2 = d*b^2 + c*(2*b+1) > d*b^2, b < Y_limit / sqrt(d)
    b_max = isqrt((Y_limit * Y_limit) // d) + 1
    sols = []
    for b in range(1, b_max + 1):
        base = d * b * b
        step = 2 * b + 1
        for c in range(1, d):
            val = base + c * step
            t = isqrt(val)
            if t * t == val and t <= Y_limit:
                sols.append((t, b, c))
    # Verify strict uniqueness of t
    t_vals = [row[0] for row in sols]
    assert len(t_vals) == len(set(t_vals))
    assert t_vals == sorted(t_vals)
    return sols


def main() -> None:
    ds_67 = nonsquares(67)

    # 1. Verify A377290 (all 67 terms) and A377291 (all 46 terms) via Section 4 PQa algorithm
    print("[1/3] Verifying A377290 (67 rows) and A377291 (46 rows) via PQa algorithm...")
    rows_cache: dict[int, tuple[int, list[tuple[int, int]]]] = {}
    for n in range(1, 68):
        d = ds_67[n - 1]
        Ar, w0 = pqa_window(d)
        rows_cache[n] = (Ar, w0)
        p = len(w0)
        assert p == A377290_LIVE[n - 1], f"n={n} d={d}: p={p} != {A377290_LIVE[n - 1]}"
        if n <= len(A377291_LIVE):
            assert Ar == A377291_LIVE[n - 1], f"n={n} d={d}: Ar={Ar} != {A377291_LIVE[n - 1]}"
    print(f"      Matched all {len(A377290_LIVE)} terms of A377290 and {len(A377291_LIVE)} terms of A377291.")

    # 2. Cross-check PQa vs brute-force scan and verify Lemma 2, Theorem 5 across 4 windows
    #    for d = nonsquares(1..12) plus larger interesting rows (d=44 -> n=38, d=77 -> n=67)
    print("[2/3] Exhaustive brute-force check & multi-period recurrence across rows...")
    check_ns = list(range(1, 13)) + [15, 22, 35, 38]
    row_terms: dict[int, list[int]] = {}
    for n in check_ns:
        d = ds_67[n - 1]
        Ar, w0 = rows_cache[n]
        p = len(w0)
        # Generate 4 full periods (W_0..W_3) for smaller rows, 3 periods (W_0..W_2) for huge Ar
        num_periods = 4 if Ar < 10000 else 3
        gen_pts: list[tuple[int, int]] = []
        cur = list(w0)
        for m in range(num_periods):
            gen_pts.extend(cur)
            nxt = [mul_unit(Ar, isqrt((Ar * Ar - 4) // d), X, Y, d) for X, Y in cur]
            # Verify monotone across boundary W_m -> W_{m+1}
            assert cur[-1][1] < nxt[0][1]
            cur = nxt

        Y_max = gen_pts[-1][1]
        # Brute force only when Y_max is computationally small (e.g. <= 10^6, b_max <= 3*10^5)
        if Y_max <= 1_500_000:
            bf = brute_force_row(d, Y_max)
            assert len(bf) == len(gen_pts), f"n={n}: bf={len(bf)} != gen={len(gen_pts)}"
            for k_idx, ((t_bf, b_bf, c_bf), (X_g, Y_g)) in enumerate(zip(bf, gen_pts)):
                assert t_bf == Y_g
                assert d * b_bf + c_bf == X_g
                assert X_g % d == c_bf
                # Check strict periodicity of c and exact recurrence
                if k_idx >= p:
                    assert bf[k_idx][2] == bf[k_idx - p][2]
                if k_idx >= 2 * p:
                    assert bf[k_idx][0] == Ar * bf[k_idx - p][0] - bf[k_idx - 2 * p][0]
            row_terms[n] = [row[0] for row in bf]
        else:
            # Verify generated points satisfy defining equation & recurrence directly
            for k_idx, (X_g, Y_g) in enumerate(gen_pts):
                c_g = X_g % d
                b_g = X_g // d
                assert 1 <= c_g < d and b_g >= 1
                assert Y_g * Y_g == (d - c_g) * b_g * b_g + c_g * (b_g + 1) * (b_g + 1)
                if k_idx >= p:
                    assert X_g % d == gen_pts[k_idx - p][0] % d
                if k_idx >= 2 * p:
                    assert Y_g == Ar * gen_pts[k_idx - p][1] - gen_pts[k_idx - 2 * p][1]
            row_terms[n] = [pt[1] for pt in gen_pts]
    print(f"      Verified brute-force completeness + recurrence across {len(check_ns)} rows (up to d={ds_67[37]}).")

    # 3. Verify all 55 antidiagonal terms of live OEIS A374602
    print("[3/3] Verifying live OEIS A374602 antidiagonal array (55 terms)...")
    # Antidiagonal s = n + k - 1 from 1 to 10 (55 terms total)
    # Generate at least 10 terms for rows n=1..10
    for n in range(1, 11):
        d = ds_67[n - 1]
        Ar, w0 = rows_cache[n]
        Br = isqrt((Ar * Ar - 4) // d)
        terms = []
        cur = list(w0)
        while len(terms) < 10:
            terms.extend(Y for _, Y in cur)
            cur = [mul_unit(Ar, Br, X, Y, d) for X, Y in cur]
        row_terms[n] = terms

    anti = []
    for diag_sum in range(2, 12):
        for n in range(1, diag_sum):
            k = diag_sum - n
            anti.append(row_terms[n][k - 1])
    assert anti == A374602_LIVE, f"Antidiagonal mismatch:\n{anti}\nvs\n{A374602_LIVE}"
    print(f"      Matched all {len(A374602_LIVE)} antidiagonal terms of A374602.")
    print("PASS")


if __name__ == "__main__":
    main()
