"""Independent exact verifier for targets/oeis-A121751 (Mathar D-finite recurrence conjecture).

Uses only exact integer and symbolic Z[k]/Q[x] arithmetic (zero floating point).
"""

import sympy as sp

OEIS_DATA_REV5 = [
    0,
    1,
    2,
    4,
    14,
    44,
    194,
    812,
    4362,
    22716,
    144282,
    897636,
    6587454,
    47632188,
    396765018,
    3268365228,
    30471767658,
    281641273164,
    2906047413234,
    29777551585092,
    336912811924014,
    3790278631556172,
    46662633394518258,
]


def primary_sequence(N: int) -> list[int]:
    """Return [0, a(1), a(2), ..., a(N)] from the primary OEIS A121751 recurrence."""
    a = [0] * (N + 1)
    a[1] = 0
    if N >= 2:
        a[2] = 1
    for n in range(3, N + 1):
        f1 = (n - 1) // 2
        f2 = (n - 2) // 2
        a[n] = 2 * f1 * a[n - 1] - (f1 * f2 - 1) * a[n - 2]
    return a


def C_coeffs(n):
    """Exact Mathar recurrence coefficients C_0(n), ..., C_6(n)."""
    return [
        256,
        -384,
        16 * (-8 * n**2 + 40 * n - 67),
        16 * (8 * n**2 - 54 * n + 87),
        4 * (4 * n**4 - 56 * n**3 + 242 * n**2 - 304 * n - 21),
        4 * (-2 * n**4 + 38 * n**3 - 249 * n**2 + 647 * n - 554),
        (n - 4) * (n - 8) * (n**2 - 12 * n + 31),
    ]


