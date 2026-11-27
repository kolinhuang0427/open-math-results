#!/usr/bin/env python3
"""Exact-arithmetic verification for OEIS A045743 Mathar (2022) D-finite conjecture."""

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

def poly_eval_shifts(poly_x, k, max_j=4):
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

def main():
    # 1. Verify OEIS closed-form a(n) satisfies P(x, y(x)) = 0 via exact truncated series
    N_ser = 50
    a = [0, 0]
    for n in range(2, N_ser):
        num = sum(
            math.comb(n - 2 + i, i) * math.comb(3 * n - 3 - i, n - 2 - 2 * i)
            for i in range((n - 2) // 2 + 1)
        )
        assert num % (n - 1) == 0
        a.append(num // (n - 1))

    oeis_data = [1, 3, 13, 66, 367, 2164, 13293, 84157, 545270, 3598244, 24100375]
    assert a[2:13] == oeis_data, f"Closed-form mismatch with OEIS DATA: {a[2:13]}"

    # Check P(x, y(x)) == 0 mod x^N_ser
    y2 = ser_mul(a, a, N_ser)
    y3 = ser_mul(y2, a, N_ser)
    y4 = ser_mul(y2, y2, N_ser)
    P_val = [0] * N_ser
    P_val[4] += 1  # x^4
    for i in range(N_ser):
        if i >= 3:
            P_val[i] += 4 * a[i - 3]  # 4x^3 y
        if i >= 2:
            P_val[i] += 6 * y2[i - 2] - a[i - 2]  # 6x^2 y^2 - x^2 y
        if i >= 1:
            P_val[i] += 4 * y3[i - 1] - y2[i - 1]  # 4x y^3 - x y^2
        P_val[i] += y4[i] + y3[i]  # y^4 + y^3
    assert all(v == 0 for v in P_val), f"P(x, y(x)) != 0: {P_val}"

    # Verify Py(x, y(x)) = -x^2 + O(x^3) != 0
    assert a[2] == 1  # hence Py(x, y(x)) has [x^2] = -1 != 0

    # 2. Verify Q(x, y) is divisible by P(x, y) in Z[x, y]
    P = {
        (4, 0): 1,
        (3, 1): 4, (2, 1): -1,
        (2, 2): 6, (1, 2): -1,
        (1, 3): 4, (0, 3): 1,
        (0, 4): 1,
    }
    Px = p_dx(P)
    Py = p_dy(P)
    N1 = {k: -v for k, v in Px.items()}

    def next_N(Nk, k):
        t1 = p_mul(Py, p_add(p_mul(Py, p_dx(Nk)), p_mul(N1, p_dy(Nk))))
        t2 = p_mul(Nk, p_add(p_mul(Py, p_dx(Py)), p_mul(N1, p_dy(Py))))
        return p_add(t1, {key: -(2 * k - 1) * v for key, v in t2.items()})

    N2 = next_N(N1, 1)
    N3 = next_N(N2, 2)
    N4 = next_N(N3, 3)

    p_inhom_c = [0, 0, 0, -86483718, -222762936, 52437120]
    p0_c = mul1([0, 0, 0, -72], [3034829 * -1, 225648])
    p1_c = mul1([0, 0, 0, 48], [-2939805, -9108520, 1430912])
    p2_c = mul1([0, 0, 0, 48], [516693, -54421082, -58671498, 31050464])
    p3_c = mul1([0, 0, 0, 1], [2048955, 140653072, -3673122304, -813515264, 1910439936])
    p4_c = mul1([0, 0, 0, 0, 2], mul1([-676909, 753968], [-5, -32, 512, 256]))

    Py2 = p_mul(Py, Py)
    Py4 = p_mul(Py2, Py2)
    Py6 = p_mul(Py4, Py2)
    Py7 = p_mul(Py6, Py)
    Q = p_add(
        p_mul(Py7, p_add(from_x(p_inhom_c), p_mul(from_x(p0_c), {(0, 1): 1}))),
        p_add(
            p_mul(p_mul(Py6, from_x(p1_c)), N1),
            p_add(
                p_mul(p_mul(Py4, from_x(p2_c)), N2),
                p_add(p_mul(p_mul(Py2, from_x(p3_c)), N3), p_mul(from_x(p4_c), N4)),
            ),
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

    # 3. Verify [x^n] extraction matches Mathar's C_0..C_4 identically in Z[n]
    assert len(p_inhom_c) - 1 == 5
    extracted = {j: [0, 0, 0, 0, 0] for j in range(5)}
    for pc, k in [(p0_c, 0), (p1_c, 1), (p2_c, 2), (p3_c, 3), (p4_c, 4)]:
        part = poly_eval_shifts(pc, k, max_j=4)
        for j in range(5):
            for deg in range(5):
                extracted[j][deg] += part[j][deg]

    C0 = mul1([0, 5], mul1([-1, 1], mul1([-2, 1], [-3651663, 1353818])))
    C1 = mul1([16], mul1([-1, 1], mul1([-2, 1], [2014500, -6864025, 2236406])))
    C2 = mul1([-16], mul1([-2, 1], [-506411475, 734160494, -326486432, 46338048]))
    C3 = mul1([8], mul1([-7, 2], [-3030735075, 2071128458, -436441232, 26592864]))
    C4 = mul1([128], mul1([-334675, 94246], mul1([-19, 4], mul1([-9, 2], [-17, 4]))))
    mathar_coeffs = {0: C0, 1: C1, 2: C2, 3: C3, 4: C4}

    for j in range(5):
        assert extracted[j] == mathar_coeffs[j], f"Mismatch at j={j}: {extracted[j]} vs {mathar_coeffs[j]}"

    # 4. Direct numerical check on closed-form a[2..49] for n = 6..49
    for n in range(6, N_ser):
        lhs = sum(
            sum(mathar_coeffs[j][deg] * (n ** deg) for deg in range(5)) * a[n - j]
            for j in range(5)
        )
        assert lhs == 0, f"Recurrence failed at n={n}: lhs={lhs}"

    print("PASS")

if __name__ == "__main__":
    main()
