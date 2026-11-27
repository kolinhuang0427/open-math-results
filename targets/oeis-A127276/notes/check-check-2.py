#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/oeis-A127276/PROOF.md.

Zero floating-point arithmetic: uses pure-Python int and fractions.Fraction
(plus exact Bareiss integer determinant) to verify:
1. A127275 power series B(x) = (sqrt(1-4x)-x)/(1-4x) and exact b_m = C(2m,m) - 4^(m-1) (m>=1).
2. Rank-2 decomposition M_n = C_n - (1/4) v v^T + (1/4) e_0 e_0^T.
3. Lemma 1 (Laurent identity, P_k(z+2+1/z) = z^k+z^{-k}, P_k(4), P_k(0)) and exact
   diagonalization P C_n P^T = diag(1, 2, ..., 2) for n = 0..25.
4. Weinstein-Aronszajn bilinear forms, exact 2x2 determinant 1 - n(n+1)/4, and direct
   exact integer Bareiss determinant det(M_n) = 2^n - n(n+1)*2^(n-2) for n = 0..25,
   matching all 26 live OEIS A127276 DATA terms.
5. Ordinary generating function -(4x-1)(x-1)/(2x-1)^3 mod x^{41}.
"""

from fractions import Fraction
from math import comb


def det_exact_int(mat):
    """Exact Bareiss integer determinant for a square list-of-lists of ints."""
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


def closed_form_a(n):
    """Exact integer value of 2^n - n*(n+1)*2^(n-2)."""
    if n == 0:
        return 1
    if n == 1:
        return 1  # 2 - 1*2/2 = 1
    return (1 << n) - n * (n + 1) * (1 << (n - 2))


MAX_N = 25
MAX_M = 2 * MAX_N

# ---------------------------------------------------------------------------
# 1. Exact A127275 series B(x) = (sqrt(1-4x)-x)/(1-4x) and rank-2 decomposition
# ---------------------------------------------------------------------------

# Compute S(x) = sqrt(1 - 4x) in Z[[x]] via S(x)^2 = 1 - 4x, S(0) = 1:
# Wait: coefficients of sqrt(1-4x) are integers: S_0 = 1, S_m = -2 * C(2m-2, m-1) / m (m>=1)!
# Also verify S(x)^2 == 1 - 4x directly!
S = [1] + [-2 * comb(2 * m - 2, m - 1) // m for m in range(1, MAX_M + 1)]
for d in range(MAX_M + 1):
    conv = sum(S[i] * S[d - i] for i in range(d + 1))
    expected = 1 if d == 0 else (-4 if d == 1 else 0)
    assert conv == expected, f"sqrt(1-4x)^2 mismatch at x^{d}"

# Verify B(x) satisfies (1 - 4x)*B(x) == S(x) - x in Z[[x]]:
b = [1] + [comb(2 * m, m) - (1 << (2 * (m - 1))) for m in range(1, MAX_M + 1)]
LIVE_OEIS_A127275 = [
    1, 1, 2, 4, 6, -4, -100, -664, -3514, -16916, -77388, -343144, -1490148,
    -6376616, -26992264, -113317936, -472661434, -1961361076, -8104733884,
    -33374212936, -137031378124, -561253753336, -2293947547384, -9358755316816,
    -38121140494564, -155064370272904,
]
assert b[:len(LIVE_OEIS_A127275)] == LIVE_OEIS_A127275
for d in range(MAX_M + 1):
    lhs = b[d] - (4 * b[d - 1] if d >= 1 else 0)
    rhs = S[d] - (1 if d == 1 else 0)
    assert lhs == rhs, f"A127275 series mismatch at m={d}"
print(f"[1] PASS A127275 series (1-4x)B(x) == sqrt(1-4x)-x and b_m = C(2m,m) - 4^(m-1) verified for m=0..{MAX_M}.")

# ---------------------------------------------------------------------------
# 2. Lemma 1 (Laurent-Chebyshev polynomials P_k) and diagonalization of C_n
# ---------------------------------------------------------------------------

# Compute P_k(t) coefficients in Z[t] up to MAX_N:
P_coeffs = [[1], [-2, 1], [2, -4, 1]]  # P_0, P_1, P_2
for k in range(3, MAX_N + 1):
    prev1 = P_coeffs[k - 1]
    prev2 = P_coeffs[k - 2]
    row = [0] * (k + 1)
    # (t - 2) * prev1 - prev2
    for i, c in enumerate(prev1):
        row[i] -= 2 * c
        row[i + 1] += c
    for i, c in enumerate(prev2):
        row[i] -= c
    P_coeffs.append(row)

# Verify Lemma 1(1), 1(2), 1(3) using exact Laurent polynomials dict[exp -> coeff]:
def laurent_mul(A, B):
    res = {}
    for e1, c1 in A.items():
        for e2, c2 in B.items():
            e = e1 + e2
            nc = res.get(e, 0) + c1 * c2
            if nc == 0:
                res.pop(e, None)
            else:
                res[e] = nc
    return res

def laurent_add(A, B):
    res = dict(A)
    for e, c in B.items():
        nc = res.get(e, 0) + c
        if nc == 0:
            res.pop(e, None)
        else:
            res[e] = nc
    return res

t_z = {-1: 1, 0: 2, 1: 1}
t_pows = [{0: 1}]
for m in range(1, MAX_N + 1):
    t_pows.append(laurent_mul(t_pows[-1], t_z))
    assert t_pows[m].get(0, 0) == comb(2 * m, m), f"Lemma 1(1) failed at m={m}"

for k in range(MAX_N + 1):
    # Evaluate P_k(t(z)) in Z[z, z^{-1}]:
    pk_z = {}
    for i, c in enumerate(P_coeffs[k]):
        if c:
            term = {e: c * coef for e, coef in t_pows[i].items()}
            pk_z = laurent_add(pk_z, term)
    if k == 0:
        assert pk_z == {0: 1}
    else:
        assert pk_z == {-k: 1, k: 1}, f"Lemma 1(2) failed at k={k}"

    # Evaluate P_k(4) and P_k(0):
    val4 = sum(c * (4**i) for i, c in enumerate(P_coeffs[k]))
    val0 = P_coeffs[k][0]
    assert val4 == (1 if k == 0 else 2), f"Lemma 1(3) P_k(4) failed at k={k}"
    assert val0 == (1 if k == 0 else 2 * ((-1)**k)), f"Lemma 1(3) P_k(0) failed at k={k}"

# Verify P C_n P^T = D = diag(1, 2, ..., 2) and C_n^{-1} = P^T D^{-1} P at n = MAX_N (covers all principal submatrices):
C_full = [[comb(2 * (i + j), i + j) for j in range(MAX_N + 1)] for i in range(MAX_N + 1)]
P_mat = [[P_coeffs[k][i] if i <= k else 0 for i in range(MAX_N + 1)] for k in range(MAX_N + 1)]
for k in range(MAX_N + 1):
    assert P_mat[k][k] == 1

# Compute P C_full P^T:
PC = [[sum(P_mat[k][r] * C_full[r][j] for r in range(k + 1)) for j in range(MAX_N + 1)] for k in range(MAX_N + 1)]
PCPT = [[sum(PC[k][s] * P_mat[l][s] for s in range(l + 1)) for l in range(MAX_N + 1)] for k in range(MAX_N + 1)]
D_diag = [1] + [2] * MAX_N
for k in range(MAX_N + 1):
    for l in range(MAX_N + 1):
        assert PCPT[k][l] == (D_diag[k] if k == l else 0), f"(P C P^T)[{k},{l}] != D"
print(f"[2] PASS Lemma 1 (Laurent identity, P_k(4), P_k(0)) and exact diagonalization P C_n P^T = diag(1,2,...,2) for n<=25.")

# ---------------------------------------------------------------------------
# 3. Rank-2 decomposition, Weinstein-Aronszajn, direct det(M_n), and live OEIS DATA
# ---------------------------------------------------------------------------

LIVE_OEIS_A127276 = [
    1, 1, -2, -16, -64, -208, -608, -1664, -4352, -11008, -27136, -65536,
    -155648, -364544, -843776, -1933312, -4390912, -9895936, -22151168,
    -49283072, -109051904, -240123904, -526385152, -1149239296, -2499805184,
    -5419040768,
]
assert len(LIVE_OEIS_A127276) == MAX_N + 1

for n in range(MAX_N + 1):
    # C_n^{-1} = P_n^T D_n^{-1} P_n in exact Fraction:
    C_inv = [
        [sum(Fraction(P_mat[k][i] * P_mat[k][j], D_diag[k]) for k in range(n + 1)) for j in range(n + 1)]
        for i in range(n + 1)
    ]
    # Check C_n * C_n^{-1} == I_{n+1}:
    for i in range(n + 1):
        for j in range(n + 1):
            s_ij = sum(C_full[i][r] * C_inv[r][j] for r in range(n + 1))
            assert s_ij == (1 if i == j else 0)

    # Check rank-2 decomposition of M_n and Weinstein-Aronszajn matrix:
    v = [4**i for i in range(n + 1)]
    e0 = [1 if i == 0 else 0 for i in range(n + 1)]
    M_n = [[b[i + j] for j in range(n + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1):
            decomp = Fraction(C_full[i][j]) - Fraction(v[i] * v[j], 4) + Fraction(e0[i] * e0[j], 4)
            assert decomp == M_n[i][j], f"Rank-2 decomposition failed at n={n}, ({i},{j})"

    vCv = sum(v[i] * C_inv[i][j] * v[j] for i in range(n + 1) for j in range(n + 1))
    eCe = C_inv[0][0]
    vCe = sum(v[i] * C_inv[i][0] for i in range(n + 1))
    assert vCv == 2 * n + 1
    assert eCe == 2 * n + 1
    assert vCe == ((-1)**n)

    # W = I_2 + V^T C_n^{-1} U:
    w00 = 1 - Fraction(vCv, 4)
    w01 = Fraction(vCe, 4)
    w10 = -Fraction(vCe, 4)
    w11 = 1 + Fraction(eCe, 4)
    det_W = w00 * w11 - w01 * w10
    assert det_W == 1 - Fraction(n * (n + 1), 4)

    # Direct exact integer Bareiss determinant of M_n:
    det_M = det_exact_int(M_n)
    cf = closed_form_a(n)
    assert det_M == cf, f"det(M_{n}) = {det_M} != closed form {cf}"
    assert det_M == (1 << n) * det_W
    assert det_M == LIVE_OEIS_A127276[n], f"Mismatch against live OEIS at n={n}"

print(f"[3] PASS Rank-2 decomposition, C_n^-1, Weinstein-Aronszajn, direct Bareiss det(M_n) == 2^n - n(n+1)2^(n-2), and all 26 live OEIS A127276 terms (n=0..25).")

# ---------------------------------------------------------------------------
# 4. Ordinary generating function -(4x-1)(x-1)/(2x-1)^3 up to n = 40
# ---------------------------------------------------------------------------

MAX_GF = 40
# -(4x-1)(x-1)/(2x-1)^3 = (1 - 5x + 4x^2) / (1 - 2x)^3
# Multiply (1 - 2x)^3 = 1 - 6x + 12x^2 - 8x^3 against sum_{n=0}^{MAX_GF} a(n) x^n:
a_gf = [closed_form_a(n) for n in range(MAX_GF + 1)]
for n in range(MAX_GF + 1):
    prod_n = a_gf[n]
    if n >= 1:
        prod_n -= 6 * a_gf[n - 1]
    if n >= 2:
        prod_n += 12 * a_gf[n - 2]
    if n >= 3:
        prod_n -= 8 * a_gf[n - 3]
    expected_num = 1 if n == 0 else (-5 if n == 1 else (4 if n == 2 else 0))
    assert prod_n == expected_num, f"G.f. identity failed at x^{n}: got {prod_n}, expected {expected_num}"

print(f"[4] PASS Ordinary g.f. (1 - 2x)^3 * sum a(n) x^n == -(4x-1)(x-1) verified exactly for n=0..{MAX_GF}.")
print("PASS")
