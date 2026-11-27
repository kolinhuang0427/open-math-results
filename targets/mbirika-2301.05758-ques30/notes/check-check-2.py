"""Independent exact-integer verifier for targets/mbirika-2301.05758-ques30.

Computes the six sequences directly from Definitions 3, 6, and 7 of arXiv:2301.05758v3,
checks Lemma 1, Corollary 2, Lemma 4, Theorems A-D, and verifies all 4 closed forms
and all 3 observations of Question 30 across 1 <= k <= 120 (zero floating point).
"""

import math


def v_p(n: int, p: int) -> int:
    assert n != 0
    n = abs(n)
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def build_sequences(N: int) -> tuple[list[int], ...]:
    P = [0] * (N + 1)
    Q = [0] * (N + 1)
    B = [0] * (N + 1)
    C = [0] * (N + 1)
    b = [0] * (N + 1)
    c = [0] * (N + 1)

    P[0], P[1] = 0, 1
    Q[0], Q[1] = 1, 1
    B[0], B[1] = 0, 1
    C[0], C[1] = 1, 3
    b[0], b[1] = 0, 0
    c[0], c[1] = -1, 1

    for n in range(2, N + 1):
        P[n] = 2 * P[n - 1] + P[n - 2]
        Q[n] = 2 * Q[n - 1] + Q[n - 2]
        B[n] = 6 * B[n - 1] - B[n - 2]
        C[n] = 6 * C[n - 1] - C[n - 2]
        b[n] = 6 * b[n - 1] - b[n - 2] + 2
        c[n] = 6 * c[n - 1] - c[n - 2]
    return P, Q, B, C, b, c


