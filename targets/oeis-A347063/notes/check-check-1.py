#!/usr/bin/env python3
"""
Independent exact-arithmetic verifier for targets/oeis-A347063/
directly from live OEIS A347063 rev. 51 definition ("Double Zumkeller numbers:
numbers whose set of divisors can be partitioned into two disjoint subsets
with equal sums and equal cardinalities") and Ianakiev's Oct 01 2024 conjecture:
  "It seems that for k>=1 all numbers of the form 18k+12 are terms."

Zero floating-point arithmetic: pure Python int and itertools only.
"""

from itertools import combinations


def divisors(n: int) -> list[int]:
    small = []
    large = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
        d += 1
    return small + large[::-1]


def find_dz_partition(n: int):
    """
    Exact bitmask DP over Python big integers.
    Returns (True, subset_A, subset_B) if n is Double Zumkeller, else (False, None, None).
    dp[c] stores a bitmask whose bit s is 1 iff some c-element subset of divisors sums to s.
    """
    divs = divisors(n)
    m = len(divs)
    if m % 2 != 0:
        return False, None, None
    total = sum(divs)
    if total % 2 != 0:
        return False, None, None
    half_cnt = m // 2
    half_sum = total // 2

    # Forward DP recording layers to reconstruct witness cleanly
    layers = [[1] + [0] * half_cnt]
    mask_limit = (1 << (half_sum + 1)) - 1
    cur = layers[0]
    for d in divs:
        nxt = cur[:]
        for c in range(half_cnt, 0, -1):
            nxt[c] |= (cur[c - 1] << d) & mask_limit
        layers.append(nxt)
        cur = nxt

    if not ((cur[half_cnt] >> half_sum) & 1):
        return False, None, None

    # Reconstruct exact subset A of size half_cnt and sum half_sum
    rem_c = half_cnt
    rem_s = half_sum
    A = []
    B = []
    for idx in range(m - 1, -1, -1):
        d = divs[idx]
        prev = layers[idx]
        if rem_c >= 1 and rem_s >= d and ((prev[rem_c - 1] >> (rem_s - d)) & 1):
            A.append(d)
            rem_c -= 1
            rem_s -= d
        else:
            B.append(d)

    A.reverse()
    B.reverse()
    assert len(A) == len(B) == half_cnt
    assert sum(A) == sum(B) == half_sum
    assert sorted(A + B) == divs
    return True, A, B


def is_prime(p: int) -> bool:
    if p < 2:
        return False
    d = 2
    while d * d <= p:
        if p % d == 0:
            return False
        d += 1
    return True


def check_proof_lemmas() -> None:
    # 1. Exact check on D0 = {1, 2, 3, 4, 6, 12}: enumerate all 2^6 = 64 subsets
    D0 = [1, 2, 3, 4, 6, 12]
    assert len(D0) == 6 and sum(D0) == 28
    sum14_subsets = []
    for r in range(len(D0) + 1):
        for comb in combinations(D0, r):
            if sum(comb) == 14:
                sum14_subsets.append(comb)
    assert sum14_subsets == [(2, 12), (1, 3, 4, 6)], f"Unexpected subsets: {sum14_subsets}"
    for comb in sum14_subsets:
        assert len(comb) % 2 == 0

    # 2. Verify base-p forcing inequalities & progression membership for all primes 17 <= p <= 2000
    primes = [p for p in range(17, 2001) if is_prime(p)]
    for p in primes:
        assert (p * p - 1) % 3 == 0
        k = (2 * (p * p - 1)) // 3
        assert k >= 192
        assert 12 * p * p == 18 * k + 12
        # s2 >= 15 vs 14p^2 + 14p + 14
        assert 15 * p * p > 14 * p * p + 14 * p + 14
        # s2 <= 13 with max s1,s0 = 28
        assert 13 * p * p + 28 * p + 28 < 14 * p * p + 14 * p + 14
        # s1 >= 15
        assert 15 * p > 14 * p + 14
        # s1 <= 13 with max s0 = 28
        assert 13 * p + 28 < 14 * p + 14

    # Directly verify DP on first few prime instances p = 17, 19, 23, 29, 31
    for p in (17, 19, 23, 29, 31):
        n = 12 * p * p
        ok, _, _ = find_dz_partition(n)
        assert not ok, f"12*{p}^2 = {n} unexpectedly Double Zumkeller!"

    print(f"PASS check_proof_lemmas: D0 subsets={(sum14_subsets)}, {len(primes)} primes in [17,2000] verified, p<=31 DP verified")


def check_minimality_and_bfile() -> None:
    # 1. Exhaustive DP check for ALL 1 <= k <= 191 -> Double Zumkeller
    for k in range(1, 192):
        n = 18 * k + 12
        ok, A, B = find_dz_partition(n)
        assert ok, f"Counterexample before k=192 at k={k}, n={n}!"

    # 2. Exact C(18, 9) = 48620 brute-force subset check on n = 3468 = 18*192 + 12
    n3468 = 18 * 192 + 12
    assert n3468 == 3468 == 12 * 17 * 17
    divs = divisors(n3468)
    assert len(divs) == 18
    sig = sum(divs)
    assert sig == 28 * (1 + 17 + 289) == 8596
    half = sig // 2
    assert half == 4298

    cnt_9 = 0
    hits = 0
    for comb in combinations(divs, 9):
        cnt_9 += 1
        if sum(comb) == half:
            hits += 1
    assert cnt_9 == 48620
    assert hits == 0, f"Found {hits} 9-subsets summing to {half} for 3468!"

    # Cross-check with DP
    ok3468, _, _ = find_dz_partition(3468)
    assert not ok3468

    print(
        f"PASS check_minimality_and_bfile: all 1<=k<=191 DZ (standalone exact integer DP), "
        f"n=3468 brute-force C(18,9)={cnt_9} hits=0"
    )


def main() -> None:
    check_proof_lemmas()
    check_minimality_and_bfile()
    print("PASS")


if __name__ == "__main__":
    main()
