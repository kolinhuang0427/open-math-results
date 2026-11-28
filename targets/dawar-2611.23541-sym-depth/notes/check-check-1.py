"""Independent exact-arithmetic verifier for targets/dawar-2611.23541-sym-depth."""

from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial, isqrt


def isqrt_ceil(n: int) -> int:
    r = isqrt(n)
    return r if r * r == n else r + 1


def verify_thresholds_and_group_action() -> None:
    """Verify Theorem 1, Theorem 2 thresholds and Lemma 1 S_n generation."""
    # 1. Theorem 1: min{d, n/2} >= 3^Delta => k >= 2 and 4(k+1) <= n
    for Delta, n_min, d_min in [(3, 54, 27), (4, 162, 81)]:
        for n in (n_min, n_min + 1, 200, 1000):
            for d in (d_min, n // 2, n, 2 * n):
                m = min(d, n // 2)
                assert m >= 3 ** Delta
                kp1 = 1
                while (kp1 + 1) ** Delta <= m:
                    kp1 += 1
                k = kp1 - 1
                assert k >= 2
                assert 4 * (k + 1) <= n
                assert (k + 1) ** Delta <= m

    # 2. Theorem 2: n >= 28, 9 <= d < n/3, 3*kappa <= n+2 => r + 2k < n, n >= k+5, k' >= 2, 4(k'+1) <= n
    for n in (28, 30, 50, 100):
        for kappa in range(2, (n + 2) // 3 + 1):
            k = kappa - 1
            for d in range(9, (n + 2) // 3):  # d < n/3
                assert d + 2 * k < n
                assert n >= k + 5
                kp1 = isqrt(d)
                assert kp1 >= 3
                assert 4 * kp1 <= n

    # 3. Lemma 1 group generation: A_U + (v w2 w1) generates A_{U uplus {v}}, and with S_U generates S_{U uplus {v}}
    # Test on U = {1,2,3,4,5}, v = 0 (size 5 + 1 = 6)
    def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(p[q[i]] for i in range(len(p)))

    def parity(p: tuple[int, ...]) -> int:
        inv = 0
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                if p[i] > p[j]:
                    inv += 1
        return inv & 1

    # Generate A_U on {1,2,3,4,5} using 3-cycles (0 stays fixed)
    A_U_gens = [(0, 2, 3, 1, 4, 5), (0, 2, 1, 4, 3, 5), (0, 1, 2, 4, 5, 3)]
    c3 = (2, 0, 1, 3, 4, 5)  # 3-cycle (0 2 1) = (v w2 w1)
    closure = {tuple(range(6))}
    frontier = [tuple(range(6))]
    while frontier:
        cur = frontier.pop()
        for g in A_U_gens + [c3]:
            nxt = compose(g, cur)
            if nxt not in closure:
                closure.add(nxt)
                frontier.append(nxt)
    assert len(closure) == factorial(6) // 2
    assert all(parity(p) == 0 for p in closure)
    # Combining with transposition (1 2) in S_U gives full S_6
    t12 = (0, 2, 1, 3, 4, 5)
    full = set(closure) | {compose(t12, p) for p in closure}
    assert len(full) == factorial(6)
    print("Theorems 1-2 thresholds & Lemma 1 S_n generation: PASS")


def verify_lemma2_decomposition() -> None:
    """Directly construct and verify Lemma 2 2-level tree decomposition + normalised pruning."""
    for d in (1, 2, 3, 5, 10, 16, 17, 35, 36, 64, 65, 100):
        # Path P_{d+1} with d edges (tw = 1, w = 1, bag size <= 2)
        r = isqrt_ceil(d)
        children = {i: ([i + 1] if i + 1 < d else []) for i in range(d)}
        bags = {i: {i, i + 1} for i in range(d)}
        rep_edges = {i: {(i, i + 1)} for i in range(d)}
        active = set(range(d))

        def subtree_weight(u: int) -> tuple[int, list[int]]:
            w_tot = 1 + len(rep_edges[u])
            nodes = [u]
            for v in children[u]:
                if v in active:
                    cw, cnodes = subtree_weight(v)
                    w_tot += cw
                    nodes.extend(cnodes)
            return w_tot, nodes

        S_nodes: set[int] = set()
        while True:
            comps_root = [u for u in active if u == 0 or (u - 1) not in active]
            heaviest_u = None
            max_depth = -1
            for cr in comps_root:
                stack = [(cr, 0)]
                while stack:
                    u, dep = stack.pop()
                    wt, _ = subtree_weight(u)
                    if wt > 2 * r and dep > max_depth:
                        max_depth = dep
                        heaviest_u = u
                    for v in children[u]:
                        if v in active:
                            stack.append((v, dep + 1))
            if heaviest_u is None:
                break
            S_nodes.add(heaviest_u)
            active.remove(heaviest_u)

        if not S_nodes:
            # S = empty (depth-1 decomposition: single node c_1 holding everything)
            bag_c1 = set().union(*(bags[u] for u in active))
            c1_edges = set().union(*(rep_edges[u] for u in active))
            K_bags = []
            K_edges = []
        else:
            bag_c1 = set().union(*(bags[u] for u in S_nodes))
            c1_edges = set().union(*(rep_edges[u] for u in S_nodes))
            comps_root = [u for u in active if u == 0 or (u - 1) not in active]
            K_bags = []
            K_edges = []
            for cr in comps_root:
                _, nodes = subtree_weight(cr)
                b = set()
                es: set[tuple[int, int]] = set()
                for u in nodes:
                    b |= bags[u]
                    es |= rep_edges[u]
                # Normalised pruning (lem:normalised-decomposition Items 2-3):
                # Item 2: keep only vertices incident to an edge in es (or below)
                used_verts = {v for e in es for v in e}
                b &= used_verts
                # Item 3: if beta'(c_K) <= beta'(c_1) (incl. es empty), absorb into c_1 and drop leaf
                if b.issubset(bag_c1):
                    c1_edges |= es
                else:
                    K_bags.append(b)
                    K_edges.append(es)

        # Item 2 on c_1 (vertices incident to any edge in F = c1_edges U union(K_edges))
        all_used = {v for e in c1_edges for v in e}
        for es in K_edges:
            all_used |= {v for e in es for v in e}
        bag_c1 &= all_used

        w_tw = 1
        assert len(c1_edges) + sum(len(es) for es in K_edges) == d
        assert len(bag_c1) <= 6 * (w_tw + 1) * r
        assert len(K_bags) <= 12 * r + 1
        for bk, es in zip(K_bags, K_edges):
            assert len(bk) <= 2 * (w_tw + 1) * r
            assert 1 <= len(es) <= 2 * r
            assert not bk.issubset(bag_c1)
            # Item 2 check: every v in bk is incident to an edge in es
            inc_verts = {v for e in es for v in e}
            assert bk.issubset(inc_verts)
    print("Lemma 2 balanced 2-level decomposition + normalised pruning (d=1..100 incl. non-squares): PASS")


def verify_theorem3_depth4_circuit() -> None:
    """Verify exact equality and Gamma_n-invariance of Theorem 3's depth-4 circuit on P_4, P_5."""
    # Pattern P_4: vertices {0,1,2,3}, bipartition A={0,2}, B={1,3}, edges (0,1), (2,1), (2,3).
    # Choose separator S = {node(2,1)}, i.e. bag(c_1) = {1, 2}, rep(c_1) = {(2,1)},
    # left component K1: bag {0,1}, rep {(0,1)}; right component K2: bag {2,3}, rep {(2,3)}.
    n = 4
    X = [[Fraction(i * n + j + 1, 7) for j in range(n)] for i in range(n)]

    def hom_P4_direct(mat: list[list[Fraction]]) -> Fraction:
        total = Fraction(0)
        for v0, v2 in product(range(n), repeat=2):
            for v1, v3 in product(range(n), repeat=2):
                total += mat[v0][v1] * mat[v2][v1] * mat[v2][v3]
        return total

    def hom_P4_depth4(mat: list[list[Fraction]]) -> Fraction:
        # Layer 1 (top Sigma): sum over gamma_1 on bag'(c_1) = {v2 in A, v1 in B}
        total = Fraction(0)
        for v2 in range(n):
            for v1 in range(n):
                # Layer 2 (Pi): x_{v2, v1} * S_{K1, v1} * S_{K2, v2}
                # Layer 3 (Sigma) & Layer 4 (Pi):
                s_K1 = sum((mat[v0][v1] for v0 in range(n)), Fraction(0))
                s_K2 = sum((mat[v2][v3] for v3 in range(n)), Fraction(0))
                total += mat[v2][v1] * s_K1 * s_K2
        return total

    val_dir = hom_P4_direct(X)
    val_d4 = hom_P4_depth4(X)
    assert val_dir == val_d4
    # Check Gamma_n-invariance under permutation of rows & cols
    sigma = (2, 0, 3, 1)
    tau = (1, 3, 0, 2)
    X_perm = [[X[sigma[i]][tau[j]] for j in range(n)] for i in range(n)]
    assert hom_P4_depth4(X_perm) == val_d4

    # Also test P_5 (edges (0,1), (2,1), (2,3), (4,3); A={0,2,4}, B={1,3}) with c_1 = {2}, K1 = {0,1,2}, K2 = {2,3,4}
    def hom_P5_direct(mat: list[list[Fraction]]) -> Fraction:
        total = Fraction(0)
        for v0, v2, v4 in product(range(n), repeat=3):
            for v1, v3 in product(range(n), repeat=2):
                total += mat[v0][v1] * mat[v2][v1] * mat[v2][v3] * mat[v4][v3]
        return total

    def hom_P5_depth4(mat: list[list[Fraction]]) -> Fraction:
        total = Fraction(0)
        for v2 in range(n):
            s_K1 = sum((mat[v0][v1] * mat[v2][v1] for v0 in range(n) for v1 in range(n)), Fraction(0))
            s_K2 = sum((mat[v2][v3] * mat[v4][v3] for v3 in range(n) for v4 in range(n)), Fraction(0))
            total += s_K1 * s_K2
        return total

    assert hom_P5_direct(X) == hom_P5_depth4(X) == hom_P5_depth4(X_perm)
    print("Theorem 3 depth-4 circuit & Gamma_n-invariance (P_4, P_5): PASS")


def verify_theorem4_fischer_and_q_descent() -> None:
    """Verify Fischer's identity, truncated exponential, and Q[t]/(mu_theta(t)) interpolation."""
    # 1. Exact Fischer's identity for b = 2, 3, 4 on rational vectors
    ys = [Fraction(3, 5), Fraction(-7, 11), Fraction(13, 17), Fraction(2, 9)]
    for b in (2, 3, 4):
        lhs = Fraction(1)
        for j in range(b):
            lhs *= ys[j]
        rhs = Fraction(0)
        for signs in product((-1, 1), repeat=b - 1):
            eps = (1,) + signs
            prod_eps = 1
            lin = Fraction(0)
            for e, y in zip(eps, ys[:b]):
                prod_eps *= e
                lin += e * y
            rhs += prod_eps * (lin ** b)
        rhs /= (2 ** (b - 1)) * factorial(b)
        assert lhs == rhs

    # 2. Exact Q[t]/(mu_theta(t)) descent test for a=2, b=2:
    # f_{2,2}(y) = 1 + y^2 + y^4/2. Roots satisfy y^4 + 2*y^2 + 2 = 0 (irreducible over Q by Eisenstein p=2!).
    # Wait: let's test the univariate polynomial reduction mod mu(t) = t^4 + 2*t^2 + 2:
    # Over Q(theta) where theta^4 + 2*theta^2 + 2 = 0:
    # Wait: if f_{2,2}(y) = 1/2 * prod_{r=1}^4 (y - root_r), over Q(theta) let's test a concrete splitting:
    # Actually let's verify truncated exponential [z^a] prod_r f_{a,b}(q * ell_r) * a! == (sum sigma_r ell_r^b)^a
    a, b = 2, 2
    ells = [Fraction(2, 3), Fraction(-5, 7)]
    sigmas = [1, -1]
    P_val = sum(sig * (ell ** b) for sig, ell in zip(sigmas, ells))
    target = P_val ** a

    # Evaluate H(z_q) at z_q = q^b for q = 0..M-1 (M = a*R'' + 1 = 2*2 + 1 = 5), extract a! * [z^a] H(z) via Lagrange
    M = a * len(ells) + 1
    zs = [Fraction(q ** b) for q in range(M)]
    H_vals = []
    for zq in zs:
        prod_val = Fraction(1)
        for sig, ell in zip(sigmas, ells):
            term_sum = Fraction(0)
            u = zq * sig * (ell ** b)
            for m_pow in range(a + 1):
                term_sum += (u ** m_pow) / factorial(m_pow)
            prod_val *= term_sum
        H_vals.append(prod_val)

    # Extract coefficient of z^a in the unique degree < M polynomial interpolating (zs[j], H_vals[j])
    def poly_mul_q(p1: list[Fraction], p2: list[Fraction]) -> list[Fraction]:
        out = [Fraction(0)] * (len(p1) + len(p2) - 1)
        for i, c1 in enumerate(p1):
            for j, c2 in enumerate(p2):
                out[i + j] += c1 * c2
        return out

    interp = [Fraction(0)] * M
    for j in range(M):
        num_poly = [Fraction(1)]
        denom = Fraction(1)
        for m_idx in range(M):
            if m_idx == j:
                continue
            num_poly = poly_mul_q(num_poly, [-zs[m_idx], Fraction(1)])
            denom *= (zs[j] - zs[m_idx])
        scale = H_vals[j] / denom
        for k_idx, coeff in enumerate(num_poly):
            interp[k_idx] += scale * coeff
    assert factorial(a) * interp[a] == target

    # 3. Also verify mod mu(t) = t^4 + 2*t^2 + 2 preserves t^0 term when evaluating product of conjugate factors:
    # Over Q(theta) with theta^4 + 2*theta^2 + 2 = 0, (y - theta)(y + theta)(y - theta_bar)...
    # Notice (y^2 - theta^2)(y^2 - (-2 - theta^2)) = y^4 + 2*y^2 + theta^2*(-2 - theta^2) = y^4 + 2*y^2 + 2!
    # Check at y = q * ell: replacing theta by t gives R(t) = (y^2 - t^2)(y^2 + 2 + t^2) in Q[t];
    # reducing R(t) modulo mu(t) = t^4 + 2*t^2 + 2 gives remainder y^4 + 2*y^2 + 2 (constant in t, matching t^0)!
    y_val = Fraction(7, 5)
    # R(t) = (y^2 - t^2)*(y^2 + 2 + t^2) = -t^4 - 2*t^2 + y^2*(y^2 + 2)
    # Using t^4 == -2*t^2 - 2 mod mu(t): R(t) == 2 + y^2*(y^2 + 2) = y^4 + 2*y^2 + 2 = 2 * f_{2,2}(y)!
    R_coeffs = [y_val ** 4 + 2 * (y_val ** 2), Fraction(0), Fraction(-2), Fraction(0), Fraction(-1)]
    # Evaluate R(t_nu) at 5 rational points t_nu, interpolate R_coeffs, and reduce mod t^4 + 2t^2 + 2:
    ts = [Fraction(v) for v in range(5)]
    R_vals = [sum(c * (tv ** idx) for idx, c in enumerate(R_coeffs)) for tv in ts]
    R_interp = [Fraction(0)] * 5
    for j in range(5):
        np_ = [Fraction(1)]
        den = Fraction(1)
        for m_idx in range(5):
            if m_idx == j:
                continue
            np_ = poly_mul_q(np_, [-ts[m_idx], Fraction(1)])
            den *= (ts[j] - ts[m_idx])
        sc = R_vals[j] / den
        for k_idx, cc in enumerate(np_):
            R_interp[k_idx] += sc * cc
    # Reduce R_interp mod (t^4 + 2t^2 + 2)
    mu = [Fraction(2), Fraction(0), Fraction(2), Fraction(0), Fraction(1)]
    rem = list(R_interp)
    lead = rem[4]
    for idx in range(5):
        rem[idx] -= lead * mu[idx]
    assert rem[1] == 0 and rem[2] == 0 and rem[3] == 0 and rem[4] == 0
    assert rem[0] == 2 * (1 + y_val ** 2 + (y_val ** 4) / 2)
    print("Theorem 4 Fischer + truncated exp + Q[t]/(mu) interpolation descent: PASS")


def main() -> None:
    verify_thresholds_and_group_action()
    verify_lemma2_decomposition()
    verify_theorem3_depth4_circuit()
    verify_theorem4_fischer_and_q_descent()
    print("PASS")


if __name__ == "__main__":
    main()
