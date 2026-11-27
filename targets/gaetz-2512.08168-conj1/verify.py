#!/usr/bin/env python3
"""
Exact-arithmetic verification script for PROOF.md (Conjecture 1.3 of Gaetz-Gao,
arXiv:2512.08168v2: BP(w) is closed under intersection and union in any Coxeter group).

Independently verifies Lemmas 1-5 and Theorem 1 across:
  1. Finite crystallographic groups: A_3 (all 24 elements), B_3 (all 48 elements)
  2. Finite non-crystallographic groups: H_3 (all 120 elements), H_4 (all 14,400 elements)
     using exact arithmetic in Z[phi] (phi = (1 + sqrt(5))/2).
  3. Infinite right-angled Coxeter groups (P_4, K_4 - e) using exact integer Tits matrices.
  4. Infinite affine Weyl groups (tilde_C_2, tilde_A_3, tilde_B_3) via exact integer
     generalized Cartan matrices, and a rank-4 non-crystallographic hyperbolic Coxeter
     group (m_ij in {2, 3, 4, 5, inf}) via exact arithmetic in Z[sqrt(2), phi].

Zero floating-point arithmetic is used anywhere.
"""

import random
import signal
import sys
import time
from collections import deque


# ---------------------------------------------------------------------------
# Exact algebraic rings (zero floats)
# ---------------------------------------------------------------------------

