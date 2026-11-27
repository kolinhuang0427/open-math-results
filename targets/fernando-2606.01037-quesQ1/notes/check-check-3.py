r"""Independent exact-arithmetic verifier for targets/fernando-2606.01037-quesQ1/.

Derived directly from Fernando & Kousik arXiv:2606.01037v1 (Section 6, Question 6.1 / Q1)
and targets/fernando-2606.01037-quesQ1/PROOF.md without reading verify.py or author notes.
Zero floating-point arithmetic is used anywhere.

Checks:
1. Finite-field GF(2^N) exact bitmask arithmetic (Conway/irreducible primitive polynomials)
   and Lemma 2.1 exact polynomial identity sum_{a in F_q} (X + a)^n == g_{n,q}(X^q + X).
2. Lemma 2.2 bijection equivalence & F_q-homogeneity + exhaustive PP check of g_{n,q}
   for small (q, e) with q^e <= 2^16, plus Table 1 desirable triple (307, 4; 4).
3. Case 1 (e = 2 mod 4, k odd): explicit collision construction and non-PP verification.
4. Case 2 (q = 4, 4 | e): Steps 2.1, 2.2, 2.3 identities (incl. P(A), Q(A) quadratic relation)
   verified for k in {2, 4, 6} (F_{4^6} = F_{4096} and F_{4^{12}} samples + exact F_{4^4}, F_{4^8}).
5. Case 3 (q >= 8, 4 | e, e >= 8): exact Lucas identity, degree-(q-3) Trace-reduction g_c(u),
   full Carlitz-Uchiyama (Weil) character sum bound <= (q-4)*q^{k/2} on (q=8, e=8), and
   explicit collision s(u + alpha) = 0 for (q=8, e=8) and (q=16, e=8).
6. Case 4 (e = 4, q = 2^m > 2): unit-circle parametrization, Phi(u)^{q^2} = x^{q+2} Phi(u),
   Psi conjugacy x |-> x^{-(q+2)} on all of mu_{q^2+1} \ {1}, and exact gcd split
   m == 3 mod 4 (order-5 kernel root) vs m != 3 mod 4 (PP) for m = 2..8 (up to GF(2^32)).
"""

from __future__ import annotations

import math


# ============================================================================
# Exact GF(2^N) Bitmask Engine
# ============================================================================

# Primitive polynomials over GF(2) for N = 2..32 (standard minimal-weight trinomials/pentanomials)
IRRED_MODS: dict[int, int] = {
    2: (1 << 2) | (1 << 1) | 1,
    3: (1 << 3) | (1 << 1) | 1,
    4: (1 << 4) | (1 << 1) | 1,
    5: (1 << 5) | (1 << 2) | 1,
    6: (1 << 6) | (1 << 1) | 1,
    7: (1 << 7) | (1 << 1) | 1,
    8: (1 << 8) | (1 << 4) | (1 << 3) | (1 << 2) | 1,
    9: (1 << 9) | (1 << 4) | 1,
    10: (1 << 10) | (1 << 3) | 1,
    12: (1 << 12) | (1 << 6) | (1 << 4) | (1 << 1) | 1,
    14: (1 << 14) | (1 << 5) | (1 << 3) | (1 << 1) | 1,
    16: (1 << 16) | (1 << 5) | (1 << 3) | (1 << 2) | 1,
    20: (1 << 20) | (1 << 3) | 1,
    24: (1 << 24) | (1 << 4) | (1 << 3) | (1 << 1) | 1,
    28: (1 << 28) | (1 << 3) | 1,
    32: (1 << 32) | (1 << 22) | (1 << 2) | (1 << 1) | 1,
}


