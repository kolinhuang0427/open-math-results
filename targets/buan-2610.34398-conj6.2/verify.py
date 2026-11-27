#!/usr/bin/env python3
"""
Exact-arithmetic verification of:
1. Buan-Hanson-Marsh (arXiv:2610.34398v1) Section 7.1 Conjecture 7.2 (conj:TFordered;
   tracked under legacy directory slug buan-2610.34398-conj6.2):
   For any tau-tilting finite algebra Lambda, ideal I <= rad(Lambda),
   TF-ordered tau_{Lambda/I}-rigid module (M_1, ..., M_t), and
   (N_1, ..., N_t) = L_I(M_1, ..., M_t):
     F(N_i) ~= M_i^{r_i} (+) X with X in add(+_{j=i+1}^t M_j) and r_i >= 1 (in fact r_i = 1).
2. Strong 2-Term Presilting Theorem:
   In K^b(proj(Lambda/I)), F(P_{N_i}) has ZERO shifted projective summands R[1],
   equivalently g_{Lambda/I}(F(N_i)) == g_Lambda(N_i) in Z^{rk Lambda}
   (and P_0(F(N_i)) ~= F(P_0(N_i)), P_1(F(N_i)) ~= F(P_1(N_i))).

All arithmetic is 100% exact over Q using integers and fractions.Fraction,
with zero float literals, zero float() calls, and zero '/' true-division operators.
"""

import ast
from collections import deque
from fractions import Fraction
import itertools
from pathlib import Path
import time

ZERO = Fraction(0, 1)
ONE = Fraction(1, 1)


def fdiv(a, b):
    """Exact Fraction division a / b without using '/'."""
    if not isinstance(a, Fraction):
        a = Fraction(a, 1)
    if not isinstance(b, Fraction):
        b = Fraction(b, 1)
    if b == ZERO:
        raise ZeroDivisionError("exact division by zero")
    return Fraction(a.numerator * b.denominator, a.denominator * b.numerator)


def to_frac(x):
    return x if isinstance(x, Fraction) else Fraction(x, 1)


# =============================================================================
# Exact Linear Algebra over Q
# =============================================================================

def rref(rows, ncols):
    """Return (pivots, reduced_nonzero_rows) in RREF over Q."""
    mat = [[to_frac(x) for x in row] for row in rows]
    m = len(mat)
    pivots = []
    r = 0
    for c in range(ncols):
        if r >= m:
            break
        piv = -1
        for i in range(r, m):
            if mat[i][c] != ZERO:
                piv = i
                break
        if piv < 0:
            continue
        if piv != r:
            mat[r], mat[piv] = mat[piv], mat[r]
        inv = fdiv(ONE, mat[r][c])
        row_r = mat[r]
        if inv != ONE:
            for j in range(c, ncols):
                if row_r[j] != ZERO:
                    row_r[j] = row_r[j] * inv
        for i in range(m):
            if i == r:
                continue
            factor = mat[i][c]
            if factor != ZERO:
                row_i = mat[i]
                row_i[c] = ZERO
                for j in range(c + 1, ncols):
                    if row_r[j] != ZERO:
                        row_i[j] = row_i[j] - factor * row_r[j]
        pivots.append(c)
        r += 1
    return pivots, mat[:r]


def nullspace(rows, ncols):
    """Return basis of {x in Q^ncols : A x = 0}."""
    pivots, red = rref(rows, ncols)
    piv_set = set(pivots)
    free_cols = [c for c in range(ncols) if c not in piv_set]
    basis = []
    for fc in free_cols:
        vec = [ZERO] * ncols
        vec[fc] = ONE
        for r_idx, pc in enumerate(pivots):
            val = red[r_idx][fc]
            if val != ZERO:
                vec[pc] = -val
        basis.append(vec)
    return basis


def mat_rank(rows, ncols):
    pivots, _ = rref(rows, ncols)
    return len(pivots)


def mat_mul(A, B, m=None, k=None, n=None):
    """Exact matrix product A * B where A is m x k and B is k x n."""
    if m is None:
        m = len(A)
    if k is None:
        k = len(B)
    if n is None:
        n = len(B[0]) if B else 0
    if m == 0 or n == 0:
        return [[ZERO] * n for _ in range(m)]
    if k == 0:
        return [[ZERO] * n for _ in range(m)]
    out = [[ZERO] * n for _ in range(m)]
    for i in range(m):
        row_a = A[i]
        row_out = out[i]
        for t in range(k):
            a_it = row_a[t]
            if a_it == ZERO:
                continue
            row_b = B[t]
            for j in range(n):
                b_tj = row_b[j]
                if b_tj != ZERO:
                    row_out[j] = row_out[j] + a_it * b_tj
    return out


def mat_vec(A, v):
    out = []
    for row in A:
        s = ZERO
        for a, x in zip(row, v):
            if a != ZERO and x != ZERO:
                s = s + a * x
        out.append(s)
    return out


def mat_transpose(A, nrows, ncols):
    return [[A[r][c] for r in range(nrows)] for c in range(ncols)]


def mat_identity(d):
    return [[ONE if i == j else ZERO for j in range(d)] for i in range(d)]


def mat_trace(A):
    s = ZERO
    for i in range(len(A)):
        s = s + A[i][i]
    return s


def is_nilpotent(A):
    d = len(A)
    if d == 0:
        return True
    cur = A
    for _ in range(d):
        if all(x == ZERO for row in cur for x in row):
            return True
        cur = mat_mul(cur, A, d, d, d)
    return all(x == ZERO for row in cur for x in row)


def solve_in_rowspace(pivots, red, vec):
    """Express vec as linear combination of red rows, or return None."""
    v = [to_frac(x) for x in vec]
    coeffs = []
    for r_idx, pc in enumerate(pivots):
        c = v[pc]
        coeffs.append(c)
        if c != ZERO:
            row_r = red[r_idx]
            for j in range(pc, len(v)):
                if row_r[j] != ZERO:
                    v[j] = v[j] - c * row_r[j]
    if any(x != ZERO for x in v):
        return None
    return coeffs


def express_in_basis(basis_vecs, ncols, target_vecs):
    """Express each vector in target_vecs in terms of basis_vecs (must be independent)."""
    m = len(basis_vecs)
    if m == 0:
        for tv in target_vecs:
            if any(x != ZERO for x in tv):
                raise ValueError("Target not in empty span")
        return [[] for _ in target_vecs]
    # Augment basis_vecs^T? No, solve transpose: sum_i c_i b_i = target
    aug = []
    for col in range(ncols):
        row = [basis_vecs[i][col] for i in range(m)] + [tv[col] for tv in target_vecs]
        aug.append(row)
    pivots, red = rref(aug, m + len(target_vecs))
    if len(pivots) != m or pivots != list(range(m)):
        raise ValueError("Basis vectors are not linearly independent")
    out = []
    for t_idx in range(len(target_vecs)):
        col = m + t_idx
        out.append([red[r_idx][col] for r_idx in range(m)])
    # Verify no inconsistency in remaining rows? rref only keeps r=m rows if consistent,
    # Wait: if inconsistent, there's a pivot >= m!
    for p in pivots:
        if p >= m:
            raise ValueError("Target vector not in span of basis")
    # Check remaining rows of rref! Since pivots == [0..m-1], all nonzero rows are accounted for,
    # wait: rref returned mat[:r], so if any pivot >= m existed it would be in pivots.
    return out


def quotient_projection(sub_vecs, total_dim):
    """
    Given sub_vecs spanning S <= Q^total_dim, return:
    (quot_dim, proj_mat, lift_mat)
    where proj_mat is quot_dim x total_dim (surjection Q^total_dim -> Q^quot_dim with kernel S)
    and lift_mat is total_dim x quot_dim (right inverse: proj_mat * lift_mat = I).
    """
    pivots, red = rref(sub_vecs, total_dim)
    piv_set = set(pivots)
    comp_cols = [c for c in range(total_dim) if c not in piv_set]
    qdim = len(comp_cols)
    # Build lift_mat: standard basis vectors for comp_cols
    lift_mat = [[ZERO] * qdim for _ in range(total_dim)]
    for j, cc in enumerate(comp_cols):
        lift_mat[cc][j] = ONE
    # Build proj_mat: for each standard basis vector e_k, reduce modulo red
    proj_mat = [[ZERO] * total_dim for _ in range(qdim)]
    col_to_q = {cc: j for j, cc in enumerate(comp_cols)}
    for k in range(total_dim):
        if k in col_to_q:
            proj_mat[col_to_q[k]][k] = ONE
        else:
            # k is a pivot column in red!
            r_idx = pivots.index(k)
            row_r = red[r_idx]
            for cc in comp_cols:
                if row_r[cc] != ZERO:
                    proj_mat[col_to_q[cc]][k] = -row_r[cc]
    return qdim, proj_mat, lift_mat


# =============================================================================
# Bound Quiver / Finite-Dimensional Basic Algebra Engine
# =============================================================================

