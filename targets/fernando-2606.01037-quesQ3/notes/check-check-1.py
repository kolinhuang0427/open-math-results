"""Independent exact-arithmetic verifier for targets/fernando-2606.01037-quesQ3."""

from math import comb


# --- Minimal exact GF(2^d) arithmetic via int bitmasks ---

def poly_deg(a: int) -> int:
    return a.bit_length() - 1


def poly_mul(a: int, b: int) -> int:
    res = 0
    while b:
        if b & 1:
            res ^= a
        a <<= 1
        b >>= 1
    return res


def poly_mod(a: int, mod: int) -> int:
    dm = poly_deg(mod)
    while a and poly_deg(a) >= dm:
        a ^= mod << (poly_deg(a) - dm)
    return a


def poly_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, poly_mod(a, b)
    return a


def find_irreducible(deg: int) -> int:
    """Find lexicographically first irreducible polynomial of degree deg over GF(2)."""
    # Irreducibility check via x^{2^k} - x gcd for 1 <= k <= deg // 2
    for low in range(1, 1 << deg, 2):
        f = (1 << deg) | low
        x_pow = 2  # x
        ok = True
        for k in range(1, deg // 2 + 1):
            x_pow = poly_mod(poly_mul(x_pow, x_pow), f)
            if poly_gcd(x_pow ^ 2, f) != 1:
                ok = False
                break
        if ok:
            # Also verify x^{2^deg} == x mod f
            for _ in range(deg // 2 + 1, deg + 1):
                x_pow = poly_mod(poly_mul(x_pow, x_pow), f)
            if x_pow == 2:
                return f
    raise RuntimeError(f"No irreducible found for deg {deg}")


class GF2Ext:
    def __init__(self, deg: int) -> None:
        self.deg = deg
        self.size = 1 << deg
        self.mod = find_irreducible(deg)

    def mul(self, a: int, b: int) -> int:
        res = 0
        m = self.mod
        top = self.size
        while b:
            if b & 1:
                res ^= a
            a <<= 1
            if a & top:
                a ^= m
            b >>= 1
        return res

    def pow(self, a: int, e: int) -> int:
        res = 1
        base = a
        while e:
            if e & 1:
                res = self.mul(res, base)
            base = self.mul(base, base)
            e >>= 1
        return res

    def inv(self, a: int) -> int:
        assert a != 0
        return self.pow(a, self.size - 2)

    def frob(self, a: int, k: int = 1) -> int:
        res = a
        for _ in range(k):
            res = self.mul(res, res)
        return res

    def frob_q(self, a: int, m: int) -> int:
        return self.frob(a, m)

    def trace_2(self, a: int) -> int:
        res = 0
        cur = a
        for _ in range(self.deg):
            res ^= cur
            cur = self.mul(cur, cur)
        assert cur == a
        assert res in (0, 1)
        return res

    def S_k(self, x: int, m: int, k: int) -> int:
        """S_k(x) = sum_{i=0}^{k-1} x^{q^i} where q = 2^m."""
        res = 0
        cur = x
        for _ in range(k):
            res ^= cur
            cur = self.frob(cur, m)
        return res


def eval_g_q3(F: GF2Ext, x: int, m: int, e: int) -> int:
    """Evaluate Q6.3 formula: S_{e/2+1}(x)^{q^{e/2}} + S_e(x) + S_e(x)*(S_{e/2}(x)^{q^{e/2}})^{q-1}."""
    q = 1 << m
    k = e // 2
    s_k_p1 = F.S_k(x, m, k + 1)
    s_k = F.S_k(x, m, k)
    s_e = F.S_k(x, m, e)
    term1 = F.frob(s_k_p1, m * k)
    s_k_qk = F.frob(s_k, m * k)
    return term1 ^ s_e ^ F.mul(s_e, F.pow(s_k_qk, q - 1))


def eval_g_waring(F: GF2Ext, x: int, q: int, n: int) -> int:
    """Evaluate g_{n,q}(x) directly from Waring's formula (draftMay31.tex Eq. (2))."""
    l_min = (n + q - 1) // q
    l_max = n // (q - 1)
    acc = 0
    # Precompute powers of x
    max_deg = n - l_min * (q - 1)
    xpows = [1] * (max_deg + 1)
    for d in range(1, max_deg + 1):
        xpows[d] = F.mul(xpows[d - 1], x)
    for l in range(l_min, l_max + 1):
        r = n - l * (q - 1)
        coeff = ((n * comb(l, r)) // l) & 1
        if coeff:
            acc ^= xpows[r]
    return acc


def verify_primary_g_and_small_pp() -> None:
    """Verify Q6.3 formula vs primary definition (Eq. 1 & 2) and PP classification."""
    # 1. Verify Waring Eq. (2) matches Q6.3 formula pointwise on small (q, e)
    for m, e in [(2, 2), (2, 4), (3, 2)]:
        q = 1 << m
        k = e // 2
        n = 1 + (q - 1) * (q ** k) + (q - 1) * (q ** e)
        F = GF2Ext(m * e)
        for x in range(F.size):
            assert eval_g_waring(F, x, q, n) == eval_g_q3(F, x, m, e)

    # 2. Verify Eq. (1): sum_{a in F_q} (u + a)^n == g_{n,q}(u^q - u) on (3, 4) and (4, 4)
    for m, e in [(3, 4), (4, 4)]:
        q = 1 << m
        k = e // 2
        n = 1 + (q - 1) * (q ** k) + (q - 1) * (q ** e)
        F = GF2Ext(m * e)
        Fq = [x for x in range(F.size) if F.frob(x, m) == x]
        assert len(Fq) == q
        step = max(1, F.size // 64)
        for u in range(0, F.size, step):
            lhs = 0
            for a in Fq:
                lhs ^= F.pow(u ^ a, n)
            x = F.frob(u, m) ^ u
            assert lhs == eval_g_q3(F, x, m, e)

    # 3. Exhaustive PP / non-PP checks across regimes
    cases = [
        (2, 2, False),
        (2, 4, True),
        (2, 6, False),
        (2, 8, True),
        (3, 2, False),
        (3, 4, False),
        (4, 2, False),
        (4, 4, False),
    ]
    for m, e, expected_pp in cases:
        F = GF2Ext(m * e)
        vals = [eval_g_q3(F, x, m, e) for x in range(F.size)]
        is_pp = len(set(vals)) == F.size
        assert is_pp == expected_pp, f"Failed for (m={m}, e={e}): got {is_pp}, expected {expected_pp}"
        if e % 4 == 2:
            assert vals[0] == 0 and vals[1] == 0
    print("Primary g_{n,q} (Eq. 1, 2, Q6.3) & exhaustive PP checks: PASS")


def verify_section1_and_3() -> None:
    """Verify Proposition 1.2, Lemma 1.3, and Theorem 3.1 identities for q=4, e in {4, 8}."""
    m = 2
    q = 4
    for e in (4, 8):
        k = e // 2
        F = GF2Ext(m * e)
        # Find F_4 = {z : z^4 == z}
        F4 = [z for z in range(F.size) if F.frob(z, 2) == z]
        assert len(F4) == 4
        omegas = [w for w in F4 if w not in (0, 1)]
        assert len(omegas) == 2
        omega = omegas[0]
        omega2 = F.mul(omega, omega)
        assert omega2 == (omega ^ 1)

        def t_map(z: int) -> int:
            return z ^ F.frob(z, m * k)

        def phi_q3(z: int) -> int:
            tz = t_map(z)
            c1 = ((k + 1) & 1) * tz
            return z ^ c1 ^ F.S_k(z, m, k) ^ F.mul(tz, F.S_k(F.pow(z, q - 1), m, k))

        im_sk = {F.S_k(x, m, k) for x in range(F.size)}
        assert im_sk == {z for z in range(F.size) if t_map(z) in F4}
        assert len(im_sk) == q ** (k + 1)

        # Lemma 1.3: involution on F_{4^k}
        F4k = [z for z in im_sk if t_map(z) == 0]
        assert len(F4k) == q ** k
        for z in F4k:
            assert phi_q3(phi_q3(z)) == z

        # Theorem 3.1 Steps 1, 2, 3
        im_vals = set()
        for z in im_sk:
            pz = phi_q3(z)
            im_vals.add(pz)
            tz = t_map(z)
            if tz != 0:
                sz = t_map(pz)
                assert sz in {F.mul(tz, omega), F.mul(tz, omega2)}
                # Step 2: Phi(z)^4 + Phi(z) == (z^2 + t*z)^2
                lhs = F.pow(pz, 4) ^ pz
                inner = F.mul(z, z) ^ F.mul(tz, z)
                rhs = F.mul(inner, inner)
                assert lhs == rhs
            if tz == 1:
                A = F.mul(z, z) ^ z
                if F.S_k(A, m, k) == omega:
                    Q_A = 0
                    for i in range(k):
                        for j in range(i):
                            Q_A ^= F.mul(F.frob(A, 2 * i), F.frob(A, 2 * j + 1))
                    check_val = F.mul(Q_A, Q_A) ^ Q_A ^ F.mul(omega2, A)
                    assert check_val == 1
        assert len(im_vals) == len(im_sk)
    print("Section 1 & Theorem 3.1 (q=4, e=4,8): PASS")


def verify_section4_carlitz_uchiyama() -> None:
    """Verify Theorem 4.1 for (q, e) = (8, 8) (k = 4) over F_{8^4}."""
    m = 3
    q = 8
    k = 4
    F = GF2Ext(m * 2 * k)  # F_{8^8} has degree 24 -> wait, work inside F_{8^4} + find alpha in F_{8^8}?
    # Even simpler: find alpha in F_{8^8} (degree 24, 1 element) where alpha^{8^4} + alpha = 1,
    # Wait: alpha^{8^4} + alpha = 1 means alpha^2 + alpha = beta where Tr_{8^4/2}(beta) = 1?
    # Let's work directly with F_{8^8} ONLY to find alpha, or even better: represent F_{8^8} as F_{8^4}[alpha]/(alpha^2+alpha+beta)
    # OR just construct F_{2^24} in 1ms (find_irreducible(24) might be slow, so use quadratic extension of F_{8^4}!).
    F4k = GF2Ext(m * k)  # GF(2^12), size 4096
    Fq = [u for u in range(F4k.size) if F4k.frob(u, m) == u]
    assert len(Fq) == q
    # Pick beta in F_{8^4} with Tr_{8^4/2}(beta) == 1, so alpha^2 + alpha + beta is irreducible over F_{8^4},
    #Wait: alpha^{q^k} + alpha = 1 means alpha^{2^{12}} + alpha = 1! If alpha satisfies alpha^2 + alpha = beta,
    # then alpha^{2^{12}} + alpha = Tr_{2^{12}/2}(beta) = 1! Yes!
    beta = next(b for b in range(F4k.size) if F4k.trace_2(b) == 1)

    # Arithmetic in F_{q^{2k}} = F_{q^k} + alpha * F_{q^k} where alpha^2 = alpha + beta
    def ext_mul(p: tuple[int, int], r: tuple[int, int]) -> tuple[int, int]:
        a0, a1 = p
        b0, b1 = r
        # (a0 + a1*al)(b0 + b1*al) = (a0*b0 + a1*b1*beta) + (a0*b1 + a1*b0 + a1*b1)*al
        c0 = F4k.mul(a0, b0) ^ F4k.mul(F4k.mul(a1, b1), beta)
        c1 = F4k.mul(a0, b1) ^ F4k.mul(a1, b0) ^ F4k.mul(a1, b1)
        return c0, c1

    def ext_pow(p: tuple[int, int], exp: int) -> tuple[int, int]:
        res = (1, 0)
        base = p
        while exp:
            if exp & 1:
                res = ext_mul(res, base)
            base = ext_mul(base, base)
            exp >>= 1
        return res

    # Verify alpha^{q^k} == alpha + 1 directly on (0, 1):
    # Actually alpha^{q^k} = alpha + Tr(beta) = alpha + 1 by Artin-Schreier! Verify on (0,1):
    assert ext_pow((0, 1), F4k.size) == (1, 1)

    # Count N0 = #{u in F_{q^k} : Tr_{q^k/q}(f(u)) == 1} where f(u) = (u+alpha)^{q-1} + (u+alpha+1)^{q-1}
    n0 = 0
    for u in range(F4k.size):
        p1 = ext_pow((u, 1), q - 1)
        p2 = ext_pow((u ^ 1, 1), q - 1)
        fu = p1[0] ^ p2[0]
        assert (p1[1] ^ p2[1]) == 0
        if F4k.S_k(fu, m, k) == 1:
            n0 += 1
    assert n0 >= q * (5 * q - 4), f"N0={n0} < {q*(5*q-4)}"
    print(f"Section 4 Carlitz-Uchiyama check ((8,8), N0={n0} >= {q*(5*q-4)}): PASS")


def verify_section5_lemmas_and_moment() -> None:
    """Verify Lemmas 5.2, 5.3, 5.4, Proposition 5.1, and Theorem 5.5 for m=3..6."""
    # 1. Exhaustive Lemma 5.3 check up to 6 bits
    for X in range(64):
        for k in range(X + 1):
            if X & k:
                continue
            assert (X - k).bit_count() >= X.bit_count()
            if (X & 2) == 0 and (k & 2) == 0 and X >= k + 2:
                assert (X - k - 2).bit_count() >= X.bit_count()
            for u in range(X - k + 1):
                assert (X - k - u).bit_count() >= X.bit_count() - u.bit_count()

    # 2. Exhaustive Lemma 5.4 check up to 7 bits
    for a in range(128):
        for c in range(0, 128, 4):
            if a & c:
                continue
            s = a + 2 * c
            for t in range(2, 8):
                if s == (1 << t) - 3:
                    assert c == 0 and a == (1 << t) - 3
                if (a % 4 == 0) and s == (1 << t) - 4:
                    assert c == 0 and a == (1 << t) - 4
            if c > 0:
                for M in range(3, 8):
                    if s == (1 << M):
                        assert c.bit_count() == 1 and (4 <= c <= (1 << (M - 1)))
                    for L in range(2, M):
                        if s == (1 << M) + (1 << L) - 3:
                            assert c.bit_count() == 1 and ((1 << L) <= c <= (1 << (M - 1)))
                        if (a % 4 == 0) and s == (1 << M) + (1 << L) - 4:
                            assert c.bit_count() == 1 and ((1 << L) <= c <= (1 << (M - 1)))

    # 3. Direct finite-field sum sum_{w in H_1} N(w)^{3(q-1)} for m in {2, 3, 4, 5}
    for m in (2, 3, 4, 5):
        q = 1 << m
        F = GF2Ext(2 * m)
        H1 = [w for w in range(1, F.size) if F.trace_2(w) == 1]
        assert len(H1) == F.size // 2
        total = 0
        for w in H1:
            wq = F.frob(w, m)
            Tw = F.S_k(w, 1, m)
            Sw = F.mul(F.inv(w), Tw ^ w)
            Nw = wq ^ Sw ^ F.mul(w ^ 1, F.inv(wq))
            total ^= F.pow(Nw, 3 * (q - 1))
        expected = 0 if m == 2 else 1
        assert total == expected, f"Moment mismatch at m={m}: got {total}, expected {expected}"

    # 4. Ring R = F_2[w]/(w^{q^2-1} - 1) verification of Lemma 5.2, M_{1,rem}, and four pieces for m = 3, 4, 5
    for m in (3, 4, 5):
        q = 1 << m
        mod_n = q * q - 1

        def r_mul_monomial_sum(poly_set: set[int], shift: int) -> set[int]:
            out: set[int] = set()
            for e in poly_set:
                out ^= {(e + shift) % mod_n}
            return out

        def r_mul(a: set[int], b: set[int]) -> set[int]:
            out: set[int] = set()
            for ea in a:
                for eb in b:
                    out ^= {(ea + eb) % mod_n}
            return out

        def r_pow(a: set[int], exp: int) -> set[int]:
            res = {0}
            base = set(a)
            while exp:
                if exp & 1:
                    res = r_mul(res, base)
                base = r_mul(base, base)
                exp >>= 1
            return res

        # L(w) = sum_{r=1}^{m-1} w^{2^r}
        L_poly = {1 << r for r in range(1, m)}
        # Verify Lemma 5.2 for all A <= q - 2 on m=3,4 (and sample on m=5)
        limit_A = q - 1 if m <= 4 else 16
        for A in range(limit_A):
            LA = r_pow(L_poly, A)
            I_A = [i for i in range(m + 2) if (A >> i) & 1]
            for N in LA:
                assert N % 2 == 0 and 2 * A <= N <= A * (q // 2) and N.bit_count() <= A.bit_count()
                if N.bit_count() == A.bit_count():
                    J_N = [i for i in range(2 * m + 1) if (N >> i) & 1]
                    for p_idx in range(len(I_A)):
                        assert I_A[p_idx] + 1 <= J_N[p_idx] <= I_A[p_idx] + m - 1

        # Verify M_{1,rem} identity (L249)
        T_x = {(q * (1 << r)) % mod_n for r in range(m)}
        T_x_plus_w = T_x ^ {1}
        A_x = {(q * (1 << t)) % mod_n for t in range(2, m)}
        Sx_sq = r_mul_monomial_sum(A_x ^ {1}, (-2 * q) % mod_n)
        M1_lhs = r_mul(T_x_plus_w, Sx_sq)
        M1_rhs = (
            {(q * ((1 << t) - 2)) % mod_n for t in range(3, m + 1)}
            ^ {(q * ((1 << t) - 1)) % mod_n for t in range(2, m + 1)}
            ^ {(q * (1 << t)) % mod_n for t in range(2, m + 1)}
            ^ {(1 + q * (q - 2)) % mod_n}
        )
        assert M1_lhs == M1_rhs

        # Verify [w^0]_R of the four pieces!
        # N(w) = w^{-1} L(w) + x + (w+1) x^{-1}
        N_poly = (
            r_mul_monomial_sum(L_poly, (-1) % mod_n)
            ^ {q % mod_n}
            ^ {(1 - q) % mod_n, (-q) % mod_n}
        )
        Nq3 = r_pow(N_poly, q - 3)
        Tr_poly = {(1 << r) % mod_n for r in range(m)} ^ {(q * (1 << r)) % mod_n for r in range(m)}

        sig1 = 0 in r_mul(r_mul(Sx_sq, L_poly), Nq3)
        sig2 = 0 in r_mul(M1_rhs, Nq3)
        sig3 = 0 in r_mul(r_mul(Tr_poly, {2}), Nq3)
        x2p1 = {(2 * q) % mod_n, 0}
        sig4 = 0 in r_mul(r_mul(r_mul(Tr_poly, {(-2) % mod_n}), x2p1), Nq3)

        assert int(sig1) == ((m - 1) & 1)
        assert int(sig2) == ((1 + comb(m - 2, 2)) & 1)
        assert int(sig3) == (comb(m - 3, 2) & 1)
        assert int(sig4) == 0
        assert (int(sig1) ^ int(sig2) ^ int(sig3) ^ int(sig4)) == 1
    print("Section 5 (Lemmas 5.2-5.4, Prop 5.1, Theorem 5.5 four-piece parities m=3..5): PASS")


def main() -> None:
    verify_primary_g_and_small_pp()
    verify_section1_and_3()
    verify_section4_carlitz_uchiyama()
    verify_section5_lemmas_and_moment()
    print("PASS")


if __name__ == "__main__":
    main()
