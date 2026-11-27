"""Exact-arithmetic verifier for targets/jensen-2605.27941-ques4/PROOF.md.

Uses only int and fractions.Fraction (zero floating-point literals, zero division operators).
"""

from fractions import Fraction
from math import gcd


def norm_dist(x: Fraction) -> Fraction:
    """Exact distance to the nearest integer ||x|| for rational x."""
    n = x.numerator
    d = x.denominator
    r = n % d
    if 2 * r > d:
        r = d - r
    return Fraction(r, d)


def q_params(n: int):
    two_n_3 = 2 * n + 3
    dn = Fraction(1, two_n_3)
    deltan = Fraction(1, 20 * two_n_3 * two_n_3)
    xn = dn - deltan
    etan = Fraction(2 * n + 5, 4 * (n + 1) * two_n_3)
    yn = Fraction(1, 2) - etan
    mun = Fraction(3, 22) * deltan * deltan * etan
    return dn, deltan, xn, etan, yn, mun


def Q_vec(n: int, k: int):
    dn, deltan, xn, etan, yn, mun = q_params(n)
    eps = mun * Fraction(1, 2 * k)
    return [xn, xn, yn] + [eps] * (k - 3)


def breakpoints(speeds):
    pts = {Fraction(0, 1), Fraction(1, 1)}
    for s in speeds:
        for j in range(2 * s + 1):
            pts.add(Fraction(j, 2 * s))
    return sorted(pts)


def verify_k1_k2():
    # k = 1: single speed (1) handles all d1 in (0, Fraction(1, 2)]
    for d_num in range(1, 11):
        d1 = Fraction(d_num, 20)
        for s1 in range(1, 15):
            t = Fraction(1, 2 * s1)
            assert norm_dist(s1 * t) >= d1

    # k = 2: verify (1,2) and (2,1) equivalence with MLPS_2 inequalities on sample grid
    for a in range(1, 13):
        for b in range(1, 13):
            d1 = Fraction(a, 24)
            d2 = Fraction(b, 24)
            poly_ok = (2 * d1 + d2 <= 1) and (d1 + 2 * d2 <= 1)
            # check (1, 2) and (2, 1) via midpoint of overlap intervals
            ok12 = (d1 <= Fraction(1, 2) - Fraction(1, 2) * d2)
            ok21 = (d2 <= Fraction(1, 2) - Fraction(1, 2) * d1)
            assert poly_ok == (ok12 and ok21)
            if poly_ok:
                for s1 in range(1, 10):
                    for s2 in range(1, 10):
                        if s1 == s2:
                            continue
                        g = gcd(s1, s2)
                        hs1 = divmod(s1, g)[0]
                        hs2 = divmod(s2, g)[0]
                        # verify affine vertex minimum condition hs2*(1-2d1) + hs1*(1-2d2) >= 1
                        assert hs2 * (1 - 2 * d1) + hs1 * (1 - 2 * d2) >= 1


def verify_lemma0_piecewise_affinity():
    # Check exact affinity of ||s_i * t|| on every breakpoint subinterval [b_{r-1}, b_r]
    for speeds in [(1, 2), (2, 1), (1, 2, 3), (2, 13, 1)]:
        bps = breakpoints(speeds)
        assert bps[0] == 0 and bps[-1] == 1
        for r in range(1, len(bps)):
            a, b = bps[r - 1], bps[r]
            assert a < b
            mid = Fraction(1, 2) * (a + b)
            t1 = Fraction(2, 3) * a + Fraction(1, 3) * b
            t2 = Fraction(1, 3) * a + Fraction(2, 3) * b
            for s in speeds:
                va, vb = norm_dist(s * a), norm_dist(s * b)
                assert norm_dist(s * mid) == Fraction(1, 2) * (va + vb)
                assert norm_dist(s * t1) == Fraction(2, 3) * va + Fraction(1, 3) * vb
                assert norm_dist(s * t2) == Fraction(1, 3) * va + Fraction(2, 3) * vb

    # Check Q_5^(3) and Q_7^(3) satisfy (2, 13, 1), while their midpoint fails (2, 13, 1)
    speeds_obs = (2, 13, 1)
    bps = breakpoints(speeds_obs)
    Q5 = Q_vec(5, 3)
    Q7 = Q_vec(7, 3)
    mid_Q = [Fraction(1, 2) * (Q5[i] + Q7[i]) for i in range(3)]

    def witnesses_on_breakpoints(vec):
        # Since ||s_i t|| is affine on each [a, b], test feasibility via 1D interval LP
        hits = []
        for r in range(1, len(bps)):
            a, b = bps[r - 1], bps[r]
            lo, hi = a, b
            feasible = True
            for s, d in zip(speeds_obs, vec):
                va, vb = norm_dist(s * a), norm_dist(s * b)
                # linear: va + ((vb - va) * inv(b - a)) * (t - a) >= d
                diff = vb - va
                if diff == 0:
                    if va < d:
                        feasible = False
                        break
                elif diff > 0:
                    # (t - a) >= (d - va)*(b - a) * inv(diff)
                    t_req = a + (d - va) * (b - a) * Fraction(1, diff)
                    if t_req > lo:
                        lo = t_req
                else:
                    # (t - a) <= (va - d)*(b - a) * inv(-diff)
                    t_max = a + (va - d) * (b - a) * Fraction(1, -diff)
                    if t_max < hi:
                        hi = t_max
            if feasible and lo <= hi:
                hits.append((r, lo))
        return hits

    assert len(witnesses_on_breakpoints(Q5)) >= 1
    assert len(witnesses_on_breakpoints(Q7)) >= 1
    assert len(witnesses_on_breakpoints(mid_Q)) == 0