class Algebra:
    """
    Finite-dimensional basic Q-algebra with primitive orthogonal idempotents e_0, ..., e_{n-1}.
    Basis elements 0..n-1 are e_0..e_{n-1}; basis[n:] span rad(A).
    comp_table[a][b] gives {c: coeff} for path composition (a followed by b),
    so on a left module M, (a followed by b).m = b.(a.m).
    """

    def __init__(self, n, basis_info, comp_table, name="Alg"):
        self.n = n
        # basis_info[idx] = (src, tgt, label)
        self.basis_info = basis_info
        self.dim = len(basis_info)
        # comp_table[a][b] = {c: coeff} for a followed by b
        self.comp_table = comp_table
        self.name = name

        # Partition basis by (src, tgt) and by src / tgt
        self.block_basis = {(i, j): [] for i in range(n) for j in range(n)}
        self.src_basis = [[] for _ in range(n)]
        self.tgt_basis = [[] for _ in range(n)]
        for idx, (s, t, _) in enumerate(basis_info):
            self.block_basis[(s, t)].append(idx)
            self.src_basis[s].append(idx)
            self.tgt_basis[t].append(idx)

        # Compute minimal generating set of rad(A) / rad^2(A) and word recipes
        self._build_generators()

        # Caches
        self._proj_cache = {}
        self._inj_cache = {}

    def _comp_vecs(self, v1, v2):
        """Compose sparse vectors {idx: coeff}: v1 followed by v2."""
        out = {}
        for b1, c1 in v1.items():
            if c1 == ZERO:
                continue
            row = self.comp_table[b1]
            for b2, c2 in v2.items():
                if c2 == ZERO:
                    continue
                prod = row.get(b2)
                if prod:
                    c12 = c1 * c2
                    for b3, c3 in prod.items():
                        nv = out.get(b3, ZERO) + c12 * c3
                        if nv == ZERO:
                            out.pop(b3, None)
                        else:
                            out[b3] = nv
        return out

    def _build_generators(self):
        n = self.n
        rad_dim = self.dim - n
        rad_indices = list(range(n, self.dim))
        # Compute rad^2 in basis[n:] coordinates
        rad2_rows = []
        for a in rad_indices:
            for b in rad_indices:
                prod = self.comp_table[a].get(b)
                if prod:
                    row = [ZERO] * rad_dim
                    for c, coeff in prod.items():
                        assert c >= n, "Product of radical elements fell outside rad"
                        row[c - n] = coeff
                    rad2_rows.append(row)
        pivs2, red2 = rref(rad2_rows, rad_dim)
        # Pick complement basis in each (src, tgt) block
        self.gens = []  # list of (src, tgt, basis_idx, label)
        cur_rows = [list(r) for r in red2]
        cur_pivs = list(pivs2)
        for s in range(n):
            for t in range(n):
                for b in self.block_basis[(s, t)]:
                    if b < n:
                        continue
                    vec = [ZERO] * rad_dim
                    vec[b - n] = ONE
                    if solve_in_rowspace(cur_pivs, cur_rows, vec) is None:
                        self.gens.append((s, t, b, self.basis_info[b][2]))
                        cur_rows.append(vec)
                        cur_pivs, cur_rows = rref(cur_rows, rad_dim)

        # Build spanning words of rad(A) from self.gens
        # Each word is (src, tgt, vec_in_rad, recipe)
        # recipe is ('gen', g_idx) or ('ext', prev_word_idx, g_idx)
        words = []
        word_rows = []
        w_pivs = []
        w_red = []
        queue = deque()
        for g_idx, (s, t, b, _) in enumerate(self.gens):
            vec = [ZERO] * rad_dim
            vec[b - n] = ONE
            if solve_in_rowspace(w_pivs, w_red, vec) is None:
                w_idx = len(words)
                words.append((s, t, {b: ONE}, ('gen', g_idx)))
                word_rows.append(vec)
                w_pivs, w_red = rref(word_rows, rad_dim)
                queue.append(w_idx)
        while queue and len(words) < rad_dim:
            wi = queue.popleft()
            ws, wt, wdict, _ = words[wi]
            for g_idx, (gs, gt, gb, _) in enumerate(self.gens):
                if wt != gs:
                    continue
                ndict = self._comp_vecs(wdict, {gb: ONE})
                if not ndict:
                    continue
                vec = [ZERO] * rad_dim
                for c, val in ndict.items():
                    vec[c - n] = val
                if solve_in_rowspace(w_pivs, w_red, vec) is None:
                    nw_idx = len(words)
                    words.append((ws, gt, ndict, ('ext', wi, g_idx)))
                    word_rows.append(vec)
                    w_pivs, w_red = rref(word_rows, rad_dim)
                    queue.append(nw_idx)
                    if len(words) == rad_dim:
                        break
        assert len(words) == rad_dim, (
            f"Generators did not span rad({self.name}): {len(words)} vs {rad_dim}"
        )
        self.words = words
        # Express each basis element b >= n in terms of words
        targets = []
        for b in rad_indices:
            tv = [ZERO] * rad_dim
            tv[b - n] = ONE
            targets.append(tv)
        self.basis_word_coeffs = express_in_basis(word_rows, rad_dim, targets)

    @classmethod
    def from_quiver(cls, n, arrows, relations, max_len=10, name="Q"):
        """
        arrows: list of (label, src, tgt) with src, tgt in 0..n-1.
        relations: list of list of (coeff, tuple_of_arrow_indices) in quiver order.
        """
        # Enumerate all paths up to max_len, grouped by (src, tgt)
        paths_by_len = [[] for _ in range(max_len + 1)]
        path_to_idx = {}
        all_paths = []  # (src, tgt, arrow_tuple)
        for v in range(n):
            p = (v, v, ())
            path_to_idx[(v, ())] = len(all_paths)
            all_paths.append(p)
            paths_by_len[0].append(len(all_paths) - 1)
        for L in range(1, max_len + 1):
            for pi in paths_by_len[L - 1]:
                s, t, tup = all_paths[pi]
                for a_idx, (_, asrc, atgt) in enumerate(arrows):
                    if t == asrc:
                        ntup = tup + (a_idx,)
                        idx = len(all_paths)
                        path_to_idx[(s, ntup)] = idx
                        all_paths.append((s, atgt, ntup))
                        paths_by_len[L].append(idx)

        total_paths = len(all_paths)
        # Build ideal rows generated by relations up to max_len
        ideal_rows = []
        for rel in relations:
            # Determine src, tgt of relation
            rel_terms = [(to_frac(c), tup) for c, tup in rel if c != 0]
            if not rel_terms:
                continue
            # Check vertex consistency per term
            for _, tup in rel_terms:
                for k in range(len(tup) - 1):
                    assert arrows[tup[k]][2] == arrows[tup[k + 1]][1]
            rs = arrows[rel_terms[0][1][0]][1]
            rt = arrows[rel_terms[0][1][-1]][2]
            max_rel_len = max(len(t) for _, t in rel_terms)
            for _, tup in rel_terms:
                assert arrows[tup[0]][1] == rs and arrows[tup[-1]][2] == rt
            # Multiply on left (prefix) and right (suffix) by paths
            for p_left_idx, (ls, lt, ltup) in enumerate(all_paths):
                if lt != rs or len(ltup) + max_rel_len > max_len:
                    continue
                for p_right_idx, (rs2, rt2, rtup) in enumerate(all_paths):
                    if rt != rs2 or len(ltup) + max_rel_len + len(rtup) > max_len:
                        continue
                    row = [ZERO] * total_paths
                    for c, tup in rel_terms:
                        full = ltup + tup + rtup
                        row[path_to_idx[(ls, full)]] += c
                    if any(x != ZERO for x in row):
                        ideal_rows.append(row)

        pivs, red = rref(ideal_rows, total_paths)
        # Verify finite-dimensionality: all paths of length max_len must lie in ideal + shorter paths!
        piv_set = set(pivs)
        # Wait: ensure max_len paths are actually zero in the quotient (i.e. rad^max_len = 0)
        for pi in paths_by_len[max_len]:
            vec = [ZERO] * total_paths
            vec[pi] = ONE
            if solve_in_rowspace(pivs, red, vec) is None:
                raise ValueError(f"{name}: algebra did not vanish by path length {max_len}")

        # Pick surviving basis paths: first e_0..e_{n-1}, then ascending length
        surviving = []
        cur_rows = [list(r) for r in red]
        cur_pivs = list(pivs)
        for L in range(max_len + 1):
            for pi in paths_by_len[L]:
                vec = [ZERO] * total_paths
                vec[pi] = ONE
                if solve_in_rowspace(cur_pivs, cur_rows, vec) is None:
                    surviving.append(pi)
                    cur_rows.append(vec)
                    cur_pivs, cur_rows = rref(cur_rows, total_paths)
        # Check that first n surviving paths are indeed e_0..e_{n-1}
        assert surviving[:n] == list(range(n)), "Idempotents collapsed!"

        # Quotient projection onto surviving paths
        qdim, proj_mat, _ = quotient_projection(red, total_paths)
        # Wait: quotient_projection picks comp_cols in ascending column order, which equals surviving!
        # Let's express every path in terms of surviving paths using rref of (red + surviving)
        # Actually, quotient_projection with comp_cols == surviving? Let's just use express_in_basis:
        surv_vecs = []
        for si in surviving:
            v = [ZERO] * total_paths
            v[si] = ONE
            surv_vecs.append(v)
        all_basis = [list(r) for r in red] + surv_vecs
        # Check len(all_basis) == total_paths
        assert len(all_basis) == total_paths
        # Express each surviving path's product in terms of all_basis, keeping only surviving part
        # Wait: much faster: solve in (red + surv_vecs) once!
        n_red = len(red)
        n_surv = len(surviving)
        # Build transition matrix on total_paths: first n_red rows are red, next n_surv are surv_vecs
        # Better: solve for the surviving-coordinate of every path!
        # Using express_in_basis on all_paths that appear as products:
        basis_info = []
        for si in surviving:
            s, t, tup = all_paths[si]
            if not tup:
                lbl = f"e{s}"
            else:
                lbl = "".join(arrows[a][0] for a in tup)
            basis_info.append((s, t, lbl))

        # Precompute projection of each path onto surviving basis
        aug_cols = []
        for col in range(total_paths):
            row = [all_basis[i][col] for i in range(total_paths)]
            aug_cols.append(row)
        # Invert by RREF with identity on right
        aug = [aug_cols[r] + [ONE if r == c else ZERO for c in range(total_paths)] for r in range(total_paths)]
        p_inv, r_inv = rref(aug, 2 * total_paths)
        assert p_inv == list(range(total_paths))
        # Path p's coefficient on surviving index k is r_inv[n_red + k][total_paths + p]
        path_coords = {}
        for p in range(total_paths):
            d = {}
            for k in range(n_surv):
                val = r_inv[n_red + k][total_paths + p]
                if val != ZERO:
                    d[k] = val
            path_coords[p] = d

        comp_table = [{} for _ in range(n_surv)]
        for i, si in enumerate(surviving):
            s1, t1, tup1 = all_paths[si]
            for j, sj in enumerate(surviving):
                s2, t2, tup2 = all_paths[sj]
                if t1 != s2:
                    continue
                if len(tup1) + len(tup2) > max_len:
                    continue
                p_prod = path_to_idx[(s1, tup1 + tup2)]
                coords = path_coords[p_prod]
                if coords:
                    comp_table[i][j] = coords

        return cls(n, basis_info, comp_table, name=name)

    def quotient(self, ideal_gens, name=None):
        """
        ideal_gens: list of dicts {basis_idx: coeff} generating a two-sided ideal I <= rad(A).
        Returns (A_quot, proj_basis) where proj_basis[b] = {q_idx: coeff} in A_quot.
        """
        n = self.n
        # Close ideal_gens under left and right multiplication by all basis elements
        rows = []
        for g in ideal_gens:
            g_clean = {k: to_frac(v) for k, v in g.items() if to_frac(v) != ZERO}
            if not g_clean:
                continue
            for a in range(self.dim):
                left_g = self._comp_vecs({a: ONE}, g_clean)
                if not left_g:
                    continue
                for b in range(self.dim):
                    full = self._comp_vecs(left_g, {b: ONE})
                    if full:
                        row = [ZERO] * self.dim
                        for k, val in full.items():
                            assert k >= n, f"Ideal not contained in rad({self.name})"
                            row[k] = val
                        rows.append(row)
        pivs, red = rref(rows, self.dim)
        qdim, proj_mat, lift_mat = quotient_projection(red, self.dim)
        # Note: since all rows are supported on >= n, pivots are all >= n,
        # so the first n comp_cols are 0..n-1!
        piv_set = set(pivs)
        comp_cols = [c for c in range(self.dim) if c not in piv_set]
        assert comp_cols[:n] == list(range(n))

        basis_info = [self.basis_info[c] for c in comp_cols]
        proj_basis = []
        for b in range(self.dim):
            d = {}
            for qi in range(qdim):
                val = proj_mat[qi][b]
                if val != ZERO:
                    d[qi] = val
            proj_basis.append(d)

        comp_table = [{} for _ in range(qdim)]
        for i, ci in enumerate(comp_cols):
            for j, cj in enumerate(comp_cols):
                prod = self.comp_table[ci].get(cj)
                if not prod:
                    continue
                qprod = {}
                for k, val in prod.items():
                    for qi, qval in proj_basis[k].items():
                        nv = qprod.get(qi, ZERO) + val * qval
                        if nv == ZERO:
                            qprod.pop(qi, None)
                        else:
                            qprod[qi] = nv
                if qprod:
                    comp_table[i][j] = qprod

        qname = name if name is not None else f"{self.name}/I"
        return Algebra(n, basis_info, comp_table, name=qname), proj_basis

    def projective(self, v):
        """Left projective P_v = A e_v."""
        if v in self._proj_cache:
            return self._proj_cache[v]
        indices = self.src_basis[v]
        pos = {b: idx for idx, b in enumerate(indices)}
        dims = [0] * self.n
        by_vert = [[] for _ in range(self.n)]
        for b in indices:
            _, t, _ = self.basis_info[b]
            by_vert[t].append(b)
        vpos = {}
        for u in range(self.n):
            dims[u] = len(by_vert[u])
            for k, b in enumerate(by_vert[u]):
                vpos[b] = k
        gen_mats = []
        for gs, gt, gb, _ in self.gens:
            mat = [[ZERO] * dims[gs] for _ in range(dims[gt])]
            for c_idx, b in enumerate(by_vert[gs]):
                prod = self.comp_table[b].get(gb)
                if prod:
                    for b2, val in prod.items():
                        r_idx = vpos[b2]
                        mat[r_idx][c_idx] = mat[r_idx][c_idx] + val
            gen_mats.append(mat)
        mod = Module(self, tuple(dims), gen_mats)
        self._proj_cache[v] = (mod, by_vert, vpos)
        return mod, by_vert, vpos

    def injective(self, v):
        """Left injective I_v = D(e_v A)."""
        if v in self._inj_cache:
            return self._inj_cache[v]
        indices = self.tgt_basis[v]
        by_vert = [[] for _ in range(self.n)]
        for b in indices:
            s, _, _ = self.basis_info[b]
            by_vert[s].append(b)
        dims = tuple(len(by_vert[u]) for u in range(self.n))
        vpos = {}
        for u in range(self.n):
            for k, b in enumerate(by_vert[u]):
                vpos[b] = k
        # Right mult by g (gs -> gt) maps e_v A e_gt -> e_v A e_gs: c |-> g * c (path g followed by c)
        # Transpose gives left action of g from e_gs I_v to e_gt I_v
        gen_mats = []
        for gs, gt, gb, _ in self.gens:
            mat = [[ZERO] * dims[gs] for _ in range(dims[gt])]
            for r_idx, c in enumerate(by_vert[gt]):
                # g followed by c lies in e_v A e_gs
                prod = self.comp_table[gb].get(c)
                if prod:
                    for b2, val in prod.items():
                        c_idx = vpos[b2]
                        mat[r_idx][c_idx] = mat[r_idx][c_idx] + val
            gen_mats.append(mat)
        mod = Module(self, dims, gen_mats)
        self._inj_cache[v] = (mod, by_vert, vpos)
        return mod, by_vert, vpos

    def simple(self, v):
        dims = tuple(1 if u == v else 0 for u in range(self.n))
        gen_mats = [[[ZERO] * dims[gs] for _ in range(dims[gt])] for gs, gt, _, _ in self.gens]
        return Module(self, dims, gen_mats)

    def zero_module(self):
        dims = (0,) * self.n
        gen_mats = [[[ZERO] * 0 for _ in range(0)] for _ in self.gens]
        return Module(self, dims, gen_mats)

    def regular(self):
        return direct_sum(self, [self.projective(v)[0] for v in range(self.n)])


# =============================================================================
# Left Modules and Morphisms
# =============================================================================

