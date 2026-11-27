#!/usr/bin/env python3
"""Exact integer polynomial and DP verifier for the e_2p_4(n) linear recurrence of arXiv:2408.13346v1."""


def poly_mul(a: list[int], b: list[int]) -> list[int]:
    res = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            res[i + j] += ai * bj
    return res


def poly_pow(a: list[int], exp: int) -> list[int]:
    res = [1]
    for _ in range(exp):
        res = poly_mul(res, a)
    return res


def poly_add(a: list[int], b: list[int]) -> list[int]:
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]


def poly_div_exact(num: list[int], den: list[int]) -> list[int]:
    rem = list(num)
    while len(rem) > 1 and rem[-1] == 0:
        rem.pop()
    while len(den) > 1 and den[-1] == 0:
        den.pop()
    assert len(rem) >= len(den)
    q_len = len(rem) - len(den) + 1
    quot = [0] * q_len
    lead = den[-1]
    for k in range(q_len - 1, -1, -1):
        c = rem[k + len(den) - 1]
        assert c % lead == 0
        q_k = c // lead
        quot[k] = q_k
        for j, dj in enumerate(den):
            rem[k + j] -= q_k * dj
    assert all(r == 0 for r in rem)
    return quot


def compute_e2p4_dp(n_max: int) -> list[int]:
    """Compute e_2p_4(n) directly from its partition definition for 0 <= n <= n_max."""
    cnt = [[0] * (n_max + 1) for _ in range(5)]
    s1 = [[0] * (n_max + 1) for _ in range(5)]
    se2 = [[0] * (n_max + 1) for _ in range(5)]
    cnt[0][0] = 1
    for t in range(1, n_max + 1):
        for j in range(1, 5):
            for s in range(t, n_max + 1):
                c_prev = cnt[j - 1][s - t]
                if c_prev:
                    cnt[j][s] += c_prev
                    s1[j][s] += s1[j - 1][s - t] + t * c_prev
                    se2[j][s] += se2[j - 1][s - t] + t * s1[j - 1][s - t]
    return se2[4]


def main() -> int:
    # 1. Verify exact factorization of D(q) and its degree-22 expansion
    d_q = poly_mul(
        poly_mul(poly_pow([1, -1], 6), poly_pow([1, 1], 4)),
        poly_mul(poly_pow([1, 0, 1], 3), poly_pow([1, 1, 1], 3)),
    )
    expected_d = [
        1, 1, 0, -3, -6, -3, 3, 12, 12, 2, -10, -18,
        -10, 2, 12, 12, 3, -3, -6, -3, 0, 1, 1,
    ]
    if d_q != expected_d:
        print(f"FAIL: D(q) mismatch: {d_q}")
        return 1

    # 2. Verify each of the 9 exact rational terms over D(q)
    # Term k numerator = base_num * (D / base_den)
    term_specs = [
        ([0] * 7 + [1], poly_mul(poly_mul(poly_pow([1, -1], 6), poly_pow([1, 1], 3)), poly_mul([1, 0, 1], [1, 1, 1]))),
        ([0] * 8 + [2], poly_mul(poly_mul(poly_pow([1, -1], 6), poly_pow([1, 1], 2)), poly_mul([1, 0, 1], poly_pow([1, 1, 1], 2)))),
        ([0] * 5 + [3], poly_mul(poly_mul(poly_pow([1, -1], 6), poly_pow([1, 1], 3)), poly_mul(poly_pow([1, 0, 1], 2), [1, 1, 1]))),
        ([0] * 6 + [1], poly_mul(poly_mul(poly_pow([1, -1], 6), poly_pow([1, 1], 4)), [1, 1, 1])),
        ([0] * 9 + [4], poly_mul(poly_mul(poly_pow([1, -1], 6), poly_pow([1, 1], 3)), poly_mul([1, 0, 1], poly_pow([1, 1, 1], 2)))),
        ([0] * 6 + [6], poly_mul(poly_mul(poly_pow([1, -1], 6), poly_pow([1, 1], 4)), poly_mul(poly_pow([1, 0, 1], 2), [1, 1, 1]))),
        ([0] * 7 + [3, -3, 3], poly_mul(poly_mul(poly_pow([1, -1], 6), [1, 1]), poly_mul([1, 0, 1], poly_pow([1, 1, 1], 3)))),
        ([0] * 7 + [9], poly_mul(poly_mul(poly_pow([1, -1], 6), poly_pow([1, 1], 3)), poly_mul(poly_pow([1, 0, 1], 2), poly_pow([1, 1, 1], 2)))),
        ([0] * 4 + [6, 0, 0, 0, 6], poly_mul(poly_mul(poly_pow([1, -1], 6), poly_pow([1, 1], 4)), poly_mul(poly_pow([1, 0, 1], 3), [1, 1, 1]))),
    ]
    total_n = [0]
    for b_num, b_den in term_specs:
        q_factor = poly_div_exact(d_q, b_den)
        total_n = poly_add(total_n, poly_mul(b_num, q_factor))
    while len(total_n) > 1 and total_n[-1] == 0:
        total_n.pop()
    expected_n = [0, 0, 0, 0, 6, 15, 34, 57, 95, 121, 146, 126, 106, 72, 50, 25, 11]
    if total_n != expected_n:
        print(f"FAIL: N(q) mismatch: {total_n}")
        return 1

    # 3. Verify Taylor series of N(q)/D(q) matches exact partition DP up to n=200 and recurrence holds
    n_max = 200
    dp = compute_e2p4_dp(n_max)
    series = [0] * (n_max + 1)
    for n in range(n_max + 1):
        val = expected_n[n] if n < len(expected_n) else 0
        for j in range(1, min(n, 22) + 1):
            val -= d_q[j] * series[n - j]
        series[n] = val
    if series != dp:
        print("FAIL: Generating function series != partition DP")
        return 1

    r = [-d_q[22 - k] for k in range(22)]
    for n in range(0, n_max - 22 + 1):
        rhs = sum(r[k] * dp[n + k] for k in range(22))
        if dp[22 + n] != rhs:
            print(f"FAIL: recurrence mismatch at n={n}")
            return 1

    print(
        f"PASS: e_2p_4(n) rational GF N(q)/D(q) (deg N=16 < deg D=22) verified and "
        f"conjectured 22-term recurrence confirmed against exact partition DP for 0 <= n <= {n_max}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
