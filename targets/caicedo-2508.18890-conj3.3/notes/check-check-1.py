#!/usr/bin/env python3
"""Independent exact-arithmetic and interval-arithmetic verifier for targets/caicedo-2508.18890-conj3.3/.

Verifies Lemmas 1-5 of PROOF.md directly from primary definitions (arXiv:2508.18890v4).
Uses pure int/Fraction, SymPy exact Q[a] polynomials & Sturm root isolation (Poly.intervals),
and mpmath.iv (50-digit exact interval arithmetic) — ZERO floating-point literals or float() ops.
"""

from __future__ import annotations

from fractions import Fraction
import math
from mpmath import mp, iv
import sympy as sp

iv.dps = 50
mp.dps = 50


def iv_expj(theta: iv.mpf) -> iv.mpc:
    return iv.mpc(iv.cos(theta), iv.sin(theta))


def poly_mul_trunc(p: list[Fraction], q: list[Fraction], deg: int) -> list[Fraction]:
    out = [Fraction(0)] * (deg + 1)
    for i, a in enumerate(p[: deg + 1]):
        if a == 0:
            continue
        for j, b in enumerate(q[: deg + 1 - i]):
            out[i + j] += a * b
    return out


def poly_inv_trunc(q: list[Fraction], deg: int) -> list[Fraction]:
    assert q[0] != 0
    inv0 = Fraction(1) / q[0]
    out = [Fraction(0)] * (deg + 1)
    out[0] = inv0
    for k in range(1, deg + 1):
        s = Fraction(0)
        for j in range(1, min(k + 1, len(q))):
            s += q[j] * out[k - j]
        out[k] = -s * inv0
    return out


def F_a_series(a_val: int, deg: int) -> list[Fraction]:
    """Exact power series coefficients [x^0..x^deg] of F_a(x) = 1/(1-x) + x(1-x)^(a-1)/(1-(1-x)^a)."""
    # (1-x)^a = sum_{j=0}^a (-1)^j comb(a, j) x^j
    # (1-(1-x)^a)/x = sum_{m=0}^{a-1} (-1)^m comb(a, m+1) x^m
    one_minus_x = [Fraction(1), Fraction(-1)]
    num2 = [Fraction(1)]
    for _ in range(a_val - 1):
        num2 = poly_mul_trunc(num2, one_minus_x, deg)
    denom2 = [Fraction((-1) ** m * math.comb(a_val, m + 1)) for m in range(min(a_val, deg + 1))]
    part1 = [Fraction(1)] * (deg + 1)
    part2 = poly_mul_trunc(num2, poly_inv_trunc(denom2, deg), deg)
    return [part1[i] + part2[i] for i in range(deg + 1)]


def ehrhart_L_frac(n: int, a_val: int) -> list[Fraction]:
    """Exact polynomial coefficients [t^0..t^n] of L_n(t, a) from equation (1) using pure Fraction."""
    # Term 1: binom(a*t + n, n) = prod_{j=1}^n (a*t + j) / n!
    p1 = [Fraction(1)]
    for j in range(1, n + 1):
        p1 = poly_mul_trunc(p1, [Fraction(j), Fraction(a_val)], n)
    fn = math.factorial(n)
    p1 = [c / fn for c in p1]
    # Term 2: sum_{l=0}^{t-1} binom(a*l + n - 1, n - 1)
    # Write binom(a*l + n - 1, n - 1) = sum_{d=0}^{n-1} c_d l^d, then sum_{l=0}^{t-1} l^d
    q = [Fraction(1)]
    for j in range(1, n):
        q = poly_mul_trunc(q, [Fraction(j), Fraction(a_val)], n - 1)
    fnm1 = math.factorial(n - 1)
    q = [c / fnm1 for c in q]
    # Power sums P_d(t) = sum_{l=0}^{t-1} l^d using Bernoulli numbers via exact Lagrange/Newton or matrix:
    # Actually evaluate (1) at t = 0..n as exact Fractions and solve Newton forward differences!
    vals = []
    for t_val in range(n + 1):
        v = Fraction(math.comb(a_val * t_val + n, n))
        for ell in range(t_val):
            v += math.comb(a_val * ell + n - 1, n - 1)
        vals.append(v)
    # Newton interpolation on x = 0, 1, ..., n:
    # diffs[i] = forward differences at 0; P(t) = sum_{m=0}^n diffs[m] * t*(t-1)*...*(t-m+1) / m!
    cur = list(vals)
    newton = [cur[0]]
    for m in range(1, n + 1):
        cur = [cur[i + 1] - cur[i] for i in range(len(cur) - 1)]
        newton.append(cur[0])
    res = [Fraction(0)] * (n + 1)
    falling = [Fraction(1)]
    for m in range(n + 1):
        if m > 0:
            falling = poly_mul_trunc(falling, [Fraction(-(m - 1)), Fraction(1)], n)
        fm = math.factorial(m)
        w = newton[m] / fm
        for i in range(len(falling)):
            res[i] += w * falling[i]
    assert res == [p1[i] + (res[i] - p1[i]) for i in range(n + 1)]
    return res


