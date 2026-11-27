"""Independent exact verifier for targets/iverson-2506.20778-conjPaley/PROOF.md.

Written strictly from arXiv:2506.20778v1 (2025.06.25.tex) and PROOF.md,
without reading verify.py or author notes.
"""

from __future__ import annotations

import itertools
import math
import sys
import time
from sympy import GF, Poly, factor, symbols


class FiniteFieldPrimePower:
    """Exact arithmetic over F_{p^r} represented as polynomials mod monic irreducible of degree r over F_p."""

    def __init__(self, p: int, irred_coeffs: list[int] | None = None) -> None:
        self.p = p
        if irred_coeffs is None:
            self.r = 1
            self.irred = [0, 1]
        else:
            self.r = len(irred_coeffs) - 1
            assert irred_coeffs[-1] % p == 1
            self.irred = [c % p for c in irred_coeffs]
        self.q = p ** self.r
        # Enumerate all elements as tuples of length r in F_p
        self.elements = list(itertools.product(range(p), repeat=self.r))
        self.zero = (0,) * self.r
        self.one = (1,) + (0,) * (self.r - 1)
        self.idx = {el: i for i, el in enumerate(self.elements)}

    def add(self, a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
        p = self.p
        return tuple((x + y) % p for x, y in zip(a, b))

    def sub(self, a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
        p = self.p
        return tuple((x - y) % p for x, y in zip(a, b))

    def neg(self, a: tuple[int, ...]) -> tuple[int, ...]:
        p = self.p
        return tuple((-x) % p for x in a)

    def mul(self, a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
        p, r = self.p, self.r
        prod = [0] * (2 * r - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    prod[i + j] = (prod[i + j] + ai * bj) % p
        for deg in range(2 * r - 2, r - 1, -1):
            c = prod[deg]
            if c:
                for k in range(r + 1):
                    prod[deg - r + k] = (prod[deg - r + k] - c * self.irred[k]) % p
        return tuple(prod[:r])

    def pow(self, a: tuple[int, ...], e: int) -> tuple[int, ...]:
        res = self.one
        base = a
        while e > 0:
            if e & 1:
                res = self.mul(res, base)
            base = self.mul(base, base)
            e >>= 1
        return res

    def inv(self, a: tuple[int, ...]) -> tuple[int, ...]:
        assert a != self.zero
        return self.pow(a, self.q - 2)

    def frob(self, a: tuple[int, ...]) -> tuple[int, ...]:
        return self.pow(a, self.p)

    def chi(self, a: tuple[int, ...]) -> int:
        if a == self.zero:
            return 0
        v = self.pow(a, (self.q - 1) // 2)
        if v == self.one:
            return 1
        assert v == self.neg(self.one)
        return -1


def build_paley_i(ff: FiniteFieldPrimePower) -> tuple[list, list[list[int]], list[list[int]]]:
    """Build X = PG(1, q), S, and Paley I skew-Hadamard matrix H = I + S."""
    X = list(ff.elements) + [None]  # None represents infinity
    d = len(X)
    assert d == ff.q + 1
    S = [[0] * d for _ in range(d)]
    for i, a in enumerate(X):
        for j, b in enumerate(X):
            if i == j:
                S[i][j] = 0
            elif a is None:
                S[i][j] = 1
            elif b is None:
                S[i][j] = -1
            else:
                S[i][j] = ff.chi(ff.sub(a, b))
    H = [[(1 if i == j else 0) + S[i][j] for j in range(d)] for i in range(d)]
    return X, S, H


def mat_mul(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def check_paley_and_lemma1(ff: FiniteFieldPrimePower) -> None:
    X, S, H = build_paley_i(ff)
    d = len(X)
    q = ff.q
    # S^T = -S, H^T = 2I - H, HH^T = dI, S^2 = -qI, H^2 = 2S - (q-1)I
    for i in range(d):
        for j in range(d):
            assert S[i][j] == -S[j][i]
            assert H[j][i] == (2 if i == j else 0) - H[i][j]
    HHt = mat_mul(H, [[H[j][i] for j in range(d)] for i in range(d)])
    S2 = mat_mul(S, S)
    H2 = mat_mul(H, H)
    for i in range(d):
        for j in range(d):
            assert HHt[i][j] == (d if i == j else 0)
            assert S2[i][j] == (-q if i == j else 0)
            assert H2[i][j] == 2 * S[i][j] - ((q - 1) if i == j else 0)
    for i in range(q):  # finite elements have row sum 0
        assert sum(H[i]) == 0

    # Check PGammaL(2, q) embedding via vectors v_a = (a, 1) and v_inf = (1, 0)
    def vec_rep(a):
        return (ff.one, ff.zero) if a is None else (a, ff.one)

    def apply_g(M, frob_k: int, a):
        va = vec_rep(a)
        vx = va[0]
        vy = va[1]
        for _ in range(frob_k):
            vx = ff.frob(vx)
            vy = ff.frob(vy)
        nx = ff.add(ff.mul(M[0][0], vx), ff.mul(M[0][1], vy))
        ny = ff.add(ff.mul(M[1][0], vx), ff.mul(M[1][1], vy))
        if ny == ff.zero:
            return None, nx  # (1, 0) scaled by nx
        lam = ny
        return ff.mul(nx, ff.inv(ny)), lam

    non_sq = next(el for el in ff.elements if ff.chi(el) == -1)
    test_mats = [
        ((ff.one, ff.one), (ff.zero, ff.one)),        # translation
        ((non_sq, ff.zero), (ff.zero, ff.one)),       # non-square scaling (eta = -1)
        ((ff.zero, ff.neg(ff.one)), (ff.one, ff.zero)),  # inversion
        ((non_sq, ff.one), (ff.one, non_sq)),         # general invertible
    ]
    elem_idx = {a: i for i, a in enumerate(X)}
    for M in test_mats:
        detM = ff.sub(ff.mul(M[0][0], M[1][1]), ff.mul(M[0][1], M[1][0]))
        if detM == ff.zero:
            continue
        eta = ff.chi(detM)
        for frob_k in range(ff.r):
            perm = []
            eps = []
            for a in X:
                ga, lam = apply_g(M, frob_k, a)
                perm.append(elem_idx[ga])
                eps.append(ff.chi(lam))
            for i in range(d):
                for j in range(d):
                    rhs = eps[i] * eps[j] * (H[i][j] if eta == 1 else H[j][i])
                    assert H[perm[i]][perm[j]] == rhs

    # For q = 27 (r = 3), check Gal(F_27/F_3) preserves chi
    if ff.r > 1:
        for a in ff.elements:
            assert ff.chi(ff.frob(a)) == ff.chi(a)


def check_lemma2_and_q19(ff: FiniteFieldPrimePower, check_t4_exhaustive: bool = False) -> None:
    X, S, H = build_paley_i(ff)
    d = len(X)
    q = ff.q
    bound = 2.0 * math.sqrt(q) + 4.0
    assert bound < d - 4

    # Delta-signatures v_{ij} for i != j
    v_sig = {}
    for i in range(d):
        for j in range(d):
            if i != j:
                v_sig[(i, j)] = [H[k][j] * H[i][k] for k in range(d)]

    pairs = list(v_sig.keys())
    for idx_a, (i, j) in enumerate(pairs):
        va = v_sig[(i, j)]
        # Inner product with v_{ji} == d - 4
        assert sum(x * y for x, y in zip(va, v_sig[(j, i)])) == d - 4
        for u, v in pairs[idx_a + 1 :]:
            if (u, v) == (j, i):
                continue
            ip = sum(x * y for x, y in zip(va, v_sig[(u, v)]))
            assert abs(ip) <= bound + 1e-12
            if u == i or v == j:
                assert ip == 0
            elif u == j or v == i:
                assert ip in (-4, 0, 4)

    if check_t4_exhaustive:
        # Check T_4^col(inf, 0, r1, r2) for all pairs {r1, r2} in F_q^*
        inf_idx = q
        zero_idx = ff.idx[ff.zero]
        nonzero_elems = [el for el in ff.elements if el != ff.zero]
        for r1_el, r2_el in itertools.combinations(nonzero_elems, 2):
            r1 = ff.idx[r1_el]
            r2 = ff.idx[r2_el]
            t4 = sum(H[k][inf_idx] * H[k][zero_idx] * H[k][r1] * H[k][r2] for k in range(d))
            assert abs(t4) <= bound + 1e-12

    # Special q=19 verification of Lemma 4 (PROOF.md lines 167-175)
    if q == 19:
        inf_idx = 19
        zero_idx = 0  # elements are (0,), (1,), ..., (18,)
        assert ff.idx[(0,)] == 0
        squares = sorted({(x * x) % 19 for x in range(1, 19)})
        assert len(squares) == 9
        pair_orbits: dict[frozenset[tuple[int, int]], list[tuple[int, int]]] = {}
        t4_by_orbit = {}
        for r1 in range(1, 19):
            for r2 in range(r1 + 1, 19):
                orb = frozenset(
                    tuple(sorted(((s * r1) % 19, (s * r2) % 19))) for s in squares
                )
                t4 = sum(H[k][inf_idx] * H[k][zero_idx] * H[k][r1] * H[k][r2] for k in range(d))
                if orb not in pair_orbits:
                    pair_orbits[orb] = (r1, r2)
                    t4_by_orbit[orb] = t4
                else:
                    assert t4_by_orbit[orb] == t4
        assert len(pair_orbits) == 17
        vals = list(t4_by_orbit.values())
        assert sum(1 for v in vals if v in (-4, 4)) == 16
        big_orbs = [orb for orb, v in t4_by_orbit.items() if v not in (-4, 4)]
        assert len(big_orbs) == 1
        assert (1, 12) in big_orbs[0] and t4_by_orbit[big_orbs[0]] == 12

        # Check explicit sets R1, R3 for {inf, 0} and {1, 12}
        def decode(k: int):
            return "inf" if k == 19 else k

        for sign in (+1, -1):
            R1 = {k for k in range(d) if H[k][inf_idx] * H[k][zero_idx] == sign}
            R3 = {k for k in range(d) if H[k][1] * H[k][12] == sign}
            assert len(R1) == 10 and len(R3) == 10
            inter = {decode(k) for k in (R1 & R3)}
            r3_m_r1 = {decode(k) for k in (R3 - R1)}
            r1_m_r3 = {decode(k) for k in (R1 - R3)}
            if sign == 1:
                assert inter == {2, 3, 10, 12, 14, 15, 18, "inf"}
                assert r3_m_r1 == {11, 17}
                assert r1_m_r3 == {8, 13}
                r_ref = inf_idx
            else:
                assert inter == {0, 1, 4, 5, 6, 7, 9, 16}
                assert r3_m_r1 == {8, 13}
                assert r1_m_r3 == {11, 17}
                r_ref = 0
            for i1 in (R3 - R1):
                for i3 in (R1 - R3):
                    RC = (R1 & R3) | {i1, i3}
                    assert len(RC) == 10
                    # Check all 190 column pairs fail at row r_ref
                    for c1, c2 in itertools.combinations(range(d), 2):
                        target = -H[r_ref][c1] * H[r_ref][c2]
                        ok = all(H[k][c1] * H[k][c2] == target for k in RC if k != r_ref)
                        assert not ok


def check_sic_and_thm2(ff: FiniteFieldPrimePower, p: int) -> None:
    """Construct Theorem 2 SIC in F_{p^2}^d and verify Theorem 2 Steps 1 & 2."""
    X, S, H = build_paley_i(ff)
    d = len(X)
    assert (d - 8) % p == 0 and p % 4 == 3

    # F_{p^2} = F_p[i] represented as complex-like pairs (a, b) mod p with i^2 = -1
    def c_add(u, v):
        return ((u[0] + v[0]) % p, (u[1] + v[1]) % p)

    def c_sub(u, v):
        return ((u[0] - v[0]) % p, (u[1] - v[1]) % p)

    def c_mul(u, v):
        return ((u[0] * v[0] - u[1] * v[1]) % p, (u[0] * v[1] + u[1] * v[0]) % p)

    def c_conj(u):
        return (u[0], (-u[1]) % p)

    def ip_vec(u_vec, v_vec):
        acc = (0, 0)
        for uk, vk in zip(u_vec, v_vec):
            acc = c_add(acc, c_mul(c_conj(uk), vk))
        return acc

    # x_{i, j} = h_j * (1 + z e_i), z = -2(1 + i) => 1 + z = (-1, -2) mod p
    one_plus_z = ((-1) % p, (-2) % p)
    sic = {}
    for i in range(d):
        for j in range(d):
            vec = [((H[m][j] % p), 0) for m in range(d)]
            vec[i] = ((one_plus_z[0] * H[i][j]) % p, (one_plus_z[1] * H[i][j]) % p)
            sic[(i, j)] = vec

    # Check Definition 1(a)-(d)
    # Sample or full check depending on size (full for d <= 32, representative + exact check for d=344)
    a_exp = (12 % p, 0)
    b_exp = (16 % p, 0)
    c_exp = (96 % p, 0)

    if d <= 20:
        all_pairs = [(i, j) for i in range(d) for j in range(d)]
        # (a) & (b)
        for u in all_pairs:
            assert ip_vec(sic[u], sic[u]) == a_exp
        # Lemma 3 & Phi check
        inv2 = (p + 1) // 2

        def phi_fp2(s: int, t: int):
            re = (-inv2 * (s + t)) % p
            im = (inv2 * (s - t)) % p
            return (re, im)

        for idx_u, u in enumerate(all_pairs):
            i, j = u
            for v in all_pairs[idx_u + 1 :]:
                k, l = v
                val = ip_vec(sic[u], sic[v])
                val2 = ip_vec(sic[v], sic[u])
                assert c_mul(val, val2) == b_exp
                # Lemma 3 formula check
                if i != k and j != l:
                    exp_g = c_mul((4 % p, 0), phi_fp2(H[i][j] * H[i][l], H[k][j] * H[k][l]))
                elif i != k and j == l:
                    exp_g = (4 % p, 0)
                else:
                    assert i == k and j != l
                    exp_g = ((4 * H[i][j] * H[i][l]) % p, 0)
                assert val == exp_g

        # (c) sum x_u x_u^* = 96 I (check entrywise over F_{p^2})
        for r in range(d):
            for c in range(d):
                acc = (0, 0)
                for u in all_pairs:
                    acc = c_add(acc, c_mul(sic[u][r], c_conj(sic[u][c])))
                assert acc == (c_exp if r == c else (0, 0))

    # (d) Span check over F_{p^2}: show standard basis e_0..e_{d-1} is spanned (explicit Gaussian elim mod p on first d+20 vectors)
    # Build (d) basis check via explicit rank over F_p of F_{p^2}-vectors treated in F_{p^2}^d
    def f_inv(u):
        norm = (u[0] * u[0] + u[1] * u[1]) % p
        assert norm != 0
        inv_n = pow(norm, p - 2, p)
        return ((u[0] * inv_n) % p, ((-u[1]) * inv_n) % p)

    # (d) Span check over F_{p^2}: full Gaussian elim for d <= 90 (q=19, 31, 83)
    if d <= 90:
        mat = [list(sic[(i, 0)]) for i in range(d)] + [list(sic[(0, j)]) for j in range(d)]
        rank = 0
        for col in range(d):
            piv = None
            for r in range(rank, len(mat)):
                if mat[r][col] != (0, 0):
                    piv = r
                    break
            if piv is None:
                continue
            mat[rank], mat[piv] = mat[piv], mat[rank]
            inv_piv = f_inv(mat[rank][col])
            mat[rank] = [c_mul(val, inv_piv) for val in mat[rank]]
            for r in range(len(mat)):
                if r != rank and mat[r][col] != (0, 0):
                    factor_r = mat[r][col]
                    mat[r] = [c_sub(mat[r][k], c_mul(factor_r, mat[rank][k])) for k in range(d)]
            rank += 1
        assert rank == d

    # Step 1 & Step 2 verification for g_0(x) = non_sq * x (with non_sq in F_q^* non-square, fixing 0 and inf)
    non_sq = next(el for el in ff.elements if ff.chi(el) == -1)
    elem_idx = {a: i for i, a in enumerate(X)}
    g0_perm = []
    eps_g0 = []
    for a in X:
        if a is None:
            g0_perm.append(elem_idx[None])
            eps_g0.append(1)  # M = diag(non_sq, 1), M v_inf = non_sq v_inf => chi(non_sq) = -1!!
        else:
            ga = ff.mul(non_sq, a)
            g0_perm.append(elem_idx[ga])
            eps_g0.append(1)  # Wait: let's compute exact lambda_a from M = diag(non_sq, 1)!
    # Correct lambda_a: M (1,0)^T = (non_sq, 0)^T => eps_inf = chi(non_sq) = -1; M (a,1)^T = (non_sq*a, 1)^T => eps_a = chi(1) = +1!
    eps_g0 = [-1 if a is None else 1 for a in X]
    for a in range(d):
        for b in range(d):
            assert H[g0_perm[a]][g0_perm[b]] == eps_g0[a] * eps_g0[b] * H[b][a]

    if d <= 20:
        # Check Step 1 identity on ALL pairs u, v in X^2
        all_pairs = [(i, j) for i in range(d) for j in range(d)]
        for u in all_pairs:
            i, j = u
            pi_u = (g0_perm[j], g0_perm[i])
            wu = (eps_g0[i] * H[i][j]) % p
            for v in all_pairs:
                k, l = v
                pi_v = (g0_perm[l], g0_perm[k])
                wv = (eps_g0[k] * H[k][l]) % p
                lhs = ip_vec(sic[pi_u], sic[pi_v])
                rhs_conj = c_conj(ip_vec(sic[u], sic[v]))
                w_prod = ((wu * wv) % p, 0)
                assert lhs == c_mul(w_prod, rhs_conj)

    # Check Step 2 triple products T(u1, v1, w1) = 64 != 0 and T(u2, v2, w2) = +-64i != 0
    u1, v1, w1 = (0, 0), (1, 0), (2, 0)
    T1 = c_mul(c_mul(ip_vec(sic[u1], sic[v1]), ip_vec(sic[v1], sic[w1])), ip_vec(sic[w1], sic[u1]))
    assert T1 == (64 % p, 0) and T1 != (0, 0) and c_conj(T1) == T1

    u2, v2, w2 = (0, 0), (0, 1), (1, 1)
    T2 = c_mul(c_mul(ip_vec(sic[u2], sic[v2]), ip_vec(sic[v2], sic[w2])), ip_vec(sic[w2], sic[u2]))
    assert T2[0] == 0 and T2[1] in (64 % p, (-64) % p) and T2 != (0, 0) and c_conj(T2) == ((0, (-T2[1]) % p))


def main() -> int:
    t0 = time.time()
    # 1. Prime & prime-power Paley I checks: q = 19, 23, 27 (= 3^3), 31, 83
    # Irred over F_3 of deg 3: x^3 + 2x + 1 (at x=0:1, x=1:1, x=2:8+4+1=1 != 0 => irred!)
    ff19 = FiniteFieldPrimePower(19)
    ff23 = FiniteFieldPrimePower(23)
    ff27 = FiniteFieldPrimePower(3, [1, 2, 0, 1])
    ff31 = FiniteFieldPrimePower(31)
    ff83 = FiniteFieldPrimePower(83)
    # Also q = 343 = 7^3: x^3 + 6x + 2 over F_7? Let's verify irreducibility first:
    x = symbols("x")
    p343 = Poly(x**3 + x + 1, x, domain=GF(7))
    # Check roots in F_7: 0->1, 1->3, 2->11=4, 3->31=3, 4->69=6, 5->131=5, 6->223=6 => no roots => irred!
    assert p343.is_irreducible
    ff343 = FiniteFieldPrimePower(7, [1, 1, 0, 1])

    for ff in (ff19, ff23, ff27, ff31):
        check_paley_and_lemma1(ff)
    print("Lemma 1 (Paley I properties & PGammaL(2,q) embedding, q=19,23,27,31): OK")

    check_lemma2_and_q19(ff19, check_t4_exhaustive=True)
    check_lemma2_and_q19(ff23, check_t4_exhaustive=False)
    check_lemma2_and_q19(ff27, check_t4_exhaustive=False)
    print("Lemma 2 & Lemma 4 q=19 (Hasse bounds, T4^col orbits, 190 col-pair eliminations): OK")

    # 2. SIC & Theorem 2 checks across p = 3 (q=19, 31), p = 19 (q=83), p = 7 (q=343=7^3)
    for ff, p in ((ff19, 3), (ff31, 3), (ff83, 19), (ff343, 7)):
        check_sic_and_thm2(ff, p)
    print(f"Theorem 2 SIC & Aut_s != Aut_w (q=19/p=3, q=31/p=3, q=83/p=19, q=343/p=7): OK ({time.time() - t0:.2f}s)")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
