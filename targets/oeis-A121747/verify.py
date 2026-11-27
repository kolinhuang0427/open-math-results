#!/usr/bin/env python3
"""Exact-arithmetic verification for OEIS A121747 Mathar (2022) D-finite conjecture."""

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
    c = [
        [38, -9],
        [43, -10],
        [3, 86, -56, 9],
        mul1([-3, 1], mul1([-4, 1], [-15, 19])),
    ]
    C = [
        [38, -9],
        mul1([3], [27, -19, 3]),
        [127, -24, -37, 9],
        [-85, 525, -392, 102, -9],
        mul1([-1], mul1([-3, 1], [-237, 510, -223, 28])),
        mul1([-1], mul1([-15, 19], mul1([-3, 1], mul1([-4, 1], [-4, 1])))),
    ]

    # 1. Verify M(n) == sum_{i=0}^3 c_i(n) * W(n-i) identically in Z[n]
    # W(n-i) = a(n-i) - (n-i-1)*a(n-i-1) - (n-i-1)*a(n-i-2)
    extracted = [[] for _ in range(6)]
    for i in range(4):
        extracted[i] = add1(extracted[i], c[i])
        extracted[i + 1] = add1(extracted[i + 1], mul1(c[i], [i + 1, -1]))
        extracted[i + 2] = add1(extracted[i + 2], mul1(c[i], [i + 1, -1]))
    for j in range(6):
        assert add1(extracted[j], C[j], sign=-1) == [], f"Operator mismatch at shift j={j}"

    # 2. Verify P_even(r) == 0 and P_odd(r) == 0 identically in Z[r]
    # W(2m) = (2m-2)! (2m^2 - 1), W(2m+1) = (2m-1)! (2m^2 + m - 1)
    def w_even_poly(m_poly):
        return add1(mul1([2], mul1(m_poly, m_poly)), [-1])

    def w_odd_poly(m_poly):
        return add1(mul1([2], mul1(m_poly, m_poly)), add1(m_poly, [-1]))

    r_p = [0, 1]
    rm1 = [-1, 1]
    rm2 = [-2, 1]
    two_r = [0, 2]
    f_even = [
        mul1([-2, 2], mul1([-3, 2], [-4, 2])),
        mul1([-3, 2], [-4, 2]),
        [-4, 2],
        [1],
    ]
    w_ev = [w_even_poly(r_p), w_odd_poly(rm1), w_even_poly(rm1), w_odd_poly(rm2)]
    P_even = []
    for i in range(4):
        P_even = add1(P_even, mul1(compose1(c[i], two_r), mul1(f_even[i], w_ev[i])))
    assert P_even == [], f"P_even != 0: {P_even}"

    two_rp1 = [1, 2]
    f_odd = [
        mul1([-1, 2], mul1([-2, 2], [-3, 2])),
        mul1([-2, 2], [-3, 2]),
        [-3, 2],
        [1],
    ]
    w_od = [w_odd_poly(r_p), w_even_poly(r_p), w_odd_poly(rm1), w_even_poly(rm1)]
    P_odd = []
    for i in range(4):
        P_odd = add1(P_odd, mul1(compose1(c[i], two_rp1), mul1(f_odd[i], w_od[i])))
    assert P_odd == [], f"P_odd != 0: {P_odd}"

    # 3. Direct numerical verification from primary recurrence and OEIS DATA for n = 6..60
    d = [0, 1, 0]
    for k in range(3, 62):
        d.append(-d[k - 1] if k % 2 == 1 else d[k - 2] + math.factorial(k - 1))
    a = [0, 1]
    for n in range(2, 61):
        a.append(n * a[n - 1] - d[n - 1] + math.factorial(n - 1) * (n // 2))

    oeis_data = [
        1, 2, 8, 44, 262, 1938, 15600, 145086, 1461888, 16438446,
        198598860, 2623055166, 36933441912, 560697617214,
    ]
    assert a[1:15] == oeis_data, "OEIS DATA mismatch"

    for n in range(6, 61):
        lhs = sum(eval1(C[j], n) * a[n - j] for j in range(6))
        assert lhs == 0, f"Recurrence failed at n={n}: lhs={lhs}"

    print("PASS")

if __name__ == "__main__":
    main()
