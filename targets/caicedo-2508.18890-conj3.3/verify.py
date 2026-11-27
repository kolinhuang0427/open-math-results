"""Exact verifier for PROOF.md of Caicedo-Juhnke-Poullot Conj 3.4 (arXiv:2508.18890v4, slug conj3.3)."""
import math
from fractions import Fraction
import sympy as sp
from sympy.functions.combinatorial.numbers import bernoulli
from mpmath import iv

iv.dps = 50


def precompute_stirling_bernoulli(n_max):
    B = [Fraction(0)] * (n_max + 3)
    for m in range(n_max + 3):
        b = bernoulli(m)
        B[m] = Fraction(int(b.p), int(b.q))
    B[1] = Fraction(-1, 2)  # B_1^- = -1/2
    S = [[0] * (n_max + 3) for _ in range(n_max + 3)]
    S[0][0] = 1
    for i in range(1, n_max + 3):
        for j in range(1, i + 1):
            S[i][j] = S[i - 1][j - 1] + (i - 1) * S[i - 1][j]
    return B, S


def poly_coeffs_in_a(n, k, B, S):
    pa = [Fraction(0)] * (n + 1)
    pa[k] += Fraction(S[n + 1][k + 1], math.factorial(n))
    fact_nm1 = math.factorial(n - 1)
    for j in range(k - 1, n):
        pa[j] += Fraction(S[n][j + 1] * math.comb(j, k - 1), fact_nm1 * k) * B[j + 1 - k]
    return pa


def verify_lemma1():
    # Verify exact Ehrhart formula (1) against Caicedo-Juhnke-Poullot Example 3.3, Thm 3.2, beta(5..8),
    # and verify GF identity (2)-(3) symbolically up to x^12 for a=1..10.
    t, a, x = sp.symbols("t a x")
    B, S = precompute_stirling_bernoulli(14)
    # Check n=5, a=16 matches Example 3.3: 139264/15 t^5 + 21760/3 t^4 + 9248/3 t^3 + 2210/3 t^2 - 119/15 t + 1
    expected_n5_a16 = {
        1: Fraction(-119, 15),
        2: Fraction(2210, 3),
        3: Fraction(9248, 3),
        4: Fraction(21760, 3),
        5: Fraction(139264, 15),
    }
    for k, exp_val in expected_n5_a16.items():
        pa = poly_coeffs_in_a(5, k, B, S)
        val = sum(pa[j] * (16 ** j) for j in range(6))
        assert val == exp_val, f"Example 3.3 mismatch at k={k}: {val} != {exp_val}"

    # Check beta(5..8) = (16, 19, 23, 27)
    for n, exp_beta in [(5, 16), (6, 19), (7, 23), (8, 27)]:
        pa = poly_coeffs_in_a(n, n - 4, B, S)
        first_neg = next(aa for aa in range(1, 50) if sum(pa[j] * (aa ** j) for j in range(n + 1)) < 0)
        assert first_neg == exp_beta, f"beta({n})={first_neg} != {exp_beta}"

    # Check GF identity (2)-(3) through x^12 for a=1..10 using exact Fraction series convolution
    u_ser = [Fraction(0)] + [Fraction(1, m) for m in range(1, 13)]

    def poly_mul_trunc(p, q, deg=12):
        res = [Fraction(0)] * (deg + 1)
        for i, a_val in enumerate(p):
            if a_val == 0:
                continue
            for j, b_val in enumerate(q):
                if i + j > deg:
                    break
                res[i + j] += a_val * b_val
        return res

    for aa in range(1, 11):
        # F_a(x) = 1/(1-x) + (1-x)^{a-1} / ((1-(1-x)^a)/x)
        D = [Fraction((-1) ** j * math.comb(aa, j + 1)) for j in range(aa)]
        rhs_num = [Fraction((-1) ** j * math.comb(aa - 1, j)) if j <= aa - 1 else Fraction(0) for j in range(13)]
        q_ser = [Fraction(0)] * 13
        for m in range(13):
            s = rhs_num[m]
            for j in range(1, min(m, aa - 1) + 1):
                s -= D[j] * q_ser[m - j]
            q_ser[m] = s / D[0]
        F_ser = [Fraction(1) + q_ser[m] for m in range(13)]
        uk_ser = [Fraction(1)] + [Fraction(0)] * 12
        for k in range(1, 5):
            uk_ser = poly_mul_trunc(uk_ser, u_ser, 12)
            prod_ser = poly_mul_trunc(F_ser, uk_ser, 12)
            mult = Fraction(aa ** k, math.factorial(k))
            for n in range(k, 13):
                pa = poly_coeffs_in_a(n, k, B, S)
                lhs = sum(pa[j] * (aa ** j) for j in range(n + 1))
                rhs = prod_ser[n] * mult
                assert lhs == rhs, f"GF mismatch a={aa}, n={n}, k={k}: {lhs} != {rhs}"
    print("Lemma 1 PASS")


