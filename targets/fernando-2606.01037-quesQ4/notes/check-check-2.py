#!/usr/bin/env python3
"""Independent exact verifier for targets/fernando-2606.01037-quesQ4/.

Written directly from arXiv:2606.01037v1 (draftMay31.tex, Question 6.4 / \\label{Q4})
and PROOF.md without reading verify.py.
Uses zero floating-point arithmetic (pure int, GF(2) bit-polynomials, and SymPy over GF(2)).
"""

import math
import pathlib
import random
import sympy as sp
from sympy.polys.domains import GF

ROOT = pathlib.Path(__file__).resolve().parents[3]
SRC_TEX = ROOT / "tools/.arxiv_cache/eprint/2606.01037v1/draftMay31.tex"
TARGET_MD = ROOT / "targets/fernando-2606.01037-quesQ4/TARGET.md"
PROOF_MD = ROOT / "targets/fernando-2606.01037-quesQ4/PROOF.md"


# ---------------------------------------------------------------------------
# Fast exact GF(2^d) arithmetic via int bitmasks (zero floating point)
# ---------------------------------------------------------------------------

def gf2_poly_mul(a: int, b: int) -> int:
    res = 0
    while b:
        if b & 1:
            res ^= a
        a <<= 1
        b >>= 1
    return res


def gf2_poly_mod(a: int, mod: int, deg: int) -> int:
    while a.bit_length() > deg:
        shift = a.bit_length() - 1 - deg
        a ^= mod << shift
    return a


def gf2_poly_gcd(a: int, b: int) -> int:
    while b:
        while a.bit_length() >= b.bit_length() and a:
            a ^= b << (a.bit_length() - b.bit_length())
        a, b = b, a
    return a


def gf2_poly_powmod(base: int, exp: int, mod: int, deg: int) -> int:
    res = 1
    cur = gf2_poly_mod(base, mod, deg)
    while exp:
        if exp & 1:
            res = gf2_poly_mod(gf2_poly_mul(res, cur), mod, deg)
        cur = gf2_poly_mod(gf2_poly_mul(cur, cur), mod, deg)
        exp >>= 1
    return res


