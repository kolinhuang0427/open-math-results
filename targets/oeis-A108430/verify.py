#!/usr/bin/env python3
"""Exact algebraic and combinatorial verification of Mathar's D-finite recurrence for OEIS A108430."""

import signal
import sys
from math import comb
import sympy as sp
from sympy.polys.matrices import DomainMatrix


def _timeout_handler(signum, frame):
    raise TimeoutError("verify.py exceeded 60s time limit")


signal.signal(signal.SIGALRM, _timeout_handler)
signal.alarm(60)


def count_paths_down_steps(n):
    """Exact DP counting total d-steps across all valid paths from (0,0) to (3n,0)."""
    # State: (y, steps_remaining?) -> track (count_paths, sum_d_steps) by (x, y)
    dp = {(0, 0): (1, 0)}
    for x in range(3 * n):
        nxt = {}
        for (cx, cy), (cnt, sd) in dp.items():
            if cx != x:
                continue
            for dx, dy, is_d in ((2, 1, 0), (1, 2, 0), (1, -1, 1)):
                nx, ny = cx + dx, cy + dy
                if nx <= 3 * n and ny >= 0:
                    oc, od = nxt.get((nx, ny), (0, 0))
                    nxt[(nx, ny)] = (oc + cnt, od + sd + cnt * is_d)
        # merge nxt into dp for future x
        for k, v in nxt.items():
            oc, od = dp.get(k, (0, 0))
            dp[k] = (oc + v[0], od + v[1])
    return dp.get((3 * n, 0), (0, 0))[1]


