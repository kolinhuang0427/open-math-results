#!/usr/bin/env python3
"""Zero-float exact verification script for OEIS A347063 counterexample (n = 3468, k = 192)."""

from itertools import combinations
from math import isqrt


def divisors(n: int):
    small, large = [], []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
    return small + large[::-1]


def double_zumkeller_partition(n: int):
    """Return an explicit valid (A, B) partition if n is Double Zumkeller, else None."""
    divs = divisors(n)
    t = len(divs)
    s = sum(divs)
    if t % 2 != 0 or s % 2 != 0:
        return None
    ht = t // 2
    hs = s // 2
    if divs[-1] > hs:
        return None

    # dp[j] maps bitmask of reachable sums using j divisors; store transition layers for witness reconstruction
    layers = []
    dp = [0] * (ht + 1)
    dp[0] = 1
    mask = (1 << (hs + 1)) - 1
    for d in divs:
        layers.append(list(dp))
        for j in range(ht - 1, -1, -1):
            dp[j + 1] = (dp[j + 1] | (dp[j] << d)) & mask

    if not ((dp[ht] >> hs) & 1):
        return None

    # Backtrack explicit witness A of size ht summing to hs
    A = []
    rem_j = ht
    rem_s = hs
    for idx in range(len(divs) - 1, -1, -1):
        d = divs[idx]
        prev = layers[idx]
        if rem_j > 0 and rem_s >= d and ((prev[rem_j - 1] >> (rem_s - d)) & 1):
            A.append(d)
            rem_j -= 1
            rem_s -= d
    assert rem_j == 0 and rem_s == 0
    A_set = set(A)
    B = [d for d in divs if d not in A_set]
    assert len(A) == len(B) == ht
    assert sum(A) == sum(B) == hs
    return sorted(A), B


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def main():
    # 1. Verify all 1 <= k <= 191 have explicit valid Double Zumkeller partitions
    for k in range(1, 192):
        n = 18 * k + 12
        part = double_zumkeller_partition(n)
        assert part is not None, f"Unexpected failure below k=192 at k={k}, n={n}"

    # 2. Verify k = 192 (n = 3468 = 12 * 17^2) is NOT Double Zumkeller via DP AND exhaustive C(18,9) search
    n_ce = 18 * 192 + 12
    assert n_ce == 3468 == 12 * (17 ** 2)
    divs_ce = divisors(n_ce)
    assert len(divs_ce) == 18
    assert sum(divs_ce) == 8596
    assert double_zumkeller_partition(n_ce) is None

    target_sum = sum(divs_ce) // 2
    valid_subsets = 0
    total_subsets = 0
    for sub in combinations(divs_ce, 9):
        total_subsets += 1
        if sum(sub) == target_sum:
            valid_subsets += 1
    assert total_subsets == 48620
    assert valid_subsets == 0

    # 3. Verify the subsets of D0 = {1,2,3,4,6,12} summing to 14 are exclusively {2,12} and {1,3,4,6}
    d0 = [1, 2, 3, 4, 6, 12]
    sums_14 = []
    for r in range(len(d0) + 1):
        for sub in combinations(d0, r):
            if sum(sub) == 14:
                sums_14.append(sub)
    assert sums_14 == [(2, 12), (1, 3, 4, 6)]
    assert all(len(sub) % 2 == 0 for sub in sums_14)

    # 4. Verify infinite family n = 12 * p^2 for primes 17 <= p <= 100
    for p in range(17, 100):
        if not is_prime(p):
            continue
        assert (2 * (p * p - 1)) % 3 == 0
        k = (2 * (p * p - 1)) // 3
        n = 12 * p * p
        assert n == 18 * k + 12
        assert p * p - 14 * p - 14 > 0
        assert p - 14 > 0
        assert double_zumkeller_partition(n) is None

    print("PASS")


if __name__ == "__main__":
    main()
