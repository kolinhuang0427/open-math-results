#!/usr/bin/env python3
"""Exact-arithmetic verification for OEIS A158960 Hasler (2014) conjecture."""

from fractions import Fraction
import math


def main():
    N = 200
    # 1. Compute H_n(1/5) exactly in Q from the primary Hermite recurrence
    H = [Fraction(1), Fraction(2, 5)]
    for n in range(2, N + 1):
        H.append(Fraction(2, 5) * H[n - 1] - 2 * (n - 1) * H[n - 2])

    # 2. Cross-check against explicit polynomial expansion of Hermite(n, 1/5)
    for n in range(51):
        explicit = Fraction(0)
        for k in range(n // 2 + 1):
            coeff = ((-1) ** k) * math.factorial(n) // (math.factorial(k) * math.factorial(n - 2 * k))
            explicit += coeff * (Fraction(2, 5) ** (n - 2 * k))
        assert H[n] == explicit, f"Explicit Hermite mismatch at n={n}"

    # 3. Verify reduced denominator is exactly 5^n and b(n) == 2^n (mod 5)
    for n in range(N + 1):
        assert H[n].denominator == 5 ** n, f"Denominator mismatch at n={n}: {H[n].denominator}"
        b = H[n].numerator
        assert b == int(H[n] * (5 ** n))
        assert b % 5 == pow(2, n, 5) != 0

    # 4. Verify OEIS DATA terms a(0..17)
    oeis_data = [
        1, 2, -46, -292, 6316, 71032, -1436936, -24183472, 454560656,
        10582510112, -183387274976, -5658029605952, 89546942024896,
        3573911647620992, -51057689020940416, -2603853531376575232,
        33085559702952161536, 2149253944507164508672,
    ]
    assert [H[n].numerator for n in range(len(oeis_data))] == oeis_data, "OEIS DATA mismatch"

    print("PASS")


if __name__ == "__main__":
    main()
