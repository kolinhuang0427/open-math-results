"""Exact-arithmetic verification for OEIS A028495 (McEachen 2026 asymptotic conjectures)."""

from fractions import Fraction


OEIS_DATA = [
    1, 1, 2, 3, 6, 10, 19, 33, 61, 108, 197, 352, 638, 1145, 2069, 3721,
    6714, 12087, 21794, 39254, 70755, 127469, 229725, 413908, 745889,
    1343980, 2421850, 4363921, 7863641, 14169633, 25532994, 46008619,
    82904974, 149389218, 269190547, 485064009, 874055885,
]


def P(r: Fraction) -> Fraction:
    return r**3 - r**2 - 2 * r + 1


def P_prime(r: Fraction) -> Fraction:
    return 3 * r**2 - 2 * r - 2


def bisect_root(lo: Fraction, hi: Fraction, steps: int = 80) -> tuple[Fraction, Fraction]:
    """Exact rational bisection on a sign-changing interval of P(r)."""
    flo = P(lo)
    fhi = P(hi)
    assert flo * fhi < 0
    for _ in range(steps):
        mid = (lo + hi) / 2
        fmid = P(mid)
        if fmid == 0:
            return mid, mid
        if flo * fmid < 0:
            hi, fhi = mid, fmid
        else:
            lo, flo = mid, fmid
    return lo, hi


def reduce_poly(coeffs: list[Fraction]) -> list[Fraction]:
    """Reduce polynomial c[0] + c[1]r + ... modulo P(r) = r^3 - r^2 - 2r + 1."""
    c = list(coeffs)
    while len(c) > 3:
        top = c.pop()
        d = len(c) - 3
        if top != 0:
            # r^(d+3) = r^d * (r^2 + 2r - 1)
            c[d + 2] += top
            c[d + 1] += 2 * top
            c[d] -= top
    while len(c) < 3:
        c.append(Fraction(0, 1))
    return c


def main() -> None:
    # 1. Verify OEIS_DATA from G.f. (1-x^2)/(1-x-2x^2+x^3)
    N = 120
    a = [1, 1, 2]  # a[0]=1, a[1]=1, a[2]=2 (since 1-x^2 = (1-x-2x^2+x^3)(1 + x + 2x^2 + ...))
    for n in range(3, N + 1):
        a.append(a[n - 1] + 2 * a[n - 2] - a[n - 3])
    for n, expected in enumerate(OEIS_DATA):
        if a[n] != expected:
            print(f"FAIL: OEIS_DATA mismatch at n={n}: {a[n]} != {expected}")
            raise SystemExit(1)

    # 2. Verify Lemma 1 sign changes on rational intervals
    checks = [
        (Fraction(-3, 2), -1),
        (Fraction(-1, 1), 1),
        (Fraction(0, 1), 1),
        (Fraction(1, 2), -1),
        (Fraction(3, 2), -1),
        (Fraction(2, 1), 1),
    ]
    for pt, sgn in checks:
        val = P(pt)
        if (val > 0 and sgn != 1) or (val < 0 and sgn != -1) or val == 0:
            print(f"FAIL: sign check failed at {pt}: P={val}")
            raise SystemExit(1)

    # 3. Verify exact algebraic trace formula sum_{j=1}^3 ((r_j^2 - 1)/P'(r_j)) r_j^n == a(n)
    # Using Newton's identities / companion trace of Q_n(r) = (r^2 - 1) r^n mod P(r):
    # By Lagrange interpolation, for any polynomial g(r), sum_{j=1}^3 g(r_j)/P'(r_j) = coeff of r^2 in (g(r) mod P(r)).
    r_pow = [Fraction(0, 1)] * (N + 3)
    for n in range(N + 1):
        g = [Fraction(0, 1)] * (n + 3)
        g[n + 2] = Fraction(1, 1)
        g[n] = Fraction(-1, 1)
        rem = reduce_poly(g)
        if rem[2] != Fraction(a[n], 1):
            print(f"FAIL: partial fraction trace mismatch at n={n}: {rem[2]} != {a[n]}")
            raise SystemExit(1)

    # 4. Exact rational bisection check of a(n)/a(n-1) vs r_1 = 2*cos(pi/7)
    # A160389 starts 1.80193773580483825247... ; sqrt(A116425) = sqrt(3.24697960371746706105...)
    r1_lo, r1_hi = bisect_root(Fraction(3, 2), Fraction(2, 1), steps=90)
    a160389_prefix = Fraction(180193773580483825247, 10**20)
    if not (r1_lo <= a160389_prefix + Fraction(1, 10**20) and a160389_prefix <= r1_hi):
        print("FAIL: r1 bisection inconsistent with A160389 digits")
        raise SystemExit(1)

    # Check A116425 = r1^2 interval
    a116425_lo = Fraction(324697960371746706105, 10**20)
    a116425_hi = a116425_lo + Fraction(1, 10**20)
    if not (r1_lo**2 <= a116425_hi and r1_hi**2 >= a116425_lo):
        print("FAIL: r1^2 inconsistent with A116425 digits")
        raise SystemExit(1)

    # Check ratio a(120)/a(119) is within 10^-15 of r1
    ratio_120 = Fraction(a[120], a[119])
    if abs(ratio_120 - r1_lo) > Fraction(1, 10**15) or abs(ratio_120 - r1_hi) > Fraction(1, 10**15):
        print(f"FAIL: ratio a(120)/a(119)={ratio_120} not converging to r1 in [{r1_lo}, {r1_hi}]")
        raise SystemExit(1)

    print("PASS")


if __name__ == "__main__":
    main()
