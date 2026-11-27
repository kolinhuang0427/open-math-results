#!/usr/bin/env python3
"""
Independent exact-arithmetic verifier for targets/ackelsberg-2604.12864-ques16.4/
from the primary source (arXiv:2604.12864v1, Ackelsberg & Richter, Section 16.1,
Question 16.4, InverseProblemDensity_arXiv_v1.tex lines 398-405, 5760-5777).

Zero floating-point arithmetic: all calculations use exact Python int and Fraction.
"""

from fractions import Fraction


def in_A(x: int, y: int) -> bool:
    """Membership predicate for A = B = (2*N x N_{>=3}) U {(2^j, 1) : j in N}, N = {1,2,...}."""
    if x < 1 or y < 1:
        return False
    if y >= 3:
        return x % 2 == 0
    if y == 1:
        # x = 2^j with j >= 1  <=>  x >= 2 and x is a power of 2
        return x >= 2 and (x & (x - 1)) == 0
    return False


def is_pow2_pos(t: int) -> bool:
    return t >= 2 and (t & (t - 1)) == 0


def exact_slice_formula_A_plus_B(x: int, y: int) -> bool:
    """Closed-form membership for A + B."""
    if x < 1 or y < 1:
        return False
    if y in (1, 3):
        return False
    if y == 2:
        # 2^j + 2^{j'} with j, j' >= 1
        j = 1
        while (1 << j) < x:
            rem = x - (1 << j)
            if is_pow2_pos(rem):
                return True
            j += 1
        return False
    # y >= 4: 2*N_{>=2} = {4, 6, 8, ...}
    return x >= 4 and (x % 2 == 0)


def check_sumset_and_slices() -> None:
    # Brute-force verify A+B on [1..Xmax] x [1..Ymax]
    # Note: min element in A has x>=2, y>=1; if (x,y) in A+B then components <= x and <= y
    Xmax, Ymax = 150, 40
    pts_A = [(x, y) for x in range(1, Xmax + 1) for y in range(1, Ymax + 1) if in_A(x, y)]
    assert len(pts_A) > 0, "A must be non-empty"

    sumset = set()
    for x1, y1 in pts_A:
        for x2, y2 in pts_A:
            sx, sy = x1 + x2, y1 + y2
            if sx <= Xmax and sy <= Ymax:
                sumset.add((sx, sy))

    for x in range(1, Xmax + 1):
        for y in range(1, Ymax + 1):
            expected = exact_slice_formula_A_plus_B(x, y)
            actual = (x, y) in sumset
            if expected != actual:
                raise AssertionError(
                    f"Slice mismatch at ({x},{y}): brute={actual}, formula={expected}"
                )

    # Check A subset of N^2 and sumset A+B subset of N^2
    for x, y in sumset:
        assert x >= 1 and y >= 1
    print(f"PASS check_sumset_and_slices: exact match on [1..{Xmax}]x[1..{Ymax}] ({len(sumset)} pts)")


