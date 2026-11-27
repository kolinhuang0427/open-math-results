#!/usr/bin/env python3
"""Exact integer arithmetic verifier for arXiv:2301.05758v3 Question 30 closed forms."""

import math


def v_p(p: int, n: int) -> int:
    assert n != 0
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def main() -> int:
    k_max = 120
    n_samples = 45
    n_seq = 2 * n_samples + k_max + 10

    P = [0, 1]
    Q = [1, 1]
    B = [0, 1]
    C = [1, 3]
    b = [0, 0]
    c = [-1, 1]
    for n in range(2, 2 * n_seq + 2):
        P.append(2 * P[-1] + P[-2])
        Q.append(2 * Q[-1] + Q[-2])
    for n in range(2, n_seq + 2):
        B.append(6 * B[-1] - B[-2])
        C.append(6 * C[-1] - C[-2])
        b.append(6 * b[-1] - b[-2] + 2)
        c.append(6 * c[-1] - c[-2])

    # Check sequence identities against Pell/associated Pell definitions
    for n in range(n_seq + 1):
        assert B[n] == P[n] * Q[n] == P[2 * n] // 2
        assert C[n] == Q[2 * n]
        if n >= 1:
            assert b[n] == (P[2 * n - 1] - 1) // 2
            assert c[n] == Q[2 * n - 1]

    # Check Lemma 4 key congruence invariants
    for r in range(n_seq // 2):
        assert C[2 * r] % 16 == 1
        assert C[2 * r + 1] % 16 == 3
        assert Q[2 * r] % 16 in (1, 3)
        assert P[2 * r + 1] % 8 in (1, 5)
    for k in range(1, k_max + 1):
        if k % 2 == 1:
            assert B[k] % 2 == 1 and Q[k] % 2 == 1
            assert B[k] % 4 == k % 4
            assert B[k] % 3 != 0 and Q[k] % 3 != 0
            if k % 3 == 0:
                assert v_p(7, B[k]) == v_p(7, Q[k]) == 1 + v_p(7, k)
        else:
            a = v_p(2, k)
            assert v_p(2, B[k]) == a and v_p(2, P[k]) == a
            assert v_p(3, B[k]) == 1 + v_p(3, k)
            assert (B[k] - 3 * k) % (1 << (a + 4)) == 0
            if k % 4 == 0:
                assert (B[k] - 51 * k) % (1 << (a + 6)) == 0
                assert (P[k] - 3 * k) % (1 << (a + 3)) == 0
                assert v_p(2, B[k] + 5 * k - 8 * P[k]) == a + 5
            if k % 6 == 0:
                assert v_p(7, B[k]) == v_p(7, P[k]) == 1 + v_p(7, k)
                assert Q[k] % 7 != 0

    # Check Corollary 2 exact sum identities and all four GCD closed forms for 1 <= k <= k_max
    for k in range(1, k_max + 1):
        gC_emp = 0
        gB_emp = 0
        gc_emp = 0
        gb_emp = 0
        for n in range(n_samples):
            sc_sum = sum(C[n + i] ** 2 for i in range(1, k + 1))
            sb_sum = sum(B[n + i] ** 2 for i in range(1, k + 1))
            scc_sum = sum(c[n + i] ** 2 for i in range(1, k + 1))
            sbb_sum = sum(b[n + i] ** 2 for i in range(1, k + 1))

            assert 2 * sc_sum == B[k] * C[2 * n + k + 1] + k
            assert 16 * sb_sum == B[k] * C[2 * n + k + 1] - k
            assert 2 * scc_sum == B[k] * C[2 * n + k] - k
            cross = P[k] * Q[2 * n + k] if k % 2 == 0 else Q[k] * P[2 * n + k]
            assert 16 * sbb_sum == B[k] * C[2 * n + k] + 5 * k - 8 * cross

            gC_emp = math.gcd(gC_emp, sc_sum)
            gB_emp = math.gcd(gB_emp, sb_sum)
            gc_emp = math.gcd(gc_emp, scc_sum)
            gb_emp = math.gcd(gb_emp, sbb_sum)

        gC_exact = math.gcd(k, B[k])
        gB_exact = gC_exact // 2 if k % 2 == 0 else gC_exact
        gc_exact = math.gcd(k, 3 * B[k])
        if k % 2 == 0:
            assert (B[k] - P[k]) % 4 == 0
            assert (B[k] + 5 * k - 8 * P[k]) % 64 == 0
            gb_exact = 4 * math.gcd(
                B[k], (B[k] - P[k]) // 4, (B[k] + 5 * k - 8 * P[k]) // 64
            )
        else:
            assert (B[k] - Q[k]) % 2 == 0
            assert (3 * B[k] + 5 * k - 8 * Q[k]) % 64 == 0
            gb_exact = 4 * math.gcd(
                B[k], (B[k] - Q[k]) // 2, (3 * B[k] + 5 * k - 8 * Q[k]) // 64
            )

        assert gC_emp == gC_exact, (k, gC_emp, gC_exact)
        assert gB_emp == gB_exact, (k, gB_emp, gB_exact)
        assert gc_emp == gc_exact, (k, gc_emp, gc_exact)
        assert gb_emp == gb_exact, (k, gb_emp, gb_exact)

        # Verify all three bullets of Question 30 directly
        assert gB_exact == (gC_exact // 2 if k % 2 == 0 else gC_exact)
        assert gC_exact == (gc_exact // 3 if k % 6 == 3 else gc_exact)
        assert gb_exact % 4 == 0

    print(
        "PASS: arXiv:2301.05758v3 Question 30 — exact closed forms and all 3 observations "
        f"verified for all 1 <= k <= {k_max} across {n_samples} shifts."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
