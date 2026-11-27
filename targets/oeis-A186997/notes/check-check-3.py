#!/usr/bin/env python3
"""Independent exact-integer verifier for OEIS A186997 (Peter Bala, Aug 02 2016 conjectures).

Written directly from OEIS A186997 definition and PROOF.md without reading verify.py or notes/.
Pure integer arithmetic (zero floats).
"""

from __future__ import annotations

import math
import sys


def v2(n: int) -> int:
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def s2(n: int) -> int:
    assert n >= 0
    return n.bit_count()


def catalan(m: int) -> int:
    return math.comb(2 * m, m) // (m + 1)


def compute_A_from_functional_eq(max_k: int) -> list[int]:
    """Compute [x^0..x^max_k] of A(x) = 1 + x*A(x)^3 + x^2*A(x)^4 directly in Z[[x]]."""
    a = [0] * (max_k + 1)
    a[0] = 1
    for k in range(1, max_k + 1):
        # Coeff of x^{k-1} in A^3
        c3 = 0
        for i in range(k):
            for j in range(k - i):
                c3 += a[i] * a[j] * a[k - 1 - i - j]
        # Coeff of x^{k-2} in A^4 (if k >= 2)
        c4 = 0
        if k >= 2:
            # Convolve A^2 with A^2 up to k-2
            a2 = [sum(a[i] * a[t - i] for i in range(t + 1)) for t in range(k - 1)]
            c4 = sum(a2[i] * a2[k - 2 - i] for i in range(k - 1))
        a[k] = c3 + c4
    return a


def main() -> int:
    MAX_K = 250  # covers 2*m+1 and 2*m for m <= 124 (beyond n=100)
    print(f"[1/4] Computing A(x) directly from A(x) = 1 + x*A^3 + x^2*A^4 up to k={MAX_K}...", flush=True)
    a_seq = compute_A_from_functional_eq(MAX_K)
    # Sanity check against OEIS A186997 opening terms (rev. 85)
    assert a_seq[:10] == [1, 1, 4, 19, 104, 614, 3816, 24595, 162896, 1101922]

    print("[2/4] Verifying Step 1 Lagrange inversion sum (2k+1)*a(k) = sum_j t_j and W(x) identity...", flush=True)
    for k in range(MAX_K + 1):
        tj_list = [
            ((-1) ** (k - j)) * (1 << j) * math.comb(2 * k + 1, j) * math.comb(2 * k + 1 - 2 * j, k - j)
            for j in range(k + 1)
        ]
        assert sum(tj_list) == (2 * k + 1) * a_seq[k], f"Lagrange inversion mismatch at k={k}"

        # Step 2 exact valuation formulas
        for j, tj in enumerate(tj_list):
            assert v2(tj) == j + v2(math.comb(2 * k + 1, j)) + s2(k + 1 - j) - 1
            assert s2(k + 1 - j) >= s2(k + 1) - s2(j)

    print("[3/4] Verifying Step 3 (odd k = 2m+1) & Step 4 (even k = 2m) ultrametric domination...", flush=True)
    # Auxiliary inequality j - s2(j) - max(v2(j), v2(j-1)) >= 0 for all 2 <= j <= 1000
    for j in range(2, 1001):
        v = max(v2(j), v2(j - 1))
        assert j - s2(j) - v >= 0

    for m in range(MAX_K // 2):
        # Catalan valuation identity
        assert v2(catalan(m)) == s2(m + 1) - 1

        # Odd k = 2m + 1
        k_odd = 2 * m + 1
        if k_odd <= MAX_K:
            tj_odd = [
                ((-1) ** (k_odd - j))
                * (1 << j)
                * math.comb(2 * k_odd + 1, j)
                * math.comb(2 * k_odd + 1 - 2 * j, k_odd - j)
                for j in range(k_odd + 1)
            ]
            v0 = v2(tj_odd[0])
            assert v0 == v2(catalan(2 * m + 1)) == v2(catalan(m))
            for j in range(1, k_odd + 1):
                assert v2(tj_odd[j]) > v0
            assert v2(a_seq[k_odd]) == v2(catalan(2 * m + 1)) == v2(catalan(m))

        # Even k = 2m, m >= 2
        if m >= 2:
            k_ev = 2 * m
            if k_ev <= MAX_K:
                tj_ev = [
                    ((-1) ** (k_ev - j))
                    * (1 << j)
                    * math.comb(2 * k_ev + 1, j)
                    * math.comb(2 * k_ev + 1 - 2 * j, k_ev - j)
                    for j in range(k_ev + 1)
                ]
                assert tj_ev[0] + tj_ev[1] == -k_ev * math.comb(2 * k_ev + 1, k_ev)
                r = v2(m) + 2
                v01 = v2(tj_ev[0] + tj_ev[1])
                assert v01 == s2(m) + r - 1 == 3 + v2(catalan(m - 2))
                for j in range(2, k_ev + 1):
                    if j <= (1 << r) - 1:
                        assert v2(math.comb(4 * m + 1, j)) == r - max(v2(j), v2(j - 1))
                        assert v2(tj_ev[j]) >= s2(m) + r > v01
                    else:
                        assert v2(tj_ev[j]) >= s2(m) + r + 1 > v01
                assert v2(a_seq[k_ev]) == 3 + v2(catalan(m - 2))

    print("[4/4] Verifying symbolic power series identity W(x)*(1 - W(x)^2) = x*(1 + W(x)^4) mod x^60...", flush=True)
    # W(x) = sum a(k) x^{2k+1} mod x^60
    deg = 60
    W = [0] * deg
    for k in range((deg - 1) // 2 + 1):
        W[2 * k + 1] = a_seq[k]

    def poly_mul(p: list[int], q: list[int]) -> list[int]:
        out = [0] * deg
        for i in range(deg):
            if p[i] == 0:
                continue
            for j in range(deg - i):
                out[i + j] += p[i] * q[j]
        return out

    W2 = poly_mul(W, W)
    W3 = poly_mul(W2, W)
    W4 = poly_mul(W2, W2)
    lhs = [W[i] - W3[i] for i in range(deg)]
    rhs = [0] + [1 + W4[0]] + [W4[i - 1] for i in range(2, deg)]
    assert lhs == rhs
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
