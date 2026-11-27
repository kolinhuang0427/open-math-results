#!/usr/bin/env python3
"""Exact-arithmetic verification for OEIS A108449 Mathar (2022) D-finite conjecture."""

# --- Sparse bivariate polynomials in Z[x, y]: {(dx, dy): coeff} ---

def p_add(A, B, sign=1):
    C = dict(A)
    for k, v in B.items():
        nv = C.get(k, 0) + sign * v
        if nv:
            C[k] = nv
        elif k in C:
            del C[k]
    return C

def p_mul(A, B):
    C = {}
    for (ax, ay), av in A.items():
        for (bx, by), bv in B.items():
            k = (ax + bx, ay + by)
            C[k] = C.get(k, 0) + av * bv
    return {k: v for k, v in C.items() if v}

def p_pow(A, e):
    res = {(0, 0): 1}
    base = A
    while e:
        if e & 1:
            res = p_mul(res, base)
        e >>= 1
        if e:
            base = p_mul(base, base)
    return res

def p_dx(A):
    return {(ix - 1, iy): ix * v for (ix, iy), v in A.items() if ix > 0}

def p_dy(A):
    return {(ix, iy - 1): iy * v for (ix, iy), v in A.items() if iy > 0}

def from_x(coeffs):
    return {(i, 0): c for i, c in enumerate(coeffs) if c}

def to_y_dict(A):
    d = {}
    for (ix, iy), v in A.items():
        d.setdefault(iy, {})[ix] = v
    return d

def poly1_div_exact(A, B):
    if not A:
        return {}
    degA = max(A)
    degB = max(B)
    lcB = B[degB]
    rem = dict(A)
    q = {}
    for k in range(degA, degB - 1, -1):
        c = rem.get(k, 0)
        if c == 0:
            continue
        assert c % lcB == 0, f"Exact division failed at deg {k}: {c} % {lcB}"
        qc = c // lcB
        q[k - degB] = qc
        for j, bv in B.items():
            idx = j + k - degB
            nv = rem.get(idx, 0) - qc * bv
            if nv:
                rem[idx] = nv
            elif idx in rem:
                del rem[idx]
    assert not rem, f"Nonzero univariate remainder: {rem}"
    return q

def poly1_sub_mul(A, q, B):
    res = dict(A)
    for ix, qv in q.items():
        for jx, bv in B.items():
            idx = ix + jx
            nv = res.get(idx, 0) - qv * bv
            if nv:
                res[idx] = nv
            elif idx in res:
                del res[idx]
    return res

def det_poly(M):
    """Exact determinant of an n x n matrix over Z[x, y] via Laplace expansion."""
    n = len(M)
    if n == 1:
        return M[0][0]
    if n == 2:
        return p_add(p_mul(M[0][0], M[1][1]), p_mul(M[0][1], M[1][0]), sign=-1)
    total = {}
    for col in range(n):
        entry = M[0][col]
        if not entry:
            continue
        sub = [row[:col] + row[col + 1:] for row in M[1:]]
        cof = p_mul(entry, det_poly(sub))
        total = p_add(total, cof, sign=(1 if col % 2 == 0 else -1))
    return total

# --- Univariate polynomials / truncated series in Z[x] ---

def ser_mul(A, B, N):
    C = [0] * N
    for i, av in enumerate(A[:N]):
        if not av:
            continue
        for j in range(min(len(B), N - i)):
            C[i + j] += av * B[j]
    return C

def ser_inv(A, N):
    assert A[0] == 1
    inv = [0] * N
    inv[0] = 1
    for k in range(1, N):
        s = 0
        for j in range(1, min(k + 1, len(A))):
            s += A[j] * inv[k - j]
        inv[k] = -s
    return inv

