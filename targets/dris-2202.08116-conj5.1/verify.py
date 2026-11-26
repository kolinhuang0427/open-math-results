import math
from fractions import Fraction
import sympy as sp

def sigma_int(n: int) -> int:
    return int(sp.divisor_sigma(n, 1))

def in_A(m: int) -> bool:
    s = sigma_int(m * m)
    return math.gcd(m, s) == math.gcd(m * m, s)

def padic_val(n: int, p: int) -> int:
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v

def verify_lemma1():
    primes_1_mod_6 = [p for p in sp.primerange(7, 200) if p % 6 == 1]
    for p in primes_1_mod_6:
        roots = [u for u in range(p) if (u * u + u + 1) % p == 0]
        assert len(roots) == 2, f"Expected 2 roots mod {p}, got {roots}"
        assert all(2 <= r <= p - 2 for r in roots), f"Unexpected root range mod {p}: {roots}"

    # Check Lemma 1(3) exhaustively for m <= 5000 and p in {7, 13, 19}
    test_primes = [7, 13, 19]
    root_map = {p: {u for u in range(p) if (u * u + u + 1) % p == 0} for p in test_primes}
    triggered = 0
    for m in range(1, 5001):
        fac = sp.factorint(m)
        for p in test_primes:
            if fac.get(p, 0) == 1:
                q_hits = [q for q, e in fac.items() if e == 1 and (q % p) in root_map[p]]
                if len(q_hits) >= 2:
                    triggered += 1
                    assert not in_A(m), f"Lemma 1 failed at m={m}, p={p}, q_hits={q_hits}"
    assert triggered >= 10
    print(f"Lemma 1 verified (primes 7..199 have 2 roots; {triggered} triggers in m<=5000 all not in A).")

def verify_lemma2():
    # Check exact CRT density of E_k over one full period M_k for k=1 (p=7) and k=2 (p=7, 13)
    for plist in ([7], [7, 13]):
        M = 1
        for p in plist:
            M *= p * p
        count_in_E = 0
        for m in range(1, M + 1):
            ok = True
            for p in plist:
                if m % p == 0 and m % (p * p) != 0:
                    ok = False
                    break
            if ok:
                count_in_E += 1
        expected = Fraction(1)
        for p in plist:
            expected *= Fraction(p * p - (p - 1), p * p)
        assert Fraction(count_in_E, M) == expected, f"Mismatch for {plist}: {count_in_E}/{M} vs {expected}"
    print("Lemma 2 verified (exact CRT periodic density of E_k matches product formula for {7} and {7,13}).")

def verify_lemma3_moments():
    # For p = 7, Q_7 has roots {2, 4} mod 7. Smallest primes in Q_7: 2, 11, 23, 37.
    # Use Q(P) = {2, 11, 23} so N_P = 4 * 121 * 529 = 256036 (fast exact period check!).
    p = 7
    roots = {u for u in range(p) if (u * u + u + 1) % p == 0}
    assert roots == {2, 4}
    Q_P = [q for q in sp.primerange(2, 25) if (q % p) in roots]
    assert Q_P == [2, 11, 23], f"Got {Q_P}"
    N_P = 1
    for q in Q_P:
        N_P *= q * q

    alphas = [Fraction(q - 1, q * q) for q in Q_P]
    S_P = sum(alphas)
    expected_var = sum(a * (1 - a) for a in alphas)

    sum_f = 0
    sum_f2 = 0
    count_le_1 = 0
    for m in range(1, N_P + 1):
        val = 0
        for q in Q_P:
            if m % q == 0 and m % (q * q) != 0:
                val += 1
        sum_f += val
        sum_f2 += val * val
        if val <= 1:
            count_le_1 += 1

    mean_f = Fraction(sum_f, N_P)
    var_f = Fraction(sum_f2, N_P) - mean_f * mean_f
    assert mean_f == S_P, f"Mean mismatch: {mean_f} vs {S_P}"
    assert var_f == expected_var, f"Var mismatch: {var_f} vs {expected_var}"
    assert var_f <= S_P
    print(f"Lemma 3 exact periodic moments verified on N_P={N_P} (Q_P={Q_P}): E[f]={mean_f}, Var(f)={var_f} <= S(P).")

def verify_paper_counts():
    # Match Dris's table for N=10, 100, 1000 (lines 352-354 of main.tex)
    cnt10 = sum(1 for m in range(1, 11) if in_A(m))
    cnt100 = sum(1 for m in range(1, 101) if in_A(m))
    cnt1000 = sum(1 for m in range(1, 1001) if in_A(m))
    assert (cnt10, cnt100, cnt1000) == (10, 99, 974), f"Got {(cnt10, cnt100, cnt1000)}"
    print(f"Dris Section 5 counts verified: N=10->{cnt10}, N=100->{cnt100}, N=1000->{cnt1000}.")

if __name__ == "__main__":
    verify_lemma1()
    verify_lemma2()
    verify_lemma3_moments()
    verify_paper_counts()
    print("PASS")
