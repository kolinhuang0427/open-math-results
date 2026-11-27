#!/usr/bin/env python3
"""
Independent exact-arithmetic verifier for targets/oeis-A274272/
directly from OEIS A274272 definitions and PROOF.md without reading
verify.py or author notes. Zero floats.
"""
from __future__ import annotations

import sympy as sp


def verify_symbolic_proof() -> None:
    x, m = sp.symbols("x m")

    # 1. Partial fraction decomposition of F(x) = 1/((1-x)(1-x^2)(1-x^3)(1-x^4))
    F_gf = 1 / ((1 - x) * (1 - x**2) * (1 - x**3) * (1 - x**4))
    pf = (
        sp.Rational(1, 24) / (1 - x) ** 4
        + sp.Rational(1, 8) / (1 - x) ** 3
        + sp.Rational(59, 288) / (1 - x) ** 2
        + sp.Rational(17, 72) / (1 - x)
        + sp.Rational(1, 8) / (1 + x)
        + sp.Rational(1, 32) / (1 + x) ** 2
        + sp.Rational(1, 8) / (1 + x**2)
        + (1 + x) / (9 * (1 + x + x**2))
    )
    assert sp.simplify(F_gf - pf) == 0

    # Cleared denominator identity (PROOF.md L26-27)
    cleared = (
        (175 - 358 * x + 263 * x**2 - 68 * x**3) * (1 + x) ** 2 * (1 + x**2) * (1 + x + x**2)
        + 9 * (5 + 4 * x) * (1 - x) ** 4 * (1 + x**2) * (1 + x + x**2)
        + 36 * (1 - x) ** 4 * (1 + x) ** 2 * (1 + x + x**2)
        + 32 * (1 + x) * (1 - x) ** 4 * (1 + x) ** 2 * (1 + x**2)
    )
    assert sp.expand(cleared - 288) == 0

    # 2. Symbolic m polynomials for poles at x=1 and x=-1 (odd m)
    pole_1 = (
        sp.Rational(1, 24) * (m + 3) * (m + 2) * (m + 1) / 6
        + sp.Rational(1, 8) * (m + 2) * (m + 1) / 2
        + sp.Rational(59, 288) * (m + 1)
        + sp.Rational(17, 72)
    )
    assert sp.expand(pole_1 - (2 * m**3 + 30 * m**2 + 135 * m + 175) / 288) == 0

    pole_m1 = -sp.Rational(1, 8) - sp.Rational(1, 32) * (m + 1)
    assert sp.expand(pole_m1 - (-9 * m - 45) / 288) == 0

    # Cube root factor identity
    assert sp.simplify((1 + x) / (9 * (1 + x + x**2)) - (1 - x**2) / (9 * (1 - x**3))) == 0

    # 3. Rational GF G(x) from the 5 geometric series
    G_sum = sp.Rational(1, 144) * (
        sp.Integer(57) / (1 - x)
        + sp.Integer(8) / (1 + x)
        + sp.Integer(63) / (1 - 5 * x)
        + sp.Integer(15) / (1 - 25 * x)
        + sp.Integer(1) / (1 - 125 * x)
    )
    D = (1 - x) * (1 + x) * (1 - 5 * x) * (1 - 25 * x) * (1 - 125 * x)
    D_exp = 1 - 155 * x + 3874 * x**2 - 15470 * x**3 - 3875 * x**4 + 15625 * x**5
    assert sp.expand(D - D_exp) == 0
    N_exp = 1 - 149 * x + 3129 * x**2 - 5655 * x**3 - 6750 * x**4
    assert sp.simplify(G_sum - N_exp / D) == 0
    print("PASS verify_symbolic_proof: PFD, cleared identity, pole formulas, and G(x) exact")


def verify_partitions_and_recurrence() -> None:
    # 1. Exact integer DP for [x^k] 1/((1-x)(1-x^2)(1-x^3)(1-x^4)) up to k = 625 = 5^4
    Mmax = 625
    dp = [0] * (Mmax + 1)
    dp[0] = 1
    for part in (1, 2, 3, 4):
        for s in range(part, Mmax + 1):
            dp[s] += dp[s - part]

    # Also cross-check direct partition enumeration at small m = 1, 5, 25, 125 (parts <= 4, or <=4 parts)
    for m_check in (1, 5, 25):
        cnt_le4_parts = 0
        for p1 in range(m_check + 1):
            for p2 in range(p1, m_check - p1 + 1):
                for p3 in range(p2, m_check - p1 - p2 + 1):
                    p4 = m_check - p1 - p2 - p3
                    if p4 >= p3:
                        cnt_le4_parts += 1
        # Wait: partitions into AT MOST 4 parts allow 0s for p1, p2, p3! Yes, p1>=0, p2>=p1, p3>=p2, p4>=p3
        assert cnt_le4_parts == dp[m_check], f"Direct partition enum mismatch at {m_check}"

    def closed_form(n: int) -> int:
        num = 57 + 8 * ((-1) ** n) + 63 * (5**n) + 3 * (5 ** (1 + 2 * n)) + (125**n)
        assert num % 144 == 0
        return num // 144

    for n in range(5):
        assert dp[5**n] == closed_form(n), f"Partition count mismatch at n={n}"

    # 2. Verify series of G(x) and recurrence for n = 0..60
    Nmax = 60
    a = [closed_form(n) for n in range(Nmax + 1)]
    oeis_prefix = [
        1, 6, 185, 15246, 1736385, 212946246, 26516391385, 3312004971246,
        413937039016385, 51740540399346246, 6467527813385891385,
        808439983261977471246, 101054973072475964016385,
        12631871013177766274346246, 1578983861125177809948391385,
    ]
    assert a[:len(oeis_prefix)] == oeis_prefix
    # Check D(x) * A(x) == N(x) mod x^(Nmax+1)
    D_coeffs = [1, -155, 3874, -15470, -3875, 15625]
    N_coeffs = [1, -149, 3129, -5655, -6750]
    for n in range(Nmax + 1):
        conv = sum(D_coeffs[j] * a[n - j] for j in range(min(n, 5) + 1))
        expected = N_coeffs[n] if n < len(N_coeffs) else 0
        assert conv == expected, f"D*A != N at n={n}: {conv} != {expected}"

    for n in range(5, Nmax + 1):
        rhs = 155 * a[n - 1] - 3874 * a[n - 2] + 15470 * a[n - 3] + 3875 * a[n - 4] - 15625 * a[n - 5]
        assert a[n] == rhs

    print(f"PASS verify_partitions_and_recurrence: direct partitions + DP at 5^0..5^4, G(x) & recurrence (0..{Nmax}): a[0..6]={a[:7]}")


def main() -> None:
    verify_symbolic_proof()
    verify_partitions_and_recurrence()
    print("PASS")


if __name__ == "__main__":
    main()
