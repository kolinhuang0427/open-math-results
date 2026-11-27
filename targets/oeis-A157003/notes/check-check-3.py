"""Independent exact-arithmetic verifier for targets/oeis-A157003/ (PROOF.md).

Zero floating-point operations or literals anywhere in this script.
Checks:
1. Exact live OEIS DATA match for A157003 (rev. 37, 28 terms) against both
   c(x*(1-x^2)) formal composition and the alternating Catalan binomial sum.
2. Exact symbolic verification in SymPy (QQ[x], QQ[n]) of Section 1 ODE and
   Section 2 K(n) + 5*K(n-1) = 0 polynomial coefficients.
3. Direct numerical verification of K(n) and Mathar's 6-term recurrence up to n = 60.
"""

from math import comb
import sympy as sp

A157003_LIVE = [
    1, 1, 2, 4, 10, 27, 78, 234, 722, 2274, 7280, 23617, 77466, 256481,
    856016, 2876940, 9728090, 33072228, 112974592, 387580856, 1334821448,
    4613225722, 15994465796, 55615889745, 193904367362, 677709772035,
    2374027931492, 8333765738127,
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

    print("[1/3] Generating A157003(0..60) from quadratic relation and checking OEIS data...")
    # (x - x^3) A(x)^2 - A(x) + 1 = 0 => a(0)=1, a(n) = [x^{n-1}] A^2 - [x^{n-3}] A^2
    a = [1]
    for n in range(1, N_MAX + 1):
        val = sum(a[i] * a[n - 1 - i] for i in range(n))
        if n >= 3:
            val -= sum(a[i] * a[n - 3 - i] for i in range(n - 2))
        a.append(val)

    assert a[: len(A157003_LIVE)] == A157003_LIVE

    # Cross-check OEIS binomial sum formula for n = 0..45
    cat = [comb(2 * k, k) // (k + 1) for k in range(46)]
    for n in range(46):
        val_sum = 0
        for k in range(n + 1):
            if (n - k) % 2 == 0:
                m = (n - k) // 2
                if m <= k:
                    sign = -1 if m % 2 == 1 else 1
                    val_sum += sign * comb(k, m) * cat[k]
        assert val_sum == a[n], f"Binomial sum mismatch at n={n}"
    print(f"      Matched all {len(A157003_LIVE)} live terms and binomial Catalan formula (n<=45).")

    print("[2/3] Symbolically verifying Section 1 ODE and Section 2 K(n) + 5*K(n-1)...")
    x, n_sym = sp.symbols("x n")
    P = x - x**3
    Delta = 1 - 4 * P
    assert sp.expand(Delta - (1 - 4 * x + 4 * x**3)) == 0

    P1 = sp.expand(Delta * P)
    P0 = sp.expand(Delta * sp.diff(P, x) - sp.Rational(1, 2) * sp.diff(Delta, x) * P)
    RHS = sp.expand(-sp.Rational(1, 4) * sp.diff(Delta, x))

    assert sp.expand(P1 - x * (1 - 4 * x - x**2 + 8 * x**3 - 4 * x**5)) == 0
    assert sp.expand(P0 - (1 - 2 * x - 3 * x**2 + 8 * x**3 - 6 * x**5)) == 0
    assert sp.expand(RHS - (1 - 3 * x**2)) == 0

    # Verify formal series A satisfies ODE up to x^{59}
    P1_c = [0, 1, -4, -1, 8, 0, -4]
    P0_c = [1, -2, -3, 8, 0, -6]
    da = [k * a[k] for k in range(1, N_MAX + 1)]
    ode_lhs = [
        poly_mul(P1_c, da, N_MAX - 1)[k] + poly_mul(P0_c, a, N_MAX - 1)[k]
        for k in range(N_MAX)
    ]
    ode_rhs = [1 if k == 0 else (-3 if k == 2 else 0) for k in range(N_MAX)]
    assert ode_lhs == ode_rhs

    # Check K(n) extraction and K(n) + 5*K(n-1) == Mathar's 6-term recurrence
    a_syms = [sp.Symbol(f"a{k}") for k in range(7)]
    P1_poly = sp.Poly(P1, x)
    P0_poly = sp.Poly(P0, x)
    K_sym = sum(
        (P1_poly.coeff_monomial(x ** (k + 1)) * (n_sym - k) + P0_poly.coeff_monomial(x**k))
        * a_syms[k]
        for k in range(6)
    )
    K_expected = (
        (n_sym + 1) * a_syms[0]
        - 2 * (2 * n_sym - 1) * a_syms[1]
        - (n_sym + 1) * a_syms[2]
        + 8 * (n_sym - 2) * a_syms[3]
        - 2 * (2 * n_sym - 7) * a_syms[5]
    )
    assert sp.expand(K_sym - K_expected) == 0

    # Shift K(n-1): replaces n -> n-1 and a_k -> a_{k+1}
    K_shift = K_expected.subs(
        {n_sym: n_sym - 1, **{a_syms[k]: a_syms[k + 1] for k in range(6)}},
        simultaneous=True,
    )
    mathar_sym = (
        (n_sym + 1) * a_syms[0]
        + (n_sym + 2) * a_syms[1]
        + (-21 * n_sym + 29) * a_syms[2]
        + (3 * n_sym - 16) * a_syms[3]
        + 40 * (n_sym - 3) * a_syms[4]
        + 2 * (-2 * n_sym + 7) * a_syms[5]
        + 10 * (-2 * n_sym + 9) * a_syms[6]
    )
    assert sp.expand(K_expected + 5 * K_shift - mathar_sym) == 0
    print("      Symbolic ODE, K(n), and K(n) + 5*K(n-1) match identically.")

    print("[3/3] Checking K(n) (n>=3) and Mathar's 6-term recurrence (n>=5) up to n = 60...")
    def get_a(idx: int) -> int:
        return a[idx] if idx >= 0 else 0

    for n in range(3, N_MAX + 1):
        k_val = (
            (n + 1) * get_a(n)
            - 2 * (2 * n - 1) * get_a(n - 1)
            - (n + 1) * get_a(n - 2)
            + 8 * (n - 2) * get_a(n - 3)
            - 2 * (2 * n - 7) * get_a(n - 5)
        )
        assert k_val == 0, f"K({n}) != 0: {k_val}"
    for n in range(5, N_MAX + 1):
        m_val = (
            (n + 1) * get_a(n)
            + (n + 2) * get_a(n - 1)
            + (-21 * n + 29) * get_a(n - 2)
            + (3 * n - 16) * get_a(n - 3)
            + 40 * (n - 3) * get_a(n - 4)
            + 2 * (-2 * n + 7) * get_a(n - 5)
            + 10 * (-2 * n + 9) * get_a(n - 6)
        )
        assert m_val == 0, f"Mathar nonzero at n={n}: {m_val}"
    print("      Both recurrences hold identically up to n = 60.")
    print("PASS")


if __name__ == "__main__":
    main()
