#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A168452 (Mathar 2024 D-finite recurrence).

Built strictly from OEIS A168452 definitions and targets/oeis-A168452/PROOF.md
without reading verify.py or notes/. Uses exact sympy and Python int arithmetic (zero floats).
"""

from __future__ import annotations

import math
import sys
import sympy as sp


def check_symbolic_proof() -> None:
    x, B, Bp, n = sp.symbols("x B Bp n")

    # Step 1: Verify binomial ratio & ODE (1) for B(x)
    # B'' = (-2 + 2*(1-6x)*B + 4x*(1-12x)*Bp) / delta, where delta = x^2*(16x - 1)
    delta = x**2 * (16 * x - 1)
    Bpp_num = -2 + 2 * (1 - 6 * x) * B + 4 * x * (1 - 12 * x) * Bp

    # Verify Step 1 LHS/RHS algebraic match:
    # sum_{n>=1} (n+1)(n+2) b(n) x^n = x^2 B'' + 4x B' + 2 B - 2
    # 4 * sum_{m>=0} (2m+1)(2m+3) b(m) x^{m+1} = 4x (4x^2 B'' + 12x B' + 3 B)
    m = sp.Symbol("m")
    assert sp.expand((2 * m + 1) * (2 * m + 3) - (4 * m * (m - 1) + 12 * m + 3)) == 0
    lhs_ode = x**2 * sp.Symbol("Bpp") + 4 * x * Bp + 2 * B - 2
    rhs_ode = 4 * x * (4 * x**2 * sp.Symbol("Bpp") + 12 * x * Bp + 3 * B)
    # rhs_ode - lhs_ode == 0 <=> delta * Bpp == Bpp_num
    assert sp.expand((rhs_ode - lhs_ode) - (delta * sp.Symbol("Bpp") - Bpp_num)) == 0

    # Step 2: Check M_0..M_5 displayed in PROOF.md match inductive differentiation of y = B^2
    D_list = [
        sp.Integer(1),
        sp.Integer(1),
        x**2 * (16 * x - 1),
        x**3 * (16 * x - 1),
        x**4 * (16 * x - 1) ** 2,
        x**5 * (16 * x - 1) ** 3,
    ]
    M_displayed = [
        B**2,
        2 * B * Bp,
        2 * ((-12 * x + 2) * B**2 + (-48 * x**2 + 4 * x) * B * Bp - 2 * B + (16 * x**3 - x**2) * Bp**2),
        -12 * ((-10 * x + 2) * B**2 + (-24 * x**2 + 2 * x) * B * Bp - 2 * B + (24 * x**3 - 2 * x**2) * Bp**2 + x * Bp),
        24 * (
            (-384 * x**2 + 110 * x - 5) * B**2
            + (-512 * x**3 + 42 * x**2) * B * Bp
            + (-82 * x + 4) * B
            + (1536 * x**4 - 252 * x**3 + 10 * x**2) * Bp**2
            + (112 * x**2 - 8 * x) * Bp
            + 1
        ),
        -48 * (
            (-15360 * x**3 + 5548 * x**2 - 447 * x + 10) * B**2
            + (-4608 * x**3 + 688 * x**2 - 25 * x) * B * Bp
            + (-3120 * x**2 + 197 * x) * B
            + (102400 * x**5 - 24880 * x**4 + 1955 * x**3 - 50 * x**2) * Bp**2
            + (10000 * x**3 - 1425 * x**2 + 50 * x) * Bp
            + (160 * x - 10)
        ),
    ]

    # Inductively verify D_k y^{(k)} = M_k:
    # Differentiating D_k y^{(k)} = M_k wrt x gives D_k y^{(k+1)} + D_k' y^{(k)} = d/dx(M_k),
    # i.e. delta * D_k * y^{(k+1)} = delta * (d/dx M_k) - delta * D_k' * (M_k / D_k),
    # so D_{k+1} * (delta * D_k * (d/dx M_k) - delta * D_k' * M_k) ... wait:
    # Clear denominator D_k * delta:
    # D_k^2 * delta * y^{(k+1)} = D_k * (delta * D_x M_k) - delta * D_k' * M_k,
    # where D_x M_k = partial_x M_k + partial_B M_k * Bp + partial_Bp M_k * (Bpp_num / delta),
    # so delta * D_x M_k = delta * (partial_x M_k + partial_B M_k * Bp) + (partial_Bp M_k) * Bpp_num.
    # Thus D_{k+1} * M_k vs M_{k+1}:
    # D_k * M_{k+1} * (delta * D_k) = D_{k+1} * (D_k * (delta * D_x M_k) - delta * D_k' * M_k) ?
    # Wait: y^{(k+1)} = M_{k+1}/D_{k+1} and y^{(k)} = M_k/D_k, so:
    # (M_{k+1} / D_{k+1}) * D_k + D_k' * (M_k / D_k) = D_x M_k
    # Multiply by D_k * D_{k+1} * delta:
    # D_k^2 * delta * M_{k+1} = D_{k+1} * (D_k * (delta * D_x M_k) - delta * D_k' * M_k)!
    for k in range(5):
        Dk = D_list[k]
        Dk1 = D_list[k + 1]
        Mk = M_displayed[k]
        Mk1 = M_displayed[k + 1]
        delta_Dx_Mk = delta * (sp.diff(Mk, x) + sp.diff(Mk, B) * Bp) + sp.diff(Mk, Bp) * Bpp_num
        lhs = sp.expand(Dk**2 * delta * Mk1)
        rhs = sp.expand(Dk1 * (Dk * delta_Dx_Mk - delta * sp.diff(Dk, x) * Mk))
        assert lhs == rhs, f"Inductive relation M_{k} -> M_{k+1} failed!"

    # Check p_k(x) = q_k(x) * D_k(x) and sum q_k * M_k == 72 - 1152*x
    p_list = [
        -24 * (61440 * x**4 + 8640 * x**3 - 2572 * x**2 + 168 * x - 3),
        -24 * x * (512000 * x**4 + 39552 * x**3 - 18056 * x**2 + 1285 * x - 27),
        -24 * x**2 * (16 * x - 1) * (46720 * x**3 + 4968 * x**2 - 1121 * x + 39),
        -12 * x**3 * (16 * x - 1) ** 2 * (2640 * x**2 + 391 * x - 34),
        -x**4 * (16 * x - 1) ** 3 * (320 * x + 63),
        -x**5 * (16 * x - 1) ** 3 * (16 * x + 3),
    ]
    total = sp.Integer(0)
    for k in range(6):
        qk, rem = sp.div(p_list[k], D_list[k], x)
        assert rem == 0, f"D_{k} does not divide p_{k}"
        total += sp.expand(qk * M_displayed[k])
    assert sp.expand(total - (72 - 1152 * x)) == 0, f"ODE combination failed: {sp.expand(total)}"

    # Step 3: Exact symbolic extraction in Z[n]
    a_coeff = {j: sp.Integer(0) for j in range(5)}
    for k in range(6):
        poly_pk = sp.Poly(p_list[k], x)
        for (d,), coef in poly_pk.terms():
            j = d - k
            assert 0 <= j <= 4, f"Index offset j={j} out of range for k={k}, d={d}"
            m_sym = n - j
            ff = sp.Integer(1)
            for i in range(k):
                ff *= (m_sym - i)
            a_coeff[j] += coef * ff

    expected_C = {
        0: 3 * (n + 4) * (n + 3) * (n + 2) * (n + 1) ** 2,
        1: -4 * n * (n + 1) * (32 * n**3 + 164 * n**2 + 233 * n + 75),
        2: 96 * (16 * n**5 + 24 * n**4 - 14 * n**3 - 28 * n**2 - 16 * n + 3),
        3: 1536 * (-8 * n**4 + 22 * n**3 - 32 * n + 15),
        4: -16384 * (2 * n - 5) * (n - 1) * (n - 2) * (n - 3) * (2 * n - 3),
    }
    for j in range(5):
        assert sp.expand(a_coeff[j] - expected_C[j]) == 0, f"Recurrence coefficient C_{j}(n) mismatch"


def run_all_checks() -> None:
    print("Check 1: Exact symbolic verification of Steps 1, 2, 3 in Z[x, B, B'] and Z[n]...")
    check_symbolic_proof()
    print("  All symbolic identities and extractions passed.")

    N = 60
    print(f"Check 2: Exact integer series expansion and recurrence check for n=0..{N}...")
    cat = [math.comb(2 * k, k) // (k + 1) for k in range(N + 2)]
    b = [cat[k] * cat[k + 1] for k in range(N + 1)]
    for k in range(1, N + 1):
        assert (k + 1) * (k + 2) * b[k] == 4 * (2 * k - 1) * (2 * k + 1) * b[k - 1]

    a = [sum(b[k] * b[n - k] for k in range(n + 1)) for n in range(N + 1)]

    # Verify OEIS A168452 %S/%T/%U values (a(0)..a(20))
    oeis_prefix = [
        1, 4, 24, 180, 1556, 14840, 152092, 1646652, 18613664, 217852008, 2623657384,
        32361812912, 407342311632, 5217211974832, 67836910362772,
        893766246630572, 11913422912188432, 160450066324972472,
        2181014117345997704, 29894260817385950064, 412839378639052110464,
    ]
    assert a[: len(oeis_prefix)] == oeis_prefix, "OEIS A168452 prefix mismatch"

    for n in range(4, N + 1):
        c0 = 3 * (n + 4) * (n + 3) * (n + 2) * (n + 1) ** 2
        c1 = -4 * n * (n + 1) * (32 * n**3 + 164 * n**2 + 233 * n + 75)
        c2 = 96 * (16 * n**5 + 24 * n**4 - 14 * n**3 - 28 * n**2 - 16 * n + 3)
        c3 = 1536 * (-8 * n**4 + 22 * n**3 - 32 * n + 15)
        c4 = -16384 * (2 * n - 5) * (n - 1) * (n - 2) * (n - 3) * (2 * n - 3)
        lhs = c0 * a[n] + c1 * a[n - 1] + c2 * a[n - 2] + c3 * a[n - 3] + c4 * a[n - 4]
        assert lhs == 0, f"Recurrence failed at n={n}: {lhs}"
    print(f"  Verified 21 OEIS terms and Mathar recurrence for 4 <= n <= {N}.")
    print("PASS")


if __name__ == "__main__":
    try:
        run_all_checks()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