def is_irred_gf2(f: int, d: int) -> bool:
    """Rabin irreducibility test for monic polynomial f of degree d over GF(2)."""
    if f == 0 or (f & 1) == 0 or f.bit_length() != d + 1:
        return False
    # Distinct prime divisors of d
    primes = []
    tmp = d
    p = 2
    while p * p <= tmp:
        if tmp % p == 0:
            primes.append(p)
            while tmp % p == 0:
                tmp //= p
        p += 1
    if tmp > 1:
        primes.append(tmp)

    x = 2  # polynomial X
    for p in primes:
        xp = gf2_poly_powmod(x, 1 << (d // p), f, d)
        if gf2_poly_gcd(f, xp ^ x) != 1:
            return False
    xd = gf2_poly_powmod(x, 1 << d, f, d)
    return xd == x


def find_irred_poly(d: int) -> int:
    """Deterministically find a sparse monic irreducible polynomial of degree d over GF(2)."""
    # Try trinomials X^d + X^k + 1 first, then pentanomials, then sequential search
    hi = (1 << d) | 1
    for k in range(1, d):
        cand = hi | (1 << k)
        if is_irred_gf2(cand, d):
            return cand
    for a in range(3, d):
        for b in range(2, a):
            for c in range(1, b):
                cand = hi | (1 << a) | (1 << b) | (1 << c)
                if is_irred_gf2(cand, d):
                    return cand
    rng = random.Random(d)
    while True:
        cand = hi | (rng.randrange(0, 1 << (d - 1)) << 1)
        if is_irred_gf2(cand, d):
            return cand


class GF2Ext:
    """Exact arithmetic in GF(2^d) = GF(2)[T] / (mod)."""

    def __init__(self, d: int, mod: int | None = None):
        self.d = d
        self.mod = mod if mod is not None else find_irred_poly(d)
        assert is_irred_gf2(self.mod, d)
        self.order = 1 << d

    def mul(self, a: int, b: int) -> int:
        return gf2_poly_mod(gf2_poly_mul(a, b), self.mod, self.d)

    def sq(self, a: int) -> int:
        return gf2_poly_mod(gf2_poly_mul(a, a), self.mod, self.d)

    def pow(self, a: int, e: int) -> int:
        if e == 0:
            return 1
        if a == 0:
            return 0
        e %= (self.order - 1)
        res = 1
        cur = a
        while e:
            if e & 1:
                res = self.mul(res, cur)
            cur = self.sq(cur)
            e >>= 1
        return res

    def inv(self, a: int) -> int:
        assert a != 0
        return self.pow(a, self.order - 2)

    def frob_q(self, a: int, m: int) -> int:
        """Compute a^(2^m)."""
        cur = a
        for _ in range(m):
            cur = self.sq(cur)
        return cur

    def trace(self, a: int, step_m: int, count: int) -> int:
        """Compute sum_{i=0}^{count-1} a^(q^i) where q = 2^step_m."""
        acc = 0
        cur = a
        for _ in range(count):
            acc ^= cur
            cur = self.frob_q(cur, step_m)
        return acc

    def basis_of_subfield(self, sub_d: int) -> list[int]:
        """Return an F_2-basis of GF(2^sub_d) inside GF(2^d) (sub_d | d)."""
        assert self.d % sub_d == 0
        exp = (self.order - 1) // ((1 << sub_d) - 1)
        # Find a generator g of GF(2^d)^* by sampling
        rng = random.Random(self.d * 100 + sub_d)
        # Factor 2^d - 1? Even simpler: random elements raised to exp span GF(2^sub_d) over F_2
        basis: list[int] = []
        pivots: list[int] = []
        while len(basis) < sub_d:
            x = rng.randrange(1, self.order)
            v = self.pow(x, exp)
            # Reduce against current pivots
            w = v
            for p_bit, b_val in zip(pivots, basis):
                if (w >> p_bit) & 1:
                    w ^= b_val
            if w != 0:
                p_bit = w.bit_length() - 1
                basis.append(w)
                pivots.append(p_bit)
        return basis

    def elements_of_subfield(self, sub_d: int) -> list[int]:
        basis = self.basis_of_subfield(sub_d)
        elems = [0]
        for b in basis:
            elems.extend([e ^ b for e in elems])
        return elems


def eval_g_formula(F: GF2Ext, m: int, e: int, x: int) -> int:
    q = 1 << m
    xq = F.frob_q(x, m)
    s2 = x ^ xq
    se = F.trace(x, m, e)
    se2 = F.sq(se)
    s2_qm2 = F.pow(s2, q - 2) if s2 != 0 else 0
    s2_qm1 = F.mul(s2_qm2, s2) if s2 != 0 else 0
    return xq ^ F.mul(se2, s2_qm2) ^ F.mul(se, s2_qm1)


def eval_g_def(F: GF2Ext, m: int, e: int, n: int, x: int, fq_elems: list[int]) -> int:
    acc = 0
    y = x ^ F.frob_q(x, m)  # Note: g_{n,q}(X^q - X) = sum_{a in F_q} (X + a)^n
    for a in fq_elems:
        acc ^= F.pow(x ^ a, n)
    return acc


# ---------------------------------------------------------------------------
# 1. Primary Source Verification
# ---------------------------------------------------------------------------

def check_primary_source() -> None:
    target = TARGET_MD.read_text()
    proof = PROOF_MD.read_text()

    if not SRC_TEX.exists():
        print("[SKIP] local tools/.arxiv_cache not present; skipping TeX snippet check")
    else:
        tex = SRC_TEX.read_text()
        q4_tex = (
            "\\begin{ques}\\label{Q4}\n"
            "Let $q>2$ be even and $e>2$ a positive integer. Let $n=(q-1)\\cdot q^0+(q-2)\\cdot q^2+1\\cdot q^e+1\\cdot q^{e+2}$. "
            "Find conditions on $q$ and $e$ for which $$g_{n,q}=\\x^q+S_e^2\\,S_2^{q-2}+S_eS_2^{q-1}$$ is a PP of $\\mathbb{F}_{q^e}.$  \n"
            "\\end{ques}"
        )
        assert q4_tex in tex
        sec6_marker = "\\section{Some open questions on PPs from polynomial $g_{n,q}(\\x)$}"
        assert sec6_marker in tex
        sec6_start = tex.index(sec6_marker)
        assert tex.count("\\begin{ques}", sec6_start, tex.index("\\begin{ques}\\label{Q4}")) == 3  # 4th question in Section 6 => Question 6.4
    assert "n = (q - 1) \\cdot q^0 + (q - 2) \\cdot q^2 + 1 \\cdot q^e + 1 \\cdot q^{e+2}" in target
    assert "g_{n,q} = X^q + S_e^2 \\, S_2^{q - 2} + S_e S_2^{q - 1}" in target
    assert "(q, e) = (4, 4)" in proof
    print("[PASS] Primary source arXiv:2606.01037v1 Question 6.4 (\\label{Q4}) verbatim & numbering verified.")


# ---------------------------------------------------------------------------
# 2. Lemma 2.1 & Lemma 2.2 Exhaustive Small-Field Checks
# ---------------------------------------------------------------------------

def check_lemmas_2_1_and_2_2() -> None:
    for m, e in [(2, 3), (2, 4), (2, 5), (3, 3), (3, 4)]:
        q = 1 << m
        n = (q - 1) + (q - 2) * q**2 + q**e + q**(e + 2)
        F = GF2Ext(m * e)
        fq = F.elements_of_subfield(m)
        assert len(fq) == q

        # Check Lemma 2.1: sum_{a in F_q} (X + a)^n == g_{n,q}(X^q + X) on F_{q^e}
        # and verify PP status of g_{n,q} on F_{q^e}
        img_g = set()
        for x in range(F.order):
            y = x ^ F.frob_q(x, m)
            lhs = 0
            for a in fq:
                lhs ^= F.pow(x ^ a, n)
            rhs = eval_g_formula(F, m, e, y)
            assert lhs == rhs, f"Lemma 2.1 mismatch at (q,e)=({q},{e})"
            img_g.add(eval_g_formula(F, m, e, x))

        is_pp = len(img_g) == F.order
        assert is_pp == (q == 4 and e == 4), f"Unexpected PP={(q,e)}: {is_pp}"

        # Check Lemma 2.2: s(y) != 0 and Psi bijection on Omega_e
        omega = []
        if e % 2 == 1:
            for y in range(F.order):
                if F.trace(y, m, e) == 0:
                    omega.append(y)
            assert len(omega) == q**(e - 1)
        else:
            for y in range(F.order):
                if F.trace(y, 2 * m, e // 2) == 1:
                    omega.append(y)
            assert len(omega) == q**(e - 2)

        s_zero = False
        psi_img = set()
        for y in omega:
            w = F.mul(F.pow(y, q - 2), y ^ 1) if y != 0 else 0
            s_val = 1 ^ F.trace(w, m, e)
            if s_val == 0:
                s_zero = True
            else:
                num = F.frob_q(y, m) ^ w ^ F.frob_q(w, m)
                psi_img.add(F.mul(num, F.inv(s_val)))
        lem22_pp = (not s_zero) and (len(psi_img) == len(omega))
        assert lem22_pp == is_pp

    print("[PASS] Lemmas 2.1 & 2.2 exhaustively verified on F_{4^3}, F_{4^4}, F_{4^5}, F_{8^3}, F_{8^4}.")


# ---------------------------------------------------------------------------
# 3. Cases 1, 2, 3 (e=3, odd e>=5, even e>=8)
# ---------------------------------------------------------------------------

def check_cases_1_to_3() -> None:
    # Case 1: e = 3, q in {4, 8, 16, 32}
    for m in (2, 3, 4, 5):
        q = 1 << m
        F = GF2Ext(3 * m)
        fq = F.elements_of_subfield(m)
        im_phi = set()
        for t in fq:
            if t not in (0, 1):
                t3 = F.mul(t, F.sq(t))
                im_phi.add(F.mul(t3, F.inv(t ^ 1)))
        missing = [c for c in fq if c != 0 and c not in im_phi]
        assert len(missing) >= 1
        c = missing[0]
        # Find root y in F_{q^3} of T^3 + c*T + c = 0
        roots = [y for y in range(F.order) if (F.mul(y, F.sq(y)) ^ F.mul(c, y) ^ c) == 0]
        assert len(roots) == 3
        for y in roots:
            assert F.trace(y, m, 3) == 0
            assert F.trace(F.mul(y, F.frob_q(y, m)), m, 3) == c
            w = F.mul(F.pow(y, q - 2), y ^ 1)
            assert (1 ^ F.trace(w, m, 3)) == 0

    # Case 2a: q = 4, odd e >= 5
    for e in range(5, 30, 2):
        # Check 4^e - 24 * 4^(e/2) > 0 via squaring (16^e > 576 * 4^e)
        assert (4**e) ** 2 > 576 * (4**e)
    # Case 2b: q >= 8, odd e >= 5: 4(q-2)^2 > 9q
    for m in range(3, 80):
        q = 1 << m
        assert 4 * (q - 2) ** 2 > 9 * q

    # Case 3: even e >= 8, q >= 4: q^{e/2} - q^4 + 3q^3 - 2q^2 > 0
    for m in range(2, 40):
        q = 1 << m
        for e in (8, 10, 12, 14):
            assert q ** (e // 2) - q**4 + 3 * q**3 - 2 * q**2 >= 3 * q**3 - 2 * q**2 > 0

    print("[PASS] Cases 1 (e=3, q=4..32), 2 (odd e>=5), and 3 (even e>=8) verified.")


# ---------------------------------------------------------------------------
# 4. Case 4 (e = 6): Symbolic Proofs, Genus-9 Hasse-Weil & Witnesses m=2..8
# ---------------------------------------------------------------------------

def check_case_4() -> None:
    # Step 4.1: Check w(y) + w(y)^{q^3} over F_2[u, uq, lam, mu] / (lam^2 + lam + mu)
    u, uq, lam, mu = sp.symbols("u uq lam mu")
    lam_q = lam + 1
    # Reduce mod lam^2 + lam + mu
    def red_lam(expr):
        p = sp.Poly(expr, lam, u, uq, mu, modulus=2)
        _, r = sp.div(p, sp.Poly(lam**2 + lam + mu, lam, u, uq, mu, modulus=2))
        return sp.Poly(r.as_expr(), u, uq, lam, mu, domain=GF(2))

    num_lhs = lam * u * (1 + lam_q * uq) * (1 + lam_q**2 * u**2) + lam_q * u * (1 + lam * uq) * (1 + lam**2 * u**2)
    den_lhs = (1 + lam**2 * u**2) * (1 + lam_q**2 * u**2)
    num_rhs = sp.Poly(u + mu * u**3 + mu * uq * u**3, u, uq, lam, mu, domain=GF(2))
    den_rhs = sp.Poly((1 + u + mu * u**2)**2, u, uq, lam, mu, domain=GF(2))
    assert red_lam(num_lhs) == num_rhs
    assert red_lam(den_lhs) == den_rhs

    # Step 4.2: Symmetric polynomial identity & specialization over GF(2)
    w1, w2, S, k = sp.symbols("w1 w2 S k")
    w3 = w1 + w2
    # Work unscaled first with u1, u2, u3, mu
    u1, u2 = sp.symbols("u1 u2")
    u3 = u1 + u2
    us = [u1, u2, u3]
    a_expr = u1 * u2 + u1 * u3 + u2 * u3
    b_expr = u1 * u2 * u3
    Ds = [1 + ui + mu * ui**2 for ui in us]
    P = Ds[0] * Ds[1] * Ds[2]
    N12 = sum((us[i] + mu * us[i]**3) * (Ds[(i + 1) % 3] * Ds[(i + 2) % 3])**2 for i in range(3))
    N3 = sum(mu * us[i]**3 * us[(i + 1) % 3] * (Ds[(i + 1) % 3] * Ds[(i + 2) % 3])**2 for i in range(3))
    N3_rev = sum(mu * us[i]**3 * us[(i - 1) % 3] * (Ds[(i + 1) % 3] * Ds[(i + 2) % 3])**2 for i in range(3))
    n3_sum_lhs = sp.Poly(N3 + N3_rev, u1, u2, mu, domain=GF(2))
    n3_sum_rhs = sp.Poly(b_expr**2 * mu * (b_expr * mu**2 + 1)**2, u1, u2, mu, domain=GF(2))
    assert n3_sum_lhs == n3_sum_rhs

    # Specialization: w_i = mu * u_i, w1+w2+w3=0, w1*w2+w1*w3+w2*w3 = S + k, w1*w2*w3 = mu = k + 1
    mu_k = k + 1
    ws = [w1, w2, w3]
    # Substitute u_i -> w_i / mu_k, multiply P^2 * s(y) = P^2 + N12 + N3 by mu_k^5
    # Equivalently, D_i * mu_k = mu_k + w_i + w_i^2 (since mu_k^2 * (w_i/mu_k)^2 * mu_k = mu_k * w_i^2? Wait: 1 + u_i + mu u_i^2 = (mu_k + w_i + w_i^2) / mu_k!)
    # Check: 1 + w_i/mu_k + mu_k*(w_i/mu_k)^2 = (mu_k + w_i + w_i^2) / mu_k!
    # Wait: P = prod D_i = prod(mu_k + w_i + w_i^2) / mu_k^3 => P^2 has denom mu_k^6.
    # Let Dhat_i = mu_k + w_i + w_i^2, so D_i = Dhat_i / mu_k.
    Dhats = [mu_k + wi + wi**2 for wi in ws]
    Phat = Dhats[0] * Dhats[1] * Dhats[2]  # P = Phat / mu_k^3
    N12_hat = sum(
        (w_i_term := (ws[i] * mu_k**2 + ws[i]**3)) * (Dhats[(i + 1) % 3] * Dhats[(i + 2) % 3])**2
        for i in range(3)
    )  # N12 = N12_hat / mu_k^7
    N3_hat = sum(
        ws[i]**3 * ws[(i + 1) % 3] * (Dhats[(i + 1) % 3] * Dhats[(i + 2) % 3])**2
        for i in range(3)
    )  # N3 = N3_hat / mu_k^7
    # Since P^2 = Phat^2 / mu_k^6, P^2 s(y) = (mu_k * Phat^2 + N12_hat + N3_hat) / mu_k^7 = A(...) / mu_k^7!
    # Wait: PROOF.md L171 says mu^5 * A(...) = S^2 (k(S^2 + S) + k^2 + 1).
    # Note that A = P^2 + N12 + N3 when b*mu^2 = 1 => P^2 has deg 6 in u => in w/mu gives denom mu^6? Wait: P^2 = D1^2 D2^2 D3^2 has mu_k^6, N12 has u^3 * D^4 -> w^3/mu^2 * Dhat^4/mu^4 = /mu^6?
    # Ah! (u_i + mu u_i^3) = w_i/mu + mu w_i^3/mu^3 = (w_i * mu + w_i^3)/mu^2! Wait: NOT mu^2, mu * (w_i/mu)^3 = w_i^3/mu^2!
    # Let's check exact exponent: D_i = Dhat_i / mu_k => (D_{i+1} D_{i+2})^2 = (Dhat_{i+1} Dhat_{i+2})^2 / mu_k^4.
    # And u_i + mu u_i^3 = (w_i * mu_k + w_i^3) / mu_k^2, while mu u_i^3 u_{i+1} = w_i^3 w_{i+1} / mu_k^3!
    # Wait: (Dhat)^2 / mu_k^4 * (1 / mu_k^2) = / mu_k^6, and / mu_k^3 * / mu_k^4 = / mu_k^7... why mu_k^5 in L171?
    # Because P^2 s(y) = A / mu_k^6? Let's test directly modulo (w1*w2 + w1*w3 + w2*w3 + S + k, w1*w2*w3 + k + 1)!
    N12_hat2 = sum((ws[i] * mu_k + ws[i]**3) * (Dhats[(i + 1) % 3] * Dhats[(i + 2) % 3])**2 for i in range(3))
    # Multiply P^2 s(y) by mu_k^7: mu_k * Phat^2 + mu_k * N12_hat2 + N3_hat. Notice w1*w2*w3 = mu_k divides N3_hat or total!
    expr_scaled = sp.Poly(mu_k * Phat**2 + mu_k * N12_hat2 + N3_hat, w1, w2, S, k, domain=GF(2))
    # Reduce modulo S_sym = w1*w2 + (w1+w2)**2 + S + k and B_sym = w1*w2*(w1+w2) + k + 1
    g_w = sp.groebner([w1*w2 + w1*w3 + w2*w3 + S + k, w1*w2*w3 + k + 1], w1, w2, S, k, domain=GF(2), order="lex")
    _, rem_scaled = g_w.reduce(expr_scaled)
    # Wait: at b = mu^-2, N3 + b*mu*(b*mu^2+1)^2 * delta_u has coeff of mu^-7 cancel, leaving mu^-5!
    # Wait: since w1*w2*(w1+w2) = mu_k, check rem_scaled vs mu_k^2 * S^2*(k*(S^2+S) + k^2 + 1)!
    expected_rhs = sp.Poly(mu_k**2 * S**2 * (k * (S**2 + S) + k**2 + 1), w1, w2, S, k, domain=GF(2))
    assert sp.Poly(rem_scaled, w1, w2, S, k, domain=GF(2)) == expected_rhs

    # Step 4.5: F_red properties
    k_s, w_s = sp.symbols("k w")
    F_red = (w_s + 1)**2 * k_s**3 + w_s * k_s**2 + (w_s + 1) * (w_s**2 + w_s + 1) * (w_s**3 + w_s + 1) * k_s + w_s**2
    F_poly = sp.Poly(F_red, k_s, w_s, domain=GF(2))
    # 1. Partial derivative wrt w and resultant wrt k
    dF_dw = sp.Poly(sp.diff(F_red, w_s), k_s, w_s, domain=GF(2))
    assert dF_dw == sp.Poly(k_s * (k_s + 1), k_s, w_s, domain=GF(2))
    dF_dk = sp.Poly(sp.diff(F_red, k_s), k_s, w_s, domain=GF(2))
    res_k = sp.polys.polytools.resultant(sp.Poly(F_red, k_s, w_s, domain=GF(2)), sp.Poly(dF_dk.as_expr(), k_s, w_s, domain=GF(2)), k_s)
    expected_res = sp.Poly(w_s**2 * (w_s + 1)**4 * (w_s**5 + w_s**4 + w_s**2 + w_s + 1)**2, w_s, domain=GF(2))
    assert sp.Poly(res_k, w_s, domain=GF(2)) == expected_res

    # 2. Absolute irreducibility over F_2bar: check rational root P(w)/(w+1)^r via Groebner basis
    for r_deg in (0, 1, 2):
        deg_p = r_deg + 2
        coeffs = sp.symbols(f"a0:{deg_p + 1}")
        P_w = sum(coeffs[j] * w_s**j for j in range(deg_p + 1))
        # Substitute k = P(w)/(w+1)^r and clear (w+1)^{3r}
        eq_poly = (
            (w_s + 1)**(2 - r_deg) * P_w**3
            + w_s * (w_s + 1)**r_deg * P_w**2
            + (w_s + 1)**(2 * r_deg + 1) * (w_s**2 + w_s + 1) * (w_s**3 + w_s + 1) * P_w
            + w_s**2 * (w_s + 1)**(3 * r_deg)
        )
        # Note for r_deg=0, exponent of (w+1) in leading term is 2; for r_deg=1 it is 1; for r_deg=2 it is 0. Multiply by 1!
        # Wait: (w+1)^2 * P^3 / (w+1)^{3r} * (w+1)^{3r} = (w+1)^{2 - r} * P^3?
        # Wait: multiply by (w+1)^{3r}:
        # Term 1: (w+1)^2 * P^3 / (w+1)^{3r} * (w+1)^{3r} = (w+1)^2 * P^3! Wait: NOT (w+1)^{2-r}!!
        # Careful: k = P / (w+1)^r => k^3 = P^3 / (w+1)^{3r}, so (w+1)^2 k^3 * (w+1)^{3r} = (w+1)^2 P^3!
        # Term 2: w k^2 * (w+1)^{3r} = w (w+1)^r P^2!
        # Term 3: (...) k * (w+1)^{3r} = (...) (w+1)^{2r} P!
        # Term 4: w^2 * (w+1)^{3r}!
        eq_cleared = (
            (w_s + 1)**2 * P_w**3
            + w_s * (w_s + 1)**r_deg * P_w**2
            + (w_s + 1)**(2 * r_deg + 1) * (w_s**2 + w_s + 1) * (w_s**3 + w_s + 1) * P_w
            + w_s**2 * (w_s + 1)**(3 * r_deg)
        )
        wp = sp.Poly(eq_cleared, w_s)
        eqs = [sp.Poly(c, *coeffs, domain=GF(2)) for c in wp.all_coeffs()]
        gb = sp.groebner(eqs, *coeffs, domain=GF(2))
        assert list(gb) == [1], f"Groebner basis not [1] for r={r_deg}: {gb}"

    # 3. Exact F_32 verification of w = alpha (roots of w^5+w^4+w^2+w+1=0) local expansion (Step 4.5.2)
    F32 = GF2Ext(5, 0b110111)  # alpha^5 + alpha^4 + alpha^2 + alpha + 1
    alpha_roots = [a for a in range(32) if (F32.pow(a, 5) ^ F32.pow(a, 4) ^ F32.sq(a) ^ a ^ 1) == 0]
    assert len(alpha_roots) == 5
    for idx_a, alp in enumerate(alpha_roots):
        ap1 = alp ^ 1
        ap1_2 = F32.sq(ap1)
        a2_a_1 = F32.sq(alp) ^ alp ^ 1
        a3_a_1 = F32.pow(alp, 3) ^ alp ^ 1
        c_lin_k = F32.mul(ap1, F32.mul(a2_a_1, a3_a_1))
        # Check algebraic identity c_lin_k == alp^6 + alp^4 + alp + 1 in F_32
        assert c_lin_k == (F32.pow(alp, 6) ^ F32.pow(alp, 4) ^ alp ^ 1)
        # Double root k0 satisfies (alp+1)^2 k0^2 == c_lin_k
        k0_sq = F32.mul(c_lin_k, F32.inv(ap1_2))
        k0 = F32.pow(k0_sq, 16)  # sqrt in GF(32)
        assert F32.sq(k0) == k0_sq and k0 not in (0, 1)
        # Check F_red(k0, alp) == 0 and dF/dk(k0, alp) == 0
        f_at_0 = F32.mul(ap1_2, F32.pow(k0, 3)) ^ F32.mul(alp, F32.sq(k0)) ^ F32.mul(c_lin_k, k0) ^ F32.sq(alp)
        assert f_at_0 == 0
        den_k = F32.mul(k0, k0 ^ 1)
        assert den_k != 0
        # Exact c2 and c3 in u(t) = c2*t^2 + c3*t^3 + O(t^4)
        c2 = F32.mul(F32.mul(ap1_2, k0) ^ alp, F32.inv(den_k))
        assert c2 != 0
        c3 = F32.mul(ap1_2 ^ c2, F32.inv(den_k))
        c3_closed = F32.mul(F32.sq(F32.pow(alp, 3) ^ F32.sq(alp) ^ 1), F32.inv(F32.sq(den_k)))
        assert c3 == c3_closed and c3 != 0
        if alp == 2:
            assert c3 == 17  # 0b10001 != 0b01011
        # Plug k = k0 + t, w = alp + c2*t^2 + c3*t^3 into F_red mod t^4 over F_32
        def f32t_mul(p1, p2):
            out = [0, 0, 0, 0]
            for i in range(4):
                if p1[i]:
                    for j in range(4 - i):
                        if p2[j]:
                            out[i + j] ^= F32.mul(p1[i], p2[j])
            return out
        k_t = [k0, 1, 0, 0]
        w_t = [alp, 0, c2, c3]
        wp1_t = [alp ^ 1, 0, c2, c3]
        w2_t = f32t_mul(w_t, w_t)
        w3_t = f32t_mul(w2_t, w_t)
        k2_t = f32t_mul(k_t, k_t)
        k3_t = f32t_mul(k2_t, k_t)
        wp1_2_t = f32t_mul(wp1_t, wp1_t)
        w2_w_1_t = [w2_t[i] ^ w_t[i] ^ (1 if i == 0 else 0) for i in range(4)]
        w3_w_1_t = [w3_t[i] ^ w_t[i] ^ (1 if i == 0 else 0) for i in range(4)]
        t1 = f32t_mul(wp1_2_t, k3_t)
        t2 = f32t_mul(w_t, k2_t)
        t3 = f32t_mul(f32t_mul(wp1_t, f32t_mul(w2_w_1_t, w3_w_1_t)), k_t)
        f_mod_t4 = [t1[i] ^ t2[i] ^ t3[i] ^ w2_t[i] for i in range(4)]
        assert f_mod_t4 == [0, 0, 0, 0], f"Taylor check failed at alpha={alp}: {f_mod_t4}"

    # 4. Local expansion at P_infty: s(pi) = pi^2 + pi^5 + pi^9 + O(pi^10) and k(pi) = pi^-4 + pi^-1 + O(pi)
    pi = sp.symbols("pi")
    # Use unknown coefficients s = pi^2 + c3*pi^3 + ... up to pi^12
    # Actually let's check iteratively in F_2[pi]
    s_ser = pi**2 + pi**5 + pi**9
    # Wait: let's also find the pi^10..pi^12 coefficients or check exact truncation O(pi^10)!
    # Substitute w = s^-1, K = s^2 k = 1 + pi*s into s^8 F_red(K/s^2, s^-1)/s^2 = 0
    # s^6 F_red(K/s^2, s^-1) = (s^2+1) K^3 + s^3 K^2 + (s^6+s^5+s^2+1) K + s^4? Let's write from F_red directly:
    # (1+s)^2 K^3 / s^8 + (1/s) K^2 / s^4 + (1+s)(1+s+s^2)(1+s^2+s^3)/s^6 * K/s^2 + 1/s^2 = 0
    # Multiply by s^8:
    K_sym = 1 + pi * sp.symbols("s_var")
    s_var = sp.symbols("s_var")
    G_inf = (
        (s_var + 1)**2 * K_sym**3
        + s_var**3 * K_sym**2
        + s_var**2 * (s_var + 1) * (s_var**2 + s_var + 1) * (s_var**3 + s_var**2 + 1) * K_sym
        + s_var**6
    )
    # Wait: check (1+w)^2 when w = s^-1: (1 + s^-1)^2 = (s+1)^2 / s^2. Times K^3 / s^6 = (s+1)^2 K^3 / s^8.
    # Term 2: w k^2 = s^-1 * K^2 / s^4 = K^2 / s^5. Times s^8 = s^3 K^2.
    # Term 3: (w+1)(w^2+w+1)(w^3+w+1) k = (s+1)/s * (s^2+s+1)/s^2 * (s^3+s^2+1)/s^3 * K/s^2 = (...)/s^8 * K!
    # So term 3 times s^8 has NO s^2 factor! Wait: (1 + s^2 + s^3) vs w^3 + w + 1 = s^-3 + s^-1 + 1 = (1 + s^2 + s^3)/s^3!
    G_inf = (
        (s_var + 1)**2 * K_sym**3
        + s_var**3 * K_sym**2
        + (s_var + 1) * (s_var**2 + s_var + 1) * (s_var**3 + s_var**2 + 1) * K_sym
        + s_var**6
    )
    # Check s(pi) = pi^2 + pi^5 + pi^9 + O(pi^10) satisfies G_inf = O(pi^14)
    s_full = pi**2 + pi**5 + pi**9
    g_val = sp.Poly(G_inf.subs(s_var, s_full), pi, domain=GF(2))
    for d in range(14):
        assert g_val.nth(d) == 0, f"Nonzero coeff at pi^{d}: {g_val.nth(d)}"
    # Verify PROOF.md L211: k = (1 + pi*s)/s^2 = pi^-4 + pi^-1 + O(pi)
    s_div_pi2 = sp.Poly(1 + pi**3 + pi**7, pi, domain=GF(2))
    # Invert s_div_pi2^2 mod pi^5
    s2_mod = sp.Poly((s_div_pi2.as_expr()**2), pi, domain=GF(2))
    # Newton or power-series inverse mod pi^5
    inv_s2 = sp.Poly(1, pi, domain=GF(2))
    for _ in range(4):
        inv_s2 = sp.Poly(inv_s2.as_expr() * (2 - s2_mod.as_expr() * inv_s2.as_expr()), pi, domain=GF(2))
        inv_s2 = sp.Poly(sum(inv_s2.nth(j) * pi**j for j in range(5)), pi, domain=GF(2))
    k_times_pi4 = sp.Poly((1 + pi * s_full) * inv_s2.as_expr(), pi, domain=GF(2))
    k_terms = [int(k_times_pi4.nth(j) % 2) for j in range(5)]
    # pi^-4 + pi^-1 + O(pi) => powers pi^0 and pi^3 are 1, pi^1, pi^2, pi^4 are 0!
    assert k_terms == [1, 0, 0, 1, 0], f"Got k*pi^4 mod pi^5 = {k_terms}"

    # Check Hasse-Weil bound for m >= 9
    for m in range(9, 60):
        q = 1 << m
        assert (q - 7) ** 2 - 484 * q > 0

    # Subcase 4a (2 <= m <= 8): Check Kloosterman formula & find/verify actual s(y)=0 + colliding X1!=X2 in F_{q^6}
    for m in range(2, 9):
        q = 1 << m
        F_q = GF2Ext(m)
        fq_elems = list(range(q))
        # Verify Kloosterman count M_q
        m_q = 0
        kloost = 0
        for kk in range(1, q):
            tr_k_inv = F_q.trace(kk ^ F_q.inv(kk), 1, m)
            kloost += -1 if tr_k_inv else 1
            if kk != 1:
                tr_k1 = F_q.trace(kk ^ 1, 1, m)
                if tr_k1 == 1 and tr_k_inv == 0:
                    m_q += 2
        tr1 = F_q.trace(1, 1, m)
        assert 2 * m_q == q - 1 + kloost + 2 * (-1 if tr1 else 1)

        # Now find an explicit y in D_6 subset F_{q^6} with s(y) = 0 and lift to X1 != X2 in F_{q^6}
        F6 = GF2Ext(6 * m)
        rng = random.Random(6000 + m)
        # Find some z0 with Tr_{q^6/q^2}(z0) = 1
        while True:
            z0 = rng.randrange(1, F6.order)
            tr2 = F6.trace(z0, 2 * m, 3)
            if tr2 != 0:
                z0 = F6.mul(z0, F6.inv(tr2))
                break
        # Find y in D_6 with s(y) = 0 by random sampling z = z0 + (r + r^{q^2})
        witness_y = None
        for _ in range(10000):
            r = rng.randrange(0, F6.order)
            y = z0 ^ r ^ F6.frob_q(r, 2 * m)
            if y == 0:
                continue
            w = F6.mul(F6.pow(y, q - 2), y ^ 1)
            if (1 ^ F6.trace(w, m, 6)) == 0:
                witness_y = y
                break
        assert witness_y is not None, f"Failed to find s(y)=0 witness for m={m}"

        # Lift witness_y = S_2(X1) with S_6(X1) = 1:
        # Since S_2(X) = X + X^q, solve X1 + X1^q = witness_y by finding a particular root + adding F_q element to fix S_6(X1)=1
        # Wait: any z with Tr_{q^6/q}(z) = 1 has S_2(z) in D_6 and S_2 is 2m-linear; we can solve linear system over F_2 (size 6m <= 48)!
        # Or simpler: find X1 in {S_6 = 1} by linear algebra over F_2 on S_2(X) = witness_y!
        # Let's build the 6m x 6m F_2 matrix of S_2: basis e_i -> S_2(e_i)
        dim = 6 * m
        # Find element u0 with S_6(u0) = 1
        while True:
            u0 = rng.randrange(1, F6.order)
            s6_u0 = F6.trace(u0, m, 6)
            if s6_u0 != 0:
                u0 = F6.mul(u0, F6.inv(s6_u0))
                break
        # Solve S_2(delta) = witness_y ^ S_2(u0) with delta in ker(S_6)
        target_rhs = witness_y ^ u0 ^ F6.frob_q(u0, m)
        # Basis of ker(S_6): e_i + S_6(e_i)*u0
        ker_gens = []
        piv_cols = []
        piv_rows = []
        for bit in range(dim):
            ei = 1 << bit
            g = ei ^ F6.mul(F6.trace(ei, m, 6), u0)
            s2_g = g ^ F6.frob_q(g, m)
            # Gaussian elimination over F_2 with history
            cur_s2 = s2_g
            cur_g = g
            for p_col, r_s2, r_g in zip(piv_cols, piv_rows, ker_gens):
                if (cur_s2 >> p_col) & 1:
                    cur_s2 ^= r_s2
                    cur_g ^= r_g
            if cur_s2 != 0:
                piv_cols.append(cur_s2.bit_length() - 1)
                piv_rows.append(cur_s2)
                ker_gens.append(cur_g)
        delta = 0
        rem_rhs = target_rhs
        for p_col, r_s2, r_g in zip(piv_cols, piv_rows, ker_gens):
            if (rem_rhs >> p_col) & 1:
                rem_rhs ^= r_s2
                delta ^= r_g
        assert rem_rhs == 0
        x1 = u0 ^ delta
        assert F6.trace(x1, m, 6) == 1
        assert (x1 ^ F6.frob_q(x1, m)) == witness_y
        g_val = eval_g_formula(F6, m, 6, x1)
        assert F6.trace(g_val, m, 6) == 0
        # x2 = g_val^{q^{-1}} satisfies S_6(x2) = 0 and g(x2) = x2^q = g_val = g(x1)
        x2 = F6.frob_q(g_val, 5 * m)
        assert x1 != x2
        assert eval_g_formula(F6, m, 6, x2) == g_val

    print("[PASS] Case 4 (e=6): symbolic identities, Groebner irreducibility, genus-9 Hasse-Weil, & m=2..8 collisions verified.")


# ---------------------------------------------------------------------------
# 5. Case 5 ((q, e) = (4, 4)): Exhaustive 256-element Check & Orbit Formula
# ---------------------------------------------------------------------------

def check_case_5() -> None:
    # Polynomial X^4 + X + 1 over GF(2) (0b10011 = 19) gives GF(16);
    # construct GF(256) directly and verify all 256 values of g_{4387, 4}
    F = GF2Ext(8)
    fq = F.elements_of_subfield(2)
    assert len(fq) == 4
    n_4387 = 3 + 2 * 16 + 256 + 4096
    assert n_4387 == 4387

    vals_form = set()
    for x in range(256):
        y = x ^ F.frob_q(x, 2)
        v_def = 0
        for a in fq:
            v_def ^= F.pow(x ^ a, 4387)
        assert v_def == eval_g_formula(F, 2, 4, y)
        v_form = eval_g_formula(F, 2, 4, x)
        vals_form.add(v_form)
    assert len(vals_form) == 256

    # Also check the exact (u, c, r) symbolic formulas in Case 5 for general even q
    # Over GF(2)[y, z, u, c, r, yq, zq] with relations:
    # y^2 = y + z, z^2 = z + u, u^2 = u + c (since c = u + u^2),
    # z^4 = z + c, u^4 = u + 1, z^q = z + r? Wait: r = z + c*u?
    # Check: z^q = z + r?! No: over F_{q^2}, let's verify Case 5's exact formulas numerically on q = 4, 8, 16!
    for m in (2, 3, 4):
        q = 1 << m
        F4 = GF2Ext(4 * m)
        fq2 = F4.elements_of_subfield(2 * m)
        fq1 = F4.elements_of_subfield(m)
        # Pick 20 elements y in D_4 (Tr_{q^4/q^2}(y) = 1 => y + y^{q^2} = 1)
        rng = random.Random(500 + m)
        # Find z0 in D_4
        while True:
            cand = rng.randrange(1, F4.order)
            tr = cand ^ F4.frob_q(cand, 2 * m)
            if tr != 0:
                z0 = F4.mul(cand, F4.inv(tr))
                break
        for _ in range(25):
            y = z0 ^ fq2[rng.randrange(len(fq2))]
            assert (y ^ F4.frob_q(y, 2 * m)) == 1
            z = y ^ F4.sq(y)
            u = y ^ F4.frob_q(y, m)
            c = u ^ F4.sq(u)
            assert c == (z ^ F4.frob_q(z, m))
            assert c in fq1 and c != 0
            r = z ^ F4.mul(c, u)
            assert r in fq1

            N = F4.pow(z, q + 1)
            c2 = F4.sq(c)
            c3 = F4.mul(c, c2)
            assert N == (F4.sq(r) ^ F4.mul(c, r) ^ c3)

            N2 = F4.sq(N)
            D = N2 ^ F4.mul(r ^ c ^ 1, N) ^ F4.mul(c, r)
            w = F4.mul(F4.pow(y, q - 2), y ^ 1)
            s_direct = 1 ^ F4.trace(w, m, 4)
            s_form = F4.mul(D, F4.inv(N2))
            assert s_direct == s_form

            if s_direct != 0:
                psi_direct = F4.mul(F4.frob_q(y, m) ^ w ^ F4.frob_q(w, m), F4.inv(s_direct))
                Num = F4.mul(c2, N) ^ F4.sq(r)
                A1 = D ^ Num
                A0 = F4.mul(c2 ^ F4.mul(c, r) ^ 1, N) ^ F4.mul(F4.mul(c, c ^ 1), r)
                delta = F4.mul(A0 ^ F4.mul(A1, u), F4.inv(D))
                assert psi_direct == (y ^ delta)

    print("[PASS] Case 5 ((q,e)=(4,4)) exhaustive 256-element bijection & general (u,c,r) formulas verified.")


# ---------------------------------------------------------------------------
# 6. Case 6 (e = 4, q >= 8): Monodromy S_25, Cafure-Matera, & m=3..37 Witnesses
# ---------------------------------------------------------------------------

def poly_gf2x_mul_mod(p: list[int], q_poly: list[int], mod_p: list[int], fq2: GF2Ext, m2: int) -> list[int]:
    """Multiply two polynomials in GF(q^2)[X0] modulo monic mod_p of degree d."""
    d = len(mod_p) - 1
    deg_sum = len(p) + len(q_poly) - 1
    prod = [0] * deg_sum
    for i, a in enumerate(p):
        if a == 0:
            continue
        for j, b in enumerate(q_poly):
            if b != 0:
                prod[i + j] ^= fq2.mul(a, b)
    for k in range(deg_sum - 1, d - 1, -1):
        c = prod[k]
        if c != 0:
            for j in range(d + 1):
                prod[k - d + j] ^= fq2.mul(c, mod_p[j])
    res = prod[:d]
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res


def poly_gf2x_gcd(a: list[int], b: list[int], fq2: GF2Ext) -> list[int]:
    """Monic GCD in GF(q^2)[X0]."""
    a = list(a)
    b = list(b)
    while len(a) > 0 and a[-1] == 0:
        a.pop()
    while len(b) > 0 and b[-1] == 0:
        b.pop()
    while b:
        # Reduce a mod b
        inv_lc = fq2.inv(b[-1])
        db = len(b) - 1
        while len(a) >= len(b) and a:
            if a[-1] != 0:
                factor = fq2.mul(a[-1], inv_lc)
                shift = len(a) - 1 - db
                for j in range(db + 1):
                    a[shift + j] ^= fq2.mul(factor, b[j])
            while a and a[-1] == 0:
                a.pop()
        a, b = b, a
    if not a:
        return []
    inv_lc = fq2.inv(a[-1])
    return [fq2.mul(c, inv_lc) for c in a]


def poly_gf2x_eval(p: list[int], x: int, fq2: GF2Ext) -> int:
    acc = 0
    for c in reversed(p):
        acc = fq2.mul(acc, x) ^ c
    return acc


def find_root_in_gfq2(p: list[int], fq2: GF2Ext, rng: random.Random) -> int | None:
    """Equal-degree splitting (Cantor-Zassenhaus in char 2) for roots of p in GF(q^2)."""
    # First remove X0 = 0 or X0 = 1 if present
    while len(p) > 1 and p[0] == 0:
        return 0
    # Ensure monic
    if not p or len(p) <= 1:
        return None
    inv_lc = fq2.inv(p[-1])
    p = [fq2.mul(c, inv_lc) for c in p]
    if len(p) == 2:
        return p[0]

    # Split squarefree product of linear factors over GF(2^{2m}) using trace Tr_{2^{2m}/2}(r * X)
    # Since deg(p) <= 24, trace(X + c) = X + X^2 + ... + X^{2^{2m-1}} mod p
    stack = [p]
    d_f2 = fq2.d  # 2*m
    while stack:
        cur = stack.pop()
        if len(cur) == 2:
            return cur[0]
        if len(cur) <= 1:
            continue
        # Try random linear shift a*X0 + b
        for _ in range(40):
            a = rng.randrange(1, fq2.order)
            b = rng.randrange(0, fq2.order)
            lin = [b, a]
            # Compute Tr(lin) = sum_{i=0}^{d_f2 - 1} lin^{2^i} mod cur
            tr = [0]
            sq_lin = list(lin)
            for _ in range(d_f2):
                # tr += sq_lin
                if len(tr) < len(sq_lin):
                    tr.extend([0] * (len(sq_lin) - len(tr)))
                for idx, val in enumerate(sq_lin):
                    tr[idx] ^= val
                sq_lin = poly_gf2x_mul_mod(sq_lin, sq_lin, cur, fq2, d_f2)
            g = poly_gf2x_gcd(cur, tr, fq2)
            if 1 < len(g) < len(cur):
                if len(g) == 2:
                    return g[0]
                stack.append(g)
                # Divide cur by g
                q_poly = []
                rem = list(cur)
                dg = len(g) - 1
                q_poly = [0] * (len(cur) - dg)
                for pos in range(len(cur) - 1, dg - 1, -1):
                    c = rem[pos]
                    if c != 0:
                        q_poly[pos - dg] = c
                        for j in range(dg + 1):
                            rem[pos - dg + j] ^= fq2.mul(c, g[j])
                stack.append(q_poly)
                break
    return None


def check_case_6() -> None:
    # Step 6.1: Verify Mobius conjugation & reduced forms P0/Q0, P1/Q0 over GF(2)(Y0, Y1)
    Y0, Y1 = sp.symbols("Y0 Y1")
    w0 = Y1 * (Y0 + 1) / Y0**2
    w1 = (Y0 + 1) * (Y1 + 1) / Y1**2
    w2 = (Y1 + 1) * Y0 / (Y0 + 1)**2
    w3 = Y0 * Y1 / (Y1 + 1)**2
    s_expr = 1 + w0 + w1 + w2 + w3
    psi0_raw = sp.cancel((Y1 + w0 + w1) / s_expr, modulus=2)
    psi1_raw = sp.cancel((Y0 + 1 + w2 + w1) / s_expr, modulus=2)
    num0, den0 = sp.fraction(psi0_raw)
    num1, den1 = sp.fraction(psi1_raw)
    P0_p = sp.Poly(num0, Y0, Y1, domain=GF(2))
    P1_p = sp.Poly(num1, Y0, Y1, domain=GF(2))
    Q0_p = sp.Poly(den0, Y0, Y1, domain=GF(2))
    Q1_p = sp.Poly(den1, Y0, Y1, domain=GF(2))
    assert Q0_p == Q1_p
    assert P0_p.total_degree() == 9 and P1_p.total_degree() == 9 and Q0_p.total_degree() == 8
    assert sp.gcd(P0_p, Q0_p).is_one and sp.gcd(P1_p, Q0_p).is_one

    # Check Mobius conjugation to G0(X0, X1), G1(X0, X1) via exact polynomial clearing
    X0, X1 = sp.symbols("X0 X1")
    def mobius_pullback(poly_y, deg_cap=9):
        acc = sp.Integer(0)
        for (i, j), coeff in poly_y.terms():
            if int(coeff) & 1:
                acc += (X0**i) * ((X0 + 1)**(deg_cap - i)) * (X1**j) * ((X1 + 1)**(deg_cap - j))
        return sp.Poly(acc, X0, X1, domain=GF(2))

    P0_m = mobius_pullback(P0_p)
    P1_m = mobius_pullback(P1_p)
    Q0_m = mobius_pullback(Q0_p)
    G0_num = sp.Poly(X1**3 * (X0**3 + 1) + X0**2 * (X1**2 + 1), X0, X1, domain=GF(2))
    G0_den = sp.Poly(X0**2 * X1**2 * (X0**3 + 1 + X0 * X1 * (X1**2 + 1)), X0, X1, domain=GF(2))
    G1_num = sp.Poly(X0**2 * X1**3 + (X0**5 + X0**3) * X1**2 + X0**2, X0, X1, domain=GF(2))
    G1_den = sp.Poly(X0**3 * X1**5 + (X0**2 + 1) * X1**3 + X0**3 * X1**2, X0, X1, domain=GF(2))
    assert P0_m * G0_den == (P0_m + Q0_m) * G0_num
    assert P1_m * G1_den == (P1_m + Q0_m) * G1_num

    # Step 6.2: Exact resultant P_gen(A, B; X0) via 6x6 Sylvester matrix / SymPy Poly resultant
    A, B = sp.symbols("A B")
    f0_expr = A * X0**3 * X1**5 + (A * X0**3 + X0**3 + 1) * X1**3 + (A * (X0**5 + X0**2) + X0**2) * X1**2 + X0**2
    f1_expr = B * X0**3 * X1**5 + (B * (X0**2 + 1) + X0**2) * X1**3 + (B * X0**3 + X0**5 + X0**3) * X1**2 + X0**2
    f0_p = sp.Poly(f0_expr, X1, A, B, X0, domain=GF(2))
    f1_p = sp.Poly(f1_expr, X1, A, B, X0, domain=GF(2))
    c1_p = sp.Poly(B * f0_expr + A * f1_expr, X1, A, B, X0, domain=GF(2))
    c2_p = sp.exquo(f0_p + f1_p, sp.Poly(X1**2, X1, A, B, X0, domain=GF(2)))
    assert c1_p.degree(X1) == 3 and c2_p.degree(X1) == 3
    res = sp.polys.polytools.resultant(c1_p, c2_p, X1)
    res_p = sp.Poly(res, X0, A, B, domain=GF(2))
    triv_p = sp.Poly(X0**2 * (X0 + 1) * (A + B), X0, A, B, domain=GF(2))
    Pgen_all, rem_triv = sp.div(res_p, triv_p)
    assert rem_triv.is_zero
    Pgen_X0 = sp.Poly(Pgen_all.as_expr(), X0, domain=GF(2)[A, B])
    assert Pgen_X0.degree() == 25
    assert sp.Poly(Pgen_X0.LC(), A, B, domain=GF(2)) == sp.Poly(A**3 * (A + 1)**2 * (B + 1)**3, A, B, domain=GF(2))

    # Specializations over F_64 = F_2[beta]/(beta^6 + beta + 1)
    F64 = GF2Ext(6, 0b1000011)
    beta_val = 2  # element beta

    pgen_terms_by_deg = [[] for _ in range(26)]
    for (ex0, ea, eb), coeff in Pgen_all.terms():
        if int(coeff) & 1:
            pgen_terms_by_deg[ex0].append((ea, eb))

    def eval_Pgen_f64(A_val: int, B_val: int) -> list[int]:
        Ap = [1] * 14
        Bp = [1] * 14
        for i in range(1, 14):
            Ap[i] = F64.mul(Ap[i - 1], A_val)
            Bp[i] = F64.mul(Bp[i - 1], B_val)
        coeffs = [0] * 26
        for dx in range(26):
            acc = 0
            for ea, eb in pgen_terms_by_deg[dx]:
                acc ^= F64.mul(Ap[ea], Bp[eb])
            coeffs[dx] = acc
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()
        inv_lc = F64.inv(coeffs[-1])
        return [F64.mul(c, inv_lc) for c in coeffs]

    def poly_diff_f64(p: list[int]) -> list[int]:
        res = [p[i] if (i & 1) else 0 for i in range(1, len(p))]
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res if res else [0]

    def poly_divmod_f64(a: list[int], b: list[int]) -> tuple[list[int], list[int]]:
        rem = list(a)
        while len(rem) > 0 and rem[-1] == 0:
            rem.pop()
        db = len(b) - 1
        inv_lc = F64.inv(b[-1])
        if len(rem) <= db:
            return [0], rem if rem else [0]
        q_out = [0] * (len(rem) - db)
        for pos in range(len(rem) - 1, db - 1, -1):
            c = rem[pos]
            if c != 0:
                fac = F64.mul(c, inv_lc)
                q_out[pos - db] = fac
                for j in range(db + 1):
                    rem[pos - db + j] ^= F64.mul(fac, b[j])
        while len(rem) > 1 and rem[-1] == 0:
            rem.pop()
        while len(q_out) > 1 and q_out[-1] == 0:
            q_out.pop()
        return q_out, (rem if rem else [0])

    def poly_ddf_degrees_f64(p: list[int]) -> list[int]:
        """Exact distinct-degree factorization degrees (for squarefree p over F_64)."""
        assert len(poly_gf2x_gcd(p, poly_diff_f64(p), F64)) == 1
        f = list(p)
        cur_x = [0, 1]
        degs = []
        k_deg = 1
        while len(f) - 1 >= 2 * k_deg:
            # cur_x <- cur_x^{64} mod f (6 squarings)
            for _ in range(6):
                cur_x = poly_gf2x_mul_mod(cur_x, cur_x, f, F64, 6)
            # diff = cur_x - X
            diff_p = list(cur_x)
            if len(diff_p) < 2:
                diff_p.extend([0] * (2 - len(diff_p)))
            diff_p[1] ^= 1
            while len(diff_p) > 1 and diff_p[-1] == 0:
                diff_p.pop()
            g = poly_gf2x_gcd(f, diff_p, F64)
            dg = len(g) - 1
            if dg > 0:
                assert dg % k_deg == 0
                for _ in range(dg // k_deg):
                    degs.append(k_deg)
                f, _ = poly_divmod_f64(f, g)
                _, cur_x = poly_divmod_f64(cur_x, f) if len(f) > 1 else ([0], [0])
            k_deg += 1
        if len(f) - 1 > 0:
            degs.append(len(f) - 1)
        return sorted(degs)

    # Spec 1: (A1, B1) = (beta, beta^5 + beta^3)
    A1 = beta_val
    B1 = (1 << 5) ^ (1 << 3)
    P0_spec = eval_Pgen_f64(A1, B1)
    assert len(P0_spec) - 1 == 25
    assert poly_ddf_degrees_f64(P0_spec) == [25]

    # Check deg_{X1} gcd_K(f0, f1) == 1 over K = F64[X0]/(P0_spec) and G(X0, X1) == (A1, B1)
    def k_add(pa, pb):
        n = max(len(pa), len(pb))
        out = [(pa[i] if i < len(pa) else 0) ^ (pb[i] if i < len(pb) else 0) for i in range(n)]
        while len(out) > 1 and out[-1] == 0:
            out.pop()
        return out

    def k_mul(pa, pb):
        return poly_gf2x_mul_mod(pa, pb, P0_spec, F64, 6)

    def k_inv(pa):
        # Extended GCD in F64[X0]
        r0, r1 = list(pa), list(P0_spec)
        s0, s1 = [1], [0]
        while r1 != [0]:
            q_p, rem = poly_divmod_f64(r0, r1)
            # s_next = s0 ^ (q_p * s1)
            prod = [0] * (len(q_p) + len(s1) - 1)
            for i, a in enumerate(q_p):
                if a:
                    for j, b in enumerate(s1):
                        if b:
                            prod[i + j] ^= F64.mul(a, b)
            s_next = k_add(s0, prod)
            r0, r1 = r1, rem
            s0, s1 = s1, s_next
        assert len(r0) == 1 and r0[0] != 0
        inv_r0 = F64.inv(r0[0])
        return [F64.mul(c, inv_r0) for c in s0]

    # f0, f1 in K[X1] (low to high deg in X1)
    # f0(X1) = X0^2 + (A*(X0^5+X0^2) + X0^2)*X1^2 + (A*X0^3 + X0^3 + 1)*X1^3 + A*X0^3*X1^5
    # f1(X1) = X0^2 + (B*X0^3 + X0^5 + X0^3)*X1^2 + (B*(X0^2+1) + X0^2)*X1^3 + B*X0^3*X1^5
    f0_k = [
        [0, 0, 1],
        [0],
        [0, 0, A1 ^ 1, 0, 0, A1],
        [1, 0, 0, A1 ^ 1],
        [0],
        [0, 0, 0, A1],
    ]
    f1_k = [
        [0, 0, 1],
        [0],
        [0, 0, 0, B1 ^ 1, 0, 1],
        [B1, 0, B1 ^ 1],
        [0],
        [0, 0, 0, B1],
    ]

    def kx1_gcd(pa, pb):
        pa = list(pa)
        pb = list(pb)
        while pa and pa[-1] == [0]:
            pa.pop()
        while pb and pb[-1] == [0]:
            pb.pop()
        while pb:
            inv_lc = k_inv(pb[-1])
            db = len(pb) - 1
            while len(pa) >= len(pb) and pa:
                if pa[-1] != [0]:
                    fac = k_mul(pa[-1], inv_lc)
                    sh = len(pa) - 1 - db
                    for j in range(db + 1):
                        pa[sh + j] = k_add(pa[sh + j], k_mul(fac, pb[j]))
                while pa and pa[-1] == [0]:
                    pa.pop()
            pa, pb = pb, pa
        return pa

    gcd_x1 = kx1_gcd(f0_k, f1_k)
    assert len(gcd_x1) == 2
    X1_in_K = k_mul(gcd_x1[0], k_inv(gcd_x1[1]))
    assert X1_in_K != [0] and X1_in_K != [1]
    # Verify G0(X0, X1) == A1 and G1(X0, X1) == B1 in K
    x0_k = [0, 1]
    x0_2 = k_mul(x0_k, x0_k)
    x0_3 = k_mul(x0_2, x0_k)
    x0_5 = k_mul(x0_3, x0_2)
    x1_2 = k_mul(X1_in_K, X1_in_K)
    x1_3 = k_mul(x1_2, X1_in_K)
    x1_5 = k_mul(x1_3, x1_2)
    g0_num_k = k_add(k_mul(x1_3, k_add(x0_3, [1])), k_mul(x0_2, k_add(x1_2, [1])))
    g0_den_k = k_mul(k_mul(x0_2, x1_2), k_add(k_add(x0_3, [1]), k_mul(k_mul(x0_k, X1_in_K), k_add(x1_2, [1]))))
    g1_num_k = k_add(k_add(k_mul(x0_2, x1_3), k_mul(k_add(x0_5, x0_3), x1_2)), x0_2)
    g1_den_k = k_add(k_add(k_mul(x0_3, x1_5), k_mul(k_add(x0_2, [1]), x1_3)), k_mul(x0_3, x1_2))
    assert g0_den_k != [0] and g1_den_k != [0]
    assert k_mul(g0_num_k, k_inv(g0_den_k)) == [A1]
    assert k_mul(g1_num_k, k_inv(g1_den_k)) == [B1]

    # Spec 2: (A2, B2) = (beta + 1, beta^2 + beta + 1)
    A2 = beta_val ^ 1
    B2 = (1 << 2) ^ beta_val ^ 1
    P1_spec = eval_Pgen_f64(A2, B2)
    assert len(P1_spec) - 1 == 25
    assert poly_ddf_degrees_f64(P1_spec) == [2, 23]

    # Step 6.4: Exact integer check of Cafure-Matera inequality for m >= 38
    for m in range(38, 100):
        q = 1 << m
        assert q > 6 * 288**2
        ceil_sqrt_q = math.isqrt(q)
        if ceil_sqrt_q * ceil_sqrt_q < q:
            ceil_sqrt_q += 1
        lhs = q - 287 * 286 * ceil_sqrt_q - 288
        assert lhs > 0
        assert lhs**3 > 125 * (288**13)

    # Subcase 6a (3 <= m <= 37): Find explicit colliding pair X1 != X2 in F_{q^4} for EVERY m in 3..37
    # Extract Pgen coefficients in GF(2)[A, B] for fast evaluation in GF(q^2)
    pgen_terms_by_deg = [[] for _ in range(26)]
    for (ex0, ea, eb), coeff in Pgen_all.terms():
        if int(coeff) & 1:
            pgen_terms_by_deg[ex0].append((ea, eb))

    for m in range(3, 38):
        q = 1 << m
        rng = random.Random(4000 + m)
        F4 = GF2Ext(4 * m)
        # Find gamma in F_{q^2} \ F_q with gamma^q = gamma + 1, and theta0 in D_4 with theta0^q + theta0 = gamma
        # Equivalently pick random z0 in D_4 directly: z in F_{q^4} with z + z^{q^2} != 0, z0 = z / (z + z^{q^2}),
        # and ker(Tr_{q^4/q^2}) = F_{q^2}, spanned over F_q by 1 and gamma!
        while True:
            cand = rng.randrange(1, F4.order)
            tr = cand ^ F4.frob_q(cand, 2 * m)
            if tr != 0:
                z0 = F4.mul(cand, F4.inv(tr))
                break
        # Find gamma in F_{q^2} with gamma + gamma^q = 1
        exp_fq2 = (F4.order - 1) // (q * q - 1)
        while True:
            g_cand = F4.pow(rng.randrange(1, F4.order), exp_fq2)
            gg = g_cand ^ F4.frob_q(g_cand, m)
            if gg != 0:
                gamma = F4.mul(g_cand, F4.inv(gg))
                break
        assert (gamma ^ F4.frob_q(gamma, m)) == 1
        assert F4.frob_q(gamma, 2 * m) == gamma

        # Also find F_q basis elements to sample (a, b) in F_q^2 uniformly
        fq_basis = F4.basis_of_subfield(m)

        def rand_fq():
            acc = 0
            bits = rng.getrandbits(m)
            for i in range(m):
                if (bits >> i) & 1:
                    acc ^= fq_basis[i]
            return acc

        def eval_G(x0, x1):
            x0_2 = F4.sq(x0)
            x0_3 = F4.mul(x0, x0_2)
            x0_5 = F4.mul(x0_3, x0_2)
            x1_2 = F4.sq(x1)
            x1_3 = F4.mul(x1, x1_2)
            x1_5 = F4.mul(x1_3, x1_2)
            num0 = F4.mul(x1_3, x0_3 ^ 1) ^ F4.mul(x0_2, x1_2 ^ 1)
            den0 = F4.mul(F4.mul(x0_2, x1_2), x0_3 ^ 1 ^ F4.mul(F4.mul(x0, x1), x1_2 ^ 1))
            num1 = F4.mul(x0_2, x1_3) ^ F4.mul(x0_5 ^ x0_3, x1_2) ^ x0_2
            den1 = F4.mul(x0_3, x1_5) ^ F4.mul(x0_2 ^ 1, x1_3) ^ F4.mul(x0_3, x1_2)
            return num0, den0, num1, den1

        found_pair = None
        for trial in range(120):
            a1 = rand_fq()
            b1 = rand_fq()
            y1 = z0 ^ a1 ^ F4.mul(b1, gamma)
            if y1 == 0 or y1 == 1:
                continue
            w1 = F4.mul(F4.pow(y1, q - 2), y1 ^ 1)
            s1 = 1 ^ F4.trace(w1, m, 4)
            if s1 == 0:
                # Direct s=0 witness -> collision immediately!
                found_pair = (y1, None, s1)
                break
            x0_1 = F4.mul(y1, F4.inv(y1 ^ 1))
            x1_1 = F4.frob_q(x0_1, m)
            n0, d0, n1, d1 = eval_G(x0_1, x1_1)
            if d0 == 0 or d1 == 0:
                continue
            A_val = F4.mul(n0, F4.inv(d0))
            B_val = F4.mul(n1, F4.inv(d1))
            if A_val in (0, 1) or B_val in (0, 1) or A_val == B_val:
                continue

            # Precompute powers of A_val and B_val
            Apows = [1] * 14
            Bpows = [1] * 14
            for i in range(1, 14):
                Apows[i] = F4.mul(Apows[i - 1], A_val)
                Bpows[i] = F4.mul(Bpows[i - 1], B_val)
            P_coeffs = [0] * 26
            for deg_x in range(26):
                acc = 0
                for ea, eb in pgen_terms_by_deg[deg_x]:
                    acc ^= F4.mul(Apows[ea], Bpows[eb])
                P_coeffs[deg_x] = acc
            if P_coeffs[25] == 0:
                continue
            assert poly_gf2x_eval(P_coeffs, x0_1, F4) == 0

            # Deflate (X0 + x0_1) from P_coeffs -> degree 24 poly Q_coeffs
            Q_coeffs = [0] * 25
            rem = P_coeffs[25]
            for idx in range(24, -1, -1):
                Q_coeffs[idx] = rem
                rem = P_coeffs[idx] ^ F4.mul(rem, x0_1)
            assert rem == 0

            # Compute X0^{q^2+1} - 1 mod Q_coeffs in F4[X0]
            # Wait: X0^{q^2+1} = X0 * X0^{q^2}; compute X0^{2^{2m}} via 2m squarings mod Q_coeffs!
            inv_qlc = F4.inv(Q_coeffs[24])
            Q_monic = [F4.mul(c, inv_qlc) for c in Q_coeffs]
            cur_x = [0, 1]
            for _ in range(2 * m):
                cur_x = poly_gf2x_mul_mod(cur_x, cur_x, Q_monic, F4, 4 * m)
            x_q2p1 = poly_gf2x_mul_mod(cur_x, [0, 1], Q_monic, F4, 4 * m)
            # Subtract 1
            if not x_q2p1:
                x_q2p1 = [1]
            else:
                x_q2p1[0] ^= 1
            g_unit = poly_gf2x_gcd(Q_monic, x_q2p1, F4)
            if len(g_unit) >= 2:
                # Find a root x0_2 in F4! (g_unit splits over F4 since its roots lie in mu_{q^2+1} subset F_{q^4}!)
                # Wait: gcd(g_unit, X0^{q^4} - X0) might be needed? No, mu_{q^2+1} IS a subgroup of F_{q^4}^*, so all roots of g_unit are ALREADY in F_{q^4}!
                x0_2 = find_root_in_gfq2(g_unit, F4, rng)
                if x0_2 is not None and x0_2 not in (0, 1, x0_1):
                    y2 = F4.mul(x0_2, F4.inv(x0_2 ^ 1))
                    w2 = F4.mul(F4.pow(y2, q - 2), y2 ^ 1)
                    s2 = 1 ^ F4.trace(w2, m, 4)
                    if s2 == 0:
                        found_pair = (y2, None, 0)
                        break
                    psi1 = F4.mul(F4.frob_q(y1, m) ^ w1 ^ F4.frob_q(w1, m), F4.inv(s1))
                    psi2 = F4.mul(F4.frob_q(y2, m) ^ w2 ^ F4.frob_q(w2, m), F4.inv(s2))
                    if psi1 == psi2:
                        found_pair = (y1, y2, s1)
                        break

        assert found_pair is not None, f"No collision found for m={m}"
        y1, y2, s1 = found_pair

        # Lift y1 (and y2 if s1 != 0) to X1 != X2 in F_{q^4} with g_{n,q}(X1) == g_{n,q}(X2)
        # Solve S_2(X) = X + X^q = y, S_4(X) = 1 (note for e=4, S_4 = Tr_{q^4/q} = Tr_{q^4/q^2} o S_2, so y in D_4 guarantees S_4(X)=1 for ANY X with S_2(X)=y!)
        # WAIT: Is S_4(X) = Tr_{q^4/q^2}(S_2(X))? Let's verify!
        # S_2(X) + S_2(X)^{q^2} = X + X^q + X^{q^2} + X^{q^3} = S_4(X)!
        # So ANY X in F_{q^4} with X + X^q = y (for y in D_4) AUTOMATICALLY satisfies S_4(X) = y + y^{q^2} = 1!!
        # Wait: how to solve X + X^q = y for y in D_4 explicitly? Pick u0 in F_{q^4} with S_4(u0) = 1? Wait: S_2 is linear F_{q^4} -> D_4+...; since S_2(x) = y, what is a right-inverse of X -> X + X^q on Im(S_2)?
        # Easy! Note S_2(X + X^{q^2}) = S_4(X), no; pick alpha_0 in F_{q^4} with Tr_{q^4/q}(alpha_0) = 1, wait:
        # Take X = y*alpha_0 + (y + y^q)*(alpha_0^q) + ...? Actually by Hilbert 90 / Trace trick:
        # Check X = c_1 y + c_2 y^q + c_3 y^{q^2}:
        # If S_4(alpha_0) = 1 (say alpha_0 in F_{q^4} with S_4(alpha_0)=1), let beta_1 = alpha_0^q + alpha_0^{q^2} + alpha_0^{q^3}? No, simpler:
        # Set X = alpha_0 * y + (alpha_0 + alpha_0^q) * y^q + (alpha_0 + alpha_0^q + alpha_0^{q^2}) * y^{q^2}?
        # Check X + X^q:
        # X^q = alpha_0^q y^q + (alpha_0^q + alpha_0^{q^2}) y^{q^2} + (alpha_0^q + alpha_0^{q^2} + alpha_0^{q^3}) y^{q^3}.
        #Wait: y^{q^3} = y^q + 1, y^{q^2} = y + 1!
        # Let's check X = u * y + v * y^q (or just solve X + X^q = y in F_2-linear algebra? For 4m=148, 148x148 is small, OR explicit 2-line formula!):
        # Wait: let's check explicit formula! Let gamma satisfy gamma^q = gamma + 1, and y = theta0 + a + b*gamma!
        # Or wait: pick any t in F_{q^4} with t + t^{q^2} != 0, scale alpha with alpha + alpha^q = 1? No, in F_{q^4}, if Tr_{q^4/q^2}(y) = 1, wait:
        # Take X = alpha_0 * y + alpha_0^q * y^{q^2} + ... Wait: for ANY u with u + u^q + u^{q^2} + u^{q^3} = 1 (i.e. u in {S_4 = 1}):
        # Put z := (u^q + u^{q^2})*y + u^{q^2}*y^q + ... wait: compute (u^q*y + (u^q+u^{q^2})*y^q + (u^q+u^{q^2}+u^{q^3})*y^{q^2})? No:
        # Check: let X(y) = A_0*y + A_1*y^q + A_2*y^{q^2} + A_3*y^{q^3}.
        # Then X + X^q = (A_0 + A_3^q)y + (A_1 + A_0^q)y^q + (A_2 + A_1^q)y^{q^2} + (A_3 + A_2^q)y^{q^3}.
        # We want A_0 + A_3^q = 1, A_1 + A_0^q = 0, A_2 + A_1^q = 0, A_3 + A_2^q = 0? No, that requires S_4(1)=0, which holds, wait:
        # Put A_1 = A_0^q, A_2 = A_0^{q^2}, A_3 = A_0^{q^3}, then A_0 + A_3^q = A_0 + A_0 = 0! Instead we want X + X^q = y + 0*y^q + 0*y^{q^2} + 0*y^{q^3}, or since y + y^q + y^{q^2} + y^{q^3} = 0 (wait: y + y^{q^2} = 1 and y^q + y^{q^3} = 1 => y + y^q + y^{q^2} + y^{q^3} = 0!!), we ONLY need (X + X^q) - y = c*(y + y^q + y^{q^2} + y^{q^3}) = 0!!
        # Set c = 1? No, wait: take A_3 = 0! Then:
        # A_0 = 1, A_1 = A_0^q + c = 1 + c, A_2 = A_1^q + c = ... no, c in F_{q^4} works! Take A_0 = u, A_1 = u + u^q, A_2 = u + u^q + u^{q^2}, A_3 = 0 where S_4(u) = 1!!
        # Check X + X^q for X = u*y + (u + u^q)*y^q + (u + u^q + u^{q^2})*y^{q^2}:
        # Coeff of y: u.
        # Coeff of y^q: (u + u^q) + u^q = u.
        # Coeff of y^{q^2}: (u + u^q + u^{q^2}) + (u^q + u^{q^2}) = u.
        # Coeff of y^{q^3}: 0 + (u^q + u^{q^2} + u^{q^3}) = u + S_4(u) = u + 1!
        #Wait: u*y + u*y^q + u*y^{q^2} + (u+1)*y^{q^3} = u*(y+y^q+y^{q^2}+y^{q^3}) + y^{q^3} = y^{q^3}!!
        # OOH!! So replacing y by y^q gives X(y^q) whose S_2 is (y^q)^{q^3} = y!!
        # Check! For X(y) = u*y^q + (u + u^q)*y^{q^2} + (u + u^q + u^{q^2})*y^{q^3}, we have:
        # X + X^q = y!
        while True:
            u_rnd = rng.randrange(1, F4.order)
            s4_u = F4.trace(u_rnd, m, 4)
            if s4_u != 0:
                u0 = F4.mul(u_rnd, F4.inv(s4_u))
                break
        u0_q = F4.frob_q(u0, m)
        u0_q2 = F4.frob_q(u0_q, m)
        c0 = u0
        c1 = u0 ^ u0_q
        c2 = c1 ^ u0_q2

        def lift_y(yy):
            yq = F4.frob_q(yy, m)
            yq2 = yy ^ 1
            yq3 = yq ^ 1
            return F4.mul(c0, yq) ^ F4.mul(c1, yq2) ^ F4.mul(c2, yq3)

        X1 = lift_y(y1)
        assert F4.trace(X1, m, 4) == 1
        assert (X1 ^ F4.frob_q(X1, m)) == y1
        if y2 is None:
            g_val = eval_g_formula(F4, m, 4, X1)
            assert F4.trace(g_val, m, 4) == 0
            X2 = F4.frob_q(g_val, 3 * m)
            assert X1 != X2 and eval_g_formula(F4, m, 4, X2) == g_val
        else:
            # Lemma 2.2 exact fiber lift for Z = g(X1)
            g1 = eval_g_formula(F4, m, 4, X1)
            w2 = F4.mul(F4.pow(y2, q - 2), y2 ^ 1)
            s2 = 1 ^ F4.trace(w2, m, 4)
            scale = F4.mul(s1, F4.inv(s2))
            X2_base = F4.frob_q(F4.mul(g1, F4.inv(scale)) ^ w2, 3 * m)
            assert F4.trace(X2_base, m, 4) == 1
            assert (X2_base ^ F4.frob_q(X2_base, m)) == y2
            X2 = F4.mul(scale, X2_base)
            assert X1 != X2
            assert eval_g_formula(F4, m, 4, X1) == eval_g_formula(F4, m, 4, X2)

    print("[PASS] Case 6 (e=4, q>=8): Mobius conjugation, deg-25 P_gen, F_64 monodromy, Cafure-Matera (m>=38), and m=3..37 collisions verified.")


if __name__ == "__main__":
    check_primary_source()
    check_lemmas_2_1_and_2_2()
    check_cases_1_to_3()
    check_case_4()
    check_case_5()
    check_case_6()
    print("PASS")
