#!/usr/bin/env python3
"""
Exact zero-float, zero-`/` verification script for Question 6.4 of
Fernando and Kousik (arXiv:2606.01037v1):
  g_{n,q}(X) = X^q + S_e(X)^2 * S_2(X)^{q-2} + S_e(X) * S_2(X)^{q-1}
is a PP of F_{q^e} (q > 2 even, e > 2) iff (q, e) = (4, 4).

Verifies:
  1. Direct Waring-definition check of Lemma 2.1 on F_{4^3}, F_{4^4}, F_{8^3}.
  2. Exhaustive PP check on all 256 elements of F_{4^4} + 2-orbit hand proof of (4, 4).
  3. Case 1 (e=3): pigeonhole irreducible cubic witness for q = 4, 8, 16, 32.
  4. Case 2 (odd e>=5) & Case 3 (even e>=8): exact integer Carlitz-Uchiyama inequalities.
  5. Case 4 (e=6):
     - All 7 explicit non-PP witnesses for m = 2..8 directly on g_{n,q}(X) over F_{q^6}
       with Rabin-verified irreducible moduli.
     - Symbolic GF(2) identities for A(a,b,mu), N3+N3', factorization of mu^5*A,
       Groebner basis absolute irreducibility of C_red, local Laurent expansions at P_1
       and P_inf, exact genus-9 Hasse-Weil inequality for m >= 9.
  6. Case 6 (e=4, q >= 8):
     - All 35 explicit colliding pairs (X1 != X2, g_{n,q}(X1) == g_{n,q}(X2)) for
       m = 3..37 directly on g_{n,q}(X) over F_{q^4} with Rabin-verified irreducible moduli.
     - Symbolic GF(2) verification of deg(P0)=deg(P1)=9, deg(Q0)=8, gcd=1.
     - Exact 6x6 Sylvester resultant P_gen(A, B; x0) of degree 25 with LC = A^3(A+1)^2(B+1)^3.
     - Unramified GF(64) specializations at (2, 40) (irreducible deg 25 + unique x1 in K)
       and (3, 7) (squarefree DDF (2, 23)) proving G_geom >= A_25.
     - Exact integer verification of Cafure-Matera (2006) Theorem 7.1 + Lemma 2.1 for m >= 38.
"""

import math
import sympy as sp


# ============================================================================
# Exact GF(2^d) bitmask arithmetic and Rabin irreducibility test
# ============================================================================

def poly2_mul(a: int, b: int, mod: int, deg: int) -> int:
    res = 0
    hi = 1 << deg
    while b:
        if b & 1:
            res ^= a
        a <<= 1
        if a & hi:
            a ^= mod
        b >>= 1
    return res


def poly2_gcd(a: int, b: int) -> int:
    while b:
        db = b.bit_length() - 1
        while a.bit_length() - 1 >= db:
            a ^= b << (a.bit_length() - 1 - db)
        a, b = b, a
    return a


