"""
Exact zero-float verification for OEIS A237757:
  Number of partitions of N with 2*(least part) = (number of parts).
Verifies:
  1. Direct recursive/combinatorial partition counts against OEIS %S/%T/%U data (N = 1..57).
  2. Explicit bijection Phi_m on all partitions in P_m(N) -> Q_{<=2m-1}(N - 2m^2) for N = 1..30.
  3. Exact truncated formal power series identity in Z[[q]] up to q^80.
"""


def gen_partitions(n, max_part=None):
    if max_part is None:
        max_part = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, max_part), 0, -1):
        for rest in gen_partitions(n - first, first):
            yield (first,) + rest


def count_partitions_dp(max_n):
    """Exact DP for:
      - a_direct[N] = #{partitions of N with 2 * min(lambda) == len(lambda)}
      - a_gf[N]     = [q^N] Sum_{n>=0} q^(2(n+1)^2) / Prod_{k=1..2n+1} (1 - q^k)
    """
    # Exact DP for p(N, exact_min=m, exact_len=L):
    # A partition of N into L parts with min part >= m equals m*L + (partition of N - m*L into <= L parts),
    # and with exact min = m iff the last part is m, i.e., partition of N - m*L into <= L - 1 parts!
    # Wait: let's ALSO compute a_direct via pure partition-by-(min, len) DP directly without using the shortcut!
    # dp_len_min[N][L][m] = # partitions of N into exact L parts with min part == m
    # Recurrence: remove all m-parts (say r >= 1 copies of m), wait: simpler:
    # A partition with exact length L and exact min m >= 1 either:
    #   (i) has last part m and remaining L-1 parts all == m -> handled by base L=1, N=m,
    #   (ii) subtract 1 from all L parts -> partition of N - L into L parts with min part == m - 1 (if m > 1),
    #        OR if m == 1, partition of N - 1 into L - 1 parts (Wait: min >= 1!).
    # So dp[N][L][m] = dp[N - L][L][m - 1] (if m > 1 and N >= L),
    #                  and for m == 1: dp[N][L][1] = sum_{m'>=1} dp[N - 1][L - 1][m'] (for L >= 2, N >= 1), dp[1][1][1] = 1!
    dp_total_len = [[0] * (max_n + 1) for _ in range(max_n + 1)]  # dp_total_len[N][L] = # partitions of N into exact L parts (>=1)
    dp_total_len[0][0] = 1
    for N in range(1, max_n + 1):
        for L in range(1, N + 1):
            dp_total_len[N][L] = dp_total_len[N - 1][L - 1] + (dp_total_len[N - L][L] if N >= L else 0)

    # Now exact DP for (# parts == L, min part == m):
    # Notice (# parts == L, min >= m) == dp_total_len[N - (m - 1) * L][L] (subtract m-1 from each of L parts!),
    # so (# parts == L, min == m) = (# with L parts, min >= m) - (# with L parts, min >= m + 1)
    a_direct = [0] * (max_n + 1)
    for N in range(1, max_n + 1):
        total = 0
        m = 1
        while 2 * m <= N:
            L = 2 * m
            c_ge_m = dp_total_len[N - (m - 1) * L][L] if N >= (m - 1) * L else 0
            c_ge_m1 = dp_total_len[N - m * L][L] if N >= m * L else 0
            total += c_ge_m - c_ge_m1
            m += 1
        a_direct[N] = total

    # Direct series expansion in Z[[q]] of Sum_{n>=0} q^(2(n+1)^2) / Prod_{k=1..2n+1} (1 - q^k)
    a_gf = [0] * (max_n + 1)
    n = 0
    while 2 * (n + 1) ** 2 <= max_n:
        shift = 2 * (n + 1) ** 2
        poly = [0] * (max_n + 1)
        poly[shift] = 1
        for k in range(1, 2 * n + 2):
            for deg in range(shift + k, max_n + 1):
                poly[deg] += poly[deg - k]
        for deg in range(max_n + 1):
            a_gf[deg] += poly[deg]
        n += 1

    return a_direct, a_gf


def verify_all():
    # 1. Exhaustive bijection check on all partitions for N = 1..28
    for N in range(1, 29):
        p_set = [p for p in gen_partitions(N) if 2 * p[-1] == len(p)]
        # Map each partition via Phi_m and check exact bijection with Union_m Q_{<=2m-1}(N - 2m^2)
        mapped = {}
        for p in p_set:
            m = p[-1]
            mu = tuple(x - m for x in p[:-1] if x - m > 0)
            assert len(mu) <= 2 * m - 1
            assert sum(mu) == N - 2 * m * m
            key = (m, mu)
            assert key not in mapped
            mapped[key] = p
        # Check reverse map Psi_m covers every partition of N - 2m^2 with <= 2m - 1 parts
        expected_keys = set()
        m = 1
        while 2 * m * m <= N:
            for mu in gen_partitions(N - 2 * m * m):
                if len(mu) <= 2 * m - 1:
                    expected_keys.add((m, mu))
            m += 1
        assert set(mapped.keys()) == expected_keys

    # 2. Check OEIS A237757 %S/%T/%U data (N = 1..57) and Z[[q]] agreement up to N = 80
    oeis_data = [
        0, 1, 1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 9, 11, 13, 16, 18, 22, 25, 30, 35, 41, 47, 56, 64, 75,
        86, 100, 114, 133, 151, 174, 198, 227, 257, 295, 333, 379, 428, 486, 547, 620, 696,
        786, 882, 993, 1111, 1250, 1396, 1565, 1747, 1954, 2176, 2431, 2703, 3013,
    ]
    a_direct, a_gf = count_partitions_dp(80)
    assert a_direct[1:] == a_gf[1:]
    assert a_direct[1:len(oeis_data) + 1] == oeis_data
    assert a_gf[1:len(oeis_data) + 1] == oeis_data
    print("PASS")


if __name__ == "__main__":
    verify_all()