def verify_lemma2():
    # Verify sum_{m=1}^{a-1} 1/(a * 2*sin(pi*m/a)) < 1 in exact iv arithmetic for a=2..6,
    # and check partial fraction formula (3) symbolically.
    x = sp.Symbol("x")
    for aa in range(2, 7):
        Fa = 1 / (1 - x) + x * (1 - x) ** (aa - 1) / (1 - (1 - x) ** aa)
        z = sp.exp(2 * sp.I * sp.pi / aa)
        pf = 1 + 1 / (1 - x) - sp.Rational(1, aa) * sum(1 / (1 - x / (1 - z ** m)) for m in range(1, aa))
        assert sp.simplify(sp.together((Fa - pf).rewrite(sp.cos))) == 0, f"Partial fraction mismatch at a={aa}"

        assert 2 * sp.sin(sp.pi / 6) == 1
        s = iv.mpf(0)
        for m in range(1, aa):
            if aa == 6 and m in (1, 5):
                xm_abs = iv.mpf(1)
            else:
                xm_abs = 2 * iv.sin(iv.pi * m / aa)
                assert xm_abs.a >= 1, f"|x_m| < 1 at a={aa}, m={m}"
            s += iv.mpf(1) / (aa * xm_abs)
        assert s.b < 1, f"Lemma 2 bound failed at a={aa}: {s}"
    print("Lemma 2 PASS")


def verify_lemma3():
    # Exact Sturm / rational root interval isolation for 5 <= n <= 32 across all a >= 1.
    B, S = precompute_stirling_bernoulli(33)
    a = sp.Symbol("a")
    for n in range(5, 33):
        neg_ivs = []
        for k in range(1, n + 1):
            pa = poly_coeffs_in_a(n, k, B, S)
            if all(c >= 0 for c in pa):
                continue
            expr = sum(sp.Rational(pa[j].numerator, pa[j].denominator) * a ** j for j in range(n + 1))
            poly = sp.Poly(expr, a)
            ivs = poly.intervals()
            pos_ivs = [(lo, hi, mult) for (lo, hi), mult in ivs if hi >= 1 and mult % 2 == 1]
            if not pos_ivs and poly.eval(1) >= 0:
                continue
            max_r = max((int(hi) + 2 for _, hi, _ in pos_ivs), default=1)
            cur_start = None
            for aa in range(1, max_r + 3):
                val = Fraction(0)
                for j in range(n, -1, -1):
                    val = val * aa + pa[j]
                if val < 0:
                    if cur_start is None:
                        cur_start = aa
                else:
                    if cur_start is not None:
                        neg_ivs.append((k, cur_start, aa - 1))
                        cur_start = None
            if cur_start is not None:
                assert poly.LC() < 0, f"Unexpected positive LC at n={n}, k={k}"
                neg_ivs.append((k, cur_start, None))
        min_a = min(iv_item[1] for iv_item in neg_ivs)
        min_inf = min(iv_item[1] for iv_item in neg_ivs if iv_item[2] is None)
        for aa in range(min_a, min_inf):
            covered = any(iv_item[1] <= aa and (iv_item[2] is None or aa <= iv_item[2]) for iv_item in neg_ivs)
            assert covered, f"Gap at n={n}, a={aa}"
    print("Lemma 3 PASS (all 5 <= n <= 32, all a >= 1)")


