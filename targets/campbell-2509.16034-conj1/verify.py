#!/usr/bin/env python3
"""Exact verification script for campbell-2509.16034-conj1 (PROOF.md)."""
import sys


def tm(k: int) -> int:
    """1-based Thue-Morse sequence: t_k = popcount(k - 1) mod 2 for k >= 1."""
    if k < 1:
        raise ValueError("k must be >= 1")
    return (k - 1).bit_count() & 1


def expected_factor_complexity_tm(n: int) -> int:
    """Exact factor complexity rho_t(n) (OEIS A005942) for n >= 1."""
    cache = {1: 2, 2: 4, 3: 6}

    def f(x: int) -> int:
        if x in cache:
            return cache[x]
        if x % 2 == 0:
            res = f(x // 2) + f(x // 2 + 1)
        else:
            res = 2 * f((x - 1) // 2 + 1)
        cache[x] = res
        return res

    return f(n)


def main() -> int:
    try:
        # 1. Direct verification from factors of Thue-Morse prefix (n = 1..120)
        L = 20000
        t = [tm(i) for i in range(1, L + 1)]
        for n in range(1, 121):
            factors = set()
            val = 0
            mask = (1 << n) - 1
            for i in range(L):
                val = ((val << 1) | t[i]) & mask
                if i >= n - 1:
                    factors.add(val)
            assert len(factors) == expected_factor_complexity_tm(n), f"Missing factors at n={n}"

        alt_pref = [0] * L
        for i in range(1, L):
            alt_pref[i] = alt_pref[i - 1] + (1 if t[i] != t[i - 1] else 0)

        direct_m, direct_M, direct_rho = {}, {}, {}
        for n in range(1, 121):
            seen_pairs = set()
            ab_classes = set()
            for start in range(0, L - n + 1):
                runs = 1 + (alt_pref[start + n - 1] - alt_pref[start])
                first = t[start]
                seen_pairs.add((first, runs))
                if runs % 2 == 0:
                    ab_classes.add((runs // 2, runs // 2))
                else:
                    ab_classes.add((runs // 2 + (1 - first), runs // 2 + first))
            alts = [r - 1 for (_, r) in seen_pairs]
            mn, Mn = min(alts), max(alts)
            assert len(seen_pairs) == 2 * (Mn - mn + 1), f"Gap in (first, runs) at n={n}"
            direct_m[n], direct_M[n], direct_rho[n] = mn, Mn, len(ab_classes)

            # Check Theorem 1 exact formula (using integer arithmetic)
            sum_formula = sum(1 + (r % 2) for r in range(mn + 1, Mn + 2))
            closed_num = 6 * (Mn - mn + 1) + (1 if mn % 2 == 0 else -1) + (1 if Mn % 2 == 0 else -1)
            assert closed_num % 4 == 0
            assert direct_rho[n] == sum_formula == closed_num // 4

        # Check paper's published first 19 terms (equation numericalproblem)
        paper_first_19 = [2, 3, 3, 4, 3, 5, 4, 5, 3, 4, 5, 6, 4, 6, 5, 4, 3, 5, 4]
        assert [direct_rho[n] for n in range(1, 20)] == paper_first_19

        # 2. Compute m_n, M_n via Lemmas 2 & 3 up to N = 40010 and verify against direct_m/M for n<=120
        N = 40010
        m = [0] * (N + 1)
        M = [0] * (N + 1)
        m[1], M[1] = 0, 0
        m[2], M[2] = 0, 1
        m[3], M[3] = 1, 2
        for k in range(4, N + 1):
            if k % 2 == 0:
                j = k // 2
                m[k] = 2 * j - 1 - M[j + 1]
                M[k] = 2 * j - 1 - m[j]
            else:
                j = (k - 1) // 2
                m[k] = 2 * j - M[j + 1]
                M[k] = 2 * j - m[j + 1]

        for n in range(1, 121):
            assert m[n] == direct_m[n] and M[n] == direct_M[n]

        # 3. Verify Theorem 2 & Theorem 3 for n up to 10000
        def rho(k: int) -> int:
            num = 6 * (M[k] - m[k] + 1) + (1 if m[k] % 2 == 0 else -1) + (1 if M[k] % 2 == 0 else -1)
            return num // 4

        for n in range(0, 10001):
            if n == 0:
                assert rho(1) == rho(1)
            else:
                assert rho(2 * n + 1) == rho(n + 1)

        for n in range(1, 10001):
            r4n = rho(4 * n)
            r4n2 = rho(4 * n + 2)
            rn1 = rho(n + 1)
            assert r4n == rn1 + 1 + (m[n + 1] % 2)
            assert r4n2 == rn1 + 1 + (M[n + 1] % 2)
            assert r4n2 - r4n == (M[n + 1] % 2) - (m[n + 1] % 2)
            expected_abs = 0 if tm(n + 1) == tm(3 * n + 1) else 1
            assert abs(r4n2 - r4n) == expected_abs

        # 4. Verify coupled mod-2 recurrence & unboundedness sequence n_j
        alpha = [m[k] % 2 for k in range(N + 1)]
        beta = [M[k] % 2 for k in range(N + 1)]
        for j in range(2, N // 2):
            assert alpha[2 * j] == 1 - beta[j + 1]
            assert beta[2 * j] == 1 - alpha[j]
            assert alpha[2 * j + 1] == beta[j + 1]
            assert beta[2 * j + 1] == alpha[j + 1]

        nj = 2
        for step in range(8):
            assert rho(nj) >= 3 + step
            nj = 4 * (nj - 1)

        print("PASS")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
