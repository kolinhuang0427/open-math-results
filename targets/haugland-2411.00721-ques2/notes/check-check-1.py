#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for Haugland-Omland Question 2.3 / Open Problem (iii).

Built strictly from primary source definitions (arXiv:2411.00721v2) and the proof claims
in targets/haugland-2411.00721-ques2/PROOF.md. Zero floating-point arithmetic.
"""

from __future__ import annotations

import math
import random
import sys


def ceil_log2(k: int) -> int:
    assert k >= 1
    if k == 1:
        return 0
    return (k - 1).bit_length()


def eval_anf(c0: int, lin: list[int], Q: list[list[int]], y: list[int]) -> int:
    k = len(y)
    val = c0 & 1
    for j in range(k):
        val ^= (lin[j] & y[j])
    for i in range(k):
        if y[i]:
            row = Q[i]
            for j in range(i + 1, k):
                val ^= (row[j] & y[j])
    return val & 1


def eval_Fn(c0: int, lin: list[int], Q: list[list[int]], n: int, x: list[int]) -> list[int]:
    k = len(lin)
    assert len(x) == n and n >= k
    out = [0] * n
    for r in range(n):
        window = [x[(r + j) % n] for j in range(k)]
        out[r] = eval_anf(c0, lin, Q, window)
    return out


def has_diameter_k(lin: list[int], Q: list[list[int]]) -> bool:
    """Check whether f depends on both y_0 and y_{k-1}."""
    k = len(lin)
    dep0 = bool(lin[0]) or any(Q[0][j] for j in range(1, k))
    dep_last = bool(lin[k - 1]) or any(Q[i][k - 1] for i in range(k - 1))
    return dep0 and dep_last


# --- Exact polynomial arithmetic over F_2 ---
# Polynomials represented as int bitmasks: bit i is coefficient of z^i.

def poly_deg(p: int) -> int:
    return p.bit_length() - 1


def poly_mul(a: int, b: int) -> int:
    res = 0
    while b:
        lsb = b & -b
        shift = lsb.bit_length() - 1
        res ^= (a << shift)
        b ^= lsb
    return res


def poly_divmod(a: int, b: int) -> tuple[int, int]:
    assert b != 0
    db = poly_deg(b)
    q = 0
    r = a
    while r and poly_deg(r) >= db:
        shift = poly_deg(r) - db
        q ^= (1 << shift)
        r ^= (b << shift)
    return q, r


def poly_gcd(a: int, b: int) -> int:
    while b:
        _, r = poly_divmod(a, b)
        a, b = b, r
    return a


def poly_inv_mod(a: int, mod: int) -> int:
    """Extended Euclidean algorithm over F_2[z] returning a^{-1} mod mod."""
    r0, r1 = mod, poly_divmod(a, mod)[1]
    t0, t1 = 0, 1
    while r1:
        q, r2 = poly_divmod(r0, r1)
        r0, r1 = r1, r2
        t0, t1 = t1, t0 ^ poly_mul(q, t1)
    assert r0 == 1, f"Not invertible mod {bin(mod)}"
    return poly_divmod(t0, mod)[1]


def poly_pow_mod(base: int, exp: int, mod: int) -> int:
    res = 1
    b = poly_divmod(base, mod)[1]
    e = exp
    while e > 0:
        if e & 1:
            res = poly_divmod(poly_mul(res, b), mod)[1]
        b = poly_divmod(poly_mul(b, b), mod)[1]
        e >>= 1
    return res


def poly_to_vec(p: int, n: int) -> list[int]:
    return [(p >> i) & 1 for i in range(n)]


def vec_to_poly(v: list[int]) -> int:
    p = 0
    for i, b in enumerate(v):
        if b & 1:
            p |= (1 << i)
    return p


def lemma3_construct_collision(
    c0: int,
    lin: list[int],
    Q: list[list[int]],
    N: int,
    s_period: int,
    u: list[int],
    gamma: list[int],
) -> list[int]:
    """Construct x in F_2^N via Lemma 3 proof formula such that F_N(x+u) = F_N(x)."""
    k = len(lin)
    P_period = 1 << s_period
    assert (N & (N - 1)) == 0 and N >= P_period + k - 1
    assert any(g != 0 for g in gamma)
    for r in range(N):
        assert u[r] == u[(r + P_period) % N]

    # tilde_P(z) = sum_{j=0}^{k-1} gamma_j z^{k-1-j}
    tilde_P = 0
    for j in range(k):
        if gamma[j]:
            tilde_P |= (1 << (k - 1 - j))
    assert tilde_P != 0 and poly_deg(tilde_P) <= k - 1

    # Factor out powers of (z + 1)
    z_plus_1 = 0b11  # z + 1
    e = 0
    R = tilde_P
    while True:
        q, rem = poly_divmod(R, z_plus_1)
        if rem == 0:
            R = q
            e += 1
        else:
            break
    assert 0 <= e <= k - 1
    # Check R(1) == 1 (odd number of terms)
    assert (R.bit_count() & 1) == 1

    mod = (1 << N) ^ 1  # z^N + 1
    R_inv = poly_inv_mod(R, mod)

    # v(u) = F_N(u) + F_N(0)
    Fn_u = eval_Fn(c0, lin, Q, N, u)
    Fn_0 = eval_Fn(c0, lin, Q, N, [0] * N)
    v = [Fn_u[r] ^ Fn_0[r] for r in range(N)]

    # Verify V(z) == (z+1)^{N - 2^s} * tilde_V(z) mod (z^N + 1)
    tilde_V = vec_to_poly(v[:P_period])
    V = vec_to_poly(v)
    factor = poly_pow_mod(z_plus_1, N - P_period, mod)
    assert poly_divmod(poly_mul(factor, tilde_V), mod)[1] == V

    # X(z) = z^{k-1} * R^{-1} * (z+1)^{N - 2^s - e} * tilde_V(z) mod (z^N + 1)
    exp = N - P_period - e
    assert exp >= 0
    zp_pow = poly_pow_mod(z_plus_1, exp, mod)
    X = poly_mul(1 << (k - 1), R_inv)
    X = poly_divmod(poly_mul(X, zp_pow), mod)[1]
    X = poly_divmod(poly_mul(X, tilde_V), mod)[1]

    x = poly_to_vec(X, N)
    x_plus_u = [x[r] ^ u[r] for r in range(N)]
    assert eval_Fn(c0, lin, Q, N, x_plus_u) == eval_Fn(c0, lin, Q, N, x)
    return x


def compute_C(Q: list[list[int]], u: list[int], k: int) -> list[list[int]]:
    N = len(u)
    C = [[0] * k for _ in range(N)]
    for r in range(N):
        for j in range(k):
            val = 0
            for i in range(k):
                val ^= (Q[i][j] & u[(r + i) % N])
            C[r][j] = val
    return C


def theorem1_find_collision(c0: int, lin: list[int], Q: list[list[int]]) -> tuple[int, list[int], list[int]]:
    """Follow Theorem 1's double induction to constructively produce (N, x, u) with u != 0 and F_N(x+u) = F_N(x)."""
    k = len(lin)
    assert k >= 2
    assert any(Q[i][j] for i in range(k) for j in range(k))
    s_max = ceil_log2(k)
    N = 1 << (s_max + 1)
    assert 2 * k <= N <= 4 * k - 4

    # Check directional derivative identity (1)-(2) on a random vector pair first
    rng = random.Random(k * 1009 + c0)
    rx = [rng.randint(0, 1) for _ in range(N)]
    ru = [rng.randint(0, 1) for _ in range(N)]
    lhs = [a ^ b for a, b in zip(eval_Fn(c0, lin, Q, N, [rx[i] ^ ru[i] for i in range(N)]), eval_Fn(c0, lin, Q, N, rx))]
    Fn_ru = eval_Fn(c0, lin, Q, N, ru)
    Fn_0 = eval_Fn(c0, lin, Q, N, [0] * N)
    C_ru = compute_C(Q, ru, k)
    for r in range(N):
        rhs = (Fn_ru[r] ^ Fn_0[r])
        for j in range(k):
            rhs ^= (C_ru[r][j] & rx[(r + j) % N])
        assert lhs[r] == rhs, "Equation (1) failed"

    def residue_sum(s: int, j: int, c: int) -> int:
        mod = 1 << s
        return sum(Q[i][j] for i in range(k) if i % mod == c % mod) & 1

    # Base case s = 0
    u_ones = [1] * N
    C_base = compute_C(Q, u_ones, k)
    gamma0 = [residue_sum(0, j, 0) for j in range(k)]
    for r in range(N):
        assert C_base[r] == gamma0
    if any(gamma0):
        x = lemma3_construct_collision(c0, lin, Q, N, 0, u_ones, gamma0)
        return N, x, u_ones

    # Outer induction s = 0 .. s_max - 1
    for s in range(s_max):
        P = 1 << s
        two_P = P << 1
        # Verify S_j^{(s)}(c) == 0
        for j in range(k):
            for c in range(P):
                assert residue_sum(s, j, c) == 0

        a = [[residue_sum(s + 1, j, c) for c in range(two_P)] for j in range(k)]
        for j in range(k):
            for b in range(P):
                assert a[j][b] == a[j][b + P], "Eq (6) failed"

        # A_j^*(T) in R_P = F_2[T]/(T^P + 1)
        mod_P = (1 << P) ^ 1
        A_star = []
        for j in range(k):
            poly = 0
            for b in range(P):
                if a[j][b]:
                    exp = (-b) % P
                    poly ^= (1 << exp)
            A_star.append(poly)

        for e in range(P):
            # W(T) = (T + 1)^{P - 1 - e} mod (T + 1)^P
            W = poly_pow_mod(0b11, P - 1 - e, mod_P)
            w = poly_to_vec(W, P)
            # Check explicit binomial formula w_m = binom(P-1-e, m) mod 2
            for m in range(P):
                assert w[m] == (math.comb(P - 1 - e, m) & 1)
            assert any(w)

            u = [w[m % two_P] if (m % two_P) < P else 0 for m in range(N)]
            assert any(u)
            C_u = compute_C(Q, u, k)

            # Verify Eq (8): [T^{r mod P}](W(T) A_j^*(T)) == C_j(r)
            H = [poly_divmod(poly_mul(W, A_star[j]), mod_P)[1] for j in range(k)]
            for r in range(N):
                for j in range(k):
                    coeff = (H[j] >> (r % P)) & 1
                    assert coeff == C_u[r][j], "Eq (8) failed"

            # Verify H_j(T) = gamma_j * sum_{r=0}^{P-1} T^r
            all_ones_P = (1 << P) - 1
            gamma = [H[j] & 1 for j in range(k)]
            for j in range(k):
                assert H[j] == (all_ones_P if gamma[j] else 0)
            for r in range(N):
                assert C_u[r] == gamma

            if any(gamma):
                x = lemma3_construct_collision(c0, lin, Q, N, s + 1, u, gamma)
                return N, x, u

    raise AssertionError("Theorem 1 failed to find a collision for degree-2 f!")


