#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for Riener-Shapiro (arXiv:2605.25743v3)
Conjecture 1.1 (conj:sos) and Conjecture 6.5 (conj:hermite).

Written solely from the primary source definitions and the mathematical
claims in PROOF.md, without consulting any finder scripts.
Uses exclusively exact integer / Fraction / SymPy rational-polynomial arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb, factorial
import sys
import sympy as sp


def poly_coeffs_desc(expr: sp.Expr, t: sp.Symbol, deg: int) -> list[sp.Expr]:
    """Return [c_0, c_1, ..., c_deg] where expr = sum_{d=0}^deg c_d * t^(deg - d)."""
    p = sp.Poly(sp.expand(expr), t)
    coeffs = [sp.Integer(0)] * (deg + 1)
    for (power,), coeff in p.terms():
        coeffs[deg - power] = sp.expand(coeff)
    return coeffs


def newton_power_sums_from_monic(coeffs_desc: list[sp.Expr], max_m: int) -> list[sp.Expr]:
    """Compute s_0, s_1, ..., s_{max_m} for monic f(t) = sum_{d=0}^r c_d t^{r-d}, c_0=1."""
    r = len(coeffs_desc) - 1
    assert sp.expand(coeffs_desc[0] - 1) == 0
    s = [sp.Integer(r)]
    for m in range(1, max_m + 1):
        # Newton's identity: s_m + sum_{j=1}^{min(m-1,r)} c_j s_{m-j} + (m c_m if m<=r else 0) = 0
        acc = sp.Integer(0)
        for j in range(1, min(m, r) + 1):
            if j < m:
                acc += coeffs_desc[j] * s[m - j]
            elif j == m:
                acc += m * coeffs_desc[m]
        s.append(sp.expand(-acc))
    return s


def hermite_matrix_from_monic(coeffs_desc: list[sp.Expr]) -> sp.Matrix:
    r = len(coeffs_desc) - 1
    s = newton_power_sums_from_monic(coeffs_desc, 2 * r - 2)
    return sp.Matrix(r, r, lambda i, j: s[i + j])


def bezoutian_matrix(f_expr: sp.Expr, t: sp.Symbol, r: int) -> sp.Matrix:
    """Compute B(f) from (f(s) f'(t) - f'(s) f(t)) / (s - t)."""
    s_sym, u_sym = sp.symbols("_s_bez _u_bez")
    fs = sp.expand(f_expr.subs(t, s_sym))
    fu = sp.expand(f_expr.subs(t, u_sym))
    df = sp.diff(f_expr, t)
    dfs = sp.expand(df.subs(t, s_sym))
    dfu = sp.expand(df.subs(t, u_sym))
    num = sp.expand(fs * dfu - dfs * fu)
    quo, rem = sp.poly(num, s_sym).div(sp.poly(s_sym - u_sym, s_sym))
    assert rem.is_zero, f"Nonzero remainder in Bezoutian division: {rem}"
    q_expr = sp.expand(quo.as_expr())
    p = sp.Poly(q_expr, s_sym, u_sym)
    B = sp.zeros(r, r)
    for (i, j), val in p.terms():
        B[i, j] = sp.expand(val)
    return B


def t_matrix_from_monic(coeffs_desc: list[sp.Expr]) -> sp.Matrix:
    r = len(coeffs_desc) - 1
    def entry(i: int, a: int) -> sp.Expr:
        if i + a <= r - 1:
            return coeffs_desc[r - 1 - i - a]
        return sp.Integer(0)
    return sp.Matrix(r, r, entry)


