"""Exact-arithmetic verification for OEIS A124380 (Kotesovec 2024 conjecture)."""

import math


OEIS_DATA = [
    1, 1, 2, 4, 9, 22, 57, 157, 453, 1368, 4296, 13995, 47138, 163779, 585741,
    2152349, 8113188, 31326760, 123748871, 499539900, 2058542819, 8651755865,
    37054078481, 161591063250, 717032333816, 3235298221401, 14834735654080,
    69085973044125, 326600050947885, 1566556077233897,
]


def compute_a_series(max_n: int) -> list[int]:
    """Compute a(0)..a(max_n) directly from sum_{m>=0} x^m prod_{k=0..m} (1 + k*x)."""
    a = [0] * (max_n + 1)
    for m in range(max_n + 1):
        # poly[r] = e_r(1..m) for r <= min(m, max_n - m)
        max_r = min(m, max_n - m)
        poly = [0] * (max_r + 1)
        poly[0] = 1
        for k in range(1, m + 1):
            upper = min(k, max_r)
            for r in range(upper, 0, -1):
                poly[r] += k * poly[r - 1]
        for r in range(max_r + 1):
            a[m + r] += poly[r]
    return a


def elem_sym_table(max_m: int) -> list[list[int]]:
    """Return table e[m][r] = e_r(1..m) via e_r(1..m) = e_r(1..m-1) + m*e_{r-1}(1..m-1)."""
    e = [[0] * (max_m + 1) for _ in range(max_m + 1)]
    e[0][0] = 1
    for m in range(1, max_m + 1):
        e[m][0] = 1
        for r in range(1, m + 1):
            e[m][r] = e[m - 1][r] + m * e[m - 1][r - 1]
    return e


def ceil_pow_3_4(x: int) -> int:
    """Smallest integer c >= 0 with c^4 >= x^3 (exact integer arithmetic)."""
    target = x ** 3
    lo, hi = 0, x + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if mid ** 4 >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


def main() -> None:
    max_n = 80
    a = compute_a_series(max_n)

    # 1. Verify OEIS DATA
    for n, expected in enumerate(OEIS_DATA):
        if a[n] != expected:
            print(f"FAIL: OEIS_DATA mismatch at n={n}: {a[n]} != {expected}")
            raise SystemExit(1)

    # 2. Verify Step 1 elementary symmetric polynomial identity and Lemma 1 bounds for n=4..max_n
    e_tbl = elem_sym_table(max_n)
    for n in range(4, max_n + 1):
        k = n // 2
        sum_e = sum(e_tbl[n - r][r] for r in range(k + 1))
        if sum_e != a[n]:
            print(f"FAIL: Step 1 mismatch at n={n}")
            raise SystemExit(1)

        # Verify termwise e_r(1..n-r) <= ((k+1+t)!)^2 / ((k-t)! (2t)!)^2 * ...
        kfact = math.factorial(k)
        for r in range(k + 1):
            t = k - r
            m = n - r
            term_bound = (
                math.factorial(k + 1 + t) ** 2
                // (math.factorial(k - t) * (math.factorial(2 * t) ** 2))
            )
            if e_tbl[m][r] > term_bound:
                print(f"FAIL: term bound failed at n={n}, r={r}")
                raise SystemExit(1)

        # Verify global Lemma 1 bounds using e < 3:
        # k! <= a(n) <= (k+1) * (2k+1)^(9 * ceil((2k+1)^(3/4)) + 2) * k!
        c34 = ceil_pow_3_4(2 * k + 1)
        upper = (k + 1) * ((2 * k + 1) ** (9 * c34 + 2)) * kfact
        if not (kfact <= a[n] <= upper):
            print(f"FAIL: Lemma 1 global bound failed at n={n}")
            raise SystemExit(1)

    print("PASS")


if __name__ == "__main__":
    main()
