"""Independent exact-arithmetic verifier for targets/jensen-2605.27941-ques4."""

from fractions import Fraction
from math import gcd
import itertools


def norm_circle(x: Fraction) -> Fraction:
    """Exact distance ||x|| = min_{m in Z} |x - m| in [0, 1/2]."""
    frac = x - (x.numerator // x.denominator)
    if frac > Fraction(1, 2):
        return 1 - frac
    return frac


def exact_safe_intervals_one_runner(s: int, d: Fraction) -> list[tuple[Fraction, Fraction]]:
    """Return exact sorted union of closed intervals in [0, 1] where ||s * t|| >= d."""
    if d <= 0:
        return [(Fraction(0), Fraction(1))]
    if d > Fraction(1, 2):
        return []
    out: list[tuple[Fraction, Fraction]] = []
    for k in range(s):
        a = Fraction(k, s) + d / s
        b = Fraction(k + 1, s) - d / s
        if a <= b:
            out.append((a, b))
    return out


def intersect_interval_lists(
    l1: list[tuple[Fraction, Fraction]],
    l2: list[tuple[Fraction, Fraction]],
) -> list[tuple[Fraction, Fraction]]:
    res: list[tuple[Fraction, Fraction]] = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        a = max(l1[i][0], l2[j][0])
        b = min(l1[i][1], l2[j][1])
        if a <= b:
            res.append((a, b))
        if l1[i][1] < l2[j][1]:
            i += 1
        else:
            j += 1
    return res


def exact_safe_measure_S123(
    s1: int, s2: int, s3: int, x: Fraction, y: Fraction
) -> Fraction:
    """Exact Lebesgue measure on [0, 1] of {t : ||s1 t|| >= x, ||s2 t|| >= x, ||s3 t|| >= y}."""
    iv1 = exact_safe_intervals_one_runner(s1, x)
    iv2 = exact_safe_intervals_one_runner(s2, x)
    iv3 = exact_safe_intervals_one_runner(s3, y)
    iv = intersect_interval_lists(intersect_interval_lists(iv1, iv2), iv3)
    return sum((b - a for a, b in iv), Fraction(0))


def check_tuple_satisfiable(speeds: tuple[int, ...], d: tuple[Fraction, ...]) -> bool:
    """Exact feasibility of exists t in [0, 1] with ||s_i t|| >= d_i for all i."""
    cur = [(Fraction(0), Fraction(1))]
    for s_i, d_i in zip(speeds, d):
        cur = intersect_interval_lists(cur, exact_safe_intervals_one_runner(s_i, d_i))
        if not cur:
            return False
    return True


def verify_section1_k1_k2() -> None:
    """Check Section 1: k=1 via (1) and k=2 via {(1,2), (2,1)} on exact rational grid."""
    # k = 1: t = 1/(2 s1) gives ||s1 t|| = 1/2 >= d1 for all d1 <= 1/2
    for s1 in range(1, 20):
        t = Fraction(1, 2 * s1)
        assert norm_circle(s1 * t) == Fraction(1, 2)

    # k = 2: compare exact satisfiability of {(1,2), (2,1)} against 2*d1 + d2 <= 1 and d1 + 2*d2 <= 1
    # Also test additional coprime pairs (s1, s2) up to 9 on feasible points (verifying Theorem A boundary consistency)
    grid = [Fraction(num, 12) for num in range(1, 7)]  # 1/12 .. 6/12 = 1/2
    for d1 in grid:
        for d2 in grid:
            in_u_s2 = check_tuple_satisfiable((1, 2), (d1, d2)) and check_tuple_satisfiable((2, 1), (d1, d2))
            in_poly = (2 * d1 + d2 <= 1) and (d1 + 2 * d2 <= 1)
            assert in_u_s2 == in_poly, f"k=2 mismatch at {(d1, d2)}: {in_u_s2} vs {in_poly}"
            if in_poly:
                for s1 in range(1, 8):
                    for s2 in range(1, 8):
                        if s1 != s2:
                            assert check_tuple_satisfiable((s1, s2), (d1, d2))
    print("Section 1 (k=1 and k=2 exact grid + small speed pairs): PASS")


def verify_lemma0_piecewise_affine() -> None:
    """Directly verify Lemma 0 (breakpoints, affinity on I_{s,r}, C_{s,r} convexity, U(S) equality)."""
    # Test finite speed family in k=3: S = {(1, 2, 3), (2, 3, 5)}
    S = [(1, 2, 3), (2, 3, 5)]
    breakpoints_by_s: dict[tuple[int, ...], list[Fraction]] = {}
    affine_pieces: dict[tuple[int, ...], list[list[tuple[int, int]]]] = {}

    for s in S:
        pts = sorted({Fraction(j, 2 * s_i) for s_i in s for j in range(2 * s_i + 1)})
        assert pts[0] == 0 and pts[-1] == 1
        breakpoints_by_s[s] = pts
        pieces: list[list[tuple[int, int]]] = []
        for r in range(1, len(pts)):
            a, b = pts[r - 1], pts[r]
            mid = (a + b) / 2
            # Verify ||s_i t|| is affine on [a, b]: check endpoint & midpoint linearity
            coeffs_r: list[tuple[int, int]] = []
            for s_i in s:
                j_floor = (2 * s_i * mid).numerator // (2 * s_i * mid).denominator
                if j_floor % 2 == 0:
                    m = j_floor // 2
                    slope, intercept = s_i, -m
                else:
                    m = (j_floor - 1) // 2
                    slope, intercept = -s_i, m + 1
                for t in (a, mid, b, (2 * a + b) / 3):
                    assert norm_circle(s_i * t) == slope * t + intercept
                coeffs_r.append((slope, intercept))
            pieces.append(coeffs_r)
        affine_pieces[s] = pieces

    # Verify U(S) matches union over phi of intersections of C_{s, phi(s)} on exact rational test points,
    # and check convexity witness inside single C_{s, r}
    test_pts = [
        (Fraction(1, 10), Fraction(1, 8), Fraction(1, 7)),
        (Fraction(1, 5), Fraction(1, 6), Fraction(1, 5)),
        (Fraction(1, 3), Fraction(1, 4), Fraction(1, 5)),
        (Fraction(1, 4), Fraction(1, 3), Fraction(1, 3)),
        (Fraction(2, 5), Fraction(2, 5), Fraction(1, 5)),
    ]
    for d in test_pts:
        in_u = all(check_tuple_satisfiable(s, d) for s in S)
        # Check piecewise union formula
        valid_regions_per_s = []
        for s in S:
            pts = breakpoints_by_s[s]
            good_rs = []
            for r in range(len(pts) - 1):
                # Exists t in [pts[r], pts[r+1]] with slope*t + intercept >= d_i for all i
                lo, hi = pts[r], pts[r + 1]
                for (slope, intercept), d_i in zip(affine_pieces[s][r], d):
                    if slope > 0:
                        lo = max(lo, (d_i - intercept) / slope)
                    else:
                        hi = min(hi, (d_i - intercept) / slope)
                if lo <= hi:
                    good_rs.append((r, lo))
            valid_regions_per_s.append(good_rs)
        in_union = all(len(g) > 0 for g in valid_regions_per_s)
        assert in_u == in_union

    # Check convex combination closure in a concrete C_{s, r} for s=(1, 2, 3)
    s0 = (1, 2, 3)
    pts0 = breakpoints_by_s[s0]
    for r in range(len(pts0) - 1):
        t_a = (3 * pts0[r] + pts0[r + 1]) / 4
        t_b = (pts0[r] + 3 * pts0[r + 1]) / 4
        d_a = tuple(min(Fraction(1, 2), norm_circle(si * t_a)) for si in s0)
        d_b = tuple(min(Fraction(1, 2), norm_circle(si * t_b)) for si in s0)
        if all(x > 0 for x in d_a) and all(x > 0 for x in d_b):
            lam = Fraction(2, 5)
            d_mix = tuple((1 - lam) * x + lam * y for x, y in zip(d_a, d_b))
            t_mix = (1 - lam) * t_a + lam * t_b
            assert pts0[r] <= t_mix <= pts0[r + 1]
            for si, dm in zip(s0, d_mix):
                assert norm_circle(si * t_mix) >= dm
    print("Lemma 0 (piecewise-affine breakpoints, affinity, U(S) distribution, convexity): PASS")


def params(n: int) -> tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction]:
    dn = Fraction(1, 2 * n + 3)
    deltan = Fraction(1, 20 * (2 * n + 3) ** 2)
    xn = dn - deltan
    etan = Fraction(2 * n + 5, 4 * (n + 1) * (2 * n + 3))
    yn = Fraction(1, 2) - etan
    mun = Fraction(3, 22) * (deltan ** 2) * etan
    return dn, deltan, xn, etan, yn, mun