def make_sym_Q(k: int, upper_bits: list[tuple[int, int]]) -> list[list[int]]:
    Q = [[0] * k for _ in range(k)]
    for i, j in upper_bits:
        assert 0 <= i < j < k
        Q[i][j] ^= 1
        Q[j][i] ^= 1
    return Q


def run_all_checks() -> None:
    print("Check 1: N bounds and Lemma 3 hypotheses for k in 2..500...")
    for k in range(2, 501):
        s_max = ceil_log2(k)
        N = 1 << (s_max + 1)
        assert 2 * k <= N <= 4 * k - 4
        for t in range(s_max + 1):
            assert (1 << t) + k - 1 < N

    print("Check 2: Eq (3) polynomial identity (w+1) sum w^t == (w+1)^L in F_2[w]...")
    for exp in range(0, 6):
        L = 1 << exp
        sum_wt = (1 << L) - 1
        assert poly_mul(0b11, sum_wt) == poly_pow_mod(0b11, L, 1 << (L + 2))
        assert sum_wt == poly_pow_mod(0b11, L - 1, 1 << (L + 2))

    print("Check 3: Exhaustive k=2 (all 8) and k=3 (all 112) degree-2 functions...")
    for k in (2, 3):
        pairs = [(i, j) for i in range(k) for j in range(i + 1, k)]
        tested = 0
        for qmask in range(1, 1 << len(pairs)):
            chosen = [pairs[idx] for idx in range(len(pairs)) if (qmask >> idx) & 1]
            Q = make_sym_Q(k, chosen)
            for lmask in range(1 << k):
                lin = [(lmask >> j) & 1 for j in range(k)]
                for c0 in (0, 1):
                    N, x, u = theorem1_find_collision(c0, lin, Q)
                    assert any(u)
                    tested += 1
        print(f"  k={k}: {tested} functions passed")

    print("Check 4: k=4 all 63 nonzero Q matrices x 16 linear+constant samples...")
    k = 4
    pairs = [(i, j) for i in range(k) for j in range(i + 1, k)]
    rng = random.Random(42)
    tested4 = 0
    for qmask in range(1, 1 << len(pairs)):
        chosen = [pairs[idx] for idx in range(len(pairs)) if (qmask >> idx) & 1]
        Q = make_sym_Q(k, chosen)
        for sample in range(16):
            lmask = sample if sample < 16 else rng.randrange(16)
            lin = [(lmask >> j) & 1 for j in range(k)]
            c0 = sample & 1
            theorem1_find_collision(c0, lin, Q)
            tested4 += 1
    print(f"  k=4: {tested4} functions passed")

    print("Check 5: Random diameter-k degree-2 functions for k=5..12 (100 each)...")
    for k in range(5, 13):
        pairs = [(i, j) for i in range(k) for j in range(i + 1, k)]
        for _ in range(100):
            while True:
                qmask = rng.randrange(1, 1 << len(pairs))
                chosen = [pairs[idx] for idx in range(len(pairs)) if (qmask >> idx) & 1]
                Q = make_sym_Q(k, chosen)
                lin = [rng.randint(0, 1) for _ in range(k)]
                if has_diameter_k(lin, Q):
                    break
            c0 = rng.randint(0, 1)
            theorem1_find_collision(c0, lin, Q)
    print("  k=5..12: 800 diameter-k functions passed")

    print("Check 6: Sharpness family f_m in Section 4 (m=1,2,3)...")
    for m in (1, 2, 3):
        k = (1 << m) + 2
        # f_m(y) = y_0 + (y_0 + y_{2^m})(y_1 + y_{2^m + 1})
        #        = y_0 + y_0 y_1 + y_0 y_{2^m+1} + y_1 y_{2^m} + y_{2^m} y_{2^m+1}
        lin = [0] * k
        lin[0] = 1
        p2m = 1 << m
        Q = make_sym_Q(k, [(0, 1), (0, p2m + 1), (1, p2m), (p2m, p2m + 1)])
        assert has_diameter_k(lin, Q)

        # At n_small = 2^{m+1} = 2^{ceil(log2 k)}, verify F is an involution (bijective)
        n_small = 1 << (m + 1)
        assert ceil_log2(k) == m + 1
        if m <= 2:
            images = set()
            for mask in range(1 << n_small):
                x = [(mask >> i) & 1 for i in range(n_small)]
                y = eval_Fn(0, lin, Q, n_small, x)
                assert eval_Fn(0, lin, Q, n_small, y) == x
                images.add(tuple(y))
            assert len(images) == (1 << n_small)
        else:
            for _ in range(2000):
                x = [rng.randint(0, 1) for _ in range(n_small)]
                y = eval_Fn(0, lin, Q, n_small, x)
                assert eval_Fn(0, lin, Q, n_small, y) == x

        # At N = 2^{m+2}, Theorem 1 constructs a collision
        N, x, u = theorem1_find_collision(0, lin, Q)
        assert N == (1 << (m + 2))
        assert any(u)
        print(f"  m={m} (k={k}): bijective involution at n={n_small}, collision at N={N} verified")

    print("PASS")


if __name__ == "__main__":
    try:
        run_all_checks()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
