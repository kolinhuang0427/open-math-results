#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/oeis-A179525/PROOF.md.

Zero floating-point arithmetic anywhere: uses exact integer polynomial arithmetic
in Z[x]/(x^N) (and Fraction for general unit seeds) directly from live OEIS A179525
rev. 74 definitions.
"""

from fractions import Fraction

OEIS_A179525 = [
    1, 1, 2, 7, 33, 197, 1419, 11966, 115575, 1257718, 15223822, 202860828,
    2950665011, 46516215168, 790009447590, 14379745626739, 279256447482090,
    5763290215111558, 125960271446527241, 2906289188751628643,
    70594767279197608011, 1800695322331687800336, 48122711251655255426539,
    1344617808976210991187090, 39206731897407002624384182,
    1190905492485213830900901986,
]

# ---------------------------------------------------------------------------
# Exact truncated power series arithmetic mod x^N over Z (or Q via Fraction)
# ---------------------------------------------------------------------------

def fps_trim(a, N):
    res = list(a[:N]) + [0] * max(0, N - len(a))
    return res

def fps_add(a, b, N):
    return [a[i] + b[i] for i in range(N)]

def fps_sub(a, b, N):
    return [a[i] - b[i] for i in range(N)]

def fps_mul(a, b, N):
    res = [0] * N
    for i in range(N):
        ai = a[i]
        if ai == 0:
            continue
        for j in range(N - i):
            res[i + j] += ai * b[j]
    return res

def fps_inv(a, N):
    """Exact multiplicative inverse in Z[[x]]/(x^N) (requires a[0] == +-1) or Q[[x]]/(x^N)."""
    c0 = a[0]
    assert c0 != 0
    if isinstance(c0, int) and abs(c0) == 1:
        inv0 = c0
    else:
        inv0 = Fraction(1) / c0
    b = [0] * N
    b[0] = inv0
    for n in range(1, N):
        s = sum(a[k] * b[n - k] for k in range(1, n + 1))
        b[n] = -s * inv0
    return b

def fps_const(c, N):
    res = [0] * N
    res[0] = c
    return res

def fps_pow(a, exp, N):
    res = fps_const(1, N)
    base = list(a)
    e = exp
    while e > 0:
        if e & 1:
            res = fps_mul(res, base, N)
        e >>= 1
        if e:
            base = fps_mul(base, base, N)
    return res

def val_x(a):
    for i, c in enumerate(a):
        if c != 0:
            return i
    return len(a)

N = 36
q = fps_trim([1, 1], N)  # q = 1 + x

def q_pow_minus_1(m, N):
    return fps_sub(fps_pow(q, m, N), fps_const(1, N), N)

def one_minus_q_pow(m, N):
    return fps_sub(fps_const(1, N), fps_pow(q, m, N), N)

# ---------------------------------------------------------------------------
# 1. Primary A(x) vs live OEIS A179525 (26 terms)
# ---------------------------------------------------------------------------

P = [fps_const(1, N)]
for m in range(1, N + 1):
    Pm = fps_mul(P[-1], q_pow_minus_1(m, N), N)
    assert val_x(Pm) >= m
    P.append(Pm)

A_series = fps_const(0, N)
for Pm in P:
    A_series = fps_add(A_series, Pm, N)

assert A_series[: len(OEIS_A179525)] == OEIS_A179525
print(f"[1] PASS Direct A(x) matches all {len(OEIS_A179525)} OEIS A179525 terms mod x^{N}.")

# ---------------------------------------------------------------------------
# 2. Lemma 1 & Theorem 1: Gladkovskii 3-step CF and x-adic convergence
# ---------------------------------------------------------------------------

def compute_Q(k, N):
    res = fps_const(1, N)
    term = fps_const(1, N)
    for n in range(1, N + 1):
        term = fps_mul(term, q_pow_minus_1(2 * k + n, N), N)
        assert val_x(term) >= n
        res = fps_add(res, term, N)
    return res

Q = {k: compute_Q(k, N) for k in range(16)}
assert Q[0] == A_series

for k in range(15):
    # Lemma 1: Q(k) == 1 + (q^{2k+1}-1) + (q^{2k+1}-1)*(q^{2k+2}-1)*Q(k+1)
    f1 = q_pow_minus_1(2 * k + 1, N)
    f2 = q_pow_minus_1(2 * k + 2, N)
    rhs = fps_add(fps_add(fps_const(1, N), f1, N), fps_mul(fps_mul(f1, f2, N), Q[k + 1], N), N)
    assert Q[k] == rhs

    # Theorem 1 bottom-up CF:
    # Q(k) = 1 - (1 - q^{2k+1}) / (1 - (1 - q^{2k+2}) / (1 - q^{2k+2} - 1/Q(k+1)))
    a = one_minus_q_pow(2 * k + 1, N)
    b = one_minus_q_pow(2 * k + 2, N)
    g = Q[k + 1]
    inv_g = fps_inv(g, N)
    D2 = fps_sub(b, inv_g, N)
    assert D2[0] == -1  # unit in Z[[x]]
    D1 = fps_sub(fps_const(1, N), fps_mul(b, fps_inv(D2, N), N), N)
    assert D1[0] == 1   # unit in Z[[x]]
    top = fps_sub(fps_const(1, N), fps_mul(a, fps_inv(D1, N), N), N)
    assert top == Q[k]

print("[2] PASS Lemma 1 & Theorem 1 exact bottom-up CF recurrence holds mod x^36 for k=0..14.")

# Convergence of finite truncations Q^{(K)}(0):
def eval_cf_trunc(K, seed, N):
    cur = seed
    for k in range(K, -1, -1):
        a = one_minus_q_pow(2 * k + 1, N)
        b = one_minus_q_pow(2 * k + 2, N)
        D2 = fps_sub(b, fps_inv(cur, N), N)
        D1 = fps_sub(fps_const(1, N), fps_mul(b, fps_inv(D2, N), N), N)
        cur = fps_sub(fps_const(1, N), fps_mul(a, fps_inv(D1, N), N), N)
    return cur

for K in range(13):
    # Seed = 1 (1 + O(x)) -> error >= 2K + 3
    q_1 = eval_cf_trunc(K, fps_const(1, N), N)
    v_1 = val_x(fps_sub(q_1, A_series, N))
    assert v_1 >= 2 * K + 3, f"K={K}: expected val >= {2*K+3}, got {v_1}"
    # Seed = 1 + 5x (1 + O(x)) -> error >= 2K + 3
    q_1p = eval_cf_trunc(K, fps_trim([1, 5], N), N)
    assert val_x(fps_sub(q_1p, A_series, N)) >= 2 * K + 3
    # Unit seed = -1 + 3x (Z[[x]]^x, g(0)=-1) -> exact error == 2K + 2
    q_m1 = eval_cf_trunc(K, fps_trim([-1, 3], N), N)
    v_m1 = val_x(fps_sub(q_m1, A_series, N))
    assert v_m1 == 2 * K + 2, f"K={K}: expected val == {2*K+2}, got {v_m1}"
    # Rational unit seed = Fraction(3, 2) + x -> error == 2K + 2
    q_rat = eval_cf_trunc(K, fps_trim([Fraction(3, 2), Fraction(1)], N), N)
    v_rat = val_x(fps_sub(q_rat, [Fraction(c) for c in A_series], N))
    assert v_rat == 2 * K + 2

print("[3] PASS Theorem 1 convergence: O(x^{2K+3}) for 1+O(x) seeds and exact x^{2K+2} order for unit seeds (K=0..12).")

# ---------------------------------------------------------------------------
# 3. Theorem 2: Peter Bala's Even-Product Conjecture
# ---------------------------------------------------------------------------

bala_sum = fps_const(0, N)
for n in range(N // 2):
    prod_even = fps_const(1, N)
    for k in range(1, 2 * n + 1):
        prod_even = fps_mul(prod_even, one_minus_q_pow(k, N), N)
    assert prod_even == P[2 * n]
    term_n = fps_mul(fps_pow(q, 2 * n + 1, N), prod_even, N)
    assert term_n == fps_add(P[2 * n], P[2 * n + 1], N)
    bala_sum = fps_add(bala_sum, term_n, N)

assert bala_sum == A_series
assert bala_sum[: len(OEIS_A179525)] == OEIS_A179525
print("[4] PASS Theorem 2: q^{2n+1}*prod_{k=1..2n}(1-q^k) == P_{2n} + P_{2n+1} and Bala sum == A(x) mod x^36.")
print("PASS")
