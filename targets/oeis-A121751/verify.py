#!/usr/bin/env python3
"""Exact-arithmetic verification for OEIS A121751 Mathar (2022) D-finite conjecture."""

# --- Univariate polynomials in Z[x]: [c_0, c_1, ...] ---

def add1(A, B, sign=1):
    n = max(len(A), len(B))
    res = [(A[i] if i < len(A) else 0) + sign * (B[i] if i < len(B) else 0) for i in range(n)]
    while res and res[-1] == 0:
        res.pop()
    return res

def mul1(A, B):
    if not A or not B:
        return []
    C = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        if a:
            for j, b in enumerate(B):
                C[i + j] += a * b
    while C and C[-1] == 0:
        C.pop()
    return C

def eval1(P, val):
    s = 0
    for c in reversed(P):
        s = s * val + c
    return s

def compose1(P, Q):
    """Return P(Q(k)) in Z[k]."""
    res = []
    q_pow = [1]
    for c in P:
        if c:
            res = add1(res, mul1([c], q_pow))
        q_pow = mul1(q_pow, Q)
    return res

def main():
    # Coefficients C_0(n)..C_6(n) in Z[n]
    C = [
        [256],
        [-384],
        mul1([16], [-67, 40, -8]),
        mul1([16], [87, -54, 8]),
        mul1([4], [-21, -304, 242, -56, 4]),
        mul1([4], [-554, 647, -249, 38, -2]),
        mul1([-4, 1], mul1([-8, 1], [31, -12, 1])),
    ]

    # Step functions over pairs (u_coeff, v_coeff) in Z[k]^2
    def step_even(r_poly, m1, m2):
        # a(2r) = 2*(r-1)*a(2r-1) - r*(r-2)*a(2r-2)
        c1 = mul1([2], add1(r_poly, [-1]))
        c2 = mul1(r_poly, add1(r_poly, [-2]))
        return (
            add1(mul1(c1, m1[0]), mul1(c2, m2[0]), sign=-1),
            add1(mul1(c1, m1[1]), mul1(c2, m2[1]), sign=-1),
        )

    def step_odd(r_poly, m1, m2):
        # a(2r+1) = 2*r*a(2r) - (r*(r-1) - 1)*a(2r-1)
        c1 = mul1([2], r_poly)
        c2 = add1(mul1(r_poly, add1(r_poly, [-1])), [-1])
        return (
            add1(mul1(c1, m1[0]), mul1(c2, m2[0]), sign=-1),
            add1(mul1(c1, m1[1]), mul1(c2, m2[1]), sign=-1),
        )

    # 1. Verify even case n = 2k identically in Z[k]
    v = ([], [1])   # a(2k-6)
    u = ([1], [])   # a(2k-5)
    a4 = step_even([-2, 1], u, v)      # 2k-4
    a3 = step_odd([-2, 1], a4, u)      # 2k-3
    a2 = step_even([-1, 1], a3, a4)    # 2k-2
    a1 = step_odd([-1, 1], a2, a3)     # 2k-1
    a0 = step_even([0, 1], a1, a2)     # 2k
    seq_even = [a0, a1, a2, a3, a4, u, v]
    coeff_u, coeff_v = [], []
    for j in range(7):
        cj = compose1(C[j], [0, 2])
        coeff_u = add1(coeff_u, mul1(cj, seq_even[j][0]))
        coeff_v = add1(coeff_v, mul1(cj, seq_even[j][1]))
    assert coeff_u == [] and coeff_v == [], f"Even case failed: u={coeff_u}, v={coeff_v}"

    # 2. Verify odd case n = 2k+1 identically in Z[k]
    v = ([], [1])   # a(2k-5)
    u = ([1], [])   # a(2k-4)
    a4 = step_odd([-2, 1], u, v)       # 2k-3
    a3 = step_even([-1, 1], a4, u)     # 2k-2
    a2 = step_odd([-1, 1], a3, a4)     # 2k-1
    a1 = step_even([0, 1], a2, a3)     # 2k
    a0 = step_odd([0, 1], a1, a2)      # 2k+1
    seq_odd = [a0, a1, a2, a3, a4, u, v]
    coeff_u, coeff_v = [], []
    for j in range(7):
        cj = compose1(C[j], [1, 2])
        coeff_u = add1(coeff_u, mul1(cj, seq_odd[j][0]))
        coeff_v = add1(coeff_v, mul1(cj, seq_odd[j][1]))
    assert coeff_u == [] and coeff_v == [], f"Odd case failed: u={coeff_u}, v={coeff_v}"

    # 3. Direct numerical verification from primary recurrence and OEIS DATA for n = 7..80
    a = [0, 0, 1]
    for n in range(3, 81):
        f1 = (n - 1) // 2
        f2 = (n - 2) // 2
        a.append(2 * f1 * a[n - 1] - (f1 * f2 - 1) * a[n - 2])

    oeis_data = [
        0, 1, 2, 4, 14, 44, 194, 812, 4362, 22716, 144282, 897636,
        6587454, 47632188, 396765018, 3268365228,
    ]
    assert a[1:17] == oeis_data, "OEIS DATA mismatch"

    for n in range(7, 81):
        lhs = sum(eval1(C[j], n) * a[n - j] for j in range(7))
        assert lhs == 0, f"Recurrence failed at n={n}: lhs={lhs}"

    print("PASS")

if __name__ == "__main__":
    main()