class Module:
    def __init__(self, alg, dims, gen_mats):
        self.alg = alg
        self.dims = tuple(dims)
        self.total_dim = sum(dims)
        # gen_mats[g_idx] is dims[gt] x dims[gs] matrix
        self.gen_mats = gen_mats
        self._basis_mats = None
        self._rad_sub = None
        self._end_info = None
        self._pres = None
        self._tau = None

    def is_zero(self):
        return self.total_dim == 0

    def basis_mats(self):
        """Return list of matrices (one per basis element b of alg) acting on self."""
        if self._basis_mats is not None:
            return self._basis_mats
        alg = self.alg
        n = alg.n
        word_mats = []
        for ws, wt, _, recipe in alg.words:
            if recipe[0] == 'gen':
                word_mats.append(self.gen_mats[recipe[1]])
            else:
                _, prev_wi, g_idx = recipe
                prev_s = alg.words[prev_wi][0]
                prev_t = alg.words[prev_wi][1]
                gt = alg.gens[g_idx][1]
                word_mats.append(
                    mat_mul(self.gen_mats[g_idx], word_mats[prev_wi], self.dims[gt], self.dims[prev_t], self.dims[prev_s])
                )
        bmats = [None] * alg.dim
        for v in range(n):
            bmats[v] = mat_identity(self.dims[v])
        for b in range(n, alg.dim):
            bs, bt, _ = alg.basis_info[b]
            m = [[ZERO] * self.dims[bs] for _ in range(self.dims[bt])]
            coeffs = alg.basis_word_coeffs[b - n]
            for wi, c in enumerate(coeffs):
                if c != ZERO:
                    wm = word_mats[wi]
                    for r in range(self.dims[bt]):
                        for col in range(self.dims[bs]):
                            if wm[r][col] != ZERO:
                                m[r][col] = m[r][col] + c * wm[r][col]
            bmats[b] = m
        self._basis_mats = bmats
        return bmats

    def radical_subspace(self):
        """Return per-vertex RREF basis of rad(self) = sum_{g} im(g_M)."""
        if self._rad_sub is not None:
            return self._rad_sub
        alg = self.alg
        rows_v = [[] for _ in range(alg.n)]
        for g_idx, (gs, gt, _, _) in enumerate(alg.gens):
            mat = self.gen_mats[g_idx]
            dg_s = self.dims[gs]
            dg_t = self.dims[gt]
            if dg_s == 0 or dg_t == 0:
                continue
            for col in range(dg_s):
                vec = [mat[r][col] for r in range(dg_t)]
                if any(x != ZERO for x in vec):
                    rows_v[gt].append(vec)
        self._rad_sub = [rref(rows_v[v], self.dims[v]) for v in range(alg.n)]
        return self._rad_sub

    def top_dims(self):
        rad = self.radical_subspace()
        return tuple(self.dims[v] - len(rad[v][0]) for v in range(self.alg.n))

    def quotient_by_submodule(self, sub_vecs_per_v):
        """Given vertex-wise spanning lists sub_vecs_per_v, return (quot_mod, proj_mats)."""
        alg = self.alg
        qdims = []
        proj_mats = []
        lift_mats = []
        for v in range(alg.n):
            qd, pm, lm = quotient_projection(sub_vecs_per_v[v], self.dims[v])
            qdims.append(qd)
            proj_mats.append(pm)
            lift_mats.append(lm)
        new_gmats = []
        for g_idx, (gs, gt, _, _) in enumerate(alg.gens):
            # pm[gt] * gen_mats[g_idx] * lm[gs]
            tmp = mat_mul(self.gen_mats[g_idx], lift_mats[gs], self.dims[gt], self.dims[gs], qdims[gs])
            ng = mat_mul(proj_mats[gt], tmp, qdims[gt], self.dims[gt], qdims[gs])
            new_gmats.append(ng)
        return Module(alg, tuple(qdims), new_gmats), proj_mats

    def submodule_from_bases(self, sub_bases_per_v):
        """Given vertex-wise independent bases (each list of vectors in Q^{dims[v]}), return (sub_mod, incl_mats)."""
        alg = self.alg
        sdims = tuple(len(sub_bases_per_v[v]) for v in range(alg.n))
        incl_mats = []
        for v in range(alg.n):
            # incl_mat is dims[v] x sdims[v]
            incl_mats.append(mat_transpose(sub_bases_per_v[v], sdims[v], self.dims[v]))
        # Express g(sub_basis) in sub_basis
        new_gmats = []
        for g_idx, (gs, gt, _, _) in enumerate(alg.gens):
            if sdims[gs] == 0 or sdims[gt] == 0:
                new_gmats.append([[ZERO] * sdims[gs] for _ in range(sdims[gt])])
                continue
            prod = mat_mul(self.gen_mats[g_idx], incl_mats[gs], self.dims[gt], self.dims[gs], sdims[gs])
            targets = [[prod[r][c] for r in range(self.dims[gt])] for c in range(sdims[gs])]
            coeffs = express_in_basis(sub_bases_per_v[gt], self.dims[gt], targets)
            # coeffs[c][r] is matrix entry [r][c]
            ng = [[coeffs[c][r] for c in range(sdims[gs])] for r in range(sdims[gt])]
            new_gmats.append(ng)
        return Module(alg, sdims, new_gmats), incl_mats

    def minimal_projective_presentation(self):
        """
        Return (P1_counts, P0_counts, P1_mod, P0_mod, d_mats, pi_mats, g_vec)
        where P1 -d-> P0 -pi-> self -> 0 is minimal projective presentation.
        """
        if self._pres is not None:
            return self._pres
        alg = self.alg
        n = alg.n
        rad = self.radical_subspace()
        # Pick top lifts at each vertex
        top_lifts = [[] for _ in range(n)]
        P0_counts = []
        for v in range(n):
            pivs, _ = rad[v]
            piv_set = set(pivs)
            comp = [c for c in range(self.dims[v]) if c not in piv_set]
            P0_counts.append(len(comp))
            for c in comp:
                vec = [ZERO] * self.dims[v]
                vec[c] = ONE
                top_lifts[v].append(vec)
        P0_counts = tuple(P0_counts)

        # Build P0 = direct sum of P_v^{P0_counts[v]} and pi: P0 -> self
        P0_summands = []
        P0_vertex_map = []  # (v, copy_idx)
        for v in range(n):
            for c_idx in range(P0_counts[v]):
                P0_summands.append(alg.projective(v)[0])
                P0_vertex_map.append((v, c_idx))
        P0_mod = direct_sum(alg, P0_summands)
        bmats_self = self.basis_mats()

        # Build pi_mats[u]: self.dims[u] x P0_mod.dims[u]
        pi_mats = [[] for _ in range(n)]
        # Initialize columns
        pi_cols = [[] for _ in range(n)]
        for v in range(n):
            Pv, by_vert_v, _ = alg.projective(v)
            for c_idx in range(P0_counts[v]):
                gen_vec = top_lifts[v][c_idx]
                for u in range(n):
                    for b in by_vert_v[u]:
                        col_vec = mat_vec(bmats_self[b], gen_vec)
                        pi_cols[u].append(col_vec)
        for u in range(n):
            if P0_mod.dims[u] == 0:
                pi_mats[u] = [[ZERO] * 0 for _ in range(self.dims[u])]
            else:
                pi_mats[u] = mat_transpose(pi_cols[u], P0_mod.dims[u], self.dims[u])

        # Compute K = ker(pi) inside P0_mod
        ker_bases = [nullspace(pi_mats[u], P0_mod.dims[u]) for u in range(n)]
        K_mod, incl_K = P0_mod.submodule_from_bases(ker_bases)

        # Projective cover of K_mod -> P1
        rad_K = K_mod.radical_subspace()
        K_top_lifts = [[] for _ in range(n)]
        P1_counts = []
        for v in range(n):
            pivs, _ = rad_K[v]
            piv_set = set(pivs)
            comp = [c for c in range(K_mod.dims[v]) if c not in piv_set]
            P1_counts.append(len(comp))
            for c in comp:
                vec = [ZERO] * K_mod.dims[v]
                vec[c] = ONE
                K_top_lifts[v].append(vec)
        P1_counts = tuple(P1_counts)

        P1_summands = []
        for v in range(n):
            for _ in range(P1_counts[v]):
                P1_summands.append(alg.projective(v)[0])
        P1_mod = direct_sum(alg, P1_summands)
        bmats_P0 = P0_mod.basis_mats()

        d_cols = [[] for _ in range(n)]
        for v in range(n):
            _, by_vert_v, _ = alg.projective(v)
            for c_idx in range(P1_counts[v]):
                # Lift generator into P0_mod via incl_K[v]
                gen_in_P0 = mat_vec(incl_K[v], K_top_lifts[v][c_idx])
                for u in range(n):
                    for b in by_vert_v[u]:
                        col_vec = mat_vec(bmats_P0[b], gen_in_P0)
                        d_cols[u].append(col_vec)
        d_mats = []
        for u in range(n):
            if P1_mod.dims[u] == 0:
                d_mats.append([[ZERO] * 0 for _ in range(P0_mod.dims[u])])
            else:
                d_mats.append(mat_transpose(d_cols[u], P1_mod.dims[u], P0_mod.dims[u]))

        g_vec = tuple(P0_counts[v] - P1_counts[v] for v in range(n))
        # Also record the exact elements d_elems[v1_copy] in P0 for tau computation!
        # Wait: for tau, we only need P1_summands, P0_summands, and the elements in e_v P0!
        self._pres = (P1_counts, P0_counts, P1_mod, P0_mod, d_mats, pi_mats, g_vec, K_top_lifts, incl_K)
        return self._pres

    def g_vector(self):
        return self.minimal_projective_presentation()[6]

    def tau(self):
        """Compute Auslander-Reiten translate tau(self) = ker(nu(d))."""
        if self._tau is not None:
            return self._tau
        alg = self.alg
        n = alg.n
        P1_counts, P0_counts, _, P0_mod, _, _, _, K_top_lifts, incl_K = self.minimal_projective_presentation()
        if sum(P1_counts) == 0:
            self._tau = alg.zero_module()
            return self._tau

        # P0_summand_offsets[s_idx] = (v0, start_col_in_P0_v0)
        p0_list = []  # (v0, offset_in_v0)
        off_v0 = [0] * n
        for v0 in range(n):
            Pv0, by_vert_v0, _ = alg.projective(v0)
            for _ in range(P0_counts[v0]):
                p0_list.append((v0, off_v0[v0]))
                off_v0[v0] += Pv0.dims[v0]
                # Wait: Pv0.dims[v0] is number of paths v0->v0; e_{v0} is at index 0 of by_vert_v0[v0]?
                # Actually, in P0_mod, direct_sum stacks summand u-spaces in order!
        # Recompute exact vertex offsets in P0_mod for each summand s_idx
        p0_summand_v = []
        for v0 in range(n):
            for _ in range(P0_counts[v0]):
                p0_summand_v.append(v0)
        p0_summand_mods = [alg.projective(v0)[0] for v0 in p0_summand_v]
        p0_offsets = []  # p0_offsets[s_idx][u] = start index in P0_mod at vertex u
        cur_off = [0] * n
        for s_idx, smod in enumerate(p0_summand_mods):
            p0_offsets.append(tuple(cur_off))
            for u in range(n):
                cur_off[u] += smod.dims[u]

        # Build nu(P1) = sum I_{v1}^{P1_counts[v1]} and nu(P0) = sum I_{v0}^{P0_counts[v0]}
        nuP1_list = [alg.injective(v1)[0] for v1 in range(n) for _ in range(P1_counts[v1])]
        nuP0_list = [alg.injective(v0)[0] for v0 in range(n) for _ in range(P0_counts[v0])]
        nuP1_mod = direct_sum(alg, nuP1_list)
        nuP0_mod = direct_sum(alg, nuP0_list)

        # Compute nu(d): nuP1_mod -> nuP0_mod
        # A summand of P1 at v1 maps to summand s0 of P0 at v0 via an element x in e_{v1} A e_{v0}
        # Specifically, gen_in_P0[u_slice] for u=v1 gives coefficients on by_vert_v0[v1]!
        # Under nu: I_{v1} -> I_{v0} sends f in D(e_{v1} A) to (y in e_{v0} A |-> f(x * y))
        # where x * y is path y followed by x (Wait: check! x in e_{v1} A e_{v0} means src=v0, tgt=v1!
        # And in P0, y in e_{v0} A e_w means src=w, tgt=v0! So y followed by x is comp_table[y][x] in e_{v1} A e_w!).
        # Let's double check: in d: P_{v1} -> P_{v0}, d(e_{v1}) = x in e_{v1} P_{v0} = e_{v1} A e_{v0} (src=v0, tgt=v1).
        # Then for g: P_{v0} -> A given by g(e_{v0}) = y in e_{v0} A e_w (src=w, tgt=v0),
        # (g o d)(e_{v1}) = g(x) = g(x * e_{v0}) = y followed by x = comp_table[y][x] in e_{v1} A e_w!
        # YES! That matches our A_2 test!
        nuP1_offsets = []
        cur = [0] * n
        for v1 in range(n):
            Iv1, _, _ = alg.injective(v1)
            for _ in range(P1_counts[v1]):
                nuP1_offsets.append(tuple(cur))
                for u in range(n):
                    cur[u] += Iv1.dims[u]

        nuP0_offsets = []
        cur = [0] * n
        for v0 in range(n):
            Iv0, _, _ = alg.injective(v0)
            for _ in range(P0_counts[v0]):
                nuP0_offsets.append(tuple(cur))
                for u in range(n):
                    cur[u] += Iv0.dims[u]

        nud_mats = [[[ZERO] * nuP1_mod.dims[u] for _ in range(nuP0_mod.dims[u])] for u in range(n)]

        p1_idx = 0
        for v1 in range(n):
            _, _, inv_vpos_v1 = alg.injective(v1)
            Iv1, by_vert_Iv1, _ = alg.injective(v1)
            for c1_idx in range(P1_counts[v1]):
                gen_in_P0 = mat_vec(incl_K[v1], K_top_lifts[v1][c1_idx])
                # Extract x_s0 for each summand s0 of P0
                for s0, v0 in enumerate(p0_summand_v):
                    _, by_vert_Pv0, _ = alg.projective(v0)
                    _, by_vert_Iv0, _ = alg.injective(v0)
                    start_p0 = p0_offsets[s0][v1]
                    x_dict = {}
                    for k, b_x in enumerate(by_vert_Pv0[v1]):
                        val = gen_in_P0[start_p0 + k]
                        if val != ZERO:
                            x_dict[b_x] = val
                    if not x_dict:
                        continue
                    # For each vertex w, map I_{v1}[w] -> I_{v0}[w]
                    for w in range(n):
                        row_off = nuP0_offsets[s0][w]
                        col_off = nuP1_offsets[p1_idx][w]
                        for r_k, y_b in enumerate(by_vert_Iv0[w]):
                            # Compute y_b followed by x_dict (in e_{v1} A e_w)
                            prod = alg._comp_vecs({y_b: ONE}, x_dict)
                            for b_res, val in prod.items():
                                c_k = inv_vpos_v1[b_res]
                                nud_mats[w][row_off + r_k][col_off + c_k] = (
                                    nud_mats[w][row_off + r_k][col_off + c_k] + val
                                )
                p1_idx += 1

        ker_bases = [nullspace(nud_mats[u], nuP1_mod.dims[u]) for u in range(n)]
        tau_mod, _ = nuP1_mod.submodule_from_bases(ker_bases)
        self._tau = tau_mod
        return tau_mod

    def apply_F(self, ideal_basis_indices, quot_alg, proj_basis):
        """
        Compute F(self) = self / (I * self) as a quot_alg-module,
        where I is spanned by ideal_basis_indices in self.alg.
        """
        alg = self.alg
        n = alg.n
        bmats = self.basis_mats()
        im_vecs = [[] for _ in range(n)]
        for b in ideal_basis_indices:
            _, bt, _ = alg.basis_info[b]
            mat = bmats[b]
            for col in range(self.dims[alg.basis_info[b][0]]):
                vec = [mat[r][col] for r in range(self.dims[bt])]
                if any(x != ZERO for x in vec):
                    im_vecs[bt].append(vec)
        # Quotient in self.alg first
        qdims = []
        proj_mats = []
        lift_mats = []
        for v in range(n):
            qd, pm, lm = quotient_projection(im_vecs[v], self.dims[v])
            qdims.append(qd)
            proj_mats.append(pm)
            lift_mats.append(lm)
        # Now evaluate quot_alg.gens on the quotient!
        # Find preimage of each quot_alg.gen in self.alg
        q_gmats = []
        for gs, gt, gb, _ in quot_alg.gens:
            # Find b_in_A projecting to gb (or linear comb)
            # Actually, in Algebra.quotient, gb corresponds to some comp_col, or just match proj_basis!
            # Wait: let's express gb in terms of proj_basis! Even simpler: look up which b has proj_basis[b] == {gb: 1}
            # (guaranteed since comp_cols all have proj_basis[ci] == {i: 1}!).
            b_orig = None
            for b in alg.block_basis[(gs, gt)]:
                if proj_basis[b] == {gb: ONE}:
                    b_orig = b
                    break
            assert b_orig is not None
            tmp = mat_mul(bmats[b_orig], lift_mats[gs], self.dims[gt], self.dims[gs], qdims[gs])
            ng = mat_mul(proj_mats[gt], tmp, qdims[gt], self.dims[gt], qdims[gs])
            q_gmats.append(ng)
        return Module(quot_alg, tuple(qdims), q_gmats)

    def end_info(self):
        """
        Compute End(self) and check whether End(self)/rad(End(self)) ~= Q
        (which also certifies indecomposability when True).
        Returns (end_basis, rad_end_basis, is_split_local).
        """
        if self._end_info is not None:
            return self._end_info
        end_basis = hom_basis(self, self)
        if not end_basis:
            self._end_info = ([], [], False)
            return self._end_info
        is_split_local = True
        rad_end = []
        td = self.total_dim
        # Flatten End(self) matrices across vertices for nilpotency test
        for phi in end_basis:
            tr = sum(mat_trace(phi[v]) for v in range(self.alg.n))
            c = fdiv(tr, Fraction(td, 1))
            # Check if phi - c * id is nilpotent at every vertex
            nilp_parts = []
            ok = True
            for v in range(self.alg.n):
                dv = self.dims[v]
                if dv == 0:
                    nilp_parts.append([])
                    continue
                diff = [
                    [phi[v][r][col] - (c if r == col else ZERO) for col in range(dv)]
                    for r in range(dv)
                ]
                if not is_nilpotent(diff):
                    ok = False
                    break
                nilp_parts.append(diff)
            if not ok:
                is_split_local = False
                break
            if any(x != ZERO for v in range(self.alg.n) for row in nilp_parts[v] for x in row):
                rad_end.append(nilp_parts)
        self._end_info = (end_basis, rad_end, is_split_local)
        return self._end_info

    def is_indecomposable_split(self):
        return self.end_info()[2]


