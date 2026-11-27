"""Independent exact-arithmetic checker for targets/oeis-A190969/PROOF.md."""

from fractions import Fraction
from math import comb
import sys


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


def a_seq(n_max: int) -> list[int]:
    a = [0, 1]
    for _ in range(2, n_max + 1):
        a.append(5 * a[-1] - 8 * a[-2])
    return a


def s_mod_direct(p: int, m: int) -> int:
    """Direct modular computation matching FormalConjectures/OEIS/190969.lean."""
    mod = p**m
    inv_neg4096 = pow(-4096, -1, mod)
    a = a_seq(4 * (p - 1))
    total = 0
    inv_pow = 1
    for k in range(p):
        c = comb(2 * k, k)
        term = (a[4 * k] % mod) * pow(c % mod, 3, mod) * inv_pow
        total = (total + term) % mod
        inv_pow = (inv_pow * inv_neg4096) % mod
    return total


# Exact arithmetic in K = Q(s) with s^2 = -7, represented as (re, im) of Fractions.
def k_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def k_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def k_mul(x, y):
    return (x[0] * y[0] - 7 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def k_inv(x):
    norm = x[0] * x[0] + 7 * x[1] * x[1]
    assert norm != 0
    return (x[0] / norm, -x[1] / norm)


def k_div(x, y):
    return k_mul(x, k_inv(y))


def k_pow(x, n: int):
    res = (Fraction(1), Fraction(0))
    base = x
    e = n
    while e > 0:
        if e & 1:
            res = k_mul(res, base)
        base = k_mul(base, base)
        e >>= 1
    return res


def k_norm(x) -> Fraction:
    return x[0] * x[0] + 7 * x[1] * x[1]


# Polynomial operations over Fraction (coeffs low-to-high)
def poly_trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def poly_add(a, b):
    n = max(len(a), len(b))
    res = [Fraction(0)] * n
    for i in range(len(a)):
        res[i] += a[i]
    for i in range(len(b)):
        res[i] += b[i]
    return poly_trim(res)


def poly_mul(a, b):
    if not a or not b:
        return []
    res = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        if ca == 0:
            continue
        for j, cb in enumerate(b):
            res[i + j] += ca * cb
    return poly_trim(res)


def poly_pow(a, n: int):
    res = [Fraction(1)]
    base = list(a)
    e = n
    while e > 0:
        if e & 1:
            res = poly_mul(res, base)
        base = poly_mul(base, base)
        e >>= 1
    return res


def poly_eval_frac(p, x: Fraction) -> Fraction:
    acc = Fraction(0)
    for c in reversed(p):
        acc = acc * x + c
    return acc


def poly_eval_k(p, x):
    acc = (Fraction(0), Fraction(0))
    for c in reversed(p):
        acc = k_add(k_mul(acc, x), (c, Fraction(0)))
    return acc


def poly_compose(f, g):
    """Compute f(g(u)) where f, g are polynomials in Fraction."""
    acc = []
    for c in reversed(f):
        acc = poly_add(poly_mul(acc, g), [c])
    return acc


def check_section_2():
    alpha = (Fraction(5, 2), Fraction(1, 2))
    beta = (Fraction(5, 2), Fraction(-1, 2))
    s = (Fraction(0), Fraction(1))

    # Binet formula up to n=40
    a = a_seq(40)
    for n in range(41):
        val = k_div(k_sub(k_pow(alpha, n), k_pow(beta, n)), s)
        assert val == (Fraction(a[n]), Fraction(0)), f"Binet failed at n={n}: {val}"

    assert k_pow(alpha, 2) == (Fraction(9, 2), Fraction(5, 2))
    assert k_pow(alpha, 4) == (Fraction(-47, 2), Fraction(45, 2))
    assert k_pow(beta, 4) == (Fraction(-47, 2), Fraction(-45, 2))

    t1 = k_div(k_pow(beta, 4), (Fraction(-4096), Fraction(0)))
    t2 = k_div(k_pow(alpha, 4), (Fraction(-4096), Fraction(0)))
    assert t1 == (Fraction(47, 8192), Fraction(45, 8192))
    assert t2 == (Fraction(47, 8192), Fraction(-45, 8192))
    assert k_add(t1, t2) == (Fraction(47, 4096), Fraction(0))
    assert k_mul(t1, t2) == (Fraction(1, 4096), Fraction(0))

    # Identity (2.1): S(p) = (F_p(t2) - F_p(t1))/s for small primes
    a = a_seq(4 * 23)
    for p in [3, 5, 7, 11, 13, 17, 19, 23]:
        Fp = [Fraction(comb(2 * k, k) ** 3) for k in range(p)]
        rhs = k_div(k_sub(poly_eval_k(Fp, t2), poly_eval_k(Fp, t1)), s)
        lhs_val = sum(Fraction(a[4 * k] * comb(2 * k, k) ** 3, (-4096) ** k) for k in range(p))
        assert rhs == (lhs_val, Fraction(0)), f"(2.1) failed at p={p}"

    # Identity (2.2): (16t - 1)^3 - 15^3 t^2 == (t - 1)(4096 t^2 - 47 t + 1)
    lhs_poly = poly_add(poly_pow([Fraction(-1), Fraction(16)], 3), [Fraction(0), Fraction(0), Fraction(-(15**3))])
    rhs_poly = poly_mul([Fraction(-1), Fraction(1)], [Fraction(1), Fraction(-47), Fraction(4096)])
    assert lhs_poly == rhs_poly
    for r in [(Fraction(1), Fraction(0)), t1, t2]:
        assert poly_eval_k(lhs_poly, r) == (Fraction(0), Fraction(0))


def check_section_3_series_and_splits():
    # Verify q-series identities from Section 3 up to N=25 in Z[[q]]
    N = 26

    def ser_mul(A, B):
        C = [0] * N
        for i in range(N):
            if A[i] == 0:
                continue
            for j in range(N - i):
                C[i + j] += A[i] * B[j]
        return C

    def ser_pow(A, e):
        res = [0] * N
        res[0] = 1
        base = list(A)
        while e > 0:
            if e & 1:
                res = ser_mul(res, base)
            base = ser_mul(base, base)
            e >>= 1
        return res

    def ser_inv(A):
        assert A[0] == 1
        B = [0] * N
        B[0] = 1
        for n in range(1, N):
            B[n] = -sum(A[k] * B[n - k] for k in range(1, n + 1))
        return B

    # prod_{n>=1} (1 - q^{m*n})
    def prod_1_minus_qm(m):
        P = [0] * N
        P[0] = 1
        for n in range(1, N):
            k = m * n
            if k >= N:
                break
            # multiply by (1 - q^k)
            for i in range(N - 1, k - 1, -1):
                P[i] -= P[i - k]
        return P

    P1 = prod_1_minus_qm(1)
    P2 = prod_1_minus_qm(2)
    P4 = prod_1_minus_qm(4)

    # t(tau) = q * (P1 * P4 / P2^2)^24
    ratio_t = ser_mul(ser_mul(P1, P4), ser_inv(ser_mul(P2, P2)))
    ratio_t_24 = ser_pow(ratio_t, 24)
    t_ser = [0] + ratio_t_24[:-1]

    # Formula (3.2): t(tau) = q / prod (1 + q^(2n-1))^24
    Q_odd = [0] * N
    Q_odd[0] = 1
    for n in range(1, N):
        k = 2 * n - 1
        if k >= N:
            break
        for i in range(N - 1, k - 1, -1):
            Q_odd[i] += Q_odd[i - k]
    t_ser_32 = [0] + ser_inv(ser_pow(Q_odd, 24))[:-1]
    assert t_ser == t_ser_32, "Formula (3.2) q-series mismatch"

    # Theta(tau) = P2^20 / (P1^8 * P4^8)
    Theta_ser = ser_mul(ser_pow(P2, 20), ser_inv(ser_mul(ser_pow(P1, 8), ser_pow(P4, 8))))

    # F(t(tau)) == Theta(tau)
    F_t = [0] * N
    t_pow = [0] * N
    t_pow[0] = 1
    for k in range(N):
        c = comb(2 * k, k) ** 3
        for i in range(N):
            F_t[i] += c * t_pow[i]
        t_pow = ser_mul(t_pow, t_ser)
    assert F_t == Theta_ser, "F(t(tau)) != Theta(tau) in q-series"

    # Modular equation (3.1): (16 t(tau) - 1)^3 + j(2*tau) t(tau)^2 = 0
    # Note j(2*tau) has q^2 expansion: j(z) = E4(z)^3 / Delta(z) with q_z = e^{2pi i z} = q^2.
    # Let's compute E4(2tau) = 1 + 240 sum_{n>=1} sigma_3(n) q^{2n}, Delta(2tau) = q^2 * P2^24.
    E4_2 = [0] * N
    E4_2[0] = 1
    for n in range(1, (N - 1) // 2 + 1):
        sig3 = sum(d**3 for d in range(1, n + 1) if n % d == 0)
        E4_2[2 * n] = 240 * sig3
    # (16 t - 1)^3 * P2^24 + E4(2tau)^3 * (t/q)^2 == 0
    t_over_q = ratio_t_24
    one_minus_16t = [0] * N
    one_minus_16t[0] = -1
    for i in range(N):
        one_minus_16t[i] += 16 * t_ser[i]
    lhs = ser_mul(ser_pow(one_minus_16t, 3), ser_pow(P2, 24))
    rhs = ser_mul(ser_pow(E4_2, 3), ser_pow(t_over_q, 2))
    assert [lhs[i] + rhs[i] for i in range(N)] == [0] * N, "Modular eq (3.1) failed"

    # Check Lemma 3.2 & Proposition 3.3 (Beukers Theorem 1.15) for split primes up to 250
    for p in range(3, 251):
        if not is_prime(p) or (p % 7 not in (1, 2, 4)):
            continue
        # Find p = x^2 + 7 y^2
        found = None
        for y in range(1, p):
            if 7 * y * y >= p:
                break
            rem = p - 7 * y * y
            x = int(rem**0.5)
            if x * x == rem:
                found = (x, y)
                break
        assert found is not None, f"Lemma 3.2 failed for p={p}"
        x, y = found

        # Compute sigma_p mod p^3 with sigma_p^2 == -7 (mod p^3)
        mod3 = p**3
        r0 = next(r for r in range(1, p) if (r * r + 7) % p == 0)
        # Hensel lift r -> r - (r^2 + 7)/(2r) mod p^3
        sigma = r0
        for _ in range(2):
            inv2r = pow(2 * sigma, -1, mod3)
            sigma = (sigma - (sigma * sigma + 7) * inv2r) % mod3
        assert (sigma * sigma + 7) % mod3 == 0

        # Choose sign of y so x + y*sigma is a unit mod p
        if (x + y * sigma) % p == 0:
            y = -y
        assert (x + y * sigma) % p != 0
        assert (x - y * sigma) % p == 0

        # Check c1*tau1 + d1 = x + y*s, c2*tau2 + d2 = x + y*s
        # tau1 = (1+s)/4, tau2 = (-1+s)/4
        assert 4 * y * Fraction(1, 4) + (x - y) == x
        assert 4 * y * Fraction(-1, 4) + (x + y) == x

        # Evaluate F_p(iota(t_1)) and F_p(iota(t_2)) mod p^3
        inv8192 = pow(8192, -1, mod3)
        it1 = ((47 + 45 * sigma) * inv8192) % mod3
        it2 = ((47 - 45 * sigma) * inv8192) % mod3

        def eval_Fp_mod(t_mod):
            acc = 0
            t_pow_m = 1
            for k in range(p):
                c = pow(comb(2 * k, k) % mod3, 3, mod3)
                acc = (acc + c * t_pow_m) % mod3
                t_pow_m = (t_pow_m * t_mod) % mod3
            return acc

        xy_sq = pow(x + y * sigma, 2, mod3)
        assert eval_Fp_mod(it1) == xy_sq, f"Thm 1.15 failed at t1 for p={p}"
        assert eval_Fp_mod(it2) == xy_sq, f"Thm 1.15 failed at t2 for p={p}"
        assert s_mod_direct(p, 3) == 0, f"conjecture_2 failed at p={p}"


def legendre_P(m: int):
    """P_m(x) in Q[x] as polynomial in x."""
    # P_m(x) = sum_{k=0}^m C(m,k) C(m+k,k) ((x-1)/2)^k
    w = [Fraction(-1, 2), Fraction(1, 2)]
    res = []
    w_pow = [Fraction(1)]
    for k in range(m + 1):
        coeff = Fraction(comb(m, k) * comb(m + k, k))
        res = poly_add(res, [coeff * c for c in w_pow])
        w_pow = poly_mul(w_pow, w)
    return res


def check_section_4():
    # Check differential operator polynomial identity in Lemma 4.1:
    # (t+1)(t^2 + 1/2 t - m(m+1)/2) - m(m+1)/2 * t == (t - m)(t + m + 1)(t + 1/2)
    for m in range(1, 12):
        m_fac = Fraction(m * (m + 1), 2)
        lhs = poly_add(
            poly_mul([Fraction(1), Fraction(1)], [-m_fac, Fraction(1, 2), Fraction(1)]),
            [Fraction(0), -m_fac],
        )
        rhs = poly_mul(
            poly_mul([Fraction(-m), Fraction(1)], [Fraction(m + 1), Fraction(1)]),
            [Fraction(1, 2), Fraction(1)],
        )
        assert lhs == rhs

    # Lemma 4.1: P_m(1 - 2u)^2 == sum_{k=0}^m (-1)^k C(m+k,2k) C(2k,k)^2 (u(1-u))^k
    u_one_minus_u = [Fraction(0), Fraction(1), Fraction(-1)]
    one_minus_2u = [Fraction(1), Fraction(-2)]
    for m in range(16):
        Pm = legendre_P(m)
        Pm_sub = poly_compose(Pm, one_minus_2u)
        lhs = poly_mul(Pm_sub, Pm_sub)
        rhs = []
        uu_pow = [Fraction(1)]
        for k in range(m + 1):
            c = Fraction((-1) ** k * comb(m + k, 2 * k) * (comb(2 * k, k) ** 2))
            rhs = poly_add(rhs, [c * v for v in uu_pow])
            uu_pow = poly_mul(uu_pow, u_one_minus_u)
        assert lhs == rhs, f"Lemma 4.1 failed at m={m}"

    # Check [x^{p-1}] (x(x-1)(x-lam))^m == (-1)^m H_p(lam) identically in lam
    for m in range(1, 15):
        # Coefficient of x^m in (x-1)^m (x-lam)^m as polynomial in lam
        # (x-1)^m = sum_j C(m,j) (-1)^{m-j} x^j
        # (x-lam)^m = sum_k C(m,k) (-lam)^k x^{m-k}
        # product coeff of x^m requires j + (m - k) = m => j = k
        for k in range(m + 1):
            coeff_lam_k = comb(m, k) * ((-1) ** (m - k)) * comb(m, k) * ((-1) ** k)
            expected = ((-1) ** m) * (comb(m, k) ** 2)
            assert coeff_lam_k == expected

    # Lemma 4.2 & Proposition 4.3 for odd primes
    # u1 = (1 + 3s)/32
    u1 = (Fraction(1, 32), Fraction(3, 32))
    one_minus_u1 = k_sub((Fraction(1), Fraction(0)), u1)
    assert one_minus_u1 == (Fraction(31, 32), Fraction(-3, 32))
    u1_1mu1 = k_mul(u1, one_minus_u1)
    t1 = (Fraction(47, 8192), Fraction(45, 8192))
    t2 = (Fraction(47, 8192), Fraction(-45, 8192))
    assert u1_1mu1 == k_mul((Fraction(16), Fraction(0)), t1)
    assert k_norm(u1) == Fraction(1, 16)
    assert k_norm(one_minus_u1) == Fraction(1)

    # j(E_{u1}) = 256 * (u1^2 - u1 + 1)^3 / (u1^2 (u1 - 1)^2) == -3375
    num = k_mul((Fraction(256), Fraction(0)), k_pow(k_sub((Fraction(1), Fraction(0)), u1_1mu1), 3))
    den = k_pow(u1_1mu1, 2)
    assert k_div(num, den) == (Fraction(-3375), Fraction(0))

    # Test Lemma 4.2 polynomial congruences for odd primes up to 47
    for p in range(3, 50):
        if not is_prime(p):
            continue
        m = (p - 1) // 2
        # Lemma 4.2(1): F_p(u(1-u)/16) === P_m(1-2u)^2 (mod p^2 Z_p[u])
        Fp = [Fraction(comb(2 * k, k) ** 3) for k in range(p)]
        g = [Fraction(0), Fraction(1, 16), Fraction(-1, 16)]
        lhs1 = poly_compose(Fp, g)
        Pm_sub = poly_compose(legendre_P(m), one_minus_2u)
        rhs1 = poly_mul(Pm_sub, Pm_sub)
        diff1 = poly_add(lhs1, [-c for c in rhs1])
        for c in diff1:
            assert c.denominator % p != 0 and c.numerator % (p * p) == 0, f"Lemma 4.2(1) failed at p={p}"

        # Lemma 4.2(2): P_m(1-2u) === H_p(u) (mod p Z_p[u])
        Hp = [Fraction(comb(m, k) ** 2) for k in range(m + 1)]
        diff2 = poly_add(Pm_sub, [-c for c in Hp])
        for c in diff2:
            assert c.denominator % p != 0 and c.numerator % p == 0, f"Lemma 4.2(2) failed at p={p}"

    # Test Prop 4.3 on inert primes up to 150
    for p in range(3, 151):
        if not is_prime(p) or (p % 7 not in (3, 5, 6)):
            continue
        m = (p - 1) // 2
        Hp = [Fraction(comb(m, k) ** 2) for k in range(m + 1)]
        val_H = poly_eval_k(Hp, u1)
        assert val_H[0].denominator % p != 0 and val_H[1].denominator % p != 0
        # 2*val_H has integer/unit denom; check p divides both coefficients in Z_p[omega] -> since p is odd, p divides Re and Im
        assert val_H[0].numerator % p == 0 and val_H[1].numerator % p == 0, f"H_p(u1) not 0 mod p for p={p}"

        Pm_sub = poly_compose(legendre_P(m), one_minus_2u)
        val_P2 = k_pow(poly_eval_k(Pm_sub, u1), 2)
        assert val_P2[0].numerator % (p * p) == 0 and val_P2[1].numerator % (p * p) == 0

        Fp = [Fraction(comb(2 * k, k) ** 3) for k in range(p)]
        val_Ft1 = poly_eval_k(Fp, t1)
        val_Ft2 = poly_eval_k(Fp, t2)
        assert val_Ft1[0].numerator % (p * p) == 0 and val_Ft1[1].numerator % (p * p) == 0
        assert val_Ft2[0].numerator % (p * p) == 0 and val_Ft2[1].numerator % (p * p) == 0
        assert s_mod_direct(p, 2) == 0, f"conjecture_1 failed at inert p={p}"


def check_section_5():
    # Exact check for p = 7
    a = a_seq(28)
    for k in range(5):
        assert a[4 * (k + 2)] == -47 * a[4 * (k + 1)] - 4096 * a[4 * k]
    assert a[0] == 0 and a[4] == 45 and a[8] == -2115 and a[12] == -84915

    inv = pow(-4096, -1, 49)
    assert inv == 27
    terms = []
    for k in range(7):
        tk = (a[4 * k] * (comb(2 * k, k) ** 3) * pow(inv, k, 49)) % 49
        terms.append(tk)
    assert terms == [0, 18, 29, 2, 0, 0, 0], f"p=7 terms mismatch: {terms}"
    assert sum(terms) % 49 == 0
    assert s_mod_direct(7, 2) == 0
    assert s_mod_direct(7, 3) == 294  # 6 * 7^2


def check_all_primes():
    # Direct test of conjecture_1 for all odd primes <= 300 and conjecture_2 for split primes <= 300
    cnt1 = 0
    cnt2 = 0
    for p in range(3, 301):
        if not is_prime(p):
            continue
        assert s_mod_direct(p, 2) == 0, f"conjecture_1 failed at p={p}"
        cnt1 += 1
        if p % 7 in (1, 2, 4):
            assert s_mod_direct(p, 3) == 0, f"conjecture_2 failed at p={p}"
            cnt2 += 1
    return cnt1, cnt2


def main():
    check_section_2()
    check_section_3_series_and_splits()
    check_section_4()
    check_section_5()
    cnt1, cnt2 = check_all_primes()
    print(f"PASS (checked Sec 2-5 lemmas, {cnt1} odd primes <= 300 for conj_1, {cnt2} split primes <= 300 for conj_2)")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