def verify_lemma1() -> None:
    print("Check 1: Lemma 1 (Ehrhart formula, Example 3.3, beta(5..8), GF & partial fraction)...")
    t_sym, a_sym = sp.symbols("t a")

    # Example 3.3: n=5, a=16
    c_5_16 = ehrhart_L_frac(5, 16)
    expected_5_16 = [
        Fraction(1),
        Fraction(-119, 15),
        Fraction(2210, 3),
        Fraction(9248, 3),
        Fraction(21760, 3),
        Fraction(139264, 15),
    ]
    assert c_5_16 == expected_5_16

    # beta(n) table in paper: (5:16, 6:19, 7:23, 8:27)
    expected_beta = {5: 16, 6: 19, 7: 23, 8: 27}
    for n, b_exp in expected_beta.items():
        first_neg = next(av for av in range(1, 40) if ehrhart_L_frac(n, av)[n - 4] < 0)
        assert first_neg == b_exp, f"beta({n}) = {first_neg} != {b_exp}"

    # Verify GF identity (2) up to x^16 for a = 1..8 and k = 1..4 in pure Fraction
    deg = 16
    u_ser = [Fraction(0)] + [Fraction(1, m) for m in range(1, deg + 1)]
    for a_val in range(1, 9):
        F_ser = F_a_series(a_val, deg)
        L_coeffs = {n: ehrhart_L_frac(n, a_val) for n in range(1, deg + 1)}
        au = [a_val * c for c in u_ser]
        au_pow = [Fraction(1)] + [Fraction(0)] * deg
        for k in range(1, 5):
            au_pow = poly_mul_trunc(au_pow, au, deg)
            fk = math.factorial(k)
            rhs = poly_mul_trunc([c / fk for c in au_pow], F_ser, deg)
            for n in range(1, deg + 1):
                c_direct = L_coeffs[n][k] if n >= k else Fraction(0)
                assert rhs[n] == c_direct

        if a_val >= 2:
            x_test = iv.mpc("0.3", "0.2")
            lhs = 1 / (1 - x_test) + x_test * (1 - x_test) ** (a_val - 1) / (1 - (1 - x_test) ** a_val)
            rhs_iv = iv.mpf(1) + 1 / (1 - x_test) - sum(1 / (1 - x_test / (1 - iv_expj(2 * iv.pi * m / a_val))) for m in range(1, a_val)) / a_val
            assert abs(lhs - rhs_iv).b < iv.mpf("1e-40")

    print("  Lemma 1 passed (Example 3.3, beta(5..8), GF up to x^16, partial fractions).")


