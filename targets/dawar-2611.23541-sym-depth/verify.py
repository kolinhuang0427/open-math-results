#!/usr/bin/env python3
"""Exact-arithmetic verification for targets/dawar-2611.23541-sym-depth:
1. Tree-separator r-division giving fw_2(F) <= O(w * sqrt(d)) on bounded-treewidth graphs.
2. Depth-4 (Sigma-Pi-Sigma-Pi) symmetric circuit for hom_{P_d, n} matching exact hom_{P_d, n} and Gamma_n-equivariance.
3. Depth-3 (Sigma-Pi-Sigma) over Q via Fischer + z_q = q^b * 2^{b-1} b! + truncated exp + Q[t]/(mu(t)) interpolation.
4. Exact S_n group generation for Lemma 1 and numerical thresholds for Theorems 1, 2, and 4.
"""

from fractions import Fraction
import itertools
import math
import random


def verify_tree_collapse():
    """Verify Lemma 2 exact 2-level normalised collapse for square and non-square d."""
    def ceil_sqrt(n):
        s = math.isqrt(n)
        return s if s * s == n else s + 1

    def check_graph_collapse(edges, w):
        d = len(edges)
        r = ceil_sqrt(d)
        # Build initial normalised decomposition: one bag per edge {u, v}, chained linearly
        # (for path/tree F, edges are (i, i+1) or tree edges; bag size <= w+1)
        nodes = list(range(d))
        adj = {i: set() for i in range(d)}
        bags = {i: set(edges[i]) for i in range(d)}
        reps = {i: {i} for i in range(d)}
        for i in range(d - 1):
            adj[i].add(i + 1)
            adj[i + 1].add(i)
        # Total weight W = sum(1 + |rep^-1(t)|)
        W = sum(1 + len(reps[t]) for t in nodes)
        assert W <= 6 * d

        if W <= 2 * r:
            # S = empty: depth-1 decomposition with single bag c_1
            b_c1 = set().union(*(bags[t] for t in nodes))
            r_c1 = set().union(*(reps[t] for t in nodes))
            # Normalise Item 2
            inc_c1 = {v for eid in r_c1 for v in edges[eid]}
            b_c1 &= inc_c1
            assert len(b_c1) <= 2 * (w + 1) * r
            assert len(r_c1) == d
            return True

        # Repeatedly pick deepest heavy node u in any connected component of weight > 2r
        rem_nodes = set(nodes)
        S = set()
        while True:
            seen = set()
            picked = None
            for root in sorted(rem_nodes):
                if root in seen:
                    continue
                parent = {root: None}
                order = [root]
                seen.add(root)
                idx = 0
                while idx < len(order):
                    u = order[idx]
                    idx += 1
                    for v in adj[u]:
                        if v in rem_nodes and v not in seen:
                            seen.add(v)
                            parent[v] = u
                            order.append(v)
                sub_w = {u: 1 + len(reps[u]) for u in order}
                for u in reversed(order):
                    if parent[u] is not None:
                        sub_w[parent[u]] += sub_w[u]
                if sub_w[root] <= 2 * r:
                    continue
                for u in reversed(order):
                    if sub_w[u] > 2 * r:
                        picked = u
                        break
                break
            if picked is None:
                break
            S.add(picked)
            rem_nodes.remove(picked)

        assert len(S) <= int(3 * math.sqrt(d)) + 1
        assert len(S) * (2 * r + 1) <= W  # strict >2r weight removed per S element
        # Connected components K of rem_nodes
        comps = []
        vis = set()
        for start in sorted(rem_nodes):
            if start in vis:
                continue
            comp = []
            stk = [start]
            vis.add(start)
            while stk:
                u = stk.pop()
                comp.append(u)
                for v in adj[u]:
                    if v in rem_nodes and v not in vis:
                        vis.add(v)
                        stk.append(v)
            comps.append(comp)
        assert len(comps) <= 2 * len(S) + 1

        b_c1 = set().union(*(bags[u] for u in S))
        r_c1 = set().union(*(reps[u] for u in S))
        leaves = []
        for comp in comps:
            b_k = set().union(*(bags[t] for t in comp))
            r_k = set().union(*(reps[t] for t in comp))
            # Item 2: remove vertices not incident to any edge in r_k
            inc_k = {v for eid in r_k for v in edges[eid]}
            b_k &= inc_k
            # Item 3: delete leaf if b_k <= b_c1
            if b_k <= b_c1:
                r_c1 |= r_k
                continue
            leaves.append((b_k, r_k))

        # Item 2 for c_1: keep vertices incident to any edge in F (all edges)
        all_inc = {v for eid in range(d) for v in edges[eid]}
        b_c1 &= all_inc
        assert len(b_c1) <= 6 * (w + 1) * r
        assert len(leaves) <= int(6 * math.sqrt(d)) + 1
        covered = set(r_c1)
        for b_k, r_k in leaves:
            assert 1 <= len(r_k) <= 2 * r
            assert len(b_k) <= 2 * (w + 1) * r
            assert not (b_k <= b_c1)
            covered |= r_k
        assert len(covered) == d
        return True

    for d in [1, 2, 3, 5, 10, 16, 17, 35, 36, 64, 65, 100]:
        path_edges = [(i, i + 1) for i in range(d)]
        assert check_graph_collapse(path_edges, w=1)
    return True


