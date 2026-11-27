#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/oeis-A165204/PROOF.md.

Zero floating-point arithmetic: uses pure-Python int, fractions.Fraction,
exact Bareiss integer determinant, and sympy symbolic algebra over
Q(u)[x, s]/(s^2 - (1 - 4x)) to verify:
1. A165203 series F_0(x) = (1+x)c(x)^3/(1-x c(x)^3) and radical formula (Section 1),
   matching all 23 live OEIS A165203 DATA terms.
2. Exact Bareiss Hankel determinants a(n) = det(b_{i+j})_{0<=i,j<=n} (n=0..27) matching
   all 28 live OEIS A165204 DATA terms, plus Lemma 1 congruence U_n H_n U_n^T = diag.
3. Exact symbolic verification of all three J-fraction transition formulas (L74-L84) in
   Lemma 2 over Q(u)[x, s]/(s^2 - 1 + 4x), Fibonacci Mobius orbit u_k = F_{6k+2}/(2F_{6k+5}),
   beta_n, R_n, and period-3 Fibonacci closed form for a(n) (n=0..27).
4. Order-6 cancellation, polynomial factorizations (L113-L114), Barker's rational g.f.,
   and 4-term recurrence for n=4..60.
"""

from fractions import Fraction
from math import comb
import sympy as sp


def det_exact_int(mat):
    n = len(mat)
    if n == 0:
        return 1
    A = [list(row) for row in mat]
    sign = 1
    prev_pivot = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            swap_row = None
            for r in range(k + 1, n):
                if A[r][k] != 0:
                    swap_row = r
                    break
            if swap_row is None:
                return 0
            A[k], A[swap_row] = A[swap_row], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = A[i][j] * pivot - A[i][k] * A[k][j]
                assert num % prev_pivot == 0
                A[i][j] = num // prev_pivot
            A[i][k] = 0
        prev_pivot = pivot
    return sign * A[n - 1][n - 1]


def fps_mul_int(A, B, D):
    out = [0] * (D + 1)
    for i, a in enumerate(A[: D + 1]):
        if not a:
            continue
        for j in range(min(len(B), D + 1 - i)):
            out[i + j] += a * B[j]
    return out


def fps_inv_frac(U, D):
    assert U[0] != 0
    inv0 = Fraction(1, U[0])
    inv = [Fraction(0)] * (D + 1)
    inv[0] = inv0
    for k in range(1, D + 1):
        acc = Fraction(0)
        for j in range(1, min(len(U), k + 1)):
            acc -= Fraction(U[j]) * inv[k - j]
        inv[k] = acc * inv0
    return inv


# ---------------------------------------------------------------------------
# 1. A165203 series F_0(x) and radical expressions (Section 1)
# ---------------------------------------------------------------------------

MAX_N = 27
MAX_M = 2 * MAX_N + 1  # 55

# Catalan c(x) and s = sqrt(1 - 4x):
c_ser = [comb(2 * m, m) // (m + 1) for m in range(MAX_M + 1)]
s_ser = [1] + [-2 * comb(2 * m - 2, m - 1) // m for m in range(1, MAX_M + 2)]
# Check x*c(x)^2 == c(x) - 1 mod x^{MAX_M+1}:
c2 = fps_mul_int(c_ser, c_ser, MAX_M)
for d in range(1, MAX_M + 1):
    assert c2[d - 1] == c_ser[d]

c3 = fps_mul_int(c2, c_ser, MAX_M)
one_plus_x_c3 = [c3[0]] + [c3[d] + c3[d - 1] for d in range(1, MAX_M + 1)]
one_minus_x_c3 = [1] + [-c3[d - 1] for d in range(1, MAX_M + 1)]
inv_den = fps_inv_frac(one_minus_x_c3, MAX_M)
F0_frac = [sum(one_plus_x_c3[i] * inv_den[d - i] for i in range(d + 1)) for d in range(MAX_M + 1)]
assert all(v.denominator == 1 for v in F0_frac)
b = [v.numerator for v in F0_frac]

LIVE_OEIS_A165203 = [
    1, 5, 20, 81, 332, 1372, 5702, 23793, 99576, 417664, 1754866, 7383204,
    31096466, 131084954, 552969854, 2334012425, 9856336324, 41639407776,
    175971686398, 743888534968, 3145439344550, 13302946909338, 56272308538682,
]
assert b[:len(LIVE_OEIS_A165203)] == LIVE_OEIS_A165203

# Verify Section 1 radical equation: 2*x*(1 - 4x - x^2)*F_0(x) == (1+x)*(5x - 1 + (1-x)*s):
# Check coeff at x^{d+1} for d = 0..MAX_M-1:
one_m4_m1 = [1, -4, -1] + [0] * (MAX_M + 1)
lhs_rad = [0] + fps_mul_int(one_m4_m1, b, MAX_M - 1)
lhs_rad = [2 * v for v in lhs_rad]
# (1 - x) * s_ser + 5x - 1:
one_mx_s = [s_ser[0]] + [s_ser[d] - s_ser[d - 1] for d in range(1, MAX_M + 1)]
inner_r = list(one_mx_s)
inner_r[0] -= 1
inner_r[1] += 5
rhs_rad = [inner_r[0]] + [inner_r[d] + inner_r[d - 1] for d in range(1, MAX_M + 1)]
assert lhs_rad[:MAX_M] == rhs_rad[:MAX_M]

print(f"[1] PASS A165203 series matches all 23 live OEIS DATA terms & radical equation mod x^{MAX_M}.")

# ---------------------------------------------------------------------------
# 2. Symbolic verification of Lemma 2 in Q(u)[x, s]/(s^2 - (1 - 4x))
# ---------------------------------------------------------------------------

u_sym, x_sym, s_sym = sp.symbols("u x s")

def mod_s2(expr):
    """Reduce polynomial/rational-in-s expression mod (s^2 - (1 - 4x)), returning a + b*s."""
    # Convert rational expr -> poly in s over Q(u, x) by clearing denominator using s^2 = 1-4x if needed
    num, den = sp.fraction(sp.together(expr))
    p_n = sp.Poly(sp.expand(num), s_sym)
    p_d = sp.Poly(sp.expand(den), s_sym)
    # Reduce p_n mod (s^2 - (1 - 4x)):
    def red_poly(p):
        c0 = sp.Integer(0)
        c1 = sp.Integer(0)
        for (deg_s,), coef in p.terms():
            q_pow, r_pow = divmod(deg_s, 2)
            term = coef * ((1 - 4 * x_sym) ** q_pow)
            if r_pow == 0:
                c0 += term
            else:
                c1 += term
        return sp.expand(c0), sp.expand(c1)

    n0, n1 = red_poly(p_n)
    d0, d1 = red_poly(p_d)
    if d1 == 0:
        return sp.cancel(n0 / d0) + sp.cancel(n1 / d0) * s_sym
    # Multiply num & den by (d0 - d1*s):
    conj_den = sp.expand(d0**2 - (1 - 4 * x_sym) * d1**2)
    r0 = sp.expand(n0 * d0 - n1 * d1 * (1 - 4 * x_sym))
    r1 = sp.expand(n1 * d0 - n0 * d1)
    return sp.cancel(r0 / conj_den) + sp.cancel(r1 / conj_den) * s_sym


def check_mod_s2_zero(expr, label, failures):
    red = mod_s2(expr)
    p = sp.Poly(sp.together(red), s_sym)
    ok = True
    for _, coef in p.terms():
        if sp.cancel(coef) != 0:
            ok = False
    if not ok:
        failures.append(f"{label}: residual {red}")
    return ok


failures = []
# Check Section 1 L28, L29, L31 verbatim:
check_mod_s2_zero(
    (2 * x_sym**2 + 3 * x_sym - 1)**2 - (1 - x_sym)**2 * s_sym**2 - (-4 * x_sym**2 * (1 - 4 * x_sym - x_sym**2)),
    "Section 1 L28 sign", failures,
)
check_mod_s2_zero(
    ((1 - 3 * x_sym) - (1 - x_sym) * s_sym) * (2 * x_sym**2 + 3 * x_sym - 1 - (1 - x_sym) * s_sym)
    - (-2 * x_sym**2 * (5 * x_sym - 1 + (1 - x_sym) * s_sym)),
    "Section 1 L29 sign", failures,
)

G_u = (x_sym**2 - u_sym * (1 - 3 * x_sym) + u_sym * (1 - x_sym) * s_sym) / (x_sym**2 * (1 + x_sym))
inv_G_u = ((1 + x_sym) * (x_sym**2 - u_sym * (1 - 3 * x_sym) - u_sym * (1 - x_sym) * s_sym)) / (4 * u_sym**2 * x_sym + 6 * u_sym * x_sym - 2 * u_sym + x_sym**2)
assert check_mod_s2_zero(G_u * inv_G_u - 1, "G_u * inv_G_u - 1", failures)

a1 = -2 * u_sym - 1
b1 = -4 * u_sym * (u_sym + 2)
H1_formula = ((1 - s_sym) - (2 * x_sym + 3 * x_sym**2 + 2 * x_sym**3 + 8 * u_sym**2 * x_sym**2 + 16 * u_sym * x_sym**2) + x_sym**2 * s_sym) / (
    4 * x_sym**2 * (u_sym + 2) * (4 * u_sym**2 * x_sym + 6 * u_sym * x_sym - 2 * u_sym + x_sym**2)
)
assert check_mod_s2_zero(inv_G_u - (1 - a1 * x_sym - b1 * x_sym**2 * H1_formula), "Lemma 2 L76 H_1(x)", failures)

# Check L78, L80, L82, L84 verbatim directly:
inv_H1 = -((u_sym + 2) * (8 * u_sym**2 * x_sym**2 + 16 * u_sym * x_sym**2 + 2 * x_sym**3 + 3 * x_sym**2 + 2 * x_sym - 1 - (1 - x_sym**2) * s_sym)) / (
    4 * u_sym**2 * x_sym + 10 * u_sym * x_sym + 2 * u_sym + x_sym**2 + 4 * x_sym + 4
)
assert check_mod_s2_zero(H1_formula * inv_H1 - 1, "H1_formula * inv_H1 - 1", failures)

a2 = 2 * u_sym + 3
b2 = sp.Rational(1, 2) / (u_sym + 2)
H2_formula = (2 * (u_sym + 2) * (1 + x_sym) * (u_sym * (1 - 3 * x_sym - (1 - x_sym) * s_sym) + 2 - 6 * x_sym + x_sym**2 - 2 * (1 - x_sym) * s_sym)) / (
    x_sym**2 * (4 * u_sym**2 * x_sym + 10 * u_sym * x_sym + 2 * u_sym + x_sym**2 + 4 * x_sym + 4)
)
assert check_mod_s2_zero(inv_H1 - (1 - a2 * x_sym - b2 * x_sym**2 * H2_formula), "Step 2 J-fraction", failures)

inv_H2 = ((u_sym + 2) - (3 * u_sym + 6) * x_sym + x_sym**2 + (u_sym + 2) * (1 - x_sym) * s_sym) / (2 * (u_sym + 2) * (1 + x_sym))
assert check_mod_s2_zero(H2_formula * inv_H2 - 1, "Lemma 2 L82 1/H_2(x)", failures)

a3 = 4
b3 = -(8 * u_sym + 17) / (2 * (u_sym + 2))
u_next = (u_sym + 2) / (8 * u_sym + 17)
G_unext = G_u.subs(u_sym, u_next)
assert check_mod_s2_zero(inv_H2 - (1 - a3 * x_sym - b3 * x_sym**2 * G_unext), "Step 3 J-fraction", failures)

if failures:
    print("[2] FAIL Verbatim PROOF.md identity checks failed:")
    for f_msg in failures:
        print("   -", f_msg)
else:
    print("[2] PASS Lemma 2 three-step J-fraction identities (L74-L84) verified identically in Q(u)[x,s]/(s^2-1+4x).")

# ---------------------------------------------------------------------------
# 3. Direct Bareiss Hankel determinants, Lemma 1 orthogonalization, Fibonacci closed form & OEIS DATA
# ---------------------------------------------------------------------------

FIB_MAX = 150
fib = [0, 1]
for _ in range(FIB_MAX):
    fib.append(fib[-1] + fib[-2])

for m in range(FIB_MAX - 6):
    assert fib[m + 6] == 4 * fib[m + 3] + fib[m]
for m in range(FIB_MAX - 12):
    assert fib[m + 12] == 18 * fib[m + 6] - fib[m]

# Build alpha_k, beta_{k+1} up to k = MAX_N - 1 using Lemma 2 orbit:
u_k = Fraction(1, 10)
alphas = [Fraction(5)]
betas = [None, Fraction(-5)]  # 1-indexed beta_1 .. beta_{MAX_N}
for k in range(10):
    assert u_k == Fraction(fib[6 * k + 2], 2 * fib[6 * k + 5])
    assert u_k + 2 == Fraction(fib[6 * k + 8], 2 * fib[6 * k + 5])
    assert 8 * u_k + 17 == Fraction(fib[6 * k + 11], fib[6 * k + 5])
    alphas.extend([-2 * u_k - 1, 2 * u_k + 3, Fraction(4)])
    b_3k2 = -4 * u_k * (u_k + 2)
    b_3k3 = Fraction(1, 1) / (2 * (u_k + 2))
    b_3k4 = -(8 * u_k + 17) / (2 * (u_k + 2))
    assert b_3k2 == Fraction(-fib[6 * k + 2] * fib[6 * k + 8], fib[6 * k + 5] ** 2)
    assert b_3k3 == Fraction(fib[6 * k + 5], fib[6 * k + 8])
    assert betas[3 * k + 1] * b_3k2 * b_3k3 == 1
    betas.extend([b_3k2, b_3k3, b_3k4])
    u_k = (u_k + 2) / (8 * u_k + 17)

# Check Lemma 1 monic polynomials p_k(t) and U_n H_n U_n^T = diag(1, beta_1, beta_1*beta_2, ...):
p_rows = [[Fraction(1)], [-alphas[0], Fraction(1)]]
for k in range(1, MAX_N):
    # p_{k+1}(t) = (t - alpha_k)*p_k(t) - beta_k*p_{k-1}(t)
    row = [Fraction(0)] * (k + 2)
    for i, c in enumerate(p_rows[k]):
        row[i] -= alphas[k] * c
        row[i + 1] += c
    for i, c in enumerate(p_rows[k - 1]):
        row[i] -= betas[k] * c
    p_rows.append(row)

# Verify U_{MAX_N} H_{MAX_N} U_{MAX_N}^T is diagonal with entries prod_{j=1}^k beta_j:
H_full = [[b[i + j] for j in range(MAX_N + 1)] for i in range(MAX_N + 1)]
U_mat = [[p_rows[k][i] if i <= k else Fraction(0) for i in range(MAX_N + 1)] for k in range(MAX_N + 1)]
UH = [[sum(U_mat[k][r] * H_full[r][j] for r in range(k + 1)) for j in range(MAX_N + 1)] for k in range(MAX_N + 1)]
UHUT = [[sum(UH[k][s] * U_mat[l][s] for s in range(l + 1)) for l in range(MAX_N + 1)] for k in range(MAX_N + 1)]
R_prod = [Fraction(1)]
for k in range(1, MAX_N + 1):
    R_prod.append(R_prod[-1] * betas[k])
for k in range(MAX_N + 1):
    for l in range(MAX_N + 1):
        assert UHUT[k][l] == (R_prod[k] if k == l else 0), f"U H U^T mismatch at ({k},{l})"

# Check direct Bareiss det(H_n) == Fibonacci formula == live OEIS A165204 DATA (n = 0..27):
LIVE_OEIS_A165204 = [
    1, -5, -21, -21, 89, 377, 377, -1597, -6765, -6765, 28657, 121393,
    121393, -514229, -2178309, -2178309, 9227465, 39088169, 39088169,
    -165580141, -701408733, -701408733, 2971215073, 12586269025, 12586269025,
    -53316291173, -225851433717, -225851433717,
]
assert len(LIVE_OEIS_A165204) == MAX_N + 1

def a_fib(n):
    k, r = divmod(n, 3)
    if r == 0:
        return ((-1) ** k) * fib[6 * k + 2]
    elif r == 1:
        return ((-1) ** (k + 1)) * fib[6 * k + 5]
    else:
        return ((-1) ** (k + 1)) * fib[6 * k + 8]

for n in range(MAX_N + 1):
    H_n = [[b[i + j] for j in range(n + 1)] for i in range(n + 1)]
    det_H = det_exact_int(H_n)
    assert det_H == a_fib(n), f"Bareiss det != a_fib at n={n}"
    assert det_H == LIVE_OEIS_A165204[n], f"Bareiss det != live OEIS at n={n}"

print(f"[3] PASS Lemma 1 orthogonalization, Fibonacci closed form, direct Bareiss det(H_n), and all 28 live OEIS A165204 terms (n=0..{MAX_N}).")

# ---------------------------------------------------------------------------
# 4. Polynomial factorizations (L113-L114), G.f., and 4-term recurrence (n=0..60)
# ---------------------------------------------------------------------------

p_fac = sp.Poly(1 + 3 * x_sym + x_sym**2, x_sym, domain=sp.ZZ)
p_den = sp.Poly(1 - 3 * x_sym + 8 * x_sym**2 - 3 * x_sym**3 + x_sym**4, x_sym, domain=sp.ZZ)
p_num = sp.Poly(1 - 8 * x_sym + 2 * x_sym**2 - x_sym**3, x_sym, domain=sp.ZZ)
assert p_fac * p_den == sp.Poly(1 + 18 * x_sym**3 + x_sym**6, x_sym, domain=sp.ZZ)
assert p_fac * p_num == sp.Poly(1 - 5 * x_sym - 21 * x_sym**2 - 3 * x_sym**3 - x_sym**4 - x_sym**5, x_sym, domain=sp.ZZ)

MAX_GF = 60
a_seq = [a_fib(n) for n in range(MAX_GF + 1)]
for n in range(6, MAX_GF + 1):
    assert a_seq[n] + 18 * a_seq[n - 3] + a_seq[n - 6] == 0

# Verify (1 - 3x + 8x^2 - 3x^3 + x^4) * sum a(n) x^n == 1 - 8x + 2x^2 - x^3 mod x^{61}:
barker_num = [1, -8, 2, -1]
for n in range(MAX_GF + 1):
    conv = a_seq[n]
    if n >= 1:
        conv -= 3 * a_seq[n - 1]
    if n >= 2:
        conv += 8 * a_seq[n - 2]
    if n >= 3:
        conv -= 3 * a_seq[n - 3]
    if n >= 4:
        conv += a_seq[n - 4]
    exp_c = barker_num[n] if n <= 3 else 0
    assert conv == exp_c, f"Barker G.f. / recurrence failed at n={n}"

print(f"[4] PASS Order-6 identity, L113-L114 factorizations, Barker G.f., and 4-term recurrence verified for n=0..{MAX_GF}.")
if failures:
    print("FAIL")
    raise SystemExit(1)
print("PASS")
