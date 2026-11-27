"""Independent exact-arithmetic verifier for targets/oeis-A178072/ (PROOF.md).

Zero floating-point operations or literals anywhere in this script.
Checks:
1. Exact live OEIS DATA match for A178072 (rev. 35, 34 terms) against both
   Somos's algebraic equation and the double binomial sum formula.
2. Exact symbolic verification in SymPy (QQ[x], QQ[n]) of all ODEs,
   polynomial coefficients A_1, A_0, R_1, P_2, P_1, P_0, R_2, and c_0..c_7(n).
3. Direct verification of Mathar's 7-term recurrence for n = 6..60.
"""

from fractions import Fraction
from math import comb
import sympy as sp

A178072_LIVE = [
    1, 0, -1, -1, -1, -1, 1, 8, 23, 45, 55, -14, -317, -1095, -2459, -3574,
    -681, 16124, 64605, 159483, 260869, 134374, -906919, -4228769,
    -11317061, -20327731, -15742753, 52640154, 293447719, 847451759,
    1648865921, 1636313816, -2986606297, -21074495982,
]


def poly_mul(a: list[int], b: list[int], deg: int) -> list[int]:
    out = [0] * (deg + 1)
    for i in range(min(len(a), deg + 1)):
        ai = a[i]
        if ai == 0:
            continue
        for j in range(min(len(b), deg + 1 - i)):
            out[i + j] += ai * b[j]
    return out


def poly_sq(a: list[int], deg: int) -> list[int]:
    return poly_mul(a, a, deg)


