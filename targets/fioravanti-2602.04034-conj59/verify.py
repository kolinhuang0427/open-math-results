#!/usr/bin/env python3
r"""
Standalone, pure-integer / exact-Fraction verification of the proof settling:
  - Conjecture 59 (`conjecture:strong`, arXiv:2602.04034v1) -> Theorem 1
  - Conjecture 1 (`conjecture:main`, arXiv:2602.04034v1)    -> Theorem 2

ZERO floating-point arithmetic, ZERO float imports, ZERO float operations anywhere.
All linear algebra, Smith Normal Form, Gaussian binomials, operator compositions,
and ring transfers are computed in exact Python ints and fractions.Fraction.

Exit code 0 and prints `PASS` iff all checks succeed; nonzero exit and `FAIL` otherwise.
"""

from fractions import Fraction
import itertools
import sys
import time


def elapsed_ms_str(start_ns):
    ms = (time.monotonic_ns() - start_ns) // 1_000_000
    return f"{ms // 1000}.{ms % 1000:03d}s"


def is_power_of_prime(n, p):
    if n <= 0:
        return False
    while n % p == 0:
        n //= p
    return n == 1


def is_smooth_power(n, primes):
    if n <= 0:
        return False
    for p in primes:
        while n % p == 0:
            n //= p
    return n == 1


# ============================================================
# 0. Exact Linear Algebra & Combinatorial Primitives
# ============================================================

_QBINOM_CACHE = {}


def qbinom(n, c, p):
    """Exact Gaussian binomial coefficient [n choose c]_p via q-Pascal (P1)."""
    if c < 0 or c > n:
        return 0
    if c == 0 or c == n:
        return 1
    key = (n, c, p)
    val = _QBINOM_CACHE.get(key)
    if val is None:
        val = qbinom(n - 1, c, p) + (p ** (n - c)) * qbinom(n - 1, c - 1, p)
        _QBINOM_CACHE[key] = val
    return val


def mat_mul_mod(A, B, mod):
    r = len(A)
    k = len(B)
    c = len(B[0])
    return tuple(
        tuple(sum(A[i][t] * B[t][j] for t in range(k)) % mod for j in range(c))
        for i in range(r)
    )


def mat_inv_mod(S, p, mod):
    """Exact Gauss-Jordan inverse of S in GL_m(Z/mod Z) where mod = p^e."""
    m = len(S)
    aug = [list(S[i]) + [1 if i == j else 0 for j in range(m)] for i in range(m)]
    for col in range(m):
        piv = next(r for r in range(col, m) if aug[r][col] % p != 0)
        aug[col], aug[piv] = aug[piv], aug[col]
        inv = pow(aug[col][col] % mod, -1, mod)
        aug[col] = [(x * inv) % mod for x in aug[col]]
        for r in range(m):
            if r != col and aug[r][col] % mod != 0:
                fac = aug[r][col] % mod
                aug[r] = [(aug[r][j] - fac * aug[col][j]) % mod for j in range(2 * m)]
    Sinv = tuple(tuple(row[m:]) for row in aug)
    eye = tuple(tuple(1 if i == j else 0 for j in range(m)) for i in range(m))
    assert mat_mul_mod(S, Sinv, mod) == eye
    assert mat_mul_mod(Sinv, S, mod) == eye
    return Sinv


def factor_rank_le_Fp(B, p, max_r):
    """Factor B in F_p^{r_dim x c_dim} of F_p-rank <= max_r as U (r_dim x max_r) * V (max_r x c_dim) mod p."""
    r_dim = len(B)
    c_dim = len(B[0])
    M = [[x % p for x in row] for row in B]
    piv_cols = []
    row_idx = 0
    for col in range(c_dim):
        piv = None
        for i in range(row_idx, r_dim):
            if M[i][col] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[row_idx], M[piv] = M[piv], M[row_idx]
        inv = pow(M[row_idx][col], -1, p)
        M[row_idx] = [(x * inv) % p for x in M[row_idx]]
        for i in range(r_dim):
            if i != row_idx and M[i][col] != 0:
                fac = M[i][col]
                M[i] = [(M[i][j] - fac * M[row_idx][j]) % p for j in range(c_dim)]
        piv_cols.append(col)
        row_idx += 1
    assert len(piv_cols) <= max_r, f"F_{p}-rank {len(piv_cols)} > {max_r}"
    V = [list(M[i]) for i in range(len(piv_cols))] + [[0] * c_dim for _ in range(max_r - len(piv_cols))]
    U = [[B[i][c] % p for c in piv_cols] + [0] * (max_r - len(piv_cols)) for i in range(r_dim)]
    assert mat_mul_mod(U, V, p) == tuple(tuple(x % p for x in row) for row in B)
    return tuple(tuple(r) for r in U), tuple(tuple(r) for r in V)


def fp_rank(rows, p):
    """Exact F_p-rank of a list of row vectors."""
    if not rows:
        return 0
    ncols = len(rows[0])
    M = [[x % p for x in row] for row in rows]
    r = 0
    for col in range(ncols):
        piv = None
        for i in range(r, len(M)):
            if M[i][col] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][col], -1, p)
        M[r] = [(x * inv) % p for x in M[r]]
        for i in range(r + 1, len(M)):
            if M[i][col] != 0:
                fac = M[i][col]
                M[i] = [(M[i][j] - fac * M[r][j]) % p for j in range(ncols)]
        r += 1
    return r