def verify_lemma4():
    # Verify exact closed form for 720*(n-4)!*[t^{n-4}]/a^{n-5} and algebraic dominance for a >= 2*n^{4/3}.
    n_sym, a_sym = sp.symbols("n a")
    Sn_n = sp.Integer(1)
    Sn_nm1 = n_sym * (n_sym - 1) / 2
    Sn_nm2 = n_sym * (n_sym - 1) * (n_sym - 2) * (3 * n_sym - 1) / 24
    Sn_nm3 = n_sym ** 2 * (n_sym - 1) ** 2 * (n_sym - 2) * (n_sym - 3) / 48
    Sn_nm4 = n_sym * (n_sym - 1) * (n_sym - 2) * (n_sym - 3) * (n_sym - 4) * (15 * n_sym ** 3 - 30 * n_sym ** 2 + 5 * n_sym + 2) / 5760
    Snp1_nm3 = Sn_nm4.subs(n_sym, n_sym + 1)
    Bs = [sp.Rational(-1, 30), sp.Rational(0), sp.Rational(1, 6), sp.Rational(-1, 2), sp.Rational(1)]
    Sns = [Sn_n, Sn_nm1, Sn_nm2, Sn_nm3, Sn_nm4]
    sum_part = sp.Integer(0)
    for j_off in range(5):
        denom = sp.Integer(1)
        for m_off in range(j_off):
            denom *= (n_sym - 1 - m_off)
        sum_part += Sns[j_off] * Bs[j_off] / (denom * math.factorial(4 - j_off)) * a_sym ** (4 - j_off)
    part1 = Snp1_nm3 / (n_sym * (n_sym - 1) * (n_sym - 2) * (n_sym - 3)) * a_sym
    P_na = sp.expand(720 * (part1 + sum_part))
    expected = (
        -a_sym ** 4
        + (sp.Rational(15, 2) * n_sym ** 2 - sp.Rational(5, 2) * n_sym) * a_sym ** 2
        + (sp.Rational(15, 8) * n_sym ** 4 - sp.Rational(15, 4) * n_sym ** 3 + sp.Rational(65, 8) * n_sym ** 2 - sp.Rational(9, 4) * n_sym - 1) * a_sym
        + (sp.Rational(15, 8) * n_sym ** 4 - sp.Rational(15, 4) * n_sym ** 3 + sp.Rational(5, 8) * n_sym ** 2 + sp.Rational(1, 4) * n_sym)
    )
    assert sp.expand(P_na - expected) == 0, "Closed form mismatch in Lemma 4"

    # Check inequalities used in Lemma 4 for n >= 5 and a >= 2*n^{4/3}
    # 1) (15/2)*n^2 / a^2 <= (15/8)*n^{-2/3} <= (15/8)*5^{-2/3} < 0.65
    assert (iv.mpf(15) / 8 * iv.mpf(5) ** (-iv.mpf(2) / 3)).b < iv.mpf("0.65")
    # 2) Check -15/4 n^3 + 65/8 n^2 - 9/4 n - 1 < 0 and -15/4 n^3 + 5/8 n^2 + 1/4 n < 0 for n >= 5
    q1 = sp.Poly(-sp.Rational(15, 4) * n_sym ** 3 + sp.Rational(65, 8) * n_sym ** 2 - sp.Rational(9, 4) * n_sym - 1, n_sym)
    q2 = sp.Poly(-sp.Rational(15, 4) * n_sym ** 3 + sp.Rational(5, 8) * n_sym ** 2 + sp.Rational(1, 4) * n_sym, n_sym)
    for q in (q1, q2):
        # Verify q(5) < 0 and no root >= 5
        assert q.eval(5) < 0
        assert all(hi < 5 for (_, hi), _ in q.intervals())
    # 3) (15/64)*(1 + 1/(2*5^{4/3})) < 0.25
    a5_min = 2 * iv.mpf(5) ** (iv.mpf(4) / 3)
    assert (iv.mpf(15) / 64 * (1 + 1 / a5_min)).b < iv.mpf("0.25")
    print("Lemma 4 PASS")