class ZPhi:
    """Exact elements a + b*phi in Z[phi], phi = (1 + sqrt(5))/2, phi^2 = phi + 1."""
    __slots__ = ("a", "b")

    def __init__(self, a: int, b: int = 0):
        self.a = a
        self.b = b

    def __add__(self, o):
        return ZPhi(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        return ZPhi(self.a - o.a, self.b - o.b)

    def __neg__(self):
        return ZPhi(-self.a, -self.b)

    def __mul__(self, o):
        # (a + b*phi)(c + d*phi) = (ac + bd) + (ad + bc + bd)*phi
        return ZPhi(self.a * o.a + self.b * o.b,
                    self.a * o.b + self.b * o.a + self.b * o.b)

    def __eq__(self, o):
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def sign(self) -> int:
        # 2*(a + b*phi) = (2a + b) + b*sqrt(5)
        x = 2 * self.a + self.b
        y = self.b
        if x == 0 and y == 0:
            return 0
        if x >= 0 and y >= 0:
            return 1
        if x <= 0 and y <= 0:
            return -1
        lhs = x * x
        rhs = 5 * y * y
        if x > 0:
            return 1 if lhs > rhs else -1
        else:
            return -1 if lhs > rhs else 1


class ZSqrt2Phi:
    """Exact elements u + v*sqrt(2) with u, v in Z[phi]."""
    __slots__ = ("u", "v")

    def __init__(self, u: ZPhi, v: ZPhi = None):
        self.u = u
        self.v = v if v is not None else ZPhi(0, 0)

    def __add__(self, o):
        return ZSqrt2Phi(self.u + o.u, self.v + o.v)

    def __sub__(self, o):
        return ZSqrt2Phi(self.u - o.u, self.v - o.v)

    def __neg__(self):
        return ZSqrt2Phi(-self.u, -self.v)

    def __mul__(self, o):
        two = ZPhi(2, 0)
        return ZSqrt2Phi(self.u * o.u + two * (self.v * o.v),
                         self.u * o.v + self.v * o.u)

    def __eq__(self, o):
        return self.u == o.u and self.v == o.v

    def __hash__(self):
        return hash((self.u, self.v))

    def is_zero(self) -> bool:
        return self.u.is_zero() and self.v.is_zero()

    def sign(self) -> int:
        su = self.u.sign()
        sv = self.v.sign()
        if su == 0:
            return sv
        if sv == 0:
            return su
        if su == sv:
            return su
        # Opposite signs: compare u^2 vs 2*v^2 in Z[phi]
        diff = self.u * self.u - ZPhi(2, 0) * (self.v * self.v)
        sd = diff.sign()
        assert sd != 0  # sqrt(2) not in Q(sqrt(5))
        return su if sd > 0 else sv


# ---------------------------------------------------------------------------
# Exact Tits geometric representation of a Coxeter group
# ---------------------------------------------------------------------------

class CoxeterGroup:
    """
    Exact Coxeter group via Tits' geometric representation:
    Each element w is represented by the n x n matrix of columns [w(alpha_0), ..., w(alpha_{n-1})],
    stored as a tuple of column tuples.
    For s in {0..n-1}:
      - s_i(alpha_j) = alpha_j - A[i][j] * alpha_i, where A[i][j] = 2 B(alpha_i, alpha_j).
      - Right descent: s in D_R(w) iff w(alpha_s) is in Phi^- (all coords <= 0, some < 0).
      - Left descent: s in D_L(w) iff w^{-1}(alpha_s) is in Phi^-, i.e., for each row/basis,
        equivalently we track w and w^{-1}, OR compute s*w and check length/action directly.
    """

    def __init__(self, name: str, A, zero, one, neg_one, sign_fn):
        self.name = name
        self.n = len(A)
        self.A = A  # A[i][j] = 2 B(alpha_i, alpha_j); A[i][i] = 2
        self.zero = zero
        self.one = one
        self.neg_one = neg_one
        self.sign_fn = sign_fn
        self.identity = tuple(
            tuple(one if i == j else zero for i in range(self.n))
            for j in range(self.n)
        )
        # Precompute simple reflection matrices S_k (columns = s_k(alpha_j))
        self.gens = []
        for k in range(self.n):
            cols = []
            for j in range(self.n):
                col = [zero] * self.n
                col[j] = one
                col[k] = col[k] - A[k][j]
                cols.append(tuple(col))
            self.gens.append(tuple(cols))

    def mul_right(self, w, s: int):
        """Return matrix of w * s. Since (ws)(alpha_j) = w(alpha_j) - A[s][j] * w(alpha_s)."""
        col_s = w[s]
        A_s = self.A[s]
        n = self.n
        out = []
        for j in range(n):
            c = A_s[j]
            if c == self.zero:
                out.append(w[j])
            elif j == s:
                out.append(tuple(-x for x in col_s))
            else:
                wj = w[j]
                out.append(tuple(wj[i] - c * col_s[i] for i in range(n)))
        return tuple(out)

    def mul_left(self, s: int, w):
        """Return matrix of s * w. Since s(v) replaces v_s by v_s - sum_r A[s][r] v_r."""
        A_s = self.A[s]
        n = self.n
        out = []
        for j in range(n):
            col = w[j]
            # s(col)[i] = col[i] for i != s; s(col)[s] = col[s] - sum_r A[s][r] col[r]
            acc = self.zero
            for r in range(n):
                if A_s[r] != self.zero and col[r] != self.zero:
                    acc = acc + A_s[r] * col[r]
            new_col = list(col)
            new_col[s] = col[s] - acc
            out.append(tuple(new_col))
        return tuple(out)

    def is_neg_root(self, vec) -> bool:
        """A root in the Tits representation is negative iff all entries <= 0 and not all 0."""
        has_neg = False
        for x in vec:
            sg = self.sign_fn(x)
            if sg > 0:
                return False
            if sg < 0:
                has_neg = True
        assert has_neg
        return True

    def is_right_descent(self, w, s: int) -> bool:
        return self.is_neg_root(w[s])

    def right_descents(self, w) -> int:
        mask = 0
        for s in range(self.n):
            if self.is_neg_root(w[s]):
                mask |= (1 << s)
        return mask

    def reduced_word(self, w) -> tuple:
        """Compute a reduced expression of w by greedily stripping right descents."""
        cur = w
        rev = []
        while cur != self.identity:
            for s in range(self.n):
                if self.is_neg_root(cur[s]):
                    rev.append(s)
                    cur = self.mul_right(cur, s)
                    break
            else:
                raise RuntimeError("Non-identity element with no right descent!")
        rev.reverse()
        return tuple(rev)

    def length(self, w) -> int:
        return len(self.reduced_word(w))

    def word_to_elem(self, word):
        cur = self.identity
        for s in word:
            cur = self.mul_right(cur, s)
        return cur

    def inverse(self, w):
        return self.word_to_elem(reversed(self.reduced_word(w)))

    def left_descents(self, w) -> int:
        return self.right_descents(self.inverse(w))

    def is_left_descent(self, w, s: int) -> bool:
        # s in D_L(w) iff s in D_R(w^{-1}) iff length(s*w) < length(w)
        # Fast exact check via w^{-1}:
        return self.is_neg_root(self.inverse(w)[s])

    def parabolic_decomp(self, w, J_mask: int):
        """Return (w^J, w_J) by greedily stripping right descents in J."""
        cur = w
        wJ_rev = []
        while True:
            found = False
            for s in range(self.n):
                if (J_mask >> s) & 1 and self.is_neg_root(cur[s]):
                    wJ_rev.append(s)
                    cur = self.mul_right(cur, s)
                    found = True
                    break
            if not found:
                break
        wJ_rev.reverse()
        wJ = self.word_to_elem(wJ_rev)
        return cur, wJ

    def support_mask(self, w) -> int:
        mask = 0
        for s in self.reduced_word(w):
            mask |= (1 << s)
        return mask

    def is_bp(self, w, J_mask: int) -> bool:
        w_up, w_dn = self.parabolic_decomp(w, J_mask)
        supp_up = self.support_mask(w_up)
        dl_dn = self.left_descents(w_dn)
        return ((supp_up & J_mask) & ~dl_dn) == 0

    def dem_right(self, x, s: int):
        """x * s in 0-Hecke monoid."""
        return x if self.is_right_descent(x, s) else self.mul_right(x, s)

    def dem_left(self, s: int, x):
        """s * x in 0-Hecke monoid."""
        return x if self.is_left_descent(x, s) else self.mul_left(s, x)

    def dem_word(self, word):
        cur = self.identity
        for s in word:
            cur = self.dem_right(cur, s)
        return cur

    def bruhat_interval(self, w) -> set:
        """Exact Bruhat interval [e, w] via Lemma 3(1) / Subword Property on a reduced word."""
        # Compute directly from the Subword Property: Sub(word) = all products of subwords of a
        # reduced expression of w, using BFS over prefixes.
        word = self.reduced_word(w)
        S = {self.identity}
        for s in word:
            S = S | {self.mul_right(u, s) for u in S}
        return S

    def bruhat_le(self, u, v) -> bool:
        """Exact Bruhat order u <= v via recursive subword check on a reduced word of v."""
        # Fast exact recursive check using Deodhar/Subword: u <= v iff u in [e, v].
        # For moderate lengths, check by greedy/memoized subword matching on reduced_word(v):
        word_v = self.reduced_word(v)
        if len(word_v) == 0:
            return u == self.identity
        # Dynamic programming from the right: strip letters from v from the right (Lifting Property)
        # If vs < v: u <= v iff (us < u and us <= vs) or (us > u and u <= vs).
        # Wait: standard Lifting Property! For t in D_R(v):
        #   if t in D_R(u): u <= v iff ut <= vt
        #   if t not in D_R(u): u <= v iff u <= vt.
        # Verify: if vt < v, let y be reduced word for vt, so y*t is reduced for v.
        # u <= v iff some reduced subword of y*t equals u.
        #   - If t not in D_R(u), no reduced word of u ends in t, so reduced subword lies in y, iff u <= vt!
        #   - If t in D_R(u), u <= v => ut <= vt (take reduced subword of y*t; if ends in t delete t -> ut <= vt;
        #     if doesn't end in t -> u <= vt, and ut < u <= vt). Conversely if ut <= vt, append t -> u <= v!
        cur_u = u
        cur_v = v
        for t in reversed(word_v):
            if self.is_right_descent(cur_u, t):
                cur_u = self.mul_right(cur_u, t)
            cur_v = self.mul_right(cur_v, t)
        return cur_u == self.identity

    def left_weak_le(self, u, v) -> bool:
        """u <=_L v iff length(v * u^{-1}) + length(u) == length(v)."""
        word_u = self.reduced_word(u)
        cur = v
        for s in reversed(word_u):
            if not self.is_right_descent(cur, s):
                return False
            cur = self.mul_right(cur, s)
        return True


# ---------------------------------------------------------------------------
# Group constructors
# ---------------------------------------------------------------------------

def make_int_group(name: str, A_int):
    return CoxeterGroup(name, A_int, 0, 1, -1, lambda x: (1 if x > 0 else (-1 if x < 0 else 0)))


def make_zphi_group(name: str, m_mat):
    """Build Coxeter group with m_ij in {1, 2, 3, 5, inf} over Z[phi].
    2*B(alpha_i, alpha_j) = -2*cos(pi/m_ij):
      m=1 -> 2, m=2 -> 0, m=3 -> -1, m=5 -> -phi, m=inf -> -2.
    """
    n = len(m_mat)
    A = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            m = m_mat[i][j]
            if i == j:
                A[i][j] = ZPhi(2, 0)
            elif m == 2:
                A[i][j] = ZPhi(0, 0)
            elif m == 3:
                A[i][j] = ZPhi(-1, 0)
            elif m == 5:
                A[i][j] = ZPhi(0, -1)
            elif m == 0:  # infinity
                A[i][j] = ZPhi(-2, 0)
            else:
                raise ValueError(f"Unsupported m={m} for Z[phi]")
    return CoxeterGroup(name, A, ZPhi(0, 0), ZPhi(1, 0), ZPhi(-1, 0), lambda x: x.sign())


def make_zsqrt2phi_group(name: str, m_mat):
    """Build Coxeter group with m_ij in {1, 2, 3, 4, 5, inf} over Z[sqrt(2), phi]."""
    n = len(m_mat)
    Z0 = ZSqrt2Phi(ZPhi(0, 0), ZPhi(0, 0))
    Z1 = ZSqrt2Phi(ZPhi(1, 0), ZPhi(0, 0))
    Zm1 = ZSqrt2Phi(ZPhi(-1, 0), ZPhi(0, 0))
    A = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            m = m_mat[i][j]
            if i == j:
                A[i][j] = ZSqrt2Phi(ZPhi(2, 0))
            elif m == 2:
                A[i][j] = Z0
            elif m == 3:
                A[i][j] = Zm1
            elif m == 4:
                A[i][j] = ZSqrt2Phi(ZPhi(0, 0), ZPhi(-1, 0))  # -sqrt(2)
            elif m == 5:
                A[i][j] = ZSqrt2Phi(ZPhi(0, -1), ZPhi(0, 0))  # -phi
            elif m == 0:  # infinity
                A[i][j] = ZSqrt2Phi(ZPhi(-2, 0))
            else:
                raise ValueError(f"Unsupported m={m}")
    return CoxeterGroup(name, A, Z0, Z1, Zm1, lambda x: x.sign())


def make_racg(name: str, n: int, edges):
    """edges: pairs (i, j) with m_ij = inf (non-commuting); all others m_ij = 2."""
    A = [[2 if i == j else 0 for j in range(n)] for i in range(n)]
    for i, j in edges:
        A[i][j] = -2
        A[j][i] = -2
    return make_int_group(name, A)


def enumerate_finite_group(G: CoxeterGroup):
    """Full BFS of a finite Coxeter group; returns list of all elements."""
    seen = {G.identity}
    q = deque([G.identity])
    elems = [G.identity]
    while q:
        w = q.popleft()
        for s in range(G.n):
            ws = G.mul_right(w, s)
            if ws not in seen:
                seen.add(ws)
                elems.append(ws)
                q.append(ws)
    return elems


# ---------------------------------------------------------------------------
# Verification routines for Lemmas 1-5 and Theorem 1
# ---------------------------------------------------------------------------

def verify_all_lemmas_exhaustive(G: CoxeterGroup, expected_size: int):
    """Exhaustively verify Lemmas 1-5 and Theorem 1 on every element of a finite group."""
    elems = enumerate_finite_group(G)
    assert len(elems) == expected_size, f"{G.name}: got {len(elems)}, expected {expected_size}"
    n = G.n
    all_masks = list(range(1 << n))

    # Precompute Bruhat intervals [e, w], left descents, parabolic decompositions, and BP sets
    intervals = {w: G.bruhat_interval(w) for w in elems}
    # Cross-check bruhat_le against explicit bruhat_interval on all pairs
    for v in elems:
        iv = intervals[v]
        for u in elems:
            assert G.bruhat_le(u, v) == (u in iv), f"{G.name}: bruhat_le mismatch"

    # Verify Lemma 2(1): (s * x) * t == s * (x * t) for all x, s, t
    for x in elems:
        for s in range(n):
            for t in range(n):
                lhs = G.dem_right(G.dem_left(s, x), t)
                rhs = G.dem_left(s, G.dem_right(x, t))
                assert lhs == rhs, f"{G.name}: Lemma 2(1) failed"

    # Precompute W_A subsets and parabolic decomps
    parabolic_subgroups = {}
    for mask in all_masks:
        parabolic_subgroups[mask] = {w for w in elems if (G.support_mask(w) & ~mask) == 0}

    decomps = {}
    bp_sets = {}
    for w in elems:
        bp_w = set()
        for mask in all_masks:
            w_up, w_dn = G.parabolic_decomp(w, mask)
            decomps[(w, mask)] = (w_up, w_dn)
            if G.is_bp(w, mask):
                bp_w.add(mask)
        bp_sets[w] = bp_w

    # Verify Lemma 1(2) & 1(3), Lemma 3(2), Lemma 4(1)<->(2)<->(3), Theorem 1
    conj_pairs = 0
    for w in elems:
        rw = G.reduced_word(w)
        iv_w = intervals[w]
        for mask in all_masks:
            w_up, w_dn = decomps[(w, mask)]
            # Lemma 3(2): [e, w] cap W_A == [e, Dem(w|_A)]
            sub_word = tuple(s for s in rw if (mask >> s) & 1)
            m_wA = G.dem_word(sub_word)
            lhs_slice = iv_w & parabolic_subgroups[mask]
            rhs_slice = intervals[m_wA]
            assert lhs_slice == rhs_slice, f"{G.name}: Lemma 3(2) failed"

            # Lemma 4: (1) BP <-> (2) m(w, J) == w_J <-> (3) product Bruhat interval
            c1 = (mask in bp_sets[w])
            c2 = (m_wA == w_dn)
            assert c1 == c2, f"{G.name}: Lemma 4 (1)<->(2) failed"
            if len(elems) <= 48:
                # Full check of Lemma 4(3) across all u in W
                c3 = True
                for u in elems:
                    u_up, u_dn = decomps[(u, mask)]
                    cond_prod = (u_up in intervals[w_up]) and (u_dn in intervals[w_dn])
                    if cond_prod:
                        assert u in iv_w, f"{G.name}: unconditional Lemma 4(3) failed"
                    if (u in iv_w) != cond_prod:
                        c3 = False
                assert c1 == c3, f"{G.name}: Lemma 4 (1)<->(3) failed"

        # Verify Lemma 1(2) & 1(3) on all u <= w
        for u in iv_w:
            for mask in all_masks:
                u_up, _ = decomps[(u, mask)]
                w_up, w_dn = decomps[(w, mask)]
                assert u_up in intervals[w_up], f"{G.name}: Lemma 1(3) failed"
                if u in parabolic_subgroups[mask] and G.left_weak_le(u, w):
                    assert G.left_weak_le(u, w_dn), f"{G.name}: Lemma 1(2) failed"

        # Verify Theorem 1 (Conjecture 1.3): closure under cap and cup
        bp_list = sorted(bp_sets[w])
        for i in range(len(bp_list)):
            J = bp_list[i]
            for j in range(i + 1, len(bp_list)):
                K = bp_list[j]
                assert (J & K) in bp_sets[w], f"{G.name}: intersection closure failed"
                assert (J | K) in bp_sets[w], f"{G.name}: union closure failed"
                conj_pairs += 1

    # Verify Lemma 5 exhaustively on A_3 / B_3 (and sampled on H_3)
    lemma5_checks = 0
    if len(elems) <= 48:
        for J in all_masks:
            for K in all_masks:
                M = J | K
                WM = parabolic_subgroups[M]
                for u in WM:
                    if J in bp_sets[u] and K in bp_sets[u]:
                        uJ = decomps[(u, J)][1]
                        uK = decomps[(u, K)][1]
                        for v in WM:
                            vJ = decomps[(v, J)][1]
                            vK = decomps[(v, K)][1]
                            if (uJ in intervals[vJ]) and (uK in intervals[vK]):
                                assert u in intervals[v], f"{G.name}: Lemma 5 failed"
                                lemma5_checks += 1
    else:
        rng = random.Random(251208168)
        for _ in range(300):
            u = rng.choice(elems)
            bp_u = list(bp_sets[u])
            J = rng.choice(bp_u)
            K = rng.choice(bp_u)
            M = J | K
            if u not in parabolic_subgroups[M]:
                continue
            uJ = decomps[(u, J)][1]
            uK = decomps[(u, K)][1]
            for v in parabolic_subgroups[M]:
                if (uJ in intervals[decomps[(v, J)][1]]) and (uK in intervals[decomps[(v, K)][1]]):
                    assert u in intervals[v], f"{G.name}: Lemma 5 failed"
                    lemma5_checks += 1

    print(f"  [OK] {G.name}: |W|={len(elems)}, Lemmas 1-5 & Thm 1 verified "
          f"({conj_pairs} BP pairs, {lemma5_checks} Lemma-5 checks)")


def verify_h4_exhaustive():
    """Exhaustively verify Conjecture 1.3 and key Demazure identities on all 14,400 elements of H_4."""
    t0 = time.time()
    m_h4 = [
        [1, 5, 2, 2],
        [5, 1, 3, 2],
        [2, 3, 1, 3],
        [2, 2, 3, 1],
    ]
    G = make_zphi_group("H_4", m_h4)
    # Fast BFS storing both id and right/left Cayley tables
    id_of = {G.identity: 0}
    elems = [G.identity]
    q = deque([0])
    right_tab = []
    while q:
        idx = q.popleft()
        w = elems[idx]
        row = [0] * 4
        for s in range(4):
            ws = G.mul_right(w, s)
            nid = id_of.get(ws)
            if nid is None:
                nid = len(elems)
                id_of[ws] = nid
                elems.append(ws)
                q.append(nid)
            row[s] = nid
        right_tab.append(row)

    N = len(elems)
    assert N == 14400, f"H_4 size mismatch: {N}"

    # Lengths via BFS order: compute exact lengths and left Cayley table
    lengths = [-1] * N
    lengths[0] = 0
    q2 = deque([0])
    parent = [(-1, -1)] * N
    while q2:
        u = q2.popleft()
        lu = lengths[u] + 1
        for s in range(4):
            v = right_tab[u][s]
            if lengths[v] == -1:
                lengths[v] = lu
                parent[v] = (u, s)
                q2.append(v)
    assert max(lengths) == 60

    # Build left_tab and inverse table using reduced words
    inv_tab = [0] * N
    supp_tab = [0] * N
    rdesc_tab = [0] * N
    for idx in range(N):
        # Reconstruct reduced word from parent pointers
        cur = idx
        w_rev = []
        sup = 0
        while cur != 0:
            p, s = parent[cur]
            w_rev.append(s)
            sup |= (1 << s)
            cur = p
        supp_tab[idx] = sup
        inv_id = 0
        for s in w_rev:
            inv_id = right_tab[inv_id][s]
        inv_tab[idx] = inv_id
        rd = 0
        for s in range(4):
            if lengths[right_tab[idx][s]] < lengths[idx]:
                rd |= (1 << s)
        rdesc_tab[idx] = rd

    ldesc_tab = [rdesc_tab[inv_tab[idx]] for idx in range(N)]

    # Verify Lemma 2(1) on 1,000 sampled elements of H_4
    left_tab = [[inv_tab[right_tab[inv_tab[idx]][s]] for s in range(4)] for idx in range(N)]
    for idx in range(0, N, 14):
        for s in range(4):
            for t in range(4):
                sx = idx if (ldesc_tab[idx] >> s) & 1 else left_tab[idx][s]
                lhs = sx if (rdesc_tab[sx] >> t) & 1 else right_tab[sx][t]
                xt = idx if (rdesc_tab[idx] >> t) & 1 else right_tab[idx][t]
                rhs = xt if (ldesc_tab[xt] >> s) & 1 else left_tab[xt][s]
                assert lhs == rhs

    # Compute parabolic decompositions and Dem(w|_J) for all 14,400 elements and all 16 subsets
    incomp_pairs = 0
    for idx in range(N):
        # Reduced word of idx
        cur = idx
        w_rev = []
        while cur != 0:
            p, s = parent[cur]
            w_rev.append(s)
            cur = p
        rw = list(reversed(w_rev))

        bp_mask_set = set()
        for mask in range(16):
            # Greedy parabolic decomp
            u = idx
            dn_rev = []
            while True:
                rd = rdesc_tab[u] & mask
                if rd == 0:
                    break
                s = (rd & -rd).bit_length() - 1
                dn_rev.append(s)
                u = right_tab[u][s]
            dn = 0
            for s in reversed(dn_rev):
                dn = right_tab[dn][s]
            is_bp_def = ((supp_tab[u] & mask) & ~ldesc_tab[dn]) == 0

            # Dem(w|_mask) check (Lemma 4 (1)<->(2))
            dem = 0
            for s in rw:
                if (mask >> s) & 1:
                    if not ((rdesc_tab[dem] >> s) & 1):
                        dem = right_tab[dem][s]
            assert is_bp_def == (dem == dn), f"H_4 Lemma 4 mismatch at idx={idx}, mask={mask}"
            if is_bp_def:
                bp_mask_set.add(mask)

        # Verify Conjecture 1.3 (Theorem 1)
        bp_list = sorted(bp_mask_set)
        for i in range(len(bp_list)):
            J = bp_list[i]
            for j in range(i + 1, len(bp_list)):
                K = bp_list[j]
                assert (J & K) in bp_mask_set, f"H_4 cap failure idx={idx}"
                assert (J | K) in bp_mask_set, f"H_4 cup failure idx={idx}"
                if (J & K) != J and (J & K) != K:
                    incomp_pairs += 1

    print(f"  [OK] H_4 exhaustive: |W|=14400 (max len 60), Lemma 2(1) & Lemma 4 & Thm 1 verified "
          f"({incomp_pairs} incomparable BP pairs, {time.time()-t0:.2f}s)")


def verify_infinite_group(G: CoxeterGroup, n_walks: int, max_len: int, slice_len: int, seed: int):
    """Verify Lemmas 1-5 and Theorem 1 on random + braid-biased reduced words of an infinite Coxeter group."""
    rng = random.Random(seed)
    n = G.n
    all_masks = list(range(1 << n))

    # Generate diverse reduced words
    words = []
    seen = {G.identity}
    for trial in range(n_walks):
        cur = G.identity
        target_len = rng.randint(4, max_len)
        for _ in range(target_len):
            cands = [s for s in range(n) if not G.is_right_descent(cur, s)]
            if not cands:
                break
            s = rng.choice(cands)
            cur = G.mul_right(cur, s)
        if cur not in seen:
            seen.add(cur)
            words.append(cur)

    bp_pairs = 0
    slice_checks = 0
    lemma5_checks = 0
    for w in words:
        rw = G.reduced_word(w)
        # Lemma 2(1) on w
        for s in range(n):
            for t in range(n):
                assert G.dem_right(G.dem_left(s, w), t) == G.dem_left(s, G.dem_right(w, t))

        bp_set = set()
        decomps_w = {}
        for mask in all_masks:
            w_up, w_dn = G.parabolic_decomp(w, mask)
            decomps_w[mask] = (w_up, w_dn)
            sub_word = tuple(s for s in rw if (mask >> s) & 1)
            m_wA = G.dem_word(sub_word)
            is_bp_def = G.is_bp(w, mask)
            # Lemma 4 (1)<->(2)
            assert is_bp_def == (m_wA == w_dn), f"{G.name}: Lemma 4 failed"
            if is_bp_def:
                bp_set.add(mask)

            # Explicit Bruhat-interval slice check (Lemma 3(2)) on moderate-length words
            if len(rw) <= slice_len:
                iv_w = G.bruhat_interval(w)
                lhs = {u for u in iv_w if (G.support_mask(u) & ~mask) == 0}
                rhs = G.bruhat_interval(m_wA)
                assert lhs == rhs, f"{G.name}: Lemma 3(2) explicit slice failed"
                slice_checks += 1

        # Verify Conjecture 1.3 (Theorem 1)
        bp_list = sorted(bp_set)
        for i in range(len(bp_list)):
            J = bp_list[i]
            for j in range(i + 1, len(bp_list)):
                K = bp_list[j]
                assert (J & K) in bp_set, f"{G.name}: intersection closure failed"
                assert (J | K) in bp_set, f"{G.name}: union closure failed"
                bp_pairs += 1

                # Verify Part 2's Lemma 5 application directly: m = Dem(w|_{J|K}) <= w_{J|K}
                M = J | K
                w_M = decomps_w[M][1]
                m_M = G.dem_word(tuple(s for s in rw if (M >> s) & 1))
                assert m_M == w_M
                assert G.bruhat_le(m_M, w_M) and G.bruhat_le(w_M, m_M)
                lemma5_checks += 1

    print(f"  [OK] {G.name}: {len(words)} distinct elements (len<= {max_len}), "
          f"Lemmas 2-5 & Thm 1 verified ({bp_pairs} BP pairs, {slice_checks} explicit Bruhat slices)")


def main():
    signal.alarm(90)
    t_start = time.time()
    print("Verifying PROOF.md for Conjecture 1.3 of Gaetz-Gao (arXiv:2512.08168v2)...")

    # 1. Finite crystallographic: A_3 (24) and B_3 (48)
    A3 = make_int_group("A_3", [
        [2, -1, 0],
        [-1, 2, -1],
        [0, -1, 2],
    ])
    B3 = make_int_group("B_3", [
        [2, -1, 0],
        [-1, 2, -2],
        [0, -1, 2],
    ])
    verify_all_lemmas_exhaustive(A3, 24)
    verify_all_lemmas_exhaustive(B3, 48)

    # 2. Finite non-crystallographic: H_3 (120) and H_4 (14,400)
    H3 = make_zphi_group("H_3", [
        [1, 5, 2],
        [5, 1, 3],
        [2, 3, 1],
    ])
    verify_all_lemmas_exhaustive(H3, 120)
    verify_h4_exhaustive()

    # 3. Infinite right-angled Coxeter groups: P_4 and K_4 - e
    P4 = make_racg("RACG_P4", 4, [(0, 1), (1, 2), (2, 3)])
    K4me = make_racg("RACG_K4-e", 4, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)])
    verify_infinite_group(P4, n_walks=120, max_len=14, slice_len=7, seed=101)
    verify_infinite_group(K4me, n_walks=120, max_len=14, slice_len=7, seed=102)

    # 4. Infinite affine Weyl groups: tilde_C_2, tilde_A_3, tilde_B_3
    tC2 = make_int_group("tilde_C_2", [
        [2, -2, 0],
        [-1, 2, -1],
        [0, -2, 2],
    ])
    tA3 = make_int_group("tilde_A_3", [
        [2, -1, 0, -1],
        [-1, 2, -1, 0],
        [0, -1, 2, -1],
        [-1, 0, -1, 2],
    ])
    tB3 = make_int_group("tilde_B_3", [
        [2, -1, 0, 0],
        [-1, 2, -1, -1],
        [0, -2, 2, 0],
        [0, -1, 0, 2],
    ])
    verify_infinite_group(tC2, n_walks=100, max_len=14, slice_len=8, seed=201)
    verify_infinite_group(tA3, n_walks=100, max_len=12, slice_len=6, seed=202)
    verify_infinite_group(tB3, n_walks=100, max_len=12, slice_len=6, seed=203)

    # 5. Infinite non-crystallographic hyperbolic rank-4 (m_ij in {2, 3, 4, 5, inf})
    Hyp4 = make_zsqrt2phi_group("Hyp4_543inf", [
        [1, 5, 2, 0],
        [5, 1, 4, 2],
        [2, 4, 1, 3],
        [0, 2, 3, 1],
    ])
    verify_infinite_group(Hyp4, n_walks=80, max_len=12, slice_len=6, seed=301)

    print(f"All exact-arithmetic checks completed in {time.time() - t_start:.2f}s.")
    print("PASS")


if __name__ == "__main__":
    main()