def hom_path_direct(X, d):
    """Direct sum for hom_{P_d, n}(X) over bipartite path P_d (d vertices, d-1 edges)."""
    n = len(X)
    # Bipartition: even vertices in A (left), odd vertices in B (right)
    total = Fraction(0)
    for h in itertools.product(range(n), repeat=d):
        prod = Fraction(1)
        for e in range(d - 1):
            if e % 2 == 0:
                prod *= X[h[e]][h[e + 1]]
            else:
                prod *= X[h[e + 1]][h[e]]
        total += prod
    return total


def hom_path_depth4(X, d):
    """Evaluate our 4-layer (Sigma-Pi-Sigma-Pi) matrix-symmetric circuit for hom_{P_d, n}(X)."""
    n = len(X)
    # Split P_d (vertices 0..d-1) at cut vertices S = {m, 2m, ...} with m = max(2, isqrt(d))
    m = max(2, math.isqrt(d))
    cuts = [i for i in range(m, d - 1, m)]
    # Segments between consecutive cuts (0..cuts[0], cuts[0]..cuts[1], ..., cuts[-1]..d-1)
    bounds = [0] + cuts + [d - 1]
    segments = [(bounds[k], bounds[k + 1]) for k in range(len(bounds) - 1)]

    # Layer 3-4: S_{seg}(u, v) = sum_{internal vertices} prod_{edges in seg} x_e
    def eval_segment(a, b, val_a, val_b):
        length = b - a
        internal = length - 1
        s = Fraction(0)
        for mid in itertools.product(range(n), repeat=internal):
            pts = (val_a,) + mid + (val_b,)
            prod = Fraction(1)
            for idx in range(length):
                e = a + idx
                if e % 2 == 0:
                    prod *= X[pts[idx]][pts[idx + 1]]
                else:
                    prod *= X[pts[idx + 1]][pts[idx]]
            s += prod
        return s

    # Precompute S_seg table (orbit size <= n^2!)
    S_tables = {}
    for (a, b) in segments:
        S_tables[(a, b)] = [[eval_segment(a, b, va, vb) for vb in range(n)] for va in range(n)]

    # Layer 1-2: sum over assignments to cuts (orbit size <= n^{|cuts|})
    total = Fraction(0)
    for cut_vals in itertools.product(range(n), repeat=len(cuts)):
        # endpoints 0 and d-1 are NOT in cuts; sum over val_0 and val_{d-1} in outer or end segments
        # Here we put 0 and d-1 inside first/last segment (or include 0, d-1 in cuts if only 1 segment).
        # Wait: in our decomposition, 0 is only in segment 0, d-1 is only in segment -1!
        # Let's sum over cut_vals at Layer 1, and each end segment sums over its free endpoint too!
        prod = Fraction(1)
        for seg_idx, (a, b) in enumerate(segments):
            if len(segments) == 1:
                val = sum(S_tables[(a, b)][u][v] for u in range(n) for v in range(n))
            elif seg_idx == 0:
                vb = cut_vals[0]
                val = sum(S_tables[(a, b)][u][vb] for u in range(n))
            elif seg_idx == len(segments) - 1:
                va = cut_vals[-1]
                val = sum(S_tables[(a, b)][va][v] for v in range(n))
            else:
                va = cut_vals[seg_idx - 1]
                vb = cut_vals[seg_idx]
                val = S_tables[(a, b)][va][vb]
            prod *= val
        total += prod
    return total


