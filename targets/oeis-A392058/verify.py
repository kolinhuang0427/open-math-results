"""Exact verification script for OEIS A392058 (Mikhail Kurkov conjecture)."""
from fractions import Fraction
from math import comb, factorial


def egf_mul(a, b, deg):
    res = [Fraction(0)] * (deg + 1)
    for k in range(deg + 1):
        res[k] = sum((comb(k, j) * a[j] * b[k - j] for j in range(k + 1)), Fraction(0))
    return res


def ogf_mul(a, b, deg):
    res = [Fraction(0)] * (deg + 1)
    for i in range(min(len(a), deg + 1)):
        if a[i] == 0:
            continue
        for j in range(min(len(b), deg + 1 - i)):
            res[i + j] += a[i] * b[j]
    return res


def ogf_inv(a, deg):
    assert a[0] != 0
    inv0 = Fraction(1) / a[0]
    res = [Fraction(0)] * (deg + 1)
    res[0] = inv0
    for k in range(1, deg + 1):
        s = sum((a[j] * res[k - j] for j in range(1, min(k + 1, len(a)))), Fraction(0))
        res[k] = -s * inv0
    return res


def ogf_compose(F, g, deg):
    # Compute F(g(u)) mod u^{deg+1} where g[0] == 0
    assert g[0] == 0
    res = [Fraction(0)] * (deg + 1)
    g_pow = [Fraction(0)] * (deg + 1)
    g_pow[0] = Fraction(1)
    for k in range(min(len(F), deg + 1)):
        fk = F[k]
        if fk != 0:
            for i in range(deg + 1):
                res[i] += fk * g_pow[i]
        if k < deg:
            g_pow = ogf_mul(g_pow, g, deg)
    return res


def compute_A392058(max_n):
    # Compute full downward antidiagonals 0..max_n
    # Row n valid up to k <= max_n - n + 1
    size = max_n + 2
    A = [[1] * size]
    col0 = [1]
    for _ in range(1, max_n + 1):
        A.append([])
    for s in range(1, max_n + 1):
        for k in range(s - 1, -1, -1):
            n = s - k
            # compute A(n, k)
            val = A[n - 1][k + 1] + sum(
                comb(k + 1, j) * A[n - 1][j] * A[k - j][0]
                for j in range(k + 1)
            )
            while len(A[n]) <= k:
                A[n].append(0)
            A[n][k] = val
        # Also extend row 0..s? Wait: for s = n+k, we need A(n-1, j) for j<=k (sum n-1+j <= s-1)
        # and A(k-j, 0) (sum k-j <= s-1), and A(n-1, k+1) (sum n+k = s, ALREADY computed earlier in loop!)
        col0.append(A[s][0])
    # Recompute rectangular grid up to n <= 10, k <= 10 using antidiagonals up to 20
    return A, col0


def main():
    max_diag = 21
    A_tri, _ = compute_A392058(max_diag)

    # 1. Verify OEIS A392058 DATA (first 9 downward antidiagonals)
    oeis_A392058_data = [
        1, 1, 2, 1, 5, 7, 1, 17, 31, 38, 1, 83, 178, 254, 292,
        1, 578, 1330, 2099, 2683, 2975,
        1, 5474, 12748, 21338, 29425, 35375, 38350,
        1, 66932, 153136, 263870, 382966, 489383, 566083, 604433,
        1, 1014002, 2249503, 3913556, 5865952, 7837136, 9538360, 10747226, 11351659,
    ]
    anti = []
    for s in range(9):
        for n in range(s + 1):
            k = s - n
            anti.append(A_tri[n][k])
    assert anti == oeis_A392058_data, "OEIS A392058 DATA mismatch"

    # Extract col0 up to max_n = 21 (valid since antidiagonal 21 has A[21][0])
    max_n = 21
    col0 = [A_tri[n][0] for n in range(max_n + 1)]

    # 2. Verify Step 1 operator identity H_n(y) = d/dy(V(y) * H_{n-1}(y)) up to n+k <= max_diag
    # V(y) = 1 + sum_{m>=1} A(m-1, 0) y^m / m! -> OGF coeffs
    V_ogf = [Fraction(1)] + [Fraction(col0[m - 1], factorial(m)) for m in range(1, max_n + 2)]
    # Check H_n(y) as OGF coeffs up to deg max_n - n
    H_ogf = [Fraction(1, factorial(k)) for k in range(max_n + 2)]
    for n in range(1, 13):
        prod = ogf_mul(V_ogf, H_ogf, max_n + 2 - n)
        H_ogf = [(k + 1) * prod[k + 1] for k in range(max_n + 2 - n)]
        for k in range(min(6, max_n + 1 - n)):
            assert H_ogf[k] * factorial(k) == A_tri[n][k], f"H_n operator mismatch at ({n},{k})"

    # 3. Verify V(integral_0^u dt/V(t)) == exp(u) directly in QQ[[u]]/(u^{max_n+2})
    deg = max_n + 1
    invV = ogf_inv(V_ogf, deg)
    Phi = [Fraction(0)] + [invV[m - 1] / m for m in range(1, deg + 1)]
    comp = ogf_compose(V_ogf, Phi, deg)
    exp_u = [Fraction(1, factorial(m)) for m in range(deg + 1)]
    assert comp == exp_u, "Functional equation V(Phi(u)) == exp(u) failed"

    # 4. Verify OEIS A233335 DATA (0..21) and A(n, 0) == A233335(n + 1)
    oeis_A233335 = [
        1, 1, 2, 7, 38, 292, 2975, 38350, 604433, 11351659, 249042701,
        6283114723, 179995680530, 5794486077958, 207806806310354,
        8241414107222095, 359171801820266717, 17107537203463252273,
        886296777786378900077, 49732564234138336160086, 3011177123882906437153214,
        196063383282648338166793297,
    ]
    a233335_from_V = []
    for m in range(max_n + 2):
        val = V_ogf[m] * factorial(m)
        assert val.denominator == 1
        a233335_from_V.append(int(val))
    assert a233335_from_V[: len(oeis_A233335)] == oeis_A233335, "OEIS A233335 DATA mismatch"
    for n in range(max_n + 1):
        assert col0[n] == a233335_from_V[n + 1], f"Conjecture failed at n={n}"

    print("PASS")


if __name__ == "__main__":
    main()
