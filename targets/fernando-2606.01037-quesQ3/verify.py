#!/usr/bin/env python3
"""Exact-arithmetic verification for fernando-2606.01037-quesQ3 (Question 6.3).

Zero floats, zero true-division (`/`). Uses exact GF(2) polynomial arithmetic
and discrete-log tables over GF(2^d). Prints PASS iff every check succeeds.
"""

import sys


def gf_mul(a, b, mod, deg):
    res = 0
    while b:
        if b & 1:
            res ^= a
        b >>= 1
        a <<= 1
        if a & (1 << deg):
            a ^= mod
    return res


def gf_pow(a, e, mod, deg):
    res = 1
    while e:
        if e & 1:
            res = gf_mul(res, a, mod, deg)
        a = gf_mul(a, a, mod, deg)
        e >>= 1
    return res


def poly_mod_2(a, b):
    db = b.bit_length() - 1
    while a.bit_length() - 1 >= db:
        a ^= b << (a.bit_length() - 1 - db)
    return a


def poly_gcd_2(a, b):
    while b:
        a, b = b, poly_mod_2(a, b)
    return a


def find_irred(deg):
    for p in range((1 << deg) + 1, 1 << (deg + 1), 2):
        cur = 2
        ok = True
        for i in range(1, deg + 1):
            cur = gf_mul(cur, cur, p, deg)
            if i < deg and deg % i == 0:
                if poly_gcd_2(cur ^ 2, p) != 1:
                    ok = False
                    break
        if ok and cur == 2:
            return p
    raise RuntimeError("No irreducible polynomial found")


