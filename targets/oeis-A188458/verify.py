"""Exact-arithmetic verification for OEIS A188458 (Gladkovskii 2013 CF conjecture)."""

from fractions import Fraction
import math


OEIS_DATA = [
    1, 1, -3, -11, 57, 361, -2763, -24611, 250737, 2873041, -36581523,
    -512343611, 7828053417, 129570724921, -2309644635483, -44110959165011,
    898621108880097, 19450718635716001, -445777636063460643,
    -10784052561125704811, 274613643571568682777,
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


def cf_step(k: int, t_next: list[Fraction]) -> list[Fraction]:
    deg = len(t_next)
    one = [Fraction(1, 1)] + [Fraction(0, 1)] * (deg - 1)
    num = [Fraction(0, 1), Fraction(0, 1), Fraction(4 * (k + 1) ** 2, 1)] + [Fraction(0, 1)] * (deg - 3)
    one_mx_sq = [Fraction(1, 1), Fraction(-2, 1), Fraction(1, 1)] + [Fraction(0, 1)] * (deg - 3)
    den = s_add(num, s_div(one_mx_sq, t_next))
    return s_sub(one, s_div(num, den))


def main() -> None:
    deg = 32
    # 1. Compute a(n) directly from e.g.f. exp(x)/cosh(2x)
    exp_x = [Fraction(1, math.factorial(n)) for n in range(deg)]
    cosh_2x = [Fraction(2**n, math.factorial(n)) if n % 2 == 0 else Fraction(0, 1) for n in range(deg)]
    egf = s_div(exp_x, cosh_2x)
    a_seq = [egf[n] * math.factorial(n) for n in range(deg)]
    for n, expected in enumerate(OEIS_DATA):
        if a_seq[n] != Fraction(expected, 1):
            print(f"FAIL: OEIS_DATA mismatch at n={n}: {a_seq[n]} != {expected}")
            raise SystemExit(1)

    # 2. Verify Lemma 1 (binomial transform via sech(u))
    cosh_u = [Fraction(1, math.factorial(n)) if n % 2 == 0 else Fraction(0, 1) for n in range(deg)]
    sech_u = s_inv(cosh_u)
    euler_2m = [sech_u[n] * math.factorial(n) for n in range(deg)]  # S(u) coefficients
    # Substitute u = 2x/(1-x) and multiply by 1/(1-x)
    one_mx = [Fraction(1, 1), Fraction(-1, 1)] + [Fraction(0, 1)] * (deg - 2)
    two_x = [Fraction(0, 1), Fraction(2, 1)] + [Fraction(0, 1)] * (deg - 2)
    u_of_x = s_div(two_x, one_mx)
    u_pow = [Fraction(1, 1)] + [Fraction(0, 1)] * (deg - 1)
    S_of_u = [Fraction(0, 1)] * deg
    for m in range(deg):
        if euler_2m[m] != 0:
            for i in range(deg):
                S_of_u[i] += euler_2m[m] * u_pow[i]
        u_pow = s_mul(u_pow, u_of_x)
    F_from_S = s_div(S_of_u, one_mx)
    if F_from_S != a_seq:
        print("FAIL: Lemma 1 binomial transform mismatch")
        raise SystemExit(1)

    # 3. Verify depth K=16 CF truncation seeded with 1 matches F(x) on x^0..x^31
    K = 16
    t_trunc = [Fraction(1, 1)] + [Fraction(0, 1)] * (deg - 1)
    for k in range(K, -1, -1):
        t_trunc = cf_step(k, t_trunc)
    F_cf = s_div(t_trunc, one_mx)
    if F_cf != a_seq:
        print("FAIL: CF truncation mismatch on x^0..x^31")
        raise SystemExit(1)

    print("PASS")


if __name__ == "__main__":
    main()
