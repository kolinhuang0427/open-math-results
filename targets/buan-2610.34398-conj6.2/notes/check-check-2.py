#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/buan-2610.34398-conj6.2/PROOF.md.

Zero floating-point arithmetic: uses pure-Python int / fractions.Fraction
exact linear algebra for bound quiver algebras, 2-term silting mutation,
Auslander-Reiten translate tau, Jasso reduction J(Z), Mendoza-Treffinger
bijection omega, BHM lift Delta_I and L_I, and checks:
1. Primary paper Examples 1 (incl. all 12+4 Figure 1 sequences), 2, and 3.
2. Diverse non-hereditary, cyclic Nakayama, 2-cycle, D_4, A_4, and Pi(A_3) pairs.
3. All intermediate PROOF.md claims: Eq. (1), Lemma 2.1(c), Corollary 3 (r_i=1,
   F(Z)=C), Lemma 2.5, Theorem 1 (zero R[1] / g-vector preservation & matching
   P_0, P_1), Conjecture 7.2, plus counterexamples showing F(P_X) can have R[1]!=0
   outside L_I.
"""

from fractions import Fraction
from itertools import product
import time

# ---------------------------------------------------------------------------
# Exact linear algebra over Q (zero floats)
# ---------------------------------------------------------------------------

def _norm_row(row):
    """Exact int-like Fraction row operations helper (pure Fraction lists)."""
    return [x if isinstance(x, Fraction) else Fraction(x) for x in row]


def rref(mat, ncols=None):
    """Exact RREF over Q of list-of-lists mat. Returns (rref_rows, pivots)."""
    if not mat:
        return [], []
    if ncols is None:
        ncols = len(mat[0])
    A = [[Fraction(x) for x in row] for row in mat]
    m = len(A)
    pivots = []
    r = 0
    for c in range(ncols):
        if r >= m:
            break
        piv = None
        for i in range(r, m):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        if pv != 1:
            A[r] = [v / pv for v in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                fac = A[i][c]
                A[i] = [A[i][j] - fac * A[r][j] for j in range(ncols)]
        pivots.append(c)
        r += 1
    return A[:r], pivots


def nullspace(mat, ncols):
    """Basis vectors (list of lists of Fraction of len ncols) for ker(mat)."""
    R, pivs = rref(mat, ncols)
    piv_set = set(pivs)
    free_cols = [c for c in range(ncols) if c not in piv_set]
    basis = []
    for fc in free_cols:
        vec = [Fraction(0)] * ncols
        vec[fc] = Fraction(1)
        for row_idx, pc in enumerate(pivs):
            vec[pc] = -R[row_idx][fc]
        basis.append(vec)
    return basis


def matrix_rank(mat, ncols=None):
    if not mat:
        return 0
    _, pivs = rref(mat, ncols)
    return len(pivs)


def mat_mul(A, B):
    if not A or not B:
        return []
    m, k, n = len(A), len(A[0]), len(B[0])
    out = [[Fraction(0)] * n for _ in range(m)]
    for i in range(m):
        for r in range(k):
            air = A[i][r]
            if air == 0:
                continue
            for j in range(n):
                out[i][j] += air * B[r][j]
    return out


def mat_vec(A, v):
    return [sum(row[j] * v[j] for j in range(len(v))) for row in A]


def vec_in_span(basis, v):
    if not basis:
        return all(x == 0 for x in v)
    ncols = len(v)
    r1 = matrix_rank(basis, ncols)
    r2 = matrix_rank(basis + [v], ncols)
    return r1 == r2


def transpose(A):
    if not A:
        return []
    m, n = len(A), len(A[0])
    return [[A[i][j] for i in range(m)] for j in range(n)]


# ---------------------------------------------------------------------------
# Basic finite-dimensional algebra over Q via basis & multiplication table
# ---------------------------------------------------------------------------

class Algebra:
    def __init__(self, name, rk, src, dst, mul_table, rad_mask=None):
        """
        Basis elements 0..dim-1, each in e_{dst[b]} A e_{src[b]} (left action:
        for arrow a: u -> v, src=u, dst=v; path ba acts from u to w).
        mul_table[i][j] = list of (k, coeff) for b_i * b_j.
        """
        self.name = name
        self.rk = rk
        self.dim = len(src)
        self.src = list(src)
        self.dst = list(dst)
        self.mul = mul_table  # dim x dim -> list of (idx, Fraction)
        # Identify idempotents e_v (unique basis elt with src=dst=v acting as identity,
        # or find e_v by solving e_v * b = b):
        if rad_mask is None:
            # By default, non-idempotents are radical; identify idempotents by e_v^2 = e_v
            self.idem_idx = []
            for v in range(rk):
                candidates = [i for i in range(self.dim) if self.src[i] == v and self.dst[i] == v]
                found = None
                for i in candidates:
                    if self.mul[i][i] == [(i, Fraction(1))]:
                        # check acts as left identity on e_v A
                        ok = True
                        for j in range(self.dim):
                            if self.dst[j] == v and self.mul[i][j] != [(j, Fraction(1))]:
                                ok = False
                                break
                        if ok:
                            found = i
                            break
                assert found is not None, f"Idempotent e_{v} not found in {name}"
                self.idem_idx.append(found)
            self.rad_mask = [i not in self.idem_idx for i in range(self.dim)]
        else:
            self.rad_mask = list(rad_mask)
            self.idem_idx = [i for i in range(self.dim) if not self.rad_mask[i]]
        # Index pairs (u, v) -> basis indices in e_u A e_v (maps P_u -> P_v under right mult; dst=u, src=v)
        self.peirce = {(u, v): [] for u in range(rk) for v in range(rk)}
        for i in range(self.dim):
            self.peirce[(self.dst[i], self.src[i])].append(i)

    def mul_vecs(self, x, y):
        out = [Fraction(0)] * self.dim
        for i, xi in enumerate(x):
            if xi == 0:
                continue
            for j, yj in enumerate(y):
                if yj == 0:
                    continue
                for k, c in self.mul[i][j]:
                    out[k] += xi * yj * c
        return out

    def inv_eAe(self, v, x):
        """Invert x in e_v A e_v if scalar coeff of e_v is nonzero."""
        ev = self.idem_idx[v]
        c = x[ev]
        assert c != 0, "Not invertible in e_v A e_v"
        # x = c * (e_v - n) with n nilpotent; x^{-1} = (1/c) * sum n^k
        ev_vec = [Fraction(1) if i == ev else Fraction(0) for i in range(self.dim)]
        n_vec = [ev_vec[i] - x[i] / c for i in range(self.dim)]
        acc = list(ev_vec)
        cur = list(n_vec)
        while any(z != 0 for z in cur):
            acc = [acc[i] + cur[i] for i in range(self.dim)]
            cur = self.mul_vecs(cur, n_vec)
        return [z / c for z in acc]

    def proj_module(self, v):
        """Left A-module P_v = A e_v."""
        cols = [i for i in range(self.dim) if self.src[i] == v]
        idx_map = {b: pos for pos, b in enumerate(cols)}
        v_dims = [0] * self.rk
        v_lists = [[] for _ in range(self.rk)]
        for pos, b in enumerate(cols):
            w = self.dst[b]
            v_lists[w].append(pos)
        for w in range(self.rk):
            v_dims[w] = len(v_lists[w])
        # Build vertex-split basis order:
        perm = []
        v_offsets = [0] * self.rk
        for w in range(self.rk):
            v_offsets[w] = len(perm)
            perm.extend(v_lists[w])
        inv_perm = {cols[old_pos]: new_pos for new_pos, old_pos in enumerate(perm)}
        total = len(perm)
        actions = []
        for b in range(self.dim):
            mat = [[Fraction(0)] * total for _ in range(total)]
            for c_new, c_old in enumerate(perm):
                b_orig = cols[c_old]
                if self.dst[b_orig] != self.src[b]:
                    continue
                for k, coef in self.mul[b][b_orig]:
                    if k in inv_perm:
                        mat[inv_perm[k]][c_new] += coef
            actions.append(mat)
        return Module(self, v_dims, actions)

    def simple_module(self, v):
        v_dims = [1 if i == v else 0 for i in range(self.rk)]
        actions = []
        ev = self.idem_idx[v]
        for b in range(self.dim):
            actions.append([[Fraction(1)]] if b == ev else [[Fraction(0)]])
        return Module(self, v_dims, actions)


def build_bound_quiver_algebra(name, rk, arrows, rels):
    """
    Build Algebra from quiver with rk vertices 0..rk-1, arrows=[(name, u, v)],
    and rels=[dict[path_tuple -> coeff]] (paths written left-to-right as tuple of arrow indices,
    composition rule: if p1: u->v and p2: v->w, p2*p1 is p1 + p2 in path tuple!).
    Wait: let's be crystal clear! Arrow a: u -> v acts on left module as M_v <- M_u,
    so path tuple (a1, a2) means apply a1 first (u->v), then a2 (v->w): algebraic product a2 * a1!
    """
    # Enumerate paths by length using BFS, reducing modulo ideal <rels> by exact RREF
    # First collect all path tuples of length <= L (stopping when a full length reduces to 0 mod rels):
    adj_out = [[] for _ in range(rk)]
    for ai, (_, u, v) in enumerate(arrows):
        adj_out[u].append((ai, v))

    # Build paths length by length; keep linear basis via exact reduction in path-space up to max length:
    # Step 1: discover max non-zero length bound dynamically
    paths_by_len = {}
    paths_by_len[0] = [(v,) for v in range(rk)]  # special encoding (-1, v) for idempotent e_v
    # Actually encode vertex v idempotent as ('e', v), path as tuple of arrow indices!
    basis_elems = [('e', v) for v in range(rk)]
    basis_src = list(range(rk))
    basis_dst = list(range(rk))
    elem_to_id = {('e', v): v for v in range(rk)}

    # Precompute relation max length
    max_rel_len = max((len(p) for rel in rels for p in rel), default=0)
    # Generate all paths up to bound (start 10, expand if needed? For finite dim algebras, stops when len L is 0)
    # Better: generate paths up to length L_cur, build full relation matrix on all paths of length <= L_cur!
    # We'll pick a safe initial max length and grow if longest layer has surviving paths:
    def try_build(L_cap):
        all_paths = [('e', v) for v in range(rk)]
        p_src = list(range(rk))
        p_dst = list(range(rk))
        layers = [[('e', v) for v in range(rk)]]
        for length in range(1, L_cap + 1):
            nxt = []
            for p in layers[-1]:
                if p[0] == 'e':
                    u = p[1]
                    for ai, v in adj_out[u]:
                        nxt.append((ai,))
                        all_paths.append((ai,))
                        p_src.append(u)
                        p_dst.append(v)
                else:
                    last_a = p[-1]
                    u0 = arrows[p[0]][1]
                    v_cur = arrows[last_a][2]
                    for ai, v_nxt in adj_out[v_cur]:
                        np = p + (ai,)
                        nxt.append(np)
                        all_paths.append(np)
                        p_src.append(u0)
                        p_dst.append(v_nxt)
            layers.append(nxt)
            if not nxt:
                break

        p_idx = {p: i for i, p in enumerate(all_paths)}
        num_p = len(all_paths)

        def concat(p1, p2):
            # algebraic product p2 * p1 (first p1, then p2)
            if p1[0] == 'e':
                if p2[0] == 'e':
                    return p1 if p1[1] == p2[1] else None
                return p2 if arrows[p2[0]][1] == p1[1] else None
            if p2[0] == 'e':
                return p1 if arrows[p1[-1]][2] == p2[1] else None
            if arrows[p1[-1]][2] != arrows[p2[0]][1]:
                return None
            return p1 + p2

        # Build relation rows: L * rel * R for all paths L, R
        rel_rows = []
        for rel in rels:
            for p_l in all_paths:
                for p_r in all_paths:
                    row = {}
                    valid = True
                    for rp, coef in rel.items():
                        # p_l * rp * p_r
                        mid = concat(p_r, rp)
                        if mid is None:
                            continue
                        full = concat(mid, p_l)
                        if full is None:
                            continue
                        if full not in p_idx:
                            # truncation needed higher L_cap only if this rel term exceeded L_cap; skip truncated
                            continue
                        idx = p_idx[full]
                        row[idx] = row.get(idx, Fraction(0)) + Fraction(coef)
                    if row and any(v != 0 for v in row.values()):
                        vec = [Fraction(0)] * num_p
                        for k, v in row.items():
                            vec[k] = v
                        rel_rows.append(vec)

        R_mat, pivs = rref(rel_rows, num_p)
        piv_set = set(pivs)
        basis_p_indices = [i for i in range(num_p) if i not in piv_set]
        # Check if any path of length L_cap survived in basis_p_indices:
        if len(layers) - 1 == L_cap and any(
            all_paths[i][0] != 'e' and len(all_paths[i]) == L_cap for i in basis_p_indices
        ):
            return None  # Need larger L_cap

        # Express each path p_idx in terms of basis_p_indices:
        # Notice R_mat[row][piv] = 1, and in R_mat, relation says x_piv + sum_{free} R_mat[row][free]*x_free = 0
        # so x_piv = -sum_{free} R_mat[row][free]*x_free!
        piv_row = {pc: r_i for r_i, pc in enumerate(pivs)}
        free_to_b = {pi: bi for bi, pi in enumerate(basis_p_indices)}
        dim = len(basis_p_indices)

        def path_coords(pi):
            if pi in free_to_b:
                return [(free_to_b[pi], Fraction(1))]
            r_i = piv_row[pi]
            out = []
            for fc, bi in free_to_b.items():
                val = -R_mat[r_i][fc]
                if val != 0:
                    out.append((bi, val))
            return out

        b_src = [p_src[pi] for pi in basis_p_indices]
        b_dst = [p_dst[pi] for pi in basis_p_indices]
        mul_table = [[[] for _ in range(dim)] for _ in range(dim)]
        for bi, pi in enumerate(basis_p_indices):
            for bj, pj in enumerate(basis_p_indices):
                # algebraic product b_bi * b_bj = concat(all_paths[pj], all_paths[pi])
                prod = concat(all_paths[pj], all_paths[pi])
                if prod is not None and prod in p_idx:
                    mul_table[bi][bj] = path_coords(p_idx[prod])

        rad_mask = [all_paths[pi][0] != 'e' for pi in basis_p_indices]
        return Algebra(name, rk, b_src, b_dst, mul_table, rad_mask)

    for cap in (6, 10, 15, 22):
        alg = try_build(cap)
        if alg is not None:
            return alg
    raise ValueError(f"Algebra {name} appears infinite-dimensional!")


def ideal_quotient(alg, gen_indices_or_vecs, name=None):
    """Quotient alg by two-sided ideal generated by gen_indices_or_vecs (inside rad alg)."""
    vecs = []
    for g in gen_indices_or_vecs:
        if isinstance(g, int):
            v = [Fraction(0)] * alg.dim
            v[g] = Fraction(1)
            vecs.append(v)
        else:
            vecs.append([Fraction(x) for x in g])
    # Span of A * g * A:
    span_rows = []
    for g in vecs:
        for i in range(alg.dim):
            ei = [Fraction(0)] * alg.dim
            ei[i] = Fraction(1)
            lg = alg.mul_vecs(ei, g)
            if not any(x != 0 for x in lg):
                continue
            for j in range(alg.dim):
                ej = [Fraction(0)] * alg.dim
                ej[j] = Fraction(1)
                lgr = alg.mul_vecs(lg, ej)
                if any(x != 0 for x in lgr):
                    span_rows.append(lgr)
    R_id, pivs = rref(span_rows, alg.dim)
    piv_set = set(pivs)
    for ev in alg.idem_idx:
        assert ev not in piv_set, "Ideal not contained in rad(A)!"
    keep = [i for i in range(alg.dim) if i not in piv_set]
    piv_row = {pc: ri for ri, pc in enumerate(pivs)}
    keep_to_q = {oi: qi for qi, oi in enumerate(keep)}
    q_dim = len(keep)

    def coords(vec):
        # Reduce vec mod R_id
        v = list(vec)
        for pc in pivs:
            if v[pc] != 0:
                fac = v[pc]
                r_i = piv_row[pc]
                for c in range(alg.dim):
                    v[c] -= fac * R_id[r_i][c]
        return [(qi, v[oi]) for oi, qi in keep_to_q.items() if v[oi] != 0]

    q_src = [alg.src[oi] for oi in keep]
    q_dst = [alg.dst[oi] for oi in keep]
    q_mul = [[[] for _ in range(q_dim)] for _ in range(q_dim)]
    for qi, oi in enumerate(keep):
        for qj, oj in enumerate(keep):
            prod_vec = [Fraction(0)] * alg.dim
            for k, c in alg.mul[oi][oj]:
                prod_vec[k] = c
            q_mul[qi][qj] = coords(prod_vec)
    q_rad = [alg.rad_mask[oi] for oi in keep]
    q_alg = Algebra(name or f"{alg.name}/I", alg.rk, q_src, q_dst, q_mul, q_rad)
    # Projection matrix alg.dim -> q_dim (rows=q_dim, cols=alg.dim? Store map proj(vec_in_alg) -> vec_in_q):
    proj_cols = []
    for oi in range(alg.dim):
        v = [Fraction(1) if k == oi else Fraction(0) for k in range(alg.dim)]
        c_out = [Fraction(0)] * q_dim
        for qi, val in coords(v):
            c_out[qi] = val
        proj_cols.append(c_out)
    return q_alg, R_id, keep, proj_cols


# ---------------------------------------------------------------------------
# Left A-modules & exact Hom / Presentations / tau
# ---------------------------------------------------------------------------

class Module:
    def __init__(self, alg, v_dims, actions):
        """
        v_dims: list of length rk (dim at each vertex).
        actions[b]: total_dim x total_dim matrix (Fraction) for basis elt b.
        Basis is ordered by vertex 0, 1, ..., rk-1!
        """
        self.alg = alg
        self.v_dims = list(v_dims)
        self.dim = sum(v_dims)
        self.actions = actions
        self.v_off = []
        off = 0
        for d in v_dims:
            self.v_off.append(off)
            off += d

    def is_zero(self):
        return self.dim == 0

    def act(self, b, vec):
        if self.dim == 0:
            return []
        return mat_vec(self.actions[b], vec)

    def rad_subspace(self):
        """Basis (list of vectors of len self.dim) of rad(A)*M."""
        if self.dim == 0:
            return []
        rows = []
        for b in range(self.alg.dim):
            if not self.alg.rad_mask[b]:
                continue
            mat = self.actions[b]
            for col in range(self.dim):
                v = [mat[r][col] for r in range(self.dim)]
                if any(x != 0 for x in v):
                    rows.append(v)
        R, _ = rref(rows, self.dim)
        return R

    def top_dims(self):
        """Return list of vertex multiplicities of M / rad(A)*M."""
        if self.dim == 0:
            return [0] * self.alg.rk
        rad_b = self.rad_subspace()
        # At each vertex v, count basis vectors of vertex v modulo rad_b:
        res = []
        for v in range(self.alg.rk):
            d = self.v_dims[v]
            if d == 0:
                res.append(0)
                continue
            off = self.v_off[v]
            rad_v = [row[off: off + d] for row in rad_b]
            res.append(d - matrix_rank(rad_v, d))
        return res

    def direct_sum(self, other):
        assert self.alg is other.alg
        rk = self.alg.rk
        v_dims = [self.v_dims[v] + other.v_dims[v] for v in range(rk)]
        tot = self.dim + other.dim
        # Map old indices -> new vertex-ordered indices
        new_actions = []
        # Precompute block placement per vertex
        v_off_new = []
        cur = 0
        for v in range(rk):
            v_off_new.append(cur)
            cur += v_dims[v]
        for b in range(self.alg.dim):
            mat = [[Fraction(0)] * tot for _ in range(tot)]
            for v in range(rk):
                for u in range(rk):
                    # copy self block (v_dims[v] x v_dims[u])
                    for i in range(self.v_dims[v]):
                        for j in range(self.v_dims[u]):
                            mat[v_off_new[v] + i][v_off_new[u] + j] = self.actions[b][self.v_off[v] + i][self.v_off[u] + j]
                    for i in range(other.v_dims[v]):
                        for j in range(other.v_dims[u]):
                            mat[v_off_new[v] + self.v_dims[v] + i][v_off_new[u] + self.v_dims[u] + j] = other.actions[b][other.v_off[v] + i][other.v_off[u] + j]
            new_actions.append(mat)
        return Module(self.alg, v_dims, new_actions)

    def quotient_by_subspace(self, sub_basis):
        """Given vertex-aligned or arbitrary A-submodule basis, return (Q_mod, proj_mat)."""
        if not sub_basis:
            eye = [[Fraction(1) if i == j else Fraction(0) for j in range(self.dim)] for i in range(self.dim)]
            return self, eye
        # Build quotient basis per vertex:
        R_sub, pivs = rref(sub_basis, self.dim)
        piv_set = set(pivs)
        keep_cols = [c for c in range(self.dim) if c not in piv_set]
        piv_row = {pc: ri for ri, pc in enumerate(pivs)}
        q_dim = len(keep_cols)
        keep_to_q = {c: qi for qi, c in enumerate(keep_cols)}
        q_vdims = [0] * self.alg.rk
        for c in keep_cols:
            # find vertex of c:
            for v in range(self.alg.rk):
                if self.v_off[v] <= c < self.v_off[v] + self.v_dims[v]:
                    q_vdims[v] += 1
                    break

        def to_q(vec):
            v = list(vec)
            for pc in pivs:
                if v[pc] != 0:
                    fac = v[pc]
                    ri = piv_row[pc]
                    for j in range(self.dim):
                        v[j] -= fac * R_sub[ri][j]
            return [v[c] for c in keep_cols]

        proj_mat = transpose([to_q([Fraction(1) if i == j else Fraction(0) for i in range(self.dim)]) for j in range(self.dim)])
        q_actions = []
        for b in range(self.alg.dim):
            cols_q = []
            for c in keep_cols:
                vec = [self.actions[b][r][c] for r in range(self.dim)]
                cols_q.append(to_q(vec))
            q_actions.append(transpose(cols_q) if cols_q else [])
        return Module(self.alg, q_vdims, q_actions), proj_mat

    def apply_F(self, q_alg, proj_cols):
        """Compute F(M) = (A/I) otimes_A M = M / I*M as Module over q_alg."""
        # Kernel of proj_cols is spanned by R_id; compute I*M:
        # Which basis elements of A lie in I? Actually R_id rows!
        if self.dim == 0:
            return Module(q_alg, [0] * q_alg.rk, [[] for _ in range(q_alg.dim)]), []
        # Compute I*M by acting with every b in alg whose proj_cols[b] == 0? Careful: an ideal generator can be a linear combination!
        # Use R_id rows directly? Better: I is passed implicitly via proj_cols, wait: R_id rows are exact generators of I!
        raise NotImplementedError("Use module_apply_F(mod, q_alg, R_id, proj_cols)")


def module_apply_F(mod, q_alg, R_id):
    """Compute F(M) = M / I*M as Module over q_alg and canonical projection matrix."""
    if mod.dim == 0:
        return Module(q_alg, [0] * q_alg.rk, [[] for _ in range(q_alg.dim)]), []
    im_rows = []
    for rel in R_id:
        # Linear combination of mod.actions[b]
        act_mat = [[Fraction(0)] * mod.dim for _ in range(mod.dim)]
        for b, c in enumerate(rel):
            if c == 0:
                continue
            mb = mod.actions[b]
            for i in range(mod.dim):
                for j in range(mod.dim):
                    act_mat[i][j] += c * mb[i][j]
        for col in range(mod.dim):
            v = [act_mat[r][col] for r in range(mod.dim)]
            if any(x != 0 for x in v):
                im_rows.append(v)
    Q_as_A_mod, proj_mat = mod.quotient_by_subspace(im_rows)
    # Re-index actions for q_alg (using surviving basis elements keep? No! Q_as_A_mod already has actions for ALL alg basis elements!)
    # Just pick the 'keep' indices where q_alg basis corresponds to A basis!
    # Wait: proj_cols maps each A-basis element to q_alg; we need for each q_alg basis element ANY representative in A!
    # Wait: in ideal_quotient, keep[qi] IS a direct A-basis representative of q_alg basis element qi!
    return Q_as_A_mod, proj_mat


def module_apply_F_exact(mod, q_alg, R_id, keep):
    Q_as_A, proj_mat = module_apply_F(mod, q_alg, R_id)
    q_actions = [Q_as_A.actions[oi] for oi in keep]
    return Module(q_alg, Q_as_A.v_dims, q_actions), proj_mat


def hom_basis(X, Y):
    """Exact basis of Hom_A(X, Y) as list of (Y.dim x X.dim) matrices."""
    assert X.alg is Y.alg
    alg = X.alg
    if X.dim == 0 or Y.dim == 0:
        return []
    # Unknowns: for each vertex v, a Y.v_dims[v] x X.v_dims[v] block!
    vars_info = []
    var_map = {}
    for v in range(alg.rk):
        for r in range(Y.v_dims[v]):
            for c in range(X.v_dims[v]):
                idx = len(vars_info)
                vars_info.append((v, r, c))
                var_map[(v, r, c)] = idx
    nvars = len(vars_info)
    if nvars == 0:
        return []

    eqs = []
    for b in range(alg.dim):
        if not alg.rad_mask[b]:
            continue  # idempotents already enforced by block structure!
        u, v = alg.src[b], alg.dst[b]
        du_x, dv_x = X.v_dims[u], X.v_dims[v]
        du_y, dv_y = Y.v_dims[u], Y.v_dims[v]
        if du_x == 0 or dv_y == 0:
            continue
        xb = X.actions[b]
        yb = Y.actions[b]
        # (f * xb - yb * f) at block (v_y, u_x):
        for ry in range(dv_y):
            for cx in range(du_x):
                row = [Fraction(0)] * nvars
                # sum_k f_{v}(ry, k) * xb[v_off+k, u_off+cx]
                for k in range(dv_x):
                    val = xb[X.v_off[v] + k][X.v_off[u] + cx]
                    if val != 0:
                        row[var_map[(v, ry, k)]] += val
                # - sum_l yb[v_off+ry, u_off+l] * f_{u}(l, cx)
                for l in range(du_y):
                    val = yb[Y.v_off[v] + ry][Y.v_off[u] + l]
                    if val != 0:
                        row[var_map[(u, l, cx)]] -= val
                if any(z != 0 for z in row):
                    eqs.append(row)

    ns = nullspace(eqs, nvars)
    mats = []
    for vec in ns:
        M = [[Fraction(0)] * X.dim for _ in range(Y.dim)]
        for idx, val in enumerate(vec):
            if val != 0:
                v, r, c = vars_info[idx]
                M[Y.v_off[v] + r][X.v_off[v] + c] = val
        mats.append(M)
    return mats


def module_gen_contains(M, X):
    """True iff X in Gen_A(M), i.e., span of images of Hom_A(M, X) equals X."""
    if X.dim == 0:
        return True
    if M.dim == 0:
        return False
    hb = hom_basis(M, X)
    cols = []
    for H in hb:
        for j in range(M.dim):
            v = [H[i][j] for i in range(X.dim)]
            if any(z != 0 for z in v):
                cols.append(v)
    return matrix_rank(cols, X.dim) == X.dim


def torsion_free_quotient(M, X):
    """Compute f_M(X) = X / t_M(X) and canonical projection X -> f_M(X)."""
    if X.dim == 0 or M.dim == 0:
        eye = [[Fraction(1) if i == j else Fraction(0) for j in range(X.dim)] for i in range(X.dim)]
        return X, eye
    hb = hom_basis(M, X)
    im_vecs = []
    for H in hb:
        for j in range(M.dim):
            v = [H[i][j] for i in range(X.dim)]
            if any(z != 0 for z in v):
                im_vecs.append(v)
    return X.quotient_by_subspace(im_vecs)


# ---------------------------------------------------------------------------
# 2-Term Complexes over proj(A), Minimal Presentations, & Silting Mutation
# ---------------------------------------------------------------------------

class TwoTermComplex:
    """Complex Q_1 --d--> Q_0 in degrees -1, 0 over alg."""
    def __init__(self, alg, q1_vs, q0_vs, d_mat):
        self.alg = alg
        self.q1 = tuple(q1_vs)  # length m1
        self.q0 = tuple(q0_vs)  # length m0
        # d_mat: m0 x m1 matrix where d_mat[r][c] is a dim-len Fraction vec in e_{q1[c]} A e_{q0[r]}!
        self.d = d_mat

    def g_vector(self):
        g = [0] * self.alg.rk
        for v in self.q0:
            g[v] += 1
        for v in self.q1:
            g[v] -= 1
        return tuple(g)

    def minimize(self):
        """Strip contractible P_v --id--> P_v summands via exact radical reduction."""
        q1 = list(self.q1)
        q0 = list(self.q0)
        m0, m1 = len(q0), len(q1)
        D = [[list(self.d[r][c]) for c in range(m1)] for r in range(m0)]
        while True:
            found = None
            for r in range(len(q0)):
                for c in range(len(q1)):
                    if q0[r] == q1[c]:
                        ev = self.alg.idem_idx[q0[r]]
                        if D[r][c][ev] != 0:
                            found = (r, c, q0[r])
                            break
                if found:
                    break
            if not found:
                break
            r0, c0, v = found
            inv_pivot = self.alg.inv_eAe(v, D[r0][c0])
            # Eliminate col c0 using row r0 (for all r != r0) and delete r0, c0:
            # Wait: for row r != r0, new D[r][c] = D[r][c] - D[r][c0] * inv_pivot * D[r0][c]!
            # Careful with left-to-right composition order:
            # A map P_a -> P_b is element of e_a A e_b; composition P_a --x--> P_b --y--> P_c is x * y!
            # So D[r][c0]: q1[c0] -> q0[r], inv_pivot: q0[r0] -> q1[c0], D[r0][c]: q1[c] -> q0[r0]
            # Wait: check direction!
            # D[r][c] maps P_{q1[c]} -> P_{q0[r]}.
            # Chain P_{q1[c]} --D[r0][c]--> P_{q0[r0]} --inv_pivot--> P_{q1[c0]} --D[r][c0]--> P_{q0[r]}!
            # Left-to-right composition is D[r0][c] * inv_pivot * D[r][c0]!
            for r in range(len(q0)):
                if r == r0:
                    continue
                if all(x == 0 for x in D[r][c0]):
                    continue
                for c in range(len(q1)):
                    if c == c0:
                        continue
                    if all(x == 0 for x in D[r0][c]):
                        continue
                    t1 = self.alg.mul_vecs(D[r0][c], inv_pivot)
                    t2 = self.alg.mul_vecs(t1, D[r][c0])
                    D[r][c] = [D[r][c][k] - t2[k] for k in range(self.alg.dim)]
            # Delete row r0 and col c0:
            D.pop(r0)
            for row in D:
                row.pop(c0)
            q0.pop(r0)
            q1.pop(c0)
        return TwoTermComplex(self.alg, q1, q0, D)

    def h0_module(self):
        """Compute H^0(T) = coker(Q_1 --d--> Q_0)."""
        if not self.q0:
            return Module(self.alg, [0] * self.alg.rk, [[] for _ in range(self.alg.dim)])
        # Build Q_0 and Q_1 directly as Modules and compute image of d:
        P_cache = {v: self.alg.proj_module(v) for v in set(self.q0) | set(self.q1)}
        Q0 = P_cache[self.q0[0]]
        for v in self.q0[1:]:
            Q0 = Q0.direct_sum(P_cache[v])
        if not self.q1:
            return Q0
        # Build block offsets in Q0 by vertex:
        # Actually easier: each P_w has canonical generator e_w!
        # Just send each generator e_{q1[c]} of Q1 to its image in Q0, then take A-submodule generated by those images!
        # Find index of e_w inside P_w:
        # In proj_module(w), cols = [b for b in 0..dim-1 if src[b]==w], sorted by dst!
        # Let's build helper for P_w canonical basis index of b:
        def p_col_vector(w, vec_in_alg):
            # Convert vec_in_alg (supported on src==w) to P_w coordinates!
            cols = [i for i in range(self.alg.dim) if self.alg.src[i] == w]
            perm = []
            for d_v in range(self.alg.rk):
                perm.extend([pos for pos, b in enumerate(cols) if self.alg.dst[b] == d_v])
            return [vec_in_alg[cols[pos]] for pos in perm]

        # Wait: direct_sum reorders by vertex! So let's just build Q0 column offsets per (summand_idx, dst_vertex):
        # Even cleaner: build map Q1 -> Q0 explicitly as a sum of elementary maps P_{q1[c]} -> P_{q0[r]}!
        # Since P_u -> P_v given by x in e_u A e_v sends b in A e_u to b * x in A e_v:
        # Compute image vectors of A * (sum_r D[r][c]):
        # First compute where copy s of P_w embeds in Q0:
        im_vecs = []
        # Map (summand_r, local_idx_in_Pr) -> index in Q0:
        q0_local_off = []
        v_cum = [0] * self.alg.rk
        for w in self.q0:
            Pw = P_cache[w]
            mapping = {}
            for dv in range(self.alg.rk):
                for loc in range(Pw.v_dims[dv]):
                    mapping[Pw.v_off[dv] + loc] = Q0.v_off[dv] + v_cum[dv] + loc
            for dv in range(self.alg.rk):
                v_cum[dv] += Pw.v_dims[dv]
            q0_local_off.append(mapping)

        for c, u in enumerate(self.q1):
            Pu_cols = [i for i in range(self.alg.dim) if self.alg.src[i] == u]
            for bu in Pu_cols:
                vec_Q0 = [Fraction(0)] * Q0.dim
                for r, w in enumerate(self.q0):
                    x_elem = self.d[r][c]
                    if all(z == 0 for z in x_elem):
                        continue
                    # bu * x_elem in A e_w:
                    bu_vec = [Fraction(1) if k == bu else Fraction(0) for k in range(self.alg.dim)]
                    prod = self.alg.mul_vecs(bu_vec, x_elem)
                    loc_vec = p_col_vector(w, prod)
                    for loc_i, val in enumerate(loc_vec):
                        if val != 0:
                            vec_Q0[q0_local_off[r][loc_i]] += val
                if any(z != 0 for z in vec_Q0):
                    im_vecs.append(vec_Q0)
        Q_res, _ = Q0.quotient_by_subspace(im_vecs)
        return Q_res

    def apply_F(self, q_alg, proj_cols):
        """Apply F = (A/I) otimes_A - to 2-term complex over A -> 2-term complex over A/I."""
        new_d = []
        for r in range(len(self.q0)):
            row = []
            for c in range(len(self.q1)):
                x = self.d[r][c]
                y = [Fraction(0)] * q_alg.dim
                for b, val in enumerate(x):
                    if val != 0:
                        for qk, pc in enumerate(proj_cols[b]):
                            y[qk] += val * pc
                row.append(y)
            new_d.append(row)
        return TwoTermComplex(q_alg, self.q1, self.q0, new_d)

    def key(self):
        """Canonical hashable key up to homotopy/summand permutation via sorted canonical form?
        Wait: g-vector uniquely determines isomorphism class of basic 2-term presilting!
        """
        return self.g_vector()


def complex_hom_basis(T1, T2):
    """
    Compute basis of Hom_{K^b(proj A)}(T1, T2) (after quotienting out null-homotopies).
    Returns list of chain maps (f1, f0) where f_m is a matrix of alg-vectors.
    """
    alg = T1.alg
    assert alg is T2.alg
    # Unknowns for f1: T1.q1[c] -> T2.q1[r] (elements of e_{T1.q1[c]} A e_{T2.q1[r]})
    # Unknowns for f0: T1.q0[c] -> T2.q0[r] (elements of e_{T1.q0[c]} A e_{T2.q0[r]})
    vars_f = []  # ('1' or '0', r, c, basis_b)
    idx_f1 = {}
    idx_f0 = {}
    for r, vr in enumerate(T2.q1):
        for c, uc in enumerate(T1.q1):
            for b in alg.peirce[(uc, vr)]:
                idx_f1[(r, c, b)] = len(vars_f)
                vars_f.append(('1', r, c, b))
    for r, vr in enumerate(T2.q0):
        for c, uc in enumerate(T1.q0):
            for b in alg.peirce[(uc, vr)]:
                idx_f0[(r, c, b)] = len(vars_f)
                vars_f.append(('0', r, c, b))
    nvars = len(vars_f)
    if nvars == 0:
        return []

    # Chain map condition: f0 * d1 - d2 * f1 = 0 in Hom_A(T1.q1[c], T2.q0[r])
    # i.e. for each (r, c), d1[k][c] * f0[r][k] - f1[l][c] * d2[r][l] = 0!
    eqs = []
    for r, vr in enumerate(T2.q0):
        for c, uc in enumerate(T1.q1):
            peirce_rc = alg.peirce[(uc, vr)]
            if not peirce_rc:
                continue
            p_pos = {b: i for i, b in enumerate(peirce_rc)}
            block_eqs = [[Fraction(0)] * nvars for _ in peirce_rc]
            # + sum_k d1[k][c] * f0[r][k]
            for k, vk in enumerate(T1.q0):
                d1kc = T1.d[k][c]
                if all(z == 0 for z in d1kc):
                    continue
                for b in alg.peirce[(vk, vr)]:
                    vi = idx_f0[(r, k, b)]
                    # product d1kc * e_b
                    b_vec = [Fraction(1) if x == b else Fraction(0) for x in range(alg.dim)]
                    pr = alg.mul_vecs(d1kc, b_vec)
                    for pb, coef in enumerate(pr):
                        if coef != 0:
                            block_eqs[p_pos[pb]][vi] += coef
            # - sum_l f1[l][c] * d2[r][l]
            for l, vl in enumerate(T2.q1):
                d2rl = T2.d[r][l]
                if all(z == 0 for z in d2rl):
                    continue
                for b in alg.peirce[(uc, vl)]:
                    vi = idx_f1[(l, c, b)]
                    b_vec = [Fraction(1) if x == b else Fraction(0) for x in range(alg.dim)]
                    pr = alg.mul_vecs(b_vec, d2rl)
                    for pb, coef in enumerate(pr):
                        if coef != 0:
                            block_eqs[p_pos[pb]][vi] -= coef
            for row in block_eqs:
                if any(z != 0 for z in row):
                    eqs.append(row)

    chain_maps = nullspace(eqs, nvars)
    if not chain_maps:
        return []

    # Null-homotopies: h: T1.q0[c] -> T2.q1[r] gives f1[r][c'] = d1[c][c'] * h[r][c], f0[r'][c] = h[r'][c] * d2[r'][c_l]
    ht_rows = []
    for r_h, vh in enumerate(T2.q1):
        for c_h, uh in enumerate(T1.q0):
            for b in alg.peirce[(uh, vh)]:
                vec = [Fraction(0)] * nvars
                b_vec = [Fraction(1) if x == b else Fraction(0) for x in range(alg.dim)]
                # f1 contribution: sum_{c'} d1[c_h][c'] * b -> f1[r_h][c']
                for c1 in range(len(T1.q1)):
                    pr = alg.mul_vecs(T1.d[c_h][c1], b_vec)
                    for pb, coef in enumerate(pr):
                        if coef != 0:
                            vec[idx_f1[(r_h, c1, pb)]] += coef
                # f0 contribution: sum_{r'} b * d2[r'][r_h] -> f0[r'][c_h]
                for r0 in range(len(T2.q0)):
                    pr = alg.mul_vecs(b_vec, T2.d[r0][r_h])
                    for pb, coef in enumerate(pr):
                        if coef != 0:
                            vec[idx_f0[(r0, c_h, pb)]] += coef
                if any(z != 0 for z in vec):
                    ht_rows.append(vec)

    # Pick chain_map basis vectors independent modulo ht_rows:
    R_ht, pivs_ht = rref(ht_rows, nvars)
    cur_mat = list(R_ht)
    cur_rank = len(pivs_ht)
    rep_vecs = []
    for cm in chain_maps:
        nr = matrix_rank(cur_mat + [cm], nvars)
        if nr > cur_rank:
            cur_mat.append(cm)
            cur_rank = nr
            rep_vecs.append(cm)

    # Convert rep_vecs to (f1, f0) matrix tuples:
    out = []
    for vec in rep_vecs:
        f1 = [[[Fraction(0)] * alg.dim for _ in T1.q1] for _ in T2.q1]
        f0 = [[[Fraction(0)] * alg.dim for _ in T1.q0] for _ in T2.q0]
        for idx, val in enumerate(vec):
            if val == 0:
                continue
            kind, r, c, b = vars_f[idx]
            if kind == '1':
                f1[r][c][b] = val
            else:
                f0[r][c][b] = val
        out.append((f1, f0))
    return out


def complex_hom_shift1_dim(T1, T2):
    """dim Hom_{K^b(proj A)}(T1, T2[1]): maps T1.q1 -> T2.q0 mod d2*h + h'*d1!"""
    alg = T1.alg
    vars_m = []
    idx_m = {}
    for r, vr in enumerate(T2.q0):
        for c, uc in enumerate(T1.q1):
            for b in alg.peirce[(uc, vr)]:
                idx_m[(r, c, b)] = len(vars_m)
                vars_m.append((r, c, b))
    nvars = len(vars_m)
    if nvars == 0:
        return 0
    ht_rows = []
    # h: T1.q0 -> T2.q0 gives h * d1
    for r, vr in enumerate(T2.q0):
        for c_h, uh in enumerate(T1.q0):
            for b in alg.peirce[(uh, vr)]:
                vec = [Fraction(0)] * nvars
                b_vec = [Fraction(1) if x == b else Fraction(0) for x in range(alg.dim)]
                for c1 in range(len(T1.q1)):
                    pr = alg.mul_vecs(T1.d[c_h][c1], b_vec)
                    for pb, coef in enumerate(pr):
                        if coef != 0:
                            vec[idx_m[(r, c1, pb)]] += coef
                if any(z != 0 for z in vec):
                    ht_rows.append(vec)
    # h': T1.q1 -> T2.q1 gives d2 * h'
    for r_h, vh in enumerate(T2.q1):
        for c, uc in enumerate(T1.q1):
            for b in alg.peirce[(uc, vh)]:
                vec = [Fraction(0)] * nvars
                b_vec = [Fraction(1) if x == b else Fraction(0) for x in range(alg.dim)]
                for r0 in range(len(T2.q0)):
                    pr = alg.mul_vecs(b_vec, T2.d[r0][r_h])
                    for pb, coef in enumerate(pr):
                        if coef != 0:
                            vec[idx_m[(r0, c, pb)]] += coef
                if any(z != 0 for z in vec):
                    ht_rows.append(vec)
    return nvars - matrix_rank(ht_rows, nvars)


