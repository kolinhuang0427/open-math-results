#!/usr/bin/env python3
"""Exact finite-field verification script for PROOF.md of targets/yip-2309.10950-rem3.1/.

Verifies all finite calculations and key algebraic lemmas in PROOF.md using exact
polynomial arithmetic over F_p (no floating point):
1. Lemma 2.2 & Lemma 2.3 (H_k degree bound, exact evaluation, UFD circle recovery at q=25,
   and H_k == 0 on canonical cosets for r = 7, 9, 11).
2. Subcase 3A (affine lines L not containing 0: |L cap N_2| in {(r-1)/2, (r+1)/2} for r=5,7,9,11).
3. Subcase 3B(i) (c = 0 norm circles: max clique <= 4 for r in {3,5,7,9,11,13,17,19,25,27}).
4. Subcase 3B(ii) (Claim 2.4, identity (4), exact |C cap N_2| formulas for lambda == N(c)
   and lambda != N(c), and Hasse bound for r = 7, 9, 11, 13).
5. Subcase 3B(iii) (complete S(theta) tables and explicit non-edge witnesses for r = 7 and r = 9,
   including the coordinate-free beta^4 = -1, N(b_1 + b_2)^4 = -1 identity at r = 9).
6. Exhaustive check of the full conjecture at q = 49, 81, and max B != empty clique < sqrt(q)
   at q = 49, 81, 121, 169.

Prints PASS on complete success, FAIL otherwise.
"""
import signal
import sys


def _timeout_handler(signum, frame):
    print("FAIL: timeout exceeded")
    sys.exit(1)


signal.signal(signal.SIGALRM, _timeout_handler)
signal.alarm(60)