def direct_sum(alg, mods):
    n = alg.n
    if not mods:
        dims = (0,) * n
        gmats = [[[ZERO] * 0 for _ in range(0)] for _ in alg.gens]
        return Module(alg, dims, gmats)
    dims = tuple(sum(m.dims[v] for m in mods) for v in range(n))
    gmats = []
    for g_idx, (gs, gt, _, _) in enumerate(alg.gens):
        mat = [[ZERO] * dims[gs] for _ in range(dims[gt])]
        r_off = 0
        c_off = 0
        for m in mods:
            mg = m.gen_mats[g_idx]
            mr = m.dims[gt]
            mc = m.dims[gs]
            for r in range(mr):
                for c in range(mc):
                    if mg[r][c] != ZERO:
                        mat[r_off + r][c_off + c] = mg[r][c]
            r_off += mr
            c_off += mc
        gmats.append(mat)
    return Module(alg, dims, gmats)


def hom_basis(M, N):
    """Return basis of Hom_A(M, N), each element as list of matrices [Phi_0, ..., Phi_{n-1}]."""
    alg = M.alg
    assert alg is N.alg
    n = alg.n
    # Variable offsets for each vertex v: M.dims[v] * N.dims[v]
    var_off = []
    tot_vars = 0
    for v in range(n):
        var_off.append(tot_vars)
        tot_vars += M.dims[v] * N.dims[v]
    if tot_vars == 0:
        return []
    eqs = []
    for g_idx, (gs, gt, _, _) in enumerate(alg.gens):
        Mg = M.gen_mats[g_idx]
        Ng = N.gen_mats[g_idx]
        ms, mt = M.dims[gs], M.dims[gt]
        ns, nt = N.dims[gs], N.dims[gt]
        if ms == 0 or nt == 0:
            continue
        # Equation for each entry (r in 0..nt-1, c in 0..ms-1):
        # sum_k Phi_gt[r][k] * Mg[k][c] - sum_l Ng[r][l] * Phi_gs[l][c] == 0
        off_t = var_off[gt]
        off_s = var_off[gs]
        for r in range(nt):
            for c in range(ms):
                row = [ZERO] * tot_vars
                if mt > 0:
                    for k in range(mt):
                        val = Mg[k][c]
                        if val != ZERO:
                            row[off_t + r * mt + k] += val
                if ns > 0:
                    for l in range(ns):
                        val = Ng[r][l]
                        if val != ZERO:
                            row[off_s + l * ms + c] -= val
                if any(x != ZERO for x in row):
                    eqs.append(row)
    ns_vecs = nullspace(eqs, tot_vars)
    basis = []
    for vec in ns_vecs:
        mats = []
        for v in range(n):
            mv, nv = M.dims[v], N.dims[v]
            off = var_off[v]
            mats.append([[vec[off + r * mv + c] for c in range(mv)] for r in range(nv)])
        basis.append(mats)
    return basis


def compose_morphisms(phi_BC, phi_AB, a_dims):
    """Return phi_BC o phi_AB for A -> B -> C where a_dims is A.dims."""
    n = len(phi_AB)
    out = []
    for v in range(n):
        A_v = a_dims[v]
        B_v = len(phi_AB[v])
        C_v = len(phi_BC[v])
        out.append(mat_mul(phi_BC[v], phi_AB[v], C_v, B_v, A_v))
    return out


def trace_pairing_rank(M_ind, Y):
    """
    For indecomposable M_ind with End(M_ind)/rad ~= Q,
    compute multiplicity of M_ind as a direct summand of Y
    via rank of trace pairing <g, f> = tr(g o f) on Hom(Y, M_ind) x Hom(M_ind, Y).
    """
    assert M_ind.is_indecomposable_split()
    f_list = hom_basis(M_ind, Y)
    g_list = hom_basis(Y, M_ind)
    if not f_list or not g_list:
        return 0
    n = M_ind.alg.n
    mat = []
    for g in g_list:
        row = []
        for f in f_list:
            comp = compose_morphisms(g, f, M_ind.dims)
            tr = sum(mat_trace(comp[v]) for v in range(n))
            row.append(tr)
        mat.append(row)
    return mat_rank(mat, len(f_list))


def is_iso_indecomp(M, N):
    if M.dims != N.dims:
        return False
    if M.total_dim == 0:
        return True
    return trace_pairing_rank(M, N) == 1


def is_in_gen(U_list, X):
    """Test whether X in Gen(sum U_list)."""
    if X.total_dim == 0:
        return True
    n = X.alg.n
    im_vecs = [[] for _ in range(n)]
    for U in U_list:
        for phi in hom_basis(U, X):
            for v in range(n):
                mat = phi[v]
                for c in range(U.dims[v]):
                    vec = [mat[r][c] for r in range(X.dims[v])]
                    if any(x != ZERO for x in vec):
                        im_vecs[v].append(vec)
    for v in range(n):
        if mat_rank(im_vecs[v], X.dims[v]) != X.dims[v]:
            return False
    return True


def torsion_free_part(U_list, X):
    """Compute f_U(X) = X / t_U(X) and projection matrices."""
    n = X.alg.n
    im_vecs = [[] for _ in range(n)]
    for U in U_list:
        for phi in hom_basis(U, X):
            for v in range(n):
                mat = phi[v]
                for c in range(U.dims[v]):
                    vec = [mat[r][c] for r in range(X.dims[v])]
                    if any(x != ZERO for x in vec):
                        im_vecs[v].append(vec)
    return X.quotient_by_submodule(im_vecs)


def is_tau_rigid(M):
    tM = M.tau()
    if tM.is_zero():
        return True
    return len(hom_basis(M, tM)) == 0


def cokernel(phi, M, N):
    """Compute cokernel of phi: M -> N as (coker_mod, proj_mats)."""
    n = N.alg.n
    im_vecs = [[] for _ in range(n)]
    for v in range(n):
        mat = phi[v]
        for c in range(M.dims[v]):
            vec = [mat[r][c] for r in range(N.dims[v])]
            if any(x != ZERO for x in vec):
                im_vecs[v].append(vec)
    return N.quotient_by_submodule(im_vecs)


def minimal_left_approx_coker(X, U_list):
    """
    Compute minimal left add(U)-approximation f: X -> U' and its cokernel.
    Each U in U_list must be pairwise non-isomorphic indecomposables with End/rad ~= Q.
    Returns coker(f).
    """
    m = len(U_list)
    if m == 0:
        return X.quotient_by_submodule([
            [[ONE if i == j else ZERO for j in range(X.dims[v])] for i in range(X.dims[v])]
            for v in range(X.alg.n)
        ])[0]  # 0 module!

    hom_XU = [hom_basis(X, U) for U in U_list]
    hom_UU = [[hom_basis(U_list[k], U_list[j]) for j in range(m)] for k in range(m)]
    rad_end_U = [U.end_info()[1] for U in U_list]

    # Flatten morphism vector in Hom(X, U_j) for linear independence test
    def flatten_morph(phi):
        out = []
        for mat in phi:
            for row in mat:
                out.extend(row)
        return out

    kept_maps = []  # list of (j, phi)
    for j in range(m):
        if not hom_XU[j]:
            continue
        Uj = U_list[j]
        n = Uj.alg.n
        flat_dim = sum(X.dims[v] * Uj.dims[v] for v in range(n))
        rad_rows = []
        for k in range(m):
            if not hom_XU[k]:
                continue
            psis = rad_end_U[j] if k == j else hom_UU[k][j]
            for psi in psis:
                for phi in hom_XU[k]:
                    rad_rows.append(flatten_morph(compose_morphisms(psi, phi, X.dims)))
        pivs, red = rref(rad_rows, flat_dim)
        for phi in hom_XU[j]:
            fv = flatten_morph(phi)
            if solve_in_rowspace(pivs, red, fv) is None:
                kept_maps.append((j, phi))
                rad_rows.append(fv)
                pivs, red = rref(rad_rows, flat_dim)

    if not kept_maps:
        # 0-map X -> 0 has cokernel 0
        return Module(X.alg, (0,) * X.alg.n, [
            [[ZERO] * 0 for _ in range(0)] for _ in X.alg.gens
        ])

    target_mods = [U_list[j] for j, _ in kept_maps]
    U_prime = direct_sum(X.alg, target_mods)
    # Assemble f: X -> U_prime
    n = X.alg.n
    f_mats = []
    for v in range(n):
        rows_v = []
        for _, phi in kept_maps:
            rows_v.extend(phi[v])
        f_mats.append(rows_v)
    coker_mod, _ = cokernel(f_mats, X, U_prime)
    return coker_mod


# =============================================================================
# Support tau-tilting Enumeration & Jasso Reduction
# =============================================================================

