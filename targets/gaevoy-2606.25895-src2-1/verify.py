#!/usr/bin/env python3
"""Exact-arithmetic (zero-float) verification for gaevoy-2606.25895-src2-1.

Verifies:
  1. Lemma 1 exact integer inequality 157464 * 9^64 * 2^8 < 2^247 and exact
     rational union bound < 1 for all 2 <= n <= 30.
  2. Theorem 5 explicit 1-SRC-II refutations of guarded Tseitin formulas
     Ts_tilde(G, alpha) on 6 diverse connected graphs (K_4, K_{3,3}, irregular
     n=7, 3x3 toroidal grid H_3, Petersen graph, Mobius ladder M_{20}), checked
     by a strict Cook-Reckhow 1-SRC-II verifier.
  3. Full recursive unfolding of the 1-SRC-II refutations of K_4 and K_{3,3}
     into pure Resolution refutations of Ts_tilde(G, alpha), plus Lemma 2
     restriction (g -> 1) producing verified pure Resolution refutations of
     Ts(G, alpha) with strictly non-increasing size.
  4. Exact Fraction edge expansion e(G) on K_4, K_{3,3}, and Petersen graph.
"""

from collections import deque
from fractions import Fraction


def comb_int(n, r):
    if r < 0 or r > n:
        return 0
    if r > n - r:
        r = n - r
    num = 1
    den = 1
    for i in range(1, r + 1):
        num *= n - r + i
        den *= i
    assert num % den == 0
    return num // den


def flip_clause(clause, var):
    return frozenset(-lit if abs(lit) == var else lit for lit in clause)


def resolve_clauses(c1, c2, pivot):
    if pivot in c1 and -pivot in c2:
        res = (c1 - {pivot}) | (c2 - {-pivot})
    elif -pivot in c1 and pivot in c2:
        res = (c1 - {-pivot}) | (c2 - {pivot})
    else:
        raise AssertionError(f"Invalid pivot {pivot} for {c1}, {c2}")
    for lit in res:
        if -lit in res:
            raise AssertionError(f"Tautological resolvent {res}")
    return frozenset(res)


def clause_from_assign(assign, extra=()):
    lits = [(-var if val == 1 else var) for var, val in assign.items()]
    lits.extend(extra)
    return frozenset(lits)


def build_guarded_tseitin(n, edges, alpha):
    assert sum(alpha) % 2 == 1
    m = len(edges)
    g = m + 1
    inc = [[] for _ in range(n)]
    for eid, (u, v) in enumerate(edges, start=1):
        assert 0 <= u < n and 0 <= v < n and u != v
        inc[u].append((v, eid))
        inc[v].append((u, eid))

    ts_clauses = set()
    all_clauses = set()
    phi = set()
    all_g_by_v = {}
    for v in range(n):
        evars = [eid for _, eid in inc[v]]
        d = len(evars)
        all_g_by_v[v] = []
        for mask in range(1 << d):
            assign = {evars[i]: (mask >> i) & 1 for i in range(d)}
            c_base = clause_from_assign(assign)
            all_clauses.add(c_base)
            c_g = frozenset(c_base | {g})
            phi.add(c_g)
            all_g_by_v[v].append(c_g)
            if (sum(assign.values()) % 2) != alpha[v]:
                ts_clauses.add(c_base)
                phi.add(frozenset(c_base | {-g}))

    expected_clauses = sum(3 * (1 << (len(inc[v]) - 1)) for v in range(n))
    assert len(phi) == expected_clauses

    # Verify exact restriction phi|_{g=1} == Ts(G, alpha)
    restricted = {frozenset(c - {-g}) for c in phi if g not in c}
    assert restricted == ts_clauses
    return m, g, inc, ts_clauses, phi, all_g_by_v


