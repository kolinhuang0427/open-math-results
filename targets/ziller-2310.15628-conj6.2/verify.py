#!/usr/bin/env python3
"""Exact verification script for Ziller arXiv:2310.15628v2 Conjecture 6.2.

Verifies:
1. Direct exact rational injectivity of phi(x)/x^2 for all 1 <= x <= 200000.
2. Exactness of the multiplicative formula phi(n)/n^2 = prod_{q^e || n} (q-1)/q^{e+1}
   and the largest-prime p-adic valuation property v_p(phi(n)/n^2) = -(v_p(n) + 1)
   for p = max_prime_factor(n) across all 2 <= n <= 50000.
"""

from fractions import Fraction
import math
import time


def sieve_phi(limit: int) -> list[int]:
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for m in range(p, limit + 1, p):
                phi[m] -= phi[m] // p
    return phi


def factorize_sieve(limit: int) -> list[int]:
    lpf = list(range(limit + 1))
    for i in range(2, int(math.isqrt(limit)) + 1):
        if lpf[i] == i:
            for j in range(i * i, limit + 1, i):
                if lpf[j] == j:
                    lpf[j] = i
    return lpf


def v_p(num: int, den: int, p: int) -> int:
    val = 0
    while num % p == 0:
        num //= p
        val += 1
    while den % p == 0:
        den //= p
        val -= 1
    return val


def main() -> None:
    t0 = time.monotonic()
    N = 200_000
    phi = sieve_phi(N)

    seen: dict[tuple[int, int], int] = {}
    for x in range(1, N + 1):
        num = phi[x]
        den = x * x
        g = math.gcd(num, den)
        key = (num // g, den // g)
        if key in seen:
            raise AssertionError(f"Collision found: x1={seen[key]}, x2={x}, val={key}")
        seen[key] = x

    # Check largest-prime valuation identity for 2 <= n <= 50_000
    M = 50_000
    spf = factorize_sieve(M)
    for n in range(2, M + 1):
        tmp = n
        factors: dict[int, int] = {}
        while tmp > 1:
            p = spf[tmp]
            factors[p] = factors.get(p, 0) + 1
            tmp //= p

        prod_val = Fraction(1, 1)
        for q, e in factors.items():
            prod_val *= Fraction(q - 1, q ** (e + 1))
        assert prod_val == Fraction(phi[n], n * n), f"Formula mismatch at n={n}"

        p_max = max(factors)
        e_max = factors[p_max]
        val = v_p(phi[n], n * n, p_max)
        assert val == -(e_max + 1), f"Valuation mismatch at n={n}: got {val}, expected {-(e_max+1)}"

    elapsed = time.monotonic() - t0
    print(f"Checked injectivity up to N={N} and valuation lemma up to M={M} in {elapsed:.2f}s")
    print("PASS")


if __name__ == "__main__":
    main()
