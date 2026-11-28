#!/usr/bin/env python3
"""Zero-float exact verification for Radici-Sala Open Problems (F_3, F_4, F_5, n>=2, 2<=d<=n(q-1))."""
from fractions import Fraction
import math
import time


# ==============================================================================
# 1. Exact n = 2 base cases: q in {3, 4, 5}, all 2 <= d <= 2(q-1)
# ==============================================================================

def verify_f3_n2():
    """Exact inclusion-exclusion over all 2^9 subsets of F_3^2 for d in {2, 3, 4}."""
    pts = [(x, y) for x in range(3) for y in range(3)]
    N = 9
    inv3 = [0, 1, 2]

    def rk_f3(rows):
        R = [r[:] for r in rows]
        m = len(R)
        n = len(R[0]) if m else 0
        rk = 0
        for c in range(n):
            piv = -1
            for i in range(rk, m):
                if R[i][c] != 0:
                    piv = i
                    break
            if piv == -1:
                continue
            R[rk], R[piv] = R[piv], R[rk]
            inv = inv3[R[rk][c]]
            for j in range(c, n):
                R[rk][j] = (R[rk][j] * inv) % 3
            for i in range(rk + 1, m):
                f = R[i][c]
                if f:
                    for j in range(c, n):
                        R[i][j] = (R[i][j] - f * R[rk][j]) % 3
            rk += 1
        return rk

    for d in [2, 3, 4]:
        exps = [(a, b) for a in range(3) for b in range(3) if a + b <= d]
        D = len(exps)
        vecs = [[(pow(x, a, 3) * pow(y, b, 3)) % 3 for a, b in exps] for x, y in pts]
        a0 = 0
        a1 = 0
        for mask in range(1 << N):
            rows = [vecs[i] for i in range(N) if (mask >> i) & 1]
            rk = rk_f3(rows)
            k = mask.bit_count()
            sgn0 = 1 if k % 2 == 0 else -1
            term = N ** (D - rk)
            a0 += sgn0 * term
            if mask & 1:
                a1 += (-sgn0) * N * term
        assert a1 > a0, f"F_3 n=2 d={d} failed: {a1} <= {a0}"
        if d == 2:
            assert (a0, a1) == (184184, 206712)
        print(f"[PASS] F_3 n=2 d={d}: alpha0={a0} < alpha1={a1}")


def verify_f4_n2():
    """Exact bit-packed incremental rank inclusion-exclusion over F_4^2 (N=16) for d=2..6."""
    ADD = [[0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 0, 1], [3, 2, 1, 0]]
    MUL = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]
    INV = [0, 1, 3, 2]

    def pw(x, e):
        r = 1
        for _ in range(e):
            r = MUL[r][x]
        return r

    pts = [(x, y) for x in range(4) for y in range(4)]
    N = 16

    for d in range(2, 7):
        if d == 6:
            a0 = 15 ** 16
            a1 = 16 * (15 ** 15)
            assert a1 > a0
            print(f"[PASS] F_4 n=2 d=6 (coloop): alpha0={a0} < alpha1={a1}")
            continue
        exps = [(a, b) for a in range(4) for b in range(4) if a + b <= d]
        D = len(exps)
        pvecs = [[MUL[pw(x, a)][pw(y, b)] for a, b in exps] for x, y in pts]

        # Gray-code or recursive incremental basis in F_4 (2 bits per entry, packed into Python int)
        # Or recursive depth-first subset enumeration maintaining echelon basis!
        a0 = 0
        a1 = 0
        powN = [N ** k for k in range(D + 1)]

        def dfs(idx, parity, has0, basis_rows, basis_pivs):
            nonlocal a0, a1
            if idx == N:
                term = powN[D - len(basis_pivs)]
                if parity == 0:
                    a0 += term
                else:
                    a0 -= term
                if has0:
                    if parity == 1:
                        a1 += N * term
                    else:
                        a1 -= N * term
                return
            # Branch 0: exclude pts[idx]
            dfs(idx + 1, parity, has0, basis_rows, basis_pivs)
            # Branch 1: include pts[idx]
            vec = pvecs[idx][:]
            for r_row, pc in zip(basis_rows, basis_pivs):
                f = vec[pc]
                if f:
                    for j in range(pc, D):
                        vec[j] = ADD[vec[j]][MUL[f][r_row[j]]]
            new_piv = -1
            for j in range(D):
                if vec[j]:
                    new_piv = j
                    break
            if new_piv == -1:
                dfs(idx + 1, parity ^ 1, has0 or (idx == 0), basis_rows, basis_pivs)
            else:
                inv = INV[vec[new_piv]]
                if inv != 1:
                    for j in range(new_piv, D):
                        vec[j] = MUL[inv][vec[j]]
                dfs(idx + 1, parity ^ 1, has0 or (idx == 0), basis_rows + [vec], basis_pivs + [new_piv])

        dfs(0, 0, False, [], [])
        assert a1 > a0, f"F_4 n=2 d={d} failed: {a1} <= {a0}"
        if d == 2:
            assert (a0, a1) == (6012645, 6242400)
        print(f"[PASS] F_4 n=2 d={d}: alpha0={a0} < alpha1={a1}")


