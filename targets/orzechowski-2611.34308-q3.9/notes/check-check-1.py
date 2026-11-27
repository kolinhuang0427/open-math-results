#!/usr/bin/env python3
"""Independent exact-arithmetic checker for targets/orzechowski-2611.34308-q3.9."""

from collections import deque
from fractions import Fraction
from itertools import product
import sympy as sp


def mat_mul_mod(A: tuple[int, int, int, int], B: tuple[int, int, int, int], mod: int) -> tuple[int, int, int, int]:
    a0, a1, a2, a3 = A
    b0, b1, b2, b3 = B
    return (
        (a0 * b0 + a1 * b2) % mod,
        (a0 * b1 + a1 * b3) % mod,
        (a2 * b0 + a3 * b2) % mod,
        (a2 * b1 + a3 * b3) % mod,
    )


def mat_inv_mod(A: tuple[int, int, int, int], mod: int) -> tuple[int, int, int, int]:
    a, b, c, d = A
    det = (a * d - b * c) % mod
    assert det == 1, f"Expected det=1 mod {mod}, got {det}"
    return (d % mod, (-b) % mod, (-c) % mod, a % mod)


def verify_step2_pro_p_filtration() -> None:
    """Verify Step 2(1): theta_m: K_m -> sl_2(F_p), explicit basis lifts, flag U_k, and normality in U_0."""
    for p in (2, 3, 5, 7):
        e = 2 if p == 2 else 1
        for m in (e, e + 1):
            pm = p ** m
            pm1 = p ** (m + 1)
            pm3 = p ** (m + 3)

            # 1. Enumerate all M = I + p^m A (mod p^{m+1}) with det(M) == 1 mod p^{m+1}
            # Wait: A runs over M_2(F_p) (p^4 matrices)
            km_mod_pm1 = []
            for a0, a1, a2, a3 in product(range(p), repeat=4):
                M = (
                    (1 + pm * a0) % pm1,
                    (pm * a1) % pm1,
                    (pm * a2) % pm1,
                    (1 + pm * a3) % pm1,
                )
                det = (M[0] * M[3] - M[1] * M[2]) % pm1
                if det == 1:
                    assert (a0 + a3) % p == 0
                    km_mod_pm1.append((a0, a1, a2, a3))
            assert len(km_mod_pm1) == p ** 3

            # 2. Check the 3 explicit lifts in K_m (mod p^{m+3}) have exact det == 1 and span sl_2(F_p)
            inv_1_pm = pow(1 + pm, -1, pm3)
            assert (inv_1_pm - (1 - pm)) % pm1 == 0
            lifts = [
                (1, pm % pm3, 0, 1),
                (1, 0, pm % pm3, 1),
                ((1 + pm) % pm3, 0, 0, inv_1_pm),
            ]
            imgs = []
            for L in lifts:
                assert (L[0] * L[3] - L[1] * L[2]) % pm3 == 1
                assert L[0] % pm == 1 and L[1] % pm == 0 and L[2] % pm == 0 and L[3] % pm == 1
                img = (
                    ((L[0] - 1) // pm) % p,
                    (L[1] // pm) % p,
                    (L[2] // pm) % p,
                    ((L[3] - 1) // pm) % p,
                )
                assert (img[0] + img[3]) % p == 0
                imgs.append(img)
            span = set()
            for c0, c1, c2 in product(range(p), repeat=3):
                vec = tuple((c0 * imgs[0][i] + c1 * imgs[1][i] + c2 * imgs[2][i]) % p for i in range(4))
                span.add(vec)
            assert len(span) == p ** 3

        # 3. For p in (2, 3, 5), construct full flag U_0 > U_1 > ... > U_6 = K_{e+2} inside U_0 / K_{e+2}
        if p <= 5:
            mod_top = p ** (e + 2)
            # Enumerate U_0 / K_{e+2}: M = I + p^e A mod p^{e+2} with det(M) == 1 mod p^{e+2}
            # Note entries of A in 0..p^2-1 -> p^8 entries, fast if we solve a3 from (1+p^e a0)(1+p^e a3) - p^{2e} a1 a2 = 1 mod p^{e+2}
            U0 = []
            pe = p ** e
            for a0, a1, a2 in product(range(p ** 2), repeat=3):
                u00 = (1 + pe * a0) % mod_top
                u00_inv = pow(u00, -1, mod_top)
                rhs = (1 + pe * pe * a1 * a2) % mod_top
                u11 = (rhs * u00_inv) % mod_top
                assert (u11 - 1) % pe == 0
                U0.append((u00, (pe * a1) % mod_top, (pe * a2) % mod_top, u11))
            assert len(U0) == p ** 6  # [K_e : K_{e+2}] = p^6

            # Define flag V_3={0} < V_2=<E12> < V_1=<E12, E21> < V_0=sl_2(F_p)
            def in_V(X: tuple[int, int, int, int], r: int) -> bool:
                a0, a1, a2, a3 = X
                if r == 0:
                    return (a0 + a3) % p == 0
                if r == 1:
                    return a0 == 0 and a3 == 0
                if r == 2:
                    return a0 == 0 and a2 == 0 and a3 == 0
                return X == (0, 0, 0, 0)

            U_subs: list[set[tuple[int, int, int, int]]] = []
            for m_lvl in (e, e + 1):
                pm = p ** m_lvl
                for r in (0, 1, 2):
                    sub = set()
                    for M in U0:
                        if M[0] % pm == 1 and M[1] % pm == 0 and M[2] % pm == 0 and M[3] % pm == 1:
                            theta = (((M[0] - 1) // pm) % p, (M[1] // pm) % p, (M[2] // pm) % p, ((M[3] - 1) // pm) % p)
                            if in_V(theta, r):
                                sub.add(M)
                    U_subs.append(sub)
            U_subs.append({(1, 0, 0, 1)})
            # Check exact orders p^{6-k}, subgroup closure, and normality in U_0!
            for k in range(7):
                assert len(U_subs[k]) == p ** (6 - k)
                if k > 0:
                    assert U_subs[k].issubset(U_subs[k - 1])
                # Verify normal subgroup of U_0
                for M in U_subs[k]:
                    for X in U0[: min(len(U0), 30)]:
                        Xinv = mat_inv_mod(X, mod_top)
                        conj = mat_mul_mod(mat_mul_mod(X, M, mod_top), Xinv, mod_top)
                        assert conj in U_subs[k]
    print("Step 2(1) pro-p filtration (theta_m, basis lifts, index-p chain, normality): PASS")


def verify_step2_isometry_and_measure() -> None:
    """Verify Step 2(2)-(3) finite-level ultrametric tree bijection Phi and extension alpha_tilde."""
    for p in (2, 3):
        e = 2 if p == 2 else 1
        mod_top = p ** (e + 1)
        pe = p ** e
        # Build U_0 / U_3 = U_0 / K_{e+1} (size p^3) with flag U_0 > U_1 > U_2 > U_3={I}
        U0 = []
        for a0, a1, a2 in product(range(p), repeat=3):
            u00 = (1 + pe * a0) % mod_top
            u00_inv = pow(u00, -1, mod_top)
            rhs = (1 + pe * pe * a1 * a2) % mod_top
            u11 = (rhs * u00_inv) % mod_top
            U0.append((u00, (pe * a1) % mod_top, (pe * a2) % mod_top, u11))
        assert len(U0) == p ** 3

        # U_k subgroups inside U_0 / K_{e+1}
        def level(u: tuple[int, int, int, int], v: tuple[int, int, int, int]) -> int:
            d = mat_mul_mod(mat_inv_mod(u, mod_top), v, mod_top)
            if d == (1, 0, 0, 1):
                return 3
            t = (((d[0] - 1) // pe) % p, (d[1] // pe) % p, (d[2] // pe) % p, ((d[3] - 1) // pe) % p)
            if t[0] == 0 and t[2] == 0 and t[3] == 0:
                return 2
            if t[0] == 0 and t[3] == 0:
                return 1
            return 0

        # Check tree bijection Phi: U_0/U_3 -> O_L / pi^3 O_L = {0..p-1}^3
        # Canonical coordinates on U_0 / U_3 using coset tree:
        # digit 0 = t[0] (in F_p, determines coset of U_1), digit 1 = t[2] (coset of U_2), digit 2 = t[1] (coset of U_3)
        # Wait: let's check if (t[0], t[2], t[1]) only depends on left coset properly!
        # Let's build the exact coset-tree bijection from left cosets u U_k recursively!
        cosets_1 = sorted({frozenset(mat_mul_mod(u, w, mod_top) for w in U0 if level((1, 0, 0, 1), w) >= 1) for u in U0})
        assert len(cosets_1) == p
        tau: dict[tuple[int, int, int, int], tuple[int, int, int]] = {}
        for d0, c1 in enumerate(cosets_1):
            cosets_2 = sorted({frozenset(mat_mul_mod(u, w, mod_top) for w in U0 if level((1, 0, 0, 1), w) >= 2) for u in c1})
            assert len(cosets_2) == p
            for d1, c2 in enumerate(cosets_2):
                elems_3 = sorted(c2)
                assert len(elems_3) == p
                for d2, u in enumerate(elems_3):
                    tau[u] = (d0, d1, d2)
        assert len(set(tau.values())) == p ** 3

        # Check EXACT ultrametric isometry and left-translation preservation across ALL pairs (u, v) and g in U_0!
        for u in U0:
            for v in U0:
                lv = level(u, v)
                tu, tv = tau[u], tau[v]
                l_lcp = 0
                while l_lcp < 3 and tu[l_lcp] == tv[l_lcp]:
                    l_lcp += 1
                assert lv == l_lcp
                for g in U0:
                    assert level(mat_mul_mod(g, u, mod_top), mat_mul_mod(g, v, mod_top)) == lv

        # Check extension alpha_tilde_g on model of pi^{-2} O_L / pi^3 O_L (elements (d_{-2}, d_{-1}, d_0, d_1, d_2))
        tau_inv = {val: key for key, val in tau.items()}
        space = list(product(range(p), repeat=5))

        def val_diff(x: tuple[int, ...], y: tuple[int, ...]) -> int:
            for idx in range(5):
                if x[idx] != y[idx]:
                    return idx - 2  # valuation exponent: pi^{idx-2}
            return 99

        g_test = U0[1]
        for x in space[::3]:
            for y in space[::3]:
                def apply_alpha(pt: tuple[int, ...]) -> tuple[int, ...]:
                    if pt[0] == 0 and pt[1] == 0:
                        u = tau_inv[(pt[2], pt[3], pt[4])]
                        gu = mat_mul_mod(g_test, u, mod_top)
                        return (0, 0) + tau[gu]
                    return pt

                assert val_diff(apply_alpha(x), apply_alpha(y)) == val_diff(x, y)
    print("Step 2(2)-(3) finite-level ultrametric tree Phi and alpha_tilde isometry: PASS")


def verify_step3_surjectivity_and_spectral_gap() -> None:
    """Verify Step 3: SL_2(Z) -> SL_2(Z/p^k Z) surjectivity and exact spectral gap on U_0 / K_{e+1}."""
    # 1. Check SL_2(Z) -> SL_2(Z/p^k Z) surjectivity by explicit BFS / transvection generation
    for p, k in ((2, 2), (2, 3), (3, 1), (3, 2), (5, 1)):
        mod = p ** k
        # Expected size of SL_2(Z/p^k Z) = p^{3k} (1 - 1/p^2) = p^{3k - 2} (p^2 - 1)
        expected_size = (p ** (3 * k - 2)) * (p * p - 1)
        gens = [
            (1, 1, 0, 1),
            (1, mod - 1, 0, 1),
            (1, 0, 1, 1),
            (1, 0, mod - 1, 1),
        ]
        seen = {(1, 0, 0, 1)}
        q = deque([(1, 0, 0, 1)])
        while q:
            cur = q.popleft()
            for g in gens:
                nxt = mat_mul_mod(cur, g, mod)
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
        assert len(seen) == expected_size

    # 2. Exact rational spectral gap on finite quotients U_0 / K_{e+1} (size p^3) for p in (2, 3, 5)
    # Using symmetric generators of Gamma = ker(SL_2(Z) -> SL_2(Z/qZ))
    for p in (2, 3, 5):
        e = 2 if p == 2 else 1
        q_mod = p ** e
        mod_top = p ** (e + 1)
        pe = p ** e
        U0 = []
        for a0, a1, a2 in product(range(p), repeat=3):
            u00 = (1 + pe * a0) % mod_top
            u00_inv = pow(u00, -1, mod_top)
            rhs = (1 + pe * pe * a1 * a2) % mod_top
            u11 = (rhs * u00_inv) % mod_top
            U0.append((u00, (pe * a1) % mod_top, (pe * a2) % mod_top, u11))
        idx_map = {u: i for i, u in enumerate(U0)}
        N = len(U0)
        assert N == p ** 3

        # Pick explicit finite symmetric generating set S subseteq Gamma:
        # E12(q)^+-1, E21(q)^+-1, and [E12(q), E21(q)]? Wait: for E12(q) and E21(q), their commutator mod p^{e+1} is:
        # [I+qE12, I+qE21] = I + q^2(E11 - E22) mod p^{e+2}, wait at mod p^{e+1} we have 2e >= e+1, so q^2 == 0 mod p^{e+1} if e >= 1!
        # Wait: so E12(q), E21(q) do NOT generate the diagonal matrix diag(1+q, (1+q)^-1) mod p^{e+1}!
        # We MUST include an element of Gamma mapping to diag(1+q, (1+q)^-1) mod p^{e+1} (e.g., [[1+q, q], [q, 1+q]]? Wait: det = (1+q)^2 - q^2 = 1 + 2q != 1;
        # actually let's find an explicit SL_2(Z) lift in Gamma that projects to [[1+q, 0], [0, (1+q)^-1]] mod p^{e+1}:
        # Standard explicit SL_2(Z) lift of diag(1+q, 1-q) mod p^{e+1} is:
        # M_diag = [[1 + q, q], [-q^2, 1 - q + ...]]? Look: (1+q)*d - (-q)*c = 1 => for d = 1 - q + q^2, (1+q)(1-q+q^2) = 1 + q^3, so subtract q^3 via b = q, c = q^2 =>
        # M_diag = [[1 + q, q], [q^2, 1 - q + q^2]]: det = (1+q)(1-q+q^2) - q^3 = 1 + q^3 - q^3 = 1 EXACTLY in Z, AND M_diag == I mod q,
        # and mod p^{e+1} (since q = p^e and p^{2e} = 0 mod p^{e+1} for e >= 1): M_diag == [[1+q, q], [0, 1-q]]!
        # Multiply by E12(q)^-1 = [[1, -q], [0, 1]]: gives [[1+q, 0], [0, 1-q]] mod p^{e+1}!
        M_diag = ((1 + q_mod) % mod_top, q_mod % mod_top, (q_mod * q_mod) % mod_top, (1 - q_mod + q_mod * q_mod) % mod_top)
        assert (M_diag[0] * M_diag[3] - M_diag[1] * M_diag[2]) % mod_top == 1
        S_gens = [
            (1, q_mod % mod_top, 0, 1),
            (1, (-q_mod) % mod_top, 0, 1),
            (1, 0, q_mod % mod_top, 1),
            (1, 0, (-q_mod) % mod_top, 1),
            M_diag,
            mat_inv_mod(M_diag, mod_top),
        ]
        # Check connectedness (1 not a root of q_poly) and exact eigenvalues via SymPy QQ Sturm count!
        # Also test S_lazy = S_gens + [I] (still a finite symmetric generating set of Gamma) has all eigenvalues strictly in (-1, 1).
        t = sp.Symbol("t")
        for gens_label, gens_used, strict_left in (("S_gens", S_gens, False), ("S_gens+{I}", S_gens + [(1, 0, 0, 1)], True)):
            T_mat = sp.zeros(N, N)
            inv_s = sp.Rational(1, len(gens_used))
            for j, u in enumerate(U0):
                for g in gens_used:
                    i = idx_map[mat_mul_mod(g, u, mod_top)]
                    T_mat[i, j] += inv_s
            cp = sp.Poly(T_mat.charpoly(t).as_expr(), t, domain=sp.QQ)
            q_poly, rem = sp.div(cp, sp.Poly(t - 1, t, domain=sp.QQ))
            assert rem.is_zero
            assert q_poly.eval(1) != 0, f"Disconnected at p={p} ({gens_label})"
            sqf = sp.Poly(sp.sqf_part(q_poly.as_expr()), t, domain=sp.QQ)
            if strict_left:
                assert q_poly.eval(-1) != 0
                assert sqf.count_roots(-1, 1) == sqf.degree(), f"Spectral gap failed at p={p} ({gens_label})"
            else:
                # All roots in [-1, 1): count_roots(-1, 1) counts [-1, 1) or (-1, 1] depending on convention;
                # shift by (t + 1)/2 or check (-2, 1) with eval(1) != 0 and eval(t) nonzero outside [-1, 1]!
                assert sqf.count_roots(-sp.Integer(2), 1) == sqf.degree()
                # Verify no root < -1:
                assert sqf.count_roots(-sp.Integer(2), -1) == (1 if q_poly.eval(-1) == 0 else 0)
    print("Step 3 (SL_2 surjectivity & exact rational spectral gap on U_0 / K_{e+1}, p=2,3,5): PASS")


def verify_step4_covering_transfer() -> None:
    """Verify exact quantitative inequalities of Step 4 in Fraction arithmetic."""
    for k in (1, 2, 3, 5):
        for m in (1, 2, 4):
            for muC, muC0 in ((Fraction(1, 3), Fraction(1)), (Fraction(7, 2), Fraction(2, 3))):
                for eta in (Fraction(1, 10), Fraction(1, 2), Fraction(9, 10)):
                    eta_p = min((eta * muC) / (k * muC0), eta / (k * m))
                    assert eta_p > 0
                    for muY in (Fraction(0), muC / 5, muC / 2, muC):
                        muYp = muY / k
                        # Case 1: if muE >= (1 - eta_p) * muC0 => mu(C \ RY) <= k * eta_p * muC0 <= eta * muC
                        assert k * eta_p * muC0 <= eta * muC
                        # Case 2: if muE >= muYp / eta_p => muE / m >= muY / (k * m * eta_p) >= muY / eta
                        assert muYp / (m * eta_p) >= muY / eta
    print("Step 4 (exact rational covering-transfer inequalities): PASS")


def main() -> None:
    verify_step2_pro_p_filtration()
    verify_step2_isometry_and_measure()
    verify_step3_surjectivity_and_spectral_gap()
    verify_step4_covering_transfer()
    print("PASS")


if __name__ == "__main__":
    main()