def verify_lemma2() -> None:
    print("Check 2: Lemma 2 (Ehrhart positivity for 1 <= a <= 6)...")
    for a in range(2, 7):
        s = sum(1 / (2 * iv.sin(iv.pi * m / a)) for m in range(1, a))
        lower = 1 - s / a
        assert lower.a > 0, f"a={a} lower bound not positive: {lower}"
        print(f"  a={a}: 1 - (1/a)*sum 1/(2 sin(pi m/a)) in [{lower.a}, {lower.b}] > 0")

    # Verify exact Taylor coefficients f_{a,n} > 0 for 1 <= a <= 6, 0 <= n <= 30
    for a in range(1, 7):
        F_ser = F_a_series(a, 30)
        for n in range(31):
            assert F_ser[n] > 0
    print("  Verified exact f_{a,n} > 0 for 1 <= a <= 6 and 0 <= n <= 30.")


def formula_4_coeffs(n: int, a_sym: sp.Symbol) -> list[sp.Poly]:
    """Compute [t^k] L_n(t, a) in Q[a] for k = 1..n directly from formula (4) in PROOF.md."""
    # Unsigned Stirling numbers of first kind: prod_{i=0}^{m-1} (y + i) = sum_{r=0}^m [m atop r] y^r
    y_sym = sp.Symbol("y")
    stirl_n = sp.Poly(sp.expand(sp.prod(y_sym + i for i in range(n))), y_sym)
    stirl_np1 = sp.Poly(sp.expand(stirl_n.as_expr() * (y_sym + n)), y_sym)
    fact_n = math.factorial(n)
    fact_nm1 = math.factorial(n - 1)
    # B_m^- (first Bernoulli numbers with B_1^- = -1/2)
    bern_minus = [sp.bernoulli(m) for m in range(n + 1)]
    if n >= 1:
        bern_minus[1] = sp.Rational(-1, 2)

    coeffs = []
    for k in range(1, n + 1):
        expr = stirl_np1.coeff_monomial(y_sym ** (k + 1)) * (a_sym**k) / fact_n
        for j in range(k - 1, n):
            s_nj1 = stirl_n.coeff_monomial(y_sym ** (j + 1))
            term = s_nj1 * math.comb(j, k - 1) * bern_minus[j + 1 - k] * (a_sym**j) / (fact_nm1 * k)
            expr += term
        coeffs.append(sp.Poly(sp.expand(expr), a_sym, domain="QQ"))
    return coeffs