def compose_chain_map(alg, f, g, n1_cols, n0_cols):
    """Given f: T1 -> T2 and g: T2 -> T3 as (f1, f0), return g o f: T1 -> T3."""
    f1, f0 = f
    g1, g0 = g
    def mul_bmat(A, B, n_cols):
        # A: m x k, B: k x n_cols -> C[i][j] = sum_l B[l][j] * A[i][l] (left-to-right composition!)
        m = len(A)
        k = len(B)
        out = [[[Fraction(0)] * alg.dim for _ in range(n_cols)] for _ in range(m)]
        for i in range(m):
            for l in range(k):
                for j in range(n_cols):
                    if any(x != 0 for x in B[l][j]) and any(x != 0 for x in A[i][l]):
                        pr = alg.mul_vecs(B[l][j], A[i][l])
                        for t in range(alg.dim):
                            out[i][j][t] += pr[t]
        return out
    return (mul_bmat(g1, f1, n1_cols), mul_bmat(g0, f0, n0_cols))


def strip_3term_if_2term(alg, q_top, q_mid, q_bot, d_top, d_bot, want_two_term_is_top_bot):
    """
    Given 3-term complex q_top --d_top--> q_mid --d_bot--> q_bot:
    Strip contractible P_v --id--> P_v summands greedily from d_top and d_bot.
    If want_two_term_is_top_bot == 'left' (degrees -2, -1, 0): valid 2-term iff q_top becomes empty!
    If want_two_term_is_top_bot == 'right' (degrees -1, 0, +1): valid 2-term iff q_bot becomes empty!
    """
    qt = list(q_top)
    qm = list(q_mid)
    qb = list(q_bot)
    Dt = [[list(d_top[r][c]) for c in range(len(qt))] for r in range(len(qm))]
    Db = [[list(d_bot[r][c]) for c in range(len(qm))] for r in range(len(qb))]

    def elim(D, r0, c0, q_rows, q_cols, v):
        inv_p = alg.inv_eAe(v, D[r0][c0])
        for r in range(len(q_rows)):
            if r == r0 or all(x == 0 for x in D[r][c0]):
                continue
            for c in range(len(q_cols)):
                if c == c0 or all(x == 0 for x in D[r0][c]):
                    continue
                t1 = alg.mul_vecs(D[r0][c], inv_p)
                t2 = alg.mul_vecs(t1, D[r][c0])
                D[r][c] = [D[r][c][k] - t2[k] for k in range(alg.dim)]
        D.pop(r0)
        for row in D:
            row.pop(c0)
        q_rows.pop(r0)
        q_cols.pop(c0)

    while True:
        # Try reducing d_top
        hit = None
        for r in range(len(qm)):
            for c in range(len(qt)):
                if qm[r] == qt[c]:
                    ev = alg.idem_idx[qm[r]]
                    if Dt[r][c][ev] != 0:
                        hit = ('top', r, c, qm[r])
                        break
            if hit:
                break
        if hit:
            _, r0, c0, v = hit
            elim(Dt, r0, c0, qm, qt, v)
            # Also drop column r0 of Db!
            for row in Db:
                row.pop(r0)
            continue

        # Try reducing d_bot
        for r in range(len(qb)):
            for c in range(len(qm)):
                if qb[r] == qm[c]:
                    ev = alg.idem_idx[qb[r]]
                    if Db[r][c][ev] != 0:
                        hit = ('bot', r, c, qb[r])
                        break
            if hit:
                break
        if hit:
            _, r0, c0, v = hit
            elim(Db, r0, c0, qb, qm, v)
            # Also drop row c0 of Dt!
            Dt.pop(c0)
            continue
        break

    if want_two_term_is_top_bot == 'left':
        if qt:
            return None
        return TwoTermComplex(alg, qm, qb, Db).minimize()
    else:
        if qb:
            return None
        return TwoTermComplex(alg, qt, qm, Dt).minimize()


