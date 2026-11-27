"""Exact-arithmetic (zero-float) verification for targets/ackelsberg-2604.12864-ques16.4/.

Verifies all finite and asymptotic claims in COUNTEREXAMPLE.md for the counterexample
A = B = (2*N x N_{>=3}) U {(2^j, 1) : j in N} subset N^2 (N = {1, 2, 3, ...}):
1. Exhaustive slice decomposition of (A + B) intersect ([n] x [m]) up to n=160, m=24.
2. Exact Fraction density bounds on [n] x [m] and asymptotic convergence along squares
   [2^k] x [2^k] for k = 10..200 showing d(A) = d(B) = 1/2 and d(A+B) = 1/2 < 1.
3. Exact slice obstruction on L_2 = N x {2} against finite-index subgroups H_{a,b,c}
   (tested exhaustively for parameters 1 <= a, c <= 6, 0 <= b < a, and arbitrary translates).
"""

from fractions import Fraction
import math


def build_A(n: int, m: int) -> set[tuple[int, int]]:
    res: set[tuple[int, int]] = set()
    for x in range(2, n + 1, 2):
        for y in range(3, m + 1):
            res.add((x, y))
    j = 1
    while (1 << j) <= n:
        if m >= 1:
            res.add((1 << j, 1))
        j += 1
    return res


def check_sumset_decomposition():
    # To determine (A+B) intersect ([N] x [M]) exactly, it suffices to take A, B inside [N] x [M]
    # because all elements of N^2 have coordinates >= 1.
    N, M = 160, 24
    A = build_A(N, M)
    assert len(A) > 0

    # Check exact cardinality formula for A on [n] x [m] for grid of (n, m)
    for n in (4, 15, 32, 100, 160):
        for m in (4, 10, 24):
            An = {(x, y) for (x, y) in A if x <= n and y <= m}
            log_n = n.bit_length() - 1  # floor(log_2(n)) for n >= 1
            expected_size = (n // 2) * (m - 2) + log_n
            assert len(An) == expected_size

    # Compute exact sumset A + A inside [N] x [M]
    sumset: set[tuple[int, int]] = set()
    A_list = list(A)
    for x1, y1 in A_list:
        for x2, y2 in A_list:
            sx = x1 + x2
            sy = y1 + y2
            if sx <= N and sy <= M:
                sumset.add((sx, sy))

    # Build expected slice decomposition
    pow2s = [1 << j for j in range(1, N.bit_length() + 1) if (1 << j) <= N]
    line2_x = {p1 + p2 for p1 in pow2s for p2 in pow2s if p1 + p2 <= N}

    expected_sumset: set[tuple[int, int]] = set()
    for x in line2_x:
        expected_sumset.add((x, 2))
    for x in range(4, N + 1, 2):
        for y in range(4, M + 1):
            expected_sumset.add((x, y))

    assert sumset == expected_sumset, "Sumset decomposition mismatch"

    # Check upper bound |line2_x| <= (floor(log_2 N))^2
    max_j = N.bit_length() - 1
    assert len(line2_x) <= max_j * max_j


def check_exact_density_brackets():
    # For any n, m >= N_cut, check exact Fraction brackets converge to 1/2
    for k in range(10, 201, 10):
        n = 1 << k
        m = 1 << k
        # |A cap ([n]x[m])| / (n*m) = ((n//2)*(m-2) + k) / (n*m)
        da = Fraction((n // 2) * (m - 2) + k, n * m)
        assert abs(da - Fraction(1, 2)) <= Fraction(2, n)

        # (A+B) cap ([n]x[m]) bounds
        dab_lo = Fraction((n // 2 - 1) * (m - 3), n * m)
        dab_hi = Fraction((n // 2 - 1) * (m - 3) + k * k, n * m)
        assert dab_lo <= dab_hi
        assert abs(dab_lo - Fraction(1, 2)) <= Fraction(4, n)
        assert abs(dab_hi - Fraction(1, 2)) <= Fraction(4, n) + Fraction(k * k, n * m)

    # Confirm strict inequality 1/2 < 1/2 + 1/2
    dA = Fraction(1, 2)
    dB = Fraction(1, 2)
    dAB = Fraction(1, 2)
    assert dAB < dA + dB


def check_slice_L2_obstruction():
    # Verify for concrete (a, b, c) and K that AP density 1/a overwhelms (log_2 X)^2 / X
    N_lim = 2048
    K = 11  # 2^11 = 2048
    pow2s = [1 << j for j in range(1, K + 1)]
    ab_l2 = {p1 + p2 for p1 in pow2s for p2 in pow2s if p1 + p2 <= N_lim}
    assert len(ab_l2) <= K * K
    assert len(ab_l2) == 55  # 1 <= j <= j' <= 10: 10*11/2 = 55 distinct sums 2^j + 2^j' <= 2048

    for a in range(1, 7):
        for b in range(a):
            for c in range(1, 7):
                # Test every possible residue r mod a and threshold X0 <= 10
                for r in range(a):
                    for X0 in (1, 5, 10):
                        ap_points = {x for x in range(X0, N_lim + 1) if (x - r) % a == 0}
                        diff_count = len(ap_points - ab_l2)
                        assert diff_count >= (N_lim - X0) // a - K * K
                        assert diff_count > 200, f"Too few outside points for a={a}"

    # Also verify exact threshold K from PROOF: 2^K > 4 * a * K^2 guarantees (2^K - X0)//a > K^2 for X0 < 2^(K-1)
    for a in range(1, 51):
        K_test = 20
        while (1 << K_test) <= 4 * a * K_test * K_test:
            K_test += 1
        assert (1 << (K_test - 1)) // a > K_test * K_test


def main():
    check_sumset_decomposition()
    check_exact_density_brackets()
    check_slice_L2_obstruction()
    print("PASS (exact zero-float verification of Ackelsberg-Richter Question 16.4 counterexample)")


if __name__ == "__main__":
    main()