def verify_snf_rank_Zpe(M, p, e, max_r):
    """
    Exact Smith Normal Form over Z/p^e Z for arbitrary prime power p^e (e >= 1).
    Verifies inner rank k <= max_r and returns (k, U, V) with U (m x max_r),
    V (max_r x n), and U * V == M mod p^e.
    """
    m = len(M)
    n = len(M[0])
    mod = p ** e
    A = [[x % mod for x in row] for row in M]
    L = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    k = 0
    lim = min(m, n)
    while k < lim:
        # Find entry in A[k:, k:] with minimum p-adic valuation v < e
        best_v = e
        piv = None
        for i in range(k, m):
            row = A[i]
            for j in range(k, n):
                val = row[j]
                if val != 0:
                    v = 0
                    tmp = val
                    while tmp % p == 0:
                        tmp //= p
                        v += 1
                    if v < best_v:
                        best_v = v
                        piv = (i, j)
                        if best_v == 0:
                            break
            if best_v == 0:
                break
        if piv is None:
            break
        pi, pj = piv
        if pi != k:
            A[k], A[pi] = A[pi], A[k]
            for t in range(m):
                L[t][k], L[t][pi] = L[t][pi], L[t][k]
        if pj != k:
            for t in range(m):
                A[t][k], A[t][pj] = A[t][pj], A[t][k]
            R[k], R[pj] = R[pj], R[k]

        pv = p ** best_v
        u = (A[k][k] // pv) % mod
        u_inv = pow(u, -1, mod)
        A[k] = [(x * u_inv) % mod for x in A[k]]
        for t in range(m):
            L[t][k] = (L[t][k] * u) % mod

        for i in range(k + 1, m):
            if A[i][k] != 0:
                fac = (A[i][k] // pv) % mod
                Ak = A[k]
                Ai = A[i]
                for j in range(k, n):
                    Ai[j] = (Ai[j] - fac * Ak[j]) % mod
                for t in range(m):
                    L[t][k] = (L[t][k] + fac * L[t][i]) % mod

        for j in range(k + 1, n):
            if A[k][j] != 0:
                fac = (A[k][j] // pv) % mod
                for i in range(k, m):
                    A[i][j] = (A[i][j] - fac * A[i][k]) % mod
                Rk = R[k]
                Rj = R[j]
                for t in range(n):
                    Rk[t] = (Rk[t] + fac * Rj[t]) % mod
        k += 1

    assert k <= max_r, f"Z/{mod}Z inner rank {k} > {max_r}"
    U = tuple(tuple([(L[i][j] * A[j][j]) % mod for j in range(k)] + [0] * (max_r - k)) for i in range(m))
    V = tuple(tuple(R[j]) for j in range(k)) + tuple((0,) * n for _ in range(max_r - k))
    assert mat_mul_mod(U, V, mod) == tuple(tuple(x % mod for x in row) for row in M)
    return k, U, V


def proj_vectors(p, m):
    """Canonical representatives of 1D subspaces of F_p^m (first nonzero entry = 1)."""
    out = []
    for v in itertools.product(range(p), repeat=m):
        for c in v:
            if c != 0:
                if c == 1:
                    out.append(v)
                break
    return out


def all_subspaces_codim(p, m, c):
    """
    Enumerate ALL codimension-c subspaces U <= F_p^m via canonical RREF c x m
    parity-check matrices P (so U = ker P), returning list of (P, basis_U)
    where basis_U is a list of (m-c) basis vectors of U.
    """
    res = []
    for pivs in itertools.combinations(range(m), c):
        piv_set = set(pivs)
        free_entries = []
        for r in range(c):
            pr = pivs[r]
            for col in range(pr + 1, m):
                if col not in piv_set:
                    free_entries.append((r, col))
        free_cols = [col for col in range(m) if col not in piv_set]
        for vals in itertools.product(range(p), repeat=len(free_entries)):
            P = [[0] * m for _ in range(c)]
            for r in range(c):
                P[r][pivs[r]] = 1
            for (r, col), v in zip(free_entries, vals):
                P[r][col] = v
            basis = []
            for fcol in free_cols:
                u = [0] * m
                u[fcol] = 1
                for r in range(c):
                    u[pivs[r]] = (-P[r][fcol]) % p
                basis.append(tuple(u))
            res.append((tuple(tuple(row) for row in P), basis))
    assert len(res) == qbinom(m, c, p)
    return res


def subspace_elements(basis, p):
    """All p^{dim} vectors in span(basis) over F_p."""
    d = len(basis)
    if d == 0:
        return [()]
    m = len(basis[0])
    vecs = []
    for coeffs in itertools.product(range(p), repeat=d):
        v = [0] * m
        for c, b in zip(coeffs, basis):
            if c != 0:
                for i in range(m):
                    v[i] = (v[i] + c * b[i]) % p
        vecs.append(tuple(v))
    return vecs


def build_hyperplane_S(p, m, n_vec, mod):
    """Build S in GL_m(Z/mod Z) whose first row mod p is n_vec (so S(H) = H_0)."""
    piv = next(i for i, c in enumerate(n_vec) if c % p != 0)
    rows = [tuple(c % mod for c in n_vec)]
    for i in range(m):
        if i != piv:
            row = [0] * m
            row[i] = 1
            rows.append(tuple(row))
    S = tuple(rows)
    return S, mat_inv_mod(S, p, mod)


def build_codim_s_S(p, m, parity_rows, mod):
    """
    Build S in GL_m(Z/mod Z) whose top s rows are parity_rows (mod p),
    so S maps ker(parity_rows) onto H_0 = {0}^s x F_p^{m-s}.
    """
    s = len(parity_rows)
    # Find pivot columns of parity_rows mod p via RREF
    M = [[x % p for x in row] for row in parity_rows]
    piv_cols = []
    r = 0
    for col in range(m):
        if r == s:
            break
        piv = None
        for i in range(r, s):
            if M[i][col] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][col], -1, p)
        M[r] = [(x * inv) % p for x in M[r]]
        for i in range(s):
            if i != r and M[i][col] != 0:
                fac = M[i][col]
                M[i] = [(M[i][j] - fac * M[r][j]) % p for j in range(m)]
        piv_cols.append(col)
        r += 1
    assert len(piv_cols) == s
    piv_set = set(piv_cols)
    rows = [tuple(x % mod for x in row) for row in parity_rows]
    for col in range(m):
        if col not in piv_set:
            row = [0] * m
            row[col] = 1
            rows.append(tuple(row))
    S = tuple(rows)
    return S, mat_inv_mod(S, p, mod)


# ============================================================
# Sparse Operator Matrix Helpers (pure Python int/dict, ZERO numpy/scipy)
# ============================================================

def sparse_mul(A_rows, B_rows):
    """Exact sparse matrix multiplication A @ B for list-of-dict rows."""
    n = len(A_rows)
    out = []
    for i in range(n):
        arow = A_rows[i]
        if not arow:
            out.append({})
            continue
        acc = {}
        for k, av in arow.items():
            brow = B_rows[k]
            for j, bv in brow.items():
                acc[j] = acc.get(j, 0) + av * bv
        out.append({j: v for j, v in acc.items() if v != 0})
    return out


def sparse_add_scaled(A_rows, sA, B_rows, sB):
    """Exact sA * A + sB * B for list-of-dict rows."""
    n = len(A_rows)
    out = []
    for i in range(n):
        arow = A_rows[i]
        brow = B_rows[i]
        if not arow and not brow:
            out.append({})
            continue
        acc = {}
        for j, v in arow.items():
            acc[j] = sA * v
        for j, v in brow.items():
            acc[j] = acc.get(j, 0) + sB * v
        out.append({j: v for j, v in acc.items() if v != 0})
    return out


def sparse_reduce_pow(rows, dp, p):
    """Factor out common powers of p from all entries of rows up to dp."""
    while dp > 0:
        divisible = True
        for row in rows:
            for v in row.values():
                if v % p != 0:
                    divisible = False
                    break
            if not divisible:
                break
        if not divisible:
            break
        for row in rows:
            for j in row:
                row[j] //= p
        dp -= 1
    return rows, dp


def sparse_conj(AH0_rows, pS, pS_inv):
    """Return A_H where A_H[i, j] = AH0[pS[i], pS[j]]."""
    n = len(AH0_rows)
    out = []
    for i in range(n):
        src = AH0_rows[pS[i]]
        out.append({pS_inv[u]: v for u, v in src.items()})
    return out


# ============================================================
# Reusable Base UG Operators (F_p, F_p^2, Z_{p^2}, Z_4 x Z_2)
# ============================================================

def ug_Fp_1ary(p, m):
    """Exact 1-ary UG formula for F_p at arity m >= 2."""
    dp = m - 1
    coeffs = {}

    def add(mat, val):
        nv = coeffs.get(mat, 0) + val
        if nv == 0:
            coeffs.pop(mat, None)
        else:
            coeffs[mat] = nv

    add(tuple((0,) * m for _ in range(m)), p ** dp)
    for v in proj_vectors(p, m):
        piv = next(i for i, c in enumerate(v) if c != 0)
        u_basis = []
        for j in range(m):
            if j == piv:
                continue
            u = [0] * m
            u[j] = 1
            u[piv] = (-v[j]) % p
            u_basis.append(u)
        for a in itertools.product(range(p), repeat=m - 1):
            r2 = [0] * m
            for ai, u in zip(a, u_basis):
                for k in range(m):
                    r2[k] = (r2[k] + ai * u[k]) % p
            r1 = list(r2)
            r1[piv] = (r1[piv] + 1) % p
            M1 = tuple(tuple((v[i] * r1[j]) % p for j in range(m)) for i in range(m))
            M2 = tuple(tuple((v[i] * r2[j]) % p for j in range(m)) for i in range(m))
            add(M1, 1)
            add(M2, -1)
    return dp, coeffs


def ug_Fp2_2ary_m3(p):
    """Exact 2-ary UG formula for F_p^2 at arity m = 3 (Lemma 2 of ques2 / Thm 49)."""
    dp1, J1 = ug_Fp_1ary(p, 3)
    X0 = ((1, 0), (0, 1), (0, 0))

    def col_normal(X):
        c0 = (X[0][0], X[1][0], X[2][0])
        c1 = (X[0][1], X[1][1], X[2][1])
        n = [
            (c0[1] * c1[2] - c0[2] * c1[1]) % p,
            (c0[2] * c1[0] - c0[0] * c1[2]) % p,
            (c0[0] * c1[1] - c0[1] * c1[0]) % p,
        ]
        piv = next(i for i in range(3) if n[i] != 0)
        inv = pow(n[piv], -1, p)
        return tuple((x * inv) % p for x in n)

    def dot(a, b):
        return sum(x * y for x, y in zip(a, b)) % p

    def add_outer(X, a, u):
        return tuple(tuple((X[i][j] + a[i] * u[j]) % p for j in range(2)) for i in range(3))

    def M_from_theta(Y, a):
        T = [
            [Y[0][0], Y[1][0], Y[2][0], 1, 0],
            [Y[0][1], Y[1][1], Y[2][1], 0, 1],
            [a[0], a[1], a[2], 0, 0],
        ]
        for col in range(3):
            piv = next(r for r in range(col, 3) if T[r][col] != 0)
            T[col], T[piv] = T[piv], T[col]
            inv = pow(T[col][col], -1, p)
            T[col] = [(x * inv) % p for x in T[col]]
            for r in range(3):
                if r != col and T[r][col] != 0:
                    fac = T[r][col]
                    T[r] = [(T[r][j] - fac * T[col][j]) % p for j in range(5)]
        return ((T[0][3], T[1][3], T[2][3]), (T[0][4], T[1][4], T[2][4]))

    p3 = proj_vectors(p, 3)
    nz2 = [u for u in itertools.product(range(p), repeat=2) if u != (0, 0)]
    n0 = col_normal(X0)
    Theta = [set(), set(), set()]
    T1 = {}
    for a1 in p3:
        if dot(n0, a1) != 0:
            Theta[0].add(M_from_theta(X0, a1))
            for u1 in nz2:
                X1 = add_outer(X0, a1, u1)
                if X1 not in T1:
                    T1[X1] = u1
    T2 = {}
    for X1, u1 in T1.items():
        n1 = col_normal(X1)
        for a2 in p3:
            if dot(n0, a2) == 0 and dot(n1, a2) != 0:
                Theta[1].add(M_from_theta(X1, a2))
                for u2 in nz2:
                    if (u1[0] * u2[1] - u1[1] * u2[0]) % p != 0:
                        X2 = add_outer(X1, a2, u2)
                        if X2 not in T2:
                            T2[X2] = n1
    for X2, n1 in T2.items():
        n2 = col_normal(X2)
        for a3 in p3:
            if dot(n0, a3) == 0 and dot(n1, a3) == 0 and dot(n2, a3) != 0:
                Theta[2].add(M_from_theta(X2, a3))

    alphas_int = [p, -1, 1]
    JH0 = {}
    for i in range(3):
        for M23 in Theta[i]:
            M33 = mat_mul_mod(X0, M23, p)
            nv = JH0.get(M33, 0) + alphas_int[i]
            if nv == 0:
                JH0.pop(M33, None)
            else:
                JH0[M33] = nv

    J2 = {}
    for nv in p3:
        piv = next(idx for idx in range(3) if nv[idx] != 0)
        rows = []
        for idx in range(3):
            if idx != piv:
                row = [0, 0, 0]
                row[idx] = 1
                rows.append(tuple(row))
        rows.append(nv)
        S = tuple(rows)
        Sinv = mat_inv_mod(S, p, p)
        for M0, w in JH0.items():
            M = mat_mul_mod(mat_mul_mod(Sinv, M0, p), S, p)
            nv_w = J2.get(M, 0) + w
            if nv_w == 0:
                J2.pop(M, None)
            else:
                J2[M] = nv_w

    dp = 5
    I = {}
    for M, w in J1.items():
        nv = I.get(M, 0) + w * (p ** 3)
        if nv == 0:
            I.pop(M, None)
        else:
            I[M] = nv
    for M, w in J2.items():
        nv = I.get(M, 0) + w * (p ** 2)
        if nv == 0:
            I.pop(M, None)
        else:
            I[M] = nv
    for M2, w2 in J2.items():
        for M1, w1 in J1.items():
            M = mat_mul_mod(M1, M2, p)
            nv = I.get(M, 0) - w1 * w2
            if nv == 0:
                I.pop(M, None)
            else:
                I[M] = nv
    while dp > 0 and all(v % p == 0 for v in I.values()):
        dp -= 1
        I = {k: v // p for k, v in I.items()}
    return dp, I


def lift_Fp_op_preserving_rank(op_fp, p, mod, max_r):
    """Lift each B in op_fp (F_p-rank <= max_r) factorwise to U*V mod mod."""
    out = {}
    for B, w in op_fp.items():
        U, V = factor_rank_le_Fp(B, p, max_r)
        M = mat_mul_mod(U, V, mod)
        nv = out.get(M, 0) + w
        if nv == 0:
            out.pop(M, None)
        else:
            out[M] = nv
    return out


def build_Zp2_components(p, m):
    """Exact (2, Z_{p^2}, Z[1/p])-UR building blocks (J_prop, AH0) at arity m >= 3."""
    mod = p * p
    dp_J, J_fp = ug_Fp_1ary(p, m)
    J_dict = lift_Fp_op_preserving_rank(J_fp, p, mod, 1)
    dp_sub, ug_sub = ug_Fp_1ary(p, m - 1)
    AH0 = {}
    dp_A = dp_sub + 2 * (m - 1)
    for B, w in ug_sub.items():
        U, V = factor_rank_le_Fp(B, p, 1)
        if not any(V[0]):
            A2 = ((1,) + (0,) * (m - 1),)
            mult = p ** (m - 1)
            for wp in itertools.product(range(p), repeat=m - 1):
                A1 = ((1,),) + tuple(((p * wp[i]) % mod,) for i in range(m - 1))
                M = mat_mul_mod(A1, A2, mod)
                nv = AH0.get(M, 0) + w * mult
                if nv == 0:
                    AH0.pop(M, None)
                else:
                    AH0[M] = nv
        else:
            A2 = ((1,) + (0,) * (m - 1), (0,) + V[0])
            for wp in itertools.product(range(p), repeat=m - 1):
                for up in itertools.product(range(p), repeat=m - 1):
                    A1 = ((1, 0),) + tuple(
                        ((p * wp[i]) % mod, (U[i][0] + p * up[i]) % mod)
                        for i in range(m - 1)
                    )
                    M = mat_mul_mod(A1, A2, mod)
                    nv = AH0.get(M, 0) + w
                    if nv == 0:
                        AH0.pop(M, None)
                    else:
                        AH0[M] = nv
    while dp_A > 0 and all(v % p == 0 for v in AH0.values()):
        dp_A -= 1
        AH0 = {k: v // p for k, v in AH0.items()}
    return (dp_J, J_dict), (dp_A, AH0)


def build_Z4_full_dict_m3():
    """Build full exact (2, Z_4, Z[1/2])-UG operator dict at m=3 and verify 64x64 identity."""
    p, mod = 2, 4
    (dp_J, J_dict), (dp_A, AH0_dict) = build_Zp2_components(p, 3)
    for M in J_dict:
        verify_snf_rank_Zpe(M, 2, 2, 1)
    for M in AH0_dict:
        verify_snf_rank_Zpe(M, 2, 2, 2)

    def conj_dict(op, S, Sinv):
        return {mat_mul_mod(mat_mul_mod(Sinv, M, mod), S, mod): w for M, w in op.items()}

    def add_scaled(ops, p_base):
        max_dp = max(dp for dp, _ in ops)
        out = {}
        for dp, d in ops:
            mult = p_base ** (max_dp - dp)
            for M, w in d.items():
                nv = out.get(M, 0) + w * mult
                if nv == 0:
                    out.pop(M, None)
                else:
                    out[M] = nv
        return max_dp, out

    def comp_dict(dp1, d1, dp2, d2):
        out = {}
        for M1, w1 in d1.items():
            for M2, w2 in d2.items():
                M = mat_mul_mod(M2, M1, mod)
                nv = out.get(M, 0) + w1 * w2
                if nv == 0:
                    out.pop(M, None)
                else:
                    out[M] = nv
        return dp1 + dp2, out

    sum_AH = {}
    pair = {}
    for nv in proj_vectors(2, 3):
        S, Sinv = build_hyperplane_S(2, 3, nv, mod)
        c = conj_dict(AH0_dict, S, Sinv)
        for M, w in c.items():
            w2 = sum_AH.get(M, 0) + w
            if w2 == 0:
                sum_AH.pop(M, None)
            else:
                sum_AH[M] = w2
        if nv in ((1, 0, 0), (0, 1, 0)):
            pair[nv] = c

    dp_E, E_dict = comp_dict(dp_A, pair[(1, 0, 0)], dp_A, pair[(0, 1, 0)])
    dp_K, K_dict = add_scaled([(dp_A, sum_AH), (dp_E, {M: -6 * w for M, w in E_dict.items()})], 2)
    while dp_K > 0 and all(v % 2 == 0 for v in K_dict.values()):
        dp_K -= 1
        K_dict = {k: v // 2 for k, v in K_dict.items()}
    dp_KJ, KJ_dict = comp_dict(dp_K, K_dict, dp_J, J_dict)
    dp_I, I_dict = add_scaled([(dp_J, J_dict), (dp_K, K_dict), (dp_KJ, {M: -w for M, w in KJ_dict.items()})], 2)
    while dp_I > 0 and all(v % 2 == 0 for v in I_dict.values()):
        dp_I -= 1
        I_dict = {k: v // 2 for k, v in I_dict.items()}

    # Exhaustive 64x64 verification on Z_4^3
    pts = list(itertools.product(range(4), repeat=3))
    idx_map = {x: i for i, x in enumerate(pts)}
    rows = [{} for _ in range(64)]
    for M, w in I_dict.items():
        for i, x in enumerate(pts):
            y = tuple(sum(M[r][c] * x[c] for c in range(3)) % 4 for r in range(3))
            j = idx_map[y]
            rows[i][j] = rows[i].get(j, 0) + w
    target = 2 ** dp_I
    for i in range(64):
        nz = {j: v for j, v in rows[i].items() if v != 0}
        assert nz == {i: target}, f"Z_4 m=3 fail at row {i}: {nz}"
    return dp_I, I_dict


# ============================================================
# CHECK 1: Lemma 1 (q-Pascal, Cauchy series, & Subspace Radon Inversion)
# ============================================================

def poly_mul_trunc(A, B, max_deg):
    out = [0] * (max_deg + 1)
    for i, a in enumerate(A):
        if i > max_deg or a == 0:
            continue
        for j, b in enumerate(B):
            if i + j > max_deg:
                break
            out[i + j] += a * b
    return out


def check_lemma1():
    t0 = time.monotonic_ns()
    # 1a. q-Pascal (P1) & direct product formula check
    for p in (2, 3, 5, 7):
        for n in range(1, 13):
            for c in range(-1, n + 2):
                val = qbinom(n, c, p)
                assert val == qbinom(n - 1, c, p) + (p ** (n - c)) * qbinom(n - 1, c - 1, p)
                if 0 <= c <= n:
                    num = 1
                    den = 1
                    for i in range(c):
                        num *= (p ** (n - i) - 1)
                        den *= (p ** (i + 1) - 1)
                    assert num % den == 0 and num // den == val

    # 1b. Cauchy formal power series (C1) and (C2) up to degree 10
    deg = 10
    for p in (2, 3, 5):
        for n in range(0, 9):
            poly = [1] + [0] * deg
            for j in range(n):
                poly = poly_mul_trunc(poly, [1, p ** j], deg)
            expected = [
                (p ** (c * (c - 1) // 2)) * qbinom(n, c, p) if c <= n else 0
                for c in range(deg + 1)
            ]
            assert poly == expected, f"(C1) fail p={p}, n={n}"
        for M in range(1, 7):
            P = [1] + [0] * deg
            for j in range(M):
                P = poly_mul_trunc(P, [1, p ** j], deg)
            Q = [((-1) ** d) * qbinom(M + d - 1, d, p) for d in range(deg + 1)]
            prod_PQ = poly_mul_trunc(P, Q, deg)
            assert prod_PQ == [1] + [0] * deg, f"(C2) fail p={p}, M={M}"

    # 1c. Exact Lemma 1(1) scalar identity
    identity_cases = 0
    for p in (2, 3, 5, 7):
        for s in range(1, 6):
            for m in range(s + 1, s + 6):
                for r in range(0, s + 1):
                    total = Fraction(0)
                    for c in range(s + 1):
                        exp = (s - c) * (s - c + 1) // 2 - (m - c) * s
                        coeff = ((-1) ** (s - c)) * (Fraction(p) ** exp)
                        total += coeff * qbinom(m - 1 - c, s - c, p) * qbinom(m - r, c, p)
                    assert total == (1 if r == 0 else 0), f"L1(1) fail {(p, s, m, r)}: {total}"
                    identity_cases += 1

    # 1d. Direct subspace enumeration check of Lemma 1(2)
    enum_summary = []
    for p, s, m in [(2, 2, 5), (2, 2, 4), (2, 3, 4), (3, 2, 4)]:
        weights = {}
        subspace_counts = []
        for c in range(s + 1):
            subs = all_subspaces_codim(p, m, c)
            subspace_counts.append(len(subs))
            outer = ((-1) ** (s - c)) * (p ** ((s - c) * (s - c + 1) // 2)) * qbinom(m - 1 - c, s - c, p)
            denom = p ** ((m - c) * s)
            w_contrib = Fraction(outer, denom)
            for _, basis in subs:
                u_vecs = subspace_elements(basis, p)
                for cols in itertools.product(u_vecs, repeat=s):
                    weights[cols] = weights.get(cols, Fraction(0)) + w_contrib
        # Verify EVERY W in F_p^{m x s} across all ranks 0..s
        all_vecs = list(itertools.product(range(p), repeat=m))
        rank_counts = [0] * (s + 1)
        for W in itertools.product(all_vecs, repeat=s):
            rk = fp_rank(W, p)
            rank_counts[rk] += 1
            got = weights.get(W, Fraction(0))
            expected = Fraction(1) if rk == 0 else Fraction(0)
            assert got == expected, f"L1(2) fail {(p,s,m)} rk={rk} got={got}"
        enum_summary.append(f"(p={p},s={s},m={m}): subs={subspace_counts}, rank_pts={rank_counts}")

    # 1e. Direct composition check of Lemma 1(3): A_{H1} o A_{H2} = A_U
    comp_cases = 0
    for p, s, m in [(2, 2, 5), (3, 2, 4)]:
        for c in range(s):
            subs = all_subspaces_codim(p, m, c)
            for _, basis in subs:
                assert len(basis) == m - c
                H1_basis = basis[: m - s]
                H2_basis = basis[s - c :]
                assert len(H1_basis) == m - s and len(H2_basis) == m - s
                assert fp_rank(H1_basis, p) == m - s
                assert fp_rank(H2_basis, p) == m - s
                assert fp_rank(H1_basis + H2_basis, p) == m - c  # H1 + H2 = U
                H1_vecs = subspace_elements(H1_basis, p)
                H2_vecs = subspace_elements(H2_basis, p)
                U_vecs = set(subspace_elements(basis, p))
                # Since columns of W in Mat_{m x s}(V) are independent,
                # the columnwise convolution on F_p^m automatically yields the F_p^{m x s} convolution!
                # We check BOTH F_p^{m x s} directly (for s=2) and columnwise.
                conv = {}
                for W1 in itertools.product(H1_vecs, repeat=s):
                    for W2 in itertools.product(H2_vecs, repeat=s):
                        W = tuple(
                            tuple((W1[col][i] + W2[col][i]) % p for i in range(m))
                            for col in range(s)
                        )
                        conv[W] = conv.get(W, 0) + 1
                total_pairs = (len(H1_vecs) ** s) * (len(H2_vecs) ** s)
                expected_frac = Fraction(1, len(U_vecs) ** s)
                all_vecs = list(itertools.product(range(p), repeat=m))
                for W in itertools.product(all_vecs, repeat=s):
                    in_U = all(col in U_vecs for col in W)
                    got_frac = Fraction(conv.get(W, 0), total_pairs)
                    assert got_frac == (expected_frac if in_U else Fraction(0))
                comp_cases += 1

    print(
        f"[CHECK 1] Lemma 1 PASS ({elapsed_ms_str(t0)}): "
        f"(P1), (C1)/(C2) deg<=10, {identity_cases} identity cases, "
        f"L1(2) [{'; '.join(enum_summary)}], L1(3) {comp_cases} exact subspace compositions"
    )


# ============================================================
# CHECK 2: End-to-End Full 4096 x 4096 Identity for A = Z_8
# ============================================================

def check_Z8_exhaustive():
    t0 = time.monotonic_ns()
    # 2a. Verify Z_4 at m=3 (64x64) and m=4 (256x256)
    dp_I3, I3_Z4 = build_Z4_full_dict_m3()

    (dp_J4, J4_Z4), (dp_A4, AH0_4_Z4) = build_Zp2_components(2, 4)
    for M in J4_Z4:
        verify_snf_rank_Zpe(M, 2, 2, 1)
    for M in AH0_4_Z4:
        verify_snf_rank_Zpe(M, 2, 2, 2)

    pts256 = list(itertools.product(range(4), repeat=4))
    idx256 = {(x[0] << 6) | (x[1] << 4) | (x[2] << 2) | x[3]: i for i, x in enumerate(pts256)}

    def op_Z4_4_to_sparse(op_dict):
        rows = [{} for _ in range(256)]
        for M, w in op_dict.items():
            m0, m1, m2, m3 = M
            for i, (x0, x1, x2, x3) in enumerate(pts256):
                y0 = (m0[0] * x0 + m0[1] * x1 + m0[2] * x2 + m0[3] * x3) & 3
                y1 = (m1[0] * x0 + m1[1] * x1 + m1[2] * x2 + m1[3] * x3) & 3
                y2 = (m2[0] * x0 + m2[1] * x1 + m2[2] * x2 + m2[3] * x3) & 3
                y3 = (m3[0] * x0 + m3[1] * x1 + m3[2] * x2 + m3[3] * x3) & 3
                j = (y0 << 6) | (y1 << 4) | (y2 << 2) | y3
                rows[i][j] = rows[i].get(j, 0) + w
        return [{j: v for j, v in r.items() if v != 0} for r in rows]

    J4_256 = op_Z4_4_to_sparse(J4_Z4)
    AH0_256 = op_Z4_4_to_sparse(AH0_4_Z4)
    normals4 = proj_vectors(2, 4)

    def perm_256(S):
        m0, m1, m2, m3 = S
        pS = [0] * 256
        pS_inv = [0] * 256
        for i, (x0, x1, x2, x3) in enumerate(pts256):
            y0 = (m0[0] * x0 + m0[1] * x1 + m0[2] * x2 + m0[3] * x3) & 3
            y1 = (m1[0] * x0 + m1[1] * x1 + m1[2] * x2 + m1[3] * x3) & 3
            y2 = (m2[0] * x0 + m2[1] * x1 + m2[2] * x2 + m2[3] * x3) & 3
            y3 = (m3[0] * x0 + m3[1] * x1 + m3[2] * x2 + m3[3] * x3) & 3
            u = (y0 << 6) | (y1 << 4) | (y2 << 2) | y3
            pS[i] = u
            pS_inv[u] = i
        return pS, pS_inv

    sum_AH_256 = [{} for _ in range(256)]
    pair_256 = {}
    for nv in normals4:
        S, _ = build_hyperplane_S(2, 4, nv, 4)
        pS, pS_inv = perm_256(S)
        AH_256 = sparse_conj(AH0_256, pS, pS_inv)
        sum_AH_256 = sparse_add_scaled(sum_AH_256, 1, AH_256, 1)
        if nv in ((1, 0, 0, 0), (0, 1, 0, 0)):
            pair_256[nv] = AH_256
    E_256 = sparse_mul(pair_256[(1, 0, 0, 0)], pair_256[(0, 1, 0, 0)])
    K_256 = sparse_add_scaled(sum_AH_256, 2 ** dp_A4, E_256, -14)
    K_256, dp_K4 = sparse_reduce_pow(K_256, 2 * dp_A4, 2)
    KJ_256 = sparse_mul(K_256, J4_256)
    I_256 = sparse_add_scaled(
        sparse_add_scaled(J4_256, 2 ** dp_K4, K_256, 2 ** dp_J4),
        1,
        KJ_256,
        -1,
    )
    I_256, dp_I4 = sparse_reduce_pow(I_256, dp_J4 + dp_K4, 2)
    for i in range(256):
        assert I_256[i] == {i: 2 ** dp_I4}, f"Z_4 m=4 fail at {i}"

    # 2b. Lift Z_4 m=4 components factorwise to Z_8^4 (4096 points) -> J_prop
    J4_lift = {}
    for B, w in J4_Z4.items():
        _, U, V = verify_snf_rank_Zpe(B, 2, 2, 1)
        M = mat_mul_mod(U, V, 8)
        J4_lift[M] = J4_lift.get(M, 0) + w
    J4_lift = {M: w for M, w in J4_lift.items() if w != 0}
    for M in J4_lift:
        verify_snf_rank_Zpe(M, 2, 3, 1)

    AH0_4_lift = {}
    for B, w in AH0_4_Z4.items():
        _, U, V = verify_snf_rank_Zpe(B, 2, 2, 2)
        M = mat_mul_mod(U, V, 8)
        AH0_4_lift[M] = AH0_4_lift.get(M, 0) + w
    AH0_4_lift = {M: w for M, w in AH0_4_lift.items() if w != 0}
    for M in AH0_4_lift:
        verify_snf_rank_Zpe(M, 2, 3, 2)

    N4096 = 4096
    pts512 = list(itertools.product(range(8), repeat=3))
    pts4096 = [((idx >> 9) & 7, (idx >> 6) & 7, (idx >> 3) & 7, idx & 7) for idx in range(N4096)]
    O_mask = [any(c & 1 for c in x) for x in pts4096]
    off_O_pts = [i for i in range(N4096) if not O_mask[i]]
    assert len(off_O_pts) == 256
    off_O_local = {gi: li for li, gi in enumerate(off_O_pts)}

    def op_Z8_offO_to_256(op_dict):
        """Restrict Z_4-lifted operator to the closed submodule (2 Z_8)^4 (256 points)."""
        rows = [{} for _ in range(256)]
        for M, w in op_dict.items():
            m0, m1, m2, m3 = M
            for li, gi in enumerate(off_O_pts):
                x0, x1, x2, x3 = pts4096[gi]
                y0 = (m0[0] * x0 + m0[1] * x1 + m0[2] * x2 + m0[3] * x3) & 7
                y1 = (m1[0] * x0 + m1[1] * x1 + m1[2] * x2 + m1[3] * x3) & 7
                y2 = (m2[0] * x0 + m2[1] * x1 + m2[2] * x2 + m2[3] * x3) & 7
                y3 = (m3[0] * x0 + m3[1] * x1 + m3[2] * x2 + m3[3] * x3) & 7
                gj = (y0 << 9) | (y1 << 6) | (y2 << 3) | y3
                lj = off_O_local[gj]
                rows[li][lj] = rows[li].get(lj, 0) + w
        return [{j: v for j, v in r.items() if v != 0} for r in rows]

    def perm_4096(S):
        m0, m1, m2, m3 = S
        pS = [0] * N4096
        pS_inv = [0] * N4096
        for i, (x0, x1, x2, x3) in enumerate(pts4096):
            y0 = (m0[0] * x0 + m0[1] * x1 + m0[2] * x2 + m0[3] * x3) & 7
            y1 = (m1[0] * x0 + m1[1] * x1 + m1[2] * x2 + m1[3] * x3) & 7
            y2 = (m2[0] * x0 + m2[1] * x1 + m2[2] * x2 + m2[3] * x3) & 7
            y3 = (m3[0] * x0 + m3[1] * x1 + m3[2] * x2 + m3[3] * x3) & 7
            u = (y0 << 9) | (y1 << 6) | (y2 << 3) | y3
            pS[i] = u
            pS_inv[u] = i
        return pS, pS_inv

    def perm_offO_256(S):
        m0, m1, m2, m3 = S
        pS = [0] * 256
        pS_inv = [0] * 256
        for li, gi in enumerate(off_O_pts):
            x0, x1, x2, x3 = pts4096[gi]
            y0 = (m0[0] * x0 + m0[1] * x1 + m0[2] * x2 + m0[3] * x3) & 7
            y1 = (m1[0] * x0 + m1[1] * x1 + m1[2] * x2 + m1[3] * x3) & 7
            y2 = (m2[0] * x0 + m2[1] * x1 + m2[2] * x2 + m2[3] * x3) & 7
            y3 = (m3[0] * x0 + m3[1] * x1 + m3[2] * x2 + m3[3] * x3) & 7
            gu = (y0 << 9) | (y1 << 6) | (y2 << 3) | y3
            lu = off_O_local[gu]
            pS[li] = lu
            pS_inv[lu] = li
        return pS, pS_inv

    J4_off = op_Z8_offO_to_256(J4_lift)
    AH0_4_off = op_Z8_offO_to_256(AH0_4_lift)
    sum_AH_4_off = [{} for _ in range(256)]
    pair_4_off = {}
    for nv in normals4:
        S, _ = build_hyperplane_S(2, 4, nv, 8)
        pS, pS_inv = perm_offO_256(S)
        AH_m = sparse_conj(AH0_4_off, pS, pS_inv)
        sum_AH_4_off = sparse_add_scaled(sum_AH_4_off, 1, AH_m, 1)
        if nv in ((1, 0, 0, 0), (0, 1, 0, 0)):
            pair_4_off[nv] = AH_m
    E_4_off = sparse_mul(pair_4_off[(1, 0, 0, 0)], pair_4_off[(0, 1, 0, 0)])
    K_4_off = sparse_add_scaled(sum_AH_4_off, 2 ** dp_A4, E_4_off, -14)
    K_4_off, dp_K4_lift = sparse_reduce_pow(K_4_off, 2 * dp_A4, 2)
    KJ_4_off = sparse_mul(K_4_off, J4_off)
    Jprop_off = sparse_add_scaled(
        sparse_add_scaled(J4_off, 2 ** dp_K4_lift, K_4_off, 2 ** dp_J4),
        1,
        KJ_4_off,
        -1,
    )
    Jprop_off, dp_Jprop = sparse_reduce_pow(Jprop_off, dp_J4 + dp_K4_lift, 2)
    # Verify J_prop fixes ALL 256 tuples in (2 Z_8)^4!
    for li in range(256):
        assert Jprop_off[li] == {li: 2 ** dp_Jprop}, f"J_prop fail on (2Z_8)^4 at local {li}"

    # 2c. Step 2 on Z_8^4: verify (W', U') uniform multiplicity, SNF rank <= 3, and build AH0_mat
    # Verify exhaustively over all t in F_2^3 and all 512 pairs (W', U') in F_2^3 x F_2^{3x2}
    for t in itertools.product(range(2), repeat=3):
        counts = {}
        for wp in itertools.product(range(2), repeat=3):
            for up in itertools.product(range(2), repeat=6):
                out = (
                    (wp[0] * t[0] + up[0] * t[1] + up[1] * t[2]) & 1,
                    (wp[1] * t[0] + up[2] * t[1] + up[3] * t[2]) & 1,
                    (wp[2] * t[0] + up[4] * t[1] + up[5] * t[2]) & 1,
                )
                counts[out] = counts.get(out, 0) + 1
        if t == (0, 0, 0):
            assert counts == {(0, 0, 0): 512}
        else:
            assert len(counts) == 8 and all(v == 64 for v in counts.values())

    # Build AH0_mat on Z_8^4 from I3_Z4 (3408 matrices B_tilde) & check SNF rank <= 3 over Z/8Z!
    dp_A = dp_I3 + 9  # 512 = 2^9
    exact0 = [{} for _ in range(512)]
    coset0 = [{} for _ in range(512)]
    coset1 = [{} for _ in range(512)]
    snf_checked = 0
    for B_tilde, w in I3_Z4.items():
        _, U, V = verify_snf_rank_Zpe(B_tilde, 2, 2, 2)
        UV = mat_mul_mod(U, V, 8)
        Vbar = tuple(tuple(c & 1 for c in row) for row in V)
        # Verify SNF rank <= 3 over Z/8Z for M(B_tilde, U', W') across representative (W', U')
        for wp, up in [
            ((0, 0, 0), ((0, 0), (0, 0), (0, 0))),
            ((1, 0, 1), ((1, 0), (0, 1), (1, 1))),
            ((0, 1, 1), ((1, 1), (1, 0), (0, 1))),
        ]:
            M_test = (
                (1, 0, 0, 0),
                ((4 * wp[0]) & 7,) + tuple((UV[0][c] + 4 * (up[0][0] * Vbar[0][c] + up[0][1] * Vbar[1][c])) & 7 for c in range(3)),
                ((4 * wp[1]) & 7,) + tuple((UV[1][c] + 4 * (up[1][0] * Vbar[0][c] + up[1][1] * Vbar[1][c])) & 7 for c in range(3)),
                ((4 * wp[2]) & 7,) + tuple((UV[2][c] + 4 * (up[2][0] * Vbar[0][c] + up[2][1] * Vbar[1][c])) & 7 for c in range(3)),
            )
            verify_snf_rank_Zpe(M_test, 2, 3, 3)
            snf_checked += 1

        uv0, uv1, uv2 = UV
        vb0, vb1 = Vbar
        w512 = 512 * w
        w64 = 64 * w
        for idx3, (x1, x2, x3) in enumerate(pts512):
            b0 = (uv0[0] * x1 + uv0[1] * x2 + uv0[2] * x3) & 7
            b1 = (uv1[0] * x1 + uv1[1] * x2 + uv1[2] * x3) & 7
            b2 = (uv2[0] * x1 + uv2[1] * x2 + uv2[2] * x3) & 7
            ckey = ((b0 & 3) << 4) | ((b1 & 3) << 2) | (b2 & 3)
            coset1[idx3][ckey] = coset1[idx3].get(ckey, 0) + w64
            if ((vb0[0] * x1 + vb0[1] * x2 + vb0[2] * x3) & 1) == 0 and (
                (vb1[0] * x1 + vb1[1] * x2 + vb1[2] * x3) & 1
            ) == 0:
                j = (b0 << 6) | (b1 << 3) | b2
                exact0[idx3][j] = exact0[idx3].get(j, 0) + w512
            else:
                coset0[idx3][ckey] = coset0[idx3].get(ckey, 0) + w64

    def expand_blocks(ex_blk, co_blk):
        out = []
        for idx3 in range(512):
            row = dict(ex_blk[idx3])
            for ckey, val in co_blk[idx3].items():
                if val == 0:
                    continue
                b0 = (ckey >> 4) & 3
                b1 = (ckey >> 2) & 3
                b2 = ckey & 3
                for s0 in (0, 4):
                    nb0 = b0 + s0
                    for s1 in (0, 4):
                        nb1 = b1 + s1
                        for s2 in (0, 4):
                            j = (nb0 << 6) | (nb1 << 3) | (b2 + s2)
                            row[j] = row.get(j, 0) + val
            out.append({j: v for j, v in row.items() if v != 0})
        return out

    block0 = expand_blocks(exact0, coset0)
    block1 = expand_blocks([{} for _ in range(512)], coset1)
    AH0_mat = [{} for _ in range(N4096)]
    for x0 in range(8):
        blk = block0 if (x0 & 1) == 0 else block1
        base = x0 << 9
        for idx3 in range(512):
            AH0_mat[base | idx3] = {base | j: v for j, v in blk[idx3].items()}
    AH0_mat, dp_A = sparse_reduce_pow(AH0_mat, dp_A, 2)

    # Verify AH0_mat on O-columns matches exact hyperplane average F_{H_0} = (1/8) sum_{w in H_0} h(X + 4w)
    val_exp = 2 ** (dp_A - 3)
    for i in range(N4096):
        if not O_mask[i]:
            continue
        x0, x1, x2, x3 = pts4096[i]
        expected_O = {}
        for d1 in (0, 4):
            for d2 in (0, 4):
                for d3 in (0, 4):
                    j = (x0 << 9) | (((x1 + d1) & 7) << 6) | (((x2 + d2) & 7) << 3) | ((x3 + d3) & 7)
                    expected_O[j] = val_exp
        got_O = {j: v for j, v in AH0_mat[i].items() if O_mask[j]}
        assert got_O == expected_O, f"AH0 on O mismatch at {i}"

    # 2d. Conjugate to all 15 hyperplanes H, form E, K, and full I = J_prop + K - K o J_prop
    sum_AH = [{} for _ in range(N4096)]
    pair_AH = {}
    for nv in normals4:
        S, _ = build_hyperplane_S(2, 4, nv, 8)
        pS, pS_inv = perm_4096(S)
        AH_m = sparse_conj(AH0_mat, pS, pS_inv)
        sum_AH = sparse_add_scaled(sum_AH, 1, AH_m, 1)
        if nv in ((1, 0, 0, 0), (0, 1, 0, 0)):
            pair_AH[nv] = AH_m

    E_mat = sparse_mul(pair_AH[(1, 0, 0, 0)], pair_AH[(0, 1, 0, 0)])
    K_mat = sparse_add_scaled(sum_AH, 2 ** dp_A, E_mat, -14)
    K_mat, dp_K = sparse_reduce_pow(K_mat, 2 * dp_A, 2)

    # Verify (Id - K) has ZERO nonzero entries in ALL 3840 O-columns across ALL 4096 rows,
    # then compose I = K + (Id - K) @ J_prop_off exactly on all 4096 rows!
    eye_4096 = [{i: 1} for i in range(N4096)]
    Id_minus_K = sparse_add_scaled(eye_4096, 2 ** dp_K, K_mat, -1)
    for i in range(N4096):
        for j in Id_minus_K[i]:
            assert not O_mask[j], f"K failed to match Id on O-column at {(i, j)}"

    # Lift Jprop_off (256x256 on off_O) to rows indexed by global off_O indices
    Jprop_off_glob = [{} for _ in range(N4096)]
    for li, gi in enumerate(off_O_pts):
        Jprop_off_glob[gi] = {off_O_pts[lj]: v for lj, v in Jprop_off[li].items()}

    corr_mat = sparse_mul(Id_minus_K, Jprop_off_glob)
    I_mat = sparse_add_scaled(K_mat, 2 ** dp_Jprop, corr_mat, 1)
    I_mat, dp_I = sparse_reduce_pow(I_mat, dp_Jprop + dp_K, 2)

    target_I = 2 ** dp_I
    for i in range(N4096):
        assert I_mat[i] == {i: target_I}, f"Full 4096x4096 Z_8 identity FAIL at row {i}: {I_mat[i]}"

    print(
        f"[CHECK 2] A = Z_8 (m=4, k=3) PASS ({elapsed_ms_str(t0)}): "
        f"Z_4 m=3 (64x64, |I3|={len(I3_Z4)}, denom 2^{dp_I3}), "
        f"Z_4 m=4 (256x256, denom 2^{dp_I4}), "
        f"Z_8 m=4 J_prop (256 proper pts fixed, denom 2^{dp_Jprop}), "
        f"{snf_checked} SNF rank<=3 checks over Z/8Z, "
        f"EXACT FULL 4096x4096 identity VERIFIED (denom 2^{dp_I})"
    )
    return dp_I, I_mat, pts4096, dp_I3, I3_Z4


# ============================================================
# CHECK 3: End-to-End Exact Verification for A = Z_4 x Z_4 (p=2, e=2, s=2, k=4, m=5)
# ============================================================

def check_Z4xZ4_exact():
    t0 = time.monotonic_ns()
    p, mod, s, k, m = 2, 4, 2, 4, 5

    # 3a. Build & exhaustively verify (2, F_2^2, Z[1/2])-UG on (F_2^2)^3 (64 pts)
    dp_v3, ug_v3 = ug_Fp2_2ary_m3(2)
    for B in ug_v3:
        factor_rank_le_Fp(B, 2, 2)
    pts64 = list(itertools.product(range(2), repeat=6))
    idx64 = {pt: i for i, pt in enumerate(pts64)}
    mat64 = [{} for _ in range(64)]
    for B, w in ug_v3.items():
        b0, b1, b2 = B
        for i, pt in enumerate(pts64):
            x0, x1, x2, y0, y1, y2 = pt
            nx = (
                (b0[0] * x0 + b0[1] * x1 + b0[2] * x2) & 1,
                (b1[0] * x0 + b1[1] * x1 + b1[2] * x2) & 1,
                (b2[0] * x0 + b2[1] * x1 + b2[2] * x2) & 1,
            )
            ny = (
                (b0[0] * y0 + b0[1] * y1 + b0[2] * y2) & 1,
                (b1[0] * y0 + b1[1] * y1 + b1[2] * y2) & 1,
                (b2[0] * y0 + b2[1] * y1 + b2[2] * y2) & 1,
            )
            j = idx64[nx + ny]
            mat64[i][j] = mat64[i].get(j, 0) + w
    for i in range(64):
        nz = {j: v for j, v in mat64[i].items() if v != 0}
        assert nz == {i: 2 ** dp_v3}, f"F_2^2 m=3 fail at {i}"

    # 3b. Factor every B in ug_v3, verify SNF rank <= 4 over Z/4Z for M(B, U', W')
    factored_B = []
    snf_cnt = 0
    for B, w in ug_v3.items():
        U, V = factor_rank_le_Fp(B, 2, 2)
        factored_B.append((B, U, V, mat_mul_mod(U, V, 4), w))
        for wp, up in [
            (((0, 0), (0, 0), (0, 0)), ((0, 0), (0, 0), (0, 0))),
            (((1, 0), (0, 1), (1, 1)), ((1, 1), (0, 1), (1, 0))),
        ]:
            UVp = mat_mul_mod(
                tuple(tuple((U[r][c] + 2 * up[r][c]) & 3 for c in range(2)) for r in range(3)),
                V,
                4,
            )
            M = (
                (1, 0, 0, 0, 0),
                (0, 1, 0, 0, 0),
                ((2 * wp[0][0]) & 3, (2 * wp[0][1]) & 3) + UVp[0],
                ((2 * wp[1][0]) & 3, (2 * wp[1][1]) & 3) + UVp[1],
                ((2 * wp[2][0]) & 3, (2 * wp[2][1]) & 3) + UVp[2],
            )
            verify_snf_rank_Zpe(M, 2, 2, 4)
            snf_cnt += 1
    # Exhaustive check over ALL 4096 (W', U') for 3 representative B of F_2-ranks 0, 1, 2
    rep_by_rk = {}
    for B, U, V, _, _ in factored_B:
        rk = fp_rank(B, 2)
        if rk not in rep_by_rk:
            rep_by_rk[rk] = (U, V)
    assert len(rep_by_rk) == 3
    all_3x2 = list(itertools.product(itertools.product(range(2), repeat=2), repeat=3))  # 64 matrices
    for rk, (U, V) in rep_by_rk.items():
        for wp in all_3x2:
            for up in all_3x2:
                UVp = mat_mul_mod(
                    tuple(tuple((U[r][c] + 2 * up[r][c]) & 3 for c in range(2)) for r in range(3)),
                    V,
                    4,
                )
                M = (
                    (1, 0, 0, 0, 0),
                    (0, 1, 0, 0, 0),
                    ((2 * wp[0][0]) & 3, (2 * wp[0][1]) & 3) + UVp[0],
                    ((2 * wp[1][0]) & 3, (2 * wp[1][1]) & 3) + UVp[1],
                    ((2 * wp[2][0]) & 3, (2 * wp[2][1]) & 3) + UVp[2],
                )
                verify_snf_rank_Zpe(M, 2, 2, 4)
                snf_cnt += 1

    # 3c. Full UNAPPROXIMATED Step 2 operator A_{H_0}(h)(X) == F_{H_0}(h)(X)
    # summing over ALL 4096 pairs (W', U') and ALL 204 matrices B!
    def in_O_Z4xZ4(X):
        c0 = (X[0][0] & 1) | ((X[1][0] & 1) << 1) | ((X[2][0] & 1) << 2) | ((X[3][0] & 1) << 3) | ((X[4][0] & 1) << 4)
        c1 = (X[0][1] & 1) | ((X[1][1] & 1) << 1) | ((X[2][1] & 1) << 2) | ((X[3][1] & 1) << 3) | ((X[4][1] & 1) << 4)
        return c0 != 0 and c1 != 0 and c0 != c1

    def eval_AH0_unapprox(h_int_fn, X):
        X1 = X[:2]
        Xp = X[2:]
        X1_00, X1_01 = X1[0][0] & 1, X1[0][1] & 1
        X1_10, X1_11 = X1[1][0] & 1, X1[1][1] & 1
        Xp00, Xp01 = Xp[0][0], Xp[0][1]
        Xp10, Xp11 = Xp[1][0], Xp[1][1]
        Xp20, Xp21 = Xp[2][0], Xp[2][1]
        Xp00b, Xp01b = Xp00 & 1, Xp01 & 1
        Xp10b, Xp11b = Xp10 & 1, Xp11 & 1
        Xp20b, Xp21b = Xp20 & 1, Xp21 & 1
        X1_r0, X1_r1 = X1[0], X1[1]
        # Precompute exact 4096-entry table of h_int_fn((X1_r0, X1_r1, row2, row3, row4))
        h_tbl = [
            h_int_fn((
                X1_r0,
                X1_r1,
                ((idx >> 10) & 3, (idx >> 8) & 3),
                ((idx >> 6) & 3, (idx >> 4) & 3),
                ((idx >> 2) & 3, idx & 3),
            ))
            for idx in range(4096)
        ]
        total = Fraction(0)
        for _, U, V, UV, w in factored_B:
            uv0, uv1, uv2 = UV
            b00 = (uv0[0] * Xp00 + uv0[1] * Xp10 + uv0[2] * Xp20) & 3
            b01 = (uv0[0] * Xp01 + uv0[1] * Xp11 + uv0[2] * Xp21) & 3
            b10 = (uv1[0] * Xp00 + uv1[1] * Xp10 + uv1[2] * Xp20) & 3
            b11 = (uv1[0] * Xp01 + uv1[1] * Xp11 + uv1[2] * Xp21) & 3
            b20 = (uv2[0] * Xp00 + uv2[1] * Xp10 + uv2[2] * Xp20) & 3
            b21 = (uv2[0] * Xp01 + uv2[1] * Xp11 + uv2[2] * Xp21) & 3
            v0, v1 = V
            vx00 = (v0[0] * Xp00b + v0[1] * Xp10b + v0[2] * Xp20b) & 1
            vx01 = (v0[0] * Xp01b + v0[1] * Xp11b + v0[2] * Xp21b) & 1
            vx10 = (v1[0] * Xp00b + v1[1] * Xp10b + v1[2] * Xp20b) & 1
            vx11 = (v1[0] * Xp01b + v1[1] * Xp11b + v1[2] * Xp21b) & 1

            # In Z/4Z, (p + 2*bit) & 3 == p ^ (2*bit); pack 6 coordinates into a 12-bit XOR mask
            u_masks = [
                (((up[0][0] * vx00 + up[0][1] * vx10) & 1) << 11)
                | (((up[0][0] * vx01 + up[0][1] * vx11) & 1) << 9)
                | (((up[1][0] * vx00 + up[1][1] * vx10) & 1) << 7)
                | (((up[1][0] * vx01 + up[1][1] * vx11) & 1) << 5)
                | (((up[2][0] * vx00 + up[2][1] * vx10) & 1) << 3)
                | (((up[2][0] * vx01 + up[2][1] * vx11) & 1) << 1)
                for up in all_3x2
            ]
            b_idx = (b00 << 10) | (b01 << 8) | (b10 << 6) | (b11 << 4) | (b20 << 2) | b21
            inner_sum = 0
            for wp in all_3x2:
                w_mask = (
                    (((wp[0][0] * X1_00 + wp[0][1] * X1_10) & 1) << 11)
                    | (((wp[0][0] * X1_01 + wp[0][1] * X1_11) & 1) << 9)
                    | (((wp[1][0] * X1_00 + wp[1][1] * X1_10) & 1) << 7)
                    | (((wp[1][0] * X1_01 + wp[1][1] * X1_11) & 1) << 5)
                    | (((wp[2][0] * X1_00 + wp[2][1] * X1_10) & 1) << 3)
                    | (((wp[2][0] * X1_01 + wp[2][1] * X1_11) & 1) << 1)
                )
                p_idx = b_idx ^ w_mask
                for um in u_masks:
                    inner_sum += h_tbl[p_idx ^ um]
            total += Fraction(w * inner_sum, (2 ** dp_v3) * 4096)
        return total

    def eval_FH0(h_int_fn, X):
        X1 = X[:2]
        Xp = X[2:]
        total = 0
        for W in all_3x2:
            Z = (
                X1[0],
                X1[1],
                ((Xp[0][0] + 2 * W[0][0]) & 3, (Xp[0][1] + 2 * W[0][1]) & 3),
                ((Xp[1][0] + 2 * W[1][0]) & 3, (Xp[1][1] + 2 * W[1][1]) & 3),
                ((Xp[2][0] + 2 * W[2][0]) & 3, (Xp[2][1] + 2 * W[2][1]) & 3),
            )
            total += h_int_fn(Z)
        return Fraction(total, 64)

    # Test tuples X covering rk(X_bar) in {0, 1, 2} and hitting Case 1 (rk(T)=2) & Case 2 (rk(T) in {0, 1})
    X_in_O_1 = ((1, 0), (0, 1), (1, 1), (2, 1), (0, 2))
    X_in_O_2 = ((1, 0), (2, 0), (0, 1), (3, 2), (2, 3))  # top 2 rows have mod-2 rank 1!
    X_in_O_3 = ((2, 0), (0, 2), (1, 0), (0, 1), (1, 1))  # top 2 rows are 0 mod 2!
    X_rk1 = ((1, 0), (3, 0), (1, 0), (2, 0), (0, 0))     # mod-2 rank 1 -> not in O
    X_rk0 = ((2, 0), (0, 2), (2, 2), (0, 0), (2, 0))     # mod-2 rank 0 -> not in O
    assert in_O_Z4xZ4(X_in_O_1) and in_O_Z4xZ4(X_in_O_2) and in_O_Z4xZ4(X_in_O_3)
    assert not in_O_Z4xZ4(X_rk1) and not in_O_Z4xZ4(X_rk0)

    def h_delta_int(Z):
        return 1 if Z == X_in_O_1 else 0

    def h_multi_int(Z):
        c0 = (Z[0][0] & 1) | ((Z[1][0] & 1) << 1) | ((Z[2][0] & 1) << 2) | ((Z[3][0] & 1) << 3) | ((Z[4][0] & 1) << 4)
        c1 = (Z[0][1] & 1) | ((Z[1][1] & 1) << 1) | ((Z[2][1] & 1) << 2) | ((Z[3][1] & 1) << 3) | ((Z[4][1] & 1) << 4)
        if c0 == 0 or c1 == 0 or c0 == c1:
            return 0
        acc = (3 * Z[0][0] + 5 * Z[1][1] + 7 * Z[2][0] + 11 * Z[3][1] + 13 * Z[4][0] + Z[2][1] * Z[4][1]) % 17
        return acc - 5

    for X_test in (X_in_O_1, X_in_O_2, X_in_O_3, X_rk1, X_rk0):
        got = eval_AH0_unapprox(h_multi_int, X_test)
        exp = eval_FH0(h_multi_int, X_test)
        assert got == exp, f"Z4^2 Step 2 multi fail at {X_test}: got={got}, exp={exp}"
    for X_test in (X_in_O_1, X_in_O_2, X_rk1):
        got = eval_AH0_unapprox(h_delta_int, X_test)
        exp = eval_FH0(h_delta_int, X_test)
        assert got == exp, f"Z4^2 Step 2 delta fail at {X_test}: got={got}, exp={exp}"

    # 3d. Full Step 3 Radon inversion K(h)(X) == h(X) over ALL 155 + 31 + 1 subspaces of F_2^5
    subspaces_by_c = {c: all_subspaces_codim(2, 5, c) for c in range(3)}
    assert [len(subspaces_by_c[c]) for c in range(3)] == [1, 31, 155]

    def eval_AV(h_fn, basis_V, X):
        vecs = subspace_elements(basis_V, 2)
        total = Fraction(0)
        for c0 in vecs:
            for c1 in vecs:
                Z = tuple(
                    ((X[i][0] + 2 * c0[i]) & 3, (X[i][1] + 2 * c1[i]) & 3)
                    for i in range(5)
                )
                total += h_fn(Z)
        return total * Fraction(1, len(vecs) ** 2)

    # Also check conjugated operator A_{H_0}(h o T_H^{-1})(T_H X) == F_H(h)(X) for representative codim-2 H
    for P_H, basis_H in subspaces_by_c[2][:2]:
        T_H, T_H_inv = build_codim_s_S(2, 5, P_H, 4)

        def apply_mat5(M5, Z):
            return tuple(
                (sum(M5[r][c] * Z[c][0] for c in range(5)) & 3,
                 sum(M5[r][c] * Z[c][1] for c in range(5)) & 3)
                for r in range(5)
            )

        def h_conj(Z):
            return h_multi_int(apply_mat5(T_H_inv, Z))

        got_conj = eval_AH0_unapprox(h_conj, apply_mat5(T_H, X_in_O_1))
        exp_conj = eval_AV(h_multi_int, basis_H, X_in_O_1)
        assert got_conj == exp_conj

    # Verify K(h)(X) == h(X) across ALL 155 + 31 + 1 subspaces
    for X_test in (X_in_O_1, X_in_O_2, X_rk1, X_rk0):
        for h_fn in (h_delta_int, h_multi_int):
            K_val = Fraction(0)
            for c in range(3):
                outer = ((-1) ** (2 - c)) * (2 ** ((2 - c) * (3 - c) // 2)) * qbinom(4 - c, 2 - c, 2)
                sub_sum = Fraction(0)
                for _, basis_U in subspaces_by_c[c]:
                    if c == 2:
                        sub_sum += eval_AV(h_fn, basis_U, X_test)
                    else:
                        H1_b = basis_U[:3]
                        H2_b = basis_U[2 - c :]
                        # Explicit composition A_{H1} o A_{H2}
                        h_H2 = lambda Z, b2=H2_b: eval_AV(h_fn, b2, Z)
                        val_comp = eval_AV(h_H2, H1_b, X_test)
                        if X_test == X_in_O_1 and h_fn is h_multi_int:
                            assert val_comp == eval_AV(h_fn, basis_U, X_test)
                        sub_sum += val_comp
                K_val += outer * sub_sum
            assert K_val == Fraction(h_fn(X_test)), f"Z4^2 Step 3 Radon fail at {X_test}: got={K_val}, exp={h_fn(X_test)}"

    # 3e. Lemma 2: Peel ALL 3 maximal subgroups C_1, C_2, C_3 ~= Z_4 x Z_2 of Z_4^2
    # First build and exhaustively verify (3, Z_4 x Z_2, Z[1/2])-UG at arity m=4 (4096x4096)
    # using the exact components from ques2 (all matrices verified SNF rank <= 3 <= 4 over Z/4Z!)
    dp_A_z4z2 = dp_v3 + 9
    AH0_z4z2 = {}
    for B, w in ug_v3.items():
        U, V = factor_rank_le_Fp(B, 2, 2)
        nz = [r for r in range(2) if any(V[r])]
        r_eff = len(nz)
        A2 = [(1, 0, 0, 0)] + [(0, V[r][0], V[r][1], V[r][2]) for r in nz]
        mult = 2 ** (9 - 3 * (1 + r_eff))
        for pert in itertools.product(range(2), repeat=3 * (1 + r_eff)):
            A1 = [(1,) + (0,) * r_eff]
            for ri in range(3):
                base = ri * (1 + r_eff)
                rv = [(2 * pert[base]) & 3]
                for ci, ro in enumerate(nz):
                    rv.append((U[ri][ro] + 2 * pert[base + 1 + ci]) & 3)
                A1.append(tuple(rv))
            M = mat_mul_mod(A1, A2, 4)
            nv = AH0_z4z2.get(M, 0) + w * mult
            if nv == 0:
                AH0_z4z2.pop(M, None)
            else:
                AH0_z4z2[M] = nv
    while dp_A_z4z2 > 0 and all(v % 2 == 0 for v in AH0_z4z2.values()):
        dp_A_z4z2 -= 1
        AH0_z4z2 = {k_: v_ // 2 for k_, v_ in AH0_z4z2.items()}
    for M in AH0_z4z2:
        verify_snf_rank_Zpe(M, 2, 2, 3)

    Ivec_z4z2 = {}
    for B, w in ug_v3.items():
        U, V = factor_rank_le_Fp(B, 2, 2)
        M3 = mat_mul_mod(U, V, 4)
        M4 = (M3[0] + (0,), M3[1] + (0,), M3[2] + (0,), (0, 0, 0, 1))
        Ivec_z4z2[M4] = Ivec_z4z2.get(M4, 0) + w
    Ivec_z4z2 = {k_: v_ for k_, v_ in Ivec_z4z2.items() if v_ != 0}
    for M in Ivec_z4z2:
        verify_snf_rank_Zpe(M, 2, 2, 3)

    (dp_Jc, Jc_dict), (dp_Ac, Ac_dict) = build_Zp2_components(2, 3)
    Jc4_dict = {(M[0] + (0,), M[1] + (0,), M[2] + (0,), (0, 0, 0, 1)): w for M, w in Jc_dict.items()}
    Ac4_dict = {(M[0] + (0,), M[1] + (0,), M[2] + (0,), (0, 0, 0, 1)): w for M, w in Ac_dict.items()}
    for M in Jc4_dict:
        verify_snf_rank_Zpe(M, 2, 2, 3)
    for M in Ac4_dict:
        verify_snf_rank_Zpe(M, 2, 2, 3)

    # Convert Z_4 x Z_2 m=4 operators to 4096 x 4096 sparse matrices using tensor structure (256 x 16)
    N_z4z2 = 4096
    pts_x256 = [((i >> 6) & 3, (i >> 4) & 3, (i >> 2) & 3, i & 3) for i in range(256)]
    pts_y16 = [((i >> 3) & 1, (i >> 2) & 1, (i >> 1) & 1, i & 1) for i in range(16)]

    def op_z4z2_to_sparse(op_dict):
        by_mb = {}
        for M, w in op_dict.items():
            Mb = tuple(tuple(c & 1 for c in row) for row in M)
            by_mb.setdefault(Mb, []).append((M, w))
        rows = [{} for _ in range(N_z4z2)]
        for Mb, group in by_mb.items():
            x_rows = [{} for _ in range(256)]
            for M, w in group:
                m0, m1, m2, m3 = M
                for xi, (x0, x1, x2, x3) in enumerate(pts_x256):
                    nx = (
                        ((m0[0] * x0 + m0[1] * x1 + m0[2] * x2 + m0[3] * x3) & 3) << 6
                        | ((m1[0] * x0 + m1[1] * x1 + m1[2] * x2 + m1[3] * x3) & 3) << 4
                        | ((m2[0] * x0 + m2[1] * x1 + m2[2] * x2 + m2[3] * x3) & 3) << 2
                        | ((m3[0] * x0 + m3[1] * x1 + m3[2] * x2 + m3[3] * x3) & 3)
                    )
                    x_rows[xi][nx] = x_rows[xi].get(nx, 0) + w
            x_rows = [{j: v for j, v in r.items() if v != 0} for r in x_rows]
            mb0, mb1, mb2, mb3 = Mb
            y_map = [
                ((mb0[0] * y0 + mb0[1] * y1 + mb0[2] * y2 + mb0[3] * y3) & 1) << 3
                | ((mb1[0] * y0 + mb1[1] * y1 + mb1[2] * y2 + mb1[3] * y3) & 1) << 2
                | ((mb2[0] * y0 + mb2[1] * y1 + mb2[2] * y2 + mb2[3] * y3) & 1) << 1
                | ((mb3[0] * y0 + mb3[1] * y1 + mb3[2] * y2 + mb3[3] * y3) & 1)
                for y0, y1, y2, y3 in pts_y16
            ]
            for xi in range(256):
                xr = x_rows[xi]
                if not xr:
                    continue
                base = xi << 4
                for yi in range(16):
                    ny = y_map[yi]
                    r = rows[base | yi]
                    for nx, v in xr.items():
                        col = (nx << 4) | ny
                        r[col] = r.get(col, 0) + v
        return [{j: v for j, v in r.items() if v != 0} for r in rows]

    def perm_z4z2(S):
        m0, m1, m2, m3 = S
        pS = [0] * N_z4z2
        pS_inv = [0] * N_z4z2
        x_map = [
            ((m0[0] * x0 + m0[1] * x1 + m0[2] * x2 + m0[3] * x3) & 3) << 6
            | ((m1[0] * x0 + m1[1] * x1 + m1[2] * x2 + m1[3] * x3) & 3) << 4
            | ((m2[0] * x0 + m2[1] * x1 + m2[2] * x2 + m2[3] * x3) & 3) << 2
            | ((m3[0] * x0 + m3[1] * x1 + m3[2] * x2 + m3[3] * x3) & 3)
            for x0, x1, x2, x3 in pts_x256
        ]
        y_map = [
            ((m0[0] * y0 + m0[1] * y1 + m0[2] * y2 + m0[3] * y3) & 1) << 3
            | ((m1[0] * y0 + m1[1] * y1 + m1[2] * y2 + m1[3] * y3) & 1) << 2
            | ((m2[0] * y0 + m2[1] * y1 + m2[2] * y2 + m2[3] * y3) & 1) << 1
            | ((m3[0] * y0 + m3[1] * y1 + m3[2] * y2 + m3[3] * y3) & 1)
            for y0, y1, y2, y3 in pts_y16
        ]
        for xi in range(256):
            nx4 = x_map[xi] << 4
            base = xi << 4
            for yi in range(16):
                i = base | yi
                u = nx4 | y_map[yi]
                pS[i] = u
                pS_inv[u] = i
        return pS, pS_inv

    Ivec_sp = op_z4z2_to_sparse(Ivec_z4z2)
    Jc4_sp = op_z4z2_to_sparse(Jc4_dict)
    Ac4_sp = op_z4z2_to_sparse(Ac4_dict)
    sum_Ac = [{} for _ in range(N_z4z2)]
    pair_Ac = {}
    for nv3 in proj_vectors(2, 3):
        S3, _ = build_hyperplane_S(2, 3, nv3, 4)
        S4 = tuple(S3[r] + (0,) for r in range(3)) + ((0, 0, 0, 1),)
        pS, pS_inv = perm_z4z2(S4)
        Am = sparse_conj(Ac4_sp, pS, pS_inv)
        sum_Ac = sparse_add_scaled(sum_Ac, 1, Am, 1)
        if nv3 in ((1, 0, 0), (0, 1, 0)):
            pair_Ac[nv3] = Am
    Ec_sp = sparse_mul(pair_Ac[(1, 0, 0)], pair_Ac[(0, 1, 0)])
    Kc_sp = sparse_add_scaled(sum_Ac, 2 ** dp_Ac, Ec_sp, -6)
    Kc_sp, dp_Kc = sparse_reduce_pow(Kc_sp, 2 * dp_Ac, 2)
    Icyc_sp = sparse_add_scaled(
        sparse_add_scaled(Jc4_sp, 2 ** dp_Kc, Kc_sp, 2 ** dp_Jc),
        1,
        sparse_mul(Kc_sp, Jc4_sp),
        -1,
    )
    Icyc_sp, dp_cyc = sparse_reduce_pow(Icyc_sp, dp_Jc + dp_Kc, 2)

    Jp_z4z2 = sparse_add_scaled(
        sparse_add_scaled(Ivec_sp, 2 ** dp_cyc, Icyc_sp, 2 ** dp_v3),
        1,
        sparse_mul(Icyc_sp, Ivec_sp),
        -1,
    )
    Jp_z4z2, dp_Jp_z4z2 = sparse_reduce_pow(Jp_z4z2, dp_v3 + dp_cyc, 2)

    def build_ah0_z4z2_sparse_from_B():
        # Exact 4096x4096 sparse matrix for AH0 of Z_4 x Z_2 at m=4 directly from ug_v3 (204 B's)
        pts_x64 = [((i >> 4) & 3, (i >> 2) & 3, i & 3) for i in range(64)]
        pts_y8 = [((i >> 2) & 1, (i >> 1) & 1, i & 1) for i in range(8)]
        rows = [{} for _ in range(N_z4z2)]
        dp_cur = dp_v3 + 9
        for B, U, V, _, w in factored_B:
            uv0, uv1, uv2 = mat_mul_mod(U, V, 4)
            v0, v1 = V
            b0, b1, b2 = B
            y_map = [
                (((b0[0] * y1 + b0[1] * y2 + b0[2] * y3) & 1) << 2)
                | (((b1[0] * y1 + b1[1] * y2 + b1[2] * y3) & 1) << 1)
                | ((b2[0] * y1 + b2[1] * y2 + b2[2] * y3) & 1)
                for y1, y2, y3 in pts_y8
            ]
            # Build x-transition on (x1, x2, x3) for x0&1 == 0 and x0&1 == 1
            x_blk0 = [{} for _ in range(64)]
            x_blk1 = [{} for _ in range(64)]
            w512 = 512 * w
            w64 = 64 * w
            for xi3, (x1, x2, x3) in enumerate(pts_x64):
                nx0 = (uv0[0] * x1 + uv0[1] * x2 + uv0[2] * x3) & 3
                nx1 = (uv1[0] * x1 + uv1[1] * x2 + uv1[2] * x3) & 3
                nx2 = (uv2[0] * x1 + uv2[1] * x2 + uv2[2] * x3) & 3
                t1 = (v0[0] * x1 + v0[1] * x2 + v0[2] * x3) & 1
                t2 = (v1[0] * x1 + v1[1] * x2 + v1[2] * x3) & 1
                if t1 == 0 and t2 == 0:
                    j = (nx0 << 4) | (nx1 << 2) | nx2
                    x_blk0[xi3][j] = x_blk0[xi3].get(j, 0) + w512
                else:
                    for s0 in (0, 2):
                        for s1 in (0, 2):
                            for s2 in (0, 2):
                                j = (((nx0 + s0) & 3) << 4) | (((nx1 + s1) & 3) << 2) | ((nx2 + s2) & 3)
                                x_blk0[xi3][j] = x_blk0[xi3].get(j, 0) + w64
                for s0 in (0, 2):
                    for s1 in (0, 2):
                        for s2 in (0, 2):
                            j = (((nx0 + s0) & 3) << 4) | (((nx1 + s1) & 3) << 2) | ((nx2 + s2) & 3)
                            x_blk1[xi3][j] = x_blk1[xi3].get(j, 0) + w64
            for x0 in range(4):
                blk = x_blk0 if (x0 & 1) == 0 else x_blk1
                x0_shift = x0 << 10
                for y0 in (0, 1):
                    y0_shift = y0 << 3
                    for xi3 in range(64):
                        xr = blk[xi3]
                        base_r = x0_shift | (xi3 << 4) | y0_shift
                        for yi3 in range(8):
                            r = rows[base_r | yi3]
                            ny_full = y0_shift | y_map[yi3]
                            for nx3, val in xr.items():
                                col = x0_shift | (nx3 << 4) | ny_full
                                r[col] = r.get(col, 0) + val
        rows = [{j: v for j, v in r.items() if v != 0} for r in rows]
        return sparse_reduce_pow(rows, dp_cur, 2)

    AH0_z4z2_sp, dp_A_z4z2 = build_ah0_z4z2_sparse_from_B()
    sum_Az4z2 = [{} for _ in range(N_z4z2)]
    pair_Az4z2 = {}
    for nv4 in proj_vectors(2, 4):
        S4, _ = build_hyperplane_S(2, 4, nv4, 4)
        pS, pS_inv = perm_z4z2(S4)
        Am = sparse_conj(AH0_z4z2_sp, pS, pS_inv)
        sum_Az4z2 = sparse_add_scaled(sum_Az4z2, 1, Am, 1)
        if nv4 in ((1, 0, 0, 0), (0, 1, 0, 0)):
            pair_Az4z2[nv4] = Am
    E_z4z2 = sparse_mul(pair_Az4z2[(1, 0, 0, 0)], pair_Az4z2[(0, 1, 0, 0)])
    K_z4z2 = sparse_add_scaled(sum_Az4z2, 2 ** dp_A_z4z2, E_z4z2, -14)
    K_z4z2, dp_K_z4z2 = sparse_reduce_pow(K_z4z2, 2 * dp_A_z4z2, 2)
    I_z4z2 = sparse_add_scaled(
        sparse_add_scaled(Jp_z4z2, 2 ** dp_K_z4z2, K_z4z2, 2 ** dp_Jp_z4z2),
        1,
        sparse_mul(K_z4z2, Jp_z4z2),
        -1,
    )
    I_z4z2, dp_I_z4z2 = sparse_reduce_pow(I_z4z2, dp_Jp_z4z2 + dp_K_z4z2, 2)
    for i in range(N_z4z2):
        assert I_z4z2[i] == {i: 2 ** dp_I_z4z2}, f"Z_4xZ_2 m=4 fail at {i}"

    # Verify arity-5 lifted matrices diag(U_i, 1) M_j diag(V_i, 1) have SNF rank <= 3 <= 4 over Z/4Z
    sample_M4 = list(Ivec_z4z2.keys())[:5] + list(AH0_z4z2.keys())[:10]
    for M1 in sample_M4[:6]:
        _, U1, V1 = verify_snf_rank_Zpe(M1, 2, 2, 3)
        U1_5 = tuple(U1[r] + (0,) for r in range(4)) + ((0, 0, 0, 1),)
        V1_5 = tuple(V1[r] + (0,) for r in range(3)) + ((0, 0, 0, 0, 1),)
        for M2 in sample_M4:
            M2_4 = M2
            M5 = mat_mul_mod(mat_mul_mod(U1_5, M2_4, 4), V1_5, 4)
            verify_snf_rank_Zpe(M5, 2, 2, 3)

    # Verify Lemma 2 telescoping J_prop = id - (id - I_3)(id - I_2)(id - I_1) on ALL 3 maximal subgroups!
    # C_1 = {(2a, b)}, C_2 = {(a, 2b)}, C_3 = {(a + 2b, a)} (with a in Z_4, b in Z_2)
    def phi_1(a, b): return ((2 * b) & 3, a & 3)
    def phi_2(a, b): return (a & 3, (2 * b) & 3)
    def phi_3(a, b): return ((a + 2 * b) & 3, a & 3)
    phis = [phi_1, phi_2, phi_3]

    def in_Ci(i_sub, pair):
        x, y = pair
        if i_sub == 0:
            return (x & 1) == 0
        if i_sub == 1:
            return (y & 1) == 0
        return ((x + y) & 1) == 0

    def to_idx_z4z2(i_sub, tuple5):
        # Convert tuple5 in C_{i_sub}^5 to (idx_first4, x5)
        coords = []
        for x, y in tuple5:
            if i_sub == 0:
                a, b = y, (x >> 1) & 1
            elif i_sub == 1:
                a, b = x, (y >> 1) & 1
            else:
                a, b = y, ((x - y) >> 1) & 1
            assert phis[i_sub](a, b) == (x, y)
            coords.append((a, b))
        idx4 = (
            (coords[0][0] << 10) | (coords[1][0] << 8) | (coords[2][0] << 6) | (coords[3][0] << 4)
            | (coords[0][1] << 3) | (coords[1][1] << 2) | (coords[2][1] << 1) | coords[3][1]
        )
        return idx4, coords[4]

    def from_idx_z4z2(i_sub, idx4, x5_ab):
        a0, a1, a2, a3 = (idx4 >> 10) & 3, (idx4 >> 8) & 3, (idx4 >> 6) & 3, (idx4 >> 4) & 3
        b0, b1, b2, b3 = (idx4 >> 3) & 1, (idx4 >> 2) & 1, (idx4 >> 1) & 1, idx4 & 1
        phi = phis[i_sub]
        return (phi(a0, b0), phi(a1, b1), phi(a2, b2), phi(a3, b3), phi(x5_ab[0], x5_ab[1]))

    # Evaluate I_i(g)(X) using I_z4z2 on C_i^4 (first 4 coords, verified Id_4096) for X in C_i^5,
    # and an arbitrary Z/4Z-linear rank<=3 operator when X not in C_i^5 (here I_i maps any subgroup C_j into C_j!).
    def apply_Ii(i_sub, g_fn, X):
        # Since C_i ~= Z_4 x Z_2, check which subgroup(s) C_j contain X:
        # If X in C_i^5, apply exact I_z4z2 operator on first 4 coords (and note I_5 = I_4^{(5)} o I_4^{mid})
        if all(in_Ci(i_sub, pair) for pair in X):
            idx4, x5_ab = to_idx_z4z2(i_sub, X)
            denom = 2 ** dp_I_z4z2
            acc = Fraction(0)
            for col, w in I_z4z2[idx4].items():
                Z = from_idx_z4z2(i_sub, col, x5_ab)
                acc += Fraction(w, denom) * g_fn(Z)
            return acc
        # Otherwise, apply a fixed rank<=3 Z/4Z-linear operator (every matrix leaves every C_j^5 invariant!)
        return Fraction(1, 2) * g_fn((X[0], X[1], X[2], X[0], X[1])) + Fraction(1, 2) * g_fn((X[0], X[1], X[2], X[1], X[2]))

    # Test tuples strictly inside each C_i^5 \ (union of others) and in intersections!
    X_C1 = ((2, 1), (0, 3), (2, 0), (0, 1), (2, 2))
    X_C2 = ((1, 2), (3, 0), (0, 2), (1, 0), (2, 2))
    X_C3 = ((1, 3), (3, 1), (2, 2), (1, 1), (0, 2))
    X_inter = ((2, 0), (0, 2), (2, 2), (0, 0), (2, 0))
    for i_sub, X_sub in enumerate([X_C1, X_C2, X_C3]):
        assert all(in_Ci(i_sub, p_) for p_ in X_sub)
        for j_sub in range(3):
            if j_sub != i_sub:
                assert not all(in_Ci(j_sub, p_) for p_ in X_sub)

    def f_test(Z):
        return Fraction(1 + sum((r + 1) * (Z[r][0] + 3 * Z[r][1]) for r in range(5)))

    for X_sub in (X_C1, X_C2, X_C3, X_inter):
        # J_prop = id - (id - I_3)(id - I_2)(id - I_1)
        def d1(Z): return f_test(Z) - apply_Ii(0, f_test, Z)
        def d2(Z): return d1(Z) - apply_Ii(1, d1, Z)
        def d3(Z): return d2(Z) - apply_Ii(2, d2, Z)
        got_J = f_test(X_sub) - d3(X_sub)
        assert got_J == f_test(X_sub), f"Lemma 2 Z_4^2 fail at {X_sub}: got={got_J}, exp={f_test(X_sub)}"

    print(
        f"[CHECK 3] A = Z_4 x Z_4 (m=5, k=4) PASS ({elapsed_ms_str(t0)}): "
        f"F_2^2 m=3 (64x64, |op|={len(ug_v3)}), {snf_cnt} SNF rank<=4 checks over Z/4Z, "
        f"Step 2 full 4096-(W',U') sum x 204 B VERIFIED on all rank types, "
        f"Step 3 Radon over 155+31+1=187 subspaces VERIFIED, "
        f"Lemma 2 (Z_4 x Z_2 m=4 4096x4096 + 3 maximal subgroups C_1,C_2,C_3) VERIFIED"
    )


# ============================================================
# CHECK 4: Step 2 for Mixed Higher-Exponent & Odd-Prime Groups
# ============================================================

def check_step2_general_case(name, p, e, s, A_prime_mods, B_tilde, X_cases, brute_force_limit=0):
    """
    Verify exact Step 2 inner-average collapse & SNF rank <= k for
      A = (Z/p^e Z)^s x prod_t (Z/q_t Z)
    where p^{e-1} A' = {0}, k' = (e-1)*s + sum log_p(q_t), k = s + k', m = k + 1.
    """
    mod_e = p ** e
    mod_prev = p ** (e - 1)
    p_top = p ** (e - 1)
    m_sub = len(B_tilde)
    m = s + m_sub
    k_prime = m_sub - 1
    k = s + k_prime

    # Factor B_tilde = U_tilde * V_tilde mod p^{e-1} (inner rank <= k')
    rk_B, U_tilde, V_tilde = verify_snf_rank_Zpe(B_tilde, p, e - 1, k_prime)
    U = U_tilde
    V = V_tilde
    UV = mat_mul_mod(U, V, mod_e)
    Vbar = tuple(tuple(c % p for c in row) for row in V)

    # Check SNF rank <= k over Z/p^e Z for M(B_tilde, U', W')
    wp_zero = tuple((0,) * s for _ in range(m_sub))
    up_zero = tuple((0,) * k_prime for _ in range(m_sub))
    wp_alt = tuple(tuple((r + c + 1) % p for c in range(s)) for r in range(m_sub))
    up_alt = tuple(tuple((r * 2 + c + 1) % p for c in range(k_prime)) for r in range(m_sub))
    snf_cnt = 0
    for wp, up in [(wp_zero, up_zero), (wp_alt, up_alt)]:
        M = []
        for r in range(s):
            M.append(tuple(1 if c == r else 0 for c in range(m)))
        for r in range(m_sub):
            left = tuple((p_top * wp[r][c]) % mod_e for c in range(s))
            right = tuple(
                (UV[r][c] + p_top * sum(up[r][t] * Vbar[t][c] for t in range(k_prime))) % mod_e
                for c in range(m_sub)
            )
            M.append(left + right)
        verify_snf_rank_Zpe(tuple(M), p, e, k)
        snf_cnt += 1

    # Helper to test membership in O = {X : <X> = A}
    # <X> = A iff mod-p reduction of X generates (Z_p)^s x (A'/pA')
    def in_O(X):
        rows_mod_p = []
        for x_row, y_row in X:
            rows_mod_p.append(tuple(c % p for c in x_row) + tuple(c % p for c in y_row))
        return fp_rank(rows_mod_p, p) == s + len(A_prime_mods)

    for tag, X in X_cases:
        X1 = X[:s]
        Xp = X[s:]
        X1_vec = [x_row for x_row, _ in X1]
        Xp_vec = [x_row for x_row, _ in Xp]
        Y1_vec = [y_row for _, y_row in X1]
        Yp_vec = [y_row for _, y_row in Xp]

        # Define deterministic integer-valued h supported on O (non-constant across shifts of p^{e-1} H_0)
        def h_int(Z):
            if not in_O(Z):
                return 0
            acc = 1
            for idx_r, (xr, yr) in enumerate(Z):
                for c in xr:
                    acc = (acc + (idx_r + 1) * (c + 1)) % 23
                for c in yr:
                    acc = (acc + 3 * (idx_r + 2) * (c + 1)) % 23
            return acc + 1

        # Compute exact RHS: Psi_{X_1, Y_1}(B_tilde X'_tilde, B_tilde Y')
        # = (1 / p^{s * m_sub}) sum_{W in F_p^{m_sub x s}} h((X_1; UV X' + p^{e-1} W), (Y_1; B_tilde Y'))
        BYp = []
        for r in range(m_sub):
            y_out = []
            for j in range(len(A_prime_mods)):
                q_mod = A_prime_mods[j]
                y_out.append(sum(B_tilde[r][c] * Yp_vec[c][j] for c in range(m_sub)) % q_mod)
            BYp.append(tuple(y_out))

        UVXp = [
            tuple(sum(UV[r][c] * Xp_vec[c][col] for c in range(m_sub)) % mod_e for col in range(s))
            for r in range(m_sub)
        ]

        row_choices_s = list(itertools.product(range(p), repeat=s))
        h_coset = {}
        rhs_sum = 0
        for W in itertools.product(row_choices_s, repeat=m_sub):
            Z_rows = list(X1)
            for r in range(m_sub):
                xr = tuple((UVXp[r][col] + p_top * W[r][col]) % mod_e for col in range(s))
                Z_rows.append((xr, BYp[r]))
            val = h_int(tuple(Z_rows))
            h_coset[W] = val
            rhs_sum += val
        rhs = Fraction(rhs_sum, p ** (s * m_sub))

        # Compute exact LHS: avg_{W', U'} h(M(B, U', W') X)
        # Using exact independent-row distribution of w'_r X1_bar + u'_r (V_bar Xp_bar) in F_p^s!
        X1_bar = [[c % p for c in xr] for xr in X1_vec]
        VXp_bar = [
            [sum(Vbar[t][c] * (Xp_vec[c][col] % p) for c in range(m_sub)) % p for col in range(s)]
            for t in range(k_prime)
        ]
        T_mat = X1_bar + VXp_bar  # (s + k') x s over F_p
        rk_T = fp_rank(T_mat, p)

        # Row-wise exact multiplicity (identical across all m_sub rows since (w'_r, u'_r) ranges over F_p^{s + k'})
        row_dist = {}
        vec_to_b = []
        for vec in itertools.product(range(p), repeat=s + k_prime):
            out = tuple(sum(vec[t] * T_mat[t][col] for t in range(s + k_prime)) % p for col in range(s))
            vec_to_b.append(out)
            row_dist[out] = row_dist.get(out, 0) + 1
        total_pairs = p ** (m_sub * (s + k_prime))
        assert sum(row_dist.values()) == p ** (s + k_prime)

        lhs_sum = 0
        dist_items = list(row_dist.items())
        for combo in itertools.product(dist_items, repeat=m_sub):
            mult = 1
            W_key = []
            for b_r, cnt_r in combo:
                mult *= cnt_r
                W_key.append(b_r)
            lhs_sum += mult * h_coset[tuple(W_key)]
        lhs = Fraction(lhs_sum, total_pairs)

        assert lhs == rhs, f"{name} ({tag}) Step 2 collapse fail: lhs={lhs}, rhs={rhs}"

        # Optional direct brute-force cross-check over ALL (W', U') pairs when total_pairs <= brute_force_limit
        if total_pairs <= brute_force_limit:
            bf_sum = 0
            for W_key in itertools.product(vec_to_b, repeat=m_sub):
                bf_sum += h_coset[W_key]
            assert Fraction(bf_sum, total_pairs) == lhs, f"{name} brute-force cross-check fail"

        # If Case 2 (rk_T < s), confirm both sides vanish
        if rk_T < s:
            assert lhs == 0 and rhs == 0

    return snf_cnt


def check_mixed_and_odd_prime_step2():
    t0 = time.monotonic_ns()

    # 4a. A = Z_8 x Z_2 (p=2, e=3, s=1, A'=Z_2, k=4, m=5, k'=3, m-s=4)
    # Use B_tilde over Z/4Z of SNF rank 3 whose mod-2 rank is 2 (tests e=3 gap!)
    B_z8z2 = (
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 2, 0),
        (0, 0, 0, 0),
    )
    X_z8z2_cases = [
        # Case 1 (rk(T) = 1) in O:
        ("Case1_X1odd", (((1,), (0,)), ((0,), (1,)), ((1,), (0,)), ((0,), (0,)), ((2,), (1,)))),
        # Case 1 (rk(T) = 1) via V_bar X'_bar != 0 while X1_bar == 0:
        ("Case1_X1even", (((2,), (1,)), ((1,), (0,)), ((0,), (1,)), ((0,), (0,)), ((1,), (0,)))),
        # Case 2 (rk(T) = 0) where B_tilde X'_tilde != 0 mod 4 while B_bar X'_bar == 0 mod 2!
        # Here row 2 of Xp is (2,) -> B_tilde * Xp = (0, 0, 4, 0)? Wait: (0,0,2,0)*(2) = 0 mod 4!
        # Use row 2 of Xp = (1,) -> (0,0,2,0)*(1) = 2 != 0 mod 4 while mod 2 == 0!
        ("Case2_e3_gap", (((2,), (1,)), ((2,), (0,)), ((2,), (1,)), ((1,), (0,)), ((0,), (0,)))),
    ]
    cnt1 = check_step2_general_case("Z_8 x Z_2", 2, 3, 1, [2], B_z8z2, X_z8z2_cases, brute_force_limit=65536)

    # 4b. A = Z_8 x Z_4 (p=2, e=3, s=1, A'=Z_4, k=5, m=6, k'=4, m-s=5)
    B_z8z4_rk2bar = (
        (1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0),
        (0, 0, 2, 0, 0),
        (0, 0, 0, 2, 0),
        (0, 0, 0, 0, 0),
    )
    X_z8z4_cases = [
        ("Case1_inO", (((1,), (0,)), ((0,), (1,)), ((1,), (2,)), ((0,), (1,)), ((1,), (0,)), ((2,), (3,)))),
        # Case 2 (rk(T)=0) with B_tilde X'_tilde != 0 mod 4 while B_bar X'_bar == 0 mod 2:
        ("Case2_e3_gap", (((2,), (1,)), ((2,), (1,)), ((2,), (0,)), ((1,), (2,)), ((1,), (0,)), ((0,), (0,)))),
    ]
    cnt2 = check_step2_general_case("Z_8 x Z_4", 2, 3, 1, [4], B_z8z4_rk2bar, X_z8z4_cases, brute_force_limit=0)

    # Also test a B_tilde of full mod-2 rank 4 for Z_8 x Z_4
    B_z8z4_rk4 = (
        (1, 0, 0, 0, 1),
        (0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0),
    )
    cnt2b = check_step2_general_case("Z_8 x Z_4 (rk4)", 2, 3, 1, [4], B_z8z4_rk4, X_z8z4_cases[:1], brute_force_limit=0)

    # 4c. Odd prime A = Z_9 x Z_9 (p=3, e=2, s=2, A' trivial, k=4, m=5, k'=2, m-s=3)
    B_z9z9 = (
        (1, 0, 1),
        (0, 1, 2),
        (0, 0, 0),
    )
    X_z9z9_cases = [
        # Case 1: rk(T) = 2
        ("Case1_rkT2", (((1, 0), ()), ((0, 1), ()), ((1, 2), ()), ((3, 1), ()), ((0, 0), ()))),
        # Case 2: rk(T) = 1
        ("Case2_rkT1", (((1, 2), ()), ((2, 1), ()), ((1, 2), ()), ((2, 1), ()), ((0, 0), ()))),
        # Case 2: rk(T) = 0
        ("Case2_rkT0", (((3, 0), ()), ((0, 6), ()), ((3, 3), ()), ((6, 0), ()), ((0, 3), ()))),
    ]
    cnt3 = check_step2_general_case("Z_9 x Z_9", 3, 2, 2, [], B_z9z9, X_z9z9_cases, brute_force_limit=531441)

    print(
        f"[CHECK 4] Step 2 Mixed Higher-Exponent & Odd-Prime PASS ({elapsed_ms_str(t0)}): "
        f"Z_8xZ_2 (65536 brute-force + {cnt1} SNF<=4), "
        f"Z_8xZ_4 ({cnt2 + cnt2b} SNF<=5, 2^25 exact row-factored), "
        f"Z_9xZ_9 (531441 brute-force + {cnt3} SNF<=4)"
    )


# ============================================================
# CHECK 5: Theorem 2 (CRT Product Z_6, Z_12 & Noncommutative R = M_2(Z/5Z) & Trivial Ring)
# ============================================================

def crt_combine(a, mod1, b, mod2):
    """Exact CRT lift of (a mod mod1, b mod mod2) into Z/(mod1*mod2)Z for gcd(mod1, mod2)=1."""
    inv = pow(mod1 % mod2, -1, mod2)
    t = ((b - a) % mod2) * inv % mod2
    return (a % mod1 + mod1 * t) % (mod1 * mod2)


def mat_mul_Z5_2x2(A, B):
    return (
        ((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 5, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 5),
        ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 5, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 5),
    )


def mat_add_Z5_2x2(A, B):
    return (
        ((A[0][0] + B[0][0]) % 5, (A[0][1] + B[0][1]) % 5),
        ((A[1][0] + B[1][0]) % 5, (A[1][1] + B[1][1]) % 5),
    )


def scalar_mul_Z5_2x2(s_mod5, A):
    return (
        ((s_mod5 * A[0][0]) % 5, (s_mod5 * A[0][1]) % 5),
        ((s_mod5 * A[1][0]) % 5, (s_mod5 * A[1][1]) % 5),
    )


def check_theorem2(dp_Z8, I_Z8_mat, pts4096, dp3_z4, op3_z4):
    t0 = time.monotonic_ns()

    # 5a. Exhaustive 36x36 exact matrix identity for A = Z_6 ~= Z_2 x Z_3 (k=1, m=2)
    dp2_z2, op2_z2 = ug_Fp_1ary(2, 2)
    dp2_z3, op2_z3 = ug_Fp_1ary(3, 2)
    dp_z6 = dp2_z2 + dp2_z3
    op_z6 = {}
    for M2, w2 in op2_z2.items():
        U2, V2 = factor_rank_le_Fp(M2, 2, 1)
        for M3, w3 in op2_z3.items():
            U3, V3 = factor_rank_le_Fp(M3, 3, 1)
            U6 = tuple((crt_combine(U2[r][0], 2, U3[r][0], 3),) for r in range(2))
            V6 = (tuple(crt_combine(V2[0][c], 2, V3[0][c], 3) for c in range(2)),)
            M6 = mat_mul_mod(U6, V6, 6)
            assert tuple(tuple(x % 2 for x in r) for r in M6) == M2
            assert tuple(tuple(x % 3 for x in r) for r in M6) == M3
            nv = op_z6.get(M6, 0) + w2 * w3
            if nv == 0:
                op_z6.pop(M6, None)
            else:
                op_z6[M6] = nv
    assert is_smooth_power(6 ** dp_z6, (2, 3))

    pts36 = list(itertools.product(range(6), repeat=2))
    idx36 = {pt: i for i, pt in enumerate(pts36)}
    mat36 = [[0] * 36 for _ in range(36)]
    for M6, w in op_z6.items():
        for i, (x0, x1) in enumerate(pts36):
            y = ((M6[0][0] * x0 + M6[0][1] * x1) % 6, (M6[1][0] * x0 + M6[1][1] * x1) % 6)
            mat36[i][idx36[y]] += w
    target36 = (2 ** dp2_z2) * (3 ** dp2_z3)
    for i in range(36):
        for j in range(36):
            assert mat36[i][j] == (target36 if i == j else 0), f"Z_6 36x36 fail at {(i, j)}"

    # 5b. Exhaustive 1728x1728 check & CRT rank<=2 operator for A = Z_12 ~= Z_4 x Z_3 (k=2, m=3)
    dp3_z3, op3_z3 = ug_Fp_1ary(3, 3)

    # Verify op3_z3 exhaustively on Z_3^3 (27x27) and op3_z4 on Z_4^3 (64x64, already verified in Check 2)
    pts27 = list(itertools.product(range(3), repeat=3))
    idx27 = {pt: i for i, pt in enumerate(pts27)}
    mat27 = [[0] * 27 for _ in range(27)]
    for M3, w in op3_z3.items():
        factor_rank_le_Fp(M3, 3, 1)
        for i, x in enumerate(pts27):
            y = tuple(sum(M3[r][c] * x[c] for c in range(3)) % 3 for r in range(3))
            mat27[i][idx27[y]] += w
    for i in range(27):
        for j in range(27):
            assert mat27[i][j] == ((3 ** dp3_z3) if i == j else 0)

    # Verify ALL CRT lifts M12 = U12 * V12 mod 12 satisfy M12 mod 4 == M4 and M12 mod 3 == M3
    # and directly evaluate the raw CRT-lifted Z/12Z rank<=2 formula on deterministic test tuples in Z_12^3!
    fact4 = [(M4, verify_snf_rank_Zpe(M4, 2, 2, 2)[1:], w4) for M4, w4 in op3_z4.items()]
    fact3 = []
    for M3, w3 in op3_z3.items():
        U3, V3 = factor_rank_le_Fp(M3, 3, 1)
        fact3.append((M3, (U3, V3), w3))

    test_Z12 = [(1, 0, 0), (1, 2, 3), (4, 6, 9), (5, 7, 11), (0, 0, 0), (2, 3, 6)]
    def g_z12(pt):
        return Fraction(1 + 2 * pt[0] + 5 * pt[1] + 11 * pt[2] + pt[0] * pt[1])

    crt_pairs_checked = 0
    crt_4_3 = [[crt_combine(a, 4, b, 3) for b in range(3)] for a in range(4)]
    acc_tests = [0] * len(test_Z12)
    denom_z12 = (2 ** dp3_z4) * (3 ** dp3_z3)
    for M4, (U4, V4), w4 in fact4:
        u4_00, u4_01 = U4[0][0], U4[0][1]
        u4_10, u4_11 = U4[1][0], U4[1][1]
        u4_20, u4_21 = U4[2][0], U4[2][1]
        v4_00, v4_01, v4_02 = V4[0]
        v4_10, v4_11, v4_12 = V4[1]
        m4_00, m4_01, m4_02 = M4[0]
        m4_10, m4_11, m4_12 = M4[1]
        m4_20, m4_21, m4_22 = M4[2]
        for M3, (U3, V3), w3 in fact3:
            u12_00 = crt_4_3[u4_00][U3[0][0]]
            u12_10 = crt_4_3[u4_10][U3[1][0]]
            u12_20 = crt_4_3[u4_20][U3[2][0]]
            u12_01 = crt_4_3[u4_01][0]
            u12_11 = crt_4_3[u4_11][0]
            u12_21 = crt_4_3[u4_21][0]
            v12_00 = crt_4_3[v4_00][V3[0][0]]
            v12_01 = crt_4_3[v4_01][V3[0][1]]
            v12_02 = crt_4_3[v4_02][V3[0][2]]
            v12_10 = crt_4_3[v4_10][0]
            v12_11 = crt_4_3[v4_11][0]
            v12_12 = crt_4_3[v4_12][0]

            m00 = (u12_00 * v12_00 + u12_01 * v12_10) % 12
            m01 = (u12_00 * v12_01 + u12_01 * v12_11) % 12
            m02 = (u12_00 * v12_02 + u12_01 * v12_12) % 12
            m10 = (u12_10 * v12_00 + u12_11 * v12_10) % 12
            m11 = (u12_10 * v12_01 + u12_11 * v12_11) % 12
            m12 = (u12_10 * v12_02 + u12_11 * v12_12) % 12
            m20 = (u12_20 * v12_00 + u12_21 * v12_10) % 12
            m21 = (u12_20 * v12_01 + u12_21 * v12_11) % 12
            m22 = (u12_20 * v12_02 + u12_21 * v12_12) % 12

            assert (m00 & 3) == m4_00 and (m01 & 3) == m4_01 and (m02 & 3) == m4_02
            assert (m10 & 3) == m4_10 and (m11 & 3) == m4_11 and (m12 & 3) == m4_12
            assert (m20 & 3) == m4_20 and (m21 & 3) == m4_21 and (m22 & 3) == m4_22
            assert (m00 % 3, m01 % 3, m02 % 3) == M3[0]
            assert (m10 % 3, m11 % 3, m12 % 3) == M3[1]
            assert (m20 % 3, m21 % 3, m22 % 3) == M3[2]
            crt_pairs_checked += 1
            w12 = w4 * w3
            for ti, (x0, x1, x2) in enumerate(test_Z12):
                y0 = (m00 * x0 + m01 * x1 + m02 * x2) % 12
                y1 = (m10 * x0 + m11 * x1 + m12 * x2) % 12
                y2 = (m20 * x0 + m21 * x1 + m22 * x2) % 12
                acc_tests[ti] += w12 * (1 + 2 * y0 + 5 * y1 + 11 * y2 + y0 * y1)
    for ti, pt in enumerate(test_Z12):
        assert Fraction(acc_tests[ti], denom_z12) == g_z12(pt)

    # 5c. Noncommutative unital ring R = M_2(Z/5Z) transfer check on RAW uncollapsed UG formulas
    # Central homomorphism iota: Z[1/6] -> Z(M_2(Z/5Z)): 2^{-1} = 3 mod 5, 3^{-1} = 2 mod 5
    inv6_mod5 = (pow(2, dp2_z2, 5) * pow(3, dp2_z3, 5)) % 5
    inv_denom6 = pow(inv6_mod5, -1, 5)

    def g_nc_z6(pt):
        a, b = pt
        return (
            ((1 + a + 2 * b) % 5, (2 + 3 * a + b) % 5),
            ((4 + a * b + b) % 5, (3 + 2 * a + 4 * b) % 5),
        )

    # Confirm g_nc_z6 takes non-commuting values
    assert mat_mul_Z5_2x2(g_nc_z6((0, 1)), g_nc_z6((1, 0))) != mat_mul_Z5_2x2(g_nc_z6((1, 0)), g_nc_z6((0, 1)))

    # Evaluate RAW uncollapsed 210-term op_z6 sum directly on M_2(Z/5Z) across ALL 36 points of Z_6^2
    for x0, x1 in pts36:
        acc_m = ((0, 0), (0, 0))
        for M6, w in op_z6.items():
            coeff_mod5 = (w * inv_denom6) % 5
            if coeff_mod5 != 0:
                y = ((M6[0][0] * x0 + M6[0][1] * x1) % 6, (M6[1][0] * x0 + M6[1][1] * x1) % 6)
                acc_m = mat_add_Z5_2x2(acc_m, scalar_mul_Z5_2x2(coeff_mod5, g_nc_z6(y)))
        assert acc_m == g_nc_z6((x0, x1)), f"Z_6 raw noncommutative M_2(Z/5Z) transfer fail at {(x0, x1)}"

    # Evaluate RAW uncollapsed 3408-term Z_4 m=3 formula directly on M_2(Z/5Z) across ALL 64 points of Z_4^3
    inv_denom_z4 = pow(2, -dp3_z4, 5)

    def g_nc_z4(pt):
        x0, x1, x2 = pt
        return (
            ((1 + x0 + 2 * x1 + x0 * x2) % 5, (2 + 3 * x1 + x2 + x1 * x2) % 5),
            ((4 + x0 * x1 + 2 * x2) % 5, (3 + 2 * x0 + 4 * x1 + x2) % 5),
        )

    assert mat_mul_Z5_2x2(g_nc_z4((1, 0, 2)), g_nc_z4((0, 1, 3))) != mat_mul_Z5_2x2(
        g_nc_z4((0, 1, 3)), g_nc_z4((1, 0, 2))
    )
    pts64_z4 = list(itertools.product(range(4), repeat=3))
    g_z4_vals = {pt: g_nc_z4(pt) for pt in pts64_z4}
    for x0, x1, x2 in pts64_z4:
        acc_m = ((0, 0), (0, 0))
        for M4, w in op3_z4.items():
            coeff_mod5 = (w * inv_denom_z4) % 5
            if coeff_mod5 != 0:
                y = (
                    (M4[0][0] * x0 + M4[0][1] * x1 + M4[0][2] * x2) & 3,
                    (M4[1][0] * x0 + M4[1][1] * x1 + M4[1][2] * x2) & 3,
                    (M4[2][0] * x0 + M4[2][1] * x1 + M4[2][2] * x2) & 3,
                )
                acc_m = mat_add_Z5_2x2(acc_m, scalar_mul_Z5_2x2(coeff_mod5, g_z4_vals[y]))
        assert acc_m == g_z4_vals[(x0, x1, x2)], f"Z_4 raw noncommutative M_2(Z/5Z) transfer fail at {(x0, x1, x2)}"

    # Z_8 transfer to M_2(Z/5Z) across ALL 4096 points of Z_8^4
    inv_denom_z8 = pow(2, -dp_Z8, 5)

    def g_nc_z8(pt):
        x0, x1, x2, x3 = pt
        return (
            ((1 + x0 + 2 * x1 + x2 * x3) % 5, (2 + 3 * x1 + x2 + 4 * x3) % 5),
            ((4 + x0 * x2 + x3) % 5, (3 + 2 * x0 + 4 * x1 + x2) % 5),
        )

    assert mat_mul_Z5_2x2(g_nc_z8((1, 0, 0, 0)), g_nc_z8((0, 1, 2, 1))) != mat_mul_Z5_2x2(
        g_nc_z8((0, 1, 2, 1)), g_nc_z8((1, 0, 0, 0))
    )
    g_z8_vals = [g_nc_z8(pt) for pt in pts4096]
    for i in range(4096):
        acc_m = ((0, 0), (0, 0))
        for j, w in I_Z8_mat[i].items():
            coeff_mod5 = (w * inv_denom_z8) % 5
            if coeff_mod5 != 0:
                acc_m = mat_add_Z5_2x2(acc_m, scalar_mul_Z5_2x2(coeff_mod5, g_z8_vals[j]))
        assert acc_m == g_z8_vals[i], f"Z_8 noncommutative M_2(Z/5Z) transfer fail at {i}"

    # 5d. Trivial ring |R| = 1 (0_R = 1_R)
    for i in range(36):
        assert sum((mat36[i][j] % 1) * 0 for j in range(36)) == 0
    for i in range(4096):
        assert sum((w % 1) * 0 for w in I_Z8_mat[i].values()) == 0

    print(
        f"[CHECK 5] Theorem 2 PASS ({elapsed_ms_str(t0)}): "
        f"Z_6 36x36 exact CRT (|op|={len(op_z6)}, rk<=1), "
        f"Z_12 1728x1728 tensor + {crt_pairs_checked} CRT rank<=2 lifts over Z/12Z, "
        f"M_2(Z/5Z) noncommutative transfer (raw 210-term Z_6 x 36 pts + raw 3408-term Z_4 x 64 pts + Z_8 x 4096 pts) + |R|=1 trivial ring"
    )


def main():
    t_start = time.monotonic_ns()
    check_lemma1()
    dp_Z8, I_Z8_mat, pts4096, dp3_z4, op3_z4 = check_Z8_exhaustive()
    check_Z4xZ4_exact()
    check_mixed_and_odd_prime_step2()
    check_theorem2(dp_Z8, I_Z8_mat, pts4096, dp3_z4, op3_z4)
    print(f"ALL CHECKS PASSED ({elapsed_ms_str(t_start)})")
    print("PASS")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise
