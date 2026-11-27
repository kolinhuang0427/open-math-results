"""Exact verification script for OEIS A274272 (Colin Barker conjectures)."""
from fractions import Fraction


def poly_mul(a, b):
    res = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
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
    # 1. Partial fraction polynomial identity for F(x) = 1/((1-x)(1-x^2)(1-x^3)(1-x^4))
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

    # 2. Verify symbolic evaluation for m = 5^n (m odd, m mod 3 in {1, 2}):
    # Basis [1, m, m^2, m^3]
    p1 = [
        Fraction(6, 144) + Fraction(2, 16) + Fraction(59, 288) + Fraction(17, 72),
        Fraction(11, 144) + Fraction(3, 16) + Fraction(59, 288),
        Fraction(6, 144) + Fraction(1, 16),
        Fraction(1, 144),
    ]
    p2 = [Fraction(-1, 8) + Fraction(-1, 32), Fraction(-1, 32), Fraction(0), Fraction(0)]
    for parity, sign_val, cube_coeff in [(0, 1, Fraction(0)), (1, -1, Fraction(-1, 9))]:
        p4 = [cube_coeff, Fraction(0), Fraction(0), Fraction(0)]
        total_m = poly_add(poly_add(p1, p2), p4)
        expected = [Fraction(57 + 8 * sign_val, 144), Fraction(63, 144), Fraction(15, 144), Fraction(1, 144)]
        assert total_m == expected, f"Mismatch at parity={parity}: {total_m} != {expected}"

    # 3. Verify rational G.f. and denominator polynomial in QQ[x]
    f1 = [Fraction(1), Fraction(-1)]
    fp = [Fraction(1), Fraction(1)]
    f5 = [Fraction(1), Fraction(-5)]
    f25 = [Fraction(1), Fraction(-25)]
    f125 = [Fraction(1), Fraction(-125)]

    den = poly_mul(poly_mul(f1, fp), poly_mul(f5, poly_mul(f25, f125)))
    assert den == [Fraction(1), Fraction(-155), Fraction(3874), Fraction(-15470), Fraction(-3875), Fraction(15625)]

    def prod_except(idx):
        factors = [f1, fp, f5, f25, f125]
        res = [Fraction(1)]
        for k, fac in enumerate(factors):
            if k != idx:
                res = poly_mul(res, fac)
        return res

    coeffs = [Fraction(57, 144), Fraction(8, 144), Fraction(63, 144), Fraction(15, 144), Fraction(1, 144)]
    g_num = [Fraction(0)]
    for idx, c in enumerate(coeffs):
        g_num = poly_add(g_num, poly_mul([c], prod_except(idx)))
    assert g_num == [Fraction(1), Fraction(-149), Fraction(3129), Fraction(-5655), Fraction(-6750)]

    # 4. Exact partition DP up to m = 5^5 = 3125 and OEIS A274272 DATA check (n = 0..14)
    max_m = 5**5
    dp = [0] * (max_m + 1)
    dp[0] = 1
    for part in (1, 2, 3, 4):
        for s in range(part, max_m + 1):
            dp[s] += dp[s - part]

    oeis_data = [
        1, 6, 185, 15246, 1736385, 212946246, 26516391385, 3312004971246,
        413937039016385, 51740540399346246, 6467527813385891385,
        808439983261977471246, 101054973072475964016385,
        12631871013177766274346246, 1578983861125177809948391385,
    ]
    for n in range(6):
        assert dp[5**n] == oeis_data[n], f"DP mismatch at n={n}"

    seq = []
    for n in range(25):
        num = 57 + 8 * ((-1) ** n) + 63 * (5**n) + 3 * (5 ** (1 + 2 * n)) + 125**n
        assert num % 144 == 0
        seq.append(num // 144)
    assert seq[: len(oeis_data)] == oeis_data

    for n in range(5, 25):
        assert seq[n] == (
            155 * seq[n - 1]
            - 3874 * seq[n - 2]
            + 15470 * seq[n - 3]
            + 3875 * seq[n - 4]
            - 15625 * seq[n - 5]
        )

    quot = [Fraction(0)] * 25
    for n in range(25):
        val = g_num[n] if n < len(g_num) else Fraction(0)
        for j in range(1, min(n, 5) + 1):
            val -= den[j] * quot[n - j]
        quot[n] = val / den[0]
        assert quot[n].denominator == 1 and int(quot[n]) == seq[n]

    print("PASS")


if __name__ == "__main__":
    main()