def verify_section3_lemmas1_2() -> None:
    # Monotonicity and range checks for n = 5..79
    for n in range(5, 80):
        dn, deltan, xn, etan, yn, mun = params(n)
        assert 0 < xn < dn <= Fraction(1, 13)
        assert 0 < mun < etan < Fraction(1, 12)
        assert Fraction(5, 12) < yn < Fraction(1, 2)
        assert etan == Fraction(1, 2 * (2 * n + 3)) + Fraction(3, 4 * (n + 1) * (2 * n + 3))
        _, _, xn1, etan1, yn1, _ = params(n + 1)
        assert xn > xn1 and etan > etan1 and yn < yn1
        assert xn - xn1 == Fraction(2, (2 * n + 3) * (2 * n + 5)) * (
            1 - Fraction(4 * n + 8, 20 * (2 * n + 3) * (2 * n + 5))
        )

    # Lemma 2 for 5 <= m < n <= 35
    for m in range(5, 35):
        _, _, xm, _, ym, _ = params(m)
        for n in range(m + 1, 36):
            dn, deltan, xn, _, yn, _ = params(n)
            x_star = dn + deltan
            assert x_star == xn + 2 * deltan
            lam = (x_star - xn) / (xm - xn)
            assert 0 < lam < 1
            assert Fraction(1, 2 * n + 3) < x_star < Fraction(1, 2 * n - 1)
            assert xm - xn > Fraction(129, 130) * Fraction(2 * (n - m), (2 * m + 3) * (2 * n + 3))
            ratio_l2 = Fraction(2 * m + 2 * n + 5, (m + 1) * (n + 1))
            assert ratio_l2 == Fraction(2, n + 1) + Fraction(2, m + 1) + Fraction(1, (m + 1) * (n + 1))
            assert ratio_l2 <= Fraction(9, 14) < Fraction(2, 3)
            assert Fraction(3, 4) * ratio_l2 <= Fraction(27, 56) < Fraction(1, 2)
            assert yn - ym < Fraction(3, 2) * Fraction(n - m, (2 * m + 3) * (2 * n + 3))
            assert (yn - ym) / (xm - xn) < Fraction(3, 4) * Fraction(130, 129) < 1
            y_star = yn - lam * (yn - ym)
            assert y_star > yn - 2 * deltan
            assert y_star > Fraction(n - x_star, 2 * n + 1)
            num = 5 * (2 * n + 5) * (2 * n + 3) - 2 * (n + 1) * (2 * n + 1)
            assert num == 16 * n * n + 74 * n + 73 and num > 0
            # Direct Lemma 1 failure check for speeds (2, 2n+1, 1) on small cases
            if n <= 12:
                assert not check_tuple_satisfiable((2, 2 * n + 1, 1), (x_star, x_star, y_star))

    # Explicit midpoint check (m=5, n=7): (Q_5 + Q_7)/2 fails MLRC for (2, 13, 1)
    _, _, x5, _, y5, _ = params(5)
    _, _, x7, _, y7, _ = params(7)
    xm_mid = (x5 + x7) / 2
    ym_mid = (y5 + y7) / 2
    assert exact_safe_measure_S123(2, 13, 1, xm_mid, ym_mid) == 0
    print("Section 3.1 & Lemmas 1-2 (including midpoint m=5,n=7): PASS")


