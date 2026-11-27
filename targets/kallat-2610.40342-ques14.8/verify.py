#!/usr/bin/env python3
"""Exact-arithmetic verifier for counterexamples to arXiv:2610.40342v1 Question 14.8."""

import math


def compute_a_recurrence(allowed_set, max_n):
    """Compute a_A(0..max_n) via the exact recurrence a(n+1) = sum_{m in A} (n)_{m-1} a(n+1-m)."""
    a = [0] * (max_n + 1)
    a[0] = 1
    for n in range(max_n):
        total = 0
        falling = 1
        for m in range(1, n + 2):
            if m in allowed_set:
                total += falling * a[n + 1 - m]
            falling *= (n - m + 1)
        a[n + 1] = total
    return a


def verify_egf_two_parts(m_part, max_n):
    """Compute a_{1, m_part}(n) directly from the exact binomial sum."""
    out = []
    for n in range(max_n + 1):
        s = 0
        for j in range(n // m_part + 1):
            num = math.factorial(m_part * j)
            den = (m_part ** j) * math.factorial(j)
            assert num % den == 0
            s += math.comb(n, m_part * j) * (num // den)
        out.append(s)
    return out


def verify_egf_single_part(m_part, max_n):
    """Compute a_{m_part}(n) directly from (mk)! / (m^k k!)."""
    out = []
    for n in range(max_n + 1):
        if n % m_part != 0:
            out.append(0)
        else:
            k = n // m_part
            num = math.factorial(m_part * k)
            den = (m_part ** k) * math.factorial(k)
            assert num % den == 0
            out.append(num // den)
    return out


def exact_least_period_on_prefix(seq):
    """Find least positive period d on a sequence whose period divides len(seq)//2."""
    half = len(seq) // 2
    for d in range(1, half + 1):
        if all(seq[i] == seq[i + d] for i in range(len(seq) - d)):
            return d
    raise AssertionError("No period found in prefix")


def main():
    max_n = 150

    # 1. Non-constant, odd prime p=3, e=3 (mod 27), sign +: A = {1, 7}
    a17_rec = compute_a_recurrence({1, 7}, max_n)
    a17_egf = verify_egf_two_parts(7, max_n)
    assert a17_rec == a17_egf, "Recurrence and EGF disagree for A={1,7}"
    expected_block_17 = [1, 1, 1, 1, 1, 1, 1, 19, 10]
    mod27 = [x % 27 for x in a17_rec]
    for n, val in enumerate(mod27):
        assert val == expected_block_17[n % 9], f"A={{1,7}} failed at n={n}"
        assert val == (1 - 9 * math.comb(n, 7)) % 27
    assert exact_least_period_on_prefix(mod27) == 9
    assert 9 < 27
    print("Check 1 (A={1,7}, p=3, e=3, mod 27, least period 9 < 27): PASS")

    # 2. Non-constant, odd prime p=5, e=2 (mod 25), sign -: A = {5}
    a5_rec = compute_a_recurrence({5}, max_n)
    a5_egf = verify_egf_single_part(5, max_n)
    assert a5_rec == a5_egf, "Recurrence and EGF disagree for A={5}"
    expected_block_5 = [1, 0, 0, 0, 0, 24, 0, 0, 0, 0]
    mod25 = [x % 25 for x in a5_rec]
    for n, val in enumerate(mod25):
        assert val == expected_block_5[n % 10], f"A={{5}} failed at n={n}"
    assert exact_least_period_on_prefix(mod25) == 10
    assert 10 < 50
    print("Check 2 (A={5}, p=5, e=2, mod 25, least period 10 < 50): PASS")

    # Also check Wilson prime p=13 for A={13} mod 169 on 0 <= n <= 52
    a13_egf = verify_egf_single_part(13, 52)
    mod169 = [x % 169 for x in a13_egf]
    for n, val in enumerate(mod169):
        if n % 13 != 0:
            assert val == 0
        else:
            assert val == (168 if (n // 13) % 2 == 1 else 1)
    assert exact_least_period_on_prefix(mod169) == 26
    assert 26 < 2 * 169
    print("Check 2b (Wilson prime p=13, A={13}, mod 169, least period 26 < 338): PASS")

    # 3. Non-constant, p=2, e=2 (mod 4), sign +: A = {2, 4}
    a24_rec = compute_a_recurrence({2, 4}, max_n)
    mod4 = [x % 4 for x in a24_rec]
    for n, val in enumerate(mod4):
        assert val == (1 if n % 2 == 0 else 0), f"A={{2,4}} failed at n={n}"
    assert exact_least_period_on_prefix(mod4) == 2
    assert 2 < 4
    print("Check 3 (A={2,4}, p=2, e=2, mod 4, least period 2 < 4): PASS")

    # 4. Constant-residue families: A={1} and A={1, 10} mod 27
    a1_rec = compute_a_recurrence({1}, max_n)
    assert all(x == 1 for x in a1_rec)
    a110_rec = compute_a_recurrence({1, 10}, max_n)
    a110_egf = verify_egf_two_parts(10, max_n)
    assert a110_rec == a110_egf
    assert all(x % 27 == 1 for x in a110_rec)
    assert exact_least_period_on_prefix([x % 27 for x in a110_rec]) == 1
    print("Check 4 (A={1} and A={1,10} mod 27, least period 1 < 27): PASS")

    print("PASS")


if __name__ == "__main__":
    main()
