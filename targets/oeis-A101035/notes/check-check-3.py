#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A101035 (Benedict W. J. Irwin, Jul 26 2017).

Zero floating-point operations: pure Python int/Fraction arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
import math
import sys

OEIS_DATA = [
    1, -3, -5, 1, -9, 15, -13, 1, 4, 27, -21, -5, -25, 39, 45, 1, -33, -12,
    -37, -9, 65, 63, -45, -5, 16, 75, 4, -13, -57, -135, -61, 1, 105, 99, 117,
    4, -73, 111, 125, -9, -81, -195, -85, -21, -36, 135, -93, -5, 36, -48,
    165, -25, -105, -12, 189, -13, 185, 171, -117, 45, -121, 183, -52, 1,
    225, -315, -133, -33, 225, -351, -141, 4,
]


def main() -> int:
    max_m = 120

    # 1. Pillai's gcd-sum function g(m) = sum_{j=1..m} gcd(j, m)
    g = [0] * (max_m + 1)
    for m in range(1, max_m + 1):
        g[m] = sum(math.gcd(j, m) for j in range(1, m + 1))

    # 2. Direct Dirichlet inverse a = g^{-1}
    a = [0] * (max_m + 1)
    a[1] = 1
    for m in range(2, max_m + 1):
        s = sum(a[d] * g[m // d] for d in range(1, m) if m % d == 0)
        assert s % g[1] == 0
        a[m] = -s // g[1]
    assert a[1 : 1 + len(OEIS_DATA)] == OEIS_DATA, "Mismatch against OEIS A101035 DATA"

    # Cross-check OEIS multiplicative formula a(p)=1-2p, a(p^e)=(p-1)^2 (e>1)
    for m in range(1, max_m + 1):
        tmp = m
        expected = 1
        p = 2
        while p * p <= tmp:
            if tmp % p == 0:
                e = 0
                while tmp % p == 0:
                    tmp //= p
                    e += 1
                expected *= (1 - 2 * p) if e == 1 else (p - 1) ** 2
            p += 1
        if tmp > 1:
            expected *= 1 - 2 * tmp
        assert a[m] == expected, f"Multiplicative formula mismatch at m={m}"

    # 3. Mobius function via direct sum_{d|n} mu(d) == [n==1]
    mu = [0] * (max_m + 1)
    mu[1] = 1
    for n in range(2, max_m + 1):
        mu[n] = -sum(mu[d] for d in range(1, n) if n % d == 0)

    # Step 1: check a == (id*mu)*(id*mu)*1
    for m in range(1, max_m + 1):
        conv = 0
        for n in range(1, m + 1):
            if m % n != 0:
                continue
            q1 = m // n
            for k in range(1, q1 + 1):
                if q1 % k == 0:
                    conv += n * mu[n] * k * mu[k]
        assert conv == a[m], f"Step 1 Dirichlet convolution mismatch at m={m}"

    # 4. Step 2: Logarithmic generating function expansion mod x^{max_m+1}
    lgf_coeff = [Fraction(0)] * (max_m + 1)
    for n in range(1, max_m + 1):
        if mu[n] == 0:
            continue
        for k in range(1, max_m // n + 1):
            if mu[k] == 0:
                continue
            nk = n * k
            pref = mu[n] * mu[k]
            for r in range(1, max_m // nk + 1):
                lgf_coeff[nk * r] += Fraction(pref, r)

    for m in range(1, max_m + 1):
        assert lgf_coeff[m] == Fraction(a[m], m), f"LGF coefficient mismatch at x^{m}"

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