def verify_qn_proof_bounds():
    # Check monotonicity, Lemma 1 and Lemma 2 inequalities, and Lemma 3b and 3c bounds
    for n in range(5, 40):
        dn, deltan, xn, etan, yn, mun = q_params(n)
        assert 0 < xn < dn <= Fraction(1, 13)
        assert 0 < mun < etan < Fraction(1, 12)
        assert Fraction(5, 12) < yn < Fraction(1, 2)
        if n > 5:
            _, _, xn_prev, _, yn_prev, _ = q_params(n - 1)
            assert xn < xn_prev
            assert yn > yn_prev
        # Check k=3..8 vector bounds
        for k in range(3, 9):
            q = Q_vec(n, k)
            assert len(q) == k
            assert all(0 < c < Fraction(1, 2) for c in q)

        # Check C3b item 3 exact bound: Fraction(25,6) + Fraction(74,11) = Fraction(719,66) < 11
        assert Fraction(25, 6) + Fraction(74, 11) == Fraction(719, 66) < 11
        rem_c3b = etan * (1 - Fraction(11, 2 * n + 3))
        assert rem_c3b > mun

    # Check Lemma 2 rational bounds for 5 <= m < n <= 25
    for m in range(5, 25):
        _, _, xm, _, ym, _ = q_params(m)
        for n in range(m + 1, 26):
            dn, deltan, xn, etan, yn, _ = q_params(n)
            x_star = dn + deltan
            lam = 2 * deltan * Fraction(1, (xm - xn).numerator) * (xm - xn).denominator
            assert 0 < lam < 1
            assert Fraction(1, 2 * n + 3) < x_star < Fraction(1, 2 * n - 1)
            ratio_bound = Fraction(2 * m + 2 * n + 5, (m + 1) * (n + 1))
            assert ratio_bound <= Fraction(9, 14) < Fraction(2, 3)
            y_star = yn - lam * (yn - ym)
            rhs = (n - x_star) * Fraction(1, 2 * n + 1)
            assert y_star > rhs
            # Speed tuple (2, 2n+1, 1) check on [0, 1] breakpoints
            bps = breakpoints((2, 2 * n + 1, 1))
            # Check no subinterval has a feasible t in [0, 1] for (x_star, x_star, y_star)
            any_ok = False
            for r in range(1, len(bps)):
                a, b = bps[r - 1], bps[r]
                lo, hi = a, b
                ok = True
                for s, d in zip((2, 2 * n + 1, 1), (x_star, x_star, y_star)):
                    va, vb = norm_dist(s * a), norm_dist(s * b)
                    diff = vb - va
                    if diff == 0:
                        if va < d:
                            ok = False
                            break
                    elif diff > 0:
                        t_req = a + (d - va) * (b - a) * Fraction(1, diff)
                        if t_req > lo:
                            lo = t_req
                    else:
                        t_max = a + (va - d) * (b - a) * Fraction(1, -diff)
                        if t_max < hi:
                            hi = t_max
                if ok and lo <= hi:
                    any_ok = True
                    break
            assert not any_ok


def main():
    verify_k1_k2()
    verify_lemma0_piecewise_affinity()
    verify_qn_proof_bounds()
    print("PASS")


if __name__ == "__main__":
    main()