class GF2Ext:
    """Exact finite field GF(2^deg) with log/exp tables."""

    def __init__(self, deg):
        self.deg = deg
        self.size = 1 << deg
        self.order = self.size - 1
        self.mod = find_irred(deg)
        # Factor order
        fs = set()
        tmp = self.order
        d = 2
        while d * d <= tmp:
            while tmp % d == 0:
                fs.add(d)
                tmp //= d
            d += 1
        if tmp > 1:
            fs.add(tmp)
        g = 2
        while any(gf_pow(g, self.order // f, self.mod, deg) == 1 for f in fs):
            g += 1
        self.exp_tbl = [0] * (2 * self.order)
        self.log_tbl = [0] * self.size
        v = 1
        for i in range(self.order):
            self.exp_tbl[i] = v
            self.exp_tbl[i + self.order] = v
            self.log_tbl[v] = i
            v = gf_mul(v, g, self.mod, deg)

    def mul(self, a, b):
        if a == 0 or b == 0:
            return 0
        return self.exp_tbl[self.log_tbl[a] + self.log_tbl[b]]

    def inv(self, a):
        if a == 0:
            raise ZeroDivisionError
        return self.exp_tbl[self.order - self.log_tbl[a]]

    def pow(self, a, e):
        if a == 0:
            return 1 if e == 0 else 0
        return self.exp_tbl[(self.log_tbl[a] * (e % self.order)) % self.order]

    def build_linear_table(self, fn_on_basis):
        tbl = [0] * self.size
        for bit in range(self.deg):
            val = fn_on_basis(1 << bit)
            step = 1 << bit
            for x in range(step):
                tbl[x | step] = tbl[x] ^ val
        return tbl

    def S_k(self, x, q, k):
        res = 0
        cur = x
        for _ in range(k):
            res ^= cur
            cur = self.pow(cur, q)
        return res


def check_g_nq_direct(m, e, expect_pp):
    """Exhaustively check g_{n,q} on GF(q^e) using exact arithmetic."""
    q = 1 << m
    k = e >> 1
    deg = m * e
    F = GF2Ext(deg)
    # Precompute S_k, S_{k+1}^{q^k}, S_e, and S_k^{q^k} as linear tables
    Sk_tbl = F.build_linear_table(lambda b: F.S_k(b, q, k))
    qk = 1 << (m * k)
    Sk_qk_tbl = F.build_linear_table(lambda b: F.pow(F.S_k(b, q, k), qk))
    Sk1_qk_tbl = F.build_linear_table(lambda b: F.pow(F.S_k(b, q, k + 1), qk))
    Se_tbl = F.build_linear_table(lambda b: F.S_k(b, q, e))

    seen = bytearray(F.size)
    exp_tbl = F.exp_tbl
    log_tbl = F.log_tbl
    order = F.order
    qm1 = q - 1

    # Check g_{n,q}(0) == 0 and for odd k, g_{n,q}(1) == 0
    def eval_g(x):
        se = Se_tbl[x]
        term3 = 0
        if se:
            z = Sk_qk_tbl[x]
            if z:
                term3 = exp_tbl[(log_tbl[se] + log_tbl[z] * qm1) % order]
        return Sk1_qk_tbl[x] ^ se ^ term3

    assert eval_g(0) == 0
    if k % 2 == 1:
        assert eval_g(1) == 0

    count = 0
    for x in range(F.size):
        y = eval_g(x)
        if not seen[y]:
            seen[y] = 1
            count += 1
    is_pp = (count == F.size)
    assert is_pp == expect_pp, f"Mismatch for (q={q}, e={e}): got {is_pp}, expected {expect_pp}"
    print(f"  [OK] Direct g_{{n,q}} on GF({q}^{e}) ({F.size} elems): PP={is_pp} (image={count})")


def check_q4_identities(e):
    """Verify Theorem 3.1 identities for q=4, 4|e."""
    q = 4
    k = e >> 1
    F = GF2Ext(2 * e)
    qk = 1 << (2 * k)
    # Find omega in GF(4) \ GF(2)
    omega = None
    for x in range(2, F.size):
        if F.mul(x, x) ^ x == 1:
            omega = x
            break
    assert omega is not None
    omega2 = F.mul(omega, omega)

    # Check Q(A)^2 + Q(A) + omega^2 A == 1 for every A in GF(4^k) with S_k(A) == omega
    Sk_tbl = F.build_linear_table(lambda b: F.S_k(b, q, k))
    # Elements of GF(4^k) satisfy x^{4^k} == x
    # Sample/enumerate GF(4^k)
    checked_A = 0
    for A in range(F.size):
        if F.pow(A, qk) != A:
            continue
        if Sk_tbl[A] != omega:
            continue
        # Compute X_j = A^{4^j}
        Xs = [0] * k
        cur = A
        for j in range(k):
            Xs[j] = cur
            cur = F.pow(cur, 4)
        Q = 0
        for i in range(1, k):
            for j in range(i):
                Q ^= F.mul(Xs[i], F.mul(Xs[j], Xs[j]))
        lhs = F.mul(Q, Q) ^ Q ^ F.mul(omega2, A)
        assert lhs == 1, f"Q(A) identity failed for e={e}"
        checked_A += 1
    assert checked_A == (1 << (2 * k - 2))
    print(f"  [OK] Theorem 3.1 Q(A)^2 + Q(A) + omega^2 A = 1 verified on all {checked_A} A in GF(4^{k}) (e={e})")


def check_regime3_carlitz_uchiyama():
    """Verify Theorem 4.1 at (q=8, e=8): s(u+alpha)=0 count >= q(5q-4)=288."""
    m = 3
    q = 8
    k = 4
    # Work in GF(8^4) = GF(2^12) for u, and we only need alpha^2 + alpha in GF(8^4)?
    # Better: work directly in GF(8^8) = GF(2^24)? Too big for log table.
    # Instead, f(u) = (u+alpha)^7 + (u+alpha+1)^7 has coefficients in GF(8^4) = GF(2^12)!
    # Note: alpha^{q^k} = alpha + 1 means alpha^2 + alpha = c0 in GF(q^k) with Tr_{q^k/2}(c0) = 1.
    # Let's express alpha^r + (alpha+1)^r in terms of c0 = alpha^2 + alpha directly!
    # r=0: 0
    # r=1: 1
    # r=2: 1
    # r=3: alpha^2 + alpha + 1 = c0 + 1
    # r=4: 1
    # r=5: alpha^4 + alpha + 1 = (c0 + alpha)^2 + alpha + 1 = c0^2 + c0 + 1
    # r=6: (alpha^2 + alpha + 1)^? Wait: (a+1)^6 + a^6 = (a^2+1)(a^4+1) + a^6 = a^4 + a^2 + 1 = c0^2 + 1!
    # r=7: (a+1)^7 + a^7 = a^6 + a^5 + a^4 + a^3 + a^2 + a + 1
    #      = (a^2+a)^3 + (a^2+a)^2 + (a^2+a) + 1 + a^4 + a^2? Let's verify in GF(2)[a] first!
    # Check exact expansion of (a+1)^r + a^r in terms of c0 = a^2 + a:
    def poly_in_c0_check():
        # Represent polynomials in a as bitmasks; c0 = a^2 + a = 0b110
        def pmul(x, y):
            r = 0
            while y:
                if y & 1:
                    r ^= x
                y >>= 1
                x <<= 1
            return r
        def ppow(x, n):
            r = 1
            while n:
                if n & 1:
                    r = pmul(r, x)
                x = pmul(x, x)
                n >>= 1
            return r
        c0 = 0b110  # a^2 + a
        c0_2 = pmul(c0, c0)
        c0_3 = pmul(c0_2, c0)
        exprs = {
            0: 0,
            1: 1,
            2: 1,
            3: c0 ^ 1,
            4: 1,
            5: c0_2 ^ c0 ^ 1,
            6: c0_2 ^ 1,
            7: c0_3 ^ c0 ^ 1,
        }
        for r, val in exprs.items():
            actual = ppow(0b11, r) ^ (1 << r)
            assert actual == val, f"Mismatch at r={r}: {bin(actual)} vs {bin(val)}"

    poly_in_c0_check()

    F = GF2Ext(12)  # GF(8^4)
    # Find c0 in GF(8^4) with Tr_{8^4/2}(c0) = 1
    Tr2_tbl = F.build_linear_table(lambda b: F.S_k(b, 2, 12))
    Trq_tbl = F.build_linear_table(lambda b: F.S_k(b, 8, 4))
    c0 = next(x for x in range(1, F.size) if Tr2_tbl[x] == 1)
    c0_2 = F.mul(c0, c0)
    c0_3 = F.mul(c0_2, c0)
    coeffs = [
        c0_3 ^ c0 ^ 1,    # u^0 (r=7)
        c0_2 ^ 1,         # u^1 (r=6)
        c0_2 ^ c0 ^ 1,    # u^2 (r=5)
        1,                # u^3 (r=4)
        c0 ^ 1,           # u^4 (r=3)
        1,                # u^5 (r=2)
        1,                # u^6 (r=1)
    ]
    N0 = 0
    for u in range(F.size):
        # Horner evaluation of f(u)
        val = 0
        for coeff in reversed(coeffs):
            val = F.mul(val, u) ^ coeff
        if Trq_tbl[val] == 1:
            N0 += 1
    lb = q * (5 * q - 4)
    assert N0 >= lb, f"N0={N0} < bound {lb}"
    print(f"  [OK] Theorem 4.1 at (q=8, e=8): exact N0={N0} >= Carlitz-Uchiyama lower bound {lb}")


def check_e4_N_identity_and_moment():
    """Verify Proposition 5.1 (N(w) formula) and Theorem 5.5 (sum_{H1} N(w)^{3(q-1)} = 1)."""
    # Part A: Check N(w) = Phi(z)*Phi(z+1) on ALL z in A_1 for m = 2, 3, 4 (GF(q^4))
    for m in [2, 3, 4]:
        q = 1 << m
        q2 = q * q
        F4 = GF2Ext(4 * m)  # GF(q^4)
        # Find alpha with alpha^{q^2} + alpha = 1
        alpha = None
        for x in range(1, F4.size):
            if F4.pow(x, q2) ^ x == 1:
                alpha = x
                break
        assert alpha is not None
        # Enumerate u in GF(q^2): u^{q^2} == u
        checked = 0
        for u in range(F4.size):
            if F4.pow(u, q2) != u:
                continue
            z = u ^ alpha
            y = F4.pow(z, q)
            # Phi(z) = 1 + y + y/z + (z+1)/y
            phi_z = 1 ^ y ^ F4.mul(y, F4.inv(z)) ^ F4.mul(z ^ 1, F4.inv(y))
            phi_z1 = F4.pow(phi_z, q2)
            prod = F4.mul(phi_z, phi_z1)
            w = F4.mul(z, z) ^ z
            wq = F4.pow(w, q)
            Tw = F4.S_k(w, 2, m)
            Sw = 1 ^ F4.mul(Tw, F4.inv(w))
            Nw = wq ^ Sw ^ F4.mul(w ^ 1, F4.inv(wq))
            assert prod == Nw, f"N(w) mismatch at m={m}"
            checked += 1
        assert checked == q2
        print(f"  [OK] Prop 5.1 N(w) = Phi(z)Phi(z+1) verified on all {checked} z in A_1 (m={m}, q={q})")

    # Part B: Direct exact sum_{w in H1} N(w)^{3(q-1)} for m = 2..8
    for m in range(2, 9):
        q = 1 << m
        F2 = GF2Ext(2 * m)
        T_tbl = F2.build_linear_table(lambda b: F2.S_k(b, 2, m))
        Wq_tbl = F2.build_linear_table(lambda b: F2.pow(b, q))
        exp_tbl = F2.exp_tbl
        log_tbl = F2.log_tbl
        order = F2.order
        E = 3 * (q - 1)
        tot = 0
        h1_cnt = 0
        for w in range(1, F2.size):
            Tw = T_tbl[w]
            wq = Wq_tbl[w]
            if (Tw ^ T_tbl[wq]) != 1:
                continue
            h1_cnt += 1
            lw = log_tbl[w]
            lwq = log_tbl[wq]
            Sw = 1 ^ (exp_tbl[log_tbl[Tw] + order - lw] if Tw else 0)
            Rw = exp_tbl[log_tbl[w ^ 1] + order - lwq] if (w ^ 1) else 0
            Nw = wq ^ Sw ^ Rw
            if Nw:
                tot ^= exp_tbl[(log_tbl[Nw] * E) % order]
        assert h1_cnt == (q * q) // 2
        expected = 0 if m == 2 else 1
        assert tot == expected, f"Moment mismatch at m={m}: got {tot}, expected {expected}"
        print(f"  [OK] Direct sum_{{w in H1}} N(w)^{{3(q-1)}} = {tot} (expected {expected}) for m={m} (q={q})")


def check_four_piece_proof_structure():
    """Verify every intermediate claim of Theorem 5.5 for m = 3, 4, 5, 6, 7."""
    def pmul(p1, p2):
        r = 0
        while p2:
            if p2 & 1:
                r ^= p1
            p2 >>= 1
            p1 <<= 1
        return r

    def ppow(p, e):
        r = 1
        while e:
            if e & 1:
                r = pmul(r, p)
            p = pmul(p, p)
            e >>= 1
        return r

    def w2(n):
        return bin(n).count("1")

    def bits_of(n):
        return [i for i in range(n.bit_length()) if (n >> i) & 1]

    for m in [3, 4, 5, 6, 7]:
        q = 1 << m
        ord_m = q * q - 1

        # 1. Verify M1_rem = (T(x) + w) * S(x)^2 identity in F_2[w]/(w^{q^2-1} - 1)
        def xor_set(s, e):
            e %= ord_m
            if e in s:
                s.remove(e)
            else:
                s.add(e)

        Sq2 = [(q * (2 * ((1 << r) - 1))) % ord_m for r in range(1, m)]
        Tx_w = [1] + [(q * (1 << s)) % ord_m for s in range(m)]
        M1_actual = set()
        for u in Tx_w:
            for v in Sq2:
                xor_set(M1_actual, u + v)

        P2_mult = []
        for t in range(3, m + 1):
            P2_mult.append((0, (1 << t) - 2))
        for t in range(2, m + 1):
            P2_mult.append((0, (1 << t) - 1))
        for t in range(2, m + 1):
            P2_mult.append((0, 1 << t))
        P2_mult.append((1, q - 2))
        M1_formula = set((al + q * be) % ord_m for al, be in P2_mult)
        assert M1_actual == M1_formula, f"M1_rem identity failed at m={m}"

        # 2. Verify Piece I, II, III, IV exact parities, zero carries, and upper-triangularity
        L_poly = 0
        for r in range(1, m):
            L_poly |= 1 << (1 << r)
        Lp_bit = [ppow(L_poly, 1 << i) for i in range(m)]
        q3 = q - 3
        bits = [i for i in range(m) if (q3 >> i) & 1]

        P1_mult = [(0, 2 * ((1 << r) - 1)) for r in range(1, m)]
        P3_mult = [((1 << j) + 2, 0) for j in range(m)] + [(2, 1 << s) for s in range(m)]
        P4_raw = {}
        for j in range(m):
            for dx in (0, 2):
                key = ((1 << j) - 2 + q * dx) % ord_m
                P4_raw[key] = (P4_raw.get(key, (0, None))[0] ^ 1, ((1 << j) - 2, dx))
        for s in range(m):
            for dx in (0, 2):
                key = (-2 + q * ((1 << s) + dx)) % ord_m
                P4_raw[key] = (P4_raw.get(key, (0, None))[0] ^ 1, (-2, (1 << s) + dx))
        P4_mult = [ab for flag, ab in P4_raw.values() if flag]

        piece_parities = []
        for pname, mult, add1 in [("I", P1_mult, True), ("II", P2_mult, False),
                                  ("III", P3_mult, False), ("IV", P4_mult, False)]:
            parity = 0
            hits = 0

            def dfs(idx, a, b, c, La):
                nonlocal parity, hits
                if idx == len(bits):
                    submasks = []
                    sub = c
                    while True:
                        submasks.append(sub)
                        if sub == 0:
                            break
                        sub = (sub - 1) & c
                    A = a + 1 if add1 else a
                    Poly = pmul(La, L_poly) if add1 else La
                    wA = w2(A)
                    IA = bits_of(A)
                    for al, be in mult:
                        D = b - c + be
                        for k in submasks:
                            N = (a - al - k - q * D) % ord_m
                            if 2 * A <= N <= A * (q // 2):
                                coeff = (Poly >> N) & 1
                                if w2(N) < wA:
                                    raise AssertionError(f"Carry ghost at m={m}, piece {pname}")
                                if coeff:
                                    assert w2(N) == wA
                                    JN = bits_of(N)
                                    assert all(IA[p] + 1 <= JN[p] <= IA[p] + m - 1 for p in range(wA))
                                    assert all(JN[p] <= IA[p + 1] for p in range(wA - 1))
                                    parity ^= 1
                                    hits += 1
                    return
                i = bits[idx]
                bit = 1 << i
                dfs(idx + 1, a | bit, b, c, pmul(La, Lp_bit[i]))
                dfs(idx + 1, a, b | bit, c, La)
                dfs(idx + 1, a, b, c | bit, La)

            dfs(0, 0, 0, 0, 1)
            if pname == "IV":
                assert hits == 0, f"Piece IV had {hits} hits at m={m}"
            piece_parities.append(parity)

        exp_I = (m - 1) & 1
        exp_II = (1 + ((m - 2) * (m - 3)) // 2) & 1
        exp_III = (((m - 3) * (m - 4)) // 2) & 1
        exp_IV = 0
        assert piece_parities == [exp_I, exp_II, exp_III, exp_IV], (
            f"Piece parities mismatch at m={m}: got {piece_parities}, expected {[exp_I, exp_II, exp_III, exp_IV]}"
        )
        assert (sum(piece_parities) & 1) == 1
        print(f"  [OK] Theorem 5.5 four-piece proof verified at m={m} (q={q}): parities={piece_parities}, sum=1")


def main():
    print("1. Direct exhaustive g_{n,q} checks:")
    for (m, e, expect_pp) in [
        (2, 2, False),
        (2, 6, False),
        (3, 2, False),
        (4, 2, False),
        (2, 4, True),
        (2, 8, True),
        (3, 4, False),
        (4, 4, False),
    ]:
        check_g_nq_direct(m, e, expect_pp)

    print("2. Theorem 3.1 (q=4, 4|e) Q(A) identity checks:")
    check_q4_identities(4)
    check_q4_identities(8)

    print("3. Theorem 4.1 (q>=8, e>=8) Carlitz-Uchiyama check:")
    check_regime3_carlitz_uchiyama()

    print("4. Proposition 5.1 and direct Theorem 5.5 moment checks:")
    check_e4_N_identity_and_moment()

    print("5. Theorem 5.5 four-piece structural proof checks:")
    check_four_piece_proof_structure()

    print("PASS")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
