#!/usr/bin/env python3
"""Exact-arithmetic verification for OEIS A119366 Mathar (2025) D-finite conjecture."""

import math

# --- Elements of Z[w]/(w^2 + w + 1) represented as (c0, c1) = c0 + c1*w ---

def w_add(a, b, sign=1):
    return (a[0] + sign * b[0], a[1] + sign * b[1])

def w_mul(a, b):
    a0, a1 = a
    b0, b1 = b
    return (a0 * b0 - a1 * b1, a0 * b1 + a1 * b0 - a1 * b1)

def w_scale(k, a):
    return (k * a[0], k * a[1])

# --- Univariate polynomials over Z[w]/(w^2 + w + 1) as lists [c_0, c_1, ...] ---

def pw_trim(P):
    p = list(P)
    while p and p[-1] == (0, 0):
        p.pop()
    return p

def pw_add(A, B, sign=1):
    n = max(len(A), len(B))
    res = []
    for i in range(n):
        ai = A[i] if i < len(A) else (0, 0)
        bi = B[i] if i < len(B) else (0, 0)
        res.append(w_add(ai, bi, sign))
    return pw_trim(res)

def pw_mul(A, B):
    if not A or not B:
        return []
    res = [(0, 0)] * (len(A) + len(B) - 1)
    for i, ai in enumerate(A):
        if ai == (0, 0):
            continue
        for j, bj in enumerate(B):
            res[i + j] = w_add(res[i + j], w_mul(ai, bj))
    return pw_trim(res)

def pw_diff(A):
    return pw_trim([w_scale(i, A[i]) for i in range(1, len(A))])

def pw_from_z(coeffs):
    return pw_trim([(c, 0) for c in coeffs])

# --- Integer univariate polynomials ---

def mul1(A, B):
    C = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        if a:
            for j, b in enumerate(B):
                C[i + j] += a * b
    return C

def poly_eval_shifts(poly_x, k, max_j=7):
    res = {j: [0, 0, 0, 0, 0] for j in range(max_j + 1)}
    for d, c in enumerate(poly_x):
        if c == 0:
            continue
        j = d - k
        assert 0 <= j <= max_j, f"Shift out of range: d={d}, k={k}, j={j}"
        poly_n = [1]
        for i in range(k):
            poly_n = mul1(poly_n, [-(j + i), 1])
        for deg, val in enumerate(poly_n):
            res[j][deg] += c * val
    return res

def verify_sqrt_annihilator(D, ps_pw):
    # Verify sum_{k=0}^4 p_k * N_k * (2x D)^{4-k} == 0 over Z[w]/(w^2 + w + 1)[x]
    Dp = pw_diff(D)
    x_poly = [(0, 0), (1, 0)]
    two_x_D = pw_mul(pw_from_z([0, 2]), D)
    N = [pw_from_z([1])]
    for k in range(4):
        Nk = N[-1]
        term1 = pw_mul(two_x_D, pw_diff(Nk))
        coeff = pw_add(pw_mul(pw_from_z([2 * (k + 1)]), D), pw_mul(pw_from_z([0, 2 * k - 1]), Dp))
        term2 = pw_mul(coeff, Nk)
        N.append(pw_add(term1, term2, sign=-1))

    tot = []
    pow_2xD = pw_from_z([1])
    powers = [pow_2xD]
    for _ in range(4):
        pow_2xD = pw_mul(pow_2xD, two_x_D)
        powers.append(pow_2xD)
    for k in range(5):
        tot = pw_add(tot, pw_mul(pw_mul(ps_pw[k], N[k]), powers[4 - k]))
    assert tot == [], f"Annihilator check failed: {tot}"