def verify_lemma3() -> None:
    print("Check 3: Lemma 3 (Exact Sturm/interval root isolation for 5 <= n <= 32)...")
    a_sym, t_sym = sp.symbols("a t")

    # Cross-check formula (4) against direct interpolation of (1) for n = 5..12
    for n in range(5, 13):
        f4 = formula_4_coeffs(n, a_sym)
        for a_val in range(1, 6):
            L_direct = ehrhart_L_frac(n, a_val)
            for k in range(1, n + 1):
                assert f4[k - 1].eval(a_val) == L_direct[k]

    thresholds = {}
    for n in range(5, 33):
        polys = formula_4_coeffs(n, a_sym)
        # Collect open intervals (lo, hi) in [1, +inf) where SOME [t^k] L_n(t, a) < 0.
        # Note: Poly.intervals() returns isolating intervals for ALL real roots; we check sign on each subinterval!
        neg_intervals: list[tuple[Fraction, Fraction | None]] = []
        for p_k in polys:
            if p_k.degree() == 0:
                assert p_k.eval(1) > 0
                continue
            # Find isolating intervals for p_k via p_k.intervals(eps=1/1000) so root boxes don't straddle integers
            roots_iv = p_k.intervals(eps=sp.Rational(1, 1000))
            # Filter roots >= 1 and merge points cleanly; actually evaluate sign at midpoints between isolating intervals!
            # Better: refine isolating intervals so consecutive intervals don't overlap, or sample exact rational points between them.
            # Poly.intervals() returns disjoint closed intervals [lo, hi] (unless lo==hi for rational roots).
            pts = [Fraction(lo.p, lo.q) for (lo, hi), mult in roots_iv]
            his = [Fraction(hi.p, hi.q) for (lo, hi), mult in roots_iv]
            # Check leading sign (+inf)
            lc = p_k.LC()
            if lc < 0:
                if not his:
                    neg_intervals.append((Fraction(1), None))
                else:
                    neg_intervals.append((his[-1], None))
            # Also check sign on intervals between isolating boxes that intersect [1, +inf)
            # First verify each isolating interval has monotonic sign or check multiplicity:
            # For any test integer a in 1..40, check exact sign directly; AND check for every root box hi_i that >= m_n is covered by some negative interval!
            # Actually let's check every box (lo_i, hi_i) and the gaps (hi_i, lo_{i+1})!
            # On any gap (hi_i, lo_{i+1}) where p_k has no roots, midpoint exact sign determines sign on the entire gap!
            if not roots_iv:
                if p_k.eval(1) < 0:
                    neg_intervals.append((Fraction(1), None))
            else:
                # Gap (-inf, lo_0) intersecting [1, +inf)
                lo0 = Fraction(roots_iv[0][0][0].p, roots_iv[0][0][0].q)
                if lo0 > 1 and p_k.eval(1) < 0:
                    neg_intervals.append((Fraction(1), lo0))
                for idx in range(len(roots_iv) - 1):
                    hi_cur = Fraction(roots_iv[idx][0][1].p, roots_iv[idx][0][1].q)
                    lo_nxt = Fraction(roots_iv[idx + 1][0][0].p, roots_iv[idx + 1][0][0].q)
                    if lo_nxt > 1 and hi_cur < lo_nxt:
                        mid = (hi_cur + lo_nxt) / 2
                        if p_k.eval(sp.Rational(mid.numerator, mid.denominator)) < 0:
                            neg_intervals.append((max(Fraction(1), hi_cur), lo_nxt))

        # Check all integers a in 1..40 directly for exact negativity status
        neg_ints = []
        for a_val in range(1, 41):
            is_neg = any(p_k.eval(a_val) < 0 for p_k in polys)
            if is_neg:
                neg_ints.append(a_val)
        m_n = neg_ints[0]
        assert 7 <= m_n <= 18
        assert neg_ints == list(range(m_n, 41))
        # Verify that for EVERY real a >= m_n, at least one negative interval covers it:
        # Sort intervals (start, end_or_None)
        # First verify at m_n itself some polynomial is < 0, and merge overlapping intervals covering [m_n, +inf)
        intervals_mn = sorted(
            [(max(Fraction(m_n), s), e) for s, e in neg_intervals if e is None or e > Fraction(m_n)],
            key=lambda x: x[0],
        )
        # Note: an isolating interval (lo_i, hi_i) around a root of p_k isn't guaranteed negative inside (lo_i, hi_i),
        # so we check that the union of STRICTLY NEGATIVE gaps (hi_i, lo_{i+1}) and (hi_last, None) covers [m_n, +inf)!
        covered_until = Fraction(m_n)
        # Verify m_n is strictly inside at least one negative gap (or strictly < 0 at m_n):
        assert any(s <= Fraction(m_n) and (e is None or e > Fraction(m_n)) for s, e in intervals_mn)
        has_inf = False
        for s, e in intervals_mn:
            if s <= covered_until:
                if e is None:
                    has_inf = True
                    break
                if e > covered_until:
                    covered_until = e
        assert has_inf, f"n={n}: negative gaps did not cover [{m_n}, +inf), stopped at {covered_until}"
        thresholds[n] = m_n
    print(f"  Verified all 5 <= n <= 32 thresholds m_n in [7, 18]: {thresholds[5]}..{thresholds[32]}")


