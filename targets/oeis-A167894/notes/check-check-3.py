#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A167894 (Sergei N. Gladkovskii, Nov 19 2013).

Zero floating-point operations: pure Python int/Fraction formal power series arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
import math
import sys

OEIS_DATA = [
    1, -1, -1, -3, -13, -71, -461, -3447, -29093, -273343, -2829325,
    -31998903, -392743957, -5201061455, -73943424413, -1123596277863,
    -18176728317413, -311951144828863, -5661698774848621, -108355864447215063,
]


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


def P_series(k: int, N: int) -> list[Fraction]:
    if k == -1:
        return fps_const(Fraction(1), N)
    fk = math.factorial(k)
    return [Fraction(math.factorial(k + m) // fk) for m in range(N)]


def cf_step(k: int, q_next: list[Fraction]) -> list[Fraction]:
    N = len(q_next)
    x = fps_x(N)
    one = fps_const(Fraction(1), N)
    kx = fps_mul(fps_const(Fraction(k), N), x)
    k1x = fps_mul(fps_const(Fraction(k + 1), N), x)
    return fps_add(fps_add(one, kx), fps_div(k1x, q_next), -1)


def main() -> int:
    N = 32
    P0 = P_series(0, N)
    A = fps_inv(P0)
    assert [int(A[i]) for i in range(len(OEIS_DATA))] == OEIS_DATA, "Mismatch against OEIS A167894 DATA"

    # Lemma 1: P_{k-1} == 1 + k*x*P_k mod x^N for k=0..10
    x = fps_x(N)
    one = fps_const(Fraction(1), N)
    for k in range(11):
        Pkm1 = P_series(k - 1, N)
        Pk = P_series(k, N)
        rhs = fps_add(one, fps_mul(fps_const(Fraction(k), N), fps_mul(x, Pk)))
        assert Pkm1 == rhs, f"Lemma 1 failed at k={k}"

    # Theorem: Q(k) = P_{k-1}/P_k satisfies CF step for k=0..10
    for k in range(11):
        Qk = fps_div(P_series(k - 1, N), P_series(k, N))
        Qk1 = fps_div(P_series(k, N), P_series(k + 1, N))
        assert Qk == cf_step(k, Qk1), f"CF step failed at k={k}"

    # Finite truncation convergence: seed=1 matches A mod x^{K+2}; general unit seed 2+x matches A mod x^{K+1}
    for K in range(16):
        q1 = fps_const(Fraction(1), N)
        q2 = fps_add(fps_const(Fraction(2), N), x)
        for k in range(K, -1, -1):
            q1 = cf_step(k, q1)
            q2 = cf_step(k, q2)
        for deg in range(min(N, K + 2)):
            assert q1[deg] == A[deg], f"Seed=1 failed K={K}, deg={deg}"
        for deg in range(min(N, K + 1)):
            assert q2[deg] == A[deg], f"General unit seed failed K={K}, deg={deg}"

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