def main():
    # 1. Verify Step 1 generating function u_j(x) vs Barry's closed form for n = 0..35
    N_ser = 36
    a = [0]
    for n in range(1, N_ser):
        num = sum(math.comb(n, 3 * k + 1) * math.comb(n, 3 * k) for k in range(n // 3 + 1))
        assert num % n == 0
        a.append(num // n)

    oeis_data = [0, 1, 1, 1, 2, 11, 51, 177, 519, 1513, 5042, 18866, 71270, 257974, 905425]
    assert a[:15] == oeis_data, f"Closed-form vs OEIS DATA mismatch: {a[:15]}"

    def solve_u(w_val):
        u = [(0, 0)] * N_ser
        one_plus_w = w_add((1, 0), w_val)
        for _ in range(N_ser):
            u2 = [(0, 0)] * N_ser
            for i in range(N_ser):
                if u[i] == (0, 0):
                    continue
                for j in range(N_ser - i):
                    u2[i + j] = w_add(u2[i + j], w_mul(u[i], u[j]))
            nxt = [(0, 0)] * N_ser
            nxt[1] = w_val
            for i in range(1, N_ser):
                nxt[i] = w_add(nxt[i], w_add(w_mul(one_plus_w, u[i - 1]), u2[i - 1]))
            u = nxt
        return u

    u0 = solve_u((1, 0))
    u1 = solve_u((0, 1))
    u2 = solve_u((-1, -1))
    for i in range(N_ser):
        s = w_add(u0[i], w_add(w_mul((-1, -1), u1[i]), w_mul((0, 1), u2[i])))
        assert s[1] == 0 and s[0] == 3 * a[i], f"Step 1 GF mismatch at x^{i}: {s} vs {3*a[i]}"

    # 2. Verify L(S_j(x)/x) = 0 identically in Z[x] and Z[w][x]
    p0_c = mul1([0, 12], [-1233, -2253, 9541, -453, 9216])
    p1_c = mul1([0, 6], [1233, 4719, -12783, -15265, 43362, -153168, -513666, 179010])
    p2_c = mul1([0, 0, 9], [-822, 1550, 8342, -12395, -117585, -237531, -519261, 232380])
    p3_c = mul1([0, 0, 0, 1], [-175, -9879, -1287, 173836, -871557, -664443, -1378881, 774306])
    p4_c = mul1([0, 0, 0, 0, 1], mul1([-1, 4], mul1([1, 1, 1], mul1([1, -3, 9], [-881, -3450, 1779]))))

    ps_pw = [pw_from_z(pc) for pc in (p0_c, p1_c, p2_c, p3_c, p4_c)]
    Delta0 = pw_from_z([1, -4])
    Delta1 = [(1, 0), (-2, -2), (0, -3)]  # 1 + 2*w^2*x - 3*w*x^2 since w^2 = -1 - w
    Delta2 = [(1, 0), (0, 2), (3, 3)]    # 1 + 2*w*x - 3*w^2*x^2
    verify_sqrt_annihilator(Delta0, ps_pw)
    verify_sqrt_annihilator(Delta1, ps_pw)
    verify_sqrt_annihilator(Delta2, ps_pw)

    # 3. Verify [x^n] extraction matches Mathar's C_0..C_7 identically in Z[n]
    assert len(p0_c) - 1 == 5
    extracted = {j: [0, 0, 0, 0, 0] for j in range(8)}
    for k, pc in enumerate((p0_c, p1_c, p2_c, p3_c, p4_c)):
        part = poly_eval_shifts(pc, k, max_j=7)
        for j in range(8):
            for deg in range(5):
                extracted[j][deg] += part[j][deg]

    C0 = mul1([0, 1], mul1([-4580, 881], mul1([-2, 1], [1, 1])))
    C1 = mul1([0, -3], [10135, -2988, -2827, 612])
    C2 = mul1([3], [-167988, 313702, -190361, 42803, -3088])
    C3 = [4115562, -5860777, 2924411, -600920, 43042]
    C4 = mul1([3], [-4965528, 6389913, -2904370, 558681, -38600])
    C5 = mul1([3], [1878084, -415064, -434711, 162695, -14776])
    C6 = mul1([-9], mul1([-6, 1], [-173519, 290611, -106831, 10835]))
    C7 = mul1([54], mul1([-6, 1], mul1([-7, 1], mul1([-1429, 593], [-13, 2]))))
    mathar_coeffs = {0: C0, 1: C1, 2: C2, 3: C3, 4: C4, 5: C5, 6: C6, 7: C7}

    for j in range(8):
        assert extracted[j] == mathar_coeffs[j], f"Mismatch at j={j}: {extracted[j]} vs {mathar_coeffs[j]}"

    # 4. Direct numerical check on a[0..N_ser-1] for n = 7..N_ser-1
    for n in range(7, N_ser):
        lhs = sum(
            sum(mathar_coeffs[j][deg] * (n ** deg) for deg in range(5)) * a[n - j]
            for j in range(8)
        )
        assert lhs == 0, f"Recurrence failed at n={n}: lhs={lhs}"

    print("PASS")

if __name__ == "__main__":
    main()
