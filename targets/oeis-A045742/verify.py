#!/usr/bin/env python3
"""Exact-arithmetic verification for OEIS A045742 Mathar (2022) D-finite conjecture."""

import math

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

# --- Univariate polynomials / series ---

def mul1(A, B):
    C = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        if a:
            for j, b in enumerate(B):
                C[i + j] += a * b
    return C

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

def poly_eval_shifts(poly_x, k, max_j=3):
    res = {j: [0, 0, 0, 0] for j in range(max_j + 1)}
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

def main():
    # 1. Verify Lagrange-Bürmann formula vs OEIS closed form and DATA for n = 2..45
    N_ser = 46
    a = [0, 0, 0]
    for n in range(3, N_ser):
        num = sum(
            k * math.comb(n + k - 2, k) * math.comb(3 * n - 3, n - 2 - k)
            for k in range(1, n - 1)
        )
        assert num % (n - 1) == 0
        a.append(num // (n - 1))

    oeis_data = [
        0, 1, 13, 141, 1456, 14778, 149031, 1499773,
        15089932, 151927854, 1531242362, 15451614738,
    ]
    assert a[2:14] == oeis_data, f"OEIS DATA mismatch: {a[2:14]}"

    # t = x*(1+t)^3 + t^2
    t_ser = [0] * N_ser
    for _ in range(N_ser):
        tp1 = [1 + t_ser[0]] + t_ser[1:]
        tp1_3 = ser_mul(tp1, ser_mul(tp1, tp1, N_ser), N_ser)
        t2 = ser_mul(t_ser, t_ser, N_ser)
        t_ser = [0] + [tp1_3[i - 1] + t2[i] for i in range(1, N_ser)]

    t2 = ser_mul(t_ser, t_ser, N_ser)
    tp1 = [1 + t_ser[0]] + t_ser[1:]
    num_y = [0] + ser_mul(t2, tp1, N_ser - 1)
    den_y = [1 - 4 * t_ser[i] + t2[i] if i == 0 else -4 * t_ser[i] + t2[i] for i in range(N_ser)]
    y_gf = ser_mul(num_y, ser_inv(den_y, N_ser), N_ser)
    assert y_gf == a, "Lagrange-Bürmann GF mismatch with closed form"

    # 2. Verify 6x6 Sylvester resultant Res_t(E1, E2) == ±2x * P(x, y)
    # E1(t) = x*t^3 + (3x+1)*t^2 + (3x-1)*t + x
    a3 = {(1, 0): 1}
    a2 = {(1, 0): 3, (0, 0): 1}
    a1 = {(1, 0): 3, (0, 0): -1}
    a0 = {(1, 0): 1}
    # E2(t) = -x*t^3 + (y-x)*t^2 - 4*y*t + y
    b3 = {(1, 0): -1}
    b2 = {(0, 1): 1, (1, 0): -1}
    b1 = {(0, 1): -4}
    b0 = {(0, 1): 1}
    Z = {}
    Syl = [
        [a3, a2, a1, a0, Z,  Z],
        [Z,  a3, a2, a1, a0, Z],
        [Z,  Z,  a3, a2, a1, a0],
        [b3, b2, b1, b0, Z,  Z],
        [Z,  b3, b2, b1, b0, Z],
        [Z,  Z,  b3, b2, b1, b0],
    ]
    res = det_poly(Syl)
    P = {
        (4, 0): 1,
        (3, 1): -27,
        (2, 3): 108, (2, 2): 108, (2, 1): 13,
        (1, 1): -1,
        (0, 3): -1, (0, 2): -1,
    }
    two_x_P = p_mul({(1, 0): 2}, P)
    assert res == two_x_P or res == {k: -v for k, v in two_x_P.items()}, "Resultant mismatch!"

    # 3. Verify Q(x, y) divisible by P(x, y) in Z[x, y]
    Px = p_dx(P)
    Py = p_dy(P)
    assert a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 1  # hence Py(x, y(x)) = -x + O(x^2) != 0

    N1 = {k: -v for k, v in Px.items()}

    def next_N(Nk, k):
        t1 = p_mul(Py, p_add(p_mul(Py, p_dx(Nk)), p_mul(N1, p_dy(Nk))))
        t2 = p_mul(Nk, p_add(p_mul(Py, p_dx(Py)), p_mul(N1, p_dy(Py))))
        return p_add(t1, {key: -(2 * k - 1) * v for key, v in t2.items()})

    N2 = next_N(N1, 1)
    N3 = next_N(N2, 2)

    p_inhom_c = [0, 0, 0, 2544]
    p0_c = [0, 0, 0, 7632]
    p1_c = [0, 0, -22728, 62256, 109296]
    p2_c = [0, 0, -947, 13344, -180144, 1018008]
    p3_c = [0, 0, 0, 523, -4554, -56484, 491832]

    Py2 = p_mul(Py, Py)
    Py4 = p_mul(Py2, Py2)
    Py5 = p_mul(Py4, Py)
    Q = p_add(
        p_mul(Py5, p_add(from_x(p_inhom_c), p_mul(from_x(p0_c), {(0, 1): 1}))),
        p_add(
            p_mul(p_mul(Py4, from_x(p1_c)), N1),
            p_add(p_mul(p_mul(Py2, from_x(p2_c)), N2), p_mul(from_x(p3_c), N3)),
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

    # 4. Verify [x^n] extraction matches Mathar's C_0..C_3 identically in Z[n]
    extracted = {j: [0, 0, 0, 0] for j in range(4)}
    for k, pc in enumerate((p0_c, p1_c, p2_c, p3_c)):
        part = poly_eval_shifts(pc, k, max_j=3)
        for j in range(4):
            for deg in range(4):
                extracted[j][deg] += part[j][deg]

    C0 = mul1([0, 1], mul1([-1, 1], [-1993, 523]))
    C1 = mul1([-6], mul1([-1, 1], [12790, -6019, 759]))
    C2 = mul1([-12], mul1([-2, 1], [6260, -17937, 4707]))
    C3 = mul1([72], mul1([-10, 3], mul1([-2224, 759], [-11, 3])))
    mathar_coeffs = {0: C0, 1: C1, 2: C2, 3: C3}

    for j in range(4):
        assert extracted[j] == mathar_coeffs[j], f"Mismatch at j={j}: {extracted[j]} vs {mathar_coeffs[j]}"

    # 5. Direct numerical check on a[2..N_ser-1] for n = 5..N_ser-1
    for n in range(5, N_ser):
        lhs = sum(
            sum(mathar_coeffs[j][deg] * (n ** deg) for deg in range(4)) * a[n - j]
            for j in range(4)
        )
        assert lhs == 0, f"Recurrence failed at n={n}: lhs={lhs}"

    print("PASS")

if __name__ == "__main__":
    main()
