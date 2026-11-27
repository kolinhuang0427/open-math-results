#!/usr/bin/env python3
"""Exact-arithmetic verification for OEIS A121584 Mathar (2022) D-finite conjecture."""

import math

def mul1(A, B):
    C = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        if a:
            for j, b in enumerate(B):
                C[i + j] += a * b
    return C

def add1(A, B, sign=1):
    n = max(len(A), len(B))
    res = [(A[i] if i < len(A) else 0) + sign * (B[i] if i < len(B) else 0) for i in range(n)]
    while res and res[-1] == 0:
        res.pop()
    return res

def eval1(P, n_val):
    s = 0
    for c in reversed(P):
        s = s * n_val + c
    return s

def main():
    # 1. Define exact integer polynomials in Z[n]
    d0 = mul1([14], mul1([1, -1], [-3, 1]))
    d1 = [13948, -10387, 1675, 14]
    d2 = mul1([7574, 3171, -1703], [-2, 1])
    d3 = mul1([2], mul1([-3433, 1071], mul1([-2, 1], [-3, 1])))
    ds = [d0, d1, d2, d3]

    C = [
        mul1([14], [1, -1]),
        [-6995, 1731, 14],
        mul1([3], [7243, 480, -577]),
        mul1([2], [6004, -11952, 2781]),
        [-54220, 36181, -5987],
        mul1([2], mul1([-3433, 1071], [-4, 1])),
    ]

    # 2. Verify operator identity (n-2)(n-3) * sum_{r=0}^5 C_r(n) a(n-r) == sum_{j=0}^3 d_j(n) B(n-j)
    # where B(n-j) = (n-j-2)a(n-j) - (2n-2j-3)a(n-j-1) + (n-j-1)a(n-j-2)
    n_m2_m3 = mul1([-2, 1], [-3, 1])
    extracted = [[] for _ in range(6)]
    for j in range(4):
        b0 = [-j - 2, 1]
        b1 = [2 * j + 3, -2]
        b2 = [-j - 1, 1]
        extracted[j] = add1(extracted[j], mul1(ds[j], b0))
        extracted[j + 1] = add1(extracted[j + 1], mul1(ds[j], b1))
        extracted[j + 2] = add1(extracted[j + 2], mul1(ds[j], b2))

    for r in range(6):
        lhs = mul1(n_m2_m3, C[r])
        assert add1(lhs, extracted[r], sign=-1) == [], f"Operator mismatch at shift r={r}"

    # 3. Verify P(n) == 0 identically in Z[n]
    # f(k) = 2k^3 - 9k^2 + 17k - 16
    def f_shift(j):
        # f(n - j) as poly in Z[n]
        u = [-j, 1]
        u2 = mul1(u, u)
        u3 = mul1(u2, u)
        res = [-16]
        res = add1(res, mul1([17], u))
        res = add1(res, mul1([-9], u2))
        res = add1(res, mul1([2], u3))
        return res

    P = []
    # j=0: d0 * (n-1)(n-2)(n-3) * f(n)
    P = add1(P, mul1(d0, mul1([-1, 1], mul1([-2, 1], mul1([-3, 1], f_shift(0))))))
    # j=1: d1 * (n-2)(n-3) * f(n-1)
    P = add1(P, mul1(d1, mul1([-2, 1], mul1([-3, 1], f_shift(1)))))
    # j=2: d2 * (n-3) * f(n-2)
    P = add1(P, mul1(d2, mul1([-3, 1], f_shift(2))))
    # j=3: d3 * f(n-3)
    P = add1(P, mul1(d3, f_shift(3)))
    assert P == [], f"P(n) != 0: {P}"

    # 4. Direct numerical check from primary recurrence and OEIS DATA for n = 6..60
    a = [0, 1, 4]
    for n in range(3, 61):
        num = (2 * n - 3) * a[n - 1] - (n - 1) * a[n - 2] + (2 * n ** 3 - 9 * n ** 2 + 17 * n - 16) * math.factorial(n - 1) // 2
        assert num % (n - 2) == 0
        a.append(num // (n - 2))

    oeis_data = [
        1, 4, 18, 93, 569, 4074, 33336, 306035, 3111771, 34708944,
        421407314, 5533007841, 78125977725, 1180594364966,
    ]
    assert a[1:15] == oeis_data, "OEIS DATA mismatch"

    for n in range(6, 61):
        lhs = sum(eval1(C[r], n) * a[n - r] for r in range(6))
        assert lhs == 0, f"Recurrence failed at n={n}: lhs={lhs}"

    print("PASS")

if __name__ == "__main__":
    main()