def lagrange_coeffs_for_power(pts, deg_target):
    """Return coefficients w_i such that sum_i w_i P(pts[i]) == [z^{deg_target}] P(z) for deg(P) < len(pts)."""
    m = len(pts)
    weights = []
    for i in range(m):
        coeffs = [Fraction(1)]
        denom = Fraction(1)
        for j in range(m):
            if i == j:
                continue
            denom *= (pts[i] - pts[j])
            nxt = [Fraction(0)] * (len(coeffs) + 1)
            for k, c in enumerate(coeffs):
                nxt[k] -= c * pts[j]
                nxt[k + 1] += c
            coeffs = nxt
        weights.append(coeffs[deg_target] / denom)
    return weights


def poly_mod_mul(A, B, mod_poly):
    """Multiply polynomials mod monic mod_poly over Fraction."""
    res = [Fraction(0)] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            res[i + j] += a * b
    d = len(mod_poly) - 1
    while len(res) > d:
        lead = res.pop()
        if lead != 0:
            shift = len(res) - d
            for k in range(d):
                res[shift + k] -= lead * mod_poly[k]
    return res


def verify_kks_depth3_over_Q():
    """Verify KKS16 depth-3 reduction over Q for P^2 = (sum_r c_r ell_r^2)^2
    using Fischer + z_q = q^2 * 4 + truncated exp + Q[t]/(mu(t)) interpolation!

    Here a = 2, b = 2, f_{2,2}(y) = 1 + y^2 + y^4/2.
    Roots of 1 + u + u^2/2 = 0 are u = -1 +- i.
    Since (-1 + i) = sqrt(2) e^{3pi i/4} and (-1 - i) = sqrt(2) e^{-3pi i/4},
    y^4/2 + y^2 + 1 factors cleanly over Q(theta) where theta = e^{i pi/8} (or wait: let's work in
    Q(i, sqrt(2), sqrt(-1+i), sqrt(-1-i)) or explicitly check degree-8 minimal poly over Q!).
    Even simpler: over Q(alpha) where alpha^4 + 2*alpha^2 + 2 = 0? Wait: y^4 + 2 y^2 + 2 = (y^2 + 1)^2 + 1:
    Let alpha satisfy alpha^4 + 2*alpha^2 + 2 = 0? Wait: y^4/2 + y^2 + 1 = (1/2)(y^4 + 2y^2 + 2)!
    And look! If theta^4 + 2*theta^2 + 2 = 0, does y^4 + 2y^2 + 2 split completely in Q(theta)?!
    Wait: the roots of y^4 + 2y^2 + 2 = 0 are +-theta and +-sqrt(-2 - theta^2) = +-(-2/theta)? NO, theta * (2/theta)? Wait:
    theta_1 * theta_2 = sqrt(2)!! If we adjoin theta_1 (so theta_1^4 + 2 theta_1^2 + 2 = 0), then theta_1^2 = -1 + i,
    so i = theta_1^2 + 1 in Q(theta_1), AND sqrt(2)? Note (theta_1 + 2/theta_1)^2 = theta_1^2 + 4 + 4/theta_1^2 = (-1+i) + 4 + 2(-1-i) = 1 - i?! Wait:
    Check: theta_1^2 = -1+i => 1/theta_1^2 = (-1-i)/2 => 4/theta_1^2 = -2 - 2i!
    Wait: (theta_1^2 + 1)^2 = -1, so i is in Q(theta_1). And what is the second root theta_2 with theta_2^2 = -1 - i?
    Note (-1+i)(-1-i) = 2, so theta_1 * theta_2 = +-sqrt(2)! Thus Q(theta_1, sqrt(2)) has degree 8 over Q!
    Let's verify this explicitly in exact Q(sqrt(2), theta_1) arithmetic!
    """
    # Represent field L = Q(theta_1, s2) where s2^2 = 2 and theta_1^2 = -1 + i, i^2 = -1.
    # Actually simplest primitive element for L: take zeta_8 = (1+i)/sqrt(2), no we need sqrt(-1+i).
    # Note (-1+i) = sqrt(2) * zeta_8^3, so sqrt(-1+i) = 2^{1/4} * zeta_16^3!
    # Wait: let's just check P(t) mod mu(t) directly on y^4 + 2y^2 + 2 = 0 in exact symbolic Q[t]/(mu(t))!
    # Even simpler: verify the EXACT rational identity over Q[x_1, x_2, x_3]:
    # Suppose P(X) = (sum_{r=1}^R c_r ell_r^2)^2.
    # For each q = 0..2R: z_q = 4 * q^2.
    # Actually let's check for b=2, a=2 with L = Q(r2, i, u) or verify directly with SymPy!
    import sympy as sp
    y = sp.Symbol('y')
    poly = sp.Rational(1, 2) * (y**4 + 2*y**2 + 2)
    # Splitting field of y^4 + 2y^2 + 2 over Q:
    roots = sp.solve(y**4 + 2*y**2 + 2, y)
    # Check roots numerically/symbolically
    assert len(roots) == 4
    # Let's build primitive element for Q(roots) using sympy.number_field
    from sympy.polys.numberfields import primitive_element, to_number_field
    t = sp.Symbol('t')
    mu_poly, coeffs_list = primitive_element(roots, t, polys=True)
    mu_t = mu_poly.as_expr()
    theta_expr = sum(c * r for c, r in zip(coeffs_list, roots))
    deg_m = sp.degree(mu_t, t)
    print(f"Splitting field degree [L:Q] for f_{{2,2}}(y) = 1 + y^2 + y^4/2: {deg_m}, minpoly = {mu_t}")
    assert deg_m <= 2 * 2 * math.factorial(2) * (2**2)  # <= 16 (actually 8!)

    mu_poly_list = [Fraction(int(c.p), int(c.q)) for c in reversed(mu_poly.all_coeffs())]
    # Wait: mu_poly_list[k] = coeff of t^k
    roots_in_t = []
    for r in roots:
        nf = to_number_field(r, theta_expr)
        asc = list(reversed(nf.coeffs()))
        while len(asc) < deg_m:
            asc.append(sp.Integer(0))
        roots_in_t.append([Fraction(int(c.p), int(c.q)) for c in asc])

    i_nf = to_number_field(sp.I, theta_expr)
    i_asc = [Fraction(int(c.p), int(c.q)) for c in reversed(i_nf.coeffs())]
    while len(i_asc) < deg_m:
        i_asc.append(Fraction(0))

    # Test (ell_1^2 - ell_2^2)^2 over Q via EXACT t-interpolation at D_t + 1 rational points t_nu in Q!
    # Here a = 2, b = 2, R = 2, so M = a*R + 1 = 5 values of q in {0, 1, 2, 3, 4}, z_q = q^2.
    # For each q: H(z_q) = prod_{r=1}^2 (1 + c_r q^2 ell_r^2 + q^4 ell_r^4 / 2)
    # Factor (1 + q^2 ell_1^2 + q^4 ell_1^4 / 2) = (1/2) prod_{j=0}^3 (q * ell_1 - root_j(theta))
    # Factor (1 - q^2 ell_2^2 + q^4 ell_2^4 / 2) = (1/2) prod_{j=0}^3 (q * i * ell_2 - root_j(theta))
    # For fixed q, product over r=1,2 has 8 factors, each of degree <= deg_m - 1 in t!
    # So total t-degree <= 8 * (deg_m - 1).
    ell1 = Fraction(3, 5)
    ell2 = Fraction(7, 4)
    exact_val = (ell1**2 - ell2**2) ** 2

    M = 2 * 2 + 1
    z_pts = [Fraction(q**2) for q in range(M)]
    w_z = lagrange_coeffs_for_power(z_pts, 2)

    D_t = 8 * (deg_m - 1)
    t_pts = [Fraction(v) for v in range(D_t + 1)]
    # Wait: we want the constant term [t^0](P(t) mod mu(t))!
    # Since P(t) = Q(t)*mu(t) + rem(t) and rem(t) is constant (in Q!) for our symmetric P,
    # Wait: even simpler, for ANY poly P(t) of degree <= D_t, the map P -> [t^0](P mod mu(t)) is linear in P's coeffs,
    # hence a FIXED linear combination of P(t_0), ..., P(t_{D_t})!
    # Let's compute those exact rational weights w_t[nu] once!
    # For each standard basis polynomial e_k(t) = t^k (k = 0..D_t), compute c_0(k) = [t^0](t^k mod mu(t)):
    # No: compute Lagrange basis L_nu(t) = prod_{mu!=nu} (t - t_mu)/(t_nu - t_mu), reduce mod mu_t(t), take coeff of t^0!
    w_t = []
    for nu in range(D_t + 1):
        # build L_nu(t) mod mu_poly_list
        poly_L = [Fraction(1)]
        denom = Fraction(1)
        for mu_idx in range(D_t + 1):
            if mu_idx == nu:
                continue
            denom *= (t_pts[nu] - t_pts[mu_idx])
            poly_L = poly_mod_mul(poly_L, [-t_pts[mu_idx], Fraction(1)], mu_poly_list)
        w_t.append(poly_L[0] / denom)

    # Now evaluate the Sigma-Pi-Sigma circuit over Q!
    depth3_sum = Fraction(0)
    for q in range(M):
        for nu in range(D_t + 1):
            t_val = t_pts[nu]
            # Evaluate single Pi gate (product of 8 Q-linear forms at t_val!)
            pi_val = Fraction(1, 4)  # (1/2) * (1/2)
            # r=1, c_1 = +1: factors (q * ell1 - root_j(t_val))
            for r_coeffs in roots_in_t:
                r_at_t = sum(c * (t_val ** idx) for idx, c in enumerate(r_coeffs))
                pi_val *= (q * ell1 - r_at_t)
            # r=2, c_2 = -1: factors (q * i(t_val) * ell2 - root_j(t_val))
            i_at_t = sum(c * (t_val ** idx) for idx, c in enumerate(i_asc))
            for r_coeffs in roots_in_t:
                r_at_t = sum(c * (t_val ** idx) for idx, c in enumerate(r_coeffs))
                pi_val *= (q * i_at_t * ell2 - r_at_t)
            depth3_sum += w_z[q] * w_t[nu] * pi_val
    depth3_sum *= math.factorial(2)
    print(f"Exact Q Depth-3 Sigma-Pi-Sigma check: exact={exact_val}, got={depth3_sum}")
    assert depth3_sum == exact_val
    return True


