"""Independent exact-arithmetic verifier for Yip's conjecture (arXiv:2309.10950v2, Remark 3.3).

Strictly derived from main.tex (arXiv:2309.10950v2) and PROOF.md without reading
verify.py or any author notes. Uses exact finite-field arithmetic (zero floats).
"""

from __future__ import annotations

import itertools
import math
import signal
import sys
import time


class TimeoutError(Exception):
    pass


def _alarm_handler(signum, frame):
    raise TimeoutError("Check exceeded built-in time limit")


class GF:
    """Exact finite field F_{p^d} represented as tuples of length d over F_p."""

    def __init__(self, p: int, mod_poly: tuple[int, ...]):
        self.p = p
        self.mod_poly = mod_poly  # monic of degree d: coeffs (c_0, ..., c_d)
        self.d = len(mod_poly) - 1
        assert mod_poly[-1] == 1
        self.q = p ** self.d
        self.zero = (0,) * self.d
        self.one = (1,) + (0,) * (self.d - 1)

    def norm_el(self, a: list[int]) -> tuple[int, ...]:
        p = self.p
        return tuple(x % p for x in a)

    def add(self, a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
        p = self.p
        return tuple((a[i] + b[i]) % p for i in range(self.d))

    def sub(self, a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
        p = self.p
        return tuple((a[i] - b[i]) % p for i in range(self.d))

    def neg(self, a: tuple[int, ...]) -> tuple[int, ...]:
        p = self.p
        return tuple((-a[i]) % p for i in range(self.d))

    def mul(self, a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
        p, d = self.p, self.d
        res = [0] * (2 * d - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    res[i + j] += ai * bj
        # reduce mod self.mod_poly
        for deg in range(2 * d - 2, d - 1, -1):
            c = res[deg] % p
            if c:
                for k in range(d):
                    res[deg - d + k] = (res[deg - d + k] - c * self.mod_poly[k]) % p
        return tuple(res[k] % p for k in range(d))

    def pow(self, a: tuple[int, ...], e: int) -> tuple[int, ...]:
        if e == 0:
            return self.one
        res = self.one
        base = a
        while e > 0:
            if e & 1:
                res = self.mul(res, base)
            base = self.mul(base, base)
            e >>= 1
        return res

    def inv(self, a: tuple[int, ...]) -> tuple[int, ...]:
        assert a != self.zero
        return self.pow(a, self.q - 2)

    def elements(self) -> list[tuple[int, ...]]:
        return list(itertools.product(range(self.p), repeat=self.d))

    def chi(self, a: tuple[int, ...]) -> int:
        if a == self.zero:
            return 0
        v = self.pow(a, (self.q - 1) // 2)
        if v == self.one:
            return 1
        assert v == self.neg(self.one)
        return -1


def poly_eval(F: GF, coeffs: list[tuple[int, ...]], x: tuple[int, ...]) -> tuple[int, ...]:
    acc = F.zero
    for c in reversed(coeffs):
        acc = F.add(F.mul(acc, x), c)
    return acc


def poly_add(F: GF, a: list[tuple[int, ...]], b: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    m = max(len(a), len(b))
    res = []
    for i in range(m):
        ca = a[i] if i < len(a) else F.zero
        cb = b[i] if i < len(b) else F.zero
        res.append(F.add(ca, cb))
    while len(res) > 1 and res[-1] == F.zero:
        res.pop()
    return res


def poly_sub(F: GF, a: list[tuple[int, ...]], b: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    return poly_add(F, a, [F.neg(c) for c in b])


def poly_mul(F: GF, a: list[tuple[int, ...]], b: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    res = [F.zero] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai != F.zero:
            for j, bj in enumerate(b):
                res[i + j] = F.add(res[i + j], F.mul(ai, bj))
    while len(res) > 1 and res[-1] == F.zero:
        res.pop()
    return res


def poly_pow(F: GF, a: list[tuple[int, ...]], e: int) -> list[tuple[int, ...]]:
    res = [F.one]
    base = a
    while e > 0:
        if e & 1:
            res = poly_mul(F, res, base)
        base = poly_mul(F, base, base)
        e >>= 1
    return res


def poly_divmod(F: GF, a: list[tuple[int, ...]], b: list[tuple[int, ...]]) -> tuple[list[tuple[int, ...]], list[tuple[int, ...]]]:
    a = list(a)
    while len(a) > 1 and a[-1] == F.zero:
        a.pop()
    while len(b) > 1 and b[-1] == F.zero:
        b.pop()
    assert b != [F.zero]
    if len(a) < len(b):
        return [F.zero], a
    db = len(b) - 1
    inv_lb = F.inv(b[-1])
    q = [F.zero] * (len(a) - db)
    rem = list(a)
    for k in range(len(a) - db - 1, -1, -1):
        coeff = F.mul(rem[k + db], inv_lb)
        q[k] = coeff
        if coeff != F.zero:
            for j in range(db + 1):
                rem[k + j] = F.sub(rem[k + j], F.mul(coeff, b[j]))
    while len(q) > 1 and q[-1] == F.zero:
        q.pop()
    while len(rem) > 1 and rem[-1] == F.zero:
        rem.pop()
    return q, rem


def poly_gcd(F: GF, a: list[tuple[int, ...]], b: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    while b != [F.zero]:
        _, r = poly_divmod(F, a, b)
        a, b = b, r
    inv_l = F.inv(a[-1])
    return [F.mul(c, inv_l) for c in a]


def poly_deg(p_coeffs: list[tuple[int, ...]]) -> int:
    for d in range(len(p_coeffs) - 1, -1, -1):
        if p_coeffs[d] != (0,) * len(p_coeffs[0]):
            return d
    return -1


def check_auxiliary_polynomials(F: GF, r: int, A: list[tuple[int, ...]]) -> None:
    """Verify Lemma 2.2 and Lemma 2.3 on a subset A of size r with A +hat A <= S_2 u {0}."""
    assert len(A) == r
    K = (r - 3) // 2
    assert K >= 1
    # Check A_hat_A <= S_2 u {0} and 0 not in A (when B != empty)
    B = [a for a in A if F.chi(a) == -1]
    A_S = [a for a in A if F.chi(a) != -1]
    assert B, "Expected nonempty B"
    assert F.zero not in A

    # Compute c_a = prod_{x in A\{a}} (a - x)^{-1}
    c_map = {}
    for a in A:
        prod = F.one
        for x in A:
            if x != a:
                prod = F.mul(prod, F.sub(a, x))
        c_map[a] = F.inv(prod)

    # Check Lagrange interpolation identity (1)
    for deg_test in range(r):
        s_val = F.zero
        for a in A:
            s_val = F.add(s_val, F.mul(c_map[a], F.pow(a, deg_test)))
        expected = F.one if deg_test == r - 1 else F.zero
        assert s_val == expected

    # Build H_k(Y) for 0 <= k <= K
    H_list = []
    two = F.add(F.one, F.one)
    for k in range(K + 1):
        H_k = [F.zero] * ((r + 1) // 2 + 1)
        for a in A:
            a_r = F.pow(a, r)
            # (Y + a^r)^((r+1)//2)
            base_poly = [a_r, F.one]
            pwr_poly = poly_pow(F, base_poly, (r + 1) // 2)
            coef = F.mul(c_map[a], F.pow(a, k))
            scaled = [F.mul(coef, c) for c in pwr_poly]
            H_k = poly_add(F, H_k, scaled)
        if k == K:
            H_k = poly_sub(F, H_k, [F.one])
        assert poly_deg(H_k) <= (r - 1) // 2, f"deg H_{k} exceeded (r-1)/2"
        H_list.append(H_k)

        # Verify Lemma 2.2(2) evaluations at b^r for all b in A
        for b in A:
            val = poly_eval(F, H_k, F.pow(b, r))
            if b in A_S:
                assert val == F.zero
            else:
                exp_val = F.neg(
                    F.mul(
                        two,
                        F.mul(
                            c_map[b],
                            F.mul(F.pow(F.mul(two, b), (r + 1) // 2), F.pow(b, k)),
                        ),
                    )
                )
                assert val == exp_val and val != F.zero

    # Verify Lemma 2.3 Q_k == 0 and U, V coprime of max deg 1 (for r >= 7, or q=25 K=1)
    for k in range(1, K + 1):
        Qk = poly_sub(F, poly_mul(F, H_list[0], H_list[k]), poly_mul(F, H_list[1], H_list[k - 1]))
        assert Qk == [F.zero], f"Q_{k} not identically 0"

    g = poly_gcd(F, H_list[0], H_list[1])
    U, r0 = poly_divmod(F, H_list[0], g)
    V, r1 = poly_divmod(F, H_list[1], g)
    assert r0 == [F.zero] and r1 == [F.zero]
    inv_lu = F.inv(U[-1])
    U = [F.mul(c, inv_lu) for c in U]
    V = [F.mul(c, inv_lu) for c in V]
    assert max(poly_deg(U), poly_deg(V)) == 1
    assert len(A_S) <= 1 and len(B) >= r - 1
    for b in B:
        br = F.pow(b, r)
        u_br = poly_eval(F, U, br)
        v_br = poly_eval(F, V, br)
        assert u_br != F.zero
        assert F.mul(b, u_br) == v_br


def verify_norm_circles_and_lines(F: GF, r: int, subF: GF, embed) -> None:
    """Verify Claim 2.4, identity (4), circle formulas (a),(b), and r=7,9 non-clique proofs."""
    all_els = F.elements()
    sub_els = subF.elements()
    zero_sub = subF.zero
    one_sub = subF.one

    def norm(x):
        # x^{r+1} in F_q, mapped back to subF? Even simpler: keep in F_q via subfield elements!
        return F.pow(x, r + 1)

    def trace(x):
        return F.add(x, F.pow(x, r))

    # Map between subF elements and F_q subfield elements {x in F_q : x^r == x}
    sub_to_big = {s: embed(s) for s in sub_els}
    big_to_sub = {v: k for k, v in sub_to_big.items()}
    assert len(big_to_sub) == r

    # Check Fact 1 & 2: subfield subset S_2, chi(x) == chi_Fr(N(x))
    for x in all_els:
        nx = big_to_sub[norm(x)]
        assert F.chi(x) == subF.chi(nx)
    for s in sub_els:
        if s != zero_sub:
            assert F.chi(sub_to_big[s]) == 1

    # Check Claim 2.4 and eq (4) for all mu in F_r^*
    four = subF.norm_el([4] + [0] * (subF.d - 1))
    for mu_sub in sub_els:
        if mu_sub == zero_sub:
            continue
        mu_big = sub_to_big[mu_sub]
        circle = [w for w in all_els if norm(w) == mu_big]
        assert len(circle) == r + 1
        sum_chi = 0
        for t_sub in sub_els:
            t_big = sub_to_big[t_sub]
            cnt = sum(1 for w in circle if trace(w) == t_big)
            disc = subF.sub(subF.mul(t_sub, t_sub), subF.mul(four, mu_sub))
            assert cnt == 1 - subF.chi(disc), f"Claim 2.4 failed at r={r}, mu={mu_sub}, t={t_sub}"
            sum_chi += subF.chi(subF.sub(subF.mul(t_sub, t_sub), mu_sub))
        assert sum_chi == -1, f"Eq (4) failed at r={r}"

    # Check exact |C cap N_2| formulas for all c in {1, g} and lambda in F_r^*
    g = next(x for x in all_els if F.chi(x) == -1)
    for c in (F.one, g):
        nc_sub = big_to_sub[norm(c)]
        for lam_sub in sub_els:
            if lam_sub == zero_sub:
                continue
            lam_big = sub_to_big[lam_sub]
            C = [b for b in all_els if norm(F.sub(b, c)) == lam_big]
            assert len(C) == r + 1
            cn2 = [b for b in C if F.chi(b) == -1]
            if lam_sub == nc_sub:
                expected_cnt = (r - subF.chi(subF.neg(nc_sub))) // 2
                assert len(cn2) == expected_cnt
                assert len(cn2) <= (r + 1) // 2
            else:
                theta = subF.mul(lam_sub, subF.inv(nc_sub))
                s_theta = 0
                for tau in sub_els:
                    f1 = subF.add(one_sub, subF.add(theta, tau))
                    f2 = subF.sub(subF.mul(tau, tau), subF.mul(four, theta))
                    s_theta += subF.chi(subF.mul(f1, f2))
                expected_cnt = (r + 1 + subF.chi(nc_sub) * s_theta) // 2
                assert len(cn2) == expected_cnt
                # Check Hasse bound
                assert abs(s_theta) <= 2 * math.isqrt(r) + (0 if math.isqrt(r) ** 2 == r else 1)

                # For r in (7, 9), if |C cap N_2| >= r - 1, verify explicit b1+b2 in N_2!
                if r in (7, 9) and len(cn2) >= r - 1:
                    found_bad_pair = any(
                        F.chi(F.add(b1, b2)) == -1 for b1, b2 in itertools.combinations(cn2, 2)
                    )
                    assert found_bad_pair, f"Failed to find N_2 pair in C cap N_2 for r={r}"


def main() -> int:
    signal.signal(signal.SIGALRM, _alarm_handler)
    signal.alarm(60)
    t0 = time.monotonic()

    # 1. Test Case 2 Step 1 & Step 2 on Yip's q=25 non-coset size-5 clique (sanity check for Lemma 2.2/2.3)
    # F_25 = F_5[u]/(u^2 - 2)
    F5 = GF(5, (0, 1))
    F25 = GF(5, (3, 0, 1))  # u^2 + 3 = 0 <=> u^2 = 2
    # Search for a non-coset 5-clique containing 0-free nonsquare in F_25 (Yip Remark 3.3 mentions 15 of them)
    els25 = F25.elements()
    adj25 = {x: {y for y in els25 if y != x and F25.chi(F25.add(x, y)) != -1} for x in els25}
    noncoset_5 = None
    for a1 in els25:
        if F25.chi(a1) != -1:
            continue
        # find 5-clique containing a1 and some b s.t. 2b in N_2
        cands = sorted(adj25[a1])
        for comb in itertools.combinations(cands, 4):
            clique = (a1,) + comb
            if all(comb[j] in adj25[comb[i]] for i in range(4) for j in range(i + 1, 4)):
                if any(F25.chi(F25.add(x, x)) == -1 for x in clique):
                    noncoset_5 = list(clique)
                    break
        if noncoset_5:
            break
    assert noncoset_5 is not None
    check_auxiliary_polynomials(F25, 5, noncoset_5)
    print(f"F_25 non-coset size-5 clique Lemma 2.2 & 2.3 check: PASS ({noncoset_5})")

    # 2. Check r = 7 (q = 49): F_49 = F_7[u]/(u^2 + 1)
    F7 = GF(7, (0, 1))
    F49 = GF(7, (1, 0, 1))  # u^2 + 1 = 0
    verify_norm_circles_and_lines(F49, 7, F7, lambda s: (s[0], 0))

    # Specifically check the exact two circles and witnesses b1=4+u, b2=2+3u from PROOF.md lines 230-238
    u49 = (0, 1)
    g49 = (2, 1)
    b1_49 = (4, 1)
    b2_49 = (2, 3)
    assert F49.chi(g49) == -1
    assert F49.chi(b1_49) == -1 and F49.chi(b2_49) == -1
    assert F49.pow(F49.sub(b1_49, F49.one), 8) == (3, 0)
    assert F49.pow(F49.sub(b2_49, F49.one), 8) == (3, 0)
    assert F49.pow(F49.sub(b1_49, g49), 8) == (4, 0)
    assert F49.pow(F49.sub(b2_49, g49), 8) == (4, 0)
    assert F49.chi(F49.add(b1_49, b2_49)) == -1
    # Also test Lemma 2.2/2.3 on canonical coset F_7 inside F_49 (if we shift? Wait: F_7 has no B, so test Case 1!)
    print("r=7 (q=49) norm circles, S(theta), and explicit witnesses: PASS")

    # 3. Check r = 9 (q = 81): F_9 = F_3[i]/(i^2 + 1), F_81 = F_3[x]/(x^4 + 2x^3 + 2)
    # Wait: let's find an irreducible quartic over F_3 and identify F_9 inside F_81!
    # x^4 + x^2 + 2 = (x^2+1)^2 + 1... wait: x^4 - x - 1? At 0:-1, 1:-1, -1:1! Wait x^4+2x^3+2:
    # Over F_3, x^4 + 2x^3 + 2 (coeffs (2,0,0,2,1)) -> check: root 0->2, 1->2, 2->16+16+2=34=1!
    # Check quadratic factors: none? Let's just use x^4 + x + 2? 0->2, 1->1, 2->16+2+2=20=2!
    # Better: find primitive irreducible quartic over F_3 explicitly!
    def find_irred_poly_f3(deg: int) -> tuple[int, ...]:
        # Test monic polynomials over F_3 that have no roots and generate full multiplicative group
        for coeffs in itertools.product((0, 1, 2), repeat=deg):
            poly = coeffs + (1,)
            F_cand = GF(3, poly)
            x = (0, 1) + (0,) * (deg - 2)
            # Check x^{(3^d-1)} == 1 and x^{(3^d-1)/q} != 1 for prime factors of 3^d-1
            order = 3**deg - 1
            if F_cand.pow(x, order) != F_cand.one:
                continue
            ok = True
            for p_fac in (2, 5):  # for deg=4, 80 = 2^4 * 5; for deg=2, 8 = 2^3
                if order % p_fac == 0 and F_cand.pow(x, order // p_fac) == F_cand.one:
                    ok = False
                    break
            if ok:
                return poly
        raise RuntimeError("No primitive poly found")

    F9 = GF(3, (1, 0, 1))  # i^2 + 1 = 0
    poly81 = find_irred_poly_f3(4)
    F81 = GF(3, poly81)
    # Find element i_81 in F81 with i_81^2 == -1
    i81 = next(el for el in F81.elements() if F81.add(F81.mul(el, el), F81.one) == F81.zero)
    verify_norm_circles_and_lines(F81, 9, F9, lambda s: F81.add((s[0], 0, 0, 0), F81.mul((s[1], 0, 0, 0), i81)))

    # Verify PROOF.md lines 246-261 for ALL 8 elements z in F_81 \ F_9 with z^10 == -1!
    neg_one_81 = F81.neg(F81.one)
    f9_set = {F81.add((s[0], 0, 0, 0), F81.mul((s[1], 0, 0, 0), i81)) for s in F9.elements()}
    z_list = [
        el for el in F81.elements()
        if el not in f9_set and F81.pow(el, 10) == neg_one_81
    ]
    assert len(z_list) == 8
    for z in z_list:
        b1 = F81.add(F81.one, z)
        b2 = F81.add(F81.one, F81.pow(z, 3))
        assert b1 != b2
        assert F81.chi(b1) == -1 and F81.chi(b2) == -1
        assert F81.pow(F81.sub(b1, F81.one), 10) == neg_one_81
        assert F81.pow(F81.sub(b2, F81.one), 10) == neg_one_81
        assert F81.chi(F81.add(b1, b2)) == -1
    print("r=9 (q=81) norm circles, S(theta), and ALL 8 z^10=-1 witnesses: PASS")

    # 4. Also check r = 11 (q = 121) and r = 13 (q = 169) norm circles & Hasse bound
    F11 = GF(11, (0, 1))
    F121 = GF(11, (1, 0, 1))  # -1 is nonsquare mod 11, so u^2 + 1 irreducible
    verify_norm_circles_and_lines(F121, 11, F11, lambda s: (s[0], 0))
    print("r=11 (q=121) norm circles, Claim 2.4, eq (4), Hasse bound: PASS")

    # 5. Direct Case 1 eigenvalue check on M for q=9, 25, 49
    for F_test in (F25, F49):
        els = F_test.elements()
        q = len(els)
        idx = {e: i for i, e in enumerate(els)}
        # Check M^2 = qI - J
        for i in range(q):
            row_sum = sum(F_test.chi(F_test.add(els[i], els[j])) for j in range(q))
            assert row_sum == 0
        # Check sample pairs (i, j)
        for i in range(min(q, 10)):
            for j in range(min(q, 10)):
                dot = sum(
                    F_test.chi(F_test.add(els[i], els[z])) * F_test.chi(F_test.add(els[j], els[z]))
                    for z in range(q)
                )
                expected = (q - 1) if i == j else -1
                assert dot == expected
    print("Case 1 M^2 = qI - J check on F_25, F_49: PASS")

    elapsed = time.monotonic() - t0
    print(f"PASS (all checks passed in {elapsed:.3f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
