"""Exact symbolic verification of Hartwig-Shrivastava (arXiv:2611.23687v1) Conjecture 1.4.

Verifies without floating-point arithmetic:
1. Exact bivariate computation over QQ(L0, c) of P[n] for n = 1, 2, 3, 4:
   - Matches explicit formulas for b^{(1)}, b^{(2)}, b^{(3)} in Section 3.1 of main.tex.
   - Verifies P_n|_{M[-m]} = 0 for all 1 <= m <= n <= 4.
   - Verifies Kac's determinant formula for S^{(n)}(L0, c) (n = 1..4).
   - Verifies D_n(L0, c) * b^{(n)}_{lam,mu}(L0, c) is a polynomial in QQ[L0, c] (n = 1..4).
   - Verifies EVERY irreducible factor of tau_{-n}(K_n) divides the denominator of some b^{(n)}_{lam,mu}.
2. Exact univariate verification over QQ(L0) at generic rational t = 101/37 (c = -10282/3737)
   for n = 1..5 (checks D_5 * b^{(5)} in QQ[L0] and all roots of tau_{-5}(K_5) are genuine poles).
"""

from collections import defaultdict
import sys
import sympy as sp

L0, c = sp.symbols("L0 c")


def partitions(n, max_part=None):
    if max_part is None:
        max_part = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, max_part), 0, -1):
        for rest in partitions(n - first, first):
            yield rest + (first,)


_neg_cache = {}


def act_neg(m, lam):
    """PBW reduction of L_{-m} L_lam^dagger in U(Vir^-), m > 0."""
    key = (m, lam)
    if key in _neg_cache:
        return _neg_cache[key]
    if not lam or m >= lam[-1]:
        res = {lam + (m,): 1}
        _neg_cache[key] = res
        return res
    a = lam[-1]
    rest = lam[:-1]
    res = defaultdict(int)
    for mu, cf in act_neg(m, rest).items():
        for nu, cf2 in act_neg(a, mu).items():
            res[nu] += cf * cf2
    if a != m:
        for nu, cf in act_neg(m + a, rest).items():
            res[nu] += (a - m) * cf
    res = {k: v for k, v in res.items() if v != 0}
    _neg_cache[key] = res
    return res


def apply_neg_vec(m, vec):
    res = defaultdict(int)
    for lam, cf in vec.items():
        for mu, cf2 in act_neg(m, lam).items():
            res[mu] += cf * cf2
    return {k: v for k, v in res.items() if v != 0}


_pos_cache = {}


def act_pos_basis(m, lam, c_val=None):
    """L_m L_lam^dagger |1> = sum_mu L_mu^dagger f_mu(L0, c) |1> (coeffs on RIGHT)."""
    key = (m, lam, c_val)
    if key in _pos_cache:
        return _pos_cache[key]
    if m < 0:
        res = {mu: sp.Integer(cf) for mu, cf in act_neg(-m, lam).items()}
        _pos_cache[key] = res
        return res
    if m == 0:
        res = {lam: L0 + sum(lam)}
        _pos_cache[key] = res
        return res
    if not lam:
        _pos_cache[key] = {}
        return {}
    a = lam[-1]
    rest = lam[:-1]
    res = defaultdict(lambda: sp.Integer(0))
    for mu, cf in act_pos_basis(m, rest, c_val).items():
        for nu, cf2 in act_neg(a, mu).items():
            res[nu] += cf * cf2
    for nu, cf in act_pos_basis(m - a, rest, c_val).items():
        res[nu] += (m + a) * cf
    if m == a and (m**3 - m) != 0:
        cc = c if c_val is None else c_val
        res[rest] += sp.Rational(m**3 - m, 12) * cc
    res = {k: sp.expand(v) for k, v in res.items() if sp.expand(v) != 0}
    _pos_cache[key] = res
    return res


def apply_L_part_to_basis(mu, eta, c_val=None):
    vec = {eta: sp.Integer(1)}
    for m in reversed(mu):
        nxt = defaultdict(lambda: sp.Integer(0))
        for lam, cf in vec.items():
            for nu, cf2 in act_pos_basis(m, lam, c_val).items():
                nxt[nu] += cf * cf2
        vec = {k: sp.expand(v) for k, v in nxt.items() if sp.expand(v) != 0}
        if not vec:
            break
    return vec