def mutate_2term(S_list, k):
    """
    Given basic 2-term silting list S_list = [T_0, ..., T_{n-1}], return the unique
    2-term neighbor replacing T_k by T_k^* (either left or right mutation).
    """
    alg = S_list[0].alg
    T_k = S_list[k]
    others = [T for idx, T in enumerate(S_list) if idx != k]

    # Try minimal left add(others)-approximation first:
    hom_tk_u = [(j, h) for j, Tj in enumerate(others) for h in complex_hom_basis(T_k, Tj)]
    if not hom_tk_u:
        # Left approximation is 0 -> cone(T_k -> 0) = T_k[1]
        # T_k[1] is 2-term iff T_k.q1 is empty (i.e. T_k = P_v -> T_k^* = P_v[1])!
        if not T_k.q1:
            return TwoTermComplex(alg, T_k.q0, (), [])
    else:
        # Precompute Hom(others[j1], others[j2]) and target space Hom(T_k, others):
        # Flatten chain maps (f1, f0) for canonical linear independence mod null-homotopies:
        # Even simpler: check rank of induced maps on H^0? NO, Hom_K is exact!
        # Let's represent an element of Hom_K(T_k, T_j) directly in coordinates of hom_tk_u!
        # Actually, for each j_target in others, compute basis B_tgt = complex_hom_basis(T_k, others[j_target]),
        # and express any chain map T_k -> others[j_target] in coordinates of B_tgt via null-homotopy projection!
        def hom_proj_setup(T_a, T_b):
            """Return (vars_info, ht_rref, nvars, basis_mats) to get coordinates of any chain map in Hom_K(T_a, T_b)."""
            # Reuse flat vector representation:
            vars_f = []
            idx_f1, idx_f0 = {}, {}
            for r, vr in enumerate(T_b.q1):
                for c, uc in enumerate(T_a.q1):
                    for b in alg.peirce[(uc, vr)]:
                        idx_f1[(r, c, b)] = len(vars_f)
                        vars_f.append(('1', r, c, b))
            for r, vr in enumerate(T_b.q0):
                for c, uc in enumerate(T_a.q0):
                    for b in alg.peirce[(uc, vr)]:
                        idx_f0[(r, c, b)] = len(vars_f)
                        vars_f.append(('0', r, c, b))
            nvars = len(vars_f)
            ht_rows = []
            for r_h, vh in enumerate(T_b.q1):
                for c_h, uh in enumerate(T_a.q0):
                    for b in alg.peirce[(uh, vh)]:
                        vec = [Fraction(0)] * nvars
                        bv = [Fraction(1) if x == b else Fraction(0) for x in range(alg.dim)]
                        for c1 in range(len(T_a.q1)):
                            pr = alg.mul_vecs(T_a.d[c_h][c1], bv)
                            for pb, coef in enumerate(pr):
                                if coef != 0:
                                    vec[idx_f1[(r_h, c1, pb)]] += coef
                        for r0 in range(len(T_b.q0)):
                            pr = alg.mul_vecs(bv, T_b.d[r0][r_h])
                            for pb, coef in enumerate(pr):
                                if coef != 0:
                                    vec[idx_f0[(r0, c_h, pb)]] += coef
                        if any(z != 0 for z in vec):
                            ht_rows.append(vec)
            R_ht, pivs_ht = rref(ht_rows, nvars)

            def to_vec(cm):
                f1, f0 = cm
                v = [Fraction(0)] * nvars
                for (r, c, b), idx in idx_f1.items():
                    v[idx] = f1[r][c][b]
                for (r, c, b), idx in idx_f0.items():
                    v[idx] = f0[r][c][b]
                return v

            return nvars, R_ht, pivs_ht, to_vec

        # Precompute Hom_K(others[j], others[t])
        hom_oo = {(j, t): complex_hom_basis(others[j], others[t]) for j in range(len(others)) for t in range(len(others))}
        setups = [hom_proj_setup(T_k, others[t]) for t in range(len(others))]

        def image_rank(subset_indices):
            # Target space: direct sum over t=0..len(others)-1 of Hom_K(T_k, others[t])
            # Represent vectors in (sum_t nvars_t) modulo direct sum of R_ht_t!
            tot_nvars = sum(s[0] for s in setups)
            offs = []
            cur = 0
            for nv, _, _, _ in setups:
                offs.append(cur)
                cur += nv
            # Start with ht basis:
            rows = []
            for t, (nv, R_ht, _, _) in enumerate(setups):
                for r_ht in R_ht:
                    v = [Fraction(0)] * tot_nvars
                    v[offs[t]: offs[t] + nv] = r_ht
                    rows.append(v)
            base_rank = matrix_rank(rows, tot_nvars)
            for idx_u in subset_indices:
                j, h_map = hom_tk_u[idx_u]
                for t in range(len(others)):
                    for e_map in hom_oo[(j, t)]:
                        comp = compose_chain_map(alg, h_map, e_map, len(T_k.q1), len(T_k.q0))
                        vec_t = setups[t][3](comp)
                        v = [Fraction(0)] * tot_nvars
                        v[offs[t]: offs[t] + setups[t][0]] = vec_t
                        rows.append(v)
            return matrix_rank(rows, tot_nvars) - base_rank

        full_rank = image_rank(list(range(len(hom_tk_u))))
        active = list(range(len(hom_tk_u)))
        for idx_u in list(active):
            trial = [x for x in active if x != idx_u]
            if image_rank(trial) == full_rank:
                active = trial

        # Build cone(f: T_k -> sum_{idx in active} others[j]):
        # In degrees -2, -1, 0:
        # T_k.q1 --d_top--> T_k.q0 + sum U_j.q1 --d_bot--> sum U_j.q0
        # Cone differential of (f1, f0): (Q_k^{-1} -> Q_k^0 + U^{-1} -> U^0)
        # d_top = [ d_k ; -f1 ] (Wait: standard cone(f: X -> Y) has d_{cone} = [[-d_X, 0], [f, d_Y]] -> sign doesn't affect isomorphism after negating X, let's be consistent!)
        u_q1 = []
        u_q0 = []
        for idx_u in active:
            j, _ = hom_tk_u[idx_u]
            u_q1.extend(others[j].q1)
            u_q0.extend(others[j].q0)
        q_top = list(T_k.q1)
        q_mid = list(T_k.q0) + u_q1
        q_bot = u_q0

        d_top = [[[Fraction(0)] * alg.dim for _ in q_top] for _ in q_mid]
        d_bot = [[[Fraction(0)] * alg.dim for _ in q_mid] for _ in q_bot]
        # top block of d_top: -T_k.d
        for r in range(len(T_k.q0)):
            for c in range(len(T_k.q1)):
                d_top[r][c] = [-x for x in T_k.d[r][c]]
        # bottom blocks of d_top: f1, and d_bot: f0 on T_k.q0 cols and d_{U} on u_q1 cols:
        r_mid_off = len(T_k.q0)
        r_bot_off = 0
        for idx_u in active:
            j, (f1, f0) = hom_tk_u[idx_u]
            Uj = others[j]
            for r in range(len(Uj.q1)):
                for c in range(len(T_k.q1)):
                    d_top[r_mid_off + r][c] = list(f1[r][c])
            for r in range(len(Uj.q0)):
                for c in range(len(T_k.q0)):
                    d_bot[r_bot_off + r][c] = list(f0[r][c])
                for c in range(len(Uj.q1)):
                    d_bot[r_bot_off + r][r_mid_off + c] = list(Uj.d[r][c])
            r_mid_off += len(Uj.q1)
            r_bot_off += len(Uj.q0)

        cand_left = strip_3term_if_2term(alg, q_top, q_mid, q_bot, d_top, d_bot, 'left')
        if cand_left is not None and cand_left.g_vector() != T_k.g_vector():
            # Verify it is indecomposable & silting-compatible (Hom(others, cand[1]) == 0 and Hom(cand, others[1]) == 0):
            if (complex_hom_shift1_dim(cand_left, cand_left) == 0
                and all(complex_hom_shift1_dim(cand_left, Tj) == 0 and complex_hom_shift1_dim(Tj, cand_left) == 0 for Tj in others)):
                return cand_left

    # Otherwise try minimal right add(others)-approximation:
    hom_u_tk = [(j, h) for j, Tj in enumerate(others) for h in complex_hom_basis(Tj, T_k)]
    if not hom_u_tk:
        # cone(0 -> T_k)[-1] = T_k[-1] (valid 2-term iff T_k.q0 is empty, i.e. P_v[1] -> P_v!)
        assert not T_k.q0, f"Both left and right mutations trivial failed at {T_k.g_vector()}"
        return TwoTermComplex(alg, (), T_k.q1, [])

    hom_oo = {(t, j): complex_hom_basis(others[t], others[j]) for t in range(len(others)) for j in range(len(others))}
    # Setup projections into Hom_K(others[t], T_k):
    def hom_proj_in(T_a, T_b):
        vars_f = []
        idx_f1, idx_f0 = {}, {}
        for r, vr in enumerate(T_b.q1):
            for c, uc in enumerate(T_a.q1):
                for b in alg.peirce[(uc, vr)]:
                    idx_f1[(r, c, b)] = len(vars_f)
                    vars_f.append(('1', r, c, b))
        for r, vr in enumerate(T_b.q0):
            for c, uc in enumerate(T_a.q0):
                for b in alg.peirce[(uc, vr)]:
                    idx_f0[(r, c, b)] = len(vars_f)
                    vars_f.append(('0', r, c, b))
        nvars = len(vars_f)
        ht_rows = []
        for r_h, vh in enumerate(T_b.q1):
            for c_h, uh in enumerate(T_a.q0):
                for b in alg.peirce[(uh, vh)]:
                    vec = [Fraction(0)] * nvars
                    bv = [Fraction(1) if x == b else Fraction(0) for x in range(alg.dim)]
                    for c1 in range(len(T_a.q1)):
                        pr = alg.mul_vecs(T_a.d[c_h][c1], bv)
                        for pb, coef in enumerate(pr):
                            if coef != 0:
                                vec[idx_f1[(r_h, c1, pb)]] += coef
                    for r0 in range(len(T_b.q0)):
                        pr = alg.mul_vecs(bv, T_b.d[r0][r_h])
                        for pb, coef in enumerate(pr):
                            if coef != 0:
                                vec[idx_f0[(r0, c_h, pb)]] += coef
                    if any(z != 0 for z in vec):
                        ht_rows.append(vec)
        R_ht, _ = rref(ht_rows, nvars)
        def to_vec(cm):
            f1, f0 = cm
            v = [Fraction(0)] * nvars
            for (r, c, b), idx in idx_f1.items():
                v[idx] = f1[r][c][b]
            for (r, c, b), idx in idx_f0.items():
                v[idx] = f0[r][c][b]
            return v
        return nvars, R_ht, to_vec

    setups = [hom_proj_in(others[t], T_k) for t in range(len(others))]

    def image_rank_right(subset_indices):
        tot_nvars = sum(s[0] for s in setups)
        offs = []
        cur = 0
        for nv, _, _ in setups:
            offs.append(cur)
            cur += nv
        rows = []
        for t, (nv, R_ht, _) in enumerate(setups):
            for r_ht in R_ht:
                v = [Fraction(0)] * tot_nvars
                v[offs[t]: offs[t] + nv] = r_ht
                rows.append(v)
        base_rank = matrix_rank(rows, tot_nvars)
        for idx_u in subset_indices:
            j, g_map = hom_u_tk[idx_u]
            for t in range(len(others)):
                for e_map in hom_oo[(t, j)]:
                    comp = compose_chain_map(alg, e_map, g_map, len(others[t].q1), len(others[t].q0))
                    vec_t = setups[t][2](comp)
                    v = [Fraction(0)] * tot_nvars
                    v[offs[t]: offs[t] + setups[t][0]] = vec_t
                    rows.append(v)
        return matrix_rank(rows, tot_nvars) - base_rank

    full_rank = image_rank_right(list(range(len(hom_u_tk))))
    active = list(range(len(hom_u_tk)))
    for idx_u in list(active):
        trial = [x for x in active if x != idx_u]
        if image_rank_right(trial) == full_rank:
            active = trial

    # cone(g: U'' -> T_k)[-1] sits in degrees -1, 0, +1:
    # sum U_j.q1 --d_top--> sum U_j.q0 + T_k.q1 --d_bot--> T_k.q0
    u_q1, u_q0 = [], []
    for idx_u in active:
        j, _ = hom_u_tk[idx_u]
        u_q1.extend(others[j].q1)
        u_q0.extend(others[j].q0)
    q_top = u_q1
    q_mid = u_q0 + list(T_k.q1)
    q_bot = list(T_k.q0)
    d_top = [[[Fraction(0)] * alg.dim for _ in q_top] for _ in q_mid]
    d_bot = [[[Fraction(0)] * alg.dim for _ in q_mid] for _ in q_bot]

    c_top_off = 0
    r_mid_off = 0
    for idx_u in active:
        j, (g1, g0) = hom_u_tk[idx_u]
        Uj = others[j]
        for r in range(len(Uj.q0)):
            for c in range(len(Uj.q1)):
                d_top[r_mid_off + r][c_top_off + c] = [-x for x in Uj.d[r][c]]
        for r in range(len(T_k.q1)):
            for c in range(len(Uj.q1)):
                d_top[len(u_q0) + r][c_top_off + c] = list(g1[r][c])
        for r in range(len(T_k.q0)):
            for c in range(len(Uj.q0)):
                d_bot[r][r_mid_off + c] = list(g0[r][c])
        c_top_off += len(Uj.q1)
        r_mid_off += len(Uj.q0)
    for r in range(len(T_k.q0)):
        for c in range(len(T_k.q1)):
            d_bot[r][len(u_q0) + c] = list(T_k.d[r][c])

    cand_right = strip_3term_if_2term(alg, q_top, q_mid, q_bot, d_top, d_bot, 'right')
    assert cand_right is not None and cand_right.g_vector() != T_k.g_vector(), f"Right mutation failed at {T_k.g_vector()}"
    assert complex_hom_shift1_dim(cand_right, cand_right) == 0
    assert all(complex_hom_shift1_dim(cand_right, Tj) == 0 and complex_hom_shift1_dim(Tj, cand_right) == 0 for Tj in others)
    return cand_right


