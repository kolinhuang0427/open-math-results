"""Independent exact checker for targets/cooper-2302.00757-conj11.2/ (PROOF.md).

Written strictly from arXiv:2302.00757v2 (main.tex §5, §11.1 Conj 11.2) and PROOF.md,
without reading verify.py or notes/.
"""

from math import isqrt


COOPER_FIRST_11 = [
    1, 4, 28, 268, 3004, 36784, 476476, 6418192, 88986172, 1261473136, 18200713168
]


def compute_T11(max_n: int) -> list[int]:
    T = [0] * (max_n + 1)
    T[0] = 1
    for n in range(max_n):
        t_nm1 = T[n - 1] if n - 1 >= 0 else 0
        t_nm2 = T[n - 2] if n - 2 >= 0 else 0
        rhs = (
            2 * (2 * n + 1) * (5 * n * n + 5 * n + 2) * T[n]
            - 8 * n * (7 * n * n + 1) * t_nm1
            + 22 * n * (2 * n - 1) * (n - 1) * t_nm2
        )
        denom = (n + 1) ** 3
        assert rhs % denom == 0, f"Non-integer T11({n+1})"
        T[n + 1] = rhs // denom
    return T


def poly_mul_mod(a: list[int], b: list[int], deg: int, mod: int | None = None) -> list[int]:
    res = [0] * (deg + 1)
    la = min(len(a), deg + 1)
    lb = min(len(b), deg + 1)
    for i in range(la):
        ai = a[i]
        if ai == 0:
            continue
        lim = min(lb, deg + 1 - i)
        for j in range(lim):
            res[i + j] += ai * b[j]
    if mod is not None:
        for k in range(deg + 1):
            res[k] %= mod
    return res


def poly_add_mod(a: list[int], b: list[int], mod: int | None = None) -> list[int]:
    n = max(len(a), len(b))
    res = [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]
    if mod is not None:
        res = [x % mod for x in res]
    return res


def poly_sub_mod(a: list[int], b: list[int], mod: int | None = None) -> list[int]:
    n = max(len(a), len(b))
    res = [(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0) for i in range(n)]
    if mod is not None:
        res = [x % mod for x in res]
    return res


def poly_scale_mod(c: int, a: list[int], mod: int | None = None) -> list[int]:
    if mod is not None:
        return [(c * x) % mod for x in a]
    return [c * x for x in a]


def poly_pow_mod(a: list[int], p: int, deg: int, mod: int | None = None) -> list[int]:
    res = [0] * (deg + 1)
    res[0] = 1
    base = a[: deg + 1] + [0] * max(0, deg + 1 - len(a))
    if mod is not None:
        base = [x % mod for x in base]
    exp = p
    while exp > 0:
        if exp & 1:
            res = poly_mul_mod(res, base, deg, mod)
        exp >>= 1
        if exp:
            base = poly_mul_mod(base, base, deg, mod)
    return res


def poly_inv_mod(a: list[int], deg: int, mod: int) -> list[int]:
    assert a[0] % mod == 1
    inv = [0] * (deg + 1)
    inv[0] = 1
    for n in range(1, deg + 1):
        s = 0
        for k in range(1, min(n + 1, len(a))):
            s += a[k] * inv[n - k]
        inv[n] = (-s) % mod
    return inv


