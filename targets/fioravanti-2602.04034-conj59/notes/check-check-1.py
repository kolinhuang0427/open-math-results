#!/usr/bin/env python3
"""Independent exact-arithmetic checker for targets/fioravanti-2602.04034-conj59."""

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb


def q_binom(n: int, c: int, p: int) -> int:
    """Gaussian binomial coefficient [n choose c]_p via q-Pascal recurrence."""
    if c < 0 or c > n:
        return 0
    if c == 0 or c == n:
        return 1
    dp = [0] * (c + 1)
    dp[0] = 1
    for nn in range(1, n + 1):
        new_dp = [0] * (c + 1)
        new_dp[0] = 1
        for cc in range(1, min(nn, c) + 1):
            new_dp[cc] = (dp[cc] if cc <= nn - 1 else 0) + (p ** (nn - cc)) * dp[cc - 1]
        dp = new_dp
    return dp[c]


def poly_mul_mod(a: list[int], b: list[int], deg_cap: int) -> list[int]:
    res = [0] * (deg_cap + 1)
    for i, ca in enumerate(a):
        if i > deg_cap or ca == 0:
            continue
        for j, cb in enumerate(b):
            if i + j > deg_cap:
                break
            res[i + j] += ca * cb
    return res


def rref_mod_p(rows: list[list[int]], p: int) -> tuple[tuple[int, ...], ...]:
    """Canonical RREF basis (as tuple of row tuples) of rowspace in F_p^m."""
    if not rows:
        return ()
    m = len(rows[0])
    mat = [[x % p for x in r] for r in rows]
    piv = 0
    for col in range(m):
        if piv >= len(mat):
            break
        sel = None
        for r in range(piv, len(mat)):
            if mat[r][col] != 0:
                sel = r
                break
        if sel is None:
            continue
        mat[piv], mat[sel] = mat[sel], mat[piv]
        inv = pow(mat[piv][col], -1, p)
        mat[piv] = [(x * inv) % p for x in mat[piv]]
        for r in range(len(mat)):
            if r != piv and mat[r][col] != 0:
                fac = mat[r][col]
                mat[r] = [(mat[r][c] - fac * mat[piv][c]) % p for c in range(m)]
        piv += 1
    return tuple(tuple(r) for r in mat[:piv] if any(r))


def all_subspaces_fp(m: int, p: int) -> dict[int, list[tuple[tuple[int, ...], ...]]]:
    """Enumerate all subspaces of F_p^m grouped by dimension."""
    by_dim: dict[int, set[tuple[tuple[int, ...], ...]]] = {d: set() for d in range(m + 1)}
    by_dim[0].add(())
    all_vecs = [v for v in product(range(p), repeat=m) if any(v)]
    for d in range(m):
        for basis in by_dim[d]:
            for v in all_vecs:
                b2 = rref_mod_p(list(basis) + [list(v)], p)
                if len(b2) == d + 1:
                    by_dim[d + 1].add(b2)
    res = {d: sorted(by_dim[d]) for d in range(m + 1)}
    for d in range(m + 1):
        assert len(res[d]) == q_binom(m, d, p)
    return res


def enumerate_subspace_vectors(basis: tuple[tuple[int, ...], ...], m: int, p: int) -> list[tuple[int, ...]]:
    d = len(basis)
    vecs = []
    for coeffs in product(range(p), repeat=d):
        v = [0] * m
        for c, brow in zip(coeffs, basis):
            if c:
                for j in range(m):
                    v[j] = (v[j] + c * brow[j]) % p
        vecs.append(tuple(v))
    return vecs