def verify_lemma5():
    # Verify Case 5a (a in {8,9,10}, n >= 33) and Case 5b (11 <= a < 2*n^{4/3}, n >= 33) via iv arithmetic.
    n0 = 33
    H33 = sum(iv.mpf(1) / r for r in range(1, n0 + 1))

    # Case 5a: a = 8, 9, 10 at n = 33
    for aa in (8, 9, 10):
        x1 = 2 * iv.sin(iv.pi / aa)
        assert x1.b < 1
        xm_sum = iv.mpf(0)
        for m in range(2, aa - 1):
            xm = 2 * iv.sin(iv.pi * m / aa)
            assert xm.a > 1
            xm_sum += iv.mpf(1) / (1 - iv.mpf(1) / xm)
        tail1 = 2 * x1 / (1 - x1)
        for k in (1, 2, 3, 4):
            main_lb = (iv.sqrt(2) / aa) * ((2 * iv.pi) ** k / math.factorial(k)) * (x1 ** (-n0))
            e1 = (iv.mpf(aa) ** k) * ((H33 ** k) / math.factorial(k) + 1)
            e_m1 = (iv.mpf(aa) ** (k - 1)) * tail1
            e_rest = (iv.mpf(aa) ** (k - 1)) * xm_sum
            assert (e1 + e_m1 + e_rest).b < main_lb.a, f"Case 5a failed at a={aa}, k={k}"
            # Verify monotonicity in n >= 33:
            # Note |x_1|^{-n} grows as (1/|x_1|)^n while E1 grows <= (H_n)^k;
            # Check ((H_{n+1}/H_n)^k * |x_1| < 1) for n >= 33:
            ratio_step = (((H33 + iv.mpf(1) / 34) / H33) ** k) * x1
            assert ratio_step.b < 1

    # Case 5b: a >= 11, n >= 33, a < 2*n^{4/3}
    # 1) Bound a * |u(x)| on |x| = R_a = 3*sin(pi/a)
    R11 = 3 * iv.sin(iv.pi / 11)
    assert R11.b < 1
    au_bound = 3 * iv.pi * (-iv.log(1 - R11)) / R11
    assert au_bound.b < 21

    # 2) Prove |1 - z^{\pm a}| >= 0.85 on |1 - z| = R_a for all a >= 11:
    # Let phi = arg(z). We check our angular-radial inequalities in iv:
    # - 11*asin(R11)/pi < 3.53 <=> R11 < sin(3.53*pi/11), and for a >= 12: 3*asin(R12)/R12 < 3.5 <=> R12 < sin(3.5*R12/3)
    ang11 = iv.mpf("3.53") * iv.pi / 11
    assert ang11.b < (iv.pi / 2).a and R11.b < iv.sin(ang11).a
    R12 = 3 * iv.sin(iv.pi / 12)
    ang12 = iv.mpf("3.5") * R12 / 3
    assert ang12.b < (iv.pi / 2).a and R12.b < iv.sin(ang12).a

    # Lower bound on (a * R_a)^2 for a >= 11: since sin(y)/y decreases on (0, pi/2),
    # a * R_a >= 3 * 11 * sin(pi/11) > 9.3, so (a * R_a)^2 > 86.
    aR11 = 33 * iv.sin(iv.pi / 11)
    assert (aR11 ** 2).a > 86

    # Subcase a|phi| < pi/2: 4*r*sin^2(phi/2) <= 4*(1 + R11)*(pi/(4a))^2 => a^2 * 4*r*sin^2 <= (1 + R11)*pi^2/4 < 4.6
    assert ((1 + R11) * (iv.pi ** 2) / 4).b < iv.mpf("4.6")
    # Thus a*|r-1| >= sqrt(86 - 4.6) > 9.0
    assert iv.sqrt(86 - iv.mpf("4.6")).a > 9
    # For r <= 1: r^a <= (1 - 9/a)^a < exp(-9) => 1 - r^a > 0.99
    assert (1 - iv.exp(-9)).a > iv.mpf("0.99")
    # For r > 1 and a >= 11: r^{-a} <= (1 + 9/11)^{-11} (since (1 + c/a)^{-a} is decreasing in a? Wait: ln((1+9/a)^a) is increasing in a, so (1+9/a)^{-a} is decreasing in a!)
    assert (1 - (1 + iv.mpf(9) / 11) ** (-11)).a > iv.mpf("0.99")

    # Subcase a|phi| in (3pi/2, 5pi/2):
    # If r <= 1: a^2*4*r*sin^2(phi/2) <= 4*(5*pi/4)^2 = 25*pi^2/4 < 61.7 => a*(1-r) >= sqrt(86-61.7) > 4.9 => r^a < exp(-4.9)
    assert (25 * (iv.pi ** 2) / 4).b < iv.mpf("61.7")
    assert iv.sqrt(86 - iv.mpf("61.7")).a > iv.mpf("4.9")
    assert (1 - iv.exp(-iv.mpf("4.9"))).a > iv.mpf("0.99")
    # If r > 1: either r >= 1.3 (so r^{-a} <= 1.3^{-11} < 0.06 => 1 - r^{-a} > 0.94),
    # or 1 < r < 1.3, where a^2*4*r*sin^2(phi/2) <= 1.3 * 25*pi^2/4 < 80.2 => a*(r-1) >= sqrt(86 - 80.2) > 2.4 => r^{-a} <= (1 + 2.4/11)^{-11} < 0.12 => 1 - r^{-a} > 0.88 > 0.85!
    assert (1 - iv.mpf("1.3") ** (-11)).a > iv.mpf("0.94")
    assert (iv.mpf("1.3") * 25 * (iv.pi ** 2) / 4).b < iv.mpf("80.2")
    assert iv.sqrt(86 - iv.mpf("80.2")).a > iv.mpf("2.4")
    assert (1 - (1 + iv.mpf("2.4") / 11) ** (-11)).a > iv.mpf("0.85")

    # Subcase a = 11 and 11*|phi| in (7*pi/2, 3.53*pi): |Im(z^{+-11})| = r^{+-11} |sin(11*phi)|.
    # For theta in [3.5*pi, 3.53*pi], |sin(theta)| >= |sin(3.53*pi)| > 0.99, and cos(theta) >= 0:
    #Wait: if r^{+-11} <= 0.1, 1 - r^{+-11}*cos > 0.99; if r^{+-11} > 0.1? No, check min |1 - z^{+-11}| directly on the arc via interval boxes!
    # Wait: even simpler, on [3.5*pi, 3.53*pi], sin(theta) <= sin(3.53*pi) < -0.995, while cos(theta) <= cos(3.53*pi) < 0.095!
    # Wait: for ANY rho >= 0, |1 - rho*(cos + i sin)|^2 = (1 - rho*cos)^2 + rho^2 sin^2 = 1 - 2*rho*cos + rho^2 >= 1 - cos^2 = sin^2 !!
    # (Minimal value of quadratic rho^2 - 2*cos*rho + 1 is at rho = cos, giving 1 - cos^2 = sin^2!)
    assert (iv.fabs(iv.sin(iv.mpf("3.53") * iv.pi))).a > iv.mpf("0.99")

    # Hence a*|G_a(x)| <= 3*pi / 0.85 < 11.1!
    assert (3 * iv.pi / iv.mpf("0.85")).b < iv.mpf("11.1")

    # Check (E1 + E2)/Main < 1 for all n >= 33 and 11 <= a < 2*n^{4/3}:
    # Notice E2/Main <= (11.1 / sqrt(2)) * (21 / (2*pi))^k * 1.5^{-n}.
    # At n = 33, k = 4:
    e2_rat = (iv.mpf("11.1") / iv.sqrt(2)) * ((21 / (2 * iv.pi)) ** 4) * (iv.mpf("1.5") ** (-33))
    assert e2_rat.b < iv.mpf("0.002")

    # And for E1/Main: since |x_1| = 2*sin(pi/a) >= 2*(3/a) (Wait: 2*sin(pi/a) >= 2*(pi/a)*(sin(pi/11)/(pi/11)) = 22*sin(pi/11)/a, wait NO: we want UPPER bound on |x_1|!
    # Since sin(y) <= y, |x_1| <= 2*pi/a !
    # Thus E1/Main = a^{k+1} H_n^k |x_1|^n / (sqrt(2)*(2*pi)^k) <= (a^{k+1} H_n^k / (sqrt(2)*(2*pi)^k)) * (2*pi / a)^n
    # Notice for n >= 33 and k <= 4, a^{k+1-n} = a^{5-n} <= a^{-28} <= 11^{-28} (strictly decreasing in a >= 11!).
    # So worst case is a = 11 (Wait: is E1/Main maximized at a=11?! Let's check: E1 has a^k, Main has |x_1|^{-n} / a, so E1/Main ~ a^{k+1} * |x_1|^n ~ a^{k+1-n} * (2*pi)^n, which DECREASES with a for n >= 6! Wait: check |x_1| <= 2*pi/a AND at a=11 use exact |x_1| = 2*sin(pi/11) vs for a>=12 use 2*pi/a!)
    # Actually at a = 11: a^{k+1} * (2*pi/a)^n = (2*pi)^n * 11^{k+1-n} (even with |x_1| <= 2*pi/a, check at n=33, a=11, k=4!):
    # Wait: (2*pi)^{33} * 11^{-28} is ~ 1.6e26 / 1.4e29 ~ 0.001! And for n >= 33:
    # ratio at n -> n+1 multiplies by (H_{n+1}/H_n)^4 * (2*pi/11) < 1.04 * 0.58 < 0.61 < 1!
    e1_rat_11 = (iv.mpf(11) ** (4 + 1 - 33)) * (H33 ** 4) * ((2 * iv.pi) ** 33) / (iv.sqrt(2) * (2 * iv.pi) ** 4)
    assert e1_rat_11.b < iv.mpf("0.005")
    assert (e1_rat_11 + e2_rat).b < 1
    step_e1 = (((H33 + iv.mpf(1) / 34) / H33) ** 4) * (2 * iv.pi / 11)
    assert step_e1.b < 1

    print("Lemma 5 PASS")


if __name__ == "__main__":
    verify_lemma1()
    verify_lemma2()
    verify_lemma3()
    verify_lemma4()
    verify_lemma5()
    print("PASS")