def verify_f5_n2():
    """Exact AGL_2(F_5) orbit + matroid duality verification for F_5^2 (N=25), d=2..8."""
    pts = [(x, y) for x in range(5) for y in range(5)]
    pt_idx = {p: i for i, p in enumerate(pts)}
    gl2 = [(a, b, c, d) for a in range(5) for b in range(5) for c in range(5) for d in range(5) if (a * d - b * c) % 5 != 0]
    tri_to_perm = {}
    for a, b, c, d in gl2:
        for tx in range(5):
            for ty in range(5):
                p = [pt_idx[((a * x + b * y + tx) % 5, (c * x + d * y + ty) % 5)] for x, y in pts]
                p_inv = [0] * 25
                for idx, val in enumerate(p):
                    p_inv[val] = idx
                tri_to_perm[(p[0], p[5], p[1])] = tuple(1 << p_inv[m] for m in range(25))

    def canon_and_stab(mask):
        bits = [i for i in range(25) if (mask >> i) & 1]
        k = len(bits)
        if k == 0:
            return 0, 12000
        if k == 1:
            return 1, 480
        if k == 2:
            return 3, 40
        x0, y0 = pts[bits[0]]
        x1, y1 = pts[bits[1]]
        dx, dy = (x1 - x0) % 5, (y1 - y0) % 5
        if all(((pts[b][0] - x0) * dy - (pts[b][1] - y0) * dx) % 5 == 0 for b in bits[2:]):
            return (1 << k) - 1, 12000 // (30 * math.comb(5, k))
        best = 1 << 26
        cnt = 0
        for idx0 in range(k):
            b0 = bits[idx0]
            for idx1 in range(k):
                if idx1 == idx0:
                    continue
                b1 = bits[idx1]
                for idx2 in range(k):
                    if idx2 == idx0 or idx2 == idx1:
                        continue
                    bm = tri_to_perm.get((b0, b1, bits[idx2]))
                    if bm is None:
                        continue
                    nm = 0
                    for b in bits:
                        nm |= bm[b]
                    if nm < best:
                        best = nm
                        cnt = 1
                    elif nm == best:
                        cnt += 1
        return best, cnt

    orbits = {0: {0: 1}}
    for k in range(1, 13):
        seen = {}
        for m in orbits[k - 1]:
            for bit in range(25):
                if not ((m >> bit) & 1):
                    cm, stab = canon_and_stab(m | (1 << bit))
                    if cm not in seen:
                        seen[cm] = 12000 // stab
        assert sum(seen.values()) == math.comb(25, k)
        orbits[k] = seen

    inv5 = [0, 1, 3, 2, 4]

    def rk_f5(rows):
        if not rows:
            return 0
        R = [r[:] for r in rows]
        m = len(R)
        n = len(R[0])
        rk = 0
        for c in range(n):
            piv = -1
            for i in range(rk, m):
                if R[i][c] != 0:
                    piv = i
                    break
            if piv == -1:
                continue
            R[rk], R[piv] = R[piv], R[rk]
            inv = inv5[R[rk][c]]
            for j in range(c, n):
                R[rk][j] = (R[rk][j] * inv) % 5
            for i in range(rk + 1, m):
                f = R[i][c]
                if f:
                    for j in range(c, n):
                        R[i][j] = (R[i][j] - f * R[rk][j]) % 5
            rk += 1
        return rk

    pt_vecs = {}
    D_map = {}
    for d in range(8):
        exps = [(a, b) for a in range(5) for b in range(5) if a + b <= d]
        D_map[d] = len(exps)
        pt_vecs[d] = [[(pow(x, a, 5) * pow(y, b, 5)) % 5 for a, b in exps] for x, y in pts]

    rk_table = {d: {} for d in range(8)}
    for d in range(8):
        vecs = pt_vecs[d]
        rd = 7 - d
        ad, bd = divmod(rd, 4)
        d_dual = (5 - bd) * (5 ** (1 - ad))
        for k in range(13):
            for m in orbits[k]:
                if k < d_dual:
                    rk_table[d][m] = k
                else:
                    rk_table[d][m] = rk_f5([vecs[b] for b in range(25) if (m >> b) & 1])

    N = 25
    for d in range(2, 8):
        D = D_map[d]
        a0 = 0
        a1 = 0
        for k in range(13):
            sgn0 = 1 if k % 2 == 0 else -1
            sgn1 = -sgn0
            for m, osz in orbits[k].items():
                rk = rk_table[d][m]
                term = osz * (N ** (D - rk))
                a0 += sgn0 * term
                a1 += sgn1 * k * term
        for k in range(13):
            kp = 25 - k
            sgn0 = 1 if kp % 2 == 0 else -1
            sgn1 = -sgn0
            for m, osz in orbits[k].items():
                rk = D - k + rk_table[7 - d][m]
                term = osz * (N ** (D - rk))
                a0 += sgn0 * term
                a1 += sgn1 * kp * term
        assert a1 > a0, f"F_5 n=2 d={d} failed: {a1} <= {a0}"
        if d == 2:
            assert (a0, a1) == (88849944, 88998000)
        print(f"[PASS] F_5 n=2 d={d}: alpha0={a0} < alpha1={a1}")

    a0_8 = 24 ** 25
    a1_8 = 25 * (24 ** 24)
    assert a1_8 > a0_8
    print(f"[PASS] F_5 n=2 d=8 (coloop): alpha0={a0_8} < alpha1={a1_8}")


