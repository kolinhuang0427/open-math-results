"""Exact-arithmetic verification suite for PROOF.md (Godard-Reis Problem 3).

Uses 100% exact integer, finite-field, polynomial, and rational arithmetic
(zero floating-point operations anywhere).
"""

import math
import random
import sys
import time
import numpy as np
import sympy as sp


# ---------------------------------------------------------------------------
# Exact polynomial and finite-field arithmetic over F_p
# ---------------------------------------------------------------------------

def poly_trim(a, p):
    a = [c % p for c in a]
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


def poly_add(a, b, p):
    n = max(len(a), len(b))
    out = [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p for i in range(n)]
    return poly_trim(out, p)


def poly_sub(a, b, p):
    n = max(len(a), len(b))
    out = [((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p for i in range(n)]
    return poly_trim(out, p)


def poly_mul(a, b, p):
    if not a or not b:
        return ()
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] += ai * bj
    return poly_trim(out, p)


def poly_divmod(a, b, p):
    assert b, "Division by zero polynomial"
    a = list(poly_trim(a, p))
    b = list(poly_trim(b, p))
    if len(a) < len(b):
        return (), tuple(a)
    inv_lc = pow(b[-1], -1, p)
    deg_b = len(b) - 1
    q = [0] * (len(a) - deg_b)
    for i in range(len(a) - 1, deg_b - 1, -1):
        if a[i] != 0:
            coeff = (a[i] * inv_lc) % p
            q[i - deg_b] = coeff
            for j in range(deg_b + 1):
                a[i - deg_b + j] = (a[i - deg_b + j] - coeff * b[j]) % p
    return poly_trim(q, p), poly_trim(a, p)


def poly_gcd(a, b, p):
    a = poly_trim(a, p)
    b = poly_trim(b, p)
    while b:
        _, r = poly_divmod(a, b, p)
        a, b = b, r
    if not a:
        return ()
    inv_lc = pow(a[-1], -1, p)
    return tuple((c * inv_lc) % p for c in a)


def poly_deriv(a, p):
    if len(a) <= 1:
        return ()
    return poly_trim([(i * a[i]) % p for i in range(1, len(a))], p)


def poly_powmod(base, exp, mod, p):
    res = (1,)
    cur = poly_divmod(base, mod, p)[1]
    while exp > 0:
        if exp & 1:
            res = poly_divmod(poly_mul(res, cur, p), mod, p)[1]
        cur = poly_divmod(poly_mul(cur, cur, p), mod, p)[1]
        exp >>= 1
    return res


def prime_factors(n):
    return sorted(sp.factorint(n).keys())


def smallest_prime_factor(n):
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0:
            return d
    return n


def divisor_count(n):
    cnt = 0
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0:
            cnt += 1 if d * d == n else 2
    return cnt


def is_irreducible_fp(f, p):
    """Rabin's irreducibility test over F_p for monic polynomial f (low-deg first)."""
    deg = len(f) - 1
    if deg <= 0:
        return False
    if deg == 1:
        return True
    x_poly = (0, 1)
    for r in prime_factors(deg):
        d = deg // r
        xp = poly_powmod(x_poly, p ** d, f, p)
        g = poly_gcd(poly_sub(xp, x_poly, p), f, p)
        if len(g) > 1:
            return False
    xpn = poly_powmod(x_poly, p ** deg, f, p)
    return xpn == x_poly


def find_irreducible_poly(p, n):
    """Deterministically find a sparse monic irreducible polynomial of degree n over F_p."""
    for c0 in range(1, p):
        f = [c0] + [0] * (n - 1) + [1]
        if is_irreducible_fp(tuple(f), p):
            return tuple(f)
    for k in range(1, n):
        for c1 in range(1, p):
            for c0 in range(1, p):
                f = [0] * (n + 1)
                f[n] = 1
                f[k] = c1
                f[0] = c0
                if is_irreducible_fp(tuple(f), p):
                    return tuple(f)
    rng = random.Random(42 + 100 * p + n)
    while True:
        f = [rng.randrange(1, p)] + [rng.randrange(p) for _ in range(n - 1)] + [1]
        if is_irreducible_fp(tuple(f), p):
            return tuple(f)


class ExtField:
    """Exact polynomial-basis finite field F_{p^n} without full table allocation."""

    def __init__(self, p, n):
        assert p >= 3 and n >= 1
        self.p = p
        self.n = n
        self.size = p ** n
        self.mod = find_irreducible_poly(p, n)
        self.zero = (0,) * n
        self.one = (1,) + (0,) * (n - 1)
        self.x = (0, 1) + (0,) * (n - 2) if n >= 2 else self.one

    def from_int(self, c):
        return (c % self.p,) + (0,) * (self.n - 1)

    def add(self, a, b):
        p = self.p
        return tuple((ai + bi) % p for ai, bi in zip(a, b))

    def sub(self, a, b):
        p = self.p
        return tuple((ai - bi) % p for ai, bi in zip(a, b))

    def neg(self, a):
        p = self.p
        return tuple((-ai) % p for ai in a)

    def scale(self, c, a):
        p = self.p
        c = c % p
        return tuple((c * ai) % p for ai in a)

    def mul(self, a, b):
        p = self.p
        n = self.n
        res = [0] * (2 * n - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bi in enumerate(b):
                    if bi:
                        res[i + j] += ai * bi
        mod = self.mod
        for k in range(2 * n - 2, n - 1, -1):
            c = res[k] % p
            if c:
                for j in range(n):
                    res[k - n + j] -= c * mod[j]
        return tuple(res[i] % p for i in range(n))

    def sq(self, a):
        return self.mul(a, a)

    def pow(self, a, e):
        res = self.one
        cur = a
        while e > 0:
            if e & 1:
                res = self.mul(res, cur)
            cur = self.mul(cur, cur)
            e >>= 1
        return res

    def inv(self, a):
        assert a != self.zero, "Zero has no inverse"
        p = self.p
        r0, r1 = self.mod, poly_trim(a, p)
        t0, t1 = (), (1,)
        while r1:
            q, r2 = poly_divmod(r0, r1, p)
            t2 = poly_sub(t0, poly_mul(q, t1, p), p)
            r0, r1, t0, t1 = r1, r2, t1, t2
        assert len(r0) == 1
        inv_lc = pow(r0[0], -1, p)
        t0 = tuple((c * inv_lc) % p for c in t0)
        return t0 + (0,) * (self.n - len(t0))

    def div(self, a, b):
        return self.mul(a, self.inv(b))

    def frob(self, a, k=1):
        return self.pow(a, self.p ** k)

    def is_square(self, a):
        if a == self.zero:
            return True
        return self.pow(a, (self.size - 1) // 2) == self.one

    def quad_char(self, a):
        if a == self.zero:
            return 0
        e = self.pow(a, (self.size - 1) // 2)
        return 1 if e == self.one else -1

    def sqrt(self, a):
        """Exact Tonelli-Shanks square root in F_{p^n}."""
        if a == self.zero:
            return self.zero
        assert self.is_square(a), "Element is not a square"
        q = self.size
        if q % 4 == 3:
            return self.pow(a, (q + 1) // 4)
        s = q - 1
        e = 0
        while s % 2 == 0:
            s //= 2
            e += 1
        rng = random.Random(17)
        z = self.x
        while self.is_square(z):
            z = tuple(rng.randrange(self.p) for _ in range(self.n))
        m = e
        c = self.pow(z, s)
        t = self.pow(a, s)
        r = self.pow(a, (s + 1) // 2)
        while t != self.one:
            i = 1
            t2i = self.sq(t)
            while t2i != self.one:
                t2i = self.sq(t2i)
                i += 1
            b = self.pow(c, 1 << (m - i - 1))
            m = i
            c = self.sq(b)
            t = self.mul(t, c)
            r = self.mul(r, b)
        return r

    def to_int(self, a):
        val = 0
        for i in range(self.n - 1, -1, -1):
            val = val * self.p + a[i]
        return val

    def from_int_id(self, val):
        out = []
        for _ in range(self.n):
            out.append(val % self.p)
            val //= self.p
        return tuple(out)


class FastFF:
    """Lookup-table finite field F_{p^n} using integer-only numpy arrays."""

    def __init__(self, p, n):
        self.ef = ExtField(p, n)
        self.p = p
        self.n = n
        self.size = p ** n
        self.mod_poly = self.ef.mod
        order = self.size - 1

        idx = np.arange(self.size, dtype=np.int32)
        vecs = np.zeros((self.size, n), dtype=np.int16)
        tmp = idx.copy()
        for i in range(n):
            vecs[:, i] = tmp % p
            tmp //= p
        self.vecs = vecs
        self.powers = np.array([p ** i for i in range(n)], dtype=np.int32)

        # Find primitive element via ExtField
        pfactors = prime_factors(order)
        prim_tup = None
        for cand_id in range(2, self.size):
            cand = self.ef.from_int_id(cand_id)
            if all(self.ef.pow(cand, order // r) != self.ef.one for r in pfactors):
                prim_tup = cand
                break
        assert prim_tup is not None
        self.prim = self.ef.to_int(prim_tup)

        # Fast sparse multiplication by prim_tup + integer encoding
        prim_terms = [(j, c) for j, c in enumerate(prim_tup) if c != 0]
        mod_terms = [(j, c) for j, c in enumerate(self.mod_poly[:-1]) if c != 0]
        powers_py = [p ** i for i in range(n)]
        self.log_tbl = np.full(self.size, 2 * order, dtype=np.int32)
        self.exp_tbl = np.zeros(4 * order + 1, dtype=np.int32)
        cur = [0] * n
        cur[0] = 1
        max_deg = 2 * n - 2
        for k in range(order):
            cid = sum(cur[i] * powers_py[i] for i in range(n))
            self.log_tbl[cid] = k
            self.exp_tbl[k] = cid
            self.exp_tbl[k + order] = cid
            # Multiply cur by prim_tup mod mod_poly
            buf = [0] * (max_deg + 1)
            for i in range(n):
                ci = cur[i]
                if ci:
                    for j, pj in prim_terms:
                        buf[i + j] += ci * pj
            for deg in range(max_deg, n - 1, -1):
                c = buf[deg] % p
                if c:
                    for j, mj in mod_terms:
                        buf[deg - n + j] -= c * mj
            cur = [buf[i] % p for i in range(n)]

        self.neg_tbl = (((-vecs) % p) @ self.powers).astype(np.int32)

        # Vectorized square, sqrt, and frobenius tables
        self.sq_tbl = np.zeros(self.size, dtype=np.int32)
        self.sq_tbl[1:] = self.exp_tbl[2 * self.log_tbl[1:]]

        self.sqrt1 = np.full(self.size, -1, dtype=np.int32)
        self.sqrt2 = np.full(self.size, -1, dtype=np.int32)
        self.sqrt1[0] = 0
        self.sqrt2[0] = 0
        # Even-log elements are squares; exp_tbl[0:order:2] gives all nonzero squares
        half_logs = np.arange(0, order // 2, dtype=np.int32)
        roots = self.exp_tbl[half_logs]
        sqs = self.exp_tbl[2 * half_logs]
        self.sqrt1[sqs] = roots
        self.sqrt2[sqs] = self.neg_tbl[roots]

        self.frob_tbl = np.zeros(self.size, dtype=np.int32)
        frob_logs = (self.log_tbl[1:].astype(np.int64) * p) % order
        self.frob_tbl[1:] = self.exp_tbl[frob_logs]

        tr_basis = np.zeros(n, dtype=np.int16)
        for i in range(n):
            cur_id = int(self.powers[i])
            s = 0
            for _ in range(n):
                s = self.add_scalar(s, cur_id)
                cur_id = int(self.frob_tbl[cur_id])
            assert s < p
            tr_basis[i] = s
        self.tr_tbl = ((vecs @ tr_basis) % p).astype(np.int16)

        if self.size <= 3500:
            v1 = vecs[:, None, :]
            v2 = vecs[None, :, :]
            self.add_tbl = (((v1 + v2) % p) @ self.powers).astype(np.int32)
        else:
            self.add_tbl = None

    def add_scalar(self, a, b):
        va = self.vecs[a]
        vb = self.vecs[b]
        s = 0
        p = self.p
        for i in range(self.n - 1, -1, -1):
            s = s * p + (int(va[i]) + int(vb[i])) % p
        return s

    def add(self, a, b):
        if self.add_tbl is not None:
            return self.add_tbl[a, b]
        return (((self.vecs[a] + self.vecs[b]) % self.p) @ self.powers).astype(np.int32)

    def sub(self, a, b):
        return self.add(a, self.neg_tbl[b])

    def mul(self, a, b):
        return self.exp_tbl[self.log_tbl[a] + self.log_tbl[b]]

    def mul_scalar(self, a, b):
        if a == 0 or b == 0:
            return 0
        return int(self.exp_tbl[int(self.log_tbl[a]) + int(self.log_tbl[b])])

    def inv(self, a):
        assert a != 0
        return int(self.exp_tbl[(self.size - 1) - int(self.log_tbl[a])])

    def pow_scalar(self, a, e):
        if e == 0:
            return 1
        if a == 0:
            return 0
        return int(self.exp_tbl[(int(self.log_tbl[a]) * e) % (self.size - 1)])

    def is_square(self, a):
        return int(self.sqrt1[a]) != -1

    def quad_char(self, a):
        if a == 0:
            return 0
        return 1 if int(self.sqrt1[a]) != -1 else -1

    def qb(self, b, x, y):
        """Exact Q_b(x, y) = x^2 + b*x*y + y^2."""
        return self.add_scalar(
            self.add_scalar(int(self.sq_tbl[x]), int(self.sq_tbl[y])),
            self.mul_scalar(b, self.mul_scalar(x, y)),
        )

    def span_from_basis(self, basis):
        els = [0]
        seen = {0}
        for v in basis:
            v = int(v)
            if v in seen:
                continue
            new_els = list(els)
            cur = v
            for _ in range(1, self.p):
                for s in els:
                    ns = self.add_scalar(s, cur)
                    new_els.append(ns)
                    seen.add(ns)
                cur = self.add_scalar(cur, v)
            els = new_els
        return np.array(els, dtype=np.int32)

    def random_subspace(self, dim, rng):
        basis = []
        span_set = {0}
        span_list = [0]
        while len(basis) < dim:
            v = rng.randrange(1, self.size)
            if v not in span_set:
                basis.append(v)
                new_els = list(span_list)
                cur = v
                for _ in range(1, self.p):
                    for s in span_list:
                        ns = self.add_scalar(s, cur)
                        new_els.append(ns)
                        span_set.add(ns)
                    cur = self.add_scalar(cur, v)
                span_list = new_els
        return np.array(span_list, dtype=np.int32), basis

    def bfs(self, b, V_arr, start=0):
        """Exact BFS in Gamma(Q_b, V) from `start`."""
        N = self.size
        inv2 = (self.p + 1) // 2
        half_b = self.mul_scalar(b, inv2)
        neg_half_b = int(self.neg_tbl[half_b])
        delta = self.add_scalar(int(self.sq_tbl[half_b]), int(self.neg_tbl[1]))

        dist = np.full(N, -1, dtype=np.int32)
        dist[start] = 0
        frontier = np.array([start], dtype=np.int32)
        cur_d = 0
        count = 1
        V_arr = np.asarray(V_arr, dtype=np.int32)
        V_vecs = self.vecs[V_arr] if self.add_tbl is None else None

        while frontier.size > 0:
            u = self.mul(delta, self.sq_tbl[frontier])
            if self.add_tbl is not None:
                w = self.add_tbl[u[:, None], V_arr[None, :]]
            else:
                w_vec = (self.vecs[u][:, None, :] + V_vecs[None, :, :]) % self.p
                w = w_vec @ self.powers
            r1 = self.sqrt1[w]
            valid = r1 != -1
            if not np.any(valid):
                break
            f_idx, _ = np.nonzero(valid)
            r1v = r1[valid]
            shift = self.mul(neg_half_b, frontier)[f_idx]
            if self.add_tbl is not None:
                y1 = self.add_tbl[shift, r1v]
                y2 = self.add_tbl[shift, self.neg_tbl[r1v]]
            else:
                y1 = self.add(shift, r1v)
                y2 = self.sub(shift, r1v)
            cand = np.concatenate([y1, y2])
            unvis = cand[dist[cand] == -1]
            if unvis.size == 0:
                break
            nxt = np.unique(unvis)
            cur_d += 1
            dist[nxt] = cur_d
            count += int(nxt.size)
            if count == N:
                break
            frontier = nxt

        return dist, count


_FF_CACHE = {}


def get_ff(p, n):
    key = (p, n)
    if key not in _FF_CACHE:
        _FF_CACHE[key] = FastFF(p, n)
    return _FF_CACHE[key]


# ---------------------------------------------------------------------------
# Exact linear algebra over F_p and over any finite field F_q
# ---------------------------------------------------------------------------

def rank_mod_p(rows, ncols, p):
    mat = [[x % p for x in r] for r in rows]
    rank = 0
    for col in range(ncols):
        piv = None
        for r in range(rank, len(mat)):
            if mat[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        inv = pow(mat[rank][col], -1, p)
        mat[rank] = [(x * inv) % p for x in mat[rank]]
        for r in range(len(mat)):
            if r != rank and mat[r][col] != 0:
                fac = mat[r][col]
                mat[r] = [(mat[r][c] - fac * mat[rank][c]) % p for c in range(ncols)]
        rank += 1
    return rank


def rref_basis_mod_p(rows, ncols, p):
    """Return RREF nonzero basis rows (each length ncols) mod p."""
    mat = [[x % p for x in r] for r in rows]
    basis = []
    rank = 0
    for col in range(ncols):
        piv = None
        for r in range(rank, len(mat)):
            if mat[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        inv = pow(mat[rank][col], -1, p)
        mat[rank] = [(x * inv) % p for x in mat[rank]]
        for r in range(len(mat)):
            if r != rank and mat[r][col] != 0:
                fac = mat[r][col]
                mat[r] = [(mat[r][c] - fac * mat[rank][c]) % p for c in range(ncols)]
        basis.append(mat[rank])
        rank += 1
    return basis


def rank_over_ff(ff, rows, ncols):
    """Exact matrix rank over FastFF `ff`."""
    mat = [[int(x) for x in r] for r in rows]
    rank = 0
    for col in range(ncols):
        piv = None
        for r in range(rank, len(mat)):
            if mat[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        inv = ff.inv(mat[rank][col])
        mat[rank] = [ff.mul_scalar(x, inv) for x in mat[rank]]
        for r in range(len(mat)):
            if r != rank and mat[r][col] != 0:
                fac = mat[r][col]
                for c in range(ncols):
                    prod = ff.mul_scalar(fac, mat[rank][c])
                    mat[r][c] = ff.add_scalar(mat[r][c], int(ff.neg_tbl[prod]))
        rank += 1
    return rank


# ---------------------------------------------------------------------------
# Suite 1: Part A — Lower bound s(n) >= n / p_0(n) + 1
# ---------------------------------------------------------------------------

def verify_part_a():
    print("[Suite 1] Part A: Lower bound s(n) >= n/p_0(n) + 1 ...", flush=True)
    rng = random.Random(202605)
    cases = [(4, 3), (4, 5), (5, 3), (5, 5), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3)]

    for n, q in cases:
        p0 = smallest_prime_factor(n)
        d0 = n // p0
        ff = get_ff(q, n)
        sub_exp = (ff.size - 1) // (q ** d0 - 1)
        subfield = [0] + [ff.pow_scalar(ff.prim, k * sub_exp) for k in range(q ** d0 - 1)]
        subfield_set = set(subfield)
        assert len(subfield_set) == q ** d0

        if n % 2 == 0:
            alpha = ff.prim
            assert not ff.is_square(alpha)
            for u in subfield:
                assert ff.is_square(u), f"Subfield element {u} not square in F_{{{q}^{n}}}"
            V = np.array([ff.mul_scalar(alpha, u) for u in subfield], dtype=np.int32)
            V_set = set(int(v) for v in V)
            assert len(V_set) == q ** d0
            for v in V:
                if v != 0:
                    assert not ff.is_square(int(v))

            b_cands = [1, 2 % q, (q - 2) % q, ff.prim, rng.randrange(1, ff.size)]
            for b in b_cands:
                if ff.size <= 7000:
                    for z in range(1, ff.size):
                        assert ff.qb(b, 0, z) not in V_set
                _, cnt = ff.bfs(b, V, start=0)
                assert cnt == 1, f"Expected 0 isolated for even ({n},{q}), got {cnt}"
        else:
            V = np.array(subfield, dtype=np.int32)
            b_cands = [1, 2 % q, (q - 2) % q]
            if d0 > 1:
                b_cands.append(next(x for x in subfield if x >= q))
            inv2 = (q + 1) // 2
            for b in b_cands:
                half_b = ff.mul_scalar(b, inv2)
                delta = ff.add_scalar(int(ff.sq_tbl[half_b]), int(ff.neg_tbl[1]))
                for x in subfield:
                    dx2 = ff.mul_scalar(delta, int(ff.sq_tbl[x]))
                    shift = ff.mul_scalar(int(ff.neg_tbl[half_b]), x)
                    for v in subfield:
                        w = ff.add_scalar(dx2, v)
                        if ff.is_square(w):
                            r = int(ff.sqrt1[w])
                            y1 = ff.add_scalar(shift, r)
                            y2 = ff.add_scalar(shift, int(ff.neg_tbl[r]))
                            assert y1 in subfield_set and y2 in subfield_set
                dist0, cnt0 = ff.bfs(b, V, start=0)
                assert cnt0 == q ** d0 < ff.size
                assert set(int(x) for x in np.nonzero(dist0 >= 0)[0]) == subfield_set
                outside = next(z for z in range(1, ff.size) if z not in subfield_set)
                _, cnt_out = ff.bfs(b, V, start=outside)
                assert cnt_out <= ff.size - q ** d0

    # Exact algebraic closure check for n = 15, q = 3 without building 3^15 vertices
    ef15 = ExtField(3, 15)
    p0_15 = smallest_prime_factor(15)
    d0_15 = 15 // p0_15
    assert p0_15 == 3 and d0_15 == 5
    sub_exp_15 = (3 ** 15 - 1) // (3 ** 5 - 1)
    beta = None
    for seed in range(2, 50):
        g = ef15.from_int_id(seed)
        cand = ef15.pow(g, sub_exp_15)
        if cand[1:] != (0,) * 14:
            beta = cand
            break
    assert beta is not None
    assert ef15.frob(beta, 5) == beta and ef15.frob(beta, 1) != beta

    powers_beta = [ef15.one]
    for _ in range(4):
        powers_beta.append(ef15.mul(powers_beta[-1], beta))
    F243 = []
    for c0 in range(3):
        for c1 in range(3):
            for c2 in range(3):
                for c3 in range(3):
                    for c4 in range(3):
                        acc = ef15.zero
                        for coeff, pb in zip((c0, c1, c2, c3, c4), powers_beta):
                            if coeff:
                                acc = ef15.add(acc, ef15.scale(coeff, pb))
                        F243.append(acc)
    F243_set = set(F243)
    assert len(F243_set) == 243

    for u in F243:
        assert ef15.frob(u, 5) == u
        if u != ef15.zero:
            assert ef15.inv(u) in F243_set
            sq15 = ef15.is_square(u)
            sq5 = ef15.pow(u, (3 ** 5 - 1) // 2) == ef15.one
            assert sq15 == sq5
            if sq15:
                rt = ef15.pow(u, (3 ** 5 + 1) // 4)
                assert ef15.sq(rt) == u and rt in F243_set
    for _ in range(200):
        u = rng.choice(F243)
        v = rng.choice(F243)
        assert ef15.add(u, v) in F243_set and ef15.mul(u, v) in F243_set

    inv2_3 = 2
    for b in [ef15.one, ef15.from_int(2), beta, ef15.add(ef15.one, beta)]:
        half_b = ef15.scale(inv2_3, b)
        delta = ef15.sub(ef15.sq(half_b), ef15.one)
        for x in F243:
            w0 = ef15.mul(delta, ef15.sq(x))
            assert w0 in F243_set
            if ef15.is_square(w0):
                rt = ef15.pow(w0, (3 ** 5 + 1) // 4)
                y1 = ef15.sub(rt, ef15.mul(half_b, x))
                y2 = ef15.sub(ef15.neg(rt), ef15.mul(half_b, x))
                assert y1 in F243_set and y2 in F243_set
        checked_out = 0
        while checked_out < 60:
            y_out = tuple(rng.randrange(3) for _ in range(15))
            if y_out in F243_set:
                continue
            x_in = rng.choice(F243)
            qval = ef15.add(ef15.add(ef15.sq(x_in), ef15.sq(y_out)), ef15.mul(b, ef15.mul(x_in, y_out)))
            assert qval not in F243_set
            checked_out += 1

    print("  [Suite 1] OK (9 explicit graphs + exact F_{3^5} < F_{3^{15}} closure verified)", flush=True)


# ---------------------------------------------------------------------------
# Suite 2: Part B — Even-n inequality, Lemma 2.1, and direct connectedness
# ---------------------------------------------------------------------------

def verify_part_b():
    print("[Suite 2] Part B: Even-n inequality, Lemma 2.1 & connectedness ...", flush=True)
    rng = random.Random(202606)

    # 1. Exact integer inequality 2(q^{2k} - 2q^{2k-1} + 2q^k) > q^{2k}
    for k in range(2, 21):
        for q in [5, 7, 9, 11, 13, 17, 19, 25]:
            lhs = 2 * (q ** (2 * k) - 2 * q ** (2 * k - 1) + 2 * q ** k)
            rhs = q ** (2 * k)
            assert lhs > rhs, f"Failed for k={k}, q={q}"

    # 2. Lemma 2.1 exact integer count of squares vs bound, and direct connectedness
    configs = [
        (3, 1, 4, 3, 5),   # F_{3^4}, s=3
        (5, 1, 4, 3, 5),   # F_{5^4}, s=3
        (3, 1, 6, 4, 5),   # F_{3^6}, s=4
        (3, 2, 4, 3, 1),   # F_{9^4} = F_{3^8}, s=3 (prime power q=9)
    ]

    for p, e, n_ext, s, n_sub in configs:
        q = p ** e
        j = n_ext - s
        n_total = e * n_ext
        ff = get_ff(p, n_total)

        if e == 1:
            fq_els = list(range(p))
        else:
            fq_exp = (ff.size - 1) // (q - 1)
            fq_els = [0] + [ff.pow_scalar(ff.prim, k * fq_exp) for k in range(q - 1)]

        def fq_span(basis):
            els = [0]
            seen = {0}
            for v in basis:
                v = int(v)
                if v in seen:
                    continue
                new_els = list(els)
                for c in fq_els:
                    if c == 0:
                        continue
                    cv = ff.mul_scalar(c, v)
                    for el in els:
                        ns = ff.add_scalar(el, cv)
                        new_els.append(ns)
                        seen.add(ns)
                els = new_els
            return np.array(els, dtype=np.int32)

        def random_fq_subspace(dim):
            basis = []
            seen = {0}
            els = [0]
            while len(basis) < dim:
                v = rng.randrange(1, ff.size)
                if v not in seen:
                    basis.append(v)
                    new_els = list(els)
                    for c in fq_els:
                        if c == 0:
                            continue
                        cv = ff.mul_scalar(c, v)
                        for el in els:
                            ns = ff.add_scalar(el, cv)
                            new_els.append(ns)
                            seen.add(ns)
                    els = new_els
            return np.array(els, dtype=np.int32)

        V_list = [fq_span([ff.pow_scalar(ff.prim, r) for r in range(s)])]
        for _ in range(n_sub - 1):
            V_list.append(random_fq_subspace(s))

        mult = np.zeros(ff.size, dtype=np.int32)
        for z in range(ff.size):
            mult[int(ff.sq_tbl[z])] += 1

        qj = q ** j
        rhs_sq = ((qj - 1) ** 2) * (q ** n_ext)
        for V_arr in V_list[:2]:
            for a in [0, 1, ff.prim, rng.randrange(1, ff.size)]:
                shifted = [ff.add_scalar(a, int(v)) for v in V_arr]
                S_sum = sum(ff.quad_char(w) for w in shifted)
                N_sq = sum(int(mult[w]) for w in shifted)
                assert N_sq == (q ** (n_ext - j)) + S_sum
                assert (qj * S_sum) ** 2 <= rhs_sq, f"Lemma 2.1 failed: S={S_sum}"
                if N_sq < (q ** (n_ext - j)):
                    deficit = (q ** (n_ext - j)) - N_sq
                    assert (qj * deficit) ** 2 <= rhs_sq

        b_cands = [2 % p, (p - 2) % p, 1, ff.prim, rng.randrange(1, ff.size)]
        if e > 1:
            b_cands = [2 % p]
        for V_arr in V_list:
            for b in b_cands:
                _, cnt = ff.bfs(b, V_arr, start=0)
                assert cnt == ff.size, f"Disconnected at q={q}, n={n_ext}, s={s}, b={b}, cnt={cnt}"

    print("  [Suite 2] OK (inequality, Lemma 2.1 square counts, & even-n connectedness verified)", flush=True)


# ---------------------------------------------------------------------------
# Suite 3: Part C — Odd-n, b = +-2 Kummer-Weil check
# ---------------------------------------------------------------------------

def poly_ext_mul(A, B, ef):
    """Multiply two polynomials over ExtField `ef` (low-deg first)."""
    if not A or not B:
        return []
    res = [ef.zero] * (len(A) + len(B) - 1)
    for i, ai in enumerate(A):
        if ai != ef.zero:
            for j, bj in enumerate(B):
                if bj != ef.zero:
                    res[i + j] = ef.add(res[i + j], ef.mul(ai, bj))
    return res


def verify_part_c():
    print("[Suite 3] Part C: Odd-n, b = +-2 Kummer-Weil & threshold check ...", flush=True)
    rng = random.Random(202607)

    # 1. Exact norm polynomial & Weil bound for (n=5, q=5), (n=5, q=7), (n=7, q=5), plus (n=7, q=11)
    test_specs = [(5, 5, 3), (5, 7, 3), (7, 5, 2), (7, 11, 1)]
    for n, q, n_planes in test_specs:
        ef = ExtField(q, n)
        planes = [(ef.x, ef.one), (ef.pow(ef.x, 3), ef.add(ef.one, ef.x))]
        while len(planes) < n_planes:
            v2 = tuple(rng.randrange(q) for _ in range(n))
            while v2 == ef.zero:
                v2 = tuple(rng.randrange(q) for _ in range(n))
            v1 = tuple(rng.randrange(q) for _ in range(n))
            while v1 == ef.zero or all(ef.scale(c, v2) == v1 for c in range(q)):
                v1 = tuple(rng.randrange(q) for _ in range(n))
            planes.append((v1, v2))

        for v1, v2 in planes[:n_planes]:
            a = ef.div(v1, v2)
            assert a[1:] != (0,) * (n - 1)
            conjs = [ef.frob(a, i) for i in range(n)]
            assert len(set(conjs)) == n, "Conjugates not distinct"

            nv2 = ef.one
            cur_v2 = v2
            for _ in range(n):
                nv2 = ef.mul(nv2, cur_v2)
                cur_v2 = ef.frob(cur_v2, 1)
            assert nv2[1:] == (0,) * (n - 1) and nv2[0] != 0
            nv2_scalar = nv2[0]

            f_ext = [ef.from_int(nv2_scalar)]
            for ai in conjs:
                f_ext = poly_ext_mul(f_ext, [ai, ef.one], ef)
            assert len(f_ext) == n + 1
            f_fq = []
            for coeff in f_ext:
                assert coeff[1:] == (0,) * (n - 1), "Norm polynomial coefficient not in F_q!"
                f_fq.append(coeff[0])
            f_fq = tuple(f_fq)
            assert len(f_fq) == n + 1 and f_fq[-1] != 0

            df = poly_deriv(f_fq, q)
            assert poly_gcd(f_fq, df, q) == (1,), "Norm polynomial not squarefree!"

            W = 0
            curve_pts = 0
            for t in range(q):
                val = 0
                for c in reversed(f_fq):
                    val = (val * t + c) % q
                if val == 0:
                    eta_fq = 0
                else:
                    eta_fq = 1 if pow(val, (q - 1) // 2, q) == 1 else -1
                W += eta_fq

                vt = ef.add(v1, ef.scale(t, v2))
                eta_ext = ef.quad_char(vt)
                assert eta_ext == eta_fq
                curve_pts += 1 + eta_ext

            assert curve_pts == q + W
            assert W * W <= ((n - 1) ** 2) * q, f"Weil bound violated: W={W}"

            if q + 1 >= n:
                sv_rows = []
                # Pick one representative per projective line (v1 + t*v2) and v2
                line_reps = [v2] + [ef.add(v1, ef.scale(t, v2)) for t in range(q)]
                for rep in line_reps:
                    # Multiply by a nonsquare in F_q if needed so we test squareness of the line
                    if ef.is_square(rep):
                        sv_rows.append(list(ef.sqrt(rep)))
                    else:
                        # If q % 4 == 1, -1 is square so whole line might be nonsquares; scale by quadratic nonresidue in F_q
                        for c in range(2, q):
                            if pow(c, (q - 1) // 2, q) != 1:
                                scaled = ef.scale(c, rep)
                                if ef.is_square(scaled):
                                    sv_rows.append(list(ef.sqrt(scaled)))
                                break
                rk = rank_mod_p(sv_rows, n, q)
                assert rk == n, f"Expected span(S_V) = F_{{{q}^{n}}}, got dim {rk}"

    # Direct FastFF connectedness check for (n=5, q=5) and (n=5, q=7) at b = +-2
    for q in (5, 7):
        ff = get_ff(q, 5)
        V_list = [
            ff.span_from_basis([1, ff.prim]),
            ff.span_from_basis([1, ff.pow_scalar(ff.prim, 3)]),
        ]
        tr0 = [x for x in range(1, ff.size) if ff.tr_tbl[x] == 0]
        v1 = tr0[0]
        v2 = next(x for x in tr0 if x not in set(ff.span_from_basis([v1])))
        V_list.append(ff.span_from_basis([v1, v2]))
        for _ in range(3):
            Vr, _ = ff.random_subspace(2, rng)
            V_list.append(Vr)
        for V_arr in V_list:
            for b in (2 % q, (q - 2) % q):
                _, cnt = ff.bfs(b, V_arr, start=0)
                assert cnt == ff.size, f"Disconnected at n=5, q={q}, b={b}"

    # 2. Part C threshold implication for all odd n in [5, 25]
    for n in range(5, 26, 2):
        m = (n - 1) // 2
        q_thresh = (n - 1 + (1 << m)) ** 2 + 1
        assert q_thresh > (1 << (n - 1))
        assert (q_thresh - (1 << (n - 1))) ** 2 > ((n - 1) ** 2) * q_thresh
        assert q_thresh > divisor_count(n)

    print("  [Suite 3] OK (Kummer-Weil norm polys, Weil bound, S_V span, connectedness, & n<=25 thresholds verified)", flush=True)


# ---------------------------------------------------------------------------
# Suite 4: Part D.1-D.2 — Non-proportionality of L_i & reflection invariance
# ---------------------------------------------------------------------------

def verify_part_d1_d2():
    print("[Suite 4] Part D.1-D.2: Non-proportionality of L_i & reflection tau_i ...", flush=True)
    rng = random.Random(202608)

    for n, p in [(5, 5), (7, 3), (9, 3)]:
        p0 = smallest_prime_factor(n)
        s = n // p0 + 1
        ff = get_ff(p, n)

        bases = [[ff.pow_scalar(ff.prim, r) for r in range(s)]]
        tr0 = [x for x in range(1, ff.size) if ff.tr_tbl[x] == 0]
        b_tr = []
        sp_tr = {0}
        for x in tr0:
            if x not in sp_tr:
                b_tr.append(x)
                sp_tr = set(int(v) for v in ff.span_from_basis(b_tr))
                if len(b_tr) == s:
                    break
        bases.append(b_tr)
        if n == 9 and p == 3:
            sub_exp = (ff.size - 1) // (3 ** 3 - 1)
            F27 = [0] + [ff.pow_scalar(ff.prim, k * sub_exp) for k in range(26)]
            F27_basis = []
            sp27 = {0}
            for x in F27:
                if x not in sp27:
                    F27_basis.append(x)
                    sp27 = set(int(v) for v in ff.span_from_basis(F27_basis))
                    if len(F27_basis) == 3:
                        break
            gamma = next(x for x in range(1, ff.size) if x not in sp27)
            bases.append(F27_basis + [gamma])
        for _ in range(2):
            _, rb = ff.random_subspace(s, rng)
            bases.append(rb)

        for basis in bases:
            assert len(basis) == s
            M = [[0] * s for _ in range(n)]
            for r, v in enumerate(basis):
                cur = int(v)
                for i in range(n):
                    M[i][r] = cur
                    cur = int(ff.frob_tbl[cur])
            assert rank_over_ff(ff, M, s) == s, "M failed to have rank s"
            for i in range(n):
                for j in range(i + 1, n):
                    assert rank_over_ff(ff, [M[i], M[j]], s) == 2, f"Rows ({i},{j}) proportional!"

    # D.2: Symbolic exact verification (no `/` operator, exact Rational only)
    x_i, y_i, b_i = sp.symbols("x_i y_i b_i")
    half = sp.Rational(1, 2)
    quarter = sp.Rational(1, 4)
    Delta_i = b_i ** 2 * quarter - 1
    Q_b = x_i ** 2 + b_i * x_i * y_i + y_i ** 2
    u_i = y_i + half * b_i * x_i
    a_i = 2 * x_i + b_i * y_i
    c_i = b_i * x_i + 2 * y_i

    y_tau = -b_i * x_i - y_i
    y_tau2 = -b_i * x_i - y_tau
    assert sp.simplify(y_tau2 - y_i) == 0, "tau_i not an involution"

    Q_b_tau = x_i ** 2 + b_i * x_i * y_tau + y_tau ** 2
    assert sp.simplify(Q_b_tau - Q_b) == 0, "tau_i does not preserve Q_b"

    u_tau = y_tau + half * b_i * x_i
    assert sp.simplify(u_tau + u_i) == 0, "tau_i(u_i) != -u_i"
    assert sp.simplify(a_i - (b_i * u_i - 2 * Delta_i * x_i)) == 0
    assert sp.simplify(c_i - 2 * u_i) == 0

    a_tau = 2 * x_i + b_i * y_tau
    assert sp.simplify((a_i - a_tau) - 2 * b_i * u_i) == 0
    lhs_inv = sp.Pow(a_i, -1) - sp.Pow(a_tau, -1)
    rhs_inv = -2 * b_i * u_i * sp.Pow(a_i * a_tau, -1)
    assert sp.simplify(sp.together(lhs_inv - rhs_inv)) == 0

    ff55 = get_ff(5, 5)
    inv2_5 = 3
    for _ in range(20):
        b_val = rng.randrange(1, ff55.size)
        while b_val in (2, 3):
            b_val = rng.randrange(1, ff55.size)
        x_val = rng.randrange(1, ff55.size)
        y_val = rng.randrange(1, ff55.size)
        half_b = ff55.mul_scalar(b_val, inv2_5)
        u_val = ff55.add_scalar(y_val, ff55.mul_scalar(half_b, x_val))
        if u_val == 0:
            continue
        y_refl = ff55.add_scalar(int(ff55.neg_tbl[ff55.mul_scalar(b_val, x_val)]), int(ff55.neg_tbl[y_val]))
        y_refl2 = ff55.add_scalar(int(ff55.neg_tbl[ff55.mul_scalar(b_val, x_val)]), int(ff55.neg_tbl[y_refl]))
        assert y_refl2 == y_val
        assert ff55.qb(b_val, x_val, y_refl) == ff55.qb(b_val, x_val, y_val)
        a_val = ff55.add_scalar(ff55.mul_scalar(2, x_val), ff55.mul_scalar(b_val, y_val))
        a_refl = ff55.add_scalar(ff55.mul_scalar(2, x_val), ff55.mul_scalar(b_val, y_refl))
        diff = ff55.add_scalar(a_val, int(ff55.neg_tbl[a_refl]))
        expected = ff55.mul_scalar(2, ff55.mul_scalar(b_val, u_val))
        assert diff == expected and diff != 0

    print("  [Suite 4] OK (L_i non-proportionality & symbolic/FF tau_i identities verified)", flush=True)


# ---------------------------------------------------------------------------
# Suite 5: Part D.3 — Exact Jacobian rank growth dim U_j >= min(n, s + j - 1)
# ---------------------------------------------------------------------------

def verify_part_d3():
    print("[Suite 5] Part D.3: Exact Jacobian rank growth dim U_j ...", flush=True)
    p = 1000003
    assert p % 4 == 3
    inv2 = (p + 1) // 2
    inv4 = (p + 1) // 4
    exp_euler = (p - 1) // 2
    exp_sqrt = (p + 1) // 4
    rng = random.Random(202609)

    for n, s in [(5, 2), (7, 2), (9, 4), (11, 2)]:
        k0 = n - s + 1
        b = [(3 + i) % p for i in range(n)]
        for bi in b:
            assert bi not in (0, 2, p - 2)
        half_b = [(bi * inv2) % p for bi in b]
        Delta = [(bi * bi * inv4 - 1) % p for bi in b]

        M = [[pow(i + 1, r, p) for r in range(s)] for i in range(n)]
        assert rank_mod_p(M, s, p) == s
        for i in range(n):
            for j in range(i + 1, n):
                assert rank_mod_p([M[i], M[j]], s, p) == 2

        V_basis = [[M[i][r] for i in range(n)] for r in range(s)]
        x_cur = [(i + 1) % p for i in range(n)]
        U_basis = []
        x_walk = [x_cur]

        for j in range(1, k0 + 1):
            dx2 = [(Delta[i] * x_cur[i] * x_cur[i]) % p for i in range(n)]
            found = None
            for _ in range(100000):
                t_cand = [rng.randrange(p) for _ in range(s)]
                ok = True
                f_vals = [0] * n
                for i in range(n):
                    li = sum(M[i][r] * t_cand[r] for r in range(s)) % p
                    fv = (dx2[i] + li) % p
                    if fv == 0 or pow(fv, exp_euler, p) != 1:
                        ok = False
                        break
                    f_vals[i] = fv
                if ok:
                    found = (t_cand, f_vals)
                    break
            assert found is not None, f"Failed to find valid walk step at n={n}, s={s}, j={j}"
            t_j, f_vals = found
            u_j = [pow(fv, exp_sqrt, p) for fv in f_vals]
            x_next = [(u_j[i] - half_b[i] * x_cur[i]) % p for i in range(n)]

            for i in range(n):
                q_val = (x_cur[i] ** 2 + b[i] * x_cur[i] * x_next[i] + x_next[i] ** 2) % p
                l_val = sum(M[i][r] * t_j[r] for r in range(s)) % p
                assert q_val == l_val

            a_j = [(2 * x_cur[i] + b[i] * x_next[i]) % p for i in range(n)]
            c_j = [(b[i] * x_cur[i] + 2 * x_next[i]) % p for i in range(n)]
            for i in range(n):
                assert a_j[i] != 0 and c_j[i] != 0
            c_inv = [pow(ci, -1, p) for ci in c_j]

            gens = []
            for v in V_basis:
                gens.append([(c_inv[i] * v[i]) % p for i in range(n)])
            for u in U_basis:
                gens.append([(c_inv[i] * a_j[i] * u[i]) % p for i in range(n)])
            U_basis = rref_basis_mod_p(gens, n, p)
            dim_Uj = len(U_basis)
            if j == 1:
                assert dim_Uj == s
            expected_min = min(n, s + j - 1)
            assert dim_Uj >= expected_min, f"Rank growth failed at (n={n}, s={s}, j={j}): {dim_Uj} < {expected_min}"

            x_walk.append(x_next)
            x_cur = x_next

        assert len(U_basis) == n, f"Did not reach full rank n={n} at k0={k0}"

        if (n, s) == (5, 2):
            dx_basis = []
            for step_src in range(k0):
                for r_src in range(s):
                    cur_dx = [0] * n
                    for j in range(1, k0 + 1):
                        dt_vec = [1 if (j - 1 == step_src and r == r_src) else 0 for r in range(s)]
                        xp, xn = x_walk[j - 1], x_walk[j]
                        nxt_dx = [0] * n
                        for i in range(n):
                            a_ji = (2 * xp[i] + b[i] * xn[i]) % p
                            c_ji = (b[i] * xp[i] + 2 * xn[i]) % p
                            rhs = (sum(M[i][r] * dt_vec[r] for r in range(s)) - a_ji * cur_dx[i]) % p
                            nxt_dx[i] = (rhs * pow(c_ji, -1, p)) % p
                        cur_dx = nxt_dx
                    dx_basis.append(cur_dx)
            assert rank_mod_p(dx_basis, n, p) == n

    print("  [Suite 5] OK (Jacobian rank growth verified up to k0 = n-s+1 for (5,2),(7,2),(9,4),(11,2))", flush=True)


# ---------------------------------------------------------------------------
# Suite 6: Direct finite-field connectedness for odd n in {5, 7, 9}
# ---------------------------------------------------------------------------

def verify_suite_6():
    print("[Suite 6] Direct odd-n finite-field connectedness tests ...", flush=True)
    rng = random.Random(202610)

    # 1. (n=5, q=5, s=2) - 3125 vertices
    ff55 = get_ff(5, 5)
    tr0_55 = [x for x in range(1, ff55.size) if ff55.tr_tbl[x] == 0]
    v1_55 = tr0_55[0]
    v2_55 = next(x for x in tr0_55 if x not in set(ff55.span_from_basis([v1_55])))
    V_list_55 = [
        ff55.span_from_basis([1, ff55.prim]),
        ff55.span_from_basis([v1_55, v2_55]),
    ]
    for _ in range(3):
        Vr, _ = ff55.random_subspace(2, rng)
        V_list_55.append(Vr)
    b_list_55 = [2, 3, 1, ff55.prim, rng.randrange(5, ff55.size)]
    for V_arr in V_list_55:
        for b in b_list_55:
            _, cnt = ff55.bfs(b, V_arr, start=0)
            assert cnt == ff55.size, f"(5,5,2) disconnected at b={b}, cnt={cnt}"

    # 2. (n=7, q=3, s=3) - 2187 vertices
    ff37 = get_ff(3, 7)
    tr0_37 = [x for x in range(1, ff37.size) if ff37.tr_tbl[x] == 0]
    b_tr37 = []
    sp_tr37 = {0}
    for x in tr0_37:
        if x not in sp_tr37:
            b_tr37.append(x)
            sp_tr37 = set(int(v) for v in ff37.span_from_basis(b_tr37))
            if len(b_tr37) == 3:
                break
    V_list_37 = [
        ff37.span_from_basis([1, ff37.prim, ff37.pow_scalar(ff37.prim, 2)]),
        ff37.span_from_basis(b_tr37),
    ]
    for _ in range(3):
        Vr, _ = ff37.random_subspace(3, rng)
        V_list_37.append(Vr)
    for V_arr in V_list_37:
        for b in [2, 1, ff37.prim, rng.randrange(3, ff37.size)]:
            _, cnt = ff37.bfs(b, V_arr, start=0)
            assert cnt == ff37.size, f"(7,3,3) disconnected at b={b}, cnt={cnt}"

    # 3. (n=9, q=3, s=4) - 19683 vertices, including F_{27} + F_3 * gamma
    ff39 = get_ff(3, 9)
    sub_exp = (ff39.size - 1) // (3 ** 3 - 1)
    F27 = [0] + [ff39.pow_scalar(ff39.prim, k * sub_exp) for k in range(26)]
    F27_set = set(F27)
    F27_basis = []
    sp27 = {0}
    for x in F27:
        if x not in sp27:
            F27_basis.append(x)
            sp27 = set(int(v) for v in ff39.span_from_basis(F27_basis))
            if len(F27_basis) == 3:
                break
    gamma1 = next(x for x in range(1, ff39.size) if x not in F27_set)
    V_adv1 = ff39.span_from_basis(F27_basis + [gamma1])
    V_adv2 = ff39.span_from_basis(F27_basis + [ff39.prim])

    b_in_F27 = [2, next(x for x in F27 if x >= 3)]
    b_out_F27 = [ff39.prim, rng.randrange(1, ff39.size)]
    while b_out_F27[-1] in F27_set:
        b_out_F27[-1] = rng.randrange(1, ff39.size)
    for b in b_in_F27 + [b_out_F27[0]]:
        _, cnt = ff39.bfs(b, V_adv1, start=0)
        assert cnt == ff39.size, f"(9,3,4) F27+gamma1 disconnected at b={b}, cnt={cnt}"
    for b in [b_in_F27[1], b_out_F27[1]]:
        _, cnt = ff39.bfs(b, V_adv2, start=0)
        assert cnt == ff39.size, f"(9,3,4) F27+prim disconnected at b={b}, cnt={cnt}"

    Vr, _ = ff39.random_subspace(4, rng)
    for b in [2, rng.randrange(1, ff39.size)]:
        _, cnt = ff39.bfs(b, Vr, start=0)
        assert cnt == ff39.size, f"(9,3,4) random disconnected at b={b}, cnt={cnt}"

    print("  [Suite 6] OK ((5,5,2), (7,3,3), & (9,3,4) including F_{27}+F_3*gamma all connected)", flush=True)


def main():
    t_start_ns = time.monotonic_ns()
    try:
        verify_part_a()
        verify_part_b()
        verify_part_c()
        verify_part_d1_d2()
        verify_part_d3()
        verify_suite_6()
    except Exception as exc:
        print(f"Verification error: {exc}", file=sys.stderr, flush=True)
        print("FAIL", flush=True)
        sys.exit(1)
    elapsed_ms = (time.monotonic_ns() - t_start_ns) // 1000000
    print(f"All 6 suites completed in {elapsed_ms} ms (exact integer/FF arithmetic, 0 floats).", flush=True)
    print("PASS", flush=True)


if __name__ == "__main__":
    main()
