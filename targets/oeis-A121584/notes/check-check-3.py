#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A121584 (Mathar 2022 D-finite recurrence).

Written directly from live OEIS A121584 (rev. 4) definitions and PROOF.md
without reading verify.py or author notes. Uses exclusively Python int / Fraction / SymPy ZZ.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
import sys
import sympy as sp


OEIS_DATA = [
    1, 4, 18, 93, 569, 4074, 33336, 306035, 3111771, 34708944, 421407314,
    5533007841, 78125977725, 1180594364966, 19012215609564,
    325058642549919, 5880810783960431, 112243265407073100,
    2254038189505807926,
]


def compute_a_upto(N: int) -> list[int]:
    a = [Fraction(0)] * (N + 1)
    a[1] = Fraction(1)
    a[2] = Fraction(4)
    for n in range(3, N + 1):
        a[n] = (
            Fraction((2 * n - 3) * a[n - 1] - (n - 1) * a[n - 2], n - 2)
            + Fraction(1, 2) * (2 * n**3 - 9 * n**2 + 17 * n - 16) * Fraction(factorial(n - 1), n - 2)
        )
        assert a[n].denominator == 1, f"a({n}) not an integer: {a[n]}"
    return [int(v.numerator) for v in a]


def main() -> int:
    N = 120
    a_vals = compute_a_upto(N)
    assert a_vals[1 : 1 + len(OEIS_DATA)] == OEIS_DATA, "Defining recurrence disagrees with OEIS A121584"
    print(f"[1/3] Defining recurrence matches all {len(OEIS_DATA)} live OEIS A121584 terms (n=1..19).")

    # Symbolic verification of Steps 1-3 in Z[n]
    n = sp.Symbol("n")
    a_syms = sp.symbols("a0 a1 a2 a3 a4 a5")  # a_syms[j] represents a(n - j)

    C = [
        14 * (-n + 1),
        14 * n**2 + 1731 * n - 6995,
        3 * (-577 * n**2 + 480 * n + 7243),
        2 * (2781 * n**2 - 11952 * n + 6004),
        -5987 * n**2 + 36181 * n - 54220,
        2 * (1071 * n - 3433) * (n - 4),
    ]
    d = [
        14 * (-n + 1) * (n - 3),
        14 * n**3 + 1675 * n**2 - 10387 * n + 13948,
        (-1703 * n**2 + 3171 * n + 7574) * (n - 2),
        2 * (1071 * n - 3433) * (n - 2) * (n - 3),
    ]
    f = lambda k: 2 * k**3 - 9 * k**2 + 17 * k - 16

    # Check Step 2: (n-2)(n-3) sum_{j=0}^5 C_j(n) a(n-j) == sum_{j=0}^3 d_j(n) B(n-j)
    M_expr = sum(C[j] * a_syms[j] for j in range(6))
    lhs = sp.expand((n - 2) * (n - 3) * M_expr)

    rhs = sp.Integer(0)
    for j in range(4):
        k = n - j
        B_k = (k - 2) * a_syms[j] - (2 * k - 3) * a_syms[j + 1] + (k - 1) * a_syms[j + 2]
        rhs += d[j] * B_k
    assert sp.expand(lhs - rhs) == 0, "Operator factorization identity failed"

    # Check Step 3: P(n) == 0 identically in Z[n]
    P_expr = (
        d[0] * (n - 1) * (n - 2) * (n - 3) * f(n)
        + d[1] * (n - 2) * (n - 3) * f(n - 1)
        + d[2] * (n - 3) * f(n - 2)
        + d[3] * f(n - 3)
    )
    assert sp.expand(P_expr) == 0, f"P(n) != 0: {sp.expand(P_expr)}"
    print("[2/3] Steps 2 & 3 exact Z[n] operator factorization and P(n) == 0 verified.")

    # Numerical check of Mathar's recurrence for 6 <= n <= N
    for nv in range(6, N + 1):
        val = sum(int(C[j].subs(n, nv)) * a_vals[nv - j] for j in range(6))
        assert val == 0, f"Mathar recurrence failed at n={nv}: {val}"
    print(f"[3/3] Mathar recurrence verified for 6 <= n <= {N}.")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