def K_poly(m):
    """Exact polynomial K_m(L0, c) in QQ[L0, c] (monic in L0 up to positive integer)."""
    prod = sp.Integer(1)
    for r in range(1, m + 1):
        if m % r != 0:
            continue
        s = m // r
        if r == s:
            phi = L0 - sp.Rational((r**2 - 1), 24) * (1 - c)
            prod *= phi
        elif r < s:
            mid = ((13 - c) * (r**2 + s**2) - 24 * r * s + 2 * (c - 1)) / sp.Integer(48)
            disc = ((r**2 - s**2) ** 2) * (c - 1) * (c - 25) / sp.Integer(48**2)
            prod *= sp.expand((L0 - mid) ** 2 - disc)
    poly = sp.Poly(sp.expand(prod), L0, c, domain=sp.QQ)
    _, prim = poly.clear_denoms()
    return prim.as_expr()


def compute_b_domain(N_max, c_val=None):
    parts = {n: list(partitions(n)) for n in range(N_max + 1)}
    K = sp.QQ.frac_field(L0, c) if c_val is None else sp.QQ.frac_field(L0)
    b_unshifted = {}  # [n] -> DomainMatrix over K (b^{(n)}(L0, c))
    b_shifted = {}    # [n] -> DomainMatrix over K (b^{(n)}(L0 + n, c))
    S_dms = {}
    R_dms = {}

    def shift_K_elem(elem, delta):
        expr = K.to_sympy(elem).subs(L0, L0 + delta)
        return K.from_sympy(expr)

    for n in range(1, N_max + 1):
        P_n = len(parts[n])
        idx_n = {p: i for i, p in enumerate(parts[n])}
        S_rows = [[K.zero for _ in range(P_n)] for _ in range(P_n)]
        for i, mu in enumerate(parts[n]):
            for j in range(i, P_n):
                val = apply_L_part_to_basis(mu, parts[n][j], c_val).get((), sp.Integer(0))
                kv = K.from_sympy(val)
                S_rows[i][j] = S_rows[j][i] = kv
        S_dm = sp.polys.matrices.DomainMatrix(S_rows, (P_n, P_n), K)
        S_dms[n] = S_dm

        RHS_rows = [[K.zero for _ in range(P_n)] for _ in range(P_n)]
        for i in range(P_n):
            RHS_rows[i][i] = -K.one

        for k in range(1, n):
            P_k = len(parts[k])
            # Shift b^{(k)}(L0, c) -> b^{(k)}(L0 + n, c) once per k
            bk_sh = [[shift_K_elem(b_unshifted[k][a, b].element, n) for b in range(P_k)] for a in range(P_k)]
            for j, eta in enumerate(parts[n]):
                for b_idx, beta in enumerate(parts[k]):
                    v_nk = apply_L_part_to_basis(beta, eta, c_val)
                    if not v_nk:
                        continue
                    v_nk_K = {gamma: K.from_sympy(cf) for gamma, cf in v_nk.items()}
                    for a_idx, alpha in enumerate(parts[k]):
                        b_coeff = bk_sh[a_idx][b_idx]
                        if not b_coeff:
                            continue
                        for gamma, cf_K in v_nk_K.items():
                            cur = {gamma: 1}
                            for part in alpha:
                                cur = apply_neg_vec(part, cur)
                            prod_coeff = b_coeff * cf_K
                            for lam, mult in cur.items():
                                RHS_rows[idx_n[lam]][j] -= prod_coeff * K(mult)

        RHS_dm = sp.polys.matrices.DomainMatrix(RHS_rows, (P_n, P_n), K)
        R_dms[n] = RHS_dm
        B_sh = S_dm.transpose().lu_solve(RHS_dm.transpose()).transpose()
        b_shifted[n] = B_sh

        # Unshift L0 -> L0 - n
        B_un_rows = [[shift_K_elem(B_sh[i, j].element, -n) for j in range(P_n)] for i in range(P_n)]
        b_unshifted[n] = sp.polys.matrices.DomainMatrix(B_un_rows, (P_n, P_n), K)

    return parts, K, b_unshifted, b_shifted, S_dms, R_dms


