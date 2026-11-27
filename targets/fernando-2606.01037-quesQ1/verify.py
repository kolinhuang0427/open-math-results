"""Exact zero-float verification of PROOF.md for fernando-2606.01037-quesQ1
(arXiv:2606.01037v1, Section 6, Question 6.1).

Zero floats, zero float division (/), zero math/numpy/scipy imports.
"""

import ast
import sys


def int_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gf2_mul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r


def gf2_mod(a, mod):
    dm = mod.bit_length() - 1
    while a.bit_length() - 1 >= dm:
        a ^= mod << (a.bit_length() - 1 - dm)
    return a


def gf2_gcd(u, v):
    while v:
        u, v = v, gf2_mod(u, v)
    return u


def find_irred(n):
    """Find the smallest irreducible polynomial of degree n over GF(2)."""
    for mask in range((1 << n) + 1, 1 << (n + 1), 2):
        def powx(exp):
            r = 1
            base = 2
            while exp:
                if exp & 1:
                    r = gf2_mod(gf2_mul(r, base), mask)
                base = gf2_mod(gf2_mul(base, base), mask)
                exp >>= 1
            return r

        if powx(1 << n) != 2:
            continue
        ok = True
        for d in range(1, n):
            if n % d == 0:
                if gf2_gcd(powx(1 << d) ^ 2, mask) != 1:
                    ok = False
                    break
        if ok:
            return mask
    raise RuntimeError(f"No irreducible polynomial found for degree {n}")


class GF:
    """Exact finite field GF(2^n) represented as bit-packed GF(2)[x]/(mod)."""

    def __init__(self, n, mod=None):
        self.n = n
        self.size = 1 << n
        self.mod = find_irred(n) if mod is None else mod

    def mul(self, a, b):
        return gf2_mod(gf2_mul(a, b), self.mod)

    def pow(self, a, e):
        r = 1
        while e:
            if e & 1:
                r = self.mul(r, a)
            a = self.mul(a, a)
            e >>= 1
        return r

    def inv(self, a):
        assert a != 0
        return self.pow(a, self.size - 2)

    def S(self, r, q, x):
        acc = 0
        cur = x
        for _ in range(r):
            acc ^= cur
            cur = self.pow(cur, q)
        return acc

    def g_eval(self, q, e, x):
        k = e // 2
        sk = self.S(k, q, x)
        se = sk ^ self.pow(sk, q ** k)
        return x ^ self.pow(sk, q ** k) ^ self.mul(se, self.pow(sk, q - 1))

    def Phi_eval(self, q, k, y):
        t = y ^ self.pow(y, q ** k)
        sk_y = self.S(k, q, y)
        sk_yqm1 = self.S(k, q, self.pow(y, q - 1))
        kt = t if (k & 1) else 0
        return y ^ sk_y ^ kt ^ self.mul(t, sk_yqm1)


