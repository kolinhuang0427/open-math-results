#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for Garrison-Seiler-Knowles arXiv:2401.09497v1 Conjecture 5.2.

Built strictly from primary source definitions (WCS.tex) and targets/garrison-2401.09497-conj5.2/PROOF.md
without reading verify.py or author notes. Pure integer arithmetic (zero floats).
"""

from __future__ import annotations

import itertools
import math
import sys


def is_wcs_by_definition(sigma: tuple[int, ...]) -> bool:
    """Check Definition 1.1 directly: sigma is a permutation of [k] and
    m | sigma(i) and m | (i - j) => m | sigma(j) for all i, j in [k] and m >= 1.
    """
    k = len(sigma)
    if sorted(sigma) != list(range(1, k + 1)):
        return False
    for i in range(1, k + 1):
        si = sigma[i - 1]
        for j in range(1, k + 1):
            diff = abs(i - j)
            for m in range(2, si + 1):
                if si % m == 0 and diff % m == 0:
                    if sigma[j - 1] % m != 0:
                        return False
    return True


def check_lemmas_on_wcs(sigma: tuple[int, ...]) -> None:
    """Verify Lemma 1, Lemma 2, Lemma 3, and Case 1/Case 2 properties on a concrete WCS."""
    k = len(sigma)
    assert sigma[0] == 1 or sigma[-1] == 1, f"Conjecture 5.2 failed at k={k}: {sigma}"

    # Lemma 1: Reversal
    rev = tuple(reversed(sigma))
    assert is_wcs_by_definition(rev)
    assert rev[0] == sigma[-1] and rev[-1] == sigma[0]

    # Lemma 2: S_m == T_m, |S_m| == k // m, c_m > k % m
    inv = [0] * (k + 1)
    for idx, val in enumerate(sigma, start=1):
        inv[val] = idx

    for m in range(1, k + 1):
        pos_m = inv[m]
        c_m = ((pos_m - 1) % m) + 1
        assert 1 <= c_m <= m
        assert c_m > (k % m), f"Lemma 2 c_m > k%m failed at k={k}, m={m}"
        S_m = [i for i in range(1, k + 1) if (i - pos_m) % m == 0]
        T_m = [i for i in range(1, k + 1) if sigma[i - 1] % m == 0]
        assert S_m == T_m
        assert len(S_m) == k // m

    # Lemma 3: GCD representation sigma(i) = gcd(a + i, L_k)
    L_k = math.lcm(*range(1, k + 1))
    # Construct a via CRT from prime powers p^{e_p} <= k
    congruences = []
    for p in range(2, k + 1):
        if all(p % d != 0 for d in range(2, math.isqrt(p) + 1)):
            pe = p
            while pe * p <= k:
                pe *= p
            c_pe = ((inv[pe] - 1) % pe) + 1
            congruences.append(((-c_pe) % pe, pe))

    a, mod = 0, 1
    for rem, m in congruences:
        # Solve a + mod * t == rem (mod m) where gcd(mod, m) == 1
        inv_mod = pow(mod, -1, m)
        t = ((rem - a) * inv_mod) % m
        a += mod * t
        mod *= m
    assert mod == L_k
    assert 0 <= a < L_k
    for i in range(1, k + 1):
        assert sigma[i - 1] == math.gcd(a + i, L_k)
        for m in range(1, k + 1):
            assert (sigma[i - 1] % m == 0) == ((a + i) % m == 0)

    # Case 1 check (even k >= 4): normalized sequence has sigma(k/2 + 1) = k/2 + 1 and sigma(1) = 1
    if k >= 4 and k % 2 == 0:
        norm = sigma if sigma[1] % 2 == 0 else rev
        assert all(norm[i - 1] % 2 == i % 2 for i in range(1, k + 1))
        assert norm[k // 2] == k // 2 + 1
        assert norm[0] == 1


def find_all_wcs_via_gcd(k: int) -> list[tuple[int, ...]]:
    """Use Lemma 3's search space (0 <= a < L_k) and verify every WCS against Definition 1.1."""
    L_k = math.lcm(*range(1, k + 1))
    res = []
    seen = set()
    # Notice for k >= 2, c_2 in {1, 2}, and for odd k >= 3, c_2 = 2 so a must be even;
    # for even k, sigma(1) or sigma(k) = 1 => either gcd(a+1, L_k)=1 or gcd(a+k, L_k)=1,
    # Wait: let's NOT assume Conjecture 5.2! Simply check ALL 0 <= a < L_k!
    # Wait: L_11 = 27720, L_12 = 27720, L_13 = 360360 (fast!).
    for a in range(L_k):
        seq = tuple(math.gcd(a + i, L_k) for i in range(1, k + 1))
        if max(seq) <= k and len(set(seq)) == k:
            assert seq not in seen
            seen.add(seq)
            assert is_wcs_by_definition(seq)
            res.append(seq)
    return res


