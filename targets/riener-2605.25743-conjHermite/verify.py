#!/usr/bin/env python3
r"""
Exact-arithmetic verification for the proof of Riener-Shapiro (arXiv:2605.25743v3)
Conjecture 6.5 (Section 6, \label{conj:hermite}) and Conjecture 1.1 (Section 1, \label{conj:sos}).

Verifies in exact rational / symbolic arithmetic (zero floating-point operations):
  1. Unimodular Bezoutian-Hermite congruence B(f) = T(f) H(f) T(f)^T,
     det T(f) = (-1)^{r(r-1)/2}, T(f)^{-1} in Z[c_1, ..., c_{r-1}]^{r x r},
     and det H(f) = disc(f) symbolically in generic roots for r = 2..6.
  2. Exact symbolic identities in Q[x_1, ..., x_n] for all 2 <= r <= n <= 6:
       - J_{n,r}(t) = (r!/n!) P^{(n-r)}(t) = binom(n,r)^{-1} sum_{|S|=r} P_S(t),
       - B(J_{n,r}) = C(x)^T W_{n,r} C(x),
       - H(J_{n,r}) = sum_j d_j v_j(x) v_j(x)^T with d_j in Q_{>0}, v_j in Q[x]^r.
  3. Exact Walsh-Hadamard positive-rational decomposition and exact rational LDL^T
     (all pivots strictly positive => W_{n,r} > 0) for W_{n,r}:
       - Full explicit (z, S) Walsh-Hadamard sum for all 2 <= r <= n <= 7
         and exact grouped identity for n = 8, 9,
       - Rational LDL^T positive definiteness for all 2 <= r <= n <= 7 (incl. (7,5))
         and (8,2), (8,3), (8,7), (8,8), (9,2), (9,3), (9,8), (9,9).
  4. Exact rational pointwise checks directly from P^{(k)} (including the paper's
     first open cases (n,k) = (7,2), (8,2), (8,3), (9,2), (9,3), (9,4), (10,4))
     in both original coordinates x and centered difference coordinates z_i = x_i - xbar,
     plus exact Sylvester-resultant discriminant & explicit Cauchy-Binet minor-sum checks.
"""

import os
import signal
import time
from fractions import Fraction
from itertools import combinations
from math import comb, factorial

# Enforce single-core execution
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

import sympy as sp

signal.alarm(90)


# ---------------------------------------------------------------------------
# Generic exact ring/field polynomial helpers (works with Fraction OR sp.Poly)
# ---------------------------------------------------------------------------

def ring_poly_mul(a, b, zero):
    res = [zero] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai != zero:
            for j, bj in enumerate(b):
                if bj != zero:
                    res[i + j] = res[i + j] + ai * bj
    return res


def ring_poly_deriv(a, k, zero):
    res = list(a)
    for _ in range(k):
        if len(res) <= 1:
            return [zero]
        res = [res[i] * i for i in range(1, len(res))]
    return res


def ring_bezoutian(f, zero):
    """Exact Bezoutian B(f) via coefficient-level division of (f(s)f'(t)-f'(s)f(t))/(s-t)."""
    r = len(f) - 1
    fp = ring_poly_deriv(f, 1, zero)
    num = [[zero] * (r + 1) for _ in range(r + 1)]
    for a in range(r + 1):
        for b in range(r):
            prod = f[a] * fp[b]
            num[a][b] = num[a][b] + prod
            num[b][a] = num[b][a] - prod
    B = [[zero] * r for _ in range(r)]
    rem = [row[:] for row in num]
    for a in range(r, 0, -1):
        for b in range(r + 1):
            c = rem[a][b]
            if c != zero:
                assert b < r, f"Unexpected degree in t: b={b}, r={r}"
                B[a - 1][b] = B[a - 1][b] + c
                rem[a][b] = zero
                rem[a - 1][b + 1] = rem[a - 1][b + 1] + c
    for a in range(r + 1):
        for b in range(r + 1):
            assert rem[a][b] == zero, f"Nonzero Bezoutian remainder at ({a},{b})"
    return B


