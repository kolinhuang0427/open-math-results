#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for Godard-Reis arXiv:2605.21866v1 Problem 3.

Built strictly from primary source definitions (godard-reis.tex) and targets/godard-2605.21866-prob3/PROOF.md
without reading verify.py or author notes. Pure integer/finite-field arithmetic (zero floats).
"""

from __future__ import annotations

from collections import deque
import math
import random
import sys


# --- Exact F_p[x] and F_{p^n} arithmetic ---

def poly_trim(a: list[int], p: int) -> list[int]:
    out = [c % p for c in a]
    while out and out[-1] == 0:
        out.pop()
    return out


def poly_add(a: list[int], b: list[int], p: int) -> list[int]:
    n = max(len(a), len(b))
    out = [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p for i in range(n)]
    return poly_trim(out, p)


def poly_sub(a: list[int], b: list[int], p: int) -> list[int]:
    n = max(len(a), len(b))
    out = [((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p for i in range(n)]
    return poly_trim(out, p)


def poly_mul(a: list[int], b: list[int], p: int) -> list[int]:
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] = (out[i + j] + ai * bj) % p
    return poly_trim(out, p)


def poly_mod(a: list[int], m: list[int], p: int) -> list[int]:
    r = list(a)
    dm = len(m) - 1
    lc_inv = pow(m[-1], -1, p)
    while len(r) - 1 >= dm and r:
        shift = len(r) - 1 - dm
        coef = (r[-1] * lc_inv) % p
        for i, mi in enumerate(m):
            r[shift + i] = (r[shift + i] - coef * mi) % p
        r = poly_trim(r, p)
    return r


def poly_gcd(a: list[int], b: list[int], p: int) -> list[int]:
    a = poly_trim(a, p)
    b = poly_trim(b, p)
    while b:
        a, b = b, poly_mod(a, b, p)
    if a:
        inv = pow(a[-1], -1, p)
        a = [(c * inv) % p for c in a]
    return a


def poly_powmod(base: list[int], exp: int, mod: list[int], p: int) -> list[int]:
    res = [1]
    b = poly_mod(base, mod, p)
    e = exp
    while e > 0:
        if e & 1:
            res = poly_mod(poly_mul(res, b, p), mod, p)
        b = poly_mod(poly_mul(b, b, p), mod, p)
        e >>= 1
    return res


def is_irreducible(f: list[int], p: int) -> bool:
    d = len(f) - 1
    if d <= 0:
        return False
    x = [0, 1]
    # Check x^{p^i} - x has gcd 1 with f for 1 <= i <= d // 2, and x^{p^d} == x mod f
    xp = list(x)
    for i in range(1, d + 1):
        xp = poly_powmod(xp, p, f, p)
        if i <= d // 2:
            g = poly_gcd(poly_sub(xp, x, p), f, p)
            if len(g) > 1:
                return False
    return xp == x


def find_irreducible(p: int, n: int) -> list[int]:
    # Deterministic sparse search: x^n + c*x + d or random
    for c in range(p):
        for d in range(1, p):
            cand = [0] * (n + 1)
            cand[0] = d
            cand[1] = (cand[1] + c) % p
            cand[n] = 1
            if is_irreducible(cand, p):
                return cand
    rng = random.Random(p * 100 + n)
    while True:
        cand = [rng.randrange(p) for _ in range(n)] + [1]
        if cand[0] != 0 and is_irreducible(cand, p):
            return cand


class GFpn:
    """Exact representation of F_{p^n} as F_p[x]/(mod_poly), elements packed as base-p ints."""

    def __init__(self, p: int, n: int):
        self.p = p
        self.n = n
        self.q_n = p ** n
        self.mod = find_irreducible(p, n)
        # Precompute multiplication table if q_n <= 20000? Even better: fast poly mul on tuples/ints.
        self._pows = [p ** i for i in range(n + 1)]
        # Precompute x^k mod self.mod for k = 0..2n-2
        self._x_pows: list[list[int]] = []
        cur = [1] + [0] * (n - 1)
        for _ in range(2 * n - 1):
            self._x_pows.append(cur)
            # multiply cur by x mod self.mod
            nxt = [0] + cur[:-1]
            top = cur[-1]
            if top:
                for i in range(n):
                    nxt[i] = (nxt[i] - top * self.mod[i]) % p
            cur = nxt

        # Precompute unpacked vectors if q_n <= 30000 for fast add/sub in BFS
        if self.q_n <= 30000:
            self._vecs = [tuple(self.unpack(x)) for x in range(self.q_n)]
        else:
            self._vecs = None

    def pack(self, coeffs: list[int]) -> int:
        res = 0
        for i in range(min(len(coeffs), self.n)):
            res += (coeffs[i] % self.p) * self._pows[i]
        return res

    def unpack(self, a: int) -> list[int]:
        out = [0] * self.n
        for i in range(self.n):
            a, out[i] = divmod(a, self.p)
        return out

    def add(self, a: int, b: int) -> int:
        if self._vecs is not None:
            ua, ub = self._vecs[a], self._vecs[b]
            p = self.p
            pows = self._pows
            res = 0
            for i in range(self.n):
                s = ua[i] + ub[i]
                if s >= p:
                    s -= p
                res += s * pows[i]
            return res
        ua, ub = self.unpack(a), self.unpack(b)
        return self.pack([(ua[i] + ub[i]) % self.p for i in range(self.n)])

    def sub(self, a: int, b: int) -> int:
        if self._vecs is not None:
            ua, ub = self._vecs[a], self._vecs[b]
            p = self.p
            pows = self._pows
            res = 0
            for i in range(self.n):
                s = ua[i] - ub[i]
                if s < 0:
                    s += p
                res += s * pows[i]
            return res
        ua, ub = self.unpack(a), self.unpack(b)
        return self.pack([(ua[i] - ub[i]) % self.p for i in range(self.n)])

    def neg(self, a: int) -> int:
        return self.sub(0, a)

    def mul(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        ua, ub = self.unpack(a), self.unpack(b)
        acc = [0] * self.n
        for i, ai in enumerate(ua):
            if ai:
                for j, bj in enumerate(ub):
                    if bj:
                        c = (ai * bj) % self.p
                        xp = self._x_pows[i + j]
                        for k in range(self.n):
                            if xp[k]:
                                acc[k] = (acc[k] + c * xp[k]) % self.p
        return self.pack(acc)

    def pow(self, a: int, e: int) -> int:
        res = 1
        base = a
        while e > 0:
            if e & 1:
                res = self.mul(res, base)
            base = self.mul(base, base)
            e >>= 1
        return res

    def inv(self, a: int) -> int:
        assert a != 0
        return self.pow(a, self.q_n - 2)

    def eta(self, a: int) -> int:
        if a == 0:
            return 0
        v = self.pow(a, (self.q_n - 1) // 2)
        return 1 if v == 1 else -1

    def Qb(self, b: int, x: int, y: int) -> int:
        xx = self.mul(x, x)
        yy = self.mul(y, y)
        xy = self.mul(x, y)
        return self.add(self.add(xx, self.mul(b, xy)), yy)

    def subspace_set(self, basis: list[int]) -> set[int]:
        res = {0}
        for vec in basis:
            new_elts = set()
            for s in res:
                cur = s
                for c in range(self.p):
                    if c > 0:
                        cur = self.add(cur, vec)
                    new_elts.add(cur)
            res = new_elts
        return res

    def primitive_element(self) -> int:
        # Find multiplicative generator of F_{p^n}^*
        order = self.q_n - 1
        factors = []
        tmp = order
        d = 2
        while d * d <= tmp:
            if tmp % d == 0:
                factors.append(d)
                while tmp % d == 0:
                    tmp //= d
            d += 1
        if tmp > 1:
            factors.append(tmp)
        for cand in range(2, self.q_n):
            if all(self.pow(cand, order // pf) != 1 for pf in factors):
                return cand
        raise AssertionError("No primitive element")

    def is_connected(self, b: int, V_set: set[int]) -> bool:
        """Exact BFS connectedness check on Gamma(Q_b, V)."""
        # Build neighbor map or compute Q_b(x, y) in V?
        # Faster: for each x, y = w - (b/2)*x where w^2 in ((b^2/4 - 1)*x^2) + V!
        # Precompute square roots dict: sq_roots[val] = list of z with z^2 == val!
        sq_roots: dict[int, list[int]] = {}
        for z in range(self.q_n):
            sq_roots.setdefault(self.mul(z, z), []).append(z)
        inv2 = pow(2, -1, self.p)
        b_half = self.mul(b, inv2)
        delta = self.sub(self.mul(b_half, b_half), 1)
        V_list = list(V_set)

        seen = bytearray(self.q_n)
        seen[0] = 1
        q = deque([0])
        count = 1
        while q:
            x = q.popleft()
            ax = self.mul(delta, self.mul(x, x))
            bx2 = self.mul(b_half, x)
            for v in V_list:
                rhs = self.add(ax, v)
                for w in sq_roots.get(rhs, ()):
                    y = self.sub(w, bx2)
                    if not seen[y]:
                        seen[y] = 1
                        count += 1
                        q.append(y)
                        if count == self.q_n:
                            return True
        return count == self.q_n


def rank_mod_p(mat: list[list[int]], p: int) -> int:
    rows = len(mat)
    cols = len(mat[0]) if rows else 0
    A = [[x % p for x in row] for row in mat]
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], -1, p)
        for j in range(c, cols):
            A[r][j] = (A[r][j] * inv) % p
        for i in range(rows):
            if i != r and A[i][c] != 0:
                fac = A[i][c]
                for j in range(c, cols):
                    A[i][j] = (A[i][j] - fac * A[r][j]) % p
        r += 1
    return r


def rank_over_field(mat: list[list[int]], F: GFpn) -> int:
    rows = len(mat)
    cols = len(mat[0]) if rows else 0
    A = [list(row) for row in mat]
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = F.inv(A[r][c])
        for j in range(c, cols):
            A[r][j] = F.mul(A[r][j], inv)
        for i in range(rows):
            if i != r and A[i][c] != 0:
                fac = A[i][c]
                for j in range(c, cols):
                    A[i][j] = F.sub(A[i][j], F.mul(fac, A[r][j]))
        r += 1
    return r


def check_section1_lower_bound() -> None:
    print("Check 1: Section 1 lower bound disconnections...")
    # Even n: (n, p) in [(4, 3), (4, 5), (6, 3), (8, 3)]
    for n, p in [(4, 3), (4, 5), (6, 3), (8, 3)]:
        F = GFpn(p, n)
        k = n // 2
        g = F.primitive_element()
        # Subfield F_{p^k} generated by g^{(p^n - 1) // (p^k - 1)}
        step = (F.q_n - 1) // (p ** k - 1)
        sub_gen = F.pow(g, step)
        # Basis of F_{p^k} over F_p: 1, sub_gen, ..., sub_gen^{k-1}
        sub_basis = [F.pow(sub_gen, i) for i in range(k)]
        # Multiply by nonsquare g -> V = g * F_{p^k}
        V_basis = [F.mul(g, v) for v in sub_basis]
        V_set = F.subspace_set(V_basis)
        assert len(V_set) == p ** k
        for v in V_set:
            if v != 0:
                assert F.eta(v) == -1
        for b in (1, 2, g):
            assert not F.is_connected(b, V_set), f"Expected disconnected at even (n={n}, p={p})"

    # Odd n: (n, p) in [(5, 3), (5, 5), (7, 3), (9, 3), (15, 3)]
    for n, p in [(5, 3), (5, 5), (7, 3), (9, 3), (15, 3)]:
        # Smallest prime factor p0(n)
        p0 = next(d for d in range(2, n + 1) if n % d == 0)
        d0 = n // p0
        F = GFpn(p, n)
        g = F.primitive_element() if n <= 9 else None
        if n <= 9:
            step = (F.q_n - 1) // (p ** d0 - 1)
            sub_gen = F.pow(g, step)
            V_basis = [F.pow(sub_gen, i) for i in range(d0)]
            V_set = F.subspace_set(V_basis)
            assert len(V_set) == p ** d0
            for b in (1, 2 % p, sub_gen):
                assert not F.is_connected(b, V_set)
        else:
            # n=15, p=3, d0=5: test subfield closure directly on 500 elements of F_{3^5}
            # F_{3^5} = {x in F_{3^{15}} : x^{3^5} == x}
            rng = random.Random(1503)
            # Pick primitive/generator via x^((3^15-1)/(3^5-1))
            exp = (3 ** 15 - 1) // (3 ** 5 - 1)
            gen_sub = F.pow(2, exp)
            while F.pow(gen_sub, 3 ** 5 - 1) != 1 or gen_sub in (0, 1):
                gen_sub = F.pow(rng.randrange(2, F.q_n), exp)
            # Verify Frobenius Frob_5(x) = x^{3^5} == x on powers
            assert F.pow(gen_sub, 3 ** 5) == gen_sub
            # For x, b in F_{3^5}, if Q_b(x, y) in F_{3^5}, then (y + b/2 x)^2 in F_{3^5} => y in F_{3^5}
            inv2 = pow(2, -1, 3)
            for _ in range(20):
                x = F.pow(gen_sub, rng.randrange(1, 3 ** 5 - 1))
                b = F.pow(gen_sub, rng.randrange(1, 3 ** 5 - 1))
                y_sub = F.pow(gen_sub, rng.randrange(1, 3 ** 5 - 1))
                assert F.pow(F.Qb(b, x, y_sub), 3 ** 5) == F.Qb(b, x, y_sub)
                # Outside F_{3^5}, e.g. y_out = [0, 1] (degree > 1) if not in F_{3^5}
                y_out = F.pack([0, 1])
                if F.pow(y_out, 3 ** 5) != y_out:
                    assert F.pow(F.Qb(b, x, y_out), 3 ** 5) != F.Qb(b, x, y_out)
    print("  Section 1 lower bound checks passed.")


def check_section2_even_n() -> None:
    print("Check 2: Section 2 even-n inequality & BFS connectedness...")
    for k in range(2, 21):
        for q in (5, 7, 9, 11, 13, 17, 19, 25):
            # q^{2k} - 2 q^{2k-1} + 2 q^k > (1/2) q^{2k} <=> 2(q^{2k} - 2 q^{2k-1} + 2 q^k) > q^{2k}
            lhs = 2 * (q ** (2 * k) - 2 * q ** (2 * k - 1) + 2 * q ** k)
            assert lhs > q ** (2 * k)

    rng = random.Random(2026)
    for n, p in [(4, 5), (6, 3)]:
        F = GFpn(p, n)
        s = n // 2 + 1
        for trial in range(5):
            # Pick random s-dim subspace
            while True:
                basis = [rng.randrange(1, F.q_n) for _ in range(s)]
                V_set = F.subspace_set(basis)
                if len(V_set) == p ** s:
                    break
            for b in (1, 2, rng.randrange(1, F.q_n)):
                assert F.is_connected(b, V_set), f"Even (n={n},p={p}) disconnected on trial {trial}"
    print("  Section 2 even-n checks passed.")


def check_section3_b_pm2() -> None:
    print("Check 3: Section 3 odd-n b = +-2 Kummer-Weil checks & connectedness...")
    # Threshold inequality: q - (n-1)sqrt(q) > 2^{n-1} when q = floor((n - 1 + 2^{(n-1)/2})^2) + 1
    for n in range(5, 25, 2):
        # exact floor of (n - 1 + 2^{(n-1)/2})^2 = (n - 1 + 2^{(n-1)/2})^2 since (n-1)/2 is integer!
        half = (n - 1) // 2
        val = (n - 1 + (1 << half))
        q_thresh = val * val + 1
        assert q_thresh > (1 << (n - 1))
        assert (q_thresh - (1 << (n - 1))) ** 2 > (n - 1) ** 2 * q_thresh

    rng = random.Random(303)
    for n, p, trials in [(5, 5, 2), (5, 7, 1)]:
        F = GFpn(p, n)
        # Test random 2-planes V: verify primitive ratio, norm polynomial squarefree, Weil bound, span(S_V), connectedness
        for trial in range(trials):
            while True:
                v1 = rng.randrange(1, F.q_n)
                v2 = rng.randrange(1, F.q_n)
                V_set = F.subspace_set([v1, v2])
                if len(V_set) == p ** 2:
                    break
            # Check a = v1 / v2 has F_p(a) = F_{p^n} (since n=5 prime, just a not in F_p)
            a = F.mul(v1, F.inv(v2))
            assert F.pow(a, p) != a

            # Compute Weil sum sum_{t in F_p} eta(v1 + t*v2) and verify |sum|^2 <= (n-1)^2 * p
            wsum = sum(F.eta(F.add(v1, F.mul(t, v2))) for t in range(p))
            assert wsum * wsum <= ((n - 1) ** 2) * p

            # Check span(S_V) == F_{p^n}
            S_V = [z for z in range(F.q_n) if F.mul(z, z) in V_set]
            # Compute F_p-rank of S_V vectors
            mat = [F.unpack(z) for z in S_V]
            assert rank_mod_p(mat, p) == n, f"span(S_V) != F_{p}^{n}"
            assert F.is_connected(2, V_set)
            assert F.is_connected(p - 2, V_set)
    print("  Section 3 b = +-2 checks passed.")


def check_section4_algebra_and_bfs() -> None:
    print("Check 4: Section 4 Lemma 4.1, tau_i, Lemma 4.3 Jacobian rank growth, & BFS...")
    rng = random.Random(404)

    # Lemma 4.1: pairwise linear independence of rows M_{i, r} = sigma_i(v_r) over F_{p^n}
    for n, p in [(5, 5), (7, 3), (9, 3)]:
        p0 = next(d for d in range(2, n + 1) if n % d == 0)
        s = n // p0 + 1
        F = GFpn(p, n)
        for _ in range(3):
            while True:
                basis = [rng.randrange(1, F.q_n) for _ in range(s)]
                if len(F.subspace_set(basis)) == p ** s:
                    break
            M = [[F.pow(v_r, p ** i) for v_r in basis] for i in range(n)]
            assert rank_over_field(M, F) == s
            for i in range(n):
                for j in range(i + 1, n):
                    assert rank_over_field([M[i], M[j]], F) == 2

    # Lemma 4.3(1) Jacobian rank growth over large prime field F_P
    P = 1000003
    inv2_P = pow(2, -1, P)
    for n, p0 in [(5, 5), (7, 7), (9, 3)]:
        s = n // p0 + 1
        k0 = n - s + 1
        # Construct generic b with b_i not in {0, 2, -2} and M in U_{s,n}(F_P)
        b = [3 + 2 * i for i in range(n)]
        delta = [((bi * bi * inv2_P * inv2_P) - 1) % P for bi in b]
        assert all(d != 0 for d in delta)
        M = [[pow(i + 1, r + 1, P) for r in range(s)] for i in range(n)]  # Vandermonde-like, pairwise indep
        assert rank_mod_p(M, P) == s
        for i in range(n):
            for j in range(i + 1, n):
                assert rank_mod_p([M[i], M[j]], P) == 2

        # Trace an explicit walk x_0, x_1, ..., x_{k0} and track U_j subset F_P^n (as n x dim basis matrix)
        x_prev = [i + 1 for i in range(n)]
        U_cols: list[list[int]] = []  # columns are basis vectors in F_P^n
        for j in range(1, k0 + 1):
            # Pick generic t^{(j)} in F_P^s such that delta_i * x_{j-1,i}^2 + L_i(t) is a nonzero square in F_P
            while True:
                t_vec = [rng.randrange(1, P) for _ in range(s)]
                L_t = [sum(M[i][r] * t_vec[r] for r in range(s)) % P for i in range(n)]
                f_vals = [(delta[i] * x_prev[i] * x_prev[i] + L_t[i]) % P for i in range(n)]
                if all(fv != 0 and pow(fv, (P - 1) // 2, P) == 1 for fv in f_vals):
                    break
            # Compute Tonelli-Shanks / sqrt since P = 1000003 == 3 (mod 4)!
            assert P % 4 == 3
            u_vals = [pow(fv, (P + 1) // 4, P) for fv in f_vals]
            for i in range(n):
                assert (u_vals[i] * u_vals[i]) % P == f_vals[i]
            x_cur = [(u_vals[i] - b[i] * inv2_P * x_prev[i]) % P for i in range(n)]

            # Check tau_i identity: a_{j,i} - tau_i(a_{j,i}) = 2 * b_i * u_{j,i} != 0
            a_diag = [(2 * x_prev[i] + b[i] * x_cur[i]) % P for i in range(n)]
            c_diag = [(b[i] * x_prev[i] + 2 * x_cur[i]) % P for i in range(n)]
            for i in range(n):
                assert c_diag[i] == (2 * u_vals[i]) % P and c_diag[i] != 0
                assert a_diag[i] == (b[i] * u_vals[i] - 2 * delta[i] * x_prev[i]) % P and a_diag[i] != 0
                tau_a = (-b[i] * u_vals[i] - 2 * delta[i] * x_prev[i]) % P
                assert (a_diag[i] - tau_a) % P == (2 * b[i] * u_vals[i]) % P

            # U_j = D(c_j)^{-1} (V + D(a_j) U_{j-1})
            c_inv = [pow(ci, -1, P) for ci in c_diag]
            gen_cols = [[(c_inv[i] * M[i][r]) % P for i in range(n)] for r in range(s)]
            for col in U_cols:
                gen_cols.append([(c_inv[i] * a_diag[i] * col[i]) % P for i in range(n)])
            # Transpose to check rank
            rk = rank_mod_p([[gen_cols[col_idx][i] for col_idx in range(len(gen_cols))] for i in range(n)], P)
            assert rk >= min(n, s + j - 1), f"Jacobian rank too small at n={n}, j={j}: {rk}"
            U_cols = gen_cols
            x_prev = x_cur
        # At j = k0, rk must equal n!
        rk_final = rank_mod_p([[U_cols[c][i] for c in range(len(U_cols))] for i in range(n)], P)
        assert rk_final == n
        print(f"  Jacobian rank growth verified for (n={n}, s={s}): reached dim {rk_final} at k0={k0}.")

    # Direct finite-field BFS connectedness for odd n=5 (q=5, s=2) and n=7 (q=3, s=3)
    F55 = GFpn(5, 5)
    for trial in range(3):
        while True:
            basis = [rng.randrange(1, F55.q_n) for _ in range(2)]
            V_set = F55.subspace_set(basis)
            if len(V_set) == 25:
                break
        for b in (1, 3, rng.randrange(4, F55.q_n)):
            assert F55.is_connected(b, V_set)

    F37 = GFpn(3, 7)
    for trial in range(3):
        while True:
            basis = [rng.randrange(1, F37.q_n) for _ in range(3)]
            V_set = F37.subspace_set(basis)
            if len(V_set) == 27:
                break
        assert F37.is_connected(rng.randrange(3, F37.q_n), V_set)
    print("  Section 4 BFS connectedness for (5,5,2) and (7,3,3) passed.")


def run_all_checks() -> None:
    check_section1_lower_bound()
    check_section2_even_n()
    check_section3_b_pm2()
    check_section4_algebra_and_bfs()
    print("PASS")


if __name__ == "__main__":
    try:
        run_all_checks()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
