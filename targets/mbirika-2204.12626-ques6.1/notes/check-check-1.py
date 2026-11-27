#!/usr/bin/env python3
r"""Independent exact-arithmetic verifier for targets/mbirika-2204.12626-ques6.1.

Checks Question 6.1 of arXiv:2204.12626v2 directly from primary definitions:
  F_0 = 0, F_1 = 1, F_n = F_{n-1} + F_{n-2}
  L_0 = 2, L_1 = 1, L_n = L_{n-1} + L_{n-2}
  \mathcal{F}^3(k) = gcd_{n >= 0} ( \sum_{i=1}^{k} F_{n+i}^3 )
  \mathcal{L}^3(k) = gcd_{n >= 0} ( \sum_{i=1}^{k} L_{n+i}^3 )
Zero floating-point arithmetic is used (only int and fractions.Fraction).
"""

from fractions import Fraction
import math


def gen_sequence(a0: int, a1: int, length: int) -> list[int]:
    seq = [a0, a1]
    while len(seq) < length:
        seq.append(seq[-1] + seq[-2])
    return seq[:length]


def window_cube_sums(seq: list[int], k: int, count: int) -> list[int]:
    assert len(seq) >= count + k
    cubes = [x * x * x for x in seq]
    return [sum(cubes[n + 1 : n + 1 + k]) for n in range(count)]


def seq_gcd(vals: list[int]) -> int:
    g = 0
    for v in vals:
        g = math.gcd(g, v)
    return g


def formula_F(F: list[int], k: int) -> Fraction:
    g = math.gcd(F[k + 1] ** 3 - 1, F[k + 2] ** 3 - 1)
    if k % 6 == 0:
        return Fraction(g, 1)
    return Fraction(g, 2)


def formula_L(L: list[int], k: int) -> Fraction:
    g = math.gcd(L[k + 1] ** 3 - 1, L[k + 2] ** 3 - 9)
    if k % 6 == 0:
        return Fraction(g, 1)
    return Fraction(g, 2)


def formula_L_27(L: list[int], k: int) -> Fraction:
    g = math.gcd(L[k + 1] ** 3 - 1, L[k + 2] ** 3 - 27)
    if k % 6 == 0:
        return Fraction(g, 1)
    return Fraction(g, 2)


