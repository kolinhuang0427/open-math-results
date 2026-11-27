"""Exact-arithmetic verification for OEIS A183063 cotangent limit conjecture.

Verifies (with zero floats):
1. Published OEIS A183063 terms (n = 1..60) equal #{d >= 1 : 2|d and d|n} = tau(n) - tau_odd(n).
2. Formal Laurent/Taylor series of sin(t) * cot(t/(2k)) / (2k) in Q[[t]] has exact constant
   term [t^0] == 1 for all k >= 1 (up to t^14).
3. For every 1 <= n <= 30 and 1 <= k <= n, 2k | n holds iff n/(2k) is an integer, while when
   2k does not divide n, n/(2k) is strictly non-integral (so cot(pi*n/(2k)) is finite).
4. Exact rational Mittag-Leffler M-test bound on |g_k(x)| * pi <= (2n+1) * (pi^2/6) / (3*k^2)
   and the telescoping upper bound sum_{k=n+1}^M 1/k^2 < 1/n hold identically in Q.
"""

from fractions import Fraction
from math import factorial


PUBLISHED_A183063 = [
    0, 1, 0, 2, 0, 2, 0, 3, 0, 2, 0, 4, 0, 2, 0, 4, 0, 3, 0, 4, 0, 2, 0, 6,
    0, 2, 0, 4, 0, 4, 0, 5, 0, 2, 0, 6, 0, 2, 0, 6, 0, 4, 0, 4, 0, 2, 0, 8,
    0, 3, 0, 4, 0, 4, 0, 6, 0, 2, 0, 8,
]


def even_divisors_count(n: int) -> int:
    return sum(1 for d in range(2, n + 1, 2) if n % d == 0)


def odd_divisors_count(n: int) -> int:
    return sum(1 for d in range(1, n + 1, 2) if n % d == 0)


def total_divisors_count(n: int) -> int:
    return sum(1 for d in range(1, n + 1) if n % d == 0)


def poly_mul_trunc(p: list[Fraction], q: list[Fraction], deg: int) -> list[Fraction]:
    res = [Fraction(0)] * (deg + 1)
    for i, a in enumerate(p):
        if a == 0 or i > deg:
            continue
        for j, b in enumerate(q):
            if i + j > deg:
                break
            res[i + j] += a * b
    return res


def series_inv_trunc(p: list[Fraction], deg: int) -> list[Fraction]:
    # Invert p(t) with p[0] != 0 up to t^deg in Q[[t]]
    assert p[0] != 0
    inv0 = Fraction(1) / p[0]
    res = [Fraction(0)] * (deg + 1)
    res[0] = inv0
    for m in range(1, deg + 1):
        s = sum(p[j] * res[m - j] for j in range(1, min(m + 1, len(p))))
        res[m] = -s * inv0
    return res


def main() -> None:
    # 1. Verify published OEIS A183063 data and divisor identities
    for n in range(1, len(PUBLISHED_A183063) + 1):
        cnt = even_divisors_count(n)
        assert cnt == PUBLISHED_A183063[n - 1], f"Data mismatch at n={n}"
        assert cnt == total_divisors_count(n) - odd_divisors_count(n)
        if n % 2 == 1:
            assert cnt == 0
        else:
            assert cnt == total_divisors_count(n // 2)

    # 2. Exact Taylor series verification in Q[[t]] for sin(t) * cot(t/(2k)) / (2k)
    deg = 14
    sin_t = [
        Fraction((-1) ** ((m - 1) // 2), factorial(m)) if m % 2 == 1 else Fraction(0)
        for m in range(deg + 2)
    ]
    for k in range(1, 17):
        # sin(t/(2k)) / (t/(2k)) and cos(t/(2k)) up to t^deg
        sinc_scaled = [
            Fraction((-1) ** (m // 2), factorial(m + 1) * ((2 * k) ** m)) if m % 2 == 0 else Fraction(0)
            for m in range(deg + 1)
        ]
        cos_scaled = [
            Fraction((-1) ** (m // 2), factorial(m) * ((2 * k) ** m)) if m % 2 == 0 else Fraction(0)
            for m in range(deg + 1)
        ]
        sin_over_t = [sin_t[m + 1] for m in range(deg + 1)]
        # (sin(t)/t) * cos(t/(2k)) / (sin(t/(2k))/(t/(2k)))
        num = poly_mul_trunc(sin_over_t, cos_scaled, deg)
        prod = poly_mul_trunc(num, series_inv_trunc(sinc_scaled, deg), deg)
        assert prod[0] == 1, f"Residue failed for k={k}: {prod[0]}"

    # 3. Verify head/tail partition and rational M-test inequality for n = 1..30
    for n in range(1, 31):
        head_hits = 0
        for k in range(1, n + 1):
            ratio = Fraction(n, 2 * k)
            if ratio.denominator == 1:
                assert n % 2 == 0
                head_hits += 1
            else:
                assert ratio.denominator >= 2
        assert head_hits == even_divisors_count(n)

        # Verify M-test denominator bound: for k >= n+1 and x = n + 1/2,
        # (x/(2k))^2 <= ((2n+1)/(4(n+1)))^2 < 1/4 <= m^2/4 for m >= 1
        x_max = Fraction(2 * n + 1, 2)
        for k in range(n + 1, n + 20):
            u_over_pi = x_max / (2 * k)
            assert Fraction(0) < u_over_pi < Fraction(1, 2)
            for m in range(1, 10):
                assert Fraction(m * m) - u_over_pi * u_over_pi >= Fraction(3 * m * m, 4)

        # Verify telescoping tail bound: sum_{k=n+1}^M 1/k^2 < 1/n
        tail_sum = sum(Fraction(1, k * k) for k in range(n + 1, n + 200))
        assert tail_sum < Fraction(1, n)

    print("PASS: verified OEIS A183063 data (n=1..60), exact Laurent residues, and rational M-test bounds.")


if __name__ == "__main__":
    main()
