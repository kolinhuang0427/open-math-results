"""Independent exact-arithmetic checker for targets/ballantine-2408.13346-e2p4-rec/PROOF.md."""

import sys
import sympy as sp


def e2p4_direct(n: int) -> int:
    """Directly enumerate P(4, n) and sum e_2(lambda)."""
    total = 0
    for l4 in range(1, n // 4 + 1):
        for l3 in range(l4, (n - l4) // 3 + 1):
            for l2 in range(l3, (n - l4 - l3) // 2 + 1):
                l1 = n - l4 - l3 - l2
                if l1 >= l2:
                    total += l1 * l2 + l1 * l3 + l1 * l4 + l2 * l3 + l2 * l4 + l3 * l4
    return total


def main():
    # 1. Symbolic check of Section 1 parameterization & e_2 polynomial
    y1, y2, y3, y4 = sp.symbols("y1 y2 y3 y4")
    lam4 = y4
    lam3 = y4 + y3
    lam2 = y4 + y3 + y2
    lam1 = y4 + y3 + y2 + y1
    assert sp.expand(lam1 + lam2 + lam3 + lam4 - (y1 + 2 * y2 + 3 * y3 + 4 * y4)) == 0
    e2_lam = lam1 * lam2 + lam1 * lam3 + lam1 * lam4 + lam2 * lam3 + lam2 * lam4 + lam3 * lam4
    e2_9term = (
        y1 * y2
        + 2 * y1 * y3
        + 3 * y1 * y4
        + y2**2
        + 4 * y2 * y3
        + 6 * y2 * y4
        + 3 * y3**2
        + 9 * y3 * y4
        + 6 * y4**2
    )
    assert sp.expand(e2_lam - e2_9term) == 0

    # 2. Section 2: Exact rational generating function and all 9 term numerators
    q = sp.Symbol("q")
    D_q = (1 - q) ** 6 * (1 + q) ** 4 * (1 + q**2) ** 3 * (1 + q + q**2) ** 3

    # Using sum_{y>=0} x^y = 1/(1-x), sum y x^y = x/(1-x)^2, sum y^2 x^y = x(1+x)/(1-x)^3,
    # and sum_{y>=1} x^y = x/(1-x), etc.
    def S0(x):
        return 1 / (1 - x)

    def S1(x):
        return x / (1 - x) ** 2

    def S2(x):
        return x * (1 + x) / (1 - x) ** 3

    def T0(x):
        return x / (1 - x)

    def T1(x):
        return x / (1 - x) ** 2

    def T2(x):
        return x * (1 + x) / (1 - x) ** 3

    terms_gf = [
        1 * S1(q) * S0(q**2) * S0(q**3) * T0(q**4),  # wait: y1*y2 -> S1(q)*S1(q^2)*S0(q^3)*T0(q^4)
    ]
    terms_gf = [
        1 * S1(q) * S1(q**2) * S0(q**3) * T0(q**4),
        2 * S1(q) * S0(q**2) * S1(q**3) * T0(q**4),
        3 * S1(q) * S0(q**2) * S0(q**3) * T1(q**4),
        1 * S0(q) * S2(q**2) * S0(q**3) * T0(q**4),
        4 * S0(q) * S1(q**2) * S1(q**3) * T0(q**4),
        6 * S0(q) * S1(q**2) * S0(q**3) * T1(q**4),
        3 * S0(q) * S0(q**2) * S2(q**3) * T0(q**4),
        9 * S0(q) * S0(q**2) * S1(q**3) * T1(q**4),
        6 * S0(q) * S0(q**2) * S0(q**3) * T2(q**4),
    ]

    expected_nums = [
        q**7 + 3 * q**8 + 7 * q**9 + 11 * q**10 + 14 * q**11 + 14 * q**12 + 11 * q**13 + 7 * q**14 + 3 * q**15 + q**16,
        2 * q**8 + 6 * q**9 + 12 * q**10 + 18 * q**11 + 20 * q**12 + 18 * q**13 + 12 * q**14 + 6 * q**15 + 2 * q**16,
        3 * q**5 + 9 * q**6 + 18 * q**7 + 24 * q**8 + 24 * q**9 + 18 * q**10 + 9 * q**11 + 3 * q**12,
        q**6 + 2 * q**7 + 6 * q**8 + 8 * q**9 + 13 * q**10 + 12 * q**11 + 13 * q**12 + 8 * q**13 + 6 * q**14 + 2 * q**15 + q**16,
        4 * q**9 + 8 * q**10 + 16 * q**11 + 20 * q**12 + 20 * q**13 + 16 * q**14 + 8 * q**15 + 4 * q**16,
        6 * q**6 + 12 * q**7 + 24 * q**8 + 24 * q**9 + 24 * q**10 + 12 * q**11 + 6 * q**12,
        3 * q**7 + 6 * q**8 + 9 * q**9 + 15 * q**10 + 15 * q**11 + 15 * q**12 + 15 * q**13 + 9 * q**14 + 6 * q**15 + 3 * q**16,
        9 * q**7 + 18 * q**8 + 27 * q**9 + 27 * q**10 + 18 * q**11 + 9 * q**12,
        6 * q**4 + 12 * q**5 + 18 * q**6 + 12 * q**7 + 12 * q**8 + 12 * q**9 + 18 * q**10 + 12 * q**11 + 6 * q**12,
    ]

    N_q = sp.Integer(0)
    for idx, (tgf, exp_num) in enumerate(zip(terms_gf, expected_nums), 1):
        num = sp.cancel(tgf * D_q)
        assert sp.Poly(num, q).domain == sp.ZZ
        assert sp.expand(num - exp_num) == 0, f"Term {idx} numerator mismatch"
        N_q += num

    expected_N = (
        6 * q**4 + 15 * q**5 + 34 * q**6 + 57 * q**7 + 95 * q**8 + 121 * q**9 + 146 * q**10
        + 126 * q**11 + 106 * q**12 + 72 * q**13 + 50 * q**14 + 25 * q**15 + 11 * q**16
    )
    assert sp.expand(N_q - expected_N) == 0

    # 3. Section 3: Expand D(q), verify recurrence coefficients, and check against e2p4_direct(0..40)
    D_poly = sp.Poly(D_q, q, domain=sp.ZZ)
    assert D_poly.degree() == 22
    d_coeffs = [int(D_poly.nth(j)) for j in range(23)]
    expected_d = [1, 1, 0, -3, -6, -3, 3, 12, 12, 2, -10, -18, -10, 2, 12, 12, 3, -3, -6, -3, 0, 1, 1]
    assert d_coeffs == expected_d
    assert sp.Poly(N_q, q).degree() == 16 < 22

    # Expand N(q) / D(q) in Z[[q]] up to q^40
    n_max = 40
    N_list = [int(sp.Poly(N_q, q).nth(j)) for j in range(17)] + [0] * (n_max - 16)
    gf_coeffs = [0] * (n_max + 1)
    for n in range(n_max + 1):
        val = N_list[n] - sum(d_coeffs[j] * gf_coeffs[n - j] for j in range(1, min(23, n + 1)))
        gf_coeffs[n] = val

    direct_coeffs = [e2p4_direct(n) for n in range(n_max + 1)]
    assert gf_coeffs == direct_coeffs, "GF coefficients != direct partition enumeration"

    # Verify the verbatim conjectured recurrence from TARGET.md for n = 0..18
    for n in range(n_max - 22 + 1):
        rhs = (
            -direct_coeffs[n]
            - direct_coeffs[1 + n]
            + 3 * direct_coeffs[3 + n]
            + 6 * direct_coeffs[4 + n]
            + 3 * direct_coeffs[5 + n]
            - 3 * direct_coeffs[6 + n]
            - 12 * direct_coeffs[7 + n]
            - 12 * direct_coeffs[8 + n]
            - 2 * direct_coeffs[9 + n]
            + 10 * direct_coeffs[10 + n]
            + 18 * direct_coeffs[11 + n]
            + 10 * direct_coeffs[12 + n]
            - 2 * direct_coeffs[13 + n]
            - 12 * direct_coeffs[14 + n]
            - 12 * direct_coeffs[15 + n]
            - 3 * direct_coeffs[16 + n]
            + 3 * direct_coeffs[17 + n]
            + 6 * direct_coeffs[18 + n]
            + 3 * direct_coeffs[19 + n]
            - direct_coeffs[21 + n]
        )
        assert direct_coeffs[22 + n] == rhs, f"Recurrence failed at n={n}"

    print(f"PASS (9-term GF, D(q)/N(q) exact, direct P(4,n) match n=0..{n_max}, 22-term recurrence verified)")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
