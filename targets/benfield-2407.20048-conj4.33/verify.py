#!/usr/bin/env python3
"""Exact integer arithmetic verifier for Benfield-Lippard arXiv:2407.20048v2 Conjecture 4.33."""


def kfib_stats(k: int, m: int):
    """Compute exact (pi_K(m), alpha_K(m), omega_K(m)) for F_0=0, F_1=1, F_n=K*F_{n-1}+F_{n-2} mod m."""
    assert m > 1
    a, b = 0, 1 % m
    seen = {}
    seq = []
    step = 0
    while (a, b) not in seen:
        seen[(a, b)] = step
        seq.append(a)
        a, b = b, (k * b + a) % m
        step += 1
    assert seen[(0, 1 % m)] == 0
    pi = step
    zeros = [i for i, val in enumerate(seq) if val == 0]
    omega = len(zeros)
    alpha = zeros[1] if omega > 1 else pi
    assert pi == alpha * omega
    return pi, alpha, omega


def k_lucas_mod_check(k: int, n_max: int) -> None:
    """Verify F_{K,2r} = F_{K,r}*L_{K,r} and L_{K,2r} == 2 (mod 4) for even K."""
    f0, f1 = 0, 1
    l0, l1 = 2, k
    f_vals = [f0, f1]
    l_vals = [l0, l1]
    for _ in range(2, 2 * n_max + 1):
        f_vals.append(k * f_vals[-1] + f_vals[-2])
        l_vals.append(k * l_vals[-1] + l_vals[-2])
    for r in range(1, n_max + 1):
        assert f_vals[2 * r] == f_vals[r] * l_vals[r]
        assert l_vals[2 * r] % 4 == 2


def main() -> int:
    # 1. Verify Lemma 3 structural identities on even K in [-16, 16] and powers of 2
    for k in range(-16, 17, 2):
        k_lucas_mod_check(k, 20)
        for x in range(1, 9):
            pi, alpha, omega = kfib_stats(k, 1 << x)
            if omega != 1 or pi != alpha or alpha % 2 != 0 or (alpha & (alpha - 1)) != 0:
                print(f"FAIL: Lemma 3 failed at K={k}, 2^{x}: {(pi, alpha, omega)}")
                return 1

    # 2. Verify specific edge case K=2, m=10 (where fiborder.tex Thm 4.29 had an lcm[1,*] typo)
    pi10, alpha10, w10 = kfib_stats(2, 10)
    if (pi10, alpha10, w10) != (12, 6, 2):
        print(f"FAIL: expected (12, 6, 2) at K=2, m=10, got {(pi10, alpha10, w10)}")
        return 1

    # 3. Exhaustively verify all 3 bullets of Conjecture 4.33 for even K in [-20, 20], 4 <= m <= 400
    checked = 0
    for k in range(-20, 21, 2):
        for m in range(4, 401):
            pi, alpha, omega = kfib_stats(k, m)
            bullet1 = (omega == 4) == (alpha % 4 in (1, 3))
            bullet2 = (omega != 2) or (pi % 4 == 0 and alpha % 2 == 0)
            bullet3 = (pi % 4 == 0) or (omega == 1)
            if not (bullet1 and bullet2 and bullet3):
                print(
                    f"FAIL: Conjecture 4.33 failed at K={k}, m={m}: "
                    f"pi={pi}, alpha={alpha}, omega={omega}"
                )
                return 1
            checked += 1

    print(
        f"PASS: Conjecture 4.33 verified across {checked} (K, m) pairs "
        "(even K in [-20, 20], 4 <= m <= 400), powers of 2 (2^1..2^8), and Lucas identities."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
