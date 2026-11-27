"""Exact-arithmetic verification for OEIS A188648 (Velin Yanev 2019 conjecture)."""

from fractions import Fraction
import math


OEIS_DATA = [
    1,
    2,
    11,
    63,
    376,
    2317,
    14545,
    92512,
    594169,
    3844787,
    25027296,
    163701327,
    1075049011,
    7083830648,
    46812088751,
    310118453573,
    2058919125662,
    13695571200353,
    91254952276859,
    608960974528058,
    4069232436916151,
]


def rising_factorial(x: Fraction, k: int) -> Fraction:
    res = Fraction(1, 1)
    for i in range(k):
        res *= x + i
    return res


def a_primary(n: int) -> int:
    return sum(math.comb(2 * n - j, j) ** 2 for j in range(n + 1))


def a_hypergeom(n: int) -> Fraction:
    total = Fraction(0, 1)
    for k in range(n + 1):
        num = rising_factorial(Fraction(-n), k) ** 2 * rising_factorial(Fraction(n + 1), k) ** 2
        den = (
            rising_factorial(Fraction(1, 2), k) ** 2
            * rising_factorial(Fraction(1), k)
            * math.factorial(k)
            * (16 ** k)
        )
        total += num / den
    return total


def main() -> None:
    for n, expected in enumerate(OEIS_DATA):
        if a_primary(n) != expected:
            print(f"FAIL: OEIS_DATA mismatch at n={n}")
            raise SystemExit(1)

    for n in range(0, 101):
        lhs = a_primary(n)
        rhs = a_hypergeom(n)
        if rhs.denominator != 1 or rhs.numerator != lhs:
            print(f"FAIL: mismatch at n={n}: {lhs} != {rhs}")
            raise SystemExit(1)
        # Also verify the termwise identity for all 0 <= k <= n on n <= 40
        if n <= 40:
            for k in range(n + 1):
                num = rising_factorial(Fraction(-n), k) * rising_factorial(Fraction(n + 1), k)
                den = rising_factorial(Fraction(1, 2), k) * math.factorial(k) * (4 ** k)
                term = (num / den) ** 2
                binom_sq = Fraction(math.comb(n + k, 2 * k) ** 2, 1)
                if term != binom_sq:
                    print(f"FAIL: termwise mismatch at n={n}, k={k}")
                    raise SystemExit(1)

    print("PASS")


if __name__ == "__main__":
    main()
