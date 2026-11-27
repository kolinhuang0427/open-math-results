"""Independent exact-arithmetic verifier for targets/oeis-A162481/ (PROOF.md).

Zero floating-point operations or literals anywhere in this script.
Checks:
1. Exact live OEIS DATA match for A162481 (rev. 23, 24 terms) via Catalan
   composition, quadratic equation A(x) = 1/(1-x)^3 + x A(x)^2, and Manyama binomial sum.
2. Exact symbolic verification in SymPy (QQ[x], QQ[n]) of Section 1 and Section 2 ODE
   derivations and coefficient extraction.
3. Direct verification of Mathar's 4-term recurrence for n = 2..60.
"""

from math import comb
import sympy as sp

A162481_LIVE = [
    1, 4, 14, 54, 235, 1119, 5658, 29800, 161621, 896198, 5056824, 28938519,
    167548937, 979653821, 5776252440, 34305807512, 205039491091, 1232333298174,
    7443336041318, 45157243590384, 275051410542141, 1681362181696823,
    10311616254855422, 63428758470722109,
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


def main() -> None:
    N_MAX = 60

    print("[1/3] Generating A162481(0..60) from quadratic relation and checking OEIS data...")
    # a(n) = binomial(n+2, 2) + sum_{k=0..n-1} a(k)*a(n-k-1)
    a = []
    for n in range(N_MAX + 1):
        val = comb(n + 2, 2) + sum(a[k] * a[n - 1 - k] for k in range(n))
        a.append(val)

    assert a[: len(A162481_LIVE)] == A162481_LIVE

    # Cross-check against sum_{k=0..n} comb(n+2k+2, n-k) * C_k for n <= 40
    cat = [comb(2 * k, k) // (k + 1) for k in range(41)]
    for n in range(41):
        val_cat = sum(comb(n + 2 * k + 2, n - k) * cat[k] for k in range(n + 1))
        assert val_cat == a[n]

    # Verify x*(1-x)^3 A(x)^2 - (1-x)^3 A(x) + 1 == 0 mod x^{61}
    a2 = poly_mul(a, a, N_MAX)
    one_m_x3 = [1, -3, 3, -1]
    lhs_q = [0] * (N_MAX + 1)
    xa2 = [0] + a2[:-1]
    t1 = poly_mul(one_m_x3, xa2, N_MAX)
    t2 = poly_mul(one_m_x3, a, N_MAX)
    for n in range(N_MAX + 1):
        lhs_q[n] = t1[n] - t2[n] + (1 if n == 0 else 0)
        assert lhs_q[n] == 0
    print(f"      Matched all {len(A162481_LIVE)} live terms, Catalan sum (n<=40), and algebraic equation to x^60.")

    print("[2/3] Symbolically verifying Section 1 & Section 2 ODE derivations...")
    x, n_sym = sp.symbols("x n")
    Q = 1 - 7 * x + 3 * x**2 - x**3
    R = (1 - x) ** 3

    # Verify (1-x)^3 - 4*x == Q
    assert sp.expand(R - 4 * x - Q) == 0

    # Verify dividing out 4*(1-x)^2 gives claimed ODE
    ode_A_p_raw = 4 * x * Q * R
    ode_A_raw = 4 * Q * R - 2 * x * (sp.diff(Q, x) * R - Q * sp.diff(R, x))
    ode_rhs_raw = Q * sp.diff(R, x) - sp.diff(Q, x) * R

    fac = 4 * (1 - x) ** 2
    P1 = sp.simplify(ode_A_p_raw / fac)
    P0 = sp.simplify(ode_A_raw / fac)
    RHS = sp.simplify(ode_rhs_raw / fac)

    assert sp.expand(P1 - x * (1 - 8 * x + 10 * x**2 - 4 * x**3 + x**4)) == 0
    assert sp.expand(P0 - (1 - 6 * x + 14 * x**2 - 4 * x**3 + x**4)) == 0
    assert sp.expand(RHS - (1 + 2 * x)) == 0

    # Check series satisfies ODE up to x^{59}
    P1_c = [0, 1, -8, 10, -4, 1]
    P0_c = [1, -6, 14, -4, 1]
    da = [k * a[k] for k in range(1, N_MAX + 1)]
    ode_lhs = [
        poly_mul(P1_c, da, N_MAX - 1)[k] + poly_mul(P0_c, a, N_MAX - 1)[k]
        for k in range(N_MAX)
    ]
    ode_rhs = [1 if k == 0 else (2 if k == 1 else 0) for k in range(N_MAX)]
    assert ode_lhs == ode_rhs

    # Check symbolic recurrence polynomials from P1, P0
    rec_sym = (
        (n_sym + 1) * sp.Symbol("a0")
        + 2 * (1 - 4 * n_sym) * sp.Symbol("a1")
        + 2 * (5 * n_sym - 3) * sp.Symbol("a2")
        + 4 * (2 - n_sym) * sp.Symbol("a3")
        + (n_sym - 3) * sp.Symbol("a4")
    )
    a_syms = [sp.Symbol(f"a{k}") for k in range(5)]
    P1_poly = sp.Poly(P1, x)
    P0_poly = sp.Poly(P0, x)
    extracted = sum(
        (P1_poly.coeff_monomial(x ** (k + 1)) * (n_sym - k) + P0_poly.coeff_monomial(x**k))
        * a_syms[k]
        for k in range(5)
    )
    assert sp.expand(extracted - rec_sym) == 0
    print("      Symbolic ODE and recurrence polynomials match identically.")

    print("[3/3] Checking Mathar's 4-term recurrence numerically for n = 2..60...")
    for n in range(2, N_MAX + 1):
        val = (
            (n + 1) * a[n]
            + 2 * (1 - 4 * n) * a[n - 1]
            + 2 * (5 * n - 3) * a[n - 2]
            + 4 * (2 - n) * (a[n - 3] if n >= 3 else 0)
            + (n - 3) * (a[n - 4] if n >= 4 else 0)
        )
        assert val == 0, f"Recurrence nonzero at n={n}: {val}"
    print("      Recurrence holds identically for all n = 2..60.")
    print("PASS")


if __name__ == "__main__":
    main()
