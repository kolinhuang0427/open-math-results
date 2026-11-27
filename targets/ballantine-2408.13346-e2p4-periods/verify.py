#!/usr/bin/env python3
"""Exact integer arithmetic verifier refuting the conjectured period table of arXiv:2408.13346v1."""


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


def minimal_period_mod(vals: list[int], m: int, r_coeffs: list[int]) -> int:
    """Compute the exact pure period of the order-22 recurrence sequence mod m."""
    state = tuple(x % m for x in vals[:22])
    cur = list(state)
    step = 0
    while True:
        nxt = sum(r_coeffs[k] * cur[k] for k in range(22)) % m
        cur = cur[1:] + [nxt]
        step += 1
        if tuple(cur) == state:
            return step


def main() -> int:
    n_max = 1305
    dp = compute_e2p4_dp(n_max)

    # Verify exact values at n=0, 4, 1150, 1154, 1246, 1250
    assert dp[0] == 0
    assert dp[4] == 6
    assert dp[1150] == 4204006824112
    assert dp[1154] == 4277582023120
    assert dp[1246] == 6275602376628
    assert dp[1250] == 6376921776108

    if dp[1150] % 10 == dp[0] % 10 or dp[1154] % 10 == dp[4] % 10:
        print("FAIL: m=10 counterexample check failed")
        return 1
    if dp[1246] % 18 == dp[0] % 18 or dp[1250] % 18 == dp[4] % 18:
        print("FAIL: m=18 counterexample check failed")
        return 1

    # Cross-check with order-22 linear recurrence and compute all 26 minimal periods
    r_coeffs = [-1, -1, 0, 3, 6, 3, -3, -12, -12, -2, 10, 18, 10, -2, -12, -12, -3, 3, 6, 3, 0, -1]
    rec = list(dp[:22])
    for n in range(22, n_max + 1):
        rec.append(sum(r_coeffs[k] * rec[n - 22 + k] for k in range(22)))
    if rec != dp:
        print("FAIL: DP != recurrence")
        return 1

    expected_periods = {
        2: 48, 3: 54, 4: 96, 5: 300, 6: 432, 7: 84, 8: 192, 9: 324, 10: 1200,
        11: 132, 12: 864, 13: 156, 14: 336, 16: 384, 17: 204, 18: 1296, 19: 228,
        21: 756, 22: 528, 23: 276, 26: 624, 27: 972, 28: 672, 29: 348, 31: 372, 37: 444,
    }
    for m, exp_p in expected_periods.items():
        per = minimal_period_mod(dp, m, r_coeffs)
        if per != exp_p:
            print(f"FAIL: period mod {m} is {per}, expected {exp_p}")
            return 1

    print(
        "PASS: Conjectured period table refuted at m=10 (e_2p_4(1150)=2 != 0 mod 10; true period 1200 != 1150) "
        "and m=18 (e_2p_4(1246)=6 != 0 mod 18; true period 1296 != 1246); all 26 exact periods verified."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
