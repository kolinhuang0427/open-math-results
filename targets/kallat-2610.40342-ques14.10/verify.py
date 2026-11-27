#!/usr/bin/env python3
"""
Exact-arithmetic verification script for Question 14.10 (prob:gcdr) of Kallat
(arXiv:2610.40342v1): PROOF.md.
Zero floating-point arithmetic is used anywhere in this script.
"""

import ast
import math
from collections import defaultdict
from fractions import Fraction


def vp(n: int, p: int) -> int:
    assert n != 0, "vp called on 0"
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def sp(n: int, p: int) -> int:
    s = 0
    while n > 0:
        s += n % p
        n //= p
    return s


def vfact(n: int, p: int) -> int:
    return (n - sp(n, p)) // (p - 1)


def falling(n: int, r: int) -> int:
    res = 1
    for j in range(1, r + 1):
        res *= n - j
    return res


def compute_a_inf_table(r: int, nmax: int) -> list[int]:
    """Exact integers a_{S_inf}(n) for 0 <= n <= nmax via
    a(n) = (n-1)*a(n-1) + (n-1)_r * a(n-r-1) for n >= r+1."""
    a = [0] * (nmax + 1)
    a[0] = 1
    for n in range(r + 1, nmax + 1):
        a[n] = (n - 1) * a[n - 1] + falling(n, r) * a[n - r - 1]
    return a


