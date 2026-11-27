from fractions import Fraction
import math


def mu_n_params(n: int):
    dn = Fraction(1, 2 * n + 3)
    delta = Fraction(1, 20 * (2 * n + 3) ** 2)
    xn = dn - delta
    eta = Fraction(2 * n + 5, 4 * (n + 1) * (2 * n + 3))
    yn = Fraction(1, 2) - eta
    mun = Fraction(3, 22) * delta ** 2 * eta
    return dn, delta, xn, eta, yn, mun


def norm_dist(x: Fraction) -> Fraction:
    r = x % 1
    return min(r, 1 - r)


def safe_intervals(s: int, d: Fraction):
    return [(Fraction(k, s) + d * Fraction(1, s), Fraction(k + 1, s) - d * Fraction(1, s)) for k in range(s)]


def intersect_intervals(a, b):
    res = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        l = max(a[i][0], b[j][0])
        r = min(a[i][1], b[j][1])
        if l < r:
            res.append((l, r))
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return res


def ok_for_speed_triple(d1: Fraction, d2: Fraction, d3: Fraction, s1: int, s2: int, s3: int) -> bool:
    for si, di in ((s1, d1), (s2, d2), (s3, d3)):
        for k in range(si):
            for t in (Fraction(k, si) + di * Fraction(1, si), Fraction(k + 1, si) - di * Fraction(1, si)):
                if norm_dist(s1 * t) >= d1 and norm_dist(s2 * t) >= d2 and norm_dist(s3 * t) >= d3:
                    return True
    return False


def verify_all():
    # 1. Verify all exact algebraic inequalities in Lemmas 1, 2, 3a-3c for n = 5..30
    for n in range(5, 31):
        dn, delta, xn, eta, yn, mun = mu_n_params(n)
        assert Fraction(0) < xn < dn <= Fraction(1, 13)
        assert Fraction(0) < mun < eta < Fraction(1, 12)
        assert yn > Fraction(5, 12)

        # Monotonicity of x_n and eta_n
        _, _, xn1, eta1, yn1, _ = mu_n_params(n + 1)
        assert xn > xn1
        assert eta > eta1
        assert yn < yn1

        # Lemma 1 threshold check: (n - x) over (2n + 1) > 1 over 3 for x < 1 over (2n - 1)
        assert Fraction(n - Fraction(1, 2 * n - 1), 2 * n + 1) > Fraction(1, 3)

        # Regime A: 5 over 2 * x_n < 1 over 4
        assert Fraction(5, 2) * xn < Fraction(1, 4)

        # Regime B: margins for m1 = 1 and m1 >= 2
        wn = delta * eta
        Wn = wn * Fraction(1, 2)
        Mn = 4 * Fraction(1, 1) * Fraction(wn.denominator, wn.numerator)
        gamma = eta - dn * Fraction(1, 2)
        assert gamma == Fraction(3, 2 * (2 * n + 2) * (2 * n + 3)) > 0
        assert eta - xn * Fraction(1, 2) > gamma > wn
        assert (1 - 2 * xn) * eta * Fraction(1, 2) > wn
        assert Fraction(3, 4) * Wn > mun

        # Subcase C1, C2, C3a margins
        gamma2 = eta - Fraction(2 * n + 5, 2 * (2 * n + 3) ** 2)
        assert gamma2 == Fraction(2 * n + 5, 2 * (2 * n + 2) * (2 * n + 3) ** 2) > 0
        step = delta * Fraction(Mn.denominator, Mn.numerator)
        assert step < eta and step < gamma and step < gamma2
        assert mun <= Fraction(1, 6) * delta ** 2 * eta

        # Subcase C3b margins (exact quadratic bounds)
        assert eta - Fraction(5, 12) * xn > Fraction(n + 10, 12 * (n + 1) * (2 * n + 3)) > mun
        even_large = 2 * xn * eta + 2 * xn * eta * Fraction(1, 1) * Fraction((1 - xn).denominator, (1 - xn).numerator)
        odd_large = 2 * xn * eta + 2 * xn * eta * Fraction(1, 1) * Fraction((Fraction(1, 2) - xn).denominator, (Fraction(1, 2) - xn).numerator)
        assert even_large < Fraction(25, 6) * xn * eta
        assert odd_large < 7 * xn * eta
        assert eta - xn * Fraction(1, 4) - 7 * xn * eta > Fraction(3, (n + 1) * (2 * n + 3) ** 2) > mun
        assert eta - (even_large + odd_large) > eta * (1 - 11 * dn) > mun

    # 2. Verify Lemma 2 (segment obstruction) exactly for all 5 <= m < n <= 20
    for n in range(6, 21):
        dn, delta, xn, eta, yn, _ = mu_n_params(n)
        x_star = dn + delta
        assert dn < x_star < Fraction(1, 2 * n - 1)
        for m in range(5, n):
            _, _, xm, _, ym, _ = mu_n_params(m)
            assert xn < x_star < xm
            lam = (x_star - xn) * Fraction((xm - xn).denominator, (xm - xn).numerator)
            assert Fraction(0) < lam < Fraction(1)
            y_star = yn - lam * (yn - ym)
            fn_xstar = (n - x_star) * Fraction(1, 2 * n + 1)
            assert y_star > fn_xstar
            assert not ok_for_speed_triple(x_star, x_star, y_star, 2, 2 * n + 1, 1)

    # 3. Verify explicit literal midpoint counterexample (Q_5 + Q_7) over 2 fails (2, 13, 1)
    _, _, x5, _, y5, _ = mu_n_params(5)
    _, _, x7, _, y7, _ = mu_n_params(7)
    x_mid = (x5 + x7) * Fraction(1, 2)
    y_mid = (y5 + y7) * Fraction(1, 2)
    assert x_mid == Fraction(66071, 976820)
    assert y_mid == Fraction(6485, 14144)
    assert Fraction(1, 15) < x_mid < Fraction(1, 11)
    assert y_mid > (6 - x_mid) * Fraction(1, 13)
    assert not ok_for_speed_triple(x_mid, x_mid, y_mid, 2, 13, 1)

    # 4. Exact rational measure check for n = 5, 6 on small speed triples
    for n in (5, 6):
        _, _, xn, _, yn, mun = mu_n_params(n)
        for s3 in range(1, 13):
            ivs3 = safe_intervals(s3, yn)
            for s1 in range(1, 15):
                if s1 == s3:
                    continue
                ivs1 = safe_intervals(s1, xn)
                ivs13 = intersect_intervals(ivs1, ivs3)
                for s2 in range(s1 + 1, 15):
                    if s2 == s3 or math.gcd(s1, math.gcd(s2, s3)) != 1:
                        continue
                    ivs123 = intersect_intervals(ivs13, safe_intervals(s2, xn))
                    meas = sum((r - l for l, r in ivs123), Fraction(0))
                    assert meas >= mun, f"n={n} triple={(s1,s2,s3)} meas={meas} < mun={mun}"

    print("PASS")


if __name__ == "__main__":
    verify_all()