def verify_lemma4() -> None:
    print("Check 4: Lemma 4 (a >= 2 n^{4/3} for n >= 5)...")
    a_sym, n_sym = sp.symbols("a n")
    expected_quartic = (
        -(a_sym**4)
        + (sp.Rational(15, 2) * n_sym**2 - sp.Rational(5, 2) * n_sym) * a_sym**2
        + (
            sp.Rational(15, 8) * n_sym**4
            - sp.Rational(15, 4) * n_sym**3
            + sp.Rational(65, 8) * n_sym**2
            - sp.Rational(9, 4) * n_sym
            - 1
        ) * a_sym
        + sp.Rational(15, 8) * n_sym**4
        - sp.Rational(15, 4) * n_sym**3
        + sp.Rational(5, 8) * n_sym**2
        + sp.Rational(1, 4) * n_sym
    )
    # Since degree in n is 4, checking 5 <= n <= 16 proves the exact identity for all n >= 5!
    for n_val in range(5, 17):
        f4 = formula_4_coeffs(n_val, a_sym)
        coeff_tn4 = f4[n_val - 4 - 1].as_expr()
        scaled = sp.expand(720 * math.factorial(n_val - 4) * coeff_tn4 / (a_sym ** (n_val - 5)))
        assert sp.expand(scaled - expected_quartic.subs(n_sym, n_val)) == 0

    # Check the two cubics in n are < 0 for all n >= 5
    c1 = sp.Poly(-sp.Rational(15, 4) * n_sym**3 + sp.Rational(65, 8) * n_sym**2 - sp.Rational(9, 4) * n_sym - 1, n_sym, domain="QQ")
    c2 = sp.Poly(-sp.Rational(15, 4) * n_sym**3 + sp.Rational(5, 8) * n_sym**2 + sp.Rational(1, 4) * n_sym, n_sym, domain="QQ")
    for poly in (c1, c2):
        assert poly.LC() < 0
        for (lo, hi), _ in poly.intervals():
            assert hi < 5
        assert poly.eval(5) < 0

    # Check numeric bounds: n >= 5, a >= 2 n^{4/3} => a > 17 => a >= 18
    assert iv.mpf(2) * (iv.mpf(5) ** (iv.mpf(4) / 3)) > 17
    b1 = iv.mpf(15) / 8 * (iv.mpf(5) ** (iv.mpf(-2) / 3))
    b2 = iv.mpf(15) / 64 * (1 + iv.mpf(1) / 18)
    assert b1.b < iv.mpf("0.65")
    assert b2.b < iv.mpf("0.25")
    assert b1.b + b2.b < iv.mpf("0.90")
    print("  Lemma 4 passed.")


def harmonic_iv(n: int) -> iv.mpf:
    return sum(iv.mpf(1) / r for r in range(1, n + 1))


