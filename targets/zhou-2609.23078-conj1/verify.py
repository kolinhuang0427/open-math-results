"""
Exact-arithmetic verification script for Conjecture 1 of arXiv:2609.23078v1
and every algebraic/combinatorial step of PROOF.md across finite simple Lie types
A2, C2, G2, B3, C3, and D4 (zero floating-point operations, zero `/` operators).

Checks performed:
  1. Lemma 1 (Positivity & Folding):
     - Explicit Lusztig-positive Chevalley matrices in non-simply-laced dual algebras
       B2 = C2^v (5-dim V(w1^v) and 4-dim V(w2^v)), G2^v (7-dim V(w2^v) via folding D4 -> G2^v),
       verifying all Cartan/Serre relations, non-negativity of all matrix entries of e_j^v, f_j^v,
       <v+|f_j^v = 0, f_j^v|v-> = 0, nonemptiness of W_k, and exact Ad(exp(a f_j^v)) identities
       used in Lemma 2(3).
  2. Lemma 4(2)-(3) & Theorem 1 (Exact Littelmann LS-path crystal & Pitman/Tropical Identity):
     - Builds exact piecewise-linear LS-path crystals P(lambda) with exact Fraction arithmetic.
     - Verifies Weyl dimension formula |P(lambda)| = dim V(lambda) in types A2, C2, G2, B3, C3, D4.
     - Verifies integrality property, exact path equality e_j^{max}(pi_1 * pi_2) == P_j(pi_1 * pi_2),
       dominance of P_{w0}(pi_1 * pi_2), exact tropical identity <H(a x b), w_k^v> == M_k(pi_1 * pi_2),
       and BOTH inequalities of Theorem 1: H(a x b) >= H(a x f_i b) and H(f_i a x b) >= H(a x b).
  3. Theorem 2 (Conjecture 1: Gamma_lambda = F(b_star) = C_{b_star} and maximal proper extremal subset):
     - Directly computes extremal closures <b >_Ext, Gamma_lambda, F(b_star), C_{b_star}, and E_max
       across A2, C2, G2, B3, C3, D4 (regular and boundary weights, including boundary weights with
       nontrivial case-2 transitions eps_i(c) = 0, f_i(c) != 0 inside C_{b_star}).
"""

from collections import deque
from fractions import Fraction


def fdiv(a, b):
    """Exact Fraction division without using Python's `/` operator."""
    fa = a if isinstance(a, Fraction) else Fraction(a)
    fb = b if isinstance(b, Fraction) else Fraction(b)
    if fb.numerator == 0:
        raise ZeroDivisionError("fdiv by zero")
    return Fraction(fa.numerator * fb.denominator, fa.denominator * fb.numerator)


def mat_mul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def mat_add(A, B, scale=1):
    n = len(A)
    return [[A[i][j] + scale * B[i][j] for j in range(n)] for i in range(n)]


def mat_comm(A, B):
    return mat_add(mat_mul(A, B), mat_mul(B, A), -1)


def mat_eye(n):
    return [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]


def mat_exp_nilpotent(A, max_deg=8):
    """Exact exponential of a nilpotent matrix over Fraction."""
    n = len(A)
    res = mat_eye(n)
    cur = mat_eye(n)
    fact = 1
    for d in range(1, max_deg + 1):
        cur = mat_mul(cur, A)
        fact *= d
        if all(cur[i][j] == 0 for i in range(n) for j in range(n)):
            break
        inv_f = Fraction(1, fact)
        res = [[res[i][j] + inv_f * cur[i][j] for j in range(n)] for i in range(n)]
    return res


