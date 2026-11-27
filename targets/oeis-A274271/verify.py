"""Exact verification script for OEIS A274271 (Colin Barker conjectures)."""
from fractions import Fraction


def poly_mul(a, b, limit=None):
    res = [Fraction(0)] * (len(a) + len(b) - 1 if limit is None else min(len(a) + len(b) - 1, limit + 1))
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            if limit is not None and i + j > limit:
                break
            res[i + j] += ai * bj
    return res


def poly_add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else Fraction(0)) + (b[i] if i < len(b) else Fraction(0)) for i in range(n)]


def poly_pow(p, e):
    res = [Fraction(1)]
    for _ in range(e):
        res = poly_mul(res, p)
    return res


def main():
    # 1. Verify the exact partial fraction polynomial identity in QQ[x]:
    # F(x) = 1 / ((1-x)(1-x^2)(1-x^3)(1-x^4))
    # 288 * (1-x)(1-x^2)(1-x^3)(1-x^4) * F_pf(x) == 288
    one_m_x = [Fraction(1), Fraction(-1)]
    one_p_x = [Fraction(1), Fraction(1)]
    one_p_x2 = [Fraction(1), Fraction(0), Fraction(1)]
    one_p_x_x2 = [Fraction(1), Fraction(1), Fraction(1)]

    t1 = poly_mul(
        [Fraction(175), Fraction(-358), Fraction(263), Fraction(-68)],
        poly_mul(poly_pow(one_p_x, 2), poly_mul(one_p_x2, one_p_x_x2)),
    )
    t2 = poly_mul(
        [Fraction(45), Fraction(36)],
        poly_mul(poly_pow(one_m_x, 4), poly_mul(one_p_x2, one_p_x_x2)),
    )
    t3 = poly_mul(
        [Fraction(36)],
        poly_mul(poly_pow(one_m_x, 4), poly_mul(poly_pow(one_p_x, 2), one_p_x_x2)),
    )
    t4 = poly_mul(
        [Fraction(32)],
        poly_mul(poly_pow(one_m_x, 4), poly_mul(poly_pow(one_p_x, 3), one_p_x2)),
    )
    lhs = poly_add(poly_add(t1, t2), poly_add(t3, t4))
    while len(lhs) > 1 and lhs[-1] == 0:
        lhs.pop()
    assert lhs == [Fraction(288)], f"Partial fraction identity failed: {lhs}"

    # 2. Verify symbolic evaluation for odd multiples of 3 using exact polynomial algebra in m:
    # Represent polynomials in m via basis [1, m, m^2, m^3]
    # [x^m] terms from (1-x)^{-r}:
    # (m+3)(m+2)(m+1)/144 + (m+2)(m+1)/16 + 59(m+1)/288 + 17/72
    p1 = [
        Fraction(6, 144) + Fraction(2, 16) + Fraction(59, 288) + Fraction(17, 72),
        Fraction(11, 144) + Fraction(3, 16) + Fraction(59, 288),
        Fraction(6, 144) + Fraction(1, 16),
        Fraction(1, 144),
    ]
    # (-1)^m = -1: -1/8 - (m+1)/32
    p2 = [Fraction(-1, 8) + Fraction(-1, 32), Fraction(-1, 32), Fraction(0), Fraction(0)]
    # 1/(8(1+x^2)) has coeff 0 for odd m
    p3 = [Fraction(0), Fraction(0), Fraction(0), Fraction(0)]
    # (1+x)/(9(1+x+x^2)) = (1-x^2)/(9(1-x^3)) has coeff 1/9 for 3|m
    p4 = [Fraction(1, 9), Fraction(0), Fraction(0), Fraction(0)]
    total_m = poly_add(poly_add(p1, p2), poly_add(p3, p4))
    target_m = [Fraction(81, 144), Fraction(63, 144), Fraction(15, 144), Fraction(1, 144)]
    assert total_m == target_m, f"Polynomial in m mismatch: {total_m} != {target_m}"

    # Verify (3+m)^2 * (9+m) == m^3 + 15 m^2 + 63 m + 81
    prod_m = poly_mul(poly_pow([Fraction(3), Fraction(1)], 2), [Fraction(9), Fraction(1)])
    assert prod_m == [Fraction(81), Fraction(63), Fraction(15), Fraction(1)]

    # 3. Verify rational generating function & recurrence identity in QQ[x]:
    d1 = [Fraction(1), Fraction(-1)]
    d3 = [Fraction(1), Fraction(-3)]
    d9 = [Fraction(1), Fraction(-9)]
    d27 = [Fraction(1), Fraction(-27)]
    den = poly_mul(poly_mul(d1, d3), poly_mul(d9, d27))
    assert den == [Fraction(1), Fraction(-40), Fraction(390), Fraction(-1080), Fraction(729)]

    g_num = poly_add(
        poly_mul([Fraction(-1, 9)], den),
        poly_add(
            poly_add(
                poly_mul([Fraction(81, 144)], poly_mul(d3, poly_mul(d9, d27))),
                poly_mul([Fraction(63, 144)], poly_mul(d1, poly_mul(d9, d27))),
            ),
            poly_add(
                poly_mul([Fraction(15, 144)], poly_mul(d1, poly_mul(d3, d27))),
                poly_mul([Fraction(1, 144)], poly_mul(d1, poly_mul(d3, d9))),
            ),
        ),
    )
    assert g_num == [Fraction(1), Fraction(-37), Fraction(288), Fraction(-405), Fraction(-81)]

    # 4. Compute exact partitions p(m, <= 4) by integer DP up to m = 3^7 = 2187
    # and match OEIS A274271 DATA (n = 0..18) via closed form / DP!
    max_m = 3**7
    dp = [0] * (max_m + 1)
    dp[0] = 1
    for part in (1, 2, 3, 4):
        for s in range(part, max_m + 1):
            dp[s] += dp[s - part]

    oeis_data = [
        1, 3, 18, 225, 4410, 105903, 2746098, 73140525, 1965803130, 52995903003,
        1430162760978, 38607856205625, 1042353276205050, 28143008896575303,
        759856474192364658, 20516081909157771525, 553933825501236490170,
        14956209814120079146803, 403817633711525094117138,
    ]
    for n in range(8):
        assert dp[3**n] == oeis_data[n], f"DP mismatch at n={n}"

    # Verify closed form, recurrence, and rational G.f. expansion through n=25
    seq = [1] + [((3 + 3**n) ** 2 * (9 + 3**n)) // 144 for n in range(1, 26)]
    for n in range(1, 26):
        num = (3 + 3**n) ** 2 * (9 + 3**n)
        assert num % 144 == 0
    assert seq[: len(oeis_data)] == oeis_data
    for n in range(5, 26):
        assert seq[n] == 40 * seq[n - 1] - 390 * seq[n - 2] + 1080 * seq[n - 3] - 729 * seq[n - 4]

    # Power series division g_num / den through degree 25
    quot = [Fraction(0)] * 26
    for n in range(26):
        val = g_num[n] if n < len(g_num) else Fraction(0)
        for j in range(1, min(n, 4) + 1):
            val -= den[j] * quot[n - j]
        quot[n] = val / den[0]
        assert quot[n].denominator == 1 and int(quot[n]) == seq[n]

    print("PASS")


if __name__ == "__main__":
    main()
