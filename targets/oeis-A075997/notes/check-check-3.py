#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A075997 (Benedict Irwin, Sep 23 2016).

Zero floating-point operations: pure Python int arithmetic.
"""

from __future__ import annotations

import sys

OEIS_DATA = [
    0, 0, 1, 0, 2, 1, 2, 1, 4, 2, 3, 2, 5, 4, 5, 2, 6, 5, 6, 5, 8, 5, 6, 5,
    10, 8, 9, 6, 9, 8, 9, 8, 13, 10, 11, 8, 12, 11, 12, 9, 14, 13, 14, 13, 16,
    11, 12, 11, 18, 16, 17, 14, 17, 16, 17, 14, 19, 16, 17, 16, 21, 20, 21, 16,
    22, 19, 20, 19, 22, 19, 20, 19, 26, 25, 26, 21, 24, 21, 22, 21,
]


def a_def(n: int) -> int:
    return sum((n // m if m % 2 == 0 else -(n // m)) for m in range(2, n + 1))


def irwin_f(a: int, b: int) -> int:
    m = abs(a - b)
    assert m > 0
    return 1 if ((a + b) % m != (a % m) + (b % m)) else 0


def conj_rhs(n: int) -> int:
    return sum(irwin_f(n + k, n - k) for k in range(1, n))


def main() -> int:
    a_vals = [a_def(n) for n in range(201)]
    assert a_vals[: len(OEIS_DATA)] == OEIS_DATA, "Mismatch against OEIS A075997 DATA"

    for n in range(201):
        parity_count = sum(1 for k in range(1, n) if (n // k) % 2 == 0)
        assert a_vals[n] == parity_count, f"Step 1 parity identity failed at n={n}"
        for k in range(1, n):
            fk = irwin_f(n + k, n - k)
            expected = 1 if (n // k) % 2 == 0 else 0
            assert fk == expected, f"Step 2 equivalence failed at n={n}, k={k}"
        assert conj_rhs(n) == a_vals[n], f"Conjecture mismatch at n={n}"

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
