"""Exact-arithmetic verification for OEIS A123145 (Gladkovskii 2012 CF conjecture)."""

from fractions import Fraction
import math


OEIS_DATA = [
    1,
    2,
    6,
    24,
    24,
    144,
    1008,
    8064,
    8064,
    80640,
    887040,
    10644480,
    10644480,
    149022720,
    2235340800,
    35765452800,
    35765452800,
    643778150400,
    12231784857600,
    244635697152000,
    244635697152000,
    5381985337344000,
    123785662758912000,
    2970855906213888000,
]


def a_sequence(max_n: int) -> list[int]:
    """Return [0, a(1), ..., a(max_n)] from the primary definition."""
    a = [0, 1]
    for n in range(2, max_n + 1):
        a.append(a[-1] if (n % 4 == 1) else n * a[-1])
    return a


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


def cf_step(k: int, g_next: list[Fraction]) -> list[Fraction]:
    """One 5-step Gladkovskii CF evaluation: G(k) from g_next = G(k+1)."""
    deg = len(g_next)
    one = [Fraction(1, 1)] + [Fraction(0, 1)] * (deg - 1)
    x = [Fraction(0, 1), Fraction(1, 1)] + [Fraction(0, 1)] * (deg - 2)
    one_plus_x = s_add(one, x)
    c = Fraction(4 * k + 1, 1)
    c_ser = [c] + [Fraction(0, 1)] * (deg - 1)
    cx = [Fraction(0, 1), c] + [Fraction(0, 1)] * (deg - 2)

    d4 = s_add(x, s_inv(g_next))
    d3 = s_sub(one_plus_x, s_div(x, d4))
    d2 = s_sub(one_plus_x, s_div(x, d3))
    d1 = s_sub(c_ser, s_div(cx, d2))
    return s_add(one, s_div(x, d1))


def main() -> None:
    deg = 45
    a = a_sequence(deg)

    # 1. Verify OEIS DATA
    for idx, expected in enumerate(OEIS_DATA, start=1):
        if a[idx] != expected:
            print(f"FAIL: OEIS_DATA mismatch at n={idx}")
            raise SystemExit(1)

    # 2. Verify Lemma 1 for all m, r with 4m+r <= deg
    for n in range(1, deg + 1):
        m, rem = divmod(n - 1, 4)
        prod = 1
        for j in range(m + 1):
            prod *= 4 * j + 1
        if Fraction(a[n], math.factorial(n)) != Fraction(1, prod):
            print(f"FAIL: Lemma 1 mismatch at n={n}")
            raise SystemExit(1)

    # 3. Verify exact 5-step CF algebraic step G(k) == cf_step(k, G(k+1)) for k=0..9
    def exact_G(k: int) -> list[Fraction]:
        ser = [Fraction(0, 1)] * deg
        ser[0] = Fraction(1, 1)
        prod = 1
        for m in range((deg - 1) // 4 + 1):
            prod *= 4 * (k + m) + 1
            for r in range(1, 5):
                idx = 4 * m + r
                if idx < deg:
                    ser[idx] = Fraction(1, prod)
        return ser

    for k in range(10):
        gk = exact_G(k)
        gk1 = exact_G(k + 1)
        if cf_step(k, gk1) != gk:
            print(f"FAIL: 5-step CF algebraic identity failed at k={k}")
            raise SystemExit(1)

    # 4. Verify depth K=10 truncation from g_{11}=1 agrees with exact G(0) through x^44,
    # and hence E(x) = d(G(0))/dx matches sum_{n=0..43} a(n+1) x^n / n!
    K = 10
    g_trunc = [Fraction(1, 1)] + [Fraction(0, 1)] * (deg - 1)
    for k in range(K, -1, -1):
        g_trunc = cf_step(k, g_trunc)

    g0_exact = exact_G(0)
    if g_trunc != g0_exact:
        print("FAIL: finite CF truncation mismatch on x^0..x^44")
        raise SystemExit(1)

    for n in range(deg - 1):
        coeff_E = Fraction(n + 1, 1) * g_trunc[n + 1]
        if coeff_E * math.factorial(n) != a[n + 1]:
            print(f"FAIL: E(x) coefficient mismatch at n={n}")
            raise SystemExit(1)

    print("PASS")


if __name__ == "__main__":
    main()
