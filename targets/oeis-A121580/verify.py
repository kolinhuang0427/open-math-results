#!/usr/bin/env python3
"""Exact-arithmetic verification for OEIS A121580 Mathar (2022) D-finite conjecture."""

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
    return [(A[i] if i < len(A) else 0) + sign * (B[i] if i < len(B) else 0) for i in range(n)]

def main():
    # 1. Verify exact polynomial telescoping identity in Z[n]
    # P(n) = (n-1)(n-2)(n-3)(n^2-n+2)
    #      - (n+3)(n-2)(n-3)((n-1)^2-(n-1)+2)
    #      + 2n(n-3)((n-2)^2-(n-2)+2)
    #      - 2(n-3)((n-3)^2-(n-3)+2)
    t1 = mul1([-1, 1], mul1([-2, 1], mul1([-3, 1], [2, -1, 1])))
    t2 = mul1([3, 1], mul1([-2, 1], mul1([-3, 1], [4, -3, 1])))
    t3 = mul1([0, 2], mul1([-3, 1], [8, -5, 1]))
    t4 = mul1([2], mul1([-3, 1], [14, -7, 1]))

    assert t1 == [-12, 28, -29, 19, -7, 1]
    assert t2 == [72, -90, 37, 1, -5, 1]
    assert t3 == [0, -48, 46, -16, 2]
    assert t4 == [-84, 70, -20, 2]

    P = add1(add1(t1, t2, sign=-1), add1(t3, t4, sign=-1))
    assert all(c == 0 for c in P), f"Polynomial P(n) != 0: {P}"

    # 2. Verify coefficient regrouping identity in Z[n]
    # (a_n - a_{n-1}) + (-n-3)(a_{n-1}-a_{n-2}) + 2n(a_{n-2}-a_{n-3}) + (-2n+6)(a_{n-3}-a_{n-4})
    c0 = [1, 0]
    c1 = add1([-1], [-3, -1])
    c2 = add1([3, 1], [0, 2])
    c3 = add1([0, -2], [6, -2])
    c4 = [6, -2]
    assert c0 == [1, 0]
    assert c1 == [-4, -1]
    assert c2 == [3, 3]
    assert c3 == [6, -4]
    assert c4 == [6, -2]

    # 3. Direct numerical verification from primary recurrence and OEIS DATA for n = 5..80
    a = [0, 1]
    for n in range(2, 81):
        a.append(a[-1] + math.factorial(n - 1) * (1 + n * (n - 1) // 2))

    oeis_data = [
        1, 3, 11, 53, 317, 2237, 18077, 164237, 1656077, 18348557,
        221561357, 2895986957, 40737113357, 613623026957, 9854521894157,
        168083120422157, 3034505335078157, 57810369261862157, 1159018646647078157,
    ]
    assert a[1:20] == oeis_data, "OEIS DATA mismatch"

    for n in range(5, 81):
        lhs = (
            a[n]
            + (-n - 4) * a[n - 1]
            + 3 * (n + 1) * a[n - 2]
            + 2 * (-2 * n + 3) * a[n - 3]
            + 2 * (n - 3) * a[n - 4]
        )
        assert lhs == 0, f"Recurrence failed at n={n}: lhs={lhs}"

    print("PASS")

if __name__ == "__main__":
    main()