def build_theorem5_src2_1_proof(n, edges, alpha):
    m, g, inc, ts_clauses, phi, all_g_by_v = build_guarded_tseitin(n, edges, alpha)
    steps = []
    clause_to_input_idx = {}

    # Phase 0: list all input clauses of phi first
    for c in sorted(phi, key=lambda cl: (len(cl), sorted(cl))):
        clause_to_input_idx[c] = len(steps)
        steps.append(("input", c))

    # BFS spanning tree from vertex 0
    order = [0]
    seen = {0}
    parent = {0: None}
    parent_edge = {}
    q = deque([0])
    while q:
        u = q.popleft()
        for w, eid in inc[u]:
            if w not in seen:
                seen.add(w)
                parent[w] = u
                parent_edge[w] = eid
                order.append(w)
                q.append(w)
    assert len(order) == n, "Graph must be connected"

    def tree_path_edges(u, w):
        def to_root(x):
            s = set()
            while parent[x] is not None:
                s.add(parent_edge[x])
                x = parent[x]
            return s
        return to_root(u) ^ to_root(w)

    def add_res(i1, i2, piv):
        idx = len(steps)
        steps.append(("res", i1, i2, piv))
        return idx

    def add_sym(j, var):
        idx = len(steps)
        steps.append(("sym", j, var))
        return idx

    def apply_sign_flip(step_idx, flip_edges):
        if not flip_edges:
            return step_idx
        cur = add_sym(step_idx, g)
        for e in sorted(flip_edges):
            cur = add_sym(cur, e)
        cur = add_sym(cur, g)
        return cur

    # Phase 1: spanning-tree induction
    U = {0}
    alpha_U = alpha[0]
    cut = sorted(eid for _, eid in inc[0])
    basic_assign = {e: 0 for e in cut}
    if (sum(basic_assign.values()) % 2) == alpha_U:
        basic_assign[cut[0]] = 1
    basic_idx = clause_to_input_idx[clause_from_assign(basic_assign, extra=[-g])]

    def derive_cut_clause(target_assign):
        assert (sum(target_assign.values()) % 2) != alpha_U
        S = [e for e in cut if target_assign[e] != basic_assign[e]]
        assert len(S) % 2 == 0
        # Compute W = vertices in U with odd degree in S
        odd_deg_U = set()
        for e in S:
            u, w = edges[e - 1]
            in_u = u if u in U else w
            if in_u in odd_deg_U:
                odd_deg_U.remove(in_u)
            else:
                odd_deg_U.add(in_u)
        W_list = sorted(odd_deg_U)
        assert len(W_list) % 2 == 0
        F1 = set()
        for i in range(0, len(W_list), 2):
            F1 ^= tree_path_edges(W_list[i], W_list[i + 1])
        F = set(S) | F1
        assert len(set(S) & F1) == 0
        for u in U:
            deg_F = sum(1 for _, eid in inc[u] if eid in F)
            assert deg_F % 2 == 0
        return apply_sign_flip(basic_idx, F)

    for v in order[1:]:
        evars = [eid for _, eid in inc[v]]
        Ev = [e for e in evars if e in cut]
        Epv = [e for e in evars if e not in cut]
        assert len(Ev) >= 1
        new_U = U | {v}
        new_alpha_U = alpha_U ^ alpha[v]
        new_cut = sorted((set(cut) - set(Ev)) | set(Epv))
        new_basic = {e: 0 for e in new_cut}
        if new_cut and (0 == new_alpha_U):
            new_basic[new_cut[0]] = 1

        r = len(Ev)
        layer = []
        for mask in range(1 << r):
            tau = {Ev[i]: (mask >> i) & 1 for i in range(r)}
            par_cut = (sum(new_basic[e] for e in cut if e not in Ev) + sum(tau.values())) % 2
            if par_cut != alpha_U:
                targ = {e: (tau[e] if e in Ev else new_basic[e]) for e in cut}
                layer.append(derive_cut_clause(targ))
            else:
                v_assign = {e: (tau[e] if e in Ev else new_basic[e]) for e in evars}
                assert (sum(v_assign.values()) % 2) != alpha[v]
                layer.append(clause_to_input_idx[clause_from_assign(v_assign, extra=[-g])])

        for bit in range(r):
            layer = [add_res(layer[i], layer[i + 1], Ev[bit]) for i in range(0, len(layer), 2)]
        assert len(layer) == 1
        basic_idx = layer[0]
        U = new_U
        alpha_U = new_alpha_U
        cut = new_cut
        basic_assign = new_basic

    # Phase 2: derive unit clause {g} from All(v_0) | g, then resolve with {-g}
    ev0 = [eid for _, eid in inc[0]]
    d0 = len(ev0)
    layer = [clause_to_input_idx[c] for c in all_g_by_v[0]]
    for bit in range(d0):
        layer = [add_res(layer[i], layer[i + 1], ev0[bit]) for i in range(0, len(layer), 2)]
    assert len(layer) == 1
    add_res(basic_idx, layer[0], g)

    return m, g, inc, ts_clauses, phi, steps


