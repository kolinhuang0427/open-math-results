#!/usr/bin/env python3
"""Independent exact-arithmetic checker for targets/kallat-2610.40342-ques14.10."""

from collections import defaultdict
from fractions import Fraction
from math import comb, factorial, gcd, isqrt


def vp(n: int, p: int) -> int:
    assert n != 0
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def vp_frac(q: Fraction, p: int) -> int:
    assert q != 0
    return vp(q.numerator, p) - vp(q.denominator, p)


def sum_digits(n: int, p: int) -> int:
    s = 0
    while n > 0:
        s += n % p
        n //= p
    return s


def vp_fact(n: int, p: int) -> int:
    return (n - sum_digits(n, p)) // (p - 1)


def ell_p(m: int, c: int, p: int) -> int:
    if c == 0:
        return 0
    return c * vp(m, p) + vp_fact(c, p)


def falling_fact(n: int, r: int) -> int:
    res = 1
    for j in range(r):
        res *= (n - j)
    return res


def a_S_exact_mod(n: int, forbidden: set[int], mod: int | None = None) -> int:
    """
    Compute exact a_S(n) (or a_S(n) % mod if mod is given) directly from the recurrence:
      a_S(0) = 1,
      a_S(m) = sum_{j not in S, 1 <= j <= m} (m-1)_{j-1} * a_S(m-j).
    Uses only exact integer arithmetic.
    """
    allowed = [j for j in range(1, n + 1) if j not in forbidden]
    a = [0] * (n + 1)
    a[0] = 1
    for m in range(1, n + 1):
        tot = 0
        # Maintain falling = (m-1)_{j-1}
        # Since allowed may be sparse, compute incrementally per step j = 1..m
        fall = 1  # (m-1)_{j-1} for j = 1
        allowed_set = set(allowed)
        for j in range(1, m + 1):
            if j in allowed_set:
                tot += fall * a[m - j]
                if mod is not None:
                    tot %= mod
            fall *= (m - j)
            if mod is not None:
                fall %= mod
        a[m] = tot if mod is None else (tot % mod)
    return a[n]