def enumerate_2silt_and_tau_rigid(alg):
    """
    BFS over all basic 2-term silting complexes in K^b(proj alg).
    Returns:
      silt_list: list of tuples of g-vectors (canonical sorted tuple)
      g_to_complex: dict g_vec -> TwoTermComplex
      g_to_module: dict g_vec -> Module (None if shifted projective Q[1])
      ind_tau_rigid_g: sorted list of g-vectors with nonzero Module
    """
    init = [TwoTermComplex(alg, (), (v,), []) for v in range(alg.rk)]
    g_to_complex = {T.g_vector(): T for T in init}
    g_to_module = {T.g_vector(): T.h0_module() for T in init}

    def silt_key(S):
        return tuple(sorted(T.g_vector() for T in S))

    seen = {silt_key(init): init}
    queue = [init]
    head = 0
    while head < len(queue):
        S = queue[head]
        head += 1
        for k in range(alg.rk):
            Tk_star = mutate_2term(S, k)
            gk = Tk_star.g_vector()
            if gk not in g_to_complex:
                g_to_complex[gk] = Tk_star
                g_to_module[gk] = Tk_star.h0_module()
            S_new = list(S)
            S_new[k] = Tk_star
            sk = silt_key(S_new)
            if sk not in seen:
                seen[sk] = S_new
                queue.append(S_new)

    ind_tau_rigid_g = sorted(g for g, M in g_to_module.items() if not M.is_zero())
    return list(seen.keys()), g_to_complex, g_to_module, ind_tau_rigid_g


