#!/usr/bin/env python3
"""Exact-arithmetic verification for OEIS A186997 Bala (2016) 2-adic conjectures."""

import math


def v2(n):
    assert n != 0
    n = abs(n)
    c = 0
    while (n & 1) == 0:
        n >>= 1
        c += 1
    return c


def s2(n):
    return bin(n).count("1")


def poly_mul_trunc(A, B, deg):
    res = [0] * (deg + 1)
    for i, a in enumerate(A[: deg + 1]):
        if a:
            for j in range(min(len(B), deg + 1 - i)):
                res[i + j] += a * B[j]
    return res


def poly_pow_trunc(A, e, deg):
    res = [0] * (deg + 1)
    res[0] = 1
    base = list(A[: deg + 1]) + [0] * max(0, deg + 1 - len(A))
    while e > 0:
        if e & 1:
            res = poly_mul_trunc(res, base, deg)
        e >>= 1
        if e:
            base = poly_mul_trunc(base, base, deg)
    return res


def main():
    N = 120
    # 1. Compute a(0..N) directly from A(x) = 1 + x*A(x)^3 + x^2*A(x)^4
    a = [1]
    for n in range(1, N + 1):
        # Compute coefficients using current a[0..n-1]
        cur = a + [0]
        a3 = poly_pow_trunc(cur, 3, n - 1)
        term = a3[n - 1]
        if n >= 2:
            a4 = poly_pow_trunc(cur, 4, n - 2)
            term += a4[n - 2]
        a.append(term)

    oeis_data = [
        1, 1, 4, 19, 104, 614, 3816, 24595, 162896, 1101922, 7580904, 52878654,
        373100272, 2658188524, 19096607120, 138182654595, 1006202473888,
        7367648586954, 54214472633064, 400698865376842, 2973344993337520,
        22142778865313364,
    ]
    assert a[: len(oeis_data)] == oeis_data, "OEIS DATA mismatch"

    # 2. Verify Step 1 Lagrange binomial sum for (2k+1)*a(k) and W*(1-W^2) == x*(1+W^4):
    for k in range(N + 1):
        rhs_sum = 0
        for j in range(k + 1):
            tj = ((-1) ** (k - j)) * (2 ** j) * math.comb(2 * k + 1, j) * math.comb(2 * k + 1 - 2 * j, k - j)
            rhs_sum += tj
        assert (2 * k + 1) * a[k] == rhs_sum, f"Lagrange identity failed at k={k}"

    # 3. Verify Catalan numbers and exact 2-adic valuation theorems for k = 0..N:
    cat = [math.comb(2 * m, m) // (m + 1) for m in range(N + 2)]
    for m in range(N + 1):
        assert v2(cat[m]) == s2(m + 1) - 1

    # Odd case: a(2m+1) for 2m+1 <= N
    for m in range((N - 1) // 2 + 1):
        k = 2 * m + 1
        assert v2(a[k]) == v2(cat[k]) == v2(cat[m]), f"Odd conj failed at m={m}"
        # Verify strict term-by-term domination from Step 3:
        t0 = ((-1) ** k) * math.comb(2 * k + 1, k)
        assert v2(t0) == v2(cat[m])
        for j in range(1, k + 1):
            tj = ((-1) ** (k - j)) * (2 ** j) * math.comb(2 * k + 1, j) * math.comb(2 * k + 1 - 2 * j, k - j)
            assert v2(tj) > v2(t0)

    # Even case: a(2m) for 2 <= m <= N // 2
    for m in range(2, N // 2 + 1):
        k = 2 * m
        assert v2(a[k]) == 3 + v2(cat[m - 2]), f"Even conj failed at m={m}"
        # Verify Step 4 identity t0 + t1 == -k * C(2k+1, k) and term-by-term domination for j >= 2:
        t0 = math.comb(2 * k + 1, k)
        t1 = -2 * (2 * k + 1) * math.comb(2 * k - 1, k - 1)
        assert t0 + t1 == -k * math.comb(2 * k + 1, k)
        assert v2(t0 + t1) == 3 + v2(cat[m - 2])
        for j in range(2, k + 1):
            tj = ((-1) ** (k - j)) * (2 ** j) * math.comb(2 * k + 1, j) * math.comb(2 * k + 1 - 2 * j, k - j)
            assert v2(tj) > v2(t0 + t1)

    print("PASS")


if __name__ == "__main__":
    main()
