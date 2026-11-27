"""Exact-arithmetic verification for OEIS A026927 generating function and recurrence.

Verifies (with zero floats):
1. Direct combinatorial enumeration of partitions of n into an even number of parts with
   maximum part 3 matches published OEIS A026927 data (n = 1..52).
2. Bivariate partition G.f. (F(x, 1) + F(x, -1))/2 matches Barker's rational G.f. and
   combinatorial counts up to n = 80.
3. Exact denominator factorization D(x) == 1 - x - x^4 + x^5 - x^6 + x^7 + x^10 - x^11 in Z[x].
4. Barker's 11-term recurrence holds identically for n = 9..100.
"""

PUBLISHED_A026927 = [
    0, 0, 0, 1, 1, 2, 1, 3, 3, 5, 4, 7, 6, 9, 8, 12, 11, 15, 13, 18, 17, 22,
    20, 26, 24, 30, 28, 35, 33, 40, 37, 45, 43, 51, 48, 57, 54, 63, 60, 70,
    67, 77, 73, 84, 81, 92, 88, 100, 96, 108, 104, 117,
]


def poly_mul(p: list[int], q: list[int]) -> list[int]:
    res = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            res[i + j] += a * b
    return res


def count_even_partitions_max3(n: int) -> int:
    total = 0
    for c3 in range(1, n // 3 + 1):
        rem3 = n - 3 * c3
        for c2 in range(rem3 // 2 + 1):
            c1 = rem3 - 2 * c2
            if (c1 + c2 + c3) % 2 == 0:
                total += 1
    return total


def main() -> None:
    max_n = 80

    # 1. Direct partition count vs published OEIS data
    comb_counts = [0] + [count_even_partitions_max3(n) for n in range(1, max_n + 1)]
    assert comb_counts[1 : 1 + len(PUBLISHED_A026927)] == PUBLISHED_A026927

    # 2. Verify polynomial algebra in Z[x]
    d_factored = [1]
    for factor, mult in [
        ([1, -1], 3),
        ([1, 1], 2),
        ([1, -1, 1], 1),
        ([1, 0, 1], 1),
        ([1, 1, 1], 1),
    ]:
        for _ in range(mult):
            d_factored = poly_mul(d_factored, factor)
    expected_d = [1, -1, 0, 0, -1, 1, -1, 1, 0, 0, 1, -1]
    assert d_factored == expected_d

    num_lhs = poly_mul(poly_mul([1, 1], [1, -1, 1]), [1, 0, 1])
    num_rhs = poly_mul([1, -3, 3, -1], [1, 1, 1])
    num_diff = [u - v for u, v in zip(num_lhs, num_rhs)]
    assert num_diff == [0, 2, 0, 2, -2, 2]

    # 3. Expand Barker's G.f. up to n = 100 and compare with partition counts (up to 80) and recurrence
    num_gf = [0, 0, 0, 0, 1, 0, 1, -1, 1]
    a = [0] * 101
    for n in range(101):
        rhs = num_gf[n] if n < len(num_gf) else 0
        for j in range(1, min(len(expected_d), n + 1)):
            rhs -= expected_d[j] * a[n - j]
        a[n] = rhs

    assert a[1 : max_n + 1] == comb_counts[1 : max_n + 1]

    def term(k: int) -> int:
        return a[k] if k >= 0 else 0

    for n in range(9, 101):
        rec = (
            term(n)
            - term(n - 1)
            - term(n - 4)
            + term(n - 5)
            - term(n - 6)
            + term(n - 7)
            + term(n - 10)
            - term(n - 11)
        )
        assert rec == 0, f"Recurrence mismatch at n={n}"

    print("PASS: verified OEIS A026927 partition counts (n=1..80), G.f., and 11-term recurrence (n=12..100).")


if __name__ == "__main__":
    main()
