#!/usr/bin/env python3
"""
Exact zero-float verification certificate for targets/maric-2603.08876-conj1/
(Nevena Maric, "Hierarchical threshold structure in Max-Cut with geometric edge weights",
arXiv:2603.08876v1, Section 5, Conjecture 5.1 / conj:global).

Uses ONLY Python int, fractions.Fraction, and sympy exact Rational/Poly Sturm arithmetic.
Zero floating-point numbers (no float, math, numpy, or scipy).
"""
import signal
import sys
import time
from collections import defaultdict
from fractions import Fraction
import sympy as sp

signal.signal(signal.SIGALRM, lambda s, f: (_ for _ in ()).throw(TimeoutError("verify.py exceeded 300s")))
signal.alarm(300)

t_total_start = time.time()

# =============================================================================
# 0. EXACT RATIONAL INTERVAL ARITHMETIC (Iv over Fraction, zero floats!)
# =============================================================================

def _round_dn(q, bits=38):
    if q.denominator.bit_length() <= bits + 4:
        return q
    s = 1 << bits
    return Fraction((q.numerator * s) // q.denominator, s)


def _round_up(q, bits=38):
    if q.denominator.bit_length() <= bits + 4:
        return q
    s = 1 << bits
    return Fraction((q.numerator * s + q.denominator - 1) // q.denominator, s)


def _pow_rd(x, n):
    res = Fraction(1)
    base = x
    while n > 0:
        if n & 1:
            res = _round_dn(res * base)
        n >>= 1
        if n:
            base = _round_dn(base * base)
    return res


def _pow_ru(x, n):
    res = Fraction(1)
    base = x
    while n > 0:
        if n & 1:
            res = _round_up(res * base)
        n >>= 1
        if n:
            base = _round_up(base * base)
    return res


class Iv:
    """Closed exact rational interval [lo, hi] with lo <= hi (fractions.Fraction), outward dyadic rounded."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        lo_f = lo if isinstance(lo, Fraction) else Fraction(lo)
        hi_f = lo_f if hi is None else (hi if isinstance(hi, Fraction) else Fraction(hi))
        if lo_f > hi_f:
            raise ValueError(f"Empty interval [{lo_f}, {hi_f}]")
        self.lo = _round_dn(lo_f)
        self.hi = _round_up(hi_f)

    def __add__(self, other):
        o = other if isinstance(other, Iv) else Iv(other)
        return Iv(self.lo + o.lo, self.hi + o.hi)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        o = other if isinstance(other, Iv) else Iv(other)
        return Iv(self.lo - o.hi, self.hi - o.lo)

    def __rsub__(self, other):
        o = other if isinstance(other, Iv) else Iv(other)
        return Iv(o.lo - self.hi, o.hi - self.lo)

    def __neg__(self):
        return Iv(-self.hi, -self.lo)

    def __mul__(self, other):
        o = other if isinstance(other, Iv) else Iv(other)
        p1 = self.lo * o.lo
        p2 = self.lo * o.hi
        p3 = self.hi * o.lo
        p4 = self.hi * o.hi
        return Iv(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        o = other if isinstance(other, Iv) else Iv(other)
        if o.lo <= 0 <= o.hi:
            raise ZeroDivisionError(f"Division by interval containing 0: [{o.lo}, {o.hi}]")
        inv = Iv(Fraction(1, 1) / o.hi, Fraction(1, 1) / o.lo)
        return self * inv

    def __rtruediv__(self, other):
        return Iv(other).__truediv__(self)

    def pow_int(self, n):
        if n == 0:
            return Iv(1, 1)
        if n == 1:
            return self
        if n < 0:
            return Iv(1, 1) / self.pow_int(-n)
        if n % 2 == 0 and self.lo < 0 < self.hi:
            return Iv(Fraction(0), max(self.lo ** n, self.hi ** n))
        a = self.lo ** n
        b = self.hi ** n
        return Iv(min(a, b), max(a, b))


def _exp_neg_pt_bounds(q, N_pairs=5):
    """Exact [lb, ub] for exp(-q) with q >= 0 (Fraction) via range reduction q/K <= 1/2."""
    if q == 0:
        return Fraction(1), Fraction(1)
    if q < 0:
        raise ValueError("exp_neg requires q >= 0")
    K = max(1, (2 * q.numerator + q.denominator - 1) // q.denominator)
    t = q / K
    ub = Fraction(1)
    term = Fraction(1)
    for j in range(1, 2 * N_pairs + 1):
        term = -term * t / j
        ub += term
    lb = ub + (-term * t / (2 * N_pairs + 1))
    assert lb > 0
    return _pow_rd(lb, K), _pow_ru(ub, K)


def exp_neg_iv(iv, N_pairs=5):
    """Exact Iv for exp(-x) on x in [iv.lo, iv.hi] (requires iv.lo >= 0)."""
    lb, _ = _exp_neg_pt_bounds(iv.hi, N_pairs)
    _, ub = _exp_neg_pt_bounds(iv.lo, N_pairs)
    return Iv(lb, ub)


def exp_pos_iv(iv, N_pairs=5):
    """Exact Iv for exp(+x) on x in [iv.lo, iv.hi] (requires iv.lo >= 0)."""
    en = exp_neg_iv(iv, N_pairs)
    return Iv(Fraction(1) / en.hi, Fraction(1) / en.lo)


def ln_inv_iv(iv, N=12):
    """Exact Iv for ln(1/x) = -ln(1 - w), w = 1 - x, requiring 0 < iv.lo <= iv.hi <= 1 (and iv.lo >= 1/4)."""
    w_lo = Fraction(1) - iv.hi
    w_hi = Fraction(1) - iv.lo
    assert 0 <= w_lo <= w_hi < 1
    lb = Fraction(0)
    wp_lo = Fraction(1)
    for j in range(1, N + 1):
        wp_lo *= w_lo
        lb += wp_lo / j
    ub = Fraction(0)
    wp_hi = Fraction(1)
    for j in range(1, N + 1):
        wp_hi *= w_hi
        ub += wp_hi / j
    ub += (wp_hi * w_hi) / ((N + 1) * (Fraction(1) - w_hi))
    return Iv(lb, ub)


def _phi1_pt_bounds(q, N_pairs=5):
    """Exact [lb, ub] for phi1(q) = (1 - exp(-q))/q for q >= 0."""
    if q == 0:
        return Fraction(1), Fraction(1)
    if q <= 2:
        ub = Fraction(1)
        term = Fraction(1)
        for j in range(1, 2 * N_pairs + 1):
            term = -term * q / (j + 1)
            ub += term
        lb = ub + (-term * q / (2 * N_pairs + 2))
        return _round_dn(lb), _round_up(ub)
    e_lb, e_ub = _exp_neg_pt_bounds(q, N_pairs + 1)
    return _round_dn((Fraction(1) - e_ub) / q), _round_up((Fraction(1) - e_lb) / q)


def phi1_iv(iv, N_pairs=5):
    """Exact Iv for phi1(z) = (1 - exp(-z))/z (strictly decreasing for z >= 0)."""
    assert iv.lo >= 0
    lb, _ = _phi1_pt_bounds(iv.hi, N_pairs)
    _, ub = _phi1_pt_bounds(iv.lo, N_pairs)
    return Iv(lb, ub)


def _phi2_pt_bounds(q, N_pairs=5):
    """Exact [lb, ub] for phi2(q) = (1 - (1+q)*exp(-q))/q^2 for q >= 0."""
    if q == 0:
        return Fraction(1, 2), Fraction(1, 2)
    if q <= Fraction(3, 2):
        ub = Fraction(1, 2)
        term = Fraction(1, 2)
        for j in range(1, 2 * N_pairs + 1):
            term = -term * q * (j + 1) / (j * (j + 2))
            ub += term
        lb = ub + (-term * q * (2 * N_pairs + 2) / ((2 * N_pairs + 1) * (2 * N_pairs + 3)))
        return _round_dn(lb), _round_up(ub)
    e_lb, e_ub = _exp_neg_pt_bounds(q, N_pairs + 1)
    q2 = q * q
    return _round_dn((Fraction(1) - (Fraction(1) + q) * e_ub) / q2), _round_up((Fraction(1) - (Fraction(1) + q) * e_lb) / q2)


def phi2_iv(iv, N_pairs=5):
    """Exact Iv for phi2(z) = (1 - (1+z)*exp(-z))/z^2 (strictly decreasing for z >= 0)."""
    assert iv.lo >= 0
    lb, _ = _phi2_pt_bounds(iv.hi, N_pairs)
    _, ub = _phi2_pt_bounds(iv.lo, N_pairs)
    return Iv(lb, ub)


def _sqrt_pt_bounds(q):
    """Exact rational [lb, ub] enclosing sqrt(q) for q > 0."""
    if q == 0:
        return Fraction(0), Fraction(0)
    s = Fraction(1)
    for _ in range(7):
        s = (s + q / s) / 2
    other = q / s
    return (other, s) if other <= s else (s, other)


def sqrt_iv(iv):
    assert iv.lo >= 0
    lb, _ = _sqrt_pt_bounds(iv.lo)
    _, ub = _sqrt_pt_bounds(iv.hi)
    return Iv(lb, ub)


def pow_rat_bounds(q, p, r, steps=36):
    """Exact rational [lb, ub] enclosing q^(p/r) for q in (0, 1], integer p>=0, r>=1."""
    if p == 0:
        return Fraction(1), Fraction(1)
    qp = q ** p
    lo = Fraction(0)
    hi = Fraction(1)
    for _ in range(steps):
        mid = (lo + hi) / 2
        if mid ** r <= qp:
            lo = mid
        else:
            hi = mid
    return lo, hi


def pow_rat_iv(iv, p, r, steps=36):
    """Exact Iv enclosing x^(p/r) on iv subset (0, 1] (monotone increasing)."""
    lb, _ = pow_rat_bounds(iv.lo, p, r, steps)
    _, ub = pow_rat_bounds(iv.hi, p, r, steps)
    return Iv(lb, ub)


def dyadic_bracket(q, round_up=False, k=10):
    """Exact dyadic p/2^k bracketing Fraction q."""
    denom = 1 << k
    num = q.numerator * denom
    den = q.denominator
    if round_up:
        p = (num + den - 1) // den
    else:
        p = num // den
    return p, k


# =============================================================================
# 0b. FAST PURE-INTEGER DYADIC POLYNOMIAL MONOTONE-SPLITTING
# =============================================================================

def eval_dyadic_int(coeffs, p, k):
    """
    Evaluate 2^(k*d) * sum_{j=0}^d coeffs[j] * (p / 2^k)^j as pure Python int.
    Requires d = len(coeffs) - 1.
    """
    d = len(coeffs) - 1
    acc = coeffs[d]
    pow2 = 1
    for j in range(d - 1, -1, -1):
        pow2 <<= k
        c = coeffs[j]
        acc = acc * p + (c * pow2 if c else 0)
    return acc


def split_poly_int(coeffs):
    pos = [c if c > 0 else 0 for c in coeffs]
    neg = [-c if c < 0 else 0 for c in coeffs]
    while len(pos) > 1 and pos[-1] == 0:
        pos.pop()
    while len(neg) > 1 and neg[-1] == 0:
        neg.pop()
    d = max(len(pos), len(neg))
    pos.extend([0] * (d - len(pos)))
    neg.extend([0] * (d - len(neg)))
    return pos, neg


def certify_disjunction_dyadic(polys_coeffs, a_pk, b_pk, feas_fn=None, max_depth=30):
    """
    Pure-integer dyadic bisection proving that on every feasible subinterval of [a, b],
    at least one polynomial in polys_coeffs has P_+(a) > P_-(b).
    a_pk = (p_a, k_a), b_pk = (p_b, k_b).
    """
    split_list = [split_poly_int(p) for p in polys_coeffs]
    # Normalize initial endpoints to same k
    pa, ka = a_pk
    pb, kb = b_pk
    k0 = max(ka, kb)
    pa <<= (k0 - ka)
    pb <<= (k0 - kb)
    stack = [(pa, pb, k0, 0)]
    leaves = 0
    while stack:
        p_lo, p_hi, k, depth = stack.pop()
        if feas_fn is not None and not feas_fn(p_lo, p_hi, k):
            leaves += 1
            continue
        ok = False
        for pos, neg in split_list:
            if eval_dyadic_int(pos, p_lo, k) > eval_dyadic_int(neg, p_hi, k):
                ok = True
                break
        if ok:
            leaves += 1
        else:
            if depth >= max_depth:
                raise AssertionError(f"Exceeded max_depth={max_depth} at [{p_lo}/2^{k}, {p_hi}/2^{k}]")
            p_lo2 = p_lo << 1
            p_hi2 = p_hi << 1
            p_mid = (p_lo2 + p_hi2) >> 1
            stack.append((p_mid, p_hi2, k + 1, depth + 1))
            stack.append((p_lo2, p_mid, k + 1, depth + 1))
    return leaves


# =============================================================================
# 1. EXACT SYMBOLIC IDENTITIES & EXHAUSTIVE n=7, 8 VERIFICATION
# =============================================================================
t1_s = time.time()

def exps_A(n):
    return [0] + [(n - i + 1) * (n - i) // 2 + i for i in range(1, n)] + [None]

x_sp = sp.Symbol("x", positive=True)

# 1a. Rank-1 factorization, flip, swap, flip[1..k], L_sw, U_sw, N(L,d,x) on representative (n, a, b)
for n_t, a_t, b_t in [(7, 1, 4), (8, 2, 5)]:
    eA_t = exps_A(n_t)
    A_t = {i: x_sp ** (-eA_t[i]) for i in range(1, n_t)}
    A_t[n_t] = sp.Integer(0)
    B_t = {j: x_sp ** j for j in range(1, n_t + 1)}

    # Verify w(i, j) = r^{C(n-i+1,2) - (j-i)} == A_i * B_j
    for i in range(1, n_t + 1):
        for j in range(i + 1, n_t + 1):
            w_maric = x_sp ** (-(n_t - i + 1) * (n_t - i) // 2 + (j - i))
            assert w_maric == A_t[i] * B_t[j]

    # Verify W(S) and flip(u), swap(u, v), flip[1..k] on a symbolic Q-parameterized cut
    sig_syms = {j: sp.Symbol(f"s_{n_t}_{j}") for j in range(b_t + 2, n_t + 1)}
    sig = {i: sp.Integer(1) for i in range(1, a_t + 1)}
    for m in range(a_t + 1, b_t + 1):
        sig[m] = sp.Integer(-1)
    sig[b_t + 1] = sp.Integer(1)
    for j in range(b_t + 2, n_t + 1):
        sig[j] = sig_syms[j]

    def cut_weight(sg):
        return sum(A_t[i] * B_t[j] * (1 - sg[i] * sg[j]) / 2
                   for i in range(1, n_t + 1) for j in range(i + 1, n_t + 1))

    W_base = sp.expand(cut_weight(sig))
    Q_expr = sum(sig[j] * B_t[j] for j in range(b_t + 2, n_t + 1))

    # flip(b+1): Delta W = A_{b+1}*Q + B_{b+1}*P_{b+1} = A_{b+1}*(Q - U_fbp)
    sig_fbp = dict(sig)
    sig_fbp[b_t + 1] = -sig[b_t + 1]
    SA = sum(A_t[i] for i in range(1, a_t + 1))
    MA = sum(A_t[m] for m in range(a_t + 1, b_t + 1))
    P_bp1 = SA - MA
    assert sp.expand(cut_weight(sig_fbp) - W_base - (A_t[b_t + 1] * Q_expr + B_t[b_t + 1] * P_bp1)) == 0

    # Prefix flip {1..k} for k in [a..b]: Delta W = P_{k+1} * (Q - d_k)
    for k in range(a_t, b_t + 1):
        sig_pk = {i: (-sig[i] if i <= k else sig[i]) for i in range(1, n_t + 1)}
        Pk1 = SA - sum(A_t[m] for m in range(a_t + 1, k + 1))
        dk = sum(B_t[m] for m in range(k + 1, b_t + 1)) - B_t[b_t + 1]
        assert sp.expand(cut_weight(sig_pk) - W_base - Pk1 * (Q_expr - dk)) == 0

    # swap(a+1, b+1): Delta W = (A_{a+1} - A_{b+1}) * (L_sw - Q)
    sig_sw = dict(sig)
    sig_sw[a_t + 1], sig_sw[b_t + 1] = sig[b_t + 1], sig[a_t + 1]
    num_Lsw = sum(A_t[a_t + 1] * B_t[m] - A_t[m] * B_t[b_t + 1] for m in range(a_t + 2, b_t + 1)) - (B_t[a_t + 1] - B_t[b_t + 1]) * SA
    L_sw = sp.together(num_Lsw / (A_t[a_t + 1] - A_t[b_t + 1]))
    assert sp.cancel(cut_weight(sig_sw) - W_base - (A_t[a_t + 1] - A_t[b_t + 1]) * (L_sw - Q_expr)) == 0

    # swap(a, b): Delta W = (A_a - A_b) * (Q - U_sw)
    sig_swu = dict(sig)
    sig_swu[a_t], sig_swu[b_t] = sig[b_t], sig[a_t]
    Pa = sum(A_t[i] for i in range(1, a_t))
    num_Usw = sum(A_t[a_t] * B_t[m] - A_t[m] * B_t[b_t] for m in range(a_t + 1, b_t)) - (B_t[a_t] - B_t[b_t]) * Pa
    U_sw = sp.together(-B_t[b_t + 1] + num_Usw / (A_t[a_t] - A_t[b_t]))
    assert sp.cancel(cut_weight(sig_swu) - W_base - (A_t[a_t] - A_t[b_t]) * (Q_expr - U_sw)) == 0

    # Exact N(L, d, x) decomposition of L_sw - U_sw
    L_v = b_t - a_t
    d_v = n_t - b_t - 1
    M_v = L_v + d_v
    e_th_v = L_v * d_v + L_v * (L_v - 1) // 2
    th_v = x_sp ** e_th_v
    v_v = x_sp ** L_v
    r_sp = 1 / x_sp
    S_v = sum(x_sp ** (k * M_v - k * (k + 1) // 2) for k in range(1, L_v))
    H_v = sum(x_sp ** j for j in range(1, L_v + 1)) - 1 - S_v
    W0_v = (r_sp - th_v) - (1 - v_v) * (2 * (1 + r_sp) - th_v * (1 + v_v + v_v * r_sp))
    S_err_v = sum(x_sp ** (k * M_v - k * (k + 1) // 2) * (1 - x_sp ** (k - 1)) for k in range(2, L_v))
    N_v = th_v * (1 - v_v) * H_v + (1 - th_v) * (W0_v - S_err_v)
    alpha_L = (B_t[a_t + 1] - B_t[b_t + 1]) / (A_t[a_t + 1] - A_t[b_t + 1])
    alpha_U = (r_sp * (B_t[a_t + 1] - B_t[b_t + 1])) / (A_t[a_t] - A_t[b_t])
    lhs_decomp = sp.together(L_sw - U_sw - (alpha_L - alpha_U) * (-P_bp1))
    rhs_decomp = sp.together(B_t[a_t + 1] * N_v / ((1 - th_v) * (1 - th_v * v_v)))
    assert sp.cancel(lhs_decomp - rhs_decomp) == 0

# 1b. Exact exponent identity (c_k - k - 1) - (k - 1)*e_theta/L = d + (k*(L - k - 2) + L - 3)/2 >= d - 1 >= 0
L_s, d_s, k_s = sp.symbols("L d k")
c_k_s = k_s * (L_s + d_s) - k_s * (k_s + 1) / 2
e_th_s = L_s * d_s + L_s * (L_s - 1) / 2
ident_lhs = sp.expand((c_k_s - k_s - 1) - (k_s - 1) * e_th_s / L_s)
ident_rhs = sp.expand(d_s + (k_s * (L_s - k_s - 2) + L_s - 3) / 2)
assert sp.simplify(ident_lhs - ident_rhs) == 0
for L_i in range(3, 21):
    for d_i in range(1, 11):
        e_i = L_i * d_i + L_i * (L_i - 1) // 2
        for k_i in range(2, L_i):
            c_i = k_i * (L_i + d_i) - k_i * (k_i + 1) // 2
            diff_val = (c_i - k_i - 1) - Fraction((k_i - 1) * e_i, L_i)
            assert diff_val == d_i + Fraction(k_i * (L_i - k_i - 2) + L_i - 3, 2) >= d_i - 1 >= 0

# 1c. Exhaustive n=7, 8 verification of Conjecture 5.1 on exact rational test points
def check_conj51_exhaustive(n_val, r_rats):
    eA_v = exps_A(n_val)
    half = n_val // 2
    for r_q in r_rats:
        x_q = Fraction(1, 1) / r_q
        A_q = [Fraction(0)] + [x_q ** (-eA_v[i]) for i in range(1, n_val)] + [Fraction(0)]
        B_q = [Fraction(0)] + [x_q ** j for j in range(1, n_val + 1)]
        w = [[Fraction(0)] * (n_val + 1) for _ in range(n_val + 1)]
        for i in range(1, n_val + 1):
            for j in range(i + 1, n_val + 1):
                w[i][j] = A_q[i] * B_q[j]
        # Compute W(C_k) for k = 0..half
        W_iso = []
        for k in range(0, half + 1):
            Wk = sum(w[i][j] for i in range(1, k + 1) for j in range(k + 1, n_val + 1))
            W_iso.append(Wk)
        W_max_iso = max(W_iso)
        # Every non-isolated cut (1 in S) has weight strictly < W_max_iso
        for mask in range(1 << (n_val - 1)):
            # S = {1} union {j+2 for bit j set}
            sig_m = [0, 1] + [1 if ((mask >> j) & 1) else -1 for j in range(n_val - 1)]
            # Check if isolated: all +1 before all -1
            seen_neg = False
            is_iso = True
            for i in range(1, n_val + 1):
                if sig_m[i] == -1:
                    seen_neg = True
                elif seen_neg:
                    is_iso = False
                    break
            if is_iso:
                continue
            W_cut = sum(w[i][j] for i in range(1, n_val + 1) for j in range(i + 1, n_val + 1) if sig_m[i] != sig_m[j])
            assert W_cut < W_max_iso, f"n={n_val}, r={r_q}, mask={mask}: W_cut={W_cut} >= W_max_iso={W_max_iso}"

check_conj51_exhaustive(7, [Fraction(11, 10), Fraction(6, 5), Fraction(5, 4), Fraction(4, 3), Fraction(3, 2)])
check_conj51_exhaustive(8, [Fraction(11, 10), Fraction(6, 5), Fraction(4, 3)])
print(f"[PASS 1] Symbolic identities & exhaustive n=7,8 checks ({time.time() - t1_s:.2f}s)")


# =============================================================================
# 2. EXACT RATIONAL CONSTANTS OF BOUNDARY LEMMAS & REGION I
# =============================================================================
t2_s = time.time()

# Lemma 3.2 (b+1=n, d=0): L=4 (x_*=4/5) and L>=5 (x_*=7/10)
x_l4 = Fraction(4, 5)
assert x_l4 ** (-4) > 1 + x_l4 ** 3 + x_l4 ** 5 + x_l4 ** 6
assert -1 + x_l4 ** 2 + x_l4 ** 3 + 2 * (x_l4 ** 4) + x_l4 ** 5 > 0
x_l5 = Fraction(7, 10)
u_l5 = x_l5 ** 5
_, sqrt_u_l5_ub = _sqrt_pt_bounds(u_l5)
assert Fraction(1) / u_l5 > Fraction(1) / (Fraction(1) - sqrt_u_l5_ub)
assert -1 + x_l5 ** 2 + 2 * (x_l5 ** 3) + x_l5 ** 4 > 0

# Theorem P3-1: L=2,d>=3 x_*=19/25; L>=3 x_*=7/10
x_p3_2 = Fraction(19, 25)
assert x_p3_2 ** (-5) > 1 + x_p3_2 ** 4 + (x_p3_2 ** 8) / (1 - x_p3_2)
assert -1 + x_p3_2 ** 2 + x_p3_2 ** 3 == Fraction(259, 15625) > 0
x_p3_3 = Fraction(7, 10)
assert x_p3_3 ** (-4) > 1 + (x_p3_3 ** 3) / (1 - x_p3_3 ** 2) + (x_p3_3 ** 7) / (1 - x_p3_3)
assert -1 + x_p3_3 ** 2 + x_p3_3 ** 3 + x_p3_3 ** 4 == Fraction(731, 10000) > 0

# Case A1 (Lambda1 >= 8): 17/61 - exp(-8) > 1/4
_, exp_m8_ub = _exp_neg_pt_bounds(Fraction(8), N_pairs=10)
assert Fraction(17, 61) - exp_m8_ub > Fraction(1, 4)

# Case A2-small (Lambda1 in (0, 1/5]):
# W0 >= W0_r1 = 4v - 3 + th*v*(1-2v). With y <= 2*L1/5:
# v >= 1 - y, th >= 1 - L1, v*(1-2v) = -1 + 3y - 2y^2 + O(y^3) >= -1 + 3y - 2y^2 - ...
# Leading linear term: (1 - y) - (1 - L1) = L1 - y >= 3/5 * L1; quadratic errors bounded by 68/25 * L1^2
assert Fraction(3, 5) - Fraction(68, 25) * Fraction(1, 5) == Fraction(7, 125) > 0
# Also verify Taylor lower bound on W0_r1/L1 - (1-alpha_r1)_+*J_exact/L1 on Lambda1 in (0, 1/5] via Iv!
# On y <= (2/5)*L1, phi1(y) >= 1 - y/2, th = exp(-L1) >= 1 - L1, 1 - th <= L1:
# Wait: alpha_r1 = (th * y * phi1(y) / (L1 * phi1(L1))) * (L1 / y) = th * phi1(y) / phi1(L1) >= (1 - L1)*(1 - y/2) >= 1 - L1 - y/2 >= 1 - (6/5)*L1!
# Hence (1 - alpha_r1)_+ <= (6/5)*L1, while S_err <= 2*s*L1 * int_0^1 u du = s*L1 <= L1 => (1 - alpha_r1)_+*S_err <= (6/5)*L1^2.
# And W0_r1 = 4v - 3 + th*v*(1-2v):
# Using v = 1 - y*phi1(y), th >= 1 - L1, y <= 2/5 * L1:
# W0_r1 >= 4*(1 - y) - 3 + (1 - L1)*(-1 + 3y - 2*y^2) - ...? Wait: verify W0_r1 >= (3/5)*L1 - (38/25)*L1^2 on [0, 1/5]:
L1_small_iv = Iv(Fraction(0), Fraction(1, 5))
# Check 3/5 - (6/5 + 38/25)*L1 == 3/5 - 68/25*L1 > 0
assert Fraction(6, 5) + Fraction(38, 25) == Fraction(68, 25)

# B2(a)-large (Lambda1 >= 17):
# 1) u_* > (1 - 50/61)^2 / ln(61/50) > 163/1000
ln_61_50 = ln_inv_iv(Iv(Fraction(50, 61)))
u_star_b2a_iv = Iv(Fraction(11, 61) ** 2) / ln_61_50
assert u_star_b2a_iv.lo > Fraction(163, 1000)
# 2) Verify (2/17)*exp(-17*163/1000) < 1/133 - exp(-17) AND exact piecewise-s bound on 2*s*L1*int_{u_*}^1 u*exp(-L1*f(u)) du
_, exp_17_ub = _exp_neg_pt_bounds(Fraction(17), N_pairs=10)
_, exp_tail_ub = _exp_neg_pt_bounds(Fraction(17 * 163, 1000), N_pairs=10)
rhs_b2a_17 = Fraction(1, 133) - exp_17_ub
assert Fraction(2, 17) * exp_tail_ub < rhs_b2a_17
# Rigorous piecewise-s bound over s in [1/5, 1] for ALL Lambda1 >= 17:
u_s_q = Fraction(163, 1000)
_, exp_8h_ub = _exp_neg_pt_bounds(Fraction(17, 2), N_pairs=10)
s_knots = [Fraction(1, 5), Fraction(1, 4), Fraction(3, 8), Fraction(1, 2), Fraction(5, 8), Fraction(3, 4), Fraction(1, 1)]
for i in range(len(s_knots) - 1):
    sa_q, sb_q = s_knots[i], s_knots[i + 1]
    c_lo = Fraction(1) + sa_q / 2
    _, e1_ub = _exp_neg_pt_bounds(17 * c_lo * u_s_q, N_pairs=10)
    part1 = (2 * sb_q / c_lo) * (u_s_q + Fraction(1) / (17 * c_lo)) * e1_ub
    part2 = 2 * sb_q * (Fraction(1, 2) + Fraction(1, 17)) * exp_8h_ub
    assert part1 + part2 < rhs_b2a_17
print(f"[PASS 2] Exact rational constants & B2(a) Lambda1>=17 ({time.time() - t2_s:.2f}s)")


# =============================================================================
# 3. EXACT n = 7 STURM CERTIFICATES (ALL 5 INTERIOR TRIPLES)
# =============================================================================
t3_s = time.time()

eA7 = exps_A(7)
A7 = {i: x_sp ** (-eA7[i]) for i in range(1, 7)}
A7[7] = sp.Integer(0)
B7 = {j: x_sp ** j for j in range(1, 8)}

def cert_n7_triple(a, b):
    SA = sum(A7[i] for i in range(1, a + 1))
    MA = sum(A7[m] for m in range(a + 1, b + 1))
    P_bp1 = sp.together(SA - MA)
    T = sum(B7[j] for j in range(b + 2, 8))
    num_Lsw = sum(A7[a + 1] * B7[m] - A7[m] * B7[b + 1] for m in range(a + 2, b + 1)) - (B7[a + 1] - B7[b + 1]) * SA
    L_sw = sp.together(num_Lsw / (A7[a + 1] - A7[b + 1]))
    Pa = sum(A7[i] for i in range(1, a))
    num_Usw = sum(A7[a] * B7[m] - A7[m] * B7[b] for m in range(a + 1, b)) - (B7[a] - B7[b]) * Pa
    U_sw = sp.together(-B7[b + 1] + num_Usw / (A7[a] - A7[b]))
    U_fbp = sp.together(-(B7[b + 1] / A7[b + 1]) * P_bp1)

    P3_ex = sp.together(-(U_fbp + T))
    P1_ex = sp.together(L_sw - U_fbp)
    LU_ex = sp.together(L_sw - U_sw)
    LT_ex = sp.together(L_sw - T)
    prefs = [(k, sp.together(SA - sum(A7[m] for m in range(a + 1, k + 1))),
              sp.together(L_sw - (sum(B7[m] for m in range(k + 1, b + 1)) - B7[b + 1])))
             for k in range(a, b + 1)]

    # Convert rational functions to integer polynomials whose signs on (0, 1) match the expression!
    def pos_denom_poly(ex):
        ex_t = sp.together(ex)
        num_p = sp.Poly(sp.numer(ex_t), x_sp, domain="ZZ")
        den_p = sp.Poly(sp.denom(ex_t), x_sp, domain="ZZ")
        if den_p.eval(sp.Rational(1, 2)) < 0:
            num_p = -num_p
            den_p = -den_p
        # Strip factors of x and (1 - x) (both > 0 on (0, 1)) so endpoints 0 and 1 are non-roots!
        if num_p != 0:
            while num_p.eval(0) == 0:
                num_p, rem = sp.div(num_p, sp.Poly(x_sp, x_sp, domain="ZZ"))
                assert rem == 0
            while num_p.eval(1) == 0:
                num_p, rem = sp.div(num_p, sp.Poly(1 - x_sp, x_sp, domain="ZZ"))
                assert rem == 0
        return num_p

    p_Pbp1 = pos_denom_poly(P_bp1)
    p_P3 = pos_denom_poly(P3_ex)
    p_P1 = pos_denom_poly(P1_ex)
    p_LU = pos_denom_poly(LU_ex)
    p_LT = pos_denom_poly(LT_ex)
    p_prefs = [(pos_denom_poly(pk), pos_denom_poly(ld)) for _, pk, ld in prefs]

    def always_pos(poly, lo_q, hi_q):
        return poly.eval(lo_q) > 0 and poly.eval(hi_q) > 0 and sp.count_roots(poly, lo_q, hi_q) == 0

    def always_nonpos(poly, lo_q, hi_q):
        return poly.eval(lo_q) <= 0 and poly.eval(hi_q) <= 0 and sp.count_roots(poly, lo_q, hi_q) == 0

    stk = [(sp.Rational(0), sp.Rational(1), 0)]
    leaves = 0
    overlaps = 0
    q1_ov, q2_ov = sp.Rational(231, 256), sp.Rational(467, 512)
    while stk:
        lo_q, hi_q, dep = stk.pop()
        if (a, b) == (1, 4) and lo_q >= q1_ov and hi_q <= q2_ov:
            overlaps += 1
            leaves += 1
            continue
        ok_pos = always_pos(p_P3, lo_q, hi_q) or always_pos(p_P1, lo_q, hi_q)
        ok_neg = always_pos(p_LU, lo_q, hi_q) or always_pos(p_LT, lo_q, hi_q)
        if not ok_neg:
            for pk_p, ld_p in p_prefs:
                if always_pos(pk_p, lo_q, hi_q) and always_pos(ld_p, lo_q, hi_q):
                    ok_neg = True
                    break
        if (ok_pos and ok_neg) or (ok_pos and always_pos(p_Pbp1, lo_q, hi_q)) or (ok_neg and always_nonpos(p_Pbp1, lo_q, hi_q)):
            leaves += 1
            continue
        assert dep < 16, f"n=7 triple {(a,b)} failed at [{lo_q}, {hi_q}]"
        mid_q = (lo_q + hi_q) / 2
        stk.append((mid_q, hi_q, dep + 1))
        stk.append((lo_q, mid_q, dep + 1))
    return leaves, overlaps

n7_leaves_total = 0
for (a_v, b_v, exp_ov_nonempty) in [(1, 3, False), (1, 4, True), (1, 5, False), (2, 4, False), (2, 5, False)]:
    lv, ov = cert_n7_triple(a_v, b_v)
    assert (ov > 0) == exp_ov_nonempty
    n7_leaves_total += lv


# Exact Sturm check of flip({1, 3, 4}) on (7, 1, 4) over [231/256, 467/512]
q1_st, q2_st = sp.Rational(231, 256), sp.Rational(467, 512)
SA14 = A7[1]
P4_14 = sp.together(A7[1] - A7[2] - A7[3])
P5_14 = sp.together(A7[1] - A7[2] - A7[3] - A7[4])
Lsw_14 = sp.together((sum(A7[2] * B7[m] - A7[m] * B7[5] for m in range(3, 5)) - (B7[2] - B7[5]) * SA14) / (A7[2] - A7[5]))
Usw_14 = sp.together(-B7[5] + sum(A7[1] * B7[m] - A7[m] * B7[4] for m in range(2, 4)) / (A7[1] - A7[4]))
delta3_14 = B7[4] - B7[5]
# Confirm q1_st < root(P4) and root(L_sw-U_sw) < q2_st via Sturm count_roots & signs:
assert P4_14.subs(x_sp, q1_st) > 0 and P4_14.subs(x_sp, q2_st) < 0 and sp.count_roots(sp.Poly(sp.numer(P4_14), x_sp), q1_st, q2_st) == 1
assert (Lsw_14 - Usw_14).subs(x_sp, q1_st) < 0 and (Lsw_14 - Usw_14).subs(x_sp, q2_st) > 0 and sp.count_roots(sp.Poly(sp.numer(sp.together(Lsw_14 - Usw_14)), x_sp), q1_st, q2_st) == 1
assert P5_14.subs(x_sp, q1_st) < 0 and P5_14.subs(x_sp, q2_st) < 0 and sp.count_roots(sp.Poly(sp.numer(P5_14), x_sp), q1_st, q2_st) == 0

sig14 = [0, 1, -1, -1, -1, 1, 0, 0]
F14 = {1, 3, 4}
cp14 = sum(A7[i] * B7[j] * sig14[i] * sig14[j] for i in range(1, 6) for j in range(i + 1, 6) if (i in F14) != (j in F14))
qc14 = sum(A7[i] * sig14[i] for i in range(1, 6) if (i in F14) != (6 in F14))
for Q_ex in [Lsw_14, Usw_14, delta3_14]:
    dw = sp.together(cp14 + qc14 * Q_ex)
    assert sp.count_roots(sp.Poly(sp.numer(dw), x_sp), q1_st, q2_st) == 0
    assert dw.subs(x_sp, q1_st) > 0 and dw.subs(x_sp, q2_st) > 0
print(f"[PASS 3] Exact n=7 Sturm certificates (all 5 triples + flip{{1,3,4}}) ({time.time() - t3_s:.2f}s)")


# =============================================================================
# 4. THEOREM A2 EXACT RATIONAL INTERVAL CERTIFICATES (Lambda1 in [1/5, 8])
# =============================================================================
t4_s = time.time()

def I0_J_m_iv(L1_iv, s_iv, m, u_min=Fraction(0), u_max=Fraction(1)):
    """Exact rational Iv for I0_m and J_m on [u_min, u_max] (f_m inscribed polyline)."""
    h_full = Fraction(1, m)
    i0 = Iv(0, 0)
    i1 = Iv(0, 0)
    for j in range(1, m + 1):
        u0 = Fraction(j - 1, m)
        u1 = Fraction(j, m)
        lo = max(u0, u_min)
        hi = min(u1, u_max)
        if hi <= lo:
            continue
        h = hi - lo
        f0_iv = Iv(u0) + s_iv * Iv(u0 * (1 - u0))
        bj_iv = Iv(1) + s_iv * Iv(1 - Fraction(2 * j - 1, m))
        f_lo_iv = f0_iv + bj_iv * Iv(lo - u0)
        z_iv = L1_iv * bj_iv * Iv(h)
        p1 = phi1_iv(z_iv)
        p2 = phi2_iv(z_iv)
        ef = exp_neg_iv(L1_iv * f_lo_iv)
        i0 = i0 + ef * Iv(h) * p1
        i1 = i1 + ef * (Iv(lo * h) * p1 + Iv(h * h) * p2)
    return i0, Iv(2) * s_iv * L1_iv * i1


def tan_int_m_iv(L1_iv, s_iv, m, u_min_iv, u_max_iv):
    """Exact rational Iv for int_{u_min}^{u_max} exp(-L1*f_tan_m) du and u*exp(-L1*f_tan_m) du."""
    h_full = Fraction(1, m)
    i0 = Iv(0, 0)
    i1 = Iv(0, 0)
    # Use conservative outer bounds of [u_min_iv, u_max_iv] inside each piece:
    # Since integrand >= 0, we need LOWER bound on integral:
    # shrink integration domain to [u_min_iv.hi, u_max_iv.lo] inside each piece!
    u_lo_in = u_min_iv.hi
    u_hi_in = u_max_iv.lo
    if u_hi_in <= u_lo_in:
        return Iv(0, 0), Iv(0, 0)
    for j in range(1, m + 1):
        u0 = Fraction(j - 1, m)
        u1 = Fraction(j, m)
        lo = max(u0, u_lo_in)
        hi = min(u1, u_hi_in)
        if hi <= lo:
            continue
        h = hi - lo
        cm = Fraction(2 * j - 1, 2 * m)
        f_cm_iv = Iv(cm) + s_iv * Iv(cm * (1 - cm))
        slope_iv = Iv(1) + s_iv * Iv(1 - 2 * cm)
        f_lo_iv = f_cm_iv + slope_iv * Iv(lo - cm)
        z_iv = L1_iv * slope_iv * Iv(h)
        p1 = phi1_iv(z_iv)
        p2 = phi2_iv(z_iv)
        ef = exp_neg_iv(L1_iv * f_lo_iv)
        i0 = i0 + ef * Iv(h) * p1
        i1 = i1 + ef * (Iv(lo * h) * p1 + Iv(h * h) * p2)
    return i0, i1


def _i0_i1_pt(l1, s, m=4, u_min=Fraction(0), u_max=Fraction(1)):
    """Fast point evaluation returning ((i0_lo, i0_hi), (i1_lo, i1_hi)) for exact (l1, s)."""
    i0_lo = Fraction(0)
    i0_hi = Fraction(0)
    i1_lo = Fraction(0)
    i1_hi = Fraction(0)
    for j in range(1, m + 1):
        u0 = Fraction(j - 1, m)
        u1 = Fraction(j, m)
        lo = max(u0, u_min)
        hi = min(u1, u_max)
        if hi <= lo:
            continue
        h = hi - lo
        f0 = u0 + s * u0 * (1 - u0)
        bj = 1 + s * (1 - Fraction(2 * j - 1, m))
        f_lo = f0 + bj * (lo - u0)
        z = l1 * bj * h
        p1_lo, p1_hi = _phi1_pt_bounds(z)
        p2_lo, p2_hi = _phi2_pt_bounds(z)
        ef_lo, ef_hi = _exp_neg_pt_bounds(l1 * f_lo)
        i0_lo += _round_dn(ef_lo * h * p1_lo)
        i0_hi += _round_up(ef_hi * h * p1_hi)
        i1_lo += _round_dn(ef_lo * (lo * h * p1_lo + h * h * p2_lo))
        i1_hi += _round_up(ef_hi * (lo * h * p1_hi + h * h * p2_hi))
    return (i0_lo, i0_hi), (i1_lo, i1_hi)


def _tan_pt(l1, s, m, u_lo_in, u_hi_in):
    """Fast point evaluation of tangent lower-bound integral ((i0_lo, i0_hi), (i1_lo, i1_hi))."""
    if u_hi_in <= u_lo_in:
        return (Fraction(0), Fraction(0)), (Fraction(0), Fraction(0))
    i0_lo = Fraction(0)
    i0_hi = Fraction(0)
    i1_lo = Fraction(0)
    i1_hi = Fraction(0)
    for j in range(1, m + 1):
        u0 = Fraction(j - 1, m)
        u1 = Fraction(j, m)
        lo = max(u0, u_lo_in)
        hi = min(u1, u_hi_in)
        if hi <= lo:
            continue
        h = hi - lo
        cm = Fraction(2 * j - 1, 2 * m)
        f_cm = cm + s * cm * (1 - cm)
        slope = 1 + s * (1 - 2 * cm)
        f_lo = f_cm + slope * (lo - cm)
        z = l1 * slope * h
        p1_lo, p1_hi = _phi1_pt_bounds(z)
        p2_lo, p2_hi = _phi2_pt_bounds(z)
        ef_lo, ef_hi = _exp_neg_pt_bounds(l1 * f_lo)
        i0_lo += _round_dn(ef_lo * h * p1_lo)
        i0_hi += _round_up(ef_hi * h * p1_hi)
        i1_lo += _round_dn(ef_lo * (lo * h * p1_lo + h * h * p2_lo))
        i1_hi += _round_up(ef_hi * (lo * h * p1_hi + h * h * p2_hi))
    return (i0_lo, i0_hi), (i1_lo, i1_hi)


# 4a. L >= 12: Phi_12(Lambda1, s, y) > 0 on Lambda1 in [1/5, 8], s in [0, 1], y in [0, min(ln(61/50), s*Lambda1/6)]
ln_122_ub = ln_61_50.hi
a2_boxes = 0
stack_a2 = [(Fraction(1, 5), Fraction(8), Fraction(0), Fraction(1), 0)]
while stack_a2:
    l1_a, l1_b, s_a, s_b, dep = stack_a2.pop()
    ym_hi = min(ln_122_ub, s_b * l1_b / 6)
    v_lo, v_hi = _exp_neg_pt_bounds(ym_hi)
    th_a_lo, th_a_hi = _exp_neg_pt_bounds(l1_a)
    th_b_lo, th_b_hi = _exp_neg_pt_bounds(l1_b)
    # W0_r1(l1_a, ym_hi) = 4*v - 3 - th*v*(2*v - 1)
    W0_r1_lo = 4 * v_lo - 3 - th_a_hi * v_hi * (2 * v_hi - 1)

    phi1_y_lo, _ = _phi1_pt_bounds(ym_hi)
    _, phi1_b_hi = _phi1_pt_bounds(l1_b)
    alpha_coef_lo = th_b_lo / phi1_b_hi

    (_, I0_4_ub), (_, I1_4_ub) = _i0_i1_pt(l1_a, s_a, 4)
    J4_ub = 2 * s_b * l1_b * I1_4_ub
    term_H_lo = 2 * s_a * alpha_coef_lo * phi1_y_lo * max(Fraction(0), phi1_y_lo - I0_4_ub)

    exp_12_lo, _ = _exp_neg_pt_bounds(l1_b / 12)
    omv_ub = 1 - v_lo
    term_b_ub = (th_a_hi / (1 - th_a_hi)) * omv_ub * (3 - v_lo - exp_12_lo - th_b_lo) / 2

    phi_lo = W0_r1_lo + term_H_lo - term_b_ub - J4_ub
    if phi_lo > 0 and phi1_y_lo > I0_4_ub:
        a2_boxes += 1
    else:
        assert dep < 20, f"A2 L>=12 exceeded depth at L1=[{l1_a},{l1_b}], s=[{s_a},{s_b}], phi_lo={phi_lo}"
        dl = (l1_b - l1_a) / 8
        ds = s_b - s_a
        if dl >= ds:
            m = (l1_a + l1_b) / 2
            stack_a2.append((m, l1_b, s_a, s_b, dep + 1))
            stack_a2.append((l1_a, m, s_a, s_b, dep + 1))
        else:
            m = (s_a + s_b) / 2
            stack_a2.append((l1_a, l1_b, m, s_b, dep + 1))
            stack_a2.append((l1_a, l1_b, s_a, m, dep + 1))

# 4b. L in {3..11}: exact bivariate polynomial Q_L(w, z) = x * N_L(w, z) > 0 via centered-form 2D box subdivision
def _build_biv_N_poly(L_v):
    """Build exact integer bivariate polynomial Q_L(w, z) = x * N_L(w, z) as dict {(iw, iz): int}."""
    even_L = (L_v % 2 == 0)
    w_sym, z_sym = sp.symbols("w z")
    x_s = w_sym ** 2 if even_L else w_sym
    v_s = x_s ** L_v
    th_s = z_sym ** L_v
    geom_s = sum(x_s ** j for j in range(1, L_v + 1))
    S_s = 0
    S_err_s = 0
    for k in range(1, L_v):
        xc_s = (z_sym ** k) * (w_sym ** (k * (L_v - k)) if even_L else x_s ** (k * (L_v - k) // 2))
        S_s += xc_s
        if k >= 2:
            S_err_s += xc_s * (1 - x_s ** (k - 1))
    H_s = geom_s - 1 - S_s
    # x * W0 = (1 - x*th) - (1 - v)*(2*(x + 1) - th*(x + x*v + v))
    xW0_s = (1 - x_s * th_s) - (1 - v_s) * (2 * (x_s + 1) - th_s * (x_s + x_s * v_s + v_s))
    Q_s = sp.expand(x_s * th_s * (1 - v_s) * H_s + (1 - th_s) * (xW0_s - x_s * S_err_s))
    poly = sp.Poly(Q_s, w_sym, z_sym, domain="ZZ")
    terms = [(iw, iz, int(c)) for (iw, iz), c in poly.terms()]
    dw_terms = [(iw - 1, iz, iw * c) for iw, iz, c in terms if iw > 0]
    dz_terms = [(iw, iz - 1, iz * c) for iw, iz, c in terms if iz > 0]
    return terms, dw_terms, dz_terms

def _eval_biv_pt_lo(terms, w_q, z_q):
    """Exact rational lower bound on P(w_q, z_q) with outward rounding (prevents denominator blowup)."""
    max_w = max((iw for iw, _, _ in terms), default=0)
    max_z = max((iz for _, iz, _ in terms), default=0)
    w_dn, w_up = [Fraction(1)] * (max_w + 1), [Fraction(1)] * (max_w + 1)
    for i in range(1, max_w + 1):
        w_dn[i] = _round_dn(w_dn[i - 1] * w_q, 32)
        w_up[i] = _round_up(w_up[i - 1] * w_q, 32)
    z_dn, z_up = [Fraction(1)] * (max_z + 1), [Fraction(1)] * (max_z + 1)
    for j in range(1, max_z + 1):
        z_dn[j] = _round_dn(z_dn[j - 1] * z_q, 32)
        z_up[j] = _round_up(z_up[j - 1] * z_q, 32)
    acc = Fraction(0)
    for iw, iz, c in terms:
        if c > 0:
            acc += _round_dn(c * w_dn[iw] * z_dn[iz], 32)
        else:
            acc -= _round_up((-c) * w_up[iw] * z_up[iz], 32)
    return acc

def _max_abs_biv(terms, wa, wb, za, zb):
    """Exact rational upper bound on max |P(w, z)| on [wa, wb] x [za, zb] subset [0, 1]^2."""
    max_w = max((iw for iw, _, _ in terms), default=0)
    max_z = max((iz for _, iz, _ in terms), default=0)
    wpa, wpb = [Fraction(1)] * (max_w + 1), [Fraction(1)] * (max_w + 1)
    for i in range(1, max_w + 1):
        wpa[i] = _round_dn(wpa[i - 1] * wa, 24)
        wpb[i] = _round_up(wpb[i - 1] * wb, 24)
    zpa, zpb = [Fraction(1)] * (max_z + 1), [Fraction(1)] * (max_z + 1)
    for j in range(1, max_z + 1):
        zpa[j] = _round_dn(zpa[j - 1] * za, 24)
        zpb[j] = _round_up(zpb[j - 1] * zb, 24)
    pos_lo = Fraction(0)
    pos_hi = Fraction(0)
    neg_lo = Fraction(0)
    neg_hi = Fraction(0)
    for iw, iz, c in terms:
        if c > 0:
            pos_lo += _round_dn(c * wpa[iw] * zpa[iz], 24)
            pos_hi += _round_up(c * wpb[iw] * zpb[iz], 24)
        else:
            mc = -c
            neg_lo += _round_dn(mc * wpa[iw] * zpa[iz], 24)
            neg_hi += _round_up(mc * wpb[iw] * zpb[iz], 24)
    lo_val = pos_lo - neg_hi
    hi_val = pos_hi - neg_lo
    return max(abs(lo_val), abs(hi_val))

a2_small_boxes = 0
for L_v in range(3, 12):
    d0 = max(1, 5 - L_v)
    even_L = (L_v % 2 == 0)
    terms_Q, terms_Qw, terms_Qz = _build_biv_N_poly(L_v)
    w_lo_q = _round_dn(pow_rat_bounds(Fraction(50, 61), 1, (2 * L_v) if even_L else L_v, steps=24)[0], 18)
    z_exp_8_lo = _round_dn(_exp_neg_pt_bounds(Fraction(8, L_v), N_pairs=8)[0], 18)
    z_exp_02_hi = _round_up(_exp_neg_pt_bounds(Fraction(1, 5 * L_v), N_pairs=8)[1], 18)
    exp_d0 = (2 * d0 + L_v - 1) if even_L else (d0 + (L_v - 1) // 2)
    stk = [(w_lo_q, Fraction(1), z_exp_8_lo, z_exp_02_hi, 0)]
    while stk:
        wa, wb, za, zb, dep = stk.pop()
        wb_pow = _pow_ru(wb, exp_d0)
        if za > wb_pow:
            a2_small_boxes += 1
            continue
        zb_eff = min(zb, wb_pow)
        if zb_eff < za:
            a2_small_boxes += 1
            continue
        wm = (wa + wb) / 2
        zm = (za + zb_eff) / 2
        hw = (wb - wa) / 2
        hz = (zb_eff - za) / 2
        q_mid = _eval_biv_pt_lo(terms_Q, wm, zm)
        mw = _max_abs_biv(terms_Qw, wa, wb, za, zb_eff)
        mz = _max_abs_biv(terms_Qz, wa, wb, za, zb_eff)
        if q_mid - hw * mw - hz * mz > 0:
            a2_small_boxes += 1
        else:
            assert dep < 18, f"A2 L={L_v} exceeded depth at w=[{wa},{wb}], z=[{za},{zb_eff}]"
            if (wb - wa) >= (zb_eff - za):
                stk.append((wm, wb, za, zb_eff, dep + 1))
                stk.append((wa, wm, za, zb_eff, dep + 1))
            else:
                stk.append((wa, wb, zm, zb_eff, dep + 1))
                stk.append((wa, wb, za, zm, dep + 1))

print(f"[PASS 4] Theorem A2 certified: {a2_boxes} 2D boxes (L>=12, analytic y-monotonicity) + {a2_small_boxes} 2D boxes (L in 3..11) ({time.time() - t4_s:.2f}s)")


# =============================================================================
# 5. THEOREM B1 EXACT RATIONAL CERTIFICATES (a >= 2, r^L >= 1.22, M >= 5)
# =============================================================================
t5_s = time.time()

def F_M_ub(u_q, M, K=None):
    """Strict rational upper bound on F_M(u_q) = 1 + sum_{k=1}^{M-2} u_q^{k - k(k+1)/(2M)}.
    When K is given, returns a UNIFORM upper bound valid for ALL M' >= M by summing k=1..K at M
    and ALWAYS adding the tail u_q^{(K+1)/2} / (1 - sqrt(u_q))."""
    res = Fraction(1)
    k_lim = (M - 2) if K is None else K
    for k in range(1, k_lim + 1):
        p_exp = 2 * k * M - k * (k + 1)
        assert p_exp > 0
        _, term_ub = pow_rat_bounds(u_q, p_exp, 2 * M, steps=28)
        res += term_ub
    if K is not None:
        _, sqrt_u_ub = _sqrt_pt_bounds(u_q)
        _, u_tail_ub = pow_rat_bounds(u_q, K + 1, 2, steps=28)
        res += u_tail_ub / (Fraction(1) - sqrt_u_ub)
    return res

# Step 1 (u > 33/50): M >= 17 (K=13) + 5 <= M <= 16
u0_b1 = Fraction(33, 50)
target_b1 = Fraction(1) / u0_b1 + Fraction(1) / (u0_b1 * u0_b1)
# For M >= 17, F_M(u0) <= 1 + sum_{k=1}^{13} u0^{k - k(k+1)/34} + u0^7/(1 - sqrt(u0))
assert F_M_ub(u0_b1, 17, K=13) < target_b1
for M_v in range(5, 17):
    assert F_M_ub(u0_b1, M_v) < target_b1

# Step 2 (u in (33/50, 37/50], ALL a >= 2):
u1_b1 = Fraction(37, 50)
# (i) F_M(37/50) < 5 < 2 + 50/37 + (50/37)^2 for ALL M >= 5 => Delta_P < 2
# Use M_1 = 30, K_1 = 22 uniformly for M >= 30, and exact F_M for 5 <= M <= 29:
assert F_M_ub(u1_b1, 30, K=22) < 5 < 2 + Fraction(50, 37) + Fraction(50, 37) ** 2
for M_v in range(5, 30):
    assert F_M_ub(u1_b1, M_v) < 5
# (ii) r* >= 4 for all M >= 5 (since S_3(37/50, M) <= S_3(37/50, 5) < 50/37 + (50/37)^2)
S3_5 = Fraction(1)
for p_e in [4, 7, 9]:
    _, ub_t = pow_rat_bounds(u1_b1, p_e, 5, steps=28)
    S3_5 += ub_t
assert S3_5 < Fraction(50, 37) + Fraction(50, 37) ** 2
# r* >= 5 for all M >= 17 (S_4(37/50, 17) < 50/37 + (50/37)^2)
S4_17 = Fraction(1)
for k in range(1, 5):
    _, ub_t = pow_rat_bounds(u1_b1, 2 * k * 17 - k * (k + 1), 34, steps=28)
    S4_17 += ub_t
assert S4_17 < Fraction(50, 37) + Fraction(50, 37) ** 2

# (iii) E_{a>=2}(S_{r*}) > 0 for r*=5 and r*>=6 on all M >= 30 (1D Iv subdivision on u in [33/50, 37/50])
b1_step2_boxes = 0
x30_lb, _ = pow_rat_bounds(u0_b1, 1, 30, steps=28)
r30_ub = Fraction(1) / x30_lb

def S_term_ub(u_hi, k, M_min=30):
    return pow_rat_bounds(u_hi, 2 * k * M_min - k * (k + 1), 2 * M_min, steps=28)[1]

stk_b1_30 = [(u0_b1, u1_b1, 0)]
while stk_b1_30:
    ua, ub, dep = stk_b1_30.pop()
    G5_lb = sum(x30_lb ** j for j in range(1, 5))
    S5_ub = Fraction(1) + sum(S_term_ub(ub, k, 30) for k in range(1, 6))
    _, sq_ub = _sqrt_pt_bounds(ub)
    _, tail_ub = pow_rat_bounds(ub, 23, 2, steps=28)
    DP5_ub = sum(S_term_ub(ub, k, 30) for k in range(6, 23)) + tail_ub / (Fraction(1) - sq_ub)
    E5_lo = 2 * (1 + ua + G5_lb - r30_ub * S5_ub) - DP5_ub * (1 + ub)
    G6_lb = sum(x30_lb ** j for j in range(1, 6))
    F30_ub = F_M_ub(ub, 30, K=22)
    E6_lo = 2 * (1 + ua + G6_lb - r30_ub * F30_ub)
    if E5_lo > 0 and E6_lo > 0:
        b1_step2_boxes += 1
    else:
        assert dep < 12, f"B1 M>=30 failed at [{ua},{ub}]"
        um = (ua + ub) / 2
        stk_b1_30.append((um, ub, dep + 1))
        stk_b1_30.append((ua, um, dep + 1))

# Certify E_{a>=2}(S_{r*}) > 0 on u in [33/50, 37/50] for 6 <= M <= 29 and all feasible r* >= 4 (M=5 impossible!)
assert F_M_ub(u1_b1, 5) < Fraction(50, 37) + Fraction(50, 37) ** 2
for M_v in range(6, 30):
    a_pk = dyadic_bracket(pow_rat_bounds(u0_b1, 1, M_v, steps=24)[0], round_up=False, k=10)
    b_pk = dyadic_bracket(pow_rat_bounds(u1_b1, 1, M_v, steps=24)[1], round_up=True, k=10)
    r_list = [4, 5] if M_v <= 16 else [5]
    for r_st in r_list:
        if r_st > M_v - 2:
            continue
        poly_d = defaultdict(int)
        poly_d[1] += 2
        poly_d[M_v + 1] += 2
        for j in range(1, r_st):
            poly_d[j + 1] += 2
        for k in range(0, r_st + 1):
            ck = k * M_v - k * (k + 1) // 2
            poly_d[ck] -= 2
        for k in range(r_st + 1, M_v - 1):
            ck = k * M_v - k * (k + 1) // 2
            poly_d[ck + M_v + 1] -= 1
            poly_d[ck + r_st] -= 1
        max_e = max(poly_d)
        p_c = [poly_d[i] for i in range(max_e + 1)]
        # Feasibility of r_st: x^{2M} * S_{r_st}(x) >= x^M + 1 (since S_{r_st} >= u^{-1} + u^{-2}),
        # and u = x^M <= 37/50 (prune if p_lo^M > 37/50 * 2^{kM} or p_hi^M < 33/50 * 2^{kM}):
        s_poly_d = defaultdict(int)
        for k in range(0, r_st + 1):
            ck = k * M_v - k * (k + 1) // 2
            s_poly_d[2 * M_v + ck] += 1
        s_poly_d[M_v] -= 1
        s_poly_d[0] -= 1
        s_max = max(s_poly_d)
        s_pos, s_neg = split_poly_int([s_poly_d[i] for i in range(s_max + 1)])
        def feas_b1_s2(p_lo, p_hi, k, M=M_v, sp_=s_pos, sn_=s_neg):
            if 50 * (p_lo ** M) > 37 * (1 << (k * M)):
                return False
            if 50 * (p_hi ** M) < 33 * (1 << (k * M)):
                return False
            # If max(S_{r*}*x^{2M} - x^M - 1) < 0 on [p_lo, p_hi], i.e. s_pos(p_hi) < s_neg(p_lo), prune!
            if eval_dyadic_int(sp_, p_hi, k) < eval_dyadic_int(sn_, p_lo, k):
                return False
            return True
        b1_step2_boxes += certify_disjunction_dyadic([p_c], a_pk, b_pk, feas_fn=feas_b1_s2, max_depth=24)
    if M_v >= 8:
        poly_d6 = defaultdict(int)
        poly_d6[1] += 2
        poly_d6[M_v + 1] += 2
        for j in range(1, 6):
            poly_d6[j + 1] += 2
        for k in range(0, M_v - 1):
            ck = k * M_v - k * (k + 1) // 2
            poly_d6[ck] -= 2
        max_e6 = max(poly_d6)
        p_c6 = [poly_d6[i] for i in range(max_e6 + 1)]
        b1_step2_boxes += certify_disjunction_dyadic([p_c6], a_pk, b_pk, max_depth=24)

# Step 3 (u >= 37/50):
# (a) L >= 12 2D box bound: (12/ln(1/v) - 1/2)*(1 - 2v + u) > 1/(1 - u/sqrt(v)) on 37/50 <= u <= v <= 50/61
b1_step3_boxes = 0
stk_b1_2d = [(u1_b1, Fraction(50, 61), u1_b1, Fraction(50, 61), 0)]
while stk_b1_2d:
    va, vb, ua, ub, dep = stk_b1_2d.pop()
    if ua > vb:
        b1_step3_boxes += 1
        continue
    ub_eff = min(ub, vb)
    v_iv = Iv(va, vb)
    u_iv = Iv(ua, ub_eff)
    lnv_iv = ln_inv_iv(v_iv)
    lhs_iv = (Iv(12) / lnv_iv - Iv(Fraction(1, 2))) * (Iv(1) - Iv(2) * v_iv + u_iv)
    rhs_iv = Iv(1) / (Iv(1) - u_iv / sqrt_iv(v_iv))
    if (lhs_iv - rhs_iv).lo > 0:
        b1_step3_boxes += 1
    else:
        assert dep < 16
        if (vb - va) >= (ub_eff - ua):
            vm = (va + vb) / 2
            stk_b1_2d.append((vm, vb, ua, ub_eff, dep + 1))
            stk_b1_2d.append((va, vm, ua, ub_eff, dep + 1))
        else:
            um = (ua + ub_eff) / 2
            stk_b1_2d.append((va, vb, um, ub_eff, dep + 1))
            stk_b1_2d.append((va, vb, ua, um, dep + 1))

# (b) Prove L=3 (M >= 5) and (L=4, d >= 2) impossible for a >= 2, r^L >= 1.22, P_{b+1} <= 0:
# For L=3, M>=5: at x^3 <= 50/61, u = x^M <= (50/61)^{5/3} < 3/4 (since (50/61)^5 < (3/4)^3), hence u^{-1}+u^{-2} > 4/3 + 16/9 = 28/9 > 3 > 1+S(x)!
assert (Fraction(50, 61) ** 5) < (Fraction(3, 4) ** 3)
assert Fraction(4, 3) + Fraction(16, 9) > 3
# For L=4, d>=2 (M >= 6): at x^4 = 50/61, 1 + x^5 + x^9 + x^12 < (61/50)^{3/2} + (61/50)^3
x4_hi = pow_rat_bounds(Fraction(50, 61), 1, 4, 28)[1]
u4_hi = pow_rat_bounds(Fraction(50, 61), 6, 4, 28)[1]
u4_lb = pow_rat_bounds(Fraction(50, 61), 6, 4, 28)[0]
assert 1 + x4_hi ** 5 + x4_hi ** 9 + x4_hi ** 12 < Fraction(1) / u4_hi + Fraction(1) / (u4_hi ** 2)

# (c) Certify all 27 (L, d) pairs (4 <= L <= 11, d < (ln(50/37)/ln(61/50) - 1)*L) via exact integer dyadic monotone-splitting
def build_B1_L0_m_T_poly(L, d):
    M = L + d
    e_th = L * d + L * (L - 1) // 2
    c = [0] * (M + e_th + M + 2)
    for j in range(1, L + 1):
        c[M + j] += 1
    for j in range(L + 1, M + 1):
        c[M + j] -= 1
        c[e_th + M + j] += 1
    c[M] -= 1
    for k in range(1, L):
        c[M + k * M - k * (k + 1) // 2] -= 1
    return c

slope_d_b1 = (ln_inv_iv(Iv(u1_b1)) / ln_61_50).hi - 1
b1_pairs_27 = [(L, d) for L in range(4, 12) for d in range(1, int(slope_d_b1 * L) + 1)
               if L + d >= 5 and not (L == 4 and d >= 2)]
assert len(b1_pairs_27) == 27
b1_leaves_27 = 0
v_50_61_q = Fraction(50, 61)
for L_v, d_v in b1_pairs_27:
    M_v = L_v + d_v
    a_pk = dyadic_bracket(pow_rat_bounds(u1_b1, 1, M_v, 20)[0], round_up=False, k=8)
    b_pk = dyadic_bracket(pow_rat_bounds(v_50_61_q, 1, L_v, 20)[1], round_up=True, k=8)
    def feas_b1(p_lo, p_hi, k, L=L_v, M=M_v):
        # p_lo/2^k > (50/61)^{1/L} => 61 * p_lo^L > 50 * 2^{kL} => prune
        if 61 * (p_lo ** L) > 50 * (1 << (k * L)):
            return False
        # p_hi/2^k < (37/50)^{1/M} => 50 * p_hi^M < 37 * 2^{kM} => prune
        if 50 * (p_hi ** M) < 37 * (1 << (k * M)):
            return False
        return True
    b1_leaves_27 += certify_disjunction_dyadic([build_B1_L0_m_T_poly(L_v, d_v)], a_pk, b_pk, feas_fn=feas_b1)

print(f"[PASS 5] Theorem B1 certified: {b1_step2_boxes} Step-2 boxes + {b1_step3_boxes} 2D boxes (L>=12) + {b1_leaves_27} dyadic leaves (27 pairs) ({time.time() - t5_s:.2f}s)")


# =============================================================================
# 6. THEOREM B2 EXACT RATIONAL CERTIFICATES (a = 1, r* = 1, r^L >= 1.22, M >= 6)
# =============================================================================
t6_s = time.time()

# 6a. u > 603/1000 (u^{-1} <= 1 + u^{5/6}) and L=2 impossible
u_b2 = Fraction(603, 1000)
_, u_b2_5_6_ub = pow_rat_bounds(u_b2, 5, 6, 28)
assert Fraction(1) / u_b2 > 1 + u_b2_5_6_ub
# L=2, M>=6, r^2 >= 1.22 => x^2 <= 50/61 => u <= (50/61)^3 < 603/1000
assert Fraction(50, 61) ** 3 < u_b2

# 6b. B2(a) (r^L in [1.22, 1.33]):
# Verify exact rational lower bounds s > 1/5 and Lambda1 > 1 for L >= 11, r^L in [1.22, 1.33], u > 603/1000:
slope_b2 = (ln_inv_iv(Iv(u_b2)) / ln_61_50).hi - 1
assert Fraction(1) / (1 + 2 * slope_b2) > Fraction(1, 5)
assert 6 * ln_61_50.lo > Fraction(1)  # D1 = d + (L-1)/2 >= 1 + 5 = 6 => Lambda1 >= 6*ln(61/50) > 1
# For L >= 11, Lambda1 in [1, 17]: 3D box subdivision on s in [1/5, 1], y in [ln(61/50), ln(133/100)], L1 in [1, 17]
ln_133_100 = ln_inv_iv(Iv(Fraction(100, 133)))
ln_u_b2_ub = ln_inv_iv(Iv(u_b2)).hi
b2a_3d_boxes = 0
stk_b2a = [(Fraction(1), Fraction(17), Fraction(1, 5), Fraction(1), ln_61_50.lo, ln_133_100.hi, 0)]
while stk_b2a:
    l1_a, l1_b, s_a, s_b, y_a, y_b, dep = stk_b2a.pop()
    # Prune infeasible boxes where L = 2*s*Lambda1 / y < 11 everywhere on the box:
    if 2 * s_b * l1_b < 11 * y_a:
        b2a_3d_boxes += 1
        continue
    # Prune infeasible boxes where M*t = ((1+s)/(2s))*y + y^2/(4*s*Lambda1) >= ln(1/u_b2) everywhere (violating u > 603/1000):
    if ((1 + s_b) / (2 * s_b)) * y_a + (y_a * y_a) / (4 * s_b * l1_b) >= ln_u_b2_ub:
        b2a_3d_boxes += 1
        continue
    L_lo = max(Fraction(11), 2 * s_a * l1_a / y_b)
    v_lo, v_hi = _exp_neg_pt_bounds(y_b)
    v_a_lo, v_a_hi = _exp_neg_pt_bounds(y_a)
    th_a_lo, th_a_hi = _exp_neg_pt_bounds(l1_a)
    th_b_lo, th_b_hi = _exp_neg_pt_bounds(l1_b)
    phi1_y_lo, _ = _phi1_pt_bounds(y_b)
    _, phi1_y_hi = _phi1_pt_bounds(y_a)
    (_, I0_4_ub), _ = _i0_i1_pt(l1_a, s_a, 4)

    # Exact: M - 1 = D1*(1 + s) - 1/2 => (M - 1)*t = ((1 + s)/(2*s) - 1/(2*L))*y >= ((1 + s_b)/(2*s_b) - 1/(2*L_lo))*y_a!
    # Also x^{M-1} <= v always, so x^{M-1} <= exp(-max(y_a, ((1 + s_b)/(2*s_b) - 1/(2*L_lo))*y_a))!
    exp_xm1_lo = max(y_a, ((1 + s_b) / (2 * s_b) - Fraction(1) / (2 * L_lo)) * y_a)
    _, xm1_ub = _exp_neg_pt_bounds(exp_xm1_lo)
    # Exact coef_P = (1-v)*[(1 - th*v) - x^{M-1}*(1 - th)] >= (1 - v_a_hi) * [(1 - th_a_hi*v_a_hi) - xm1_ub*(1 - th_a_hi)]
    # Wait: (1 - th*v) - x^{M-1}*(1-th) = (1 - x^{M-1}) + th*(x^{M-1} - v) >= (1 - xm1_ub) + th_a_hi*(xm1_ub - v_a_hi) ?
    # Even cleaner: for x^{M-1} <= xm1_ub <= v, (1 - th*v) - x^{M-1}*(1-th) >= (1 - th*v) - xm1_ub*(1 - th) = 1 - xm1_ub - th*(v - xm1_ub)!
    # Since v >= xm1_ub (as exp_xm1_lo >= y_a and wait: v_a_hi >= xm1_ub!), 1 - xm1_ub - th_a_hi*max(0, v_a_hi - xm1_ub) is a STRICT lower bound on (1-th*v)-x^{M-1}*(1-th)!
    # Even simpler: coef_P = (1-v)*[(1 - x^{M-1}) - th*(v - x^{M-1})] >= (1 - v_a_hi) * (1 - xm1_ub - th_a_hi * max(Fraction(0), v_a_hi - xm1_ub))
    # AND since coef_P/(1-th) = (1-v)*[1 - x^{M-1} + th*(1-v)/(1-th)] is INCREASING in th (decreasing in L1)!
    # Wait: (1-v)*[1 - xm1_ub + (th_b_lo / (1 - th_b_lo))*(1 - v_a_hi)] is a STRICT lower bound on coef_P/(1-th)!
    coef_over_omth_lo = (1 - v_a_hi) * (1 - xm1_ub + (th_b_lo / (1 - th_b_lo)) * (1 - v_a_hi))
    u_star_lo = min(Fraction(1), coef_over_omth_lo / y_b)

    # Positive part >= L * (1-th) * y * int_{2/L}^{u_*} (u_* - u) exp(-L1*f_tan4) du
    lo_p_q = Fraction(2) / L_lo
    (i0_t_lo, _), (_, i1_t_hi) = _tan_pt(l1_b, s_b, 4, lo_p_q, u_star_lo)
    diff_tan_lo = u_star_lo * i0_t_lo - i1_t_hi
    pos_part_lo = L_lo * (1 - th_a_hi) * y_a * max(Fraction(0), diff_tan_lo)

    # Negative tail <= (1-th) * 2*s*L1 * int_{u_{*lo}}^1 (u - u_{*lo}) exp(-L1*f_4) du
    # Since integrand >= 0 is decreasing in (L1, s), integral is maximized at (l1_a, s_a)!
    (I0_neg_lb_a, _), (_, I1_neg_ub_a) = _i0_i1_pt(l1_a, s_a, 4, u_min=u_star_lo, u_max=Fraction(1))
    neg_part_ub = (1 - th_b_lo) * 2 * s_b * l1_b * max(Fraction(0), I1_neg_ub_a - u_star_lo * I0_neg_lb_a)

    # Exact L-free H term: th*(1-v)*H >= 2*s*L1*th*phi1(y)*(phi1(y) - I0_4) - th*(1-v)*(3 - v - exp(-L1/11) - th)/2
    exp_11_lo, _ = _exp_neg_pt_bounds(l1_b / 11)
    H_diff_lo = phi1_y_lo - I0_4_ub
    if H_diff_lo >= 0:
        H_main_lo = 2 * s_a * l1_a * th_b_lo * phi1_y_lo * H_diff_lo
    else:
        H_main_lo = 2 * s_b * l1_b * th_a_hi * phi1_y_hi * H_diff_lo
    H_err_ub = th_a_hi * (1 - v_lo) * (3 - v_lo - exp_11_lo - th_b_lo) / 2
    # Exact W0 = 4v - 3 - th*v*(2v-1) + (r-1)*(2v - 1 + th*v*(1-v)), and r-1 = e^t - 1 > t = y/L = y^2 / (2*s*Lambda1)!
    W0_r1_lo = 4 * v_lo - 3 - th_a_hi * v_hi * (2 * v_hi - 1) + (y_a * y_a / (2 * s_b * l1_b)) * (2 * v_lo - 1)
    # Handle sign of W0_r1_lo rigorously!
    omth_W0_lo = (1 - th_a_hi) * W0_r1_lo if W0_r1_lo >= 0 else (1 - th_b_lo) * W0_r1_lo
    total_lo = H_main_lo - H_err_ub + omth_W0_lo + pos_part_lo - neg_part_ub
    if total_lo > 0:
        b2a_3d_boxes += 1
    else:
        assert dep < 24, f"B2(a) L>=11 failed at L1=[{l1_a},{l1_b}], s=[{s_a},{s_b}], y=[{y_a},{y_b}], total_lo={total_lo}"
        dl = (l1_b - l1_a) / l1_a
        ds = (s_b - s_a) / s_a
        dy = (y_b - y_a) / y_a
        if dl >= ds and dl >= dy:
            m = (l1_a + l1_b) / 2
            stk_b2a.append((m, l1_b, s_a, s_b, y_a, y_b, dep + 1))
            stk_b2a.append((l1_a, m, s_a, s_b, y_a, y_b, dep + 1))
        elif ds >= dy:
            m = (s_a + s_b) / 2
            stk_b2a.append((l1_a, l1_b, m, s_b, y_a, y_b, dep + 1))
            stk_b2a.append((l1_a, l1_b, s_a, m, y_a, y_b, dep + 1))
        else:
            m = (y_a + y_b) / 2
            stk_b2a.append((l1_a, l1_b, s_a, s_b, m, y_b, dep + 1))
            stk_b2a.append((l1_a, l1_b, s_a, s_b, y_a, m, dep + 1))

# Certify all 45 pairs (3 <= L <= 8, M >= 6, d < 1.54*L) via exact integer dyadic monotone-splitting for L_sw - U_sw > 0
def build_B2_Lsw_m_Usw_poly(L, d):
    M = L + d
    e_th = L * d + L * (L - 1) // 2
    L_poly = defaultdict(int)
    for j in range(1, L + 1):
        L_poly[1 + j] += 1
    L_poly[1 + L] -= 1
    for k in range(1, L):
        L_poly[1 + L + k * M - k * (k + 1) // 2] -= 1
    L_poly[1 - M] -= 1
    L_poly[1 + L - M] += 1

    U_poly = defaultdict(int)
    for j in range(-1, L - 1):
        U_poly[1 + j] += 1
    U_poly[1 + L - 1] -= 1
    U_poly[1 + L] -= 1
    U_poly[1 + e_th + 2 * L - 1] += 1
    U_poly[1 + e_th + 2 * L] += 1
    U_poly[1 + M + L - 1] -= 1
    for k in range(1, L):
        U_poly[1 + M + L - 1 + k * M - k * (k + 1) // 2] -= 1
    U_poly[0] -= 1
    U_poly[L] += 1

    diff = defaultdict(int)
    for e, v in L_poly.items():
        diff[M + e] += v
        diff[M + e + e_th + L] -= v
    for e, v in U_poly.items():
        diff[M + e] -= v
        diff[M + e + e_th] += v
    max_e = max((e for e, v in diff.items() if v != 0), default=0)
    c = [0] * (max_e + 1)
    for e, v in diff.items():
        if v != 0:
            c[e] = v
    return c

# Certify all pairs (3 <= L <= 10, M >= 6, d <= floor(slope_b2*L)) via exact integer dyadic monotone-splitting
b2_small = [(L, d) for L in range(3, 11) for d in range(1, int(slope_b2 * L) + 1) if L + d >= 6]
b2a_leaves_small = 0
for L_v, d_v in b2_small:
    M_v = L_v + d_v
    a_pk = dyadic_bracket(pow_rat_bounds(u_b2, 1, M_v, 20)[0], round_up=False, k=8)
    b_pk = dyadic_bracket(pow_rat_bounds(Fraction(50, 61), 1, L_v, 20)[1], round_up=True, k=8)
    def feas_b2a(p_lo, p_hi, k, L=L_v, M=M_v):
        if 61 * (p_lo ** L) > 50 * (1 << (k * L)):
            return False
        if 133 * (p_hi ** L) < 100 * (1 << (k * L)):
            return False
        if (1 << (k * (2 * M - 1))) > (p_hi ** M) * (1 << (k * (M - 1))) + (p_hi ** (2 * M - 1)):
            return False
        return True
    b2a_leaves_small += certify_disjunction_dyadic([build_B2_Lsw_m_Usw_poly(L_v, d_v)], a_pk, b_pk, feas_fn=feas_b2a)

# 6c. B2(b) (r^L >= 1.33):
# L >= 9 2D box bound on 603/1000 <= u <= v <= 100/133 with u^{-1} <= 1 + v^{-1/9}*u
b2b_2d_boxes = 0
stk_b2b = [(u_b2, Fraction(100, 133), u_b2, Fraction(100, 133), 0)]
while stk_b2b:
    va, vb, ua, ub, dep = stk_b2b.pop()
    if ua > vb:
        b2b_2d_boxes += 1
        continue
    ub_eff = min(ub, vb)
    # Check feasibility u^{-1} <= 1 + v^{-1/9}*u
    va_m1_9_ub = Fraction(1) / pow_rat_bounds(va, 1, 9, 24)[0]
    if Fraction(1) / ub_eff > 1 + va_m1_9_ub * ub_eff:
        b2b_2d_boxes += 1
        continue
    v_iv = Iv(va, vb)
    u_iv = Iv(ua, ub_eff)
    lnv_iv = ln_inv_iv(v_iv)
    r9_iv = Iv(1) / pow_rat_iv(v_iv, 1, 9, 24)
    q_iv = u_iv / sqrt_iv(v_iv)
    lhs_iv = (Iv(9) / lnv_iv - Iv(Fraction(1, 2))) * (Iv(1) - Iv(2) * v_iv + u_iv)
    rhs_iv = v_iv / (Iv(1) - q_iv) + (Iv(1) - v_iv) * (Iv(1) + r9_iv * u_iv)
    if (lhs_iv - rhs_iv).lo > 0:
        b2b_2d_boxes += 1
    else:
        assert dep < 16, f"B2(b) L>=9 failed at v=[{va},{vb}], u=[{ua},{ub_eff}]"
        if (vb - va) >= (ub_eff - ua):
            vm = (va + vb) / 2
            stk_b2b.append((vm, vb, ua, ub_eff, dep + 1))
            stk_b2b.append((va, vm, ua, ub_eff, dep + 1))
        else:
            um = (ua + ub_eff) / 2
            stk_b2b.append((va, vb, um, ub_eff, dep + 1))
            stk_b2b.append((va, vb, ua, um, dep + 1))

def build_B2_Lsw_m_T_poly(L, d):
    M = L + d
    e_th = L * d + L * (L - 1) // 2
    c = [0] * (M + e_th + M + 2)
    for j in range(1, L + 1):
        c[M + j] += 1
    c[M + L] -= 1
    for k in range(1, L):
        c[M + L + k * M - k * (k + 1) // 2] -= 1
    c[0] -= 1
    c[L] += 1
    for j in range(L + 1, M + 1):
        c[M + j] -= 1
        c[M + e_th + j] += 1
    return c

slope_b2b = (ln_inv_iv(Iv(u_b2)) / ln_133_100).hi - 1
b2b_small = [(L, d) for L in range(4, 9) for d in range(1, int(slope_b2b * L) + 1) if L + d >= 6]
# Also verify L=3 impossible for r^3 >= 1.33, M >= 6: u <= (100/133)^2 < 603/1000!
assert Fraction(100, 133) ** 2 < u_b2
b2b_leaves_small = 0
for L_v, d_v in b2b_small:
    M_v = L_v + d_v
    a_pk = dyadic_bracket(pow_rat_bounds(Fraction(60, 100), 1, M_v, 20)[0], round_up=False, k=8)
    b_pk = dyadic_bracket(pow_rat_bounds(Fraction(100, 133), 1, L_v, 20)[1], round_up=True, k=8)
    def feas_b2b(p_lo, p_hi, k, L=L_v, M=M_v):
        if 133 * (p_lo ** L) > 100 * (1 << (k * L)):
            return False
        if (1 << (k * (2 * M - 1))) > (p_hi ** M) * (1 << (k * (M - 1))) + (p_hi ** (2 * M - 1)):
            return False
        return True
    pT = build_B2_Lsw_m_T_poly(L_v, d_v)
    pU = build_B2_Lsw_m_Usw_poly(L_v, d_v)
    b2b_leaves_small += certify_disjunction_dyadic([pT, pU], a_pk, b_pk, feas_fn=feas_b2b)

print(f"[PASS 6] Theorem B2 certified: {b2a_3d_boxes} 3D boxes (L>=11) + {b2a_leaves_small} leaves ({len(b2_small)} pairs, L<=10) + {b2b_2d_boxes} 2D boxes (L>=9) + {b2b_leaves_small} leaves ({len(b2b_small)} pairs, L<=8) ({time.time() - t6_s:.2f}s)")


# =============================================================================
# 7. THEOREM C EXACT RATIONAL CERTIFICATES (a = 1, r* >= 2, r^L >= 1.22, M >= 6)
# =============================================================================
t7_s = time.time()

# 7a. Certify rational phi bounds (38/100 < phi^{-2}, phi^{-1} < 62/100), u > 1/2 for r*=2 (M>=6), and Delta_P < 2:
assert 5 * (100 ** 2) < (224) ** 2  # (sqrt(5)-1)/2 < 62/100 <=> sqrt(5) < 224/100
assert 5 * (100 ** 2) < (224) ** 2 and (300 - 76) ** 2 > 5 * (100 ** 2)  # (3-sqrt(5))/2 > 38/100 <=> sqrt(5) < 224/100
assert 1 + pow_rat_bounds(Fraction(1, 2), 5, 6, 24)[1] + pow_rat_bounds(Fraction(1, 2), 3, 2, 24)[1] < 2
assert F_M_ub(Fraction(62, 100), 26, K=24) - Fraction(100, 62) < 2
for M_v in range(6, 26):
    # Split [38/100, 62/100] into 8 subintervals and check F_M(u_b) - 1/u_a < 2 whenever feasible
    for i in range(8):
        ua = Fraction(38, 100) + Fraction(i * 3, 100)
        ub = ua + Fraction(3, 100)
        if F_M_ub(ub, M_v) < Fraction(1) / ub:
            continue
        assert F_M_ub(ub, M_v) - Fraction(1) / ua < 2
# Also 1 + u - (r-1)*G_{r*}: since r <= (38/100)^{-1/6} < 6/5 and G_{r*} <= x/(1-x) = 1/(r-1),
# (r-1)*G_{r*} < 1 ALWAYS! Thus 1 + u - (r-1)*G_{r*} > u > 0 IDENTICALLY!

# 7b. Certify r* >= 3 (M >= 6): E_C(S_ub) > 0 for M >= 26 (1D Iv on [38/100, 62/100]) + 6 <= M <= 25
c_r3_boxes = 0
stk_c_r3 = [(Fraction(38, 100), Fraction(62, 100), 0)]
while stk_c_r3:
    ua, ub, dep = stk_c_r3.pop()
    u_iv = Iv(ua, ub)
    x_lb, _ = pow_rat_bounds(ua, 1, 26, 24)
    x_iv = Iv(x_lb, Fraction(1))
    r_iv = Iv(1) / x_iv
    # S_ub(u, 26, K0=24)
    S_ub_ub = F_M_ub(ub, 26, K=24) - 1
    DP_iv = Iv(max(Fraction(0), Fraction(1) + (F_M_ub(ua, 26, K=24) - 1) - Fraction(1) / ua),
               Fraction(1) + S_ub_ub - Fraction(1) / ub)
    # Wait: DP = 1 + S - 1/u <= 1 + S_ub(ub) - 1/ub (since 1+S_ub-1/u is increasing in u!)
    # Check: S_ub is increasing in u and -1/u is increasing in u! So DP_ub = 1 + S_ub(ub) - 1/ub!
    DP_ub = Fraction(1) + S_ub_ub - Fraction(1) / ub
    G3_iv = x_iv + x_iv.pow_int(2)
    # E_C = 2*(1 + u + G - r/u) - DP*(1 + u - (r-1)*G)
    if DP_ub < 0:
        c_r3_boxes += 1
        continue
    E3_iv = Iv(2) * (Iv(1) + u_iv + G3_iv - r_iv / u_iv) - Iv(Fraction(0), DP_ub) * (Iv(1) + u_iv - (r_iv - Iv(1)) * G3_iv)
    if E3_iv.lo > 0:
        c_r3_boxes += 1
    else:
        assert dep < 14
        um = (ua + ub) / 2
        stk_c_r3.append((um, ub, dep + 1))
        stk_c_r3.append((ua, um, dep + 1))

for M_v in range(6, 26):
    stk_m = [(Fraction(38, 100), Fraction(62, 100), 0)]
    while stk_m:
        ua, ub, dep = stk_m.pop()
        u_iv = Iv(ua, ub)
        x_iv = pow_rat_iv(u_iv, 1, M_v, 24)
        r_iv = Iv(1) / x_iv
        S_ub_ub = F_M_ub(ub, M_v) - 1
        # r* >= 3 feasibility: 1/u > 1 + x^{M-1} + x^{2M-3} and 1/u <= 1 + S
        # => 1/ua > 1 + x_iv.lo^{M-1} + x_iv.lo^{2M-3} and 1/ub <= 1 + S_ub_ub
        S2_lb = Fraction(1) + (x_iv.lo ** (M_v - 1)) + (x_iv.lo ** (2 * M_v - 3))
        if Fraction(1) / ub > Fraction(1) + S_ub_ub or Fraction(1) / ua <= S2_lb:
            c_r3_boxes += 1
            continue
        DP_ub = Fraction(1) + S_ub_ub - Fraction(1) / ub
        G3_iv = x_iv + x_iv.pow_int(2)
        E3_iv = Iv(2) * (Iv(1) + u_iv + G3_iv - r_iv / u_iv) - Iv(Fraction(0), DP_ub) * (Iv(1) + u_iv - (r_iv - Iv(1)) * G3_iv)
        if E3_iv.lo > 0:
            c_r3_boxes += 1
        else:
            assert dep < 14, f"C r*>=3 M={M_v} failed at [{ua},{ub}]"
            um = (ua + ub) / 2
            stk_m.append((um, ub, dep + 1))
            stk_m.append((ua, um, dep + 1))

# 7c. Certify r*=2, M >= 35: u > 51/100 and E_C(S_ub(K0=26)) > 0 on [51/100, 62/100]
# Using exact identity 1 + u - (r-1)*x = u + x => E_C = 2*(1 + u) + (2 - DP)*x - 2*r/u - DP*u,
# which is STRICTLY INCREASING in x (since 2 - DP > 0 and r = 1/x) and STRICTLY DECREASING in DP!
u_c_r2 = Fraction(51, 100)
assert Fraction(100, 51) > 1 + pow_rat_bounds(u_c_r2, 34, 35, 24)[1] + pow_rat_bounds(u_c_r2, 67, 35, 24)[1]
c_r2_35_boxes = 0
stk_c_35 = [(u_c_r2, Fraction(62, 100), 0)]
while stk_c_35:
    ua, ub, dep = stk_c_35.pop()
    x_lb, _ = pow_rat_bounds(ua, 1, 35, 24)
    r_ub = Fraction(1) / x_lb
    S_ub_ub = F_M_ub(ub, 35, K=26) - 1
    DP_ub = Fraction(1) + S_ub_ub - Fraction(1) / ub
    assert DP_ub < 2
    # Prune if u > phi^{-1} on whole box (since r*>=2 forces 1/u > 1 + u => 1/ua > 1 + ua):
    if Fraction(1) / ua <= 1 + ua:
        c_r2_35_boxes += 1
        continue
    # Strictly valid lower bound using monotonicity in x (2 - DP_ub > 0) and DP:
    E2_lo = 2 * (1 + ua) + (2 - DP_ub) * x_lb - 2 * r_ub / ua - DP_ub * ub
    if E2_lo > 0:
        c_r2_35_boxes += 1
    else:
        assert dep < 16, f"C r*=2 M>=35 failed at [{ua},{ub}], E2_lo={E2_lo}"
        um = (ua + ub) / 2
        stk_c_35.append((um, ub, dep + 1))
        stk_c_35.append((ua, um, dep + 1))

# 7d. Certify r*=2, 6 <= M <= 34: all 421 pairs via exact integer dyadic monotone-splitting for (L_sw > T) | (L_sw > hi_p)
def build_C_hi_poly(L, d, r_star=2):
    M = L + d
    e_th = L * d + L * (L - 1) // 2
    deg_h = max(M + L + (L - 1) * M, M + e_th + L) + 2
    pH = [0] * (deg_h + 1)
    for j in range(1, L + 1):
        pH[M + j] += 1
    pH[M + L] -= 1
    for k in range(1, L):
        pH[M + L + k * M - k * (k + 1) // 2] -= 1
    pH[0] -= 1
    pH[L] += 1
    for j in range(r_star, L):
        pH[M + j] -= 1
        pH[M + e_th + j] += 1
    pH[M + L] += 1
    pH[M + e_th + L] -= 1
    return pH

c_pairs_small = [(L, M - L) for M in range(6, 35) for L in range(3, M)]
assert len(c_pairs_small) == 493
c_leaves_small = 0
for L_v, d_v in c_pairs_small:
    M_v = L_v + d_v
    a_pk = dyadic_bracket(pow_rat_bounds(Fraction(1, 2), 1, M_v, 20)[0], round_up=False, k=8)
    b_pk = dyadic_bracket(pow_rat_bounds(Fraction(50, 61), 1, L_v, 20)[1], round_up=True, k=8)
    def feas_c(p_lo, p_hi, k, L=L_v, M=M_v):
        if 61 * (p_lo ** L) > 50 * (1 << (k * L)):
            return False
        if (1 << (k * (2 * M - 1))) <= (p_lo ** M) * (1 << (k * (M - 1))) + (p_lo ** (2 * M - 1)):
            return False
        if (1 << (k * (3 * M - 3))) > (p_hi ** M) * (1 << (k * (2 * M - 3))) + (p_hi ** (2 * M - 1)) * (1 << (k * (M - 2))) + (p_hi ** (3 * M - 3)):
            return False
        return True
    pT = build_B2_Lsw_m_T_poly(L_v, d_v)
    pH = build_C_hi_poly(L_v, d_v, r_star=2)
    c_leaves_small += certify_disjunction_dyadic([pT, pH], a_pk, b_pk, feas_fn=feas_c)

print(f"[PASS 7] Theorem C certified: {c_r3_boxes} boxes (r*>=3) + {c_r2_35_boxes} boxes (r*=2, M>=35) + {c_leaves_small} dyadic leaves ({len(c_pairs_small)} pairs, M<=34) ({time.time() - t7_s:.2f}s)")
print(f"PASS (total elapsed {time.time() - t_total_start:.2f}s)")