def ring_hermite_from_monic(f, zero, one):
    """Ordinary Hermite matrix H(f) via exact Newton's identities from monic f."""
    r = len(f) - 1
    assert f[r] == one
    c = [f[r - d] for d in range(r + 1)]
    e = [c[d] if d % 2 == 0 else -c[d] for d in range(r + 1)]
    s = [zero] * (2 * r - 1)
    s[0] = one * r
    for m in range(1, 2 * r - 1):
        val = zero
        for j in range(1, min(m - 1, r) + 1):
            term = e[j] * s[m - j]
            val = val + term if (j - 1) % 2 == 0 else val - term
        if m <= r:
            term = e[m] * m
            val = val + term if (m - 1) % 2 == 0 else val - term
        s[m] = val
    return [[s[i + j] for j in range(r)] for i in range(r)]


def ring_T_and_Tinv(f, zero, one):
    """Build T(f) and its exact polynomial inverse T(f)^{-1} = L(f)^{-1} J."""
    r = len(f) - 1
    assert f[r] == one
    c = [f[r - d] for d in range(r + 1)]
    T = [[c[r - 1 - i - a] if i + a <= r - 1 else zero for a in range(r)] for i in range(r)]
    # L = J T is unit lower triangular: L[i][a] = c[i - a] for a <= i
    L = [[c[i - a] if a <= i else zero for a in range(r)] for i in range(r)]
    Linv = [[zero] * r for _ in range(r)]
    for j in range(r):
        Linv[j][j] = one
        for i in range(j + 1, r):
            acc = zero
            for k in range(j, i):
                acc = acc + L[i][k] * Linv[k][j]
            Linv[i][j] = -acc
    Tinv = [[Linv[i][r - 1 - j] for j in range(r)] for i in range(r)]
    return T, Tinv


def ring_mat_mul(A, B, zero):
    m, k, n = len(A), len(A[0]), len(B[0])
    assert len(B) == k
    out = [[zero] * n for _ in range(m)]
    for i in range(m):
        for t in range(k):
            ait = A[i][t]
            if ait != zero:
                for j in range(n):
                    btj = B[t][j]
                    if btj != zero:
                        out[i][j] = out[i][j] + ait * btj
    return out


