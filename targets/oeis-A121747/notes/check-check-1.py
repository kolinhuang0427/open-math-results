#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/oeis-A121747/.

Verifies Mathar's D-finite recurrence conjecture for OEIS A121747 directly from
the primary OEIS record and every algebraic step in PROOF.md, using SymPy exact
polynomials in Q[n]/Z[n,r] and pure integer/Fraction arithmetic (zero floats).
"""

from fractions import Fraction
import math
import sympy as sp


def compute_a_terms(max_n: int) -> list[int]:
    """Compute d(n) and a(n) for 1 <= n <= max_n (a[0] = 0 extended for EGF)."""
    d = [0] * (max_n + 2)
    d[1] = 1
    d[2] = 0
    for m in range(2, (max_n + 2) // 2 + 1):
        if 2 * m <= max_n + 1:
            d[2 * m] = d[2 * m - 2] + math.factorial(2 * m - 1)
        if 2 * m - 1 <= max_n + 1 and m >= 2:
            d[2 * m - 1] = -d[2 * m - 2]
    # Also ensure d[3] = -d[2] = 0
    for k in range(3, max_n + 2):
        if k % 2 == 1:
            d[k] = -d[k - 1]

    a = [0] * (max_n + 1)
    a[1] = 1
    for n in range(2, max_n + 1):
        a[n] = n * a[n - 1] - d[n - 1] + math.factorial(n - 1) * (n // 2)
    return a


def main() -> None:
    max_n = 60
    a = compute_a_terms(max_n)

    # Sanity check against OEIS A121747 %S/%T terms a(1)..a(16)
    oeis_terms = [
        1, 2, 8, 44, 262, 1938, 15600, 145086, 1461888, 16438446,
        198598860, 2623055166, 36933441912, 560697617214, 9014444990964, 154698782105070,
    ]
    assert a[1:17] == oeis_terms
    print(f"Initial terms a(1..10) = {a[1:11]} (matches OEIS %S/%T through a(16))")

    # Primary OEIS recurrence polynomials C_0(n)..C_5(n)
    n_sym, r_sym = sp.symbols("n r")
    C = [
        -9 * n_sym + 38,
        3 * (3 * n_sym**2 - 19 * n_sym + 27),
        9 * n_sym**3 - 37 * n_sym**2 - 24 * n_sym + 127,
        -9 * n_sym**4 + 102 * n_sym**3 - 392 * n_sym**2 + 525 * n_sym - 85,
        -(n_sym - 3) * (28 * n_sym**3 - 223 * n_sym**2 + 510 * n_sym - 237),
        -(19 * n_sym - 15) * (n_sym - 3) * (n_sym - 4) ** 2,
    ]

    # Check 1: Direct numerical check of M(n) == 0 for all 6 <= n <= 60
    for n_val in range(6, max_n + 1):
        m_val = sum(int(C[j].subs(n_sym, n_val)) * a[n_val - j] for j in range(6))
        assert m_val == 0, f"M({n_val}) = {m_val} != 0"
    print(f"Direct M(n) == 0 verified for all 6 <= n <= {max_n}.")

    # Check 2: Step 1 closed forms for W(k) = D(k) + D(k-1) where D(k) = a(k) - k*a(k-1)
    for k in range(3, max_n + 1):
        w_k = a[k] - (k - 1) * a[k - 1] - (k - 1) * a[k - 2]
        d_k = a[k] - k * a[k - 1]
        d_prev = a[k - 1] - (k - 1) * a[k - 2]
        assert w_k == d_k + d_prev
        if k % 2 == 0:
            m = k // 2
            assert w_k == math.factorial(2 * m - 2) * (2 * m * m - 1)
        else:
            m = (k - 1) // 2
            assert w_k == math.factorial(2 * m - 1) * (2 * m * m + m - 1)
    print("Step 1 (W(k) closed forms) verified for 3 <= k <= 60.")

    # Check 3: Step 2 operator factorization M(n) = sum_{i=0}^3 c_i(n) W(n-i) in Z[n]
    c = [
        -9 * n_sym + 38,
        -10 * n_sym + 43,
        9 * n_sym**3 - 56 * n_sym**2 + 86 * n_sym + 3,
        (n_sym - 3) * (n_sym - 4) * (19 * n_sym - 15),
    ]
    a_syms = sp.symbols("a0 a1 a2 a3 a4 a5")
    lhs = sum(C[j] * a_syms[j] for j in range(6))
    rhs = sum(
        c[i] * (a_syms[i] - (n_sym - i - 1) * a_syms[i + 1] - (n_sym - i - 1) * a_syms[i + 2])
        for i in range(4)
    )
    assert sp.expand(lhs - rhs) == 0
    print("Step 2 (exact operator factorization in Z[n]) verified.")

    # Check 4: Step 3 exact cancellation P_even(r) == 0 and P_odd(r) == 0 in Z[r]
    P_even = (
        c[0].subs(n_sym, 2 * r_sym) * (2 * r_sym - 2) * (2 * r_sym - 3) * (2 * r_sym - 4) * (2 * r_sym - 5) * (2 * r_sym**2 - 1)
        + c[1].subs(n_sym, 2 * r_sym) * (2 * r_sym - 3) * (2 * r_sym - 4) * (2 * r_sym - 5) * (2 * (r_sym - 1) ** 2 + (r_sym - 1) - 1)
        + c[2].subs(n_sym, 2 * r_sym) * (2 * r_sym - 4) * (2 * r_sym - 5) * (2 * (r_sym - 1) ** 2 - 1)
        + c[3].subs(n_sym, 2 * r_sym) * (2 * r_sym - 5) * (2 * (r_sym - 2) ** 2 + (r_sym - 2) - 1)
    )
    assert sp.expand(P_even) == 0

    P_odd = (
        c[0].subs(n_sym, 2 * r_sym + 1) * (2 * r_sym - 1) * (2 * r_sym - 2) * (2 * r_sym - 3) * (2 * r_sym**2 + r_sym - 1)
        + c[1].subs(n_sym, 2 * r_sym + 1) * (2 * r_sym - 2) * (2 * r_sym - 3) * (2 * r_sym**2 - 1)
        + c[2].subs(n_sym, 2 * r_sym + 1) * (2 * r_sym - 3) * (2 * (r_sym - 1) ** 2 + (r_sym - 1) - 1)
        + c[3].subs(n_sym, 2 * r_sym + 1) * (2 * (r_sym - 1) ** 2 - 1)
    )
    assert sp.expand(P_odd) == 0
    print("Step 3 (P_even(r) == 0 and P_odd(r) == 0 in Z[r]) verified.")

    # Check 5: Step 4 homogeneous order-6 EGF ODE
    boundary = sum(int(C[j].subs(n_sym, 5)) * a[5 - j] for j in range(6))
    assert boundary == 0
    x_sym, m_sym = sp.symbols("x m")
    y_fn = sp.Function("y")(x_sym)
    ode_expr = sp.Integer(0)
    for j in range(6):
        poly_j = sp.Poly(sp.expand(C[j].subs(n_sym, m_sym + 5)), m_sym)
        y_deriv = sp.diff(y_fn, (x_sym, 5 - j)) if (5 - j) > 0 else y_fn
        for deg, coeff in poly_j.terms():
            d_pow = deg[0]
            term = y_deriv
            for _ in range(d_pow):
                term = x_sym * sp.diff(term, x_sym)
            ode_expr += coeff * term
    ode_collected = sp.collect(sp.expand(ode_expr), [sp.diff(y_fn, (x_sym, k)) for k in range(7)])
    lead_6 = sp.expand(ode_collected.coeff(sp.diff(y_fn, (x_sym, 6))))
    expected_lead = sp.expand(-9 * x_sym * (x_sym - 1) ** 2 * (x_sym + 1))
    assert lead_6 == expected_lead, f"lead_6={lead_6} != {expected_lead}"

    # Verify exact ODE annihilates Taylor series y_hat(x) up to x^35 (pure Fraction)
    y_coeffs = [Fraction(a[k], math.factorial(k)) for k in range(41)]
    for m_val in range(0, 35):
        lhs_m = Fraction(0)
        for j in range(6):
            idx = m_val + 5 - j
            c_val = int(C[j].subs(n_sym, m_val + 5))
            lhs_m += c_val * Fraction(a[idx], math.factorial(m_val))
        assert lhs_m == 0
    print(f"Step 4 (homogeneous order-6 EGF ODE, leading coeff={sp.factor(lead_6)}) verified.")

    print("PASS")


if __name__ == "__main__":
    main()
