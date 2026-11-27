"""Independent exact-arithmetic checker for targets/oeis-A121580/."""

from fractions import Fraction
from math import factorial
import sys
import sympy as sp


def a_seq(n_max: int) -> list[int]:
    """a(1)=1, a(n) = a(n-1) + (n-1)!*(1 + n*(n-1)//2) for n >= 2 (1-indexed, a[0]=None)."""
    a = [None, 1]
    for n in range(2, n_max + 1):
        a.append(a[-1] + factorial(n - 1) * (1 + n * (n - 1) // 2))
    return a


def main():
    oeis_data = [
        1, 3, 11, 53, 317, 2237, 18077, 164237, 1656077, 18348557, 221561357,
        2895986957, 40737113357, 613623026957, 9854521894157, 168083120422157,
        3034505335078157, 57810369261862157, 1159018646647078157,
    ]
    n_max = 60
    a = a_seq(n_max)
    assert a[1 : 1 + len(oeis_data)] == oeis_data, "OEIS A121580 data mismatch"

    # Also verify Deutsch's closed form: a(n) = (1/2)*sum_{j=0..n+1} j! - n!
    for n in range(1, 25):
        s = sum(factorial(j) for j in range(n + 2))
        assert s % 2 == 0
        assert a[n] == s // 2 - factorial(n)

    # Step 1: Coefficient-matching identity in first differences
    n_sym = sp.Symbol("n")
    a0, a1, a2, a3, a4 = sp.symbols("a0 a1 a2 a3 a4")
    lhs_diff = a0 + (-n_sym - 4) * a1 + 3 * (n_sym + 1) * a2 + 2 * (-2 * n_sym + 3) * a3 + 2 * (n_sym - 3) * a4
    rhs_diff = (a0 - a1) + (-n_sym - 3) * (a1 - a2) + 2 * n_sym * (a2 - a3) + (-2 * n_sym + 6) * (a3 - a4)
    assert sp.expand(lhs_diff - rhs_diff) == 0

    # Step 2: Exact polynomial cancellation P(n) == 0 in Z[n]
    t1 = (n_sym - 1) * (n_sym - 2) * (n_sym - 3) * (n_sym**2 - n_sym + 2)
    t2 = -(n_sym + 3) * (n_sym - 2) * (n_sym - 3) * ((n_sym - 1) ** 2 - (n_sym - 1) + 2)
    t3 = 2 * n_sym * (n_sym - 3) * ((n_sym - 2) ** 2 - (n_sym - 2) + 2)
    t4 = -2 * (n_sym - 3) * ((n_sym - 3) ** 2 - (n_sym - 3) + 2)
    assert sp.expand(t1 - (n_sym**5 - 7 * n_sym**4 + 19 * n_sym**3 - 29 * n_sym**2 + 28 * n_sym - 12)) == 0
    assert sp.expand(t2 - (-n_sym**5 + 5 * n_sym**4 - n_sym**3 - 37 * n_sym**2 + 90 * n_sym - 72)) == 0
    assert sp.expand(t3 - (2 * n_sym**4 - 16 * n_sym**3 + 46 * n_sym**2 - 48 * n_sym)) == 0
    assert sp.expand(t4 - (-2 * n_sym**3 + 20 * n_sym**2 - 70 * n_sym + 84)) == 0
    assert sp.expand(t1 + t2 + t3 + t4) == 0

    # Direct check of Mathar's recurrence for 5 <= n <= 60
    for n in range(5, n_max + 1):
        val = (
            a[n]
            + (-n - 4) * a[n - 1]
            + 3 * (n + 1) * a[n - 2]
            + 2 * (-2 * n + 3) * a[n - 3]
            + 2 * (n - 3) * a[n - 4]
        )
        assert val == 0, f"Mathar recurrence failed at n={n}"

    # Step 3: Verify a(0)=0 boundary case and explicit order-4 EGF ODE up to x^45
    assert a[4] - 8 * a[3] + 15 * a[2] - 10 * a[1] + 2 * 0 == 0
    M = 45
    y_hat = [Fraction(0)] + [Fraction(a[n], factorial(n)) for n in range(1, M + 5)]
    def deriv(s):
        return [Fraction(i) * s[i] for i in range(1, len(s))]
    y1 = deriv(y_hat)
    y2 = deriv(y1)
    y3 = deriv(y2)
    y4 = deriv(y3)
    for m in range(M):
        # (1-x)y4 + (3x-8)y3 + (15-4x)y2 + (2x-10)y1 + 2y
        c4 = y4[m] - (y4[m - 1] if m > 0 else Fraction(0))
        c3 = -8 * y3[m] + (3 * y3[m - 1] if m > 0 else Fraction(0))
        c2 = 15 * y2[m] - (4 * y2[m - 1] if m > 0 else Fraction(0))
        c1 = -10 * y1[m] + (2 * y1[m - 1] if m > 0 else Fraction(0))
        c0 = 2 * y_hat[m]
        assert c4 + c3 + c2 + c1 + c0 == 0, f"Step 3 ODE failed at x^{m}"

    print(f"PASS (OEIS data n=1..19, Steps 1-3 identities & EGF ODE to x^{M-1}, Mathar recurrence 5<=n<={n_max})")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
