#!/usr/bin/env python3
"""Independent exact-arithmetic checker for targets/jensen-2605.27941-ques2."""

from fractions import Fraction
from math import ceil, gcd


def dist_Z(x: Fraction) -> Fraction:
    """Exact ||x|| = min_{m in Z} |x - m|."""
    q = x.numerator // x.denominator
    rem = x - q
    return rem if rem <= Fraction(1, 2) else Fraction(1) - rem


def params(n: int) -> tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction]:
    dn = Fraction(1, 2 * n + 3)
    deltan = Fraction(1, 20 * (2 * n + 3) ** 2)
    xn = dn - deltan
    etan = Fraction(2 * n + 5, 4 * (n + 1) * (2 * n + 3))
    yn = Fraction(1, 2) - etan
    mun = Fraction(3, 22) * (deltan ** 2) * etan
    return dn, deltan, xn, etan, yn, mun


def exact_safe_measure_S123(s1: int, s2: int, s3: int, x: Fraction, y: Fraction) -> Fraction:
    """Compute exact Lebesgue measure of {t in [0, 1) : ||s1 t|| >= x, ||s2 t|| >= x, ||s3 t|| >= y}."""
    def safe_intervals(s: int, thresh: Fraction) -> list[tuple[Fraction, Fraction]]:
        # ||s t|| >= thresh on [0, 1) is union over k=0..s-1 of [(k + thresh)/s, (k + 1 - thresh)/s]
        if thresh >= Fraction(1, 2):
            if thresh > Fraction(1, 2):
                return []
            # point intervals have measure 0
            return []
        return [(Fraction(k, s) + thresh / s, Fraction(k + 1, s) - thresh / s) for k in range(s)]

    def intersect_lists(A: list[tuple[Fraction, Fraction]], B: list[tuple[Fraction, Fraction]]) -> list[tuple[Fraction, Fraction]]:
        res = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo < hi:
                res.append((lo, hi))
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res

    I1 = safe_intervals(s1, x)
    I3 = safe_intervals(s3, y)
    I13 = intersect_lists(I1, I3)
    # Only generate s2-safe intervals overlapping [a, b] in I13 (avoids O(s2) blowup when s2 is large!)
    total = Fraction(0)
    for a, b in I13:
        k_lo = max(0, (s2 * a).numerator // (s2 * a).denominator - 1)
        k_hi = min(s2 - 1, (s2 * b).numerator // (s2 * b).denominator + 1)
        for k in range(k_lo, k_hi + 1):
            lo = max(a, Fraction(k, s2) + x / s2)
            hi = min(b, Fraction(k + 1, s2) - x / s2)
            if lo < hi:
                total += (hi - lo)
    return total


def verify_section1_and_lemmas1_2() -> None:
    for n in range(5, 80):
        dn, deltan, xn, etan, yn, mun = params(n)
        assert 0 < xn < dn <= Fraction(1, 13)
        assert 0 < mun < etan < Fraction(1, 12)
        assert Fraction(5, 12) < yn < Fraction(1, 2)
        for k in (3, 4, 10):
            eps = mun / (2 * k)
            assert 0 < eps < mun

        dn1, deltan1, xn1, etan1, yn1, _ = params(n + 1)
        assert xn - xn1 == Fraction(2, (2 * n + 3) * (2 * n + 5)) * (
            1 - Fraction(4 * n + 8, 20 * (2 * n + 3) * (2 * n + 5))
        )
        assert xn > xn1 and etan > etan1 and yn < yn1

    # Lemma 2 for 5 <= m < n <= 35
    for m in range(5, 35):
        _, _, xm, _, ym, _ = params(m)
        for n in range(m + 1, 36):
            dn, deltan, xn, etan, yn, _ = params(n)
            x_star = dn + deltan
            assert x_star == xn + 2 * deltan
            lam = (x_star - xn) / (xm - xn)
            assert 0 < lam < 1
            assert Fraction(1, 2 * n + 3) < x_star < Fraction(1, 2 * n - 1)
            assert xm - xn > Fraction(129, 130) * Fraction(2 * (n - m), (2 * m + 3) * (2 * n + 3))
            # Lemma 2 second-term bound via 1/(n+1) + 1/(m+1) + 1/((m+1)(n+1)) decomposition
            ratio_l2 = Fraction(2 * m + 2 * n + 5, (m + 1) * (n + 1))
            assert ratio_l2 == Fraction(2, n + 1) + Fraction(2, m + 1) + Fraction(1, (m + 1) * (n + 1))
            assert ratio_l2 <= Fraction(9, 14) < Fraction(2, 3)
            assert Fraction(3, 4) * ratio_l2 <= Fraction(27, 56) < Fraction(1, 2)
            assert yn - ym < Fraction(3, 2) * Fraction(n - m, (2 * m + 3) * (2 * n + 3))
            assert (yn - ym) / (xm - xn) < Fraction(3, 4) * Fraction(130, 129) < 1
            y_star = yn - lam * (yn - ym)
            assert y_star > yn - 2 * deltan
            assert y_star > Fraction(n - x_star, 2 * n + 1)
            # Check polynomial numerator on L77: 16n^2 + 74n + 73 > 0
            num = 5 * (2 * n + 5) * (2 * n + 3) - 2 * (n + 1) * (2 * n + 1)
            assert num == 16 * n * n + 74 * n + 73 and num > 0

    # Explicit midpoint check (m=5, n=7) from L80
    _, _, x5, _, y5, _ = params(5)
    _, _, x7, _, y7, _ = params(7)
    xm_mid = (x5 + x7) / 2
    ym_mid = (y5 + y7) / 2
    assert xm_mid == Fraction(66071, 976820)
    assert ym_mid == Fraction(6485, 14144)
    assert Fraction(1, 15) < xm_mid < Fraction(1, 11)
    assert ym_mid > (6 - xm_mid) / 13
    # Verify exact measure of S_{123}(2, 13, 1) at midpoint is ZERO!
    assert exact_safe_measure_S123(2, 13, 1, xm_mid, ym_mid) == 0
    print("Section 1 & Lemmas 1-2 (including midpoint m=5,n=7): PASS")


def verify_lemma3b_and_3c_ineqs() -> None:
    # 1. Lemma 3b exhaustive exact rational check
    for n in range(5, 12):
        dn = Fraction(1, 2 * n + 3)
        for s3 in range(1, 25):
            for s in range(1, 50):
                if s % (2 * s3) == 0:
                    continue
                q = (2 * s3) // gcd(s, 2 * s3)
                assert q >= 2
                # theta = 0
                bad0 = sum(1 for k in range(s3) if dist_Z(Fraction(s * (2 * k + 1), 2 * s3)) < dn)
                assert Fraction(bad0, s3) <= Fraction(1, 3)
                # arbitrary theta sample when q >= 3
                if q >= 3:
                    for num in range(0, 12):
                        theta = Fraction(num, 12 * q)
                        bad_th = sum(
                            1 for k in range(s3)
                            if dist_Z(Fraction(s * (2 * k + 1), 2 * s3) + theta) < dn
                        )
                        assert Fraction(bad_th, s3) <= Fraction(1, 2)

    # 2. Check all inequalities inside Lemma 3c for n = 5..80
    for n in range(5, 81):
        dn, deltan, xn, etan, yn, mun = params(n)
        wn = deltan * etan
        Wn = wn / 2
        Mn = 4 / wn
        # Regime A
        assert Fraction(5, 2) * xn < Fraction(1, 4)
        assert etan > mun
        # Regime B (m1 = 1 and m1 >= 2)
        assert etan - dn / 2 == Fraction(3, 2 * (2 * n + 2) * (2 * n + 3)) > wn
        assert min(etan / 2, Fraction(11, 26) * etan) > wn
        assert Fraction(3, 4) * Wn == Fraction(3, 8) * deltan * etan > mun
        # Regime C1, C2, C3a
        gamma_n = etan - dn / 2
        assert deltan / Mn < gamma_n
        gamma_pp = etan - Fraction(2 * n + 5, 2 * (2 * n + 3) ** 2)
        assert gamma_pp == Fraction(2 * n + 5, 2 * (2 * n + 2) * (2 * n + 3) ** 2) > 0
        assert deltan / Mn < gamma_pp
        assert Fraction(1, 6) * (deltan ** 2) * etan > mun
        # Regime C3b
        assert 2 + Fraction(2, 1 - Fraction(1, 13)) == Fraction(25, 6)
        assert 2 + Fraction(2, Fraction(1, 2) - Fraction(1, 13)) == Fraction(74, 11) < 7
        assert etan - Fraction(5, 12) * dn == Fraction(n + 10, 12 * (n + 1) * (2 * n + 3)) > mun
        assert etan - dn / 4 - 7 * dn * etan == Fraction(2 * n * n - 3 * n - 23, 4 * (n + 1) * (2 * n + 3) ** 2) >= Fraction(3, (n + 1) * (2 * n + 3) ** 2) > mun
        # Combined Regime C3b sum: (25/6) + (74/11) = 719/66 < 11
        assert Fraction(25, 6) + Fraction(74, 11) == Fraction(719, 66) < 11
        assert etan * (1 - Fraction(11, 2 * n + 3)) >= Fraction(2, 13) * etan > mun

    # 3. Direct exact 1D safe-measure checks for n = 5 across all distinct triples (s1, s2, s3) in 1..14
    # PLUS targeted Regime A/B/C1/C2/C3a/C3b triples!
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

    # Targeted triples hitting C3a (s1=2, s3=1, s2 mult of 13 even & odd) and C3b (s3=1, s1=4, s2=3..15)
    targeted = [
        (2, 13, 1), (2, 26, 1), (2, 39, 1), (2, 52, 1), (2, 11, 1), (2, 14, 1),
        (4, 3, 1), (4, 5, 1), (4, 6, 1), (4, 15, 1), (4, 17, 1), (6, 5, 1), (6, 8, 1),
        (300, 301, 1),  # Regime A at n=5 (2/eta_5 ~ 25)
        (3, 300000, 1),  # Regime B at n=5 (M_5 = 281216)
    ]
    for s1, s2, s3 in targeted:
        meas = exact_safe_measure_S123(s1, s2, s3, x5, y5)
        assert meas >= mu5, f"Targeted triple {(s1, s2, s3)} failed: {meas} < {mu5}"

    print("Lemmas 3b & 3c (exhaustive 1..14 + targeted A/B/C1/C2/C3a/C3b): PASS")


def main() -> None:
    verify_section1_and_lemmas1_2()
    verify_lemma3b_and_3c_ineqs()
    assert Fraction(25, 6) + Fraction(74, 11) == Fraction(719, 66) < 11
    print("PASS")


if __name__ == "__main__":
    main()
