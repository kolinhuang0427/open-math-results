#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/oeis-A119262/.

Directly constructs a(n) and M_n from the primary OEIS A119262 definition,
verifies Step 1 (B_n = P_n M_n P_n^{-1} leading principal submatrix of B),
Step 2 (Laplace expansion & block minors det(B_n^{(r, n-1)}) = (-1)^(n-1-r) d_r),
and Step 3 (det(M_n) = a(n+1)) using pure int/SymPy exact integers (zero floats).
"""

import math
import sympy as sp


def binom(u: int, v: int) -> int:
    if v < 0 or u < v:
        return 0
    return math.comb(u, v)


def compute_a(max_n: int) -> list[int]:
    a = [0] * (max_n + 1)
    a[0] = 0
    a[1] = 1
    for n in range(2, max_n + 1):
        a[n] = sum(a[k] * binom(n - k - 1, n - 2 * k) for k in range(1, n // 2 + 1))
    return a


def build_M(n: int) -> sp.Matrix:
    """1-indexed M_n directly from OEIS A119262 formula."""
    rows = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            if i < j - 1:
                row.append(0)
            elif i == j - 1:
                row.append(-1)
            else:
                row.append(binom(i - j, n - i))
        rows.append(row)
    return sp.Matrix(rows)


def build_B(n: int) -> sp.Matrix:
    """0-indexed leading n x n submatrix of infinite matrix B."""
    rows = []
    for r in range(n):
        row = []
        for c in range(n):
            if r > c + 1:
                row.append(0)
            elif r == c + 1:
                row.append(-1)
            else:
                row.append(binom(c - r, r))
        rows.append(row)
    return sp.Matrix(rows)


def main() -> None:
    max_n = 28
    a = compute_a(max_n)
    oeis_terms = [
        0, 1, 1, 1, 2, 3, 5, 8, 14, 25, 46, 85, 158, 294, 548, 1022, 1908, 3567,
        6683, 12556, 23669, 44781, 85046, 162122, 310157, 595322, 1146057, 2212004, 4278908,
    ]
    assert a == oeis_terms
    print(f"Sequence a(0..15) = {a[:16]} (matches OEIS %S/%T through a(28)).")

    # Verify Step 1, Step 2, Step 3 for 1 <= n <= 20
    d = [1]  # d_0 = 1
    for n in range(1, 21):
        M_n = build_M(n)
        B_n = build_B(n)
        # Permutation matrix P_n (reverses indices)
        P_n = sp.Matrix([[1 if i + j == n - 1 else 0 for j in range(n)] for i in range(n)])
        assert P_n * M_n * P_n == B_n

        # Verify leading principal submatrix property (B_{n-1} == B_n[:n-1, :n-1])
        if n >= 2:
            assert B_n[: n - 1, : n - 1] == build_B(n - 1)

        det_M = int(M_n.det())
        det_B = int(B_n.det())
        assert det_M == det_B

        # Check all minors B_n^{(r, n-1)} for n <= 12
        if n <= 12:
            for r in range(n):
                minor = B_n.minor_submatrix(r, n - 1)
                det_minor = int(minor.det())
                assert det_minor == ((-1) ** (n - 1 - r)) * d[r]

        # Check Step 2 recurrence and Step 3 identification with a(n+1)
        d_rec = sum(binom(n - 1 - r, r) * d[r] for r in range(n))
        assert det_M == d_rec
        assert det_M == a[n + 1]
        d.append(det_M)

    print("Verified P_n M_n P_n^-1 = B_n, all minor identities (n<=12), Laplace recurrence, and det(M_n) = a(n+1) for 1 <= n <= 20.")
    print("PASS")


if __name__ == "__main__":
    main()
