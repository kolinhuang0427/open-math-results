"""Exact-arithmetic verification for OEIS A167894 (Gladkovskii CF conjecture)."""

from fractions import Fraction
import math


OEIS_DATA = [
    1, -1, -1, -3, -13, -71, -461, -3447, -29093, -273343, -2829325, -31998903,
    -392743957, -5201061455, -73943424413, -1123596277863, -18176728317413,
    -311951144828863, -5661698774848621, -108355864447215063,
]


def s_add(p: list[Fraction], q: list[Fraction]) -> list[Fraction]:
    return [x + y for x, y in zip(p, q)]


def s_sub(p: list[Fraction], q: list[Fraction]) -> list[Fraction]:
    return [x - y for x, y in zip(p, q)]


def s_mul(p: list[Fraction], q: list[Fraction]) -> list[Fraction]:
    deg = len(p)
    out = [Fraction(0, 1)] * deg
    for i in range(deg):
        if p[i] == 0:
            continue
        for j in range(deg - i):
            out[i + j] += p[i] * q[j]
    return out


def s_inv(p: list[Fraction]) -> list[Fraction]:
    assert p[0] != 0
    deg = len(p)
    out = [Fraction(0, 1)] * deg
    out[0] = Fraction(1, 1) / p[0]
    for n in range(1, deg):
        s = sum((p[k] * out[n - k] for k in range(1, n + 1)), Fraction(0, 1))
        out[n] = -s / p[0]
    return out


def s_div(p: list[Fraction], q: list[Fraction]) -> list[Fraction]:
    return s_mul(p, s_inv(q))


def P_series(k: int, deg: int) -> list[Fraction]:
    if k == -1:
        return [Fraction(1, 1)] + [Fraction(0, 1)] * (deg - 1)
    kfact = math.factorial(k)
    return [Fraction(math.factorial(k + m) // kfact, 1) for m in range(deg)]


def cf_step(k: int, q_next: list[Fraction]) -> list[Fraction]:
    deg = len(q_next)
    one_kx = [Fraction(1, 1), Fraction(k, 1)] + [Fraction(0, 1)] * (deg - 2)
    k1x = [Fraction(0, 1), Fraction(k + 1, 1)] + [Fraction(0, 1)] * (deg - 2)
    return s_sub(one_kx, s_div(k1x, q_next))


def main() -> None:
    deg = 40
    # 1. Verify OEIS_DATA against 1 / sum_{k>=0} k! x^k
    a_ser = s_inv(P_series(0, deg))
    for n, expected in enumerate(OEIS_DATA):
        if a_ser[n] != Fraction(expected, 1):
            print(f"FAIL: OEIS_DATA mismatch at n={n}: {a_ser[n]} != {expected}")
            raise SystemExit(1)

    # 2. Verify Lemma 1 and exact Q(k) CF recurrence for k = 0..15
    for k in range(16):
        pk_prev = P_series(k - 1, deg)
        pk = P_series(k, deg)
        pk1 = P_series(k + 1, deg)
        kx = [Fraction(0, 1), Fraction(k, 1)] + [Fraction(0, 1)] * (deg - 2)
        one = [Fraction(1, 1)] + [Fraction(0, 1)] * (deg - 1)
        if s_add(one, s_mul(kx, pk)) != pk_prev:
            print(f"FAIL: Lemma 1 mismatch at k={k}")
            raise SystemExit(1)
        qk = s_div(pk_prev, pk)
        qk1 = s_div(pk, pk1)
        if cf_step(k, qk1) != qk:
            print(f"FAIL: CF step mismatch at k={k}")
            raise SystemExit(1)

    # 3. Verify depth K = 38 truncation seeded with 1 matches 1/P_0(x) through x^39
    K = 38
    q_trunc = [Fraction(1, 1)] + [Fraction(0, 1)] * (deg - 1)
    for k in range(K, -1, -1):
        q_trunc = cf_step(k, q_trunc)

    if q_trunc != a_ser:
        print("FAIL: finite CF truncation mismatch on x^0..x^39")
        raise SystemExit(1)

    print("PASS")


if __name__ == "__main__":
    main()