def poly_eval_shifts(poly_x, k, max_j=8):
    """Extract [x^n](poly_x(x) * y^(k)(x)) as univariate Z[n] coeffs for a(n-j)."""
    # result[j] = list of coeffs [c0, c1, c2, c3] in Z[n]
    res = {j: [0, 0, 0, 0] for j in range(max_j + 1)}
    for d, c in enumerate(poly_x):
        if c == 0:
            continue
        j = d - k
        assert 0 <= j <= max_j, f"Shift out of range: d={d}, k={k}, j={j}"
        # c * prod_{i=0..k-1} (n - j - i) in powers of n
        poly_n = [1]
        for i in range(k):
            a0 = -(j + i)
            nxt = [0] * (len(poly_n) + 1)
            for deg, val in enumerate(poly_n):
                nxt[deg] += a0 * val
                nxt[deg + 1] += val
            poly_n = nxt
        for deg, val in enumerate(poly_n):
            res[j][deg] += c * val
    return res

def main():
    # 1. Verify direct combinatorial path count (n = 0..12) matches Deutsch's GF
    N_comb = 13
    # DP for all paths ending at height 0 (no pyramid check) and primitive pyramid-free paths
    #Wait: compute a(n) directly by DP over sequences of primitive returns with pyramid subtraction,
    # AND independently verify brute-force exact step enumeration for n=0..6!
    from functools import lru_cache

    @lru_cache(None)
    def count_unrestricted(up_rem, h):
        # Paths from height h using up_rem up-steps to return to height 0 (final step allowed anywhere)
        if up_rem == 0:
            return 1  # only d^h works
        tot = count_unrestricted(up_rem - 1, h + 1) + count_unrestricted(up_rem - 1, h + 2)
        if h > 0:
            tot += count_unrestricted(up_rem, h - 1)
        return tot

    # Exact brute-force enumeration of ALL valid paths for n = 0..5 to verify Step 1 bijections directly
    brute = []
    for n in range(6):
        cnt = 0
        def dfs(y_pos, up_used, path, last_h0_idx, cur_run_type, cur_run_len, on_pyr_prefix):
            nonlocal cnt
            if up_used == n and y_pos == 0:
                # Explicitly check pyramid condition on the full step sequence
                L = len(path)
                h = 0
                heights = [0]
                for ch in path:
                    h += 1 if ch == "u" else (2 if ch == "U" else -1)
                    heights.append(h)
                ok = True
                for i in range(L):
                    if heights[i] == 0:
                        for p in range(1, n + 1):
                            if i + 2 * p <= L and path[i:i + p] == ["u"] * p and path[i + p:i + 2 * p] == ["d"] * p:
                                ok = False
                                break
                            if i + 3 * p <= L and path[i:i + p] == ["U"] * p and path[i + p:i + 3 * p] == ["d"] * (2 * p):
                                ok = False
                                break
                        if not ok:
                            break
                if ok:
                    cnt += 1
                return
            if up_used < n:
                dfs(y_pos + 1, up_used + 1, path + ["u"], 0, "", 0, False)
                dfs(y_pos + 2, up_used + 1, path + ["U"], 0, "", 0, False)
            if y_pos > 0:
                dfs(y_pos - 1, up_used, path + ["d"], 0, "", 0, False)
        dfs(0, 0, [], 0, "", 0, False)
        brute.append(cnt)
    assert brute == [1, 0, 4, 32, 252, 2112], f"Brute force mismatch: {brute}"

    # Verify A(x) = sum count_unrestricted(n, 0) x^n satisfies A = 1 + x*A^2 + x*A^3 through x^12
    A_dp = [count_unrestricted(n, 0) for n in range(N_comb)]
    A2 = ser_mul(A_dp, A_dp, N_comb)
    A3 = ser_mul(A2, A_dp, N_comb)
    rhs_A = [1] + [A2[n - 1] + A3[n - 1] for n in range(1, N_comb)]
    assert A_dp == rhs_A, f"A_dp equation mismatch"

    # Compute y(x) = (1 - x) / (1 + x - x*(1-x)*A*(1+A)) through x^65
    N_ser = 65
    A = [1] + [0] * (N_ser - 1)
    for _ in range(N_ser):
        AA2 = ser_mul(A, A, N_ser)
        AA3 = ser_mul(AA2, A, N_ser)
        A = [1] + [AA2[n - 1] + AA3[n - 1] for n in range(1, N_ser)]
    assert A[:N_comb] == A_dp

    # (1-x)*A*(1+A)
    one_plus_A = [A[0] + 1] + A[1:]
    A_one_plus_A = ser_mul(A, one_plus_A, N_ser)
    x_one_minus_x = [0, 1, -1] + [0] * (N_ser - 3)
    sub_term = ser_mul(x_one_minus_x, A_one_plus_A, N_ser)
    denom = [1, 1] + [0] * (N_ser - 2)
    denom = [denom[i] - sub_term[i] for i in range(N_ser)]
    num = [1, -1] + [0] * (N_ser - 2)
    y_ser = ser_mul(num, ser_inv(denom, N_ser), N_ser)

    assert y_ser[:6] == brute, f"GF vs brute mismatch: {y_ser[:6]} vs {brute}"
    oeis_data = [1, 0, 4, 32, 252, 2112, 18484, 166976, 1545548, 14583808,
                 139774180, 1356966240, 13316740764, 131890671680, 1316627340564,
                 13234192747648, 133829733962732, 1360586260341248,
                 13898403178004420, 142578916276009632]
    assert y_ser[:20] == oeis_data, "GF vs OEIS DATA mismatch"

    # 2. Verify Sylvester resultant Res_A(E1, E2) == x^2 * P(x, y) in Z[x, y]
    # E1(A) = x*A^3 + x*A^2 - 1*A + 1  (coeffs a3, a2, a1, a0)
    a3 = {(1, 0): 1}
    a2 = {(1, 0): 1}
    a1 = {(0, 0): -1}
    a0 = {(0, 0): 1}
    # E2(A) = -x*(1-x)*y * A^2 - x*(1-x)*y * A + ((1+x)*y - (1-x))  (coeffs b2, b1, b0)
    b2 = {(1, 1): -1, (2, 1): 1}
    b1 = {(1, 1): -1, (2, 1): 1}
    b0 = {(0, 0): -1, (1, 0): 1, (0, 1): 1, (1, 1): 1}
    Z = {}
    Syl = [
        [a3, a2, a1, a0, Z],
        [Z,  a3, a2, a1, a0],
        [b2, b1, b0, Z,  Z],
        [Z,  b2, b1, b0, Z],
        [Z,  Z,  b2, b1, b0],
    ]
    res = det_poly(Syl)
    P = {
        (0, 0): -1, (1, 0): 3, (2, 0): -3, (3, 0): 1,
        (0, 1): 1, (1, 1): 3, (2, 1): -9, (3, 1): 5,
        (1, 2): -5, (2, 2): -1, (3, 2): 5, (4, 2): 1,
        (1, 3): -1, (2, 3): 9, (3, 3): -3, (4, 3): 3,
    }
    x2P = p_mul({(2, 0): 1}, P)
    assert res == x2P, f"Resultant mismatch!"

    # 3. Verify P(x, y) = 0 implied ODE via exact Z[x, y] division Q / P == 0
    Px = p_dx(P)
    Py = p_dy(P)
    assert Py.get((0, 0), 0) + Py.get((0, 1), 0) * y_ser[0] == 1  # Py(0, y(0)) = 1

    N1 = {k: -v for k, v in Px.items()}

    def next_N(Nk, k):
        t1 = p_mul(Py, p_add(p_mul(Py, p_dx(Nk)), p_mul(N1, p_dy(Nk))))
        t2 = p_mul(Nk, p_add(p_mul(Py, p_dx(Py)), p_mul(N1, p_dy(Py))))
        return p_add(t1, {key: -(2 * k - 1) * v for key, v in t2.items()})

    N2 = next_N(N1, 1)
    N3 = next_N(N2, 2)

    p_inhom_c = [0, -42504, 168166, 25086, -67380, 4452, 3006, 342]
    p0_c = [0, 42504, -86846, -530862, -505764, 32148, 10962, 1026]
    p1_c = [0, -7392, 152034, -739372, 746190, 41064, -93474, 55332, 25362, 2592]

    def mul1(A, B):
        C = [0] * (len(A) + len(B) - 1)
        for i, a in enumerate(A):
            for j, b in enumerate(B):
                C[i + j] += a * b
        return C

    p2_c = mul1([0, 0, 1], mul1([-1, 1], [2773, -21731, -72523, 65427, -270837, 74775, 36747, 3033]))
    p3_c = mul1([0, 0, 0, 2], mul1([1, -2, 1], mul1([431, 87], mul1([-1, 11, 1], [-1, 9, -3, 3]))))

    p_inhom = from_x(p_inhom_c)
    p0 = from_x(p0_c)
    p1 = from_x(p1_c)
    p2 = from_x(p2_c)
    p3 = from_x(p3_c)

    Py2 = p_mul(Py, Py)
    Py4 = p_mul(Py2, Py2)
    Py5 = p_mul(Py4, Py)
    Q = p_add(
        p_mul(Py5, p_add(p_inhom, p_mul(p0, {(0, 1): 1}))),
        p_add(
            p_mul(p_mul(Py4, p1), N1),
            p_add(p_mul(p_mul(Py2, p2), N2), p_mul(p3, N3)),
        ),
    )

    Qy = to_y_dict(Q)
    Py_d = to_y_dict(P)
    degP = max(Py_d)
    lcP = Py_d[degP]
    rem = {iy: dict(poly) for iy, poly in Qy.items()}
    for k in range(max(rem), degP - 1, -1):
        if k not in rem or not rem[k]:
            continue
        qk = poly1_div_exact(rem[k], lcP)
        for j, Bp in Py_d.items():
            idx = j + k - degP
            newp = poly1_sub_mul(rem.get(idx, {}), qk, Bp)
            if newp:
                rem[idx] = newp
            elif idx in rem:
                del rem[idx]
    assert not rem, "Q is not divisible by P in Z[x, y]!"

    # 4. Verify [x^n] extraction from the ODE equals Mathar's 9 polynomials identically in Z[n]
    assert len(p_inhom_c) - 1 == 7
    extracted = {j: [0, 0, 0, 0] for j in range(9)}
    for pc, k in [(p0_c, 0), (p1_c, 1), (p2_c, 2), (p3_c, 3)]:
        part = poly_eval_shifts(pc, k, max_j=8)
        for j in range(9):
            for deg in range(4):
                extracted[j][deg] += part[j][deg]

    mathar_coeffs = {
        0: [0, -2895, -5359, 862],  # n*(2n+1)*(431n-2895) = 862n^3 - 5359n^2 - 2895n
        1: [2*26109, -2*64084, 2*68622, -2*9395],
        2: [-2*574587, 2*1044822, -2*508196, 2*59288],
        3: [2*3485484, -2*3607435, 2*1070605, -2*94965],
        4: [-4*1970505, 4*1402336, -4*351474, 4*29036],
        5: [-6*237177, -6*99178, 6*63052, -6*6703],
        6: [-6*127341, 6*74580, -6*14914, 6*1012],
        7: [-6*282762, 6*135199, -6*21429, 6*1127],
        8: mul1([9], mul1([-165, 29], mul1([-15, 2], [-8, 1]))),
    }
    assert extracted[0] == mul1([0, 1], mul1([1, 2], [-2895, 431]))
    for j in range(9):
        assert extracted[j] == mathar_coeffs[j], f"Polynomial mismatch at shift j={j}: {extracted[j]} vs {mathar_coeffs[j]}"

    # Cross-check recurrence directly on y_ser[0..64] for n = 8..64
    for n in range(8, N_ser):
        lhs = sum(
            sum(mathar_coeffs[j][deg] * (n ** deg) for deg in range(4)) * y_ser[n - j]
            for j in range(9)
        )
        assert lhs == 0, f"Recurrence failed at n={n}: lhs={lhs}"

    print("PASS")

if __name__ == "__main__":
    main()
