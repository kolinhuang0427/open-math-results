#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A028495 (Bill McEachen, Feb 11 2026).

Zero floating-point operations: pure Python int/Fraction + SymPy exact algebra.
"""

from __future__ import annotations

from fractions import Fraction
import sys
import sympy as sp

OEIS_DATA = [
    1, 1, 2, 3, 6, 10, 19, 33, 61, 108, 197, 352, 638, 1145, 2069, 3721,
    6714, 12087, 21794, 39254, 70755, 127469, 229725, 413908, 745889,
    1343980, 2421850, 4363921, 7863641, 14169633, 25532994, 46008619,
    82904974, 149389218, 269190547, 485064009, 874055885,
]


def P(r: Fraction) -> Fraction:
    return r**3 - r**2 - 2 * r + 1


def bisect_root(lo: Fraction, hi: Fraction, steps: int = 120) -> tuple[Fraction, Fraction]:
    assert P(lo) * P(hi) < 0
    s_lo = P(lo) > 0
    for _ in range(steps):
        mid = (lo + hi) / 2
        val = P(mid)
        if val == 0:
            return mid, mid
        if (val > 0) == s_lo:
            lo = mid
        else:
            hi = mid
    return lo, hi


def main() -> int:
    # 1. Exact g.f. / recurrence sequence matching OEIS DATA
    max_n = 120
    a = [0] * (max_n + 1)
    a[0], a[1], a[2] = 1, 1, 2
    for n in range(3, max_n + 1):
        a[n] = a[n - 1] + 2 * a[n - 2] - a[n - 3]
    assert a[: len(OEIS_DATA)] == OEIS_DATA, "Mismatch against OEIS A028495 DATA"

    # 2. Lemma 1: exact rational endpoint signs and root isolation
    assert P(Fraction(-3, 2)) == Fraction(-13, 8) and P(Fraction(-1)) == 1
    assert P(Fraction(0)) == 1 and P(Fraction(1, 2)) == Fraction(-1, 8)
    assert P(Fraction(3, 2)) == Fraction(-7, 8) and P(Fraction(2)) == 1

    # Symbolic cyclotomic verification: (zeta^7 + 1)/(zeta + 1) == zeta^3 * P(zeta + 1/zeta)
    z = sp.Symbol("z")
    r_expr = z + 1 / z
    poly_cyc = sp.simplify((z**7 + 1) / (z + 1) / z**3)
    poly_P = sp.simplify(r_expr**3 - r_expr**2 - 2 * r_expr + 1)
    assert sp.simplify(poly_cyc - poly_P) == 0

    # Exact partial fraction identity in Q[r]/(P(r)) via SymPy RootOf
    x, r = sp.symbols("x r")
    P_sym = sp.Poly(r**3 - r**2 - 2 * r + 1, r)
    roots = sp.real_roots(P_sym)
    assert len(roots) == 3  # ordered r_3 < r_2 < r_1
    r3_sym, r2_sym, r1_sym = roots
    P_deriv = sp.diff(r**3 - r**2 - 2 * r + 1, r)
    # Check sum_j c_j * r_j^n == a[n] for n = 0..12 via symmetric algebraic reduction
    # Using exact companion matrix trace / Newton sums for exact verification:
    # Let S_n = sum_{j=1}^3 ((r_j^2 - 1)/P'(r_j)) * r_j^n.
    # For any cubic, if P(r)=0 and P'(r)=3r^2-2r-2, in Q[r]/(P(r)) the inverse of P'(r) is explicit:
    _, _, g = sp.gcdex(sp.Poly(3 * r**2 - 2 * r - 2, r, domain="QQ"), sp.Poly(P_sym, domain="QQ"))
    assert g == 1
    Pinv = sp.invert(sp.Poly(3 * r**2 - 2 * r - 2, r, domain="QQ"), sp.Poly(P_sym, domain="QQ"))
    # Companion matrix trace: Tr(c_poly(C_mat) * C_mat^n) == a[n]
    C_mat = sp.Matrix([[0, 0, -1], [1, 0, 2], [0, 1, 1]])  # charpoly r^3 - r^2 - 2r + 1
    assert sp.factor(C_mat.charpoly(r).as_expr()) == r**3 - r**2 - 2 * r + 1
    c_poly = sp.rem(sp.Poly((r**2 - 1), r, domain="QQ") * Pinv, sp.Poly(P_sym, domain="QQ"))
    c_coeffs = c_poly.all_coeffs()
    c_mat = sp.zeros(3, 3)
    for coeff in c_coeffs:
        c_mat = c_mat * C_mat + sp.Rational(coeff) * sp.eye(3)
    cur = sp.eye(3)
    for n in range(30):
        tr_val = int((c_mat * cur).trace())
        assert tr_val == a[n], f"Partial fraction trace mismatch at n={n}: {tr_val} vs {a[n]}"
        cur = cur * C_mat

    # 3. Exact rational bisection of r_1, r_2, r_3 & explicit c_1, c_2, c_3 bounds
    r1_lo, r1_hi = bisect_root(Fraction(3, 2), Fraction(2))
    r2_lo, r2_hi = bisect_root(Fraction(0), Fraction(1, 2))
    r3_lo, r3_hi = bisect_root(Fraction(-3, 2), Fraction(-1))
    assert r1_lo > Fraction(18019, 10000) and r1_hi < Fraction(18020, 10000)
    # Check 2*cos(pi/7) = sqrt(2 + 2*cos(2*pi/7)): if r1 = 2*cos(pi/7), r1^2 = 2 + 2*cos(2*pi/7)
    # Verify (r1^2 - 2) satisfies the minimal polynomial of 2*cos(2*pi/7): y^3 + y^2 - 2y - 1 = 0!
    assert sp.rem(sp.Poly((r**2 - 2) ** 3 + (r**2 - 2) ** 2 - 2 * (r**2 - 2) - 1, r), P_sym) == 0

    # Check exact rational decay a(n)/a(n-1) bracketed tightly around r_1 for n=120
    ratio_120 = Fraction(a[120], a[119])
    assert abs(ratio_120 - r1_lo) < Fraction(1, 10**8)

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
