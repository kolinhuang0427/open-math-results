#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for OEIS A237757 (Peter Bala, Feb 02 2021).

Zero floating-point operations: pure Python int combinatorics and q-series DP.
"""

from __future__ import annotations

import sys

OEIS_DATA = [
    0, 1, 1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 9, 11, 13, 16, 18, 22,
    25, 30, 35, 41, 47, 56, 64, 75, 86, 100, 114, 133, 151, 174, 198,
    227, 257, 295, 333, 379, 428, 486, 547, 620, 696, 786, 882, 993,
    1111, 1250, 1396, 1565, 1747, 1954, 2176, 2431, 2703, 3013,
]


def partitions_exact(N: int, max_part: int) -> list[tuple[int, ...]]:
    """Generate all partitions of N (parts in decreasing order) with parts <= max_part."""
    if N == 0:
        return [()]
    out: list[tuple[int, ...]] = []
    for p in range(min(N, max_part), 0, -1):
        for tail in partitions_exact(N - p, p):
            out.append((p,) + tail)
    return out


def main() -> int:
    max_N = len(OEIS_DATA)  # 58

    # 1. Exact q-series expansion of Bala's sum: sum_{n>=0} q^{2(n+1)^2} / prod_{k=1..2n+1} (1 - q^k)
    bala_coeff = [0] * (max_N + 1)
    n = 0
    while 2 * (n + 1) ** 2 <= max_N:
        shift = 2 * (n + 1) ** 2
        rem_deg = max_N - shift
        # 1 / prod_{k=1..2n+1} (1 - q^k) up to q^{rem_deg}
        dp = [0] * (rem_deg + 1)
        dp[0] = 1
        for k in range(1, 2 * n + 2):
            for s in range(k, rem_deg + 1):
                dp[s] += dp[s - k]
        for s in range(rem_deg + 1):
            bala_coeff[shift + s] += dp[s]
        n += 1

    assert bala_coeff[1 : max_N + 1] == OEIS_DATA, "Mismatch against OEIS A237757 DATA"

    # 2. Direct %N partition count & explicit Phi_m / Psi_m bijection verification for N = 1..28
    for N in range(1, 29):
        all_parts = partitions_exact(N, N)
        pm_all = [lam for lam in all_parts if 2 * lam[-1] == len(lam)]
        assert len(pm_all) == OEIS_DATA[N - 1], f"Direct %N mismatch at N={N}"

        # Verify bijection Phi_m <-> Psi_m for every m >= 1 with 2*m^2 <= N
        reconstructed = []
        m = 1
        while 2 * m * m <= N:
            pm = [lam for lam in pm_all if lam[-1] == m]
            # Target: Q_{<= 2m-1}(N - 2m^2)
            # By conjugation, also count partitions into parts <= 2m-1:
            q_parts = [mu for mu in partitions_exact(N - 2 * m * m, N) if len(mu) <= 2 * m - 1]
            q_conj = partitions_exact(N - 2 * m * m, 2 * m - 1)
            assert len(q_parts) == len(q_conj)

            mapped = [tuple(x - m for x in lam if x > m) for lam in pm]
            assert set(mapped) == set(q_parts) and len(mapped) == len(q_parts)

            for mu in q_parts:
                padded = list(mu) + [0] * (2 * m - len(mu))
                psi_mu = tuple(x + m for x in padded)
                assert len(psi_mu) == 2 * m and psi_mu[-1] == m and sum(psi_mu) == N
                assert tuple(x - m for x in psi_mu if x > m) == mu
                reconstructed.append(psi_mu)
            m += 1
        assert set(reconstructed) == set(pm_all) and len(reconstructed) == len(pm_all)

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
