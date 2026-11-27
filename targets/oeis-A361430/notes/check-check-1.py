#!/usr/bin/env python3
"""Independent exact-integer verifier for targets/oeis-A361430/.

Built directly from OEIS A298674, A298824, A298825, A298826, A306653, A361430
and PROOF.md without reading verify.py or author notes. Zero floats.
"""
from __future__ import annotations

from math import gcd, isqrt

# Verbatim OEIS %S data:
# A361430 (%S, n=1..87):
OEIS_A361430 = [
    1,0,0,1,0,0,0,2,1,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,1,0,2,0,0,0,0,4,0,0,
    0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,
    0,0,0,2,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,
]
# A298826 (%S, n=1..108):
OEIS_A298826 = [
    1,0,0,1,0,0,0,2,-1,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,-1,0,-2,0,0,0,0,4,0,
    0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,
    0,0,0,0,0,-2,0,0,0,0,0,0,0,0,-3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,-2,
]
# A306653 (%S, n=1..28):
OEIS_A306653 = [
    1,-2,-2,2,-2,4,-2,0,0,4,-2,-4,-2,4,4,0,-2,0,-2,-4,4,4,-2,0,0,4,0,-4,
]


def mobius(n: int) -> int:
    if n == 1:
        return 1
    cnt = 0
    d = 2
    x = n
    while d * d <= x:
        if x % d == 0:
            x //= d
            if x % d == 0:
                return 0
            cnt += 1
        d += 1
    if x > 1:
        cnt += 1
    return -1 if (cnt % 2 == 1) else 1


def divisors(n: int) -> list[int]:
    small, large = [], []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
    return small + large[::-1]


def factorize(n: int) -> list[tuple[int, int]]:
    res = []
    d = 2
    x = n
    while d * d <= x:
        if x % d == 0:
            e = 0
            while x % d == 0:
                x //= d
                e += 1
            res.append((d, e))
        d += 1
    if x > 1:
        res.append((x, 1))
    return res


def tau(n: int) -> int:
    ans = 1
    for _, e in factorize(n):
        ans *= (e + 1)
    return ans


def T_matrix_primary(u: int, v: int) -> int:
    """T(u, v) = (A * B)(u, v) = sum_{d | gcd(u, v)} mu(d) * d."""
    return sum(mobius(d) * d for d in divisors(gcd(u, v)))


def c_primary(n: int) -> int:
    """Primary matrix-convolution definition of A298826(n) = A298825(n)/n from A298674."""
    total = 0
    divs = divisors(n)
    for m in range(1, n + 1):
        for k in divs:
            total += T_matrix_primary(n // k, m) * T_matrix_primary(k, m + 2)
    assert total % n == 0, f"A298825({n})={total} not divisible by {n}"
    return total // n


def b_func(j: int) -> int:
    """PROOF.md Sec 2: b(j) = sum_{d1*d2=j, gcd(d1,d2)|2} mu(d1)*mu(d2)*gcd(d1,d2)."""
    tot = 0
    for d1 in divisors(j):
        d2 = j // d1
        g = gcd(d1, d2)
        if 2 % g == 0:
            tot += mobius(d1) * mobius(d2) * g
    return tot


def main() -> int:
    # 1. Check primary matrix definition against exact OEIS %S for A298826 (n=1..108) & A361430 (n=1..87)
    N_MAX = 150
    c_vals = [0] + [c_primary(n) for n in range(1, N_MAX + 1)]
    assert c_vals[1:109] == OEIS_A298826, "Mismatch vs OEIS A298826 %S"
    assert [abs(c_vals[n]) for n in range(1, 88)] == OEIS_A361430, "Mismatch vs OEIS A361430 %S"
    print(f"PASS Primary matrix A298826(1..108) & |A298826(1..87)| == OEIS %S exactly.")

    # 2. Check CRT convolution c = tau * b and b(1..28) == A306653 %S, plus multiplicativity of b
    b_vals = [0] + [b_func(n) for n in range(1, 301)]
    assert b_vals[1:29] == OEIS_A306653, "Mismatch b vs A306653"
    for n in range(1, N_MAX + 1):
        conv = sum(tau(n // j) * b_vals[j] for j in divisors(n))
        assert conv == c_vals[n], f"Convolution mismatch at n={n}"
    for u in range(1, 35):
        for v in range(1, 35):
            if gcd(u, v) == 1 and u * v <= 300:
                assert b_vals[u * v] == b_vals[u] * b_vals[v]
    print("PASS CRT convolution c = tau * b, b == A306653, and b multiplicativity.")

    # 3. Check Schulte's prime-power formula, Kotesovec's |c(n)| = A361430(n), and Oudra's formula for n=1..500
    def schulte_c(n: int) -> int:
        ans = 1
        for p, e in factorize(n):
            ans *= ((-1) ** p) * (e - 1)
        return ans

    def a361430_def(n: int) -> int:
        ans = 1
        for _, e in factorize(n):
            ans *= (e - 1)
        return ans

    def oudra_c(n: int) -> int:
        s = sum(mobius(d) * tau(d) * tau(n // d) for d in divisors(n))
        return (-1 if (n + 1) % 2 == 1 else 1) * s

    for n in range(1, N_MAX + 1):
        assert c_vals[n] == schulte_c(n), f"Schulte mismatch at n={n}"
        assert abs(c_vals[n]) == a361430_def(n), f"Kotesovec mismatch at n={n}"
        assert c_vals[n] == oudra_c(n), f"Oudra mismatch at n={n}"

    # Also verify Schulte == Oudra and |Schulte| == A361430 up to n = 2000 (and b(p^e) directly on prime powers)
    for n in range(1, 2001):
        assert schulte_c(n) == oudra_c(n)
        assert abs(schulte_c(n)) == a361430_def(n)

    for p in (2, 3, 5, 7, 11, 13):
        pe = p
        for e in range(1, 12):
            if pe <= 50000:
                exp_b = -2 if e == 1 else (2 if (p == 2 and e == 2) else 0)
                assert b_func(pe) == exp_b
            pe *= p
    print("PASS Schulte, Kotesovec, and Oudra formulas verified for n=1..150 (primary), n=1..2000 (multiplicative/divisor), and prime powers.")
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