def main() -> None:
    K_MAX = 120
    N_SHIFT = 50
    SEQ_MAX = 2 * N_SHIFT + 2 * K_MAX + 10
    P, Q, B, C, b, c = build_sequences(SEQ_MAX)

    # 1. Verify Binet-derived identities used in Section 1 & Lemma 4
    for n in range(0, SEQ_MAX // 2):
        assert B[n] == P[n] * Q[n]
        assert 2 * B[n] == P[2 * n]
        assert C[n] == Q[2 * n]
        if n >= 1:
            assert 2 * b[n] == P[2 * n - 1] - 1
            assert c[n] == Q[2 * n - 1]
        assert Q[n] ** 2 - 2 * P[n] ** 2 == (-1) ** n
        assert C[n] == 2 * Q[n] ** 2 - (-1) ** n
        assert C[n] == 4 * P[n] ** 2 + (-1) ** n

    # 2. Verify Lemma 1 and Corollary 2 exact consecutive-square sum formulas
    for k in range(1, 51):
        for n in range(0, 21):
            sc = sum(C[n + i] ** 2 for i in range(1, k + 1))
            sb = sum(B[n + i] ** 2 for i in range(1, k + 1))
            slc = sum(c[n + i] ** 2 for i in range(1, k + 1))
            slb = sum(b[n + i] ** 2 for i in range(1, k + 1))
            assert 2 * sc == B[k] * C[2 * n + k + 1] + k
            assert 16 * sb == B[k] * C[2 * n + k + 1] - k
            assert 2 * slc == B[k] * C[2 * n + k] - k
            tail = P[k] * Q[2 * n + k] if k % 2 == 0 else Q[k] * P[2 * n + k]
            assert 16 * slb == B[k] * C[2 * n + k] + 5 * k - 8 * tail

    # 3. Verify Lemma 4 modular & p-adic valuations across 1 <= k <= K_MAX
    for r in range(K_MAX):
        assert C[2 * r] % 16 == 1
        assert C[2 * r + 1] % 16 == 3
        assert Q[2 * r] % 16 in (1, 3)
        assert P[2 * r + 1] % 8 in (1, 5)

    for k in range(1, K_MAX + 1):
        if k % 2 == 1:
            assert B[k] % 2 == 1 and Q[k] % 2 == 1
            assert B[k] % 4 == k % 4
            assert B[k] % 3 != 0 and Q[k] % 3 != 0
            if k % 3 == 0:
                assert v_p(B[k], 7) == v_p(Q[k], 7) == 1 + v_p(k, 7)
        else:
            a = v_p(k, 2)
            assert v_p(B[k], 2) == v_p(P[k], 2) == a
            assert v_p(B[k], 3) == 1 + v_p(k, 3)
            assert (B[k] - 3 * k) % (1 << (a + 4)) == 0
            assert v_p(3 * B[k] + k, 2) == a + 1
            assert v_p(3 * B[k] - k, 2) == a + 3
            assert v_p(B[k] - k, 2) == a + 1
            if k % 4 == 0:
                assert (B[k] - 51 * k) % (1 << (a + 6)) == 0
                assert (P[k] - 3 * k) % (1 << (a + 3)) == 0
                assert v_p(B[k] + 5 * k - 8 * P[k], 2) == a + 5
            if k % 6 == 0:
                assert v_p(B[k], 7) == v_p(P[k], 7) == 1 + v_p(k, 7)
                assert Q[k] % 7 != 0

    # 4. Verify all 4 closed forms and all 3 Question 30 observations against direct GCDs over 0 <= n <= N_SHIFT
    for k in range(1, K_MAX + 1):
        gC_emp = math.gcd(*(sum(C[n + i] ** 2 for i in range(1, k + 1)) for n in range(N_SHIFT)))
        gB_emp = math.gcd(*(sum(B[n + i] ** 2 for i in range(1, k + 1)) for n in range(N_SHIFT)))
        gc_emp = math.gcd(*(sum(c[n + i] ** 2 for i in range(1, k + 1)) for n in range(N_SHIFT)))
        gb_emp = math.gcd(*(sum(b[n + i] ** 2 for i in range(1, k + 1)) for n in range(N_SHIFT)))

        gC_thm = math.gcd(k, B[k])
        gB_thm = gC_thm // 2 if k % 2 == 0 else gC_thm
        gc_thm = math.gcd(k, 3 * B[k])

        if k % 2 == 0:
            assert (B[k] - P[k]) % 4 == 0
            assert (B[k] + 5 * k - 8 * P[k]) % 64 == 0
            c1 = (B[k] - P[k]) // 4
            c0 = (B[k] + 5 * k - 8 * P[k]) // 64
            gb_thm = 4 * math.gcd(B[k], c1, c0)
            assert v_p(gb_thm, 2) == v_p(k, 2) + 1
            # Check Theorem D exact quadratic representation on n=0..15
            for n in range(16):
                m = 2 * n + k
                xn = (Q[m] - 1) // 2
                assert (xn * (xn - 1)) % 8 == 0
                wn = (xn * (xn - 1)) // 8
                sb = sum(b[n + i] ** 2 for i in range(1, k + 1))
                assert sb == 4 * (B[k] * wn + c1 * xn + c0)
        else:
            assert (B[k] - Q[k]) % 2 == 0
            assert (3 * B[k] + 5 * k - 8 * Q[k]) % 64 == 0
            d1 = (B[k] - Q[k]) // 2
            c0p = (3 * B[k] + 5 * k - 8 * Q[k]) // 64
            gb_thm = 4 * math.gcd(B[k], d1, c0p)
            assert v_p(gb_thm, 2) == 2
            for n in range(16):
                m = 2 * n + k
                yn = (P[m] - 1) // 4
                sb = sum(b[n + i] ** 2 for i in range(1, k + 1))
                assert sb == 4 * (B[k] * yn**2 + d1 * yn + c0p)

        assert gC_emp == gC_thm, f"G_C mismatch at k={k}"
        assert gB_emp == gB_thm, f"G_B mismatch at k={k}"
        assert gc_emp == gc_thm, f"G_c mismatch at k={k}"
        assert gb_emp == gb_thm, f"G_b mismatch at k={k}"

        # Observations 1, 2, 3 of Question 30
        assert (2 * gB_thm == gC_thm) if (k % 2 == 0) else (gB_thm == gC_thm)
        assert (3 * gC_thm == gc_thm) if (k % 6 == 3) else (gC_thm == gc_thm)
        assert gb_thm % 4 == 0

    print("PASS")
    print(f"Verified all 6 sequences, Lemma 1, Corollary 2, Lemma 4, Theorems A-D, and all 3 Question 30 observations for 1 <= k <= {K_MAX}.")


if __name__ == "__main__":
    main()