def check_exact_density_bounds() -> None:
    """
    Verify exact counting formulas on [n] x [m] and explicit rational upper/lower bounds
    for n, m in {4..64}, plus asymptotic sandwich at large N using exact Fraction.
    """
    for n in range(4, 65):
        b = n.bit_length() - 1  # |{2^j <= n : j >= 1}|
        # Precompute |(A+B)_2 cap [n]|
        s2_n = sum(1 for x in range(1, n + 1) if exact_slice_formula_A_plus_B(x, 2))
        assert s2_n <= b * b, f"s2({n})={s2_n} > b^2={b*b}"
        assert s2_n <= (b - 1) * (b - 1) + 1 or n < 4  # actually <= b^2 (in fact <= b*(b+1)//2)

        for m in range(4, 65):
            # Exact count |A cap ([n] x [m])|
            brute_A = sum(1 for x in range(1, n + 1) for y in range(1, m + 1) if in_A(x, y))
            formula_A = (n // 2) * (m - 2) + b
            assert brute_A == formula_A, f"A count mismatch at ({n},{m}): {brute_A} != {formula_A}"

            # Exact rational density bounds for A
            dens_A = Fraction(brute_A, n * m)
            lb_A = Fraction(1, 2) - Fraction(1, m) - Fraction(1, 2 * n)
            ub_A = Fraction(1, 2) + Fraction(b, n * m)
            assert lb_A <= dens_A <= ub_A, f"A density bound fail at ({n},{m})"

            # Exact count |(A+B) cap ([n] x [m])|
            brute_AB = sum(
                1 for x in range(1, n + 1) for y in range(1, m + 1) if exact_slice_formula_A_plus_B(x, y)
            )
            formula_AB = (m - 3) * (n // 2 - 1) + s2_n
            assert brute_AB == formula_AB, f"AB count mismatch at ({n},{m}): {brute_AB} != {formula_AB}"

            # Exact rational density bounds for A+B:
            # LB: (m-3)*(n-3)/(2*n*m) = 1/2 - 3/(2n) - 3/(2m) + 9/(2nm) >= 1/2 - 3/(2n) - 3/(2m)
            # UB: (m-3)*(n/2 - 1)/(nm) + b^2/(nm) <= 1/2 + b^2/(nm)
            dens_AB = Fraction(brute_AB, n * m)
            lb_AB = Fraction(1, 2) - Fraction(3, 2 * n) - Fraction(3, 2 * m)
            ub_AB = Fraction(1, 2) + Fraction(b * b, n * m)
            assert lb_AB <= dens_AB <= ub_AB, f"AB density bound fail at ({n},{m})"

    # Check explicit numerical separation at large scale N = 2^20:
    # For ALL n, m >= N = 2^20:
    #   dens_A(n, m) >= 1/2 - 3/(2*N)
    #   dens_AB(n, m) <= 1/2 + (floor(log2 n))^2 / (n * m)
    # Note: for n >= N >= 16 and m >= N, (log2 n)^2 / n is strictly decreasing for n >= 8,
    # Wait: let's check integer k -> k^2 / 2^k decreasing for k >= 3: (k+1)^2 / 2 <= k^2 for k >= 3?
    # For k=3: 16/8=2 vs 9/4=2.25; for k>=4: (k+1)^2 / k^2 <= 25/16 < 2.
    # For n in [2^k, 2^{k+1}-1] (k >= 20), b = k, so b^2 / n <= k^2 / 2^k <= 20^2 / 2^20.
    N_exp = 20
    N = 1 << N_exp
    for k in range(N_exp, 40):
        assert Fraction((k + 1) * (k + 1), 1 << (k + 1)) < Fraction(k * k, 1 << k)
    lb_A_inf = Fraction(1, 2) - Fraction(3, 2 * N)
    ub_AB_inf = Fraction(1, 2) + Fraction(N_exp * N_exp, N * N)
    assert ub_AB_inf < 2 * lb_A_inf, "Failed lower density separation"
    assert ub_AB_inf - Fraction(1, 2) < Fraction(1, 10**6)
    assert Fraction(1, 2) - lb_A_inf < Fraction(1, 10**5)
    print(
        f"PASS check_exact_density_bounds: verified on 4<=n,m<=64 and N=2^20 separation: "
        f"d(A+B) <= {float_free_frac(ub_AB_inf)} < 2*d(A) >= {float_free_frac(2*lb_A_inf)}"
    )


def float_free_frac(f: Fraction) -> str:
    return f"{f.numerator}/{f.denominator}"


def check_subgroup_translate_intersection() -> None:
    """
    Verify directly from H_{a,b,c} = {(a*n + b*m, c*m) : m, n in Z} and
    H = H_{a,b,c} cap (N x N) that for every translate v in Z^2:
      (v + H) cap (N x {2}) equals:
        empty set if (2 - v_2) is not in c * N (i.e. 2 - v_2 <= 0 or (2 - v_2) % c != 0),
        { (x, 2) : x >= max(1, v_1 + 1) and x % a == (v_1 + b * m_i) % a } otherwise,
        where m_i = (2 - v_2) // c.
    Exhaustively checked for 1 <= a, c <= 5, 0 <= b < a, v in [-8, 8]^2, x in [1, 128].
    """
    Xlim = 128
    count_cases = 0
    count_nonempty = 0
    for a in range(1, 6):
        for c in range(1, 6):
            for b in range(0, a):
                for v1 in range(-8, 9):
                    for v2 in range(-8, 9):
                        count_cases += 1
                        # Direct enumeration from H_{a,b,c} cap (N x N)
                        # We need y = v2 + c*m == 2 with c*m >= 1, so m = (2 - v2)/c >= 1.
                        # Search generous m range covering all possibilities:
                        direct_xs = set()
                        m_max = (abs(2 - v2) // c) + 5
                        for m in range(1, m_max + 1):
                            if v2 + c * m != 2:
                                continue
                            # Now need 1 <= x <= Xlim with x = v1 + a*n + b*m AND a*n + b*m >= 1
                            n_min = (-abs(v1) - abs(b * m) - 5) // a
                            n_max = (Xlim + abs(v1) + abs(b * m) + 5) // a
                            for n in range(n_min, n_max + 1):
                                hx = a * n + b * m
                                hy = c * m
                                if hx >= 1 and hy >= 1:
                                    x = v1 + hx
                                    if 1 <= x <= Xlim:
                                        direct_xs.add(x)

                        # Closed-form AP formula
                        if 2 - v2 <= 0 or (2 - v2) % c != 0:
                            formula_xs = set()
                        else:
                            mi = (2 - v2) // c
                            assert mi >= 1
                            x0 = max(1, v1 + 1)
                            res = (v1 + b * mi) % a
                            formula_xs = {x for x in range(x0, Xlim + 1) if x % a == res}
                            count_nonempty += 1

                        assert direct_xs == formula_xs, (
                            f"AP mismatch a={a},b={b},c={c},v=({v1},{v2}): "
                            f"direct={sorted(direct_xs)[:10]} formula={sorted(formula_xs)[:10]}"
                        )

    # Also verify exact counting bound floor((2^K - X0)/a) <= |AP cap [2^K]| and Case 1/2 gap
    for a in (1, 2, 3, 5, 17, 100):
        for X0 in (1, 5, 100, 10000):
            # Pick K such that 2^K > max(X0, 4 * a * K^2)
            # In fact check all K from threshold to threshold + 5
            K = 1
            while not ((1 << K) > max(X0, 4 * a * K * K)):
                K += 1
            for KK in range(K, K + 6):
                limit = 1 << KK
                # Minimum possible count in [X0, limit] for ANY residue mod a
                # Number of integers in [X0, limit] is limit - X0 + 1 >= (limit - X0),
                # so at least floor((limit - X0) / a) elements in any mod-a class!
                # Verify directly on residue class (X0 - 1) % a (worst-case shift) when limit <= 2^20
                if KK <= 20:
                    worst_res = (X0 - 1) % a
                    exact_cnt = ((limit - worst_res) // a) - ((X0 - 1 - worst_res) // a)
                    assert exact_cnt >= (limit - X0) // a
                lb_U = (limit - X0) // a
                # |(A+B) cap ([2^KK] x {2})| <= (KK - 1)^2 < KK^2
                # (since 2^j + 2^{j'} <= 2^KK => 2^j < 2^KK => j <= KK - 1)
                ub_AB = (KK - 1) * (KK - 1)
                assert lb_U > ub_AB, f"Gap fail at a={a}, X0={X0}, K={KK}: {lb_U} <= {ub_AB}"
                assert (limit - X0) // a - KK * KK > 0

    print(
        f"PASS check_subgroup_translate_intersection: {count_cases} (a,b,c,v) cases "
        f"({count_nonempty} nonempty APs), plus asymptotic Case 2 gaps verified"
    )


def main() -> None:
    check_sumset_and_slices()
    check_exact_density_bounds()
    check_subgroup_translate_intersection()
    print("PASS")


if __name__ == "__main__":
    main()
