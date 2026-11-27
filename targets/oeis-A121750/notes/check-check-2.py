"""Independent exact verifier for targets/oeis-A121750 (Mathar D-finite recurrence conjecture).

Uses only exact integer and symbolic Z[n]/Z[r]/Q[x] arithmetic (zero floating point).
"""

import sympy as sp

OEIS_DATA_REV13 = [
    0,
    1,
    5,
    26,
    184,
    1338,
    11652,
    108210,
    1140336,
    12849714,
    159858900,
    2117522754,
    30442090248,
    463511103426,
    7569181895436,
    130254363597330,
    2383020441932256,
    45738553437874962,
    927010880040945924,
]


def fact(m: int) -> int:
    res = 1
    for i in range(2, m + 1):
        res *= i
    return res


def primary_sequence(N: int) -> tuple[list[int], list[int]]:
    """Return ([0, a(1), ..., a(N)], [0, d(1), ..., d(N)]) from OEIS A121750."""
    d = [0] * (N + 1)
    d[1] = 1
    if N >= 2:
        d[2] = 0
    for k in range(3, N + 1):
        if k % 2 == 0:
            d[k] = d[k - 2] + fact(k - 1)
        else:
            d[k] = -d[k - 1]

    a = [0] * (N + 1)
    a[1] = 0
    for n in range(2, N + 1):
        a[n] = n * a[n - 1] + d[n - 1] + fact(n - 1) * ((n - 1) // 2)
    return a, d


def C_coeffs(n):
    return [
        1,
        -n - 2,
        -n**2 + 4 * n - 2,
        n**3 - 3 * n**2 - 4 * n + 11,
        -(n - 1) * (n**2 - 11 * n + 26),
        -(n**3) + 5 * n**2 + 7 * n - 43,
        (n - 3) * (n - 5) ** 2,
    ]


def c_ops(n):
    return [
        1,
        -3,
        -(n**2) + 2 * n + 3,
        2 * n**2 - 10 * n + 8,
        -(n**2) + 8 * n - 15,
    ]


def W_even(m):
    return 2 * m**2 - 2 * m


def W_odd(m):
    return 2 * m**2 + m


def main() -> None:
    # 1. Verify primary recurrence reproduces all 19 live OEIS rev. 13 terms.
    N = 80
    a, _d = primary_sequence(N)
    assert a[1 : len(OEIS_DATA_REV13) + 1] == OEIS_DATA_REV13, "Mismatch with OEIS data"

    # 2. Verify Step 1 formulas for D(k) and W(k) = D(k) + D(k-1) for k = 3..80.
    for k_val in range(3, N + 1):
        W_val = a[k_val] - (k_val - 1) * a[k_val - 1] - (k_val - 1) * a[k_val - 2]
        if k_val % 2 == 0:
            m = k_val // 2
            assert W_val == fact(2 * m - 2) * W_even(m)
        else:
            m = (k_val - 1) // 2
            assert W_val == fact(2 * m - 1) * W_odd(m)

    # 3. Verify Step 2 operator factorization M(n) == sum_{i=0}^4 c_i(n)*W(n-i) identically in Z[n].
    n_sym = sp.Symbol("n")
    a_syms = sp.symbols("a0 a1 a2 a3 a4 a5 a6")  # a_j represents a(n-j)
    lhs = sum(c * aj for c, aj in zip(C_coeffs(n_sym), a_syms))
    rhs = sum(
        c * (a_syms[i] - (n_sym - i - 1) * a_syms[i + 1] - (n_sym - i - 1) * a_syms[i + 2])
        for i, c in enumerate(c_ops(n_sym))
    )
    assert sp.expand(lhs - rhs) == 0, f"Step 2 factorization mismatch: {sp.expand(lhs - rhs)}"

    # 4. Verify Step 3 exact polynomial cancellation P_even(r) == 0 and P_odd(r) == 0 in Z[r].
    r = sp.Symbol("r")

    ce = c_ops(2 * r)
    P_even = sp.expand(
        ce[0] * (2 * r - 2) * (2 * r - 3) * (2 * r - 4) * (2 * r - 5) * W_even(r)
        + ce[1] * (2 * r - 3) * (2 * r - 4) * (2 * r - 5) * W_odd(r - 1)
        + ce[2] * (2 * r - 4) * (2 * r - 5) * W_even(r - 1)
        + ce[3] * (2 * r - 5) * W_odd(r - 2)
        + ce[4] * W_even(r - 2)
    )
    assert sp.Poly(P_even, r, domain="ZZ").is_zero, f"P_even != 0: {P_even}"

    co = c_ops(2 * r + 1)
    P_odd = sp.expand(
        co[0] * (2 * r - 1) * (2 * r - 2) * (2 * r - 3) * (2 * r - 4) * W_odd(r)
        + co[1] * (2 * r - 2) * (2 * r - 3) * (2 * r - 4) * W_even(r)
        + co[2] * (2 * r - 3) * (2 * r - 4) * W_odd(r - 1)
        + co[3] * (2 * r - 4) * W_even(r - 1)
        + co[4] * W_odd(r - 2)
    )
    assert sp.Poly(P_odd, r, domain="ZZ").is_zero, f"P_odd != 0: {P_odd}"

    # 5. Direct numerical verification M(n) == 0 for 7 <= n <= 80.
    for n_val in range(7, N + 1):
        M_val = sum(c * a[n_val - j] for j, c in enumerate(C_coeffs(n_val)))
        assert M_val == 0, f"M({n_val}) = {M_val} != 0"

    # 6. Verify Step 4 EGF ODE explicitly.
    x, m_sym = sp.symbols("x m")
    y_fn = sp.Function("y")(x)

    def theta_pow(expr, deg: int):
        res = expr
        for _ in range(deg):
            res = sp.expand(x * sp.diff(res, x))
        return res

    ode_lhs = sp.Integer(0)
    rhs_const = sp.Integer(0)
    C_in_m = C_coeffs(m_sym + 6)
    for j in range(7):
        s = 6 - j
        poly = sp.Poly(C_in_m[j], m_sym, domain="ZZ")
        for (deg,), coeff in poly.terms():
            ode_lhs += coeff * theta_pow(sp.diff(y_fn, (x, s)), deg)
            if deg == 0:
                rhs_const += coeff * a[s]

    ode_lhs = sp.expand(ode_lhs)
    assert rhs_const == -3, f"Expected constant -3, got {rhs_const}"
    lead_y6 = sp.factor(ode_lhs.coeff(sp.diff(y_fn, (x, 6))))
    assert sp.expand(lead_y6 - (1 - x) ** 2 * (1 + x)) == 0, f"Unexpected leading coeff: {lead_y6}"

    M_TRUNC = 25
    y_trunc = sum(sp.Rational(a[n], fact(n)) * x**n for n in range(1, M_TRUNC + 1))
    diff_poly = sp.expand(ode_lhs.subs(y_fn, y_trunc).doit() - rhs_const)
    assert sp.series(diff_poly, x, 0, M_TRUNC - 5).removeO() == 0
    homog_ode = sp.expand(sp.diff(ode_lhs, x))
    assert sp.series(homog_ode.subs(y_fn, y_trunc).doit(), x, 0, M_TRUNC - 6).removeO() == 0

    print("PASS")
    print(f"Verified OEIS data n=1..{len(OEIS_DATA_REV13)}, Step 1 k=3..{N}, Step 2 identity in Z[n], P_even=P_odd=0 in Z[r], M(n)=0 for n=7..{N}.")
    print(f"Step 4 ODE: y^(6) coeff = {lead_y6}, inhomogeneous constant = {rhs_const}, homogeneous order-7 ODE verified up to x^{M_TRUNC-7}.")


if __name__ == "__main__":
    main()
