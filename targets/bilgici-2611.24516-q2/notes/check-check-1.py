"""Independent exact-arithmetic verifier for targets/bilgici-2611.24516-q2."""

# Table of expected values from PROOF.md L48-65 (centered mod 19 in {-9..9} for e_a)
EXPECTED_ROWS = {
    0:  (0, 1,  (-4, -9,  4,  2, -6,  4,  3,  6, -1), 16,  5, 11,  9, 14, 14),
    1:  (0, 9,  (-5, -4,  3, -7, -4,  6, -3,  2, -9), 18,  9,  9, 15,  2, 13),
    2:  (0, 16, (-5,  2,  6, -8,  4, -4, -3,  9,  2), 15, 18, 16, 16,  1, 15),
    3:  (0, 8,  (-4, -9,  4,  6, -6, -1,  4, -6,  9), 15,  0, 15,  9, 13, 15),
    4:  (0, 9,  ( 4,  2,  4,  8,  1,  0,  9, -9,  9),  7, 11, 15, 13,  0, 13),
    5:  (0, 10, ( 0, -3,  0, -9,  8, -4, -5, -7,  2),  7,  3,  4, 18,  1, 17),
    6:  (1, 15, ( 1,  0,  0, -3,  4,  4,  1,  3,  7),  1,  4, 16, 14,  4, 10),
    7:  (0, 6,  ( 1, -4,  0, -9,  4,  3,  3,  7,  9), 17, 11,  6, 18, 17,  1),
    8:  (0, 6,  ( 0,  0,  5, -4, -3, -8,  3, -5, -1), 14,  6,  8, 13, 17, 15),
    9:  (0, 7,  ( 0, -5,  1,  7, -5,  0, -2, -5, -6),  0,  0,  0, 14, 17, 16),
    10: (0, 9,  (-3,  6, -4, -9, -5,  1,  2,  3,  2),  7, 15, 11, 15,  8,  7),
    11: (0, 9,  ( 4,  7,  1, -1, -1, -2, -5,  6,  2), 11,  5,  6, 18,  6, 12),
    12: (0, 13, (-5,  1, -7, -4,  5, -8,  5,  9, -6), 14,  0, 14,  0,  1, 18),
    13: (1, 3,  ( 0,  6, -4, -9, -5, -7,  0, -2,  4),  3, 11, 11, 10,  3,  7),
    14: (0, 7,  ( 0, -3,  4,  6, -7, -2,  3,  5,  5),  1, 10, 10,  1,  2, 18),
    15: (0, 15, ( 0,  1,  0, -5, -8, -4,  5,  6,  7), 10,  6,  4, 18, 10,  8),
    16: (0, 18, ( 6, -9, -3, -8,  5, -5, -4,  1, -6),  7,  9, 17, 12,  2, 10),
    18: (0, 14, ( 4,  2,  6, -5, -6, -9, -7,  8, -8), 12,  7,  5,  7,  3,  4),
}


def poly_mul_mod19(a: list[int], b: list[int], deg: int) -> list[int]:
    out = [0] * deg
    for i, ai in enumerate(a[:deg]):
        if ai == 0:
            continue
        for j in range(min(len(b), deg - i)):
            out[i + j] = (out[i + j] + ai * b[j]) % 19
    return out


def poly_pow_mod19(base: list[int], exp: int, deg: int) -> list[int]:
    res = [0] * deg
    res[0] = 1
    b = (base + [0] * deg)[:deg]
    while exp > 0:
        if exp & 1:
            res = poly_mul_mod19(res, b, deg)
        exp >>= 1
        if exp > 0:
            b = poly_mul_mod19(b, b, deg)
    return res


def mul_one_minus_xk_mod19(poly: list[int], k: int, coeff: int = 1) -> None:
    """In-place multiply poly by (1 - coeff * x^k) mod 19 (note coeff=1: subtract shifted)."""
    deg = len(poly)
    for i in range(deg - 1, k - 1, -1):
        poly[i] = (poly[i] - coeff * poly[i - k]) % 19