def main() -> None:
    N_MAX = 60

    print("[1/3] Generating A178072(0..60) from algebraic equation and checking OEIS data...")
    # (2x + x^3) A^2 - (1 + 2x + x^2) A + 1 = 0 =>
    # a(0) = 1, a(n) = -2*a(n-1) - a(n-2) + 2*[x^{n-1}] A^2 + [x^{n-3}] A^2
    a = [1]
    for n in range(1, N_MAX + 1):
        val = -2 * a[n - 1] - (a[n - 2] if n >= 2 else 0)
        # 2 * [x^{n-1}] A^2:
        for i in range(n):
            val += 2 * a[i] * a[n - 1 - i]
        # + [x^{n-3}] A^2:
        if n >= 3:
            for i in range(n - 2):
                val += a[i] * a[n - 3 - i]
        a.append(val)

    assert a[: len(A178072_LIVE)] == A178072_LIVE

    # Also verify exact algebraic equation up to x^60
    lhs = [0] * (N_MAX + 1)
    a2 = poly_sq(a, N_MAX)
    P_x = [0, 2, 0, 1]
    R_x = [1, 2, 1]
    Pa2 = poly_mul(P_x, a2, N_MAX)
    Ra = poly_mul(R_x, a, N_MAX)
    for n in range(N_MAX + 1):
        lhs[n] = Pa2[n] - Ra[n] + (1 if n == 0 else 0)
        assert lhs[n] == 0

    # Also check binomial formula in OEIS FORMULA for n = 0..25
    # Note: for n-k-i-1 < 0 and n-2k-i == 0, C(-1, 0) = 1
    def ext_comb(n_val: int, k_val: int) -> int:
        if k_val < 0:
            return 0
        if n_val >= 0:
            return comb(n_val, k_val)
        res = 1
        for j in range(k_val):
            res = res * (n_val - j) // (j + 1)
        return res

    for n in range(26):
        s_bin = Fraction(0)
        for k in range(n // 2 + 1):
            inner = 0
            for i in range(min(k, n - 2 * k) + 1):
                inner += (
                    comb(k, i)
                    * ext_comb(n - k - i - 1, n - 2 * k - i)
                    * (2 ** (n - 2 * k - i))
                    * ((-1) ** (k - i))
                )
            s_bin += Fraction(comb(n - k, k), n - 2 * k + 1) * inner
        assert s_bin == a[n], f"Binomial formula mismatch at n={n}"
    print(f"      Matched all {len(A178072_LIVE)} live terms, algebraic equation to x^60, and binomial sum (n<=25).")

    print("[2/3] Symbolically verifying Section 1 & Section 2 ODE derivations and polynomials...")
    x, n_sym = sp.symbols("x n")
    P = 2 * x + x**3
    R = (1 + x) ** 2
    Delta = sp.expand(R**2 - 4 * P)
    assert sp.expand(Delta - (1 - 4 * x + 6 * x**2 + x**4)) == 0

    A1 = sp.expand(Delta * P)
    A0 = sp.expand(Delta * sp.diff(P, x) - sp.Rational(1, 2) * sp.diff(Delta, x) * P)
    R1 = sp.expand(sp.Rational(1, 2) * Delta * sp.diff(R, x) - sp.Rational(1, 4) * sp.diff(Delta, x) * R)

    assert sp.expand(A1 - (2 * x - 8 * x**2 + 13 * x**3 - 4 * x**4 + 8 * x**5 + x**7)) == 0
    assert sp.expand(A0 - (2 - 4 * x + 3 * x**2 - 10 * x**3 + 10 * x**4 + x**6)) == 0
    assert sp.expand(R1 - (2 - 4 * x - 3 * x**2 + 2 * x**3 - x**4)) == 0

    # Verify formal series satisfies A1*A' + A0*A == R1 mod x^60
    da = [k * a[k] for k in range(1, N_MAX + 1)]
    A1_coeffs = [int(sp.Poly(A1, x).coeff_monomial(x**k)) for k in range(8)]
    A0_coeffs = [int(sp.Poly(A0, x).coeff_monomial(x**k)) for k in range(7)]
    R1_coeffs = [int(sp.Poly(R1, x).coeff_monomial(x**k)) for k in range(5)]
    ode1_lhs = [
        poly_mul(A1_coeffs, da, N_MAX - 1)[k] + poly_mul(A0_coeffs, a, N_MAX - 1)[k]
        for k in range(N_MAX)
    ]
    ode1_rhs = [R1_coeffs[k] if k < len(R1_coeffs) else 0 for k in range(N_MAX)]
    assert ode1_lhs == ode1_rhs

    # Apply L = x*(1+5x)*d/dx + 4x
    L_mult = x * (1 + 5 * x)
    P2 = sp.expand(L_mult * A1)
    P1 = sp.expand(L_mult * (sp.diff(A1, x) + A0) + 4 * x * A1)
    P0 = sp.expand(L_mult * sp.diff(A0, x) + 4 * x * A0)
    R2 = sp.expand(L_mult * sp.diff(R1, x) + 4 * x * R1)

    assert sp.expand(P2 - (2 * x**2 + 2 * x**3 - 27 * x**4 + 61 * x**5 - 12 * x**6 + 40 * x**7 + x**8 + 5 * x**9)) == 0
    assert sp.expand(P1 - (4 * x + 8 * x**2 - 90 * x**3 + 236 * x**4 - 96 * x**5 + 282 * x**6 + 8 * x**7 + 44 * x**8)) == 0
    assert sp.expand(P0 - (4 * x - 30 * x**2 + 12 * x**3 - 150 * x**4 + 240 * x**5 + 6 * x**6 + 34 * x**7)) == 0
    assert sp.expand(R2 - (4 * x - 42 * x**2 - 36 * x**3 + 34 * x**4 - 24 * x**5)) == 0

    P2_poly = sp.Poly(P2, x)
    P1_poly = sp.Poly(P1, x)
    P0_poly = sp.Poly(P0, x)
    expected_ck = [
        2 * n_sym * (n_sym + 1),
        2 * n_sym * (n_sym + 1),
        -3 * (3 * n_sym - 1) * (3 * n_sym - 4),
        61 * n_sym**2 - 191 * n_sym + 36,
        6 * (-2 * n_sym**2 + 2 * n_sym - 1),
        2 * (5 * n_sym - 1) * (4 * n_sym - 15),
        n_sym * (n_sym - 5),
        (5 * n_sym - 1) * (n_sym - 6),
    ]
    for k in range(8):
        p2k = P2_poly.coeff_monomial(x ** (k + 2))
        p1k = P1_poly.coeff_monomial(x ** (k + 1))
        p0k = P0_poly.coeff_monomial(x**k)
        ck = sp.expand(p2k * (n_sym - k) * (n_sym - k - 1) + p1k * (n_sym - k) + p0k)
        assert sp.expand(ck - expected_ck[k]) == 0, f"c_{k}(n) mismatch"
    print("      All symbolic ODEs and coefficient polynomials c_0..c_7 match identically.")

    print("[3/3] Checking Mathar's 7-term recurrence numerically for n = 6..60...")
    for n in range(6, N_MAX + 1):
        val = (
            2 * n * (n + 1) * a[n]
            + 2 * n * (n + 1) * a[n - 1]
            - 3 * (3 * n - 1) * (3 * n - 4) * a[n - 2]
            + (61 * n * n - 191 * n + 36) * a[n - 3]
            + 6 * (-2 * n * n + 2 * n - 1) * a[n - 4]
            + 2 * (5 * n - 1) * (4 * n - 15) * a[n - 5]
            + n * (n - 5) * a[n - 6]
            + (5 * n - 1) * (n - 6) * (a[n - 7] if n >= 7 else 0)
        )
        assert val == 0, f"Recurrence nonzero at n={n}: {val}"
    print("      Recurrence holds identically for all n = 6..60.")
    print("PASS")


if __name__ == "__main__":
    main()
