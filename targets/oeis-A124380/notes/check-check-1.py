#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/oeis-A124380/.

Built directly from OEIS A124380 rev. 39 and PROOF.md without reading verify.py
or author notes. Zero Python float literals/calls (pure int + mpmath.iv dps=30).
"""
from __future__ import annotations

from math import comb, factorial
from mpmath import iv

iv.dps = 30

# Verbatim OEIS A124380 %S/%T/%U (n=0..29)
OEIS_DATA = [
    1,1,2,4,9,22,57,157,453,1368,4296,13995,47138,163779,585741,2152349,
    8113188,31326760,123748871,499539900,2058542819,8651755865,
    37054078481,161591063250,717032333816,3235298221401,14834735654080,
    69085973044125,326600050947885,1566556077233897,
]


def a_from_ogf(n_max: int) -> list[int]:
    """Compute a(0..n_max) directly from A(x) = sum_{m>=0} x^m prod_{k=0}^m (1 + k*x) in exact ints."""
    a = [0] * (n_max + 1)
    # Build prod_{k=0}^m (1 + k*x) incrementally
    poly = [1]  # for m = 0: prod_{k=0}^0 (1 + k*x) = 1
    for m in range(n_max + 1):
        if m > 0:
            # Multiply poly by (1 + m*x), truncated to degree n_max - m
            lim = n_max - m
            new_poly = [0] * (min(len(poly), lim) + 1)
            for d in range(min(len(poly) - 1, lim) + 1):
                new_poly[d] += poly[d]
            for d in range(min(len(poly) - 1, lim - 1) + 1):
                new_poly[d + 1] += m * poly[d]
            poly = new_poly
        for r, coeff in enumerate(poly):
            if m + r <= n_max:
                a[m + r] += coeff
    return a


def elem_sym_table(m_max: int) -> list[list[int]]:
    """Build e_r(1..m) for 0 <= r <= m <= m_max."""
    tab = [[0] * (m + 1) for m in range(m_max + 1)]
    tab[0][0] = 1
    for m in range(1, m_max + 1):
        tab[m][0] = 1
        for r in range(1, m + 1):
            prev_same = tab[m - 1][r] if r <= m - 1 else 0
            tab[m][r] = tab[m - 1][r - 1] * m + prev_same
    return tab


def main() -> int:
    N_MAX = 160
    a_ogf = a_from_ogf(N_MAX)
    assert a_ogf[:30] == OEIS_DATA, "OGF mismatch vs OEIS A124380 %S/%T/%U"
    print("PASS OGF A(x) exact coefficients match OEIS A124380 (n=0..29)")

    # Check Section 1 identity a(n) = sum_{r=0}^{floor(n/2)} e_r(1..n-r) for n=0..N_MAX
    e_tab = elem_sym_table(N_MAX)
    for n in range(N_MAX + 1):
        rhs = sum(e_tab[n - r][r] for r in range(n // 2 + 1))
        assert rhs == a_ogf[n], f"e_r sum mismatch at n={n}"
    print(f"PASS Section 1 e_r representation for all n=0..{N_MAX}")

    # Check Lemma 1 intermediate and final factorial bounds for n=4..N_MAX
    e_iv = iv.exp(iv.mpf(1))
    for n in range(4, N_MAX + 1):
        k = n // 2
        k_fact = factorial(k)
        assert a_ogf[n] >= k_fact

        # Check termwise bounds for r = 0..k
        T_iv = e_iv * (iv.mpf(2 * k + 1) ** (iv.mpf(3) / 4))
        for r in range(k + 1):
            t = k - r
            m = n - r
            er = e_tab[m][r]
            assert er <= comb(m, r) * factorial(m) // factorial(m - r)
            assert er * factorial(r) * (factorial(2 * t) ** 2) <= factorial(k + 1 + t) ** 2
            if t == 0:
                assert er <= ((2 * k + 1) ** 2) * k_fact
            else:
                # Check (k+1+t)!^2 / ((k-t)! k!) <= (2k+1)^{3t+2}
                lhs_int = (factorial(k + 1 + t) ** 2) // (factorial(k - t) * k_fact)
                assert lhs_int <= (2 * k + 1) ** (3 * t + 2)
                # Check (2t)!^2 > (2t/e)^{4t}
                assert (iv.mpf(factorial(2 * t)) ** 2).a > ((iv.mpf(2 * t) / e_iv) ** (4 * t)).b

        # Final Lemma 1 upper bound in iv
        exp_bound = iv.mpf(3) * T_iv + iv.mpf(2)
        ub_iv = iv.mpf(k + 1) * (iv.mpf(2 * k + 1) ** exp_bound) * iv.mpf(k_fact)
        assert iv.mpf(a_ogf[n]).b <= ub_iv.a, f"Lemma 1 upper bound failed at n={n}"

        # Section 3 log(k!) bounds and log(a(n)) sandwich
        log_k_fact = iv.log(iv.mpf(k_fact))
        int_lo = iv.mpf(k) * iv.log(iv.mpf(k)) - iv.mpf(k) + iv.mpf(1)
        int_hi = iv.mpf(k + 1) * iv.log(iv.mpf(k + 1)) - iv.mpf(k)
        assert int_lo.a <= log_k_fact.a and log_k_fact.b <= int_hi.b

        log_a = iv.log(iv.mpf(a_ogf[n]))
        diff_ub = iv.log(iv.mpf(k + 1)) + exp_bound * iv.log(iv.mpf(2 * k + 1))
        assert log_a.a >= log_k_fact.a and (log_a - log_k_fact).b <= diff_ub.a

    print(f"PASS Lemma 1 (exact & interval bounds) and Section 3 log bounds verified for n=4..{N_MAX}")
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
