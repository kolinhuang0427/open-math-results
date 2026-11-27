"""Exact-arithmetic verification for OEIS A075997 (Irwin 2016 conjecture)."""


OEIS_DATA = [
    0, 0, 1, 0, 2, 1, 2, 1, 4, 2, 3, 2, 5, 4, 5, 2, 6, 5, 6, 5, 8, 5, 6, 5, 10,
    8, 9, 6, 9, 8, 9, 8, 13, 10, 11, 8, 12, 11, 12, 9, 14, 13, 14, 13, 16, 11,
    12, 11, 18, 16, 17, 14, 17, 16, 17, 14, 19, 16, 17, 16, 21, 20, 21, 16, 22,
    19, 20, 19, 22, 19, 20, 19, 26, 25, 26, 21, 24, 21, 22, 21,
]


def a_primary(n: int) -> int:
    total = 0
    for k in range(2, n + 1):
        sign = 1 if (k % 2 == 0) else -1
        total += sign * (n // k)
    return total


def f_irwin(a: int, b: int) -> int:
    d = abs(a - b)
    return 1 if ((a + b) % d) != ((a % d) + (b % d)) else 0


def irwin_sum(n: int) -> int:
    return sum(f_irwin(n + k, n - k) for k in range(1, n))


def main() -> None:
    for n, expected in enumerate(OEIS_DATA):
        if a_primary(n) != expected:
            print(f"FAIL: OEIS_DATA mismatch at n={n}")
            raise SystemExit(1)

    for n in range(0, 401):
        a_n = a_primary(n)
        parity_sum = sum(1 for k in range(1, n) if (n // k) % 2 == 0)
        s_n = irwin_sum(n)
        if a_n != parity_sum or a_n != s_n:
            print(f"FAIL: mismatch at n={n}: a={a_n}, parity={parity_sum}, irwin={s_n}")
            raise SystemExit(1)

    print("PASS")


if __name__ == "__main__":
    main()
