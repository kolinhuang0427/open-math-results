"""Independent exact-arithmetic verifier for targets/benfield-2407.20048-conj5.3/ (clause (vi))."""

import math
import sys


def eventual_period_and_order(a: int, b: int, m: int) -> tuple[int, int, int, list[int]]:
    """
    Directly simulate U_0=0, U_1=1, U_n = a*U_{n-1} + b*U_{n-2} mod m.
    Returns (preperiod, period_len, omega, period_seq).
    """
    seen = {}
    seq = []
    u0, u1 = 0 % m, 1 % m
    idx = 0
    while (u0, u1) not in seen:
        seen[(u0, u1)] = idx
        seq.append(u0)
        u0, u1 = u1, (a * u1 + b * u0) % m
        idx += 1
    pre = seen[(u0, u1)]
    period_seq = seq[pre:]
    omega = period_seq.count(0)
    return pre, len(period_seq), omega, period_seq


def mult_order(base: int, mod: int) -> int:
    assert math.gcd(base, mod) == 1
    x = base % mod
    k = 1
    while x != 1:
        x = (x * base) % mod
        k += 1
    return k


def check_clause_vi():
    a, b = 3, 4
    # Confirm (3, 4) falls strictly under clause (vi) (not (i)-(v))
    assert (a, b) not in {(0, 1), (1, 0), (-1, -1), (2, -1), (-2, -1), (-1, 0), (1, -1), (0, -1)}
    assert b not in (-1, 1)
    assert abs(a) - abs(b) != 1

    # Closed form U_n = (4^n - (-1)^n) / 5 for 0 <= n <= 60
    u0, u1 = 0, 1
    for n in range(61):
        num = (4**n) - ((-1) ** n)
        assert num % 5 == 0
        assert u0 == num // 5
        u0, u1 = u1, a * u1 + b * u0

    # Test all 2 <= m <= 200 against exact period/order predictions
    seen_omegas = set()
    for m in range(2, 201):
        pre, pi, omega, _ = eventual_period_and_order(a, b, m)
        seen_omegas.add(omega)
        if m % 2 == 0:
            assert omega == 0, f"Even m={m} had omega={omega}"
        else:
            assert pre == 0, f"Odd m={m} had preperiod={pre}"
            alpha = mult_order(-4, 5 * m)
            if alpha % 2 == 0:
                assert pi == alpha and omega == 1, f"Odd m={m}, even alpha={alpha}: pi={pi}, omega={omega}"
            else:
                assert pi == 2 * alpha and omega == 2, f"Odd m={m}, odd alpha={alpha}: pi={pi}, omega={omega}"

    assert seen_omegas == {0, 1, 2}

    # Explicit values in COUNTEREXAMPLE.md
    assert eventual_period_and_order(3, 4, 2)[2] == 0
    pre3, pi3, om3, pseq3 = eventual_period_and_order(3, 4, 3)
    assert pre3 == 0 and pi3 == 2 and om3 == 1 and pseq3 == [0, 1]
    pre5, pi5, om5, pseq5 = eventual_period_and_order(3, 4, 5)
    assert pre5 == 0 and pi5 == 10 and om5 == 2 and pseq5 == [0, 1, 3, 3, 1, 0, 4, 2, 2, 4]


def main():
    check_clause_vi()
    print("PASS (Conjecture 5.3 clause (vi) refuted: (3,4)-Fibonacci has range {0,1,2} verified m=2..200)")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