def main() -> None:
    # 1. Verify primary recurrence reproduces all 23 live OEIS rev. 5 terms.
    N = 100
    a = primary_sequence(N)
    assert a[1 : len(OEIS_DATA_REV5) + 1] == OEIS_DATA_REV5, "Mismatch with OEIS data"

    # 2. Verify Step 1 parity split against the floor recurrence for m = 3..200.
    a_long = primary_sequence(200)
    for m in range(3, 201):
        if m % 2 == 0:
            r = m // 2
            rhs = 2 * (r - 1) * a_long[2 * r - 1] - r * (r - 2) * a_long[2 * r - 2]
        else:
            r = (m - 1) // 2
            rhs = 2 * r * a_long[2 * r] - (r**2 - r - 1) * a_long[2 * r - 1]
        assert rhs == a_long[m], f"Step 1 parity failure at m={m}"

    # 3. Verify Step 2 exact polynomial cancellation in Z[k].
    k, u, v = sp.symbols("k u v")

    # Even case: n = 2k, u = a(2k-5), v = a(2k-6)
    e_2k_m6 = v
    e_2k_m5 = u
    e_2k_m4 = 2 * (k - 3) * e_2k_m5 - (k - 2) * (k - 4) * e_2k_m6
    e_2k_m3 = 2 * (k - 2) * e_2k_m4 - ((k - 2) * (k - 3) - 1) * e_2k_m5
    e_2k_m2 = 2 * (k - 2) * e_2k_m3 - (k - 1) * (k - 3) * e_2k_m4
    e_2k_m1 = 2 * (k - 1) * e_2k_m2 - ((k - 1) * (k - 2) - 1) * e_2k_m3
    e_2k = 2 * (k - 1) * e_2k_m1 - k * (k - 2) * e_2k_m2

    even_vals = [e_2k, e_2k_m1, e_2k_m2, e_2k_m3, e_2k_m4, e_2k_m5, e_2k_m6]
    M_even = sp.expand(sum(c * val for c, val in zip(C_coeffs(2 * k), even_vals)))
    A_even = sp.Poly(M_even.coeff(u), k, domain="ZZ")
    B_even = sp.Poly(M_even.coeff(v), k, domain="ZZ")
    assert M_even == 0 and A_even.is_zero and B_even.is_zero, f"Even non-zero: {M_even}"

    # Odd case: n = 2k+1, u = a(2k-4), v = a(2k-5)
    o_2k_m5 = v
    o_2k_m4 = u
    o_2k_m3 = 2 * (k - 2) * o_2k_m4 - ((k - 2) * (k - 3) - 1) * o_2k_m5
    o_2k_m2 = 2 * (k - 2) * o_2k_m3 - (k - 1) * (k - 3) * o_2k_m4
    o_2k_m1 = 2 * (k - 1) * o_2k_m2 - ((k - 1) * (k - 2) - 1) * o_2k_m3
    o_2k = 2 * (k - 1) * o_2k_m1 - k * (k - 2) * o_2k_m2
    o_2k_p1 = 2 * k * o_2k - (k * (k - 1) - 1) * o_2k_m1

    odd_vals = [o_2k_p1, o_2k, o_2k_m1, o_2k_m2, o_2k_m3, o_2k_m4, o_2k_m5]
    M_odd = sp.expand(sum(c * val for c, val in zip(C_coeffs(2 * k + 1), odd_vals)))
    A_odd = sp.Poly(M_odd.coeff(u), k, domain="ZZ")
    B_odd = sp.Poly(M_odd.coeff(v), k, domain="ZZ")
    assert M_odd == 0 and A_odd.is_zero and B_odd.is_zero, f"Odd non-zero: {M_odd}"

    # 4. Direct numerical check M(n) = 0 for 7 <= n <= 100.
    for n_val in range(7, N + 1):
        M_val = sum(c * a[n_val - j] for j, c in enumerate(C_coeffs(n_val)))
        assert M_val == 0, f"M({n_val}) = {M_val} != 0"

    # 5. Step 3 verification: explicit EGF ODE from sum_{n>=7} M(n) x^{n-6}/(n-6)! = 0.
    # Let m = n - 6 >= 1, so n = m + 6. Write C_j(m + 6) = sum_r d_{j,r} m^r.
    x, m_sym = sp.symbols("x m")
    y_fn = sp.Function("y")(x)

    def theta_pow(expr, r: int):
        res = expr
        for _ in range(r):
            res = sp.expand(x * sp.diff(res, x))
        return res

    ode_lhs = sp.Integer(0)
    rhs_const = sp.Integer(0)
    C_in_m = C_coeffs(m_sym + 6)
    for j in range(7):
        s = 6 - j
        poly = sp.Poly(C_in_m[j], m_sym, domain="ZZ")
        for (r,), coeff in poly.terms():
            ode_lhs += coeff * theta_pow(sp.diff(y_fn, (x, s)), r)
            # At m = 0: for s >= 1, sum_{m>=1} m^r a(m+s) x^m/m! = theta^r y^(s)(x) - (r==0)*a(s).
            # For s = 0 (j = 6), a(0) is not in y(x) = sum_{n>=1} a(n) x^n/n!, so m=0 term is 0.
            if s >= 1 and r == 0:
                rhs_const += coeff * a[s]

    ode_lhs = sp.expand(ode_lhs)
    lead_coeff_y6 = sp.factor(ode_lhs.coeff(sp.diff(y_fn, (x, 6))))
    assert lead_coeff_y6 == 16 * (x - 2) ** 2 * (x + 2) ** 2, (
        f"Unexpected y^(6) coeff: {lead_coeff_y6}"
    )

    # Verify truncated EGF y_trunc(x) satisfies ode_lhs == rhs_const (and d/dx(ode_lhs) == 0) up to x^23.
    M_TRUNC = 30
    y_trunc = sum(sp.Rational(a[n], sp.factorial(n)) * x**n for n in range(1, M_TRUNC + 1))
    # Coefficients of x^0..x^(M_TRUNC-6) in (ode_lhs - rhs_const) must vanish identically.
    diff_poly = sp.expand(ode_lhs.subs(y_fn, y_trunc).doit() - rhs_const)
    diff_series = sp.series(diff_poly, x, 0, M_TRUNC - 5).removeO()
    assert diff_series == 0, f"Truncated ODE residual: {diff_series}"

    homog_ode = sp.expand(sp.diff(ode_lhs, x))
    homog_res = sp.series(homog_ode.subs(y_fn, y_trunc).doit(), x, 0, M_TRUNC - 6).removeO()
    assert homog_res == 0, f"Truncated homogeneous 7th-order ODE residual: {homog_res}"

    print("PASS")
    print(f"Verified OEIS data n=1..{len(OEIS_DATA_REV5)}, Step 1 m=3..200, Step 2 A_even=B_even=A_odd=B_odd=0 in Z[k], M(n)=0 for n=7..{N}.")
    print(f"Step 3 ODE: y^(6) coeff = {lead_coeff_y6}, inhomogeneous constant = {rhs_const}, homogeneous order-7 ODE verified up to x^{M_TRUNC-7}.")


if __name__ == "__main__":
    main()
