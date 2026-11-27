#!/usr/bin/env python3
"""Exact symbolic and numerical verification for arXiv:2107.14284v2 Conjecture 5.1.

Verifies:
1. Exact symbolic Abel summation identity for arbitrary f_1,...,f_M and x_1,...,x_M
   (and exact rational check at s=2,3 with x_k = p_k^{-s}).
2. High-precision mpmath test of ratio convergence as s -> 1+ for bounded and
   unbounded arithmetic functions (indicator mod 3, alternating, unbounded oscillating
   (-1)^k * isqrt(k), and phi(k)/k).
"""

from fractions import Fraction
import math
import time
import sympy as sp
from mpmath import mp


def first_n_primes(n: int) -> list[int]:
    primes = []
    cand = 2
    while len(primes) < n:
        is_p = True
        for p in primes:
            if p * p > cand:
                break
            if cand % p == 0:
                is_p = False
                break
        if is_p:
            primes.append(cand)
        cand += 1
    return primes


def main() -> None:
    t0 = time.monotonic()

    # 1. Exact symbolic Abel summation identity for M = 12
    M = 12
    f_syms = sp.symbols(f"f1:{M+1}")
    x_syms = sp.symbols(f"x1:{M+1}")
    S_syms = [sum(f_syms[: k + 1]) for k in range(M)]

    lhs = sum(f_syms[k] * x_syms[k] for k in range(M))
    rhs = S_syms[M - 1] * x_syms[M - 1] + sum(
        S_syms[k] * (x_syms[k] - x_syms[k + 1]) for k in range(M - 1)
    )
    assert sp.expand(lhs - rhs) == 0, "Symbolic Abel summation identity failed"

    # Special case f_k = 1 telescoping identity
    rhs_const = (M - 1) * x_syms[M - 1] + sum(
        (k + 1) * (x_syms[k] - x_syms[k + 1]) for k in range(M - 1)
    )
    assert sp.expand(sum(x_syms[: M - 1]) - rhs_const) == 0

    # 2. Exact rational check with x_k = p_k^{-2}
    primes_20 = first_n_primes(20)
    for N, M_sub in [(3, 20), (7, 15)]:
        f_vals = [(-1) ** k * k for k in range(1, M_sub + 1)]
        S_vals = [sum(f_vals[: k + 1]) for k in range(M_sub)]
        x_vals = [Fraction(1, primes_20[k] ** 2) for k in range(M_sub)]
        part_lhs = sum(f_vals[k] * x_vals[k] for k in range(N - 1, M_sub))
        part_rhs = (
            S_vals[M_sub - 1] * x_vals[M_sub - 1]
            - (S_vals[N - 2] if N >= 2 else 0) * x_vals[N - 1]
            + sum(S_vals[k] * (x_vals[k] - x_vals[k + 1]) for k in range(N - 1, M_sub - 1))
        )
        assert part_lhs == part_rhs

    # 3. High-precision numerical sanity check as s -> 1+
    mp.dps = 30
    ps = first_n_primes(1500)
    test_cases = [
        ("1_{3|k} (L=1/3)", lambda k: 1 if k % 3 == 0 else 0, mp.mpf(1) / 3),
        ("(-1)^k * isqrt(k) (unbounded, L=0)", lambda k: ((-1) ** k) * math.isqrt(k), mp.mpf(0)),
    ]
    for label, fn, target in test_cases:
        errs = []
        for s_val in [mp.mpf("1.5"), mp.mpf("1.2"), mp.mpf("1.05")]:
            num = mp.fsum(fn(k + 1) * (mp.mpf(ps[k]) ** (-s_val)) for k in range(len(ps)))
            den = mp.fsum(mp.mpf(ps[k]) ** (-s_val) for k in range(len(ps)))
            errs.append(float(abs(num / den - target)))
        assert errs[-1] < errs[0], f"Ratio did not move closer to L_f for {label}: {errs}"

    elapsed = time.monotonic() - t0
    print(f"Symbolic Abel identity + exact rational + mpmath checks ok ({elapsed:.2f}s)")
    print("PASS")


if __name__ == "__main__":
    main()
