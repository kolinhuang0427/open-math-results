#!/usr/bin/env python3
"""Exact zero-float verification of the counterexample to Ackelsberg-Richter Question 16.3."""

from fractions import Fraction


def build_counterexample(N0: int, D: int, N1: int):
    N = max(N1, N0 + 1, 10 * D)
    A = {x for x in range(1, N + 1) if x % 2 == 1}
    B = A | set(range(N - D + 1, N + 1))
    return N, A, B


def check_instance(N0: int, D: int, N1: int) -> None:
    eps = Fraction(1, 10)
    alpha = Fraction(4, 9)
    beta = Fraction(4, 9)
    assert alpha + beta < 1

    N, A, B = build_counterexample(N0, D, N1)
    assert N >= N1 and N >= N0 + 1 and N >= 10 * D
    assert A.issubset(range(1, N + 1))
    assert B.issubset(range(1, N + 1))

    # 1. Check uniform prefix density bounds on (N0, N]
    a_pref = 0
    b_pref = 0
    for n in range(1, N + 1):
        if n in A:
            a_pref += 1
        if n in B:
            b_pref += 1
        if n > N0:
            assert Fraction(a_pref, n) >= Fraction(1, 2) > alpha
            assert Fraction(b_pref, n) >= Fraction(1, 2) > beta

    # 2. Check B hits every residue class mod D
    assert {b % D for b in B} == set(range(D))

    # 3. Compute (A + B) \cap [N] directly and verify upper bound
    AB_cap_N = {a + b for a in A for b in B if a + b <= N}
    expected_superset = {x for x in range(2, N + 1, 2)} | {
        x for x in range(max(1, N - D + 2), N + 1) if x % 2 == 1
    }
    assert AB_cap_N.issubset(expected_superset)
    assert len(AB_cap_N) <= N // 2 + D // 2

    lhs = Fraction(len(AB_cap_N), N)
    assert lhs <= Fraction(11, 20)
    assert lhs < alpha + beta - eps
    assert lhs < Fraction(1, 2) + Fraction(1, 2) - eps


def check_general_eps(eps: Fraction, N0: int, D: int, N1: int) -> None:
    eta = (Fraction(1, 2) - eps) / 4
    alpha = Fraction(1, 2) - eta
    beta = alpha
    gap = Fraction(1, 2) - eps - 2 * eta
    thresh = (D + gap - 1) // gap if isinstance(gap, int) else -(-D // gap)
    N = max(N1, N0 + 1, int(thresh))
    A = {x for x in range(1, N + 1) if x % 2 == 1}
    B = A | set(range(N - D + 1, N + 1))
    assert {b % D for b in B} == set(range(D))
    AB_cap_N = {a + b for a in A for b in B if a + b <= N}
    assert Fraction(len(AB_cap_N), N) < alpha + beta - eps


def main() -> None:
    for N0 in (1, 2, 5, 10):
        for D in (1, 2, 3, 5, 10, 25, 60):
            for N1 in (1, 50, 200):
                check_instance(N0, D, N1)
    for eps in (Fraction(1, 10), Fraction(1, 3), Fraction(2, 5), Fraction(9, 20)):
        for D in (1, 3, 10):
            check_general_eps(eps, 1, D, 1)
    print("PASS (exact zero-float verification of Ackelsberg-Richter Question 16.3 counterexample)")


if __name__ == "__main__":
    main()