def main():
    # 1. Exact bivariate check N = 1..4
    parts4, K4, b4, b4_sh, S4, RHS4 = compute_b_domain(4, c_val=None)

    # Check against explicit paper formulas in Section 3.1
    assert sp.simplify(K4.to_sympy(b4[1][0, 0].element) - sp.Rational(-1, 2) / (L0 - 1)) == 0
    den2 = 16 * L0**2 + 2 * L0 * c - 74 * L0 - 3 * c + 84
    assert sp.simplify(K4.to_sympy(b4[2][0, 0].element) - (-(4 * L0 - 6) / den2)) == 0
    assert sp.simplify(K4.to_sympy(b4[2][0, 1].element) - (3 / den2)) == 0
    assert sp.simplify(K4.to_sympy(b4[2][1, 1].element) - ((8 * L0 + c - 34) / (4 * (L0 - 1) * den2))) == 0
    den3 = (L0 - 1) * (3 * L0**2 + L0 * c - 25 * L0 - 2 * c + 50)
    assert sp.simplify(K4.to_sympy(b4[3][0, 0].element) - (-(L0 - 3) * (L0 - 2) / (2 * den3))) == 0

    D_n_expr = sp.Integer(1)
    for n in range(1, 5):
        P_n = len(parts4[n])
        # Check B_sh * S == RHS identically over K4
        assert (b4_sh[n] * S4[n] - RHS4[n]).is_zero_matrix, f"Matrix identity failed at n={n}"

        # Check Kac determinant over K4
        kac_prod = sp.Integer(1)
        for m in range(1, n + 1):
            kac_prod *= K_poly(m) ** len(parts4[n - m])
        det_elem = S4[n].det()
        kac_elem = K4.from_sympy(kac_prod)
        ratio = det_elem / kac_elem
        assert ratio.denom.is_ground and ratio.numer.is_ground and ratio != 0, f"Kac det mismatch n={n}"

        tau_Kn = sp.expand(K_poly(n).subs(L0, L0 - n))
        D_n_expr = sp.expand(D_n_expr * tau_Kn)
        D_n_K = K4.from_sympy(D_n_expr)

        # (a) Every entry of D_n * b^{(n)} is a polynomial in QQ[L0, c]
        entries = [b4[n][i, j].element for i in range(P_n) for j in range(i, P_n)]
        for el in entries:
            assert (D_n_K * el).denom.is_ground, f"n={n}: D_n failed to clear denominator of {el}"

        # (b) Removing any irreducible factor of tau_{-n}(K_n) leaves a non-polynomial entry
        for fac, mult in sp.factor_list(tau_Kn, L0, c, domain=sp.QQ)[1]:
            assert mult == 1
            D_drop = D_n_K / K4.from_sympy(fac)
            assert any(not (D_drop * el).denom.is_ground for el in entries), (
                f"n={n}: factor {fac} of tau_{-n}(K_n) was unnecessary!"
            )

        print(f"Bivariate exact QQ(L0, c) n={n} PASS")

    # 2. Exact univariate check for n = 1..5 at generic t = 101/37
    t_val = sp.Rational(101, 37)
    c_val = sp.Rational(13) - 6 * (t_val + 1 / t_val)
    parts5, K5, b5, b5_sh, S5, RHS5 = compute_b_domain(5, c_val=c_val)
    assert (b5_sh[5] * S5[5] - RHS5[5]).is_zero_matrix
    D_5_expr = sp.Integer(1)
    for k in range(1, 6):
        D_5_expr = sp.expand(D_5_expr * K_poly(k).subs({L0: L0 - k, c: c_val}))
    D_5_K = K5.from_sympy(D_5_expr)
    P_5 = len(parts5[5])
    entries5 = [b5[5][i, j].element for i in range(P_5) for j in range(i, P_5)]
    for el in entries5:
        assert (D_5_K * el).denom.is_ground, f"n=5 univariate D_5 failed to clear denominators"
    tau_K5 = sp.expand(K_poly(5).subs({L0: L0 - 5, c: c_val}))
    for fac, _ in sp.factor_list(tau_K5, L0, domain=sp.QQ)[1]:
        D_drop = D_5_K / K5.from_sympy(fac)
        assert any(not (D_drop * el).denom.is_ground for el in entries5), f"n=5 factor {fac} unnecessary!"
    print("Univariate exact QQ(L0) at t=101/37 n=5 PASS")
    print("PASS")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("FAIL:", exc)
        sys.exit(1)
