"""Exact-arithmetic verification for OEIS A077026 (counterexample & exact offset)."""

from fractions import Fraction


OEIS_DATA = [
    1, 2, 2, 4, 3, 5, 5, 6, 6, 8, 6, 10, 9, 9, 9, 13, 11, 12, 12, 14, 14, 16,
    12, 18, 17, 17, 17, 19, 17, 21, 21, 22, 20, 22, 20, 26, 26, 24, 22, 28,
    25, 29, 27, 29, 29, 29, 27, 33, 33, 32, 32, 36, 30, 34, 34, 38, 38, 38,
    34, 40, 39, 39, 37, 43, 41, 45, 43, 41, 41, 45, 43, 50, 48,
]


def floor_frac(num: int, den: int) -> int:
    return num // den


def a_primary(n: int) -> int:
    total = 0
    for k in range(1, n + 1):
        t1 = floor_frac(n + k, k)          # floor(n/k + 1)
        t2 = floor_frac(2 * n + k, 2 * k)  # floor(n/k + 1/2)
        total += t1 - t2
    return total


def f_irwin(a: int, b: int) -> int:
    d = abs(a - b)
    return 1 if ((a + b) % d) != ((a % d) + (b % d)) else 0


def irwin_sum(n: int) -> int:
    return sum(1 - f_irwin(n, k) for k in range(1, n))


def main() -> None:
    for idx, expected in enumerate(OEIS_DATA, start=1):
        if a_primary(idx) != expected:
            print(f"FAIL: OEIS_DATA mismatch at n={idx}")
            raise SystemExit(1)

    # Confirm minimal counterexample n=1 and universal failure + exact offset for n=1..400
    if a_primary(1) != 1 or irwin_sum(1) != 0:
        print("FAIL: minimal counterexample n=1 check failed")
        raise SystemExit(1)

    for n in range(1, 401):
        a_n = a_primary(n)
        s_n = irwin_sum(n)
        if s_n == a_n or s_n != a_n - 1:
            print(f"FAIL: unexpected equality/offset at n={n}: a={a_n}, s={s_n}")
            raise SystemExit(1)

    print("PASS")


if __name__ == "__main__":
    main()
