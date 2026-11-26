#!/usr/bin/env python3
"""Exact symbolic and series verification of Mathar's D-finite recurrence for OEIS A250917."""

import signal
import sys
from math import comb, factorial
import sympy as sp


def _timeout_handler(signum, frame):
    raise TimeoutError("verify.py exceeded 60s time limit")


signal.signal(signal.SIGALRM, _timeout_handler)
signal.alarm(60)


def main():
    x = sp.Symbol("x")
    K = sp.QQ.frac_field(x)
    Delta = K.from_sympy(1 - 4 * x)
    dDelta = K.from_sympy(-4)

    def add(p, q):
        return (p[0] + q[0], p[1] + q[1])

    def mul(p, q):
        return (p[0] * q[0] + p[1] * q[1] * Delta, p[0] * q[1] + p[1] * q[0])

    def diff_alg(p):
        a, b = p

        def dk(u):
            num = u.numer
            den = u.denom
            return K(num.diff(0) * den - num * den.diff(0)) / K(den * den)

        return (dk(a), dk(b) + b * dDelta / (K.from_sympy(2) * Delta))

    one = K.from_sympy(1)
    two_x = K.from_sympy(2 * x)
    C = (one / two_x, -one / two_x)
    C3 = mul(mul(C, C), C)
    g = mul((K.from_sympy(x), K.from_sympy(0)), C3)
    gp = diff_alg(g)

    Fk = [(K.from_sympy(1), K.from_sympy(0))]
    for _ in range(5):
        p = Fk[-1]
        Fk.append(add(diff_alg(p), mul(p, gp)))

    Kx = (K.from_sympy(x), K.from_sympy(0))

    def apply_theta_poly(clist, G_ratio):
        cur = G_ratio
        res = (K.from_sympy(0), K.from_sympy(0))
        for d, c in enumerate(clist):
            if c != 0:
                res = add(res, mul((K.from_sympy(c), K.from_sympy(0)), cur))
            if d + 1 < len(clist):
                cur = mul(Kx, add(diff_alg(cur), mul(cur, gp)))
        return res

    m = sp.Symbol("m")
    n = m + 5
    polys = [
        sp.Integer(2),
        -11 * n + 20,
        n**3 + 9 * n**2 - 116 * n + 164,
        -4 * n**4 + 35 * n**3 + n**2 - 317 * n + 342,
        -6 * (n - 3) * (6 * n**3 - 50 * n**2 + 147 * n - 176),
        12 * (n - 5) * (2 * n - 9) * (n - 3) * (n - 4),
    ]
    total = (K.from_sympy(0), K.from_sympy(0))
    for r_idx, expr in enumerate(polys):
        p = sp.Poly(sp.expand(expr), m)
        deg = p.degree() if expr != 0 else 0
        clist = [p.coeff_monomial(m**d) for d in range(deg + 1)]
        total = add(total, apply_theta_poly(clist, Fk[5 - r_idx]))

    assert total == (K.from_sympy(0), K.from_sympy(0)), f"Nonzero operator: {total}"

    # Verify exponential series exp(x * C(x)^3) directly using exact Catalan numbers
    N = 20
    Cat = [comb(2 * k, k) // (k + 1) for k in range(N + 1)]
    # [x^k] C(x)^3 = sum_{i+j+l=k} Cat[i]*Cat[j]*Cat[l]
    C3_coeff = [
        sum(Cat[i] * Cat[j] * Cat[k - i - j] for i in range(k + 1) for j in range(k - i + 1))
        for k in range(N + 1)
    ]
    # g(x) = x * C(x)^3 = sum_{k>=1} C3_coeff[k-1] * x^k
    a_egf = [0] * (N + 1)
    a_egf[0] = 1
    for nn in range(1, N + 1):
        a_egf[nn] = sum(
            comb(nn - 1, k - 1) * factorial(k) * C3_coeff[k - 1] * a_egf[nn - k]
            for k in range(1, nn + 1)
        )

    oeis_prefix = [
        1, 1, 7, 73, 1033, 18541, 403831, 10351237, 305355793, 10192132153,
        379819484551, 15634219476481, 704566985120857, 34506514429777573,
        1825081888365736183, 103685565729559782781,
    ]
    assert a_egf[:len(oeis_prefix)] == oeis_prefix, "E.g.f. mismatch with OEIS data"

    for nn in range(5, N + 1):
        lhs = (
            2 * a_egf[nn]
            + (-11 * nn + 20) * a_egf[nn - 1]
            + (nn**3 + 9 * nn**2 - 116 * nn + 164) * a_egf[nn - 2]
            + (-4 * nn**4 + 35 * nn**3 + nn**2 - 317 * nn + 342) * a_egf[nn - 3]
            - 6 * (nn - 3) * (6 * nn**3 - 50 * nn**2 + 147 * nn - 176) * a_egf[nn - 4]
            + 12 * (nn - 5) * (2 * nn - 9) * (nn - 3) * (nn - 4) * a_egf[nn - 5]
        )
        assert lhs == 0, f"Recurrence failed at n={nn}: {lhs}"

    print("PASS")
    print(f"Differential operator in Q(x)[S]/(S^2 - (1-4x)) vanishes identically: {total}")
    print(f"Verified exact integers a(0..{len(oeis_prefix)-1}) and recurrence for n=5..{N}.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