def mat_T(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def poly_from_roots_ring(xs, zero, one):
    p = [one]
    for x in xs:
        p = ring_poly_mul(p, [-x, one], zero)
    return p


# ---------------------------------------------------------------------------
# Fraction-specific helpers
# ---------------------------------------------------------------------------

def exact_det_fraction(M):
    n = len(M)
    A = [row[:] for row in M]
    det = Fraction(1)
    for col in range(n):
        piv = None
        for row in range(col, n):
            if A[row][col] != 0:
                piv = row
                break
        if piv is None:
            return Fraction(0)
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            det = -det
        pv = A[col][col]
        det *= pv
        for row in range(col + 1, n):
            factor = A[row][col] / pv
            if factor:
                for j in range(col + 1, n):
                    A[row][j] -= factor * A[col][j]
    return det


def exact_disc_via_resultant(f):
    r = len(f) - 1
    lc = f[r]
    assert lc != 0
    fp = ring_poly_deriv(f, 1, Fraction(0))
    f_desc = list(reversed(f))
    fp_desc = list(reversed(fp))
    size = 2 * r - 1
    S = [[Fraction(0)] * size for _ in range(size)]
    for i in range(r - 1):
        for j, val in enumerate(f_desc):
            S[i][i + j] = val
    for i in range(r):
        for j, val in enumerate(fp_desc):
            S[r - 1 + i][i + j] = val
    res = exact_det_fraction(S)
    sign = -1 if ((r * (r - 1)) // 2) % 2 == 1 else 1
    return sign * res / lc


def build_W_exact(n, r):
    subsets = list(combinations(range(n), r - 1))
    masks = [sum(1 << i for i in U) for U in subsets]
    N = len(subsets)
    scale = Fraction(r, comb(n, r) * comb(n, r - 1))
    W = [[Fraction(0)] * N for _ in range(N)]
    for i in range(N):
        mi = masks[i]
        for j in range(i, N):
            mj = masks[j]
            union_sz = (mi | mj).bit_count()
            diff_sz = (mi & ~mj).bit_count()
            val = scale * Fraction(n - union_sz, diff_sz + 1)
            W[i][j] = val
            W[j][i] = val
    return subsets, masks, W


def gamma_exact(n, s):
    a = n - 1 - s
    b = s
    poly = [1]
    for _ in range(a):
        nxt = [0] * (len(poly) + 1)
        for i, c in enumerate(poly):
            nxt[i] += c
            nxt[i + 1] += c
        poly = nxt
    for _ in range(b):
        nxt = [0] * (len(poly) + 1)
        for i, c in enumerate(poly):
            nxt[i] += c
            nxt[i + 1] -= c
        poly = nxt
    integral = sum(Fraction(c, k + 2) for k, c in enumerate(poly))
    return integral / Fraction(2 ** (n - 2))


def exact_ldlt(M):
    N = len(M)
    L = [[Fraction(0)] * N for _ in range(N)]
    d = [Fraction(0)] * N
    for i in range(N):
        L[i][i] = Fraction(1)
        s = M[i][i] - sum(L[i][k] * L[i][k] * d[k] for k in range(i))
        assert s > 0, f"Non-positive pivot at index {i}: {s}"
        d[i] = s
        for j in range(i + 1, N):
            val = M[j][i] - sum(L[j][k] * L[i][k] * d[k] for k in range(i))
            L[j][i] = val / d[i]
    for i in range(N):
        for j in range(i, N):
            rec = sum(L[i][k] * d[k] * L[j][k] for k in range(i + 1))
            assert rec == M[i][j], f"LDL^T mismatch at ({i},{j})"
    return L, d


# ---------------------------------------------------------------------------
# Suite 1: Symbolic unimodular Bezoutian-Hermite congruence for r = 2..6
# ---------------------------------------------------------------------------

def run_suite_1():
    print("[Suite 1] Symbolic Bezoutian-Hermite congruence B(f) = T(f) H(f) T(f)^T (r = 2..6)...")
    for r in range(2, 7):
        R, *thetas = sp.ring(",".join(f"th{i}" for i in range(1, r + 1)), sp.ZZ)
        zero, one = R.zero, R.one
        f = poly_from_roots_ring(thetas, zero, one)
        B = ring_bezoutian(f, zero)
        # Direct power-sum Hermite matrix from roots
        H_roots = [[zero] * r for _ in range(r)]
        for i in range(r):
            for j in range(r):
                H_roots[i][j] = sum((th ** (i + j) for th in thetas), zero)
        H_newton = ring_hermite_from_monic(f, zero, one)
        assert H_roots == H_newton, f"Newton vs root Hermite mismatch at r={r}"
        T, Tinv = ring_T_and_Tinv(f, zero, one)
        prod_B = ring_mat_mul(ring_mat_mul(T, H_roots, zero), mat_T(T), zero)
        assert B == prod_B, f"B != T H T^T for r={r}"
        # Verify T * Tinv == I in Z[c_1, ..., c_{r-1}] using generic indeterminate coefficients
        Rc, *cs = sp.ring(",".join(f"c{i}" for i in range(1, r + 1)), sp.ZZ)
        f_gen = list(reversed([Rc.one] + list(cs)))  # ascending powers
        T_gen, T_gen_inv = ring_T_and_Tinv(f_gen, Rc.zero, Rc.one)
        I_gen = [[Rc.one if i == j else Rc.zero for j in range(r)] for i in range(r)]
        assert ring_mat_mul(T_gen, T_gen_inv, Rc.zero) == I_gen, f"T * Tinv != I in Z[c] for r={r}"
        assert ring_mat_mul(T_gen_inv, T_gen, Rc.zero) == I_gen, f"Tinv * T != I in Z[c] for r={r}"
        # Verify H = V^T V (Vandermonde factorization => det H = prod (th_a - th_b)^2 = disc(f))
        V = [[thetas[row] ** col for col in range(r)] for row in range(r)]
        assert ring_mat_mul(mat_T(V), V, zero) == H_roots, f"H != V^T V for r={r}"
    print("  Suite 1 OK (r = 2..6 over exact polynomial rings Z[th] and Z[c]).")


# ---------------------------------------------------------------------------
# Suite 2: Full symbolic proof verification in Q[x_1, ..., x_n] (2 <= r <= n <= 6)
# ---------------------------------------------------------------------------

def run_suite_2():
    print("[Suite 2] Full symbolic verification in Q[x_1,...,x_n] for all 2 <= r <= n <= 6...")
    count = 0
    for n in range(2, 7):
        R, *xs = sp.ring(",".join(f"x{i}" for i in range(1, n + 1)), sp.QQ)
        zero, one = R.zero, R.one
        P = poly_from_roots_ring(xs, zero, one)
        for r in range(2, n + 1):
            k = n - r
            Pk = ring_poly_deriv(P, k, zero)
            inv_lc = sp.QQ(factorial(r), factorial(n))
            J = [c * inv_lc for c in Pk]

            # Verify subset-average identity J_{n,r} = binom(n,r)^{-1} sum_{|S|=r} P_S
            inv_bin = sp.QQ(1, comb(n, r))
            J_sub = [zero] * (r + 1)
            for S in combinations(range(n), r):
                PS = poly_from_roots_ring([xs[i] for i in S], zero, one)
                for idx in range(r + 1):
                    J_sub[idx] = J_sub[idx] + PS[idx] * inv_bin
            assert J == J_sub, f"Subset average mismatch at (n,r)=({n},{r})"

            B = ring_bezoutian(J, zero)
            H = ring_hermite_from_monic(J, zero, one)
            T, Tinv = ring_T_and_Tinv(J, zero, one)
            assert B == ring_mat_mul(ring_mat_mul(T, H, zero), mat_T(T), zero)

            subsets, _, W_frac = build_W_exact(n, r)
            N = len(subsets)
            C = [poly_from_roots_ring([xs[u] for u in U], zero, one) for U in subsets]
            W_R = [[one * sp.QQ(val.numerator, val.denominator) for val in row] for row in W_frac]

            # Theorem 1: B(J_{n,r}) == C(x)^T W_{n,r} C(x) in Q[x_1, ..., x_n]
            B_rhs = ring_mat_mul(ring_mat_mul(mat_T(C), W_R, zero), C, zero)
            assert B == B_rhs, f"B != C^T W C symbolically at (n,r)=({n},{r})"

            # Theorem 3: exact rational LDL^T factorization H(J_{n,r}) == sum_j d_j v_j(x) v_j(x)^T
            L_frac, d_frac = exact_ldlt(W_frac)
            L_R = [[one * sp.QQ(val.numerator, val.denominator) for val in row] for row in L_frac]
            # M(x) = L^T C(x) T(J_{n,r})^{-T} (N x r over Q[x_1, ..., x_n])
            M = ring_mat_mul(ring_mat_mul(mat_T(L_R), C, zero), mat_T(Tinv), zero)
            H_sos = [[zero] * r for _ in range(r)]
            for idx in range(N):
                d_val = sp.QQ(d_frac[idx].numerator, d_frac[idx].denominator)
                row_m = M[idx]
                for i in range(r):
                    for j in range(i, r):
                        term = (row_m[i] * row_m[j]) * d_val
                        H_sos[i][j] = H_sos[i][j] + term
                        if i != j:
                            H_sos[j][i] = H_sos[j][i] + term
            assert H == H_sos, f"H != M^T D M symbolically at (n,r)=({n},{r})"
            count += 1
    print(f"  Suite 2 OK ({count} pairs, all 2 <= r <= n <= 6 verified symbolically over Q[x]).")


# ---------------------------------------------------------------------------
# Suite 3: Walsh-Hadamard identity & exact rational LDL^T for W_{n,r}
# ---------------------------------------------------------------------------

def run_suite_3():
    print("[Suite 3] Exact Walsh-Hadamard decomposition & rational LDL^T of W_{n,r}...")
    wh_count = 0
    ldlt_count = 0
    for n in range(2, 10):
        gammas = [gamma_exact(n, s) for s in range(n)]
        assert all(g > 0 for g in gammas)
        for r in range(2, n + 1):
            subsets, masks, W = build_W_exact(n, r)
            N = len(subsets)
            scale = Fraction(r, comb(n, r) * comb(n, r - 1))
            if n <= 7:
                W_wh = [[Fraction(0)] * N for _ in range(N)]
                for z in range(n):
                    zbit = 1 << z
                    other_bits = [1 << i for i in range(n) if i != z]
                    valid_idx = [idx for idx, m in enumerate(masks) if (m & zbit) == 0]
                    for s_mask in range(1 << (n - 1)):
                        S_bits = 0
                        s_size = 0
                        for pos, bit in enumerate(other_bits):
                            if (s_mask >> pos) & 1:
                                S_bits |= bit
                                s_size += 1
                        w = scale * gammas[s_size]
                        signs = [-1 if (masks[idx] & S_bits).bit_count() & 1 else 1 for idx in valid_idx]
                        for a_pos, idx_a in enumerate(valid_idx):
                            sa = signs[a_pos]
                            for b_pos in range(a_pos, len(valid_idx)):
                                idx_b = valid_idx[b_pos]
                                contrib = w if sa == signs[b_pos] else -w
                                W_wh[idx_a][idx_b] += contrib
                                if idx_a != idx_b:
                                    W_wh[idx_b][idx_a] += contrib
                assert W_wh == W, f"Full Walsh-Hadamard sum mismatch at (n,r)=({n},{r})"
            else:
                max_d = min(r - 1, n - r)
                for d in range(max_d + 1):
                    total = Fraction(0)
                    for k_in in range(2 * d + 1):
                        for k_out in range(n - 1 - 2 * d + 1):
                            ways = comb(2 * d, k_in) * comb(n - 1 - 2 * d, k_out)
                            sign = -1 if (k_in % 2 == 1) else 1
                            total += sign * ways * gammas[k_in + k_out]
                    assert total == Fraction(1, d + 1), (
                        f"Walsh-Hadamard 1/(d+1) mismatch at n={n}, d={d}: got {total}"
                    )
            wh_count += 1

            if N <= 36:
                exact_ldlt(W)
                ldlt_count += 1
    print(f"  Suite 3 OK ({wh_count} pairs verified for Walsh-Hadamard, {ldlt_count} exact rational LDL^T > 0).")


# ---------------------------------------------------------------------------
# Suite 4: Exact rational pointwise checks on higher (n, r) & Cauchy-Binet
# ---------------------------------------------------------------------------

def verify_pointwise_case(n, r, xs, check_cauchy_binet=False, check_resultant=True):
    k = n - r
    zero, one = Fraction(0), Fraction(1)
    xs_f = [Fraction(x) for x in xs]
    xbar = sum(xs_f) / Fraction(n)
    zs_f = [x - xbar for x in xs_f]

    subsets, _, W = build_W_exact(n, r)
    N = len(subsets)

    for label, coords in [("original", xs_f), ("centered", zs_f)]:
        P = poly_from_roots_ring(coords, zero, one)
        Pk = ring_poly_deriv(P, k, zero)
        lc = Fraction(factorial(n), factorial(r))
        J = [c / lc for c in Pk]

        H = ring_hermite_from_monic(J, zero, one)
        B = ring_bezoutian(J, zero)
        T, Tinv = ring_T_and_Tinv(J, zero, one)

        assert B == ring_mat_mul(ring_mat_mul(T, H, zero), mat_T(T), zero), (
            f"B != T H T^T at ({n},{r}) [{label}]"
        )

        C = [poly_from_roots_ring([coords[u] for u in U], zero, one) for U in subsets]
        B_rhs = ring_mat_mul(ring_mat_mul(mat_T(C), W, zero), C, zero)
        assert B == B_rhs, f"B != C^T W C at ({n},{r}) [{label}]"

        G = ring_mat_mul(C, mat_T(Tinv), zero)
        H_rhs = ring_mat_mul(ring_mat_mul(mat_T(G), W, zero), G, zero)
        assert H == H_rhs, f"H != G^T W G at ({n},{r}) [{label}]"

        if label == "centered":
            det_H = exact_det_fraction(H)
            if check_resultant:
                disc_Pk = exact_disc_via_resultant(
                    ring_poly_deriv(poly_from_roots_ring(xs_f, zero, one), k, zero)
                )
                expected_disc_Pk = (lc ** (2 * r - 2)) * det_H
                assert disc_Pk == expected_disc_Pk, (
                    f"D_k^(n) != (n!/r!)^{{2r-2}} det H at ({n},{r}): {disc_Pk} vs {expected_disc_Pk}"
                )
            if check_cauchy_binet:
                L, d = exact_ldlt(W)
                M = ring_mat_mul(mat_T(L), G, zero)
                cb_sum = Fraction(0)
                for rows in combinations(range(N), r):
                    weight = Fraction(1)
                    for idx in rows:
                        weight *= d[idx]
                    sub = [M[idx] for idx in rows]
                    det_sub = exact_det_fraction(sub)
                    cb_sum += weight * det_sub * det_sub
                assert cb_sum == det_H, f"Cauchy-Binet mismatch at ({n},{r}): {cb_sum} vs {det_H}"


def run_suite_4():
    print("[Suite 4] Exact pointwise checks (incl. open cases (7,5), (8,5), (8,6), (9,5), (9,6), (9,7), (10,6))...")
    cb_cases = [
        (3, 2, [0, 1, 4]),
        (3, 3, [-2, 1, 5]),
        (4, 2, [-3, 0, 2, 7]),
        (4, 3, [-3, 0, 2, 7]),
        (4, 4, [-3, 0, 2, 7]),
        (5, 2, [-5, -1, 0, 3, 8]),
        (5, 3, [-5, -1, 0, 3, 8]),
        (5, 4, [-5, -1, 0, 3, 8]),
        (5, 5, [-5, -1, 0, 3, 8]),
        (6, 2, [-7, -2, 1, 3, 6, 11]),
        (6, 3, [-7, -2, 1, 3, 6, 11]),
        (6, 5, [-7, -2, 1, 3, 6, 11]),
        (6, 6, [-7, -2, 1, 3, 6, 11]),
        (7, 2, [-9, -4, -1, 2, 5, 8, 13]),
        (7, 6, [-9, -4, -1, 2, 5, 8, 13]),
        (7, 7, [-9, -4, -1, 2, 5, 8, 13]),
    ]
    for n, r, xs in cb_cases:
        verify_pointwise_case(n, r, xs, check_cauchy_binet=True, check_resultant=True)

    open_cases = [
        (7, 5, [-9, -4, -1, 2, 5, 8, 13]),              # (n, k) = (7, 2): FIRST OPEN CASE in paper
        (7, 5, [0, 0, 1, 2, 5, 9, 14]),                 # repeated root test
        (7, 5, [-11, -3, -2, 0, 1, 4, 20]),
        (8, 5, [-10, -5, -2, 0, 3, 7, 11, 16]),         # (n, k) = (8, 3)
        (8, 6, [-10, -5, -2, 0, 3, 7, 11, 16]),         # (n, k) = (8, 2)
        (9, 5, [-12, -7, -3, -1, 2, 5, 8, 13, 19]),     # (n, k) = (9, 4)
        (9, 6, [-12, -7, -3, -1, 2, 5, 8, 13, 19]),     # (n, k) = (9, 3)
        (9, 7, [-12, -7, -3, -1, 2, 5, 8, 13, 19]),     # (n, k) = (9, 2)
        (10, 6, [-13, -8, -4, -1, 0, 2, 5, 9, 14, 21]), # (n, k) = (10, 4)
    ]
    for n, r, xs in open_cases:
        verify_pointwise_case(n, r, xs, check_cauchy_binet=False, check_resultant=True)
    print(f"  Suite 4 OK ({len(cb_cases)} full Cauchy-Binet + {len(open_cases)} open/higher cases verified).")


def main():
    t0 = time.time()
    run_suite_1()
    run_suite_2()
    run_suite_3()
    run_suite_4()
    elapsed = time.time() - t0
    print(f"ALL SUITES VERIFIED EXACTLY in {elapsed:.2f}s.")
    print("PASS")


if __name__ == "__main__":
    main()