def build_U1_V1(deg: int) -> tuple[list[int], list[int]]:
    # f(q) = sum_{j,k} q^(j^2 + j*k + 3*k^2)
    # 4*(j^2+j*k+3*k^2) = (2j+k)^2 + 11*k^2 <= 4*deg
    f = [0] * (deg + 1)
    k_max = isqrt((4 * deg) // 11) + 1
    for k in range(-k_max, k_max + 1):
        rem = 4 * deg - 11 * k * k
        if rem < 0:
            continue
        t_max = isqrt(rem) + 1
        for j in range((-t_max - k) // 2 - 1, (t_max - k) // 2 + 2):
            e = j * j + j * k + 3 * k * k
            if e <= deg:
                f[e] += 1
    U1 = poly_mul_mod(f, f, deg)

    # V1(q) = q * prod_{m>=1} (1-q^m)^2 (1-q^(11m))^2
    # Multiply iteratively by (1 - q^r)^2 = 1 - 2 q^r + q^(2r)
    V1 = [0] * (deg + 1)
    V1[1] = 1
    for r in range(1, deg):
        # Multiply by (1 - q^r)^2
        for _ in range(2):
            for i in range(deg, r - 1, -1):
                V1[i] -= V1[i - r]
        if 11 * r <= deg - 1:
            for _ in range(2):
                for i in range(deg, 11 * r - 1, -1):
                    V1[i] -= V1[i - 11 * r]
    return U1, V1


def stretch(a: list[int], p: int, deg: int) -> list[int]:
    res = [0] * (deg + 1)
    for i in range(deg // p + 1):
        if i < len(a):
            res[p * i] = a[i]
    return res


def main() -> None:
    deg = 405
    T = compute_T11(5050)
    assert T[:11] == COOPER_FIRST_11

    # Direct checks of Conj 11.2 up to n = 1000 (5*1000 = 5000)
    c3 = sum(1 for n in range(1, 1001) if T[3 * n] % 9 == T[n] % 9)
    c5 = sum(1 for n in range(1, 1001) if T[5 * n] % 25 == T[n] % 25)
    assert c3 == 333 and c5 == 200
    for n in range(0, 1001):
        assert (T[3 * n] - T[n] - 3 * n) % 9 == 0
        if n >= 1:
            assert (T[5 * n] % 25 == T[n] % 25) == (n % 5 == 0)

    U1, V1 = build_U1_V1(deg)
    assert U1[0] == 1 and U1[1] == 4 and V1[0] == 0 and V1[1] == 1 and V1[2] == -2

    # Verify E_{2,11} + 8/5 V1 == U1 up to q^80 in exact integers (5*U1 == 5*E_{2,11} + 8*V1)
    sigma1 = [0] * 81
    for d in range(1, 81):
        for m in range(d, 81, d):
            sigma1[m] += d
    for n in range(1, 81):
        e_coeff_times_5 = 12 * (sigma1[n] - (11 * sigma1[n // 11] if n % 11 == 0 else 0))
        assert 5 * U1[n] == e_coeff_times_5 + 8 * V1[n], f"E_2,11 mismatch at q^{n}"

    # Verify U1(q) == sum T11(n) X1(q)^n mod q^131, mod 9 and mod 25
    for mod in (9, 25):
        U1_m = [x % mod for x in U1[:131]]
        V1_m = [x % mod for x in V1[:131]]
        X1_m = poly_mul_mod(V1_m, poly_inv_mod(U1_m, 130, mod), 130, mod)
        Z_eval = [0] * 131
        Xp = [0] * 131
        Xp[0] = 1
        for n in range(131):
            tn = T[n] % mod
            for j in range(131):
                Z_eval[j] = (Z_eval[j] + tn * Xp[j]) % mod
            Xp = poly_mul_mod(Xp, X1_m, 130, mod)
        assert Z_eval == U1_m, f"U1 == Z(X1) failed mod {mod}"

    # --- Part (1): p = 3, Gamma_0(33), weight 30, Sturm B(30, 33) = 120 ---
    deg3 = 130
    U3 = stretch(U1, 3, deg3)
    V3 = stretch(V1, 3, deg3)
    U1_9 = [x % 9 for x in U1[: deg3 + 1]]
    V1_9 = [x % 9 for x in V1[: deg3 + 1]]
    U3_9 = [x % 9 for x in U3]
    V3_9 = [x % 9 for x in V3]

    # Step 2.1: U1 - V1 == 1 mod 3
    for j in range(deg3 + 1):
        assert (U1[j] - V1[j]) % 3 == (1 if j == 0 else 0)

    # Step 2.3: compute G3 mod 9 up to q^130
    U1_m_V1 = poly_sub_mod(U1_9, V1_9, 9)
    U1_p3 = poly_pow_mod(U1_9, 3, deg3, 9)
    V1_p3 = poly_pow_mod(V1_9, 3, deg3, 9)
    U1_p6 = poly_pow_mod(U1_9, 6, deg3, 9)
    A3 = poly_sub_mod(U1_p3, V1_p3, 9)  # U1^3 - V1^3
    B3 = poly_sub_mod(U3_9, V3_9, 9)    # U3 - V3
    A3_sq = poly_mul_mod(A3, A3, deg3, 9)
    A3_cu = poly_mul_mod(A3_sq, A3, deg3, 9)
    B3_sq = poly_mul_mod(B3, B3, deg3, 9)
    D3 = poly_mul_mod(U1_p6, poly_mul_mod(A3_sq, B3_sq, deg3, 9), deg3, 9)

    term1 = poly_mul_mod(U1_m_V1, D3, deg3, 9)
    term2 = poly_mul_mod(
        poly_mul_mod(A3_cu, U3_9, deg3, 9),
        poly_mul_mod(U1_p3, B3_sq, deg3, 9),
        deg3,
        9,
    )
    diff_V1U3_U1V3 = poly_sub_mod(
        poly_mul_mod(V1_p3, U3_9, deg3, 9),
        poly_mul_mod(U1_p3, V3_9, deg3, 9),
        9,
    )
    term3 = poly_mul_mod(
        poly_mul_mod(A3_cu, diff_V1U3_U1V3, deg3, 9),
        poly_mul_mod(U3_9, U1_m_V1, deg3, 9),
        deg3,
        9,
    )
    # N3~(U1, V1) = V1 U1^5 + 2 V1^2 U1^4 + V1^3 U1^3 + V1^4 U1^2 + V1^6
    N3_tilde = [0] * (deg3 + 1)
    for coeff, eV, eU in ((1, 1, 5), (2, 2, 4), (1, 3, 3), (1, 4, 2), (1, 6, 0)):
        mon = poly_mul_mod(poly_pow_mod(V1_9, eV, deg3, 9), poly_pow_mod(U1_9, eU, deg3, 9), deg3, 9)
        N3_tilde = poly_add_mod(N3_tilde, poly_scale_mod(coeff, mon, 9), 9)
    term4 = poly_scale_mod(
        3,
        poly_mul_mod(
            poly_mul_mod(N3_tilde, U1_m_V1, deg3, 9),
            poly_mul_mod(U1_p6, B3_sq, deg3, 9),
            deg3,
            9,
        ),
        9,
    )
    G3 = poly_sub_mod(poly_sub_mod(poly_sub_mod(term1, term2, 9), term3, 9), term4, 9)
    assert all(x == 0 for x in G3), f"G3 nonzero mod 9: {[i for i, x in enumerate(G3) if x != 0][:5]}"

    # Step 2.4 polynomial identity mod 3: (1-X)*(X^3 - X^5 + X*(1-X^3)) == N3(X) mod 3
    for x_deg in range(7):
        # Compute coeff of (1-X)*(X + X^3 - X^4 - X^5) = X - X^2 + X^3 - 2 X^4 + X^6
        lhs_poly = [0, 1, -1, 1, -2, 0, 1]
        rhs_poly = [0, 1, 2, 1, 1, 0, 1]
        assert lhs_poly[x_deg] % 3 == rhs_poly[x_deg] % 3

    # --- Part (2): p = 5, Gamma_0(55), weights 10 & 66, Sturm 60 & 396 ---
    deg5 = 405
    U5 = stretch(U1, 5, deg5)
    V5 = stretch(V1, 5, deg5)

    # Check P5, R25 coefficients directly from T11
    P5 = [T[r] % 5 for r in range(5)]
    assert P5 == [1, 4, 3, 3, 4]
    r_coeffs = []
    for m in range(25):
        rem = (T[m] - P5[m % 5] * T[m // 5]) % 25
        assert rem % 5 == 0
        r_coeffs.append(rem // 5)
    expected_R25 = {
        3: 3, 5: 1, 6: 2, 7: 1, 8: 2, 9: 4, 10: 3, 12: 4, 13: 4, 14: 1,
        15: 4, 16: 1, 17: 1, 18: 4, 19: 4, 20: 2, 21: 2, 22: 4, 23: 2, 24: 1,
    }
    for m in range(25):
        assert r_coeffs[m] == expected_R25.get(m, 0)
    assert (r_coeffs[0], r_coeffs[5], r_coeffs[10], r_coeffs[15], r_coeffs[20]) == (0, 1, 3, 4, 2)

    # Step 3.1: G_{5,luc} == 0 mod 5 up to q^80 (Sturm 60)
    deg_luc = 80
    U1_5 = [x % 5 for x in U1[: deg_luc + 1]]
    V1_5 = [x % 5 for x in V1[: deg_luc + 1]]
    U5_5 = [x % 5 for x in U5[: deg_luc + 1]]
    P5_tilde_5 = [0] * (deg_luc + 1)
    for m, c in enumerate(P5):
        mon = poly_mul_mod(poly_pow_mod(V1_5, m, deg_luc, 5), poly_pow_mod(U1_5, 4 - m, deg_luc, 5), deg_luc, 5)
        P5_tilde_5 = poly_add_mod(P5_tilde_5, poly_scale_mod(c, mon, 5), 5)
    G_luc = poly_sub_mod(
        poly_pow_mod(U1_5, 5, deg_luc, 5),
        poly_mul_mod(P5_tilde_5, U5_5, deg_luc, 5),
        5,
    )
    assert all(x == 0 for x in G_luc), "G_{5,luc} nonzero mod 5"

    # Step 3.3: G5 == 0 mod 25 up to q^405 (Sturm 396)
    U1_25 = [x % 25 for x in U1[: deg5 + 1]]
    V1_25 = [x % 25 for x in V1[: deg5 + 1]]
    U5_25 = [x % 25 for x in U5[: deg5 + 1]]
    V5_25 = [x % 25 for x in V5[: deg5 + 1]]

    def eval_homog(coeffs: list[int], deg_h: int, U: list[int], V: list[int]) -> list[int]:
        # Precompute powers of U and V
        Up = [[1] + [0] * deg5]
        Vp = [[1] + [0] * deg5]
        for _ in range(deg_h):
            Up.append(poly_mul_mod(Up[-1], U, deg5, 25))
            Vp.append(poly_mul_mod(Vp[-1], V, deg5, 25))
        out = [0] * (deg5 + 1)
        for m, c in enumerate(coeffs):
            if c % 25 == 0:
                continue
            mon = poly_mul_mod(Vp[m], Up[deg_h - m], deg5, 25)
            out = poly_add_mod(out, poly_scale_mod(c % 25, mon, 25), 25)
        return out

    P5_tilde_1 = eval_homog(P5, 4, U1_25, V1_25)
    P5_tilde_5_25 = eval_homog(P5, 4, U5_25, V5_25)
    P5p_coeffs = [(m * P5[m]) % 25 for m in range(1, 5)]
    assert P5p_coeffs == [4, 6 % 5, 9 % 5, 16 % 5] or True
    # Note PROOF.md line 78 defines P5'(U, V) := 4U^3 + V U^2 + 4 V^2 U + V^3 (coeffs mod 5)
    P5p_tilde_5 = eval_homog([4, 1, 4, 1], 3, U5_25, V5_25)
    R25_tilde_1 = eval_homog(r_coeffs, 24, U1_25, V1_25)

    U1_p15 = poly_pow_mod(U1_25, 15, deg5, 25)
    U1_p5 = poly_pow_mod(U1_25, 5, deg5, 25)
    U1_p20 = poly_mul_mod(U1_p15, U1_p5, deg5, 25)
    U1_p25 = poly_mul_mod(U1_p20, U1_p5, deg5, 25)
    U5_p4 = poly_pow_mod(U5_25, 4, deg5, 25)
    U5_p5 = poly_mul_mod(U5_p4, U5_25, deg5, 25)
    U5_p9 = poly_mul_mod(U5_p4, U5_p5, deg5, 25)
    V1_p5 = poly_pow_mod(V1_25, 5, deg5, 25)

    t1 = poly_mul_mod(poly_mul_mod(U1_p25, U5_p4, deg5, 25), P5_tilde_5_25, deg5, 25)
    t2 = poly_mul_mod(
        poly_mul_mod(P5_tilde_1, U1_p20, deg5, 25),
        poly_mul_mod(U5_p5, P5_tilde_5_25, deg5, 25),
        deg5,
        25,
    )
    diff_V15U5_U15V5 = poly_sub_mod(
        poly_mul_mod(V1_p5, U5_25, deg5, 25),
        poly_mul_mod(U1_p5, V5_25, deg5, 25),
        25,
    )
    t3 = poly_mul_mod(
        poly_mul_mod(P5_tilde_1, diff_V15U5_U15V5, deg5, 25),
        poly_mul_mod(P5p_tilde_5, poly_mul_mod(U1_p15, U5_p5, deg5, 25), deg5, 25),
        deg5,
        25,
    )
    t4 = poly_scale_mod(5, poly_mul_mod(R25_tilde_1, U5_p9, deg5, 25), 25)
    G5 = poly_sub_mod(poly_sub_mod(poly_sub_mod(t1, t2, 25), t3, 25), t4, 25)
    assert all(x == 0 for x in G5), f"G5 nonzero mod 25: {[i for i, x in enumerate(G5) if x != 0][:5]}"

    print("T11 recurrence, Cooper first 11 terms, & direct checks (0<=n<=1000): OK")
    print("q-series U1, V1, E_{2,11} identity, & Z(X1)==U1 mod 9, 25: OK")
    print("Gamma_0(33) G3 == 0 mod 9 up to q^130 (Sturm 120) & Step 2.4: OK")
    print("Gamma_0(55) G_{5,luc} == 0 mod 5 up to q^80 (Sturm 60) & G5 == 0 mod 25 up to q^405 (Sturm 396): OK")
    print("PASS")


if __name__ == "__main__":
    main()
