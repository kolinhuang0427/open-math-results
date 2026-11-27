"""Independent exact verifier for targets/oeis-A187430 (Irwin 2017 Catalan g.f. conjecture).

Directly enumerates nonnegative walks via integer DP from the primary OEIS A187430
definition and verifies Steps 1-3 in exact Z[x,y,u,C] / Q[[t]] / Q[[x]] arithmetic
(zero floating point).
"""

import math
import sympy as sp

OEIS_DATA_REV55 = [
    1, 0, 2, 2, 11, 24, 93, 272, 971, 3194, 11293, 39148, 139687, 497756,
    1798002, 6517194, 23807731, 87336870, 322082967, 1192381270, 4431889344,
    16527495396, 61831374003, 231973133544, 872598922407, 3290312724374,
    12434632908623, 47089829065940, 178672856753641,
]


def walk_dp(N: int) -> tuple[list[list[int]], list[int], list[int]]:
    """Exact integer DP for nonnegative walks with steps {-2, -1, +1, +2}."""
    w: list[list[int]] = [[1]]  # w[n][h] for 0 <= h <= 2*n
    for n in range(1, N + 1):
        prev = w[n - 1]
        cur = [0] * (2 * n + 1)
        for h in range(2 * n + 1):
            total = 0
            for step in (-2, -1, 1, 2):
                ph = h - step
                if 0 <= ph < len(prev):
                    total += prev[ph]
            cur[h] = total
        w.append(cur)
    a = [w[n][0] for n in range(N + 1)]
    g1 = [w[n][1] if 1 < len(w[n]) else 0 for n in range(N + 1)]
    return w, a, g1


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
    N = 32
    w, a, g1 = walk_dp(N)

    # 1. Verify primary DP reproduces all 29 live OEIS A187430 rev. 55 terms.
    assert a[: len(OEIS_DATA_REV55)] == OEIS_DATA_REV55, "Mismatch with OEIS A187430 data"

    # 2. Verify Step 1 kernel identity u^2*G(t,u) == u^2 + t*(u^4+u^3+u+1)*G(t,u) - t*(u+1)*A(t) - t*u*G1(t)
    # exact integer coefficient check for all t^n (0 <= n <= N) and u^m (0 <= m <= 2*n+2).
    for n in range(N + 1):
        for m in range(2 * n + 3):
            lhs = w[n][m - 2] if (2 <= m and m - 2 < len(w[n])) else 0
            rhs = 1 if (n == 0 and m == 2) else 0
            if n >= 1:
                prev = w[n - 1]
                for shift in (4, 3, 1, 0):
                    if 0 <= m - shift < len(prev):
                        rhs += prev[m - shift]
                if m in (0, 1):
                    rhs -= a[n - 1]
                if m == 1:
                    rhs -= g1[n - 1]
            assert lhs == rhs, f"Step 1 kernel mismatch at (n, m)=({n}, {m})"

    # 3. Verify Step 2 exact factorization K(t, u) == M(t, u) * Q(t, u) in Q(y)[u].
    u, x, y, C = sp.symbols("u x y C")
    t_sub = y * (1 - y) ** 2 / (1 - y + y**2) ** 2
    s_sub = y / (1 - y)
    K_sub = u**2 - t_sub * (u**4 + u**3 + u + 1)
    M_sub = u**2 - s_sub * u - y
    Q_sub = ((1 - y) ** 2 / (1 - y + y**2) ** 2) * (-y * u**2 - s_sub * u + 1)
    assert sp.cancel(K_sub - M_sub * Q_sub) == 0, "Step 2 kernel factorization K != M*Q"

    # Also verify exact integer series reversion f(t*A(t)) == t mod t^{N+2} and G1(t) == (s(t)-y(t))/t mod t^{N+1}.
    y_ser = [0] + a[:N]  # y_ser[k] = [t^k] t*A(t) for 0 <= k <= N
    y2 = poly_mul_trunc(y_ser, y_ser, N)
    one_minus_y = [1] + [-v for v in y_ser[1:]]
    num = poly_mul_trunc(y_ser, poly_mul_trunc(one_minus_y, one_minus_y, N), N)
    base = [1 if i == 0 else (-y_ser[i] + y2[i]) for i in range(N + 1)]
    den = poly_mul_trunc(base, base, N)
    f_of_y = poly_mul_trunc(num, poly_inv_trunc(den, N), N)
    assert f_of_y == [0, 1] + [0] * (N - 1), f"Series reversion mismatch: {f_of_y}"

    s_ser = poly_mul_trunc(y_ser, poly_inv_trunc(one_minus_y, N), N)
    assert [s_ser[n + 1] - y_ser[n + 1] for n in range(N)] == g1[:N], "G1(t) identity mismatch"

    # 4. Verify Step 3 algebraic identity modulo x*C^2 - C + 1 in Z[x, C].
    step3_poly = sp.expand((1 - x) ** 2 * (1 - C) * C**2 + x * (C**2 - C + 1) ** 2)
    _quot, rem = sp.div(step3_poly, x * C**2 - C + 1, C, x)
    assert rem == 0, f"Step 3 polynomial remainder != 0: {rem}"

    # 5. Direct exact integer formal power series check of Irwin's identity through x^30.
    M_X = 30
    lhs_coeffs = [0] * (M_X + 1)
    lhs_coeffs[0] = 1
    for n in range(M_X):
        sign = -1 if (n % 2 == 1) else 1
        for k in range(M_X - n):
            lhs_coeffs[n + 1 + k] += a[n] * sign * math.comb(2 * n + 1 + k, k)
    catalan_coeffs = [math.comb(2 * m, m) // (m + 1) for m in range(M_X + 1)]
    assert lhs_coeffs == catalan_coeffs, "Irwin g.f. vs Catalan mismatch"

    print("PASS")
    print(
        f"Verified OEIS A187430 data n=0..{len(OEIS_DATA_REV55)-1}, Step 1 kernel (n<={N}), "
        f"Step 2 K=MQ + reversion f(t*A(t))=t (t^{N}), Step 3 mod (xC^2-C+1), and Irwin g.f. == Catalan through x^{M_X}."
    )


if __name__ == "__main__":
    main()