def main():
    z = sp.Symbol("z")
    K = sp.QQ.frac_field(z)
    inv_z = K.from_sympy(1 / z)
    Kz = K.from_sympy(z)

    def add(p, q):
        return (p[0] + q[0], p[1] + q[1], p[2] + q[2])

    def mul(p, q):
        d = [K.from_sympy(0)] * 5
        for i in range(3):
            for j in range(3):
                d[i + j] += p[i] * q[j]
        for deg in (4, 3):
            c = d[deg]
            if c != 0:
                d[deg - 1] -= c
                d[deg - 2] += c * inv_z
                d[deg - 3] -= c * inv_z
        return (d[0], d[1], d[2])

    def inv_alg(p):
        basis = (
            (K.from_sympy(1), K.from_sympy(0), K.from_sympy(0)),
            (K.from_sympy(0), K.from_sympy(1), K.from_sympy(0)),
            (K.from_sympy(0), K.from_sympy(0), K.from_sympy(1)),
        )
        cols = [mul(p, b) for b in basis]
        dm = DomainMatrix([[cols[j][i] for j in range(3)] for i in range(3)], (3, 3), K)
        rhs = DomainMatrix([[K.from_sympy(1)], [K.from_sympy(0)], [K.from_sympy(0)]], (3, 1), K)
        sol = dm.lu_solve(rhs)
        return (sol[0, 0].element, sol[1, 0].element, sol[2, 0].element)

    G = (K.from_sympy(0), K.from_sympy(1), K.from_sympy(0))
    G2 = mul(G, G)
    G3 = mul(G2, G)
    den_Gp = add(
        add(
            mul((K.from_sympy(3 * z), K.from_sympy(0), K.from_sympy(0)), G2),
            mul((K.from_sympy(2 * z), K.from_sympy(0), K.from_sympy(0)), G),
        ),
        (K.from_sympy(-1), K.from_sympy(0), K.from_sympy(0)),
    )
    Gp = mul(add(G3, G2), inv_alg((-den_Gp[0], -den_Gp[1], -den_Gp[2])))

    def dk(u):
        num = u.numer
        den = u.denom
        return K(num.diff(0) * den - num * den.diff(0)) / K(den * den)

    def diff_alg(p):
        base = (dk(p[0]), dk(p[1]), dk(p[2]))
        dp_dG = (p[1], K.from_sympy(2) * p[2], K.from_sympy(0))
        return add(base, mul(dp_dG, Gp))

    num_A = mul(
        (Kz, K.from_sympy(0), K.from_sympy(0)),
        add(G2, mul((K.from_sympy(2), K.from_sympy(0), K.from_sympy(0)), G3)),
    )
    A = mul(num_A, inv_alg((-den_Gp[0], -den_Gp[1], -den_Gp[2])))

    def theta(p):
        dp = diff_alg(p)
        return (Kz * dp[0], Kz * dp[1], Kz * dp[2])

    def apply_poly(poly_expr, n_sym, alg_el):
        p = sp.Poly(sp.expand(poly_expr), n_sym)
        cur = alg_el
        res = (K.from_sympy(0), K.from_sympy(0), K.from_sympy(0))
        deg = p.degree()
        for d in range(deg + 1):
            c = p.coeff_monomial(n_sym**d)
            if c != 0:
                res = add(res, (K.from_sympy(c) * cur[0], K.from_sympy(c) * cur[1], K.from_sympy(c) * cur[2]))
            if d < deg:
                cur = theta(cur)
        return res

    n = sp.Symbol("n")
    c0 = n * (2 * n + 1) * (23982 * n - 28681)
    c1 = -640736 * n**3 + 1168048 * n**2 - 901220 * n + 247035
    c2 = 1196488 * n**3 - 6448608 * n**2 + 10992587 * n - 5911365
    c3 = 2 * (2 * n - 5) * (28283 * n - 6993) * (n - 3)

    T0 = apply_poly(c0, n, A)
    T1 = apply_poly(c1, n, (Kz * A[0], Kz * A[1], Kz * A[2]))
    T2 = apply_poly(c2, n, (Kz**2 * A[0], Kz**2 * A[1], Kz**2 * A[2]))
    T3 = apply_poly(c3, n, (Kz**3 * A[0], Kz**3 * A[1], Kz**3 * A[2]))

    Phi = add(add(T0, T1), add(T2, T3))
    expected = (K.from_sympy(-49573 * z**2 - 42291 * z), K.from_sympy(0), K.from_sympy(0))
    assert Phi == expected, f"Unexpected Phi: {Phi}"

    # Verify binomial formula vs exact path DP (n=1..7) and OEIS data (n=1..14)
    a_bin = [0] + [
        sum(k * comb(nn, 2 * nn - k) * comb(nn + k, nn - 1) for k in range(nn, 2 * nn + 1)) // nn
        for nn in range(1, 21)
    ]
    for nn in range(1, 8):
        assert count_paths_down_steps(nn) == a_bin[nn], f"Path DP mismatch at n={nn}"

    oeis_prefix = [
        3, 31, 311, 3151, 32299, 334335, 3488239, 36627487, 386618387,
        4098713631, 43611791783, 465496885231, 4981942135611, 53443871159551,
    ]
    assert a_bin[1:1 + len(oeis_prefix)] == oeis_prefix, "OEIS prefix mismatch"

    for nn in range(3, 21):
        lhs = (
            nn * (2 * nn + 1) * (23982 * nn - 28681) * a_bin[nn]
            + (-640736 * nn**3 + 1168048 * nn**2 - 901220 * nn + 247035) * a_bin[nn - 1]
            + (1196488 * nn**3 - 6448608 * nn**2 + 10992587 * nn - 5911365) * a_bin[nn - 2]
            + 2 * (2 * nn - 5) * (28283 * nn - 6993) * (nn - 3) * a_bin[nn - 3]
        )
        assert lhs == 0, f"Recurrence failed at n={nn}"

    print("PASS")
    print(f"Phi(z) in Q(z)[G_1]/(zG_1^3+zG_1^2-G_1+1) = {Phi}")
    print(f"Verified path DP (n=1..7), OEIS data (n=1..14), and recurrence (n=3..20).")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