class FiniteField:
    """Exact finite field F_{p^d} = F_p[u]/(mod_poly), elements represented as ints in 0..q-1."""

    def __init__(self, p: int, mod_poly: tuple[int, ...]):
        self.p = p
        self.d = len(mod_poly) - 1
        self.q = p ** self.d
        assert mod_poly[-1] % p == 1
        self.mod = [c % p for c in mod_poly]
        # Precompute tuple <-> int maps
        self.to_tup = []
        self.to_int = {}
        for x in range(self.q):
            t = []
            v = x
            for _ in range(self.d):
                t.append(v % p)
                v //= p
            tt = tuple(t)
            self.to_tup.append(tt)
            self.to_int[tt] = x

        # Precompute add / neg / mul tables for small q <= 1000
        self.add_t = [[0] * self.q for _ in range(self.q)]
        self.neg_t = [0] * self.q
        for a in range(self.q):
            ta = self.to_tup[a]
            self.neg_t[a] = self.to_int[tuple((-c) % p for c in ta)]
            for b in range(self.q):
                tb = self.to_tup[b]
                self.add_t[a][b] = self.to_int[tuple((ta[i] + tb[i]) % p for i in range(self.d))]

        self.mul_t = [[0] * self.q for _ in range(self.q)]
        for a in range(self.q):
            ta = self.to_tup[a]
            for b in range(self.q):
                tb = self.to_tup[b]
                prod = [0] * (2 * self.d - 1)
                for i in range(self.d):
                    if ta[i]:
                        for j in range(self.d):
                            prod[i + j] = (prod[i + j] + ta[i] * tb[j]) % p
                for deg in range(2 * self.d - 2, self.d - 1, -1):
                    c = prod[deg] % p
                    if c:
                        shift = deg - self.d
                        for k in range(self.d + 1):
                            prod[shift + k] = (prod[shift + k] - c * self.mod[k]) % p
                self.mul_t[a][b] = self.to_int[tuple(prod[: self.d])]

        self.zero = 0
        self.one = 1
        # Inverses and primitive element
        self.inv_t = [0] * self.q
        for a in range(1, self.q):
            for b in range(1, self.q):
                if self.mul_t[a][b] == 1:
                    self.inv_t[a] = b
                    break
            assert self.inv_t[a] != 0

        # Find generator
        factors = []
        n = self.q - 1
        f = 2
        while f * f <= n:
            if n % f == 0:
                factors.append(f)
                while n % f == 0:
                    n //= f
            f += 1
        if n > 1:
            factors.append(n)
        self.gen = None
        for a in range(2, self.q):
            if all(self.pow(a, (self.q - 1) // pf) != 1 for pf in factors):
                self.gen = a
                break
        assert self.gen is not None

        # Squares S_2 and nonsquares N_2
        self.S2 = set()
        for a in range(1, self.q):
            self.S2.add(self.mul_t[a][a])
        assert len(self.S2) == (self.q - 1) // 2
        self.N2 = set(range(1, self.q)) - self.S2

        # Quadratic character
        self.chi = [0] * self.q
        for a in self.S2:
            self.chi[a] = 1
        for a in self.N2:
            self.chi[a] = -1

        # Subfield F_r if d is even
        assert self.d % 2 == 0
        self.r = p ** (self.d // 2)
        self.frob = [self.pow(a, self.r) for a in range(self.q)]
        self.norm = [self.mul_t[a][self.frob[a]] for a in range(self.q)]
        self.trace = [self.add_t[a][self.frob[a]] for a in range(self.q)]
        self.Fr = [a for a in range(self.q) if self.frob[a] == a]
        assert len(self.Fr) == self.r
        self.Fr_set = set(self.Fr)
        self.Fr_S2 = {self.mul_t[a][a] for a in self.Fr if a != 0}
        assert len(self.Fr_S2) == (self.r - 1) // 2
        self.Fr_chi = {}
        for a in self.Fr:
            if a == 0:
                self.Fr_chi[a] = 0
            elif a in self.Fr_S2:
                self.Fr_chi[a] = 1
            else:
                self.Fr_chi[a] = -1

    def add(self, a, b):
        return self.add_t[a][b]

    def sub(self, a, b):
        return self.add_t[a][self.neg_t[b]]

    def neg(self, a):
        return self.neg_t[a]

    def mul(self, a, b):
        return self.mul_t[a][b]

    def inv(self, a):
        assert a != 0
        return self.inv_t[a]

    def div(self, a, b):
        return self.mul_t[a][self.inv_t[b]]

    def pow(self, a, e):
        res = 1
        base = a
        while e > 0:
            if e & 1:
                res = self.mul_t[res][base]
            base = self.mul_t[base][base]
            e >>= 1
        return res

    def elem(self, coeffs):
        t = [0] * self.d
        for i, c in enumerate(coeffs):
            t[i] = c % self.p
        return self.to_int[tuple(t)]

    # Univariate polynomial helpers over F_q (ascending degree lists)
    def poly_trim(self, P):
        P = list(P)
        while P and P[-1] == 0:
            P.pop()
        return P

    def poly_add(self, A, B):
        n = max(len(A), len(B))
        R = [0] * n
        for i in range(len(A)):
            R[i] = self.add_t[R[i]][A[i]]
        for i in range(len(B)):
            R[i] = self.add_t[R[i]][B[i]]
        return self.poly_trim(R)

    def poly_mul(self, A, B):
        if not A or not B:
            return []
        R = [0] * (len(A) + len(B) - 1)
        for i, ai in enumerate(A):
            if ai:
                for j, bj in enumerate(B):
                    if bj:
                        R[i + j] = self.add_t[R[i + j]][self.mul_t[ai][bj]]
        return self.poly_trim(R)

    def poly_pow(self, A, e):
        res = [1]
        base = list(A)
        while e > 0:
            if e & 1:
                res = self.poly_mul(res, base)
            base = self.poly_mul(base, base)
            e >>= 1
        return res

    def poly_eval(self, P, x):
        res = 0
        for c in reversed(P):
            res = self.add_t[self.mul_t[res][x]][c]
        return res

    def poly_divmod(self, A, B):
        A = self.poly_trim(A)
        B = self.poly_trim(B)
        assert B
        db = len(B) - 1
        inv_lb = self.inv(B[-1])
        Q = [0] * max(0, len(A) - db)
        while len(A) >= len(B):
            deg = len(A) - 1
            coef = self.mul(A[-1], inv_lb)
            Q[deg - db] = coef
            shift = deg - db
            for i in range(len(B)):
                A[shift + i] = self.sub(A[shift + i], self.mul(coef, B[i]))
            A = self.poly_trim(A)
        return self.poly_trim(Q), A

    def poly_gcd(self, A, B):
        A = self.poly_trim(A)
        B = self.poly_trim(B)
        while B:
            _, R = self.poly_divmod(A, B)
            A, B = B, R
        if A:
            inv_la = self.inv(A[-1])
            A = [self.mul(c, inv_la) for c in A]
        return A


def max_clique_bitmask(adj: list[int]) -> int:
    """Exact maximum clique size via Bron-Kerbosch with Tomita pivoting."""
    best = 0

    def bk(r_size: int, P: int):
        nonlocal best
        if P == 0:
            if r_size > best:
                best = r_size
            return
        if r_size + P.bit_count() <= best:
            return
        # Pivot maximizing |P & adj[u]|
        best_u = -1
        best_deg = -1
        tmp = P
        while tmp:
            lsb = tmp & -tmp
            u = lsb.bit_length() - 1
            deg = (P & adj[u]).bit_count()
            if deg > best_deg:
                best_deg = deg
                best_u = u
            tmp ^= lsb
        cand = P & ~adj[best_u]
        while cand:
            lsb = cand & -cand
            v = lsb.bit_length() - 1
            bk(r_size + 1, P & adj[v])
            P ^= lsb
            cand ^= lsb

    bk(0, (1 << len(adj)) - 1)
    return best


def all_cliques_of_size_ge(adj: list[int], target: int) -> list[tuple[int, ...]]:
    """Enumerate all cliques of size >= target."""
    res = []

    def dfs(cur: list[int], P: int):
        if len(cur) >= target:
            res.append(tuple(cur))
        if len(cur) + P.bit_count() < target:
            return
        tmp = P
        while tmp:
            lsb = tmp & -tmp
            v = lsb.bit_length() - 1
            cur.append(v)
            dfs(cur, P & adj[v] & ~((1 << (v + 1)) - 1))
            cur.pop()
            tmp ^= lsb

    dfs([], (1 << len(adj)) - 1)
    return res


def gps_adj_on_subset(F: FiniteField, verts: list[int]) -> list[int]:
    n = len(verts)
    adj = [0] * n
    S2_0 = F.S2 | {0}
    for i in range(n):
        vi = verts[i]
        for j in range(i + 1, n):
            if F.add(vi, verts[j]) in S2_0:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    return adj


def verify_all():
    # Standard fields F_{r^2} for r = 3, 5, 7, 9, 11, 13, 17, 19, 25, 27
    fields = {
        3: FiniteField(3, (1, 0, 1)),             # F_9 = F_3[u]/(u^2 + 1)
        5: FiniteField(5, (3, 0, 1)),             # F_25 = F_5[u]/(u^2 - 2)
        7: FiniteField(7, (1, 0, 1)),             # F_49 = F_7[u]/(u^2 + 1)
        9: FiniteField(3, (2, 0, 0, 2, 1)),       # F_81 = F_3[u]/(u^4 + 2u^3 + 2)
        11: FiniteField(11, (1, 0, 1)),           # F_121 = F_11[u]/(u^2 + 1)
        13: FiniteField(13, (11, 0, 1)),          # F_169 = F_13[u]/(u^2 - 2)
        17: FiniteField(17, (14, 0, 1)),          # F_289 = F_17[u]/(u^2 - 3)
        19: FiniteField(19, (1, 0, 1)),           # F_361 = F_19[u]/(u^2 + 1)
        25: FiniteField(5, (2, 0, 4, 0, 1)),      # F_625 = F_5[u]/(u^4 - u^2 + 2)
        27: FiniteField(3, (2, 1, 0, 0, 0, 0, 1)),  # F_729 = F_3[u]/(u^6 + u + 2)
    }

    # Sanity-check Facts 1 & 2 on every field
    for r, F in fields.items():
        assert F.r == r
        assert F.neg(1) in F.S2 and F.add(1, 1) in F.S2
        for x in F.Fr:
            if x != 0:
                assert x in F.S2
        for x in range(F.q):
            assert F.chi[x] == F.Fr_chi[F.norm[x]]

    # 1. Verify Lemma 2.2 & Lemma 2.3 on q=25 non-coset clique & canonical cosets r=7,9,11
    F25 = fields[5]
    u = F25.elem([0, 1])
    A25 = [F25.elem([1, 0]), u, F25.elem([3, 1]), F25.elem([0, 4]), F25.elem([3, 4])]
    assert all(F25.add(a, b) in F25.S2 or F25.add(a, b) == 0 for i, a in enumerate(A25) for b in A25[i + 1:])
    c25 = {}
    for a in A25:
        prod = 1
        for x in A25:
            if x != a:
                prod = F25.mul(prod, F25.sub(a, x))
        c25[a] = F25.inv(prod)
    # Check Lagrange identity (1)
    for j in range(5):
        s = 0
        for a in A25:
            s = F25.add(s, F25.mul(c25[a], F25.pow(a, j)))
        assert s == (1 if j == 4 else 0)
    # Compute H_0, H_1
    H = []
    for k in range(2):
        P = []
        for a in A25:
            term = F25.poly_pow([F25.frob[a], 1], 3)
            coef = F25.mul(c25[a], F25.pow(a, k))
            term = [F25.mul(coef, t) for t in term]
            P = F25.poly_add(P, term)
        if k == 1:
            P = F25.poly_add(P, [F25.neg(1)])
        assert len(P) - 1 <= 2
        for b in A25:
            val = F25.poly_eval(P, F25.frob[b])
            if b in F25.S2:
                assert val == 0
            else:
                expected = F25.mul(F25.neg(F25.add(1, 1)), F25.mul(c25[b], F25.mul(F25.pow(F25.add(b, b), 3), F25.pow(b, k))))
                assert val == expected
        H.append(P)
    W = F25.poly_gcd(H[0], H[1])
    U, r0 = F25.poly_divmod(H[0], W)
    V, r1 = F25.poly_divmod(H[1], W)
    assert not r0 and not r1 and len(U) - 1 == 1 and len(V) - 1 == 1
    for b in A25:
        if b in F25.N2:
            assert F25.mul(b, F25.poly_eval(U, F25.frob[b])) == F25.poly_eval(V, F25.frob[b])
            assert F25.norm[F25.add(b, 1)] == F25.elem([4, 0])

    # Canonical cosets at r = 7, 9, 11 -> H_k == 0 identically
    for r in (7, 9, 11):
        F = fields[r]
        alpha = F.pow(F.gen, 2)
        A_can = [F.mul(alpha, x) for x in F.Fr]
        c_can = {}
        for a in A_can:
            prod = 1
            for x in A_can:
                if x != a:
                    prod = F.mul(prod, F.sub(a, x))
            c_can[a] = F.inv(prod)
        K = (r - 3) // 2
        for k in range(K + 1):
            P = []
            for a in A_can:
                term = F.poly_pow([F.frob[a], 1], (r + 1) // 2)
                coef = F.mul(c_can[a], F.pow(a, k))
                term = [F.mul(coef, t) for t in term]
                P = F.poly_add(P, term)
            if k == K:
                P = F.poly_add(P, [F.neg(1)])
            assert P == []

    # 2. Subcase 3A: affine lines L not containing 0 for r = 5, 7, 9, 11
    for r in (5, 7, 9, 11):
        F = fields[r]
        seen_lines = set()
        for eta in range(1, F.q):
            dir_coset = frozenset(F.mul(eta, t) for t in F.Fr)
            if dir_coset in seen_lines:
                continue
            seen_lines.add(dir_coset)
            expected_n2 = (r - 1) // 2 if eta in F.N2 else (r + 1) // 2
            visited = set(dir_coset)
            for z0 in range(F.q):
                if z0 in visited:
                    continue
                L = [F.add(z0, x) for x in dir_coset]
                visited.update(L)
                cnt_n2 = sum(1 for x in L if x in F.N2)
                assert cnt_n2 == expected_n2

    # 3. Subcase 3B(i): c = 0 norm circles have max clique <= 4
    for r, F in fields.items():
        for lam in F.Fr:
            if lam != 0 and lam not in F.Fr_S2:
                C = [b for b in range(1, F.q) if F.norm[b] == lam]
                assert len(C) == r + 1
                mc = max_clique_bitmask(gps_adj_on_subset(F, C))
                assert mc <= 4, f"c=0 failed at r={r}: mc={mc}"

    # 4. Subcase 3B(ii) & 3B(iii): Claim 2.4, (4), (5), (7), and exact r=7, 9 circle disposal
    for r in (7, 9, 11, 13):
        F = fields[r]
        four = F.add(F.add(1, 1), F.add(1, 1))
        # Check identity (4)
        for a in F.Fr:
            if a != 0:
                s4 = sum(F.Fr_chi[F.sub(F.mul(t, t), a)] for t in F.Fr)
                assert s4 == -1
        # Check Claim 2.4
        for mu in F.Fr:
            if mu == 0:
                continue
            counts = {t: 0 for t in F.Fr}
            for w in range(1, F.q):
                if F.norm[w] == mu:
                    counts[F.trace[w]] += 1
            for t in F.Fr:
                disc = F.sub(F.mul(t, t), F.mul(four, mu))
                assert counts[t] == 1 - F.Fr_chi[disc]

        # Check all circles c in {1, g}, lambda in F_r^*
        for c in (1, F.gen):
            nc = F.norm[c]
            for lam in F.Fr:
                if lam == 0:
                    continue
                C_n2 = [b for b in range(F.q) if F.norm[F.sub(b, c)] == lam and b in F.N2]
                if lam == nc:
                    expected = (r - F.Fr_chi[F.neg(nc)]) // 2
                    assert len(C_n2) == expected and len(C_n2) < r - 1
                else:
                    theta = F.div(lam, nc)
                    one_p_th = F.add(1, theta)
                    four_th = F.mul(four, theta)
                    S_th = sum(
                        F.Fr_chi[F.mul(F.add(one_p_th, tau), F.sub(F.mul(tau, tau), four_th))]
                        for tau in F.Fr
                    )
                    # Check Hasse bound: |S_th|^2 <= 4*r
                    assert S_th * S_th <= 4 * r
                    # Check symmetry S(theta) = chi(theta) * S(theta^{-1})
                    th_inv = F.inv(theta)
                    S_th_inv = sum(
                        F.Fr_chi[F.mul(F.add(F.add(1, th_inv), tau), F.sub(F.mul(tau, tau), F.mul(four, th_inv)))]
                        for tau in F.Fr
                    )
                    assert S_th == F.Fr_chi[theta] * S_th_inv
                    assert 2 * len(C_n2) == (r + 1) + F.Fr_chi[nc] * S_th
                    if r >= 11:
                        assert len(C_n2) < r - 1

    # Explicit r = 7 witnesses from PROOF.md
    F49 = fields[7]
    b1_49 = F49.elem([4, 1])
    b2_49 = F49.elem([2, 3])
    g_49 = F49.elem([2, 1])
    assert b1_49 != b2_49 and b1_49 in F49.N2 and b2_49 in F49.N2
    assert g_49 in F49.N2 and F49.norm[g_49] == F49.elem([5, 0])
    # Circle 1: c=1, lam=3
    assert F49.norm[F49.sub(b1_49, 1)] == F49.elem([3, 0])
    assert F49.norm[F49.sub(b2_49, 1)] == F49.elem([3, 0])
    # Circle 2: c=2+u, lam=4
    assert F49.norm[F49.sub(b1_49, g_49)] == F49.elem([4, 0])
    assert F49.norm[F49.sub(b2_49, g_49)] == F49.elem([4, 0])
    # Non-edge sum
    assert F49.add(b1_49, b2_49) == F49.elem([6, 4])
    assert F49.add(b1_49, b2_49) in F49.N2

    # Explicit r = 9 algebraic proof check (for ALL 8 elements z with z^10 = -1, z not in F_9)
    F81 = fields[9]
    minus1_81 = F81.neg(1)
    Z8 = [z for z in range(1, F81.q) if F81.pow(z, 10) == minus1_81 and z not in F81.Fr_set]
    assert len(Z8) == 8
    C81_n2 = {b for b in range(F81.q) if F81.norm[F81.sub(b, 1)] == minus1_81 and b in F81.N2}
    assert C81_n2 == {F81.add(1, z) for z in Z8}
    for z in Z8:
        z3 = F81.pow(z, 3)
        assert z3 in Z8 and z3 != z
        b1 = F81.add(1, z)
        b2 = F81.add(1, z3)
        assert b1 in C81_n2 and b2 in C81_n2 and b1 != b2
        beta = F81.sub(z, F81.inv(z))
        assert beta in F81.Fr_set and F81.pow(beta, 4) == minus1_81
        nb = F81.norm[F81.add(b1, b2)]
        rhs = F81.neg(F81.mul(beta, F81.add(F81.add(F81.mul(beta, beta), beta), 1)))
        assert nb == rhs
        assert F81.pow(nb, 4) == minus1_81
        assert F81.add(b1, b2) in F81.N2

    # 6. Exhaustive conjecture verification for q = 49, 81, plus B != empty check for q = 121, 169
    for r in (7, 9):
        F = fields[r]
        verts = list(range(F.q))
        adj = gps_adj_on_subset(F, verts)
        assert max_clique_bitmask(adj) == r
        cliques = all_cliques_of_size_ge(adj, r)
        canonical = {tuple(sorted(F.mul(alpha, x) for x in F.Fr)) for alpha in F.S2}
        assert len(canonical) == (r + 1) // 2
        assert set(cliques) == canonical

    for r in (11, 13):
        F = fields[r]
        b0 = F.gen
        nbrs = [x for x in range(1, F.q) if x != b0 and (F.add(x, b0) in F.S2 or F.add(x, b0) == 0)]
        mc_noncoset = 1 + max_clique_bitmask(gps_adj_on_subset(F, nbrs))
        assert mc_noncoset < r

    print("PASS")


if __name__ == "__main__":
    verify_all()