def check_case2_arith_proof_on_odd_composites() -> None:
    """Independently test all inequalities and modular identities of Case 2 (Steps 1-4)
    across all admissible (A, B, R) with 3 <= A < B odd, gcd(A, B) = 1, k = A*B*R <= 150.
    """
    tested_triples = 0
    for A in range(3, 40, 2):
        for B in range(A + 2, 60, 2):
            if math.gcd(A, B) != 1:
                continue
            for R in range(1, 15, 2):
                k = A * B * R
                if k > 150:
                    break
                BR = B * R
                assert BR >= 5 and k >= 15
                # Factor BR + 1 = 2^s * u
                val = BR + 1
                s = 0
                while val % 2 == 0:
                    val //= 2
                    s += 1
                u = val
                assert s >= 1 and u % 2 == 1
                assert B < k and BR + 1 < 3 * BR <= k

                i_1 = (A - 1) * BR
                assert 1 <= 2 * BR <= i_1 < k

                # Test all residue classes a_mod mod (2^s * A * B) consistent with:
                # 2 | a, a == -1 (mod A), B | a, (BR+1)/2 | (a + 1 - A)
                # Note gcd(A, B) = 1, gcd(2^s, A*B) = 1.
                # By Step 1 & Step 2, if s == 1 then a + i_1 is divisible by 2^1 = 2 and u and B => B(BR+1) | (a+i_1) => contradiction.
                # If s >= 2, check both congruence classes for a + 1 - A mod 2^s (0 vs 2^{s-1}):
                # 0 mod 2^s => B(BR+1) | (a+i_1) => impossible if gcd(a+i_1, L_k) = sigma(i_1) <= k!
                # 2^{s-1} mod 2^s => Step 4 constructs u distinct indices i_0..i_{u-1} in [k] with 2^s * A | (a + i_t)!
                M = (1 << s) * A * B
                # First solve a == -1 mod A, a == 0 mod B => a0 = B * ((-inv_B_A) % A)
                inv_B_A = pow(B, -1, A)
                a0 = B * ((-inv_B_A) % A)
                assert a0 % A == A - 1 and a0 % B == 0

                if s == 1:
                    # Step 3: for s == 1, 2 | a and 2 | (A - 1) => 2 | (a + 1 - A), so 2^s | (a + i_1) automatically!
                    inv_AB_2 = pow(A * B, -1, 2)
                    t_lift = ((0 - a0) * inv_AB_2) % 2
                    a_even = a0 + A * B * t_lift
                    assert a_even % 2 == 0 and (a_even + 1 - A) % 2 == 0
                    assert (a_even + i_1) % 2 == 0
                else:
                    # Step 3: s >= 2, solve a == A - 1 + 2^{s-1} (mod 2^s)
                    inv_AB_2s = pow(A * B, -1, 1 << s)
                    target_2s = (A - 1 + (1 << (s - 1))) % (1 << s)
                    t_lift = ((target_2s - a0) * inv_AB_2s) % (1 << s)
                    a_cand = a0 + A * B * t_lift
                    assert 0 <= a_cand < M
                    assert a_cand % 2 == 0
                    assert a_cand % A == A - 1
                    assert a_cand % B == 0
                    assert (a_cand + 1 - A) % (1 << s) == (1 << (s - 1))

                    # Step 4: construct i_t for t = 0..u-1
                    indices = []
                    for t in range(u):
                        i_t = ((1 << (s - 1)) - 1) * A + 1 + t * (1 << s) * A
                        assert 1 <= i_t < k
                        assert (a_cand + i_t) % ((1 << s) * A) == 0
                        indices.append(i_t)
                    assert len(set(indices)) == u
                    assert k < u * (1 << s) * A
                    assert k // ((1 << s) * A) == u - 1
                tested_triples += 1
    assert tested_triples > 0
    print(f"  Verified Case 2 Steps 2-4 identities and bounds on {tested_triples} odd composite (A,B,R) triples (k <= 150).")


def run_all_checks() -> None:
    print("Check 1: Exhaustive permutation check of Definition 1.1 & Lemmas 1-3 for k=1..8...")
    expected_counts = {1: 1, 2: 2, 3: 2, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4}
    for k in range(1, 9):
        wcs_list = [p for p in itertools.permutations(range(1, k + 1)) if is_wcs_by_definition(p)]
        assert len(wcs_list) == expected_counts[k], f"Count mismatch at k={k}: {len(wcs_list)}"
        for sigma in wcs_list:
            check_lemmas_on_wcs(sigma)
    print("  k=1..8 exhaustive permutations passed.")

    print("Check 2: Exhaustive GCD search (all 0 <= a < L_k) for k=3..12 (incl. k=9,10,12)...")
    for k in range(3, 13):
        wcs_list = find_all_wcs_via_gcd(k)
        assert len(wcs_list) >= 2
        for sigma in wcs_list:
            check_lemmas_on_wcs(sigma)
        print(f"  k={k}: N(k)={len(wcs_list)} verified.")

    print("Check 3: Case 2 Steps 1-4 modular & inequality checks on odd composite k <= 150...")
    check_case2_arith_proof_on_odd_composites()

    print("PASS")


if __name__ == "__main__":
    try:
        run_all_checks()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
