"""Independent exact verifier for targets/oeis-A121752 (Mathar D-finite recurrence conjecture).

Uses only exact integer and symbolic Z[n]/Z[r]/Q[x] arithmetic (zero floating point).
"""

import sympy as sp

OEIS_DATA_REV4 = [
    1,
    2,
    7,
    39,
    235,
    1746,
    14166,
    132408,
    1341432,
    15148080,
    183764880,
    2435607360,
    34406268480,
    523839899520,
    8444375452800,
    145266278169600,
    2631329637350400,
    50481429165619200,
    1015073771517388800,
]


def fact(m: int) -> int:
    res = 1
    for i in range(2, m + 1):
        res *= i
    return res


def f_primary(n: int) -> int:
    return n * (n // 2) - (n - 2) * ((n - 1) // 2) - 1


def primary_sequence(N: int) -> list[int]:
    """Return [0, a(1), a(2), ..., a(N)] from the primary OEIS A121752 recurrence."""
    a = [0] * (N + 1)
    a[1] = 1
    if N >= 2:
        a[2] = 2
    for n in range(3, N + 1):
        a[n] = (2 * n - 3) * a[n - 1] - (n - 1) * (n - 3) * a[n - 2] + fact(n - 2) * f_primary(n)
    return a


def C_coeffs(n):
    return [
        -460 * n + 1223,
        460 * n**2 + 460 * n - 5569,
        460 * n**3 - 3826 * n**2 + 7853 * n + 1313,
        -460 * n**4 + 1840 * n**3 + 5501 * n**2 - 31045 * n + 31726,
        1223 * n**4 - 13205 * n**3 + 45787 * n**2 - 51389 * n + 558,
        -2 * (426 * n - 1111) * (n - 6) * (n - 4) ** 2,
    ]


def e_coeffs(n):
    return [
        -460 * n + 1223,
        1683 * n - 5569,
        460 * n**3 - 2143 * n**2 + 601 * n + 6882,
        -1223 * n**3 + 10388 * n**2 - 25365 * n + 17962,
        2 * (n - 6) * (n - 4) * (426 * n - 1111),
    ]


def S_even(r):
    return (r - 1) * (4 * r**2 - 3 * r + 1)


def S_odd(r):
    return r**2 * (4 * r - 3)


def main() -> None:
    # 1. Verify primary recurrence matches all 19 OEIS rev. 4 terms.
    N = 80
    a = primary_sequence(N)
    assert a[1 : len(OEIS_DATA_REV4) + 1] == OEIS_DATA_REV4, "Mismatch with OEIS data"

    # 2. Verify Step 1 parity formulas for f(j), S(k), and D(k) = a(k) - k*a(k-1) for k = 3..80.
    running_S = 0
    for k_val in range(3, N + 1):
        fk = f_primary(k_val)
        if k_val % 2 == 0:
            m = k_val // 2
            assert fk == 4 * m - 3
        else:
            m = (k_val - 1) // 2
            assert fk == 2 * m - 1
        running_S += (k_val - 2) * fk
        if k_val % 2 == 0:
            r_val = k_val // 2
            assert running_S == S_even(r_val)
        else:
            r_val = (k_val - 1) // 2
            assert running_S == S_odd(r_val)
        D_val = a[k_val] - k_val * a[k_val - 1]
        assert D_val == fact(k_val - 3) * running_S, f"D({k_val}) mismatch"

    # 3. Verify Step 2 operator factorization M(n) == sum_{i=0}^4 e_i(n)*D(n-i) identically in Z[n][a_0..a_5].
    n_sym = sp.Symbol("n")
    a_syms = sp.symbols("a0 a1 a2 a3 a4 a5")  # a_j represents a(n-j)
    lhs = sum(c * aj for c, aj in zip(C_coeffs(n_sym), a_syms))
    rhs = sum(e * (a_syms[i] - (n_sym - i) * a_syms[i + 1]) for i, e in enumerate(e_coeffs(n_sym)))
    assert sp.expand(lhs - rhs) == 0, f"Step 2 factorization mismatch: {sp.expand(lhs - rhs)}"

    # 4. Verify Step 3 exact polynomial cancellation P_even(r) == 0 and P_odd(r) == 0 in Z[r].
    r = sp.Symbol("r")

    ee = e_coeffs(2 * r)
    P_even = sp.expand(
        ee[0] * (2 * r - 3) * (2 * r - 4) * (2 * r - 5) * (2 * r - 6) * S_even(r)
        + ee[1] * (2 * r - 4) * (2 * r - 5) * (2 * r - 6) * S_odd(r - 1)
        + ee[2] * (2 * r - 5) * (2 * r - 6) * S_even(r - 1)
        + ee[3] * (2 * r - 6) * S_odd(r - 2)
        + ee[4] * S_even(r - 2)
    )
    assert sp.Poly(P_even, r, domain="ZZ").is_zero, f"P_even != 0: {P_even}"

    eo = e_coeffs(2 * r + 1)
    P_odd = sp.expand(
        eo[0] * (2 * r - 2) * (2 * r - 3) * (2 * r - 4) * (2 * r - 5) * S_odd(r)
        + eo[1] * (2 * r - 3) * (2 * r - 4) * (2 * r - 5) * S_even(r)
        + eo[2] * (2 * r - 4) * (2 * r - 5) * S_odd(r - 1)
        + eo[3] * (2 * r - 5) * S_even(r - 1)
        + eo[4] * S_odd(r - 2)
    )
    assert sp.Poly(P_odd, r, domain="ZZ").is_zero, f"P_odd != 0: {P_odd}"

    # 5. Direct numerical verification M(n) == 0 for 6 <= n <= 80.
    for n_val in range(6, N + 1):
        M_val = sum(c * a[n_val - j] for j, c in enumerate(C_coeffs(n_val)))
        assert M_val == 0, f"M({n_val}) = {M_val} != 0"

    # 6. Verify Step 3 D-finiteness: sum_{n>=6} M(n) x^{n-5}/(n-5)! = 0 -> linear ODE with poly coeffs.
    x, m_sym = sp.symbols("x m")
    y_fn = sp.Function("y")(x)

    def theta_pow(expr, deg: int):
        res = expr
        for _ in range(deg):
            res = sp.expand(x * sp.diff(res, x))
        return res

    ode_lhs = sp.Integer(0)
    rhs_const = sp.Integer(0)
    C_in_m = C_coeffs(m_sym + 5)
    for j in range(6):
        s = 5 - j
        poly = sp.Poly(C_in_m[j], m_sym, domain="ZZ")
        for (deg,), coeff in poly.terms():
            ode_lhs += coeff * theta_pow(sp.diff(y_fn, (x, s)), deg)
            if s >= 1 and deg == 0:
                rhs_const += coeff * a[s]

    ode_lhs = sp.expand(ode_lhs)
    lead_y5 = sp.factor(ode_lhs.coeff(sp.diff(y_fn, (x, 5))))
    assert lead_y5 != 0 and lead_y5.subs(x, 0) == C_coeffs(5)[0]

    M_TRUNC = 25
    y_trunc = sum(sp.Rational(a[n], fact(n)) * x**n for n in range(1, M_TRUNC + 1))
    diff_poly = sp.expand(ode_lhs.subs(y_fn, y_trunc).doit() - rhs_const)
    assert sp.series(diff_poly, x, 0, M_TRUNC - 4).removeO() == 0
    homog_ode = sp.expand(sp.diff(ode_lhs, x))
    assert sp.series(homog_ode.subs(y_fn, y_trunc).doit(), x, 0, M_TRUNC - 5).removeO() == 0

    print("PASS")
    print(f"Verified OEIS data n=1..{len(OEIS_DATA_REV4)}, Step 1 k=3..{N}, Step 2 identity in Z[n], P_even=P_odd=0 in Z[r], M(n)=0 for n=6..{N}.")
    print(f"Step 3 ODE: y^(5) coeff = {lead_y5}, inhomogeneous constant = {rhs_const}, homogeneous order-6 ODE verified up to x^{M_TRUNC-6}.")


if __name__ == "__main__":
    main()
