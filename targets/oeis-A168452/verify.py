#!/usr/bin/env python3
"""Exact-arithmetic verification for OEIS A168452 Mathar (2024) D-finite conjecture."""

import math

# --- Sparse polynomials in Z[x, B, Bp]: {(dx, dB, dBp): coeff} ---

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
    for (ax, aB, aBp), av in A.items():
        for (bx, bB, bBp), bv in B.items():
            k = (ax + bx, aB + bB, aBp + bBp)
            C[k] = C.get(k, 0) + av * bv
    return {k: v for k, v in C.items() if v}

def p_dx(A):
    return {(ix - 1, iB, iBp): ix * v for (ix, iB, iBp), v in A.items() if ix > 0}

def p_dB(A):
    return {(ix, iB - 1, iBp): iB * v for (ix, iB, iBp), v in A.items() if iB > 0}

def p_dBp(A):
    return {(ix, iB, iBp - 1): iBp * v for (ix, iB, iBp), v in A.items() if iBp > 0}

def from_x(coeffs):
    return {(i, 0, 0): c for i, c in enumerate(coeffs) if c}

def mul1(A, B):
    C = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        if a:
            for j, b in enumerate(B):
                C[i + j] += a * b
    return C

def poly_eval_shifts(poly_x, k, max_j=4):
    res = {j: [0, 0, 0, 0, 0, 0] for j in range(max_j + 1)}
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
    # 1. Verify B(x) ODE on Catalan-product b(n) = C(n)*C(n+1) through x^40
    N = 45
    cat = [math.comb(2 * k, k) // (k + 1) for k in range(N + 2)]
    b = [cat[k] * cat[k + 1] for k in range(N)]
    for n in range(1, N):
        assert (n + 1) * (n + 2) * b[n] == 4 * (2 * n - 1) * (2 * n + 1) * b[n - 1]

    a = [sum(b[k] * b[n - k] for k in range(n + 1)) for n in range(N)]
    oeis_data = [1, 4, 24, 180, 1556, 14840, 152092, 1646652, 18613664, 217852008]
    assert a[:10] == oeis_data, f"Self-convolution mismatch: {a[:10]}"

    # Check (x^2(16x-1)) B'' == -2 + 2(1-6x)B + 4x(1-12x)B' on b[0..N-1]
    b1 = [n * b[n] for n in range(1, N)] + [0]
    b2 = [n * b1[n] for n in range(1, N)] + [0]
    for n in range(N - 2):
        lhs = (16 * b2[n - 3] if n >= 3 else 0) - (b2[n - 2] if n >= 2 else 0)
        rhs = (-2 if n == 0 else 0) + 2 * b[n] - (12 * b[n - 1] if n >= 1 else 0) + (4 * b1[n - 1] if n >= 1 else 0) - (48 * b1[n - 2] if n >= 2 else 0)
        assert lhs == rhs, f"B ODE mismatch at x^{n}: {lhs} != {rhs}"

    # 2. Verify M_0..M_5 and differentiation consistency in Z[x, B, Bp]
    delta = from_x([0, 0, -1, 16])  # x^2*(16x - 1)
    B_var = {(0, 1, 0): 1}
    Bp_var = {(0, 0, 1): 1}
    # delta * B'' = -2 + 2(1-6x)B + 4x(1-12x)B'
    delta_B2 = p_add(
        from_x([-2]),
        p_add(
            p_mul(from_x([2, -12]), B_var),
            p_mul(from_x([0, 4, -48]), Bp_var),
        ),
    )

    def delta_diff(E):
        # Returns delta * dE/dx in Z[x, B, Bp]
        return p_add(
            p_mul(delta, p_add(p_dx(E), p_mul(p_dB(E), Bp_var))),
            p_mul(p_dBp(E), delta_B2),
        )

    D_c = [
        [1],
        [1],
        [0, 0, -1, 16],
        [0, 0, 0, -1, 16],
        mul1([0, 0, 0, 0, 1], mul1([-1, 16], [-1, 16])),
        mul1([0, 0, 0, 0, 0, 1], mul1([-1, 16], mul1([-1, 16], [-1, 16]))),
    ]
    D = [from_x(d) for d in D_c]

    M = [
        {(0, 2, 0): 1},  # B^2
        {(0, 1, 1): 2},  # 2*B*B'
        p_add(
            p_mul(from_x([4, -24]), {(0, 2, 0): 1}),
            p_add(
                p_mul(from_x([0, 8, -96]), {(0, 1, 1): 1}),
                p_add({(0, 1, 0): -4}, p_mul(from_x([0, 0, -2, 32]), {(0, 0, 2): 1})),
            ),
        ),
        p_add(
            p_mul(from_x([-24, 120]), {(0, 2, 0): 1}),
            p_add(
                p_mul(from_x([0, -24, 288]), {(0, 1, 1): 1}),
                p_add(
                    {(0, 1, 0): 24},
                    p_add(
                        p_mul(from_x([0, 0, 24, -288]), {(0, 0, 2): 1}),
                        {(1, 0, 1): -12},
                    ),
                ),
            ),
        ),
        p_add(
            p_mul(from_x([-120, 2640, -9216]), {(0, 2, 0): 1}),
            p_add(
                p_mul(from_x([0, 0, 1008, -12288]), {(0, 1, 1): 1}),
                p_add(
                    p_mul(from_x([96, -1968]), {(0, 1, 0): 1}),
                    p_add(
                        p_mul(from_x([0, 0, 240, -6048, 36864]), {(0, 0, 2): 1}),
                        p_add(p_mul(from_x([0, -192, 2688]), {(0, 0, 1): 1}), {(0, 0, 0): 24}),
                    ),
                ),
            ),
        ),
        p_add(
            p_mul(from_x([-480, 21456, -266304, 737280]), {(0, 2, 0): 1}),
            p_add(
                p_mul(from_x([0, 1200, -33024, 221184]), {(0, 1, 1): 1}),
                p_add(
                    p_mul(from_x([0, -9456, 149760]), {(0, 1, 0): 1}),
                    p_add(
                        p_mul(from_x([0, 0, 2400, -93840, 1194240, -4915200]), {(0, 0, 2): 1}),
                        p_add(
                            p_mul(from_x([0, -2400, 68400, -480000]), {(0, 0, 1): 1}),
                            from_x([480, -7680]),
                        ),
                    ),
                ),
            ),
        ),
    ]

    # Verify D[k+1]*y^(k+1) = M[k+1] recursively via:
    # delta * D[k+1] * M[k]' == delta * D[k]' * M[k] + D[k] * M[k+1] * ... wait:
    # From D_k y^(k) = M_k, differentiating gives D_k y^(k+1) + D_k' y^(k) = M_k'.
    # Multiply by delta * D_k * D_{k+1}:
    # D_k^2 * delta * M_{k+1} == D_{k+1} * (D_k * (delta * M_k') - (delta * D_k') * M_k).
    for k in range(5):
        lhs = p_mul(p_mul(D[k], D[k]), p_mul(delta, M[k + 1]))
        rhs = p_mul(
            D[k + 1],
            p_add(
                p_mul(D[k], delta_diff(M[k])),
                p_mul(p_mul(delta, p_dx(D[k])), M[k]),
                sign=-1,
            ),
        )
        assert lhs == rhs, f"Derivative relation M[{k+1}] failed!"

    # 3. Verify sum q_k(x) * M_k(x, B, Bp) == 72 - 1152*x identically in Z[x, B, Bp]
    q_c = [
        mul1([-24], [-3, 168, -2572, 8640, 61440]),
        mul1([-24], [0, -27, 1285, -18056, 39552, 512000]),
        mul1([-24], [39, -1121, 4968, 46720]),
        mul1([-12], mul1([-1, 16], [-34, 391, 2640])),
        mul1([-1], mul1([-1, 16], [63, 320])),
        mul1([-1], [3, 16]),
    ]
    D_c = [
        [1],
        [1],
        [0, 0, -1, 16],
        [0, 0, 0, -1, 16],
        mul1([0, 0, 0, 0, 1], mul1([-1, 16], [-1, 16])),
        mul1([0, 0, 0, 0, 0, 1], mul1([-1, 16], mul1([-1, 16], [-1, 16]))),
    ]
    p_c = [mul1(q_c[k], D_c[k]) for k in range(6)]
    for k in range(6):
        assert from_x(D_c[k]) == D[k]

    total = {}
    for k in range(6):
        total = p_add(total, p_mul(from_x(q_c[k]), M[k]))
    assert total == from_x([72, -1152]), f"ODE reduction mismatch: {total}"

    # 4. Verify [x^n] extraction matches Mathar's C_0..C_4 identically in Z[n]
    extracted = {j: [0, 0, 0, 0, 0, 0] for j in range(5)}
    for k in range(6):
        part = poly_eval_shifts(p_c[k], k, max_j=4)
        for j in range(5):
            for deg in range(6):
                extracted[j][deg] += part[j][deg]

    C0 = mul1([3], mul1([4, 1], mul1([3, 1], mul1([2, 1], mul1([1, 1], [1, 1])))))
    C1 = mul1([0, -4], mul1([1, 1], [75, 233, 164, 32]))
    C2 = mul1([96], [3, -16, -28, -14, 24, 16])
    C3 = mul1([1536], [15, -32, 0, 22, -8, 0])
    C4 = mul1([-16384], mul1([-5, 2], mul1([-1, 1], mul1([-2, 1], mul1([-3, 1], [-3, 2])))))
    mathar_coeffs = {0: C0, 1: C1, 2: C2, 3: C3, 4: C4}

    for j in range(5):
        assert extracted[j] == mathar_coeffs[j], f"Polynomial mismatch at j={j}: {extracted[j]} vs {mathar_coeffs[j]}"

    # 5. Direct numerical check on a[0..N-1] for n = 4..N-1
    for n in range(4, N):
        lhs = sum(
            sum(mathar_coeffs[j][deg] * (n ** deg) for deg in range(6)) * a[n - j]
            for j in range(5)
        )
        assert lhs == 0, f"Recurrence failed at n={n}: lhs={lhs}"

    print("PASS")

if __name__ == "__main__":
    main()
