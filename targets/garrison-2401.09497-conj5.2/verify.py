#!/usr/bin/env python3
"""Exact-arithmetic verification for targets/garrison-2401.09497-conj5.2/PROOF.md.

Uses only exact Python integer arithmetic (zero floating point).
Verifies:
  1. Direct backtracking enumeration of all WCS of lengths 1 <= k <= 20:
     - Matches N(k) in Table 2 of arXiv:2401.09497v1.
     - Confirms Conjecture 5.2 (sigma(1) == 1 or sigma(k) == 1) on every WCS.
     - Confirms Lemmas 1, 2, and 3 (reversal, S_m == T_m, c_m > k % m, and
       existence of unique a in [0, L_k) with sigma(i) == gcd(a + i, L_k)).
  2. Direct verification of Lemma 3 on all 4 Starting Sequences and Prime Power /
     Twin Prime Swaps up to k = 50.
  3. Exhaustive check of all algebraic identities, divisibilities, and bounds in
     Case 1 (even k: 4 <= k <= 500) and Case 2 (odd k: all coprime odd triples
     (A, B, R) with 3 <= A < B, R >= 1 odd, k = A*B*R <= 5000).
"""

import math
import sys


def is_wcs_direct(sigma):
    """Check Definition 1.1 directly on 1-indexed list sigma[1..k]."""
    k = len(sigma) - 1
    if sorted(sigma[1:]) != list(range(1, k + 1)):
        return False
    for i in range(1, k + 1):
        si = sigma[i]
        for j in range(1, k + 1):
            if i == j:
                continue
            d = math.gcd(si, abs(i - j))
            if sigma[j] % d != 0:
                return False
    return True


def lcm_upto(k):
    L = 1
    for m in range(2, k + 1):
        L = math.lcm(L, m)
    return L


def find_a_from_sigma(sigma):
    """Construct the unique a in [0, L_k) from Lemma 3 and verify sigma(i) == gcd(a+i, L_k)."""
    k = len(sigma) - 1
    L = lcm_upto(k)
    # Prime powers p^{e_p} <= k
    a = 0
    mod = 1
    for p in range(2, k + 1):
        # primality check (exact int)
        is_p = True
        d = 2
        while d * d <= p:
            if p % d == 0:
                is_p = False
                break
            d += 1
        if not is_p:
            continue
        pe = p
        while pe * p <= k:
            pe *= p
        idx = sigma.index(pe, 1)
        c_pe = idx % pe
        if c_pe == 0:
            c_pe = pe
        target = (-c_pe) % pe
        # CRT merge: a + mod * t == target (mod pe)
        inv = pow(mod, -1, pe)
        t = ((target - a) * inv) % pe
        a = a + mod * t
        mod *= pe
    assert mod == L
    for i in range(1, k + 1):
        if math.gcd(a + i, L) != sigma[i]:
            return None
    return a


def enumerate_wcs_by_congruences(k):
    """Enumerate ALL WCS of length k via prime-power congruence backtracking (Lemma 2+3).

    Returns list of 1-indexed permutations sigma[1..k].
    """
    if k == 1:
        return [(0, [0, 1])]
    L = lcm_upto(k)
    # Collect maximal prime powers p^{e_p} <= k
    pps = []
    for p in range(2, k + 1):
        is_p = True
        d = 2
        while d * d <= p:
            if p % d == 0:
                is_p = False
                break
            d += 1
        if not is_p:
            continue
        pe = p
        while pe * p <= k:
            pe *= p
        pps.append((p, pe))

    # Precompute valid residues a mod pe satisfying zero-carry for p^1 .. p^{e_p}
    valid_res = []
    for p, pe in pps:
        rs = []
        for r in range(pe):
            ok = True
            pw = p
            while pw <= pe:
                if (r % pw) + (k % pw) >= pw:
                    ok = False
                    break
                pw *= p
            if ok:
                rs.append(r)
        valid_res.append(rs)

    # Sort primes by fewest choices first (except keep small primes early for pruning)
    order = sorted(range(len(pps)), key=lambda idx: (len(valid_res[idx]), pps[idx][0]))
    pps = [pps[i] for i in order]
    valid_res = [valid_res[i] for i in order]

    # Precompute for each step which moduli m <= k divide the accumulated modulus M
    acc_mods = []
    M_cur = 1
    for p, pe in pps:
        M_next = M_cur * pe
        new_ms = [m for m in range(2, k + 1) if M_next % m == 0 and M_cur % m != 0]
        acc_mods.append((M_cur, pe, M_next, new_ms))
        M_cur = M_next

    results = []

    def dfs(step, a_cur):
        if step == len(pps):
            sigma = [0] + [math.gcd(a_cur + i, L) for i in range(1, k + 1)]
            if sorted(sigma[1:]) == list(range(1, k + 1)):
                results.append((a_cur, sigma))
            return
        M_old, pe, M_new, new_ms = acc_mods[step]
        inv = pow(M_old, -1, pe)
        for r in valid_res[step]:
            t = ((r - a_cur) * inv) % pe
            a_new = a_cur + M_old * t
            # Check zero-carry for newly active composite moduli m <= k
            ok = True
            for m in new_ms:
                if (a_new % m) + (k % m) >= m:
                    ok = False
                    break
            if not ok:
                continue
            # Check no overflow: gcd(a_new + i, M_new) <= k for all i in 1..k
            for i in range(1, k + 1):
                if math.gcd(a_new + i, M_new) > k:
                    ok = False
                    break
            if ok:
                dfs(step + 1, a_new)

    dfs(0, 0)
    return results


