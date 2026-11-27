#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A177260 (Mathar 2022 D-finite recurrence).

Written directly from primary-source OEIS A177260 (rev. 27) definitions and PROOF.md
without inspecting verify.py or author notes. Uses exclusively Python int / Fraction.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
import sys


OEIS_DATA = [
    1, 0, 1, 2, 8, 44, 262, 1846, 14789, 133232, 1333112, 14669758,
    176081478, 2289458896, 32056423888, 480890367598, 7694774125983,
    130818028518432, 2354820682603399, 44743035640567412,
    894883797133726171, 18792952193893804872, 413452012727711517437,
]


def a_double_sum(n: int) -> int:
    total = Fraction(0)
    for s in range(n + 1):
        for t in range((n - s) // 4 + 1):
            sgn = -1 if ((s + t) & 1) else 1
            total += Fraction(sgn * factorial(n - 3 * t), factorial(s) * factorial(t))
    assert total.denominator == 1
    return int(total.numerator)


def poly_mul_trunc(p: list[int], q: list[int], deg: int) -> list[int]:
    out = [0] * (deg + 1)
    for i, pi in enumerate(p):
        if pi == 0 or i > deg:
            continue
        for j, qj in enumerate(q):
            if i + j > deg:
                break
            out[i + j] += pi * qj
    return out


def main() -> int:
    N = 90
    a_vals = [a_double_sum(n) for n in range(N + 1)]
    assert a_vals[: len(OEIS_DATA)] == OEIS_DATA, "Double sum disagrees with live OEIS A177260 data"

    # Step 1: Verify y(x) == sum_{m=0}^N m! x^m / (1 + x + x^4)^{m+1} mod x^{N+1}
    # Compute 1 / (1 + x + x^4) mod x^{N+1}
    D = [1, 1, 0, 0, 1] + [0] * (N - 4)
    inv_D = [0] * (N + 1)
    inv_D[0] = 1
    for m in range(1, N + 1):
        inv_D[m] = -(inv_D[m - 1] + (inv_D[m - 4] if m >= 4 else 0))

    # u(x) = x / (1 + x + x^4)
    u = [0] + inv_D[:N]
    # y_ogf = inv_D * sum_{m=0}^N m! u^m
    F_u = [1] + [0] * N
    u_pow = [1] + [0] * N
    for m in range(1, N + 1):
        u_pow = poly_mul_trunc(u_pow, u, N)
        fm = factorial(m)
        for k in range(m, N + 1):
            F_u[k] += fm * u_pow[k]
    y_ogf = poly_mul_trunc(inv_D, F_u, N)
    assert y_ogf == a_vals, "Step 1 OGF identity mismatch"

    # Step 2: Verify ODE x^2(1+x+x^4)y' + (-1+x^2+2x^4+4x^5+3x^8)y + (1-3x^4) == 0 mod x^N
    yp = [m * a_vals[m] for m in range(1, N + 1)] + [0]
    c_yp = [0, 0, 1, 1, 0, 0, 1] + [0] * (N - 6)
    c_y = [-1, 0, 1, 0, 2, 4, 0, 0, 3] + [0] * (N - 8)
    inhom = [1, 0, 0, 0, -3] + [0] * (N - 4)
    t1 = poly_mul_trunc(c_yp, yp, N - 1)
    t2 = poly_mul_trunc(c_y, a_vals, N - 1)
    for m in range(N):
        assert t1[m] + t2[m] + inhom[m] == 0, f"Step 2 ODE failed at x^{m}"

    # Step 3: Verify Mathar's recurrence for 8 <= n <= N
    for n in range(8, N + 1):
        rhs = (
            (n - 1) * a_vals[n - 1]
            + (n - 1) * a_vals[n - 2]
            + 2 * a_vals[n - 4]
            + (n - 1) * a_vals[n - 5]
            + 3 * a_vals[n - 8]
        )
        assert a_vals[n] == rhs, f"Recurrence failed at n={n}"

    print(f"[1/2] Double sum matches all {len(OEIS_DATA)} live OEIS A177260 terms and Step 1 OGF up to x^{N}.")
    print(f"[2/2] Step 2 ODE and Step 3 Mathar recurrence verified for 8 <= n <= {N}.")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