def sylvester_discriminant(f_expr: sp.Expr, t: sp.Symbol, deg: int) -> sp.Expr:
    """Primary-source definition: (-1)^{m(m-1)/2} lc(f)^{-1} Res(f, f')."""
    p = sp.Poly(sp.expand(f_expr), t)
    assert p.degree() == deg
    lc = p.LC()
    df = sp.diff(f_expr, t)
    res = sp.resultant(f_expr, df, t)
    sign = -1 if (deg * (deg - 1) // 2) % 2 == 1 else 1
    return sp.simplify(sign * res / lc)


def exact_gamma(n: int, s: int) -> Fraction:
    """Exact Fraction for gamma_{n,s} = 2^{-(n-2)} int_0^1 u (1+u)^{n-1-s} (1-u)^s du."""
    # Expand (1+u)^a (1-u)^b exactly
    a = n - 1 - s
    b = s
    # Polynomial coefficients of u^k for k=0..n-1
    poly = [Fraction(0)] * n
    for i in range(a + 1):
        ci = comb(a, i)
        for j in range(b + 1):
            cj = comb(b, j) * ((-1) ** j)
            poly[i + j] += ci * cj
    # Multiply by u and integrate over [0,1]: int_0^1 u^{k+1} du = 1/(k+2)
    integral = sum(poly[k] * Fraction(1, k + 2) for k in range(n))
    return integral / Fraction(2 ** (n - 2))


def exact_W_matrix(n: int, r: int) -> tuple[list[tuple[int, ...]], list[list[Fraction]]]:
    subsets = list(combinations(range(1, n + 1), r - 1))
    scale = Fraction(r, comb(n, r) * comb(n, r - 1))
    N = len(subsets)
    W = [[Fraction(0)] * N for _ in range(N)]
    sets = [set(u) for u in subsets]
    for i in range(N):
        for j in range(i, N):
            union_sz = len(sets[i] | sets[j])
            diff_sz = len(sets[i] - sets[j])
            val = scale * Fraction(n - union_sz, diff_sz + 1)
            W[i][j] = val
            W[j][i] = val
    return subsets, W


def exact_ldlt(M: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[Fraction]]:
    """Exact rational L0 * D * L0^T factorization in Fraction arithmetic."""
    N = len(M)
    L = [[Fraction(0)] * N for _ in range(N)]
    D = [Fraction(0)] * N
    for j in range(N):
        L[j][j] = Fraction(1)
        s = M[j][j] - sum(L[j][k] * L[j][k] * D[k] for k in range(j))
        assert s > 0, f"Pivot D[{j}]={s} not strictly positive!"
        D[j] = s
        for i in range(j + 1, N):
            val = M[i][j] - sum(L[i][k] * L[j][k] * D[k] for k in range(j))
            L[i][j] = val / D[j]
    return L, D


def check_lemma1() -> None:
    print("[1/5] Checking Lemma 1 symbolically for 2 <= n <= 6, 0 <= k <= n-2...")
    t = sp.Symbol("t")
    for n in range(2, 7):
        xs = sp.symbols(f"x1:{n+1}")
        P = sp.Integer(1)
        for xi in xs:
            P *= (t - xi)
        P = sp.expand(P)
        for k in range(0, n - 1):
            r = n - k
            Pk = sp.expand(sp.diff(P, t, k))
            lc = sp.Poly(Pk, t).LC()
            expected_lc = sp.Rational(factorial(n), factorial(r))
            assert sp.expand(lc - expected_lc) == 0, f"lc mismatch at n={n}, k={k}"
            J = sp.expand(Pk / lc)

            # Subset average for J_{n,r}
            subsets_r = list(combinations(range(n), r))
            J_sub = sp.Integer(0)
            for S in subsets_r:
                PS = sp.Integer(1)
                for idx in S:
                    PS *= (t - xs[idx])
                J_sub += PS
            J_sub = sp.expand(J_sub / comb(n, r))
            assert sp.expand(J - J_sub) == 0, f"J_sub mismatch at n={n}, k={k}"

            # Subset average for J'_{n,r}
            dJ = sp.expand(sp.diff(J, t))
            subsets_rm1 = list(combinations(range(n), r - 1))
            dJ_sub = sp.Integer(0)
            for T in subsets_rm1:
                PT = sp.Integer(1)
                for idx in T:
                    PT *= (t - xs[idx])
                dJ_sub += PT
            dJ_sub = sp.expand(sp.Rational(r, comb(n, r - 1)) * dJ_sub)
            assert sp.expand(dJ - dJ_sub) == 0, f"dJ_sub mismatch at n={n}, k={k}"
    print("  Lemma 1: PASS (all 15 pairs for 2 <= n <= 6)")


def check_lemma2() -> None:
    print("[2/5] Checking Lemma 2 symbolically for r = 2..6...")
    t = sp.Symbol("t")
    for r in range(2, 7):
        cs = [sp.Integer(1)] + list(sp.symbols(f"c1:{r+1}"))
        f = sum(cs[d] * t ** (r - d) for d in range(r + 1))
        B = bezoutian_matrix(f, t, r)
        T = t_matrix_from_monic(cs)
        H = hermite_matrix_from_monic(cs)

        # (1) B(f) = T(f) H(f) T(f)^T
        diff_1 = sp.expand(B - T * H * T.T)
        assert diff_1.is_zero_matrix, f"B != T H T^T at r={r}"

        # (2) det T(f), J, L(f), Neumann series inverse
        det_T = sp.expand(T.det())
        expected_det = (-1) ** (r // 2)
        assert det_T == expected_det, f"det T mismatch at r={r}: {det_T} vs {expected_det}"
        assert (-1) ** (r // 2) == (-1) ** comb(r, 2)

        J = sp.Matrix(r, r, lambda i, j: 1 if i + j == r - 1 else 0)
        L = J * T
        for i in range(r):
            for a in range(r):
                expected = cs[i - a] if a <= i else sp.Integer(0)
                assert sp.expand(L[i, a] - expected) == 0
        N_mat = L - sp.eye(r)
        assert (N_mat ** r).is_zero_matrix
        L_inv = sp.zeros(r, r)
        N_pow = sp.eye(r)
        for m in range(r):
            L_inv += ((-1) ** m) * N_pow
            N_pow = sp.expand(N_pow * N_mat)
        T_inv = sp.expand(L_inv * J)
        assert sp.expand(T * T_inv - sp.eye(r)).is_zero_matrix
        assert sp.expand(T_inv * T - sp.eye(r)).is_zero_matrix
        # Verify T_inv only depends on c_1,...,c_{r-1}
        assert cs[r] not in T_inv.free_symbols

        # (3) H(f) = T^{-1} B (T^{-1})^T and det H(f) = disc(f)
        # Note: since T * T_inv == I and B == T * H * T^T, T_inv * B * T_inv^T == H follows algebraically,
        # and we also verify it directly via fast Poly matrix multiplication for r <= 5 and exact rational points for r=6.
        if r <= 5:
            R_ring = sp.polys.rings.ring(cs[1:], sp.QQ)[0]
            def to_ring_mat(M):
                return [[R_ring.from_expr(M[i, j]) for j in range(r)] for i in range(r)]
            def matmul_ring(A, B_m):
                return [[sum(A[i][k] * B_m[k][j] for k in range(r)) for j in range(r)] for i in range(r)]
            def trans_ring(A):
                return [[A[j][i] for j in range(r)] for i in range(r)]
            Tinv_r = to_ring_mat(T_inv)
            B_r = to_ring_mat(B)
            H_r = to_ring_mat(H)
            prod_r = matmul_ring(matmul_ring(Tinv_r, B_r), trans_ring(Tinv_r))
            for i in range(r):
                for j in range(r):
                    assert prod_r[i][j] == H_r[i][j], f"H != T^-1 B T^-T at r={r}"
        else:
            for trial in range(3):
                subs = {cs[d]: sp.Rational(d + 2 * trial + 1, trial + 3) for d in range(1, r + 1)}
                assert (H.subs(subs) - T_inv.subs(subs) * B.subs(subs) * T_inv.subs(subs).T).is_zero_matrix

        if r <= 5:
            thetas = sp.symbols(f"th1:{r+1}")
            f_roots = sp.Integer(1)
            for th in thetas:
                f_roots *= (t - th)
            f_roots = sp.expand(f_roots)
            coeffs_roots = poly_coeffs_desc(f_roots, t, r)
            H_roots = hermite_matrix_from_monic(coeffs_roots)
            V = sp.Matrix(r, r, lambda l, a: thetas[l] ** a)
            assert sp.expand(H_roots - V.T * V).is_zero_matrix
            if r <= 4:
                van_disc = sp.Integer(1)
                for a in range(r):
                    for b in range(a + 1, r):
                        van_disc *= (thetas[b] - thetas[a]) ** 2
                assert sp.expand(H_roots.det() - van_disc) == 0
            else:
                # For r=5, verify det(V)^2 == prod (th_b - th_a)^2 via ring arithmetic
                van_prod = sp.Integer(1)
                for a in range(r):
                    for b in range(a + 1, r):
                        van_prod *= (thetas[b] - thetas[a])
                assert sp.expand(V.det() - van_prod) == 0 or sp.expand(V.det() + van_prod) == 0
        else:
            # For r=6, check det(H) == (-1)^{r(r-1)/2} Res(f, f') via a monic specialization with symbolic coefficients
            # Substitute c_d -> generic rational values? Even better: check symbolically with 3 symbolic params or exact resultant!
            # Actually r=6 resultant of generic degree-6 polynomial takes <2s? Let's test a few generic rational polys + partial symbolic.
            pass

        # Also check det H(f) == sylvester_discriminant(f, t, r) symbolically for r <= 4 and at rational tuples for r=5,6
        if r <= 4:
            sylv = sylvester_discriminant(f, t, r)
            assert sp.expand(H.det() - sylv) == 0
        else:
            for trial in range(3):
                subs = {cs[d]: sp.Rational(d + 2 * trial + 1, trial + 3) for d in range(1, r + 1)}
                f_num = f.subs(subs)
                H_num = H.subs(subs)
                assert sp.Rational(H_num.det()) == sp.Rational(sylvester_discriminant(f_num, t, r))
    print("  Lemma 2: PASS (r = 2..6)")


def check_lemma3() -> None:
    print("[3/5] Checking Lemma 3 symbolically for 2 <= r <= n <= 6...")
    t = sp.Symbol("t")
    for n in range(2, 7):
        xs = sp.symbols(f"x1:{n+1}")
        for r in range(2, n + 1):
            subsets_r = list(combinations(range(n), r))
            J = sp.Integer(0)
            for S in subsets_r:
                PS = sp.Integer(1)
                for idx in S:
                    PS *= (t - xs[idx])
                J += PS
            J = sp.expand(J / comb(n, r))
            B_J = bezoutian_matrix(J, t, r)

            subsets_rm1, W_frac = exact_W_matrix(n, r)
            W_sp = sp.Matrix(len(subsets_rm1), len(subsets_rm1),
                             lambda i, j: sp.Rational(W_frac[i][j].numerator, W_frac[i][j].denominator))
            assert (W_sp - W_sp.T).is_zero_matrix

            C = sp.zeros(len(subsets_rm1), r)
            for row_idx, U in enumerate(subsets_rm1):
                PU = sp.Integer(1)
                for u_one_based in U:
                    PU *= (t - xs[u_one_based - 1])
                PU = sp.expand(PU)
                p = sp.Poly(PU, t)
                for (pwr,), coeff in p.terms():
                    C[row_idx, pwr] = sp.expand(coeff)

            rhs = sp.expand(C.T * W_sp * C)
            assert sp.expand(B_J - rhs).is_zero_matrix, f"B(J) != C^T W C at n={n}, r={r}"
    print("  Lemma 3: PASS (all 15 pairs for 2 <= r <= n <= 6)")


def check_lemma4() -> None:
    print("[4/5] Checking Lemma 4 in exact Fraction arithmetic for 2 <= r <= n <= 8...")
    u_sym = sp.Symbol("u")
    for n in range(2, 9):
        gammas = [exact_gamma(n, s) for s in range(n)]
        for s in range(n):
            assert gammas[s] > 0
            # Cross-check against sympy.integrate
            sp_g = sp.Rational(1, 2 ** (n - 2)) * sp.integrate(
                u_sym * (1 + u_sym) ** (n - 1 - s) * (1 - u_sym) ** s, (u_sym, 0, 1)
            )
            assert Fraction(sp_g.p, sp_g.q) == gammas[s]

        for r in range(2, n + 1):
            subsets, W = exact_W_matrix(n, r)
            N = len(subsets)
            scale = Fraction(r, comb(n, r) * comb(n, r - 1))

            # Build rank-1 sum directly
            W_recon = [[Fraction(0)] * N for _ in range(N)]
            for z in range(1, n + 1):
                others = [el for el in range(1, n + 1) if el != z]
                # Precompute chi_{z, S} for each S subset of others
                for mask in range(1 << (n - 1)):
                    S = {others[b] for b in range(n - 1) if (mask >> b) & 1}
                    g = gammas[len(S)] * scale
                    chi = [0] * N
                    for idx, U in enumerate(subsets):
                        if z not in U:
                            inter = sum(1 for el in U if el in S)
                            chi[idx] = -1 if (inter & 1) else 1
                    for i in range(N):
                        ci = chi[i]
                        if ci == 0:
                            continue
                        gi = g * ci
                        for j in range(i, N):
                            cj = chi[j]
                            if cj != 0:
                                W_recon[i][j] += gi * cj
            for i in range(N):
                for j in range(i, N):
                    assert W_recon[i][j] == W[i][j], f"W recon mismatch at n={n}, r={r}, ({i},{j})"

            # Exact L0 D L0^T check (verifies strict positive definiteness via Sylvester)
            L0, D = exact_ldlt(W)
            assert all(d > 0 for d in D)
            # Reconstruct L0 D L0^T
            for i in range(N):
                for j in range(i, N):
                    val = sum(L0[i][k] * D[k] * L0[j][k] for k in range(min(i, j) + 1))
                    assert val == W[i][j], f"LDL^T recon mismatch at n={n}, r={r}"
    print("  Lemma 4: PASS (all 28 pairs for 2 <= r <= n <= 8)")


def build_C_and_J_numeric(xs: list[Fraction], r: int, subsets: list[tuple[int, ...]]) -> tuple[list[Fraction], sp.Matrix]:
    """Direct computation from P^{(n-r)} without using Lemma 1 shortcuts."""
    n = len(xs)
    k = n - r
    t = sp.Symbol("t")
    P = sp.Integer(1)
    for xv in xs:
        P *= (t - sp.Rational(xv.numerator, xv.denominator))
    P = sp.expand(P)
    Pk = sp.expand(sp.diff(P, t, k))
    lc = sp.Rational(factorial(n), factorial(r))
    assert sp.Poly(Pk, t).LC() == lc
    J = sp.expand(Pk / lc)
    coeffs = poly_coeffs_desc(J, t, r)

    C = sp.zeros(len(subsets), r)
    for row_idx, U in enumerate(subsets):
        PU = sp.Integer(1)
        for u_one_based in U:
            xv = xs[u_one_based - 1]
            PU *= (t - sp.Rational(xv.numerator, xv.denominator))
        p = sp.Poly(sp.expand(PU), t)
        for (pwr,), coeff in p.terms():
            C[row_idx, pwr] = sp.Rational(coeff)
    return coeffs, C


def check_theorem1_and_corollary2() -> None:
    print("[5/5] Checking Theorem 1 and Corollary 2 (symbolic 2<=r<=n<=5 + exact open cases)...")
    t = sp.Symbol("t")

    # Symbolic check for all 2 <= r <= n <= 5
    for n in range(2, 6):
        xs = sp.symbols(f"x1:{n+1}")
        xbar = sum(xs) / sp.Integer(n)
        zs = [xi - xbar for xi in xs]
        P_x = sp.Integer(1)
        for xi in xs:
            P_x *= (t - xi)
        P_x = sp.expand(P_x)

        gammas = [exact_gamma(n, s) for s in range(n)]

        for k in range(0, n - 1):
            r = n - k
            subsets, W = exact_W_matrix(n, r)
            L0, D = exact_ldlt(W)
            N = len(subsets)
            L0_sp = sp.Matrix(N, N, lambda i, j: sp.Rational(L0[i][j].numerator, L0[i][j].denominator))
            D_sp = sp.diag(*[sp.Rational(d.numerator, d.denominator) for d in D])

            # Direct P^{(k)} in x
            Pk_x = sp.expand(sp.diff(P_x, t, k))
            lc = sp.Rational(factorial(n), factorial(r))
            J_x = sp.expand(Pk_x / lc)
            coeffs_x = poly_coeffs_desc(J_x, t, r)
            H_x = hermite_matrix_from_monic(coeffs_x)
            T_x = t_matrix_from_monic(coeffs_x)
            T_inv_x = sp.expand(T_x.inv())

            C_x = sp.zeros(N, r)
            for row_idx, U in enumerate(subsets):
                PU = sp.Integer(1)
                for u_one_based in U:
                    PU *= (t - xs[u_one_based - 1])
                p = sp.Poly(sp.expand(PU), t)
                for (pwr,), coeff in p.terms():
                    C_x[row_idx, pwr] = sp.expand(coeff)

            # Check M(x)^T D M(x) == H(J_{n,r}(x))
            M_x = sp.expand(L0_sp.T * C_x * T_inv_x.T)
            assert sp.expand(H_x - M_x.T * D_sp * M_x).is_zero_matrix

            # Check explicit rank-1 sum in Theorem 1
            scale = sp.Rational(r, comb(n, r) * comb(n, r - 1))
            H_rank1 = sp.zeros(r, r)
            TCt = sp.expand(T_inv_x * C_x.T)
            for z_idx in range(1, n + 1):
                others = [el for el in range(1, n + 1) if el != z_idx]
                for mask in range(1 << (n - 1)):
                    S_set = {others[b] for b in range(n - 1) if (mask >> b) & 1}
                    g = gammas[len(S_set)]
                    g_sp = sp.Rational(g.numerator, g.denominator)
                    chi = sp.Matrix(N, 1, lambda i, _: (
                        0 if z_idx in subsets[i] else (-1 if len(S_set & set(subsets[i])) % 2 else 1)
                    ))
                    w = sp.expand(TCt * chi)
                    H_rank1 += g_sp * (w * w.T)
            H_rank1 = sp.expand(scale * H_rank1)
            assert sp.expand(H_x - H_rank1).is_zero_matrix

            # Corollary 2: substitute x_i -> z_i = x_i - xbar and check full Cauchy-Binet minor sum == D_k^{(n)}
            subs_z = {xs[i]: zs[i] for i in range(n)}
            M_z = sp.expand(M_x.subs(subs_z, simultaneous=True))

            # Verify translation invariance of M_z entries (each is a polynomial in differences x_i - x_j)
            shift = sp.Symbol("_shift_delta")
            subs_shift = {xi: xi + shift for xi in xs}
            assert sp.expand(M_z.subs(subs_shift, simultaneous=True) - M_z).is_zero_matrix

            R_x = sp.polys.rings.ring(xs, sp.QQ)[0]
            M_z_ring = [[R_x.from_expr(M_z[i, j]) for j in range(r)] for i in range(N)]

            def ring_det(rows: list[list]) -> object:
                m = len(rows)
                if m == 1:
                    return rows[0][0]
                if m == 2:
                    return rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0]
                if m == 3:
                    return (
                        rows[0][0] * (rows[1][1] * rows[2][2] - rows[1][2] * rows[2][1])
                        - rows[0][1] * (rows[1][0] * rows[2][2] - rows[1][2] * rows[2][0])
                        + rows[0][2] * (rows[1][0] * rows[2][1] - rows[1][1] * rows[2][0])
                    )
                acc = R_x.zero
                for c in range(m):
                    el = rows[0][c]
                    if not el:
                        continue
                    sub = [row[:c] + row[c + 1 :] for row in rows[1:]]
                    term = el * ring_det(sub)
                    acc = acc + term if (c % 2 == 0) else acc - term
                return acc

            if n <= 4 or r <= 3:
                Dk_direct = sylvester_discriminant(Pk_x, t, r)
                lc_frac = R_x.from_expr(lc ** (r - 1))
                cb_sum_r = R_x.zero
                for I in combinations(range(N), r):
                    prod_d = R_x.one
                    for idx in I:
                        prod_d *= R_x.from_expr(D_sp[idx, idx])
                    minor = ring_det([M_z_ring[idx] for idx in I])
                    scaled = lc_frac * minor
                    cb_sum_r += prod_d * scaled * scaled
                assert R_x.from_expr(Dk_direct) == cb_sum_r, f"Cauchy-Binet mismatch at n={n}, k={k}"
            elif (n, k) == (5, 0):
                # For k=0, N=r=5 so single minor: det(M_z) * prod_d^{1/2}; check det(M_z^T D M_z) == prod_{a<b}(x_a-x_b)^2
                prod_d = R_x.one
                for idx in range(N):
                    prod_d *= R_x.from_expr(D_sp[idx, idx])
                minor = ring_det(M_z_ring)
                van = R_x.one
                for a in range(n):
                    for b in range(a + 1, n):
                        diff_ab = R_x.from_expr(xs[a] - xs[b])
                        van *= diff_ab * diff_ab
                assert prod_d * minor * minor == van, "k=0 minor mismatch at n=5"
            else:
                # (5, 1): symbolic H(z) == M_z^T D M_z already verified; verify full CB minor sum at 3 rational points
                H_z = sp.expand(H_x.subs(subs_z, simultaneous=True))
                assert sp.expand(H_z - M_z.T * D_sp * M_z).is_zero_matrix
                for trial in range(3):
                    pts = {xs[i]: sp.Rational(i * (trial + 1) - 3, trial + 2) for i in range(n)}
                    Pk_num = Pk_x.subs(pts)
                    Dk_num = sp.Rational(sylvester_discriminant(Pk_num, t, r))
                    M_num = M_z.subs(pts)
                    cb_num = sp.Rational(0)
                    lc_pow = lc ** (r - 1)
                    for I in combinations(range(N), r):
                        prod_d = sp.Rational(1)
                        for idx in I:
                            prod_d *= D_sp[idx, idx]
                        minor_num = sp.Rational(M_num[list(I), :].det())
                        cb_num += prod_d * (lc_pow * minor_num) ** 2
                    assert cb_num == Dk_num, f"Numeric CB mismatch at (5,1) trial {trial}"
            print(f"    symbolic (n={n}, k={k}): PASS", flush=True)

    # Exact rational checks on open/higher cases: (7,2), (7,3), (8,2), (8,3), (8,4), (9,2), (9,3), (9,4)
    # Plus full Cauchy-Binet minor sum on n=6, k=2 (r=4, N=20, binom(20,4)=4845 minors)
    def frac_det(mat: list[list[Fraction]]) -> Fraction:
        m = len(mat)
        A = [row[:] for row in mat]
        det = Fraction(1)
        for col in range(m):
            piv = None
            for row in range(col, m):
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
            for row in range(col + 1, m):
                if A[row][col] != 0:
                    fac = A[row][col] / pv
                    for k2 in range(col, m):
                        A[row][k2] -= fac * A[col][k2]
        return det

    def sp_mat_to_frac(M: sp.Matrix) -> list[list[Fraction]]:
        return [
            [Fraction(int(M[i, j].p), int(M[i, j].q)) for j in range(M.cols)]
            for i in range(M.rows)
        ]

    open_cases = [
        (6, 2, [Fraction(-3, 2), Fraction(-1, 3), Fraction(0), Fraction(2, 5), Fraction(1), Fraction(7, 4)]),
        (7, 2, [Fraction(-5, 2), Fraction(-1), Fraction(-1, 4), Fraction(1, 3), Fraction(3, 2), Fraction(2), Fraction(11, 3)]),
        (7, 3, [Fraction(-2), Fraction(-3, 4), Fraction(0), Fraction(1, 2), Fraction(4, 3), Fraction(5, 2), Fraction(4)]),
        (8, 2, [Fraction(-4), Fraction(-2), Fraction(-1, 2), Fraction(0), Fraction(1, 3), Fraction(1), Fraction(5, 2), Fraction(7, 2)]),
        (8, 3, [Fraction(-3), Fraction(-3, 2), Fraction(-1, 3), Fraction(1, 4), Fraction(1), Fraction(2), Fraction(3), Fraction(9, 2)]),
        (8, 4, [Fraction(-5), Fraction(-2), Fraction(-1), Fraction(0), Fraction(1, 2), Fraction(3, 2), Fraction(3), Fraction(5)]),
        (9, 2, [Fraction(-4), Fraction(-5, 2), Fraction(-1), Fraction(-1, 3), Fraction(0), Fraction(1, 2), Fraction(3, 2), Fraction(3), Fraction(5)]),
        (9, 3, [Fraction(-3), Fraction(-2), Fraction(-1, 2), Fraction(0), Fraction(1, 4), Fraction(1), Fraction(2), Fraction(7, 2), Fraction(6)]),
        (9, 4, [Fraction(-5), Fraction(-3), Fraction(-1), Fraction(-1, 2), Fraction(1, 3), Fraction(1), Fraction(5, 2), Fraction(4), Fraction(7)]),
    ]
    for n, k, x_vals in open_cases:
        r = n - k
        subsets, W = exact_W_matrix(n, r)
        L0, D = exact_ldlt(W)
        N = len(subsets)

        coeffs_x, C_x_sp = build_C_and_J_numeric(x_vals, r, subsets)
        H_x = sp_mat_to_frac(hermite_matrix_from_monic(coeffs_x))
        T_inv_x = sp_mat_to_frac(t_matrix_from_monic(coeffs_x).inv())
        C_x = sp_mat_to_frac(C_x_sp)

        # M_x = L0^T * C_x * T_inv_x^T
        CT = [
            [sum(C_x[i][a] * T_inv_x[j][a] for a in range(r)) for j in range(r)]
            for i in range(N)
        ]
        M_x = [
            [sum(L0[a][i] * CT[a][j] for a in range(i, N)) for j in range(r)]
            for i in range(N)
        ]
        for i in range(r):
            for j in range(r):
                val = sum(M_x[a][i] * D[a] * M_x[a][j] for a in range(N))
                assert val == H_x[i][j], f"H_x SOS mismatch at ({n},{k})"

        # Check explicit rank-1 sum at x_vals for n <= 8
        if n <= 8:
            gammas = [exact_gamma(n, s) for s in range(n)]
            scale = Fraction(r, comb(n, r) * comb(n, r - 1))
            H_rank1 = [[Fraction(0)] * r for _ in range(r)]
            # TCt[i][u] = sum_a T_inv_x[i][a] * C_x[u][a] = CT[u][i]
            for z_idx in range(1, n + 1):
                others = [el for el in range(1, n + 1) if el != z_idx]
                for mask in range(1 << (n - 1)):
                    S_set = {others[b] for b in range(n - 1) if (mask >> b) & 1}
                    g = gammas[len(S_set)]
                    w = [Fraction(0)] * r
                    for u_idx, U in enumerate(subsets):
                        if z_idx not in U:
                            sgn = -1 if (len(S_set & set(U)) & 1) else 1
                            row_ct = CT[u_idx]
                            for i in range(r):
                                w[i] += sgn * row_ct[i]
                    for i in range(r):
                        gw = g * w[i]
                        for j in range(i, r):
                            H_rank1[i][j] += gw * w[j]
            for i in range(r):
                for j in range(i, r):
                    assert scale * H_rank1[i][j] == H_x[i][j], f"Rank-1 H_x mismatch at ({n},{k})"

        # Centered coordinates z_vals
        xbar = sum(x_vals) / Fraction(n)
        z_vals = [xi - xbar for xi in x_vals]
        coeffs_z, C_z_sp = build_C_and_J_numeric(z_vals, r, subsets)
        H_z = sp_mat_to_frac(hermite_matrix_from_monic(coeffs_z))
        T_inv_z = sp_mat_to_frac(t_matrix_from_monic(coeffs_z).inv())
        C_z = sp_mat_to_frac(C_z_sp)
        CT_z = [
            [sum(C_z[i][a] * T_inv_z[j][a] for a in range(r)) for j in range(r)]
            for i in range(N)
        ]
        M_z = [
            [sum(L0[a][i] * CT_z[a][j] for a in range(i, N)) for j in range(r)]
            for i in range(N)
        ]
        Gram_z = [
            [sum(M_z[a][i] * D[a] * M_z[a][j] for a in range(N)) for j in range(r)]
            for i in range(r)
        ]
        assert Gram_z == H_z, f"H_z SOS mismatch at ({n},{k})"

        # Compare det(M_z^T D M_z) * (n!/r!)^{2r-2} against direct Sylvester disc(P^{(k)})
        P_num = sp.Integer(1)
        for xv in x_vals:
            P_num *= (t - sp.Rational(xv.numerator, xv.denominator))
        Pk_num = sp.expand(sp.diff(P_num, t, k))
        Dk_sp = sp.Rational(sylvester_discriminant(Pk_num, t, r))
        Dk_direct = Fraction(int(Dk_sp.p), int(Dk_sp.q))
        lc = Fraction(factorial(n), factorial(r))
        Dk_from_M = (lc ** (2 * r - 2)) * frac_det(Gram_z)
        assert Dk_direct == Dk_from_M and Dk_direct > 0, f"Discriminant mismatch at ({n},{k})"

        # Full Cauchy-Binet minor sum for (6, 2)
        if (n, k) == (6, 2):
            cb_sum = Fraction(0)
            lc_pow = lc ** (r - 1)
            for I in combinations(range(N), r):
                prod_d = Fraction(1)
                for idx in I:
                    prod_d *= D[idx]
                minor = frac_det([M_z[idx] for idx in I])
                s_term = lc_pow * minor
                cb_sum += prod_d * s_term * s_term
            assert cb_sum == Dk_direct, "Full Cauchy-Binet failed at (6, 2)"
        print(f"    exact open/higher ({n}, {k}): PASS", flush=True)

    print("  Theorem 1 & Corollary 2: PASS (symbolic 2<=r<=n<=5 + full CB (6,2) + exact open cases up to (9,4))")


def main() -> int:
    check_lemma1()
    check_lemma2()
    check_lemma3()
    check_lemma4()
    check_theorem1_and_corollary2()
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
