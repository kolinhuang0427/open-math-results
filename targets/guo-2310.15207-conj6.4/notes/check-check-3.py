#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for Guo (arXiv:2310.15207v1) Conjectures 6.4 and 6.3.

Written directly from qLucas.tex (arXiv:2310.15207v1) and PROOF.md.
Uses pure SymPy exact ZZ[q]/QQ[q] polynomial and cyclotomic modular arithmetic (zero floats).
"""

from __future__ import annotations

import sys
import sympy as sp

q = sp.Symbol("q")


def q_poch(a_pow: int, step_pow: int, m: int, mod_poly: sp.Poly | None = None) -> sp.Poly:
    """Compute (q^{a_pow}; q^{step_pow})_m as an exact Poly in ZZ[q], optionally reduced mod mod_poly."""
    res = sp.Poly(1, q, domain="ZZ")
    for k in range(m):
        factor = sp.Poly(1 - q ** (a_pow + k * step_pow), q, domain="ZZ")
        res = res * factor
        if mod_poly is not None:
            res = sp.rem(res, mod_poly)
    return res


def R4_num_den(n: int, r: int, mod_poly: sp.Poly) -> tuple[sp.Poly, sp.Poly]:
    m1 = (n**r - 1) // 4
    m2 = (n ** (r - 1) - 1) // 4
    num = sp.rem(q_poch(1, 2, m1, mod_poly) * q_poch(2 * n, 2 * n, m2, mod_poly), mod_poly)
    den = sp.rem(q_poch(2, 2, m1, mod_poly) * q_poch(n, 2 * n, m2, mod_poly), mod_poly)
    return num, den


def R3_num_den(n: int, r: int, mod_poly: sp.Poly) -> tuple[sp.Poly, sp.Poly]:
    m1 = (n**r - 1) // 2
    m2 = (n ** (r - 1) - 1) // 2
    q_brack_n = sp.Poly(sum(q**j for j in range(n)), q, domain="ZZ")  # [n] = (1-q^n)/(1-q)
    num = sp.rem(q_brack_n * q_poch(3, 4, m1, mod_poly) * q_poch(5 * n, 4 * n, m2, mod_poly), mod_poly)
    den = sp.rem(q_poch(5, 4, m1, mod_poly) * q_poch(3 * n, 4 * n, m2, mod_poly), mod_poly)
    # Remove any common (1 - q^N) factor before modular inverse check
    return num, den


def check_rational_congruence_mod_poly(
    num1: sp.Poly, den1: sp.Poly, num2: sp.Poly, den2: sp.Poly, phi_N: sp.Poly, mod2: sp.Poly
) -> None:
    """Verify num1/den1 === num2/den2 (mod mod2) after cancelling shared cyclotomic factors with phi_N."""
    # Factor out exact shared GCDs in ZZ[q]
    g1 = sp.gcd(num1, den1)
    num1c, den1c = sp.quo(num1, g1), sp.quo(den1, g1)
    g2 = sp.gcd(num2, den2)
    num2c, den2c = sp.quo(num2, g2), sp.quo(den2, g2)
    # Verify denominators are coprime to phi_N (hence invertible mod phi_N^2)
    assert sp.gcd(den1c, phi_N).degree() == 0, "den1 shares factor with Phi_N"
    assert sp.gcd(den2c, phi_N).degree() == 0, "den2 shares factor with Phi_N"
    diff = sp.rem(num1c * den2c - num2c * den1c, mod2)
    assert diff.is_zero, f"Congruence failed: remainder {diff}"


def main() -> int:
    # 1. Verify Lemma Eq. (2): q^a/(1-q^a) + q^{N-a}/(1-q^{N-a}) + 1 == 0 mod Phi_N(q)
    for N in [5, 9, 13, 25]:
        phi_N = sp.Poly(sp.cyclotomic_poly(N, q), q, domain="ZZ")
        for a in range(1, N):
            # (q^a*(1-q^{N-a}) + q^{N-a}*(1-q^a) + (1-q^a)*(1-q^{N-a})) mod Phi_N == 0
            lhs = sp.Poly(
                q**a * (1 - q ** (N - a)) + q ** (N - a) * (1 - q**a) + (1 - q**a) * (1 - q ** (N - a)),
                q,
                domain="ZZ",
            )
            assert sp.rem(lhs, phi_N).is_zero, f"Eq (2) failed at N={N}, a={a}"

    # 2. Verify Delta Q_4(a) (Eq 4), Delta Q_3(a) (Eq 6), and pairing sums across n, s
    for n in [5, 9, 13, 17, 21, 25]:
        assert n % 4 == 1
        for s in [1, 2]:
            N = n**s
            # Delta Q_4(a)
            qnum = {}
            for i in range(N):
                val = (N + 1) // 2 + 2 * i
                qnum[val % N] = val // N
            qden = {}
            for i in range(N):
                val = (N + 3) // 2 + 2 * i
                qden[val % N] = val // N
            for a in range(1, N):
                dq4 = qnum[a] - qden[a]
                expected = ((-1) ** (a - 1)) if a <= (N - 1) // 2 else ((-1) ** a)
                assert dq4 == expected, f"Delta Q4 mismatch N={N}, a={a}"
            assert sum(((-1) ** (a - 1)) for a in range(1, (N - 1) // 2 + 1) if a % n != 0) == 0

            # Delta Q_3(a)
            q1 = {}
            for i in range(N):
                val = 4 * i + 1
                q1[val % N] = val // N
            q2 = {}
            for i in range(N):
                val = 4 * i + 3
                q2[val % N] = val // N
            for a in range(1, N):
                dq3 = q1[a] - q2[a]
                expected = -2 if (a % 4 in (0, 1)) else 2
                assert dq3 == expected, f"Delta Q3 mismatch N={N}, a={a}"
            assert sum((q1[a] - q2[a]) for a in range(1, (N - 1) // 2 + 1) if a % n != 0) == 0

    # 3. Verify Step 2.2 / 3.2 exact rational function cancellation T4 (Eq 3) and T3 (Eq 5)
    for n, r in [(5, 2), (9, 2), (13, 2)]:
        k0, k1 = (n ** (r - 1) - 1) // 4, (n**r - 1) // 4
        j0 = (n ** (r - 2) - 1) // 4
        # Compare exact factor-exponent sets after removing n-multiples matching j0..k0-1:
        num_exps4 = [2 * k + 1 for k in range(k0, k1)] + [n * (2 * j + 2) for j in range(j0, k0)]
        den_exps4 = [2 * k + 2 for k in range(k0, k1)] + [n * (2 * j + 1) for j in range(j0, k0)]
        from collections import Counter
        c_net4 = Counter(num_exps4)
        c_net4.subtract(Counter(den_exps4))
        rhs_num4 = sorted([2 * k + 1 for k in range(k0, k1) if (2 * k + 1) % n != 0])
        rhs_den4 = sorted([2 * k + 2 for k in range(k0, k1) if (2 * k + 2) % n != 0])
        assert sorted([e for e, c in c_net4.items() for _ in range(max(0, c))]) == rhs_num4
        assert sorted([e for e, c in c_net4.items() for _ in range(max(0, -c))]) == rhs_den4

        v0, v1 = (n ** (r - 1) - 1) // 2, (n**r - 1) // 2
        w0 = (n ** (r - 2) - 1) // 2
        num_exps3 = [4 * k + 3 for k in range(v0, v1)] + [n * (4 * j + 5) for j in range(w0, v0)]
        den_exps3 = [4 * k + 5 for k in range(v0, v1)] + [n * (4 * j + 3) for j in range(w0, v0)]
        c_net3 = Counter(num_exps3)
        c_net3.subtract(Counter(den_exps3))
        rhs_num3 = sorted([4 * k + 3 for k in range(v0, v1) if (4 * k + 3) % n != 0])
        rhs_den3 = sorted([4 * k + 5 for k in range(v0, v1) if (4 * k + 5) % n != 0])
        assert sorted([e for e, c in c_net3.items() for _ in range(max(0, c))]) == rhs_num3
        assert sorted([e for e, c in c_net3.items() for _ in range(max(0, -c))]) == rhs_den3

    # 4. Direct verification of Conjectures 6.4 and 6.3 mod Phi_{n^s}(q)^2
    # Cancel matching (1 - q^m) exponents BEFORE polynomial multiplication mod Phi_N^2,
    # and keep exact multiplicity for any remaining N-divisible factor in numerator/denominator!
    from collections import Counter
    for n, r, s in [(5, 2, 1), (5, 3, 1), (5, 3, 2), (9, 2, 1), (13, 2, 1)]:
        N = n**s
        phi_N = sp.Poly(sp.cyclotomic_poly(N, q), q, domain="ZZ")
        mod2 = phi_N * phi_N

        def eval_ratio_mod2(num_exps: list[int], den_exps: list[int], extra_num: sp.Poly | None = None) -> tuple[sp.Poly, sp.Poly]:
            cnt = Counter(num_exps)
            cnt.subtract(Counter(den_exps))
            rem_num = [e for e, c in cnt.items() for _ in range(max(0, c))]
            rem_den = [e for e, c in cnt.items() for _ in range(max(0, -c))]
            mult = sum(1 for e in rem_num + rem_den if e % N == 0) + 3
            mod_k = phi_N ** mult
            nu = extra_num if extra_num is not None else sp.Poly(1, q, domain="ZZ")
            de = sp.Poly(1, q, domain="ZZ")
            for e in rem_num:
                nu = sp.rem(nu * sp.Poly(1 - q**e, q, domain="ZZ"), mod_k)
            for e in rem_den:
                de = sp.rem(de * sp.Poly(1 - q**e, q, domain="ZZ"), mod_k)
            while sp.rem(nu, phi_N).is_zero and sp.rem(de, phi_N).is_zero:
                nu = sp.quo(nu, phi_N)
                de = sp.quo(de, phi_N)
            assert sp.gcd(de, phi_N).degree() == 0, f"Denominator shares factor with Phi_{N}"
            return sp.rem(nu, mod2), sp.rem(de, mod2)

        def r4_exps(r_val: int):
            m1, m2 = (n**r_val - 1) // 4, (n ** (r_val - 1) - 1) // 4
            return (
                [1 + 2 * k for k in range(m1)] + [2 * n * (k + 1) for k in range(m2)],
                [2 * (k + 1) for k in range(m1)] + [n * (1 + 2 * k) for k in range(m2)],
            )

        n4r, d4r = eval_ratio_mod2(*r4_exps(r))
        n4s, d4s = eval_ratio_mod2(*r4_exps(s))
        assert sp.rem(n4r * d4s - n4s * d4r, mod2).is_zero, f"Conj 6.4 failed at {(n, r, s)}"

        q_brack_n = sp.Poly(sum(q**j for j in range(n)), q, domain="ZZ")
        def r3_exps(r_val: int):
            m1, m2 = (n**r_val - 1) // 2, (n ** (r_val - 1) - 1) // 2
            return (
                [3 + 4 * k for k in range(m1)] + [5 * n + 4 * n * k for k in range(m2)],
                [5 + 4 * k for k in range(m1)] + [3 * n + 4 * n * k for k in range(m2)],
            )

        n3r, d3r = eval_ratio_mod2(*r3_exps(r), extra_num=q_brack_n)
        n3s, d3s = eval_ratio_mod2(*r3_exps(s), extra_num=q_brack_n)
        assert sp.rem(n3r * d3s - n3s * d3r, mod2).is_zero, f"Conj 6.3 failed at {(n, r, s)}"

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
