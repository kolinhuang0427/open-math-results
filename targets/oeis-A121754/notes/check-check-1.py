#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/oeis-A121754/.

Verifies Mathar's D-finite recurrence conjecture for OEIS A121754 directly from
the primary OEIS record and every algebraic step in PROOF.md, using SymPy exact
polynomials in Q[n]/Z[n,r] and pure integer/Fraction arithmetic (zero floats).
"""

from fractions import Fraction
import math
import sympy as sp


def compute_a_terms(max_n: int) -> list[int]:
    """Compute a(n) for 0 <= n <= max_n (a[0] unused; offset 1, a(1)=0, a(2)=1)."""
    a = [0] * (max_n + 1)
    a[1] = 0
    if max_n >= 2:
        a[2] = 1
    for n in range(3, max_n + 1):
        # f(n) = n - 2 + (1/2)*(1 + (-1)^(n-1))*(n - 1)
        parity_term = (n - 1) if ((n - 1) % 2 == 0) else 0
        f_n = (n - 2) + parity_term
        a[n] = (2 * n - 3) * a[n - 1] - (n - 1) * (n - 3) * a[n - 2] + math.factorial(n - 2) * f_n
    return a


def main() -> None:
    max_n = 60
    a = compute_a_terms(max_n)

    # Sanity check against OEIS A121754 %S/%T terms a(1)..a(16)
    oeis_terms = [
        0, 1, 6, 31, 211, 1530, 13086, 120888, 1260792, 14140080,
        174692880, 2304970560, 32969263680, 500368821120, 8139251433600, 139686867532800,
    ]
    assert a[1:17] == oeis_terms
    print(f"Initial terms a(1..10) = {a[1:11]} (matches OEIS %S/%T through a(16))")

    # Primary OEIS recurrence polynomials C_0(n)..C_5(n)
    n_sym, r_sym = sp.symbols("n r")
    C = [
        16 * (n_sym + 1),
        -16 * n_sym**2 - 178 * n_sym + 531,
        -16 * n_sym**3 + 178 * n_sym**2 - 393 * n_sym - 510,
        16 * n_sym**4 + 98 * n_sym**3 - 1439 * n_sym**2 + 4222 * n_sym - 3623,
        -146 * n_sym**4 + 1479 * n_sym**3 - 4483 * n_sym**2 + 3054 * n_sym + 2841,
        (130 * n_sym - 311) * (n_sym - 6) * (n_sym - 4) ** 2,
    ]

    # Check 1: Direct numerical check of M(n) == 0 for all 6 <= n <= 60
    for n_val in range(6, max_n + 1):
        m_val = sum(int(C[j].subs(n_sym, n_val)) * a[n_val - j] for j in range(6))
        assert m_val == 0, f"M({n_val}) = {m_val} != 0"
    print(f"Direct M(n) == 0 verified for all 6 <= n <= {max_n}.")

    # Check 2: Step 1 identities for D(k) = a(k) - k*a(k-1) and S(k)
    for k in range(2, max_n + 1):
        d_k = a[k] - k * a[k - 1]
        if k >= 3:
            d_prev = a[k - 1] - (k - 1) * a[k - 2]
            f_k = (k - 2) + ((k - 1) if ((k - 1) % 2 == 0) else 0)
            assert d_k - (k - 3) * d_prev == math.factorial(k - 2) * f_k
            if k % 2 == 0:
                r = k // 2
                s_k = (r - 1) ** 2 * (4 * r - 1)
            else:
                r = (k - 1) // 2
                s_k = r**2 * (4 * r - 1)
            assert d_k == math.factorial(k - 3) * s_k
    # Symbolic induction check for S(2r) and S(2r+1)
    S_even_sym = (r_sym - 1) ** 2 * (4 * r_sym - 1)
    S_odd_sym = r_sym**2 * (4 * r_sym - 1)
    assert sp.expand(S_even_sym - S_odd_sym.subs(r_sym, r_sym - 1) - (2 * r_sym - 2) * (2 * r_sym - 2)) == 0
    assert sp.expand(S_odd_sym - S_even_sym - (2 * r_sym - 1) * (4 * r_sym - 1)) == 0
    print("Step 1 (D(k) reduction and S(k) closed forms) verified.")

    # Check 3: Step 2 operator factorization M(n) = sum_{i=0}^4 e_i(n) D(n-i) in Z[n]
    e = [
        16 * (n_sym + 1),
        -9 * (18 * n_sym - 59),
        -16 * n_sym**3 + 16 * n_sym**2 + 300 * n_sym - 1041,
        146 * n_sym**3 - 1171 * n_sym**2 + 2581 * n_sym - 1541,
        -(n_sym - 6) * (n_sym - 4) * (130 * n_sym - 311),
    ]
    a_syms = sp.symbols("a0 a1 a2 a3 a4 a5")  # a_j stands for a(n - j)
    lhs = sum(C[j] * a_syms[j] for j in range(6))
    rhs = sum(e[i] * (a_syms[i] - (n_sym - i) * a_syms[i + 1]) for i in range(5))
    diff_poly = sp.expand(lhs - rhs)
    assert diff_poly == 0, f"Step 2 factorization mismatch: {diff_poly}"
    print("Step 2 (exact operator factorization in Z[n]) verified.")

    # Check 4: Step 3 exact polynomial cancellation P_even(r) == 0 and P_odd(r) == 0
    assert e[4].subs(n_sym, 6) == 0
    # Even n = 2r
    S_even_args = [
        S_even_sym,
        S_odd_sym.subs(r_sym, r_sym - 1),
        S_even_sym.subs(r_sym, r_sym - 1),
        S_odd_sym.subs(r_sym, r_sym - 2),
        S_even_sym.subs(r_sym, r_sym - 2),
    ]
    P_even = (
        e[0].subs(n_sym, 2 * r_sym) * (2 * r_sym - 3) * (2 * r_sym - 4) * (2 * r_sym - 5) * (2 * r_sym - 6) * S_even_args[0]
        + e[1].subs(n_sym, 2 * r_sym) * (2 * r_sym - 4) * (2 * r_sym - 5) * (2 * r_sym - 6) * S_even_args[1]
        + e[2].subs(n_sym, 2 * r_sym) * (2 * r_sym - 5) * (2 * r_sym - 6) * S_even_args[2]
        + e[3].subs(n_sym, 2 * r_sym) * (2 * r_sym - 6) * S_even_args[3]
        + e[4].subs(n_sym, 2 * r_sym) * S_even_args[4]
    )
    assert sp.expand(P_even) == 0, f"P_even != 0: {sp.expand(P_even)}"

    # Odd n = 2r + 1
    S_odd_args = [
        S_odd_sym,
        S_even_sym,
        S_odd_sym.subs(r_sym, r_sym - 1),
        S_even_sym.subs(r_sym, r_sym - 1),
        S_odd_sym.subs(r_sym, r_sym - 2),
    ]
    P_odd = (
        e[0].subs(n_sym, 2 * r_sym + 1) * (2 * r_sym - 2) * (2 * r_sym - 3) * (2 * r_sym - 4) * (2 * r_sym - 5) * S_odd_args[0]
        + e[1].subs(n_sym, 2 * r_sym + 1) * (2 * r_sym - 3) * (2 * r_sym - 4) * (2 * r_sym - 5) * S_odd_args[1]
        + e[2].subs(n_sym, 2 * r_sym + 1) * (2 * r_sym - 4) * (2 * r_sym - 5) * S_odd_args[2]
        + e[3].subs(n_sym, 2 * r_sym + 1) * (2 * r_sym - 5) * S_odd_args[3]
        + e[4].subs(n_sym, 2 * r_sym + 1) * S_odd_args[4]
    )
    assert sp.expand(P_odd) == 0, f"P_odd != 0: {sp.expand(P_odd)}"
    print("Step 3 (P_even(r) == 0 and P_odd(r) == 0 in Z[r]) verified.")

    # Check 5: Verify D-finiteness of EGF y_hat(x) = sum_{n>=1} a(n) x^n / n!
    # Multiplying M(n) = 0 by x^(n-5)/(n-5)! and summing n>=6 yields a linear ODE with polynomial coefficients.
    # For each j in 0..5, write C_j(n) as a linear combination of falling factorials in m = n - 5:
    # Actually C_j(n) * a(n-j) * x^(n-5)/(n-5)! -> Express C_j(n) / ((n-5)(n-6)...(n-j+1))?
    # Note j=0..5: we need 1/(n-5)! * C_j(n) -> write C_j(n) * (n-j)!/(n-5)! * a(n-j) x^(n-5)/(n-j)!
    # Notice for j=5: coeff is C_5(n) * x^(n-5) * a(n-5)/(n-5)!, where C_5(n) = (130n-311)(n-6)(n-4)^2.
    # Wait: for j <= 4, (n-j)!/(n-5)! = prod_{t=j}^{4} (n-t), while for j=5, (n-5)!/(n-5)! = 1!
    # Better: shift index to x^(n)/(n)!? Wait: PROOF.md multiplies by x^(n-5)/(n-5)!:
    # Let m = n - j >= 1 (so n = m + j). For j=0..5:
    #   a(n-j)/(n-5)! * x^(n-5) = (m!/(m+j-5)!) * (a(m)/m!) * x^(m+j-5).
    # Wait: for j=5, m+j-5 = m, so m!/(m+0)! = 1; for j<=4, m!/(m+j-5)! is 1 / prod_{t=j-4}^0 (m-t)?? NO!
    # Wait: (n-5)! has FEWER factors than (n-j)! for j<=4, so (n-j)!/(n-5)! = (n-4)...(n-j) is a POLYNOMIAL in n?
    # Wait: (n-j)! / (n-5)! = (n-j)(n-j-1)...(n-4) only for j <= 4 (e.g. j=4 gives (n-4), j=0 gives n(n-1)(n-2)(n-3)(n-4))!
    # So C_j(n) * (n-j)! / (n-5)! is ALREADY a polynomial Q_j(m) in m = n - j (for j=0..5)!
    # And multiplying by x^(n-5) = x^(m+j-5): since m = x d/dx on x^m, Q_j(x d/dx) y_hat(x) (minus n<=5 boundary terms) = sum_{m>=1} Q_j(m) a(m)/m! x^m,
    # and multiplying by x^{5-j} (wait: x^(n-5) = x^{j-5} x^m! For j=0..4, j-5 < 0! Wait: to avoid negative powers of x, multiply M(n)=0 by x^n / (n-5)!? No, multiply by x^n / n! no, multiply by x^{n-5} / (n-5)! and then multiply the whole sum by x^5, OR multiply by x^n / (n-5)! directly!).
    # Multiplying M(n)=0 by x^n / (n-5)! gives for each j=0..5:
    # sum_{n>=6} C_j(n) * [(n-j)! / (n-5)!] * a(n-j)/(n-j)! * x^n = sum_{m >= 6-j} Q_j(m) a(m)/m! * x^{m+j},
    # where Q_j(m) = C_j(m+j) * prod_{t=j}^{4} (m + j - t) is an exact polynomial in m!
    # Since deg(Q_0) = 1 + 5 = 6, replacing m -> theta = x d/dx gives a genuine order-6 polynomial-coeff ODE for y_hat(x) (up to a polynomial of degree <= 10 from n<6)!
    x_sym = sp.Symbol("x")
    m_sym = sp.Symbol("m")
    # Build the order-6 operator L_hat(y) = sum_{j=0}^5 x^j Q_j(theta) y, checking exact identity on Taylor series up to x^35!
    Q_polys = []
    for j in range(6):
        falling = sp.Integer(1)
        for t in range(j, 5):
            falling *= (m_sym + j - t)
        Q_j = sp.expand(C[j].subs(n_sym, m_sym + j) * falling)
        Q_polys.append(Q_j)
    # Check nontriviality: highest theta power comes from j=0 (deg Q_0 = 6) with coeff 16 * m^6 -> 16 * x^6 * y^(6)(x) != 0!
    assert sp.Poly(Q_polys[0], m_sym).degree() == 6 and sp.Poly(Q_polys[0], m_sym).LC() == 16
    # Verify sum_{j=0}^5 [x^n] (x^j Q_j(theta) y_hat(x)) == 0 for ALL 6 <= n <= 35 (exact Fraction coefficients)!
    y_coeffs = [Fraction(a[k], math.factorial(k)) if k >= 1 else Fraction(0) for k in range(41)]
    for n_val in range(6, 36):
        coeff_n = Fraction(0)
        for j in range(6):
            m_val = n_val - j
            if m_val >= 1:
                q_val = int(Q_polys[j].subs(m_sym, m_val))
                coeff_n += q_val * y_coeffs[m_val]
        assert coeff_n == 0, f"EGF ODE coeff at x^{n_val} nonzero: {coeff_n}"
    # Also verify that converting to d/dx gives a nonzero order-6 differential operator (leading coeff on y^(6) is 16*x^6 + ...)
    y_fn = sp.Function("y")(x_sym)
    ode_expr = sp.Integer(0)
    for j in range(6):
        poly_j = sp.Poly(Q_polys[j], m_sym)
        for deg, coeff in poly_j.terms():
            d = deg[0]
            # Compute theta^d (y)
            term = y_fn
            for _ in range(d):
                term = x_sym * sp.diff(term, x_sym)
            ode_expr += coeff * (x_sym**j) * term
    ode_collected = sp.collect(sp.expand(ode_expr), [sp.diff(y_fn, (x_sym, k)) for k in range(7)])
    lead_coeff = sp.factor(ode_collected.coeff(sp.diff(y_fn, (x_sym, 6))))
    assert lead_coeff != 0
    print(f"EGF order-6 polynomial-coeff ODE verified (leading coeff of y^(6): {lead_coeff}).")

    print("PASS")


if __name__ == "__main__":
    main()