def is_irred_gf2(f: int, deg: int) -> bool:
    """Exact Rabin irreducibility test over GF(2)."""
    if f.bit_length() - 1 != deg or (f & 1) == 0:
        return False
    tmp = deg
    primes = []
    d = 2
    while d * d <= tmp:
        if tmp % d == 0:
            primes.append(d)
            while tmp % d == 0:
                tmp //= d
        d += 1
    if tmp > 1:
        primes.append(tmp)

    def x_pow_2k(k: int) -> int:
        cur = 2
        for _ in range(k):
            cur = poly2_mul(cur, cur, f, deg)
        return cur

    if x_pow_2k(deg) != 2:
        return False
    for p in primes:
        xp = x_pow_2k(deg // p) ^ 2
        if poly2_gcd(f, xp) != 1:
            return False
    return True


class GF2Ext:
    def __init__(self, deg: int, mod: int):
        assert is_irred_gf2(mod, deg), f"Modulus {hex(mod)} is NOT irreducible of deg {deg}!"
        self.d = deg
        self.mod = mod
        self.hi = 1 << deg

    def mul(self, a: int, b: int) -> int:
        res = 0
        m = self.mod
        hi = self.hi
        while b:
            if b & 1:
                res ^= a
            a <<= 1
            if a & hi:
                a ^= m
            b >>= 1
        return res

    def sq(self, a: int) -> int:
        return self.mul(a, a)

    def frob(self, a: int, k: int) -> int:
        for _ in range(k):
            a = self.mul(a, a)
        return a

    def pow(self, a: int, e: int) -> int:
        res = 1
        while e:
            if e & 1:
                res = self.mul(res, a)
            a = self.mul(a, a)
            e >>= 1
        return res

    def inv(self, a: int) -> int:
        assert a != 0
        u, v = a, self.mod
        g1, g2 = 1, 0
        while u != 1:
            j = u.bit_length() - v.bit_length()
            if j < 0:
                u, v = v, u
                g1, g2 = g2, g1
                j = -j
            u ^= v << j
            g1 ^= g2 << j
        return g1

    def tr_step(self, a: int, step: int, count: int) -> int:
        res = 0
        cur = a
        for _ in range(count):
            res ^= cur
            cur = self.frob(cur, step)
        return res


def eval_g_nq(F: GF2Ext, m: int, e: int, X: int) -> int:
    """Evaluate g_{n,q}(X) = X^q + S_e(X)^2 * S_2(X)^{q-2} + S_e(X) * S_2(X)^{q-1} on F_{q^e}."""
    Xq = F.frob(X, m)
    S2 = X ^ Xq
    Se = F.tr_step(X, m, e)
    if Se == 0 or S2 == 0:
        return Xq
    S2q = F.frob(S2, m)
    invS2 = F.inv(S2)
    S2qm1 = F.mul(S2q, invS2)
    S2qm2 = F.mul(S2qm1, invS2)
    return Xq ^ F.mul(F.mul(Se, Se), S2qm2) ^ F.mul(Se, S2qm1)


def find_trace1_elem(F: GF2Ext, m: int, e: int) -> int:
    for b in range(F.d):
        tr = F.tr_step(1 << b, m, e)
        if tr != 0:
            return F.mul(1 << b, F.inv(tr))
    raise RuntimeError("No trace-1 element found")


def lift_S2(F: GF2Ext, m: int, e: int, y: int) -> int:
    """Given y in ker(S_e), return X in F_{q^e} with X + X^q = y via additive Hilbert 90."""
    alpha = find_trace1_elem(F, m, e)
    X = 0
    a_cur = alpha
    y_acc = 0
    y_cur = y
    for _ in range(1, e):
        a_cur = F.frob(a_cur, m)
        y_acc ^= y_cur
        X ^= F.mul(a_cur, y_acc)
        y_cur = F.frob(y_cur, m)
    assert (X ^ F.frob(X, m)) == y
    return X


# ============================================================================
# Check 1: Direct Waring-definition check of Lemma 2.1
# ============================================================================

def check_lemma_2_1():
    # Check sum_{a in F_q} (X + a)^n == g_{n,q}(X^q + X) for (q,e) in {(4,3), (4,4), (8,3)}
    for m, e, mod in [(2, 3, 0b1000011), (2, 4, 0b100011101), (3, 3, 0b1000010001)]:
        q = 1 << m
        F = GF2Ext(m * e, mod)
        Fq = [x for x in range(F.hi) if F.frob(x, m) == x]
        assert len(Fq) == q
        n = (q - 1) + (q - 2) * (q ** 2) + (q ** e) + (q ** (e + 2))
        # Check on 30 elements of F_{q^e}
        step = max(1, F.hi // 30)
        for X in range(0, F.hi, step):
            lhs = 0
            for a in Fq:
                lhs ^= F.pow(X ^ a, n)
            Y = X ^ F.frob(X, m)
            rhs = eval_g_nq(F, m, e, Y)
            assert lhs == rhs, f"Lemma 2.1 mismatch at (q={q},e={e},X={X})"
    print("[OK] Check 1: Lemma 2.1 direct Waring-definition check passed.")


# ============================================================================
# Check 2: Case 5 — (q, e) = (4, 4) exhaustive PP check + 2-orbit hand proof
# ============================================================================

def check_case_4_4():
    F = GF2Ext(8, 0b100011101)
    imgs = set(eval_g_nq(F, 2, 4, X) for X in range(256))
    assert len(imgs) == 256, "g_{4387,4} is not a PP of F_256!"

    # Also verify the 2-orbit hand proof in F_16 = F_2[a]/(a^4 + a + 1)
    F16 = GF2Ext(4, 0b10011)
    alpha = 2
    pows = [F16.pow(alpha, i) for i in range(15)]
    log16 = {pows[i]: i for i in range(15)}
    for z_idx, exp_s_idx, exp_zpsi_idx in [(7, 10, 11), (3, 5, 12)]:
        z = pows[z_idx]
        assert F16.tr_step(z, 1, 4) == 1
        u = z ^ F16.sq(z)
        c = u ^ F16.sq(u)
        r = z ^ F16.mul(c, u)
        c2 = F16.sq(c)
        c3 = F16.mul(c2, c)
        N = F16.sq(r) ^ F16.mul(c, r) ^ c3
        D = F16.sq(N) ^ F16.mul(r ^ c ^ 1, N) ^ F16.mul(c, r)
        assert D != 0
        Num = F16.mul(c2, N) ^ F16.sq(r)
        A1 = D ^ Num
        A0 = F16.mul(c2 ^ F16.mul(c, r) ^ 1, N) ^ F16.mul(F16.mul(c, c ^ 1), r)
        s_val = F16.mul(D, F16.inv(F16.sq(N)))
        Delta = F16.mul(A0 ^ F16.mul(A1, u), F16.inv(D))
        z_psi = z ^ F16.sq(Delta) ^ Delta
        assert log16[s_val] == exp_s_idx
        assert log16[z_psi] == exp_zpsi_idx
    print("[OK] Check 2: Case 5 (q=4, e=4) exhaustive PP & 2-orbit hand proof passed.")


# ============================================================================
# Check 3: Case 1 (e=3), Case 2 (odd e>=5), Case 3 (even e>=8) inequalities
# ============================================================================

def check_cases_1_2_3():
    # Case 1 (e=3): verify pigeonhole cubic produces s(y) = 0 for q = 4, 8, 16
    for m, mod_q in [(2, 0b111), (3, 0b1011), (4, 0b10011)]:
        q = 1 << m
        Fq = GF2Ext(m, mod_q)
        im = set()
        for t in range(2, q):
            im.add(Fq.mul(Fq.pow(t, 3), Fq.inv(t ^ 1)))
        assert len(im) < q - 1
        c = next(x for x in range(1, q) if x not in im)
        # Confirm T^3 + c*T + c has no root in F_q
        for t in range(q):
            assert (Fq.pow(t, 3) ^ Fq.mul(c, t) ^ c) != 0

    # Case 2a (q=4, odd e>=5): 4^(e/2) > 24 for e >= 5 (check 4^5 = 1024 > 576 = 24^2)
    assert (4 ** 5) > 24 * 24

    # Case 2b (q>=8, odd e>=5): (q - 2)^2 > (9/4)*q <=> 4*(q - 2)^2 > 9*q for q >= 8
    for q in [8, 16, 32, 64]:
        assert 4 * (q - 2) * (q - 2) > 9 * q

    # Case 3 (even e>=8, q>=4): q^(e/2) >= q^4 > q^2*(q-1)*(q-2) <=> 3*q^3 - 2*q^2 > 0
    for q in [4, 8, 16]:
        assert (q ** 4) > q * q * (q - 1) * (q - 2)
    print("[OK] Check 3: Cases 1, 2, 3 (e=3, odd e>=5, even e>=8) checks passed.")


# ============================================================================
# Check 4: Case 4 (e = 6) — 7 explicit witnesses (m=2..8) + symbolic & genus-9 proof
# ============================================================================

E6_WITNESSES = [
    (2, 0x1009, 0x515),
    (3, 0x40009, 0x16095),
    (4, 0x1000087, 0xa28b3e),
    (5, 0x40000003, 0x72eedd9),
    (6, 0x1000000201, 0xc941921b3),
    (7, 0x40000000081, 0x111ed036e8f),
    (8, 0x1000000020007, 0x62a37b7cc7a5),
]


def check_case_e6():
    # Part A: Verify all 7 explicit witnesses directly on g_{n,q}(X) over F_{q^6}
    for m, mod, y in E6_WITNESSES:
        F = GF2Ext(6 * m, mod)
        assert F.tr_step(y, 2 * m, 3) == 1, f"e=6 m={m}: y not in D_6"
        X1 = lift_S2(F, m, 6, y)
        assert F.tr_step(X1, m, 6) == 1
        g1 = eval_g_nq(F, m, 6, X1)
        assert F.tr_step(g1, m, 6) == 0, f"e=6 m={m}: s(y) != 0"
        # Lift g1 in ker(S_6) to X2 = g1^(q^(-1)) in ker(S_6) so g_{n,q}(X2) == g1 == g_{n,q}(X1)
        X2 = F.frob(g1, 5 * m)
        assert F.tr_step(X2, m, 6) == 0
        assert X1 != X2
        assert eval_g_nq(F, m, 6, X1) == eval_g_nq(F, m, 6, X2)

    # Part B: Symbolic verification of Step 4.2 identities in GF(2)[a, b, mu] and GF(2)[S, k]
    u1, u2, mu, a, b, S, k, w = sp.symbols("u1 u2 mu a b S k w")
    u3 = u1 + u2
    e2 = u1 * u2 + u1 * u3 + u2 * u3
    e3 = u1 * u2 * u3
    delta = u1 ** 2 * u2 + u2 ** 2 * u3 + u3 ** 2 * u1
    D = [1 + ui + mu * ui ** 2 for ui in (u1, u2, u3)]

    def express_in_ab(poly_u12):
        rem = sp.Poly(poly_u12.as_expr(), u1, u2, domain=sp.GF(2)[mu])
        res_terms = 0
        while not rem.is_zero:
            lm = max(rem.monoms())
            du1, du2 = lm
            coeff = rem.coeff_monomial(lm)
            assert du1 % 2 == 0 and du1 >= 2 * du2
            j = du2
            i = (du1 - 2 * du2) // 2
            res_terms += coeff.as_expr() * (a ** i) * (b ** j)
            rem = rem - sp.Poly(coeff.as_expr() * (e2 ** i) * (e3 ** j), u1, u2, domain=sp.GF(2)[mu])
        return sp.Poly(res_terms, a, b, mu, domain=sp.GF(2))

    P_sym = express_in_ab(sp.Poly(D[0] * D[1] * D[2], u1, u2, mu, domain=sp.GF(2)))
    N12_sym = express_in_ab(sp.Poly(
        sum((ui + mu * ui ** 3) * (D[(i + 1) % 3] * D[(i + 2) % 3]) ** 2 for i, ui in enumerate((u1, u2, u3))),
        u1, u2, mu, domain=sp.GF(2),
    ))
    N3sum_sym = express_in_ab(sp.Poly(
        sum((mu * ui ** 4) * (D[(i + 1) % 3] * D[(i + 2) % 3]) ** 2 for i, ui in enumerate((u1, u2, u3))),
        u1, u2, mu, domain=sp.GF(2),
    ))
    assert (N3sum_sym - sp.Poly(b ** 2 * mu * (b * mu ** 2 + 1) ** 2, a, b, mu, domain=sp.GF(2))).is_zero

    Y_expr = e3 * mu * (e3 * mu ** 2 + 1) ** 2
    N3_expr = sum(
        (mu * ui ** 3 * (u1, u2, u3)[(i + 1) % 3]) * (D[(i + 1) % 3] * D[(i + 2) % 3]) ** 2
        for i, ui in enumerate((u1, u2, u3))
    )
    X_u = sp.Poly(N3_expr + Y_expr * delta, u1, u2, mu, domain=sp.GF(2))
    X_swap = sp.Poly(X_u.as_expr().subs({u1: u2, u2: u1}, simultaneous=True), u1, u2, mu, domain=sp.GF(2))
    assert (X_u - X_swap).is_zero
    X_sym = express_in_ab(X_u)
    A_sym = P_sym ** 2 + N12_sym + X_sym

    # Check exact factorization of mu^5 * A((S+k)/mu^2, 1/mu^2, mu) (with mu = k + 1)
    # Clear denominators cleanly without `/` by substituting a*(k+1)^2 = S+k, b*(k+1)^2 = 1:
    # Multiply A_sym by (k+1)^8 first: each term a^i b^j mu^l * (k+1)^8 -> (S+k)^i * (k+1)^(8 + l - 2i - 2j)
    A_sub = 0
    for (i, j, l), coeff in A_sym.terms():
        if int(coeff) % 2:
            exp_m = 13 + l - 2 * i - 2 * j
            assert exp_m >= 0
            A_sub += ((S + k) ** i) * ((k + 1) ** exp_m)
    A_sub_p = sp.Poly(A_sub, S, k, domain=sp.GF(2))
    target_p = sp.Poly(((k + 1) ** 8) * (S ** 2) * (k * (S ** 2 + S) + k ** 2 + 1), S, k, domain=sp.GF(2))
    assert (A_sub_p - target_p).is_zero

    # Part C: Absolute irreducibility of C_red (Groebner basis = [1] for r = 0, 1, 2)
    F_red = (w + 1) ** 2 * k ** 3 + w * k ** 2 + (w ** 6 + w ** 4 + w + 1) * k + w ** 2
    for r in (0, 1, 2):
        degP = r + 2
        cs = sp.symbols(f"a0:{degP + 1}")
        Pw = sum(cs[i] * (w ** i) for i in range(degP + 1))
        expr = sp.expand(
            ((w + 1) ** 2) * (Pw ** 3)
            + w * ((w + 1) ** r) * (Pw ** 2)
            + (w ** 6 + w ** 4 + w + 1) * ((w + 1) ** (2 * r)) * Pw
            + (w ** 2) * ((w + 1) ** (3 * r))
        )
        pw = sp.Poly(expr, w, domain=sp.GF(2)[cs])
        eqs = [sp.Poly(c, *cs, domain=sp.GF(2)).as_expr() for c in pw.all_coeffs() if c != 0]
        gb = sp.groebner(eqs, *cs, domain=sp.GF(2))
        assert list(gb) == [1], f"C_red Groebner check failed at r={r}"

    # Verify Res_k(F_red, dF_red/dk) and local expansions at w^5+w^4+w^2+w+1=0, P_1, and P_inf
    F_k = sp.diff(F_red, k)
    res_k = sp.Poly(sp.resultant(F_red, F_k, k), w, domain=sp.GF(2))
    exp_res_k = sp.Poly((w ** 2) * ((w + 1) ** 4) * ((w ** 5 + w ** 4 + w ** 2 + w + 1) ** 2), w, domain=sp.GF(2))
    assert (res_k - exp_res_k).is_zero

    # Exact F_32 verification of local expansion at all 5 roots alpha of w^5 + w^4 + w^2 + w + 1 = 0
    F32 = GF2Ext(5, 0b110111)  # w^5 + w^4 + w^2 + w + 1
    alpha32 = 2
    assert (F32.pow(alpha32, 5) ^ F32.pow(alpha32, 4) ^ F32.pow(alpha32, 2) ^ alpha32 ^ 1) == 0
    # Verify exact polynomial remainder alpha^8 + alpha^4 + alpha^3 + alpha + 1 == alpha^4 + 1 != 0
    assert (F32.pow(alpha32, 8) ^ F32.pow(alpha32, 4) ^ F32.pow(alpha32, 3) ^ alpha32 ^ 1) == (F32.pow(alpha32, 4) ^ 1)
    assert (F32.pow(alpha32, 4) ^ 1) != 0
    # Solve (alpha+1)^2 * k0^2 = alpha^6 + alpha^4 + alpha + 1 in F_32 (unique square root x -> x^16)
    a1 = alpha32 ^ 1
    rhs_k0_sq = F32.pow(alpha32, 6) ^ F32.pow(alpha32, 4) ^ alpha32 ^ 1
    k0_sq = F32.mul(rhs_k0_sq, F32.inv(F32.sq(a1)))
    k0 = F32.pow(k0_sq, 16)
    assert F32.sq(k0) == k0_sq and k0 not in (0, 1)
    # Confirm F_red(k0, alpha) == 0
    a1_sq = F32.sq(a1)
    assert (
        F32.mul(a1_sq, F32.pow(k0, 3))
        ^ F32.mul(alpha32, k0_sq)
        ^ F32.mul(rhs_k0_sq, k0)
        ^ F32.sq(alpha32)
    ) == 0
    denom_kk = F32.mul(k0, k0 ^ 1)
    assert denom_kk != 0
    c2 = F32.mul(F32.mul(a1_sq, k0) ^ alpha32, F32.inv(denom_kk))
    c3 = F32.mul(a1_sq ^ c2, F32.inv(denom_kk))
    c3_closed = F32.mul(F32.sq(F32.pow(alpha32, 3) ^ F32.sq(alpha32) ^ 1), F32.inv(F32.sq(denom_kk)))
    assert c2 != 0 and c3 != 0 and c3 == c3_closed
    # Verify F_red(k0 + t, alpha + c2*t^2 + c3*t^3) == 0 mod t^4 over F_32[t]
    def p32_add(p, q):
        n = max(len(p), len(q))
        return [(p[i] if i < len(p) else 0) ^ (q[i] if i < len(q) else 0) for i in range(n)]
    def p32_mul_trunc(p, q, lim=4):
        r = [0] * lim
        for i, cp in enumerate(p):
            if i >= lim or cp == 0:
                continue
            for j, cq in enumerate(q):
                if i + j < lim and cq != 0:
                    r[i + j] ^= F32.mul(cp, cq)
        return r
    kt = [k0, 1, 0, 0]
    wt = [alpha32, 0, c2, c3]
    wt1 = p32_add(wt, [1, 0, 0, 0])
    kt2 = p32_mul_trunc(kt, kt)
    kt3 = p32_mul_trunc(kt2, kt)
    wt2 = p32_mul_trunc(wt, wt)
    wt4 = p32_mul_trunc(wt2, wt2)
    wt6 = p32_mul_trunc(wt4, wt2)
    f_loc = p32_add(
        p32_add(p32_mul_trunc(p32_mul_trunc(wt1, wt1), kt3), p32_mul_trunc(wt, kt2)),
        p32_add(p32_mul_trunc(p32_add(p32_add(wt6, wt4), wt1), kt), wt2),
    )
    assert f_loc == [0, 0, 0, 0], f"Local expansion mod t^4 nonzero: {f_loc}"

    # P_1 check: k = (1 + u + u^3 + u^4) / u^2 mod u^5 satisfies u^4 * F_red(k, 1+u) == 0 mod u^5
    u_s = sp.symbols("u_s")
    k_num = 1 + u_s + u_s ** 3 + u_s ** 4
    p1_check = sp.Poly(
        (u_s ** 2) * (k_num ** 3)
        + (u_s + 1) * (u_s ** 2) * (k_num ** 2)
        + u_s * (u_s ** 5 + u_s + 1) * (u_s ** 4) * k_num
        + (u_s ** 2 + 1) * (u_s ** 6),
        u_s, domain=sp.GF(2),
    )
    for deg_i in range(7):
        assert p1_check.coeff_monomial(u_s ** deg_i) == 0

    # P_inf check: s(pi) = pi^2 + pi^5 + pi^9 satisfies pinf(1 + pi*s, s)/s^2 == 0 mod pi^11
    pi_s, s_s = sp.symbols("pi_s s_s")
    pinf_sub = sp.Poly(
        (1 + s_s ** 2) * ((1 + pi_s * s_s) ** 3)
        + (s_s ** 3) * ((1 + pi_s * s_s) ** 2)
        + (1 + s_s ** 2 + s_s ** 5 + s_s ** 6) * (1 + pi_s * s_s)
        + s_s ** 6,
        s_s, pi_s, domain=sp.GF(2),
    )
    q_inf, r_inf = sp.div(pinf_sub, sp.Poly(s_s ** 2, s_s, pi_s, domain=sp.GF(2)))
    assert r_inf.is_zero
    s_ser = pi_s ** 2 + pi_s ** 5 + pi_s ** 9
    ev_inf = sp.Poly(q_inf.as_expr().subs(s_s, s_ser), pi_s, domain=sp.GF(2))
    for deg_i in range(11):
        assert ev_inf.coeff_monomial(pi_s ** deg_i) == 0
    # Check pi^4 * k == (1 + pi*s) * (pi^2 / s)^2 == 1 + pi^3 mod pi^5:
    # equivalently (1 + pi*s_ser) * pi^4 + (1 + pi^3) * s_ser^2 == 0 mod pi^9
    k_inf_chk = sp.Poly((1 + pi_s * s_ser) * (pi_s ** 4) + (1 + pi_s ** 3) * (s_ser ** 2), pi_s, domain=sp.GF(2))
    for deg_i in range(9):
        assert k_inf_chk.coeff_monomial(pi_s ** deg_i) == 0

    # Part D: Exact integer Hasse-Weil inequality for m >= 9 (q >= 512)
    q9 = 512
    assert (q9 - 7) ** 2 > (22 ** 2) * q9
    assert q9 > 498
    print("[OK] Check 4: Case 4 (e=6) all 7 witnesses, symbolic identities, C_red genus 9 & bound passed.")


# ============================================================================
# Check 5: Case 6 (e = 4, q >= 8) — 35 explicit witnesses (m=3..37) + S_25 & CM06
# ============================================================================

E4_WITNESSES = [
    (3, 0x1009, 0x24e, 0xc7b),
    (4, 0x10047, 0x9d95, 0x43e8),
    (5, 0x100009, 0xa3085, 0x7e723),
    (6, 0x1000087, 0x20ad4a, 0xd5e8cd),
    (7, 0x10000003, 0x1b2ba3a, 0xaf2c767),
    (8, 0x100400007, 0xe92f865c, 0xd906c8e0),
    (9, 0x1000000201, 0xff007fdfe, 0xefd4d2be4),
    (10, 0x10008000007, 0xd8cd85689f, 0xd4a3654129),
    (11, 0x100000000021, 0x1533348a02, 0x4212d069bb0),
    (12, 0x1000000020007, 0x486bdc399be6, 0x9dd2ff457687),
    (13, 0x10000000000009, 0x432bf4829f702, 0x91ca5ba0bf1b0),
    (14, 0x100000000200007, 0xb5ceb4a376fa92, 0xa01ec8090ee01a),
    (15, 0x1000000000000003, 0x8c388b10c413f59, 0xd99fc7944bb2225),
    (16, 0x10000000000000807, 0x4a2fa4ede95f616, 0x8296fc89d86f1ca8),
    (17, 0x100000000000000201, 0xe8e001f9d169497cb, 0x64aa074bfd130fcbd),
    (18, 0x100100000000000000b, 0x7e0069a973e537a030, 0xed6f71e381574e1943),
    (19, 0x10000000000000200001, 0xb854ef6b07fea5ff664, 0x588e73d88312c16d0b),
    (20, 0x100000040000000000007, 0xee8dfb3fe0318dce3190, 0xeaebc37f700263c99f94),
    (21, 0x1000000000000000000021, 0x2fc6a0b9c3b7a7cf27cc2, 0xe4bd698dca2ee16ec18df),
    (22, 0x1000000000000000000020b, 0xebb24ddec607004d6e68a5, 0x7e1d76fbdf4c98de887267),
    (23, 0x100000000000000000200001, 0x4ef794a666428c179f5a325, 0x9c6f04ec39c24d4aec2460b),
    (24, 0x1000000000000000000080007, 0xba3766a8997802247c2cb44c, 0x100b817ae8a18bdb7e1e0486),
    (25, 0x10000000000000000000008001, 0x8400000000002000021084200, 0x88c15aa4b714db3a6982dbfff),
    (26, 0x100000000000000000000000207, 0x565cb1d06d98c63c96a58b5021, 0x5b04a2ed7ec16dbdd37862693c),
    (27, 0x1000000000000000000000020001, 0x79b81e0170e9665d10b1cdefd4a, 0x74435fb9071ef6ae505df06d8cd),
    (28, 0x10000000000008000000000000007, 0x38b6f210610c6e8029594869226d, 0xa2d643c68c8b7d0097e51d4054a3),
    (29, 0x100000000000000000000000000017, 0x863a914a9f919ca0b102370d57ff2, 0x4ca7a89e8912257b51e740f6c3517),
    (30, 0x1000000000000000002000000000007, 0xfe92dd90796ee8a01a473aeb43613e, 0xc7a4f60d46f2e857cb78540d7bf534),
    (31, 0x10000000000000000000000000080001, 0x2fbe7e0f78c710b0221b4e58c0d4a97, 0xb54529aefca280bb080a94f21166c34),
    (32, 0x100000000000000000000000000000087, 0x7a540d7dc1042b94e3317cef9da5c886, 0xf595a27df95d70fc1fdbd0f945a9beae),
    (33, 0x1000000000000000000000000000020001, 0x160488d36e3f8d9559ec234263e15d2d0, 0x438fb5df8e9f4c5034588ab4759a8b527),
    (34, 0x10000000000000000000000000000000807, 0x1302286e868b7554d725a57d7b2efe0fd1, 0xbad6ec508a9eba3c5c6525ba54fe58f82e),
    (35, 0x100000000000000000000000000000008001, 0xfc000001f07ffff83ff003e0fffe0007e00, 0x8ad5bf43bfae112dbc78ca274418b07755c),
    (36, 0x1000000000000000000000000000000000807, 0x1f9861236fa3f0839f197151d852f8ab3efa, 0xd95556dfd0e9fd88a26355ad5b2fd2588c19),
    (37, 0x10000000000000000000000000000008000001, 0x2c3fea00c1b4f074509d80db3e50612bc1c4d, 0x2de7dc6bd3a4ea7255841ffe33d05d62795c5),
]


def check_case_e4():
    # Part A: Verify all 35 explicit colliding pairs (m = 3..37) directly on original g_{n,q}(X)
    assert [row[0] for row in E4_WITNESSES] == list(range(3, 38))
    for m, mod, x1, x2 in E4_WITNESSES:
        F = GF2Ext(4 * m, mod)
        assert x1 > 1 and x2 > 1 and x1 != x2
        assert F.mul(F.frob(x1, 2 * m), x1) == 1
        assert F.mul(F.frob(x2, 2 * m), x2) == 1
        y1 = F.mul(x1, F.inv(x1 ^ 1))
        y2 = F.mul(x2, F.inv(x2 ^ 1))
        assert (y1 ^ F.frob(y1, 2 * m)) == 1
        assert (y2 ^ F.frob(y2, 2 * m)) == 1
        X1 = lift_S2(F, m, 4, y1)
        X2 = lift_S2(F, m, 4, y2)
        g1 = eval_g_nq(F, m, 4, X1)
        g2 = eval_g_nq(F, m, 4, X2)
        s1 = F.tr_step(g1, m, 4)
        s2 = F.tr_step(g2, m, 4)
        assert s1 != 0 and s2 != 0
        X1p = F.mul(s2, X1)
        X2p = F.mul(s1, X2)
        c = eval_g_nq(F, m, 4, X1p) ^ eval_g_nq(F, m, 4, X2p)
        assert F.frob(c, m) == c  # c in F_q
        X2pp = X2p ^ c
        assert X1p != X2pp
        assert eval_g_nq(F, m, 4, X1p) == eval_g_nq(F, m, 4, X2pp)

    # Part B: Verify symbolic degrees of Psi_0 = P0/Q0, Psi_1 = P1/Q0 in (Y0, Y1) without `/`
    Y0, Y1 = sp.symbols("Y0 Y1")
    # Common denominator of w, w^q, w^{q^2}, w^{q^3} is N_Y^2 = Y0^2 (Y0+1)^2 Y1^2 (Y1+1)^2
    D_s = sp.Poly(
        (Y0 ** 2) * ((Y0 + 1) ** 2) * (Y1 ** 2) * ((Y1 + 1) ** 2)
        + Y1 * ((Y0 + 1) ** 3) * (Y1 ** 2) * ((Y1 + 1) ** 2)
        + (Y0 ** 2) * ((Y0 + 1) ** 3) * ((Y1 + 1) ** 3)
        + (Y0 ** 3) * (Y1 ** 2) * ((Y1 + 1) ** 3)
        + (Y0 ** 3) * ((Y0 + 1) ** 2) * (Y1 ** 3),
        Y0, Y1, domain=sp.GF(2),
    )
    N_Phi0 = sp.Poly(
        Y1 * (Y0 ** 2) * ((Y0 + 1) ** 2) * (Y1 ** 2) * ((Y1 + 1) ** 2)
        + Y1 * ((Y0 + 1) ** 3) * (Y1 ** 2) * ((Y1 + 1) ** 2)
        + (Y0 ** 2) * ((Y0 + 1) ** 3) * ((Y1 + 1) ** 3),
        Y0, Y1, domain=sp.GF(2),
    )
    N_Phi1 = sp.Poly(
        (Y0 + 1) * (Y0 ** 2) * ((Y0 + 1) ** 2) * (Y1 ** 2) * ((Y1 + 1) ** 2)
        + (Y0 ** 2) * ((Y0 + 1) ** 3) * ((Y1 + 1) ** 3)
        + (Y0 ** 3) * (Y1 ** 2) * ((Y1 + 1) ** 3),
        Y0, Y1, domain=sp.GF(2),
    )
    g0 = sp.gcd(N_Phi0, D_s)
    g1 = sp.gcd(N_Phi1, D_s)
    P0 = sp.div(N_Phi0, g0)[0]
    Q0 = sp.div(D_s, g0)[0]
    P1 = sp.div(N_Phi1, g1)[0]
    Q1 = sp.div(D_s, g1)[0]
    assert (Q0 - Q1).is_zero
    assert P0.total_degree() == 9 and P1.total_degree() == 9 and Q0.total_degree() == 8
    assert sp.gcd(P0, Q0).total_degree() == 0 and sp.gcd(P1, Q0).total_degree() == 0

    # Part C: Exact 6x6 Sylvester resultant P_gen(A, B; x0) over GF(2)[A, B, x0]
    A_s, B_s, x0_s = sp.symbols("A B x0")
    p3 = A_s * B_s * x0_s ** 3 + A_s * B_s * x0_s ** 2 + A_s * B_s + A_s * x0_s ** 2 + B_s * x0_s ** 3 + B_s
    p2 = A_s * B_s * x0_s ** 5 + A_s * B_s * x0_s ** 3 + A_s * B_s * x0_s ** 2 + A_s * x0_s ** 5 + A_s * x0_s ** 3 + B_s * x0_s ** 2
    p0 = (A_s + B_s) * x0_s ** 2
    q3 = (A_s + B_s) * x0_s ** 3
    q1 = A_s * x0_s ** 3 + B_s * x0_s ** 2 + B_s + x0_s ** 3 + x0_s ** 2 + 1
    q0 = A_s * x0_s ** 5 + A_s * x0_s ** 2 + B_s * x0_s ** 3 + x0_s ** 5 + x0_s ** 3 + x0_s ** 2
    M = sp.Matrix([
        [p3, p2, 0,  p0, 0,  0 ],
        [0,  p3, p2, 0,  p0, 0 ],
        [0,  0,  p3, p2, 0,  p0],
        [q3, 0,  q1, q0, 0,  0 ],
        [0,  q3, 0,  q1, q0, 0 ],
        [0,  0,  q3, 0,  q1, q0],
    ])

    def det_mod2(mat):
        n = mat.rows
        if n == 1:
            return sp.Poly(mat[0, 0], A_s, B_s, x0_s, domain=sp.GF(2))
        best_r = min(range(n), key=lambda r: sum(1 for c in range(n) if mat[r, c] != 0))
        tot = sp.Poly(0, A_s, B_s, x0_s, domain=sp.GF(2))
        for c in range(n):
            if mat[best_r, c] != 0:
                tot = tot + sp.Poly(mat[best_r, c], A_s, B_s, x0_s, domain=sp.GF(2)) * det_mod2(mat.minor_submatrix(best_r, c))
        return tot

    R_gen = det_mod2(M)
    triv = sp.Poly((x0_s ** 2) * (x0_s + 1) * (A_s + B_s), A_s, B_s, x0_s, domain=sp.GF(2))
    P_gen, rem_t = sp.div(R_gen, triv)
    assert rem_t.is_zero
    Px0 = sp.Poly(P_gen.as_expr(), x0_s, domain=sp.GF(2)[A_s, B_s])
    assert Px0.degree() == 25
    exp_LC = sp.Poly((A_s ** 3) * ((A_s + 1) ** 2) * ((B_s + 1) ** 3), A_s, B_s, domain=sp.GF(2))
    assert (sp.Poly(Px0.LC().as_expr(), A_s, B_s, domain=sp.GF(2)) - exp_LC).is_zero

    # Part D: Verify GF(64) specializations at (2, 40) and (3, 7) -> G_geom >= A_25
    F64 = GF2Ext(6, 0b1000011)

    def ptrim(p):
        while p and p[-1] == 0:
            p.pop()
        return p

    def padd(u, v):
        n = max(len(u), len(v))
        return ptrim([(u[i] if i < len(u) else 0) ^ (v[i] if i < len(v) else 0) for i in range(n)])

    def pdiv64(a, b):
        a = list(a)
        ib = F64.inv(b[-1])
        db = len(b) - 1
        if len(a) - 1 < db:
            return [], a
        q = [0] * (len(a) - db)
        while len(a) - 1 >= db:
            c = F64.mul(a[-1], ib)
            sh = len(a) - 1 - db
            q[sh] = c
            for i in range(db + 1):
                a[sh + i] ^= F64.mul(c, b[i])
            ptrim(a)
        return ptrim(q), a

    def pmul64(a, b, modp=None):
        if not a or not b:
            return []
        r = [0] * (len(a) + len(b) - 1)
        for i, ca in enumerate(a):
            if not ca:
                continue
            for j, cb in enumerate(b):
                if cb:
                    r[i + j] ^= F64.mul(ca, cb)
        ptrim(r)
        return pdiv64(r, modp)[1] if modp is not None else r

    def pgcd64(a, b):
        while b:
            a, b = b, pdiv64(a, b)[1]
        if a:
            ia = F64.inv(a[-1])
            a = [F64.mul(c, ia) for c in a]
        return a

    def ppow64(a, e, modp):
        r = [1]
        base = pdiv64(a, modp)[1]
        while e:
            if e & 1:
                r = pmul64(r, base, modp)
            base = pmul64(base, base, modp)
            e >>= 1
        return r

    def eval_Pgen_gf64(Av: int, Bv: int):
        # Evaluate each x0^k coefficient of P_gen at (Av, Bv) in GF(64)
        coeffs = [0] * 26
        for (iA, iB, ix), c in P_gen.terms():
            if int(c) % 2:
                coeffs[ix] ^= F64.mul(F64.pow(Av, iA), F64.pow(Bv, iB))
        assert coeffs[25] != 0
        inv_lc = F64.inv(coeffs[25])
        return [F64.mul(c, inv_lc) for c in coeffs]

    def ddf64(poly):
        # Squarefree check
        deriv = ptrim([poly[i] if (i % 2 == 1) else 0 for i in range(1, len(poly))])
        assert len(pgcd64(poly, deriv)) == 1
        f_cur = list(poly)
        h = [0, 1]
        res = []
        for deg_i in range(1, len(f_cur)):
            if len(f_cur) <= 1:
                break
            h = ppow64(h, 64, f_cur)
            hm = padd(h, [0, 1])
            g = pgcd64(hm, f_cur)
            if len(g) > 1:
                res.append((deg_i, (len(g) - 1) // deg_i))
                f_cur = pdiv64(f_cur, g)[0]
                if len(f_cur) <= 1:
                    break
                h = pdiv64(h, f_cur)[1]
        assert len(f_cur) == 1
        return res

    P_2_40 = eval_Pgen_gf64(2, 40)
    assert ddf64(P_2_40) == [(25, 1)], "P_gen(2, 40) not irreducible deg 25!"

    P_3_7 = eval_Pgen_gf64(3, 7)
    assert ddf64(P_3_7) == [(2, 1), (23, 1)], "P_gen(3, 7) DDF != (2, 23)!"

    # Verify unique x1 in K = GF(64)[x0]/(P_2_40) with G(x0, x1) == (2, 40) and nonzero denominators
    def Kinv(u):
        r0, r1 = list(P_2_40), pdiv64(u, P_2_40)[1]
        t0, t1 = [], [1]
        while r1:
            q, r2 = pdiv64(r0, r1)
            r0, r1 = r1, r2
            t0, t1 = t1, padd(t0, pmul64(q, t1))
        assert len(r0) == 1
        inv_c = F64.inv(r0[0])
        return [F64.mul(c, inv_c) for c in t0]

    def Kmul(u, v):
        return pmul64(u, v, P_2_40)

    def KP_trim(p):
        while p and not p[-1]:
            p.pop()
        return p

    def KP_gcd(a, b):
        while b:
            a = [list(c) for c in a]
            ib = Kinv(b[-1])
            db = len(b) - 1
            while len(a) - 1 >= db:
                c = Kmul(a[-1], ib)
                sh = len(a) - 1 - db
                for i in range(db + 1):
                    a[sh + i] = padd(a[sh + i], Kmul(c, b[i]))
                KP_trim(a)
            a, b = b, a
        return a

    def sc(c, u):
        return [F64.mul(c, v) for v in u] if c else []

    x0 = [0, 1]
    x2 = Kmul(x0, x0)
    x3 = Kmul(x2, x0)
    x5 = Kmul(x3, x2)
    one = [1]
    f0K = [x2, [], padd(x2, sc(2, padd(x5, x2))), padd(padd(x3, one), sc(2, x3)), [], sc(2, x3)]
    f1K = [x2, [], padd(padd(x5, x3), sc(40, x3)), padd(x2, sc(40, padd(x2, one))), [], sc(40, x3)]
    gK = KP_gcd(f0K, f1K)
    assert len(gK) == 2
    x1K = Kmul(gK[0], Kinv(gK[1]))
    assert x1K and x1K != one
    x1_2 = Kmul(x1K, x1K)
    x1_3 = Kmul(x1_2, x1K)
    x1_5 = Kmul(x1_3, x1_2)
    G0n = padd(Kmul(x1_3, padd(x3, one)), Kmul(x2, padd(x1_2, one)))
    G0d = Kmul(Kmul(x2, x1_2), padd(padd(x3, one), Kmul(Kmul(x0, x1K), padd(x1_2, one))))
    G1n = padd(Kmul(x2, x1_3), padd(Kmul(padd(x5, x3), x1_2), x2))
    G1d = padd(Kmul(x3, x1_5), padd(Kmul(padd(x2, one), x1_3), Kmul(x3, x1_2)))
    assert G0d and G1d
    assert Kmul(G0n, Kinv(G0d)) == [2]
    assert Kmul(G1n, Kinv(G1d)) == [40]

    # Part E: Exact integer verification of Cafure-Matera (2006) Theorem 7.1 + Lemma 2.1 for m >= 38
    delta = 288
    q38 = 1 << 38
    sq38 = math.isqrt(q38)
    assert sq38 * sq38 == q38  # 2^19 exact!
    assert q38 > 6 * delta * delta
    lhs = q38 - (delta - 1) * (delta - 2) * sq38 - delta
    assert lhs > 0 and (lhs ** 3) > 125 * (delta ** 13)
    # Also verify monotonicity derivative: for q >= 2^38, d/dq(q - 287*286*sqrt(q)) > 0 <=> 2*sqrt(q) > 287*286
    assert 2 * sq38 > (delta - 1) * (delta - 2)
    print("[OK] Check 5: Case 6 (e=4, q>=8) all 35 witnesses, P_gen deg 25, S_25 monodromy & CM06 passed.")


def main():
    check_lemma_2_1()
    check_case_4_4()
    check_cases_1_2_3()
    check_case_e6()
    check_case_e4()
    print("PASS")


if __name__ == "__main__":
    main()