class AlgebraData:
    """Precomputed support tau-tilting poset and indecomposable tau-rigid modules for Algebra."""

    def __init__(self, alg):
        self.alg = alg
        self.indecomps = []  # list of indecomposable tau-rigid modules
        self.proj_indices = [None] * alg.n
        self.stau_pairs = []  # list of (T_frozenset, P_frozenset, split_proj_T_frozenset)
        self.tors_order = {}  # (idx1, idx2) -> True iff Gen(T_1) <= Gen(T_2)
        self.hom_cache = {}
        self.gen_cache = {}
        self._enumerate_stau_tilting()

    def get_or_add_ind(self, M):
        assert M.is_indecomposable_split(), f"Non-indecomposable module in {self.alg.name}"
        for idx, ex in enumerate(self.indecomps):
            if is_iso_indecomp(M, ex):
                return idx
        idx = len(self.indecomps)
        self.indecomps.append(M)
        return idx

    def has_hom(self, i, j):
        key = (i, j)
        if key not in self.hom_cache:
            self.hom_cache[key] = len(hom_basis(self.indecomps[i], self.indecomps[j])) > 0
        return self.hom_cache[key]

    def in_gen(self, U_key, x_idx):
        key = (U_key, x_idx)
        if key not in self.gen_cache:
            U_mods = [self.indecomps[i] for i in U_key]
            self.gen_cache[key] = is_in_gen(U_mods, self.indecomps[x_idx])
        return self.gen_cache[key]

    def _enumerate_stau_tilting(self):
        alg = self.alg
        n = alg.n
        self._jasso_cache = {}
        for v in range(n):
            Pv, _, _ = alg.projective(v)
            self.proj_indices[v] = self.get_or_add_ind(Pv)

        start_T = frozenset(self.proj_indices)
        start_P = frozenset()
        seen = {}
        queue = deque()

        def register_pair(T_set, P_set):
            key = (T_set, P_set)
            if key in seen:
                return
            assert len(T_set) + len(P_set) == n
            # Compute split projective summands of T_set
            split_T = set()
            for x in T_set:
                U_key = tuple(sorted(T_set - {x}))
                if not self.in_gen(U_key, x):
                    split_T.add(x)
            idx = len(self.stau_pairs)
            seen[key] = idx
            self.stau_pairs.append((T_set, P_set, frozenset(split_T)))
            queue.append(idx)

        register_pair(start_T, start_P)

        while queue:
            cur_idx = queue.popleft()
            T_set, P_set, split_T = self.stau_pairs[cur_idx]
            for x in sorted(split_T):
                U_set = T_set - {x}
                U_sorted = sorted(U_set)
                U_mods = [self.indecomps[i] for i in U_sorted]
                coker = minimal_left_approx_coker(self.indecomps[x], U_mods)
                if coker.is_zero():
                    # T' = U_set, find missing projective v with Hom(P_v, U) = 0
                    missing = []
                    for v in range(n):
                        pv_idx = self.proj_indices[v]
                        if pv_idx in P_set:
                            continue
                        if all(not self.has_hom(pv_idx, u) for u in U_set):
                            missing.append(pv_idx)
                    assert len(missing) == 1, f"Expected unique missing projective, got {missing}"
                    register_pair(U_set, P_set | {missing[0]})
                else:
                    y_idx = self.get_or_add_ind(coker)
                    assert y_idx not in U_set
                    register_pair(U_set | {y_idx}, P_set)

        # Verify tau-rigidity of all discovered indecomposables
        for M in self.indecomps:
            assert is_tau_rigid(M), f"Non-tau-rigid module discovered in {alg.name}"

        # Precompute torsion-class inclusion T_a <= T_b (iff T_a in Gen(T_b))
        num_t = len(self.stau_pairs)
        for b in range(num_t):
            Tb_key = tuple(sorted(self.stau_pairs[b][0]))
            for a in range(num_t):
                if a == b:
                    self.tors_order[(a, b)] = True
                    continue
                Ta_set = self.stau_pairs[a][0]
                ok = all(self.in_gen(Tb_key, x) for x in Ta_set)
                self.tors_order[(a, b)] = ok

    def find_stau_for_gen(self, M_indices):
        """Return index of stau_pair (T, P) with Gen(T) == Gen(M)."""
        M_key = tuple(sorted(M_indices))
        # Gen(M) == Gen(T) iff all M in Gen(T) AND T <= all T' containing M,
        # OR simply: M_i in Gen(T) and P_s(Gen(M)) == split_T?
        # Wait: every x in split_T must be in Gen(M) AND every m in M must be in Gen(T)!
        candidates = []
        for idx, (T_set, _, split_T) in enumerate(self.stau_pairs):
            T_key = tuple(sorted(T_set))
            if all(self.in_gen(T_key, m) for m in M_key) and all(self.in_gen(M_key, s) for s in split_T):
                candidates.append(idx)
        assert len(candidates) == 1, f"Expected unique torsion class for Gen(M), got {candidates}"
        return candidates[0]

    def bongartz_completion(self, M_indices):
        """Return stau_pair index of Bongartz completion P(lperp(tau M)), i.e. largest T containing M."""
        M_set = set(M_indices)
        cands = [idx for idx, (T_set, _, _) in enumerate(self.stau_pairs) if M_set.issubset(T_set)]
        assert cands
        # Pick unique maximum under tors_order
        max_cands = [a for a in cands if all(self.tors_order[(b, a)] for b in cands)]
        assert len(max_cands) == 1
        return max_cands[0]

    def tf_ordered_sequences(self):
        """Return all TF-ordered tau-rigid sequences (as tuples of indecomp indices) of lengths 1..n."""
        # Collect all basic tau-rigid sets from stau_pairs
        rigid_sets = set()
        for T_set, _, _ in self.stau_pairs:
            t_list = sorted(T_set)
            for r in range(1, len(t_list) + 1):
                for sub in itertools.combinations(t_list, r):
                    rigid_sets.add(sub)
        seqs_by_len = {r: [] for r in range(1, self.alg.n + 1)}
        for rset in sorted(rigid_sets):
            r = len(rset)
            for perm in itertools.permutations(rset):
                ok = True
                for i in range(r - 1):
                    tail_key = tuple(sorted(perm[i + 1:]))
                    if self.in_gen(tail_key, perm[i]):
                        ok = False
                        break
                if ok:
                    seqs_by_len[r].append(perm)
        return seqs_by_len


def jasso_reduction(alg_data, z_idx):
    """
    Given indecomposable tau-rigid Z = alg_data.indecomps[z_idx] in mods(Lambda),
    construct Gamma ~= End(P_bar)^op where P_bar = (+) f_Z(Q_i) for Q_i in B_Z \\ Z.
    Returns (Gamma, P_bar_mods, Q_indices, phi_func, phi_inv_func, gamma_morphs).
    """
    if z_idx in alg_data._jasso_cache:
        return alg_data._jasso_cache[z_idx]
    alg = alg_data.alg
    bz_idx = alg_data.bongartz_completion([z_idx])
    bz_T = alg_data.stau_pairs[bz_idx][0]
    Q_indices = sorted(bz_T - {z_idx})
    r = len(Q_indices)
    Z_mod = alg_data.indecomps[z_idx]
    P_bar = [torsion_free_part([Z_mod], alg_data.indecomps[q])[0] for q in Q_indices]

    if r == 0:
        res = (None, P_bar, Q_indices, None, None, None)
        alg_data._jasso_cache[z_idx] = res
        return res

    # Build Gamma = End(direct_sum(P_bar))^op
    # hom_blocks[i][j] = Hom(P_bar[j], P_bar[i])
    hom_blocks = [[hom_basis(P_bar[j], P_bar[i]) for j in range(r)] for i in range(r)]
    # Check each P_bar[i] is indecomposable_split
    rad_diag = []
    basis_info = []
    block_basis_maps = [[[] for _ in range(r)] for _ in range(r)]
    # First r basis elements are idempotents e_0 .. e_{r-1}
    for i in range(r):
        id_i = [mat_identity(P_bar[i].dims[v]) for v in range(alg.n)]
        basis_info.append((i, i, f"e{i}"))
        block_basis_maps[i][i].append((i, id_i))
    # Then radical elements: diagonal rad_end_U[i], and off-diagonal hom_blocks[i][j]
    for i in range(r):
        _, rad_i, ok = P_bar[i].end_info()
        assert ok, "P_bar[i] not split local"
        rad_diag.append(rad_i)
        for k, rphi in enumerate(rad_i):
            b_idx = len(basis_info)
            basis_info.append((i, i, f"r{i}_{k}"))
            block_basis_maps[i][i].append((b_idx, rphi))
    for i in range(r):
        for j in range(r):
            if i == j:
                continue
            for k, hphi in enumerate(hom_blocks[i][j]):
                b_idx = len(basis_info)
                basis_info.append((i, j, f"h{i}_{j}_{k}"))
                block_basis_maps[i][j].append((b_idx, hphi))

    # Build flattening helper for block (i, j) to express products in basis_info
    def flatten_hom(i, j, phi):
        out = []
        for v in range(alg.n):
            for row in phi[v]:
                out.extend(row)
        return out

    block_rrefs = {}
    for i in range(r):
        for j in range(r):
            items = block_basis_maps[i][j]
            if not items:
                block_rrefs[(i, j)] = None
                continue
            vecs = [flatten_hom(i, j, phi) for _, phi in items]
            # Wait: let's express products using express_in_basis!
            block_rrefs[(i, j)] = (items, vecs, len(vecs[0]))

    dim_G = len(basis_info)
    comp_table = [{} for _ in range(dim_G)]
    # Recall: b1 in block (i, j) is P_bar[j] -> P_bar[i], b2 in block (j, k) is P_bar[k] -> P_bar[j],
    # and b1 followed by b2 in Gamma = End^op is b1 o b2 : P_bar[k] -> P_bar[i]!
    for i in range(r):
        for j in range(r):
            items1 = block_basis_maps[i][j]
            if not items1:
                continue
            for k in range(r):
                items2 = block_basis_maps[j][k]
                if not items2:
                    continue
                if block_rrefs[(i, k)] is None:
                    continue
                target_items = block_basis_maps[i][k]
                _, tvecs, tdim = block_rrefs[(i, k)]
                prods = []
                prod_pairs = []
                for b1, phi1 in items1:
                    for b2, phi2 in items2:
                        comp = compose_morphisms(phi1, phi2, P_bar[k].dims)
                        fv = flatten_hom(i, k, comp)
                        if any(x != ZERO for x in fv):
                            prods.append(fv)
                            prod_pairs.append((b1, b2))
                if not prods:
                    continue
                coeffs_list = express_in_basis(tvecs, tdim, prods)
                for (b1, b2), coeffs in zip(prod_pairs, coeffs_list):
                    d = {}
                    for pos_t, c in enumerate(coeffs):
                        if c != ZERO:
                            d[target_items[pos_t][0]] = c
                    if d:
                        comp_table[b1][b2] = d

    Gamma = Algebra(r, basis_info, comp_table, name=f"J({alg.name})")
    # Store full flat maps for basis elements of Gamma so Phi and Phi^-1 are instant!
    gamma_morphs = [None] * dim_G
    for i in range(r):
        for j in range(r):
            for b_idx, phi in block_basis_maps[i][j]:
                gamma_morphs[b_idx] = phi

    def phi_func(X):
        """Phi: J(Z) -> mod(Gamma), X |-> Hom(P_bar, X)."""
        h_spaces = [hom_basis(P_bar[i], X) for i in range(r)]
        dims = tuple(len(h_spaces[i]) for i in range(r))
        # Flat representation of Hom(P_bar[i], X) for solving
        flat_spaces = []
        for i in range(r):
            vecs = []
            for h in h_spaces[i]:
                fv = []
                for v in range(alg.n):
                    for row in h[v]:
                        fv.extend(row)
                vecs.append(fv)
            flat_spaces.append(vecs)
        gen_mats = []
        for gs, gt, gb, _ in Gamma.gens:
            if dims[gs] == 0 or dims[gt] == 0:
                gen_mats.append([[ZERO] * dims[gs] for _ in range(dims[gt])])
                continue
            morph = gamma_morphs[gb]  # P_bar[gt] -> P_bar[gs]
            # Action sends h in Hom(P_bar[gs], X) to h o morph in Hom(P_bar[gt], X)
            targets = []
            for h in h_spaces[gs]:
                comp = compose_morphisms(h, morph, P_bar[gt].dims)
                fv = []
                for v in range(alg.n):
                    for row in comp[v]:
                        fv.extend(row)
                targets.append(fv)
            fdim = sum(P_bar[gt].dims[v] * X.dims[v] for v in range(alg.n))
            coeffs_list = express_in_basis(flat_spaces[gt], fdim, targets)
            mat = [[coeffs_list[c][r_i] for c in range(dims[gs])] for r_i in range(dims[gt])]
            gen_mats.append(mat)
        return Module(Gamma, dims, gen_mats)

    def phi_inv_func(Y):
        """Phi^-1: mod(Gamma) -> J(Z) <= mod(Lambda) via projective presentation."""
        if Y.is_zero():
            return Module(alg, (0,) * alg.n, [[[ZERO] * 0 for _ in range(0)] for _ in alg.gens])
        P1_counts, P0_counts, _, P0_mod, _, _, _, K_top_lifts, incl_K = Y.minimal_projective_presentation()
        p0_list = [i for i in range(r) for _ in range(P0_counts[i])]
        p1_list = [i for i in range(r) for _ in range(P1_counts[i])]
        L0_mods = [P_bar[i] for i in p0_list]
        L1_mods = [P_bar[i] for i in p1_list]
        L0 = direct_sum(alg, L0_mods)
        if not p1_list:
            return L0
        L1 = direct_sum(alg, L1_mods)

        # Find exact vertex offsets in P0_mod for each summand s0
        p0_offsets = []
        cur = [0] * r
        for i0 in p0_list:
            Pi0, _, _ = Gamma.projective(i0)
            p0_offsets.append(tuple(cur))
            for u in range(r):
                cur[u] += Pi0.dims[u]

        # Build morphism D: L1 -> L0 in mod(Lambda)
        # L1 summand p1_idx (at vertex i1) maps to L0 summand s0 (at vertex i0)
        # via x in e_{i1} Gamma e_{i0} -> gamma_morphs corresponds to P_bar[i0] -> P_bar[i1]?!
        # WAIT: check! In Gamma, d_Gamma: Gamma e_{i1} -> Gamma e_{i0} sends e_{i1} to x in e_{i1} Gamma e_{i0}.
        # Under Phi(P_bar[k]) = Gamma e_k: Hom_Gamma(Gamma e_{i1}, Gamma e_{i0}) = e_{i1} Gamma e_{i0}
        # = Hom_Lambda(P_bar[i1], P_bar[i0])?!
        # WAIT A SECOND! Earlier: block (i, j) in Gamma is Hom_Lambda(P_bar[j], P_bar[i])!
        # Let's check! If x is in block (i1, i0) = e_{i0} Gamma e_{i1}?!
        # Careful: in Gamma, basis_info[b] = (src, tgt, lbl) where block_basis[(s, t)] has morphisms P_bar[t] -> P_bar[s].
        # And in Gamma.projective(i0) = Gamma e_{i0}, its basis elements have src == i0, tgt == i1!
        # So e_{i1} (Gamma e_{i0}) has src == i0, tgt == i1, which is block (i0, i1) = Hom_Lambda(P_bar[i1], P_bar[i0])!!
        # YES! That matches d_Lambda: P_bar[i1] -> P_bar[i0]!
        l0_offsets = []
        cur_l0 = [0] * alg.n
        for m0 in L0_mods:
            l0_offsets.append(tuple(cur_l0))
            for v in range(alg.n):
                cur_l0[v] += m0.dims[v]

        l1_offsets = []
        cur_l1 = [0] * alg.n
        for m1 in L1_mods:
            l1_offsets.append(tuple(cur_l1))
            for v in range(alg.n):
                cur_l1[v] += m1.dims[v]

        D_mats = [[[ZERO] * L1.dims[v] for _ in range(L0.dims[v])] for v in range(alg.n)]
        p1_idx = 0
        for i1 in range(r):
            for c1 in range(P1_counts[i1]):
                gen_in_P0 = mat_vec(incl_K[i1], K_top_lifts[i1][c1])
                for s0, i0 in enumerate(p0_list):
                    _, by_vert_Pi0, _ = Gamma.projective(i0)
                    start_p0 = p0_offsets[s0][i1]
                    for k, b_x in enumerate(by_vert_Pi0[i1]):
                        coeff = gen_in_P0[start_p0 + k]
                        if coeff == ZERO:
                            continue
                        morph = gamma_morphs[b_x]  # P_bar[i1] -> P_bar[i0]
                        for v in range(alg.n):
                            r_off = l0_offsets[s0][v]
                            c_off = l1_offsets[p1_idx][v]
                            mv = morph[v]
                            for rr in range(P_bar[i0].dims[v]):
                                for cc in range(P_bar[i1].dims[v]):
                                    if mv[rr][cc] != ZERO:
                                        D_mats[v][r_off + rr][c_off + cc] += coeff * mv[rr][cc]
                p1_idx += 1

        coker_mod, _ = cokernel(D_mats, L1, L0)
        return coker_mod

    res = (Gamma, P_bar, Q_indices, phi_func, phi_inv_func, gamma_morphs)
    alg_data._jasso_cache[z_idx] = res
    return res