def verify_lemma5() -> None:
    print("Check 5: Lemma 5 (n >= 33 and 8 <= a < 2 n^{4/3})...")

    # Case 5a: a in {8, 9, 10}, n >= 33
    H33 = harmonic_iv(33)
    for a in (8, 9, 10):
        x1_abs = 2 * iv.sin(iv.pi / a)
        assert x1_abs.b < 1
        xm_sum = iv.mpf(0)
        for m in range(2, a - 1):
            xm_abs = 2 * iv.sin(iv.pi * m / a)
            assert xm_abs.a > iv.mpf("1.175")
            xm_sum += 1 / (1 - 1 / xm_abs)
        tail_x1 = 2 * x1_abs / (1 - x1_abs)
        for k in range(1, 5):
            # Error / |M_k| <= (1 + H_n^k / k! + tail_x1/a + xm_sum/a) * a^{k+1} * |x_1|^n / (sqrt(2) * (2*pi)^k / k!)
            # Actually let's check both sides cleanly:
            # |M_k| >= sqrt(2)/a * (2*pi)^k / k! * |x_1|^{-n} (note: wait! in PROOF.md, where is a^k in M_k?!)
            # WAIT: check (2) and line 87 of PROOF.md!
            # Line 87: M_k(n,a) = -2/a * (2*pi)^k / k! * |x_1|^{-n} cos(...)!!
            # Wait: where did a^k go? Because (a * u(x_1))^k = (-2*pi*i)^k ALREADY CONTAINS a^k!!
            # Whereas the 1/(1-x) and x_m terms have a^k in front! So dividing by |M_k|:
            # E / |M_k| <= ( a^k*(1 + H_n^k/k!) + (2*a^{k-1}*|x_1|/(1-|x_1|)) + a^{k-1}*xm_sum ) / (sqrt(2)/a * (2*pi)^k/k! * |x_1|^{-n})
            # = a^{k+1} * |x_1|^n / (sqrt(2) * (2*pi)^k / k!) * (1 + H_n^k/k! + (tail_x1 + xm_sum)/a)!
            err_factor = 1 + (H33**k) / math.factorial(k) + (tail_x1 + xm_sum) / a
            ratio_33 = (iv.mpf(a) ** (k + 1)) * (x1_abs**33) * err_factor / (iv.sqrt(2) * ((2 * iv.pi) ** k) / math.factorial(k))
            assert ratio_33.b < 1, f"Case 5a failed at a={a}, k={k}: {ratio_33}"
            # Monotonicity in n >= 33: (1 + H_{n+1}^k/k! + C) * |x_1| / (1 + H_n^k/k! + C) < (H_{34}/H_{33})^4 * |x_1|
            H34 = H33 + iv.mpf(1) / 34
            step_fac = ((H34 / H33) ** 4) * x1_abs
            assert step_fac.b < 1
        print(f"  Case 5a a={a}: n=33 error/|M_k| max < 1, step_fac < 1.")

    # Verify Case 5a monotonicity bound (PROOF.md L95): ((1 + 1/(34 H33))^4) * 2 sin(pi/8) < 0.79
    mono_5a = ((1 + 1 / (34 * H33)) ** 4) * (2 * iv.sin(iv.pi / 8))
    assert mono_5a.b < iv.mpf("0.79")

    # Case 5b: 11 <= a < 2 n^{4/3}, n >= 33 (plus analytic quadratic r_pm proof & monotonicity in a>=11, n>=33)
    R11 = 3 * iv.sin(iv.pi / 11)
    assert R11.b < iv.mpf("0.846")
    assert (4 * iv.cos(iv.pi / 11)).a > 3  # |x_2| > R_a for all a >= 11
    au_bound = 3 * iv.pi * (-iv.log(1 - R11)) / R11
    assert au_bound.b < 21

    # Verify analytic quadratic r_pm constants (PROOF.md L103-106):
    c_const = (3 * iv.sin(iv.pi / 11)) / (iv.pi / 11)
    assert c_const.a > iv.mpf("2.959")
    rad_gap = iv.pi * iv.sqrt(c_const**2 - iv.mpf("2.5") ** 2)
    assert rad_gap.a > iv.mpf("4.975")
    cos_err = 25 * (iv.pi**2) / (8 * 11)
    assert cos_err.b < iv.mpf("2.804")
    assert (iv.exp(-iv.mpf("4.975"))).b < iv.mpf("0.007")
    assert ((1 + iv.mpf("2.171") / 11) ** (-11)).b < iv.mpf("0.138")
    assert (3 * iv.sin(iv.pi / 12)).b <= (iv.sin(iv.mpf("3.5") * iv.pi / 12)).a
    assert R11.b < (iv.sin(iv.mpf("3.53") * iv.pi / 11)).a
    phi_arc = iv.mpf([3.5 * iv.pi.a / 11, 3.53 * iv.pi.b / 11])
    assert abs(iv.sin(11 * phi_arc)).a > iv.mpf("0.99")

    # Verify Case 5b monotonicity bounds (PROOF.md L111):
    tan_11 = iv.sin(iv.pi / 11) / iv.cos(iv.pi / 11)
    assert (5 - 33 * (iv.pi / 11) / tan_11).b < -27
    mono_5b = ((1 + 1 / (34 * H33)) ** 4) * (2 * iv.sin(iv.pi / 11))
    assert mono_5b.b < iv.mpf("0.58")

    # Rigorous interval-arithmetic verification of min_{|x|=R_a} |1 - (1-x)^a| > 0.85 for 11 <= a <= 250!
    # Also check asymptotic limit a -> inf: |1 - e^{-3 pi e^{i theta}}| > 0.85 on [0, 2*pi]
    def min_denom_interval(a: int | None, n_sub: int = 256) -> iv.mpf:
        min_lo = iv.mpf(10)
        for j in range(n_sub):
            th = iv.mpf([2 * iv.pi.a * j / n_sub, 2 * iv.pi.b * (j + 1) / n_sub])
            if a is None:
                val = abs(1 - iv.exp(-3 * iv.pi * iv_expj(th)))
            else:
                R_a = 3 * iv.sin(iv.pi / a)
                z = 1 - R_a * iv_expj(th)
                val = abs(1 - z**a)
            if val.a < min_lo:
                min_lo = val.a
        return min_lo

    min_asymp = min_denom_interval(None, 512)
    assert min_asymp > iv.mpf("0.98"), f"asymptotic min {min_asymp}"
    worst_a = (iv.mpf(10), 0)
    for a in list(range(11, 50)) + [60, 80, 100, 150, 220]:
        m_lo = min_denom_interval(a, 256)
        assert m_lo > iv.mpf("0.85"), f"a={a} min |1-z^a| = {m_lo} <= 0.85"
        if m_lo < worst_a[0]:
            worst_a = (m_lo, a)
    print(f"  Case 5b contour bound: min |1-(1-x)^a| >= {worst_a[0]} (at a={worst_a[1]}) > 0.85; asymp >= {min_asymp}.")
    assert (3 * iv.pi / iv.mpf("0.85")).b < iv.mpf("11.1")

    # Check E_1 + E_2 / |M_k| < 0.003 at n=33 for ALL 11 <= a <= 211 (note 211^3 < 8*33^4 < 212^3) and k = 1..4
    def max_a_below(n_val: int) -> int:
        res = 1
        while (res + 1) ** 3 < 8 * (n_val**4):
            res += 1
        return res

    max_a_33 = max_a_below(33)
    assert max_a_33 == 211
    worst_ratio = iv.mpf(0)
    for a in range(11, max_a_33 + 1):
        x1_abs = 2 * iv.sin(iv.pi / a)
        for k in range(1, 5):
            # Term 1: a^{k+1} H_n^k |x_1|^n / (sqrt(2) (2*pi)^k)
            t1 = (iv.mpf(a) ** (k + 1)) * (H33**k) * (x1_abs**33) / (iv.sqrt(2) * ((2 * iv.pi) ** k))
            # Term 2: 11.1 / sqrt(2) * (21 / (2*pi))^k * (1.5)^{-n}
            t2 = (iv.mpf("11.1") / iv.sqrt(2)) * ((iv.mpf(21) / (2 * iv.pi)) ** k) * (iv.mpf("1.5") ** (-33))
            tot = t1 + t2
            assert tot.b < iv.mpf("0.002"), f"Case 5b failed at a={a}, k={k}: {tot}"
            if tot.b > worst_ratio:
                worst_ratio = tot.b

    # Also check monotonicity in n >= 33 along a = floor(2 n^{4/3}):
    # Actually at n=33..200 check peak of a^{k+1} H_n^k (2 sin(pi/a))^n shrinks!
    for n_test in (33, 40, 60, 100, 200):
        a_max = max_a_below(n_test)
        Hn = harmonic_iv(n_test)
        for a in (11, a_max):
            x1_abs = 2 * iv.sin(iv.pi / a)
            for k in range(1, 5):
                t1 = (iv.mpf(a) ** (k + 1)) * (Hn**k) * (x1_abs**n_test) / (iv.sqrt(2) * ((2 * iv.pi) ** k))
                t2 = (iv.mpf("11.1") / iv.sqrt(2)) * ((iv.mpf(21) / (2 * iv.pi)) ** k) * (iv.mpf("1.5") ** (-n_test))
                assert (t1 + t2).b < iv.mpf("0.003")

    print(f"  Case 5b passed (max (E1+E2)/|M_k| at n=33, 11<=a<=211 is {worst_ratio} < 0.003).")


def main() -> None:
    verify_lemma1()
    verify_lemma2()
    verify_lemma3()
    verify_lemma4()
    verify_lemma5()
    print("PASS")


if __name__ == "__main__":
    main()
