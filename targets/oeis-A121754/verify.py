#!/usr/bin/env python3
"""Exact-arithmetic verification for OEIS A121754 Mathar (2022) D-finite conjecture."""

import math

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
    res = []
    q_pow = [1]
    for c in P:
        if c:
            res = add1(res, mul1([c], q_pow))
        q_pow = mul1(q_pow, Q)
    return res

def main():
    e = [
        [16, 16],
        mul1([-9], [-59, 18]),
        [-1041, 300, 16, -16],
        [-1541, 2581, -1171, 146],
        mul1([-1], mul1([-6, 1], mul1([-4, 1], [-311, 130]))),
    ]
    C = [
        [16, 16],
        [531, -178, -16],
        [-510, -393, 178, -16],
        [-3623, 4222, -1439, 98, 16],
        [2841, 3054, -4483, 1479, -146],
        mul1([-311, 130], mul1([-6, 1], mul1([-4, 1], [-4, 1]))),
    ]

    # 1. Verify M(n) == sum_{i=0}^4 e_i(n) * (a(n-i) - (n-i)*a(n-i-1)) in Z[n]
    extracted = [[] for _ in range(6)]
    for i in range(5):
        extracted[i] = add1(extracted[i], e[i])
        extracted[i + 1] = add1(extracted[i + 1], mul1(e[i], [i, -1]))
    for j in range(6):
        assert add1(extracted[j], C[j], sign=-1) == [], f"Operator mismatch at shift j={j}"

    # 2. Verify P_even(r) == 0 and P_odd(r) == 0 identically in Z[r]
    # S(2r) = (r-1)^2 (4r-1), S(2r+1) = r^2 (4r-1)
    def S_even(r_poly):
        rm1 = add1(r_poly, [-1])
        return mul1(mul1(rm1, rm1), add1(mul1([4], r_poly), [-1]))

    def S_odd(r_poly):
        return mul1(mul1(r_poly, r_poly), add1(mul1([4], r_poly), [-1]))

    # Even case n = 2r
    r_p = [0, 1]
    rm1 = [-1, 1]
    rm2 = [-2, 1]
    two_r = [0, 2]
    f_even = [
        mul1([-3, 2], mul1([-4, 2], mul1([-5, 2], [-6, 2]))),
        mul1([-4, 2], mul1([-5, 2], [-6, 2])),
        mul1([-5, 2], [-6, 2]),
        [-6, 2],
        [1],
    ]
    S_ev_list = [S_even(r_p), S_odd(rm1), S_even(rm1), S_odd(rm2), S_even(rm2)]
    P_even = []
    for i in range(5):
        P_even = add1(P_even, mul1(compose1(e[i], two_r), mul1(f_even[i], S_ev_list[i])))
    assert P_even == [], f"P_even != 0: {P_even}"

    # Odd case n = 2r+1
    two_rp1 = [1, 2]
    f_odd = [
        mul1([-2, 2], mul1([-3, 2], mul1([-4, 2], [-5, 2]))),
        mul1([-3, 2], mul1([-4, 2], [-5, 2])),
        mul1([-4, 2], [-5, 2]),
        [-5, 2],
        [1],
    ]
    S_od_list = [S_odd(r_p), S_even(r_p), S_odd(rm1), S_even(rm1), S_odd(rm2)]
    P_odd = []
    for i in range(5):
        P_odd = add1(P_odd, mul1(compose1(e[i], two_rp1), mul1(f_odd[i], S_od_list[i])))
    assert P_odd == [], f"P_odd != 0: {P_odd}"

    # 3. Direct numerical check from primary recurrence and OEIS DATA for n = 6..60
    a = [0, 0, 1]
    for n in range(3, 61):
        f = (n - 2) + ((1 + (-1) ** (n - 1)) // 2) * (n - 1)
        a.append((2 * n - 3) * a[n - 1] - (n - 1) * (n - 3) * a[n - 2] + math.factorial(n - 2) * f)

    oeis_data = [
        0, 1, 6, 31, 211, 1530, 13086, 120888, 1260792, 14140080,
        174692880, 2304970560, 32969263680, 500368821120,
    ]
    assert a[1:15] == oeis_data, "OEIS DATA mismatch"

    for n in range(6, 61):
        lhs = sum(eval1(C[j], n) * a[n - j] for j in range(6))
        assert lhs == 0, f"Recurrence failed at n={n}: lhs={lhs}"

    print("PASS")

if __name__ == "__main__":
    main()
