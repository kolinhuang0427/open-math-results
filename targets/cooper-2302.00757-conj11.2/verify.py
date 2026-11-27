#!/usr/bin/env python3
"""Exact verification of the Sturm-bound proof of Cooper Conjecture 11.2 (arXiv:2302.00757v2)."""

from fractions import Fraction


def compute_T11(max_n: int) -> list[int]:
    """Compute exact integer values T_11(0..max_n) from the 4-term recurrence."""
    T = {-2: Fraction(0), -1: Fraction(0), 0: Fraction(1)}
    for n in range(max_n):
        rhs = (
            (2 * n + 1) * (10 * n * n + 10 * n + 4) * T[n]
            - 8 * n * (7 * n * n + 1) * T[n - 1]
            + 22 * n * (2 * n - 1) * (n - 1) * T[n - 2]
        )
        T[n + 1] = rhs / ((n + 1) ** 3)
        assert T[n + 1].denominator == 1, f"Non-integer T_11({n+1})"
    return [int(T[i]) for i in range(max_n + 1)]


def compute_UV(N: int) -> tuple[list[int], list[int]]:
    """Compute exact integer q-series U_1 = Z(q) and V_1 = eta(q)^2 eta(q^11)^2 up to q^N."""
    f = [0] * (N + 1)
    lim = int((N + 1) ** 0.5) + 3
    for j in range(-lim, lim + 1):
        for k in range(-lim, lim + 1):
            m = j * j + j * k + 3 * k * k
            if m <= N:
                f[m] += 1
    U = [0] * (N + 1)
    for i in range(N + 1):
        fi = f[i]
        if fi == 0:
            continue
        for j in range(N + 1 - i):
            U[i + j] += fi * f[j]
    V = [0] * (N + 1)
    V[1] = 1
    for n in range(1, N + 1):
        for _ in range(2):
            for k in range(N, n - 1, -1):
                V[k] -= V[k - n]
        if 11 * n <= N:
            for _ in range(2):
                for k in range(N, 11 * n - 1, -1):
                    V[k] -= V[k - 11 * n]
    return U, V


def poly_mul(a: list[int], b: list[int], N: int, mod: int | None = None) -> list[int]:
    c = [0] * (N + 1)
    for i, ai in enumerate(a):
        if mod is not None:
            ai %= mod
        if ai == 0:
            continue
        for j in range(min(len(b), N + 1 - i)):
            c[i + j] += ai * b[j]
    if mod is not None:
        return [x % mod for x in c]
    return c


def poly_pow(a: list[int], e: int, N: int, mod: int | None = None) -> list[int]:
    res = [0] * (N + 1)
    res[0] = 1
    base = [x % mod for x in a[: N + 1]] if mod is not None else a[: N + 1]
    while e > 0:
        if e & 1:
            res = poly_mul(res, base, N, mod)
        base = poly_mul(base, base, N, mod)
        e >>= 1
    return res