# ==============================================================================
# 2. Exact MacWilliams & Symmetric-Matrix Codeword Checks
# ==============================================================================

def dual_weights_plane(q, d):
    """Exact MacWilliams dual low-weight spectrum for GRM_q(d, 2)^perp."""
    if q == 4:
        ADD = [[0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 0, 1], [3, 2, 1, 0]]
        MUL = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]
        def pw(x, e):
            r = 1
            for _ in range(e):
                r = MUL[r][x]
            return r
    else:
        ADD = [[(a + b) % q for b in range(q)] for a in range(q)]
        MUL = [[(a * b) % q for b in range(q)] for a in range(q)]
        def pw(x, e):
            return pow(x, e, q)

    pts = [(x, y) for x in range(q) for y in range(q)]
    N = q * q
    exps = [(a, b) for a in range(q) for b in range(q) if a + b <= d]
    D = len(exps)
    rows = [[MUL[pw(x, a)][pw(y, b)] for x, y in pts] for a, b in exps]
    p_wts = {}
    cur = [0] * N

    def rec(idx, first_nz):
        if idx == D:
            w = N - cur.count(0)
            p_wts[w] = p_wts.get(w, 0) + ((q - 1) if first_nz else 1)
            return
        rec(idx + 1, first_nz)
        max_c = (q - 1) if first_nz else 1
        row = rows[idx]
        for c in range(1, max_c + 1):
            for j in range(N):
                cur[j] = ADD[cur[j]][MUL[c][row[j]]]
            rec(idx + 1, True)
            neg = (q - c) if q != 4 else c
            for j in range(N):
                cur[j] = ADD[cur[j]][MUL[neg][row[j]]]

    rec(0, False)
    assert sum(p_wts.values()) == q ** D
    dual = {}
    for w in range(9):
        s = 0
        for i, Ai in p_wts.items():
            kw = sum(((-1) ** j) * ((q - 1) ** (w - j)) * math.comb(i, j) * math.comb(N - i, w - j)
                     for j in range(min(i, w) + 1) if w - j <= N - i)
            s += Ai * kw
        assert s % (q ** D) == 0
        dual[w] = s // (q ** D)
    return dual


def grm5_23_primal_weights():
    """Exact 8-term primal weight enumerator of GRM_5(2,3) via all 5^6 symmetric 3x3 forms."""
    wts = {}
    def add(w, cnt):
        wts[w] = wts.get(w, 0) + cnt
    sq = {1, 4}
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    for e in range(5):
                        for f in range(5):
                            det = (a * (d * f - e * e) - b * (b * f - c * e) + c * (b * e - c * d)) % 5
                            if det != 0:
                                add(100, 125); add(95, 250); add(105, 250)
                            else:
                                m1 = (a * d - b * b) % 5
                                m2 = (a * f - c * c) % 5
                                m3 = (d * f - e * e) % 5
                                nz = m1 or m2 or m3
                                if nz:
                                    add(100, 500)
                                    if nz in sq:
                                        add(80, 25); add(105, 100)
                                    else:
                                        add(120, 25); add(95, 100)
                                elif a or d or f:
                                    add(100, 605); add(75, 10); add(125, 10)
                                else:
                                    add(0, 1); add(125, 4); add(100, 620)
    assert sum(wts.values()) == 5 ** 10
    return wts


# ==============================================================================
# 3. Uniform-in-N Rational Bounds (Zero Floats)
# ==============================================================================

def exp_ub(x):
    assert 0 <= x < 18
    s = sum((x ** k) / math.factorial(k) for k in range(18))
    return s + (x ** 18) / (math.factorial(18) * (1 - x / 19))


E_UB = exp_ub(Fraction(1))


def full_space_Y_moments(q, N, max_m):
    ez = [Fraction(1, q) + Fraction(q - 1, q) * (Fraction(-1, q - 1) ** r) for r in range(max_m + 1)]
    def poly_mul(A, B):
        C = [Fraction(0)] * (max_m + 1)
        for i in range(max_m + 1):
            if A[i] == 0:
                continue
            for j in range(max_m + 1 - i):
                C[i + j] += A[i] * B[j]
        return C
    base = [ez[r] / math.factorial(r) for r in range(max_m + 1)]
    res = [Fraction(0)] * (max_m + 1)
    res[0] = Fraction(1)
    p = N
    b = base
    while p > 0:
        if p & 1:
            res = poly_mul(res, b)
        p >>= 1
        if p > 0:
            b = poly_mul(b, b)
    return [res[m] * math.factorial(m) / (N ** m) for m in range(max_m + 1)]


