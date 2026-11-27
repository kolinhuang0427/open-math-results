#!/usr/bin/env python3
"""Exact integer arithmetic verifier for OEIS A177260 Mathar recurrence proof."""

import math
import sys


def series_mul_trunc(p, q, deg):
    res = [0] * (deg + 1)
    for i, a in enumerate(p):
        if a == 0:
            continue
        for j, b in enumerate(q):
            if i + j > deg:
                break
            res[i + j] += a * b
    return res


def series_inv_unit(p, deg):
    assert p[0] == 1
    inv = [0] * (deg + 1)
    inv[0] = 1
    for k in range(1, deg + 1):
        s = sum(p[i] * inv[k - i] for i in range(1, min(k, len(p) - 1) + 1))
        inv[k] = -s
    return inv


def a_double_sum(n):
    tot = 0
    for s in range(n + 1):
        for t in range((n - s) // 4 + 1):
            num = math.factorial(n - 3 * t)
            den = math.factorial(s) * math.factorial(t)
            assert num % den == 0
            q = num // den
            tot += q if ((s + t) % 2 == 0) else -q
    return tot


def main():
    N = 45
    F = [math.factorial(m) for m in range(N + 1)]

    D = [1, 1, 0, 0, 1]  # 1 + x + x^4
    invD = series_inv_unit(D, N)
    u = [0] + invD[:N]

    y_ogf = [0] * (N + 1)
    upow = [0] * (N + 1)
    upow[0] = 1
    for m in range(N + 1):
        term = series_mul_trunc(upow, invD, N)
        fm = F[m]
        for k in range(N + 1):
            y_ogf[k] += fm * term[k]
        if m < N:
            upow = series_mul_trunc(upow, u, N)

    a = [a_double_sum(n) for n in range(N + 1)]
    if a != y_ogf:
        print("FAIL: double sum != OGF")
        sys.exit(1)

    expected = [
        1, 0, 1, 2, 8, 44, 262, 1846, 14789, 133232, 1333112, 14669758,
        176081478, 2289458896, 32056423888, 480890367598, 7694774125983,
        130818028518432, 2354820682603399, 44743035640567412,
        894883797133726171, 18792952193893804872, 413452012727711517437,
    ]
    if a[:len(expected)] != expected:
        print("FAIL: OEIS A177260 DATA mismatch")
        sys.exit(1)

    yp = [n * a[n] for n in range(1, N + 1)]
    for n in range(N + 1):
        t1 = yp[n - 2] if 2 <= n and n - 2 < len(yp) else 0
        t2 = yp[n - 3] if 3 <= n and n - 3 < len(yp) else 0
        t3 = yp[n - 6] if 6 <= n and n - 6 < len(yp) else 0
        val = (
            t1 + t2 + t3
            - a[n]
            + (a[n - 2] if n >= 2 else 0)
            + 2 * (a[n - 4] if n >= 4 else 0)
            + 4 * (a[n - 5] if n >= 5 else 0)
            + 3 * (a[n - 8] if n >= 8 else 0)
            + (1 if n == 0 else (-3 if n == 4 else 0))
        )
        if val != 0:
            print(f"FAIL: ODE failed at x^{n}: {val}")
            sys.exit(1)

    for n in range(8, N + 1):
        rhs = (n - 1) * a[n - 1] + (n - 1) * a[n - 2] + 2 * a[n - 4] + (n - 1) * a[n - 5] + 3 * a[n - 8]
        if a[n] != rhs:
            print(f"FAIL: recurrence failed at n={n}: {a[n]} != {rhs}")
            sys.exit(1)

    print("PASS")


if __name__ == "__main__":
    main()
