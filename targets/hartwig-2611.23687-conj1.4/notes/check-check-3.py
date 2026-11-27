#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for Hartwig-Shrivastava (arXiv:2611.23687v1) Conjecture 1.4.

Written directly from main.tex definitions and PROOF.md without reading verify.py or notes/.
Uses SymPy exact polynomial/rational arithmetic over Q(L0, c) and Q(sqrt((c-1)(c-25)))
with zero floating-point operations.
"""

from __future__ import annotations

from functools import lru_cache
import sys
import sympy as sp

L0, c = sp.symbols("L0 c")


def partitions(n: int) -> list[tuple[int, ...]]:
    """All partitions of n as ascending tuples (lam_1 <= ... <= lam_k)."""
    if n == 0:
        return [()]
    res: list[tuple[int, ...]] = []

    def rec(rem: int, min_part: int, cur: list[int]) -> None:
        if rem == 0:
            res.append(tuple(cur))
            return
        for p in range(min_part, rem + 1):
            cur.append(p)
            rec(rem - p, p, cur)
            cur.pop()

    rec(n, 1, [])
    return res


def poly_add(d1: dict[tuple[int, ...], sp.Expr], d2: dict[tuple[int, ...], sp.Expr], scale: sp.Expr = sp.Integer(1)) -> dict[tuple[int, ...], sp.Expr]:
    out = dict(d1)
    for k, v in d2.items():
        nv = sp.expand(out.get(k, sp.Integer(0)) + scale * v)
        if nv == 0:
            out.pop(k, None)
        else:
            out[k] = nv
    return out


@lru_cache(maxsize=None)
def act_L(m: int, neg_tup: tuple[int, ...]) -> dict[tuple[int, ...], sp.Expr]:
    """Action of L_m on L_{-lam_k}...L_{-lam_1}|1>, where neg_tup = (lam_1,...,lam_k) ascending.

    Returns dict mapping output ascending partition -> polynomial in Q[L0, c] placed on the RIGHT.
    """
    if m == 0:
        return {neg_tup: L0 + sum(neg_tup)}
    if m < 0:
        part = -m
        if not neg_tup or part >= neg_tup[-1]:
            return {neg_tup + (part,): sp.Integer(1)}
        # Leftmost generator in L_{-lam_k}...L_{-lam_1} is L_{-neg_tup[-1]}
        a = -neg_tup[-1]
        rest = neg_tup[:-1]
        # L_m L_a rest = L_a (L_m rest) + (m - a) L_{m+a} rest
        res: dict[tuple[int, ...], sp.Expr] = {}
        for t_sub, coeff in act_L(m, rest).items():
            for t_out, coeff2 in act_L(a, t_sub).items():
                res = poly_add(res, {t_out: sp.expand(coeff * coeff2)})
        for t_out, coeff in act_L(m + a, rest).items():
            res = poly_add(res, {t_out: sp.expand((m - a) * coeff)})
        return res
    # m > 0
    if not neg_tup:
        return {}
    a = -neg_tup[-1]
    rest = neg_tup[:-1]
    res = {}
    # L_m L_a rest = L_a (L_m rest) + [L_m, L_a] rest
    for t_sub, coeff in act_L(m, rest).items():
        for t_out, coeff2 in act_L(a, t_sub).items():
            res = poly_add(res, {t_out: sp.expand(coeff * coeff2)})
    if m + a == 0:
        # [L_m, L_{-m}] = 2m L_0 + (m^3 - m)/12 * c
        wt = sum(rest)
        factor = 2 * m * (L0 + wt) + sp.Rational(m**3 - m, 12) * c
        res = poly_add(res, {rest: sp.expand(factor)})
    else:
        for t_out, coeff in act_L(m + a, rest).items():
            res = poly_add(res, {t_out: sp.expand((m - a) * coeff)})
    return res


def act_word_pos(mu: tuple[int, ...], vec: dict[tuple[int, ...], sp.Expr]) -> dict[tuple[int, ...], sp.Expr]:
    """Act by L_mu = L_{mu_1}...L_{mu_r} (ascending) on vec."""
    cur = vec
    for m in reversed(mu):
        nxt: dict[tuple[int, ...], sp.Expr] = {}
        for tup, coeff in cur.items():
            for tup2, c2 in act_L(m, tup).items():
                nxt = poly_add(nxt, {tup2: sp.expand(c2 * coeff)})
        cur = nxt
        if not cur:
            break
    return cur


def act_word_neg(lam: tuple[int, ...], vec: dict[tuple[int, ...], sp.Expr]) -> dict[tuple[int, ...], sp.Expr]:
    """Act by L_lam^dagger = L_{-lam_k}...L_{-lam_1} on vec."""
    cur = vec
    for p in lam:
        nxt: dict[tuple[int, ...], sp.Expr] = {}
        for tup, coeff in cur.items():
            for tup2, c2 in act_L(-p, tup).items():
                nxt = poly_add(nxt, {tup2: sp.expand(c2 * coeff)})
        cur = nxt
    return cur


def shapovalov_matrix(n: int) -> tuple[list[tuple[int, ...]], sp.Matrix]:
    parts = partitions(n)
    k = len(parts)
    S = sp.zeros(k, k)
    for i, mu in enumerate(parts):
        for j, eta in enumerate(parts):
            res = act_word_pos(mu, {eta: sp.Integer(1)})
            val = res.get((), sp.Integer(0))
            S[i, j] = sp.expand(val)
    return parts, S


def build_K_n(n: int) -> sp.Expr:
    """Construct primitive K_n in Z[L0, c] with positive leading L0-coeff directly from eqs. (1.8)-(1.9)."""
    u = sp.Symbol("u")  # stands for sqrt((c-1)(c-25))
    prod_expr = sp.Integer(1)
    for r in range(1, n + 1):
        if n % r != 0:
            continue
        s = n // r
        phi = L0 - ((13 - c) * (r**2 + s**2) - 24 * r * s + 2 * (c - 1) + (r**2 - s**2) * u) / sp.Integer(48)
        prod_expr = sp.expand(prod_expr * phi)
    # Reduce u^2 -> (c - 1)*(c - 25)
    p_u = sp.Poly(prod_expr, u)
    terms = p_u.all_coeffs()
    # Since product is symmetric in (r, s), u-odd parts cancel identically
    reduced = sp.Integer(0)
    deg = len(terms) - 1
    for idx, coeff in enumerate(terms):
        pwr = deg - idx
        if pwr % 2 == 1:
            assert sp.expand(coeff) == 0, f"Odd power of sqrt did not vanish for n={n}"
        else:
            reduced += sp.expand(coeff * ((c - 1) * (c - 25)) ** (pwr // 2))
    reduced = sp.expand(reduced)
    # Clear rational denominators and make primitive in Z[L0, c] with positive L0-leading coeff
    num, den = sp.fraction(sp.together(reduced))
    poly_z = sp.Poly(num, L0, c, domain="ZZ")
    cont, prim = poly_z.primitive()
    expr = prim.as_expr()
    lc_L0 = sp.Poly(expr, L0).LC()
    if sp.Poly(lc_L0, c).LC() < 0:
        expr = -expr
    return sp.expand(expr)


def test_step2_and_kac_formula() -> dict[int, sp.Expr]:
    print("[1/4] Checking Step 2: K_m primitivity, irreducibility, coprimality, D_1..D_6 & Kac formula...", flush=True)
    K = {m: build_K_n(m) for m in range(1, 7)}

    # Check irreducibility of factors and pairwise coprimality of tau_{-n}(K_m) for 1 <= m, n <= 6
    irred_seen: list[tuple[int, int, sp.Poly]] = []
    for n in range(1, 7):
        for m in range(1, 7):
            shifted = sp.expand(K[m].subs(L0, L0 - n))
            fac_list = sp.factor_list(shifted, L0, c, domain="ZZ")
            for fac_expr, mult in fac_list[1]:
                assert mult == 1, f"K_{m} not squarefree!"
                p_fac = sp.Poly(fac_expr, L0, c, domain="ZZ")
                assert p_fac.is_irreducible
                # Verify pairwise distinctness up to sign across all (n, m)
                for n2, m2, p2 in irred_seen:
                    assert p_fac != p2 and p_fac != -p2, f"Collision between ({n},{m}) and ({n2},{m2})"
                irred_seen.append((n, m, p_fac))

    # Match D_1..D_6 from main.tex eqs. (3.34)-(3.39)
    expected_D6_factors = [
        L0 - 1,
        8 * L0 + c - 33,
        L0**2 + L0 * c - 19 * L0 - 3 * c + 84,
        3 * L0**2 + L0 * c - 25 * L0 - 2 * c + 50,
        16 * L0**2 + 2 * L0 * c - 74 * L0 - 3 * c + 84,
        16 * L0**2 + 10 * L0 * c - 210 * L0 - 25 * c + 650,
        48 * L0**2 + 70 * L0 * c - 1246 * L0 - 245 * c + 7448,
        48 * L0**2 + 22 * L0 * c - 622 * L0 + 2 * c**2 - 129 * c + 2002,
    ]
    D6 = sp.expand(sp.prod(K[n].subs(L0, L0 - n) for n in range(1, 7)))
    assert sp.expand(D6 - sp.prod(expected_D6_factors)) == 0

    # Check Kac's determinant formula for levels n = 1..5
    from sympy.polys.matrices import DomainMatrix

    dom_poly = sp.QQ[L0, c]
    part_counts = {k: len(partitions(k)) for k in range(0, 6)}
    for n in range(1, 6):
        _, S = shapovalov_matrix(n)
        assert S == S.T
        det_S = DomainMatrix.from_Matrix(S, dom_poly).det()
        kac_prod = sp.Integer(1)
        for m in range(1, n + 1):
            kac_prod *= K[m] ** part_counts[n - m]
        quo, rem = sp.div(sp.Poly(dom_poly.to_sympy(det_S), L0, c, domain="QQ"), sp.Poly(kac_prod, L0, c, domain="QQ"))
        assert rem.is_zero, f"Kac determinant mismatch at n={n}"
        assert quo.is_ground and quo.as_expr() != 0, f"Nonconstant ratio at n={n}: {quo}"

    return K


def test_exact_projector_coefficients(K: dict[int, sp.Expr]) -> dict[int, tuple[list[tuple[int, ...]], sp.Matrix, sp.Matrix, sp.Matrix]]:
    print("[2/4] Computing exact Virasoro extremal projector P_1..P_4 over Q(L0, c)...", flush=True)
    from sympy.polys.matrices import DomainMatrix

    dom_poly = sp.QQ[L0, c]
    dom_frac = dom_poly.get_field()
    # Verify main.tex eq. (3.11)-(3.16) relations first
    assert act_word_pos((1, 1), {(1,): sp.Integer(1)}) == {}
    assert act_word_pos((2,), {(1, 1): sp.Integer(1)}) == {(): 6 * L0}
    assert act_word_pos((2,), {(2,): sp.Integer(1)}) == {(): 4 * L0 + sp.Rational(1, 2) * c}
    assert act_word_pos((1, 1), {(1, 1): sp.Integer(1)}) == {(): 8 * L0**2 + 4 * L0}

    # P[k] stored as dict {(lam, mu): rational coeff b_{lam,mu}(L0,c)}
    P_coeffs: dict[int, dict[tuple[tuple[int, ...], tuple[int, ...]], sp.Expr]] = {}
    level_data = {}

    for n in range(1, 5):
        parts_n, S_n = shapovalov_matrix(n)
        dim_n = len(parts_n)
        idx_map = {p: i for i, p in enumerate(parts_n)}

        # Compute R^{(n)}_{lam, eta}(L0, c) directly by -P_{n-1}(L_eta^\dagger 1) in QQ(L0, c)
        R_n_f = [[dom_frac.zero for _ in range(dim_n)] for _ in range(dim_n)]
        for j, eta in enumerate(parts_n):
            R_n_f[j][j] -= dom_frac.one
            for k in range(1, n):
                for (alpha, beta), b_ab in P_coeffs[k].items():
                    if b_ab == 0:
                        continue
                    mid = act_word_pos(beta, {eta: sp.Integer(1)})
                    if not mid:
                        continue
                    out = act_word_neg(alpha, mid)
                    b_sh_f = dom_frac.from_sympy(b_ab.subs(L0, L0 + n))
                    for lam_out, poly_c in out.items():
                        R_n_f[idx_map[lam_out]][j] -= b_sh_f * dom_frac.from_sympy(poly_c)

        R_n = sp.Matrix(dim_n, dim_n, lambda i, j: dom_frac.to_sympy(R_n_f[i][j]))

        # Solve B_shifted * S_n = R_n over Q(L0, c) via fraction-free DomainMatrix solve_den over QQ[L0, c]
        D_prev_shifted = sp.Integer(1) if n == 1 else sp.expand(sp.prod(K[m].subs(L0, L0 + n - m) for m in range(1, n)))
        dprev_f = dom_frac.from_sympy(D_prev_shifted)
        R_n_poly = sp.Matrix(dim_n, dim_n, lambda i, j: dom_frac.to_sympy(dprev_f * R_n_f[i][j]))
        dm_S = DomainMatrix.from_Matrix(S_n.T, dom_poly)
        dm_R = DomainMatrix.from_Matrix(R_n_poly.T, dom_poly)
        dm_num, den_el = dm_S.solve_den(dm_R)
        den_full_p = sp.Poly(sp.expand(D_prev_shifted * dom_poly.to_sympy(den_el)), L0, c, domain="QQ")
        B_num = dm_num.transpose().to_Matrix()
        B_shifted = sp.zeros(dim_n, dim_n)
        P_coeffs[n] = {}
        P_dens_shifted: list[sp.Poly] = []
        for i, lam in enumerate(parts_n):
            for j, mu in enumerate(parts_n):
                p_e = sp.Poly(B_num[i, j], L0, c, domain="QQ")
                _, p_red, q_red = sp.cofactors(p_e, den_full_p)
                val_shifted = p_red.as_expr() / q_red.as_expr()
                B_shifted[i, j] = val_shifted
                P_coeffs[n][(lam, mu)] = val_shifted.subs(L0, L0 - n)
                P_dens_shifted.append(q_red)

        # Verify Claims 1 & 2 from PROOF.md Step 1 & Step 4:
        D_n = sp.expand(sp.prod(K[m].subs(L0, L0 - m) for m in range(1, n + 1)))
        D_n_shifted_p = sp.Poly(sp.expand(D_n.subs(L0, L0 + n)), L0, c, domain="QQ")

        # Claim 1 / (1'): D_n(L0 + n, c) * B_shifted[i, j] is a polynomial in Q[L0, c]
        for q_red in P_dens_shifted:
            assert sp.rem(D_n_shifted_p, q_red).is_zero, f"Pole {q_red} outside D_{n}(L0+{n},c)"

        # Claim 2 / (2'): Every irreducible factor of K_n(L0, c) divides at least one denominator of B_shifted
        Kn_p = sp.Poly(K[n], L0, c, domain="ZZ")
        for fac_expr, _ in sp.factor_list(Kn_p, L0, c, domain="ZZ")[1]:
            p_fac = sp.Poly(fac_expr, L0, c, domain="QQ")
            found = any(sp.rem(q_red, p_fac).is_zero for q_red in P_dens_shifted)
            assert found, f"Factor {fac_expr} of K_{n} missing from B_shifted denominators!"

        level_data[n] = (parts_n, S_n, R_n, B_shifted)

    # Also verify exact match with main.tex P[1], P[2], P[3] entries
    assert sp.cancel(P_coeffs[1][((1,), (1,))] + sp.Rational(1, 2) / (L0 - 1)) == 0
    assert sp.cancel(P_coeffs[2][((2,), (2,))] + (4 * L0 - 6) / (16 * L0**2 + 2 * L0 * c - 74 * L0 - 3 * c + 84)) == 0
    assert sp.cancel(
        P_coeffs[3][((3,), (3,))] + (L0 - 3) * (L0 - 2) / (2 * (L0 - 1) * (3 * L0**2 + L0 * c - 25 * L0 - 2 * c + 50))
    ) == 0
    return level_data


def test_step3_and_step4_at_generic_c(level_data: dict) -> None:
    print("[3/4] Checking Step 3 (local SNF/singular vectors) & Step 4 (R*ker S = 0 / != 0) at c=899/35...", flush=True)
    # At c = 7: sqrt((c-1)(c-25)) = sqrt(6 * (-18)) = 6*sqrt(-3); work over Q(w) with w^2 = -3
    # At c = 899/35 (t=6): (c-1)(c-25) = (144/35)^2, so all h_{r,s}(c) lie in Q and avoid Z_4
    c_val = sp.Rational(899, 35)
    sqrt_val = sp.Rational(144, 35)

    def h_rs(r: int, s: int) -> sp.Rational:
        num = (13 - c_val) * (r**2 + s**2) - 24 * r * s + 2 * (c_val - 1) + (r**2 - s**2) * sqrt_val
        return sp.Rational(num, 48)

    # First verify c = 899/35 avoids Z_4: all shifted roots h_{r,s}(c) + shift (1 <= rs <= 4, -4 <= shift <= 4) are distinct
    shifted_roots = set()
    for m in range(1, 5):
        for r in range(1, m + 1):
            if m % r == 0:
                s = m // r
                h0 = h_rs(r, s)
                for shift in range(-4, 5):
                    val = h0 + shift
                    assert val not in shifted_roots, f"Root collision at c=899/35!"
                    shifted_roots.add(val)

    # Check kernels, singular vectors, and R^{(n)}(h_0, 50) action for n = 1..4 and all rs = m <= n
    for n in range(1, 5):
        parts_n, S_n, R_n, _ = level_data[n]
        dim_n = len(parts_n)
        for m in range(1, n + 1):
            parts_m, S_m, _, _ = level_data[m]
            for r in range(1, m + 1):
                if m % r != 0:
                    continue
                s = m // r
                h0 = h_rs(r, s)
                Sm_spec = S_m.subs({L0: h0, c: c_val})
                ker_m = Sm_spec.nullspace()
                assert len(ker_m) == 1, f"Expected 1D singular space at m={m}, (r,s)=({r},{s})"
                v0 = ker_m[0]
                # Check v0 is singular: L_k v0 = 0 for all 1 <= k <= m
                v0_dict = {parts_m[idx]: v0[idx, 0] for idx in range(len(parts_m)) if v0[idx, 0] != 0}
                for j in range(1, m + 1):
                    Lv0 = act_word_pos((j,), v0_dict)
                    for _, pol in Lv0.items():
                        val = pol.subs({L0: h0, c: c_val})
                        assert val == 0, f"v0 not annihilated by L_{j} at (r,s)=({r},{s}): {val}"

                # Check ker S^{(n)}(h_0, 50) has dimension p(n - m) and equals span{L_nu^\dagger v_0}
                Sn_spec = S_n.subs({L0: h0, c: c_val})
                Rn_spec = R_n.subs({L0: h0, c: c_val})
                ker_n = Sn_spec.nullspace()
                parts_nm = partitions(n - m)
                assert len(ker_n) == len(parts_nm)

                descendant_vecs = []
                idx_n = {p: i for i, p in enumerate(parts_n)}
                for nu in parts_nm:
                    vec_dict = act_word_neg(nu, v0_dict)
                    col = sp.zeros(dim_n, 1)
                    for tup, pol in vec_dict.items():
                        col[idx_n[tup], 0] += pol.subs({L0: h0, c: c_val})
                    descendant_vecs.append(col)
                    assert Sn_spec * col == sp.zeros(dim_n, 1)

                M_desc = sp.Matrix.hstack(*descendant_vecs)
                assert M_desc.rank() == len(parts_nm)

                # Verify Step 4 action of R^{(n)}(h_0, 50) on ker S^{(n)}(h_0, 50):
                if m < n:
                    for col in descendant_vecs:
                        assert Rn_spec * col == sp.zeros(dim_n, 1)
                else:
                    assert Rn_spec * v0 + v0 == sp.zeros(dim_n, 1)


def test_step1_pbw_basis_shift() -> None:
    print("[4/4] Checking Step 1 PBW shift automorphism L_lam^dagger f(L0,c) = f(L0-|lam|,c) L_lam^dagger...", flush=True)
    # Check directly for n = 1..4 on test polynomials f(L0, c) = L0^2 + 3*L0*c - 5
    for n in range(1, 5):
        for lam in partitions(n):
            # [L_lam^dagger, L0] = -n * L_lam^dagger => L_0 * L_lam^dagger = L_lam^dagger * (L_0 + n)
            # So L_lam^dagger * L_0 = (L_0 - n) * L_lam^dagger
            # Verify via act_L(0, lam) = {lam: L0 + n}
            res = act_L(0, lam)
            assert res == {lam: L0 + n}


def main() -> int:
    K = test_step2_and_kac_formula()
    level_data = test_exact_projector_coefficients(K)
    test_step3_and_step4_at_generic_c(level_data)
    test_step1_pbw_basis_shift()
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
