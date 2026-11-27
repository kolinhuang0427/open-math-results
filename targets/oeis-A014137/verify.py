"""Exact-arithmetic verification for OEIS A014137 (Gladkovskii 2013 CF conjecture)."""

from fractions import Fraction
import math


OEIS_DATA = [
    1, 2, 4, 9, 23, 65, 197, 626, 2056, 6918, 23714, 82500, 290512, 1033412,
    3707852, 13402697, 48760367, 178405157, 656043857, 2423307047, 8987427467,
    33453694487, 124936258127, 467995871777, 1757900019101, 6619846420553,
    24987199492705, 94520750408709, 358268702159069,
]


def catalan(n: int) -> int:
    return math.comb(2 * n, n) // (n + 1)


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


def cf_step(k: int, q_next: list[Fraction]) -> list[Fraction]:
    """One Gladkovskii CF step computing Q(k) from q_next = Q(k+1)."""
    deg = len(q_next)
    one = [Fraction(1, 1)] + [Fraction(0, 1)] * (deg - 1)
    c2 = Fraction(2 * k + 3, 1)
    c2_ser = [c2] + [Fraction(0, 1)] * (deg - 1)
    c1 = Fraction(k + 1, 1)
    c1_ser = [c1] + [Fraction(0, 1)] * (deg - 1)
    x_2_4k3 = [Fraction(0, 1), Fraction(2 * (4 * k + 3), 1)] + [Fraction(0, 1)] * (deg - 2)
    x_2_k1_4k3 = [Fraction(0, 1), Fraction(2 * (k + 1) * (4 * k + 3), 1)] + [Fraction(0, 1)] * (deg - 2)
    x_4k1 = [Fraction(0, 1), Fraction(4 * k + 1, 1)] + [Fraction(0, 1)] * (deg - 2)

    d2 = s_add(x_2_4k3, s_div(c2_ser, q_next))
    d1 = s_sub(c1_ser, s_div(x_2_k1_4k3, d2))
    return s_add(one, s_div(x_4k1, d1))


def exact_Q(k: int, deg: int) -> list[Fraction]:
    c2k = catalan(2 * k)
    return [Fraction(catalan(n + 2 * k), c2k) for n in range(deg)]


def main() -> None:
    deg = 40
    # 1. Verify OEIS_DATA matches partial sums of Catalan numbers
    partial = 0
    for n, expected in enumerate(OEIS_DATA):
        partial += catalan(n)
        if partial != expected:
            print(f"FAIL: OEIS_DATA mismatch at n={n}")
            raise SystemExit(1)

    # 2. Verify Lemma 1 and exact CF step identity Q(k) == cf_step(k, Q(k+1)) for k=0..14
    for k in range(15):
        if Fraction(catalan(2 * k + 1), catalan(2 * k)) != Fraction(4 * k + 1, k + 1):
            print(f"FAIL: r_1 mismatch at k={k}")
            raise SystemExit(1)
        if Fraction(catalan(2 * k + 2), catalan(2 * k + 1)) != Fraction(2 * (4 * k + 3), 2 * k + 3):
            print(f"FAIL: r_2 mismatch at k={k}")
            raise SystemExit(1)
        qk = exact_Q(k, deg)
        qk1 = exact_Q(k + 1, deg)
        if cf_step(k, qk1) != qk:
            print(f"FAIL: CF step mismatch at k={k}")
            raise SystemExit(1)

    # 3. Verify depth K=20 truncation seeded with 1 matches Q(0)/(1-x) on x^0..x^39
    K = 20
    q_trunc = [Fraction(1, 1)] + [Fraction(0, 1)] * (deg - 1)
    for k in range(K, -1, -1):
        q_trunc = cf_step(k, q_trunc)

    one_minus_x = [Fraction(1, 1), Fraction(-1, 1)] + [Fraction(0, 1)] * (deg - 2)
    gf = s_div(q_trunc, one_minus_x)

    partial = 0
    for n in range(deg):
        partial += catalan(n)
        if gf[n] != Fraction(partial, 1):
            print(f"FAIL: GF coefficient mismatch at n={n}: {gf[n]} != {partial}")
            raise SystemExit(1)

    print("PASS")


if __name__ == "__main__":
    main()