def verify_lemma3b_and_3c() -> None:
    # 0. Lemma 3a exact bad-measure check on boundary intervals (including s=1, x=2/5, J=[1/20, 19/20])
    for s_test, x_test, a_test, b_test in [
        (1, Fraction(2, 5), Fraction(1, 20), Fraction(19, 20)),
        (3, Fraction(1, 13), Fraction(1, 10), Fraction(7, 10)),
        (7, Fraction(1, 15), Fraction(1, 8), Fraction(5, 6)),
    ]:
        bad_iv = intersect_interval_lists(
            [(a_test, b_test)],
            [(Fraction(0), Fraction(1))] if False else (
                [(Fraction(0), x_test / s_test)]
                + [(Fraction(m, s_test) - x_test / s_test, Fraction(m, s_test) + x_test / s_test) for m in range(1, s_test)]
                + [(1 - x_test / s_test, Fraction(1))]
            ),
        )
        bad_meas = sum((b - a for a, b in bad_iv), Fraction(0))
        L_test = b_test - a_test
        assert bad_meas <= 2 * x_test * L_test + Fraction(2 * x_test, s_test)

    # 1. Lemma 3b exhaustive exact rational check
    for n in range(5, 12):
        dn = Fraction(1, 2 * n + 3)
        for s3 in range(1, 25):
            for s in range(1, 50):
                if s % (2 * s3) == 0:
                    continue
                q = (2 * s3) // gcd(s, 2 * s3)
                assert q >= 2
                good_unshifted = 0
                for k in range(s3):
                    tk = Fraction(2 * k + 1, 2 * s3)
                    if norm_circle(s * tk) >= dn:
                        good_unshifted += 1
                assert 3 * good_unshifted >= 2 * s3
                if q >= 3:
                    for denom_th in (7, 13):
                        for num_th in range(denom_th):
                            theta = Fraction(num_th, denom_th)
                            good_shifted = 0
                            for k in range(s3):
                                tk = Fraction(2 * k + 1, 2 * s3)
                                if norm_circle(s * tk + theta) >= dn:
                                    good_shifted += 1
                            assert 2 * good_shifted >= s3

    # 2. Lemma 3c algebraic inequalities for n = 5..80
    for n in range(5, 81):
        dn, deltan, xn, etan, _, mun = params(n)
        wn = deltan * etan
        Wn = wn / 2
        Mn = 4 / wn
        assert Fraction(5, 2) * xn < Fraction(1, 4)
        assert (1 - 5 * xn) * 2 * etan > etan > mun
        assert etan - dn / 2 == Fraction(3, 2 * (2 * n + 2) * (2 * n + 3)) > wn
        assert Fraction(11, 26) * etan > wn
        assert Fraction(3, 4) * Wn == Fraction(3, 8) * deltan * etan > mun
        assert Fraction(1, 6) * (deltan ** 2) * etan > mun
        assert Fraction(1, 4) * (deltan ** 2) * etan > mun
        gamma_n = etan - dn / 2
        assert gamma_n > deltan / Mn
        gamma_pp = etan - Fraction(2 * n + 5, 2 * (2 * n + 3) ** 2)
        assert gamma_pp == Fraction(2 * n + 5, 2 * (2 * n + 2) * (2 * n + 3) ** 2) > 0
        assert deltan / Mn < gamma_pp
        assert Fraction(1, 2) * (deltan ** 2) * etan > mun
        # Regime C3b
        assert 2 + Fraction(2, 1 - Fraction(1, 13)) == Fraction(25, 6)
        assert 2 + Fraction(2, Fraction(1, 2) - Fraction(1, 13)) == Fraction(74, 11) < 7
        assert etan - Fraction(5, 12) * dn == Fraction(n + 10, 12 * (n + 1) * (2 * n + 3)) > mun
        assert etan - dn / 4 - 7 * dn * etan == Fraction(2 * n * n - 3 * n - 23, 4 * (n + 1) * (2 * n + 3) ** 2) >= Fraction(3, (n + 1) * (2 * n + 3) ** 2) > mun
        assert Fraction(25, 6) + Fraction(74, 11) == Fraction(719, 66) < 11
        assert etan * (1 - Fraction(11, 2 * n + 3)) >= Fraction(2, 13) * etan > mun

    # 3. Direct exact 1D safe-measure checks for n = 5 across all distinct triples in 1..14 + targeted regimes
    _, _, x5, _, y5, mu5 = params(5)
    for s1 in range(1, 15):
        for s2 in range(1, 15):
            if s2 == s1:
                continue
            for s3 in range(1, 15):
                if s3 == s1 or s3 == s2:
                    continue
                meas = exact_safe_measure_S123(s1, s2, s3, x5, y5)
                assert meas >= mu5, f"Triple {(s1, s2, s3)} failed: {meas} < {mu5}"

    targeted = [
        (2, 13, 1), (2, 26, 1), (2, 39, 1), (2, 52, 1), (2, 11, 1), (2, 14, 1),
        (4, 3, 1), (4, 5, 1), (4, 6, 1), (4, 15, 1), (4, 17, 1), (6, 5, 1), (6, 8, 1),
        (300, 301, 1),
        (3, 300000, 1),
    ]
    for s1, s2, s3 in targeted:
        meas = exact_safe_measure_S123(s1, s2, s3, x5, y5)
        assert meas >= mu5, f"Targeted triple {(s1, s2, s3)} failed: {meas} < {mu5}"

    # 4. Also verify k=4 extension Q_5^(4) with epsilon_{5,4} = mu_5 / 8 for small speed 4-tuples
    eps_5_4 = mu5 / 8
    for s4 in (4, 7, 11, 16):
        iv123 = intersect_interval_lists(
            intersect_interval_lists(exact_safe_intervals_one_runner(2, x5), exact_safe_intervals_one_runner(13, x5)),
            exact_safe_intervals_one_runner(1, y5),
        )
        iv1234 = intersect_interval_lists(iv123, exact_safe_intervals_one_runner(s4, eps_5_4))
        assert sum((b - a for a, b in iv1234), Fraction(0)) > 0

    print("Lemmas 3b, 3c, 4 (exhaustive 1..14 + targeted + k=4 union bound): PASS")


def main() -> None:
    verify_section1_k1_k2()
    verify_lemma0_piecewise_affine()
    verify_section3_lemmas1_2()
    verify_lemma3b_and_3c()
    print("PASS")


if __name__ == "__main__":
    main()
