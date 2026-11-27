#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A077026 refutation (Benedict Irwin, Sep 22 2016).

Zero floating-point operations: pure Python int arithmetic.
"""

from __future__ import annotations

import sys

OEIS_DATA = [
    1, 2, 2, 4, 3, 5, 5, 6, 6, 8, 6, 10, 9, 9, 9, 13, 11, 12, 12, 14,
    14, 16, 12, 18, 17, 17, 17, 19, 17, 21, 21, 22, 20, 22, 20, 26, 26,
    24, 22, 28, 25, 29, 27, 29, 29, 29, 27, 33, 33, 32, 32, 36, 30, 34,
    34, 38, 38, 38, 34, 40, 39, 39, 37, 43, 41, 45, 43, 41, 41, 45, 43,
    50, 48,
]


def a_def(n: int) -> int:
    # floor(n/k + 1) - floor(n/k + 1/2) = (n // k + 1) - ((2*n + k) // (2*k))
    return sum((n // k + 1) - ((2 * n + k) // (2 * k)) for k in range(1, n + 1))


def irwin_f(a: int, b: int) -> int:
    m = abs(a - b)
    assert m > 0
    return 1 if ((a + b) % m != (a % m) + (b % m)) else 0


def conj_rhs(n: int) -> int:
    return sum(1 - irwin_f(n, k) for k in range(1, n))


def main() -> int:
    a_vals = [a_def(n) for n in range(1, 201)]
    assert a_vals[: len(OEIS_DATA)] == OEIS_DATA, "Mismatch against OEIS A077026 DATA"

    # Explicit minimal counterexample n = 1 and n = 2
    assert a_def(1) == 1 and conj_rhs(1) == 0 and conj_rhs(1) != a_def(1)
    assert a_def(2) == 2 and conj_rhs(2) == 1 and conj_rhs(2) != a_def(2)

    # Exact discrepancy theorem for n = 1..200 and termwise correspondence
    for n in range(1, 201):
        for d in range(1, n):
            k = n - d
            term_a = (n // d + 1) - ((2 * n + d) // (2 * d))
            term_s = 1 - irwin_f(n, k)
            expected = 1 if 2 * (n % d) < d else 0
            assert term_a == expected and term_s == expected
        assert ((n // n + 1) - ((2 * n + n) // (2 * n))) == 1
        assert conj_rhs(n) == a_def(n) - 1, f"Discrepancy mismatch at n={n}"

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
