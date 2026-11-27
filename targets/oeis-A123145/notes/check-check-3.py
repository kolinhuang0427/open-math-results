#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A123145 (Sergei N. Gladkovskii, Nov 26 2012).

Zero floating-point operations: pure Python int/Fraction formal power series arithmetic mod x^N.
"""

from __future__ import annotations

from fractions import Fraction
import math
import sys

OEIS_DATA = [
    1,
    2,
    6,
    24,
    24,
    144,
    1008,
    8064,
    8064,
    80640,
    887040,
    10644480,
    10644480,
    149022720,
    2235340800,
    35765452800,
    35765452800,
    643778150400,
    12231784857600,
    244635697152000,
    244635697152000,
    5381985337344000,
    123785662758912000,
    2970855906213888000,
]


def a_seq(max_n: int) -> list[int]:
    a = [0] * (max_n + 1)
    a[1] = 1
    for n in range(2, max_n + 1):
        a[n] = a[n - 1] if (n % 4 == 1) else n * a[n - 1]
    return a


def fps_add(p: list[Fraction], q: list[Fraction], sign: int = 1) -> list[Fraction]:
    return [p[i] + sign * q[i] for i in range(len(p))]


def fps_mul(p: list[Fraction], q: list[Fraction]) -> list[Fraction]:
    N = len(p)
    out = [Fraction(0)] * N
    for i in range(N):
        if p[i] == 0:
            continue
        for j in range(N - i):
            out[i + j] += p[i] * q[j]
    return out


def fps_inv(q: list[Fraction]) -> list[Fraction]:
    """Invert formal power series q with q[0] != 0 modulo x^len(q)."""
    N = len(q)
    assert q[0] != 0
    inv = [Fraction(0)] * N
    inv[0] = Fraction(1) / q[0]
    for i in range(1, N):
        s = sum((q[j] * inv[i - j] for j in range(1, i + 1)), Fraction(0))
        inv[i] = -s / q[0]
    return inv


def fps_div(p: list[Fraction], q: list[Fraction]) -> list[Fraction]:
    return fps_mul(p, fps_inv(q))


def fps_const(c: Fraction, N: int) -> list[Fraction]:
    out = [Fraction(0)] * N
    out[0] = c
    return out


def fps_x(N: int) -> list[Fraction]:
    out = [Fraction(0)] * N
    if N > 1:
        out[1] = Fraction(1)
    return out


def G_series(k: int, N: int) -> list[Fraction]:
    out = [Fraction(0)] * N
    out[0] = Fraction(1)
    prod = 1
    m = 0
    while 4 * m + 1 < N:
        prod *= 4 * k + 4 * m + 1
        coeff = Fraction(1, prod)
        for r in range(1, 5):
            idx = 4 * m + r
            if idx < N:
                out[idx] = coeff
        m += 1
    return out


def cf_step(k: int, g_next: list[Fraction]) -> list[Fraction]:
    """Evaluate 1 + x / (4k+1 - x(4k+1) / (1+x - x / (1+x - x / (x + 1/g_next)))) in Q[[x]] mod x^N."""
    N = len(g_next)
    one = fps_const(Fraction(1), N)
    x = fps_x(N)
    one_plus_x = fps_add(one, x)
    c = Fraction(4 * k + 1)
    c_fps = fps_const(c, N)
    cx = fps_mul(c_fps, x)

    D4 = fps_add(x, fps_inv(g_next))
    D3 = fps_add(one_plus_x, fps_div(x, D4), -1)
    D2 = fps_add(one_plus_x, fps_div(x, D3), -1)
    D1 = fps_add(c_fps, fps_div(cx, D2), -1)
    return fps_add(one, fps_div(x, D1))


def main() -> int:
    max_n = 44
    a = a_seq(max_n)
    assert a[1 : 1 + len(OEIS_DATA)] == OEIS_DATA, "Mismatch against OEIS A123145 DATA"

    # Lemma 1: a(4m+r)/(4m+r)! == 1 / prod_{j=0..m} (4j+1)
    for m in range(11):
        prod = 1
        for j in range(m + 1):
            prod *= 4 * j + 1
        expected = Fraction(1, prod)
        for r in range(1, 5):
            n = 4 * m + r
            assert Fraction(a[n], math.factorial(n)) == expected, f"Lemma 1 failed at n={n}"

    N = 42
    G0_exact = G_series(0, N)
    G0_from_a = [Fraction(1)] + [Fraction(a[n], math.factorial(n)) for n in range(1, N)]
    assert G0_exact == G0_from_a, "G(0) series mismatch against a(n)/n!"

    # Check d/dx G(0) == sum_{n>=0} a(n+1) x^n / n!
    dG0 = [Fraction(n) * G0_exact[n] for n in range(1, N)]
    E_expected = [Fraction(a[n + 1], math.factorial(n)) for n in range(N - 1)]
    assert dG0 == E_expected, "E(x) derivative mismatch"

    # Lemma 2 & Theorem: exact 5-step CF identity G(k) == cf_step(k, G(k+1)) mod x^N for k=0..5
    for k in range(6):
        Gk = G_series(k, N)
        Gk1 = G_series(k + 1, N)
        assert Gk == cf_step(k, Gk1), f"5-step CF identity failed at k={k}"

    # Finite truncation convergence check: depth K seeded with 1 matches G(0) mod x^{4K+5}
    for K in range(9):
        g = fps_const(Fraction(1), N)
        for k in range(K, -1, -1):
            g = cf_step(k, g)
        # Exact discrepancy: x^{4(K+1)} / prod_{j=0..K}(4j+1) * (1 - G(K+1))
        prod = 1
        for j in range(K + 1):
            prod *= 4 * j + 1
        GK1 = G_series(K + 1, N)
        diff_GK1 = fps_add(fps_const(Fraction(1), N), GK1, -1)
        shift = 4 * (K + 1)
        expected_err = [Fraction(0)] * shift + [c / prod for c in diff_GK1[: max(0, N - shift)]]
        assert fps_add(g, G0_exact, -1) == expected_err, f"Error formula mismatch at K={K}"
        for deg in range(min(N, 4 * K + 5)):
            assert g[deg] == G0_exact[deg], f"Truncation K={K} failed at x^{deg}"

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