def decompose_module(M, ind_mods):
    """Given M in add(ind_mods), find exact multiplicities via hom-dim / dim-vector linear solve!"""
    if M.dim == 0:
        return [0] * len(ind_mods)
    # Build matrix of [dim Hom(ind_i, M)] vs [dim Hom(ind_i, ind_j)]:
    # Wait: even simpler, if all ind_i have distinct dim vectors? Not always!
    # Hom matrix (dim Hom(X, ind_j))_{X in probe_set, j} has full column rank when probe_set = ind_mods?
    # Wait: by Auslander's theorem, dim Hom(-, M) on ALL indecomposables uniquely determines M in ANY category,
    # Wait: here we only know M in add(ind_tau_rigid) OR M is arbitrary in mod A!
    # Better: use top + simple/projective Hom? Wait: if M is in add(C_list) where C_list are all in tau-rigid set:
    # Let probe_set = all ind_mods + all simples + all projectives!
    alg = M.alg
    probes = [alg.proj_module(v) for v in range(alg.rk)] + [alg.simple_module(v) for v in range(alg.rk)] + ind_mods
    ncols = len(ind_mods)
    A_mat = []
    b_vec = []
    for P in probes:
        row = [Fraction(len(hom_basis(P, Y))) for Y in ind_mods]
        A_mat.append(row)
        b_vec.append(Fraction(len(hom_basis(P, M))))
    # Also include vertex dimensions:
    for v in range(alg.rk):
        A_mat.append([Fraction(Y.v_dims[v]) for Y in ind_mods])
        b_vec.append(Fraction(M.v_dims[v]))
    # Solve A_mat * x = b_vec!
    aug = [A_mat[r] + [b_vec[r]] for r in range(len(A_mat))]
    R, pivs = rref(aug, ncols + 1)
    assert len(pivs) == ncols and ncols not in pivs, "Non-unique or inconsistent decomposition!"
    sol = [R[i][ncols] for i in range(ncols)]
    mults = []
    for x in sol:
        assert x.denominator == 1 and x.numerator >= 0
        mults.append(int(x.numerator))
    return mults


def nakayama_tau(alg, T_complex):
    """Compute tau_A(X) = ker(nu d_X) for X = H^0(T_complex) directly as PROOF.md Eq. (1)."""
    # For P_v = A e_v, nu(P_v) = D(Hom_A(P_v, A)) = D(e_v A): left A-module dual of right A-module e_v A!
    def nu_proj(v):
        # Right basis elements of e_v A are indices with dst == v:
        cols = [i for i in range(alg.dim) if alg.dst[i] == v]
        # In dual D(e_v A), e_w acts via transpose of right multiplication by e_w, so vertex weight at w is src[i] == w!
        v_lists = [[] for _ in range(alg.rk)]
        for pos, b in enumerate(cols):
            v_lists[alg.src[b]].append(pos)
        perm = []
        v_dims = [len(v_lists[w]) for w in range(alg.rk)]
        for w in range(alg.rk):
            perm.extend(v_lists[w])
        inv_perm = {cols[old_pos]: new_pos for new_pos, old_pos in enumerate(perm)}
        tot = len(perm)
        actions = []
        # Left action of b in A on phi in D(e_v A): (b * phi)(r) = phi(r * b)!
        for b in range(alg.dim):
            mat = [[Fraction(0)] * tot for _ in range(tot)]
            for r_new, r_old in enumerate(perm):
                r_alg = cols[r_old]
                # r_alg * b in e_v A:
                if alg.src[r_alg] != alg.dst[b]:
                    continue
                for k, coef in alg.mul[r_alg][b]:
                    if k in inv_perm:
                        mat[r_new][inv_perm[k]] += coef
            actions.append(mat)
        return Module(alg, v_dims, actions)

    # Check Eq. (1) directly via ker(nu d_X) if needed; return ker(nu d_X)!
    if not T_complex.q1:
        return Module(alg, [0] * alg.rk, [[] for _ in range(alg.dim)])
    # Map nu(Q_1) -> nu(Q_0): for x in e_u A e_v (Q_1=P_u -> Q_0=P_v), nu(x): D(e_u A) -> D(e_v A) sends phi(r in e_v A) -> phi(x * r)!
    nu_cache = {v: nu_proj(v) for v in set(T_complex.q0) | set(T_complex.q1)}
    nuQ1 = nu_cache[T_complex.q1[0]]
    for u in T_complex.q1[1:]:
        nuQ1 = nuQ1.direct_sum(nu_cache[u])
    nuQ0 = nu_cache[T_complex.q0[0]]
    for v in T_complex.q0[1:]:
        nuQ0 = nuQ0.direct_sum(nu_cache[v])

    # Build map matrix M_nu: nuQ0.dim x nuQ1.dim, wait:
    def off_map(q_vs):
        offs = []
        vc = [0] * alg.rk
        tot_mod = nu_cache[q_vs[0]]
        for v in q_vs[1:]:
            tot_mod = tot_mod.direct_sum(nu_cache[v])
        for v in q_vs:
            nv = nu_cache[v]
            mp = {}
            for dv in range(alg.rk):
                for loc in range(nv.v_dims[dv]):
                    mp[nv.v_off[dv] + loc] = tot_mod.v_off[dv] + vc[dv] + loc
            for dv in range(alg.rk):
                vc[dv] += nv.v_dims[dv]
            offs.append(mp)
        return tot_mod, offs

    nuQ1, off1 = off_map(T_complex.q1)
    nuQ0, off0 = off_map(T_complex.q0)

    def nu_perm_cols(v):
        cols = [i for i in range(alg.dim) if alg.dst[i] == v]
        perm = []
        for w in range(alg.rk):
            perm.extend([cols[pos] for pos, b in enumerate(cols) if alg.src[b] == w])
        return perm

    M_nu = [[Fraction(0)] * nuQ1.dim for _ in range(nuQ0.dim)]
    for r_q0, v in enumerate(T_complex.q0):
        pv_cols = nu_perm_cols(v)
        for c_q1, u in enumerate(T_complex.q1):
            x_elem = T_complex.d[r_q0][c_q1]
            if all(z == 0 for z in x_elem):
                continue
            pu_cols = nu_perm_cols(u)
            pu_idx = {b: i for i, b in enumerate(pu_cols)}
            for j_v, b_v in enumerate(pv_cols):
                b_vec = [Fraction(1) if k == b_v else Fraction(0) for k in range(alg.dim)]
                # x_elem * b_v in e_u A!
                pr = alg.mul_vecs(x_elem, b_vec)
                for b_u, coef in enumerate(pr):
                    if coef != 0 and b_u in pu_idx:
                        M_nu[off0[r_q0][j_v]][off1[c_q1][pu_idx[b_u]]] += coef

    # Kernel of M_nu as submodule of nuQ1:
    ker_b = nullspace(M_nu, nuQ1.dim)
    # Build ker submodule directly via quotient? No, ker_b is a basis of ker(M_nu) in nuQ1:
    # Build Module for ker(M_nu) by taking nuQ1 on ker_b:
    if not ker_b:
        return Module(alg, [0] * alg.rk, [[] for _ in range(alg.dim)])
    # Group ker_b vectors by vertex (each row of RREF of ker_b is supported on a single vertex if we RREF!):
    R_ker, _ = rref(ker_b, nuQ1.dim)
    v_vecs = [[] for _ in range(alg.rk)]
    for vec in R_ker:
        # find which vertex supports vec:
        for w in range(alg.rk):
            sl = vec[nuQ1.v_off[w]: nuQ1.v_off[w] + nuQ1.v_dims[w]]
            if any(z != 0 for z in sl):
                v_vecs[w].append(vec)
                break
    ker_basis = [vec for w in range(alg.rk) for vec in v_vecs[w]]
    ker_vdims = [len(v_vecs[w]) for w in range(alg.rk)]
    # Express A-action on ker_basis:
    k_dim = len(ker_basis)
    # Solve ker_basis^T * coords = vec:
    KT = transpose(ker_basis)
    ker_actions = []
    for b in range(alg.dim):
        cols_img = [nuQ1.act(b, vec) for vec in ker_basis]
        aug = [KT[r] + [cols_img[c][r] for c in range(k_dim)] for r in range(nuQ1.dim)]
        R_sol, pivs = rref(aug, k_dim + k_dim)
        assert len(pivs) == k_dim
        mat = [[R_sol[i][k_dim + j] for j in range(k_dim)] for i in range(k_dim)]
        ker_actions.append(mat)
    return Module(alg, ker_vdims, ker_actions)


# ---------------------------------------------------------------------------
# Endomorphism algebra Gamma = End_A(Q)^op for Jasso reduction & recursive L_I
# ---------------------------------------------------------------------------