# =============================================================================
# Pair (Lambda, I): Lifting, Delta_I, omega, L_I, and Verification
# =============================================================================

class AlgebraPair:
    def __init__(self, alg, ideal_gens, label="Pair"):
        self.alg = alg
        self.label = label
        # Expand ideal basis indices in alg
        rows = []
        for g in ideal_gens:
            g_clean = {k: to_frac(v) for k, v in g.items() if to_frac(v) != ZERO}
            for a in range(alg.dim):
                left_g = alg._comp_vecs({a: ONE}, g_clean)
                if not left_g:
                    continue
                for b in range(alg.dim):
                    full = alg._comp_vecs(left_g, {b: ONE})
                    if full:
                        row = [ZERO] * alg.dim
                        for k, val in full.items():
                            row[k] = val
                        rows.append(row)
        # Note: quotient_alg is built via alg.quotient(ideal_gens)
        self.quot, self.proj_basis = alg.quotient(ideal_gens, name=f"{alg.name}/I")
        # Also get an explicit basis of I as dicts {basis_idx: coeff} in alg (or check apply_F)
        pivs, red = rref(rows, alg.dim)
        self.ideal_basis_vecs = []
        for row in red:
            d = {k: val for k, val in enumerate(row) if val != ZERO}
            if d:
                self.ideal_basis_vecs.append(d)

        self.data_L = AlgebraData(self.alg)
        self.data_Q = AlgebraData(self.quot)
        self._F_cache_L = {}  # ind_idx_L -> Module in quot
        self._lift_1_cache = {}  # c_idx in data_Q -> z_idx in data_L
        self._jasso_cache = {}  # (c_idx, z_idx) -> sub-AlgebraPair

    def apply_F(self, mod_L):
        """Compute F(mod_L) = mod_L / (I * mod_L) as a self.quot module."""
        alg = self.alg
        n = alg.n
        bmats = mod_L.basis_mats()
        im_vecs = [[] for _ in range(n)]
        for ivec in self.ideal_basis_vecs:
            # Group by src vertex
            by_src = {}
            for b, coeff in ivec.items():
                bs, bt, _ = alg.basis_info[b]
                by_src.setdefault(bs, []).append((bt, b, coeff))
            for bs, terms in by_src.items():
                for col in range(mod_L.dims[bs]):
                    out_v = {}
                    for bt, b, coeff in terms:
                        mat = bmats[b]
                        for r in range(mod_L.dims[bt]):
                            val = coeff * mat[r][col]
                            if val != ZERO:
                                lst = out_v.setdefault(bt, [ZERO] * mod_L.dims[bt])
                                lst[r] = lst[r] + val
                    for bt, vec in out_v.items():
                        if any(x != ZERO for x in vec):
                            im_vecs[bt].append(vec)

        qdims = []
        proj_mats = []
        lift_mats = []
        for v in range(n):
            qd, pm, lm = quotient_projection(im_vecs[v], mod_L.dims[v])
            qdims.append(qd)
            proj_mats.append(pm)
            lift_mats.append(lm)

        q_gmats = []
        for gs, gt, gb, _ in self.quot.gens:
            b_orig = None
            for b in alg.block_basis[(gs, gt)]:
                if self.proj_basis[b] == {gb: ONE}:
                    b_orig = b
                    break
            assert b_orig is not None
            tmp = mat_mul(bmats[b_orig], lift_mats[gs], mod_L.dims[gt], mod_L.dims[gs], qdims[gs])
            ng = mat_mul(proj_mats[gt], tmp, qdims[gt], mod_L.dims[gt], qdims[gs])
            q_gmats.append(ng)
        return Module(self.quot, tuple(qdims), q_gmats)

    def F_of_ind(self, l_idx):
        if l_idx not in self._F_cache_L:
            self._F_cache_L[l_idx] = self.apply_F(self.data_L.indecomps[l_idx])
        return self._F_cache_L[l_idx]

    def lift_single(self, c_idx):
        """
        Compute Z = P_s(phi^+(Gen_{Lambda/I} C)) for indecomposable tau-rigid C = data_Q.indecomps[c_idx].
        Returns z_idx in data_L.
        """
        if c_idx in self._lift_1_cache:
            return self._lift_1_cache[c_idx]
        # Find T_C = stau_pair in data_Q for Gen(C)
        tc_idx = self.data_Q.find_stau_for_gen([c_idx])
        TC_set = self.data_Q.stau_pairs[tc_idx][0]
        TC_key = tuple(sorted(TC_set))

        # Congruence class: all stau_pairs (T, P) in data_L such that Gen(F(T)) == Gen(C)
        # Since F(T) is support tau-tilting, Gen(F(T)) == Gen(C) iff
        # all summands of F(T) lie in Gen(TC) and all summands of TC lie in Gen(F(T)).
        cong = []
        for t_idx, (T_set, _, _) in enumerate(self.data_L.stau_pairs):
            F_T_mods = [self.F_of_ind(x) for x in T_set]
            # Check F_T_mods in Gen(TC)
            TC_mods = [self.data_Q.indecomps[c] for c in TC_key]
            if not all(is_in_gen(TC_mods, fm) for fm in F_T_mods):
                continue
            if not all(is_in_gen(F_T_mods, cm) for cm in TC_mods):
                continue
            cong.append(t_idx)
        assert cong, "Empty congruence class!"
        # Find unique maximum in cong
        max_elems = [a for a in cong if all(self.data_L.tors_order[(b, a)] for b in cong)]
        assert len(max_elems) == 1, f"Expected unique max in congruence class, got {max_elems}"
        top_idx = max_elems[0]
        split_Z = self.data_L.stau_pairs[top_idx][2]
        assert len(split_Z) == 1, f"Expected indecomposable Z, got {split_Z}"
        z_idx = next(iter(split_Z))
        self._lift_1_cache[c_idx] = z_idx
        return z_idx

    def _get_jasso_subpair(self, c_idx, z_idx):
        key = (c_idx, z_idx)
        if key in self._jasso_cache:
            return self._jasso_cache[key]
        Gamma, P_bar, Q_indices, phi_L, phi_L_inv, gamma_morphs = jasso_reduction(self.data_L, z_idx)
        assert Gamma is not None
        r = Gamma.n
        C_mod = self.data_Q.indecomps[c_idx]
        alg = self.alg
        n = alg.n

        FZ_P_bar = []
        comp_projs = []
        comp_lifts = []
        for i in range(r):
            M = P_bar[i]
            bmats = M.basis_mats()
            im_vecs = [[] for _ in range(n)]
            for ivec in self.ideal_basis_vecs:
                by_src = {}
                for b, coeff in ivec.items():
                    bs, bt, _ = alg.basis_info[b]
                    by_src.setdefault(bs, []).append((bt, b, coeff))
                for bs, terms in by_src.items():
                    for col in range(M.dims[bs]):
                        out_v = {}
                        for bt, b, coeff in terms:
                            mat = bmats[b]
                            for r_k in range(M.dims[bt]):
                                val = coeff * mat[r_k][col]
                                if val != ZERO:
                                    lst = out_v.setdefault(bt, [ZERO] * M.dims[bt])
                                    lst[r_k] = lst[r_k] + val
                        for bt, vec in out_v.items():
                            if any(x != ZERO for x in vec):
                                im_vecs[bt].append(vec)
            f_qdims = []
            f_pms = []
            f_lms = []
            for v in range(n):
                qd, pm, lm = quotient_projection(im_vecs[v], M.dims[v])
                f_qdims.append(qd)
                f_pms.append(pm)
                f_lms.append(lm)
            q_gmats = []
            for gs, gt, gb, _ in self.quot.gens:
                b_orig = None
                for b in alg.block_basis[(gs, gt)]:
                    if self.proj_basis[b] == {gb: ONE}:
                        b_orig = b
                        break
                tmp = mat_mul(bmats[b_orig], f_lms[gs], M.dims[gt], M.dims[gs], f_qdims[gs])
                q_gmats.append(mat_mul(f_pms[gt], tmp, f_qdims[gt], M.dims[gt], f_qdims[gs]))
            FM = Module(self.quot, tuple(f_qdims), q_gmats)
            FZM, fc_pms = torsion_free_part([C_mod], FM)
            p_tot = [mat_mul(fc_pms[v], f_pms[v], FZM.dims[v], FM.dims[v], M.dims[v]) for v in range(n)]
            lifts_v = []
            for v in range(n):
                dv_m = M.dims[v]
                dv_f = FZM.dims[v]
                if dv_f == 0:
                    lifts_v.append([[ZERO] * 0 for _ in range(dv_m)])
                    continue
                aug = [
                    p_tot[v][row_i] + [ONE if row_i == col_j else ZERO for col_j in range(dv_f)]
                    for row_i in range(dv_f)
                ]
                pivs_a, red_a = rref(aug, dv_m + dv_f)
                assert len(pivs_a) == dv_f
                lm_v = [[ZERO] * dv_f for _ in range(dv_m)]
                for row_i, pc in enumerate(pivs_a):
                    for col_j in range(dv_f):
                        lm_v[pc][col_j] = red_a[row_i][dv_m + col_j]
                lifts_v.append(lm_v)
            FZ_P_bar.append(FZM)
            comp_projs.append(p_tot)
            comp_lifts.append(lifts_v)

        # Compute F_Z(gamma_morphs[b]): FZ_P_bar[j] -> FZ_P_bar[i] for b in block (i, j)
        fz_morphs = [None] * Gamma.dim
        ideal_gens_IZ = []
        for i in range(r):
            for j in range(r):
                b_list = Gamma.block_basis[(i, j)]
                if not b_list:
                    continue
                flat_cols = []
                for b in b_list:
                    morph = gamma_morphs[b]  # P_bar[j] -> P_bar[i]
                    fzm = []
                    fv = []
                    for v in range(n):
                        tmp = mat_mul(
                            morph[v],
                            comp_lifts[j][v],
                            P_bar[i].dims[v],
                            P_bar[j].dims[v],
                            FZ_P_bar[j].dims[v],
                        )
                        res_v = mat_mul(
                            comp_projs[i][v],
                            tmp,
                            FZ_P_bar[i].dims[v],
                            P_bar[i].dims[v],
                            FZ_P_bar[j].dims[v],
                        )
                        fzm.append(res_v)
                        for row in res_v:
                            fv.extend(row)
                    fz_morphs[b] = fzm
                    flat_cols.append(fv)
                fdim = len(flat_cols[0])
                if fdim == 0:
                    for b in b_list:
                        ideal_gens_IZ.append({b: ONE})
                else:
                    # Transpose flat_cols to fdim x len(b_list) matrix and take nullspace
                    eq_mat = mat_transpose(flat_cols, len(b_list), fdim)
                    for ns_vec in nullspace(eq_mat, len(b_list)):
                        d = {b_list[idx_k]: val for idx_k, val in enumerate(ns_vec) if val != ZERO}
                        if d:
                            ideal_gens_IZ.append(d)

        sub_pair = AlgebraPair(Gamma, ideal_gens_IZ, label=f"{self.label}->red")

        def psi_Q(Y):
            """Equivalence J_{Lambda/I}(C) -> mod(Gamma/I_Z), Y |-> Hom_{Lambda/I}(FZ_P_bar, Y)."""
            h_spaces = [hom_basis(FZ_P_bar[i], Y) for i in range(r)]
            dims = tuple(len(h_spaces[i]) for i in range(r))
            flat_spaces = []
            for i in range(r):
                vecs = []
                for h in h_spaces[i]:
                    fv = []
                    for v in range(n):
                        for row in h[v]:
                            fv.extend(row)
                    vecs.append(fv)
                flat_spaces.append(vecs)
            gen_mats = []
            for gs, gt, gb, _ in sub_pair.quot.gens:
                if dims[gs] == 0 or dims[gt] == 0:
                    gen_mats.append([[ZERO] * dims[gs] for _ in range(dims[gt])])
                    continue
                b_orig = None
                for b in Gamma.block_basis[(gs, gt)]:
                    if sub_pair.proj_basis[b] == {gb: ONE}:
                        b_orig = b
                        break
                assert b_orig is not None
                fzm = fz_morphs[b_orig]  # FZ_P_bar[gt] -> FZ_P_bar[gs]
                targets = []
                for h in h_spaces[gs]:
                    comp = compose_morphisms(h, fzm, FZ_P_bar[gt].dims)
                    fv = []
                    for v in range(n):
                        for row in comp[v]:
                            fv.extend(row)
                    targets.append(fv)
                fdim = sum(FZ_P_bar[gt].dims[v] * Y.dims[v] for v in range(n))
                coeffs_list = express_in_basis(flat_spaces[gt], fdim, targets)
                mat = [[coeffs_list[c][r_i] for c in range(dims[gs])] for r_i in range(dims[gt])]
                gen_mats.append(mat)
            return Module(sub_pair.quot, dims, gen_mats)

        res = (sub_pair, phi_L, phi_L_inv, psi_Q)
        self._jasso_cache[key] = res
        return res

    def delta_I(self, tau_exc_seq):
        """
        Recursively compute Delta_I(C_1, ..., C_t) = (Z_1, ..., Z_t) as Module objects in mod(Lambda).
        Input: list of indecomposable Modules in mod(Lambda/I).
        """
        t = len(tau_exc_seq)
        assert t >= 1
        # Identify C_t in data_Q
        c_t = tau_exc_seq[-1]
        c_idx = None
        for idx, ex in enumerate(self.data_Q.indecomps):
            if is_iso_indecomp(c_t, ex):
                c_idx = idx
                break
        assert c_idx is not None, "C_t is not tau-rigid in Lambda/I"
        z_idx = self.lift_single(c_idx)
        Z_t = self.data_L.indecomps[z_idx]
        if t == 1:
            return [Z_t]

        sub_pair, phi_L, phi_L_inv, psi_Q = self._get_jasso_subpair(c_idx, z_idx)
        sub_C = [psi_Q(C_i) for C_i in tau_exc_seq[:-1]]
        sub_Z = sub_pair.delta_I(sub_C)
        lifted = [phi_L_inv(z_sub) for z_sub in sub_Z]
        return lifted + [Z_t]

    def omega(self, seq_mods, in_quot=False):
        """Mendoza-Treffinger map omega(M_1, ..., M_t)."""
        t = len(seq_mods)
        out = []
        for i in range(t - 1):
            tail = seq_mods[i + 1:]
            res, _ = torsion_free_part(tail, seq_mods[i])
            out.append(res)
        out.append(seq_mods[-1])
        return out

    def omega_inv_L(self, Z_seq):
        """
        Compute omega^{-1}(Z_1, ..., Z_t) = (N_1, ..., N_t) in mod(Lambda),
        returning list of indices in self.data_L.indecomps.
        """
        t = len(Z_seq)
        # Identify Z_t in data_L
        zt_idx = None
        for idx, ex in enumerate(self.data_L.indecomps):
            if is_iso_indecomp(Z_seq[-1], ex):
                zt_idx = idx
                break
        assert zt_idx is not None
        if t == 1:
            return [zt_idx]

        # Recursively invert (Z_1, ..., Z_{t-1}) in J(Z_t) ~= mod(Gamma)
        Gamma, P_bar, Q_indices, phi_L, phi_L_inv, _ = jasso_reduction(self.data_L, zt_idx)
        gamma_data = AlgebraData(Gamma)
        sub_Z = [phi_L(Z_i) for Z_i in Z_seq[:-1]]
        # Recursively compute omega_inv in gamma_data
        sub_N_indices = _omega_inv_general(gamma_data, sub_Z)
        sub_N_in_L = [phi_L_inv(gamma_data.indecomps[ni]) for ni in sub_N_indices]

        # Find unique indecomposable tau-rigid partner N_i of Z_t in data_L with f_{Z_t}(N_i) ~= sub_N_in_L[i]
        # Only need to check indecomposables that co-occur with zt_idx in some stau_pair!
        partners = set()
        for T_set, _, _ in self.data_L.stau_pairs:
            if zt_idx in T_set:
                partners.update(T_set)
        partners.discard(zt_idx)
        Z_t_mod = self.data_L.indecomps[zt_idx]
        N_indices = []
        for target_mod in sub_N_in_L:
            matches = []
            for p_idx in sorted(partners):
                cand_red, _ = torsion_free_part([Z_t_mod], self.data_L.indecomps[p_idx])
                if cand_red.dims == target_mod.dims and is_iso_indecomp(cand_red, target_mod):
                    matches.append(p_idx)
            assert len(matches) == 1, f"Expected unique Jasso lift for partner, got {matches}"
            N_indices.append(matches[0])
        N_indices.append(zt_idx)
        return N_indices


def _omega_inv_general(alg_data, Z_seq):
    """Invert omega on an arbitrary AlgebraData."""
    t = len(Z_seq)
    zt_idx = None
    for idx, ex in enumerate(alg_data.indecomps):
        if is_iso_indecomp(Z_seq[-1], ex):
            zt_idx = idx
            break
    assert zt_idx is not None
    if t == 1:
        return [zt_idx]
    Gamma, _, _, phi_L, phi_L_inv, _ = jasso_reduction(alg_data, zt_idx)
    gamma_data = AlgebraData(Gamma)
    sub_Z = [phi_L(Z_i) for Z_i in Z_seq[:-1]]
    sub_N_indices = _omega_inv_general(gamma_data, sub_Z)
    sub_N_in_L = [phi_L_inv(gamma_data.indecomps[ni]) for ni in sub_N_indices]

    partners = set()
    for T_set, _, _ in alg_data.stau_pairs:
        if zt_idx in T_set:
            partners.update(T_set)
    partners.discard(zt_idx)
    Z_t_mod = alg_data.indecomps[zt_idx]
    N_indices = []
    for target_mod in sub_N_in_L:
        matches = []
        for p_idx in sorted(partners):
            cand_red, _ = torsion_free_part([Z_t_mod], alg_data.indecomps[p_idx])
            if cand_red.dims == target_mod.dims and is_iso_indecomp(cand_red, target_mod):
                matches.append(p_idx)
        assert len(matches) == 1
        N_indices.append(matches[0])
    N_indices.append(zt_idx)
    return N_indices



# =============================================================================
# Helpers to Build Ideal Generators & Verify All Conjectures
# =============================================================================

def elem_from_labels(alg, labels):
    """Compose basis elements with matching labels in quiver order."""
    cur = None
    for lbl in labels:
        found = None
        for b_idx, (_, _, blbl) in enumerate(alg.basis_info):
            if blbl == lbl:
                found = {b_idx: ONE}
                break
        if found is None:
            return {}
        cur = found if cur is None else alg._comp_vecs(cur, found)
    return cur if cur is not None else {}


def rad_power_gens(alg, k):
    """Return list of elements spanning rad^k(alg)."""
    assert k >= 1
    cur = [{b: ONE} for b in range(alg.n, alg.dim)]
    for _ in range(k - 1):
        nxt = []
        for c in cur:
            for b in range(alg.n, alg.dim):
                p = alg._comp_vecs(c, {b: ONE})
                if p:
                    nxt.append(p)
        cur = nxt
    return cur


def verify_pair(pair, check_fig1=False, check_pns_c=None):
    """
    Exhaustively verify Conjecture 7.2 (conj:TFordered), Corollary 3 (r_i == 1),
    AND the Strong 2-Term Presilting Theorem
    (zero shifted projectives in F(P_{N_i}), i.e. g_{Lambda/I}(F(N_i)) == g_Lambda(N_i))
    for ALL TF-ordered tau_{Lambda/I}-rigid sequences of ALL lengths t = 1..rk.
    Also verify:
      - omega(N_1, ..., N_t) ~= Delta_I(omega_I(M_1, ..., M_t))
      - existence of non-L_I-lifted tau-rigid X in Lambda with g_{Lambda/I}(F(X)) != g_Lambda(X)
    """
    seqs_by_len = pair.data_Q.tf_ordered_sequences()
    total_seqs = 0
    total_terms = 0
    non_trivial_X_count = 0
    r_gt_1_count = 0
    example_X = None
    example_r_gt_1 = None

    # Cache g-vectors and minimal projective presentations in Lambda and Lambda/I
    g_L = [M.g_vector() for M in pair.data_L.indecomps]
    F_mods = [pair.F_of_ind(i) for i in range(len(pair.data_L.indecomps))]
    g_F = [fm.g_vector() for fm in F_mods]
    pres_L = [M.minimal_projective_presentation() for M in pair.data_L.indecomps]
    pres_F = [fm.minimal_projective_presentation() for fm in F_mods]

    # Check non-L_I-lifted modules with nonzero shifted projective R[1] in F(P_X)
    g_mismatch_indices = [
        i for i in range(len(pair.data_L.indecomps)) if g_F[i] != g_L[i]
    ]

    for t in sorted(seqs_by_len.keys()):
        for m_seq_idx in seqs_by_len[t]:
            total_seqs += 1
            M_mods = [pair.data_Q.indecomps[mi] for mi in m_seq_idx]
            C_mods = pair.omega(M_mods)
            Z_mods = pair.delta_I(C_mods)
            N_idx_list = pair.omega_inv_L(Z_mods)
            N_mods = [pair.data_L.indecomps[ni] for ni in N_idx_list]

            # Self-check: N_mods must be TF-ordered in Lambda and omega(N_mods) ~= Z_mods
            N_omega = pair.omega(N_mods)
            for k in range(t):
                assert is_iso_indecomp(N_omega[k], Z_mods[k]), (
                    f"[{pair.label}] omega(N) != Z at pos {k}"
                )
            for i in range(t - 1):
                tail_key = tuple(sorted(N_idx_list[i + 1:]))
                assert not pair.data_L.in_gen(tail_key, N_idx_list[i]), (
                    f"[{pair.label}] N_mods is not TF-ordered!"
                )

            # Check Conjecture 7.2 + Corollary 3 (r_i == 1) + Strong 2-Term Presilting Theorem for every i = 0..t-1
            for i in range(t):
                total_terms += 1
                ni = N_idx_list[i]
                FN_i = F_mods[ni]

                # (a) Conjecture 7.2 + Corollary 3: F(N_i) ~= M_i (+) (+_{j=i+1}^{t-1} M_j^{s_{ij}})
                mults = {}
                dim_sum = 0
                for j in range(i, t):
                    mj = m_seq_idx[j]
                    M_j = pair.data_Q.indecomps[mj]
                    c_j = trace_pairing_rank(M_j, FN_i)
                    if c_j > 0:
                        mults[j] = c_j
                        dim_sum += c_j * M_j.total_dim
                assert mults.get(i, 0) == 1, (
                    f"[{pair.label}] FAIL Conj 7.2 / Cor 3: r_{i} == {mults.get(i, 0)} != 1 for seq {m_seq_idx}"
                )
                assert dim_sum == FN_i.total_dim, (
                    f"[{pair.label}] FAIL Conj 7.2: extra summands outside add(M_{{>=i}}) "
                    f"for seq {m_seq_idx}, pos {i}: dim_sum={dim_sum} vs dim={FN_i.total_dim}"
                )
                if mults[i] >= 2:
                    r_gt_1_count += 1
                    if example_r_gt_1 is None:
                        example_r_gt_1 = (m_seq_idx, i, mults[i], FN_i.dims)
                if any(j > i for j in mults):
                    non_trivial_X_count += 1
                    if example_X is None:
                        example_X = (m_seq_idx, i, dict(mults), FN_i.dims)

                # (b) Strong 2-Term Presilting Theorem:
                # Zero shifted projectives R[1] in F(P_{N_i}) <=> g_{Lambda/I}(F(N_i)) == g_Lambda(N_i)
                # Also explicitly check P_0(F(N_i)) == P_0(N_i) and P_1(F(N_i)) == P_1(N_i)
                assert g_F[ni] == g_L[ni], (
                    f"[{pair.label}] FAIL Strong 2-Term Presilting: "
                    f"g_F({ni})={g_F[ni]} != g_L({ni})={g_L[ni]}"
                )
                assert pres_F[ni][1] == pres_L[ni][1], (
                    f"[{pair.label}] P_0 mismatch: {pres_F[ni][1]} vs {pres_L[ni][1]}"
                )
                assert pres_F[ni][0] == pres_L[ni][0], (
                    f"[{pair.label}] P_1 mismatch: {pres_F[ni][0]} vs {pres_L[ni][0]}"
                )

    # Check non-trivial P_ns(Gen C) if requested
    if check_pns_c is not None:
        c_mod = check_pns_c
        c_idx = None
        for idx, ex in enumerate(pair.data_Q.indecomps):
            if is_iso_indecomp(c_mod, ex):
                c_idx = idx
                break
        assert c_idx is not None
        tc_idx = pair.data_Q.find_stau_for_gen([c_idx])
        T_set, _, split_T = pair.data_Q.stau_pairs[tc_idx]
        pns_set = T_set - split_T
        assert len(pns_set) > 0, f"[{pair.label}] Expected non-trivial P_ns(Gen C) != 0!"

    # Check Figure 1 if requested (A_3 -> A_3/<ba>)
    if check_fig1:
        assert len(seqs_by_len[3]) == 12, f"Expected 12 length-3 Q seqs, got {len(seqs_by_len[3])}"
        lam_seqs = pair.data_L.tf_ordered_sequences()
        assert len(lam_seqs[3]) == 16, f"Expected 16 length-3 L seqs, got {len(lam_seqs[3])}"
        # Check exact lifted vs unlifted dimensions match Figure 1
        lifted_dims = set()
        for m_seq_idx in seqs_by_len[3]:
            M_mods = [pair.data_Q.indecomps[mi] for mi in m_seq_idx]
            N_idx_list = pair.omega_inv_L(pair.delta_I(pair.omega(M_mods)))
            lifted_dims.add(tuple(pair.data_L.indecomps[ni].dims for ni in N_idx_list))
        assert len(lifted_dims) == 12
        # Check the 4 unlifted sequences in Figure 1 (rows 13-16)
        # Rows 13-16 TF-ordered Lambda-modules (by dims):
        # 13: ((1,1,1), (1,1,0), (1,0,0))
        # 14: ((0,1,0), (1,1,1), (1,1,0))
        # 15: ((1,1,1), (0,1,0), (1,1,0))
        # 16: ((1,1,1), (1,1,0), (0,1,0))
        expected_unlifted = {
            ((1, 1, 1), (1, 1, 0), (1, 0, 0)),
            ((0, 1, 0), (1, 1, 1), (1, 1, 0)),
            ((1, 1, 1), (0, 1, 0), (1, 1, 0)),
            ((1, 1, 1), (1, 1, 0), (0, 1, 0)),
        }
        all_L_dims = {tuple(pair.data_L.indecomps[ni].dims for ni in seq) for seq in lam_seqs[3]}
        assert all_L_dims - lifted_dims == expected_unlifted, (
            f"Unlifted mismatch: {all_L_dims - lifted_dims}"
        )

    return {
        "label": pair.label,
        "dim_L": pair.alg.dim,
        "dim_Q": pair.quot.dim,
        "ind_L": len(pair.data_L.indecomps),
        "ind_Q": len(pair.data_Q.indecomps),
        "seqs": total_seqs,
        "seq_counts_by_len": {k: len(v) for k, v in seqs_by_len.items()},
        "terms": total_terms,
        "non_trivial_X": non_trivial_X_count,
        "r_gt_1": r_gt_1_count,
        "g_mismatch_inds": len(g_mismatch_indices),
        "example_X": example_X,
        "example_r_gt_1": example_r_gt_1,
    }


def build_test_pairs():
    pairs = []

    # 1. Paper Example 1: A_3 (1 -> 2 -> 3), I = <b a>
    a3 = Algebra.from_quiver(
        3,
        [("a", 0, 1), ("b", 1, 2)],
        [],
        name="A3",
    )
    pairs.append((
        AlgebraPair(a3, [elem_from_labels(a3, ["a", "b"])], label="1. Paper Ex1: A3 -> A3/<ba>"),
        {"check_fig1": True},
    ))

    # 2a. Paper Example 3: Cyclic Nakayama C_2 = k(1 -> 2 -> 1)/rad^3, I = rad^2/rad^3
    c2 = Algebra.from_quiver(
        2,
        [("a", 0, 1), ("b", 1, 0)],
        [
            [(1, (0, 1, 0))],
            [(1, (1, 0, 1))],
        ],
        max_len=4,
        name="C2/J3",
    )
    pairs.append((
        AlgebraPair(c2, rad_power_gens(c2, 2), label="2a. Paper Ex3: C2/J3 -> C2/J2"),
        {},
    ))

    # 2b. Rank-3 Cyclic Nakayama C_3 = k(1 -> 2 -> 3 -> 1)/rad^4, I = rad^3/rad^4
    c3 = Algebra.from_quiver(
        3,
        [("a", 0, 1), ("b", 1, 2), ("c", 2, 0)],
        [
            [(1, (0, 1, 2, 0))],
            [(1, (1, 2, 0, 1))],
            [(1, (2, 0, 1, 2))],
        ],
        max_len=5,
        name="C3/J4",
    )
    p2b = AlgebraPair(c3, rad_power_gens(c3, 3), label="2b. Cyclic Nakayama: C3/J4 -> C3/J3")
    pairs.append((p2b, {"check_pns_c": p2b.quot.projective(0)[0]}))

    # 3. D_4 (1 -> 0 -> 3, 2 -> 0 -> 3), I = <c a> (exhibits non-trivial multi-summand X != 0)
    d4 = Algebra.from_quiver(
        4,
        [("a", 1, 0), ("b", 2, 0), ("c", 0, 3)],
        [],
        name="D4",
    )
    pairs.append((
        AlgebraPair(d4, [elem_from_labels(d4, ["a", "c"])], label="3. D4 -> D4/<ca>"),
        {},
    ))

    # 4. Non-trivial P_ns(Gen C) + non-hereditary 2-cycle:
    # k(1 -a-> 2 -b-> 3, 2 -g-> 1)/<g a, b a g>, I = <g>
    # Note: in quiver order, g a is (0, 2) and b a g is (2, 0, 1)
    loop2c = Algebra.from_quiver(
        3,
        [("a", 0, 1), ("b", 1, 2), ("g", 1, 0)],
        [
            [(1, (0, 2))],
            [(1, (2, 0, 1))],
        ],
        max_len=5,
        name="2Cycle",
    )
    p4 = AlgebraPair(loop2c, [elem_from_labels(loop2c, ["g"])], label="4. 2-cycle/<ga,bag> -> A3")
    pairs.append((p4, {"check_pns_c": p4.quot.projective(0)[0]}))

    # 5a & 5b. Non-zero K_Z / non-hereditary 4-vertex quiver:
    # k(1 -a-> 2 -b-> 3 <-g- 4)/<b a> with I = <g>, and also k(1->2->3<-4) with I = <b a>
    q4_rel = Algebra.from_quiver(
        4,
        [("a", 0, 1), ("b", 1, 2), ("g", 3, 2)],
        [[(1, (0, 1))]],
        name="Q4/<ba>",
    )
    pairs.append((
        AlgebraPair(q4_rel, [elem_from_labels(q4_rel, ["g"])], label="5a. Q4/<ba> -> Q4/<ba,g>"),
        {},
    ))
    q4_hered = Algebra.from_quiver(
        4,
        [("a", 0, 1), ("b", 1, 2), ("g", 3, 2)],
        [],
        name="Q4",
    )
    pairs.append((
        AlgebraPair(q4_hered, [elem_from_labels(q4_hered, ["a", "b"])], label="5b. Q4 -> Q4/<ba>"),
        {},
    ))

    # 6a. Paper Example 2: 1 -a-> 2 with loops b: 1->1, g: 2->2, L = <g a b, b^2, g^2>, I = <b, g>
    ex2 = Algebra.from_quiver(
        2,
        [("a", 0, 1), ("b", 0, 0), ("g", 1, 1)],
        [
            [(1, (1, 0, 2))],  # b followed by a followed by g = g a b
            [(1, (1, 1))],
            [(1, (2, 2))],
        ],
        max_len=4,
        name="Ex2",
    )
    pairs.append((
        AlgebraPair(ex2, [elem_from_labels(ex2, ["b"]), elem_from_labels(ex2, ["g"])], label="6a. Paper Ex2 -> A2"),
        {},
    ))

    # 6b. Loop algebra A3 + loop at vertex 2: k(1 -a-> 2 -b-> 3, e: 2->2)/<e^2, b e a>, I = <e>
    # (Exhibits non-empty X != 0 with loop relations)
    loop_a3 = Algebra.from_quiver(
        3,
        [("a", 0, 1), ("b", 1, 2), ("e", 1, 1)],
        [
            [(1, (2, 2))],      # e^2 = 0
            [(1, (0, 2, 1))],   # b e a = 0
        ],
        max_len=5,
        name="A3+loop2",
    )
    pairs.append((
        AlgebraPair(loop_a3, [elem_from_labels(loop_a3, ["e"])], label="6b. A3+loop2 -> A3"),
        {},
    ))

    # 6c. Preprojective algebra Pi(A3) -> kA3 (non-hereditary symmetric-like 2-cycles, X != 0)
    pi_a3 = Algebra.from_quiver(
        3,
        [("a", 0, 1), ("as", 1, 0), ("b", 1, 2), ("bs", 2, 1)],
        [
            [(1, (0, 1))],                 # a* a = 0
            [(1, (3, 2))],                 # b b* = 0
            [(1, (1, 0)), (-1, (2, 3))],   # a a* - b* b = 0
        ],
        max_len=5,
        name="Pi(A3)",
    )
    pairs.append((
        AlgebraPair(
            pi_a3,
            [elem_from_labels(pi_a3, ["as"]), elem_from_labels(pi_a3, ["bs"])],
            label="6c. Pi(A3) -> A3",
        ),
        {},
    ))

    return pairs


def ast_check_exact_arithmetic(filepath):
    """AST-check that verify.py has ZERO float literals, ZERO float calls, and ZERO '/' divisions."""
    src = Path(filepath).read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(filepath))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            raise AssertionError(f"Float literal found at line {node.lineno}: {node.value}")
        if isinstance(node, ast.Div):
            raise AssertionError(f"True division '/' operator found at line {node.lineno}")
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name) and func.id in {"float", "round"}:
                raise AssertionError(f"Forbidden float call {func.id}() at line {node.lineno}")
            if isinstance(func, ast.Attribute) and func.attr == "float":
                raise AssertionError(f"Forbidden .float() call at line {node.lineno}")


def main():
    t0_ns = time.monotonic_ns()
    ast_check_exact_arithmetic(__file__)
    print("AST exact-arithmetic check: OK (0 floats, 0 '/' divisions)")

    pairs = build_test_pairs()
    total_seqs_all = 0
    total_terms_all = 0
    total_X_all = 0
    total_r2_all = 0
    total_gmismatch_all = 0

    for pair, opts in pairs:
        t_start_ns = time.monotonic_ns()
        res = verify_pair(pair, **opts)
        dt_ms = (time.monotonic_ns() - t_start_ns) // 1000000
        total_seqs_all += res["seqs"]
        total_terms_all += res["terms"]
        total_X_all += res["non_trivial_X"]
        total_r2_all += res["r_gt_1"]
        total_gmismatch_all += res["g_mismatch_inds"]
        print(
            f"[{res['label']}] dim=({res['dim_L']},{res['dim_Q']}) "
            f"ind=({res['ind_L']},{res['ind_Q']}) "
            f"seqs={res['seqs']} {res['seq_counts_by_len']} "
            f"terms={res['terms']} X!=0:{res['non_trivial_X']} r>=2:{res['r_gt_1']} "
            f"nonLifted_g!=:{res['g_mismatch_inds']} ({dt_ms} ms)"
        )
        if res["example_X"] is not None:
            print(f"   sample X!=0: {res['example_X']}")
        if res["example_r_gt_1"] is not None:
            print(f"   sample r>=2: {res['example_r_gt_1']}")

    total_ms = (time.monotonic_ns() - t0_ns) // 1000000
    assert total_gmismatch_all > 0, "Expected non-L_I-lifted modules with R[1] != 0"
    print(
        f"SUMMARY: {len(pairs)} pairs, {total_seqs_all} TF-ordered seqs, "
        f"{total_terms_all} terms, X!=0:{total_X_all}, r>=2:{total_r2_all}, "
        f"nonLifted_g!=:{total_gmismatch_all}, elapsed={total_ms} ms"
    )
    print("PASS")


if __name__ == "__main__":
    main()