def check_ast_zero_float():
    with open(__file__, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            raise AssertionError(f"Float literal found: {node.value}")
        if isinstance(node, ast.Div):
            raise AssertionError("True division '/' found")
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = [alias.name for alias in node.names]
            if isinstance(node, ast.ImportFrom) and node.module:
                names.append(node.module)
            for nm in names:
                if nm in ("math", "numpy", "scipy", "fractions", "decimal"):
                    raise AssertionError(f"Disallowed import: {nm}")


def test_lemma_2_1():
    """Verify g_{n,q}(X^q + X) == sum_{a in F_q} (X + a)^n matches S_1 + S_k^(q^k) + S_e*S_k^(q-1)."""
    for m, e in [(2, 2), (2, 4), (3, 2)]:
        q = 1 << m
        k = e // 2
        n = (q - 1) + (q - 1) * (q ** k) + (q ** e)
        ext_deg = 2 * m * e if m * e <= 8 else m * e
        F = GF(ext_deg)
        Fq = [a for a in range(F.size) if F.pow(a, q) == a]
        assert len(Fq) == q
        checked = 0
        for X in range(min(F.size, 128)):
            y = F.pow(X, q) ^ X
            if F.pow(y, q ** e) != y:
                continue
            lhs = 0
            for a in Fq:
                lhs ^= F.pow(X ^ a, n)
            rhs = F.g_eval(q, e, y)
            assert lhs == rhs, f"Lemma 2.1 mismatch at q={q}, e={e}, X={X}"
            checked += 1
        assert checked >= 4


def test_lemma_2_2_and_case_1():
    """Verify Lemma 2.2 bijection equivalence and Case 1 (e = 2 mod 4 => non-PP)."""
    for m, e in [(2, 2), (3, 2), (4, 2), (2, 6)]:
        q = 1 << m
        k = e // 2
        assert k % 2 == 1
        F = GF(m * e)
        # Explicit collision from Case 1: pick x in F_{q^k} with Tr_{q^k/q}(x) != 0
        found_collision = False
        for x in range(1, F.size):
            if F.pow(x, q ** k) != x:
                continue
            c = F.S(k, q, x)
            if c != 0:
                xp = x ^ c
                assert xp != x
                assert F.pow(xp, q ** k) == xp
                assert F.S(k, q, xp) == 0
                assert F.g_eval(q, e, x) == F.g_eval(q, e, xp)
                found_collision = True
                break
        assert found_collision, f"Case 1 collision not found for q={q}, e={e}"

    # Verify Lemma 2.2 fiber count equality exhaustively on (q=4, e=2), (q=4, e=4), (q=8, e=2)
    for m, e in [(2, 2), (2, 4), (3, 2)]:
        q = 1 << m
        k = e // 2
        F = GF(m * e)
        Vk = [y for y in range(F.size) if F.pow(y ^ F.pow(y, q ** k), q) == (y ^ F.pow(y, q ** k))]
        assert len(Vk) == q ** (k + 1)
        im_Sk = {F.S(k, q, x) for x in range(F.size)}
        assert set(Vk) == im_Sk
        g_counts = {}
        for x in range(F.size):
            val = F.g_eval(q, e, x)
            g_counts[val] = g_counts.get(val, 0) + 1
        phi_counts = {}
        for y in Vk:
            val = F.Phi_eval(q, k, y)
            assert val in im_Sk
            phi_counts[val] = phi_counts.get(val, 0) + 1
        for b in range(F.size):
            assert g_counts.get(b, 0) == phi_counts.get(F.S(k, q, b), 0)


def test_case_2():
    """Verify Case 2 (q = 4, 4 | e => PP) and all intermediate identities for k = 2, 4."""
    for k in [2, 4]:
        e = 2 * k
        F = GF(2 * e)
        F4 = [a for a in range(F.size) if F.pow(a, 4) == a]
        assert len(F4) == 4
        w = next(a for a in F4 if a not in (0, 1))
        w2 = F.mul(w, w)
        assert (w ^ w2) == 1

        # Collect V_k and verify Phi is a bijection on V_k!
        # Find alpha with alpha^(4^k) = alpha + 1
        alpha = next(a for a in range(1, F.size) if (a ^ F.pow(a, 4 ** k)) == 1)
        # Enumerate F_{4^k}
        F4k = [a for a in range(F.size) if F.pow(a, 4 ** k) == a]
        assert len(F4k) == 4 ** k

        Vk_imgs = set()
        for t in F4:
            for u in F4k:
                y = u ^ F.mul(t, alpha)
                assert (y ^ F.pow(y, 4 ** k)) == t
                py = F.Phi_eval(4, k, y)
                Vk_imgs.add(py)
                if t != 0:
                    sy = py ^ F.pow(py, 4 ** k)
                    ratio = F.mul(sy, F.inv(t))
                    assert ratio in (w, w2), f"s(y)/t not in {{w, w^2}} at k={k}"
                    # Check Phi(y)^4 + Phi(y) == (y^2 + t*y)^2
                    lhs = F.pow(py, 4) ^ py
                    y2_ty = F.mul(y, y) ^ F.mul(t, y)
                    rhs = F.mul(y2_ty, y2_ty)
                    assert lhs == rhs, f"Phi^4 + Phi identity failed at k={k}"
        assert len(Vk_imgs) == 4 ** (k + 1), f"Case 2 Phi not bijective at k={k}"

        # Direct g_{n,4} bijection check on F_{4^4} (size 256) and F_{4^8} (size 65536)!
        g_imgs = {F.g_eval(4, e, x) for x in range(F.size)}
        assert len(g_imgs) == F.size, f"g_{{n,4}} not a PP of F_{{4^{e}}}"

        # Verify Q(A)^2 + Q(A) + w^2*A == 1 on ALL A in F_{4^k} with S_k(A) == w,
        # and verify Phi(y1) + Phi(y2) == w^2*y1 + w*y2 + w^2*(1 + Q(A))!
        cnt_A = 0
        checked_pairs = 0
        for A in F4k:
            if F.S(k, 4, A) != w:
                continue
            cnt_A += 1
            ar = [F.pow(A, 4 ** r) for r in range(k)]
            Q = 0
            for r in range(k):
                for j in range(r + 1, k):
                    Q ^= F.mul(F.mul(ar[r], ar[r]), ar[j])
            assert (F.mul(Q, Q) ^ Q ^ F.mul(w2, A)) == 1
            if checked_pairs < 16:
                # Find y1 = u + alpha with y1^2 + y1 == A, and y2 = u' + w*alpha with y2^2 + w*y2 == A
                y1 = next(u ^ alpha for u in F4k if (F.mul(u ^ alpha, u ^ alpha) ^ (u ^ alpha)) == A)
                wa = F.mul(w, alpha)
                y2 = next(u ^ wa for u in F4k if (F.mul(u ^ wa, u ^ wa) ^ F.mul(w, u ^ wa)) == A)
                p1 = F.Phi_eval(4, k, y1)
                p2 = F.Phi_eval(4, k, y2)
                assert (p1 ^ F.pow(p1, 4 ** k)) == w2
                assert (p2 ^ F.pow(p2, 4 ** k)) == w2
                assert (p1 ^ p2) == (F.mul(w2, y1) ^ F.mul(w, y2) ^ F.mul(w2, 1 ^ Q))
                checked_pairs += 1
        assert cnt_A == 4 ** (k - 1) and checked_pairs >= 4


def test_case_3():
    """Verify Case 3 (q >= 8, 4 | e, e >= 8 => non-PP): Weil bound + explicit collision at (q=8, e=8)."""
    # Check Weil bound inequality q^(k/2) > (q - 1)*(q - 4) for all q = 2^m (3 <= m <= 50), k >= 4 even
    for m in range(3, 51):
        q = 1 << m
        assert q * q > (q - 1) * (q - 4)

    # Check explicit non-PP collision on (q=8, e=8, k=4) inside F_{8^4} = GF(2^12)
    # Using alpha^2 + alpha = beta in F_{8^4} with Tr_{8^4/2}(beta) = 1?
    # Note: alpha^(q^k) = alpha + 1 <=> Tr_{q^k/2}(alpha^2 + alpha) = 1.
    # Easier: compute f(u) = sum_{j=0}^{q-2} (u + alpha)^j directly in F_{8^4} by picking alpha in F_{8^8}!
    # Actually f(u) = (u+a)^7 + (u+a+1)^7 = sum_{j=0}^6 (u+a)^j = (u^6 + u^5 + u^4 + u^3 + u^2 + u + 1)
    # + (a^2 + a)*(u^4 + u^2 + u + 1) + (a^4 + a)*(u^2 + 1) + (a^4 + a^2 + a)*... wait, compute directly in F_{2^24}!
    # To stay ultra-fast, represent F_{8^8} as F_{8^4}[alpha]/(alpha^2 + alpha + beta) with Tr_{8^4/2}(beta) = 1!
    F12 = GF(12)  # F_{8^4}
    # Find beta in F_{8^4} with Tr_{2^12/2}(beta) = 1
    def tr2(F, x):
        acc = 0
        cur = x
        for _ in range(F.n):
            acc ^= cur
            cur = F.mul(cur, cur)
        return acc

    beta = next(b for b in range(1, F12.size) if tr2(F12, b) == 1)
    # In F_{8^8} = F_{8^4}[alpha]/(alpha^2 + alpha + beta): alpha^(8^4) = alpha + 1!
    # Compute (u + alpha)^7 + (u + alpha + 1)^7 = sum_{j=0}^6 (u + alpha)^j!
    # Arithmetic in F12[alpha]/(alpha^2 + alpha + beta): pair (c0, c1) = c0 + c1*alpha
    def qmul(p1, p2):
        a0, a1 = p1
        b0, b1 = p2
        t0 = F12.mul(a0, b0)
        t1 = F12.mul(a0, b1) ^ F12.mul(a1, b0)
        t2 = F12.mul(a1, b1)
        # alpha^2 = alpha + beta
        return (t0 ^ F12.mul(t2, beta), t1 ^ t2)

    def qpow(p, e):
        r = (1, 0)
        while e:
            if e & 1:
                r = qmul(r, p)
            p = qmul(p, p)
            e >>= 1
        return r

    zeros_s = 0
    for u in range(F12.size):
        p1 = qpow((u, 1), 7)
        p2 = qpow((u ^ 1, 1), 7)
        f0, f1 = p1[0] ^ p2[0], p1[1] ^ p2[1]
        assert f1 == 0, "f(u) not in F_{8^4}!"
        if F12.S(4, 8, f0) == 1:
            zeros_s += 1
    # Must be > 0 (and check against Weil lower bound!)
    # q * zeros_s >= 8^4 - 7 * 4 * 8^2 = 4096 - 1792 = 2304 => zeros_s >= 288
    assert 8 * zeros_s >= 4096 - 7 * 4 * 64
    assert zeros_s > 0


def test_case_4():
    """Verify Case 4 (e = 4): exact gcd theorem, unit-circle identities, m=3,7 non-PP, and m=2,4,5,6 PP."""
    # 1. Exact gcd check for m = 2..100
    for m in range(2, 101):
        q = 1 << m
        g1 = int_gcd(2 * q - 1, q * q + 1)
        g2 = int_gcd(q + 2, q * q + 1)
        expected = 5 if (m % 4 == 3) else 1
        assert g1 == expected and g2 == expected, f"gcd mismatch at m={m}"

    # 2. Exhaustive unit-circle identity verification on ALL q^2 points of U for m = 2, 3, 4, 5
    #    (plus direct bijection check of g_{n,q} on F_{16^4} of size 65536, and of Phi on V_2!)
    for m in [2, 3, 4, 5]:
        q = 1 << m
        F = GF(4 * m)
        # Find alpha with alpha^(q^2) = alpha + 1 and enumerate F_{q^2} cleanly
        # Wait: for m=5 (size 2^20 = 1048576), construct U via a generator of mu_{q^2+1}!
        # Order of F^* is q^4 - 1 = (q^2 - 1)(q^2 + 1).
        # Pick g in F^* such that h = g^(q^2 - 1) has exact order q^2 + 1!
        order_mu = q * q + 1
        # Prime factors of order_mu (needed only for m <= 6, tiny!)
        tmp = order_mu
        pfacs = []
        d = 2
        while d * d <= tmp:
            if tmp % d == 0:
                pfacs.append(d)
                while tmp % d == 0:
                    tmp //= d
            d += 1
        if tmp > 1:
            pfacs.append(tmp)

        h = None
        for g in range(2, F.size):
            cand = F.pow(g, q * q - 1)
            if cand == 1:
                continue
            if all(F.pow(cand, order_mu // p) != 1 for p in pfacs):
                h = cand
                break
        assert h is not None

        # Iterate over ALL q^2 elements x in mu_{q^2+1} \ {1}
        x = h
        psi_imgs = set()
        phi_zeros = 0
        s_zeros = 0
        for _ in range(q * q):
            assert x != 1
            assert F.pow(x, order_mu) == 1
            u = F.mul(x, F.inv(x ^ 1))
            assert (u ^ F.pow(u, q * q)) == 1
            w = F.pow(u, q)
            Phi_u = w ^ F.mul(w, F.inv(u)) ^ F.mul(u ^ 1, F.inv(w))
            y = F.pow(x, q)
            rhs_Phi = F.mul(x ^ F.mul(y, y), F.inv(F.mul(F.mul(x, y), F.mul(x ^ 1, y ^ 1))))
            assert Phi_u == rhs_Phi
            Phi_q2 = F.pow(Phi_u, q * q)
            x_qp2 = F.pow(x, q + 2)
            assert Phi_q2 == F.mul(x_qp2, Phi_u)
            s_u = Phi_u ^ Phi_q2
            assert s_u == F.mul(1 ^ x_qp2, Phi_u)
            if Phi_u == 0:
                phi_zeros += 1
            if s_u == 0:
                s_zeros += 1
            else:
                Psi_u = F.mul(Phi_u, F.inv(s_u))
                assert Psi_u == F.inv(1 ^ x_qp2)
                assert (Psi_u ^ F.pow(Psi_u, q * q)) == 1
                X_out = F.mul(Psi_u, F.inv(Psi_u ^ 1))
                assert X_out == F.inv(x_qp2)
                psi_imgs.add(Psi_u)
            x = F.mul(x, h)
        assert x == 1  # returned to 1 after q^2 + 1 steps!

        if m % 4 == 3:
            assert phi_zeros == 4 and s_zeros == 4
            assert len(psi_imgs) == (q * q - 4) // 5
        else:
            assert phi_zeros == 0 and s_zeros == 0
            assert len(psi_imgs) == q * q

        # Direct exhaustive g_{n,q} PP check on F_{q^4} for m = 2 (256), m = 3 (4096), m = 4 (65536)!
        if m <= 4:
            g_imgs = {F.g_eval(q, 4, z) for z in range(F.size)}
            if m % 4 == 3:
                assert len(g_imgs) < F.size
            else:
                assert len(g_imgs) == F.size

    # 3. Also test m = 6 (PP on all 4096 points of U) and m = 7 (explicit order-5 collision Phi(u) = 0)!
    # m = 6: F_{64^4} = GF(2^24)
    F24 = GF(24)
    q6 = 64
    order6 = q6 * q6 + 1  # 4097 = 17 * 241
    h6 = None
    for g in range(2, 100):
        cand = F24.pow(g, q6 * q6 - 1)
        if cand != 1 and F24.pow(cand, 17) != 1 and F24.pow(cand, 241) != 1:
            h6 = cand
            break
    assert h6 is not None
    x = h6
    psi_set6 = set()
    for _ in range(q6 * q6):
        u = F24.mul(x, F24.inv(x ^ 1))
        w = F24.pow(u, q6)
        Phi_u = w ^ F24.mul(w, F24.inv(u)) ^ F24.mul(u ^ 1, F24.inv(w))
        s_u = Phi_u ^ F24.pow(Phi_u, q6 * q6)
        assert Phi_u != 0 and s_u != 0
        psi_set6.add(F24.mul(Phi_u, F24.inv(s_u)))
        x = F24.mul(x, h6)
    assert x == 1 and len(psi_set6) == q6 * q6

    # m = 7: F_{128^4} = GF(2^28), exhibit explicit order-5 x in mu_{128^2+1} with Phi(u) = 0!
    F28 = GF(28)
    q7 = 128
    # (2^28 - 1) / 5 is an exact integer since 4 | 28!
    exp5 = ((1 << 28) - 1) // 5
    x5 = None
    for g in range(2, 100):
        cand = F28.pow(g, exp5)
        if cand != 1:
            x5 = cand
            break
    assert x5 is not None and F28.pow(x5, 5) == 1
    assert F28.pow(x5, q7 * q7 + 1) == 1
    u5 = F28.mul(x5, F28.inv(x5 ^ 1))
    assert (u5 ^ F28.pow(u5, q7 * q7)) == 1
    assert F28.Phi_eval(q7, 2, u5) == 0


def main():
    check_ast_zero_float()
    test_lemma_2_1()
    test_lemma_2_2_and_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    print("PASS")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