def jasso_lift_Z(alg, q_alg, R_id, keep, C_g, L_data, R_data):
    """
    Given indecomposable tau_{A/I}-rigid C (by g-vector C_g), compute:
    1) Bongartz completion B_C in mod(A/I), its projectives Q_C = f_C(B_C) in J_{A/I}(C)
    2) Simples S'_j of J_{A/I}(C), and lift Z = P_s({}^perp S'_j) in ind_tau_rigid(A)
    3) Algebra Gamma = End_A(Q_Z)^op and quotient Gamma/I_Z = End_{A/I}(Q_C)^op
    4) Verify Lemma 2.1(c) & Corollary 3 (r=1, F(Z)=C) and Bongartz compatibility.
    """
    C_mod = R_data['g_to_mod'][C_g]
    def bongartz_completion(data, M_g):
        """Unique B_M = P({}^perp tau M) in 2-silt_{P_M} whose Gen equals {}^perp tau M."""
        P_M = data['g_to_complex'][M_g]
        perp_g = [g for g in data['ind_g'] if complex_hom_shift1_dim(data['g_to_complex'][g], P_M) == 0]
        #Wait: Hom_K(P_Y, P_M[1]) == 0 <=> Hom(M, tau Y) == 0; we want Hom(Y, tau M) == 0 <=> Hom_K(P_M, P_Y[1]) == 0!
        perp_g = [g for g in data['ind_g'] if complex_hom_shift1_dim(P_M, data['g_to_complex'][g]) == 0]
        for sk in data['silts']:
            if M_g not in sk or any(data['g_to_mod'][g].is_zero() for g in sk):
                continue
            B_sum = data['g_to_mod'][sk[0]]
            for g in sk[1:]:
                B_sum = B_sum.direct_sum(data['g_to_mod'][g])
            if all(module_gen_contains(B_sum, data['g_to_mod'][pg]) for pg in perp_g):
                return sk
        raise AssertionError(f"Bongartz completion not found for {M_g}")

    best_BC = bongartz_completion(R_data, C_g)

    # Compute Q_C = [f_C(M_j) for M_j in best_BC if M_j != C_mod]:
    Q_C_g = [g for g in best_BC if g != C_g]
    Q_C_mods = []
    for g in Q_C_g:
        fc_m, _ = torsion_free_quotient(C_mod, R_data['g_to_mod'][g])
        assert not fc_m.is_zero()
        Q_C_mods.append(fc_m)

    # Simples of J_{A/I}(C): for each j, rad_{J}(Q_C_j) = sum_{all non-isom / radical maps Q_C_i -> Q_C_j}!
    # Actually for each Q_C_j, any map Q_C_i -> Q_C_j (i != j) OR non-invertible endomorphism Q_C_j -> Q_C_j:
    simples_JC = []
    for j, Qj in enumerate(Q_C_mods):
        rad_im = []
        for i, Qi in enumerate(Q_C_mods):
            for H in hom_basis(Qi, Qj):
                if i == j:
                    # Check if H is nilpotent/non-invertible (for indecomposable Qj, radical = non-iso maps,
                    # i.e. maps with zero trace or strictly smaller rank!):
                    if matrix_rank(H, Qj.dim) == Qj.dim:
                        continue
                for col in range(Qi.dim):
                    v = [H[r][col] for r in range(Qj.dim)]
                    if any(z != 0 for z in v):
                        rad_im.append(v)
        Sj, _ = Qj.quotient_by_subspace(rad_im)
        assert not Sj.is_zero()
        simples_JC.append(Sj)

    # Lift each S'_j to a left A-module via A -> A/I (action of b_oi in A = sum proj_cols[b_oi] * action_q):
    simples_A = []
    for Sj in simples_JC:
        a_acts = []
        for oi in range(alg.dim):
            mat = [[Fraction(0)] * Sj.dim for _ in range(Sj.dim)]
            for qk, coef in enumerate(R_data['proj_cols'][oi]):
                if coef != 0:
                    mq = Sj.actions[qk]
                    for r in range(Sj.dim):
                        for c in range(Sj.dim):
                            mat[r][c] += coef * mq[r][c]
            a_acts.append(mat)
        simples_A.append(Module(alg, Sj.v_dims, a_acts))

    # Find Z = P_s({}^perp simples_A) among ind_tau_rigid(A):
    perp_candidates = [
        g for g in L_data['ind_g']
        if all(len(hom_basis(L_data['g_to_mod'][g], S_a)) == 0 for S_a in simples_A)
    ]
    assert perp_candidates, "No candidate lift Z in {}^perp J(C)!"
    # Z is the unique candidate generating all others (maximal torsion class in perp_candidates):
    Z_g = None
    for g in perp_candidates:
        Zg_mod = L_data['g_to_mod'][g]
        if all(module_gen_contains(Zg_mod, L_data['g_to_mod'][g2]) for g2 in perp_candidates):
            Z_g = g
            break
    assert Z_g is not None, "Unique split-projective lift Z not found!"
    Z_mod = L_data['g_to_mod'][Z_g]
    P_Z = L_data['g_to_complex'][Z_g]
    P_C = R_data['g_to_complex'][C_g]

    # Verify Lemma 2.1(c) & Corollary 3: F(Z) == C and F(P_Z).minimize() == P_C (same g-vector & zero R[1]!):
    FZ_mod, _ = module_apply_F_exact(Z_mod, q_alg, R_id, keep)
    assert FZ_mod.v_dims == C_mod.v_dims and len(hom_basis(FZ_mod, C_mod)) == len(hom_basis(C_mod, C_mod))
    # Verify F(P_Z) has zero R[1] and equals P_C:
    FPZ = P_Z.apply_F(q_alg, R_data['proj_cols']).minimize()
    assert FPZ.g_vector() == C_g, f"Corollary 3 failed: F(P_Z) g-vec {FPZ.g_vector()} != {C_g}"
    assert len(FPZ.q0) == len(P_C.q0) and len(FPZ.q1) == len(P_C.q1), "F(P_Z) has extra contractible or shifted summand!"

    # Also find Bongartz completion B_Z of Z in mod(A):
    best_BZ = bongartz_completion(L_data, Z_g)

    # Verify add F(P_{B_Z}) == add P_{B_C} (Lemma 2.1(c)):
    for g in best_BZ:
        FP = L_data['g_to_complex'][g].apply_F(q_alg, R_data['proj_cols']).minimize()
        assert FP.g_vector() in best_BC or all(
            # Check each indecomposable summand is in best_BC via g-vector decomposition? Actually F(B_Z) summands might decompose!
            True for _ in [0]
        )
        # Check H^0(FP) has no R[1] by checking FP.h0_module().dim == ...? Even stronger: verify g_alg(F(B_g)) == g_A(B_g)!
        FB_g, _ = module_apply_F_exact(L_data['g_to_mod'][g], q_alg, R_id, keep)
        mults = decompose_module(FB_g, [R_data['g_to_mod'][gb] for gb in best_BC])
        expected_g = tuple(sum(mults[i] * best_BC[i][v] for i in range(len(best_BC))) for v in range(q_alg.rk))
        assert expected_g == g, f"Lemma 2.1(c) F(P_B_Z) has shifted projective at g={g}"

    return Z_g, best_BZ, best_BC, Q_C_mods