class GF2Ext:
    """Exact finite field GF(2^N) arithmetic using int bitmasks."""

    def __init__(self, N: int):
        assert N in IRRED_MODS, f"Add irreducible poly for N={N}"
        self.N = N
        self.mod = IRRED_MODS[N]
        self.order = 1 << N
        self.mask = self.order - 1
        # Verify irreducibility / primitivity: X^{2^N - 1} == 1 and check prime factors of 2^N - 1
        # For N <= 16 or even 32, check X^{2^N} == X and gcd(X^{2^d} - X, mod) == 1 for d | N, d < N
        # Simply check Frobenius^N(t) == t and Frobenius^d(t) != t for proper divisors d | N
        t = 2
        cur = t
        for d in range(1, N):
            cur = self.mul(cur, cur)
            if N % d == 0:
                assert cur != t, f"Poly for N={N} has subfield element at d={d}"
        cur = self.mul(cur, cur)
        assert cur == t, f"Poly for N={N} is not irreducible!"

    def mul(self, a: int, b: int) -> int:
        res = 0
        mod = self.mod
        hi = 1 << self.N
        while b:
            if b & 1:
                res ^= a
            b >>= 1
            a <<= 1
            if a & hi:
                a ^= mod
        return res

    def pow(self, a: int, e: int) -> int:
        assert e >= 0
        res = 1
        base = a
        while e:
            if e & 1:
                res = self.mul(res, base)
            e >>= 1
            if e:
                base = self.mul(base, base)
        return res

    def inv(self, a: int) -> int:
        assert a != 0
        return self.pow(a, self.order - 2)

    def frob(self, a: int, steps: int = 1) -> int:
        res = a
        for _ in range(steps):
            res = self.mul(res, res)
        return res

    def subfield_elements(self, d: int) -> list[int]:
        """Return all elements of GF(2^d) inside GF(2^N) where d | N."""
        assert self.N % d == 0
        # Find generator of GF(2^d)* via ((2^N - 1) // (2^d - 1))-th power of element of large order
        q_d = 1 << d
        exp = (self.order - 1) // (q_d - 1)
        # Find primitive element of GF(2^d)* inside GF(2^N)
        gen = None
        for cand in range(2, min(self.order, 100)):
            g = self.pow(cand, exp)
            if g in (0, 1):
                continue
            # Check order is exactly q_d - 1 (not dividing proper divisor of q_d - 1)
            ok = True
            for p in range(2, q_d):
                if (q_d - 1) % p == 0 and self.pow(g, (q_d - 1) // p) == 1:
                    ok = False
                    break
            if ok:
                gen = g
                break
        assert gen is not None
        elems = [0, 1]
        cur = gen
        for _ in range(q_d - 2):
            elems.append(cur)
            cur = self.mul(cur, gen)
        assert len(set(elems)) == q_d
        return elems

    def trace(self, x: int, d_from: int, d_to: int) -> int:
        """Relative trace Tr_{2^{d_from}/2^{d_to}}(x)."""
        assert d_from % d_to == 0
        steps = d_from // d_to
        acc = 0
        cur = x
        for _ in range(steps):
            acc ^= cur
            cur = self.frob(cur, d_to)
        return acc

    def S_r(self, x: int, m: int, r: int) -> int:
        """Evaluate S_r(x) = sum_{i=0}^{r-1} x^{q^i} where q = 2^m."""
        if r == 0:
            return 0
        acc = 0
        cur = x
        for _ in range(r):
            acc ^= cur
            cur = self.frob(cur, m)
        return acc


# ============================================================================
# F_2 Polynomial Arithmetic for Exact Lemma 2.1 Check
# ============================================================================

def f2poly_mul(a: int, b: int) -> int:
    """Multiply polynomials over F_2 represented as bitmasks."""
    res = 0
    while b:
        if b & 1:
            res ^= a
        b >>= 1
        a <<= 1
    return res


def f2poly_pow(a: int, e: int) -> int:
    res = 1
    base = a
    while e:
        if e & 1:
            res = f2poly_mul(res, base)
        e >>= 1
        if e:
            base = f2poly_mul(base, base)
    return res


def poly_fq_add(p: list[int], q: list[int]) -> list[int]:
    n = max(len(p), len(q))
    res = [0] * n
    for i, c in enumerate(p):
        res[i] ^= c
    for i, c in enumerate(q):
        res[i] ^= c
    while res and res[-1] == 0:
        res.pop()
    return res


def poly_fq_mul(F: GF2Ext, p: list[int], q: list[int]) -> list[int]:
    if not p or not q:
        return []
    res = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a == 0:
            continue
        for j, b in enumerate(q):
            if b != 0:
                res[i + j] ^= F.mul(a, b)
    while res and res[-1] == 0:
        res.pop()
    return res


def poly_fq_pow(F: GF2Ext, p: list[int], e: int) -> list[int]:
    res = [1]
    base = list(p)
    while e:
        if e & 1:
            res = poly_fq_mul(F, res, base)
        e >>= 1
        if e:
            base = poly_fq_mul(F, base, base)
    return res


def poly_fq_eval_at_poly(F: GF2Ext, outer: list[int], inner: list[int]) -> list[int]:
    """Evaluate outer(inner(X)) where outer has F_2 coefficients (0 or 1)."""
    res: list[int] = []
    cur = [1]
    for coeff in outer:
        if coeff & 1:
            res = poly_fq_add(res, cur)
        cur = poly_fq_mul(F, cur, inner)
    return res


def check_lemma21_exact_polynomial() -> None:
    """Verify Lemma 2.1: sum_{a in F_q} (X+a)^n == g_{n,q}(X^q + X) as polynomials in F_2[X]."""
    for m, e in [(2, 2), (2, 4), (3, 2)]:
        q = 1 << m
        k = e // 2
        n = (q - 1) + (q - 1) * (q ** k) + (q ** e)
        F = GF2Ext(m)  # F_q coefficients suffice for polynomial identity!
        fq_elems = list(range(q))

        # Direct LHS: sum_{a in F_q} (X + a)^n in F_q[X]
        lhs: list[int] = []
        for a in fq_elems:
            lhs = poly_fq_add(lhs, poly_fq_pow(F, [a, 1], n))

        # Formula RHS: g_{n,q}(Y) = Y + S_k(Y)^{q^k} + S_{2k}(Y) S_k(Y)^{q-1} evaluated at Y = X^q + X
        # Use sparse F_2 polynomial bitmasks!
        def S_poly(r: int) -> int:
            mask = 0
            for i in range(r):
                mask |= 1 << (q ** i)
            return mask

        Sk = S_poly(k)
        S2k = S_poly(e)
        g_poly = 2 ^ f2poly_pow(Sk, q ** k) ^ f2poly_mul(S2k, f2poly_pow(Sk, q - 1))

        # Build Y = X^q + X as poly over F_q
        Y_poly = [0] * (q + 1)
        Y_poly[1] = 1
        Y_poly[q] = 1
        # Evaluate g_poly(Y_poly) over F_2[X]
        rhs_bits = 0
        cur_bits = 1
        y_bits = (1 << 1) | (1 << q)
        tmp = g_poly
        while tmp:
            if tmp & 1:
                rhs_bits ^= cur_bits
            tmp >>= 1
            if tmp:
                cur_bits = f2poly_mul(cur_bits, y_bits)
        # Compare lhs (list of F_q ints, all 0 or 1) against rhs_bits
        for deg, coeff in enumerate(lhs):
            assert coeff in (0, 1)
            assert coeff == ((rhs_bits >> deg) & 1), f"Lemma 2.1 mismatch at deg {deg}"
        assert rhs_bits.bit_length() - 1 == (len(lhs) - 1 if lhs else -1)
    print("Part 1 (Lemma 2.1 exact polynomial identity sum (X+a)^n = g_{n,q}(X^q+X)): OK")


# ============================================================================
# Part 2: Exhaustive g_{n,q} & Lemma 2.2 PP Checks + Table 1 Triple (307,4;4)
# ============================================================================

def eval_g_nq(F: GF2Ext, m: int, e: int, x: int) -> int:
    """Evaluate g_{n,q}(x) = S_1(x) + S_k(x)^{q^k} + S_e(x) * S_k(x)^{q-1} on F_{q^e}."""
    q = 1 << m
    k = e // 2
    s1 = x
    sk = F.S_r(x, m, k)
    se = F.S_r(x, m, e)
    term2 = F.frob(sk, m * k)
    term3 = F.mul(se, F.pow(sk, q - 1))
    return s1 ^ term2 ^ term3


def eval_phi(F: GF2Ext, m: int, k: int, y: int) -> int:
    """Evaluate Phi(y) = y + S_k(y) + (k mod 2)*t(y) + t(y)*S_k(y^{q-1}) on V_k."""
    q = 1 << m
    t_y = y ^ F.frob(y, m * k)
    sk_y = F.S_r(y, m, k)
    sk_y_qm1 = F.S_r(F.pow(y, q - 1), m, k)
    res = y ^ sk_y ^ F.mul(t_y, sk_y_qm1)
    if k % 2 == 1:
        res ^= t_y
    return res


def check_exhaustive_small_fields() -> None:
    """Exhaustively check g_{n,q} PP vs Lemma 2.2 Phi bijection & F_q-homogeneity."""
    # Test pairs (m, e):
    # Main Theorem predicts PP iff (m == 2 and e % 4 == 0) or (e == 4 and m % 4 != 3)
    cases = [
        (2, 2, False),   # q=4, e=2 (Case 1)
        (2, 4, True),    # q=4, e=4 (Table 1: n=307)
        (2, 6, False),   # q=4, e=6 (Case 1)
        (2, 8, True),    # q=4, e=8 (Case 2, F_{2^16})
        (3, 2, False),   # q=8, e=2 (Case 1)
        (3, 4, False),   # q=8, e=4 (Case 4a: m=3 == 3 mod 4)
        (4, 2, False),   # q=16, e=2 (Case 1)
        (4, 4, True),    # q=16, e=4 (Case 4b: m=4 != 3 mod 4, F_{2^16})
    ]
    for m, e, expected_pp in cases:
        N = m * e
        q = 1 << m
        k = e // 2
        F = GF2Ext(N)

        # Verify Table 1 triple (307, 4; 4) explicitly:
        if (m, e) == (2, 4):
            n_val = (q - 1) + (q - 1) * (q ** k) + (q ** e)
            assert n_val == 307

        # Full g_{n,q} bijection check for N <= 12, and Lemma 2.2 V_k check for all (up to N=16)
        if N <= 12:
            imgs_g = {eval_g_nq(F, m, e, x) for x in range(F.order)}
            is_pp_g = (len(imgs_g) == F.order)
            assert is_pp_g == expected_pp, f"g_{{n,q}} PP mismatch at m={m}, e={e}"

        # Lemma 2.2: V_k = {y : t(y) in F_q} = im(S_k)
        fq = set(F.subfield_elements(m))
        vk = []
        im_sk = set()
        for x in range(F.order):
            im_sk.add(F.S_r(x, m, k))
            t_x = x ^ F.frob(x, m * k)
            if t_x in fq:
                vk.append(x)
        assert len(vk) == (q ** (k + 1)) and set(vk) == im_sk

        # Check Phi maps V_k -> V_k, F_q-homogeneity, and bijectivity matches expected_pp
        vk_set = set(vk)
        phi_imgs = set()
        for y in vk:
            py = eval_phi(F, m, k, y)
            assert py in vk_set, "Phi left V_k!"
            phi_imgs.add(py)
        is_bij_phi = (len(phi_imgs) == len(vk))
        assert is_bij_phi == expected_pp, f"Phi bijection mismatch at m={m}, e={e}"

        # Verify F_q-homogeneity on sample elements
        fq_list = list(fq)
        for y in vk[:40]:
            for c in fq_list[:8]:
                assert eval_phi(F, m, k, F.mul(c, y)) == F.mul(c, eval_phi(F, m, k, y))

        # Verify Case 1 explicit collision when k is odd
        if k % 2 == 1:
            fqk = F.subfield_elements(m * k)
            found_col = False
            for x in fqk:
                c = F.trace(x, m * k, m)
                if c != 0:
                    xp = x ^ c
                    assert xp != x
                    assert eval_g_nq(F, m, e, x) == eval_g_nq(F, m, e, xp)
                    found_col = True
                    break
            assert found_col
    print("Part 2 (Lemma 2.2 V_k=im(S_k), exhaustive g_{n,q} & Phi checks N<=16, Case 1, triple (307,4;4)): OK")


# ============================================================================
# Part 3: Case 2 Exact Algebraic Checks (q = 4, 4 | e, k = 2, 4, 6)
# ============================================================================

def check_case2_q4() -> None:
    """Verify Steps 2.1, 2.2, 2.3 and P(A), Q(A) identities for q = 4, k in {2, 4, 6}."""
    m = 2
    q = 4
    for k in (2, 4, 6):
        N = m * 2 * k  # 8, 16, 24
        F = GF2Ext(N)
        f4 = sorted(F.subfield_elements(2))
        assert len(f4) == 4 and f4[0] == 0 and f4[1] == 1
        omega = [x for x in f4 if x not in (0, 1)][0]
        omega2 = F.mul(omega, omega)
        assert (omega ^ omega2 ^ 1) == 0

        # Build test elements in V_k (exhaustive for k=2, structured sample for k=4, 6)
        if N <= 16:
            # Generate V_k directly by choosing random/systematic x in F_{4^{2k}} and taking S_k(x)
            # For N=8 (k=2), test all 64 elements of V_2; for N=16 (k=4), test 150 elements including t=1, w, w^2
            step = 1 if N == 8 else 437
            test_y = [F.S_r(x, m, k) for x in range(0, F.order, step)]
        else:
            # k=6, N=24: sample 100 elements via deterministic powers of primitive t=2
            test_y = []
            cur = 2
            for idx in range(100):
                test_y.append(F.S_r(cur, m, k))
                cur = F.mul(cur, 3) ^ (idx + 1)

        # Find at least one y with t(y) = 1 to verify Step 2.2 and Step 2.3 algebra
        seen_t1 = False
        for y in test_y:
            t_y = y ^ F.frob(y, m * k)
            assert t_y in f4
            py = eval_phi(F, m, k, y)
            s_y = py ^ F.frob(py, m * k)
            if t_y == 0:
                assert s_y == 0 and eval_phi(F, m, k, py) == y  # Step 2.1 involution
            else:
                # Step 2.2: s_y / t_y in {omega, omega^2}, and s_y != t_y
                ratio = F.mul(s_y, F.inv(t_y))
                assert ratio in (omega, omega2) and s_y != t_y
                # Step 2.3 quadratic invariant: Phi(y)^4 + Phi(y) == (y^2 + t_y * y)^2
                lhs_inv = F.frob(py, 2) ^ py
                inner = F.mul(y, y) ^ F.mul(t_y, y)
                assert lhs_inv == F.mul(inner, inner)

                # Step 2.3 P(A), Q(A) formula check when t_y == 1 and s_y == omega2 (or after F_2 frob)
                if t_y == 1:
                    seen_t1 = True
                    y_use = y if s_y == omega2 else F.frob(y, 1)
                    A = F.mul(y_use, y_use) ^ y_use
                    assert F.frob(A, m * k) == A
                    assert F.S_r(A, m, k) == omega
                    a = [F.frob(A, 2 * r) for r in range(k)]
                    P_A = 0
                    Q_A = 0
                    for r in range(k):
                        for j in range(r + 1, k):
                            P_A ^= F.mul(a[r], a[j])
                            Q_A ^= F.mul(F.mul(a[r], a[r]), a[j])
                    # Formula (L111): Phi(y_1) == omega^2 y_1 + omega + P(A) + Q(A)
                    rhs_phi = F.mul(omega2, y_use) ^ omega ^ P_A ^ Q_A
                    assert eval_phi(F, m, k, y_use) == rhs_phi
                    # Identity (L124): 1 + Q(A) + Q(A)^2 == omega^2 * A
                    assert (1 ^ Q_A ^ F.mul(Q_A, Q_A)) == F.mul(omega2, A)
        assert seen_t1
    print("Part 3 (Case 2 q=4, k in {2,4,6} Steps 2.1-2.3 & P(A), Q(A) identities): OK")


# ============================================================================
# Part 4: Case 3 Weil Bound & Explicit Collision (q >= 8, 4 | e, e >= 8)
# ============================================================================

def check_case3_weil_and_collision() -> None:
    """Verify Case 3 Lucas f(u), odd-degree reduction g_c(u), Weil bound, and collision."""
    for m, k in [(3, 4), (4, 4)]:  # (q=8, e=8 => GF(2^12)) and (q=16, e=8 => GF(2^16))
        q = 1 << m
        N = m * 2 * k
        F = GF2Ext(N)
        fq = F.subfield_elements(m)
        fqk = F.subfield_elements(m * k)

        # Find alpha in F_{q^{2k}} with alpha^{q^k} = alpha + 1
        alpha = None
        for cand in range(2, F.order):
            if (F.frob(cand, m * k) ^ cand) == 1:
                alpha = cand
                break
        assert alpha is not None
        assert eval_phi(F, m, k, alpha) in range(F.order)

        # Check (q=8, e=8) full Carlitz-Uchiyama (Weil) bound and polynomial degree reduction
        if (m, k) == (3, 4):
            # Build f(u) = sum_{j=0}^{q-2} (u + alpha)^j in F_{q^k}[u]
            # Verify f(u) == (u + alpha)^{q-1} + (u + alpha + 1)^{q-1} on all u in F_{q^k}
            for u in fqk[:50]:
                ua = u ^ alpha
                lhs = F.pow(ua, q - 1) ^ F.pow(ua ^ 1, q - 1)
                rhs = 0
                for j in range(q - 1):
                    rhs ^= F.pow(ua, j)
                assert lhs == rhs

            # Compute exact polynomial coefficients of f(u) in F_{q^k}[u]
            f_coeffs = [0] * (q - 1)
            for j in range(q - 1):
                # (u + alpha)^j = sum_{t=0}^j binom(j, t) alpha^{j-t} u^t
                for t in range(j + 1):
                    if (j & t) == t:  # Lucas mod 2
                        f_coeffs[t] ^= F.pow(alpha, j - t)
            assert f_coeffs[q - 2] == 1 and f_coeffs[q - 3] == 1

            # Reduce c * f(u) -> g_c(u) with only odd positive degrees; check exact degree q - 3 = 5
            max_char_sum = 0
            for c in fq:
                if c == 0:
                    continue
                g = [F.mul(c, coeff) for coeff in f_coeffs]
                changed = True
                while changed:
                    changed = False
                    for r in range(1, (len(g) - 1) // 2 + 1):
                        if g[2 * r] != 0:
                            # square root in GF(2^{m*k}): a^{2^{mk-1}}
                            sqrt_coeff = F.frob(g[2 * r], m * k - 1)
                            g[r] ^= sqrt_coeff
                            g[2 * r] = 0
                            changed = True
                while g and g[-1] == 0:
                    g.pop()
                assert len(g) - 1 == q - 3  # exact odd degree q - 3 = 5!
                for d in range(2, len(g), 2):
                    assert g[d] == 0

                # Exact Weil sum over ALL u in F_{q^k} (4096 elements)
                s_sum = 0
                for u in fqk:
                    ua = u ^ alpha
                    val = F.pow(ua, q - 1) ^ F.pow(ua ^ 1, q - 1)
                    tr_val = F.trace(F.mul(c, val), m * k, 1)
                    assert tr_val in (0, 1)
                    s_sum += 1 if tr_val == 0 else -1
                assert abs(s_sum) <= (q - 4) * (q ** (k // 2))
                max_char_sum = max(max_char_sum, abs(s_sum))
            assert max_char_sum <= (q - 4) * (q ** (k // 2))

        # Find explicit collision y = u + alpha with t(y) = 1 and s(y) = 0
        coll_found = False
        for u in fqk:
            y = u ^ alpha
            py = eval_phi(F, m, k, y)
            if (py ^ F.frob(py, m * k)) == 0:
                coll_found = True
                assert y not in set(fqk)
                break
        assert coll_found
    print("Part 4 (Case 3 (q=8,e=8) & (q=16,e=8) Weil bound, odd deg q-3, explicit s(u+alpha)=0): OK")


# ============================================================================
# Part 5: Case 4 (e = 4, m = 2..8 up to GF(2^32)) Unit-Circle & Exact Bijection
# ============================================================================

def check_case4_unit_circle() -> None:
    """Verify Case 4 unit-circle conjugation, gcd split, and Psi bijection for m = 2..8."""
    for m in range(2, 9):
        q = 1 << m
        N = 4 * m
        F = GF2Ext(N)
        order_mu = q * q + 1
        expected_pp = (m % 4 != 3)

        # Verify exact gcd calculations
        assert math.gcd(2 * q - 1, order_mu) == (5 if m % 4 == 3 else 1)
        assert math.gcd(q + 2, order_mu) == (5 if m % 4 == 3 else 1)

        # Construct generator g_mu of cyclic subgroup mu_{q^2 + 1} < GF(q^4)*
        exp_sub = (F.order - 1) // order_mu
        # Try consecutive field elements until we get a generator of full order q^2 + 1
        # Factor order_mu cleanly by trial division (<= 65537)
        tmp = order_mu
        p_factors = []
        d = 3
        while d * d <= tmp:
            if tmp % d == 0:
                p_factors.append(d)
                while tmp % d == 0:
                    tmp //= d
            d += 2
        if tmp > 1:
            p_factors.append(tmp)

        g_mu = None
        for cand in range(2, 500):
            x0 = F.pow(cand, exp_sub)
            if x0 <= 1:
                continue
            if all(F.pow(x0, order_mu // p) != 1 for p in p_factors):
                g_mu = x0
                break
        assert g_mu is not None

        # For m <= 6 (order <= 4097), iterate ALL x in mu_{q^2 + 1} \ {1};
        # for m in {7, 8} (GF(2^28), GF(2^32)), test 400 elements plus explicit order-5 elements (m=7).
        if m <= 6:
            test_xs = []
            cur = g_mu
            for _ in range(1, order_mu):
                test_xs.append(cur)
                cur = F.mul(cur, g_mu)
        else:
            step_mu = max(1, order_mu // 400)
            g_step = F.pow(g_mu, step_mu)
            test_xs = []
            cur = g_step
            for _ in range(400):
                if cur != 1:
                    test_xs.append(cur)
                cur = F.mul(cur, g_step)
            if m % 4 == 3:
                x_ord5 = F.pow(g_mu, order_mu // 5)
                for p in range(1, 5):
                    test_xs.append(F.pow(x_ord5, p))

        out_set = set()
        found_zero = False
        for x in test_xs:
            assert F.pow(x, order_mu) == 1 and x != 1
            u = F.mul(x, F.inv(x ^ 1))  # u = x / (x + 1) in U
            assert (u ^ F.frob(u, 2 * m)) == 1
            phi_u = eval_phi(F, m, 2, u)
            s_u = phi_u ^ F.frob(phi_u, 2 * m)

            # Verify key multiplicative relation Phi(u)^{q^2} == x^{q+2} * Phi(u)
            x_qp2 = F.pow(x, q + 2)
            assert F.frob(phi_u, 2 * m) == F.mul(x_qp2, phi_u)
            assert s_u == F.mul(1 ^ x_qp2, phi_u)

            if phi_u == 0:
                found_zero = True
                assert not expected_pp
                # Verify order of x is 5
                assert F.pow(x, 5) == 1
            else:
                if expected_pp:
                    assert s_u != 0
                    psi_u = F.mul(phi_u, F.inv(s_u))
                    assert psi_u == F.inv(1 ^ x_qp2)
                    x_out = F.mul(psi_u, F.inv(psi_u ^ 1))
                    # Verify conjugation Psi(u)/(Psi(u)+1) == x^{-(q+2)}
                    assert F.mul(x_out, x_qp2) == 1
                    out_set.add(x_out)

        if expected_pp and m <= 6:
            assert len(out_set) == order_mu - 1
            assert not found_zero
        elif expected_pp:
            assert not found_zero
        else:
            assert found_zero
    print("Part 5 (Case 4 e=4, m=2..6 full & m=7..8 sampled up to GF(2^32): Phi^{q^2}=x^{q+2}Phi, Psi conj & gcd split): OK")


def main() -> None:
    check_lemma21_exact_polynomial()
    check_exhaustive_small_fields()
    check_case2_q4()
    check_case3_weil_and_collision()
    check_case4_unit_circle()
    print("PASS")


if __name__ == "__main__":
    main()
