#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/oeis-A274271/PROOF.md.

Zero floating-point arithmetic: uses pure-Python int, fractions.Fraction,
and exact sympy polynomial/rational algebra over Q(x) to verify:
1. Partition GF F(x) = 1/((1-x)(1-x^2)(1-x^3)(1-x^4)) up to x^6561 (n=0..8),
   matching closed form and all 19 live OEIS A274271 DATA terms.
2. Exact symbolic partial fraction decomposition (Section 1 L24-L30) in Q(x).
3. Pole-by-pole coefficient extraction formulas (Section 2) at m = 3^n for n=1..25.
4. Rational generating function, denominator expansion, and 4-term recurrence (Section 3)
   for n = 0..40.
"""

from fractions import Fraction
import sympy as sp

x = sp.Symbol("x")

# ---------------------------------------------------------------------------
# 1. Direct partition GF expansion up to m = 3^8 = 6561 & live OEIS DATA
# ---------------------------------------------------------------------------

MAX_M = 3 ** 8  # 6561
dp = [0] * (MAX_M + 1)
dp[0] = 1
for part in (1, 2, 3, 4):
    for m in range(part, MAX_M + 1):
        dp[m] += dp[m - part]

def a_closed(n):
    if n == 0:
        return 1
    m = 3 ** n
    num = ((3 + m) ** 2) * (9 + m)
    assert num % 144 == 0
    return num // 144

for n in range(9):
    assert dp[3 ** n] == a_closed(n), f"Partition count mismatch at n={n} (3^n={3**n})"

LIVE_OEIS_A274271 = [
    1, 3, 18, 225, 4410, 105903, 2746098, 73140525, 1965803130, 52995903003,
    1430162760978, 38607856205625, 1042353276205050, 28143008896575303,
    759856474192364658, 20516081909157771525, 553933825501236490170,
    14956209814120079146803, 403817633711525094117138,
]
for n, val in enumerate(LIVE_OEIS_A274271):
    assert a_closed(n) == val, f"OEIS A274271 mismatch at n={n}"

print(f"[1] PASS Direct partition DP [x^(3^n)]F(x) (n=0..8, up to x^6561) and all {len(LIVE_OEIS_A274271)} live OEIS A274271 terms match.")

# ---------------------------------------------------------------------------
# 2. Section 1 symbolic partial fraction decomposition in Q(x)
# ---------------------------------------------------------------------------

F_expr = 1 / ((1 - x) * (1 - x**2) * (1 - x**3) * (1 - x**4))
pf_expr = (
    sp.Rational(1, 24) / (1 - x)**4
    + sp.Rational(1, 8) / (1 - x)**3
    + sp.Rational(59, 288) / (1 - x)**2
    + sp.Rational(17, 72) / (1 - x)
    + sp.Rational(1, 8) / (1 + x)
    + sp.Rational(1, 32) / (1 + x)**2
    + sp.Rational(1, 8) / (1 + x**2)
    + (1 + x) / (9 * (1 + x + x**2))
)
assert sp.cancel(F_expr - pf_expr) == 0, "Partial fraction decomposition failed"

# Check L26, L27, L29-30 polynomial identities directly:
p_one = (175 - 358*x + 263*x**2 - 68*x**3)
assert sp.cancel(
    p_one / (288 * (1 - x)**4)
    - (sp.Rational(1, 24)/(1-x)**4 + sp.Rational(1, 8)/(1-x)**3 + sp.Rational(59, 288)/(1-x)**2 + sp.Rational(17, 72)/(1-x))
) == 0
poly_id = (
    p_one * (1 + x)**2 * (1 + x**2) * (1 + x + x**2)
    + 9 * (5 + 4*x) * (1 - x)**4 * (1 + x**2) * (1 + x + x**2)
    + 36 * (1 - x)**4 * (1 + x)**2 * (1 + x + x**2)
    + 32 * (1 + x) * (1 - x)**4 * (1 + x)**2 * (1 + x**2)
)
assert sp.expand(poly_id) == 288, "L29-L30 cleared-denominator polynomial identity failed"
print("[2] PASS Section 1 partial fraction identity and cleared-denominator polynomial identity verified in Q(x).")

# ---------------------------------------------------------------------------
# 3. Section 2 pole-by-pole coefficient extraction for n = 1..25
# ---------------------------------------------------------------------------

for n in range(1, 26):
    m = 3 ** n
    assert m % 2 == 1 and m % 3 == 0
    c_1 = Fraction((m+3)*(m+2)*(m+1), 144) + Fraction((m+2)*(m+1), 16) + Fraction(59*(m+1), 288) + Fraction(17, 72)
    assert c_1 == Fraction(2*m**3 + 30*m**2 + 135*m + 175, 288)
    c_m1 = -Fraction(1, 8) - Fraction(m + 1, 32)
    assert c_m1 == Fraction(-9*m - 45, 288)
    c_i = Fraction(0)  # m odd
    c_w = Fraction(1, 9)  # 3 | m
    tot = c_1 + c_m1 + c_i + c_w
    assert tot.denominator == 1 and tot.numerator == a_closed(n)

# Also verify (1+x)/(9*(1+x+x^2)) = (1-x^2)/(9*(1-x^3)) = (1/9)*sum (x^{3j} - x^{3j+2}) symbolically:
assert sp.cancel((1 + x) / (9 * (1 + x + x**2)) - (1 - x**2) / (9 * (1 - x**3))) == 0
print("[3] PASS Section 2 pole-by-pole extraction and closed form verified for n=1..25.")

# ---------------------------------------------------------------------------
# 4. Section 3 rational generating function and 4-term recurrence (n = 0..40)
# ---------------------------------------------------------------------------

G_sum = (
    -sp.Rational(1, 9)
    + sp.Rational(1, 144) * (
        81 / (1 - x) + 63 / (1 - 3*x) + 15 / (1 - 9*x) + 1 / (1 - 27*x)
    )
)
G_target = (1 - 37*x + 288*x**2 - 405*x**3 - 81*x**4) / ((1 - x) * (1 - 3*x) * (1 - 9*x) * (1 - 27*x))
assert sp.cancel(G_sum - G_target) == 0, "Rational G.f. mismatch"

den_exp = sp.Poly((1 - x) * (1 - 3*x) * (1 - 9*x) * (1 - 27*x), x, domain=sp.ZZ)
assert den_exp == sp.Poly(1 - 40*x + 390*x**2 - 1080*x**3 + 729*x**4, x, domain=sp.ZZ)

MAX_R = 40
a_seq = [a_closed(n) for n in range(MAX_R + 1)]
num_c = [1, -37, 288, -405, -81]
for n in range(MAX_R + 1):
    val = a_seq[n]
    if n >= 1:
        val -= 40 * a_seq[n - 1]
    if n >= 2:
        val += 390 * a_seq[n - 2]
    if n >= 3:
        val -= 1080 * a_seq[n - 3]
    if n >= 4:
        val += 729 * a_seq[n - 4]
    exp_v = num_c[n] if n <= 4 else 0
    assert val == exp_v, f"G.f. / recurrence mismatch at n={n}"

print(f"[4] PASS Section 3 rational G.f., denominator expansion, and 4-term recurrence verified for n=0..{MAX_R}.")
print("PASS")
