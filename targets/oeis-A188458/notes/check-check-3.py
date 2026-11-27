#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A188458 (Sergei N. Gladkovskii, Nov 12 2013).

Zero floating-point operations: pure Python int/Fraction formal power series arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
import math
import sys

OEIS_DATA = [
    1, 1, -3, -11, 57, 361, -2763, -24611, 250737, 2873041, -36581523,
    -512343611, 7828053417, 129570724921, -2309644635483, -44110959165011,
    898621108880097, 19450718635716001, -445777636063460643,
    -10784052561125704811, 274613643571568682777,
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


def fps_compose_nil(f: list[Fraction], g: list[Fraction]) -> list[Fraction]:
    """Compose f(g(x)) mod x^N assuming g[0] == 0."""
    assert g[0] == 0
    N = len(f)
    out = [Fraction(0)] * N
    gp = fps_const(Fraction(1), N)
    for k in range(N):
        if f[k] != 0:
            for i in range(N):
                out[i] += f[k] * gp[i]
        gp = fps_mul(gp, g)
    return out


def main() -> int:
    N = 28
    # exp(t), cosh(2t), sech(t), tanh(t) in Q[[t]] mod t^N
    exp_t = [Fraction(1, math.factorial(n)) for n in range(N)]
    cosh_t = [Fraction(1, math.factorial(n)) if n % 2 == 0 else Fraction(0) for n in range(N)]
    sinh_t = [Fraction(1, math.factorial(n)) if n % 2 == 1 else Fraction(0) for n in range(N)]
    cosh_2t = [Fraction(2**n, math.factorial(n)) if n % 2 == 0 else Fraction(0) for n in range(N)]
    egf = fps_div(exp_t, cosh_2t)
    a = [int(egf[n] * math.factorial(n)) for n in range(N)]
    assert a[: len(OEIS_DATA)] == OEIS_DATA, "Mismatch against OEIS A188458 DATA"

    sech_t = fps_inv(cosh_t)
    tanh_t = fps_mul(sinh_t, sech_t)

    # Lemma 1: F(x) = (1/(1-x)) * S(2x/(1-x))
    S_u = [sech_t[n] * math.factorial(n) for n in range(N)]  # sum E_{2m} u^{2m}
    F_x = [Fraction(val) for val in a]
    one_minus_x = [Fraction(1), Fraction(-1)] + [Fraction(0)] * (N - 2)
    u_of_x = fps_div([Fraction(0), Fraction(2)] + [Fraction(0)] * (N - 2), one_minus_x)
    rhs_lemma1 = fps_div(fps_compose_nil(S_u, u_of_x), one_minus_x)
    assert F_x == rhs_lemma1, "Lemma 1 failed"

    # Lemma 2: J_k(u) = L(tanh^k * sech) and T_k(u)
    N_lap = 26
    J = []
    cur_f = sech_t[:N_lap]
    for k in range(10):
        J.append([cur_f[n] * math.factorial(n) for n in range(N_lap)])
        cur_f = fps_mul(cur_f, tanh_t[:N_lap])

    # T_0(u) = J_0(u), T_k(u) = J_k(u) / (k * u * J_{k-1}(u))
    M_u = 18  # check mod u^M_u (since dividing by u^k drops k degrees)
    T = [J[0][:M_u]]
    for k in range(1, 9):
        # J[k] starts at u^k; shift both num and den by k (or shift J[k] by k and k*J[k-1] by k-1)
        num_shift = J[k][k : k + M_u]
        den_shift = [Fraction(k) * c for c in J[k - 1][k - 1 : k - 1 + M_u]]
        T.append(fps_div(num_shift, den_shift))

    u2 = [Fraction(0), Fraction(0), Fraction(1)] + [Fraction(0)] * (M_u - 3)
    one_u = fps_const(Fraction(1), M_u)
    for k in range(8):
        rhs = fps_inv(fps_add(one_u, fps_mul(fps_const(Fraction((k + 1) ** 2), M_u), fps_mul(u2, T[k + 1]))))
        assert T[k] == rhs, f"Lemma 2 failed at k={k}"

    # Theorem: Gladkovskii CF step in x and finite truncation convergence
    B = fps_mul(one_minus_x, one_minus_x)
    x2 = [Fraction(0), Fraction(0), Fraction(1)] + [Fraction(0)] * (N - 3)
    one_x = fps_const(Fraction(1), N)

    def cf_step_x(k: int, t_next: list[Fraction]) -> list[Fraction]:
        A = fps_mul(fps_const(Fraction(4 * (k + 1) ** 2), N), x2)
        denom = fps_add(A, fps_div(B, t_next))
        return fps_add(one_x, fps_div(A, denom), -1)

    T0_tilde = fps_compose_nil(S_u, u_of_x)
    for K in range(8):
        t_cur = fps_const(Fraction(1), N)
        t_odd = fps_add(one_x, [Fraction(0), Fraction(1)] + [Fraction(0)] * (N - 2))
        for k in range(K, -1, -1):
            t_cur = cf_step_x(k, t_cur)
            t_odd = cf_step_x(k, t_odd)
        conv_1 = fps_div(t_cur, one_minus_x)
        conv_odd = fps_div(t_odd, one_minus_x)
        for deg in range(min(N, 2 * K + 4)):
            assert conv_1[deg] == F_x[deg], f"Seed=1 failed K={K}, deg={deg}"
        for deg in range(min(N, 2 * K + 3)):
            assert conv_odd[deg] == F_x[deg], f"Seed=1+x failed K={K}, deg={deg}"
        assert fps_div(T0_tilde, one_minus_x) == F_x

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