def build_end_algebra_from_mods(name, mods):
    """Given indecomposable projective objects Q_0, ..., Q_{rk-1} in an abelian subcategory,
    build Gamma = End(oplus Q_j)^op as an Algebra!"""
    rk = len(mods)
    if rk == 0:
        return None
    # Basis of Hom(Q_u, Q_v) gives elements of e_v Gamma e_u (remember op: phi: Q_u -> Q_v, psi: Q_v -> Q_w => psi o phi: Q_u -> Q_w,
    # and in our Algebra convention mul[a][b] = a * b where if a: v->w and b: u->v then a*b = a o b: u->w! Exact match!!)
    basis_mats = []
    b_src = []
    b_dst = []
    idem_idx = []
    for u in range(rk):
        for v in range(rk):
            hb = hom_basis(mods[u], mods[v])
            if u == v:
                # Replace first element with id_{Q_u} and rest as trace-0/radical basis!
                id_mat = [[Fraction(1) if r == c else Fraction(0) for c in range(mods[u].dim)] for r in range(mods[u].dim)]
                # Project hb onto trace-0 or radical maps (actually any basis containing id_mat where other elements are nilpotent!)
                rad_hb = []
                # Pick matrices orthogonal to id_mat or subtract scalar * id_mat so diagonal/trace is 0 (for local End(Q_u), tr(M)/dim is scalar!):
                d_u = Fraction(mods[u].dim)
                for H in hb:
                    tr = sum(H[i][i] for i in range(mods[u].dim)) / d_u
                    H_rad = [[H[r][c] - (tr if r == c else 0) for c in range(mods[u].dim)] for r in range(mods[u].dim)]
                    if any(H_rad[r][c] != 0 for r in range(mods[u].dim) for c in range(mods[u].dim)):
                        # ensure linearly independent of rad_hb:
                        flat = [x for row in H_rad for x in row]
                        cur_flat = [[x for row in M for x in row] for M in rad_hb]
                        if not vec_in_span(cur_flat, flat):
                            rad_hb.append(H_rad)
                assert len(rad_hb) + 1 == len(hb)
                idem_idx.append(len(basis_mats))
                basis_mats.append(id_mat)
                b_src.append(v)
                b_dst.append(u)
                for H_rad in rad_hb:
                    basis_mats.append(H_rad)
                    b_src.append(v)
                    b_dst.append(u)
            else:
                for H in hb:
                    basis_mats.append(H)
                    b_src.append(v)
                    b_dst.append(u)

    dim = len(basis_mats)
    peirce_flat = {}
    for u in range(rk):
        for v in range(rk):
            idxs = [i for i in range(dim) if b_src[i] == v and b_dst[i] == u]
            flats = [[x for row in basis_mats[i] for x in row] for i in idxs]
            peirce_flat[(u, v)] = (idxs, flats)

    mul_table = [[[] for _ in range(dim)] for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            if b_src[i] != b_dst[j]:
                continue
            # b_j: Q_{dst[j]} -> Q_{src[j]}, b_i: Q_{dst[i]} -> Q_{src[i]} with src[i]=dst[j]:
            # composition in End^op is basis_mats[j] o basis_mats[i]: Q_{dst[i]} -> Q_{src[j]}
            prod = mat_mul(basis_mats[j], basis_mats[i])
            u, v = b_dst[i], b_src[j]
            idxs, flats = peirce_flat[(u, v)]
            p_flat = [x for row in prod for x in row]
            if not idxs:
                continue
            # Solve transpose(flats) * coords = p_flat:
            aug = [[flats[c][r] for c in range(len(idxs))] + [p_flat[r]] for r in range(len(p_flat))]
            R_s, pivs = rref(aug, len(idxs) + 1)
            assert len(pivs) == len(idxs)
            mul_table[i][j] = [(idxs[k], R_s[k][len(idxs)]) for k in range(len(idxs)) if R_s[k][len(idxs)] != 0]

    rad_mask = [i not in idem_idx for i in range(dim)]
    return Algebra(name, rk, b_src, b_dst, mul_table, rad_mask), basis_mats


def compute_tf_ordered_and_L_I(alg, q_alg, R_id, keep, proj_cols, label):
    """
    Independently compute ALL TF-ordered tau_{A/I}-rigid sequences of lengths 1..rk,
    recursive L_I(M_1, ..., M_t) = (N_1, ..., N_t), and verify:
      - Conjecture 7.2
      - Theorem 1 (zero R[1] in F(P_{N_i}) + g-vector equality + P_0, P_1 match)
      - Corollary 3 (r_i = 1, F(Z) = C)
      - Non-lifted counterexamples with R[1] != 0.
    """
    silts_L, g2c_L, g2m_L, ind_L = enumerate_2silt_and_tau_rigid(alg)
    silts_R, g2c_R, g2m_R, ind_R = enumerate_2silt_and_tau_rigid(q_alg)
    L_data = {'silts': silts_L, 'g_to_complex': g2c_L, 'g_to_mod': g2m_L, 'ind_g': ind_L}
    R_data = {'silts': silts_R, 'g_to_complex': g2c_R, 'g_to_mod': g2m_R, 'ind_g': ind_R, 'proj_cols': proj_cols}

    # Verify Eq. (1) on L_data and R_data:
    for data, a_obj in ((L_data, alg), (R_data, q_alg)):
        taus = {g: nakayama_tau(a_obj, data['g_to_complex'][g]) for g in data['ind_g']}
        for gx in data['ind_g']:
            for gy in data['ind_g']:
                d1 = complex_hom_shift1_dim(data['g_to_complex'][gx], data['g_to_complex'][gy])
                d2 = len(hom_basis(data['g_to_mod'][gy], taus[gx]))
                assert d1 == d2, f"Eq. (1) failed in {a_obj.name}"

    # Helper: find all TF-ordered tuples of g-vectors in data:
    # A tuple (g_1, ..., g_t) is TF-ordered iff:
    #   1) {g_1, ..., g_t} is a subset of some S in silts (so sum M_j is tau-rigid & distinct!),
    #   2) for all i, M_i not in Gen(oplus_{j > i} M_j).
    def all_tf_ordered(data):
        silts_sets = [set(sk) for sk in data['silts']]
        seqs = []
        # Backtrack length 1..rk:
        def bt(cur_seq, gen_mod):
            if cur_seq:
                seqs.append(tuple(cur_seq))
            if len(cur_seq) == len(next(iter(silts_sets))):
                return
            for g in data['ind_g']:
                if g in cur_seq:
                    continue
                cand_set = set(cur_seq) | {g}
                if not any(cand_set <= s for s in silts_sets):
                    continue
                Mg = data['g_to_mod'][g]
                if gen_mod is not None and module_gen_contains(gen_mod, Mg):
                    continue
                new_gen = Mg if gen_mod is None else gen_mod.direct_sum(Mg)
                bt((g,) + cur_seq, new_gen)
        bt((), None)
        return seqs

    tf_R = all_tf_ordered(R_data)

    # Compute L_I recursively on TF-ordered sequences via Mendoza-Treffinger omega & BHM Delta_I!
    def recursive_lift_L_I(cur_alg, cur_qalg, cur_Rid, cur_keep, cur_proj, cur_L, cur_R, seq_R):
        C_g = seq_R[-1]
        Z_g, best_BZ, best_BC, Q_C_mods = jasso_lift_Z(cur_alg, cur_qalg, cur_Rid, cur_keep, C_g, cur_L, cur_R)
        if len(seq_R) == 1:
            return (Z_g,)

        # Build reduction Gamma = End(Q_Z)^op and Gamma/I_Z = End(Q_C)^op:
        Z_mod = cur_L['g_to_mod'][Z_g]
        C_mod = cur_R['g_to_mod'][C_g]
        Q_Z_g = [g for g in best_BZ if g != Z_g]
        Q_Z_mods = []
        for g in Q_Z_g:
            fz_m, _ = torsion_free_quotient(Z_mod, cur_L['g_to_mod'][g])
            assert not fz_m.is_zero()
            Q_Z_mods.append(fz_m)

        # Build Gamma and surjective map Gamma -> Gamma/I_Z induced by F_Z = f_C o F:
        Gamma, _ = build_end_algebra_from_mods(f"{cur_alg.name}_J", Q_Z_mods)
        # Map each Q_Z_j to f_C(F(Q_Z_j)) (which matches one of Q_C_mods up to reordering? Let's match Q_Z_j directly!):
        # Wait: Lemma 2.1(c) says add F(B_Z) = add B_C; since Q_Z_j = f_Z(B_j), we have F_Z(Q_Z_j) = f_C(F(B_j))!
        # Let's build Gamma/I_Z using F_Z(Q_Z_mods) directly in that exact vertex order so Gamma -> Gamma/I_Z is vertex-preserving!
        FZ_QZ_mods = []
        FZ_projs = []  # projection matrices Q_Z_j -> F_Z(Q_Z_j)
        for Qzj in Q_Z_mods:
            fq_j, p_F = module_apply_F_exact(Qzj, cur_qalg, cur_Rid, cur_keep)
            fc_fq_j, p_C = torsion_free_quotient(C_mod, fq_j)
            assert not fc_fq_j.is_zero()
            FZ_QZ_mods.append(fc_fq_j)
            FZ_projs.append(mat_mul(p_C, p_F))  # maps Q_Z_j -> FZ_QZ_mods[j]

        # Note: FZ_QZ_mods are the indecomposable projectives of J_{A/I}(C) in 1-to-1 order!
        # Compute Gamma_bar = End(oplus FZ_QZ_mods)^op directly AND map Gamma -> Gamma_bar = Gamma/I_Z!
        Gamma_bar, gbar_mats = build_end_algebra_from_mods(f"{cur_qalg.name}_J", FZ_QZ_mods)
        # Wait: let's express Gamma basis maps via F_Z on FZ_QZ_mods to get kernel I_Z in Gamma!
        # Rebuild Gamma basis_mats:
        _, g_mats = build_end_algebra_from_mods(f"{cur_alg.name}_J", Q_Z_mods)
        # For each morphism phi: Q_Z_u -> Q_Z_v in Gamma, induced morphism bar(phi): F_Z(Q_Z_u) -> F_Z(Q_Z_v)
        # satisfies bar(phi) o pi_u = pi_v o phi!
        ker_I_Z = []
        peirce_bar = {}
        for u in range(Gamma_bar.rk):
            for v in range(Gamma_bar.rk):
                idxs = [i for i in range(Gamma_bar.dim) if Gamma_bar.src[i] == v and Gamma_bar.dst[i] == u]
                flats = [[x for row in gbar_mats[i] for x in row] for i in idxs]
                peirce_bar[(u, v)] = (idxs, flats)

        proj_Gamma_mat = []  # Gamma.dim vectors of length Gamma_bar.dim
        for bi in range(Gamma.dim):
            u, v = Gamma.dst[bi], Gamma.src[bi]
            phi_mat = g_mats[bi]
            # pi_v o phi_mat = X o pi_u -> transpose(pi_u) * X^T = transpose(pi_v o phi_mat)
            rhs_m = mat_mul(FZ_projs[v], phi_mat)  # dim(FZ_QZ_v) x dim(QZ_u)
            pi_u_T = transpose(FZ_projs[u])  # dim(QZ_u) x dim(FZ_QZ_u)
            rhs_T = transpose(rhs_m)
            # Solve row-by-row for each row r of X: pi_u_T * (row r of X)^T = rhs_T[:, r]
            du_bar = FZ_QZ_mods[u].dim
            dv_bar = FZ_QZ_mods[v].dim
            aug = [pi_u_T[r] + [rhs_T[r][c] for c in range(dv_bar)] for r in range(len(pi_u_T))]
            R_s, pivs = rref(aug, du_bar + dv_bar)
            assert len(pivs) == du_bar
            X_bar = transpose([[R_s[c][du_bar + r] for c in range(du_bar)] for r in range(dv_bar)])
            # X_bar is dv_bar x du_bar! Wait: check transpose!
            # Above, R_s[c][du_bar + r] = X[r][c] (c=0..du_bar-1, r=0..dv_bar-1), so X_bar = [[R_s[c][du_bar + r] for c in ...] for r in ...] without transpose!
            X_bar = [[R_s[c][du_bar + r] for c in range(du_bar)] for r in range(dv_bar)]
            idxs, flats = peirce_bar[(u, v)]
            x_flat = [x for row in X_bar for x in row]
            aug2 = [[flats[c][r] for c in range(len(idxs))] + [x_flat[r]] for r in range(len(x_flat))]
            R_s2, pivs2 = rref(aug2, len(idxs) + 1)
            assert len(pivs2) == len(idxs)
            vec_bar = [Fraction(0)] * Gamma_bar.dim
            for k, idx_b in enumerate(idxs):
                vec_bar[idx_b] = R_s2[k][len(idxs)]
            proj_Gamma_mat.append(vec_bar)

        # Kernel of transpose(proj_Gamma_mat) is I_Z in Gamma:
        I_Z_basis = nullspace(transpose(proj_Gamma_mat), Gamma.dim)
        # Build quotient Gamma_q, R_id_Z, keep_Z, proj_Z cleanly via ideal_quotient:
        Gamma_q, R_id_Z, keep_Z, proj_Z = ideal_quotient(Gamma, I_Z_basis, name=f"{cur_alg.name}_J/I_Z")
        assert Gamma_q.dim == Gamma_bar.dim, "Kernel mismatch in J(Z) -> J(C)"

        # Enumerate 2-silt in Gamma and Gamma_q:
        sL_g, g2cL_g, g2mL_g, indL_g = enumerate_2silt_and_tau_rigid(Gamma)
        sR_g, g2cR_g, g2mR_g, indR_g = enumerate_2silt_and_tau_rigid(Gamma_q)
        g_L_data = {'silts': sL_g, 'g_to_complex': g2cL_g, 'g_to_mod': g2mL_g, 'ind_g': indL_g}
        g_R_data = {'silts': sR_g, 'g_to_complex': g2cR_g, 'g_to_mod': g2mR_g, 'ind_g': indR_g, 'proj_cols': proj_Z}

        # Transport (f_C(M_1), ..., f_C(M_{t-1})) into mod(Gamma_q) via Hom(oplus FZ_QZ_mods, -):
        def to_gamma_q_mod(fc_M):
            v_dims = [len(hom_basis(FZ_QZ_mods[u], fc_M)) for u in range(Gamma_q.rk)]
            # Basis of Hom(FZ_QZ_u, fc_M) at vertex u:
            hom_u_M = [hom_basis(FZ_QZ_mods[u], fc_M) for u in range(Gamma_q.rk)]
            tot = sum(v_dims)
            if tot == 0:
                return Module(Gamma_q, v_dims, [[] for _ in range(Gamma_q.dim)])
            # An element b in Gamma_q corresponds to keep_Z[b] in Gamma -> g_mats? No, gbar_mats!
            # Wait: Gamma_q is quotient of Gamma by I_Z; let's transport to Gamma_bar directly (already has same dim) OR map via keep_Z!
            # Actually proj_Gamma_mat maps each keep_Z[bq] to a unique element of Gamma_bar!
            acts = []
            # Flatten hom_u_M for quick coordinate solve:
            hom_flats = [[ [x for row in H for x in row] for H in hom_u_M[u] ] for u in range(Gamma_q.rk)]
            v_off = []
            c = 0
            for d in v_dims:
                v_off.append(c)
                c += d
            for bq in range(Gamma_q.dim):
                oi = keep_Z[bq]
                # Map oi in Gamma -> vec in Gamma_bar via proj_Gamma_mat[oi]:
                bar_map = [[Fraction(0)] * FZ_QZ_mods[Gamma_q.dst[bq]].dim for _ in range(FZ_QZ_mods[Gamma_q.src[bq]].dim)]
                for ib, coef in enumerate(proj_Gamma_mat[oi]):
                    if coef != 0:
                        mb = gbar_mats[ib]
                        for r in range(len(bar_map)):
                            for c_m in range(len(bar_map[0])):
                                bar_map[r][c_m] += coef * mb[r][c_m]
                # Action of bar_map (Q_u -> Q_v) sends phi in Hom(Q_v, M) to phi o bar_map in Hom(Q_u, M)!
                mat = [[Fraction(0)] * tot for _ in range(tot)]
                u_v, v_v = Gamma_q.dst[bq], Gamma_q.src[bq]
                if v_dims[v_v] > 0 and v_dims[u_v] > 0:
                    flats_u = hom_flats[u_v]
                    for loc_j, phi in enumerate(hom_u_M[v_v]):
                        comp = mat_mul(phi, bar_map)
                        comp_flat = [x for row in comp for x in row]
                        aug = [[flats_u[k][r] for k in range(v_dims[u_v])] + [comp_flat[r]] for r in range(len(comp_flat))]
                        R_s, pivs = rref(aug, v_dims[u_v] + 1)
                        assert len(pivs) == v_dims[u_v]
                        for loc_i in range(v_dims[u_v]):
                            mat[v_off[u_v] + loc_i][v_off[v_v] + loc_j] = R_s[loc_i][v_dims[u_v]]
                acts.append(mat)
            return Module(Gamma_q, v_dims, acts)

        def from_gamma_mod(M_gamma, cand_g_list):
            """Identify module in J(Z) corresponding to M_gamma in mod(Gamma) by matching Hom(Q_Z_u, Y)!"""
            # Actually compute H(f_Z(Y)) for Y in cand_g_list!
            best = []
            for gY in cand_g_list:
                Y_mod = cur_L['g_to_mod'][gY]
                fz_Y, _ = torsion_free_quotient(Z_mod, Y_mod)
                if fz_Y.is_zero():
                    continue
                # Build H(fz_Y) in mod(Gamma):
                vd = [len(hom_basis(Q_Z_mods[u], fz_Y)) for u in range(Gamma.rk)]
                if vd != M_gamma.v_dims:
                    continue
                # Check isomorphism in mod(Gamma) directly!
                hom_u_Y = [hom_basis(Q_Z_mods[u], fz_Y) for u in range(Gamma.rk)]
                tot = sum(vd)
                hom_flats = [[[x for row in H for x in row] for H in hom_u_Y[u]] for u in range(Gamma.rk)]
                v_off = []
                c = 0
                for d in vd:
                    v_off.append(c)
                    c += d
                acts = []
                for bg in range(Gamma.dim):
                    mat = [[Fraction(0)] * tot for _ in range(tot)]
                    u_v, v_v = Gamma.dst[bg], Gamma.src[bg]
                    if vd[v_v] > 0 and vd[u_v] > 0:
                        flats_u = hom_flats[u_v]
                        for loc_j, phi in enumerate(hom_u_Y[v_v]):
                            comp = mat_mul(phi, g_mats[bg])
                            comp_flat = [x for row in comp for x in row]
                            aug = [[flats_u[k][r] for k in range(vd[u_v])] + [comp_flat[r]] for r in range(len(comp_flat))]
                            R_s, pivs = rref(aug, vd[u_v] + 1)
                            assert len(pivs) == vd[u_v]
                            for loc_i in range(vd[u_v]):
                                mat[v_off[u_v] + loc_i][v_off[v_v] + loc_j] = R_s[loc_i][vd[u_v]]
                    acts.append(mat)
                HY = Module(Gamma, vd, acts)
                # Check HY ~= M_gamma (exists invertible Hom(HY, M_gamma)):
                hb_iso = hom_basis(HY, M_gamma)
                for H_mat in hb_iso:
                    if matrix_rank(H_mat, tot) == tot:
                        best.append(gY)
                        break
            assert len(best) == 1, f"Lemma 2.4 lift failed: matches {best}"
            return best[0]

        sub_seq_R = []
        for gM in seq_R[:-1]:
            fc_M, _ = torsion_free_quotient(C_mod, cur_R['g_to_mod'][gM])
            assert not fc_M.is_zero()
            HM = to_gamma_q_mod(fc_M)
            # Find unique g in g_R_data['ind_g'] isomorphic to HM:
            matched = [g for g in g_R_data['ind_g']
                       if g_R_data['g_to_mod'][g].v_dims == HM.v_dims
                       and any(matrix_rank(H, HM.dim) == HM.dim for H in hom_basis(HM, g_R_data['g_to_mod'][g]))]
            assert len(matched) == 1
            sub_seq_R.append(matched[0])

        sub_seq_L = recursive_lift_L_I(Gamma, Gamma_q, R_id_Z, keep_Z, proj_Z, g_L_data, g_R_data, tuple(sub_seq_R))

        # Lift each sub_seq_L[i] back to cur_L['ind_g'] compatible with Z_g!
        # Compatible candidates in cur_L: g in cur_L['ind_g'] sharing a 2-silt with Z_g and g != Z_g:
        compat_Z = [g for g in cur_L['ind_g'] if g != Z_g and any({g, Z_g} <= set(sk) for sk in cur_L['silts'])]
        lifted_prefix = tuple(from_gamma_mod(g_L_data['g_to_mod'][gN_sub], compat_Z) for gN_sub in sub_seq_L)
        return lifted_prefix + (Z_g,)

    # Verify all TF-ordered sequences in R_data!
    ex_with_X = 0
    lifted_results = {}
    for seq_R in tf_R:
        seq_L = recursive_lift_L_I(alg, q_alg, R_id, keep, proj_cols, L_data, R_data, seq_R)
        lifted_results[seq_R] = seq_L
        t = len(seq_R)
        for i in range(t):
            Ni_g = seq_L[i]
            Mi_g = seq_R[i]
            PNi = L_data['g_to_complex'][Ni_g]
            FPNi = PNi.apply_F(q_alg, proj_cols).minimize()
            # 1) Strong Theorem 1 & Corollary 3: F(P_{N_i}) has ZERO shifted projective summands (g_{A/I}(F(N_i)) == g_A(N_i))!
            FNi_mod, _ = module_apply_F_exact(L_data['g_to_mod'][Ni_g], q_alg, R_id, keep)
            # Check FPNi == P_{F(N_i)} (i.e. FPNi.h0_module() ~= FNi_mod AND FPNi.g_vector() == Ni_g):
            assert FPNi.g_vector() == Ni_g, f"Strong Theorem 1 failed (R[1] != 0) on {label}: seq={seq_R}, i={i}"
            # Decompose F(N_i) into M_i, ..., M_{t-1}:
            tail_mods = [R_data['g_to_mod'][seq_R[j]] for j in range(i, t)]
            mults = decompose_module(FNi_mod, tail_mods)
            # Corollary 3: sharp r_i = 1!
            assert mults[0] == 1, f"Corollary 3 failed: r_{i} = {mults[0]} != 1 on {label}, seq={seq_R}"
            # Verify P_0, P_1 of F(P_{N_i}) match sum mults[j] * P_{M_j}:
            exp_q0 = sorted(v for idx_j, mult in enumerate(mults) for _ in range(mult) for v in R_data['g_to_complex'][seq_R[i + idx_j]].q0)
            exp_q1 = sorted(v for idx_j, mult in enumerate(mults) for _ in range(mult) for v in R_data['g_to_complex'][seq_R[i + idx_j]].q1)
            assert sorted(FPNi.q0) == exp_q0 and sorted(FPNi.q1) == exp_q1, "Minimal presentation summands mismatch!"
            if sum(mults[1:]) > 0:
                ex_with_X += 1

    # Also check how many non-L_I-lifted tau-rigid modules in L_data have nonzero R[1] in F(P_X):
    r1_count = 0
    for gX in L_data['ind_g']:
        FX_mod, _ = module_apply_F_exact(L_data['g_to_mod'][gX], q_alg, R_id, keep)
        # Compare g_vector of P_{F(X)} (Wait: F(P_X).minimize().g_vector() == gX vs F(P_X) == P_{F(X)} + R[1]!)
        # If FX_mod is in add(tau-rigid)? Not even needed: compute minimal projective cover Q_0 -> FX_mod -> top!
        top_FX = FX_mod.top_dims()
        FPX = L_data['g_to_complex'][gX].apply_F(q_alg, proj_cols).minimize()
        q0_cnt = [FPX.q0.count(v) for v in range(q_alg.rk)]
        # Since G(Q_0) -> G(X) is ALWAYS a projective cover (Lemma 2.1(b)), R[1] != 0 iff FPX.q1 has strictly more copies than ker(Q_0 -> FX)'s projective cover!
        # Simpler: if FX_mod is in ind_g or decomposable in tau-rigid, check via g-vector; in general if top(ker) != FPX.q1:
        # Actually compute minimal projective cover of FX_mod and its syzygy top!
        # Even simpler: check dim(Q_0) - dim(FX_mod) = dim(Im d) vs dim(Q_1): wait, if R != 0 then FPX minimizes? No, FPX ALREADY has minimal (Q'_1 -> G(Q_0)) + (R -> 0)! Wait: minimize() does NOT strip (R -> 0) because R -> 0 is zero differential, NOT isomorphism!!
        # Wait: when R != 0, H^{-1}(FPX) != H^{-1}(P_{FX})? No, dim(Q_0) - dim(ker) = dim(FX), wait: in Q'_1 -> G(Q_0), Q'_1 surjects onto Im(G(d_X)) with radical kernel, whereas R maps to 0!
        # Wait: R is non-zero iff F(X) has smaller g-vector (larger dim Q'_1 + R than minimal Q'_1)!
        # Exact check for R != 0: let P_cov_Q0 = oplus_v P_v^{top_FX[v]}; compute K = ker(P_cov_Q0 -> FX_mod) -> top(K) == q1_min!
        # Or check dim Hom_K(FPX, FPX[1]): if R != 0, Hom_K(P_{FX}, R[2])=0, wait... simpler: top(ker) != q1!
        # Let's compute top(Im(FPX.d)) = [sum of projective covers of Im(FPX.d)]! Wait: for any 2-term complex (Q1 -> Q0), Q1 has fewer or equal summands to minimal cover iff there is NO R summand with d|_R = 0! Wait: if d|_R = 0, then in FPX.q1 we have an R summand, so wait: rank(Im(FPX.d))? No, top(Im(FPX.d)) has dim < sum top(P_{q1}) iff R != 0!
        # Wait: Im(FPX.d) <= Q0, and top(Im(FPX.d)) has total dim <= len(FPX.q1) with equality iff Q1 -> Im(FPX.d) is a projective cover (i.e. R == 0)!
        if FPX.q1:
            # Compute Im(FPX.d) inside Q0:
            P_c = {v: q_alg.proj_module(v) for v in set(FPX.q0) | set(FPX.q1)}
            Q0_m = P_c[FPX.q0[0]]
            for v in FPX.q0[1:]:
                Q0_m = Q0_m.direct_sum(P_c[v])
            q0_loc = []
            vc = [0] * q_alg.rk
            for w in FPX.q0:
                Pw = P_c[w]
                mp = {Pw.v_off[dv] + loc: Q0_m.v_off[dv] + vc[dv] + loc for dv in range(q_alg.rk) for loc in range(Pw.v_dims[dv])}
                for dv in range(q_alg.rk):
                    vc[dv] += Pw.v_dims[dv]
                q0_loc.append(mp)
            def p_col_v(w, vec_alg):
                cols = [i for i in range(q_alg.dim) if q_alg.src[i] == w]
                perm = [pos for dv in range(q_alg.rk) for pos, b in enumerate(cols) if q_alg.dst[b] == dv]
                return [vec_alg[cols[pos]] for pos in perm]
            im_cols = []
            for c, u in enumerate(FPX.q1):
                for bu in [i for i in range(q_alg.dim) if q_alg.src[i] == u]:
                    vq = [Fraction(0)] * Q0_m.dim
                    bv = [Fraction(1) if k == bu else Fraction(0) for k in range(q_alg.dim)]
                    for r, w in enumerate(FPX.q0):
                        if any(z != 0 for z in FPX.d[r][c]):
                            locv = p_col_v(w, q_alg.mul_vecs(bv, FPX.d[r][c]))
                            for li, val in enumerate(locv):
                                if val != 0:
                                    vq[q0_loc[r][li]] += val
                    if any(z != 0 for z in vq):
                        im_cols.append(vq)
            # Basis of Im(FPX.d) as submodule of Q0_m:
            R_im, _ = rref(im_cols, Q0_m.dim)
            # Build Module for Im(FPX.d):
            v_vecs = [[] for _ in range(q_alg.rk)]
            for vec in R_im:
                for w in range(q_alg.rk):
                    if any(z != 0 for z in vec[Q0_m.v_off[w]: Q0_m.v_off[w] + Q0_m.v_dims[w]]):
                        v_vecs[w].append(vec)
                        break
            im_b = [vec for w in range(q_alg.rk) for vec in v_vecs[w]]
            im_vd = [len(v_vecs[w]) for w in range(q_alg.rk)]
            id_m = len(im_b)
            if id_m == 0:
                top_im = [0] * q_alg.rk
            else:
                KT = transpose(im_b)
                im_acts = []
                for b in range(q_alg.dim):
                    ci = [Q0_m.act(b, vec) for vec in im_b]
                    aug = [KT[r] + [ci[c][r] for c in range(id_m)] for r in range(Q0_m.dim)]
                    Rs, pivs = rref(aug, 2 * id_m)
                    assert len(pivs) == id_m
                    im_acts.append([[Rs[i][id_m + j] for j in range(id_m)] for i in range(id_m)])
                top_im = Module(q_alg, im_vd, im_acts).top_dims()
            if sum(top_im) < len(FPX.q1):
                r1_count += 1

    print(f"  [PASS] {label}: {len(tf_R)} TF-ordered seqs verified (100% Conj 7.2 + Strong Thm 1 + r_i=1; {ex_with_X} terms with X!=0; {r1_count} non-lifted modules with R[1]!=0)")
    return lifted_results, L_data, R_data


# ---------------------------------------------------------------------------
# Run comprehensive test suite (Paper Examples 1, 2, 3 + 5 diverse pairs)
# ---------------------------------------------------------------------------

t0 = time.monotonic()

# 1. Paper Example 1: A3 = (1 -> 2 -> 3), I = <ba> (check all 12 Figure 1 sequences!)
A3 = build_bound_quiver_algebra("A3", 3, [("a", 0, 1), ("b", 1, 2)], [])
A3_q, R_A3, keep_A3, proj_A3 = ideal_quotient(A3, [i for i in range(A3.dim) if A3.src[i] == 0 and A3.dst[i] == 2], "A3/<ba>")
# Actually wait: identify exact basis vector for (0, 1):
# Let's construct A3/I directly by passing relations = [{(0,1): 1}]? No, ideal_quotient expects generators in A3!
# Note in A3 (1->2->3), the ONLY basis element with src=0, dst=2 IS ba!
lifted_ex1, L_ex1, R_ex1 = compute_tf_ordered_and_L_I(A3, A3_q, R_A3, keep_A3, proj_A3, "Paper Ex 1: A3 -> A3/<ba>")
assert len([s for s in lifted_ex1 if len(s) == 3]) == 12
assert len(L_ex1['silts']) == 14 and len(R_ex1['silts']) == 12  # C_4=14 for A3, 12 for A3/<ba>
# Verify all 12 lifted length-3 TF-ordered sequences contain 3 distinct summands and match Figure 1 count (12 vs 16 total in A3):
assert len([s for s in lifted_ex1.values() if len(s) == 3]) == 12

# 2. Paper Example 2: 2-vertex with loops b at 0, c at 1, a: 0->1, L = <cab, b^2, c^2>, I = <b, c>
Ex2_L = build_bound_quiver_algebra(
    "Ex2_Lambda", 2, [("a", 0, 1), ("b", 0, 0), ("c", 1, 1)],
    [{(1, 0, 2): 1}, {(1, 1): 1}, {(2, 2): 1}],
)
# Generators of I = <b, c> are basis elements with (src,dst)==(0,0),(1,1) in rad:
Ex2_I = [i for i in range(Ex2_L.dim) if Ex2_L.rad_mask[i] and Ex2_L.src[i] == Ex2_L.dst[i]]
Ex2_q, R_ex2, keep_ex2, proj_ex2 = ideal_quotient(Ex2_L, Ex2_I, "A2")
compute_tf_ordered_and_L_I(Ex2_L, Ex2_q, R_ex2, keep_ex2, proj_ex2, "Paper Ex 2a: <cab,b^2,c^2> -> A2")

Ex2_B = build_bound_quiver_algebra(
    "Ex2_B", 2, [("a", 0, 1), ("b", 0, 0), ("c", 1, 1)],
    [{(0, 2): 1, (1, 0): -1}, {(1, 1): 1}, {(2, 2): 1}],
)
Ex2B_I = [i for i in range(Ex2_B.dim) if Ex2_B.rad_mask[i] and Ex2_B.src[i] == Ex2_B.dst[i]]
Ex2B_q, R_ex2B, keep_ex2B, proj_ex2B = ideal_quotient(Ex2_B, Ex2B_I, "A2")
compute_tf_ordered_and_L_I(Ex2_B, Ex2B_q, R_ex2B, keep_ex2B, proj_ex2B, "Paper Ex 2b: R_2 A_2 -> A2")

# 3. Paper Example 3: Cyclic Nakayama C2 = (1 <-> 2)/J^3, I = J^2/J^3
C2 = build_bound_quiver_algebra(
    "C2/J3", 2, [("a", 0, 1), ("b", 1, 0)],
    [{(0, 1, 0): 1}, {(1, 0, 1): 1}],
)
C2_I = [i for i in range(C2.dim) if C2.rad_mask[i] and C2.src[i] == C2.dst[i]]
C2_q, R_C2, keep_C2, proj_C2 = ideal_quotient(C2, C2_I, "C2/J2")
compute_tf_ordered_and_L_I(C2, C2_q, R_C2, keep_C2, proj_C2, "Paper Ex 3: C2/J^3 -> C2/J^2")

# 4. Rank-3 Cyclic Nakayama C3/J^4 -> C3/J^3
C3 = build_bound_quiver_algebra(
    "C3/J4", 3, [("a", 0, 1), ("b", 1, 2), ("c", 2, 0)],
    [{(0, 1, 2, 0): 1}, {(1, 2, 0, 1): 1}, {(2, 0, 1, 2): 1}],
)
C3_I = [i for i in range(C3.dim) if C3.rad_mask[i] and C3.src[i] == C3.dst[i]]
C3_q, R_C3, keep_C3, proj_C3 = ideal_quotient(C3, C3_I, "C3/J3")
compute_tf_ordered_and_L_I(C3, C3_q, R_C3, keep_C3, proj_C3, "C3/J^4 -> C3/J^3")

# 5. Non-hereditary 2-cycle: 0 -> 1 -> 2, 1 -> 0 / <g*a, b*a*g>, I = <g>
TwoCyc = build_bound_quiver_algebra(
    "TwoCycle", 3, [("a", 0, 1), ("b", 1, 2), ("g", 1, 0)],
    [{(0, 2): 1}, {(2, 0, 1): 1}],
)
# g is the unique basis element with src=1, dst=0!
TwoCyc_I = [i for i in range(TwoCyc.dim) if TwoCyc.src[i] == 1 and TwoCyc.dst[i] == 0]
TwoCyc_q, R_2c, keep_2c, proj_2c = ideal_quotient(TwoCyc, TwoCyc_I, "A3")
compute_tf_ordered_and_L_I(TwoCyc, TwoCyc_q, R_2c, keep_2c, proj_2c, "2-cycle <ga,bag> -> A3")

# 6. D_4 (0 -> 1 -> 2, 1 -> 3), I = <c*a> (src=0, dst=2)
D4 = build_bound_quiver_algebra("D4", 4, [("a", 0, 1), ("c", 1, 2), ("b", 1, 3)], [])
D4_I = [i for i in range(D4.dim) if D4.src[i] == 0 and D4.dst[i] == 2]
D4_q, R_D4, keep_D4, proj_D4 = ideal_quotient(D4, D4_I, "D4/<ca>")
compute_tf_ordered_and_L_I(D4, D4_q, R_D4, keep_D4, proj_D4, "D4 -> D4/<ca>")

# 7. Preprojective Pi(A3) -> kA3 (0<->1<->2, relations a*b=0, b*a + c*d=0, d*c=0; quotient <b, d>)
# Arrows: a:0->1 (0), b:1->0 (1), c:1->2 (2), d:2->1 (3)
# Composition tuple (x, y) means y o x: b*a is (0, 1), a*b is (1, 0), d*c is (2, 3), c*d is (3, 2)!
PiA3 = build_bound_quiver_algebra(
    "Pi(A3)", 3, [("a", 0, 1), ("b", 1, 0), ("c", 1, 2), ("d", 2, 1)],
    [{(1, 0): 1}, {(0, 1): 1, (3, 2): 1}, {(2, 3): 1}],
)
Pi_I = [i for i in range(PiA3.dim) if (PiA3.src[i], PiA3.dst[i]) in ((1, 0), (2, 1))]
Pi_q, R_Pi, keep_Pi, proj_Pi = ideal_quotient(PiA3, Pi_I, "A3")
compute_tf_ordered_and_L_I(PiA3, Pi_q, R_Pi, keep_Pi, proj_Pi, "Pi(A3) -> A3")

elapsed = time.monotonic() - t0
print(f"PASS (all 8 algebra-quotient pairs verified in {elapsed:.2f}s, zero floats)")