def center19(x: int) -> int:
    x %= 19
    return x - 19 if x > 9 else x


def rho(x: int) -> int:
    r = x % 19
    return min(r, 19 - r)


def inv19(a: int) -> int:
    a %= 19
    assert a != 0
    return pow(a, 17, 19)


def main() -> None:
    M = 19
    Y_DEG = 19  # compute y-series modulo y^19
    Q_DEG = M * Y_DEG  # 361

    # 1. Build P_0(y) and P_a(y) (1 <= a <= 9) in F_{19}[[y]]/(y^{19})
    P: list[list[int]] = []
    # P_0 = (y^19; y^19)_inf == 1 mod y^19
    p0 = [0] * Y_DEG
    p0[0] = 1
    P.append(p0)
    for a in range(1, 10):
        pa = [0] * Y_DEG
        pa[0] = 1
        for k in range(a, Y_DEG, 19):
            mul_one_minus_xk_mod19(pa, k)
        for k in range(19 - a, Y_DEG, 19):
            mul_one_minus_xk_mod19(pa, k)
        P.append(pa)

    def get_P(idx: int) -> list[int]:
        r = rho(idx)
        return P[r]

    def G(A: int, B: int) -> list[int]:
        assert 1 <= A < B <= 9
        res = poly_mul_mod19(get_P(A), get_P(B), Y_DEG)
        res = poly_mul_mod19(res, get_P(A + B), Y_DEG)
        res = poly_mul_mod19(res, get_P(B - A), Y_DEG)
        return res

    def shift_y(poly: list[int], v: int) -> list[int]:
        return ([0] * v + poly)[:Y_DEG]

    def lin_comb(c1: int, s1: int, A1: int, B1: int, c2: int, s2: int, A2: int, B2: int) -> list[int]:
        g1 = shift_y(G(A1, B1), s1)
        g2 = shift_y(G(A2, B2), s2)
        return [(c1 * g1[i] + c2 * g2[i]) % 19 for i in range(Y_DEG)]

    # 2. Exact Table \ref{tab:B} from manuscript.tex L354-363
    B_table: dict[int, list[int]] = {
        0:  lin_comb( 1, 0, 3, 9,  4, 1, 4, 6),
        1:  lin_comb( 9, 0, 4, 9,  7, 1, 2, 6),
        2:  lin_comb(-3, 0, 2, 9,  4, 1, 6, 7),
        3:  lin_comb( 8, 0, 3, 8, -6, 1, 7, 9),
        4:  lin_comb( 9, 0, 4, 8,  2, 1, 5, 6),
        5:  lin_comb( 8, 0, 2, 8,  2, 0, 5, 9),
        6:  lin_comb( 3, 1, 1, 6, -7, 1, 7, 8),
        7:  lin_comb( 6, 0, 1, 9,  5, 2, 3, 4),
        8:  lin_comb( 6, 0, 5, 8, -5, 3, 2, 3),
        9:  lin_comb( 7, 0, 3, 7, -3, 2, 2, 4),
        10: lin_comb(-8, 0, 1, 8, -2, 0, 4, 7),
        11: lin_comb( 9, 0, 2, 7,  2, 1, 3, 5),
        12: lin_comb(-6, 0, 6, 9,  8, 1, 4, 5),
        13: lin_comb( 3, 1, 2, 5,  4, 3, 1, 3),
        14: lin_comb( 7, 0, 5, 7,  9, 2, 1, 4),
        15: lin_comb(-4, 0, 6, 8, -1, 4, 1, 2),
        16: lin_comb(-1, 0, 1, 7,  5, 1, 8, 9),
        17: [0] * Y_DEG,
        18: lin_comb(-5, 0, 3, 6,  1, 1, 1, 5),
    }

    # 3. Independently compute f(q)^10 mod (19, q^{361}) and verify 19-dissection matches Table \ref{tab:B}
    # Note: P_0(q^19) == 1 mod q^361 because y^19 = q^{361} == 0 mod q^361!
    fq = [0] * Q_DEG
    fq[0] = 1
    for n in range(1, Q_DEG):
        mul_one_minus_xk_mod19(fq, n)
    fq10 = poly_pow_mod19(fq, 10, Q_DEG)
    for r in range(19):
        comp_from_f10 = [fq10[19 * k + r] for k in range(Y_DEG)]
        assert comp_from_f10 == B_table[r], f"19-dissection mismatch at r={r}"
    print("19-dissection of f(q)^10 mod (19, q^361) vs Table tab:B: PASS")

    # 4. Check logarithmic-derivative obstruction and all table entries in PROOF.md
    for r in range(19):
        if r == 17:
            assert all(x == 0 for x in B_table[r])
            continue
        Br = B_table[r]
        v = next(i for i, val in enumerate(Br) if val != 0)
        c = Br[v]
        cinv = inv19(c)
        # Normalized series B_tilde = c^{-1} y^{-v} B_r mod y^{19-v} (note v <= 1, so 19-v >= 18 >= 12)
        f_norm = [(Br[v + i] * cinv) % 19 for i in range(Y_DEG - v)]
        assert f_norm[0] == 1

        # Newton's recurrence: d_n = n*f_n - sum_{k=1}^{n-1} d_k * f_{n-k} mod 19
        d = [0] * (Y_DEG - v)
        for n in range(1, Y_DEG - v):
            s = (n * f_norm[n]) % 19
            for k in range(1, n):
                s = (s - d[k] * f_norm[n - k]) % 19
            d[n] = s

        # Solve e_1..e_9 mod 19 from d_1..d_9
        e = [0] * 10
        for a in range(1, 10):
            rhs = d[a]
            for m in range(1, a):
                if a % m == 0:
                    rhs = (rhs + m * e[m]) % 19
            e[a] = (-inv19(a) * rhs) % 19

        d10_pred = (-(e[1] + 2 * e[2] + 5 * e[5]) - 10 * e[9]) % 19
        d11_pred = (-e[1] - 11 * e[8]) % 19
        diff10 = (d[10] - d10_pred) % 19
        diff11 = (d[11] - d11_pred) % 19

        # Check every value against PROOF.md L48-65 table
        exp_tuple = (
            v, c, tuple(center19(e[a]) for a in range(1, 10)),
            d[10], d10_pred, diff10,
            d[11], d11_pred, diff11,
        )
        assert exp_tuple == EXPECTED_ROWS[r], f"Table mismatch at r={r}: got {exp_tuple}, expected {EXPECTED_ROWS[r]}"

        # Verify PROOF.md L71 explicit r=0 example
        if r == 0:
            assert Br[:12] == [1, 4, 0, 14, 0, 15, 18, 18, 0, 4, 15, 0]
            assert d[1:12] == [4, 3, 11, 14, 15, 5, 2, 4, 1, 16, 9], (
                f"PROOF.md L71 mismatch: actual d[1:12]={d[1:12]}"
            )

        # Verify obstruction
        assert diff11 != 0, f"d_11 matched at r={r}!"
        if r != 9:
            assert diff10 != 0, f"d_10 matched at r={r}!"

        # Independently multiply prod_{a=1}^9 P_a(y)^{e_a mod 19} mod (19, y^{19-v}) and check discrepancy
        prod = [0] * (Y_DEG - v)
        prod[0] = 1
        for a in range(1, 10):
            if e[a] != 0:
                prod = poly_mul_mod19(prod, poly_pow_mod19(P[a], e[a], Y_DEG - v), Y_DEG - v)
        assert prod[:10] == f_norm[:10]
        assert prod[:12] != f_norm[:12]

    print("All 18 nonzero rows logarithmic-derivative obstruction & direct product checks: PASS")
    print("PASS")


if __name__ == "__main__":
    main()
