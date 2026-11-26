"""Independent exact-arithmetic verifier for OEIS A250917 (Mathar 2020 D-finite recurrence).

Strictly derived from OEIS A250917 (revision 20) and PROOF.md without reading
verify.py beforehand. Checks:
1. Exact algebraic vanishing in Q(x)[S]/(S^2 - (1 - 4x)) for the differential operator L[F](x).
2. Independent power-series expansion of exp(x * C(x)^3) up to n=25, compared against
   all 19 OEIS data terms and the explicit binomial formula on OEIS A250917.
3. Exact recurrence verification for n=3..25 (with a(-1)=0), plus n=1,2 failure check.
"""

from __future__ import annotations

import math
import signal
import sys
import time
import sympy as sp


class TimeoutError(Exception):
    pass


def _alarm_handler(signum, frame):
    raise TimeoutError("Check exceeded built-in time limit")


OEIS_DATA = [
    1, 1, 7, 73, 1033, 18541, 403831, 10351237, 305355793, 10192132153,
    379819484551, 15634219476481, 704566985120857, 34506514429777573,
    1825081888365736183, 103685565729559782781, 6297505655719537293601,
    407233553972252986277617, 27935786938445348562454663,
]


def main() -> int:
    signal.signal(signal.SIGALRM, _alarm_handler)
    signal.alarm(45)
    t0 = time.monotonic()

    x = sp.Symbol("x")
    n = sp.Symbol("n")
    m = sp.Symbol("m")
    delta = 1 - 4 * x

    # Represent elements of Q(x)[S]/(S^2 - (1-4x)) as (A(x), B(x)) for A + B*S.
    def add_alg(u, v):
        return (sp.cancel(u[0] + v[0]), sp.cancel(u[1] + v[1]))

    def mul_alg(u, v):
        a1, b1 = u
        a2, b2 = v
        return (
            sp.cancel(a1 * a2 + b1 * b2 * delta),
            sp.cancel(a1 * b2 + a2 * b1),
        )

    def diff_alg(u):
        # d/dx (A + B*S) = A' + B'*S + B*(-2/(1-4x))*S
        a, b = u
        return (
            sp.cancel(sp.diff(a, x)),
            sp.cancel(sp.diff(b, x) - 2 * b / delta),
        )

    # C(x) = (1 - S) / (2x)
    C_alg = (sp.Rational(1, 2) / x, -sp.Rational(1, 2) / x)
    # Check C = 1 + x*C^2 in A
    C2_alg = mul_alg(C_alg, C_alg)
    rhs_C = add_alg((sp.Integer(1), sp.Integer(0)), mul_alg((x, sp.Integer(0)), C2_alg))
    assert sp.cancel(C_alg[0] - rhs_C[0]) == 0 and sp.cancel(C_alg[1] - rhs_C[1]) == 0

    # g(x) = x * C(x)^3 in A, and g'(x)
    C3_alg = mul_alg(C2_alg, C_alg)
    g_alg = mul_alg((x, sp.Integer(0)), C3_alg)
    gp_alg = diff_alg(g_alg)

    # For F(x) = exp(g(x)), d/dx (u * F) = (u' + u * g') * F.
    def diff_F_coeff(u):
        return add_alg(diff_alg(u), mul_alg(u, gp_alg))

    def theta_F_coeff(u):
        return mul_alg((x, sp.Integer(0)), diff_F_coeff(u))

    # Compute coefficients of F^{(r)}(x) = F_coeff[r] * F(x) for r = 0..5
    F_coeff = [(sp.Integer(1), sp.Integer(0))]
    for _ in range(5):
        F_coeff.append(diff_F_coeff(F_coeff[-1]))

    # Exact polynomials P_r(n) from OEIS A250917 Formula section
    P = [
        sp.Integer(2),
        -11 * n + 20,
        n**3 + 9 * n**2 - 116 * n + 164,
        -4 * n**4 + 35 * n**3 + n**2 - 317 * n + 342,
        -6 * (n - 3) * (6 * n**3 - 50 * n**2 + 147 * n - 176),
        12 * (n - 5) * (2 * n - 9) * (n - 3) * (n - 4),
    ]

    # Apply Q_r(theta) to F^{(5-r)}(x) where Q_r(m) = P_r(m + 5)
    total_R = (sp.Integer(0), sp.Integer(0))
    for r in range(6):
        Qr_poly = sp.Poly(sp.expand(P[r].subs(n, m + 5)), m)
        coeffs = Qr_poly.all_coeffs()[::-1]  # c_0, c_1, ..., c_d
        # Evaluate sum_j c_j * theta^j(F^{(5-r)}) via Horner or accumulation
        cur = F_coeff[5 - r]
        term = (sp.Integer(0), sp.Integer(0))
        for j, cj in enumerate(coeffs):
            if cj != 0:
                term = add_alg(term, (sp.cancel(cj * cur[0]), sp.cancel(cj * cur[1])))
            if j + 1 < len(coeffs):
                cur = theta_F_coeff(cur)
        total_R = add_alg(total_R, term)

    assert total_R[0] == 0 and total_R[1] == 0, f"Nonzero operator residual: {total_R}"
    print(f"Exact differential operator check in Q(x)[S]/(S^2-(1-4x)): R(x,S) = {total_R}")

    # 2. Independent series expansion up to N=25 via exact integer/Rational coefficients
    N = 25
    # Catalan numbers C_k = binom(2k, k) // (k + 1)
    cat = [sp.Rational(math.comb(2 * k, k), k + 1) for k in range(N + 1)]
    # C(x)^3 coefficients: [x^k] C(x)^3
    c2 = [sum(cat[i] * cat[k - i] for i in range(k + 1)) for k in range(N + 1)]
    c3 = [sum(c2[i] * cat[k - i] for i in range(k + 1)) for k in range(N + 1)]
    # g(x) = x * C(x)^3 = sum_{k=1..N} g_k x^k with g_k = c3[k-1]
    g_coeff = [sp.Integer(0)] + [c3[k - 1] for k in range(1, N + 1)]

    # F(x) = exp(g(x)) = sum f_n x^n via n * f_n = sum_{k=1..n} k * g_k * f_{n-k}
    f_coeff = [sp.Integer(0)] * (N + 1)
    f_coeff[0] = sp.Integer(1)
    for k_n in range(1, N + 1):
        f_coeff[k_n] = sum(j * g_coeff[j] * f_coeff[k_n - j] for j in range(1, k_n + 1)) / k_n

    a = [int(f_coeff[k_n] * math.factorial(k_n)) for k_n in range(N + 1)]
    assert a[: len(OEIS_DATA)] == OEIS_DATA, "Mismatch with OEIS A250917 data"

    # Cross-check OEIS binomial formula: a(n) = sum_{k=0..n} n!/k! * C(2n+k-1, n-k) * 3k/(n+2k)
    for k_n in range(1, N + 1):
        val = sum(
            sp.Rational(math.factorial(k_n), math.factorial(k))
            * math.comb(2 * k_n + k - 1, k_n - k)
            * sp.Rational(3 * k, k_n + 2 * k)
            for k in range(k_n + 1)
        )
        assert val == a[k_n], f"Binomial formula mismatch at n={k_n}: {val} vs {a[k_n]}"
    print(f"Series & OEIS formula match all 19 OEIS terms and exact values up to n={N}")

    # 3. Direct check of Mathar's recurrence for n=1..N (with a(-r)=0 for r>0)
    def get_a(idx: int) -> int:
        return a[idx] if idx >= 0 else 0

    def eval_rec(k_n: int) -> int:
        return sum(int(P[r].subs(n, k_n)) * get_a(k_n - r) for r in range(6))

    assert eval_rec(1) != 0 and eval_rec(2) != 0
    for k_n in range(3, N + 1):
        res = eval_rec(k_n)
        assert res == 0, f"Recurrence failed at n={k_n}: {res}"
    print(f"Direct recurrence check: fails at n=1,2 (as stated), == 0 for all n=3..{N}")

    elapsed = time.monotonic() - t0
    print(f"PASS (all checks passed in {elapsed:.3f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
