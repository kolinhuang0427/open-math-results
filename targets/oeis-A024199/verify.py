"""Exact-arithmetic verification for OEIS A024199 (Peter Bala 2016 conjecture)."""

from fractions import Fraction
import math


OEIS_DATA = [
    0,
    1,
    2,
    13,
    76,
    789,
    7734,
    110937,
    1528920,
    28018665,
    497895210,
    11110528485,
    241792844580,
    6361055257725,
    163842638377950,
    4964894559637425,
    147721447995130800,
    5066706567801827025,
    171002070002301095250,
    6548719685561840296125,
    247199273204273879989500,
]


def odd_dfact_from_m(m: int) -> Fraction:
    """Exact value of (2m - 1)!! for any integer m."""
    if m == 0:
        return Fraction(1, 1)
    if m >= 1:
        prod = 1
        for j in range(1, m + 1):
            prod *= 2 * j - 1
        return Fraction(prod, 1)
    r = -m  # m = -r <= -1, so 2m - 1 = -(2r + 1)
    denom = 1
    for j in range(1, r + 1):
        denom *= 2 * j - 1
    sign = -1 if (r % 2 == 1) else 1
    return Fraction(sign, denom)


def a_primary(n: int) -> Fraction:
    """Primary OEIS definition: a(n) = (2n-1)!! * sum_{j=0..n-1} (-1)^j/(2j+1)."""
    if n == 0:
        return Fraction(0, 1)
    df = odd_dfact_from_m(n)
    total = Fraction(0, 1)
    for j in range(n):
        sign = 1 if (j % 2 == 0) else -1
        total += Fraction(sign, 2 * j + 1)
    return df * total


def term_T(n: int, k: int) -> Fraction:
    """Summand T(n, k) = (-1)^(n-k+1) * k! * (2n - 2k - 3)!!."""
    sign = 1 if ((n - k + 1) % 2 == 0) else -1
    m = n - k - 1  # 2m - 1 = 2n - 2k - 3
    return Fraction(sign * math.factorial(k), 1) * odd_dfact_from_m(m)


def b_bala(n: int) -> Fraction:
    """Bala's conjectured sum formula."""
    if n == 0:
        return Fraction(0, 1)
    return Fraction(1, 2) * sum((term_T(n, k) for k in range(2 * n)), Fraction(0, 1))


def series_mul(a: list[Fraction], b: list[Fraction], deg: int) -> list[Fraction]:
    res = [Fraction(0, 1)] * (deg + 1)
    for i in range(deg + 1):
        if a[i] == 0:
            continue
        for j in range(deg + 1 - i):
            res[i + j] += a[i] * b[j]
    return res


def main() -> None:
    # 1. Verify Lemma 1 on m in [-50, 50]
    for m in range(-50, 51):
        lhs = (2 * m - 1) * odd_dfact_from_m(m - 1)
        rhs = odd_dfact_from_m(m)
        if lhs != rhs:
            print(f"FAIL: Lemma 1 mismatch at m={m}: {lhs} != {rhs}")
            raise SystemExit(1)

    # 2. Verify OEIS DATA against primary definition
    for n, expected in enumerate(OEIS_DATA):
        val = a_primary(n)
        if val.denominator != 1 or val.numerator != expected:
            print(f"FAIL: DATA mismatch at n={n}: {val} != {expected}")
            raise SystemExit(1)

    # 3. Verify Lemma 2, telescoping identity, boundary cancellation, and Bala's conjecture up to n=80
    max_n = 80
    for n in range(1, max_n + 1):
        a_n = a_primary(n)
        a_prev = a_primary(n - 1)
        if a_n - (2 * n - 1) * a_prev != (1 if (n - 1) % 2 == 0 else -1) * odd_dfact_from_m(n - 1):
            print(f"FAIL: Lemma 2 mismatch at n={n}")
            raise SystemExit(1)

        if n >= 2:
            for k in range(2 * n - 2):
                lhs = term_T(n, k) - (2 * n - 1) * term_T(n - 1, k)
                rhs = 2 * (term_T(n, k) - term_T(n, k + 1))
                if lhs != rhs:
                    print(f"FAIL: telescoping mismatch at n={n}, k={k}")
                    raise SystemExit(1)
            expected_boundary = Fraction(2 ** (n - 1) * math.factorial(n - 1), 1)
            if term_T(n, 2 * n - 2) != expected_boundary or term_T(n, 2 * n - 1) != expected_boundary:
                print(f"FAIL: boundary mismatch at n={n}")
                raise SystemExit(1)

        b_n = b_bala(n)
        if b_n != a_n:
            print(f"FAIL: Bala conjecture mismatch at n={n}: {b_n} != {a_n}")
            raise SystemExit(1)

    # 4. Verify EGF identity sqrt(1 - 2x) * Y(x) == (1/2) * arcsin(2x) up to x^40 in Q[[x]]
    deg = 40
    Y = [a_primary(n) / math.factorial(n) for n in range(deg + 1)]

    # sqrt(1 - 2x) = sum_{m>=0} binom(1/2, m) (-2x)^m
    sqrt_1m2x = [Fraction(0, 1)] * (deg + 1)
    c = Fraction(1, 1)
    sqrt_1m2x[0] = c
    for m in range(1, deg + 1):
        c = c * Fraction(Fraction(1, 2) - (m - 1), m) * (-2)
        sqrt_1m2x[m] = c

    # (1/2) * arcsin(2x) = (1/2) * sum_{k>=0} (2k)! / (4^k (k!)^2 (2k+1)) * (2x)^(2k+1)
    #                    = sum_{k>=0} ((2k-1)!! / (k! * 2^k)) * 2^(2k) / (2k+1) * x^(2k+1)
    #                    = sum_{k>=0} (2k)! / ((k!)^2 * (2k+1)) * x^(2k+1)
    half_arcsin_2x = [Fraction(0, 1)] * (deg + 1)
    for k in range(deg + 1):
        p = 2 * k + 1
        if p > deg:
            break
        half_arcsin_2x[p] = Fraction(math.factorial(2 * k), math.factorial(k) ** 2 * (2 * k + 1))

    lhs_ser = series_mul(sqrt_1m2x, Y, deg)
    if lhs_ser != half_arcsin_2x:
        print("FAIL: EGF formal power series mismatch")
        raise SystemExit(1)

    print("PASS")


if __name__ == "__main__":
    main()
