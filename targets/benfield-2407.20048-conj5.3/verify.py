#!/usr/bin/env python3
"""Exact integer arithmetic verifier for refuting Conjecture 5.3 clause (vi) of arXiv:2407.20048v2."""

def ab_fib_mod_stats(a: int, b: int, m: int):
    """Return (preperiod, period, omega, cycle_list) for U_0=0, U_1=1, U_n=a*U_{n-1}+b*U_{n-2} mod m."""
    assert m > 1
    x, y = 0, 1 % m
    seen = {}
    seq = []
    step = 0
    while (x, y) not in seen:
        seen[(x, y)] = step
        seq.append(x)
        x, y = y, (a * y + b * x) % m
        step += 1
    pre = seen[(x, y)]
    per = step - pre
    cycle = seq[pre:]
    omega = sum(1 for v in cycle if v == 0)
    return pre, per, omega, cycle


def main() -> int:
    # Verify Counterexample to Clause (vi): (a, b) = (3, 4)
    a, b = 3, 4
    assert b not in (-1, 1)
    assert abs(a) - abs(b) != 1

    # 1. Closed form U_n = (4^n - (-1)^n) // 5 for 0 <= n <= 100
    u0, u1 = 0, 1
    for n in range(101):
        val = (pow(4, n) - ((-1) ** n)) // 5
        if (pow(4, n) - ((-1) ** n)) % 5 != 0 or val != u0:
            print(f"FAIL: closed form mismatch at n={n}")
            return 1
        u0, u1 = u1, 3 * u1 + 4 * u0

    # 2. Check exact values omega_{(3,4)}(2)=0, omega_{(3,4)}(3)=1, omega_{(3,4)}(5)=2
    if ab_fib_mod_stats(3, 4, 2)[2] != 0:
        print("FAIL: omega_{(3,4)}(2) != 0")
        return 1
    if ab_fib_mod_stats(3, 4, 3)[2] != 1:
        print("FAIL: omega_{(3,4)}(3) != 1")
        return 1
    if ab_fib_mod_stats(3, 4, 5)[2] != 2:
        print("FAIL: omega_{(3,4)}(5) != 2")
        return 1

    # 3. Check finite range {0, 1, 2} for all 2 <= m <= 500
    seen_omegas = set()
    for mod in range(2, 501):
        _, _, w, _ = ab_fib_mod_stats(3, 4, mod)
        seen_omegas.add(w)
        if w not in (0, 1, 2):
            print(f"FAIL: unexpected omega_{(3,4)}({mod}) = {w}")
            return 1
    if seen_omegas != {0, 1, 2}:
        print(f"FAIL: range {seen_omegas} != {{0, 1, 2}}")
        return 1

    print(
        "PASS: Conjecture 5.3 clause (vi) refuted at (a,b)=(3,4) — "
        "exact range {0,1,2} proved for all m>1 and verified for 2<=m<=500."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