def stretch(a: list[int], p: int, N: int) -> list[int]:
    res = [0] * (N + 1)
    for i in range(N // p + 1):
        res[p * i] = a[i]
    return res


def eval_homog(coeffs: list[int], V: list[int], U: list[int], deg: int, N: int, mod: int) -> list[int]:
    Vpows = [poly_pow(V, i, N, mod) for i in range(len(coeffs))]
    Upows = [poly_pow(U, i, N, mod) for i in range(deg + 1)]
    res = [0] * (N + 1)
    for i, ci in enumerate(coeffs):
        if ci % mod == 0:
            continue
        term = poly_mul(Vpows[i], Upows[deg - i], N, mod)
        for k in range(N + 1):
            res[k] = (res[k] + ci * term[k]) % mod
    return res


def main() -> None:
    # 1. Sanity check Z(q) == sum T_11(n) X_1(q)^n up to q^30
    T30 = compute_T11(30)
    U30, V30 = compute_UV(30)
    # Compute X_1 = V_1 / U_1 exactly in Z[[q]]
    X30 = [0] * 31
    for i in range(31):
        s = V30[i]
        for j in range(1, i + 1):
            s -= U30[j] * X30[i - j]
        assert s % U30[0] == 0
        X30[i] = s // U30[0]
    Z_from_X = [0] * 31
    Xp = [0] * 31
    Xp[0] = 1
    for n in range(31):
        for k in range(31):
            Z_from_X[k] += T30[n] * Xp[k]
        Xp = poly_mul(Xp, X30, 30)
    assert Z_from_X == U30, "Modular parametrization Z(q) != sum T_11(n) X(q)^n"

    # 2. Check U_1 - V_1 == 1 (mod 3) up to q^30 (Sturm bound B(2,11) = 2)
    assert all((U30[k] - V30[k]) % 3 == (1 if k == 0 else 0) for k in range(31))

    # 3. Check F_3 polynomial identity in F_3[X]: (1-X)(X^3 - X^5 + X(1-X^3)) == X + 2X^2 + X^3 + X^4 + X^6 (mod 3)
    # Coefficients of (1 - X)*(X + X^3 - X^4 - X^5):
    pA = [1, -1]
    pB = [0, 1, 0, 1, -1, -1]
    prod = [0] * 7
    for i, a in enumerate(pA):
        for j, b in enumerate(pB):
            prod[i + j] += a * b
    assert [x % 3 for x in prod] == [0, 1, 2, 1, 1, 0, 1]

    # 4. Sturm-bound check for p=3 on Gamma_0(33): weight 30, Sturm bound 4*30 = 120 (verify up to q^130)
    N3 = 130
    U1, V1 = compute_UV(N3)
    U3 = stretch(U1, 3, N3)
    V3 = stretch(V1, 3, N3)
    m9 = 9
    U1_m_V1 = [(U1[k] - V1[k]) % m9 for k in range(N3 + 1)]
    U3_m_V3 = [(U3[k] - V3[k]) % m9 for k in range(N3 + 1)]
    U1_3 = poly_pow(U1, 3, N3, m9)
    V1_3 = poly_pow(V1, 3, N3, m9)
    D1 = [(U1_3[k] - V1_3[k]) % m9 for k in range(N3 + 1)]
    D1_2 = poly_pow(D1, 2, N3, m9)
    D1_3 = poly_mul(D1_2, D1, N3, m9)
    U1_6 = poly_pow(U1, 6, N3, m9)
    U3_m_V3_2 = poly_pow(U3_m_V3, 2, N3, m9)
    denom3 = poly_mul(poly_mul(U1_6, D1_2, N3, m9), U3_m_V3_2, N3, m9)
    assert denom3[0] == 1

    term3_A = poly_mul(U1_m_V1, denom3, N3, m9)
    term3_B = poly_mul(poly_mul(D1_3, poly_mul(U3, U1_3, N3, m9), N3, m9), U3_m_V3_2, N3, m9)
    diff3 = [(poly_mul(V1_3, U3, N3, m9)[k] - poly_mul(U1_3, V3, N3, m9)[k]) % m9 for k in range(N3 + 1)]
    term3_C = poly_mul(poly_mul(D1_3, diff3, N3, m9), poly_mul(U3, U1_m_V1, N3, m9), N3, m9)
    numR = eval_homog([0, 1, 2, 1, 1, 0, 1], V1, U1, 6, N3, m9)
    term3_D = [(3 * x) % m9 for x in poly_mul(poly_mul(numR, U1_m_V1, N3, m9), poly_mul(U1_6, U3_m_V3_2, N3, m9), N3, m9)]
    G3 = [(term3_A[k] - term3_B[k] - term3_C[k] - term3_D[k]) % m9 for k in range(N3 + 1)]
    assert all(x == 0 for x in G3), "Gamma_0(33) Sturm check mod 9 failed"

    # 5. Compute P_5 and R_25 directly from T_11(0..24)
    P5 = [T30[r] % 5 for r in range(5)]
    assert P5 == [1, 4, 3, 3, 4]
    P5p = [(i * P5[i]) % 5 for i in range(1, 5)]
    R25 = [((T30[m] - P5[m % 5] * T30[m // 5]) % 25) // 5 for m in range(25)]
    assert [R25[5 * r] for r in range(5)] == [0, 1, 3, 4, 2]

    # 6. Sturm-bound check for p=5 Lucas on Gamma_0(55): weight 10, Sturm bound 6*10 = 60 (verify up to q^80)
    N5 = 400
    U1, V1 = compute_UV(N5)
    U5 = stretch(U1, 5, N5)
    V5 = stretch(V1, 5, N5)
    P5_hom1_mod5 = eval_homog(P5, V1, U1, 4, 80, 5)
    U1_5_mod5 = poly_pow(U1, 5, 80, 5)
    G5_luc = [(U1_5_mod5[k] - poly_mul(P5_hom1_mod5, U5, 80, 5)[k]) % 5 for k in range(81)]
    assert all(x == 0 for x in G5_luc), "Gamma_0(55) Lucas Sturm check mod 5 failed"

    # 7. Sturm-bound check for p=5 mod 25 on Gamma_0(55): weight 66, Sturm bound 6*66 = 396 (verify up to q^400)
    m25 = 25
    P5_hom1 = eval_homog(P5, V1, U1, 4, N5, m25)
    P5_hom5 = eval_homog(P5, V5, U5, 4, N5, m25)
    P5p_hom5 = eval_homog(P5p, V5, U5, 3, N5, m25)
    R25_hom1 = eval_homog(R25, V1, U1, 24, N5, m25)
    U1_5 = poly_pow(U1, 5, N5, m25)
    V1_5 = poly_pow(V1, 5, N5, m25)
    U1_15 = poly_pow(U1, 15, N5, m25)
    U1_20 = poly_pow(U1, 20, N5, m25)
    U1_25 = poly_mul(U1_20, U1_5, N5, m25)
    U5_4 = poly_pow(U5, 4, N5, m25)
    U5_5 = poly_mul(U5_4, U5, N5, m25)
    U5_9 = poly_mul(U5_4, U5_5, N5, m25)
    assert poly_mul(poly_mul(poly_pow(U1, 24, N5, m25), U5_4, N5, m25), P5_hom5, N5, m25)[0] == 1

    lhs5 = poly_mul(poly_mul(U1_25, U5_4, N5, m25), P5_hom5, N5, m25)
    t5_1 = poly_mul(poly_mul(P5_hom1, U1_20, N5, m25), poly_mul(U5_5, P5_hom5, N5, m25), N5, m25)
    diff5 = [(poly_mul(V1_5, U5, N5, m25)[k] - poly_mul(U1_5, V5, N5, m25)[k]) % m25 for k in range(N5 + 1)]
    t5_2 = poly_mul(poly_mul(P5_hom1, diff5, N5, m25), poly_mul(P5p_hom5, poly_mul(U1_15, U5_5, N5, m25), N5, m25), N5, m25)
    t5_3 = [(5 * x) % m25 for x in poly_mul(R25_hom1, U5_9, N5, m25)]
    G5 = [(lhs5[k] - t5_1[k] - t5_2[k] - t5_3[k]) % m25 for k in range(N5 + 1)]
    assert all(x == 0 for x in G5), "Gamma_0(55) Sturm check mod 25 failed"

    # 8. Direct integer check on 1 <= n <= 120 (T_11 up to 600)
    T600 = compute_T11(600)
    for n in range(1, 121):
        assert (T600[3 * n] - T600[n] - 3 * n) % 9 == 0, f"Part 1 failed at n={n}"
        assert ((T600[5 * n] - T600[n]) % 25 == 0) == (n % 5 == 0), f"Part 2 failed at n={n}"

    print("PASS")


if __name__ == "__main__":
    main()
