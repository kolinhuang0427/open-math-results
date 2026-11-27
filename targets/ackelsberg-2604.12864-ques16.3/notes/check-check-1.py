#!/usr/bin/env python3
"""
Independent exact-arithmetic verifier for targets/ackelsberg-2604.12864-ques16.3/
from the primary source (arXiv:2604.12864v1, Ackelsberg & Richter, Section 16.1,
Question 16.3, InverseProblemDensity_arXiv_v1.tex lines 398-405, 5747-5757).

Zero floating-point arithmetic: uses exact Python int and Fraction only.
"""

from fractions import Fraction


def build_AB(N: int, D: int):
    A = {x for x in range(1, N + 1) if x % 2 == 1}
    tail = set(range(N - D + 1, N + 1))
    B = A | tail
    return A, B


def check_instance(N0: int, D: int, N1: int, eps: Fraction, alpha: Fraction, beta: Fraction, N: int) -> tuple[Fraction, Fraction]:
    assert N >= N1
    assert N > N0
    assert N - D + 1 >= 1
    assert alpha > 0 and beta > 0

    A, B = build_AB(N, D)
    assert A.issubset(set(range(1, N + 1)))
    assert B.issubset(set(range(1, N + 1)))

    # 1. Check min_{N0 < n <= N} |A cap [n]|/n >= alpha and same for B
    for n in range(N0 + 1, N + 1):
        cnt_A = sum(1 for x in A if x <= n)
        cnt_B = sum(1 for x in B if x <= n)
        assert Fraction(cnt_A, n) >= alpha, f"A density failed at n={n}: {cnt_A}/{n} < {alpha}"
        assert Fraction(cnt_B, n) >= beta, f"B density failed at n={n}: {cnt_B}/{n} < {beta}"

    # 2. Check B intersects every residue class mod D
    residues = {b % D for b in B}
    assert len(residues) == D, f"Missing residue classes mod {D}: got {len(residues)}"

    # 3. Brute-force compute |(A+B) cap [N]| / N
    sumset_N = {a + b for a in A for b in B if a + b <= N}
    dens_AB = Fraction(len(sumset_N), N)
    rhs = alpha + beta - eps
    assert dens_AB < rhs, f"Expected violation {dens_AB} < {rhs} failed at N0={N0}, D={D}, N={N}"
    return dens_AB, rhs


def ceil_frac(f: Fraction) -> int:
    return (f.numerator + f.denominator - 1) // f.denominator


def main() -> None:
    # A. Verify primary construction (eps = 1/10, alpha = beta = 4/9, N = max(N1, N0+1, 10*D))
    eps = Fraction(1, 10)
    alpha = Fraction(4, 9)
    beta = Fraction(4, 9)
    cases = 0
    for N0 in (1, 2, 5, 17):
        for D in (1, 2, 3, 7, 10):
            for N1 in (1, 15, 120):
                N = max(N1, N0 + 1, 10 * D)
                dens_AB, rhs = check_instance(N0, D, N1, eps, alpha, beta, N)
                assert dens_AB <= Fraction(11, 20) < rhs
                cases += 1
    print(f"PASS primary_construction: {cases} tuples (N0,D,N1) tested; all <= 11/20 < 71/90")

    # B. Verify patched L70 generalization for 0 < eps < 1/2:
    # alpha = beta = 1/2 - eta with 0 < eta < (1/2 - eps)/2,
    # D0 = ceil(D), N >= max(N1, N0+1, ceil(D0 / (1/2 - eps - 2*eta)))
    gen_cases = 0
    for eps_g in (Fraction(1, 10), Fraction(1, 3), Fraction(2, 5), Fraction(9, 20)):
        eta_g = (Fraction(1, 2) - eps_g) / 4
        assert Fraction(0) < eta_g < (Fraction(1, 2) - eps_g) / 2
        alpha_g = Fraction(1, 2) - eta_g
        denom_gap = Fraction(1, 2) - eps_g - 2 * eta_g
        for D0 in (1, 2, 5, 10):
            for N0 in (1, 4):
                for N1 in (1, 30):
                    N_g = max(N1, N0 + 1, ceil_frac(Fraction(D0) / denom_gap))
                    dens_AB_g, rhs_g = check_instance(N0, D0, N1, eps_g, alpha_g, alpha_g, N_g)
                    assert dens_AB_g <= Fraction(1, 2) + Fraction(D0, 2 * N_g) < rhs_g
                    gen_cases += 1
    print(f"PASS general_eps_L70: {gen_cases} instances across eps in {{1/10, 1/3, 2/5, 9/20}} refuted")
    print("PASS")


if __name__ == "__main__":
    main()