def strict_verify_src2_1(phi, steps):
    """Independent strict Cook-Reckhow verifier for 1-SRC-II."""
    phi_set = set(phi)
    derived_clauses = []
    premise_sets = []
    seen_clauses = set()

    for idx, st in enumerate(steps):
        kind = st[0]
        if kind == "input":
            c = frozenset(st[1])
            assert c in phi_set, f"Step {idx}: input clause not in phi"
            derived_clauses.append(c)
            premise_sets.append(frozenset([c]))
            seen_clauses.add(c)
        elif kind == "res":
            _, i1, i2, piv = st
            assert 0 <= i1 < idx and 0 <= i2 < idx and piv > 0
            c = resolve_clauses(derived_clauses[i1], derived_clauses[i2], piv)
            derived_clauses.append(c)
            premise_sets.append(premise_sets[i1] | premise_sets[i2])
            seen_clauses.add(c)
        elif kind == "sym":
            _, j, var = st
            assert 0 <= j < idx and var > 0
            B = premise_sets[j]
            assert B <= phi_set, f"Step {idx}: justification premises not in phi"
            new_B = frozenset(flip_clause(b, var) for b in B)
            assert new_B <= phi_set, f"Step {idx}: phi(B_i) not in phi"
            assert new_B <= seen_clauses, f"Step {idx}: phi(B_i) not yet derived"
            c = flip_clause(derived_clauses[j], var)
            derived_clauses.append(c)
            premise_sets.append(new_B)
            seen_clauses.add(c)
        else:
            raise AssertionError(f"Unknown rule: {kind}")

    assert derived_clauses[-1] == frozenset(), "Final clause is not empty"
    return derived_clauses, premise_sets


def unfold_to_pure_res(phi, steps):
    """Recursively unfold a 1-SRC-II proof into a pure Resolution proof."""
    res_steps = []
    # For each (step_idx, frozenset_of_flipped_vars) -> res_step_idx
    memo = {}

    def apply_flips(clause, flip_set):
        return frozenset(-lit if abs(lit) in flip_set else lit for lit in clause)

    def emit(idx, flip_set):
        key = (idx, flip_set)
        if key in memo:
            return memo[key]
        st = steps[idx]
        if st[0] == "input":
            c = apply_flips(st[1], flip_set)
            assert c in phi
            out = len(res_steps)
            res_steps.append(("input", c))
            memo[key] = out
            return out
        elif st[0] == "res":
            _, i1, i2, piv = st
            r1 = emit(i1, flip_set)
            r2 = emit(i2, flip_set)
            out = len(res_steps)
            res_steps.append(("res", r1, r2, piv))
            memo[key] = out
            return out
        elif st[0] == "sym":
            _, j, var = st
            new_flips = flip_set ^ frozenset([var])
            out = emit(j, new_flips)
            memo[key] = out
            return out
        else:
            raise AssertionError(st)

    last = emit(len(steps) - 1, frozenset())
    assert last == len(res_steps) - 1
    return res_steps


def verify_pure_res(phi, res_steps):
    phi_set = set(phi)
    clauses = []
    for idx, st in enumerate(res_steps):
        if st[0] == "input":
            c = frozenset(st[1])
            assert c in phi_set
            clauses.append(c)
        elif st[0] == "res":
            _, i1, i2, piv = st
            assert 0 <= i1 < idx and 0 <= i2 < idx
            clauses.append(resolve_clauses(clauses[i1], clauses[i2], piv))
        else:
            raise AssertionError(st)
    assert clauses[-1] == frozenset()
    return clauses


def restrict_res_g_true(res_steps, g, ts_clauses):
    """Exact Lemma 2 restriction (g -> 1) + weakening elimination."""
    orig_clauses = []
    out_steps = []
    out_clauses = []
    map_idx = {}

    for idx, st in enumerate(res_steps):
        if st[0] == "input":
            c = frozenset(st[1])
            orig_clauses.append(c)
            if g in c:
                continue
            c_res = frozenset(c - {-g})
            assert c_res in ts_clauses
            map_idx[idx] = len(out_steps)
            out_steps.append(("input", c_res))
            out_clauses.append(c_res)
        elif st[0] == "res":
            _, i1, i2, piv = st
            c1, c2 = orig_clauses[i1], orig_clauses[i2]
            c = resolve_clauses(c1, c2, piv)
            orig_clauses.append(c)
            if g in c:
                continue
            if piv == g:
                # Pick the parent containing -g (so g not in that parent)
                kept_parent = i2 if -g in c2 else i1
                assert g not in orig_clauses[kept_parent]
                map_idx[idx] = map_idx[kept_parent]
                assert out_clauses[map_idx[idx]] <= frozenset(c - {-g})
            else:
                r1, r2 = map_idx[i1], map_idx[i2]
                d1, d2 = out_clauses[r1], out_clauses[r2]
                if piv not in d1 and -piv not in d1:
                    map_idx[idx] = r1
                elif piv not in d2 and -piv not in d2:
                    map_idx[idx] = r2
                else:
                    d = resolve_clauses(d1, d2, piv)
                    map_idx[idx] = len(out_steps)
                    out_steps.append(("res", r1, r2, piv))
                    out_clauses.append(d)
                assert out_clauses[map_idx[idx]] <= frozenset(c - {-g})

    final_idx = map_idx[len(res_steps) - 1]
    assert out_clauses[final_idx] == frozenset()
    trimmed = out_steps[: final_idx + 1]
    verify_pure_res(ts_clauses, trimmed)
    assert len(trimmed) <= len(res_steps)
    return trimmed


