"""Independent exact-arithmetic checker for targets/benfield-2407.20048-conj4.33/."""

from math import gcd, lcm
import sys


def pisano_invariants(K: int, m: int) -> tuple[int, int, int]:
    """
    Directly compute (pi_K(m), alpha_K(m), omega_K(m)) by simulating
    F_{K,0}=0, F_{K,1}=1, F_{K,n} = K*F_{K,n-1} + F_{K,n-2} (mod m).
    """
    seen = {}
    seq = []
    f0, f1 = 0 % m, 1 % m
    idx = 0
    while (f0, f1) not in seen:
        seen[(f0, f1)] = idx
        seq.append(f0)
        f0, f1 = f1, (K * f1 + f0) % m
        idx += 1
    assert seen[(f0, f1)] == 0, f"Not purely periodic at K={K}, m={m}"
    pi = len(seq)
    alpha = next(i for i in range(1, pi + 1) if (seq[i] if i < pi else 0) == 0)
    omega = seq.count(0)
    return pi, alpha, omega


def v2(n: int) -> int:
    assert n > 0
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def check_identities():
    for K in range(-10, 21, 2):
        F = [0, 1]
        L = [2, K]
        for n in range(2, 41):
            F.append(K * F[-1] + F[-2])
            L.append(K * L[-1] + L[-2])
        # F_{n+1}*F_{n-1} - F_n^2 = (-1)^n (with F_{-1}=1)
        for n in range(1, 40):
            fm1 = 1 if n == 0 else F[n - 1]
            assert F[n + 1] * fm1 - F[n] ** 2 == (-1) ** n
        # F_{2r} = F_r * L_r, L_{2r} = L_r^2 - 2(-1)^r === 2 (mod 4)
        for r in range(1, 20):
            assert F[2 * r] == F[r] * L[r]
            assert L[2 * r] == L[r] ** 2 - 2 * ((-1) ** r)
            assert L[2 * r] % 4 == 2


def check_lemmas():
    # Lemma 1(1)-(3) and Lemma 3 for even K in [-10, 20]
    for K in range(-10, 21, 2):
        # Lemma 3: powers of 2
        for x in range(1, 8):
            m = 1 << x
            pi, alpha, omega = pisano_invariants(K, m)
            assert omega == 1
            assert pi == alpha
            assert (alpha & (alpha - 1)) == 0 and alpha >= 2

        # Lemma 1(3) and Lemma 2 for odd n in [3, 100]
        for n in range(3, 100, 2):
            pi, alpha, omega = pisano_invariants(K, n)
            assert omega in (1, 2, 4)
            assert pi == alpha * omega
            # beta = F_{K, alpha+1} mod n
            f0, f1 = 0, 1
            for _ in range(alpha):
                f0, f1 = f1, (K * f1 + f0) % n
            beta = f1
            assert (beta * beta - ((-1) ** alpha)) % n == 0
            # Check order of beta mod n == omega
            ord_b = 1
            cur = beta % n
            while cur != 1:
                cur = (cur * beta) % n
                ord_b += 1
            assert ord_b == omega

            # Lemma 2 claims
            assert (omega == 4) == ((alpha % 4) in (1, 3))
            if omega == 2:
                assert pi % 4 == 0 and alpha % 2 == 0
            if pi % 4 != 0:
                assert omega == 1

        # Lemma 1(4): lcm relations for a, b in [2, 25]
        cache = {m: pisano_invariants(K, m) for m in range(2, 26)}
        for a in range(2, 26):
            for b in range(a, 26):
                L = lcm(a, b)
                pi_L, al_L, _ = pisano_invariants(K, L)
                assert al_L == lcm(cache[a][1], cache[b][1])
                assert pi_L == lcm(cache[a][0], cache[b][0])


def check_conjecture_sweep():
    count = 0
    seen_subcases = set()
    for K in range(-10, 41, 2):
        for m in range(4, 251):
            pi, alpha, omega = pisano_invariants(K, m)
            # Bullet 1: omega == 4 iff alpha === +-1 (mod 4)
            assert (omega == 4) == ((alpha % 4) in (1, 3)), f"Bullet 1 failed at K={K}, m={m}"
            # Bullet 2: omega == 2 => 4 | pi and 2 | alpha
            if omega == 2:
                assert pi % 4 == 0 and alpha % 2 == 0, f"Bullet 2 failed at K={K}, m={m}"
            # Bullet 3: 4 \nmid pi => omega == 1
            if pi % 4 != 0:
                assert omega == 1, f"Bullet 3 failed at K={K}, m={m}"

            # Track coverage of Case 1, Case 2, and all subcases of Case 3
            if m % 2 == 1:
                seen_subcases.add("case1_odd")
            elif (m & (m - 1)) == 0:
                seen_subcases.add("case2_pow2")
            else:
                n = m >> v2(m)
                _, al_n, om_n = pisano_invariants(K, n)
                _, al_2x, _ = pisano_invariants(K, m // n)
                a = v2(al_2x)
                v = v2(al_n)
                if om_n == 1:
                    seen_subcases.add("case3_om1")
                elif om_n == 2:
                    seen_subcases.add("case3_om2_alev" if a <= v else "case3_om2_agtv")
                elif om_n == 4:
                    seen_subcases.add("case3_om4_a1" if a == 1 else "case3_om4_age2")
            count += 1

    expected = {
        "case1_odd",
        "case2_pow2",
        "case3_om1",
        "case3_om2_alev",
        "case3_om2_agtv",
        "case3_om4_a1",
        "case3_om4_age2",
    }
    assert seen_subcases == expected, f"Missing subcases: {expected - seen_subcases}"
    return count


def main():
    check_identities()
    check_lemmas()
    cnt = check_conjecture_sweep()
    print(f"PASS (Lemmas 1-3 + all 7 proof subcases verified across {cnt} even-(K,m) pairs)")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