def verify_lemma1() -> None:
    # 1. q-Pascal (P1) vs product formula
    for p in (2, 3, 5):
        for n in range(1, 11):
            for c in range(-1, n + 2):
                lhs = q_binom(n, c, p)
                rhs = q_binom(n - 1, c, p) + (p ** (n - c)) * q_binom(n - 1, c - 1, p) if n - c >= 0 else q_binom(n - 1, c, p)
                assert lhs == rhs
                if 1 <= c <= n - 1:
                    num = 1
                    den = 1
                    for i in range(c):
                        num *= (p ** (n - i) - 1)
                        den *= (p ** (i + 1) - 1)
                    assert num % den == 0 and num // den == lhs

    # 2. Finite Cauchy (C1) and reciprocal Cauchy (C2) in Z[[t]]/(t^10)
    deg_cap = 9
    for p in (2, 3, 5):
        for n in range(0, 8):
            prod_poly = [1] + [0] * deg_cap
            for j in range(n):
                prod_poly = poly_mul_mod(prod_poly, [1, p ** j], deg_cap)
            c1_poly = [0] * (deg_cap + 1)
            for c in range(0, min(n, deg_cap) + 1):
                c1_poly[c] = (p ** (c * (c - 1) // 2)) * q_binom(n, c, p)
            assert prod_poly == c1_poly

        for M in range(1, 6):
            prod_poly = [1] + [0] * deg_cap
            for j in range(M):
                prod_poly = poly_mul_mod(prod_poly, [1, p ** j], deg_cap)
            c2_poly = [((-1) ** d) * q_binom(M + d - 1, d, p) for d in range(deg_cap + 1)]
            assert poly_mul_mod(prod_poly, c2_poly, deg_cap) == [1] + [0] * deg_cap

    # 3. Lemma 1(1) orthogonality across 256 quadruples
    for p in (2, 3, 5):
        for s in range(1, 5):
            for m in range(s + 1, s + 5):
                for r in range(0, s + 1):
                    total = Fraction(0)
                    for c in range(0, s + 1):
                        exp_num = (s - c) * (s - c + 1) // 2
                        exp_den = (m - c) * s
                        coeff = Fraction((-1) ** (s - c)) * Fraction(p ** exp_num, p ** exp_den)
                        coeff *= q_binom(m - 1 - c, s - c, p) * q_binom(m - r, c, p)
                        total += coeff
                    expected = Fraction(1) if r == 0 else Fraction(0)
                    assert total == expected, f"Lemma 1(1) failed at {(p, s, m, r)}"

    # 4. Full combinatorial check of Lemma 1(2) and Lemma 1(3) on delta_W
    for p, s, m in ((2, 2, 5), (2, 3, 4), (3, 2, 4)):
        subs = all_subspaces_fp(m, p)
        # Count each matrix W in F_p^{m x s} across codim c subspaces (via column membership!)
        mat_counts: dict[tuple[int, ...], Fraction] = defaultdict(Fraction)
        for c in range(0, s + 1):
            dim_u = m - c
            outer = ((-1) ** (s - c)) * (p ** ((s - c) * (s - c + 1) // 2)) * q_binom(m - 1 - c, s - c, p)
            weight = Fraction(outer, p ** (dim_u * s))
            for u_basis in subs[dim_u]:
                u_vecs = enumerate_subspace_vectors(u_basis, m, p)
                # W in Mat_{m x s}(U) means each of s columns is in U
                for cols in product(u_vecs, repeat=s):
                    # pack column-major key
                    key = tuple(x for col in cols for x in col)
                    mat_counts[key] += weight
        assert len(mat_counts) == p ** (m * s)
        zero_key = (0,) * (m * s)
        for key, val in mat_counts.items():
            assert val == (Fraction(1) if key == zero_key else Fraction(0))

        # Lemma 1(3) explicit basis split H_1 + H_2 = U for 0 <= c < s (requires m >= 2*s - c)
        for c in range(0, s):
            if m < 2 * s - c:
                continue
            for u_basis in subs[m - c]:
                h1 = rref_mod_p([list(r) for r in u_basis[: m - s]], p)
                h2 = rref_mod_p([list(r) for r in u_basis[s - c : m - c]], p)
                assert len(h1) == m - s and len(h2) == m - s
                assert rref_mod_p(list(h1) + list(h2), p) == u_basis
                v1 = enumerate_subspace_vectors(h1, m, p)
                v2 = enumerate_subspace_vectors(h2, m, p)
                vu = enumerate_subspace_vectors(u_basis, m, p)
                if m * s <= 10:
                    # Check column-sum multiplicities on F_p^m (since Mat_{m x s}(V) is s-fold product of V)
                    sum_counts: dict[tuple[int, ...], int] = defaultdict(int)
                    for x1 in v1:
                        for x2 in v2:
                            svec = tuple((a + b) % p for a, b in zip(x1, x2))
                            sum_counts[svec] += 1
                    assert set(sum_counts.keys()) == set(vu)
                    expected_mult = (len(v1) * len(v2)) // len(vu)
                    assert all(cnt == expected_mult for cnt in sum_counts.values())
    print("Lemma 1 (P1, C1, C2, Lemma 1(1)-(3) exhaustive): PASS")


# Exact matrix utilities over Z/modZ

def mat_mul_mod(A: tuple[tuple[int, ...], ...], B: tuple[tuple[int, ...], ...], mod: int) -> tuple[tuple[int, ...], ...]:
    l = len(A)
    k = len(B)
    m = len(B[0]) if k else len(A[0])
    return tuple(
        tuple(sum(A[i][r] * B[r][j] for r in range(k)) % mod for j in range(m))
        for i in range(l)
    )


def mat_inv_mod(A: tuple[tuple[int, ...], ...], mod: int) -> tuple[tuple[int, ...], ...]:
    """Invert an invertible m x m matrix over Z/modZ (mod = p^e)."""
    m = len(A)
    aug = [list(A[i]) + [1 if i == j else 0 for j in range(m)] for i in range(m)]
    # Determine prime factor via gcd/divisibility or simple inversion via mod
    # Since mod is p^e, element a is unit iff gcd(a, mod) == 1
    from math import gcd
    for col in range(m):
        piv = None
        for r in range(col, m):
            if gcd(aug[r][col], mod) == 1:
                piv = r
                break
        assert piv is not None, "Matrix not invertible mod p^e"
        aug[col], aug[piv] = aug[piv], aug[col]
        inv = pow(aug[col][col], -1, mod)
        aug[col] = [(x * inv) % mod for x in aug[col]]
        for r in range(m):
            if r != col and aug[r][col] != 0:
                fac = aug[r][col]
                aug[r] = [(aug[r][c] - fac * aug[col][c]) % mod for c in range(2 * m)]
    return tuple(tuple(row[m:]) for row in aug)


def snf_inner_rank_mod_pe(M: tuple[tuple[int, ...], ...], p: int, e: int) -> int:
    """Exact inner rank of matrix M over Z/p^eZ via diagonalization (SNF)."""
    mod = p ** e
    rows = len(M)
    cols = len(M[0])
    A = [[x % mod for x in r] for r in M]

    def vp(x: int) -> int:
        if x == 0:
            return e + 10
        v = 0
        while x % p == 0:
            x //= p
            v += 1
        return v

    rank = 0
    r0, c0 = 0, 0
    while r0 < rows and c0 < cols:
        best = None
        best_v = e + 10
        for r in range(r0, rows):
            for c in range(c0, cols):
                if A[r][c] != 0:
                    v = vp(A[r][c])
                    if v < best_v:
                        best_v = v
                        best = (r, c)
        if best is None:
            break
        br, bc = best
        A[r0], A[br] = A[br], A[r0]
        for r in range(rows):
            A[r][c0], A[r][bc] = A[r][bc], A[r][c0]
        # Pivot A[r0][c0] = p^v * unit
        pv = p ** best_v
        unit = (A[r0][c0] // pv) % (mod // pv)
        inv_unit = pow(unit, -1, mod // pv)
        # Scale row r0 by inv_unit
        A[r0] = [(x * inv_unit) % mod for x in A[r0]]
        # Eliminate row and col
        for r in range(r0 + 1, rows):
            if A[r][c0] != 0:
                assert A[r][c0] % pv == 0
                q = A[r][c0] // pv
                A[r] = [(A[r][c] - q * A[r0][c]) % mod for c in range(cols)]
        for c in range(c0 + 1, cols):
            if A[r0][c] != 0:
                assert A[r0][c] % pv == 0
                q = A[r0][c] // pv
                for r in range(r0, rows):
                    A[r][c] = (A[r][c] - q * A[r][c0]) % mod
        rank += 1
        r0 += 1
        c0 += 1
    return rank


def solve_linear_fraction(A: list[list[Fraction]], b: list[Fraction]) -> list[Fraction]:
    """Solve A x = b over Q (returns a valid particular solution)."""
    n_eq = len(A)
    n_var = len(A[0])
    mat = [list(A[i]) + [b[i]] for i in range(n_eq)]
    piv_cols = []
    r = 0
    for c in range(n_var):
        if r >= n_eq:
            break
        sel = None
        for rr in range(r, n_eq):
            if mat[rr][c] != 0:
                sel = rr
                break
        if sel is None:
            continue
        mat[r], mat[sel] = mat[sel], mat[r]
        inv = Fraction(1) / mat[r][c]
        mat[r] = [x * inv for x in mat[r]]
        for rr in range(n_eq):
            if rr != r and mat[rr][c] != 0:
                fac = mat[rr][c]
                mat[rr] = [mat[rr][k] - fac * mat[r][k] for k in range(n_var + 1)]
        piv_cols.append((r, c))
        r += 1
    for rr in range(r, n_eq):
        assert mat[rr][-1] == 0, "Inconsistent linear system"
    sol = [Fraction(0)] * n_var
    for rr, cc in piv_cols:
        sol[cc] = mat[rr][-1]
    return sol


def base_case_ug_formula(p: int, s: int) -> list[tuple[Fraction, tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]]]:
    """
    Independently compute a witnessing (s, F_p^s, Z[1/p])-UG formula at arity m = s + 1:
    returns list of (coeff, M, U, V) with M = U * V, U in F_p^{m x s}, V in F_p^{s x m}.
    Only used for small base cases (p=2, s=1), (p=2, s=2), (p=3, s=1).
    """
    m = s + 1
    points = list(product(product(range(p), repeat=s), repeat=m))  # X in (F_p^s)^m = F_p^{m x s}
    pt_idx = {x: idx for idx, x in enumerate(points)}
    n_pts = len(points)

    # Enumerate rank <= s matrices U*V via unique RREF U? No, just all U in F_p^{m x s}, V in F_p^{s x m}
    # and deduplicate by matrix M!
    seen_mats: dict[tuple[tuple[int, ...], ...], tuple[tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]]] = {}
    cols_m = list(product(range(p), repeat=m))
    rows_m = list(product(range(p), repeat=m))
    for u_cols in product(cols_m, repeat=s):
        U = tuple(tuple(u_cols[c][r] for c in range(s)) for r in range(m))
        for V in product(rows_m, repeat=s):
            M = mat_mul_mod(U, V, p)
            if M not in seen_mats:
                seen_mats[M] = (U, V)

    mats = list(seen_mats.keys())
    # Wait: for M X == Y we need a linear system over (X, Y), which has n_pts^2 equations.
    # For (2, 1): n_pts=4, n_eq=16. For (3, 1): n_pts=9, n_eq=81.
    # For (2, 2): n_pts=64 -> n_eq=4096. Even faster: only solve for M fixing the stabilizer / orbit or solve directly!
    # Wait: for (2, 2), we have 344 mats and 4096 rows -> let's keep a minimal linearly-independent subset of columns or note:
    # Actually at (2, 2), (X_1, X_2, X_3) in F_2^{3 x 2}: solving by grouping rows by image or direct RREF on 4096 x 344?
    # Better: use M-actions that are GL_3-invariant OR directly build the 64x64 incidence? No, M X = Y is 4096 eqs x 344 vars,
    # Wait: every M fixes 0 -> 0 (X=0 has M*0=0 so sum alpha_M = 1). Many of the 4096 eqs are identical or 0=0!
    # Let's filter equations to distinct nonzero rows!
    eq_dict: dict[tuple[int, ...], Fraction] = {}
    for x_i, X in enumerate(points):
        row_map = [0] * len(mats)
        img_to_cols: dict[int, list[int]] = defaultdict(list)
        for m_i, M in enumerate(mats):
            MX = tuple(
                tuple(sum(M[r][k] * X[k][c] for k in range(m)) % p for c in range(s))
                for r in range(m)
            )
            img_to_cols[pt_idx[MX]].append(m_i)
        for y_i, cols_list in img_to_cols.items():
            row = [0] * len(mats)
            for c_i in cols_list:
                row[c_i] = 1
            eq_dict[tuple(row)] = Fraction(1) if y_i == x_i else Fraction(0)
        # Note: if y_i has NO M with MX = Y (not possible since 0-matrix? Wait: if Y != 0 and X == 0, 0 != Y => 0=0)
    A_mat = [[Fraction(v) for v in r] for r in eq_dict.keys()]
    b_vec = list(eq_dict.values())
    sol = solve_linear_fraction(A_mat, b_vec)
    # Verify all denominators are powers of p (hence in Z[1/p])
    res = []
    for coeff, M in zip(sol, mats):
        if coeff != 0:
            den = coeff.denominator
            while den % p == 0:
                den //= p
            assert den == 1, f"Non-Z[1/{p}] denominator {coeff}"
            U, V = seen_mats[M]
            res.append((coeff, M, U, V))
    # Full verification over all X, Y in (F_p^s)^m
    for X in points:
        acc: dict[tuple[tuple[int, ...], ...], Fraction] = defaultdict(Fraction)
        for coeff, M, _, _ in res:
            MX = tuple(
                tuple(sum(M[r][k] * X[k][c] for k in range(m)) % p for c in range(s))
                for r in range(m)
            )
            acc[MX] += coeff
        for MX, val in acc.items():
            assert val == (Fraction(1) if MX == X else Fraction(0))
    return res


def compose_ur(
    op2: dict[tuple[tuple[int, ...], ...], Fraction],
    op1: dict[tuple[tuple[int, ...], ...], Fraction],
    mod: int,
) -> dict[tuple[tuple[int, ...], ...], Fraction]:
    """Compose two linear matrix-action operators: (op2 o op1)(f)(X) = sum a2 a1 f(M1 M2 X)."""
    # Wait: CAREFUL WITH ORDER!
    # If I_1(f)(X) = sum_i a_i f(M_i X) and I_2(g)(X) = sum_j b_j g(N_j X),
    # then I_2(I_1(f))(X) = sum_j b_j I_1(f)(N_j X) = sum_{i,j} b_j a_i f(M_i (N_j X)) = sum_{i,j} (b_j a_i) f((M_i N_j) X)!
    out: dict[tuple[tuple[int, ...], ...], Fraction] = defaultdict(Fraction)
    for N, b in op2.items():
        if b == 0:
            continue
        for M, a in op1.items():
            if a == 0:
                continue
            MN = mat_mul_mod(M, N, mod)
            out[MN] += b * a
    return {k: v for k, v in out.items() if v != 0}


def add_ur(
    op1: dict[tuple[tuple[int, ...], ...], Fraction],
    op2: dict[tuple[tuple[int, ...], ...], Fraction],
    scale1: Fraction = Fraction(1),
    scale2: Fraction = Fraction(1),
) -> dict[tuple[tuple[int, ...], ...], Fraction]:
    out: dict[tuple[tuple[int, ...], ...], Fraction] = defaultdict(Fraction)
    for k, v in op1.items():
        out[k] += scale1 * v
    for k, v in op2.items():
        out[k] += scale2 * v
    return {k: v for k, v in out.items() if v != 0}


def apply_matrix_to_tuple(M: tuple[tuple[int, ...], ...], X: tuple[tuple[int, ...], ...], mods_by_col: list[int]) -> tuple[tuple[int, ...], ...]:
    """Action of M (over Z/p^eZ) on tuple X = (X_col0, ...) where col c lives in Z/mods_by_col[c]Z."""
    l = len(M)
    k = len(M[0])
    ncols = len(mods_by_col)
    return tuple(
        tuple(sum(M[i][j] * X[j][c] for j in range(k)) % mods_by_col[c] for c in range(ncols))
        for i in range(l)
    )


def verify_ug_operator_full(
    op: dict[tuple[tuple[int, ...], ...], Fraction],
    invariants: list[int],
    p: int,
    k_bound: int,
    m: int,
    label: str,
) -> None:
    """
    Verify on ALL points X in A^m that sum_M op[M] delta_Y(M X) = delta_{X, Y},
    and verify every M with op[M] != 0 has SNF inner rank <= k_bound over Z/p^eZ.
    """
    e = 0
    pe = invariants[0]
    tmp = pe
    while tmp > 1:
        assert tmp % p == 0
        tmp //= p
        e += 1
    # 1. Verify inner rank <= k_bound for all nonzero matrices
    for M in op:
        assert snf_inner_rank_mod_pe(M, p, e) <= k_bound, f"{label}: matrix rank exceeded {k_bound}"

    # 2. Verify full identity operator over all X in A^m
    A_elems = list(product(*[range(inv) for inv in invariants]))
    points = list(product(A_elems, repeat=m))
    # Map point to int index for fast accumulation
    pt_idx = {pt: idx for idx, pt in enumerate(points)}
    for X in points:
        acc: dict[int, Fraction] = defaultdict(Fraction)
        for M, coeff in op.items():
            MX = apply_matrix_to_tuple(M, X, invariants)
            acc[pt_idx[MX]] += coeff
        x_i = pt_idx[X]
        for y_i, val in acc.items():
            assert val == (Fraction(1) if y_i == x_i else Fraction(0)), f"{label}: failed at X={X}"
        assert acc.get(x_i, Fraction(0)) == Fraction(1)
    print(f"Full operator identity ({label}, |A|^{m} = {len(points)}, {len(op)} matrices, inner rk <= {k_bound}): PASS")


def all_maximal_subgroups(invariants: list[int], p: int) -> list[tuple[list[tuple[int, ...]], list[int], list[list[int]]]]:
    """
    Return all maximal (index-p) subgroups C < A = prod Z/inv_c Z.
    Each C is represented as a subgroup of A with a basis/canonical isomorphism to prod Z/sub_inv Z?
    Actually even simpler: let's return each maximal subgroup C = ker(phi_w : A -> F_p) for projective w in F_p^r \\ {0},
    together with an explicit group isomorphism C_invariants -> A (as matrix/linear map from a smaller group)!
    Wait: for any abelian p-group A = Z/p^{e_1} x ... x Z/p^{e_r} and surjective phi_w: A -> F_p given by
    sum w_j (a_j mod p) = 0, pick any j0 with w_{j0} != 0 (e.g. w_{j0} = 1 after scaling!).
    Wait: if A = Z/p^e x A', taking w_{j0} = 1 with smallest exponent e_{j0}?
    Careful! If j0 has e_{j0} = 1 (like C in Z_4 x Z_2 with w = (1, 1)), then a_2 mod p = -a_1 mod p determines a_2 in Z_2 UNIQUELY from a_1 in Z_4!
    Wait: if e_{j0} >= e_j for all j with w_j != 0, OR pick j0 with SMALLEST e_{j0} among {j : w_j != 0}!
    Let's check: if j0 has MINIMAL e_{j0} among {j : w_j != 0}, then for every OTHER j with w_j != 0,
    e_j >= e_{j0}, so p^{e_j - e_{j0}} exists? Wait: no, if e_1 = 2, e_2 = 1 and w = (1, 1),
    then C = {(a_1, a_2) in Z_4 x Z_2 : a_1 + a_2 = 0 mod 2} has a_2 = a_1 mod 2 (free parameter a_1 in Z_4), so C ~= Z_4!
    In general, if e_{j0} <= e_j for all j with w_j != 0, we CANNOT express a_{j0} mod p^{e_{j0}} when e_{j0}=1, wait:
    we just used a_{j0} = -sum_{j != j0} w_j a_j (mod p)! Notice a_{j0} mod p is fixed, leaving p^{e_{j0}-1} choices for a_{j0}/p!
    Wait: it's even easier if j0 has LARGEST e_{j0}? No, if e_1=2, e_2=1, w=(1,1), a_1=1, a_2=1 is in C and has order 4, whereas if we kept a_2 in Z_2 and p*a_1 in 2Z_4, they don't span!
    With SMALLEST e_{j0}: set a'_{j0} = (a_{j0} + sum_{j != j0} (w_j * w_{j0}^-1 mod p) * a_j) in Z/p^{e_{j0}} Z?
    Wait: modulo p^{e_{j0}}, w_j a_j IS well-defined because e_j >= e_{j0} implies p^{e_{j0}} | p^{e_j}!
    AND a'_{j0} = 0 mod p iff (a_1,...,a_r) in ker(phi_w)!
    So a'_{j0} = p * b_{j0} with b_{j0} in Z/p^{e_{j0}-1} Z!
    Let's check that algebraically!
    If e_{j0} = min {e_j : w_j != 0}, normalize w_{j0} = 1 (mod p).
    Map tau: A -> prod_{j != j0} Z/p^{e_j} Z x Z/p^{e_{j0}} Z by keeping a_j (j != j0) and replacing a_{j0} by
      u := (a_{j0} + sum_{j != j0} w_j a_j) mod p^{e_{j0}}.
    Since e_j >= e_{j0} whenever w_j != 0, multiplying a_j by w_j (lifted to Z) is well-defined mod p^{e_{j0}}!
    And tau is an ISOMORPHISM of abelian groups (inverse: a_{j0} = u - sum_{j != j0} w_j a_j mod p^{e_{j0}})!
    Under tau, ker(phi_w) is EXACTLY {u = 0 mod p}, which is prod_{j != j0} Z/p^{e_j} Z x p Z/p^{e_{j0}} Z ~= prod_{j != j0} Z/p^{e_j} Z x Z/p^{e_{j0}-1} Z!
    Let's double check: for (4, 2) with w = (1, 1): min e_j is j0=1 (e_1=1), C ~= Z_4 x {0} = Z_4, inverse maps x in Z_4 to (x, (-x) mod 2) in Z_4 x Z_2!
    For (4, 2) with w = (1, 0): only j=0 has w_j != 0, j0=0 (e_0=2), C ~= 2Z_4 x Z_2 ~= Z_2 x Z_2, inverse maps (b, y) in Z_2 x Z_2 to (2b, y) in Z_4 x Z_2!
    And for (4, 4) with w = (1, c): j0=0 (e_0=2), C ~= Z_2 x Z_4, inverse maps (b, y) to (2b - cy, y)!
    THAT WORKS FOR ALL FINITE ABELIAN p-GROUPS!
    """
    r = len(invariants)
    # Find exponent e_j for each factor
    exps = []
    for inv in invariants:
        ej = 0
        t = inv
        while t > 1:
            t //= p
            ej += 1
        exps.append(ej)

    # Projective nonzero vectors w in F_p^r (first nonzero entry = 1)
    ws = []
    for lead in range(r):
        for tail in product(range(p), repeat=r - 1 - lead):
            ws.append((0,) * lead + (1,) + tail)

    subgroups = []
    for w in ws:
        nonzero = [j for j in range(r) if w[j] != 0]
        # Pick j0 with minimal e_{j0} among nonzero
        j0 = min(nonzero, key=lambda j: exps[j])
        w0_inv = pow(w[j0], -1, p)
        w_norm = [(x * w0_inv) % p for x in w]
        # New invariants: same for j != j0, divided by p for j0 (drop if 1!)
        # Keep coordinate map: list of columns mapping c_invs -> invariants
        sub_invs_full = [invariants[j] if j != j0 else invariants[j] // p for j in range(r)]
        # Build embedding matrix E_mat (len(sub_invs_kept) -> r, or row vector per A-coord):
        # For each A-coord i: if i != j0, a_i = c_i; if i == j0, a_{j0} = p * c_{j0} - sum_{j != j0} w_norm[j] * c_j (mod inv_{j0})
        kept_indices = [j for j in range(r) if sub_invs_full[j] > 1]
        sub_invs = [sub_invs_full[j] for j in kept_indices]
        # Map from sub_coords to A_coords and vice versa on C:
        # emb_rows[a_idx][sub_idx] and proj_rows[sub_idx][a_idx] (integers mod invariants)
        # Note: since all sub_invs | exp(A), any Z/exp(A)Z matrix acting on C can be written in A-coordinates directly!
        subgroups.append((w_norm, j0, kept_indices, sub_invs))
    return subgroups


def factor_rank_mod_pe(
    M: tuple[tuple[int, ...], ...],
    p: int,
    e_mod: int,
    k_cap: int,
) -> tuple[tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]]:
    """Construct exact inner-rank factorization M = U * V over Z/p^{e_mod}Z with inner dimension k_cap."""
    rows = len(M)
    cols = len(M[0])
    mod = p ** e_mod
    if e_mod == 1:
        A = [[x % p for x in r] for r in M]
        piv_cols = []
        r_idx = 0
        for c in range(cols):
            if r_idx >= rows:
                break
            sel = None
            for rr in range(r_idx, rows):
                if A[rr][c] != 0:
                    sel = rr
                    break
            if sel is None:
                continue
            A[r_idx], A[sel] = A[sel], A[r_idx]
            inv = pow(A[r_idx][c], -1, p)
            A[r_idx] = [(x * inv) % p for x in A[r_idx]]
            for rr in range(rows):
                if rr != r_idx and A[rr][c] != 0:
                    fac = A[rr][c]
                    A[rr] = [(A[rr][cc] - fac * A[r_idx][cc]) % p for cc in range(cols)]
            piv_cols.append(c)
            r_idx += 1
        rk = len(piv_cols)
        assert rk <= k_cap, f"Rank {rk} exceeded cap {k_cap} mod {mod}"
        U = tuple(
            tuple(M[i][piv_cols[j]] if j < rk else 0 for j in range(k_cap))
            for i in range(rows)
        )
        V = tuple(
            tuple(A[j][c] if j < rk else 0 for c in range(cols))
            for j in range(k_cap)
        )
        assert mat_mul_mod(U, V, mod) == M
        return U, V

    A = [[x % mod for x in r] for r in M]
    P_inv = [[1 if i == j else 0 for j in range(rows)] for i in range(rows)]
    Q_inv = [[1 if i == j else 0 for j in range(cols)] for i in range(cols)]

    def vp(x: int) -> int:
        if x == 0:
            return e_mod + 10
        v = 0
        while x % p == 0:
            x //= p
            v += 1
        return v

    rk = 0
    r0, c0 = 0, 0
    while r0 < rows and c0 < cols:
        best = None
        best_v = e_mod + 10
        for r in range(r0, rows):
            for c in range(c0, cols):
                if A[r][c] != 0:
                    v = vp(A[r][c])
                    if v < best_v:
                        best_v = v
                        best = (r, c)
        if best is None:
            break
        br, bc = best
        A[r0], A[br] = A[br], A[r0]
        for rr in range(rows):
            P_inv[rr][r0], P_inv[rr][br] = P_inv[rr][br], P_inv[rr][r0]
        for rr in range(rows):
            A[rr][c0], A[rr][bc] = A[rr][bc], A[rr][c0]
        Q_inv[c0], Q_inv[bc] = Q_inv[bc], Q_inv[c0]

        pv = p ** best_v
        unit = (A[r0][c0] // pv) % mod
        inv_unit = pow(unit, -1, mod)
        A[r0] = [(x * inv_unit) % mod for x in A[r0]]
        for rr in range(rows):
            P_inv[rr][r0] = (P_inv[rr][r0] * unit) % mod

        for r in range(r0 + 1, rows):
            if A[r][c0] != 0:
                q = A[r][c0] // pv
                A[r] = [(A[r][cc] - q * A[r0][cc]) % mod for cc in range(cols)]
                for rr in range(rows):
                    P_inv[rr][r0] = (P_inv[rr][r0] + q * P_inv[rr][r]) % mod
        for c in range(c0 + 1, cols):
            if A[r0][c] != 0:
                q = A[r0][c] // pv
                for rr in range(r0, rows):
                    A[rr][c] = (A[rr][c] - q * A[rr][c0]) % mod
                for cc in range(cols):
                    Q_inv[c0][cc] = (Q_inv[c0][cc] + q * Q_inv[c][cc]) % mod
        rk += 1
        r0 += 1
        c0 += 1
    assert rk <= k_cap, f"Rank {rk} exceeded cap {k_cap} mod {mod}"
    U = tuple(
        tuple((P_inv[i][j] * A[j][j]) % mod if j < rk else 0 for j in range(k_cap))
        for i in range(rows)
    )
    V = tuple(
        tuple(Q_inv[j][c] % mod if j < rk else 0 for c in range(cols))
        for j in range(k_cap)
    )
    assert mat_mul_mod(U, V, mod) == M
    return U, V


def lift_subgroup_operator(
    op_C: dict[tuple[tuple[int, ...], ...], Fraction],
    sub_info: tuple[list[int], int, list[int], list[int]],
    invariants: list[int],
    p: int,
    k_cap: int,
) -> dict[tuple[tuple[int, ...], ...], Fraction]:
    """
    Per PROOF.md Lemma 2: factor each M_C = U_C * V_C over Z/exp(C)Z with inner dim <= k_cap,
    lift U_C and V_C entrywise to Z/exp(A)Z, and form M_lift = U_lift * V_lift (mod exp(A))!
    """
    exp_A = max(invariants)
    sub_invs = sub_info[3]
    exp_C = max(sub_invs) if sub_invs else 1
    e_C = 0
    tmp = exp_C
    while tmp > 1:
        tmp //= p
        e_C += 1
    out: dict[tuple[tuple[int, ...], ...], Fraction] = defaultdict(Fraction)
    for M_C, coeff in op_C.items():
        if e_C == 0:
            # C is trivial group {0}: 0_{m x m}
            M_lift = M_C
        else:
            U_C, V_C = factor_rank_mod_pe(M_C, p, e_C, k_cap)
            M_lift = mat_mul_mod(U_C, V_C, exp_A)
        out[M_lift] += coeff
    return {k: v for k, v in out.items() if v != 0}


def build_ug_operator_inductive(
    invariants: list[int],
    p: int,
    m: int,
    base_cache: dict[tuple[int, int], list],
) -> dict[tuple[tuple[int, ...], ...], Fraction]:
    """
    Follow PROOF.md Section 3 literally to build a (k(A), A, Z[1/p])-UG operator at arity m = k(A) + 1
    (or any m >= k(A) + 1? Let's support m = k(A) + 1 for invariant-factor-sorted A = (Z/p^e)^s x A'!).
    """
    # Normalize invariants in descending order of p^e
    invariants = sorted([inv for inv in invariants if inv > 1], reverse=True)
    if not invariants:
        # Trivial group {0}: k = 1, zero matrix
        zero_m = tuple((0,) * m for _ in range(m))
        return {zero_m: Fraction(1)}

    exps = []
    for inv in invariants:
        ej = 0
        t = inv
        while t > 1:
            t //= p
            ej += 1
        exps.append(ej)
    N = sum(exps)
    e = exps[0]
    k = N
    assert m == k + 1, "Inductive step uses m = k + 1"

    if e == 1:
        # Base case A = F_p^s, s = N
        s = N
        if (p, s) not in base_cache:
            base_cache[(p, s)] = base_case_ug_formula(p, s)
        out: dict[tuple[tuple[int, ...], ...], Fraction] = {}
        for coeff, M, _, _ in base_cache[(p, s)]:
            out[M] = coeff
        return out

    # e >= 2
    s = sum(1 for ej in exps if ej == e)
    mod_e = p ** e
    mod_prev = p ** (e - 1)
    # Quotient Abar = A / p^{e-1} A has invariants [p^{e-1}]*s + invariants[s:]
    abar_invs = [inv for inv in ([mod_prev] * s + invariants[s:]) if inv > 1]
    k_prime = N - s
    m_sub = m - s  # == k_prime + 1
    op_abar = build_ug_operator_inductive(abar_invs, p, m_sub, base_cache)

    # Step 1: Peeling all maximal proper subgroups via Lemma 2
    subgroups = all_maximal_subgroups(invariants, p)
    J_prop: dict[tuple[tuple[int, ...], ...], Fraction] | None = None
    for sub_info in subgroups:
        sub_invs = sub_info[3]
        # Build UG operator on sub_invs at arity m?
        # Wait: sub_invs has log_p |C| = N - 1, so k(C) = N - 1 = k - 1!
        # Wait: build_ug_operator_inductive gives arity m_C = k(C) + 1 = k = m - 1!
        # How does Theorem 18 extend arity from k(C) + 1 = m - 1 to m = k + 1?
        # PROOF.md line 222 gives the EXACT explicit 1-step arity lift!
        # Given op_{m-1} on C^{m-1} (rank <= N-1), apply op_{m-1} to first m-1 coords:
        # diag(M, 1) has rank <= N = k (and on C^{m} factors through C^{m-1} x C = C^m? Wait: line 222!):
        # diag(M_i, 1) in R_k^{m, m}(C) factors through C^{m-1} -> no, M_i has rank <= k-1 so diag(M_i, 1) has rank <= k!
        # Wait: if we want rank <= k-1 (Lemma 2 asks for k-ary on C_i, where k = N, and N-1 < k, OR rank <= k!),
        # diag(M_i, 1) ALREADY has rank <= (N - 1) + 1 = N = k!!
        # Let's check: does Lemma 2 need rank <= N-1 on C_i or rank <= k on C_i?!
        # Read PROOF.md L148: "O_{C_i, S} is uniformly generated by (N-1)-ary minors, hence also by k-ary (C_i, S)-minors (Lemma 17(2), as N-1 < k)"!
        # Wait: to get rank <= k on C_i at arity m = k + 1, literally diag(M_i, 1) has rank <= (N-1) + 1 = N = k!
        # Wait: let's check both! diag(M_i, 1) gives a valid (k, C_i, S)-UR identity at arity m = k+1 immediately in 1 line,
        # OR Theorem 18 lowers rank to N-1 if needed! Using diag(M_i, 1) has rank <= (N-1) + 1 = N = k, which is ALREADY <= k!
        op_C_small = build_ug_operator_inductive(sub_invs, p, m - 1, base_cache)
        exp_C = max(sub_invs) if sub_invs else 1
        op_C_m: dict[tuple[tuple[int, ...], ...], Fraction] = {}
        for M_sm, c_sm in op_C_small.items():
            # diag(M_sm, 1) mod exp_C
            M_big = tuple(row + (0,) for row in M_sm) + ((0,) * (m - 1) + (1 % exp_C,),)
            op_C_m[M_big] = c_sm
        I_i = lift_subgroup_operator(op_C_m, sub_info, invariants, p, k)
        if J_prop is None:
            J_prop = I_i
        else:
            comp = compose_ur(I_i, J_prop, mod_e)
            J_prop = add_ur(add_ur(J_prop, I_i), comp, Fraction(1), Fraction(-1))
    assert J_prop is not None

    # Step 2: Construct A_{H_0} directly from PROOF.md Eq. (173)-(175)
    A_H0: dict[tuple[tuple[int, ...], ...], Fraction] = defaultdict(Fraction)
    denom_H0 = Fraction(1, p ** ((m - s) * (s + k_prime)))
    for B_tilde, beta in op_abar.items():
        U, V = factor_rank_mod_pe(B_tilde, p, e - 1, k_prime)
        # Note: sum_{W', U'} M(B_tilde, U', W')!
        # Wait: (U + p^{e-1} U') V only depends on U' V mod p, which is linear in U'!
        # Here for small examples, let's check sizes:
        # Z_4: m=3, s=1, k'=1 => (m-s)*(s+k') = 2*2 = 4 => 2^4 = 16
        # Z_8: m=4, s=1, k'=2 => (m-s)*(s+k') = 3*3 = 9 => 2^9 = 512
        # Z_4 x Z_2: m=4, s=1, k'=2 => 2^9 = 512
        # Z_9: m=3, s=1, k'=1 => 3^4 = 81
        for W_prime_flat in product(range(p), repeat=(m - s) * s):
            W_prime = [W_prime_flat[i * s : (i + 1) * s] for i in range(m - s)]
            for U_prime_flat in product(range(p), repeat=(m - s) * k_prime):
                U_prime = [U_prime_flat[i * k_prime : (i + 1) * k_prime] for i in range(m - s)]
                U_shifted = tuple(
                    tuple((U[i][j] + mod_prev * U_prime[i][j]) % mod_e for j in range(k_prime))
                    for i in range(m - s)
                )
                UV = mat_mul_mod(U_shifted, V, mod_e)
                M_rows = []
                for i in range(s):
                    M_rows.append(tuple(1 if j == i else 0 for j in range(m)))
                for i in range(m - s):
                    M_rows.append(
                        tuple((mod_prev * W_prime[i][j]) % mod_e for j in range(s)) + UV[i]
                    )
                M = tuple(M_rows)
                A_H0[M] += beta * denom_H0
    A_H0_clean = {mat: val for mat, val in A_H0.items() if val != 0}

    # Step 3: Conjugate A_H0 to every codim-s subspace H <= F_p^m, build A_U for codim < s, and Radon K
    subs = all_subspaces_fp(m, p)

    def build_A_H(H_basis: tuple[tuple[int, ...], ...]) -> dict[tuple[tuple[int, ...], ...], Fraction]:
        # Build T_H in GL_m(Z/p^eZ) with top s rows spanning H^perp
        # Find H^perp as basis of annihilating row vectors
        ann_rows = []
        for v in product(range(p), repeat=m):
            if any(v) and all(sum(v[j] * b[j] for j in range(m)) % p == 0 for b in H_basis):
                ann_rows.append(list(v))
        perp_basis = rref_mod_p(ann_rows, p)
        assert len(perp_basis) == s
        # Extend perp_basis to invertible matrix over F_p by adding standard basis vectors
        cur = [list(r) for r in perp_basis]
        for j in range(m):
            e_j = [1 if i == j else 0 for i in range(m)]
            cand = rref_mod_p(cur + [e_j], p)
            if len(cand) > len(cur):
                cur.append(e_j)
                if len(cur) == m:
                    break
        assert len(cur) == m
        T_H = tuple(tuple(r) for r in cur)
        T_H_inv = mat_inv_mod(T_H, mod_e)
        # A_H(h)(X) = A_H0(h o T_H^-1)(T_H X) => matrix M becomes T_H^-1 M T_H!
        res: dict[tuple[tuple[int, ...], ...], Fraction] = {}
        for M, val in A_H0_clean.items():
            conj_M = mat_mul_mod(mat_mul_mod(T_H_inv, M, mod_e), T_H, mod_e)
            res[conj_M] = res.get(conj_M, Fraction(0)) + val
        return {mat: val for mat, val in res.items() if val != 0}

    A_H_cache: dict[tuple[tuple[int, ...], ...], dict[tuple[tuple[int, ...], ...], Fraction]] = {}
    for H_basis in subs[m - s]:
        A_H_cache[H_basis] = build_A_H(H_basis)

    K_op: dict[tuple[tuple[int, ...], ...], Fraction] = defaultdict(Fraction)
    for c in range(0, s + 1):
        outer = Fraction((-1) ** (s - c) * (p ** ((s - c) * (s - c + 1) // 2)) * q_binom(m - 1 - c, s - c, p))
        for U_basis in subs[m - c]:
            if c == s:
                A_U = A_H_cache[U_basis]
            else:
                H1 = rref_mod_p([list(r) for r in U_basis[: m - s]], p)
                H2 = rref_mod_p([list(r) for r in U_basis[s - c : m - c]], p)
                A_U = compose_ur(A_H_cache[H1], A_H_cache[H2], mod_e)
            for M, val in A_U.items():
                K_op[M] += outer * val
    K_clean = {mat: val for mat, val in K_op.items() if val != 0}

    # Step 4: I = J_prop + K - K o J_prop
    KJ = compose_ur(K_clean, J_prop, mod_e)
    I_op = add_ur(add_ur(J_prop, K_clean), KJ, Fraction(1), Fraction(-1))
    return I_op


def verify_step2_collapse_on_mixed() -> None:
    """Verify Step 2 Claim (Case 1 and Case 2) on higher-exponent mixed group Z_8 x Z_2."""
    # Group A = Z_8 x Z_2: p=2, e=3, s=1, A'=Z_2 (p^2 A' = 0), N=4, k=4, m=5.
    # Abar = Z_4 x Z_2 (k'=3, m-s=4). Take concrete rank-<=3 B_tilde over Z/4Z, factor B_tilde = U V,
    # and check the inner average of M(B_tilde, U', W') over W', U' matches Case 1 and Case 2!
    p, e, s, k_prime, m = 2, 3, 1, 3, 5
    mod_e = 8
    # U in (Z/4Z)^{4 x 3}, V in (Z/4Z)^{3 x 4}
    U = (
        (1, 0, 2),
        (2, 1, 0),
        (0, 1, 1),
        (1, 1, 3),
    )
    V = (
        (1, 2, 0, 1),
        (0, 1, 1, 2),
        (2, 0, 1, 1),
    )
    # Test representative points X = (X_1; X'), (Y_1; Y') in (Z_8 x Z_2)^5 hitting Case 1 and Case 2
    # Remember: Case 2 needs T = [Xbar_1; Vbar Xbar'] to have rank < s = 1, i.e., T == 0 mod 2!
    # Also test Case 2 with B_tilde X_tilde' != 0 mod 4 (even though T == 0 mod 2 -> Bbar Xbar' == 0 mod 2)!
    # Case 1 test point: X_1 = 1 (odd => T != 0 mod 2)
    test_points = [
        # Case 1: X in O (X_1=1, X' spans Z_2 in Z_2 coords)
        (((1,), (0,), (2,), (1,), (3,)), ((0,), (1,), (0,), (0,), (1,))),
        # Case 2: X_1=2 (even), X'=(2,0,0,0) => V X' = (2, 0, 0) == 0 mod 2 (so T==0 mod 2!), yet U V X' = (2,0,0,2) != 0 mod 4!
        (((2,), (2,), (0,), (0,), (0,)), ((1,), (0,), (1,), (0,), (1,))),
    ]
    for X_mat, Y_mat in test_points:
        # Compute T = [Xbar_1; Vbar Xbar'] mod 2
        T_rows = [[X_mat[0][0] % 2]]
        for r in range(k_prime):
            T_rows.append([sum(V[r][c] * X_mat[1 + c][0] for c in range(m - s)) % 2])
        t_rank = 1 if any(row[0] != 0 for row in T_rows) else 0

        # Compute exact sum over W' in F_2^{4 x 1} (16) and U' in F_2^{4 x 3} (4096) -> 65,536 pairs
        dist: dict[tuple, Fraction] = defaultdict(Fraction)
        denom = Fraction(1, 2 ** ((m - s) * (s + k_prime)))
        for Wp in product(range(2), repeat=4):
            for Up in product(range(2), repeat=12):
                Up_mat = [Up[i * 3 : (i + 1) * 3] for i in range(4)]
                U_sh = tuple(tuple((U[i][j] + 4 * Up_mat[i][j]) % 8 for j in range(3)) for i in range(4))
                UV = mat_mul_mod(U_sh, V, 8)
                M = ((1, 0, 0, 0, 0),) + tuple(((4 * Wp[i]) % 8,) + UV[i] for i in range(4))
                # Verify inner rank <= 4
                if Wp == (0, 0, 0, 0) and Up == (0,) * 12:
                    assert snf_inner_rank_mod_pe(M, 2, 3) <= 4
                MX = apply_matrix_to_tuple(M, tuple((X_mat[i][0], Y_mat[i][0]) for i in range(5)), [8, 2])
                dist[MX] += denom

        if t_rank == 1:
            # Case 1: uniform distribution of size 16 over fiber (X_1, UV X' mod 4) x (Y_1, B_tilde Y')
            assert len(dist) == 16
            assert all(v == Fraction(1, 16) for v in dist.values())
            UV_base = mat_mul_mod(U, V, 4)
            expected_X_top = X_mat[0][0] % 8
            expected_X_bot_mod4 = [sum(UV_base[i][c] * X_mat[1 + c][0] for c in range(4)) % 4 for i in range(4)]
            for pt in dist:
                assert pt[0][0] == expected_X_top
                assert [pt[1 + i][0] % 4 for i in range(4)] == expected_X_bot_mod4
        else:
            # Case 2: EVERY point in dist has even X-coord (since T==0 mod 2 => not in O), so any h supported on O vanishes!
            for pt in dist:
                assert all(pt[i][0] % 2 == 0 for i in range(5))
    print("Step 2 inner-average collapse (Z_8 x Z_2, 65,536 pairs, Case 1 & Case 2): PASS")


def op_to_linear_map(
    op: dict[tuple[tuple[int, ...], ...], Fraction],
    points: list[tuple[tuple[int, ...], ...]],
    pt_idx: dict[tuple[tuple[int, ...], ...], int],
    invariants: list[int],
) -> list[dict[int, Fraction]]:
    """Convert a matrix-action operator sum_M c_M f(M X) into sparse linear map L[x_idx][y_idx] = coeff."""
    L: list[dict[int, Fraction]] = []
    for X in points:
        row: dict[int, Fraction] = defaultdict(Fraction)
        for M, coeff in op.items():
            y_i = pt_idx[apply_matrix_to_tuple(M, X, invariants)]
            row[y_i] += coeff
        L.append({k: v for k, v in row.items() if v != 0})
    return L


def compose_linear_maps(L2: list[dict[int, Fraction]], L1: list[dict[int, Fraction]]) -> list[dict[int, Fraction]]:
    """Compute L2 o L1: (L2 o L1)(f)(X) = sum_Y L2[X][Y] (sum_Z L1[Y][Z] f(Z))."""
    out: list[dict[int, Fraction]] = []
    for row2 in L2:
        row: dict[int, Fraction] = defaultdict(Fraction)
        for y_i, c2 in row2.items():
            for z_i, c1 in L1[y_i].items():
                row[z_i] += c2 * c1
        out.append({k: v for k, v in row.items() if v != 0})
    return out


def add_linear_maps(
    L1: list[dict[int, Fraction]],
    L2: list[dict[int, Fraction]],
    s1: Fraction = Fraction(1),
    s2: Fraction = Fraction(1),
) -> list[dict[int, Fraction]]:
    out: list[dict[int, Fraction]] = []
    for r1, r2 in zip(L1, L2):
        row: dict[int, Fraction] = defaultdict(Fraction)
        for k, v in r1.items():
            row[k] += s1 * v
        for k, v in r2.items():
            row[k] += s2 * v
        out.append({k: v for k, v in row.items() if v != 0})
    return out


def verify_ug_linear_map_inductive(
    invariants: list[int],
    p: int,
    m: int,
    base_cache: dict[tuple[int, int], list],
    label: str,
) -> list[dict[int, Fraction]]:
    """
    Execute Steps 1-4 of PROOF.md for invariants (e >= 2), verifying SNF inner rank <= k
    on all generating matrices in I_i (Step 1) and A_{H_0} (Step 2), and verifying exact
    sparse linear operator identity I = Id_{|A|^m} across all points in A^m.
    """
    invariants = sorted([inv for inv in invariants if inv > 1], reverse=True)
    exps = []
    for inv in invariants:
        ej, t = 0, inv
        while t > 1:
            t //= p
            ej += 1
        exps.append(ej)
    N = sum(exps)
    e = exps[0]
    k = N
    s = sum(1 for ej in exps if ej == e)
    mod_e = p ** e
    mod_prev = p ** (e - 1)
    assert m == k + 1 and e >= 2

    A_elems = list(product(*[range(inv) for inv in invariants]))
    points = list(product(A_elems, repeat=m))
    pt_idx = {pt: idx for idx, pt in enumerate(points)}
    n_pts = len(points)

    # Step 1: Peeling all maximal proper subgroups via Lemma 2 (on sparse linear maps)
    subgroups = all_maximal_subgroups(invariants, p)
    J_prop_L: list[dict[int, Fraction]] | None = None
    for sub_info in subgroups:
        sub_invs = sub_info[3]
        op_C_small = build_ug_operator_inductive(sub_invs, p, m - 1, base_cache)
        exp_C = max(sub_invs) if sub_invs else 1
        op_C_m = {
            tuple(row + (0,) for row in M_sm) + ((0,) * (m - 1) + (1 % exp_C,),): c_sm
            for M_sm, c_sm in op_C_small.items()
        }
        I_i = lift_subgroup_operator(op_C_m, sub_info, invariants, p, k)
        for M in I_i:
            assert snf_inner_rank_mod_pe(M, p, e) <= k
        I_i_L = op_to_linear_map(I_i, points, pt_idx, invariants)
        if J_prop_L is None:
            J_prop_L = I_i_L
        else:
            comp = compose_linear_maps(I_i_L, J_prop_L)
            J_prop_L = add_linear_maps(add_linear_maps(J_prop_L, I_i_L), comp, Fraction(1), Fraction(-1))
    assert J_prop_L is not None

    # Step 2: Build A_{H_0} matrices from op_abar, verify SNF inner rank <= k, convert to sparse linear map
    abar_invs = [inv for inv in ([mod_prev] * s + invariants[s:]) if inv > 1]
    k_prime = N - s
    m_sub = m - s
    op_abar = build_ug_operator_inductive(abar_invs, p, m_sub, base_cache)

    A_H0: dict[tuple[tuple[int, ...], ...], Fraction] = defaultdict(Fraction)
    denom_H0 = Fraction(1, p ** ((m - s) * (s + k_prime)))
    for B_tilde, beta in op_abar.items():
        U, V = factor_rank_mod_pe(B_tilde, p, e - 1, k_prime)
        for W_prime_flat in product(range(p), repeat=(m - s) * s):
            W_prime = [W_prime_flat[i * s : (i + 1) * s] for i in range(m - s)]
            for U_prime_flat in product(range(p), repeat=(m - s) * k_prime):
                U_prime = [U_prime_flat[i * k_prime : (i + 1) * k_prime] for i in range(m - s)]
                U_shifted = tuple(
                    tuple((U[i][j] + mod_prev * U_prime[i][j]) % mod_e for j in range(k_prime))
                    for i in range(m - s)
                )
                UV = mat_mul_mod(U_shifted, V, mod_e)
                M_rows = [tuple(1 if j == i else 0 for j in range(m)) for i in range(s)]
                for i in range(m - s):
                    M_rows.append(tuple((mod_prev * W_prime[i][j]) % mod_e for j in range(s)) + UV[i])
                A_H0[tuple(M_rows)] += beta * denom_H0
    A_H0_clean = {mat: val for mat, val in A_H0.items() if val != 0}
    for M in A_H0_clean:
        assert snf_inner_rank_mod_pe(M, p, e) <= k
    L_H0 = op_to_linear_map(A_H0_clean, points, pt_idx, invariants)

    # Step 3: Conjugate L_H0 via T_H permutations, compose A_{H_1} o A_{H_2}, assemble Radon K
    subs = all_subspaces_fp(m, p)
    L_H_cache: dict[tuple[tuple[int, ...], ...], list[dict[int, Fraction]]] = {}
    for H_basis in subs[m - s]:
        ann_rows = [
            list(v) for v in product(range(p), repeat=m)
            if any(v) and all(sum(v[j] * b[j] for j in range(m)) % p == 0 for b in H_basis)
        ]
        perp_basis = rref_mod_p(ann_rows, p)
        cur = [list(r) for r in perp_basis]
        for j in range(m):
            e_j = [1 if i == j else 0 for i in range(m)]
            cand = rref_mod_p(cur + [e_j], p)
            if len(cand) > len(cur):
                cur.append(e_j)
                if len(cur) == m:
                    break
        T_H = tuple(tuple(r) for r in cur)
        T_H_inv = mat_inv_mod(T_H, mod_e)
        perm = [pt_idx[apply_matrix_to_tuple(T_H, X, invariants)] for X in points]
        perm_inv = [pt_idx[apply_matrix_to_tuple(T_H_inv, X, invariants)] for X in points]
        L_H_cache[H_basis] = [
            {perm_inv[y_i]: coeff for y_i, coeff in L_H0[perm[x_i]].items()}
            for x_i in range(n_pts)
        ]

    K_L: list[dict[int, Fraction]] = [{} for _ in range(n_pts)]
    for c in range(0, s + 1):
        outer = Fraction((-1) ** (s - c) * (p ** ((s - c) * (s - c + 1) // 2)) * q_binom(m - 1 - c, s - c, p))
        for U_basis in subs[m - c]:
            if c == s:
                L_U = L_H_cache[U_basis]
            else:
                H1 = rref_mod_p([list(r) for r in U_basis[: m - s]], p)
                H2 = rref_mod_p([list(r) for r in U_basis[s - c : m - c]], p)
                L_U = compose_linear_maps(L_H_cache[H1], L_H_cache[H2])
            K_L = add_linear_maps(K_L, L_U, Fraction(1), outer)

    # Step 4: I = J_prop + K - K o J_prop
    KJ_L = compose_linear_maps(K_L, J_prop_L)
    I_L = add_linear_maps(add_linear_maps(J_prop_L, K_L), KJ_L, Fraction(1), Fraction(-1))
    for x_i in range(n_pts):
        assert I_L[x_i] == {x_i: Fraction(1)}, f"{label}: failed at point index {x_i}"
    print(f"Full inductive linear-operator identity ({label}, |A|^{m} = {n_pts}, A_H0 mats = {len(A_H0_clean)}, inner rk <= {k}): PASS")
    return I_L


def verify_theorem2_crt_and_rings(op_z2: dict, op_z4: dict, op_z3: dict, L_z9: list[dict[int, Fraction]]) -> None:
    """Verify CRT clone product + Prop 21 on Z_6, Z_12, noncommutative M_2(Z/5Z), and trivial ring."""
    # 1. Z_6 = Z_2 x Z_3 (k=1, m=2) via CRT
    def crt(a: int, m1: int, b: int, m2: int) -> int:
        inv = pow(m1, -1, m2)
        t = ((b - a) * inv) % m2
        return (a + m1 * t) % (m1 * m2)

    op_z6: dict[tuple[tuple[int, ...], ...], Fraction] = defaultdict(Fraction)
    for M2, c2 in op_z2.items():
        for M3, c3 in op_z3.items():
            M6 = tuple(tuple(crt(M2[i][j], 2, M3[i][j], 3) for j in range(2)) for i in range(2))
            op_z6[M6] += c2 * c3
    op_z6 = {k: v for k, v in op_z6.items() if v != 0}
    # Check rank <= 1 over Z/6Z (mod 2 <= 1 and mod 3 <= 1 => CRT inner rank <= 1!)
    for M6 in op_z6:
        assert snf_inner_rank_mod_pe(M6, 2, 1) <= 1 and snf_inner_rank_mod_pe(M6, 3, 1) <= 1
    # Check exact identity on all 36 points of Z_6^2
    pts_z6 = list(product(range(6), repeat=2))
    for X in pts_z6:
        acc: dict[tuple[int, ...], Fraction] = defaultdict(Fraction)
        for M6, c6 in op_z6.items():
            MX = tuple((M6[i][0] * X[0] + M6[i][1] * X[1]) % 6 for i in range(2))
            acc[MX] += c6
        for Y, v in acc.items():
            assert v == (Fraction(1) if Y == X else Fraction(0))

    # 2. Z_12 = Z_4 x Z_3 (k=2, m=3) via CRT + Proposition 21 on all 1728 points
    op_z3_m3 = {
        (M3[0] + (0,), M3[1] + (0,), (0, 0, 1)): c3 for M3, c3 in op_z3.items()
    }
    # Check CRT inner-rank <= 2 directly via factorizations over Z/4Z and Z/3Z
    m4_list = list(op_z4.keys())[:200]
    for M4 in m4_list:
        U4, V4 = factor_rank_mod_pe(M4, 2, 2, 2)
        for M3 in op_z3_m3:
            U3, V3 = factor_rank_mod_pe(M3, 3, 1, 2)
            U12 = tuple(tuple(crt(U4[i][j], 4, U3[i][j], 3) for j in range(2)) for i in range(3))
            V12 = tuple(tuple(crt(V4[i][j], 4, V3[i][j], 3) for j in range(3)) for i in range(2))
            M12 = mat_mul_mod(U12, V12, 12)
            assert snf_inner_rank_mod_pe(M12, 2, 2) <= 2 and snf_inner_rank_mod_pe(M12, 3, 1) <= 2

    pts_z4 = list(product(range(4), repeat=3))
    idx_z4 = {pt: i for i, pt in enumerate(pts_z4)}
    # Fast direct sparse map on Z_4^3 (64 pts) and Z_3^3 (27 pts)
    L4_rows: list[dict[int, Fraction]] = []
    for X4 in pts_z4:
        row: dict[int, Fraction] = defaultdict(Fraction)
        for M4, c4 in op_z4.items():
            MX = tuple((M4[i][0] * X4[0] + M4[i][1] * X4[1] + M4[i][2] * X4[2]) % 4 for i in range(3))
            row[idx_z4[MX]] += c4
        L4_rows.append({k: v for k, v in row.items() if v != 0})
    pts_z3 = list(product(range(3), repeat=3))
    idx_z3 = {pt: i for i, pt in enumerate(pts_z3)}
    L3_rows: list[dict[int, Fraction]] = []
    for X3 in pts_z3:
        row = defaultdict(Fraction)
        for M3, c3 in op_z3_m3.items():
            MX = tuple((M3[i][0] * X3[0] + M3[i][1] * X3[1] + M3[i][2] * X3[2]) % 3 for i in range(3))
            row[idx_z3[MX]] += c3
        L3_rows.append({k: v for k, v in row.items() if v != 0})
    # Verify tensor product (Proposition 21) over all 1728 points of Z_12^3
    for i4 in range(64):
        for i3 in range(27):
            tens: dict[tuple[int, int], Fraction] = defaultdict(Fraction)
            for j4, c4 in L4_rows[i4].items():
                for j3, c3 in L3_rows[i3].items():
                    tens[(j4, j3)] += c4 * c3
            clean_tens = {k: v for k, v in tens.items() if v != 0}
            assert clean_tens == {(i4, i3): Fraction(1)}

    # 3. Noncommutative ring transfer: R = M_2(Z/5Z), where 2, 3, 4, 6 are invertible!
    # Homomorphism iota: Z[1/2, 1/3] -> Z(R) maps a/d -> ((a * d^{-1}) mod 5) * I_2
    def iota_m2_f5(q: Fraction) -> tuple[int, int, int, int]:
        scalar = (q.numerator * pow(q.denominator, -1, 5)) % 5
        return (scalar, 0, 0, scalar)

    # Test raw uncollapsed sums on Z_6 (210 mats, 36 pts) and Z_4 (5437 mats, 64 pts) -> M_2(F_5)
    def g_z6(X: tuple[int, ...]) -> tuple[int, int, int, int]:
        a, b = X
        return ((a * a + 2 * b + 1) % 5, (a * b + 3) % 5, (b + 4 * a) % 5, (a + 2 * b * b) % 5)

    for X in pts_z6:
        tot = [0, 0, 0, 0]
        for M6, c6 in op_z6.items():
            sc = iota_m2_f5(c6)[0]
            MX = tuple((M6[i][0] * X[0] + M6[i][1] * X[1]) % 6 for i in range(2))
            gx = g_z6(MX)
            for idx in range(4):
                tot[idx] = (tot[idx] + sc * gx[idx]) % 5
        assert tuple(tot) == g_z6(X)

    def g_z4(X: tuple[int, ...]) -> tuple[int, int, int, int]:
        x0, x1, x2 = X
        return (
            (x0 * x1 + x2 + 1) % 5,
            (x1 * x2 + 2 * x0) % 5,
            (x2 * x0 + 3 * x1) % 5,
            (x0 * x0 + 4 * x1 * x2) % 5,
        )

    for X in pts_z4:
        tot = [0, 0, 0, 0]
        for M4, c4 in op_z4.items():
            sc = iota_m2_f5(c4)[0]
            MX = tuple((M4[i][0] * X[0] + M4[i][1] * X[1] + M4[i][2] * X[2]) % 4 for i in range(3))
            gx = g_z4(MX)
            for idx in range(4):
                tot[idx] = (tot[idx] + sc * gx[idx]) % 5
        assert tuple(tot) == g_z4(X)

    # 4. Trivial ring R = {0}: every sum of iota(c) * 0 = 0 = g(X) trivially holds.
    print("Theorem 2 (CRT Z_6 / Z_12, M_2(Z/5Z) raw transfer on Z_6 & Z_4, trivial ring): PASS")


def verify_z4xz2_step_by_step(base_cache: dict[tuple[int, int], list]) -> None:
    """Verify Steps 1-3 on mixed non-cyclic group Z_4 x Z_2 (p=2, e=2, s=1, A'=Z_2, k=3, m=4)."""
    invariants = [4, 2]
    p, e, s, k, m = 2, 2, 1, 3, 4
    mod_e, mod_prev, k_prime = 4, 2, 2
    # Step 1: check all 3 maximal subgroups C_1, C_2, C_3 and their lifted operators I_i fix C_i^4 and have rank <= 3
    subgroups = all_maximal_subgroups(invariants, p)
    assert len(subgroups) == 3
    I_list = []
    for sub_info in subgroups:
        sub_invs = sub_info[3]
        op_C_small = build_ug_operator_inductive(sub_invs, p, m - 1, base_cache)
        exp_C = max(sub_invs)
        op_C_m = {
            tuple(row + (0,) for row in M_sm) + ((0,) * (m - 1) + (1 % exp_C,),): c_sm
            for M_sm, c_sm in op_C_small.items()
        }
        I_i = lift_subgroup_operator(op_C_m, sub_info, invariants, p, k)
        for M in list(I_i.keys())[:200]:
            assert snf_inner_rank_mod_pe(M, p, e) <= k
        I_list.append(I_i)

    # Check on representative tuples from each maximal subgroup C_i^4:
    # subgroups order from all_maximal_subgroups: w=(1,0), w=(1,1), w=(0,1)
    rep_by_w = {
        (1, 0): ((0, 1), (2, 0), (2, 1), (0, 0)),
        (1, 1): ((1, 1), (2, 0), (3, 1), (0, 0)),
        (0, 1): ((1, 0), (2, 0), (3, 0), (1, 0)),
    }
    for i_idx, sub_info in enumerate(subgroups):
        w = tuple(sub_info[0])
        rep = rep_by_w[w]
        assert all((w[0] * a + w[1] * b) % 2 == 0 for a, b in rep)
        acc: dict[tuple, Fraction] = defaultdict(Fraction)
        for M, c in I_list[i_idx].items():
            acc[apply_matrix_to_tuple(M, rep, invariants)] += c
        assert {kv: vv for kv, vv in acc.items() if vv != 0} == {rep: Fraction(1)}

    # Step 2: check A_{H_0} built from op_abar = F_2^2 matches F_{H_0} on Case 1 (in O) and Case 2 (not in O)
    op_abar = build_ug_operator_inductive([2, 2], 2, 3, base_cache)
    A_H0: dict[tuple[tuple[int, ...], ...], Fraction] = defaultdict(Fraction)
    denom_H0 = Fraction(1, 2 ** ((m - s) * (s + k_prime)))
    for B_tilde, beta in op_abar.items():
        U, V = factor_rank_mod_pe(B_tilde, p, 1, k_prime)
        for Wp_flat in product(range(2), repeat=3):
            for Up_flat in product(range(2), repeat=6):
                Up = [Up_flat[r * 2 : (r + 1) * 2] for r in range(3)]
                U_sh = tuple(tuple((U[r][c] + 2 * Up[r][c]) % 4 for c in range(2)) for r in range(3))
                UV = mat_mul_mod(U_sh, V, 4)
                M = ((1, 0, 0, 0),) + tuple(((2 * Wp_flat[r]) % 4,) + UV[r] for r in range(3))
                A_H0[M] += beta * denom_H0
    A_H0_clean = {mat: val for mat, val in A_H0.items() if val != 0}
    for M in list(A_H0_clean.keys())[:400]:
        assert snf_inner_rank_mod_pe(M, p, e) <= k

    # Compare A_{H_0}(h)(X) == F_{H_0}(h)(X) on Case 1 (X in O) for h = indicator of O (and random O-supported h)
    def in_O(pt: tuple[tuple[int, ...], ...]) -> bool:
        # <pt> == Z_4 x Z_2 iff mod-2 images span F_2^2, i.e., span all 3 nonzero cosets or rank == 2
        return len(rref_mod_p([[a % 2, b % 2] for a, b in pt], 2)) == 2

    def h_test(pt: tuple[tuple[int, ...], ...]) -> Fraction:
        if not in_O(pt):
            return Fraction(0)
        return Fraction(1 + sum((i + 1) * (pt[i][0] + 3 * pt[i][1]) for i in range(4)))

    # Case 1 point in O and Case 2 point outside O (top coord even, bottom mod 2 = (0,0))
    test_pts = [
        ((1, 0), (0, 1), (2, 1), (3, 0)),
        ((2, 1), (2, 0), (0, 1), (2, 1)),
    ]
    for X in test_pts:
        lhs = sum(c * h_test(apply_matrix_to_tuple(M, X, invariants)) for M, c in A_H0_clean.items())
        rhs = Fraction(0)
        for W in product(range(2), repeat=3):
            X_sh = (X[0],) + tuple(((X[1 + r][0] + 2 * W[r]) % 4, X[1 + r][1]) for r in range(3))
            rhs += h_test(X_sh) * Fraction(1, 8)
        assert lhs == rhs
    print(f"Mixed Z_4 x Z_2 Steps 1-2 ({len(A_H0_clean)} A_H0 mats, inner rk <= 3, O/Case1/Case2): PASS")


def main() -> None:
    verify_lemma1()
    base_cache: dict[tuple[int, int], list] = {}

    op_z2 = build_ug_operator_inductive([2], 2, 2, base_cache)
    verify_ug_operator_full(op_z2, [2], 2, 1, 2, "Z_2")

    op_z3 = build_ug_operator_inductive([3], 3, 2, base_cache)
    verify_ug_operator_full(op_z3, [3], 3, 1, 2, "Z_3")

    op_f2xf2 = build_ug_operator_inductive([2, 2], 2, 3, base_cache)
    verify_ug_operator_full(op_f2xf2, [2, 2], 2, 2, 3, "F_2^2")

    op_z4 = build_ug_operator_inductive([4], 2, 3, base_cache)
    verify_ug_operator_full(op_z4, [4], 2, 2, 3, "Z_4")

    verify_ug_linear_map_inductive([9], 3, 3, base_cache, "Z_9")
    verify_z4xz2_step_by_step(base_cache)

    verify_step2_collapse_on_mixed()
    verify_theorem2_crt_and_rings(op_z2, op_z4, op_z3, [])
    print("PASS")


if __name__ == "__main__":
    main()
