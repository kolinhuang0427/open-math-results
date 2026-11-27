"""Exact verification script for OEIS A383410 (Mikhail Kurkov conjecture)."""
from fractions import Fraction
from math import comb, factorial


def egf_mul(a, b, deg):
    # Coefficients are EGF coefficients [c_k], representing sum c_k x^k / k!
    res = [Fraction(0)] * (deg + 1)
    for k in range(deg + 1):
        res[k] = sum((comb(k, j) * a[j] * b[k - j] for j in range(k + 1)), Fraction(0))
    return res


def series_inv_power2(D, deg):
    # Compute D^{-2} in QQ[[x]]/(x^{deg+1}) via ordinary power series coefficients
    assert D[0] == 1
    invD = [Fraction(0)] * (deg + 1)
    invD[0] = Fraction(1)
    for k in range(1, deg + 1):
        invD[k] = -sum((D[j] * invD[k - j] for j in range(1, min(k + 1, len(D)))), Fraction(0))
    res = [Fraction(0)] * (deg + 1)
    for i in range(deg + 1):
        for j in range(deg + 1 - i):
            res[i + j] += invD[i] * invD[j]
    return res


def compute_A383410(max_n, max_k):
    # A[n][k] defined on 0 <= n <= max_n, 0 <= k <= max_k + max_n - n
    A = [[1] * (max_k + max_n + 2)]
    for n in range(1, max_n + 1):
        lim = max_k + max_n + 1 - n
        row = []
        for k in range(lim + 1):
            val = sum(
                comb(n - 1, i) * comb(k + 1, j) * A[i][j]
                for i in range(n)
                for j in range(k + 2)
            )
            row.append(val)
        A.append(row)
    return A


def main():
    max_n = 19
    A = compute_A383410(max_n, 6)

    # 1. Verify OEIS A383410 DATA (first 10 downward antidiagonals)
    oeis_A383410_antidiags = [
        1, 1, 2, 1, 4, 8, 1, 8, 22, 44, 1, 16, 62, 154, 308,
        1, 32, 178, 554, 1306, 2612, 1, 64, 518, 2038, 5690, 12994, 25988,
        1, 128, 1522, 7634, 25366, 66338, 148282, 296564,
        1, 256, 4502, 29014, 115298, 346366, 867002, 1908274, 3816548,
        1, 512, 13378, 111554, 532726, 1844042, 5179798, 12564434, 27333706, 54667412,
    ]
    anti = []
    for s in range(10):
        for n in range(s + 1):
            k = s - n
            anti.append(A[n][k])
    assert anti == oeis_A383410_antidiags, "OEIS A383410 DATA mismatch"

    # 2. Verify Step 1 row-EGF identity F_n(y) = sum binom(n-1, i) * d/dy(e^y * F_i(y))
    y_deg = max_n + 6
    F_rows = [[Fraction(1) for _ in range(y_deg + 1)]]  # F_0(y) = e^y -> EGF coeffs 1
    ey_egf = [Fraction(1)] * (y_deg + 1)
    for n in range(1, max_n + 1):
        cur_deg = y_deg - n
        Fn = [Fraction(0)] * (cur_deg + 1)
        for i in range(n):
            c = comb(n - 1, i)
            prod = egf_mul(ey_egf, F_rows[i], cur_deg + 1)
            for k in range(cur_deg + 1):
                Fn[k] += c * prod[k + 1]
        F_rows.append(Fn)
        for k in range(min(6, len(A[n]))):
            assert Fraction(A[n][k]) == Fn[k], f"EGF mismatch at n={n}, k={k}"

    # 3. Verify bivariate PDE identity F(x, y) = e^{-y} / (1 + e^{-y} - e^x)^2
    # Check directly on coefficients [x^n/n! y^k/k!] up to n+k <= 10!
    D_max = 10
    # Compute D(x, y) = 1 + e^{-y} - e^x as bivariate OGF c[n][k] x^n y^k
    # Wait: D(x, y) = 1 + sum_{k>=1} (-1)^k y^k/k! - sum_{n>=1} x^n/n!
    D_bi = [[Fraction(0)] * (D_max + 1) for _ in range(D_max + 1)]
    D_bi[0][0] = Fraction(1)
    for k in range(1, D_max + 1):
        D_bi[0][k] = Fraction((-1) ** k, factorial(k))
    for n in range(1, D_max + 1):
        D_bi[n][0] = Fraction(-1, factorial(n))
    # Compute 1/D_bi in QQ[[x, y]]/(x,y)^{D_max+1}
    invD_bi = [[Fraction(0)] * (D_max + 1) for _ in range(D_max + 1)]
    invD_bi[0][0] = Fraction(1)
    for tot in range(1, D_max + 1):
        for n in range(tot + 1):
            k = tot - n
            s = Fraction(0)
            for a in range(n + 1):
                for b in range(k + 1):
                    if a == 0 and b == 0:
                        continue
                    s += D_bi[a][b] * invD_bi[n - a][k - b]
            invD_bi[n][k] = -s
    # U_bi = invD_bi^2, F_bi = e^{-y} * U_bi
    U_bi = [[Fraction(0)] * (D_max + 1) for _ in range(D_max + 1)]
    for n in range(D_max + 1):
        for k in range(D_max + 1 - n):
            U_bi[n][k] = sum(
                invD_bi[a][b] * invD_bi[n - a][k - b]
                for a in range(n + 1)
                for b in range(k + 1)
            )
    for n in range(D_max + 1):
        for k in range(D_max + 1 - n):
            f_nk = sum(
                Fraction((-1) ** b, factorial(b)) * U_bi[n][k - b]
                for b in range(k + 1)
            )
            assert f_nk * factorial(n) * factorial(k) == A[n][k], f"Bivariate mismatch at ({n},{k})"

    # 4. Verify (2 - e^x)^{-2} equals A005649 DATA (n = 0..19) and A(n, 0)
    D_x = [Fraction(2)] + [Fraction(-1, factorial(n)) for n in range(1, max_n + 1)]
    # Wait: D_x[0] = 1 for (1 - (e^x - 1)), wait 2 - e^x = 1 - (e^x - 1) so use D_x[0]=1
    D_x[0] = Fraction(1)
    U_x = series_inv_power2(D_x, max_n)
    oeis_A005649 = [
        1, 2, 8, 44, 308, 2612, 25988, 296564, 3816548, 54667412,
        862440068, 14857100084, 277474957988, 5584100659412, 120462266974148,
        2772968936479604, 67843210855558628, 1757952715142990612,
        48093560991292628228, 1385244691781856307124,
    ]
    for n in range(max_n + 1):
        val = U_x[n] * factorial(n)
        assert val.denominator == 1
        assert int(val) == oeis_A005649[n] == A[n][0], f"Mismatch at n={n}"

    print("PASS")


if __name__ == "__main__":
    main()