def main() -> None:
    F = gen_sequence(0, 1, 100)
    L = gen_sequence(2, 1, 100)

    # Sanity check initial values from primary source
    assert F[:7] == [0, 1, 1, 2, 3, 5, 8]
    assert L[:7] == [2, 1, 3, 4, 7, 11, 18]

    # 1a: F^3(k) for 6 \nmid k, k = 2
    s_F2 = window_cube_sums(F, 2, 20)
    assert s_F2[0] == 2 and s_F2[1] == 9 and s_F2[2] == 35
    g_F2 = seq_gcd(s_F2)
    f_F2 = formula_F(F, 2)
    print(f"1a (F^3, k=2): first_sums={s_F2[:5]}, actual_gcd={g_F2}, conj_formula={f_F2}")
    assert g_F2 == 1
    assert f_F2 == Fraction(1, 2)
    assert Fraction(g_F2) != f_F2

    # 1b: F^3(k) for 6 | k, k = 6
    s_F6 = window_cube_sums(F, 6, 20)
    assert s_F6[0] == 674 and s_F6[1] == 2870
    assert math.gcd(s_F6[0], s_F6[1]) == 2
    # Prove 2 | F^3(6) for all n via F_n mod 2 period 3
    f_mod2 = [x % 2 for x in F[:15]]
    assert f_mod2[:3] == [0, 1, 1]
    for i in range(len(f_mod2) - 3):
        assert f_mod2[i] == f_mod2[i + 3]
    for start in range(3):
        block_sum_mod2 = sum((f_mod2[start + i] ** 3) for i in range(6)) % 2
        assert block_sum_mod2 == 0
    g_F6 = seq_gcd(s_F6)
    f_F6 = formula_F(F, 6)
    print(f"1b (F^3, k=6): first_sums={s_F6[:3]}, actual_gcd={g_F6}, conj_formula={f_F6}")
    assert g_F6 == 2
    assert f_F6 == Fraction(4, 1)
    assert Fraction(g_F6) != f_F6

    # Check even k in {2, 4, ..., 30} for F^3(k)
    f_even_mismatches = []
    for k in range(2, 31, 2):
        actual = seq_gcd(window_cube_sums(F, k, 20))
        conj = formula_F(F, k)
        if Fraction(actual) != conj:
            f_even_mismatches.append((k, actual, conj))
    print(f"F^3 even k in [2..30] mismatches ({len(f_even_mismatches)}/15): {f_even_mismatches[:5]}...")
    assert len(f_even_mismatches) == 15

    # 2a: L^3(k) for 6 \nmid k, k = 2
    s_L2 = window_cube_sums(L, 2, 20)
    assert s_L2[0] == 28 and s_L2[1] == 91 and s_L2[2] == 407
    assert math.gcd(28, 91) == 7 and math.gcd(7, 407) == 1
    g_L2 = seq_gcd(s_L2)
    f_L2 = formula_L(L, 2)
    print(f"2a (L^3, k=2): first_sums={s_L2[:5]}, actual_gcd={g_L2}, conj_formula={f_L2}")
    assert g_L2 == 1
    assert f_L2 == Fraction(1, 2)
    assert Fraction(g_L2) != f_L2

    # 2b: L^3(k) for 6 | k, k = 12
    s_L12 = window_cube_sums(L, 12, 20)
    assert s_L12[:3] == [43702500, 185123260, 784200340]
    claimed_L12 = [43702500, 185123260, 784200340]
    L12_sums_match = (s_L12[:3] == claimed_L12)
    g_L12_3 = seq_gcd(s_L12[:3])
    g_L12 = seq_gcd(s_L12)
    assert g_L12_3 == 20 and g_L12 == 20
    # Prove 20 | L^3(12) for all n >= 0:
    # mod 4 period 6: (2, 1, 3, 0, 3, 3) -> cubes mod 4 sum to 2 mod 4, so 12 consecutive sum to 0 mod 4.
    l_mod4 = [x % 4 for x in L[:24]]
    assert l_mod4[:6] == [2, 1, 3, 0, 3, 3]
    for i in range(len(l_mod4) - 6):
        assert l_mod4[i] == l_mod4[i + 6]
    for start in range(6):
        assert sum((l_mod4[start + i] ** 3) for i in range(12)) % 4 == 0
    # mod 5 period 4: (2, 1, 3, 4) -> cubes mod 5 are (3, 1, 2, 4), sum=10 == 0 mod 5, so 12=3*4 consecutive sum to 0 mod 5.
    l_mod5 = [x % 5 for x in L[:20]]
    assert l_mod5[:4] == [2, 1, 3, 4]
    for i in range(len(l_mod5) - 4):
        assert l_mod5[i] == l_mod5[i + 4]
    for start in range(4):
        assert sum((l_mod5[start + i] ** 3) for i in range(12)) % 5 == 0
    f_L12 = formula_L(L, 12)
    assert L[13] ** 3 - 1 == 141420760
    assert L[14] ** 3 - 9 == 599077098
    assert f_L12 == Fraction(2, 1)
    print(f"2b (L^3, k=12): gcd(first 3)={g_L12_3}, actual_gcd={g_L12}, conj_formula={f_L12}")
    assert Fraction(g_L12) != f_L12

    # Remark: even with L_2^3 = 27 instead of 9, k=6 fails
    s_L6 = window_cube_sums(L, 6, 20)
    g_L6 = seq_gcd(s_L6)
    f_L6_27 = formula_L_27(L, 6)
    assert L[7] ** 3 - 1 == 24388
    assert L[8] ** 3 - 27 == 103796
    assert g_L6 == 2
    assert f_L6_27 == Fraction(28, 1)
    print(f"2b remark (L^3 with 27, k=6): actual_gcd={g_L6}, alt_formula={f_L6_27}")

    # Also check even k in {2, 4, ..., 30} for L^3(k)
    l_even_mismatches = []
    for k in range(2, 31, 2):
        actual = seq_gcd(window_cube_sums(L, k, 20))
        conj = formula_L(L, k)
        if Fraction(actual) != conj:
            l_even_mismatches.append((k, actual, conj))
    print(f"L^3 even k in [2..30] mismatches ({len(l_even_mismatches)}/15): {l_even_mismatches[:5]}...")
    assert len(l_even_mismatches) == 14
    assert seq_gcd(window_cube_sums(L, 6, 20)) == 2 and formula_L(L, 6) == Fraction(2, 1)

    print(f"2b L^3(12) first 3 sums match COUNTEREXAMPLE.md L51: {L12_sums_match} (true={s_L12[:3]}, claimed={claimed_L12})")
    if L12_sums_match:
        print("PASS")
    else:
        print("FAIL")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
