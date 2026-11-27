#!/usr/bin/env python3
"""Exact-arithmetic verifier for OEIS A208425 Conjecture (ii), Part 1 (conjecture_2).

Verifies for primes p == 1 (mod 3):
  1. Exact equivalence of both definitions of a(j) (sum form and generating-function form).
  2. Hockey-stick reduction sum_{j=0}^{p-1} a(j) = sum_{k=0}^{3n} t_k and exact mod p^2 values.
  3. Polynomial differential identity H(u(X)) == (1 - 2 X^p) tilde_Q(X) - C(4n,2n) R(X) (mod p)
     and exact rational telescoping identity for 2 Q_{4n+1}(X) over Q[X].
  4. Harmonic identity H_n - H_{2n} == H_{3n} (mod p) and Sun-Tauraso sum_{k=0}^{p-1} C(2k,k) == 1 (mod p^2).
  5. 3-orbit cancellation sum_{x in F_p} P(x) L(x) == 0 (mod p), giving
     sum_{i=0}^{2n-1} 1/((2i+1) C(2i,i)) == 0 (mod p) and sum_{k=0}^{4n} C(2k,k) == 1 (mod p^2).
  6. The full target supercongruence sum_{k=0}^{p-1} a(k) == C(2(p-1)/3, (p-1)/3) (mod p^2)
     for all 45 primes p == 1 (mod 3) with 7 <= p <= 499 (directly from a(k) for p <= 200
     and via the exact hockey-stick identity for all p <= 499).

Uses exact integer and rational arithmetic only (no floating point). Prints PASS or FAIL.
"""
from fractions import Fraction
import math
import signal
import sys
import time

TIMEOUT_SECONDS = 120


def _timeout_handler(signum, frame):
    print("FAIL: timeout exceeded")
    sys.exit(1)


signal.signal(signal.SIGALRM, _timeout_handler)
signal.alarm(TIMEOUT_SECONDS)


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    d = 2
    while d * d <= num:
        if num % d == 0:
            return False
        d += 1
    return True