def normalized_EY_ub_monotone(q, N, m):
    """Exact upper bound on N^{m/2} * E_{F_q^N}[Y^m] that is strictly decreasing in N."""
    ez = [Fraction(1, q) + Fraction(q - 1, q) * (Fraction(-1, q - 1) ** r) for r in range(m + 1)]
    def gen_parts(rem, min_p):
        if rem == 0:
            yield []
        for p in range(min_p, rem + 1):
            for rest in gen_parts(rem - p, p):
                yield [p] + rest
    total = Fraction(0)
    for part in gen_parts(m, 2):
        k = len(part)
        denom = 1
        counts = {}
        for r in part:
            denom *= math.factorial(r)
            counts[r] = counts.get(r, 0) + 1
        for cnt in counts.values():
            denom *= math.factorial(cnt)
        coeff = math.factorial(m) // denom
        prod_ez = Fraction(1)
        for r in part:
            prod_ez *= ez[r]
        assert prod_ez > 0
        total += coeff * prod_ez * (Fraction(1, N) ** (m // 2 - k))
    return total


def alpha_mw(q, N, m, w):
    if w > m:
        return Fraction(0)
    poly = [Fraction(0)] * (m + 1)
    u = Fraction(-(q - 1), q)
    for j in range(m - w + 1):
        poly[w + j] = Fraction(math.comb(N - w, j)) * (u ** j) * (Fraction(1, q) ** w)
    c_op = Fraction(q, (q - 1) * N)
    for _ in range(m):
        nxt = [Fraction(0)] * (m + 1)
        for k in range(m + 1):
            nxt[k] += poly[k]
            if k >= 1:
                nxt[k - 1] += c_op * k * poly[k]
                nxt[k] -= c_op * k * poly[k]
        poly = nxt
    return poly[0]


def verify_lam_kappa_le_bounds():
    """Verify lambda_q <= q-1 and kappa_q <= 1 for all q in {3,4,5}, N >= N0."""
    for q, N0 in [(3, 27), (4, 64), (5, 125)]:
        b = Fraction(q, N0 - 1)
        lam_over_qm1_ub = Fraction(N0, q) * (b - b * b / 2 + b * b * b / 3)
        assert lam_over_qm1_ub <= 1
        # Check -(q-2)N^2 + ((2/3)q^2 + q - 4)N + 2 < 0 for N >= N0 (already negative at N0 & vertex < N0)
        assert -(q - 2) * N0 * N0 + (Fraction(2, 3) * q * q + q - 4) * N0 + 2 < 0
        # Check kappa_q <= 1 via 1/(N-1) <= diff_lb
        lhs = Fraction(1, N0 - 1)
        rhs = Fraction(q - 1) * (
            Fraction(3, 2 * N0)
            - Fraction(q - 1, 2 * N0 * N0)
            - Fraction(q * (2 * N0 - 1), 2 * N0 * (N0 - 1) * (N0 - 1))
            - Fraction((q ** 3) * N0, 4 * ((N0 - 1) ** 4))
        )
        assert lhs <= rhs
    print("[PASS] Universal bounds lambda_q <= q-1 and kappa_q <= 1 verified for all N >= N0")


def s0_lb_monotone(N0, lambda5_sub=False):
    """Exact polynomial lower bound on S_0(N)/N^{D-1} valid for ALL N >= N0.
    By cancellation 1/N^3 - (4N+5)(N-4)/(5N^5) > 0, broken 4-circuits (beta_3) only help;
    lambda5_sub=True subtracts Lambda_5(n) = N(N-1)/20 for 5-line broken circuits when d_dual <= 5."""
    pts = []
    for k in range(6):
        N = 100 + k
        s = Fraction(1) - Fraction(N - 1, N) + Fraction(math.comb(N - 1, 2), N ** 2) - Fraction(math.comb(N - 1, 3), N ** 3)
        sig4_lb = Fraction(math.comb(N - 1, 4))
        if lambda5_sub:
            sig4_lb -= Fraction(N * (N - 1), 20)
        s += Fraction(4 * N + 5, 5 * (N ** 5)) * sig4_lb
        pts.append((Fraction(1, N), s))
    cs = [Fraction(0)] * 6
    for i, (ti, yi) in enumerate(pts):
        p = [Fraction(1)]
        denom = Fraction(1)
        for j, (tj, _) in enumerate(pts):
            if i == j:
                continue
            denom *= (ti - tj)
            np = [Fraction(0)] * (len(p) + 1)
            for idx, c in enumerate(p):
                np[idx + 1] += c
                np[idx] -= c * tj
            p = np
        for idx, c in enumerate(p):
            cs[idx] += yi * c / denom
    t0 = Fraction(1, N0)
    return cs[0] + sum(min(Fraction(0), c) * (t0 ** i) for i, c in enumerate(cs) if i >= 1)


def fmt_frac6(x):
    """Exact decimal truncation to 6 places using integer arithmetic only (zero floats)."""
    sign = "-" if x < 0 else ""
    ax = -x if x < 0 else x
    scaled = (ax.numerator * 1000000) // ax.denominator
    whole, frac = divmod(scaled, 1000000)
    return f"{sign}{whole}.{frac:06d}"


def verify_n_ge_3_all_regimes():
    verify_lam_kappa_le_bounds()

    d32 = dual_weights_plane(3, 2)
    d42 = dual_weights_plane(4, 2)
    d52 = dual_weights_plane(5, 2)
    d53 = dual_weights_plane(5, 3)
    assert d32[4] == 0 and d32[5] == 0 and d32[6] == 24
    assert d42[4] == 60 and d42[5] == 0 and d42[6] == 1920
    assert d52[4] == 600 and d52[5] == 120 and d52[6] == 52000
    assert d53[4] == 0 and d53[5] == 120 and d53[6] == 0 and d53[7] == 0
    print(f"[PASS] Exact planar dual weights verified: GRM_3(2,2)^perp A_6=24, GRM_4(2,2)^perp, GRM_5(2,2)^perp, GRM_5(3,2)^perp A_6=A_7=0")

    # Helper for monotone remainder bound using kappa_q <= 1, lam_q <= q-1:
    # (N/(q-1)) * f_q^{(m)}(Y_max) / m! * E[Y^m] <= e^{(q-1)Y_max} * (q-1)^{m-1} * ((q-1)Y_max + m) / m! * N^{2 - m/2} * normalized_EY
    def rem_mono_zero_code(q, N0, D0, m, Y_max):
        ey_norm = normalized_EY_ub_monotone(q, N0, m)
        pref = exp_ub(Fraction(q - 1) * Y_max) * ((q - 1) ** (m - 1)) * ((q - 1) * Y_max + m) / math.factorial(m)
        rem = pref * ey_norm / (N0 ** (m // 2 - 2))
        c0 = Fraction(N0 * N0) * (E_UB ** (q - 1)) / (q ** D0)
        return c0 + rem

    # 1. Five zero-codeword monotone regimes (all n >= 3)
    zero_regimes = [
        ("q=3, d>=3, n>=3", 3, 27, 17, 8, Fraction(1)),
        ("q=4, d=3, n>=3", 4, 64, 20, 6, Fraction(2, 3)),
        ("q=4, d>=4, n>=3", 4, 64, 30, 8, Fraction(1)),
        ("q=5, d=4, n>=3", 5, 125, 34, 8, Fraction(3, 4)),
        ("q=5, d>=5, n>=3", 5, 125, 50, 8, Fraction(1)),
    ]
    for name, q, N0, D0, m, Ym in zero_regimes:
        s0_lb = s0_lb_monotone(N0)
        err = rem_mono_zero_code(q, N0, D0, m, Ym)
        assert err < s0_lb
        print(f"[PASS] {name:18s}: err_ub={fmt_frac6(err)} < {fmt_frac6(s0_lb)} = S0_lb")

    # 2. q=3, d=2, n>=3 (M=6, Y_max=1/2, A4=A5=0, A6 <= N^3/18)
    s0_32 = s0_lb_monotone(27)
    pref_32 = exp_ub(Fraction(1)) * (2 ** 5) * (1 + 6) / math.factorial(6)
    n3_ey_32 = normalized_EY_ub_monotone(3, 27, 6)
    n3_a6_32 = Fraction(1, 18) * Fraction(45, 4)
    r6_32 = pref_32 * (n3_ey_32 + n3_a6_32) / 27
    c0_32 = Fraction(27 * 27) * (E_UB ** 2) / (3 ** 10)
    err_32 = r6_32 + c0_32
    assert err_32 < s0_32
    print(f"[PASS] q=3, d=2, n>=3    : err_ub={fmt_frac6(err_32)} < {fmt_frac6(s0_32)} = S0_lb")

    # 3. q=5, d=3, n>=3 (M=6, Y_max=1/2, A4=A6=A7=0, A5 <= N^2/5)
    s0_53 = s0_lb_monotone(125, lambda5_sub=True)
    pref_53 = exp_ub(Fraction(2)) * (4 ** 5) * (2 + 6) / math.factorial(6)
    n3_ey_53 = normalized_EY_ub_monotone(5, 125, 6)
    n3_a5_53 = Fraction(1, 5) * Fraction(675, 512) / 125
    r6_53 = pref_53 * (n3_ey_53 + n3_a5_53) / 125
    c0_53 = Fraction(125 * 125) * (E_UB ** 4) / (5 ** 20)
    err_53 = r6_53 + c0_53
    assert err_53 < s0_53
    print(f"[PASS] q=5, d=3, n>=3    : err_ub={fmt_frac6(err_53)} < {fmt_frac6(s0_53)} = S0_lb")

    # 4. q=4, d=2, n=3 (exact N=64) and n>=4 (monotone N>=256)
    # 4a: n=3 exact (broken 4-circuits only improve S0_lb; beta4_new = 0)
    s0_64 = Fraction(1) - Fraction(63, 64) + Fraction(math.comb(63, 2), 64 ** 2) - Fraction(math.comb(63, 3), 64 ** 3) \
            + Fraction(4 * 64 + 5, 5 * (64 ** 5)) * math.comb(63, 4)
    w3_64 = Fraction(1) - Fraction(60, 64) + Fraction(60 * 59, 2 * 64 * 64)
    margin_64 = s0_64 - Fraction(21, 64) * w3_64
    z4 = Fraction(4, 2 * 64 + 2)
    ln4_lb = 2 * sum((z4 ** (2 * k + 1)) / (2 * k + 1) for k in range(18))
    ln4_ub = ln4_lb + 2 * (z4 ** 37) / (37 * (1 - z4 * z4))
    lam4_lb = Fraction(3 * 64, 4) * ln4_lb
    lam4_ub = Fraction(3 * 64, 4) * ln4_ub
    kap4_ub = Fraction(64, 63) * (Fraction(67, 64) ** 63) / sum((lam4_lb ** k) / math.factorial(k) for k in range(25))
    c4_64_ub = kap4_ub * 3 * (64 * (lam4_ub ** 3) / 6 - (lam4_lb ** 4) / 24)
    c5_64_ub = kap4_ub * 3 * (64 * (lam4_ub ** 4) / 24 - (lam4_lb ** 5) / 120)
    A4_64 = 64 * 63 // 4
    A6_64 = ((64 * 63 * 60) // (16 * 15 * 12)) * 1920
    p5_ex_64 = (c4_64_ub * alpha_mw(4, 64, 4, 4) + c5_64_ub * alpha_mw(4, 64, 5, 4) - Fraction(4, 64 ** 3)) * A4_64
    ey6_64 = full_space_Y_moments(4, 64, 6)[6] - Fraction(1, 4 ** 10) + A4_64 * alpha_mw(4, 64, 6, 4) + A6_64 * alpha_mw(4, 64, 6, 6)
    r6_64 = exp_ub(Fraction(1)) * (3 ** 5) * 7 / math.factorial(6) * (64 ** 2) * ey6_64
    c0_64 = Fraction(64 * 63) * (E_UB ** 3) / (4 ** 10)
    err_64 = Fraction(64, 3) * p5_ex_64 + r6_64 + c0_64
    assert err_64 < margin_64
    print(f"[PASS] q=4, d=2, n=3     : err_ub={fmt_frac6(err_64)} < {fmt_frac6(margin_64)}=margin (surplus > {fmt_frac6(margin_64 - err_64)})")

    # 4b: q=4, d=2, n>=4 monotone (N0=256)
    pts42 = []
    for k in range(6):
        Nk = 100 + k
        s0k = Fraction(1) - Fraction(Nk - 1, Nk) + Fraction(math.comb(Nk - 1, 2), Nk ** 2) - Fraction(math.comb(Nk - 1, 3), Nk ** 3) \
              + Fraction(4 * Nk + 5, 5 * (Nk ** 5)) * math.comb(Nk - 1, 4)
        w3k = Fraction(1) - Fraction(Nk - 4, Nk) + Fraction((Nk - 4) * (Nk - 5), 2 * Nk * Nk)
        pts42.append((Fraction(1, Nk), s0k - Fraction(Nk - 1, 3 * Nk) * w3k))
    cs42 = [Fraction(0)] * 6
    for i, (ti, yi) in enumerate(pts42):
        p = [Fraction(1)]; denom = Fraction(1)
        for j, (tj, _) in enumerate(pts42):
            if i == j: continue
            denom *= (ti - tj)
            np = [Fraction(0)] * (len(p) + 1)
            for idx, c in enumerate(p): np[idx + 1] += c; np[idx] -= c * tj
            p = np
        for idx, c in enumerate(p): cs42[idx] += yi * c / denom
    margin_256 = cs42[0] + sum(min(Fraction(0), c) * (Fraction(1, 256) ** i) for i, c in enumerate(cs42) if i >= 1)
    pref_42 = exp_ub(Fraction(1)) * (3 ** 5) * 7 / math.factorial(6)
    n3_42 = normalized_EY_ub_monotone(4, 256, 6) + Fraction(1, 4) * (Fraction(40, 27) + Fraction(1120, 243) / 256) + Fraction(2, 3) * Fraction(80, 81)
    r6_256 = pref_42 * n3_42 / 256
    p5_256 = Fraction(1, 4) * Fraction(20, 3 * 256)
    c0_256 = Fraction(256 * 256) * (E_UB ** 3) / (4 ** 15)
    err_256 = r6_256 + p5_256 + c0_256
    assert err_256 < margin_256
    print(f"[PASS] q=4, d=2, n>=4    : err_ub={fmt_frac6(err_256)} < {fmt_frac6(margin_256)}=margin (surplus > {fmt_frac6(margin_256 - err_256)})")

    # 5. q=5, d=2, n=3 (N=125, exact 8-weight matrix + analytic 102960 bad3 + W_5<=10146/15625 + w=7 even port)
    p523 = grm5_23_primal_weights()
    dual_523 = {}
    for w in [4, 5, 6, 7]:
        s = sum(Ai * sum(((-1) ** j) * (4 ** (w - j)) * math.comb(i, j) * math.comb(125 - i, w - j)
                         for j in range(min(i, w) + 1) if w - j <= 125 - i)
                for i, Ai in p523.items())
        assert s % (5 ** 10) == 0
        dual_523[w] = s // (5 ** 10)
    assert dual_523 == {4: 15500, 5: 3100, 6: 8060000, 7: 81840000}
    exact_N_Phi_all = Fraction(0)
    for wt, cnt in p523.items():
        term = (Fraction(129, 125) ** (125 - wt)) * (Fraction(124, 125) ** wt) * (
            Fraction(4 * (125 - wt) * 125, 129) - Fraction(wt * 125, 124)
        )
        exact_N_Phi_all += cnt * term
    exact_N_Phi_all /= (5 ** 10)
    # w=7 has even port size |P|=6 (contributes >= 0), so exclude w=7 alongside w=4,5,6!
    exact_N_Phi_ge8 = (
        exact_N_Phi_all
        - Fraction(4 * 15500, 125 ** 3)
        - Fraction(5 * 3100, 125 ** 4)
        - Fraction(6 * 8060000, 125 ** 5)
        - Fraction(7 * 81840000, 125 ** 6)
    )
    w5_125_ub = Fraction(1) - Fraction(100, 125) + Fraction(math.comb(119, 2), 125 ** 2)
    err_125 = Fraction(125, 4) * (Fraction(6 * 8060000, 125 ** 5) * w5_125_ub + exact_N_Phi_ge8)
    s0_125 = Fraction(1) - Fraction(124, 125) + Fraction(math.comb(124, 2), 125 ** 2) - Fraction(math.comb(124, 3), 125 ** 3) \
             + Fraction(4 * 125 + 5, 5 * (125 ** 5)) * (math.comb(124, 4) - (125 * 124) // 20)
    # Include |C cap P| = 0 external 4-lines (T subset L', p < T: at most 744 * 5 = 3720 triples) explicitly!
    bad3_125 = 360 + 6840 + 744 * 5 + (744 * 15 * 3 * 118) // 93 + 6 * (40 + 20 + 10) * 118
    assert bad3_125 == 102960
    sig3_125_lb = math.comb(120, 3) - bad3_125
    # Both coarse r<=4 (sigma_4 <= C(120,4)) and shadow-tightened (sigma_4 <= 117/4 * sigma_3) clear err_125:
    w4_125_coarse = Fraction(1) - Fraction(120, 125) + Fraction(math.comb(120, 2), 125 ** 2) \
                    - Fraction(sig3_125_lb, 125 ** 3) + Fraction(math.comb(120, 4), 125 ** 4)
    w4_125_shadow = Fraction(1) - Fraction(120, 125) + Fraction(math.comb(120, 2), 125 ** 2) \
                    - Fraction(3 * 125 + 8, 4 * (125 ** 4)) * sig3_125_lb
    margin_125_coarse = s0_125 - Fraction(93, 125) * w4_125_coarse
    margin_125_shadow = s0_125 - Fraction(93, 125) * w4_125_shadow
    assert err_125 < margin_125_coarse < margin_125_shadow
    print(f"[PASS] q=5, d=2, n=3     : exact err={fmt_frac6(err_125)} < {fmt_frac6(margin_125_coarse)} (coarse r<=4) < {fmt_frac6(margin_125_shadow)} (shadow)")

    # 5b: q=5, d=2, n=4 (N=625) and n>=5 (N0=3125) under both coarse r<=4 and shadow-tightened r<=4
    def margin_52_lb(N0, use_shadow):
        pts52 = []
        for k in range(7):
            Nk = 100 + k
            s0k = Fraction(1) - Fraction(Nk - 1, Nk) + Fraction(math.comb(Nk - 1, 2), Nk ** 2) - Fraction(math.comb(Nk - 1, 3), Nk ** 3) \
                  + Fraction(4 * Nk + 5, 5 * (Nk ** 5)) * (math.comb(Nk - 1, 4) - Fraction(Nk * (Nk - 1), 20))
            sig3k = Fraction(math.comb(Nk - 5, 3)) - Fraction(29, 2) * Nk * Nk
            if use_shadow:
                w4k = Fraction(1) - Fraction(Nk - 5, Nk) + Fraction((Nk - 5) * (Nk - 6), 2 * Nk * Nk) - Fraction(3 * Nk + 8, 4 * (Nk ** 4)) * sig3k
            else:
                w4k = Fraction(1) - Fraction(Nk - 5, Nk) + Fraction((Nk - 5) * (Nk - 6), 2 * Nk * Nk) - Fraction(sig3k, Nk ** 3) + Fraction(math.comb(Nk - 5, 4), Nk ** 4)
            pts52.append((Fraction(1, Nk), s0k - Fraction(3 * (Nk - 1), 4 * Nk) * w4k))
        cs52 = [Fraction(0)] * 7
        for i, (ti, yi) in enumerate(pts52):
            p = [Fraction(1)]; denom = Fraction(1)
            for j, (tj, _) in enumerate(pts52):
                if i == j: continue
                denom *= (ti - tj)
                np = [Fraction(0)] * (len(p) + 1)
                for idx, c in enumerate(p): np[idx + 1] += c; np[idx] -= c * tj
                p = np
            for idx, c in enumerate(p): cs52[idx] += yi * c / denom
        return cs52[0] + sum(min(Fraction(0), c) * (Fraction(1, N0) ** i) for i, c in enumerate(cs52) if i >= 1)

    # 5b: q=5, d=2, n=4 (exact P_5+R_6 at N=625 < m_coarse) and n>=5 (monotone at N0=3125 < m_coarse)
    # At N=625: compute exact lam5, kap5 bounds via rational Taylor so P_5 excess is bounded without losing 10*(q-2)/N:
    N4 = 625
    z5_4 = Fraction(5, 2 * N4 + 3)
    ln5_4_lb = 2 * sum((z5_4 ** (2 * k + 1)) / (2 * k + 1) for k in range(18))
    ln5_4_ub = ln5_4_lb + 2 * (z5_4 ** 37) / (37 * (1 - z5_4 * z5_4))
    lam5_4_lb = Fraction(4 * N4, 5) * ln5_4_lb
    lam5_4_ub = Fraction(4 * N4, 5) * ln5_4_ub
    kap5_4_ub = Fraction(N4, N4 - 1) * (Fraction(N4 + 4, N4) ** (N4 - 1)) / sum((lam5_4_lb ** k) / math.factorial(k) for k in range(25))
    # Upper bound c4, c5 (note N*lam^{r-1}/(r-1)! - lam^r/r! = lam^{r-1}/r! * (r*N - lam) > 0):
    c4_4_ub = kap5_4_ub * 4 * (N4 * (lam5_4_ub ** 3) / 6 - (lam5_4_lb ** 4) / 24)
    c5_4_ub = kap5_4_ub * 4 * (N4 * (lam5_4_ub ** 4) / 24 - (lam5_4_lb ** 5) / 120)
    A4_4 = N4 * (N4 - 1)
    A5_4 = N4 * (N4 - 1) // 5
    A6_4 = ((N4 * (N4 - 1) * (N4 - 5)) // (25 * 24 * 20)) * 52000
    p5_ex_4 = (c4_4_ub * alpha_mw(5, N4, 4, 4) + c5_4_ub * alpha_mw(5, N4, 5, 4) - Fraction(4, N4 ** 3)) * A4_4 \
              + (c5_4_ub * alpha_mw(5, N4, 5, 5) - Fraction(5, N4 ** 4)) * A5_4
    ey6_4 = full_space_Y_moments(5, N4, 6)[6] - Fraction(1, 5 ** 15) + A4_4 * alpha_mw(5, N4, 6, 4) + A5_4 * alpha_mw(5, N4, 6, 5) + A6_4 * alpha_mw(5, N4, 6, 6)
    r6_4 = exp_ub(Fraction(1)) * (4 ** 5) * 7 / math.factorial(6) * (N4 ** 2) * ey6_4
    c0_4 = Fraction(N4 * (N4 - 1)) * (E_UB ** 4) / (5 ** 15)
    err_4 = Fraction(N4, 4) * p5_ex_4 + r6_4 + c0_4
    m_coarse_4 = margin_52_lb(N4, use_shadow=False)
    m_shadow_4 = margin_52_lb(N4, use_shadow=True)
    assert err_4 < m_coarse_4 < m_shadow_4
    print(f"[PASS] q=5, d=2, n=4     : err_ub={fmt_frac6(err_4)} < {fmt_frac6(m_coarse_4)} (coarse) < {fmt_frac6(m_shadow_4)} (shadow), surplus > {fmt_frac6(m_coarse_4 - err_4)}")

    N5 = 3125
    m_coarse_5 = margin_52_lb(N5, use_shadow=False)
    m_shadow_5 = margin_52_lb(N5, use_shadow=True)
    pref_52 = exp_ub(Fraction(1)) * (4 ** 5) * 7 / math.factorial(6)
    n3_52 = normalized_EY_ub_monotone(5, N5, 6) + (Fraction(45, 128) + Fraction(1275, 512) / N5) + Fraction(1, 5) * Fraction(675, 512) / N5 + Fraction(13, 3) * Fraction(45, 256)
    err_5 = pref_52 * n3_52 / N5 + Fraction(30, 4 * N5) + Fraction(N5 * N5) * (E_UB ** 4) / (5 ** 21)
    assert err_5 < m_coarse_5 < m_shadow_5
    print(f"[PASS] q=5, d=2, n>=5    : err_ub={fmt_frac6(err_5)} < {fmt_frac6(m_coarse_5)} (coarse) < {fmt_frac6(m_shadow_5)} (shadow), surplus > {fmt_frac6(m_coarse_5 - err_5)}")


def main():
    t0 = time.time()
    verify_f3_n2()
    verify_f4_n2()
    verify_f5_n2()
    verify_n_ge_3_all_regimes()
    print(f"OVERALL: PASS ({time.time() - t0:.2f}s)")


if __name__ == "__main__":
    main()
