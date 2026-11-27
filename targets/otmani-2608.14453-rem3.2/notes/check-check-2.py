"""Independent exact-arithmetic checker for targets/otmani-2608.14453-rem3.2/PROOF.md."""

from fractions import Fraction
from math import comb
import sys
import sympy as sp


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def clf_numbers(k_max: int) -> list[int]:
    """Compute P_k via the second exact formula and cross-check first formula + recurrence."""
    P = []
    for k in range(k_max + 1):
        val2 = (2**k) * sum(comb(k, 2 * m) * (comb(2 * m, m) ** 2) * (4 ** (k - 2 * m)) for m in range(k // 2 + 1))
        if k <= 40:
            val1 = Fraction(0)
            for j in range(k + 1):
                val1 += Fraction((comb(2 * j, j) ** 2) * (comb(2 * k - 2 * j, k - j) ** 2), comb(k, j))
            assert val1.denominator == 1 and int(val1) == val2, f"CLF formula mismatch at k={k}"
        if k >= 2:
            lhs = (k**2) * val2
            rhs = 8 * (3 * k * k - 3 * k + 1) * P[k - 1] - 128 * ((k - 1) ** 2) * P[k - 2]
            assert lhs == rhs, f"CLF recurrence failed at k={k}"
        P.append(val2)
    assert P[0] == 1 and P[1] == 8
    return P


def check_symbolic_operator_and_telescoping():
    # Verify (1+x) L_A = -x L_G identically on polynomials of degree 5 (in D^2, D, 1)
    x = sp.Symbol("x")
    y = 1 + x
    # Coefficients of D^2, D, 1 in L_G and L_A from PROOF.md lines 98-99:
    LG_d2 = y**2 * (2 - 3 * y + y**2)
    LG_d1 = y * (2 - 6 * y + 3 * y**2)
    LG_d0 = y * (y - 1)
    assert sp.expand(LG_d2 - (1 + x) ** 2 * x * (x - 1)) == 0
    assert sp.expand(LG_d1 - (1 + x) * (3 * x**2 - 1)) == 0
    assert sp.expand(LG_d0 - x * (1 + x)) == 0

    LA_d2 = x**2 * (1 - x**2)
    LA_d1 = x * (1 - 3 * x**2)
    LA_d0 = -(x**2)
    assert sp.expand((1 + x) * LA_d2 + x * LG_d2) == 0
    assert sp.expand((1 + x) * LA_d1 + x * LG_d1) == 0
    assert sp.expand((1 + x) * LA_d0 + x * LG_d0) == 0

    # Verify exact Staver identity (Lemma 6(1)) for M = 0..30
    for M in range(31):
        TM = sum(Fraction(1, comb(M, k) ** 2) for k in range(M + 1))
        lhs = Fraction(2 * (2 * M + 3) * comb(2 * M + 2, M + 1), (M + 1) ** 2) * TM
        rhs = 6 * sum(Fraction(comb(2 * r, r), r) for r in range(1, M + 2))
        assert lhs == rhs, f"Staver identity failed at M={M}"

    # Verify exact Apery identity (Lemma 6(3)) for m = 1..30
    for m in range(1, 31):
        lhs = sum(Fraction((-1) ** k, (k**2) * comb(m, k) * comb(m + k, k)) for k in range(1, m + 1))
        rhs = ((-1) ** (m - 1)) * (
            3 * sum(Fraction(1, (k**2) * comb(2 * k, k)) for k in range(1, m + 1))
            + 2 * sum(Fraction((-1) ** k, k**2) for k in range(1, m + 1))
        )
        assert lhs == rhs, f"Apery identity failed at m={m}"


def check_polynomial_ode_identity(P_seq: list[int]):
    # Check exact L_G(G)(x) = p^2 (1+x)^p (-2 v_p + v_{p-1}(1+x)) in Q[x] for p in {5,7,11,13,17,19}
    x = sp.Symbol("x")
    for p in (5, 7, 11, 13, 17, 19):
        v = [sp.Rational(P_seq[i], 16**i) for i in range(p + 1)]
        G = sum(v[i] * (1 + x) ** i for i in range(p))
        dG = sp.diff(G, x)
        d2G = sp.diff(dG, x)
        LG_G = (1 + x) ** 2 * x * (x - 1) * d2G + (1 + x) * (3 * x**2 - 1) * dG + x * (1 + x) * G
        rhs = p**2 * (1 + x) ** p * (-2 * v[p] + v[p - 1] * (1 + x))
        assert sp.expand(LG_G - rhs) == 0, f"L_G(G) polynomial identity failed at p={p}"


def check_lemmas_for_primes(P_seq: list[int], p_max_lemmas: int = 73, p_max_direct: int = 107):
    primes_direct = [p for p in range(5, p_max_direct + 1) if is_prime(p)]
    for p in primes_direct:
        n = (p - 1) // 2
        eps = 1 if n % 2 == 0 else -1
        p3 = p**3
        p4 = p**4

        # Direct verification of Remark 3.2 mod p^3
        inv128 = pow(128, -1, p3)
        inv256 = pow(256, -1, p3)
        lhs_sum = 0
        rhs_sum = 0
        p128 = 1
        p256 = 1
        for k in range(p):
            lhs_sum = (lhs_sum + (P_seq[k] % p3) * (P_seq[k] % p3) * p128) % p3
            c4 = pow(comb(2 * k, k) % p3, 4, p3)
            rhs_sum = (rhs_sum + c4 * p256) % p3
            p128 = (p128 * inv128) % p3
            p256 = (p256 * inv256) % p3
        assert lhs_sum == (eps * rhs_sum) % p3, f"Remark 3.2 failed directly at p={p}"

        if p > p_max_lemmas:
            continue

        # Modular checks of Lemmas 1-6 mod p^4 / p^3 / p
        inv16_p4 = pow(16, -1, p4)
        c = [(pow(comb(2 * m, m) % p4, 2, p4) * pow(inv16_p4, m, p4)) % p4 for m in range(p)]
        v = [((P_seq[i] % p4) * pow(inv16_p4, i, p4)) % p4 for i in range(p + 1)]
        B = []
        for m in range(n + 1):
            bm = sum((v[i] * (comb(i, 2 * m) % p4)) % p4 for i in range(2 * m, p)) % p4
            B.append(bm)
        Ep = [(c[m] - eps * B[m]) % p4 for m in range(n + 1)]

        # Lemma 1
        assert lhs_sum == sum(c[m] * B[m] for m in range(n + 1)) % p3
        assert rhs_sum == sum(c[m] * c[m] for m in range(n + 1)) % p3
        # Check mod p^4 truncation in Lemma 1(2)
        full_rhs_p4 = sum((pow(comb(2 * k, k) % p4, 4, p4) * pow(pow(256, -1, p4), k, p4)) % p4 for k in range(p)) % p4
        assert full_rhs_p4 == sum(c[m] * c[m] for m in range(n + 1)) % p4
        for m in range(n + 1):
            assert c[m] % p == pow(comb(n, m), 2, p)
            assert c[m] % p == c[n - m] % p
        assert c[n] % p == 1

        # Lemma 2
        Hn2 = sum(pow(k, -2, p) for k in range(1, n + 1)) % p
        assert Hn2 == 0
        assert comb(2 * n, n) % p3 == (eps * pow(4, p - 1, p3)) % p3

        # Lemma 3
        assert (2 * v[p]) % p == 1
        for j in range(n + 1, p):
            r = p - j
            assert (comb(2 * j, j) // p) % p == (-2 * pow(r * comb(2 * r, r), -1, p)) % p
        assert v[p - 1] % p == eps % p
        assert Ep[n] % (p * p) == 0
        E_tilde = []
        for m in range(n + 1):
            assert Ep[m] % (p * p) == 0, f"p^2 does not divide Ep({m}) at p={p}"
            E_tilde.append((eps * (Ep[m] // (p * p))) % p)
        alt_harm = sum(((-1) ** t) * pow(t, -2, p) for t in range(1, n + 1)) % p
        assert E_tilde[n] == (-pow(2, -1, p) * eps * alt_harm) % p

        # Lemma 4
        for m in range(1, n + 1):
            assert (4 * m * m * E_tilde[m] - ((2 * m - 1) ** 2) * E_tilde[m - 1]) % p == 1

        # Lemma 5
        S = [(E_tilde[m] + E_tilde[n - m]) % p for m in range(n + 1)]
        for m in range(1, n + 1):
            assert (4 * m * m * S[m] - ((2 * m - 1) ** 2) * S[m - 1]) % p == 0
        assert all(s == 0 for s in S)
        Tn1 = sum(pow(comb(n - 1, k), -2, p) for k in range(n)) % p
        assert S[0] == (2 * E_tilde[n] - Tn1) % p

        # Lemma 6(2) & (4)
        inv_sum = sum(pow(r * r * comb(2 * r, r), -1, p) for r in range(1, n + 1)) % p
        assert (3 * inv_sum) % p == (-2 * eps * Tn1) % p
        assert Tn1 == (-eps * alt_harm) % p

    return len(primes_direct)


def main():
    P_seq = clf_numbers(110)
    check_symbolic_operator_and_telescoping()
    check_polynomial_ode_identity(P_seq)
    cnt = check_lemmas_for_primes(P_seq, p_max_lemmas=73, p_max_direct=107)
    print(f"PASS (CLF + Lemmas 1-6 verified for 5<=p<=73, Remark 3.2 verified for all {cnt} primes 5<=p<=107)")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