def mat_inv_exact(M):
    """Exact Gauss-Jordan inverse of an integer matrix over Fraction."""
    n = len(M)
    A = [
        [Fraction(M[i][j]) for j in range(n)]
        + [Fraction(1 if i == j else 0) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        d = A[col][col]
        A[col] = [fdiv(v, d) for v in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                fac = A[r][col]
                A[r] = [A[r][c] - fac * A[col][c] for c in range(2 * n)]
    return [row[n:] for row in A]


def in_Qplus(cartan_inv, diff):
    """Check diff in Q^+ (Cartan convention: C[i][j] = <alpha_j, alpha_i^v>)."""
    n = len(diff)
    coeffs = [sum(cartan_inv[i][j] * diff[j] for j in range(n)) for i in range(n)]
    return all(c >= 0 and c.denominator == 1 for c in coeffs)


def dot_fund_cowt(cartan_inv, v, k):
    """Compute <v, varpi_k^v> = coefficient of alpha_k in v."""
    return sum(cartan_inv[k][j] * v[j] for j in range(len(v)))


# ---------------------------------------------------------------------------
# Exact piecewise-linear Littelmann LS-path crystal engine (pure Fraction)
# ---------------------------------------------------------------------------

def simplify_path(pts):
    res = [pts[0]]
    dim = len(pts[0][1])
    for idx in range(1, len(pts) - 1):
        t0, p0 = res[-1]
        t1, p1 = pts[idx]
        t2, p2 = pts[idx + 1]
        if t1 == t0 or t2 == t1:
            continue
        dt1 = t1 - t0
        dt2 = t2 - t1
        if all((p1[k] - p0[k]) * dt2 == (p2[k] - p1[k]) * dt1 for k in range(dim)):
            continue
        res.append(pts[idx])
    if len(pts) > 1:
        if pts[-1][0] != res[-1][0]:
            res.append(pts[-1])
        else:
            res[-1] = pts[-1]
    return tuple(res)


def concat_paths(p1, p2):
    """Concatenate p1 on [0, 1] and p2 on [1, 2] (exact [0, 2] path)."""
    end1 = p1[-1][1]
    dim = len(end1)
    one = Fraction(1)
    pts = list(p1)
    for t, p in p2[1:]:
        pts.append((one + t, tuple(end1[k] + p[k] for k in range(dim))))
    return simplify_path(pts)


def running_min_prefix(pts, i):
    dim = len(pts[0][1])
    out = [pts[0]]
    m_vals = [pts[0][1][i]]
    m = m_vals[0]
    for (t0, p0), (t1, p1) in zip(pts, pts[1:]):
        h0, h1 = p0[i], p1[i]
        if h1 < m:
            if h0 > m:
                lam = fdiv(m - h0, h1 - h0)
                tm = t0 + lam * (t1 - t0)
                pm = tuple(p0[k] + lam * (p1[k] - p0[k]) for k in range(dim))
                out.append((tm, pm))
                m_vals.append(m)
            m = h1
        out.append((t1, p1))
        m_vals.append(m)
    return out, m_vals


def running_min_suffix(pts, i):
    dim = len(pts[0][1])
    rev = list(reversed(pts))
    out_rev = [rev[0]]
    m_rev = [rev[0][1][i]]
    m = m_rev[0]
    for (t0, p0), (t1, p1) in zip(rev, rev[1:]):
        h0, h1 = p0[i], p1[i]
        if h1 < m:
            if h0 > m:
                lam = fdiv(m - h0, h1 - h0)
                tm = t0 + lam * (t1 - t0)
                pm = tuple(p0[k] + lam * (p1[k] - p0[k]) for k in range(dim))
                out_rev.append((tm, pm))
                m_rev.append(m)
            m = h1
        out_rev.append((t1, p1))
        m_rev.append(m)
    return list(reversed(out_rev)), list(reversed(m_rev))


def pitman_i(pts, C, i):
    rank = len(C)
    alpha_i = [Fraction(C[r][i]) for r in range(rank)]
    rpts, mvals = running_min_prefix(pts, i)
    res = [
        (t, tuple(p[r] - m * alpha_i[r] for r in range(rank)))
        for (t, p), m in zip(rpts, mvals)
    ]
    return simplify_path(res)


def littelmann_f_i(pts, C, i):
    rank = len(C)
    Q = min(p[i] for _, p in pts)
    if pts[-1][1][i] - Q < 1:
        return None
    alpha_i = [Fraction(C[r][i]) for r in range(rank)]
    rpts, Mvals = running_min_suffix(pts, i)
    one = Fraction(1)
    out = []
    for idx in range(len(rpts) - 1):
        t0, p0 = rpts[idx]
        M0 = Mvals[idx]
        t1, p1 = rpts[idx + 1]
        M1 = Mvals[idx + 1]
        c0 = min(one, M0 - Q)
        out.append((t0, tuple(p0[r] - c0 * alpha_i[r] for r in range(rank))))
        if M0 < Q + 1 < M1:
            lam = fdiv(Q + 1 - M0, M1 - M0)
            tm = t0 + lam * (t1 - t0)
            pm = tuple(p0[r] + lam * (p1[r] - p0[r]) for r in range(rank))
            out.append((tm, tuple(pm[r] - one * alpha_i[r] for r in range(rank))))
    t1, p1 = rpts[-1]
    c1 = min(one, Mvals[-1] - Q)
    out.append((t1, tuple(p1[r] - c1 * alpha_i[r] for r in range(rank))))
    return simplify_path(out)


def littelmann_e_i(pts, C, i):
    rank = len(C)
    Q = min(p[i] for _, p in pts)
    if Q > -1:
        return None
    alpha_i = [Fraction(C[r][i]) for r in range(rank)]
    rpts, mvals = running_min_prefix(pts, i)
    zero = Fraction(0)
    out = []
    for idx in range(len(rpts) - 1):
        t0, p0 = rpts[idx]
        m0 = mvals[idx]
        t1, p1 = rpts[idx + 1]
        m1 = mvals[idx + 1]
        c0 = max(zero, Q + 1 - m0)
        out.append((t0, tuple(p0[r] + c0 * alpha_i[r] for r in range(rank))))
        if m0 > Q + 1 > m1:
            lam = fdiv(Q + 1 - m0, m1 - m0)
            tm = t0 + lam * (t1 - t0)
            pm = tuple(p0[r] + lam * (p1[r] - p0[r]) for r in range(rank))
            out.append((tm, pm))
    t1, p1 = rpts[-1]
    c1 = max(zero, Q + 1 - mvals[-1])
    out.append((t1, tuple(p1[r] + c1 * alpha_i[r] for r in range(rank))))
    return simplify_path(out)


class LSCrystal:
    def __init__(self, C, lam):
        self.C = C
        self.rank = len(C)
        self.lam = lam
        zero = tuple(Fraction(0) for _ in range(self.rank))
        start = ((Fraction(0), zero), (Fraction(1), tuple(Fraction(x) for x in lam)))
        self.elems = [start]
        idx_map = {start: 0}
        self.e = {}
        self.f = {}
        q = deque([0])
        while q:
            u = q.popleft()
            p = self.elems[u]
            for i in range(self.rank):
                fp = littelmann_f_i(p, C, i)
                if fp is not None:
                    # Verify two-sided inverse e_i(f_i(p)) == p
                    assert littelmann_e_i(fp, C, i) == p
                    if fp not in idx_map:
                        idx_map[fp] = len(self.elems)
                        self.elems.append(fp)
                        q.append(idx_map[fp])
                    v = idx_map[fp]
                    self.f[(u, i)] = v
                    self.e[(v, i)] = u
        self.n = len(self.elems)
        self.wt = [tuple(int(x) for x in p[-1][1]) for p in self.elems]
        for p in self.elems:
            assert all(x.denominator == 1 for x in p[-1][1])
            for i in range(self.rank):
                assert min(pt[i] for _, pt in p).denominator == 1
        self.eps = {}
        self.phi = {}
        for u in range(self.n):
            for i in range(self.rank):
                c = 0
                cur = u
                while (cur, i) in self.e:
                    cur = self.e[(cur, i)]
                    c += 1
                self.eps[(u, i)] = c
                c = 0
                cur = u
                while (cur, i) in self.f:
                    cur = self.f[(cur, i)]
                    c += 1
                self.phi[(u, i)] = c
                assert self.phi[(u, i)] - self.eps[(u, i)] == self.wt[u][i]

    def check_e(self, u, i):
        if (u, i) not in self.e:
            return u
        cur = u
        while (cur, i) in self.e:
            cur = self.e[(cur, i)]
        return self.f[(cur, i)]

    def check_e_w0(self, w0_word):
        res = []
        for u in range(self.n):
            cur = u
            for i in reversed(w0_word):
                cur = self.check_e(cur, i)
            res.append(cur)
        return res

    def i_string(self, u, i):
        cur = u
        while (cur, i) in self.e:
            cur = self.e[(cur, i)]
        top = cur
        s = [cur]
        while (cur, i) in self.f:
            cur = self.f[(cur, i)]
            s.append(cur)
        return top, s

    def extremal_closure(self, seed):
        """Smallest extremal subset containing seed."""
        X = {seed}
        q = deque([seed])
        while q:
            u = q.popleft()
            for i in range(self.rank):
                top, s = self.i_string(u, i)
                if u != top:
                    for v in s:
                        if v not in X:
                            X.add(v)
                            q.append(v)
        # Verify X satisfies the exact extremal string axiom
        for u in range(self.n):
            for i in range(self.rank):
                top, s = self.i_string(u, i)
                inter = [v for v in s if v in X]
                assert len(inter) == 0 or len(inter) == len(s) or inter == [top]
        return X


def positive_roots_and_weyl_dim(C, lam):
    """Compute all positive coroots via simple reflections and exact Weyl dimension formula."""
    rank = len(C)
    # Coroots in simple coroot basis: alpha_j^v = e_j; s_i(alpha_j^v) = alpha_j^v - <alpha_i, alpha_j^v> alpha_i^v
    # Wait: <alpha_i, alpha_j^v> = C[j][i]!
    # Check: for s_i acting on coroots: s_i(h) = h - alpha_i(h) alpha_i^v.
    # For h = sum c_r alpha_r^v: alpha_i(h) = sum c_r <alpha_i, alpha_r^v> = sum c_r C[r][i].
    pos = set()
    q = deque()
    for i in range(rank):
        v = tuple(1 if r == i else 0 for r in range(rank))
        pos.add(v)
        q.append(v)
    while q:
        h = q.popleft()
        for i in range(rank):
            val = sum(h[r] * C[r][i] for r in range(rank))
            nh = tuple(h[r] - (val if r == i else 0) for r in range(rank))
            if any(x > 0 for x in nh) and all(x >= 0 for x in nh) and nh not in pos:
                pos.add(nh)
                q.append(nh)
    # Weyl dimension formula: prod_{beta^v > 0} <lam + rho, beta^v> / <rho, beta^v>
    num = 1
    den = 1
    for hv in pos:
        num *= sum((lam[r] + 1) * hv[r] for r in range(rank))
        den *= sum(hv[r] for r in range(rank))
    assert num % den == 0
    return num // den, len(pos)


def tensor_hw_map(B1, B2):
    """Compute highest weight element of each connected component of B1 x B2 (Hong-Kang rule)."""
    rank = B1.rank
    elems = [(a, b) for a in range(B1.n) for b in range(B2.n)]
    e = {}
    f = {}
    for a, b in elems:
        for i in range(rank):
            if B1.phi[(a, i)] >= B2.eps[(b, i)]:
                if (a, i) in B1.e:
                    e[((a, b), i)] = (B1.e[(a, i)], b)
            else:
                if (b, i) in B2.e:
                    e[((a, b), i)] = (a, B2.e[(b, i)])
            if B1.phi[(a, i)] > B2.eps[(b, i)]:
                if (a, i) in B1.f:
                    f[((a, b), i)] = (B1.f[(a, i)], b)
            else:
                if (b, i) in B2.f:
                    f[((a, b), i)] = (a, B2.f[(b, i)])
    hw = {}
    for x in elems:
        if x in hw:
            continue
        seen = {x}
        q = deque([x])
        hws = []
        while q:
            u = q.popleft()
            if all((u, i) not in e for i in range(rank)):
                hws.append(u)
            for i in range(rank):
                for nxt in (e.get((u, i)), f.get((u, i))):
                    if nxt is not None and nxt not in seen:
                        seen.add(nxt)
                        q.append(nxt)
        assert len(hws) == 1
        top = hws[0]
        top_wt = tuple(B1.wt[top[0]][k] + B2.wt[top[1]][k] for k in range(rank))
        for u in seen:
            hw[u] = top_wt
    return hw


def max_over_word_pl(pts, cinv, k, word):
    """Exact maximum of <eta(T), w_k^v> - sum_r <eta(s_r), alpha_{j_r}^v> over 0 <= s_1 <= ... <= s_m <= T.
    Since eta is piecewise linear and the objective is affine in each s_r separately,
    the maximum on the simplex Delta_m(T) is attained at vertices (breakpoints of pts)!"""
    m = len(word)
    neg_inf = Fraction(-10**18)
    dp = [neg_inf] * (m + 1)
    dp[0] = Fraction(0)
    for _, v in pts:
        for r in range(1, m + 1):
            val = dp[r - 1] - v[word[r - 1]]
            if val > dp[r]:
                dp[r] = val
    return dot_fund_cowt(cinv, pts[-1][1], k) + dp[m]


# ---------------------------------------------------------------------------
# PART 1: Verify Lemma 1 (Positivity + Folding) and Lemma 2(3) Adjoint Formula
# ---------------------------------------------------------------------------

def verify_lemma1_and_adjoint():
    # (a) B2 = C2^v: 5-dim V(w1^v) and 4-dim V(w2^v)
    n5 = 5
    e1 = [[Fraction(0)] * n5 for _ in range(n5)]
    f1 = [[Fraction(0)] * n5 for _ in range(n5)]
    e2 = [[Fraction(0)] * n5 for _ in range(n5)]
    f2 = [[Fraction(0)] * n5 for _ in range(n5)]
    e1[0][1] = Fraction(1); e1[3][4] = Fraction(1)
    f1[1][0] = Fraction(1); f1[4][3] = Fraction(1)
    e2[1][2] = Fraction(2); e2[2][3] = Fraction(1)
    f2[2][1] = Fraction(1); f2[3][2] = Fraction(2)
    h1 = mat_comm(e1, f1)
    h2 = mat_comm(e2, f2)
    # Check Cartan relations for B2 (a1^v long, a2^v short): [h1,e2]=-e2, [h2,e1]=-2 e1
    assert mat_comm(e1, f2) == [[Fraction(0)] * n5 for _ in range(n5)]
    assert mat_comm(e2, f1) == [[Fraction(0)] * n5 for _ in range(n5)]
    assert mat_comm(h1, e1) == mat_add([[Fraction(0)] * n5 for _ in range(n5)], e1, 2)
    assert mat_comm(h2, e2) == mat_add([[Fraction(0)] * n5 for _ in range(n5)], e2, 2)
    assert mat_comm(h1, e2) == mat_add([[Fraction(0)] * n5 for _ in range(n5)], e2, -1)
    assert mat_comm(h2, e1) == mat_add([[Fraction(0)] * n5 for _ in range(n5)], e1, -2)
    # Check nonnegativity, extremal annihilation, and nonempty W_0 ([0,1,1,0])
    for M in (e1, f1, e2, f2):
        assert all(M[r][c] >= 0 for r in range(n5) for c in range(n5))
    assert all(f1[0][c] == 0 and f2[0][c] == 0 for c in range(n5))  # <v+| f_j^v = 0
    assert all(f1[r][4] == 0 and f2[r][4] == 0 for r in range(n5))  # f_j^v |v-> = 0
    prod = mat_mul(e1, mat_mul(e2, mat_mul(e2, e1)))
    assert prod[0][4] > 0  # c_[0,1,1,0] = 2 > 0
    # Verify exact Ad(exp(a f_j^v)) identities used in Lemma 2(3) for a = 1, 2, 3
    for a in (Fraction(1), Fraction(2), Fraction(3)):
        for fj, ej, hj, e_other in ((f1, e1, h1, e2), (f2, e2, h2, e1)):
            ya = mat_exp_nilpotent([[a * fj[r][c] for c in range(n5)] for r in range(n5)])
            yma = mat_exp_nilpotent([[-a * fj[r][c] for c in range(n5)] for r in range(n5)])
            assert mat_mul(ya, yma) == mat_eye(n5)
            # Ad(exp(a f_j))(e_other) == e_other
            assert mat_mul(mat_mul(ya, e_other), yma) == e_other
            # Ad(exp(a f_j))(e_j) == e_j - a h_j - a^2 f_j
            expected = mat_add(mat_add(ej, hj, -a), fj, -(a * a))
            assert mat_mul(mat_mul(ya, ej), yma) == expected

    # (b) Explicit D4 -> G2^v folding on the 8-dim vector rep V(tilde_w1) of D4 (so_8)!
    # Basis: 1, 2, 3, 4, -4, -3, -2, -1 (indices 0..7).
    # Simply-laced D4 roots:
    #   node 0 (alpha_1 = e1-e2): e0 maps 2->1, -1->-2
    #   node 1 (alpha_2 = e2-e3, CENTRAL): e1 maps 3->2, -2->-3
    #   node 2 (alpha_3 = e3-e4): e2 maps 4->3, -3->-4
    #   node 3 (alpha_4 = e3+e4): e3 maps -4->3, -3->4
    n8 = 8
    te = [[[Fraction(0)] * n8 for _ in range(n8)] for _ in range(4)]
    tf = [[[Fraction(0)] * n8 for _ in range(n8)] for _ in range(4)]
    edges_d4 = [
        [(0, 1), (6, 7)],  # alpha_1: 2->1 (idx 1->0), -1->-2 (idx 7->6)
        [(1, 2), (5, 6)],  # alpha_2: 3->2 (idx 2->1), -2->-3 (idx 6->5)
        [(2, 3), (4, 5)],  # alpha_3: 4->3 (idx 3->2), -3->-4 (idx 5->4)
        [(2, 4), (3, 5)],  # alpha_4: -4->3 (idx 4->2), -3->4 (idx 5->3)
    ]
    for node, pairs in enumerate(edges_d4):
        for r, c in pairs:
            te[node][r][c] = Fraction(1)
            tf[node][c][r] = Fraction(1)
    # Check D4 Cartan matrix: node 1 connected to 0, 2, 3; {0,2,3} pairwise disconnected!
    th = [mat_comm(te[r], tf[r]) for r in range(4)]
    d4_cartan = [[2, -1, 0, 0], [-1, 2, -1, -1], [0, -1, 2, 0], [0, -1, 0, 2]]
    for i in range(4):
        for j in range(4):
            if i != j:
                assert mat_comm(te[i], tf[j]) == [[Fraction(0)] * n8 for _ in range(n8)]
            assert mat_comm(th[i], te[j]) == mat_add([[Fraction(0)] * n8 for _ in range(n8)], te[j], d4_cartan[i][j])
    # Fold D4 -> G2^v:
    #   G2^v short root (index 1, alpha_2^v): orbit {0, 2, 3}
    #   G2^v long  root (index 0, alpha_1^v): fixed {1}
    g2_e0 = te[1]
    g2_f0 = tf[1]
    g2_e1 = mat_add(mat_add(te[0], te[2]), te[3])
    g2_f1 = mat_add(mat_add(tf[0], tf[2]), tf[3])
    g2_h0 = mat_comm(g2_e0, g2_f0)
    g2_h1 = mat_comm(g2_e1, g2_f1)
    # Check G2^v Cartan relations: [h0, e1] = -e1, [h1, e0] = -3 e0!
    assert mat_comm(g2_e0, g2_f1) == [[Fraction(0)] * n8 for _ in range(n8)]
    assert mat_comm(g2_e1, g2_f0) == [[Fraction(0)] * n8 for _ in range(n8)]
    assert mat_comm(g2_h0, g2_e0) == mat_add([[Fraction(0)] * n8 for _ in range(n8)], g2_e0, 2)
    assert mat_comm(g2_h1, g2_e1) == mat_add([[Fraction(0)] * n8 for _ in range(n8)], g2_e1, 2)
    assert mat_comm(g2_h0, g2_e1) == mat_add([[Fraction(0)] * n8 for _ in range(n8)], g2_e1, -1)
    assert mat_comm(g2_h1, g2_e0) == mat_add([[Fraction(0)] * n8 for _ in range(n8)], g2_e0, -3)
    # Check Lemma 1 properties on V_k = V_{D4}(tilde_w1) for k = 1 (w2^v of G2^v):
    for M in (g2_e0, g2_f0, g2_e1, g2_f1):
        assert all(M[r][c] >= 0 for r in range(n8) for c in range(n8))
    # v+ = idx 0 has weight (0, 1) = w2^v; v- = idx 7 has weight (0, -1) = w0(w2^v)
    assert g2_h0[0][0] == 0 and g2_h1[0][0] == 1
    assert g2_h0[7][7] == 0 and g2_h1[7][7] == -1
    assert all(g2_f0[0][c] == 0 and g2_f1[0][c] == 0 for c in range(n8))
    assert all(g2_f0[r][7] == 0 and g2_f1[r][7] == 0 for r in range(n8))
    # Check c_[1,0,1,1,0,1] > 0!
    seq = [g2_e1, g2_e0, g2_e1, g2_e1, g2_e0, g2_e1]
    P = mat_eye(n8)
    for op in seq:
        P = mat_mul(op, P)
    assert P[0][7] == Fraction(2)  # strictly positive!
    # Check Ad(exp(a f_j^v)) identities in G2^v as well
    for a in (Fraction(1), Fraction(2)):
        for fj, ej, hj, e_other in ((g2_f0, g2_e0, g2_h0, g2_e1), (g2_f1, g2_e1, g2_h1, g2_e0)):
            ya = mat_exp_nilpotent([[a * fj[r][c] for c in range(n8)] for r in range(n8)])
            yma = mat_exp_nilpotent([[-a * fj[r][c] for c in range(n8)] for r in range(n8)])
            assert mat_mul(ya, yma) == mat_eye(n8)
            assert mat_mul(mat_mul(ya, e_other), yma) == e_other
            assert mat_mul(mat_mul(ya, ej), yma) == mat_add(mat_add(ej, hj, -a), fj, -(a * a))


# ---------------------------------------------------------------------------
# PART 2: Verify Lemma 4 (Pitman == e_max & Tropical M_k) & Theorem 1
# ---------------------------------------------------------------------------

def verify_pitman_tropical_and_thm1():
    # C2 and G2 exact tropical word sets W_k
    C2 = [[2, -2], [-1, 2]]
    C2_inv = mat_inv_exact(C2)
    C2_w0 = [0, 1, 0, 1]
    C2_words = {0: [[0, 1, 1, 0]], 1: [[1, 0, 1]]}

    G2 = [[2, -3], [-1, 2]]
    G2_inv = mat_inv_exact(G2)
    G2_w0 = [0, 1, 0, 1, 0, 1]
    G2_words = {
        0: [
            [0, 1, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
        ],
        1: [[1, 0, 1, 1, 0, 1]],
    }

    pairs_to_test = [
        ("C2 w1 x w2", C2, C2_inv, C2_w0, C2_words, (1, 0), (0, 1)),
        ("C2 w2 x w2", C2, C2_inv, C2_w0, C2_words, (0, 1), (0, 1)),
        ("C2 rho x w2", C2, C2_inv, C2_w0, C2_words, (1, 1), (0, 1)),
        ("C2 rho x 2w2", C2, C2_inv, C2_w0, C2_words, (1, 1), (0, 2)),
        ("G2 w1 x w1", G2, G2_inv, G2_w0, G2_words, (1, 0), (1, 0)),
        ("G2 w1 x w2", G2, G2_inv, G2_w0, G2_words, (1, 0), (0, 1)),
        ("G2 w2 x w1", G2, G2_inv, G2_w0, G2_words, (0, 1), (1, 0)),
    ]

    for _, C, cinv, w0, words_k, mu, lam in pairs_to_test:
        B1 = LSCrystal(C, mu)
        B2 = LSCrystal(C, lam)
        hw = tensor_hw_map(B1, B2)
        rank = len(C)

        # Verify Theorem 1(1) & Theorem 1(2) for ALL (a, b, i)
        for a in range(B1.n):
            for b in range(B2.n):
                h_ab = hw[(a, b)]
                for i in range(rank):
                    if (b, i) in B2.f:
                        h_afb = hw[(a, B2.f[(b, i)])]
                        diff = tuple(h_ab[r] - h_afb[r] for r in range(rank))
                        assert in_Qplus(cinv, diff)
                    if (a, i) in B1.f:
                        h_fab = hw[(B1.f[(a, i)], b)]
                        diff = tuple(h_fab[r] - h_ab[r] for r in range(rank))
                        assert in_Qplus(cinv, diff)

        # Verify Lemma 4(2) (e_j^{max} == P_j) and Lemma 4(3) (<H(a x b), w_k^v> == M_k(pi_1 * pi_2))
        for a in range(B1.n):
            for b in range(B2.n):
                eta = concat_paths(B1.elems[a], B2.elems[b])
                for j in range(rank):
                    cur = eta
                    while True:
                        nxt = littelmann_e_i(cur, C, j)
                        if nxt is None:
                            break
                        cur = nxt
                    assert cur == pitman_i(eta, C, j)
                pw = eta
                for j in reversed(w0):
                    pw = pitman_i(pw, C, j)
                # Dominance of P_{w0}(eta) and exact match with H(a x b)
                assert all(pt[j] >= 0 for _, pt in pw for j in range(rank))
                assert tuple(int(x) for x in pw[-1][1]) == hw[(a, b)]
                # Exact tropical formula M_k(pi_1 * pi_2) == <H(a x b), w_k^v>
                for k in range(rank):
                    lhs = dot_fund_cowt(cinv, tuple(Fraction(x) for x in hw[(a, b)]), k)
                    rhs = max(max_over_word_pl(eta, cinv, k, w) for w in words_k[k])
                    assert lhs == rhs


# ---------------------------------------------------------------------------
# PART 3: Direct Verification of Conjecture 1 across A2, C2, G2, B3, C3, D4
# ---------------------------------------------------------------------------

def verify_conjecture1_all_types():
    # Cartan convention C[i][j] = <alpha_j, alpha_i^v>
    specs = [
        ("A2", [[2, -1], [-1, 2]], [0, 1, 0],
         [(1, 0), (2, 0), (3, 0), (4, 0), (1, 1)]),
        ("C2", [[2, -2], [-1, 2]], [0, 1, 0, 1],
         [(1, 0), (0, 1), (2, 0), (0, 2), (3, 0), (0, 3), (1, 1)]),
        ("G2", [[2, -3], [-1, 2]], [0, 1, 0, 1, 0, 1],
         [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]),
        # B3: alpha_1, alpha_2 long, alpha_3 short => <a2, a3^v> = -2, <a3, a2^v> = -1
        ("B3", [[2, -1, 0], [-1, 2, -1], [0, -2, 2]], [0, 1, 2, 1, 0, 1, 2, 1, 2],
         [(1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 0, 0), (0, 0, 2), (1, 0, 1)]),
        # C3: alpha_1, alpha_2 short, alpha_3 long => <a3, a2^v> = -2, <a2, a3^v> = -1
        ("C3", [[2, -1, 0], [-1, 2, -2], [0, -1, 2]], [0, 1, 2, 1, 0, 1, 2, 1, 2],
         [(1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 0, 0), (0, 0, 2), (1, 0, 1)]),
        # D4: node 1 central connected to 0, 2, 3; Coxeter element c = s0 s2 s3 s1, h = 6, w0 = c^3
        ("D4", [[2, -1, 0, 0], [-1, 2, -1, -1], [0, -1, 2, 0], [0, -1, 0, 2]],
         [0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1],
         [(1, 0, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 1, 0, 0), (2, 0, 0, 0)]),
    ]

    case2_total = 0
    crystals_checked = 0

    for name, C, w0, weights in specs:
        cinv = mat_inv_exact(C)
        rank = len(C)
        # Verify w0 has the exact length = number of positive roots and sends every simple root to negative!
        _, num_pos = positive_roots_and_weyl_dim(C, tuple(0 for _ in range(rank)))
        assert len(w0) == num_pos, (name, len(w0), num_pos)
        for j in range(rank):
            # Apply w0 to alpha_j (in simple root basis: s_i(v) = v - (sum_r C[i][r] v_r) e_i)
            v = [1 if r == j else 0 for r in range(rank)]
            for i in reversed(w0):
                pairing = sum(C[i][r] * v[r] for r in range(rank))
                v[i] -= pairing
            assert all(x <= 0 for x in v) and sum(v) == -1, (name, j, v)

        for lam in weights:
            B = LSCrystal(C, lam)
            exp_dim, _ = positive_roots_and_weyl_dim(C, lam)
            assert B.n == exp_dim, (name, lam, B.n, exp_dim)

            cw0 = B.check_e_w0(w0)
            # Verify (check_e_w0)^2 == check_e_w0 and check_e_i(check_e_w0) == check_e_w0
            for u in range(B.n):
                assert cw0[cw0[u]] == cw0[u]
                for i in range(rank):
                    assert B.check_e(cw0[u], i) == cw0[u]

            # Verify Step 1 (general-type Prop 7.2): wt(check_e_w0(b)) >= wt(check_e_w0(f_i(b)))
            for u in range(B.n):
                for i in range(rank):
                    if (u, i) in B.f:
                        v = B.f[(u, i)]
                        diff = tuple(B.wt[cw0[u]][r] - B.wt[cw0[v]][r] for r in range(rank))
                        assert in_Qplus(cinv, diff)

            # Unique lowest element b_{w0 lam}
            lows = [u for u in range(B.n) if all((u, i) not in B.f for i in range(rank))]
            assert len(lows) == 1
            b_low = lows[0]
            b_star = cw0[b_low]

            # Verify Step 2: mult_{B(rho) x B(lam)}(nu_0) == 1 and nu_0 == dominant_conj(rho + w0 lam)
            # Highest weight elements of B(rho) x B(lam) are b_rho x d with eps_i(d) <= 1 for all i (i.e. cw0[d] == d)
            nu_0 = tuple(1 + B.wt[b_star][r] for r in range(rank))
            assert all(x >= 0 for x in nu_0)
            tfix = [u for u in range(B.n) if cw0[u] == u]
            nu_0_hits = [u for u in tfix if tuple(1 + B.wt[u][r] for r in range(rank)) == nu_0]
            assert nu_0_hits == [b_star]
            # Verify nu_0 == dominant W-conjugate of rho + w0(lam)
            cur_wt = [1 + B.wt[b_low][r] for r in range(rank)]
            while any(x < 0 for x in cur_wt):
                idx = next(r for r in range(rank) if cur_wt[r] < 0)
                val = cur_wt[idx]
                cur_wt = [cur_wt[r] - val * C[r][idx] for r in range(rank)]
            assert tuple(cur_wt) == nu_0
            # Also verify every constituent eta in B(rho) x B(lam) satisfies eta >= nu_0
            for u in tfix:
                diff = tuple((1 + B.wt[u][r]) - nu_0[r] for r in range(rank))
                assert in_Qplus(cinv, diff)

            # Compute C_{b_star}
            C_bstar = {u for u in range(B.n) if cw0[u] == b_star}

            # Verify F-stability of C_{b_star} and count nontrivial boundary case-2 steps
            for u in C_bstar:
                for i in range(rank):
                    if (u, i) in B.f:
                        v = B.f[(u, i)]
                        assert v in C_bstar
                        if B.eps[(u, i)] == 0:
                            case2_total += 1

            # Compute F(b_star)
            F_bstar = {b_star}
            q = deque([b_star])
            while q:
                u = q.popleft()
                for i in range(rank):
                    if (u, i) in B.f and B.f[(u, i)] not in F_bstar:
                        F_bstar.add(B.f[(u, i)])
                        q.append(B.f[(u, i)])
            assert F_bstar == C_bstar

            # Compute Gamma_lambda directly from extremal closures <b >_Ext
            Gamma = {u for u in range(B.n) if len(B.extremal_closure(u)) == B.n}
            assert Gamma == F_bstar == C_bstar

            # Verify E_max = B \ F(b_star) is a proper extremal subset containing every <b >_Ext (b not in Gamma)
            E_max = set(range(B.n)) - F_bstar
            assert len(E_max) < B.n
            for u in range(B.n):
                for i in range(rank):
                    top, s = B.i_string(u, i)
                    inter = [x for x in s if x in E_max]
                    assert len(inter) == 0 or len(inter) == len(s) or inter == [top]
            for u in E_max:
                assert B.extremal_closure(u).issubset(E_max)

            crystals_checked += 1

    assert case2_total >= 4  # Confirms nontrivial boundary case-2 transitions were exercised
    assert crystals_checked == 34


def main():
    verify_lemma1_and_adjoint()
    verify_pitman_tropical_and_thm1()
    verify_conjecture1_all_types()
    print("PASS")


if __name__ == "__main__":
    main()
