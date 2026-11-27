"""Independent exact checker for targets/oeis-A379818/ (PROOF.md).

Written strictly from live OEIS A379818 (rev 8), A025480 (rev 235),
and PROOF.md, without reading verify.py.
"""

from math import comb


OEIS_A379818_DATA = [
    1, 1, 4, 1, 10, 4, 10, 1, 22, 10, 28, 4, 49, 10, 22, 1, 46, 22, 64, 10,
    118, 28, 64, 4, 190, 49, 118, 10, 190, 22, 46, 1, 94, 46, 136, 22, 256,
    64, 148, 10, 424, 118, 292, 28, 478, 64, 136, 4, 661, 190, 478, 49, 796,
    118, 256, 10, 1177, 190, 424, 22, 661, 46,
]

OEIS_A025480_DATA = [
    0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2, 10, 5, 11, 1,
    12, 6, 13, 3, 14, 7, 15, 0, 16, 8, 17, 4, 18, 9, 19, 2, 20, 10, 21, 5, 22,
    11, 23, 1, 24, 12, 25, 6, 26, 13, 27, 3, 28, 14, 29, 7, 30, 15, 31, 0, 32,
    16, 33, 8, 34, 17, 35, 4, 36, 18, 37, 9, 38, 19, 39, 2, 40, 20, 41, 10,
]


def v2(n: int) -> int:
    assert n >= 1
    return (n & -n).bit_length() - 1


def main() -> None:
    N = 10000
    # 1. A025480 up to N
    b = [0] * (N + 1)
    for r in range(1, N + 1):
        if r % 2 == 0:
            b[r] = r // 2
        else:
            b[r] = b[r // 2]
    assert b[: len(OEIS_A025480_DATA)] == OEIS_A025480_DATA

    # Test Lemma: b(2^r * (2k+1) - 1) == k
    lemma_checks = 0
    for r in range(13):
        for k in range(100):
            idx = (1 << r) * (2 * k + 1) - 1
            if idx <= N:
                assert b[idx] == k
                lemma_checks += 1

    # 2. A379818 up to N
    a = [0] * (N + 1)
    a[0] = 1
    for t in range(1, N + 1):
        if t % 2 == 1:
            n = (t - 1) // 2
            a[t] = a[n]
        else:
            n = t // 2
            fn = v2(n)
            p2 = 1 << fn
            a[t] = a[n] + a[n - p2] + a[2 * n - p2] + a[b[n - 1]]
    assert a[: len(OEIS_A379818_DATA)] == OEIS_A379818_DATA

    # 3. Verify Kurkov's conjecture formula for all (m, k) with 2^m*(2k+1) <= N
    def c(m: int, j: int) -> int:
        return comb(m + 2, j + 1) - comb(m, j)

    formula_checks = 0
    for m in range(15):
        for k in range(N + 1):
            idx = (1 << m) * (2 * k + 1)
            if idx > N:
                break
            rhs = sum(c(m, j) * a[(1 << j) * k] for j in range(m + 1))
            assert a[idx] == rhs, f"Mismatch at m={m}, k={k}: {a[idx]} != {rhs}"
            formula_checks += 1

    # 4. Verify inductive step Pascal identities for m = 1..30
    for m in range(1, 31):
        assert c(m, 0) == m + 1 == c(m - 1, 0) + 1
        assert c(m, m) == m + 1 == 1 + c(m - 1, m - 1)
        for j in range(1, m):
            assert c(m - 1, j) + c(m - 1, j - 1) == c(m, j)

    print(f"A025480 data (84 terms) & Lemma ({lemma_checks} pairs): OK")
    print(f"A379818 data (62 terms) & Kurkov formula ({formula_checks} (m,k) pairs up to n={N}): OK")
    print("Pascal boundary & interior identities (1<=m<=30): OK")
    print("PASS")


if __name__ == "__main__":
    main()