def a_sum(j: int) -> int:
    return sum(
        math.comb(j, k) * math.comb(j - k, k) * math.comb(j + k, k)
        for k in range(j // 2 + 1)
    )


def a_gf_coeff(j: int) -> int:
    # [x^j] sum_{k>=0} ((3k)! / k!^3) * x^{2k} / (1-x)^{3k+1}
    total = 0
    for k in range(j // 2 + 1):
        trinomial = math.factorial(3 * k) // (math.factorial(k) ** 3)
        total += trinomial * math.comb(j + k, 3 * k)
    return total


def poly_add_mod(a, b, p):
    L = max(len(a), len(b))
    res = [0] * L
    for i in range(len(a)):
        res[i] = (res[i] + a[i]) % p
    for i in range(len(b)):
        res[i] = (res[i] + b[i]) % p
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res


def poly_mul_mod(a, b, p):
    res = [0] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        if ca == 0:
            continue
        for j, cb in enumerate(b):
            if cb:
                res[i + j] = (res[i + j] + ca * cb) % p
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res


def poly_pow_mod(base, exp, p):
    res = [1]
    b = base[:]
    e = exp
    while e > 0:
        if e & 1:
            res = poly_mul_mod(res, b, p)
        b = poly_mul_mod(b, b, p)
        e >>= 1
    return res


def poly_mul_Q(a, b):
    res = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        if ca == 0:
            continue
        for j, cb in enumerate(b):
            if cb:
                res[i + j] += ca * cb
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res


def poly_pow_Q(base, exp):
    res = [Fraction(1)]
    b = base[:]
    e = exp
    while e > 0:
        if e & 1:
            res = poly_mul_Q(res, b)
        b = poly_mul_Q(b, b)
        e >>= 1
    return res


def poly_int_Q(poly):
    res = [Fraction(0)] * (len(poly) + 1)
    for deg, c in enumerate(poly):
        if c:
            res[deg + 1] = c / (deg + 1)
    return res


def poly_rem_phi_Q(poly):
    # Remainder modulo Phi(X) = X^2 - X + 1 (so X^2 == X - 1)
    p = list(poly)
    while len(p) > 2:
        c = p.pop()
        if c:
            p[-1] += c
            p[-2] -= c
    while len(p) < 2:
        p.append(Fraction(0))
    return p[0], p[1]


def verify_polynomial_lemmas(p: int):
    """Verify exact Q[X] telescoping and F_p[X] identity H(u) == A(X) (mod p)."""
    n = (p - 1) // 6
    r = 2 * n
    m = 3 * n
    c_2r = math.comb(4 * n, 2 * n)

    # 1. Build H(u(X)) in F_p[X], where u(X) = X - X^2 = [0, 1, -1]
    u_mod = [0, 1, p - 1]
    u_pow = [1]
    Hu = [0]
    for exp in range(1, m + 4 * n + 2):
        u_pow = poly_mul_mod(u_pow, u_mod, p)
        k = exp - (4 * n + 1)
        if 0 <= k <= m and k != r:
            coeff = (3 * math.comb(2 * k, k) * pow(3 * k + 1, p - 2, p)) % p
            term = [(coeff * c) % p for c in u_pow]
            Hu = poly_add_mod(Hu, term, p)

    # 2. Build exact Q_{4n+1}(X) = int_0^X u(t)^{4n} dt over Q[X]
    u_Q = [Fraction(0), Fraction(1), Fraction(-1)]
    u_4n_Q = poly_pow_Q(u_Q, 4 * n)
    assert u_4n_Q[p - 1] == Fraction(c_2r), f"[t^(p-1)] u^(4n) mismatch at p={p}"
    Q_4n1 = poly_int_Q(u_4n_Q)

    # Verify Q_{4n+1}(1) = (4n)!^2 / (8n+1)! and p*Q_{4n+1}(1) == C(4n,2n) (mod p^2)
    Q_val_1 = sum(Q_4n1)
    expected_Q1 = Fraction(math.factorial(4 * n) ** 2, math.factorial(8 * n + 1))
    assert Q_val_1 == expected_Q1, f"Q(1) mismatch at p={p}"
    diff_Q1 = p * Q_val_1 - Fraction(c_2r)
    assert diff_Q1.denominator % p != 0 and diff_Q1.numerator % (p * p) == 0, (
        f"p*Q(1) != C(4n,2n) mod p^2 at p={p}"
    )

    # Verify exact telescoping identity in Q[X]:
    # 2 Q_{4n+1}(X) == Q_{4n+1}(1) * (1 + (2X - 1) * sum_{k=0}^{4n} C(2k,k) u(X)^k)
    sum_poly = [Fraction(0)]
    u_k = [Fraction(1)]
    for k in range(4 * n + 1):
        ck = Fraction(math.comb(2 * k, k))
        if len(u_k) > len(sum_poly):
            sum_poly.extend([Fraction(0)] * (len(u_k) - len(sum_poly)))
        for idx, val in enumerate(u_k):
            sum_poly[idx] += ck * val
        if k < 4 * n:
            u_k = poly_mul_Q(u_k, u_Q)
    rhs_tele = poly_mul_Q([Fraction(-1), Fraction(2)], sum_poly)
    rhs_tele[0] += Fraction(1)
    rhs_tele = [Q_val_1 * c for c in rhs_tele]
    lhs_tele = [2 * c for c in Q_4n1]
    while len(lhs_tele) < len(rhs_tele):
        lhs_tele.append(Fraction(0))
    while len(rhs_tele) < len(lhs_tele):
        rhs_tele.append(Fraction(0))
    assert lhs_tele == rhs_tele, f"Exact Q[X] telescoping identity failed at p={p}"

    # 3. Build tilde_Q(X) = Q_{4n+1}(X) - C(4n,2n) X^p / p in Z_(p)[X] and reduce mod p
    tQ_Q = list(Q_4n1)
    tQ_Q[p] -= Fraction(c_2r, p)
    tQ_mod = []
    for c in tQ_Q:
        assert c.denominator % p != 0, f"p divides denominator in tilde_Q at p={p}"
        tQ_mod.append((c.numerator * pow(c.denominator, p - 2, p)) % p)

    # Check tilde_Q(1) == 0 (mod p) and tilde_Q == 0 mod (p, Phi)
    assert sum(tQ_mod) % p == 0, f"tilde_Q(1) != 0 mod p at p={p}"
    rem0, rem1 = poly_rem_phi_Q(tQ_Q)
    assert rem0.denominator % p != 0 and rem0.numerator % p == 0, f"rem0 != 0 mod p at p={p}"
    assert rem1.denominator % p != 0 and rem1.numerator % p == 0, f"rem1 != 0 mod p at p={p}"

    # 4. Build R(X) = sum_{j=1}^{p-1} ((-1)^j C(p,j)/p) X^{p+j} in Z[X]
    R_Q = [Fraction(0)] * (2 * p)
    R_mod = [0] * (2 * p)
    for j in range(1, p):
        cj = ((-1) ** j) * (math.comb(p, j) // p)
        R_Q[p + j] = Fraction(cj)
        R_mod[p + j] = cj % p
    r0, r1 = poly_rem_phi_Q(R_Q)
    assert r0 == 0 and r1 == 0, f"Phi does not divide R(X) in Z[X] at p={p}"

    # 5. Build A(X) = (1 - 2 X^p) tilde_Q(X) - C(4n,2n) R(X) in F_p[X] and check Hu == A
    one_minus_2Xp = [0] * (p + 1)
    one_minus_2Xp[0] = 1
    one_minus_2Xp[p] = (p - 2) % p
    term1 = poly_mul_mod(one_minus_2Xp, tQ_mod, p)
    term2 = [((-c_2r) * c) % p for c in R_mod]
    A_mod = poly_add_mod(term1, term2, p)
    assert Hu == A_mod, f"H(u(X)) != A(X) in F_p[X] at p={p}"


def main():
    t0 = time.time()

    # Check equivalence of both definitions of a(j) for 0 <= j <= 60
    for j in range(61):
        v1 = a_sum(j)
        v2 = a_gf_coeff(j)
        assert v1 == v2, f"a({j}) definition mismatch: {v1} vs {v2}"

    # Check exact polynomial lemmas for the first 6 primes p == 1 (mod 3)
    poly_primes = [7, 13, 19, 31, 37, 43]
    for p in poly_primes:
        verify_polynomial_lemmas(p)

    # Check all primes p == 1 (mod 3), 7 <= p <= 499
    primes = [p for p in range(7, 500) if is_prime(p) and p % 3 == 1]
    assert len(primes) == 45

    for p in primes:
        n = (p - 1) // 6
        r = 2 * n
        m = 3 * n
        p2 = p * p
        rhs = math.comb(4 * n, 2 * n) % p2

        # Direct sum_{j=0}^{p-1} a(j) for p <= 200
        if p <= 200:
            s_direct = sum(a_sum(j) for j in range(p)) % p2
            assert s_direct == rhs, f"Direct conjecture_2 fail at p={p}: {s_direct} != {rhs}"

        # Hockey-stick sum sum_{k=0}^{3n} t_k (and termwise mod p^2 reduction)
        s_tk = 0
        F_1 = 0
        for k in range(m + 1):
            tk = math.comb(3 * k, k) * math.comb(2 * k, k) * math.comb(p + k, 3 * k + 1)
            s_tk = (s_tk + tk) % p2
            if k == r:
                assert tk % p2 == rhs, f"t_r mod p^2 fail at p={p}"
            else:
                assert tk % p == 0, f"p does not divide t_{k} at p={p}"
                q_term = (math.comb(2 * k, k) * pow(3 * k + 1, p - 2, p)) % p
                assert (tk // p) % p == q_term, f"t_{k}/p mod p fail at p={p}"
                F_1 = (F_1 + q_term) % p
        assert s_tk == rhs, f"Hockey-stick conjecture_2 fail at p={p}"
        assert F_1 == 0, f"F(1) != 0 mod p at p={p}"

        # Harmonic identity H_n - H_{2n} == H_{3n} (mod p)
        def H(M):
            return sum(pow(j, p - 2, p) for j in range(1, M + 1)) % p

        assert (H(n) - H(2 * n) - H(3 * n)) % p == 0, f"Harmonic identity fail at p={p}"

        # Sun-Tauraso full sum and truncated sum mod p^2
        s_full = sum(math.comb(2 * k, k) for k in range(p)) % p2
        s_4n = sum(math.comb(2 * k, k) for k in range(4 * n + 1)) % p2
        assert s_full == 1, f"sum_{{k=0}}^{{p-1}} C(2k,k) != 1 mod p^2 at p={p}"
        assert s_4n == 1, f"sum_{{k=0}}^{{4n}} C(2k,k) != 1 mod p^2 at p={p}"

        # Piece 2: sum_{i=0}^{2n-1} 1/((2i+1) C(2i,i)) == 0 (mod p) and 3-orbit cancellation
        s_beta = sum(
            pow(((2 * i + 1) * math.comb(2 * i, i)) % p, p - 2, p)
            for i in range(2 * n)
        ) % p
        assert s_beta == 0, f"Beta sum != 0 mod p at p={p}"

        # Check termwise complement identity C(2(p-1-i), p-1-i) / p == -1/((2i+1)C(2i,i)) mod p
        for i in range(2 * n):
            cb = math.comb(2 * (p - 1 - i), p - 1 - i)
            assert cb % p == 0
            expected = (-pow(((2 * i + 1) * math.comb(2 * i, i)) % p, p - 2, p)) % p
            assert (cb // p) % p == expected

        # Verify L(x) = (1 - x^p - (1-x)^p)/p mod p vanishes at {0,1,zeta,zeta^{-1}}
        # and P(x)L(x) + P(y)L(y) + P(z)L(z) == 0 (mod p) on every 3-orbit
        roots = [x for x in range(p) if (x * x - x + 1) % p == 0]
        assert len(roots) == 2

        def L_eval(x):
            return ((1 - pow(x, p, p2) - pow(1 - x, p, p2)) // p) % p

        def P_eval(x):
            u = (x * (1 - x)) % p
            return ((1 - pow(u, 2 * n, p)) * pow((1 - x + x * x) % p, p - 2, p)) % p

        for special in [0, 1] + roots:
            assert L_eval(special) == 0, f"L({special}) != 0 at p={p}"

        visited = set([0, 1] + roots)
        total_PL = 0
        for x in range(p):
            if x in visited:
                continue
            y = pow((1 - x) % p, p - 2, p)
            z = ((x - 1) * pow(x, p - 2, p)) % p
            assert len({x, y, z}) == 3
            visited.update((x, y, z))
            orb_sum = (P_eval(x) * L_eval(x) + P_eval(y) * L_eval(y) + P_eval(z) * L_eval(z)) % p
            assert orb_sum == 0, f"3-orbit sum nonzero at p={p}, x={x}"
            total_PL = (total_PL + orb_sum) % p
        assert len(visited) == p and total_PL == 0

    elapsed = time.time() - t0
    print(
        f"PASS: verified a(j) equivalence (j<=60), exact Q[X] & F_p[X] polynomial lemmas "
        f"(p in {poly_primes}), and all steps + target conjecture_2 for all {len(primes)} primes "
        f"p == 1 (mod 3), 7 <= p <= 499 (direct a(j) sum for p <= 200) in {elapsed:.2f}s."
    )


if __name__ == "__main__":
    main()
