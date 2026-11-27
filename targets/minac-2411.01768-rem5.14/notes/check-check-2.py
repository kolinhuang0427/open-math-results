#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/minac-2411.01768-rem5.14/COUNTEREXAMPLE.md.

Zero floating point: exact polynomial arithmetic over F_q (prime fields and F_4),
direct vertex-level Cayley gcd-graph construction from arXiv:2411.01768v2 Def. 1 & 2,
explicit CRT graph isomorphism verification, and exact Mobius irreducibility counts.
"""

from collections import deque
from itertools import product

# ---------------------------------------------------------------------------
# 1. Exact finite field F_q and polynomial arithmetic F_q[x]
# ---------------------------------------------------------------------------

class FqPolyRing:
    """Polynomial ring F_q[x] where elements of F_q are ints (if q prime)
    or tuples over F_p mod irred poly (for F_4 = F_2[t]/(t^2+t+1))."""

    def __init__(self, q, p=None, mod_poly=None):
        self.q = q
        self.p = q if p is None else p
        self.mod_poly = mod_poly  # None for prime field F_p
        if mod_poly is None:
            self.elems = list(range(q))
            self.zero = 0
            self.one = 1
        else:
            deg = len(mod_poly) - 1
            self.elems = list(product(range(self.p), repeat=deg))
            self.zero = (0,) * deg
            self.one = (1,) + (0,) * (deg - 1)

    def f_add(self, a, b):
        if self.mod_poly is None:
            return (a + b) % self.p
        return tuple((x + y) % self.p for x, y in zip(a, b))

    def f_sub(self, a, b):
        if self.mod_poly is None:
            return (a - b) % self.p
        return tuple((x - y) % self.p for x, y in zip(a, b))

    def f_neg(self, a):
        return self.f_sub(self.zero, a)

    def _raw_poly_mul(self, a, b):
        res = [0] * (len(a) + len(b) - 1)
        for i, ai in enumerate(a):
            for j, bj in enumerate(b):
                res[i + j] = (res[i + j] + ai * bj) % self.p
        return res

    def f_mul(self, a, b):
        if self.mod_poly is None:
            return (a * b) % self.p
        d = len(self.mod_poly) - 1
        prod = self._raw_poly_mul(a, b)
        for i in range(len(prod) - 1, d - 1, -1):
            c = prod[i]
            if c != 0:
                for j, mj in enumerate(self.mod_poly):
                    prod[i - d + j] = (prod[i - d + j] - c * mj) % self.p
        return tuple(prod[:d])

    def f_inv(self, a):
        assert a != self.zero
        if self.mod_poly is None:
            return pow(a, self.p - 2, self.p)
        for b in self.elems:
            if b != self.zero and self.f_mul(a, b) == self.one:
                return b
        raise ZeroDivisionError

    # Polynomials over F_q stored as tuples of coeffs [c_0, ..., c_d] with c_d != 0 (empty () for 0)
    def trim(self, p):
        lst = list(p)
        while lst and lst[-1] == self.zero:
            lst.pop()
        return tuple(lst)

    def monic(self, p):
        p = self.trim(p)
        if not p:
            return p
        inv = self.f_inv(p[-1])
        return tuple(self.f_mul(c, inv) for c in p)

    def p_add(self, a, b):
        n = max(len(a), len(b))
        res = []
        for i in range(n):
            ca = a[i] if i < len(a) else self.zero
            cb = b[i] if i < len(b) else self.zero
            res.append(self.f_add(ca, cb))
        return self.trim(res)

    def p_sub(self, a, b):
        n = max(len(a), len(b))
        res = []
        for i in range(n):
            ca = a[i] if i < len(a) else self.zero
            cb = b[i] if i < len(b) else self.zero
            res.append(self.f_sub(ca, cb))
        return self.trim(res)

    def p_mul(self, a, b):
        a, b = self.trim(a), self.trim(b)
        if not a or not b:
            return ()
        res = [self.zero] * (len(a) + len(b) - 1)
        for i, ca in enumerate(a):
            for j, cb in enumerate(b):
                res[i + j] = self.f_add(res[i + j], self.f_mul(ca, cb))
        return self.trim(res)

    def p_divmod(self, a, b):
        a, b = self.trim(a), self.trim(b)
        assert b, "division by zero polynomial"
        if len(a) < len(b):
            return (), a
        rem = list(a)
        db = len(b) - 1
        inv_lc = self.f_inv(b[-1])
        q = [self.zero] * (len(a) - len(b) + 1)
        for i in range(len(a) - 1, db - 1, -1):
            c = rem[i]
            if c != self.zero:
                fac = self.f_mul(c, inv_lc)
                q[i - db] = fac
                for j, bj in enumerate(b):
                    rem[i - db + j] = self.f_sub(rem[i - db + j], self.f_mul(fac, bj))
        return self.trim(q), self.trim(rem[:db])

    def p_mod(self, a, b):
        return self.p_divmod(a, b)[1]

    def p_gcd(self, a, b):
        a, b = self.trim(a), self.trim(b)
        while b:
            a, b = b, self.p_mod(a, b)
        return self.monic(a)

    def all_polys_lt(self, deg):
        return [self.trim(coeffs) for coeffs in product(self.elems, repeat=deg)]

    def is_irreducible(self, p):
        p = self.monic(p)
        d = len(p) - 1
        if d <= 0:
            return False
        for k in range(1, d // 2 + 1):
            for c in product(self.elems, repeat=k):
                cand = tuple(c) + (self.one,)
                if self.p_mod(p, cand) == ():
                    return False
        return True

    def monic_divisors(self, f):
        f = self.monic(f)
        d = len(f) - 1
        divs = []
        for k in range(d + 1):
            for c in product(self.elems, repeat=k):
                cand = tuple(c) + (self.one,)
                if self.p_mod(f, cand) == ():
                    divs.append(cand)
        return divs

def check_gcd_graph_pair(ring, f, D1, D2, label):
    """Independently build G_f(D1), G_f(D2) and their complements from Def. 1 & 2,
    verify component structure, connectedness of complements, and explicit CRT isomorphism."""
    f = ring.monic(f)
    deg_f = len(f) - 1
    divs = set(ring.monic_divisors(f))
    assert f in divs
    proper_divs = divs - {f}
    D1, D2 = set(D1), set(D2)
    assert D1 <= proper_divs and D2 <= proper_divs
    assert D1 != D2

    verts = ring.all_polys_lt(deg_f)
    V = len(verts)
    assert V == ring.q ** deg_f
    v_idx = {v: i for i, v in enumerate(verts)}

    gcds = [ring.p_gcd(v, f) for v in verts]

    def build_adj(D):
        # Directly from Cayley Def. (L276-277): S_D = {h in A/f : gcd(h, f) in D}
        S_D = [verts[k] for k in range(V) if gcds[k] in D]
        adj = [set() for _ in range(V)]
        for i in range(V):
            vi = verts[i]
            for s in S_D:
                j = v_idx[ring.p_add(vi, s)]
                adj[i].add(j)
        # For small graphs (V <= 100), double-check every pair directly via Def. (L274):
        if V <= 100:
            for i in range(V):
                for j in range(i + 1, V):
                    assert (j in adj[i]) == (ring.p_gcd(ring.p_sub(verts[i], verts[j]), f) in D)
        return adj

    def check_components_disjoint_cliques(adj, num_cliques, clique_size):
        seen = [False] * V
        comps = 0
        for s in range(V):
            if seen[s]:
                continue
            comp = []
            q = deque([s])
            seen[s] = True
            while q:
                u = q.popleft()
                comp.append(u)
                for w in adj[u]:
                    if not seen[w]:
                        seen[w] = True
                        q.append(w)
            assert len(comp) == clique_size
            cset = set(comp)
            for u in comp:
                assert adj[u] == (cset - {u})
            comps += 1
        assert comps == num_cliques

    def check_complete_multipartite(adj, num_parts, part_size):
        # Complement of num_parts disjoint K_{part_size} is K_{part_size, ..., part_size}
        comp_adj = [set(range(V)) - {i} - adj[i] for i in range(V)]
        check_components_disjoint_cliques(comp_adj, num_parts, part_size)
        # Also directly verify connected and regular of degree (num_parts - 1) * part_size
        seen = {0}
        dq = deque([0])
        while dq:
            u = dq.popleft()
            for w in adj[u]:
                if w not in seen:
                    seen.add(w)
                    dq.append(w)
        assert len(seen) == V
        exp_deg = (num_parts - 1) * part_size
        assert all(len(adj[i]) == exp_deg for i in range(V))

    adj1 = build_adj(D1)
    adj2 = build_adj(D2)
    # Build complements tilde_D1, tilde_D2 directly from definition too!
    tD1 = proper_divs - D1
    tD2 = proper_divs - D2
    assert tD1 != tD2
    tadj1 = build_adj(tD1)
    tadj2 = build_adj(tD2)

    return verts, v_idx, adj1, adj2, tadj1, tadj2, check_components_disjoint_cliques, check_complete_multipartite

def verify_crt_isomorphism(ring, g, h, verts, v_idx, adj1, adj2, tadj1, tadj2):
    """Explicitly construct CRT bijection Phi: A/f -> A/f from Counterexample Section 3
    and verify it preserves adjacency and non-adjacency on ALL pairs (u, v)."""
    f = ring.p_mul(g, h)
    deg_g = len(g) - 1
    deg_h = len(h) - 1
    assert deg_g == deg_h
    assert ring.p_gcd(g, h) == (ring.one,)

    # CRT map theta: a -> (a mod g, a mod h), and explicit inverse table
    theta = {}
    inv_theta = {}
    for i, a in enumerate(verts):
        pair = (ring.p_mod(a, g), ring.p_mod(a, h))
        theta[i] = pair
        assert pair not in inv_theta
        inv_theta[pair] = i
    assert len(inv_theta) == len(verts)

    # Bijection psi: F_q[x]/(g) -> F_q[x]/(h) (canonical degree-coeff isomorphism since deg g == deg h!)
    # Every element mod g (or mod h) is uniquely a poly of degree < d!
    # Check psi(r) = r as degree < d polynomial gives a valid F_q-linear bijection!
    phi = [0] * len(verts)
    for i in range(len(verts)):
        x, y = theta[i]
        phi[i] = inv_theta[(y, x)]
    assert len(set(phi)) == len(verts)

    # Verify edge preservation across ALL pairs (i, j) for BOTH G_f(D_k) and G_f(tilde_D_k):
    for i in range(len(verts)):
        pi = phi[i]
        for j in range(i + 1, len(verts)):
            pj = phi[j]
            assert (j in adj1[i]) == (pj in adj2[pi])
            assert (j in tadj1[i]) == (pj in tadj2[pi])

# ---------------------------------------------------------------------------
# 2. Check Section 1: Minimal counterexample (16 vertices over F_2[x])
# ---------------------------------------------------------------------------

F2 = FqPolyRing(2)
x = (0, 1)
P1 = (0, 1)          # x
P2 = (1, 1, 1)       # x^2 + x + 1
assert F2.is_irreducible(P1) and F2.is_irreducible(P2)
f_sec1 = F2.p_mul(F2.p_mul(P1, P1), P2)  # x^2 (x^2 + x + 1)
assert f_sec1 == (0, 0, 1, 1, 1)
D1_sec1 = {F2.p_mul(P1, P1)}  # {x^2}
D2_sec1 = {P2, F2.p_mul(P1, P2)}  # {x^2+x+1, x(x^2+x+1)}

verts, v_idx, a1, a2, ta1, ta2, chk_clq, chk_mp = check_gcd_graph_pair(F2, f_sec1, D1_sec1, D2_sec1, "Sec1")
chk_clq(a1, 4, 4)
chk_clq(a2, 4, 4)
chk_mp(ta1, 4, 4)
chk_mp(ta2, 4, 4)
verify_crt_isomorphism(F2, F2.p_mul(P1, P1), P2, verts, v_idx, a1, a2, ta1, ta2)
print("[1] PASS Section 1: f=x^2(x^2+x+1) over F_2[x] (16 vertices): G_f(D1) ~= 4 K_4 ~= G_f(D2), connected complements ~= K_{4,4,4,4}.")

# ---------------------------------------------------------------------------
# 3. Check Section 2: Minimal squarefree counterexample (64 vertices over F_2[x])
# ---------------------------------------------------------------------------

P3 = (1, 1, 0, 1)    # x^3 + x + 1
assert F2.is_irreducible(P3)
f_sec2 = F2.p_mul(F2.p_mul(P1, P2), P3)  # x(x^2+x+1)(x^3+x+1)
D1_sec2 = {F2.p_mul(P1, P2)}
D2_sec2 = {P3, F2.p_mul(P1, P3), F2.p_mul(P2, P3)}

verts, v_idx, a1, a2, ta1, ta2, chk_clq, chk_mp = check_gcd_graph_pair(F2, f_sec2, D1_sec2, D2_sec2, "Sec2")
chk_clq(a1, 8, 8)
chk_clq(a2, 8, 8)
chk_mp(ta1, 8, 8)
chk_mp(ta2, 8, 8)
verify_crt_isomorphism(F2, F2.p_mul(P1, P2), P3, verts, v_idx, a1, a2, ta1, ta2)
print("[2] PASS Section 2: squarefree f=x(x^2+x+1)(x^3+x+1) over F_2[x] (64 vertices): 8 K_8 and connected K_{8,...,8}.")

# ---------------------------------------------------------------------------
# 4. Check Section 3: Explicit constructions across F_3, F_4, F_5 & Mobius S(m, q) > 0
# ---------------------------------------------------------------------------

def test_general_prop(ring, P1, a, P2, label):
    assert ring.is_irreducible(P1) and ring.is_irreducible(P2)
    assert P1 != P2
    d1, d2 = len(P1) - 1, len(P2) - 1
    assert d2 == a * d1 and a >= 2
    g = (ring.one,)
    for _ in range(a):
        g = ring.p_mul(g, P1)
    h = P2
    f = ring.p_mul(g, h)
    div_h = set(ring.monic_divisors(h)) - {h}
    div_g = set(ring.monic_divisors(g)) - {g}
    D1 = {ring.p_mul(g, u) for u in div_h}
    D2 = {ring.p_mul(h, v) for v in div_g}
    assert D1.isdisjoint(D2)
    verts, v_idx, a1, a2, ta1, ta2, chk_clq, chk_mp = check_gcd_graph_pair(ring, f, D1, D2, label)
    qd = ring.q ** d2
    chk_clq(a1, qd, qd)
    chk_clq(a2, qd, qd)
    chk_mp(ta1, qd, qd)
    chk_mp(ta2, qd, qd)
    verify_crt_isomorphism(ring, g, h, verts, v_idx, a1, a2, ta1, ta2)
    print(f"    PASS {label}: q={ring.q}, deg(P1)={d1}, deg(P2)={d2}, |V|={len(verts)} -> {qd} K_{{{qd}}} and connected {qd}-partite.")

print("[3] Checking Section 3 general theorem on F_3, F_4, F_5...")
F3 = FqPolyRing(3)
test_general_prop(F3, (0, 1), 2, (1, 0, 1), "F3 (x^2)*(x^2+1)")
F4 = FqPolyRing(4, p=2, mod_poly=(1, 1, 1))
test_general_prop(F4, ((0, 0), (1, 0)), 2, ((0, 1), (1, 0), (1, 0)), "F4 (x^2)*(x^2+x+t)")
F5 = FqPolyRing(5)
test_general_prop(F5, (0, 1), 2, (2, 0, 1), "F5 (x^2)*(x^2+2)")

# Check Mobius irreducible count S(m, q) > 0 and bound q^m - sum_{k<=m/2} q^k > 0 for all q in 2..50, m in 1..20:
def mobius(n):
    if n == 1:
        return 1
    p_cnt = 0
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            temp //= d
            if temp % d == 0:
                return 0
            p_cnt += 1
        d += 1
    if temp > 1:
        p_cnt += 1
    return -1 if (p_cnt % 2 == 1) else 1

for q in range(2, 51):
    for m in range(1, 21):
        tot = sum(mobius(m // k) * (q ** k) for k in range(1, m + 1) if m % k == 0)
        assert tot % m == 0 and tot // m > 0
        # Also verify exact inequality q^m - sum_{k<=m//2} q^k > 0:
        assert q ** m - sum(q ** k for k in range(1, m // 2 + 1)) > 0

print("[4] PASS Irreducible count S(m, q) > 0 and explicit lower bound q^m - sum_{k<=m/2} q^k > 0 for all q<=50, m<=20.")
print("PASS")