def exact_edge_expansion(n, edges):
    best = None
    for mask in range(1, 1 << n):
        u_sz = bin(mask).count("1")
        if u_sz > n // 2:
            continue
        cut = 0
        for u, v in edges:
            in_u = (mask >> u) & 1
            in_v = (mask >> v) & 1
            if in_u != in_v:
                cut += 1
        ratio = Fraction(cut, u_sz)
        if best is None or ratio < best:
            best = ratio
    return best


def verify_lemma_1():
    # Exact integer inequality (2B)^8 < 1
    assert 157464 * (9**64) * (2**8) < (2**247)
    # Exact rational union bound < 1 for 2 <= n <= 30
    for n in range(2, 31):
        total = Fraction(0)
        for u in range(1, n // 2 + 1):
            s = u // 8
            t = u + s
            prob = Fraction(comb_int(t, u), comb_int(n, u)) ** 8
            term = comb_int(n, u) * comb_int(n - u, s) * prob
            assert term < Fraction(1, 1 << u)
            total += term
        assert total < 1
    print("[OK] Lemma 1 exact integer inequality and exact rational union bound (n=2..30) verified")


def verify_theorem_5_and_lemmas_2_3():
    graphs = [
        (
            "K_4",
            4,
            [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)],
            [1, 0, 0, 0],
            True,
            Fraction(2, 1),
        ),
        (
            "K_{3,3}",
            6,
            [(i, 3 + j) for i in range(3) for j in range(3)],
            [1, 0, 0, 0, 0, 0],
            True,
            Fraction(5, 3),
        ),
        (
            "Irregular_7",
            7,
            [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 0), (0, 3), (1, 4), (2, 5)],
            [1, 1, 1, 0, 0, 0, 0],
            False,
            None,
        ),
        (
            "Torus_3x3",
            9,
            [
                (3 * r + c, 3 * r + ((c + 1) % 3))
                for r in range(3)
                for c in range(3)
            ]
            + [
                (3 * r + c, 3 * ((r + 1) % 3) + c)
                for r in range(3)
                for c in range(3)
            ],
            [1] * 9,
            False,
            None,
        ),
        (
            "Petersen_10",
            10,
            [(i, (i + 1) % 5) for i in range(5)]
            + [(5 + i, 5 + ((i + 2) % 5)) for i in range(5)]
            + [(i, 5 + i) for i in range(5)],
            [1] + [0] * 9,
            False,
            Fraction(1, 1),
        ),
        (
            "Mobius_20",
            20,
            [(i, (i + 1) % 20) for i in range(20)] + [(i, i + 10) for i in range(10)],
            [1] + [0] * 19,
            False,
            None,
        ),
    ]

    for name, n, edges, alpha, do_unfold, exp_e in graphs:
        m, g, inc, ts_clauses, phi, steps = build_theorem5_src2_1_proof(n, edges, alpha)
        strict_verify_src2_1(phi, steps)
        delta = max(len(inc[v]) for v in range(n))
        bound = sum(3 * (1 << (len(inc[v]) - 1)) for v in range(n)) + (n - 1) * (
            (1 << (delta - 1)) * (m + 4) - 1
        ) + (1 << delta)
        assert len(steps) <= bound

        extra = ""
        if do_unfold:
            unfolded = unfold_to_pure_res(phi, steps)
            verify_pure_res(phi, unfolded)
            restricted = restrict_res_g_true(unfolded, g, ts_clauses)
            extra += f" unfolded_Res={len(unfolded)} restricted_Ts_Res={len(restricted)}"
        if exp_e is not None:
            e_val = exact_edge_expansion(n, edges)
            assert e_val == exp_e
            extra += f" e(G)={e_val}"

        print(
            f"[OK] {name:12s}: n={n:2d} m={m:2d} Delta={delta} |Phi|={len(phi):3d} "
            f"1-SRC-II={len(steps):4d} <= {bound}{extra}"
        )


def main():
    verify_lemma_1()
    verify_theorem_5_and_lemmas_2_3()
    print("PASS")


if __name__ == "__main__":
    main()
