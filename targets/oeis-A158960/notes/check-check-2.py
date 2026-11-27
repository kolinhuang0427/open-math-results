"""Independent exact-rational verifier for targets/oeis-A158960.

Directly computes H_n(1/5) in exact fractions.Fraction from the physicists' Hermite
recurrence, verifies reduced denominator == 5^n, b(n) mod 5 == 2^n mod 5 != 0,
and matches all 18 live OEIS A158960 rev. 28 data terms (zero floating point).
"""

from fractions import Fraction
import math

OEIS_DATA_REV28 = [
    1,
    2,
    -46,
    -292,
    6316,
    71032,
    -1436936,
    -24183472,
    454560656,
    10582510112,
    -183387274976,
    -5658029605952,
    89546942024896,
    3573911647620992,
    -51057689020940416,
    -2603853531376575232,
    33085559702952161536,
    2149253944507164508672,
]


def main() -> None:
    N = 100
    x = Fraction(1, 5)
    H = [Fraction(0)] * (N + 1)
    H[0] = Fraction(1)
    H[1] = 2 * x
    for n in range(2, N + 1):
        H[n] = 2 * x * H[n - 1] - 2 * (n - 1) * H[n - 2]

    b = [0] * (N + 1)
    b[0], b[1] = 1, 2
    for n in range(2, N + 1):
        b[n] = 2 * b[n - 1] - 50 * (n - 1) * b[n - 2]

    for n in range(N + 1):
        assert H[n] == Fraction(b[n], 5**n)
        assert H[n].denominator == 5**n, f"Denominator mismatch at n={n}: {H[n].denominator}"
        assert H[n].numerator == b[n]
        assert b[n] % 5 == pow(2, n, 5) != 0

        # Cross-check Greubel's explicit formula on OEIS A158960 for n <= 40
        if n <= 40:
            explicit = sum(
                ((-1) ** k) * (math.factorial(n) // (math.factorial(k) * math.factorial(n - 2 * k)))
                * (2 ** (n - 2 * k))
                * (5 ** (2 * k))
                for k in range(n // 2 + 1)
            )
            assert explicit == b[n]

    assert b[: len(OEIS_DATA_REV28)] == OEIS_DATA_REV28, "Mismatch with OEIS A158960 data"

    print("PASS")
    print(f"Verified OEIS A158960 data n=0..{len(OEIS_DATA_REV28)-1}, exact Fraction H_n(1/5) denominator == 5^n and b(n)==2^n (mod 5) for 0 <= n <= {N}.")


if __name__ == "__main__":
    main()