def a_S_all_k_mod(n: int, r: int, mod: int | None = None) -> tuple[int, list[int]]:
    """
    Compute a_{S_infty}(n) and a_{S_k}(n) for all k in (r, n] cleanly,
    modulo `mod` (or exact if mod is None).
    Wait: for large n (like n=1248), O(n^3) would be 1248^3 ~ 2e9; instead notice:
    F_{S_infty \\cup {k}}(x) = F_{S_infty}(x) * exp(-x^k / k)!
    SO a_{S_k}(n) = sum_{t=0}^{floor(n/k)} (-1)^t * n! / (k^t * t! * (n - k*t)!) * a_{S_infty}(n - k*t)!!
    CHECK THAT IDENTITY!!
    F_{S_k}(x) = exp(sum_{m > r, m != k} x^m/m) = F_{S_infty}(x) * exp(-x^k / k)!
    Extracting n! * [x^n] gives:
      a_{S_k}(n) = sum_{t=0}^{floor(n/k)} (-1)^t * (n! / ((n - k*t)! * k^t * t!)) * a_{S_infty}(n - k*t)!!
    Since for k > r, n - k*t only visits <= floor(n/k) values, computing ALL a_{S_k}(n) for k in (r, n]
    takes only O(n^2 + n log n) operations total!
    """
    a_inf = [0] * (n + 1)
    a_inf[0] = 1
    for m in range(1, n + 1):
        tot = 0
        fall = 1
        for j in range(1, m + 1):
            if j > r:
                tot += fall * a_inf[m - j]
                if mod is not None:
                    tot %= mod
            if j < m:
                fall *= (m - j)
                if mod is not None:
                    fall %= mod
        a_inf[m] = tot if mod is None else (tot % mod)

    results = []
    for k in range(r + 1, n + 1):
        tot = 0
        # t = 0 term is a_inf[n]
        # Each term t >= 0 has integer coefficient C(n, k*t) * (k*t)! / (k^t * t!)
        # Notice coeff(t) is an integer (since it counts t disjoint k-cycles on k*t elements out of n)!
        # Wait: term_coeff = n! // ((n - k*t)! * (k**t) * t!)
        coeff = 1
        for t in range(0, n // k + 1):
            if t > 0:
                # Multiply coeff by prod_{u=0}^{k-1} (n - k*(t-1) - u) // (k * t)
                num = coeff
                for u in range(k):
                    num *= (n - k * (t - 1) - u)
                den = k * t
                assert num % den == 0
                coeff = num // den
            term = coeff * a_inf[n - k * t]
            if t % 2 == 1:
                tot -= term
            else:
                tot += term
            if mod is not None:
                tot %= mod
        results.append(tot if mod is None else (tot % mod))
    return a_inf[n], results


def verify_lemma2_and_theorem2() -> None:
    # 1. Lemma 2.1: Delta(m) = m/16 - (v2(m) + 1) for 65 <= m <= 5000
    zero_ms = []
    le1_non_zero = []
    for m in range(65, 5001):
        d = Fraction(m, 16) - (vp(m, 2) + 1)
        assert d >= 0
        if d == 0:
            zero_ms.append(m)
        elif d <= 1:
            le1_non_zero.append((m, d))
    assert zero_ms == [80, 96, 128]
    assert le1_non_zero == [(72, Fraction(1, 2))]

    # 2. Lemma 2.2: Exhaustive DP on P_{>64}(1248) proving max cost_2 = 75 and unique 4 partitions
    # State at each weight w in 0..1248: best cost and list of partitions achieving >= 75?
    # Even simpler: maintain upper bound! At weight w, remaining = 1248 - w; max remaining cost <= (1248-w)/16 * ?
    # Actually Lemma 2.1 already says for any part m >= 65, ell_m(c) = c(v2(m)+1) - s2(c) <= m*c/16 - s2(c)!
    # So remaining cost from remaining weight R is <= floor(R / 16) - (1 if R > 0 else 0)!
    # Let's STILL verify by pure DP WITHOUT Lemma 2.1: max_cost[w] over parts m >= 65!
    # Wait: DP over parts m = 65..1248 with weights 0..1248:
    # 1184 parts x 1249 weights x ~10 multiplicities = ~500k ops -> < 0.2s!
    NEG_INF = -10**9
    dp = [NEG_INF] * 1249
    dp[0] = 0
    for m in range(65, 1249):
        max_c = 1248 // m
        # Precompute ell_m(c) for c = 1..max_c
        costs = [ell_p(m, c, 2) for c in range(max_c + 1)]
        new_dp = list(dp)
        for w in range(1249):
            base = dp[w]
            if base == NEG_INF:
                continue
            for c in range(1, max_c + 1):
                w2 = w + c * m
                if w2 > 1248:
                    break
                val = base + costs[c]
                if val > new_dp[w2]:
                    new_dp[w2] = val
        dp = new_dp
    assert dp[1248] == 75

    # Now find ALL partitions of 1248 into parts > 64 with cost >= 75 via DFS using suffix DP upper bound?
    # Wait: run DP BACKWARDS to get suffix_max[m][rem] = max cost using parts >= m of weight <= rem? Even simpler:
    # Use the simple exact upper bound on remaining cost: any multiset of parts >= m with total weight R
    # has sum(ell_j(c_j)) <= sum(j * c_j / 16 - s2(c_j)) <= floor(R / 16) (exact by Lemma 2.1 since R >= 0)!
    # Wait: we don't even need Lemma 2.1 if we run DP from m=1248 down to 65 storing max_from_m[rem] = max cost using parts >= m of weight == rem,
    # Wait: 1184 x 1249 ints is 1.4M ints -> we can just build suffix_dp[m] ONLY for active m, or use DP tracking ALL partitions of weight w achieving dp[w] >= 75?
    # Wait: how many states reach 75? Let's check with exact DFS pruned by remaining_weight // 16 (verified above that Delta(m) >= 0 for all m >= 65!):
    top_parts = []

    def dfs_1248(m_idx: int, rem: int, cur_cost: int, cur: list[tuple[int, int]]) -> None:
        if rem == 0:
            if cur_cost >= 75:
                top_parts.append((cur_cost, tuple(cur)))
            return
        if m_idx > rem:
            return
        # Since Delta(m) >= 0 for all m >= 65 and rem > 0 => sum s2(c_j) >= 1,
        # remaining cost from weight rem is <= (rem // 16) - 1!
        if cur_cost + (rem // 16) - 1 < 75:
            return
        for m in range(m_idx, rem + 1):
            for c in range(1, rem // m + 1):
                cur.append((m, c))
                dfs_1248(m + 1, rem - c * m, cur_cost + ell_p(m, c, 2), cur)
                cur.pop()

    dfs_1248(65, 1248, 0, [])
    expected_top = {
        (75, ((96, 13),)),
        (75, ((96, 1), (128, 9))),
        (75, ((80, 6), (96, 8))),
        (75, ((80, 8), (96, 1), (128, 4))),
    }
    assert set(top_parts) == expected_top

    # 3. Direct permutation-recurrence check at n = 1248 (mod 2^{1173}, ZERO partition-bound shortcuts!)
    # Precompute integer coefficients coeff(1248, k, t) = 1248! / ((1248 - k*t)! * k^t * t!) once!
    assert vp_fact(1248, 2) == 1244
    mod2 = 2 ** 1173
    coeffs_1248: dict[int, list[int]] = {}
    for k in range(65, 1249):
        c_list = [1]
        coeff = 1
        for t in range(1, 1248 // k + 1):
            num = coeff
            for u in range(k):
                num *= (1248 - k * (t - 1) - u)
            den = k * t
            assert num % den == 0
            coeff = num // den
            c_list.append(coeff % mod2)
        coeffs_1248[k] = c_list

    for r in range(64, 80):
        a_inf = [0] * 1249
        a_inf[0] = 1
        for m in range(1, 1249):
            tot = 0
            fall = 1
            for j in range(1, m + 1):
                if j > r:
                    tot += fall * a_inf[m - j]
                if j < m:
                    fall = (fall * (m - j)) % mod2
            a_inf[m] = tot % mod2
        assert a_inf[1248] == 0 or vp(a_inf[1248], 2) >= 1170

        v2_G = 1173
        for k in range(r + 1, 1249):
            tot = 0
            for t, c_mod in enumerate(coeffs_1248[k]):
                term = c_mod * a_inf[1248 - k * t]
                tot = (tot - term) if (t % 2 == 1) else (tot + term)
            tot %= mod2
            v_k = vp(tot, 2) if tot != 0 else 1173
            if v_k < v2_G:
                v2_G = v_k
        assert v2_G == 1170, f"Unexpected v2(G_{r}(1248)) = {v2_G}"
        a_96_only = factorial(1248) // ((96 ** 13) * factorial(13))
        assert vp(a_96_only, 2) == 1169
        if r in (64, 79):
            assert a_S_exact_mod(1248, set(range(1, 1249)) - {96}, mod2) == a_96_only % mod2
    print("Theorem 2 & Lemmas 2.1-2.2 (all r in [64..79] at n=1248, exact DP + mod 2^1173 recurrence): PASS")


def verify_lemmas_4_1_to_4_3() -> None:
    # 1. Lemma 4.1: Trade identity & bounds for 0 <= 2t <= Y' <= 45, x0 in {0,1,2}
    for x0 in (0, 1, 2):
        for Yp in range(0, 46):
            for t in range(0, Yp // 2 + 1):
                lhs = ell_p(9, Yp - 2 * t, 3) + ell_p(6, 3 * t + x0, 3)
                delta = vp(comb(Yp, 2 * t), 3) + (vp_fact(2 * t, 3) - vp_fact(t, 3))
                rhs = ell_p(9, Yp, 3) + x0 - delta
                assert lhs == rhs and delta >= 0
                assert (delta == 0) == (t == 0 or (t == 1 and Yp % 3 == 2))
                if t >= 5:
                    assert delta >= 2
                if Yp % 3 == 2:
                    if Yp % 9 == 2:
                        assert (delta <= 1) == (t in (0, 1))
                    elif Yp % 9 == 5:
                        assert (delta <= 1) == (t in (0, 1, 2))
                    else:
                        assert (delta <= 1) == (t in (0, 1, 2, 3, 4))

    # 2. Lemma 4.2(1): ell_m(c) <= (5/36) m c - 1/2 for m >= 4, m not in {6,9}, 1 <= c <= 20
    for m in range(4, 200):
        if m in (6, 9):
            continue
        for c in range(1, 21):
            assert Fraction(ell_p(m, c, 3)) <= Fraction(5 * m * c, 36) - Fraction(1, 2)

    # Compute exact mu_max(w) for w in 0..30 by exhaustive partition enumeration avoiding {6, 9}
    mu_max = [-1] * 31

    def enum_mu(m_idx: int, rem: int, cur_cost: int) -> None:
        if rem == 0:
            if cur_cost > mu_max[target_w]:
                mu_max[target_w] = cur_cost
            return
        if m_idx > rem:
            return
        if m_idx in (6, 9):
            enum_mu(m_idx + 1, rem, cur_cost)
            return
        for c in range(0, rem // m_idx + 1):
            enum_mu(m_idx + 1, rem - c * m_idx, cur_cost + ell_p(m_idx, c, 3))

    for target_w in range(31):
        enum_mu(4, target_w, 0)

    assert [mu_max[w] for w in range(31)] == [
        0, -1, -1, -1, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0,
        1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 3, 2, 2, 3
    ]

    # Check Lemma 4.2(3) table exhaustively
    expected_table = {
        0: ({(0, 0, 0)}, set(), set()),
        1: ({(1, 1, 4)}, {(1, 0, 10), (2, 2, 7)}, set()),
        2: ({(1, 1, 5)}, {(1, 0, 11), (2, 2, 8)}, set()),
        3: ({(1, 2, 0)}, {(1, 0, 12)}, {(2, 1, 15), (2, 2, 9), (3, 2, 18)}),
        4: ({(0, 0, 4)}, {(1, 1, 7)}, set()),
        5: ({(0, 0, 5)}, {(1, 1, 8)}, set()),
        6: ({(0, 1, 0)}, set(), {(1, 0, 15), (1, 1, 9), (2, 1, 18), (2, 2, 12)}),
        7: ({(0, 0, 7), (1, 2, 4)}, {(1, 0, 16), (1, 1, 10)}, set()),
        8: ({(0, 0, 8), (1, 2, 5)}, {(1, 0, 17), (1, 1, 11)}, set()),
    }
    for rho in range(9):
        d_ref = 1 if rho in (1, 2, 3) else 0
        e_rho = (1 if rho in (1, 2, 6) else 0) + (2 if rho == 3 else 0)
        got0, got1, got2 = set(), set(), set()
        for delta in (0, 1, 2):
            d = d_ref + delta
            for x0 in (0, 1, 2):
                w = 9 * d + rho - 6 * x0
                if w < 0 or mu_max[w] == -1:
                    continue
                min_drop = 2 * delta + vp_fact(delta, 3) + e_rho - x0 - mu_max[w]
                assert min_drop >= 0
                if min_drop == 0:
                    got0.add((d, x0, w))
                elif min_drop == 1:
                    got1.add((d, x0, w))
                elif min_drop == 2 and rho in (3, 6):
                    got2.add((d, x0, w))
        assert (got0, got1, got2) == expected_table[rho], f"Table mismatch at rho={rho}: {(got0, got1, got2)}"

    # 3. Lemma 4.3: tau_t(x0, y) and S(x0, y) mod 9 for 5 <= y <= 150, y == 2 mod 3
    for x0 in (1, 2):
        for y in range(5, 150, 3):
            S_val = Fraction(0)
            for t in range(0, y // 2 + 1):
                num = (3 ** t) * falling_fact(y, 2 * t)
                den = (8 ** t) * (falling_fact(x0 + 3 * t, 3 * t) if t > 0 else 1)
                tau = Fraction(num, den)
                assert tau.denominator % 3 != 0
                delta = vp(comb(y, 2 * t), 3) + (vp_fact(2 * t, 3) - vp_fact(t, 3))
                assert vp_frac(tau, 3) == delta
                if t <= 4:
                    S_val += tau
                if t == 1:
                    r_t1 = (1 + tau)
                    r_mod9 = (r_t1.numerator * pow(r_t1.denominator, -1, 9)) % 9
                    assert r_mod9 == (3 if x0 == 1 else 0)
            s_mod9 = (S_val.numerator * pow(S_val.denominator, -1, 9)) % 9
            ym9 = y % 9
            if x0 == 1:
                assert s_mod9 == {2: 3, 5: 0, 8: 6}[ym9]
            else:
                assert s_mod9 == {2: 0, 5: 6, 8: 3}[ym9]
    print("Lemmas 4.1-4.3 (trade identity, mu_max table 0..30, S(x0,y) mod 9): PASS")


def delta3_formula(n: int) -> int:
    if n % 81 == 51 and n >= 51:
        return 2
    if n % 27 in (1, 2, 3, 24) and n % 81 != 51 and n >= 55:
        return 1
    return 0


def delta3G_formula(n: int) -> int:
    if n % 81 in (30, 51) and n >= 51:
        return 2
    if n % 27 in (1, 2, 3, 24) and n % 81 not in (30, 51) and n >= 55:
        return 1
    return 0


def verify_theorems_1_3_4() -> None:
    # 1. Exact check of Theorems 1, 3, 4 on ALL n in 5..40 via exact DP for Lambda_3(n),
    # exact part-set f_P(n) for g_3(n) (and all 2^{n-3} subsets S for 5 <= n <= 16!),
    # and exact integer a_{S_k}(n) for G_3(n)!
    # Plus for n in 41..120: exact integer a_{S_k}(n) for G_3(n), exact DP for Lambda_3(n),
    # and for n in {51, 55, 56, 57, 78, 81, 82, 83, 84, 105, 111} + 5..62 exact f_P(n) check!
    for n in range(5, 65):
        nfact = factorial(n)
        fall3 = falling_fact(n - 1, 3)

        # (a) Brute-force all partitions in P_{>3}(n) (note for n=64, max parts is 16 -> ~100k partitions total if computed cleanly!)
        # Actually at n=64, unrestricted partitions of 64 is ~1.7M; with parts >= 4 it's smaller (~200k).
        # Let's do full partition enumeration for n <= 45 (~20k partitions max!) and for 46..120 use DP + low-valuation f_P!
        if n <= 42:
            f_P: dict[frozenset[int], int] = defaultdict(int)
            lam_vals = []

            def enum_parts(m_idx: int, rem: int, prod_den: int, parts: list[int]) -> None:
                if rem == 0:
                    N_lam = nfact // prod_den
                    lam_vals.append(N_lam)
                    f_P[frozenset(parts)] += N_lam
                    return
                if m_idx > rem:
                    return
                for c in range(0, rem // m_idx + 1):
                    if c == 0:
                        enum_parts(m_idx + 1, rem, prod_den, parts)
                    else:
                        parts.append(m_idx)
                        enum_parts(m_idx + 1, rem - c * m_idx, prod_den * (m_idx ** c) * factorial(c), parts)
                        parts.pop()

            enum_parts(4, n, 1, [])
            Lam3 = gcd(*lam_vals)
            g3 = gcd(*f_P.values())

            # For n <= 16, also directly verify g_3(n) = gcd over ALL 2^{n-3} subsets S >= {1,2,3}
            if n <= 16:
                all_aS = []
                for mask in range(1 << (n - 3)):
                    A_set = [4 + i for i in range(n - 3) if (mask >> i) & 1]
                    tot_S = 0
                    A_fs = set(A_set)
                    for P, val in f_P.items():
                        if P.issubset(A_fs):
                            tot_S += val
                    assert tot_S == a_S_exact_mod(n, set(range(1, n + 1)) - A_fs)
                    all_aS.append(tot_S)
                assert gcd(*all_aS) == g3
        else:
            # Compute exact Lambda_3(n) at p=2 and p=3 via DP (and check q > 3 via exact cost_q DP!)
            # AND compute f_P(n) EXACTLY at p=3 using Proposition 11.3(iv): collect ALL partitions with cost_3 >= kappa_3 - 2!
            Lam3 = None  # We check v_p(Lambda_3(n)) directly per prime p!

        # Exact G_3(n) via exact integer recurrence a_{S_k}(n)
        _, ask_list = a_S_all_k_mod(n, 3, None)
        G3 = gcd(*ask_list)

        exp_v2_ratio = (n - 2) // 4
        exp_L3 = vp(fall3, 3) + (n - 4) // 9 + (n + 2) // 9
        exp_v3_g3 = exp_L3 + delta3_formula(n)
        exp_v3_G3 = exp_L3 + delta3G_formula(n)

        assert vp(G3, 2) == vp(fall3, 2) + exp_v2_ratio
        assert vp(G3, 3) == exp_v3_G3
        # Check primes q in {5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61}
        for q in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61):
            if q <= n:
                assert vp(G3, q) == vp(fall3, q)

        if n <= 42:
            assert vp(Lam3, 2) == vp(G3, 2)
            assert vp(g3, 2) == vp(G3, 2)
            assert vp(Lam3, 3) == exp_L3
            assert vp(g3, 3) == exp_v3_g3
            for q in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41):
                if q <= n:
                    assert vp(Lam3, q) == vp(fall3, q)
                    assert vp(g3, q) == vp(fall3, q)

    # 2. Check G_3(n) AND Proposition 11.3(iv) exact f_P(n) for n in 43..200 at primes 2, 3, 5, 7
    # Using exact mod-3^{exp_v3_G3 + 2} DFS for all partitions of cost >= kappa_3 - 2 (instant!),
    # plus exact mod-2^{v2(G3)+2} for Lambda_3(n) & G_3(n)!
    test_ns = list(range(43, 135)) + [138, 165, 192, 213, 273, 354]
    for n in test_ns:
        fall3 = falling_fact(n - 1, 3)
        exp_v2_G = vp(fall3, 2) + (n - 2) // 4
        exp_L3 = vp(fall3, 3) + (n - 4) // 9 + (n + 2) // 9
        exp_v3_g = exp_L3 + delta3_formula(n)
        exp_v3_G = exp_L3 + delta3G_formula(n)

        mod2_n = 2 ** (exp_v2_G + 3)
        mod3_n = 3 ** (exp_v3_G + 3)
        # Check G_3(n) mod 2^{...} and mod 3^{...}
        _, ask_m2 = a_S_all_k_mod(n, 3, mod2_n)
        _, ask_m3 = a_S_all_k_mod(n, 3, mod3_n)
        assert min(vp(x, 2) if x != 0 else 99999 for x in ask_m2) == exp_v2_G
        assert min(vp(x, 3) if x != 0 else 99999 for x in ask_m3) == exp_v3_G

        # Also check DP max cost at p=2 and p=3 -> Lambda_3(n)
        dp2 = [-10**9] * (n + 1)
        dp3 = [-10**9] * (n + 1)
        dp2[0] = 0
        dp3[0] = 0
        for m in range(4, n + 1):
            max_c = n // m
            c2s = [ell_p(m, c, 2) for c in range(max_c + 1)]
            c3s = [ell_p(m, c, 3) for c in range(max_c + 1)]
            nd2, nd3 = list(dp2), list(dp3)
            for w in range(n + 1):
                b2, b3 = dp2[w], dp3[w]
                for c in range(1, max_c + 1):
                    w2 = w + c * m
                    if w2 > n:
                        break
                    if b2 + c2s[c] > nd2[w2]:
                        nd2[w2] = b2 + c2s[c]
                    if b3 + c3s[c] > nd3[w2]:
                        nd3[w2] = b3 + c3s[c]
            dp2, dp3 = nd2, nd3
        assert vp_fact(n, 2) - dp2[n] == exp_v2_G
        assert vp_fact(n, 3) - dp3[n] == exp_L3

        # Verify v_3(g_3(n)) directly via Proposition 11.3(iv): sum N(lambda) mod 3^{exp_L3 + 3} over all lambda
        # with cost_3(lambda) >= dp3[n] - 2!
        # Wait: bound remaining cost_3 from weight rem using exact suffix?
        # Even simpler: check Theorem 1(b)'s cost_3 <= (5/36) w ? Care: part 6 has 1/6 = 6/36, part 9 has 2/9 = 8/36!
        # So for ANY part m >= 4, ell_m(c) <= (2/9) m c (since for m=9: (2c + (c-s3(c))/2) <= (2.5 c - 0.5) <= 2.5 c / 9 * 9... wait:
        # at m=9, c=9: ell_9(9) = 18 + 4 = 22 <= (22/81)*81, in general v_3(m)+1/2 <= (5/18) m! Check: m=9 => (2+0.5)/9 = 2.5/9 = 5/18!
        # Wait: ell_m(c) = c*v_3(m) + (c - s_3(c))/2 <= c*(v_3(m) + 1/2) - 1/2 <= (5/18)*m*c!
        # Let's double check (v_3(m) + 1/2) / m <= 5/18 for ALL m >= 4:
        # e=0: 0.5/4 = 1/8 < 5/18; e=1 (m>=6): 1.5/6 = 1/4 < 5/18; e=2 (m>=9): 2.5/9 = 5/18; e=3 (m>=27): 3.5/27 < 5/18!
        # YES! So cost_3(remaining weight R) <= (5 * R) // 18!
        if n <= 125:
            threshold_cost = dp3[n] - 2
            f_P_low: dict[frozenset[int], int] = defaultdict(int)
            nfact = factorial(n)
            parts_order = [9, 6] + [m for m in range(4, n + 1) if m not in (6, 9)]

            def dfs_p3(idx: int, rem: int, cur_cost: int, prod_den: int, parts: list[int]) -> None:
                if rem == 0:
                    if cur_cost >= threshold_cost:
                        f_P_low[frozenset(parts)] += (nfact // prod_den)
                    return
                if idx >= len(parts_order):
                    return
                ub = (5 * rem) // 18 if idx < 2 else (5 * rem - 18) // 36
                if cur_cost + ub < threshold_cost:
                    return
                for j in range(idx, len(parts_order)):
                    m = parts_order[j]
                    if m > rem:
                        if j >= 2:
                            break
                        continue
                    for c in range(1, rem // m + 1):
                        parts.append(m)
                        dfs_p3(j + 1, rem - c * m, cur_cost + ell_p(m, c, 3), prod_den * (m ** c) * factorial(c), parts)
                        parts.pop()

            dfs_p3(0, n, 0, 1, [])
            min_v3_fP = min(vp(val, 3) for val in f_P_low.values() if val != 0)
            # Notice if min_v3_fP <= exp_L3 + 2, then v_3(g_3(n)) = min(min_v3_fP, exp_L3 + 3?)
            # Wait: threshold_cost = dp3[n] - 2 corresponds to v_3 = exp_L3 + 2!
            # Any omitted partition has v_3 >= exp_L3 + 3 > exp_v3_g (since exp_v3_g <= exp_L3 + 2 always!).
            assert min_v3_fP == exp_v3_g, f"Mismatch v3(g3({n})): got {min_v3_fP}, expected {exp_v3_g}"

    # 3. Check Kallat Theorem 11.1 numbers at n = 111, 192, 273, 354 + rational fractions in Case 2a, 4d, 4f
    _, ask_111 = a_S_all_k_mod(111, 3, None)
    G3_111 = gcd(*ask_111)
    assert G3_111 == 147259794302866275623239680
    assert vp(G3_111, 3) == 28
    assert vp(a_S_exact_mod(111, set(range(1, 112)) - {4, 9}), 3) == 27
    for n_cex, exp_v in ((111, 27), (192, 45), (273, 63), (354, 81)):
        assert vp(a_S_exact_mod(n_cex, set(range(1, n_cex + 1)) - {4, 9}), 3) == exp_v
        _, ask_c = a_S_all_k_mod(n_cex, 3, 3 ** (exp_v + 3))
        assert min(vp(x, 3) if x != 0 else exp_v + 3 for x in ask_c) == exp_v + 1

    assert Fraction(1, 8) + Fraction(1, (4 ** 2) * 2) == Fraction(5, 32)
    assert Fraction(1, (4 ** 3) * 6) + Fraction(1, 12) == Fraction(11, 128)
    assert 1 + Fraction(12, (4 ** 3) * 6) == Fraction(33, 32)
    assert Fraction(1, 12) + Fraction(1, (4 ** 3) * 6) + Fraction(1, 35) + Fraction(1, 32) == Fraction(653, 4480)
    print("Theorems 1, 3, 4 (all n in 5..134 + {138,165,192,213,273,354}): PASS")


def main() -> None:
    verify_lemma2_and_theorem2()
    verify_lemmas_4_1_to_4_3()
    verify_theorems_1_3_4()
    print("PASS")


if __name__ == "__main__":
    main()
