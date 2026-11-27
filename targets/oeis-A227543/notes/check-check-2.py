#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/oeis-A227543/PROOF.md.

Zero floating-point arithmetic: pure-Python exact integer polynomial rings
Z[f_0, ..., f_8] and Z[q] modulo x^{N+1} to verify:
1. Step 1: x-adic stabilization B_m^{(N+1)} == B_m^{(N)} mod x^{N-m+2} and
   B_m(x) * (1 - f_m * x * B_{m+1}(x)) == 1 in Z[f_0..f_8][[x]].
2. Step 2: Product GFs R_tilde_d(x) satisfy R_tilde_d - R_tilde_{d-1} = f_d * x * R_tilde_{d+1}.
3. Step 3: Diagonal recurrence Q_tilde(d,k), exact equivalence P_tilde(n,k) == P(n,k),
   and b(n) == P(n,n) universally in Z[f_0..f_8] for all 0 <= n <= 9.
4. Step 4: Specialization R = Z[q], f(m) = q^m: A(x,q) = 1 + x*A(qx,q)*A(x,q) agrees
   with B_0(x) and P(n,n) for n=0..12, matches all 93 terms of live OEIS A227543 (rows 0..8),
   and matches non-trivial integer sequences f(m) up to n=20.
"""

# ---------------------------------------------------------------------------
# Pure-Python exact multivariate polynomial ring Z[f_0, ..., f_{V-1}]
# Represented as dict[tuple[int, ...], int] (sparse sorted-monomial -> coeff)
# ---------------------------------------------------------------------------

def poly_zero():
    return {}


def poly_one():
    return {(): 1}


def poly_var(idx):
    return {((idx, 1),): 1}


def poly_add(a, b):
    res = dict(a)
    for m, c in b.items():
        nc = res.get(m, 0) + c
        if nc == 0:
            res.pop(m, None)
        else:
            res[m] = nc
    return res


def poly_sub(a, b):
    res = dict(a)
    for m, c in b.items():
        nc = res.get(m, 0) - c
        if nc == 0:
            res.pop(m, None)
        else:
            res[m] = nc
    return res


def mul_monomials(m1, m2):
    if not m1:
        return m2
    if not m2:
        return m1
    i = j = 0
    n1, n2 = len(m1), len(m2)
    out = []
    while i < n1 and j < n2:
        v1, e1 = m1[i]
        v2, e2 = m2[j]
        if v1 == v2:
            out.append((v1, e1 + e2))
            i += 1
            j += 1
        elif v1 < v2:
            out.append((v1, e1))
            i += 1
        else:
            out.append((v2, e2))
            j += 1
    if i < n1:
        out.extend(m1[i:])
    if j < n2:
        out.extend(m2[j:])
    return tuple(out)


def poly_mul(a, b):
    if not a or not b:
        return {}
    res = {}
    for m1, c1 in a.items():
        for m2, c2 in b.items():
            m = mul_monomials(m1, m2)
            nc = res.get(m, 0) + c1 * c2
            if nc == 0:
                res.pop(m, None)
            else:
                res[m] = nc
    return res


# ---------------------------------------------------------------------------
# Formal power series in R[[x]] truncated at degree D (length D+1 list)
# ---------------------------------------------------------------------------

def fps_mul(A, B, D):
    out = [poly_zero() for _ in range(D + 1)]
    for i in range(min(len(A), D + 1)):
        if not A[i]:
            continue
        for j in range(min(len(B), D + 1 - i)):
            if B[j]:
                out[i + j] = poly_add(out[i + j], poly_mul(A[i], B[j]))
    return out


def fps_inv_unit(U, D):
    """Exact inverse of U = 1 + sum_{k>=1} u_k x^k mod x^{D+1}."""
    assert U[0] == poly_one(), "Not a unit with constant term 1"
    inv = [poly_zero() for _ in range(D + 1)]
    inv[0] = poly_one()
    for k in range(1, D + 1):
        acc = poly_zero()
        for j in range(1, k + 1):
            if j < len(U) and U[j] and inv[k - j]:
                acc = poly_sub(acc, poly_mul(U[j], inv[k - j]))
        inv[k] = acc
    return inv


def fps_one_minus_fxS(f_elem, S, D):
    """Compute 1 - f_elem * x * S mod x^{D+1}."""
    out = [poly_zero() for _ in range(D + 1)]
    out[0] = poly_one()
    for k in range(1, D + 1):
        if k - 1 < len(S) and S[k - 1]:
            out[k] = poly_sub(poly_zero(), poly_mul(f_elem, S[k - 1]))
    return out


# ---------------------------------------------------------------------------
# 1. Universal check over Z[f_0, ..., f_9] for n = 0..9
# ---------------------------------------------------------------------------

MAX_N = 9
F = [poly_var(m) for m in range(MAX_N + 2)]

# Compute approximants B_m^{(N)} mod x^{MAX_N + 1} for N = 0..MAX_N
B_approx = {}
for N in range(MAX_N + 1):
    cur = [poly_one()] + [poly_zero() for _ in range(MAX_N)]  # B_{N+1}^{(N)} = 1
    B_approx[(N, N + 1)] = cur
    for m in range(N, -1, -1):
        denom = fps_one_minus_fxS(F[m], cur, MAX_N)
        cur = fps_inv_unit(denom, MAX_N)
        B_approx[(N, m)] = cur

# Step 1: check B_m^{(N+1)} == B_m^{(N)} mod x^{N - m + 2}
for N in range(MAX_N):
    for m in range(N + 2):
        mod_deg = N - m + 2  # checks indices 0 .. mod_deg - 1
        assert mod_deg <= MAX_N + 1
        b_next = B_approx[(N + 1, m)]
        b_prev = B_approx[(N, m)]
        for k in range(min(mod_deg, MAX_N + 1)):
            assert b_next[k] == b_prev[k], f"Stabilization failed at N={N}, m={m}, k={k}"

# Exact B_m(x) mod x^{MAX_N + 1} (B_m^{(MAX_N)} is exact mod x^{MAX_N - m + 2}, so use N = MAX_N + MAX_N?
# Wait: for R_tilde_d mod x^{MAX_N + 1}, we need B_m(x) exact mod x^{MAX_N + 1} for all m=0..MAX_N!
# By Step 1, B_m^{(N)} agrees with B_m^{(N+1)} mod x^{N - m + 2}; choosing N_top = 2*MAX_N gives
# exactness mod x^{MAX_N + 2} for all 0 <= m <= MAX_N!
N_TOP = 2 * MAX_N
B_exact = {}
cur = [poly_one()] + [poly_zero() for _ in range(MAX_N)]
for m in range(N_TOP, -1, -1):
    f_m = poly_var(m)
    denom = fps_one_minus_fxS(f_m, cur, MAX_N)
    cur = fps_inv_unit(denom, MAX_N)
    if m <= MAX_N + 1:
        B_exact[m] = cur

# Verify exact CF equation B_m(x) * (1 - f(m)*x*B_{m+1}(x)) == 1 mod x^{MAX_N + 1} for m = 0..MAX_N:
unit_one = [poly_one()] + [poly_zero() for _ in range(MAX_N)]
for m in range(MAX_N + 1):
    lhs = fps_mul(B_exact[m], fps_one_minus_fxS(F[m], B_exact[m + 1], MAX_N), MAX_N)
    assert lhs == unit_one, f"Exact CF equation failed at m={m}"
print(f"[1] PASS Step 1: B_m^(N) x-adic stabilization and exact CF equation in Z[f_0..f_{MAX_N}] mod x^{MAX_N+1}.")

# Step 2: R_tilde_d(x) = prod_{j=0}^d B_j(x), R_tilde_{-1}(x) = 1
R_tilde = {-1: unit_one}
for d in range(MAX_N + 2):
    R_tilde[d] = fps_mul(R_tilde[d - 1], B_exact[d] if d in B_exact else fps_inv_unit(fps_one_minus_fxS(poly_var(d), [poly_one()] + [poly_zero()]*MAX_N, MAX_N), MAX_N), MAX_N)

# Better: ensure B_exact has m up to MAX_N + 1 so R_tilde[d] uses exact B_d for d = 0..MAX_N + 1 (we populated m <= MAX_N + 1 above!)
for d in range(MAX_N + 1):
    lhs_diff = [poly_sub(R_tilde[d][k], R_tilde[d - 1][k]) for k in range(MAX_N + 1)]
    # f(d) * x * R_tilde_{d+1}(x)
    rhs_shift = [poly_zero()] + [poly_mul(F[d], R_tilde[d + 1][k - 1]) for k in range(1, MAX_N + 1)]
    assert lhs_diff == rhs_shift, f"Step 2 product GF identity failed at d={d}"
print(f"[2] PASS Step 2: R_tilde_d(x) - R_tilde_{{d-1}}(x) == f_d * x * R_tilde_{{d+1}}(x) for d=0..{MAX_N} mod x^{MAX_N+1}.")

# Step 3: Q_tilde(d, k), P_tilde(n, k), and Kurkov's P(n, k)
def Q_tilde(d, k):
    return R_tilde[d][k]

for d in range(-1, MAX_N + 1):
    assert Q_tilde(d, 0) == poly_one()
for k in range(1, MAX_N + 1):
    assert Q_tilde(-1, k) == poly_zero()
for d in range(MAX_N + 1):
    for k in range(1, MAX_N + 1):
        assert Q_tilde(d, k) == poly_add(Q_tilde(d - 1, k), poly_mul(F[d], Q_tilde(d + 1, k - 1)))

# Compute Kurkov's P(n, k) directly from the recurrence in OEIS A227543:
P = {}
for n in range(MAX_N + 1):
    P[(n, 0)] = poly_one()
    for k in range(1, n + 3):
        P[(n, k)] = poly_zero()

for n in range(1, MAX_N + 1):
    for k in range(1, n + 1):
        P[(n, k)] = poly_add(P[(n - 1, k)], poly_mul(F[n - k], P[(n, k - 1)]))

# Verify P_tilde(n, k) == P(n, k) for all 0 <= n <= MAX_N, 0 <= k <= n + 1, and b(n) == P(n, n):
b_seq = B_exact[0]
for n in range(MAX_N + 1):
    for k in range(n + 2):
        p_tilde = Q_tilde(n - k, k) if k <= n else poly_zero()
        assert p_tilde == P[(n, k)], f"P_tilde != P at (n={n}, k={k})"
    assert b_seq[n] == P[(n, n)], f"b({n}) != P({n},{n}) in Z[f_0..f_{MAX_N}]"
print(f"[3] PASS Step 3: Q_tilde diagonal recurrence, P_tilde(n,k)==P(n,k), and universal b(n)==P(n,n) in Z[f_0..f_{MAX_N}] for n=0..{MAX_N}.")

# ---------------------------------------------------------------------------
# 2. Specialization R = Z[q], f(m) = q^m, and live OEIS A227543 data (rows 0..8)
# ---------------------------------------------------------------------------

# Sparse univariate polynomial in Z[q]: dict[int, int]
def q_add(a, b):
    res = dict(a)
    for e, c in b.items():
        nc = res.get(e, 0) + c
        if nc == 0:
            res.pop(e, None)
        else:
            res[e] = nc
    return res

def q_sub(a, b):
    res = dict(a)
    for e, c in b.items():
        nc = res.get(e, 0) - c
        if nc == 0:
            res.pop(e, None)
        else:
            res[e] = nc
    return res

def q_mul(a, b):
    res = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = e1 + e2
            nc = res.get(e, 0) + c1 * c2
            if nc == 0:
                res.pop(e, None)
            else:
                res[e] = nc
    return res

def q_shift_x(A_fps):
    """Given A(x, q), return A(q*x, q): [x^n] -> q^n * [x^n]."""
    out = []
    for n, p in enumerate(A_fps):
        out.append({e + n: c for e, c in p.items()})
    return out

def q_fps_mul(A, B, D):
    out = [{} for _ in range(D + 1)]
    for i in range(min(len(A), D + 1)):
        if not A[i]:
            continue
        for j in range(min(len(B), D + 1 - i)):
            if B[j]:
                out[i + j] = q_add(out[i + j], q_mul(A[i], B[j]))
    return out

N_Q = 12
# Fixed point of A(x, q) = 1 + x * A(qx, q) * A(x, q) in Z[q][[x]] mod x^{N_Q+1}:
A_fps = [{0: 1}] + [{} for _ in range(N_Q)]
for _ in range(N_Q):
    Aqx = q_shift_x(A_fps)
    prod = q_fps_mul(Aqx, A_fps, N_Q)
    A_fps = [{0: 1}] + prod[:N_Q]

# Verify functional equation A(x, q) == 1 + x * A(qx, q) * A(x, q) mod x^{N_Q+1}:
Aqx = q_shift_x(A_fps)
rhs_fe = [{0: 1}] + q_fps_mul(Aqx, A_fps, N_Q)[:N_Q]
assert A_fps == rhs_fe, "Functional equation A(x,q) = 1 + x*A(qx,q)*A(x,q) failed!"

# Independently compute B_0(x) mod x^{N_Q+1} from the continued fraction with f(m) = q^m:
cur_B = [{0: 1}] + [{} for _ in range(N_Q)]
for m in range(2 * N_Q, -1, -1):
    # B_m = 1 / (1 - q^m * x * B_{m+1})
    denom = [{0: 1}] + [{} for _ in range(N_Q)]
    for k in range(1, N_Q + 1):
        denom[k] = {e + m: -c for e, c in cur_B[k - 1].items()}
    inv_b = [{0: 1}] + [{} for _ in range(N_Q)]
    for k in range(1, N_Q + 1):
        acc = {}
        for j in range(1, k + 1):
            acc = q_sub(acc, q_mul(denom[j], inv_b[k - j]))
        inv_b[k] = acc
    cur_B = inv_b
assert cur_B == A_fps, "Continued fraction B_0(x) disagrees with A(x, q)!"

# Independently compute Kurkov's P(n, k) with f(m) = q^m up to n = N_Q:
P_q = {}
for n in range(N_Q + 1):
    P_q[(n, 0)] = {0: 1}
    for k in range(1, n + 2):
        P_q[(n, k)] = {}
for n in range(1, N_Q + 1):
    for k in range(1, n + 1):
        fm_term = {e + (n - k): c for e, c in P_q[(n, k - 1)].items()}
        P_q[(n, k)] = q_add(P_q[(n - 1, k)], fm_term)

for n in range(N_Q + 1):
    assert A_fps[n] == P_q[(n, n)], f"A227543 specialization failed at n={n}"

# Verify all 93 terms of live OEIS A227543 (rev. 113) rows n = 0..8:
LIVE_OEIS_A227543 = [
    1,
    1,
    1, 1,
    1, 2, 1, 1,
    1, 3, 3, 3, 2, 1, 1,
    1, 4, 6, 7, 7, 5, 5, 3, 2, 1, 1,
    1, 5, 10, 14, 17, 16, 16, 14, 11, 9, 7, 5, 3, 2, 1, 1,
    1, 6, 15, 25, 35, 40, 43, 44, 40, 37, 32, 28, 22, 18, 13, 11, 7, 5, 3, 2, 1, 1,
    1, 7, 21, 41, 65, 86, 102, 115, 118, 118, 113, 106, 96, 85, 73, 63, 53, 42, 34, 26, 20, 15, 11, 7, 5, 3, 2, 1, 1,
]
built = []
for n in range(9):
    max_deg = n * (n - 1) // 2
    row_p = P_q[(n, n)]
    assert all(0 <= e <= max_deg for e in row_p), f"Unexpected q-degree in row n={n}"
    for k in range(max_deg + 1):
        built.append(row_p.get(k, 0))
assert built == LIVE_OEIS_A227543, "Mismatch against live OEIS A227543 rows 0..8!"
print(f"[4] PASS Specialization f(m)=q^m: A(x,q)==B_0(x)==sum P(n,n)x^n mod x^{N_Q+1}, and all {len(built)} terms match live OEIS A227543 (rows 0..8).")

# ---------------------------------------------------------------------------
# 3. Integer-sequence sanity checks up to n = 20 for diverse f(m)
# ---------------------------------------------------------------------------

def check_integer_sequence(name, f_vals, n_max=20):
    # CF evaluation B_0(x) mod x^{n_max+1}
    cur = [1] + [0] * n_max
    for m in range(2 * n_max, -1, -1):
        fm = f_vals[m]
        denom = [1] + [-fm * cur[k - 1] for k in range(1, n_max + 1)]
        inv_b = [1] + [0] * n_max
        for k in range(1, n_max + 1):
            s = 0
            for j in range(1, k + 1):
                s -= denom[j] * inv_b[k - j]
            inv_b[k] = s
        cur = inv_b
    # Kurkov P(n, k)
    Pint = {(n, 0): 1 for n in range(n_max + 1)}
    for n in range(n_max + 1):
        for k in range(1, n + 2):
            Pint[(n, k)] = 0
    for n in range(1, n_max + 1):
        for k in range(1, n + 1):
            Pint[(n, k)] = Pint[(n - 1, k)] + f_vals[n - k] * Pint[(n, k - 1)]
    for n in range(n_max + 1):
        assert cur[n] == Pint[(n, n)], f"Integer check {name} failed at n={n}"

M_TOT = 45
fib = [1, 1]
for _ in range(M_TOT):
    fib.append(fib[-1] + fib[-2])

check_integer_sequence("linear f(m)=m+1", [m + 1 for m in range(M_TOT)])
check_integer_sequence("alternating f(m)=(-1)^m*(m+2)", [((-1)**m) * (m + 2) for m in range(M_TOT)])
check_integer_sequence("zero-gaps f(m)=0 if m%3==1 else 2*m+1", [0 if m % 3 == 1 else 2 * m + 1 for m in range(M_TOT)])
check_integer_sequence("fibonacci f(m)=F_{m+1}", fib[:M_TOT])
print("[5] PASS Arbitrary integer-sequence checks up to n=20 (linear, alternating, zero-gapped, Fibonacci).")
print("PASS")
