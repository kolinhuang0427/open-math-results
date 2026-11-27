"""Independent exact-integer verifier for targets/kallat-2610.40342-ques14.8.

Directly computes a_A(n) from the EGF exp(sum_{m in A} x^m/m) via exact
cycle-recurrence DP: a_A(0) = 1, a_A(n) = sum_{m in A, m <= n} falling(n-1, m-1) * a_A(n-m)
for n >= 1, and checks all three non-constant counterexamples plus constant families
modulo p^e (zero floating point).
"""


def falling(n: int, k: int) -> int:
    res = 1
    for i in range(k):
        res *= n - i
    return res


def a_seq(A: set[int], N: int) -> list[int]:
    """Exact integer sequence a_A(0..N) from exponential generating function / cycle-of-n recurrence."""
    a = [0] * (N + 1)
    a[0] = 1
    sorted_A = sorted(A)
    for n in range(1, N + 1):
        total = 0
        for m in sorted_A:
            if m <= n:
                total += falling(n - 1, m - 1) * a[n - m]
        a[n] = total
    return a


def least_period(seq: list[int], mod: int) -> int:
    residues = [x % mod for x in seq]
    n = len(residues)
    for per in range(1, n):
        if all(residues[i] == residues[i + per] for i in range(n - per)):
            return per
    raise AssertionError("No period found")


def main() -> None:
    N = 120

    # 1. Odd p, sign +: A = {1, 7}, p = 3, e = 3 (p^e = 27), predicted period 27, true period 9.
    a1 = a_seq({1, 7}, N)
    expected_block_1 = [1, 1, 1, 1, 1, 1, 1, 19, 10]
    for n in range(N + 1):
        assert a1[n] % 27 == expected_block_1[n % 9]
    assert least_period(a1, 27) == 9 < 27

    # 2. Odd p, sign -: A = {5}, p = 5, e = 2 (p^e = 25), predicted period 50, true period 10.
    a2 = a_seq({5}, N)
    expected_block_2 = [1, 0, 0, 0, 0, 24, 0, 0, 0, 0]
    for n in range(N + 1):
        assert a2[n] % 25 == expected_block_2[n % 10]
    assert least_period(a2, 25) == 10 < 50

    # 3. p = 2, sign +: A = {2, 4}, p = 2, e = 2 (p^e = 4), predicted period 4, true period 2.
    a3 = a_seq({2, 4}, N)
    expected_block_3 = [1, 0]
    for n in range(N + 1):
        assert a3[n] % 4 == expected_block_3[n % 2]
    assert least_period(a3, 4) == 2 < 4

    # 4. Constant-residue families: A = {1} and A = {1, 10} mod 27, A = {1, 5} mod 4.
    for A_set, mod in [({1}, 27), ({1, 10}, 27), ({1, 5}, 4), ({1, 8}, 7)]:
        ac = a_seq(A_set, N)
        assert all(x % mod == 1 for x in ac)
        assert least_period(ac, mod) == 1 < mod

    print("PASS")
    print(f"Verified counterexamples A={{1,7}} mod 27 (period 9<27), A={{5}} mod 25 (period 10<50), A={{2,4}} mod 4 (period 2<4), and constant families for 0 <= n <= {N}.")


if __name__ == "__main__":
    main()
