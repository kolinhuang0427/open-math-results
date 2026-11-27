#!/usr/bin/env python3
"""Exact-arithmetic verifier for the proof of OEIS A190969 (conjecture_1 and conjecture_2).

Verifies:
  1. Algebraic decomposition in K = Q(sqrt(-7)), recurrence a(n), coordinates t_1, t_2, u_1,
     norms, Weierstrass discriminant, and j-invariant j(E_{u_1}) = -3375.
  2. q-series identities up to q^30 for t(tau), Theta(tau), lambda(2*tau), and
     (16*t(tau) - 1)^3 + j(2*tau)*t(tau)^2 = 0, plus exact rational bounds and
     certified mpmath interval check for t(tau_1) = t_1.
  3. Symbolic ODE proof of the Finite Clausen Identity and exact polynomial congruences
     modulo p^2 and p for all odd primes 3 <= p <= 31.
  4. Explicit verification of the ramified prime p = 7 (including all 7 terms).
  5. Inert-prime verification (H_p(u_1) == 0 mod p, F_p(t_1) == F_p(t_2) == 0 mod p^2)
     for all odd inert primes p <= 200 (including p = 3, 5).
  6. Split-prime verification of Beukers' Theorem 1.15 (F_p(t_1) == F_p(t_2) == gamma_p^2 mod p^3)
     for all odd split primes p <= 200.
  7. Direct verification of conjecture_1 (mod p^2) and conjecture_2 (mod p^3) matching
     FormalConjectures/OEIS/190969.lean for all odd primes 3 <= p <= 300.
"""

import math
import os
import signal
import sys
from fractions import Fraction

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

import sympy as sp


def _timeout_handler(signum, frame):
    raise TimeoutError("verify.py exceeded 120s timeout")


signal.signal(signal.SIGALRM, _timeout_handler)
signal.alarm(120)


# ---------- Exact arithmetic in K = Q(s) with s^2 = -7 ----------

