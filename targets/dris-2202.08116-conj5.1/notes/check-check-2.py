"""Independent exact-arithmetic test script for Proof of Conjecture 5.1 (arXiv:2202.08116v1).

Tests Lemma 1, Lemma 2, Lemma 3 (exact CRT moments & Chebyshev bound),
Conclusion inequalities, and Dris's primary-source table counts using exact
integer and Fraction arithmetic (zero floating point).
"""

from __future__ import annotations

import math
import signal
import sys
import time
from fractions import Fraction


class TimeoutError(Exception):
    pass


def _alarm_handler(signum, frame):
    raise TimeoutError("Check script exceeded built-in time limit")


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def factorize(n: int) -> dict[int, int]:
    fac: dict[int, int] = {}
    d = 2
    x = n
    while d * d <= x:
        while x % d == 0:
            fac[d] = fac.get(d, 0) + 1
            x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        fac[x] = fac.get(x, 0) + 1
    return fac


def sigma_of_square_sieve(limit: int) -> list[int]:
    """Compute sigma(m^2) exactly for 1 <= m <= limit via prime-power multiplicativity."""
    spf = list(range(limit + 1))
    for i in range(2, math.isqrt(limit) + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i

    sig2 = [1] * (limit + 1)
    for m in range(2, limit + 1):
        x = m
        val = 1
        while x > 1:
            p = spf[x]
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            # sigma(p^(2e)) = (p^(2e+1) - 1) // (p - 1)
            val *= (pow(p, 2 * e + 1) - 1) // (p - 1)
        sig2[m] = val
    return sig2


def roots_u2_u_1_mod_p(p: int) -> list[int]:
    return [u for u in range(p) if (u * u + u + 1) % p == 0]


def main() -> int:
    signal.signal(signal.SIGALRM, _alarm_handler)
    signal.alarm(45)
    t0 = time.monotonic()

    # 1. Check Dris primary-source table (main.tex lines 352-355) up to 10^4
    limit = 10000
    sig2 = sigma_of_square_sieve(limit)
    in_A = [False] * (limit + 1)
    for m in range(1, limit + 1):
        g1 = math.gcd(m, sig2[m])
        g2 = math.gcd(m * m, sig2[m])
        in_A[m] = (g1 == g2)

    expected_counts = {10: 10, 100: 99, 1000: 974, 10000: 9561}
    for cap, exp in expected_counts.items():
        got = sum(1 for m in range(1, cap + 1) if in_A[m])
        assert got == exp, f"Count mismatch at {cap}: got {got}, expected {exp}"
    print(f"Primary-source table counts verified up to {limit}: {expected_counts}")

    # 2. Check Lemma 1 for all primes p == 1 (mod 6) up to 200
    primes_1mod6 = [p for p in range(7, 200, 6) if is_prime(p)]
    roots_map: dict[int, tuple[int, int]] = {}
    for p in primes_1mod6:
        rts = roots_u2_u_1_mod_p(p)
        assert len(rts) == 2, f"Expected 2 roots mod {p}, got {rts}"
        r_p, s_p = rts[0], rts[1]
        assert 2 <= r_p < s_p <= p - 2, f"Roots out of {{2..p-2}} for p={p}: {rts}"
        assert p not in (r_p, s_p)
        # Check conclusion inequality (p-1)/p^2 >= 1/(2p)
        assert Fraction(p - 1, p * p) >= Fraction(1, 2 * p)
        roots_map[p] = (r_p, s_p)

    # Verify Lemma 1 implication on all m <= 10000 for first 6 primes 1 mod 6
    small_primes = [p for p in range(2, limit + 1) if is_prime(p)]
    q_sets: dict[int, set[int]] = {}
    for p in primes_1mod6[:6]:
        r_p, s_p = roots_map[p]
        q_sets[p] = {q for q in small_primes if q % p in (r_p, s_p)}
        assert p not in q_sets[p]

    lemma1_hits = 0
    for m in range(1, limit + 1):
        fac = factorize(m)
        for p in primes_1mod6[:6]:
            if fac.get(p, 0) == 1:
                q_exact_1 = [q for q in fac if fac[q] == 1 and q in q_sets[p]]
                if len(q_exact_1) >= 2:
                    assert not in_A[m], f"Lemma 1 failed at m={m}, p={p}, qs={q_exact_1}"
                    lemma1_hits += 1
                    break
    print(f"Lemma 1 verified on m <= {limit} ({lemma1_hits} excluded integers all satisfy m not in A)")

    # 3. Check Lemma 2: covering A <= E_k U union B_i and exact density of E_k over M_k
    for k in (1, 2, 3):
        pk_list = primes_1mod6[:k]
        # Verify A cap [1..limit] subset E_k U union B_i
        for m in range(1, limit + 1):
            if not in_A[m]:
                continue
            fac = factorize(m)
            in_Ek = all(fac.get(p, 0) != 1 for p in pk_list)
            in_some_Bi = any(
                sum(1 for q, e in fac.items() if e == 1 and q in q_sets[p]) <= 1
                for p in pk_list
            )
            assert in_Ek or in_some_Bi, f"Lemma 2 covering failed at k={k}, m={m}"

        # Exact period check for k=1 (M_1=49) and k=2 (M_2=8281)
        if k <= 2:
            M_k = 1
            expected_dens = Fraction(1, 1)
            for p in pk_list:
                M_k *= p * p
                expected_dens *= Fraction(p * p - (p - 1), p * p)
            cnt_Ek = 0
            for m in range(1, M_k + 1):
                if all((m % (p * p)) % p != 0 or (m % (p * p)) == 0 for p in pk_list):
                    cnt_Ek += 1
            got_dens = Fraction(cnt_Ek, M_k)
            assert got_dens == expected_dens, f"E_{k} density mismatch: {got_dens} vs {expected_dens}"
            print(f"Lemma 2 exact period check k={k} (M_{k}={M_k}): d(E_{k}) = {got_dens}")

    # 4. Check Lemma 3 exact CRT moments and Chebyshev inequality for p=7
    # Q_7 = {q prime : q % 7 in {2, 4}} = {2, 11, 23, 37, 53, ...}
    # Check exact CRT moments on Q_7(23) = [2, 11, 23] (N_P = 4*121*529 = 256036)
    # Note S(23) = 1/4 + 10/121 + 22/529 = 0.374... (< 1), so also test a small
    # artificial set of 3 primes? Wait: we must test Q_p itself! For Q_7(23),
    # exact E[f_P] = S(P) and exact Var(f_P) = sum alpha_q(1-alpha_q) hold identically!
    q7_23 = [2, 11, 23]
    N_P = 1
    for q in q7_23:
        N_P *= q * q
    assert N_P == 256036

    sum_f = 0
    sum_f2 = 0
    count_le1 = 0
    for m in range(1, N_P + 1):
        f_val = 0
        for q in q7_23:
            r = m % (q * q)
            if r != 0 and r % q == 0:
                f_val += 1
        sum_f += f_val
        sum_f2 += f_val * f_val
        if f_val <= 1:
            count_le1 += 1

    mean_exact = Fraction(sum_f, N_P)
    var_exact = Fraction(sum_f2, N_P) - mean_exact * mean_exact

    expected_mean = sum(Fraction(q - 1, q * q) for q in q7_23)
    expected_var = sum(
        Fraction(q - 1, q * q) * (1 - Fraction(q - 1, q * q)) for q in q7_23
    )
    assert mean_exact == expected_mean, f"Mean mismatch: {mean_exact} vs {expected_mean}"
    assert var_exact == expected_var, f"Var mismatch: {var_exact} vs {expected_var}"
    assert var_exact <= expected_mean
    print(f"Lemma 3 exact CRT check on Q_7(23) (N_P={N_P}): E[f]={mean_exact}, Var(f)={var_exact}, d(B~)={Fraction(count_le1, N_P)}")

    # Also verify exact Chebyshev bound via exact Fraction DP when S(P) > 1
    # (For Q_7, sum (q-1)/q^2 ~ (1/3) ln ln P diverges via Dirichlet's theorem, reaching > 1
    # around P ~ e^{e^3}; here we verify exact CRT-product distribution & Chebyshev on
    # a 12-prime independent Bernoulli set with sum alpha_q > 1, and confirm growth of S_7(P).)
    primes_up_to = [x for x in range(2, 10000) if is_prime(x)]
    q7_all = [q for q in primes_up_to if q % 7 in (2, 4)]
    s7 = sum(Fraction(q - 1, q * q) for q in q7_all)
    assert s7 > Fraction(1, 2)

    # Exact DP for sum of independent Bernoulli((q-1)/q^2) on primes up to 41 (sum > 1.15)
    test_primes = [q for q in range(2, 42) if is_prime(q)]
    dist_dp: dict[int, Fraction] = {0: Fraction(1, 1)}
    for q in test_primes:
        alpha = Fraction(q - 1, q * q)
        one_minus = 1 - alpha
        nxt: dict[int, Fraction] = {}
        for k_val, prob in dist_dp.items():
            nxt[k_val] = nxt.get(k_val, Fraction(0, 1)) + prob * one_minus
            nxt[k_val + 1] = nxt.get(k_val + 1, Fraction(0, 1)) + prob * alpha
        dist_dp = nxt
    mu = sum(k_val * p_val for k_val, p_val in dist_dp.items())
    var = sum((k_val - mu) ** 2 * p_val for k_val, p_val in dist_dp.items())
    p_le_1 = dist_dp.get(0, Fraction(0, 1)) + dist_dp.get(1, Fraction(0, 1))
    assert mu > 1
    assert var == sum(Fraction(q - 1, q * q) * (1 - Fraction(q - 1, q * q)) for q in test_primes)
    assert p_le_1 <= var / ((mu - 1) ** 2) <= mu / ((mu - 1) ** 2)
    print(f"Lemma 3 Chebyshev bound verified in exact Fraction DP (13 primes, E={mu}, P(<=1) <= Var/(E-1)^2 <= E/(E-1)^2)")

    elapsed = time.monotonic() - t0
    print(f"PASS (all exact checks passed in {elapsed:.3f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
