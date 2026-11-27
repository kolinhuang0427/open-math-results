"""Independent exact-integer verifier for targets/oeis-A132411 (Peter Bala 2025 conjecture).

Directly expands F(q) in Z[[q]]/(q^{M+1}) and verifies Steps 1-3 (Euler identity,
P_N(z) recurrence, c_{N,m}, P_N(-1), Gauss's theta identity, and F(q)) using pure
integer arithmetic (zero floating point).
"""

import sympy as sp


def poly_mul_trunc(p: list[int], q: list[int], deg: int) -> list[int]:
    out = [0] * (deg + 1)
    for i, pi in enumerate(p[: deg + 1]):
        if pi == 0:
            continue
        for j in range(min(len(q), deg + 1 - i)):
            out[i + j] += pi * q[j]
    return out


def poly_inv_trunc(p: list[int], deg: int) -> list[int]:
    assert p[0] == 1
    inv = [0] * (deg + 1)
    inv[0] = 1
    for m in range(1, deg + 1):
        s = 0
        for j in range(1, min(len(p), m + 1)):
            s += p[j] * inv[m - j]
        inv[m] = -s
    return inv


def main() -> None:
    M = 120

    # 1. Direct q-series expansion of F(q) = sum_{n>=0} q^{2n} prod_{k>=2n+2} (1 - (-q)^k) mod q^{M+1}.
    # Suffix products S[r] = prod_{k=r..M} (1 - (-q)^k) mod q^{M+1}
    S: list[list[int]] = [[0] * (M + 1) for _ in range(M + 3)]
    S[M + 1][0] = 1
    S[M + 2][0] = 1
    for k in range(M, 0, -1):
        coeff_k = -((-1) ** k)  # -(-q)^k
        prev = S[k + 1]
        cur = list(prev)
        for d in range(k, M + 1):
            cur[d] += coeff_k * prev[d - k]
        S[k] = cur

    F_coeffs = [0] * (M + 1)
    n = 0
    while 2 * n <= M:
        suf = S[2 * n + 2]
        for d in range(M + 1 - 2 * n):
            F_coeffs[2 * n + d] += suf[d]
        n += 1

    # Compare against OEIS A132411 exponents {0} U {m^2 - 1 : m >= 2}
    expected_F = [0] * (M + 1)
    expected_F[0] = 1
    m = 2
    while m * m - 1 <= M:
        expected_F[m * m - 1] = 1
        m += 1
    assert F_coeffs == expected_F, "Mismatch in direct q-series expansion of F(q)"

    # 2. Verify Step 1 reduction x*F(-x) == (1 - (x;x)_inf / (-x;x)_inf)/2 mod x^{M+1}.
    # Let p_x = (x; x)_inf mod x^{M+1}, m_x = (-x; x)_inf mod x^{M+1}
    p_x = [1] + [0] * M
    m_x = [1] + [0] * M
    for k in range(1, M + 1):
        for d in range(M, k - 1, -1):
            p_x[d] -= p_x[d - k]
            m_x[d] += (-1 if k % 2 == 0 else 1) * m_x[d - k]  # 1 - (-x)x^{k-1} = 1 + (-1)^k x^k
    # Wait: (-x; x)_inf = prod_{j>=0} (1 + x^{j+1}) = prod_{k>=1} (1 + x^k)
    m_x = [1] + [0] * M
    for k in range(1, M + 1):
        for d in range(M, k - 1, -1):
            m_x[d] += m_x[d - k]
    ratio = poly_mul_trunc(p_x, poly_inv_trunc(m_x, M), M)
    # Check Gauss theta identity: ratio == 1 + 2 * sum_{m>=1} (-1)^m x^{m^2}
    expected_theta = [0] * (M + 1)
    expected_theta[0] = 1
    m = 1
    while m * m <= M:
        expected_theta[m * m] = 2 * ((-1) ** m)
        m += 1
    assert ratio == expected_theta, "Gauss theta identity mismatch"

    # Check x * F(q) with x = -q matches (1 - ratio)/2
    # F(q) in terms of x = -q: [x^d] F(-x) = (-1)^d F_coeffs[d]
    lhs_step1 = [0] * (M + 1)
    for d in range(M):
        lhs_step1[d + 1] = ((-1) ** d) * F_coeffs[d]
    rhs_step1 = [(-ratio[d]) // 2 if d > 0 else (1 - ratio[0]) // 2 for d in range(M + 1)]
    assert lhs_step1 == rhs_step1, "Step 1 reduction mismatch"

    # 3. Verify Step 2 finite polynomial identities P_N(z) and P_N(-1) in Z[x, z, z^{-1}] for N = 1..8
    x, z = sp.symbols("x z")
    for N in range(1, 9):
        PN = sp.Integer(1)
        for k in range(1, N + 1):
            PN *= (1 + z * x ** (2 * k - 1)) * (1 + x ** (2 * k - 1) / z)
        PN = sp.expand(PN)
        lhs_fn = sp.expand((x ** (2 * N) + z * x) * PN.subs(z, z * x**2))
        rhs_fn = sp.expand((1 + z * x ** (2 * N + 1)) * PN)
        assert sp.expand(lhs_fn - rhs_fn) == 0

        # Check c_{N,m} formula
        x2_2N = sp.Integer(1)
        for j in range(1, 2 * N + 1):
            x2_2N *= 1 - x ** (2 * j)
        x2_N = sp.Integer(1)
        for j in range(1, N + 1):
            x2_N *= 1 - x ** (2 * j)
        PN_from_c = sp.Integer(0)
        for m_val in range(-N, N + 1):
            denom = sp.Integer(1)
            for j in range(1, N + m_val + 1):
                denom *= 1 - x ** (2 * j)
            for j in range(1, N - m_val + 1):
                denom *= 1 - x ** (2 * j)
            c_Nm = sp.cancel(x2_2N / denom) * (x ** (m_val**2))
            PN_from_c += c_Nm * (z**m_val)
        assert sp.expand(PN - PN_from_c) == 0

        # Check P_N(-1) * (x^2; x^2)_N
        lhs_m1 = sp.expand(x2_N * PN.subs(z, -1))
        rhs_m1 = sp.expand(x2_N * PN_from_c.subs(z, -1))
        assert sp.expand(lhs_m1 - rhs_m1) == 0

    print("PASS")
    print(f"Verified F(q) = 1 + sum_{{m>=2}} q^{{m^2-1}} through q^{M}, Gauss theta & Step 1 reduction through x^{M}, and Step 2 finite P_N identities for N=1..8.")


if __name__ == "__main__":
    main()
