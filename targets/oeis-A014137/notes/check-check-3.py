#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A014137 (Sergei N. Gladkovskii, May 14 2013).

Zero floating-point operations: pure Python int/Fraction formal power series arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
import math
import sys

OEIS_DATA = [
    1, 2, 4, 9, 23, 65, 197, 626, 2056, 6918, 23714, 82500, 290512,
    1033412, 3707852, 13402697, 48760367, 178405157, 656043857, 2423307047,
    8987427467, 33453694487, 124936258127, 467995871777, 1757900019101,
    6619846420553, 24987199492705, 94520750408709, 358268702159069,
]


def catalan(n: int) -> int:
    return math.comb(2 * n, n) // (n + 1)


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


def Q_series(k: int, N: int) -> list[Fraction]:
    c2k = catalan(2 * k)
    return [Fraction(catalan(n + 2 * k), c2k) for n in range(N)]


def cf_step(k: int, q_next: list[Fraction]) -> list[Fraction]:
    N = len(q_next)
    one = fps_const(Fraction(1), N)
    x = fps_x(N)
    num_top = fps_mul(fps_const(Fraction(4 * k + 1), N), x)
    k1 = fps_const(Fraction(k + 1), N)
    num_mid = fps_mul(fps_const(Fraction(2 * (k + 1) * (4 * k + 3)), N), x)
    term_2x_4k3 = fps_mul(fps_const(Fraction(2 * (4 * k + 3)), N), x)
    D2 = fps_add(term_2x_4k3, fps_div(fps_const(Fraction(2 * k + 3), N), q_next))
    D1 = fps_add(k1, fps_div(num_mid, D2), -1)
    return fps_add(one, fps_div(num_top, D1))


def main() -> int:
    N = 40
    C = [catalan(n) for n in range(N + 25)]
    a = []
    running = 0
    for j in range(N):
        running += C[j]
        a.append(running)
    assert a[: len(OEIS_DATA)] == OEIS_DATA, "Mismatch against OEIS A014137 DATA"

    # Lemma 1 & Lemma 2 & CF step for k=0..10
    for k in range(11):
        r1 = Fraction(4 * k + 1, k + 1)
        r2 = Fraction(2 * (4 * k + 3), 2 * k + 3)
        assert Fraction(C[2 * k + 1], C[2 * k]) == r1
        assert Fraction(C[2 * k + 2], C[2 * k + 1]) == r2

        Qk = Q_series(k, N)
        Qk1 = Q_series(k + 1, N)
        assert Qk == cf_step(k, Qk1), f"CF step failed at k={k}"

    # Finite truncation convergence & exact error formula Q^{(K)}(0) - Q(0) = C_{2K+2} x^{2K+2} (1 - Q(K+1))
    Q0 = Q_series(0, N)
    one_minus_x = fps_add(fps_const(Fraction(1), N), fps_x(N), -1)
    assert fps_div(Q0, one_minus_x) == [Fraction(v) for v in a]

    for K in range(12):
        q = fps_const(Fraction(1), N)
        for k in range(K, -1, -1):
            q = cf_step(k, q)
        c2k2 = catalan(2 * K + 2)
        QK1 = Q_series(K + 1, N)
        diff_QK1 = fps_add(fps_const(Fraction(1), N), QK1, -1)
        shift = 2 * K + 2
        expected_err = [Fraction(0)] * shift + [Fraction(c2k2) * c for c in diff_QK1[: max(0, N - shift)]]
        assert fps_add(q, Q0, -1) == expected_err, f"Error formula failed at K={K}"
        for deg in range(min(N, 2 * K + 3)):
            assert q[deg] == Q0[deg], f"Truncation K={K} failed at x^{deg}"

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
