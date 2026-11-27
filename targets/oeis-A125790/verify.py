import math
import signal
from fractions import Fraction

signal.alarm(30)

OEIS_ANTIDIAG = [
    1,1,1,1,2,1,1,4,3,1,1,10,9,4,1,1,36,35,16,5,1,1,202,201,84,25,6,1,1,1828,
    1827,656,165,36,7,1,1,27338,27337,8148,1625,286,49,8,1,1,692004,692003,
    167568,25509,3396,455,64,9,1,1,30251722,30251721,5866452,664665,64350,
    6321,680,81,10,1
]


def compute_T(max_n: int, max_k: int):
    # Need T(0, 0..max_k * 2^max_n)? No! If we only need T(n, k) for k <= max_k_at_n,
    # compute by rows dynamically or size K_top = max_k * (1 << max_n) when max_n small!
    # Wait: for max_n = 10, max_k = 15, K_top = 15 * 1024 = 15360 — tiny!
    K_needed = max_k
    rows = {}
    # Compute needed max_k at each row n: row n needs up to K_n
    limits = [0] * (max_n + 1)
    limits[max_n] = max_k
    for r in range(max_n - 1, -1, -1):
        limits[r] = 2 * limits[r + 1]
    rows[0] = [1] * (limits[0] + 1)
    for n in range(1, max_n + 1):
        row = [1] * (limits[n] + 1)
        prev = rows[n - 1]
        for k in range(1, limits[n] + 1):
            row[k] = row[k - 1] + prev[2 * k]
        rows[n] = row
    return rows


def main():
    # 1. Match OEIS antidiagonal data (rows/cols n+k <= 10)
    rows_diag = compute_T(10, 10)
    antidiag = []
    for d in range(11):
        for k in range(d + 1):
            n = d - k
            antidiag.append(rows_diag[n][k])
    assert antidiag == OEIS_ANTIDIAG

    # 2. Verify Step 1 polynomiality & P_n(-1) == 0, plus Step 2 row GF for n = 1..12 up to x^25!
    max_n = 12
    max_deg = 25
    rows = compute_T(max_n, max_deg)

    for n in range(1, max_n + 1):
        T_row = rows[n][: max_deg + 1]
        # Compute c_i = coeff of x^i in (1 - x)^{n+1} * sum T(n,k) x^k
        coeffs = []
        for i in range(max_deg + 1):
            c_i = sum(
                math.comb(n + 1, j) * T_row[i - j] * ((-1) ** j)
                for j in range(min(i, n + 1) + 1)
            )
            coeffs.append(c_i)
        # Verify ALL c_i == 0 for i >= n!
        assert all(c == 0 for c in coeffs[n:]), f"Failed at n={n}: {coeffs[n:]}"

        # Also explicitly check Step 1 polynomial interpolation & P_n(-1) == 0
        # Backward difference at t=n gives P_n(-1) directly:
        pn_minus_1 = sum(
            ((-1) ** (j + 1)) * math.comb(n + 1, j) * T_row[n - j]
            for j in range(n + 1)
        ) * ((-1) ** (n + 1))
        assert pn_minus_1 == 0

    print(f"PASS: OEIS A125790 (66 antidiagonal terms) matched verbatim; "
          f"P_n(-1)=0 and row g.f. numerator degree <= n-1 verified to x^{max_deg} for all 1 <= n <= {max_n}.")


if __name__ == "__main__":
    main()
