#!/usr/bin/env python3
"""Exact-arithmetic verification for OEIS A119262 Irwin (2017) determinant conjecture."""

import math


def bareiss_det(mat):
    """Exact integer determinant using Bareiss fraction-free Gaussian elimination."""
    n = len(mat)
    A = [list(row) for row in mat]
    sign = 1
    prev_pivot = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            swap = -1
            for r in range(k + 1, n):
                if A[r][k] != 0:
                    swap = r
                    break
            if swap == -1:
                return 0
            A[k], A[swap] = A[swap], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = A[i][j] * pivot - A[i][k] * A[k][j]
                assert num % prev_pivot == 0
                A[i][j] = num // prev_pivot
            A[i][k] = 0
        prev_pivot = pivot
    return sign * A[n - 1][n - 1]


def build_M(n):
    M = [[0] * n for _ in range(n)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i < j - 1:
                M[i - 1][j - 1] = 0
            elif i == j - 1:
                M[i - 1][j - 1] = -1
            else:
                u, v = i - j, n - i
                M[i - 1][j - 1] = math.comb(u, v) if (0 <= v <= u) else 0
    return M


def main():
    N = 40
    # 1. Compute a(0..N+1) directly from the primary recurrence
    a = [0, 1]
    for n in range(2, N + 2):
        a.append(sum(a[k] * math.comb(n - k - 1, n - 2 * k) for k in range(1, n // 2 + 1)))

    oeis_data = [
        0, 1, 1, 1, 2, 3, 5, 8, 14, 25, 46, 85, 158, 294, 548, 1022, 1908,
        3567, 6683, 12556, 23669, 44781, 85046, 162122, 310157, 595322,
        1146057, 2212004, 4278908, 8292738, 16097018, 31286456, 60873574,
        118543329, 231009934, 450434739, 878687665, 1714754256, 3347381462,
    ]
    assert a[: len(oeis_data)] == oeis_data, "OEIS DATA mismatch"

    # 2. Verify Step 1-2 matrix reversal and exact Bareiss determinants det(M_n) == a(n+1) for n=1..N
    for n in range(1, N + 1):
        M = build_M(n)
        B = [[M[n - 1 - r][n - 1 - c] for c in range(n)] for r in range(n)]
        for r in range(n):
            for c in range(n):
                if r > c + 1:
                    assert B[r][c] == 0
                elif r == c + 1:
                    assert B[r][c] == -1
                else:
                    assert B[r][c] == (math.comb(c - r, r) if r <= c - r else 0)
        detM = bareiss_det(M)
        detB = bareiss_det(B)
        assert detM == detB == a[n + 1], f"Determinant mismatch at n={n}"

    print("PASS")


if __name__ == "__main__":
    main()
