"""Exact-arithmetic verifier for Otmani Remark 3.1 (arXiv:2608.14453v2) and all proof lemmas."""

from fractions import Fraction
from math import comb
import sympy as sp


def clf_sequence(limit: int) -> list[int]:
    """Compute Catalan-Larcombe-French numbers P_0..P_limit using the exact recurrence."""
    P = [1, 8]
    for k in range(2, limit + 1):
        num = 8 * (3 * k * k - 3 * k + 1) * P[k - 1] - 128 * (k - 1) ** 2 * P[k - 2]
        assert num % (k * k) == 0
        P.append(num // (k * k))
    return P


def mod_p_k(q: Fraction, pk: int) -> int:
    """Exact reduction of a rational q in Z_(p) modulo p^k."""
    return (q.numerator % pk) * pow(q.denominator, -1, pk) % pk


def check_polynomial_identities() -> None:
    """Verify the exact algebraic identities used in Lemmas 4 and 6."""
    # Check Staver polynomial identity (Lemma 6.1) and Apery telescoping (Lemma 6.3)
    M, k, m = sp.symbols("M k m", integer=True)
    lhs_s = sp.expand((2 * k - 3 * M - 1) * (k + 1) ** 2 - (2 * k - 3 * M - 3) * (M - k) ** 2)
    rhs_s = sp.expand(2 * (2 * M + 3) * (M - k) ** 2 - (M + 1) ** 3)
    assert lhs_s == rhs_s

    # Check Staver exact sum for M = 0..15
    for mv in range(16):
        T_M = sum(Fraction(1, comb(mv, j) ** 2) for j in range(mv + 1))
        lhs = Fraction(2 * (2 * mv + 3) * comb(2 * mv + 2, mv + 1), (mv + 1) ** 2) * T_M
        rhs = 6 * sum(Fraction(comb(2 * r, r), r) for r in range(1, mv + 2))
        assert lhs == rhs

    # Check Apery exact sum for m = 1..15
    for mv in range(1, 16):
        lhs = sum(Fraction((-1) ** j, j * j * comb(mv, j) * comb(mv + j, j)) for j in range(1, mv + 1))
        rhs = (-1) ** (mv - 1) * (
            3 * sum(Fraction(1, j * j * comb(2 * j, j)) for j in range(1, mv + 1))
            + 2 * sum(Fraction((-1) ** j, j * j) for j in range(1, mv + 1))
        )
        assert lhs == rhs

    # Check (1+x) L_A = -x L_G exact operator identity on generic degree-8 polynomial
    x = sp.Symbol("x")
    y = 1 + x
    c_syms = sp.symbols("c0:9")
    f = sum(c_syms[i] * x ** i for i in range(9))
    theta_y = lambda expr: y * sp.diff(expr, x)
    theta_x = lambda expr: x * sp.diff(expr, x)
    LG_f = (
        2 * theta_y(theta_y(f))
        - y * (3 * theta_y(theta_y(f)) + 3 * theta_y(f) + f)
        + y ** 2 * (theta_y(theta_y(f) + f) + theta_y(f) + f)
    )
    LA_f = theta_x(theta_x(f)) - x ** 2 * (theta_x(theta_x(f) + f) + theta_x(f) + f)
    assert sp.expand((1 + x) * LA_f + x * LG_f) == 0


def check_prime(p: int, verify_all_lemmas: bool = True) -> None:
    """Verify Remark 3.1 mod p^3 and (optionally) every lemma in PROOF.md for prime p > 3."""
    n = (p - 1) // 2
    p2, p3 = p * p, p * p * p
    eps = 1 if n % 2 == 0 else -1
    P = clf_sequence(p)

    # Check both definitions of P_k match recurrence for small k (up to min(p, 12))
    for k in range(min(p + 1, 13)):
        def1 = sum(Fraction(comb(2 * j, j) ** 2 * comb(2 * k - 2 * j, k - j) ** 2, comb(k, j)) for j in range(k + 1))
        def2 = 2 ** k * sum(comb(k, 2 * m) * comb(2 * m, m) ** 2 * 4 ** (k - 2 * m) for m in range(k // 2 + 1))
        assert def1 == P[k] and def2 == P[k]

    # Direct Remark 3.1 check mod p^3
    lhs = sum(Fraction(P[k] ** 2, 128 ** k) for k in range(p))
    rhs = eps * sum(Fraction(comb(2 * k, k) ** 4, 256 ** k) for k in range(p))
    assert mod_p_k(lhs - rhs, p3) == 0

    if not verify_all_lemmas:
        return

    v = [Fraction(P[i], 16 ** i) for i in range(p + 1)]
    c = [Fraction(comb(2 * m, m) ** 2, 16 ** m) for m in range(n + 1)]
    B = [sum(v[i] * comb(i, 2 * m) for i in range(2 * m, p)) for m in range(n + 1)]
    E = [c[m] - eps * B[m] for m in range(n + 1)]

    # Lemma 1
    assert lhs == sum(c[m] * B[m] for m in range(n + 1))
    assert mod_p_k(rhs - eps * sum(c[m] ** 2 for m in range(n + 1)), p ** 4) == 0
    for m in range(n + 1):
        assert mod_p_k(c[m], p) == (comb(n, m) ** 2) % p

    # Lemma 2
    Hn2 = sum(Fraction(1, k * k) for k in range(1, n + 1))
    assert mod_p_k(Hn2, p) == 0
    assert comb(p - 1, n) % p3 == (eps * pow(4, p - 1, p3)) % p3

    # Lemma 3
    assert mod_p_k(v[p], p) == pow(2, -1, p)
    assert mod_p_k(v[p - 1], p) == eps % p
    tE = []
    for m in range(n + 1):
        em = mod_p_k(E[m], p3)
        assert em % p2 == 0
        tE.append((eps * (em // p2)) % p)
    alt_sq = mod_p_k(sum(Fraction((-1) ** t, t * t) for t in range(1, n + 1)), p)
    assert tE[n] == (-pow(2, -1, p) * eps * alt_sq) % p

    # Lemma 4 & Lemma 5
    for m in range(1, n + 1):
        assert (4 * m * m * tE[m] - (2 * m - 1) ** 2 * tE[m - 1]) % p == 1
        Sm = (tE[m] + tE[n - m]) % p
        Sm_prev = (tE[m - 1] + tE[n + 1 - m]) % p
        assert (4 * m * m * Sm - (2 * m - 1) ** 2 * Sm_prev) % p == 0
    for m in range(n + 1):
        assert (tE[m] + tE[n - m]) % p == 0

    # Lemma 6
    Tn1 = mod_p_k(sum(Fraction(1, comb(n - 1, k) ** 2) for k in range(n)), p)
    assert (tE[n] - tE[0]) % p == Tn1
    assert Tn1 == (-eps * alt_sq) % p


def main() -> None:
    check_polynomial_identities()
    primes = list(sp.primerange(5, 102))
    for p in primes:
        # Full lemma checks up to p=47, direct exact mod p^3 check for all 5 <= p <= 101
        check_prime(p, verify_all_lemmas=(p <= 47))
    print(f"PASS: verified exact identities and Remark 3.1 mod p^3 for all {len(primes)} primes 5 <= p <= 101.")


if __name__ == "__main__":
    main()
