#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A188648 (Velin Yanev, Oct 31 2019).

Zero floating-point operations: pure Python int and fractions.Fraction.
"""

from __future__ import annotations

from fractions import Fraction
import math
import sys

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
    res = Fraction(1)
    for i in range(k):
        res *= x + i
    return res


def a_def(n: int) -> int:
    return sum(math.comb(2 * n - j, j) ** 2 for j in range(n + 1))


def main() -> int:
    a_vals = [a_def(n) for n in range(31)]
    assert a_vals[: len(OEIS_DATA)] == OEIS_DATA, "Mismatch against OEIS A188648 DATA"

    half = Fraction(1, 2)
    sixteenth = Fraction(1, 16)
    for n in range(31):
        hyper_sum = Fraction(0)
        for k in range(n + 2):  # include k = n + 1 to verify termination
            num = (rising_factorial(Fraction(-n), k) ** 2) * (rising_factorial(Fraction(n + 1), k) ** 2)
            den = (rising_factorial(half, k) ** 2) * rising_factorial(Fraction(1), k) * Fraction(math.factorial(k))
            term = (num / den) * (sixteenth ** k)
            if k <= n:
                expected_term = Fraction(math.comb(n + k, 2 * k) ** 2)
                assert term == expected_term, f"Termwise identity failed at n={n}, k={k}"
                hyper_sum += term
            else:
                assert term == 0, f"Series failed to vanish at k={k} > n={n}"
        assert hyper_sum == Fraction(a_vals[n]), f"Total sum failed at n={n}"

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