class KElem:
    """Exact element a + b*s in Q(sqrt(-7)), s^2 = -7."""

    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, other):
        if not isinstance(other, KElem):
            other = KElem(other)
        return KElem(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        if not isinstance(other, KElem):
            other = KElem(other)
        return KElem(self.a - other.a, self.b - other.b)

    def __neg__(self):
        return KElem(-self.a, -self.b)

    def __mul__(self, other):
        if not isinstance(other, KElem):
            other = KElem(other)
        return KElem(self.a * other.a - 7 * self.b * other.b,
                     self.a * other.b + self.b * other.a)

    def conj(self):
        return KElem(self.a, -self.b)

    def norm(self):
        return self.a * self.a + 7 * self.b * self.b

    def __truediv__(self, other):
        if not isinstance(other, KElem):
            other = KElem(other)
        n = other.norm()
        num = self * other.conj()
        return KElem(num.a / n, num.b / n)

    def __pow__(self, e):
        assert e >= 0
        res = KElem(1, 0)
        base = self
        while e > 0:
            if e & 1:
                res = res * base
            base = base * base
            e >>= 1
        return res

    def __eq__(self, other):
        if not isinstance(other, KElem):
            other = KElem(other)
        return self.a == other.a and self.b == other.b

    def __repr__(self):
        return f"({self.a}) + ({self.b})*s"


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


def seq_a_list(max_n: int) -> list[int]:
    a = [0, 1]
    for _ in range(2, max_n + 1):
        a.append(5 * a[-1] - 8 * a[-2])
    return a


def s_mod_p_m(p: int, m: int) -> int:
    """Compute S(p) mod p^m directly matching FormalConjectures/OEIS/190969.lean."""
    mod = p ** m
    a = [0, 1]
    for _ in range(2, 4 * (p - 1) + 1):
        a.append((5 * a[-1] - 8 * a[-2]) % mod)
    inv_base = pow(-4096 % mod, -1, mod)
    inv_pow = 1
    total = 0
    for k in range(p):
        cb = math.comb(2 * k, k) % mod
        term = (a[4 * k] * pow(cb, 3, mod) * inv_pow) % mod
        total = (total + term) % mod
        inv_pow = (inv_pow * inv_base) % mod
    return total


# ---------- Modular arithmetic in O_K / (M) using Z[s] / (M) for odd M ----------
# Since M is odd, 2 is invertible mod M, so O_K / M O_K = (Z/MZ)[s] / (s^2 + 7).

def kmod_add(u, v, mod):
    return ((u[0] + v[0]) % mod, (u[1] + v[1]) % mod)


def kmod_mul(u, v, mod):
    return ((u[0] * v[0] - 7 * u[1] * v[1]) % mod,
            (u[0] * v[1] + u[1] * v[0]) % mod)


def kmod_from_kelem(x: KElem, mod: int):
    ra = (x.a.numerator * pow(x.a.denominator, -1, mod)) % mod
    rb = (x.b.numerator * pow(x.b.denominator, -1, mod)) % mod
    return (ra, rb)


def eval_Fp_kmod(t_mod, p: int, mod: int):
    acc = (0, 0)
    tpow = (1, 0)
    for k in range(p):
        c = pow(math.comb(2 * k, k) % mod, 3, mod)
        acc = kmod_add(acc, ((c * tpow[0]) % mod, (c * tpow[1]) % mod), mod)
        tpow = kmod_mul(tpow, t_mod, mod)
    return acc


def eval_Hp_kmod(u_mod, p: int, mod: int):
    m = (p - 1) // 2
    acc = (0, 0)
    upow = (1, 0)
    for k in range(m + 1):
        c = pow(math.comb(m, k) % mod, 2, mod)
        acc = kmod_add(acc, ((c * upow[0]) % mod, (c * upow[1]) % mod), mod)
        upow = kmod_mul(upow, u_mod, mod)
    return acc


def eval_Pm_1m2u_kmod(u_mod, m: int, mod: int):
    acc = (0, 0)
    upow = (1, 0)
    for k in range(m + 1):
        sign = -1 if (k & 1) else 1
        c = (sign * math.comb(m, k) * math.comb(m + k, k)) % mod
        acc = kmod_add(acc, ((c * upow[0]) % mod, (c * upow[1]) % mod), mod)
        upow = kmod_mul(upow, u_mod, mod)
    return acc


# ---------- Truncated integer power series operations ----------

def ps_mul(a: list[int], b: list[int], N: int) -> list[int]:
    out = [0] * N
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j in range(N - i):
            out[i + j] += ai * b[j]
    return out


def ps_inv(a: list[int], N: int) -> list[int]:
    assert a[0] == 1
    out = [0] * N
    out[0] = 1
    for n in range(1, N):
        s = 0
        for k in range(1, n + 1):
            s += a[k] * out[n - k]
        out[n] = -s
    return out


def ps_pow(a: list[int], e: int, N: int) -> list[int]:
    if e < 0:
        return ps_pow(ps_inv(a, N), -e, N)
    res = [0] * N
    res[0] = 1
    base = a[:N]
    while e > 0:
        if e & 1:
            res = ps_mul(res, base, N)
        base = ps_mul(base, base, N)
        e >>= 1
    return res


def eta_prod(step: int, N: int) -> list[int]:
    """Compute prod_{n>=1} (1 - q^{step * n}) mod q^N."""
    res = [0] * N
    res[0] = 1
    for n in range(1, N):
        d = step * n
        if d >= N:
            break
        for i in range(N - 1, d - 1, -1):
            res[i] -= res[i - d]
    return res


# ---------- Check 1: Algebraic identities in K = Q(sqrt(-7)) ----------

def check_1_algebra():
    s = KElem(0, 1)
    alpha = KElem(Fraction(5, 2), Fraction(1, 2))
    beta = KElem(Fraction(5, 2), Fraction(-1, 2))
    assert alpha + beta == KElem(5)
    assert alpha * beta == KElem(8)
    assert alpha - beta == s

    a_seq = seq_a_list(80)
    for n in range(81):
        val = (alpha ** n - beta ** n) / s
        assert val == KElem(a_seq[n]), f"Binet mismatch at n={n}"

    assert alpha ** 4 == KElem(Fraction(-47, 2), Fraction(45, 2))
    assert beta ** 4 == KElem(Fraction(-47, 2), Fraction(-45, 2))

    t1 = beta ** 4 / KElem(-4096)
    t2 = alpha ** 4 / KElem(-4096)
    assert t1 == KElem(Fraction(47, 8192), Fraction(45, 8192))
    assert t2 == KElem(Fraction(47, 8192), Fraction(-45, 8192))
    assert t2 == t1.conj()

    # Exact identity S(p) = (F_p(t2) - F_p(t1)) / s in Q for odd primes 3 <= p <= 19
    for p in [3, 5, 7, 11, 13, 17, 19]:
        lhs = sum(Fraction(a_seq[4 * k] * (math.comb(2 * k, k) ** 3), (-4096) ** k)
                  for k in range(p))
        Fp_t1 = KElem(0)
        Fp_t2 = KElem(0)
        for k in range(p):
            c = KElem(math.comb(2 * k, k) ** 3)
            Fp_t1 = Fp_t1 + c * (t1 ** k)
            Fp_t2 = Fp_t2 + c * (t2 ** k)
        rhs = (Fp_t2 - Fp_t1) / s
        assert rhs == KElem(lhs), f"S(p) decomposition mismatch at p={p}"

    # Cubic factorization (16t - 1)^3 - 15^3 t^2 = (t - 1)(4096 t^2 - 47 t + 1)
    t_sym = sp.Symbol("t")
    assert sp.expand((16 * t_sym - 1) ** 3 - (15 ** 3) * t_sym ** 2
                     - (t_sym - 1) * (4096 * t_sym ** 2 - 47 * t_sym + 1)) == 0
    for root in [KElem(1), t1, t2]:
        val = (KElem(16) * root - KElem(1)) ** 3 - KElem(15 ** 3) * (root ** 2)
        assert val == KElem(0)

    # Legendre parameter u_1 = (1 + 3s)/32
    u1 = KElem(Fraction(1, 32), Fraction(3, 32))
    one_m_u1 = KElem(1) - u1
    assert one_m_u1 == KElem(Fraction(31, 32), Fraction(-3, 32))
    assert u1 * one_m_u1 == KElem(16) * t1
    assert u1.norm() == Fraction(1, 16)
    assert one_m_u1.norm() == Fraction(1, 1)
    Delta = KElem(16) * (u1 ** 2) * (one_m_u1 ** 2)
    assert Delta.norm() == Fraction(1, 1)
    j_Eu1 = KElem(256) * ((KElem(1) - u1 * one_m_u1) ** 3) / ((u1 * one_m_u1) ** 2)
    assert j_Eu1 == KElem(-3375)
    assert -3375 == -(15 ** 3)
    print("Check 1 (Algebraic identities in Q(sqrt(-7))): OK")


# ---------- Check 2: q-series identities & certified interval check ----------

def check_2_modular():
    N = 31  # up to q^30
    e1 = eta_prod(1, N)
    e2 = eta_prod(2, N)
    e4 = eta_prod(4, N)

    # t(q) = q * (e1 * e4 / e2^2)^24
    ratio = ps_mul(ps_mul(e1, e4, N), ps_inv(ps_mul(e2, e2, N), N), N)
    t_body = ps_pow(ratio, 24, N)
    t_q = [0] + t_body[: N - 1]

    # Product formula q / prod_{n>=1} (1 + q^{2n-1})^24
    odd_prod = [0] * N
    odd_prod[0] = 1
    for m in range(1, N, 2):
        for i in range(N - 1, m - 1, -1):
            odd_prod[i] += odd_prod[i - m]
    t_alt_body = ps_inv(ps_pow(odd_prod, 24, N), N)
    t_alt = [0] + t_alt_body[: N - 1]
    assert t_q == t_alt, "Product identity for t(tau) failed"

    # Theta(q) = e2^20 / (e1^8 * e4^8) == theta_3(2*tau)^4 == sum C(2k,k)^3 t(q)^k
    Theta_q = ps_mul(ps_pow(e2, 20, N), ps_inv(ps_mul(ps_pow(e1, 8, N), ps_pow(e4, 8, N), N), N), N)
    theta3 = [0] * N
    theta3[0] = 1
    for k in range(1, N):
        if k * k >= N:
            break
        theta3[k * k] = 2
    assert Theta_q == ps_pow(theta3, 4, N), "Theta != theta_3^4"

    F_of_t = [0] * N
    t_pow = [0] * N
    t_pow[0] = 1
    for k in range(N):
        c = math.comb(2 * k, k) ** 3
        for i in range(N):
            F_of_t[i] += c * t_pow[i]
        t_pow = ps_mul(t_pow, t_q, N)
    assert F_of_t == Theta_q, "F(t(q)) != Theta(q)"

    # lambda(2*tau) = 16 * q * e1^8 * e4^16 / e2^24
    lam_body = ps_mul(ps_mul(ps_pow(e1, 8, N), ps_pow(e4, 16, N), N), ps_inv(ps_pow(e2, 24, N), N), N)
    lam_q = [0] + [16 * x for x in lam_body[: N - 1]]
    one_m_lam = [1 - lam_q[0]] + [-x for x in lam_q[1:]]
    prod_lam = ps_mul(lam_q, one_m_lam, N)
    assert prod_lam == [16 * x for x in t_q], "lambda*(1-lambda) != 16*t"

    # j(2*tau) * t(q)^2 == (1 - 16*t(q))^3
    # Here q_z = q^2, so E_4(2*tau) = 1 + 240 * sum_{n>=1} sigma_3(n) q^{2n}
    # and Delta(2*tau) = q^2 * prod_{n>=1} (1 - q^{2n})^24.
    # Thus j(2*tau)*t(q)^2 = E_4(2*tau)^3 * (t(q)/q)^2 / prod(1 - q^{2n})^24.
    E4_2tau = [0] * N
    E4_2tau[0] = 1
    for n in range(1, N):
        if 2 * n >= N:
            break
        sig3 = sum(d ** 3 for d in range(1, n + 1) if n % d == 0)
        E4_2tau[2 * n] = 240 * sig3
    lhs = ps_mul(ps_pow(E4_2tau, 3, N), ps_mul(ps_pow(t_body, 2, N), ps_inv(ps_pow(e2, 24, N), N), N), N)
    one_m_16t = [1 - 16 * t_q[0]] + [-16 * x for x in t_q[1:]]
    rhs = ps_pow(one_m_16t, 3, N)
    assert lhs == rhs, "(1 - 16t)^3 != j(2*tau)*t^2"

    # Exact rational verification of elementary bounds used for t(tau_1) = t_1
    assert Fraction(26, 10) ** 2 < 7
    assert Fraction(314, 100) * Fraction(26, 10) / 2 > 4
    assert Fraction(27, 10) ** 4 > 50
    assert Fraction(1, 50) / (1 - Fraction(1, 50) ** 2) == Fraction(50, 2499)
    assert Fraction(50, 2499) < Fraction(1, 49)
    assert Fraction(24, 49) < Fraction(1, 2)

    # Certified mpmath interval verification of t(tau_1) = t_1
    import mpmath
    mpmath.iv.dps = 50
    iv = mpmath.iv
    rho = iv.exp(-iv.pi * iv.sqrt(7) / 2)
    assert rho < iv.mpf("0.02")  # < 1/50
    q_iv = iv.mpc(0, rho)
    # Truncate product at M = 40; tail sum_{n>40} |log(1+q^{2n-1})| < 2*rho^81 < 10^-135
    M = 40
    prod_iv = iv.mpc(1, 0)
    for n in range(1, M + 1):
        prod_iv *= (1 + q_iv ** (2 * n - 1))
    # Rigorous tail enclosure: |prod_{n>M} (1+q^{2n-1}) - 1| <= exp(sum_{n>M} rho^{2n-1}) - 1
    # = exp(rho^{2M+1}/(1 - rho^2)) - 1
    tail_bound = iv.exp(rho ** (2 * M + 1) / (1 - rho ** 2)) - 1
    assert tail_bound < iv.mpf("1e-45")
    tail_err = iv.mpf(tail_bound.b)
    tail_box = iv.mpc(iv.mpf([1 - tail_err, 1 + tail_err]), iv.mpf([-tail_err, tail_err]))
    t_tau1_iv = q_iv / ((prod_iv * tail_box) ** 24)
    t1_iv = iv.mpc(iv.mpf(47) / 8192, iv.mpf(45) * iv.sqrt(7) / 8192)
    assert t1_iv.real in t_tau1_iv.real and t1_iv.imag in t_tau1_iv.imag
    assert abs(t_tau1_iv) < iv.mpf("0.02")
    assert t_tau1_iv.imag > 0
    print("Check 2 (Modular q-series up to q^30 + certified interval t(tau_1)=t_1): OK")


# ---------- Check 3: Finite Clausen ODE & polynomial congruences ----------

def check_3_clausen_and_poly_congruences():
    z, m, t = sp.symbols("z m t")
    y = sp.Function("y")(z)
    Y = y ** 2

    def th(expr):
        return z * sp.diff(expr, z)

    y2 = (-(1 - sp.Rational(3, 2) * z) * sp.diff(y, z) - m * (m + 1) / sp.Integer(4) * y) / (z * (1 - z))
    y3 = sp.simplify(sp.diff(y2, z).subs(sp.diff(y, z, 2), y2))

    A = z * (1 - z) * sp.diff(Y, z, 2) + (1 - sp.Rational(3, 2) * z) * sp.diff(Y, z) + (m * (m + 1) / sp.Integer(2)) * Y
    assert sp.simplify((A - 2 * z * (1 - z) * sp.diff(y, z) ** 2).subs(sp.diff(y, z, 2), y2)) == 0
    B = z * sp.diff(A, z) + A + (m * (m + 1) / sp.Integer(2)) * z * sp.diff(Y, z)
    assert sp.simplify(B.subs(sp.diff(y, z, 3), y3).subs(sp.diff(y, z, 2), y2)) == 0

    poly_factor = sp.expand((t + 1) * (t ** 2 + t / 2 - m * (m + 1) / 2) - (m * (m + 1) / 2) * t
                            - (t - m) * (t + m + 1) * (t + sp.Rational(1, 2)))
    assert poly_factor == 0

    e1 = th(Y) + sp.Rational(1, 2) * Y
    e2 = th(e1) + (m + 1) * e1
    e3 = th(e2) - m * e2
    op_Y = th(th(th(Y))) - z * e3
    assert sp.simplify(z * B - op_Y) == 0

    # Verify Finite Clausen identity in Q[u] for 0 <= m <= 15
    u = sp.Symbol("u")
    for mv in range(16):
        Pm = sum(sp.binomial(mv, k) * sp.binomial(mv + k, k) * ((-u) ** k) for k in range(mv + 1))
        rhs = sum(((-1) ** k) * sp.binomial(mv + k, 2 * k) * (sp.binomial(2 * k, k) ** 2) * ((u * (1 - u)) ** k)
                  for k in range(mv + 1))
        assert sp.expand(Pm ** 2 - rhs) == 0, f"Finite Clausen failed at m={mv}"

    # Verify exact polynomial congruences mod p^2 and mod p for odd primes 3 <= p <= 31
    x = sp.Symbol("x")
    for p in range(3, 32, 2):
        if not is_prime(p):
            continue
        mv = (p - 1) // 2
        p2 = p * p
        inv16_p2 = pow(16, -1, p2)

        # F_p(u(1-u)/16) mod p^2 in (Z/p^2 Z)[u]
        Fp_poly = sp.Poly(0, u, domain=sp.ZZ)
        u1mu = sp.Poly(u - u ** 2, u, domain=sp.ZZ)
        pow_u1mu = sp.Poly(1, u, domain=sp.ZZ)
        inv16_pow = 1
        for k in range(p):
            coeff = (pow(math.comb(2 * k, k) % p2, 3, p2) * inv16_pow) % p2
            Fp_poly = sp.Poly((Fp_poly + coeff * pow_u1mu).as_expr(), u, domain=sp.ZZ)
            pow_u1mu = sp.Poly((pow_u1mu * u1mu).as_expr(), u, domain=sp.ZZ)
            inv16_pow = (inv16_pow * inv16_p2) % p2

        Pm_poly = sp.Poly(sum(((-1) ** k) * math.comb(mv, k) * math.comb(mv + k, k) * (u ** k)
                              for k in range(mv + 1)), u, domain=sp.ZZ)
        Pm_sq = sp.Poly((Pm_poly * Pm_poly).as_expr(), u, domain=sp.ZZ)
        diff_p2 = sp.Poly((Fp_poly - Pm_sq).as_expr(), u, domain=sp.ZZ)
        assert all(c % p2 == 0 for c in diff_p2.all_coeffs()), f"Fp != Pm^2 mod p^2 at p={p}"

        Hp_poly = sp.Poly(sum((math.comb(mv, k) ** 2) * (u ** k) for k in range(mv + 1)), u, domain=sp.ZZ)
        diff_p = sp.Poly((Pm_poly - Hp_poly).as_expr(), u, domain=sp.ZZ)
        assert all(c % p == 0 for c in diff_p.all_coeffs()), f"Pm != Hp mod p at p={p}"

        # Also check [x^{p-1}] (x(x-1)(x-u))^m == (-1)^m H_p(u) in Z[u] for p <= 19
        if p <= 19:
            expr = sp.expand((x * (x - 1) * (x - u)) ** mv)
            coeff_xp1 = sp.Poly(expr, x).nth(p - 1)
            assert sp.expand(coeff_xp1 - ((-1) ** mv) * Hp_poly.as_expr()) == 0

    print("Check 3 (Finite Clausen ODE + polynomial congruences for 3 <= p <= 31): OK")


# ---------- Check 4: Ramified prime p = 7 ----------

def check_4_ramified_p7():
    a_seq = seq_a_list(28)
    exact_S7 = sum(Fraction(a_seq[4 * k] * (math.comb(2 * k, k) ** 3), (-4096) ** k) for k in range(7))
    assert exact_S7.denominator % 7 != 0
    assert exact_S7.numerator % 49 == 0
    assert exact_S7.numerator % 343 != 0

    inv49 = pow(-4096, -1, 49)
    inv343 = pow(-4096, -1, 343)
    terms49 = []
    for k in range(7):
        ak = a_seq[4 * k]
        cb = math.comb(2 * k, k)
        t49 = (ak * (cb ** 3) * pow(inv49, k, 49)) % 49
        terms49.append((k, ak, cb, t49))
    assert sum(t[3] for t in terms49) % 49 == 0
    assert s_mod_p_m(7, 2) == 0
    assert s_mod_p_m(7, 3) == 294 == 6 * 49
    print(f"Check 4 (Ramified p=7: S(7) mod 49 = 0, S(7) mod 343 = 294; terms mod 49 = {[t[3] for t in terms49]}): OK")


# ---------- Check 5: Inert primes p == 3, 5, 6 (mod 7) ----------

def check_5_inert_primes():
    t1 = KElem(Fraction(47, 8192), Fraction(45, 8192))
    t2 = t1.conj()
    u1 = KElem(Fraction(1, 32), Fraction(3, 32))
    count = 0
    for p in range(3, 201, 2):
        if not is_prime(p) or (p % 7) not in (3, 5, 6):
            continue
        m = (p - 1) // 2
        p2 = p * p
        u1_p = kmod_from_kelem(u1, p)
        assert eval_Hp_kmod(u1_p, p, p) == (0, 0), f"H_p(u_1) != 0 mod p at p={p}"
        assert eval_Pm_1m2u_kmod(u1_p, m, p) == (0, 0), f"P_m(1-2u_1) != 0 mod p at p={p}"
        t1_p2 = kmod_from_kelem(t1, p2)
        t2_p2 = kmod_from_kelem(t2, p2)
        assert eval_Fp_kmod(t1_p2, p, p2) == (0, 0), f"F_p(t_1) != 0 mod p^2 at p={p}"
        assert eval_Fp_kmod(t2_p2, p, p2) == (0, 0), f"F_p(t_2) != 0 mod p^2 at p={p}"
        assert s_mod_p_m(p, 2) == 0
        count += 1
    print(f"Check 5 (Inert primes p <= 200, count={count}, incl. p=3,5): OK")


# ---------- Check 6: Split primes p == 1, 2, 4 (mod 7) ----------

def find_x_y_split(p: int) -> tuple[int, int]:
    """Find positive integers x, y with x^2 + 7*y^2 = p."""
    for y in range(1, math.isqrt(p // 7) + 1):
        rem = p - 7 * y * y
        x = math.isqrt(rem)
        if x * x == rem and x > 0:
            return x, y
    raise AssertionError(f"No x^2 + 7y^2 = {p}")


def sqrt_minus7_mod_p3(p: int) -> int:
    """Compute sigma_p mod p^3 with sigma_p^2 == -7 (mod p^3)."""
    r = None
    for a in range(1, p):
        if (a * a + 7) % p == 0:
            r = a
            break
    assert r is not None
    # Two Hensel lift steps: mod p -> mod p^2 -> mod p^4 (reduce mod p^3)
    mod = p
    for _ in range(2):
        mod *= mod
        inv2r = pow((2 * r) % mod, -1, mod)
        r = (r - (r * r + 7) * inv2r) % mod
    p3 = p ** 3
    r %= p3
    assert (r * r + 7) % p3 == 0
    return r


def check_6_split_primes():
    count = 0
    for p in range(3, 201, 2):
        if not is_prime(p) or (p % 7) not in (1, 2, 4):
            continue
        p3 = p ** 3
        x, y = find_x_y_split(p)
        sig = sqrt_minus7_mod_p3(p)
        # Orient y so gamma_p = x + y*sig is a p-adic unit
        if (x + y * sig) % p == 0:
            y = -y
        gamma_p = (x + y * sig) % p3
        assert gamma_p % p != 0
        assert ((x - y * sig) * gamma_p) % p3 == p

        inv8192 = pow(8192, -1, p3)
        t1_p3 = ((47 + 45 * sig) * inv8192) % p3
        t2_p3 = ((47 - 45 * sig) * inv8192) % p3

        def eval_Fp_mod_p3(t_val):
            acc = 0
            tp = 1
            for k in range(p):
                c = pow(math.comb(2 * k, k) % p3, 3, p3)
                acc = (acc + c * tp) % p3
                tp = (tp * t_val) % p3
            return acc

        gamma_sq = (gamma_p * gamma_p) % p3
        # Also verify rational form 4x^2 - 2p - p^2/(4x^2) mod p^3
        rat_sq = (4 * x * x - 2 * p - (p * p) * pow(4 * x * x, -1, p3)) % p3
        assert gamma_sq == rat_sq

        assert eval_Fp_mod_p3(t1_p3) == gamma_sq, f"Beukers Thm 1.15 mismatch at t1, p={p}"
        assert eval_Fp_mod_p3(t2_p3) == gamma_sq, f"Beukers Thm 1.15 mismatch at t2, p={p}"
        assert s_mod_p_m(p, 3) == 0
        count += 1
    print(f"Check 6 (Split primes p <= 200, Beukers Thm 1.15, count={count}): OK")


# ---------- Check 7: Direct verification up to p <= 300 ----------

def check_7_direct_range():
    c1_count = 0
    c2_count = 0
    for p in range(3, 301, 2):
        if not is_prime(p):
            continue
        assert s_mod_p_m(p, 2) == 0, f"conjecture_1 failed at p={p}"
        c1_count += 1
        if (p % 7) in (1, 2, 4):
            assert s_mod_p_m(p, 3) == 0, f"conjecture_2 failed at p={p}"
            c2_count += 1
    print(f"Check 7 (Direct Lean-faithful check 3 <= p <= 300: {c1_count} odd primes mod p^2, {c2_count} split primes mod p^3): OK")


def main():
    check_1_algebra()
    check_2_modular()
    check_3_clausen_and_poly_congruences()
    check_4_ramified_p7()
    check_5_inert_primes()
    check_6_split_primes()
    check_7_direct_range()
    print("PASS")


if __name__ == "__main__":
    main()