def compute_a_Sk(n: int, k: int, a_inf: list[int], fact: list[int]) -> int:
    """Exact integer a_{S_k}(n) via inclusion-exclusion on k-cycles."""
    tot = 0
    kj = 1
    for j in range(0, n // k + 1):
        term = (fact[n] // (fact[n - j * k] * kj * fact[j])) * a_inf[n - j * k]
        if j & 1:
            tot -= term
        else:
            tot += term
        kj *= k
    return tot


def max_cost_dp(nmax: int, r: int, p: int) -> list[int]:
    """Exact kappa_{r,p}(n) = max_{lambda |- n, min > r} cost_p(lambda)."""
    dp = [-10**9] * (nmax + 1)
    dp[0] = 0
    fv = [vfact(i, p) for i in range(nmax + 1)]
    for m in range(r + 1, nmax + 1):
        vm = vp(m, p)
        ndp = dp[:]
        for c in range(1, nmax // m + 1):
            g = c * vm + fv[c]
            step = c * m
            for s in range(step, nmax + 1):
                v = dp[s - step] + g
                if v > ndp[s]:
                    ndp[s] = v
        dp = ndp
    return dp


def verify_q2_counterexample() -> None:
    print("[1/5] Verifying Q2 disproof (Theorem 2: 64 <= r <= 79, n = 1248, p = 2)...")
    n = 1248
    assert vfact(n, 2) == 1244

    # Check Lemma 2.1: Delta(m) = m/16 - (v_2(m) + 1) in exact Fractions for 65 <= m <= 1248
    zeros = []
    le_one = []
    for m in range(65, n + 1):
        delta = Fraction(m, 16) - (vp(m, 2) + 1)
        assert delta >= 0, f"Delta({m}) < 0"
        if delta == 0:
            zeros.append(m)
        elif delta <= 1:
            le_one.append((m, delta))
    assert zeros == [80, 96, 128], f"Unexpected zeros: {zeros}"
    assert le_one == [(72, Fraction(1, 2))], f"Unexpected le_one: {le_one}"

    # Check Step 2 of Lemma 2.2: 5a + 6b + 8c = 78 with s_2(a) + s_2(b) + s_2(c) <= 3
    sols = []
    for a in range(0, 78 // 5 + 1):
        for b in range(0, (78 - 5 * a) // 6 + 1):
            rem = 78 - 5 * a - 6 * b
            if rem % 8 == 0:
                c = rem // 8
                s_sum = sp(a, 2) + sp(b, 2) + sp(c, 2)
                assert s_sum >= 3
                if s_sum == 3:
                    sols.append((a, b, c))
    assert sorted(sols) == [(0, 1, 9), (0, 13, 0), (6, 8, 0), (8, 1, 4)]

    # Exact DP over ALL parts m in [65..1248] to confirm kappa_{64,2}(1248) == 75
    # and enumerate ALL partitions achieving cost >= 75 (iteratively, no recursion limit)
    fv2 = [vfact(i, 2) for i in range(n + 1)]
    dp_pref = [[-10**9] * (n + 1)]
    dp_pref[0][0] = 0
    for m in range(65, n + 1):
        prev = dp_pref[-1]
        cur = prev[:]
        vm = vp(m, 2)
        for c in range(1, n // m + 1):
            g = c * vm + fv2[c]
            step = c * m
            for s in range(step, n + 1):
                val = prev[s - step] + g
                if val > cur[s]:
                    cur[s] = val
        dp_pref.append(cur)
    assert dp_pref[-1][n] == 75

    # Iterative stack DFS for all partitions of 1248 with parts >= 65 and cost >= 75
    top_parts = []
    stack = [(n - 64, n, 0, ())]
    while stack:
        idx, rem, cur_cost, parts = stack.pop()
        if rem == 0:
            top_parts.append(dict(parts))
            continue
        if idx == 0 or cur_cost + dp_pref[idx][rem] < 75:
            continue
        m = 64 + idx
        vm = vp(m, 2)
        if cur_cost + dp_pref[idx - 1][rem] >= 75:
            stack.append((idx - 1, rem, cur_cost, parts))
        for c in range(1, rem // m + 1):
            g = c * vm + fv2[c]
            if cur_cost + g + dp_pref[idx - 1][rem - c * m] >= 75:
                stack.append((idx - 1, rem - c * m, cur_cost + g, parts + ((m, c),)))
    expected_top = [
        {96: 13},
        {96: 1, 128: 9},
        {80: 6, 96: 8},
        {80: 8, 96: 1, 128: 4},
    ]
    assert sorted(sorted(d.items()) for d in top_parts) == sorted(sorted(d.items()) for d in expected_top)

    # Exact check of a_{S_k}(1248) mod 2^E (E = 1175 > 1170) for ALL 64 <= r <= 79 and ALL r < k <= 1248!
    # Every term (n! / ((n-jk)! k^j j!)) * a_inf(n-jk) is an exact integer; writing m! = 2^{v_2(m!)} * odd(m!),
    # its exact residue mod 2^E is computed in exact integer arithmetic with zero approximation.
    E = 1175
    MOD = 1 << E
    MASK = MOD - 1

    # Precompute odd(m!) mod 2^E and its exact modular inverse mod 2^E for 0 <= m <= n
    u_fact = [1] * (n + 1)
    for i in range(1, n + 1):
        odd_i = i >> vp(i, 2)
        u_fact[i] = (u_fact[i - 1] * odd_i) & MASK
    u_fact_inv = [pow(u, -1, MOD) for u in u_fact]
    odd_inv = [0] * (n + 1)
    v2_int = [0] * (n + 1)
    for k in range(1, n + 1):
        vk = vp(k, 2)
        v2_int[k] = vk
        odd_inv[k] = pow(k >> vk, -1, MOD)

    # Exact witness S = N \ {96}: a_S(1248) = 1248! / (96^13 * 13!)
    a_witness = math.factorial(n) // ((96**13) * math.factorial(13))
    assert vp(a_witness, 2) == 1169

    # Cross-check exact modular method against full unreduced arbitrary-precision integers at r = 64!
    fact_full = [1] * (n + 1)
    for i in range(1, n + 1):
        fact_full[i] = fact_full[i - 1] * i
    a_inf_64_full = compute_a_inf_table(64, n)

    for r in range(64, 80):
        # Exact a_{S_inf}(m) mod 2^E via integer recurrence
        a_inf_mod = [0] * (n + 1)
        a_inf_mod[0] = 1
        for m in range(r + 1, n + 1):
            fall = 1
            for t in range(1, r + 1):
                fall = (fall * (m - t)) & MASK
            a_inf_mod[m] = ((m - 1) * a_inf_mod[m - 1] + fall * a_inf_mod[m - r - 1]) & MASK
        if r == 64:
            assert a_inf_mod[n] == (a_inf_64_full[n] & MASK)

        v_inf = vp(a_inf_mod[n], 2) if a_inf_mod[n] != 0 else E
        assert v_inf >= 1170
        v_G = v_inf
        for k in range(r + 1, n + 1):
            tot = a_inf_mod[n]
            vk_int = v2_int[k]
            ok_inv = odd_inv[k]
            ok_inv_j = 1
            for j in range(1, n // k + 1):
                rem = n - j * k
                a_rem = a_inf_mod[rem]
                ok_inv_j = (ok_inv_j * ok_inv) & MASK
                if a_rem == 0:
                    continue
                v_coeff = fv2[n] - fv2[rem] - j * vk_int - fv2[j]
                if v_coeff >= E:
                    continue
                u_coeff = (u_fact[n] * u_fact_inv[rem] % MOD) * (ok_inv_j * u_fact_inv[j] % MOD) & MASK
                term = ((u_coeff << v_coeff) * a_rem) & MASK
                if j & 1:
                    tot = (tot - term) & MASK
                else:
                    tot = (tot + term) & MASK
            if r == 64 and k in (65, 72, 80, 96, 128, 1248):
                exact_val = compute_a_Sk(n, k, a_inf_64_full, fact_full)
                assert tot == (exact_val & MASK)
            vk = vp(tot, 2) if tot != 0 else E
            assert vk >= 1170, f"Failed at r={r}, k={k}: v_2={vk}"
            if vk < v_G:
                v_G = vk
        assert v_G == 1170, f"Expected v_2(G_{r}(1248))=1170, got {v_G}"
    print("  -> Confirmed EXACTLY for all 16 values 64 <= r <= 79 and all r < k <= 1248: v_2(g_r)=1169 < 1170=v_2(G_r).")


def verify_finite_lemmas_r3() -> None:
    print("[2/5] Verifying finite bounds for r = 3 (Theorem 3, Lemma 4.2, Lemma 4.3, Subcase 4f)...")
    # Theorem 3 finite bound: parts >= 5, p = 2, w in {9..11, 13..15, 17..19}
    dp2 = max_cost_dp(20, 4, 2)
    for delta in (1, 2, 3):
        for nu in (1, 2, 3):
            w = 4 * delta + 4 + nu
            rhs = 2 * delta + vfact(delta, 2) + (1 if nu == 2 else 0)
            assert dp2[w] < rhs, f"Theorem 3 bound failed at delta={delta}, nu={nu}"

    # Lemma 4.2 finite table for w <= 30 avoiding {6, 9}
    wmax = 30
    fv3 = [vfact(i, 3) for i in range(wmax + 1)]
    dp_mu = [-10**9] * (wmax + 1)
    dp_mu[0] = 0
    for m in range(4, wmax + 1):
        if m in (6, 9):
            continue
        vm = vp(m, 3)
        ndp = dp_mu[:]
        for c in range(1, wmax // m + 1):
            g = c * vm + fv3[c]
            step = c * m
            for s in range(step, wmax + 1):
                if dp_mu[s - step] + g > ndp[s]:
                    ndp[s] = dp_mu[s - step] + g
        dp_mu = ndp

    for w in range(4, wmax + 1):
        if dp_mu[w] >= 0:
            assert dp_mu[w] <= (5 * w - 18) // 36

    expected_d0 = {
        0: [(0, 0, 0)],
        1: [(1, 1, 4)],
        2: [(1, 1, 5)],
        3: [(1, 2, 0)],
        4: [(0, 0, 4)],
        5: [(0, 0, 5)],
        6: [(0, 1, 0)],
        7: [(0, 0, 7), (1, 2, 4)],
        8: [(0, 0, 8), (1, 2, 5)],
    }
    expected_d1 = {
        0: [],
        1: [(1, 0, 10), (2, 2, 7)],
        2: [(1, 0, 11), (2, 2, 8)],
        3: [(1, 0, 12)],
        4: [(1, 1, 7)],
        5: [(1, 1, 8)],
        6: [],
        7: [(1, 0, 16), (1, 1, 10)],
        8: [(1, 0, 17), (1, 1, 11)],
    }
    expected_d2 = {
        3: [(2, 1, 15), (2, 2, 9), (3, 2, 18)],
        6: [(1, 0, 15), (1, 1, 9), (2, 1, 18), (2, 2, 12)],
    }
    for rho in range(9):
        dref = 1 if rho in (1, 2, 3) else 0
        e_rho = 2 if rho == 3 else (1 if rho in (1, 2, 6) else 0)
        got0, got1, got2 = [], [], []
        for delta in range(3):
            d = dref + delta
            for x0 in range(3):
                w = 9 * d + rho - 6 * x0
                if w < 0 or w > wmax or dp_mu[w] < 0:
                    continue
                md = 2 * delta + fv3[delta] + e_rho - x0 - dp_mu[w]
                assert md >= 0
                if md == 0:
                    got0.append((d, x0, w))
                elif md == 1:
                    got1.append((d, x0, w))
                elif md == 2:
                    got2.append((d, x0, w))
        assert got0 == expected_d0[rho], f"drop=0 mismatch at rho={rho}: {got0}"
        assert got1 == expected_d1[rho], f"drop=1 mismatch at rho={rho}: {got1}"
        if rho in expected_d2:
            assert got2 == expected_d2[rho], f"drop=2 mismatch at rho={rho}: {got2}"

    # Lemma 4.3 exact mod-9 table for j = 0..10
    expected_mod9 = {(1, 2): 3, (1, 5): 0, (1, 8): 6, (2, 2): 0, (2, 5): 6, (2, 8): 3}
    for x0 in (1, 2):
        for ry in (2, 5, 8):
            for j in range(1 if ry == 2 else 0, 11):
                y = 9 * j + ry
                tot = Fraction(0)
                for t in range(0, min(4, y // 2) + 1):
                    num = (9 ** (2 * t)) * math.factorial(y) * math.factorial(x0)
                    den = (6 ** (3 * t)) * math.factorial(y - 2 * t) * math.factorial(x0 + 3 * t)
                    tot += Fraction(num, den)
                assert tot.denominator % 3 != 0
                res9 = (tot.numerator * pow(tot.denominator, -1, 9)) % 9
                assert res9 == expected_mod9[(x0, ry)], f"Lemma 4.3 mismatch at ({x0}, {y})"

    # Subcase 4f exact rational sum for a_{S_6}(81j + 30)
    s6_coeff = Fraction(1, 12) + Fraction(1, 64 * 6) + Fraction(1, 35) + Fraction(1, 32)
    assert s6_coeff == Fraction(653, 4480)
    assert s6_coeff.numerator % 3 != 0 and s6_coeff.denominator % 3 != 0
    print("  -> All finite tables, bounds, and Lemma 4.3 congruences PASSED.")


def delta3(n: int) -> int:
    if n >= 51 and n % 81 == 51:
        return 2
    if n >= 55 and (n % 27 in (1, 2, 3, 24)):
        return 1
    return 0


def delta3_G(n: int) -> int:
    if n >= 51 and (n % 81 in (30, 51)):
        return 2
    if n >= 55 and (n % 27 in (1, 2, 3, 24)):
        return 1
    return 0


def verify_r3_exhaustive(nmax: int = 275) -> None:
    print(f"[3/5] Verifying Theorem 1, 3, 4 exhaustively for all 5 <= n <= {nmax} (incl. exact g_3, G_3, Lambda_3)...")
    fact = [1] * (nmax + 1)
    for i in range(1, nmax + 1):
        fact[i] = fact[i - 1] * i
    a_inf = compute_a_inf_table(3, nmax)
    dp2 = max_cost_dp(nmax, 3, 2)
    dp3 = max_cost_dp(nmax, 3, 3)

    # Prefix DP for exact part-set enumeration at p = 3
    fv3 = [vfact(i, 3) for i in range(nmax + 1)]
    dp3_pref = [[-10**9] * (nmax + 1)]
    dp3_pref[0][0] = 0
    for m in range(4, nmax + 1):
        prev = dp3_pref[-1]
        cur = prev[:]
        vm = vp(m, 3)
        for c in range(1, nmax // m + 1):
            g = c * vm + fv3[c]
            step = c * m
            for s in range(step, nmax + 1):
                val = prev[s - step] + g
                if val > cur[s]:
                    cur[s] = val
        dp3_pref.append(cur)

    # Verify Case 1 explicit values in PROOF.md (n = 5..9) and Kallat's table (n = 5..14)
    assert compute_a_Sk(5, 4, a_inf, fact) == 24
    assert compute_a_Sk(6, 5, a_inf, fact) == 120
    assert compute_a_Sk(7, 4, a_inf, fact) == 720
    assert compute_a_Sk(8, 5, a_inf, fact) == 6300
    assert compute_a_Sk(9, 4, a_inf, fact) == 40320

    kallat_tab = []
    for n in range(5, nmax + 1):
        f3 = falling(n, 3)
        # Compute exact G_3(n) across ALL 4 <= k <= n (and verify a_{S_{n-1}}(n) == a_inf[n])
        assert compute_a_Sk(n, n - 1, a_inf, fact) == a_inf[n]
        G_val = 0
        for k in range(4, n + 1):
            G_val = math.gcd(G_val, compute_a_Sk(n, k, a_inf, fact))
        if n <= 14:
            kallat_tab.append(G_val // f3)

        # Verify prime factors of G_3(n) / (n-1)_3 are only 2 and 3
        m3 = G_val // f3
        assert G_val % f3 == 0
        tmp = m3
        while tmp % 2 == 0:
            tmp //= 2
        while tmp % 3 == 0:
            tmp //= 3
        assert tmp == 1, f"Prime > 3 divides m_3({n}): {tmp}"

        # Verify exact p = 2 formulas (Theorem 3)
        v2_lam = vfact(n, 2) - dp2[n]
        pred_v2 = vp(f3, 2) + (n - 2) // 4
        assert v2_lam == pred_v2 == vp(G_val, 2), f"p=2 mismatch at n={n}"

        # Verify exact p = 3 formulas for Lambda_3 and G_3 (Theorem 4)
        v3_lam = vfact(n, 3) - dp3[n]
        pred_L3 = vp(f3, 3) + (n - 4) // 9 + (n + 2) // 9
        pred_v3_g = pred_L3 + delta3(n)
        pred_v3_G = pred_L3 + delta3_G(n)
        assert v3_lam == pred_L3, f"Lambda_3 p=3 mismatch at n={n}"
        assert vp(G_val, 3) == pred_v3_G, f"G_3 p=3 mismatch at n={n}: got {vp(G_val, 3)} vs {pred_v3_G}"

        # Whenever G_3 > Lambda_3 at p = 3, compute EXACT v_3(g_3(n)) via Proposition 11.3(iv)!
        gap = pred_v3_G - v3_lam
        if gap > 0:
            M = dp3[n]
            min_cost = M - (gap - 1)
            by_P: dict[frozenset[int], int] = defaultdict(int)
            stack = [(n - 3, n, 0, ())]
            while stack:
                idx, rem, cur_cost, parts = stack.pop()
                if rem == 0:
                    P = frozenset(mm for mm, _ in parts)
                    den = 1
                    for mm, cc in parts:
                        den *= (mm**cc) * fact[cc]
                    by_P[P] += fact[n] // den
                    continue
                if idx == 0 or cur_cost + dp3_pref[idx][rem] < min_cost:
                    continue
                m = 3 + idx
                vm = vp(m, 3)
                if cur_cost + dp3_pref[idx - 1][rem] >= min_cost:
                    stack.append((idx - 1, rem, cur_cost, parts))
                for c in range(1, rem // m + 1):
                    g_add = c * vm + fv3[c]
                    if cur_cost + g_add + dp3_pref[idx - 1][rem - c * m] >= min_cost:
                        stack.append((idx - 1, rem - c * m, cur_cost + g_add, parts + ((m, c),)))
            v3_g = pred_v3_G
            for tot in by_P.values():
                if tot != 0:
                    v = vp(tot, 3)
                    if v < v3_g:
                        v3_g = v
            assert v3_g == pred_v3_g, f"g_3 p=3 mismatch at n={n}: got {v3_g} vs {pred_v3_g}"

    assert kallat_tab == [1, 2, 6, 6, 6, 12, 12, 12, 36, 72]
    print(f"  -> All {nmax - 4} values 5 <= n <= {nmax} match Theorem 1, 3, 4 identically (including Kallat's table).")


def verify_primes_above_3(nmax: int = 80) -> None:
    print(f"[4/5] Verifying v_q(Lambda_3(n)) == v_q((n-1)_3) for all primes 5 <= q <= n <= {nmax}...")
    primes = []
    for x in range(5, nmax + 1):
        d = 2
        is_p = True
        while d * d <= x:
            if x % d == 0:
                is_p = False
                break
            d += 1
        if is_p:
            primes.append(x)
    for q in primes:
        dpq = max_cost_dp(nmax, 3, q)
        for n in range(max(5, q), nmax + 1):
            vq_lam = vfact(n, q) - dpq[n]
            assert vq_lam == vp(falling(n, 3), q), f"q={q}, n={n} mismatch"
    print(f"  -> Verified across all {len(primes)} primes q in [5..{nmax}].")


def verify_beyond_900() -> None:
    print("[5/5] Verifying n = 921 (= 11*81 + 30, beyond Kallat's n <= 900) and n = 942 (= 11*81 + 51)...")
    nmax = 942
    fact = [1] * (nmax + 1)
    for i in range(1, nmax + 1):
        fact[i] = fact[i - 1] * i
    a_inf = compute_a_inf_table(3, nmax)

    # n = 921: y = 101 = 11*9 + 2
    n = 921
    f3 = falling(n, 3)
    L3 = vp(f3, 3) + (n - 4) // 9 + (n + 2) // 9
    assert L3 == 206
    # Witness S = N \ {4, 9}
    y0 = (n - 12) // 9
    assert y0 == 101
    a_49 = sum(
        fact[n] // ((4 ** ((n - 9 * y) // 4)) * fact[(n - 9 * y) // 4] * (9**y) * fact[y])
        for y in range(y0, -1, -4)
    )
    assert vp(a_49, 3) == L3 + 1 == 207
    # Exact check of ALL 4 <= k <= 921!
    v3_G = vp(a_inf[n], 3)
    v2_G = vp(a_inf[n], 2)
    for k in range(4, n + 1):
        val = compute_a_Sk(n, k, a_inf, fact)
        v3_G = min(v3_G, vp(val, 3))
        v2_G = min(v2_G, vp(val, 2))
    assert v3_G == L3 + 2 == 208
    assert v2_G == vp(f3, 2) + (n - 2) // 4 == 233
    assert vp(compute_a_Sk(n, 6, a_inf, fact), 3) == 208

    # n = 942 (= 11*81 + 51): check witness a_{S_inf} - a_{S_15} gives L3 + 2
    n2 = 942
    f3_2 = falling(n2, 3)
    L3_2 = vp(f3_2, 3) + (n2 - 4) // 9 + (n2 + 2) // 9
    diff15 = a_inf[n2] - compute_a_Sk(n2, 15, a_inf, fact)
    assert vp(diff15, 3) == L3_2 + 2
    print("  -> Confirmed n = 921 (v_3(g_3)=207 < 208=v_3(G_3), v_2=233) and n = 942 (v_3=L3+2).")


def verify_zero_floats_self() -> None:
    """AST-check that this file contains zero float literals or float() calls."""
    with open(__file__, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            raise AssertionError(f"Float literal found: {node.value}")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "float":
            raise AssertionError("float() call found")
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            raise AssertionError("True-division '/' operator found")


if __name__ == "__main__":
    verify_zero_floats_self()
    verify_q2_counterexample()
    verify_finite_lemmas_r3()
    verify_r3_exhaustive(275)
    verify_primes_above_3(80)
    verify_beyond_900()
    print("PASS")