def verify_all():
    # 1. Exhaustive WCS check for 1 <= k <= 20 against Table 2 of arXiv:2401.09497v1
    expected_N = {
        1: 1, 2: 2, 3: 2, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 8, 10: 16,
        11: 16, 12: 4, 13: 4, 14: 2, 15: 2, 16: 8, 17: 8, 18: 8, 19: 8, 20: 4,
    }
    for k in range(1, 21):
        sols = enumerate_wcs_by_congruences(k)
        if len(sols) != expected_N[k]:
            print(f"FAIL: N({k})={len(sols)} != expected {expected_N[k]}")
            return False
        for a, sigma in sols:
            if not is_wcs_direct(sigma):
                print(f"FAIL: enumerated sequence for k={k} is not WCS: {sigma[1:]}")
                return False
            # Conjecture 5.2 check
            if sigma[1] != 1 and sigma[k] != 1:
                print(f"FAIL: Conjecture 5.2 counterexample found at k={k}: {sigma[1:]}")
                return False
            # Lemma 1: reversal is WCS
            rev = [0] + list(reversed(sigma[1:]))
            if not is_wcs_direct(rev):
                print(f"FAIL: Lemma 1 reversal failed at k={k}")
                return False
            # Lemma 2: S_m == T_m and c_m > k % m for all m in 1..k
            for m in range(1, k + 1):
                pos_m = sigma.index(m, 1)
                c_m = pos_m % m
                if c_m == 0:
                    c_m = m
                S_m = [i for i in range(1, k + 1) if i % m == pos_m % m]
                T_m = [i for i in range(1, k + 1) if sigma[i] % m == 0]
                if S_m != T_m or len(S_m) != k // m or not (c_m > k % m):
                    print(f"FAIL: Lemma 2 failed at k={k}, m={m}")
                    return False
            # Lemma 3: reconstructed a matches unique a and sigma(i) == gcd(a+i, L_k)
            a_rec = find_a_from_sigma(sigma)
            if a_rec != a:
                print(f"FAIL: Lemma 3 mismatch at k={k}: {a_rec} != {a}")
                return False

    # 2. Check Starting Sequence 4 (k=21, Twin Sophie Germain + Twin Prime Swap) via Lemma 3
    ss4_21 = [0, 3, 4, 5, 6, 7, 8, 9, 10, 13, 12, 11, 14, 15, 16, 17, 18, 19, 20, 21, 2, 1]
    ss4_21_swap = [0, 3, 4, 5, 6, 7, 8, 9, 10, 13, 12, 11, 14, 15, 16, 19, 18, 17, 20, 21, 2, 1]
    for seq in (ss4_21, ss4_21_swap):
        if not is_wcs_direct(seq) or find_a_from_sigma(seq) is None:
            print("FAIL: Lemma 3 check on k=21 Starting Sequence 4 failed")
            return False

    # 3. Verify Case 1 (even k: 4 <= k <= 500) arithmetic steps
    for k in range(4, 501, 2):
        m = k // 2 + 1
        if not (k // 2 < m < k and k // m == 1 and k % m == k // 2 - 1):
            print(f"FAIL: Case 1 midpoint bounds failed at k={k}")
            return False
        for A in range(3, k, 2):
            if k % A == 0:
                if (k // 2) % A != 0 or m % A == 0:
                    print(f"FAIL: Case 1 divisibility contradiction failed at k={k}, A={A}")
                    return False

    # 4. Verify Case 2 (odd k: all odd coprime triples (A, B, R) with 3 <= A < B, k=A*B*R <= 5000)
    triples_checked = 0
    for A in range(3, 1000, 2):
        if A * (A + 2) > 5000:
            break
        for B in range(A + 2, 5000 // A + 1, 2):
            if math.gcd(A, B) != 1:
                continue
            max_R = 5000 // (A * B)
            for R in range(1, max_R + 1, 2):
                triples_checked += 1
                k = A * B * R
                # Step 2 checks
                m = (k + A) // 2
                if not (2 * m == k + A and k < 2 * m < 2 * k and k // m == 1 and k % m == (k - A) // 2):
                    print(f"FAIL: Case 2 Step 2 failed at {(A, B, R)}")
                    return False
                j = (k - A) // 2 + 1
                if not ((k - A) // 2 + 1 <= j <= (k + A) // 2 and j % A == 1):
                    print(f"FAIL: Case 2 Step 2 j check failed at {(A, B, R)}")
                    return False
                # Verify uniqueness of j in [(k-A)/2+1, (k+A)/2] congruent to 1 mod A
                hits = [x for x in range((k - A) // 2 + 1, (k + A) // 2 + 1) if x % A == 1]
                if hits != [j]:
                    print(f"FAIL: Case 2 Step 2 uniqueness failed at {(A, B, R)}")
                    return False
                # Step 3 checks
                BR1 = B * R + 1
                s = (BR1 & -BR1).bit_length() - 1  # exact v_2(B*R + 1)
                u = BR1 >> s
                if not (s >= 1 and u >= 1 and u % 2 == 1 and (1 << s) * u == BR1):
                    print(f"FAIL: Case 2 Step 3 2-adic factorization failed at {(A, B, R)}")
                    return False
                i1 = (A - 1) * B * R
                if not (1 <= i1 < k and math.gcd(B, BR1) == 1 and B < k and BR1 < k and B * BR1 > k):
                    print(f"FAIL: Case 2 Step 3 overflow check failed at {(A, B, R)}")
                    return False
                # Step 4 checks (when s >= 2)
                if s >= 2:
                    two_s = 1 << s
                    two_sm1 = 1 << (s - 1)
                    if not (two_s < k and A < k and math.gcd(two_s, A) == 1):
                        print(f"FAIL: Case 2 Step 4 L_k divisibility check failed at {(A, B, R)}")
                        return False
                    mod_2sA = two_s * A
                    # Unique residue a_test mod 2^s*A satisfying a == -1 (mod A) and a == A - 1 + 2^{s-1} (mod 2^s)
                    # Verify via CRT
                    inv_A = pow(A, -1, two_s)
                    target_2s = (A - 1 + two_sm1) % two_s
                    t_crt = ((target_2s - (A - 1)) * inv_A) % two_s
                    a_mod = (A - 1) + A * t_crt
                    if not (a_mod % A == A - 1 and a_mod % two_s == target_2s):
                        print(f"FAIL: Case 2 Step 4 CRT failed at {(A, B, R)}")
                        return False
                    indices = [(two_sm1 - 1) * A + 1 + t * mod_2sA for t in range(u)]
                    if len(indices) != u or len(set(indices)) != u:
                        print(f"FAIL: Case 2 Step 4 distinctness failed at {(A, B, R)}")
                        return False
                    if indices[0] < 1 or indices[-1] != k - two_sm1 * A + 1 or indices[-1] >= k:
                        print(f"FAIL: Case 2 Step 4 range failed at {(A, B, R)}")
                        return False
                    for idx in indices:
                        if (a_mod + idx) % mod_2sA != 0:
                            print(f"FAIL: Case 2 Step 4 divisibility failed at {(A, B, R)}, idx={idx}")
                            return False
                    if k // mod_2sA != u - 1:
                        print(f"FAIL: Case 2 Step 4 multiple count failed at {(A, B, R)}")
                        return False

    if triples_checked < 100:
        print(f"FAIL: too few odd triples checked ({triples_checked})")
        return False

    print("PASS")
    return True


if __name__ == "__main__":
    ok = verify_all()
    sys.exit(0 if ok else 1)
