#!/usr/bin/env python3
"""Exact integer arithmetic verifier refuting Question 6.1 of arXiv:2204.12626v2."""

import math


def main() -> int:
    f_seq = [0, 1]
    l_seq = [2, 1]
    for _ in range(20):
        f_seq.append(f_seq[-1] + f_seq[-2])
        l_seq.append(l_seq[-1] + l_seq[-2])

    # 1a. F^3(2) = 1 vs conjectured 1/2 * gcd(F_3^3 - 1, F_4^3 - 1) = 1/2
    s_f2_0 = sum(f_seq[i] ** 3 for i in range(1, 3))
    s_f2_1 = sum(f_seq[1 + i] ** 3 for i in range(1, 3))
    assert s_f2_0 == 2 and s_f2_1 == 9
    assert math.gcd(s_f2_0, s_f2_1) == 1
    g_f2_rhs = math.gcd(f_seq[3] ** 3 - 1, f_seq[4] ** 3 - 1)
    assert g_f2_rhs == 1  # half of 1 is 1/2 != 1

    # 1b. F^3(6) = 2 (since 2 | sum of 6 consecutive F_i^3, and 4 does not divide 674) vs gcd(F_7^3-1, F_8^3-1) = 4
    s_f6_0 = sum(f_seq[i] ** 3 for i in range(1, 7))
    s_f6_1 = sum(f_seq[1 + i] ** 3 for i in range(1, 7))
    assert s_f6_0 == 674 and s_f6_1 == 2870
    assert math.gcd(s_f6_0, s_f6_1) == 2
    g_f6_rhs = math.gcd(f_seq[7] ** 3 - 1, f_seq[8] ** 3 - 1)
    assert f_seq[7] ** 3 - 1 == 2196 and f_seq[8] ** 3 - 1 == 9260
    assert g_f6_rhs == 4 and g_f6_rhs != 2

    # 2a. L^3(2) = 1 vs conjectured 1/2 * gcd(L_3^3 - 1, L_4^3 - 9) = 1/2
    s_l2_0 = sum(l_seq[i] ** 3 for i in range(1, 3))
    s_l2_1 = sum(l_seq[1 + i] ** 3 for i in range(1, 3))
    s_l2_2 = sum(l_seq[2 + i] ** 3 for i in range(1, 3))
    assert (s_l2_0, s_l2_1, s_l2_2) == (28, 91, 407)
    assert math.gcd(s_l2_0, s_l2_1, s_l2_2) == 1
    g_l2_rhs = math.gcd(l_seq[3] ** 3 - 1, l_seq[4] ** 3 - 9)
    assert (l_seq[3] ** 3 - 1, l_seq[4] ** 3 - 9) == (63, 334)
    assert g_l2_rhs == 1  # half of 1 is 1/2 != 1

    # 2b. L^3(12) = 20 (proved via period 6 mod 4 and period 4 mod 5) vs gcd(L_13^3 - 1, L_14^3 - 9) = 2
    assert [x % 4 for x in l_seq[:6]] == [2, 1, 3, 0, 3, 3]
    assert [x % 4 for x in l_seq[6:12]] == [2, 1, 3, 0, 3, 3]
    assert sum((x ** 3) % 4 for x in l_seq[:6]) % 4 == 2
    assert [x % 5 for x in l_seq[:4]] == [2, 1, 3, 4]
    assert [x % 5 for x in l_seq[4:8]] == [2, 1, 3, 4]
    assert sum((x ** 3) % 5 for x in l_seq[:4]) % 5 == 0
    s_l12 = [sum(l_seq[n + i] ** 3 for i in range(1, 13)) for n in range(3)]
    assert math.gcd(*s_l12) == 20
    g_l12_rhs = math.gcd(l_seq[13] ** 3 - 1, l_seq[14] ** 3 - 9)
    assert g_l12_rhs == 2 and g_l12_rhs != 20

    # Also verify L^3(6) = 2 vs gcd(L_7^3 - 1, L_8^3 - 27) = 28
    s_l6 = [sum(l_seq[n + i] ** 3 for i in range(1, 7)) for n in range(3)]
    assert math.gcd(*s_l6) == 2
    assert math.gcd(l_seq[7] ** 3 - 1, l_seq[8] ** 3 - 27) == 28

    print(
        "PASS: Question 6.1 of arXiv:2204.12626v2 refuted — "
        "F^3(2)=1 != 1/2, F^3(6)=2 != 4, L^3(2)=1 != 1/2, L^3(12)=20 != 2."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
