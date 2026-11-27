"""Exact-arithmetic verification for OEIS A101035 (Irwin 2017 L.g.f. conjecture)."""

from fractions import Fraction
import math


OEIS_DATA = [
    1, -3, -5, 1, -9, 15, -13, 1, 4, 27, -21, -5, -25, 39, 45, 1, -33, -12,
    -37, -9, 65, 63, -45, -5, 16, 75, 4, -13, -57, -135, -61, 1, 105, 99,
    117, 4, -73, 111, 125, -9, -81, -195, -85, -21, -36, 135, -93, -5, 36,
    -48, 165, -25, -105, -12, 189, -13, 185, 171, -117, 45, -121, 183, -52,
    1, 225, -315, -133, -33, 225, -351, -141, 4,
]


def mobius_sieve(N: int) -> list[int]:
    mu = [0] * (N + 1)
    mu[1] = 1
    primes: list[int] = []
    is_comp = [False] * (N + 1)
    for i in range(2, N + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > N:
                break
            is_comp[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def main() -> None:
    N = 180
    mu = mobius_sieve(N)

    # 1. Compute Pillai's gcd-sum function g(m) = A018804(m) from primary definition
    g = [0] * (N + 1)
    for m in range(1, N + 1):
        g[m] = sum(math.gcd(j, m) for j in range(1, m + 1))

    # 2. Compute Dirichlet inverse a = g^{-1} directly from (a * g)(m) = eps(m)
    a = [0] * (N + 1)
    a[1] = 1
    for m in range(2, N + 1):
        s = sum(a[d] * g[m // d] for d in range(1, m) if m % d == 0)
        assert s % g[1] == 0
        a[m] = -s // g[1]

    for idx, expected in enumerate(OEIS_DATA, start=1):
        if a[idx] != expected:
            print(f"FAIL: OEIS_DATA mismatch at n={idx}: {a[idx]} != {expected}")
            raise SystemExit(1)

    # 3. Compute exact coefficients of sum_{n,k>=1} mu(n)*mu(k)*log(1/(1-x^(nk))) up to x^N
    lgf_coeff = [Fraction(0, 1)] * (N + 1)
    for n in range(1, N + 1):
        if mu[n] == 0:
            continue
        for k in range(1, N // n + 1):
            if mu[k] == 0:
                continue
            nk = n * k
            mk = mu[n] * mu[k]
            for r in range(1, N // nk + 1):
                lgf_coeff[nk * r] += Fraction(mk, r)

    for m in range(1, N + 1):
        if lgf_coeff[m] != Fraction(a[m], m):
            print(f"FAIL: LGF mismatch at m={m}: {lgf_coeff[m]} != {Fraction(a[m], m)}")
            raise SystemExit(1)

    print("PASS")


if __name__ == "__main__":
    main()