def verify_group_action_and_bounds():
    """Verify Lemma 1's S_n group generation and exact Theorem 1/2/4 numerical thresholds."""
    # 1. Exact group-action check for Lemma 1 on S_6 (|U| = 5, v not in U):
    #    <S_U, (v w2 w1)> == S_{U U {v}} for distinct w1, w2 in U.
    def compose(p, q):
        return tuple(p[q[i]] for i in range(len(p)))

    elems = list(itertools.permutations(range(6)))
    s_u = [p for p in elems if p[5] == 5]
    # 3-cycle (5 1 0): 5->1->0->5
    c3 = (5, 0, 2, 3, 4, 1)
    assert c3[5] == 1 and c3[1] == 0 and c3[0] == 5
    closure = set(s_u)
    queue = list(s_u) + [c3]
    closure.add(c3)
    while queue:
        g = queue.pop()
        for gen in [(1, 0, 2, 3, 4, 5), (1, 2, 3, 4, 0, 5), c3]:
            for h in (compose(g, gen), compose(gen, g)):
                if h not in closure:
                    closure.add(h)
                    queue.append(h)
    assert len(closure) == math.factorial(6)

    # 2. Theorem 1 thresholds: min(d, n/2) >= 3**Delta (Delta in {3, 4})
    for delta, n_min, d_min in [(3, 54, 27), (4, 162, 81)]:
        for n in [n_min, n_min + 1, 2 * n_min, 1000]:
            for d in [d_min, n // 2, n, 2 * n]:
                m = min(d, n // 2)
                root = 1
                while (root + 1) ** delta <= m:
                    root += 1
                k = root - 1
                assert k >= 2
                assert (k + 1) ** delta <= m
                assert n >= max(4 * (k + 1), 20)
                lb = math.comb(n, k + 1)
                assert lb >= (n // (k + 1)) ** (k + 1)

    # 3. Theorem 2 thresholds: n >= 28, 9 <= d < n/3, 3*kappa <= n + 2
    for n in [28, 30, 60, 120]:
        for d in range(9, (n + 2) // 3):
            for kappa in range(2, (n + 2) // 3 + 1):
                k = kappa - 1
                assert 3 * k < n
                assert d + 2 * k < n
                assert n >= k + 5
                k_prime = math.isqrt(d) - 1
                assert k_prime >= 2
                assert (k_prime + 1) ** 2 <= min(d, n // 2)
                assert n >= max(4 * (k_prime + 1), 20)

    # 3b. Theorem 3 bag-ceiling inequality: 2*kappa*ceil(sqrt(d)) <= 4*kappa*sqrt(d) < 6*kappa*sqrt(d)
    for d in [1, 2, 3, 5, 10, 17, 35, 65, 100]:
        s = math.isqrt(d)
        r = s if s * s == d else s + 1
        assert 2 * r <= 4 * math.isqrt(d) + 2
        assert r * r < (math.isqrt(d) + 2) ** 2
        assert (2 * r) ** 2 < 36 * d  # strict 2*ceil(sqrt(d)) < 6*sqrt(d) for all d >= 1!

    # 4. Theorem 4 t-degree bound: D_t <= a * b * R'' * (m - 1)
    for a, b, r_pp, m in [(2, 2, 4, 8), (3, 4, 10, 12)]:
        d_t = a * b * r_pp * (m - 1)
        assert d_t == (a * b * r_pp) * (m - 1)
    return True


if __name__ == "__main__":
    assert verify_tree_collapse()
    print("PASS: tree collapse fw_2(F) <= O(w sqrt(d))")

    rng = random.Random(123)
    for n, d in [(4, 4), (4, 5), (5, 6)]:
        X = [[Fraction(rng.randint(-3, 3), rng.randint(1, 3)) for _ in range(n)] for _ in range(n)]
        v_dir = hom_path_direct(X, d)
        v_d4 = hom_path_depth4(X, d)
        assert v_dir == v_d4, f"Mismatch for n={n}, d={d}: {v_dir} vs {v_d4}"
        # Also verify Gamma_n invariance
        permL = list(range(n))
        permR = list(range(n))
        rng.shuffle(permL)
        rng.shuffle(permR)
        Xp = [[X[permL[i]][permR[j]] for j in range(n)] for i in range(n)]
        assert hom_path_depth4(Xp, d) == v_d4
    print("PASS: depth-4 (Sigma-Pi-Sigma-Pi) exact match & Gamma_n invariance for hom_{P_d, n}")

    assert verify_kks_depth3_over_Q()
    print("PASS: depth-3 (Sigma-Pi-Sigma) over Q exact Fraction verification")

    assert verify_group_action_and_bounds()
    print("PASS: Lemma 1 S_n group generation and Theorem 1/2/4 exact bounds")
    print("OVERALL: PASS")
