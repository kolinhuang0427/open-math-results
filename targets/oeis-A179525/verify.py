"""Exact-arithmetic verification for OEIS A179525 (Gladkovskii CF & Bala even-product GF)."""

from fractions import Fraction
import math


OEIS_DATA = [
    1, 1, 2, 7, 33, 197, 1419, 11966, 115575, 1257718, 15223822, 202860828,
    2950665011, 46516215168, 790009447590, 14379745626739, 279256447482090,
    5763290215111558, 125960271446527241, 2906289188751628643,
    70594767279197608011, 1800695322331687800336, 48122711251655255426539,
    1344617808976210991187090, 39206731897407002624384182,
    1190905492485213830900901986,
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


def q_pow(m: int, deg: int) -> list[Fraction]:
    """Series expansion of (1+x)^m truncated to degree < deg."""
    return [Fraction(math.comb(m, j), 1) for j in range(deg)]


def exact_Q(k: int, deg: int) -> list[Fraction]:
    one = [Fraction(1, 1)] + [Fraction(0, 1)] * (deg - 1)
    total = list(one)
    term = list(one)
    for n in range(1, deg + 2):
        fac = s_sub(q_pow(2 * k + n, deg), one)
        term = s_mul(term, fac)
        total = s_add(total, term)
    return total


def cf_step(k: int, q_next: list[Fraction]) -> list[Fraction]:
    deg = len(q_next)
    one = [Fraction(1, 1)] + [Fraction(0, 1)] * (deg - 1)
    q1 = q_pow(2 * k + 1, deg)
    q2 = q_pow(2 * k + 2, deg)
    a = s_sub(one, q1)
    b = s_sub(one, q2)
    d2 = s_sub(b, s_inv(q_next))
    d1 = s_sub(one, s_div(b, d2))
    return s_sub(one, s_div(a, d1))


def main() -> None:
    deg = 30
    one = [Fraction(1, 1)] + [Fraction(0, 1)] * (deg - 1)

    # 1. Verify OEIS_DATA against A(x) = Q(0)
    a_ser = exact_Q(0, deg)
    for n, expected in enumerate(OEIS_DATA):
        if a_ser[n] != Fraction(expected, 1):
            print(f"FAIL: OEIS_DATA mismatch at n={n}: {a_ser[n]} != {expected}")
            raise SystemExit(1)

    # 2. Verify exact CF recurrence Q(k) == cf_step(k, Q(k+1)) for k=0..10
    for k in range(11):
        if cf_step(k, exact_Q(k + 1, deg)) != exact_Q(k, deg):
            print(f"FAIL: CF step mismatch at k={k}")
            raise SystemExit(1)

    # 3. Verify depth K=14 finite truncation seeded with 1 matches A(x) through x^29
    q_trunc = list(one)
    for k in range(14, -1, -1):
        q_trunc = cf_step(k, q_trunc)
    if q_trunc != a_ser:
        print("FAIL: finite CF truncation mismatch on x^0..x^29")
        raise SystemExit(1)

    # 4. Verify Bala's even-product GF matches A(x) through x^29
    bala = [Fraction(0, 1)] * deg
    p_even = list(one)
    for n in range(deg // 2 + 2):
        bala = s_add(bala, s_mul(q_pow(2 * n + 1, deg), p_even))
        p_even = s_mul(p_even, s_sub(one, q_pow(2 * n + 1, deg)))
        p_even = s_mul(p_even, s_sub(one, q_pow(2 * n + 2, deg)))
    if bala != a_ser:
        print("FAIL: Bala even-product GF mismatch on x^0..x^29")
        raise SystemExit(1)

    print("PASS")


if __name__ == "__main__":
    main()
