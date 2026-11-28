"""Independent exact verifier for targets/cai-2610.02047-plog-reg."""

from __future__ import annotations

import pathlib
import random
import re
import tarfile
from collections import deque


# Literal representation: non-zero int (v > 0 -> var v positive, -v -> negated)
# Multiclause: tuple[int, ...] (may have repeated literals; red(M) = frozenset(M))


def var_of(lit: int) -> int:
    return abs(lit)


def is_taut(lits: frozenset[int] | tuple[int, ...]) -> bool:
    s = set(lits)
    return any(-x in s for x in s)


def alpha_satisfies(alpha: dict[int, int], clause: frozenset[int]) -> bool:
    for lit in clause:
        v = abs(lit)
        if v in alpha:
            val = alpha[v]
            if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                return True
    return False


def c_alpha_lits(alpha: dict[int, int]) -> frozenset[int]:
    return frozenset((-v if val == 1 else v) for v, val in alpha.items())


def ordered_subclause(clause: frozenset[int], allowed_vars: set[int], order_idx: dict[int, int]) -> tuple[int, ...]:
    return tuple(sorted((l for l in clause if abs(l) in allowed_vars), key=lambda l: order_idx[abs(l)]))


def c1_family(ordered_lits: tuple[int, ...]) -> list[tuple[int, ...]]:
    r = len(ordered_lits)
    out: list[tuple[int, ...]] = []
    for i in range(r):
        out.append((-ordered_lits[i],) + ordered_lits[i + 1:])
    return out


class MResDAG:
    """Tracks mRes derivation steps and converts via lem:mres-to-res to verify regularity."""

    def __init__(self, initial_clauses: set[frozenset[int]]) -> None:
        self.initial_clauses = initial_clauses
        self.nodes: list[dict] = []
        self.by_key: dict[tuple[str, frozenset[int], tuple], int] = {}

    def add_initial(self, c: frozenset[int]) -> int:
        assert c in self.initial_clauses
        key = ("init", c, ())
        if key not in self.by_key:
            idx = len(self.nodes)
            self.nodes.append({"kind": "init", "red": c, "parents": (), "pivot": None})
            self.by_key[key] = idx
        return self.by_key[key]

    def add_axiom(self, v: int, target: frozenset[int]) -> int:
        assert v in target and -v in target
        key = ("taut", target, (v,))
        if key not in self.by_key:
            idx = len(self.nodes)
            self.nodes.append({"kind": "taut", "red": target, "parents": (), "pivot": None})
            self.by_key[key] = idx
        return self.by_key[key]

    def add_weaken(self, p: int, target: frozenset[int]) -> int:
        pred = self.nodes[p]["red"]
        assert pred.issubset(target), f"Invalid weaken: {pred} not subset of {target}"
        if pred == target:
            return p
        key = ("weak", target, (p,))
        if key not in self.by_key:
            idx = len(self.nodes)
            self.nodes.append({"kind": "weak", "red": target, "parents": (p,), "pivot": None})
            self.by_key[key] = idx
        return self.by_key[key]

    def add_resolve(self, p1: int, p2: int, v: int) -> int:
        r1 = self.nodes[p1]["red"]
        r2 = self.nodes[p2]["red"]
        assert v in r1 and -v in r2, f"Missing pivot +/-{v} in {r1}, {r2}"
        target = (r1 - {v}) | (r2 - {-v})
        # Check lem:mres-to-res: if target is non-tautological, non-elim becomes weaken in pi'
        key = ("res", target, (p1, p2, v))
        if key not in self.by_key:
            idx = len(self.nodes)
            self.nodes.append({"kind": "res", "red": target, "parents": (p1, p2), "pivot": v})
            self.by_key[key] = idx
        return self.by_key[key]

    def verify_regular_refutation(self, root_id: int) -> tuple[bool, int]:
        assert self.nodes[root_id]["red"] == frozenset(), "Root is not empty clause"
        # Convert via lem:mres-to-res: delete tautological nodes, replace non-elim res with weaken
        reachable: set[int] = set()
        q = deque([root_id])
        while q:
            u = q.popleft()
            if u in reachable:
                continue
            reachable.add(u)
            nd = self.nodes[u]
            assert not is_taut(nd["red"]) or nd["kind"] == "taut"
            if is_taut(nd["red"]):
                continue
            if nd["kind"] == "res":
                p1, p2 = nd["parents"]
                v = nd["pivot"]
                red = nd["red"]
                if v in red:
                    q.append(p1)
                elif -v in red:
                    q.append(p2)
                else:
                    q.append(p1)
                    q.append(p2)
            else:
                for p in nd["parents"]:
                    q.append(p)

        # Topological order on reachable non-tautological nodes
        non_taut = [u for u in range(len(self.nodes)) if u in reachable and not is_taut(self.nodes[u]["red"])]
        seen_res_vars: dict[int, set[int]] = {}
        for u in non_taut:
            nd = self.nodes[u]
            if nd["kind"] == "init":
                seen_res_vars[u] = set()
            elif nd["kind"] == "weak":
                p = nd["parents"][0]
                seen_res_vars[u] = set(seen_res_vars[p])
            elif nd["kind"] == "res":
                p1, p2 = nd["parents"]
                v = nd["pivot"]
                red = nd["red"]
                if v in red:
                    seen_res_vars[u] = set(seen_res_vars[p1])
                elif -v in red:
                    seen_res_vars[u] = set(seen_res_vars[p2])
                else:
                    # Variable-eliminating resolution on v!
                    if v in seen_res_vars[p1] or v in seen_res_vars[p2]:
                        return False, len(non_taut)
                    seen_res_vars[u] = seen_res_vars[p1] | seen_res_vars[p2] | {v}
        return True, len(non_taut)


def lemma2_elim(
    dag: MResDAG,
    g_lits: frozenset[int],
    e_lits: frozenset[int],
    h_ordered: tuple[int, ...],
    l0_id: int,
    r_ids: list[int],
) -> int:
    target = g_lits | e_lits
    assert not is_taut(target)
    q = len(h_ordered)
    if q == 0:
        return dag.add_weaken(l0_id, target)
    j_set = [j for j, lit in enumerate(h_ordered) if -lit in g_lits]
    if j_set:
        j0 = max(j_set)
        tail = frozenset(h_ordered[j0 + 1:])
        cur = dag.add_weaken(r_ids[j0], target | tail)
        start = j0 + 1
    else:
        cur = l0_id
        start = 0
    for j in range(start, q):
        lit = h_ordered[j]
        tail = frozenset(h_ordered[j + 1:])
        cur_red = dag.nodes[cur]["red"]
        assert cur_red == (target | {lit} | tail), f"S_{j-1} mismatch: {cur_red} vs {target | {lit} | tail}"
        r_red = dag.nodes[r_ids[j]]["red"]
        assert -lit in r_red
        if lit in g_lits:
            # In mRes we can still resolve or weaken directly (lem:mres-to-res drops R_j)
            cur = dag.add_weaken(cur, target | tail)
        else:
            res_id = dag.add_resolve(cur, r_ids[j], abs(lit)) if lit > 0 else dag.add_resolve(r_ids[j], cur, abs(lit))
            cur = dag.add_weaken(res_id, target | tail)
    assert dag.nodes[cur]["red"] == target
    return cur


class TreeNode:
    def __init__(self, nid: int, kind: str, bag_v: set[int], bag_c: set[int], payload: int | None, children: list[int]) -> None:
        self.nid = nid
        self.kind = kind  # leaf, intro_v, forget_v, intro_c, forget_c, join
        self.bag_v = bag_v
        self.bag_c = bag_c
        self.payload = payload
        self.children = children


def build_proof_on_td(
    clauses: list[frozenset[int]],
    nodes: dict[int, TreeNode],
    root_id: int,
    p_paths: dict[int, set[int]],
) -> tuple[bool, int]:
    """Execute the corrected bottom-up construction and verify regularity on the whole DAG."""
    # Post-order traversal and forg(v) order
    post_order: list[int] = []
    forg_node: dict[int, int] = {}

    def dfs(u: int) -> None:
        nd = nodes[u]
        for ch in nd.children:
            dfs(ch)
        post_order.append(u)
        if nd.kind == "forget_v":
            assert nd.payload is not None
            forg_node[nd.payload] = u

    dfs(root_id)
    post_idx = {u: i for i, u in enumerate(post_order)}
    all_vars = set(forg_node.keys())
    var_order = {v: post_idx[forg_node[v]] for v in all_vars}

    # Subtree Var_t and Cls_t
    var_t: dict[int, set[int]] = {}
    cls_t: dict[int, set[int]] = {}
    for u in post_order:
        nd = nodes[u]
        vt = set(nd.bag_v)
        ct = set(nd.bag_c)
        for ch in nd.children:
            vt |= var_t[ch]
            ct |= cls_t[ch]
        var_t[u] = vt
        cls_t[u] = ct

    # Compute inconsistent states bottom-up via consistency DP
    # Assignment on bag_v encoded as sorted tuple of (v, val)
    def all_alphas(bag_v: set[int]) -> list[dict[int, int]]:
        vs = sorted(bag_v)
        out: list[dict[int, int]] = []
        for mask in range(1 << len(vs)):
            out.append({v: (mask >> i) & 1 for i, v in enumerate(vs)})
        return out

    def key_alpha(a: dict[int, int]) -> tuple[tuple[int, int], ...]:
        return tuple(sorted(a.items()))

    inconsistent: dict[tuple[int, tuple[tuple[int, int], ...], frozenset[int]], bool] = {}

    for u in post_order:
        nd = nodes[u]
        for alpha in all_alphas(nd.bag_v):
            ka = key_alpha(alpha)
            bc = sorted(nd.bag_c)
            for amask in range(1 << len(bc)):
                aset = frozenset(c for i, c in enumerate(bc) if (amask >> i) & 1)
                if nd.kind == "leaf":
                    inc = False
                elif nd.kind == "intro_c":
                    c = nd.payload
                    assert c is not None
                    ch = nd.children[0]
                    if c not in aset:
                        inc = inconsistent[(ch, ka, aset)]
                    elif alpha_satisfies(alpha, clauses[c]):
                        inc = inconsistent[(ch, ka, aset - {c})]
                    else:
                        inc = True
                elif nd.kind == "intro_v":
                    x = nd.payload
                    assert x is not None
                    ch = nd.children[0]
                    lit = x if alpha[x] == 1 else -x
                    a_sub = frozenset(c for c in aset if lit not in clauses[c])
                    alpha_p = {k: v for k, v in alpha.items() if k != x}
                    inc = inconsistent[(ch, key_alpha(alpha_p), a_sub)]
                elif nd.kind == "forget_v":
                    x = nd.payload
                    assert x is not None
                    ch = nd.children[0]
                    a0 = dict(alpha)
                    a0[x] = 0
                    a1 = dict(alpha)
                    a1[x] = 1
                    inc = inconsistent[(ch, key_alpha(a0), aset)] and inconsistent[(ch, key_alpha(a1), aset)]
                elif nd.kind == "forget_c":
                    c = nd.payload
                    assert c is not None
                    ch = nd.children[0]
                    inc = inconsistent[(ch, ka, aset | {c})]
                elif nd.kind == "join":
                    c1, c2 = nd.children
                    # By join_zero_recursion: inconsistent iff for all A1 U A2 = A, one side inc
                    # Equivalently, check exact all subsets A1 <= A and A2 = A \ A1? Wait: A1 U A2 = A
                    # Check all A1 <= A, A2 = A \ A1 suffices by monotonicity!
                    inc = True
                    al = sorted(aset)
                    for m1 in range(1 << len(al)):
                        a1 = frozenset(c for i, c in enumerate(al) if (m1 >> i) & 1)
                        a2 = aset - a1
                        if not (inconsistent[(c1, ka, a1)] or inconsistent[(c2, ka, a2)]):
                            inc = False
                            break
                else:
                    raise ValueError(nd.kind)
                inconsistent[(u, ka, aset)] = inc

    assert inconsistent[(root_id, (), frozenset())], "Formula must be unsatisfiable"

    dag = MResDAG(set(clauses))
    derived: dict[tuple[int, tuple[tuple[int, int], ...], frozenset[int], tuple[tuple[int, int], ...]], int] = {}

    def target_m(
        u: int,
        alpha: dict[int, int],
        aset: frozenset[int],
        choices: dict[int, int],
    ) -> frozenset[int]:
        nd = nodes[u]
        pt = {c for c in nd.bag_c if u in p_paths[c]}
        lits: set[int] = set(c_alpha_lits(alpha))
        for c in aset:
            if c in pt:
                if not alpha_satisfies(alpha, clauses[c]):
                    lits |= {l for l in clauses[c] if abs(l) not in var_t[u]}
            else:
                sub = ordered_subclause(clauses[c], var_t[u], var_order)
                c1s = c1_family(sub)
                lits |= set(c1s[choices[c]])
        for c in nd.bag_c - pt - aset:
            if not alpha_satisfies(alpha, clauses[c]):
                lits |= {l for l in clauses[c] if abs(l) in var_t[u]}
        return frozenset(lits)

    def get_derived(u: int, alpha: dict[int, int], aset: frozenset[int], choices: dict[int, int]) -> int:
        nd = nodes[u]
        pt = {c for c in nd.bag_c if u in p_paths[c]}
        off_a = sorted(aset - pt)
        ckey = tuple((c, choices[c]) for c in off_a)
        key = (u, key_alpha(alpha), aset, ckey)
        if key in derived:
            return derived[key]
        t_lits = target_m(u, alpha, aset, choices)
        if is_taut(t_lits):
            for l in t_lits:
                if -l in t_lits:
                    res = dag.add_axiom(abs(l), t_lits)
                    derived[key] = res
                    return res
        raise KeyError(f"Missing non-tautological derived clause {key}")

    def make_target(u: int, t_lits: frozenset[int], builder) -> int:
        if is_taut(t_lits):
            for l in t_lits:
                if -l in t_lits:
                    return dag.add_axiom(abs(l), t_lits)
        return builder()

    # Build bottom-up
    for u in post_order:
        nd = nodes[u]
        pt = {c for c in nd.bag_c if u in p_paths[c]}
        for alpha in all_alphas(nd.bag_v):
            ka = key_alpha(alpha)
            bc = sorted(nd.bag_c)
            for amask in range(1 << len(bc)):
                aset = frozenset(c for i, c in enumerate(bc) if (amask >> i) & 1)
                if not inconsistent[(u, ka, aset)]:
                    continue
                off_a = sorted(aset - pt)
                # Check if any off-path clause has empty internal part
                sub_map = {c: ordered_subclause(clauses[c], var_t[u], var_order) for c in off_a}
                if any(len(sub_map[c]) == 0 for c in off_a):
                    continue
                choice_lists = [[i for i in range(len(sub_map[c]))] for c in off_a]

                # Cartesian product of choices
                def iter_choices(idx: int, cur: dict[int, int]):
                    if idx == len(off_a):
                        yield dict(cur)
                        return
                    c = off_a[idx]
                    for ci in choice_lists[idx]:
                        cur[c] = ci
                        yield from iter_choices(idx + 1, cur)

                for choices in iter_choices(0, {}):
                    ckey = tuple((c, choices[c]) for c in off_a)
                    full_key = (u, ka, aset, ckey)
                    t_lits = target_m(u, alpha, aset, choices)
                    if is_taut(t_lits):
                        for l in t_lits:
                            if -l in t_lits:
                                derived[full_key] = dag.add_axiom(abs(l), t_lits)
                                break
                        continue

                    if nd.kind == "intro_c":
                        c = nd.payload
                        assert c is not None
                        ch = nd.children[0]
                        if c not in aset:
                            mp = get_derived(ch, alpha, aset, choices)
                            derived[full_key] = dag.add_weaken(mp, t_lits)
                        elif alpha_satisfies(alpha, clauses[c]):
                            mp = get_derived(ch, alpha, aset - {c}, choices)
                            derived[full_key] = dag.add_weaken(mp, t_lits)
                        else:
                            if c in pt:
                                init_id = dag.add_initial(clauses[c])
                                derived[full_key] = dag.add_weaken(init_id, t_lits)
                            else:
                                li = sub_map[c][choices[c]]
                                derived[full_key] = dag.add_axiom(abs(li), t_lits)

                    elif nd.kind == "intro_v":
                        x = nd.payload
                        assert x is not None
                        ch = nd.children[0]
                        lit = x if alpha[x] == 1 else -x
                        a_x = frozenset(c for c in aset if lit not in clauses[c])
                        alpha_p = {k: v for k, v in alpha.items() if k != x}
                        # Project choices for c in a_x \ pt
                        base_choices: dict[int, int] = {}
                        for c in a_x - pt:
                            sub_c = sub_map[c]
                            sub_cp = ordered_subclause(clauses[c], var_t[ch], var_order)
                            lead = sub_c[choices[c]]
                            assert lead != -lit, "Non-tautological M cannot start at -lit"
                            base_choices[c] = sub_cp.index(lead)
                        a_base = set(a_x)
                        w_p_set: set[int] = set()
                        for c in (aset - a_x) - pt:
                            sub_c = sub_map[c]
                            p_pos = sub_c.index(lit)
                            idx_c = choices[c]
                            assert idx_c >= p_pos
                            if idx_c > p_pos:
                                a_base.add(c)
                                sub_cp = ordered_subclause(clauses[c], var_t[ch], var_order)
                                base_choices[c] = sub_cp.index(sub_c[idx_c])
                            else:
                                if (
                                    not alpha_satisfies(alpha_p, clauses[c])
                                    and len(ordered_subclause(clauses[c], var_t[ch] - nodes[ch].bag_v, var_order)) > 0
                                ):
                                    w_p_set.add(c)
                        s_sat_set: set[int] = {
                            c
                            for c in (nd.bag_c - pt - aset)
                            if lit in clauses[c]
                            and not alpha_satisfies(alpha_p, clauses[c])
                            and len(ordered_subclause(clauses[c], var_t[ch] - nodes[ch].bag_v, var_order)) > 0
                        }
                        w_elim = sorted(w_p_set | s_sat_set)
                        a_base_fs = frozenset(a_base)
                        p_ch = {c for c in nodes[ch].bag_c if ch in p_paths[c]}
                        assert p_ch == pt

                        def build_intro_level(d: int, u_set: frozenset[int], u_choices: dict[int, int]) -> int:
                            if d == len(w_elim):
                                ch_choices = dict(base_choices)
                                ch_choices.update(u_choices)
                                return get_derived(ch, alpha_p, a_base_fs | u_set, ch_choices)
                            cd = w_elim[d]
                            sub_cp = ordered_subclause(clauses[cd], var_t[ch], var_order)
                            h_ord = tuple(l for l in sub_cp if abs(l) not in nodes[ch].bag_v)
                            # Target at level d
                            g_set: set[int] = set(c_alpha_lits(alpha_p))
                            for c in (a_base_fs | u_set):
                                if c in pt:
                                    if not alpha_satisfies(alpha_p, clauses[c]):
                                        g_set |= {l for l in clauses[c] if abs(l) not in var_t[ch]}
                                else:
                                    sc = ordered_subclause(clauses[c], var_t[ch], var_order)
                                    ci = u_choices[c] if c in u_set else base_choices[c]
                                    g_set |= set(c1_family(sc)[ci])
                            for c in (frozenset(w_elim[:d]) - u_set):
                                g_set |= set(ordered_subclause(clauses[c], var_t[ch], var_order))
                            for c in nodes[ch].bag_c - pt - (a_base_fs | u_set | frozenset(w_elim)):
                                if not alpha_satisfies(alpha_p, clauses[c]):
                                    g_set |= {l for l in clauses[c] if abs(l) in var_t[ch]}
                            g_fs = frozenset(g_set)
                            if is_taut(g_fs):
                                for l in g_fs:
                                    if -l in g_fs:
                                        return dag.add_axiom(abs(l), g_fs)
                            if len(h_ord) == 0:
                                return build_intro_level(d + 1, u_set, u_choices)
                            l0_id = build_intro_level(d + 1, u_set, u_choices)
                            r_ids: list[int] = []
                            for hl in h_ord:
                                nc = dict(u_choices)
                                nc[cd] = sub_cp.index(hl)
                                r_ids.append(build_intro_level(d + 1, u_set | {cd}, nc))
                            return lemma2_elim(dag, g_fs, frozenset(), h_ord, l0_id, r_ids)

                        m_tp = build_intro_level(0, frozenset(), {})
                        derived[full_key] = dag.add_weaken(m_tp, t_lits)

                    elif nd.kind == "forget_v":
                        x = nd.payload
                        assert x is not None
                        ch = nd.children[0]
                        a0 = dict(alpha)
                        a0[x] = 0
                        a1 = dict(alpha)
                        a1[x] = 1
                        if x in t_lits:
                            m0 = get_derived(ch, a0, aset, choices)
                            derived[full_key] = dag.add_weaken(m0, t_lits)
                        elif -x in t_lits:
                            m1 = get_derived(ch, a1, aset, choices)
                            derived[full_key] = dag.add_weaken(m1, t_lits)
                        else:
                            m0 = get_derived(ch, a0, aset, choices)
                            m1 = get_derived(ch, a1, aset, choices)
                            res = dag.add_resolve(m0, m1, x)
                            derived[full_key] = dag.add_weaken(res, t_lits)

                    elif nd.kind == "forget_c":
                        c = nd.payload
                        assert c is not None
                        ch = nd.children[0]
                        p_ch = {cc for cc in nodes[ch].bag_c if ch in p_paths[cc]}
                        if c in p_ch:
                            derived[full_key] = dag.add_weaken(get_derived(ch, alpha, aset | {c}, choices), t_lits)
                        else:
                            c_ord = ordered_subclause(clauses[c], var_t[ch], var_order)
                            assert set(c_ord) == clauses[c]
                            j_set = [j for j, l in enumerate(c_ord) if -l in t_lits]
                            l0_id = dag.add_weaken(dag.add_initial(clauses[c]), t_lits | clauses[c]) if not j_set else -1
                            r_ids: list[int] = []
                            for j in range(len(c_ord)):
                                if j_set and j < max(j_set):
                                    r_ids.append(-1)
                                else:
                                    nc = dict(choices)
                                    nc[c] = j
                                    r_ids.append(get_derived(ch, alpha, aset | {c}, nc))
                            derived[full_key] = lemma2_elim(dag, t_lits, frozenset(), c_ord, l0_id, r_ids)

                    elif nd.kind == "join":
                        c1, c2 = nd.children
                        p_c1 = {d for d in nd.bag_c if c1 in p_paths[d]}
                        p_c2 = {d for d in nd.bag_c if c2 in p_paths[d]}
                        b1 = aset & p_c1
                        b2 = aset & p_c2
                        b0_unsat = sorted(d for d in (aset & pt) if not alpha_satisfies(alpha, clauses[d]))
                        b1_pure = frozenset(
                            d for d in (b1 & set(b0_unsat))
                            if not {l for l in clauses[d] if abs(l) in (var_t[c2] - nd.bag_v)}
                        )
                        b2_pure = frozenset(
                            d for d in (b2 & set(b0_unsat))
                            if not {l for l in clauses[d] if abs(l) in (var_t[c1] - nd.bag_v)}
                        )
                        b0_split = sorted(set(b0_unsat) - b1_pure - b2_pure)
                        a1_off: set[int] = set()
                        a2_off: set[int] = set()
                        for c in off_a:
                            lead = sub_map[c][choices[c]]
                            if abs(lead) in (var_t[c1] - nd.bag_v):
                                a1_off.add(c)
                            else:
                                a2_off.add(c)

                        def build_join(
                            h: int,
                            a1_b: frozenset[int],
                            a2_b: frozenset[int],
                            cb2: dict[int, int],
                            cb1: dict[int, int],
                        ) -> int:
                            # Target T(h, ...)
                            t_set: set[int] = set(c_alpha_lits(alpha))
                            for d in ((a1_b & b1) | b1_pure):
                                t_set |= {l for l in clauses[d] if abs(l) not in var_t[c1]}
                            for d in a1_b & b2:
                                t_set |= set(c1_family(ordered_subclause(clauses[d], var_t[c1], var_order))[cb2[d]])
                            for d in ((a2_b & b2) | b2_pure):
                                t_set |= {l for l in clauses[d] if abs(l) not in var_t[c2]}
                            for d in a2_b & b1:
                                t_set |= set(c1_family(ordered_subclause(clauses[d], var_t[c2], var_order))[cb1[d]])
                            for d in b0_split[h:]:
                                t_set |= {l for l in clauses[d] if abs(l) not in var_t[u]}
                            for c in off_a:
                                t_set |= set(c1_family(sub_map[c])[choices[c]])
                            for c in (nd.bag_c - pt - aset):
                                if not alpha_satisfies(alpha, clauses[c]):
                                    t_set |= {l for l in clauses[c] if abs(l) in var_t[u]}
                            t_fs = frozenset(t_set)
                            if is_taut(t_fs):
                                for l in t_fs:
                                    if -l in t_fs:
                                        return dag.add_axiom(abs(l), t_fs)

                            if h == len(b0_split):
                                a1 = frozenset(a1_off | a1_b | b1_pure)
                                a2 = frozenset(a2_off | a2_b | b2_pure)
                                if inconsistent[(c1, ka, a1)]:
                                    # Eliminate E_1 = D_1 U (A_2^{off} intersect U_alpha)
                                    elim_list = sorted(
                                        c for c in ((p_c2 - aset) | a2_off)
                                        if not alpha_satisfies(alpha, clauses[c])
                                        and len({l for l in ordered_subclause(clauses[c], var_t[c1], var_order) if abs(l) not in nd.bag_v}) > 0
                                    )
                                    base_ch1: dict[int, int] = {}
                                    for c in a1_off:
                                        sc1 = ordered_subclause(clauses[c], var_t[c1], var_order)
                                        base_ch1[c] = sc1.index(sub_map[c][choices[c]])
                                    for d in (a1_b & b2):
                                        base_ch1[d] = cb2[d]

                                    def elim_c1(idx: int, extra: frozenset[int], ech: dict[int, int]) -> int:
                                        if idx == len(elim_list):
                                            ch1 = dict(base_ch1)
                                            ch1.update(ech)
                                            return get_derived(c1, alpha, a1 | extra, ch1)
                                        ce = elim_list[idx]
                                        sc1 = ordered_subclause(clauses[ce], var_t[c1], var_order)
                                        h_ord = tuple(l for l in sc1 if abs(l) not in nd.bag_v)
                                        g_set: set[int] = set(c_alpha_lits(alpha))
                                        for c in (a1 | extra):
                                            if c in p_c1:
                                                if not alpha_satisfies(alpha, clauses[c]):
                                                    g_set |= {l for l in clauses[c] if abs(l) not in var_t[c1]}
                                            else:
                                                sc_c = ordered_subclause(clauses[c], var_t[c1], var_order)
                                                ci = ech[c] if c in extra else base_ch1[c]
                                                g_set |= set(c1_family(sc_c)[ci])
                                        for c in (nd.bag_c - p_c1 - (a1 | extra) - frozenset(elim_list[idx:])):
                                            if not alpha_satisfies(alpha, clauses[c]):
                                                g_set |= {l for l in clauses[c] if abs(l) in var_t[c1]}
                                        g_fs = frozenset(g_set)
                                        if is_taut(g_fs):
                                            for l in g_fs:
                                                if -l in g_fs:
                                                    return dag.add_axiom(abs(l), g_fs)
                                        l0_id = elim_c1(idx + 1, extra, ech)
                                        r_ids = []
                                        for hl in h_ord:
                                            nc = dict(ech)
                                            nc[ce] = sc1.index(hl)
                                            r_ids.append(elim_c1(idx + 1, extra | {ce}, nc))
                                        return lemma2_elim(dag, g_fs, frozenset(), h_ord, l0_id, r_ids)

                                    m1_p = elim_c1(0, frozenset(), {})
                                    return dag.add_weaken(m1_p, t_fs)
                                else:
                                    assert inconsistent[(c2, ka, a2)]
                                    elim_list = sorted(
                                        c for c in (p_c1 - aset)
                                        if not alpha_satisfies(alpha, clauses[c])
                                        and len({l for l in ordered_subclause(clauses[c], var_t[c2], var_order) if abs(l) not in nd.bag_v}) > 0
                                    )
                                    base_ch2: dict[int, int] = {}
                                    for c in a2_off:
                                        sc2 = ordered_subclause(clauses[c], var_t[c2], var_order)
                                        base_ch2[c] = sc2.index(sub_map[c][choices[c]])
                                    for d in (a2_b & b1):
                                        base_ch2[d] = cb1[d]

                                    def elim_c2(idx: int, extra: frozenset[int], ech: dict[int, int]) -> int:
                                        if idx == len(elim_list):
                                            ch2 = dict(base_ch2)
                                            ch2.update(ech)
                                            return get_derived(c2, alpha, a2 | extra, ch2)
                                        ce = elim_list[idx]
                                        sc2 = ordered_subclause(clauses[ce], var_t[c2], var_order)
                                        h_ord = tuple(l for l in sc2 if abs(l) not in nd.bag_v)
                                        g_set: set[int] = set(c_alpha_lits(alpha))
                                        for c in (a2 | extra):
                                            if c in p_c2:
                                                if not alpha_satisfies(alpha, clauses[c]):
                                                    g_set |= {l for l in clauses[c] if abs(l) not in var_t[c2]}
                                            else:
                                                sc_c = ordered_subclause(clauses[c], var_t[c2], var_order)
                                                ci = ech[c] if c in extra else base_ch2[c]
                                                g_set |= set(c1_family(sc_c)[ci])
                                        for c in (nd.bag_c - p_c2 - (a2 | extra) - frozenset(elim_list[idx:])):
                                            if not alpha_satisfies(alpha, clauses[c]):
                                                g_set |= {l for l in clauses[c] if abs(l) in var_t[c2]}
                                        g_fs = frozenset(g_set)
                                        if is_taut(g_fs):
                                            for l in g_fs:
                                                if -l in g_fs:
                                                    return dag.add_axiom(abs(l), g_fs)
                                        l0_id = elim_c2(idx + 1, extra, ech)
                                        r_ids = []
                                        for hl in h_ord:
                                            nc = dict(ech)
                                            nc[ce] = sc2.index(hl)
                                            r_ids.append(elim_c2(idx + 1, extra | {ce}, nc))
                                        return lemma2_elim(dag, g_fs, frozenset(), h_ord, l0_id, r_ids)

                                    m2_p = elim_c2(0, frozenset(), {})
                                    return dag.add_weaken(m2_p, t_fs)

                            d = b0_split[h]
                            if d in b2:
                                sc1 = ordered_subclause(clauses[d], var_t[c1], var_order)
                                h_ord = tuple(l for l in sc1 if abs(l) not in nd.bag_v)
                                l0_id = build_join(h + 1, a1_b, a2_b | {d}, cb2, cb1)
                                r_ids = []
                                for hl in h_ord:
                                    ncb2 = dict(cb2)
                                    ncb2[d] = sc1.index(hl)
                                    r_ids.append(build_join(h + 1, a1_b | {d}, a2_b, ncb2, cb1))
                                d_ext = frozenset(l for l in clauses[d] if abs(l) not in var_t[u])
                                g_base = t_fs - d_ext
                                return lemma2_elim(dag, g_base, d_ext, h_ord, l0_id, r_ids)
                            else:
                                assert d in b1
                                sc2 = ordered_subclause(clauses[d], var_t[c2], var_order)
                                h_ord = tuple(l for l in sc2 if abs(l) not in nd.bag_v)
                                l0_id = build_join(h + 1, a1_b | {d}, a2_b, cb2, cb1)
                                r_ids = []
                                for hl in h_ord:
                                    ncb1 = dict(cb1)
                                    ncb1[d] = sc2.index(hl)
                                    r_ids.append(build_join(h + 1, a1_b, a2_b | {d}, cb2, ncb1))
                                d_ext = frozenset(l for l in clauses[d] if abs(l) not in var_t[u])
                                g_base = t_fs - d_ext
                                return lemma2_elim(dag, g_base, d_ext, h_ord, l0_id, r_ids)

                        derived[full_key] = build_join(0, frozenset(), frozenset(), {}, {})

    bot_id = get_derived(root_id, {}, frozenset(), {})
    return dag.verify_regular_refutation(bot_id)


def test_concrete_counterexample_to_proof_l165() -> bool:
    """Construct an instance where PROOF.md L165 (D_1 without A_2^{off}) fails:
    At join t_0, c in A_2^{off} intersect U_alpha has y_1 in Var_{t_1} - chi_v(t_0),
    C_c = -y_2, and (t_1, alpha, A_1) is inconsistent; M_1(A_1) contains y_1 not in T."""
    # Clauses: c0=(1 or 2), c1=(-1), c2=(-2)
    # Var 1 in T_{t1}, Var 2 in T_{t2}; c0=(1 or 2) in chi_c(t0) with P_{c0} = empty (off-path!)
    clauses = [frozenset({1, 2}), frozenset({-1}), frozenset({-2})]
    # Nice TD rooted at 10 (empty)
    nodes = {
        1: TreeNode(1, "leaf", set(), set(), None, []),
        2: TreeNode(2, "intro_c", set(), {0}, 0, [1]),
        3: TreeNode(3, "intro_v", {1}, {0}, 1, [2]),
        4: TreeNode(4, "intro_c", {1}, {0, 1}, 1, [3]),
        5: TreeNode(5, "forget_c", {1}, {0}, 1, [4]),
        6: TreeNode(6, "forget_v", set(), {0}, 1, [5]),  # t1: bag={c0}, Var_t1={1}
        11: TreeNode(11, "leaf", set(), set(), None, []),
        12: TreeNode(12, "intro_c", set(), {0}, 0, [11]),
        13: TreeNode(13, "intro_v", {2}, {0}, 2, [12]),
        14: TreeNode(14, "intro_c", {2}, {0, 2}, 2, [13]),
        15: TreeNode(15, "forget_c", {2}, {0}, 2, [14]),
        16: TreeNode(16, "forget_v", set(), {0}, 2, [15]),  # t2: bag={c0}, Var_t2={2}
        20: TreeNode(20, "join", set(), {0}, None, [6, 16]),  # t0: bag={c0}, off-path!
        21: TreeNode(21, "forget_c", set(), set(), 0, [20]),  # root
    }
    p_paths = {0: set(), 1: {4}, 2: {14}}  # c0 is completely off-path!

    # Check under PROOF.md L165: for A={0}, C_0 = (-2), A_1^{off}={}, A_2^{off}={0}
    # A_1 = {} is inconsistent at t1 (since c1=(-1) is in Cls_{t1} - chi_c(t1))
    # D_1 = ((P_{t2} intersect chi_c(t0)) - A) intersect U_alpha = empty set!
    # So M_1' = M(t1, {}, {}) = c0_{t1}^{int} = {+1}, while T = C_0 = {-2}!
    # {+1} is NOT a subset of {-2}!
    m1_proof_l165 = frozenset({1})
    target_t = frozenset({-2})
    witness_fails_l165 = not m1_proof_l165.issubset(target_t)

    # Now verify our corrected construction succeeds with a valid regular refutation on this exact TD!
    ok, length = build_proof_on_td(clauses, nodes, 21, p_paths)
    assert ok, "Corrected construction failed on the counterexample TD"
    print(f"JOIN_COUNTEREXAMPLE: L165_fails={witness_fails_l165}, corrected_regular_ok={ok}, len={length}")
    return witness_fails_l165


def test_pigeonhole_and_neg_lit_cases() -> None:
    # Unsat 3-variable / 2-pigeon / tricky neg-lit and P_t join decomposition
    # Clauses: c0=(1 or 2 or 3), c1=(-1 or -2), c2=(-1 or 2), c3=(1 or -2), c4=(-3)
    # Wait: (1 or -2), (-1 or 2), (-1 or -2), (1 or 2 or 3), (-3) -> forces 1=2=0, 3=1, contradicts -3!
    clauses = [
        frozenset({1, 2, 3}),
        frozenset({-1, -2}),
        frozenset({-1, 2}),
        frozenset({1, -2}),
        frozenset({-3}),
    ]
    # Build TD where c0=(1,2,3) has P_{c0} going into c1 (containing vars 1,2) and NOT c2 (containing var 3),
    # and ALSO test c0 completely off-path!
    nodes = {
        1: TreeNode(1, "leaf", set(), set(), None, []),
        2: TreeNode(2, "intro_c", set(), {0}, 0, [1]),
        3: TreeNode(3, "intro_v", {1}, {0}, 1, [2]),
        4: TreeNode(4, "intro_v", {1, 2}, {0}, 2, [3]),
        5: TreeNode(5, "intro_c", {1, 2}, {0, 1}, 1, [4]),
        6: TreeNode(6, "forget_c", {1, 2}, {0}, 1, [5]),
        7: TreeNode(7, "intro_c", {1, 2}, {0, 2}, 2, [6]),
        8: TreeNode(8, "forget_c", {1, 2}, {0}, 2, [7]),
        9: TreeNode(9, "intro_c", {1, 2}, {0, 3}, 3, [8]),
        10: TreeNode(10, "forget_c", {1, 2}, {0}, 3, [9]),
        11: TreeNode(11, "forget_v", {2}, {0}, 1, [10]),
        12: TreeNode(12, "forget_v", set(), {0}, 2, [11]),  # t1: bag={c0}, Var={1,2}
        21: TreeNode(21, "leaf", set(), set(), None, []),
        22: TreeNode(22, "intro_c", set(), {0}, 0, [21]),
        23: TreeNode(23, "intro_v", {3}, {0}, 3, [22]),
        24: TreeNode(24, "intro_c", {3}, {0, 4}, 4, [23]),
        25: TreeNode(25, "forget_c", {3}, {0}, 4, [24]),
        26: TreeNode(26, "forget_v", set(), {0}, 3, [25]),  # t2: bag={c0}, Var={3}
        30: TreeNode(30, "join", set(), {0}, None, [12, 26]),
        31: TreeNode(31, "forget_c", set(), set(), 0, [30]),
    }
    for mode, p0 in [("on_t1", {31, 30, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2}), ("on_t2", {31, 30, 26, 25, 24, 23, 22}), ("off", set())]:
        p_paths = {0: p0, 1: {5}, 2: {7}, 3: {9}, 4: {24}}
        ok, length = build_proof_on_td(clauses, nodes, 31, p_paths)
        assert ok, f"Failed regularity on mode {mode}"
    print("COMPLEX_TD_MODES: on_t1=PASS, on_t2=PASS, off=PASS")


def test_audit2_adversarial_tds() -> None:
    """Test the 4 crash counterexamples and multi-clause join cases from AUDIT.md."""
    # (1) Case 3 intro_v: off-path c0=(x1 or x2) not in A, satisfied by alpha(x2)=1 but not alpha'
    c_1 = [frozenset({1, 2}), frozenset({-1}), frozenset({1})]
    td_1 = {
        1: TreeNode(1, "leaf", set(), set(), None, []),
        2: TreeNode(2, "intro_c", set(), {0}, 0, [1]),
        3: TreeNode(3, "intro_v", {1}, {0}, 1, [2]),
        4: TreeNode(4, "intro_c", {1}, {0, 1}, 1, [3]),
        5: TreeNode(5, "forget_c", {1}, {0}, 1, [4]),
        6: TreeNode(6, "intro_c", {1}, {0, 2}, 2, [5]),
        7: TreeNode(7, "forget_c", {1}, {0}, 2, [6]),
        8: TreeNode(8, "forget_v", set(), {0}, 1, [7]),       # t': bag={c0}, Var={1}
        9: TreeNode(9, "intro_v", {2}, {0}, 2, [8]),          # t: intro_v(2)
        10: TreeNode(10, "forget_c", {2}, set(), 0, [9]),
        11: TreeNode(11, "forget_v", set(), set(), 2, [10]),
    }
    ok1, _ = build_proof_on_td(c_1, td_1, 11, {0: set(), 1: {4}, 2: {6}})
    assert ok1, "Adversarial TD 1 (S_sat in intro_v) failed"

    # (2) Case 3 intro_v: W_p clause satisfied by alpha' (x1 in chi_v(t')) with forg(x3) < forg(x1) < forg(x2)
    c_2 = [frozenset({1, 2}), frozenset({3, 2}), frozenset({-3}), frozenset({3}), frozenset({-1})]
    td_2 = {
        1: TreeNode(1, "leaf", set(), set(), None, []),
        2: TreeNode(2, "intro_v", {1}, set(), 1, [1]),
        3: TreeNode(3, "intro_c", {1}, {0}, 0, [2]),
        4: TreeNode(4, "intro_c", {1}, {0, 1}, 1, [3]),
        5: TreeNode(5, "intro_v", {1, 3}, {0, 1}, 3, [4]),
        6: TreeNode(6, "intro_c", {1, 3}, {0, 1, 2}, 2, [5]),
        7: TreeNode(7, "forget_c", {1, 3}, {0, 1}, 2, [6]),
        8: TreeNode(8, "intro_c", {1, 3}, {0, 1, 3}, 3, [7]),
        9: TreeNode(9, "forget_c", {1, 3}, {0, 1}, 3, [8]),
        10: TreeNode(10, "forget_v", {1}, {0, 1}, 3, [9]),   # t': forg(3) first
        11: TreeNode(11, "intro_v", {1, 2}, {0, 1}, 2, [10]), # t: intro_v(2)
        12: TreeNode(12, "forget_c", {1, 2}, {0}, 1, [11]),
        13: TreeNode(13, "forget_v", {1}, {0}, 2, [12]),     # forg(2) after forg(3)
        14: TreeNode(14, "intro_c", {1}, {0, 4}, 4, [13]),
        15: TreeNode(15, "forget_c", {1}, {0}, 4, [14]),
        16: TreeNode(16, "forget_c", {1}, set(), 0, [15]),
        17: TreeNode(17, "forget_v", set(), set(), 1, [16]),
    }
    ok2, _ = build_proof_on_td(c_2, td_2, 17, {0: set(), 1: set(), 2: {6}, 3: {8}, 4: {14}})
    assert ok2, "Adversarial TD 2 (alpha'-satisfied W_p clause) failed"

    # (3) Case 5 forget_c with G != bot and J == empty: c0=(x1), c1=(-x2), c2=(x2)
    c_3 = [frozenset({1}), frozenset({-2}), frozenset({2})]
    td_3 = {
        1: TreeNode(1, "leaf", set(), set(), None, []),
        2: TreeNode(2, "intro_v", {2}, set(), 2, [1]),
        3: TreeNode(3, "intro_v", {1, 2}, set(), 1, [2]),
        4: TreeNode(4, "intro_c", {1, 2}, {0}, 0, [3]),
        5: TreeNode(5, "forget_v", {2}, {0}, 1, [4]),
        6: TreeNode(6, "forget_c", {2}, set(), 0, [5]),      # forget_c(c0) with bag_v={2}, G={2}, J=empty
        7: TreeNode(7, "intro_c", {2}, {1}, 1, [6]),
        8: TreeNode(8, "forget_c", {2}, set(), 1, [7]),
        9: TreeNode(9, "intro_c", {2}, {2}, 2, [8]),
        10: TreeNode(10, "forget_c", {2}, set(), 2, [9]),
        11: TreeNode(11, "forget_v", set(), set(), 2, [10]),
    }
    ok3, _ = build_proof_on_td(c_3, td_3, 11, {0: set(), 1: {7}, 2: {9}})
    assert ok3, "Adversarial TD 3 (forget_c with G != bot, J=empty) failed"

    # (4) Multi-clause join with P_{t_i}\A != empty, |elim_list| >= 2, lead in chi_v(t_0), shared ext lit in d_{t_0}^{ext}
    # Clauses: c0=(1 or 2 or 4), c1=(3 or 4), c2=(5 or 4), c3=(-1), c4=(-2 or 4), c5=(-3), c6=(-5), c7=(-4)
    c_4 = [
        frozenset({1, 2, 4}),
        frozenset({3, 4}),
        frozenset({5, 4}),
        frozenset({-1}),
        frozenset({-2}),
        frozenset({-3}),
        frozenset({-5}),
        frozenset({-4}),
    ]
    td_4 = {
        1: TreeNode(1, "leaf", set(), set(), None, []),
        2: TreeNode(2, "intro_v", {4}, set(), 4, [1]),
        3: TreeNode(3, "intro_c", {4}, {0}, 0, [2]),
        4: TreeNode(4, "intro_c", {4}, {0, 1}, 1, [3]),
        5: TreeNode(5, "intro_c", {4}, {0, 1, 2}, 2, [4]),
        6: TreeNode(6, "intro_v", {1, 4}, {0, 1, 2}, 1, [5]),
        7: TreeNode(7, "intro_c", {1, 4}, {0, 1, 2, 3}, 3, [6]),
        8: TreeNode(8, "forget_c", {1, 4}, {0, 1, 2}, 3, [7]),
        9: TreeNode(9, "intro_v", {1, 3, 4}, {0, 1, 2}, 3, [8]),
        10: TreeNode(10, "intro_c", {1, 3, 4}, {0, 1, 2, 5}, 5, [9]),
        11: TreeNode(11, "forget_c", {1, 3, 4}, {0, 1, 2}, 5, [10]),
        12: TreeNode(12, "forget_v", {1, 4}, {0, 1, 2}, 3, [11]),
        13: TreeNode(13, "forget_v", {4}, {0, 1, 2}, 1, [12]),   # t1: bag={4; c0,c1,c2}, Var={1,3,4}
        21: TreeNode(21, "leaf", set(), set(), None, []),
        22: TreeNode(22, "intro_v", {4}, set(), 4, [21]),
        23: TreeNode(23, "intro_c", {4}, {0}, 0, [22]),
        24: TreeNode(24, "intro_c", {4}, {0, 1}, 1, [23]),
        25: TreeNode(25, "intro_c", {4}, {0, 1, 2}, 2, [24]),
        26: TreeNode(26, "intro_v", {2, 4}, {0, 1, 2}, 2, [25]),
        27: TreeNode(27, "intro_c", {2, 4}, {0, 1, 2, 4}, 4, [26]),
        28: TreeNode(28, "forget_c", {2, 4}, {0, 1, 2}, 4, [27]),
        29: TreeNode(29, "intro_v", {2, 5, 4}, {0, 1, 2}, 5, [28]),
        30: TreeNode(30, "intro_c", {2, 5, 4}, {0, 1, 2, 6}, 6, [29]),
        31: TreeNode(31, "forget_c", {2, 5, 4}, {0, 1, 2}, 6, [30]),
        32: TreeNode(32, "forget_v", {2, 4}, {0, 1, 2}, 5, [31]),
        33: TreeNode(33, "forget_v", {4}, {0, 1, 2}, 2, [32]),   # t2: bag={4; c0,c1,c2}, Var={2,5,4}
        40: TreeNode(40, "join", {4}, {0, 1, 2}, None, [13, 33]),
        # Also test a parent join where var 4 is forgotten BEFORE parent join, or kept above:
        41: TreeNode(41, "forget_c", {4}, {1, 2}, 0, [40]),
        42: TreeNode(42, "forget_c", {4}, {2}, 1, [41]),
        43: TreeNode(43, "forget_c", {4}, set(), 2, [42]),
        44: TreeNode(44, "intro_c", {4}, {7}, 7, [43]),
        45: TreeNode(45, "forget_c", {4}, set(), 7, [44]),
        46: TreeNode(46, "forget_v", set(), set(), 4, [45]),
    }
    p4 = {
        0: {40, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23},  # c0 root-to-leaf in T(c0) via t2
        1: {41, 40, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4},  # c1 root-to-leaf in T(c1) via t1
        2: {42, 41, 40, 33, 32, 31, 30, 29, 28, 27, 26, 25},  # c2 root-to-leaf in T(c2) via t2
        3: {7}, 4: {27}, 5: {10}, 6: {30}, 7: {44},
    }
    ok4, _ = build_proof_on_td(c_4, td_4, 46, p4)
    assert ok4, "Adversarial TD 4 (multi-clause join) failed"

    # (5) Case 3 intro_v with |W| = 2 (both c0=(1,2) and c1=(3,2) in W_p union S_sat)
    c_5 = [frozenset({1, 2}), frozenset({3, 2}), frozenset({-1}), frozenset({1}), frozenset({-3}), frozenset({3})]
    td_5 = {
        1: TreeNode(1, "leaf", set(), set(), None, []),
        2: TreeNode(2, "intro_c", set(), {0}, 0, [1]),
        3: TreeNode(3, "intro_c", set(), {0, 1}, 1, [2]),
        4: TreeNode(4, "intro_v", {1}, {0, 1}, 1, [3]),
        5: TreeNode(5, "intro_c", {1}, {0, 1, 2}, 2, [4]),
        6: TreeNode(6, "forget_c", {1}, {0, 1}, 2, [5]),
        7: TreeNode(7, "intro_c", {1}, {0, 1, 3}, 3, [6]),
        8: TreeNode(8, "forget_c", {1}, {0, 1}, 3, [7]),
        9: TreeNode(9, "forget_v", set(), {0, 1}, 1, [8]),
        10: TreeNode(10, "intro_v", {3}, {0, 1}, 3, [9]),
        11: TreeNode(11, "intro_c", {3}, {0, 1, 4}, 4, [10]),
        12: TreeNode(12, "forget_c", {3}, {0, 1}, 4, [11]),
        13: TreeNode(13, "intro_c", {3}, {0, 1, 5}, 5, [12]),
        14: TreeNode(14, "forget_c", {3}, {0, 1}, 5, [13]),
        15: TreeNode(15, "forget_v", set(), {0, 1}, 3, [14]),  # t': Var={1,3}, chi_c={c0,c1}
        16: TreeNode(16, "intro_v", {2}, {0, 1}, 2, [15]),    # t: intro_v(2) -> |W| = 2!
        17: TreeNode(17, "forget_c", {2}, {1}, 0, [16]),
        18: TreeNode(18, "forget_c", {2}, set(), 1, [17]),
        19: TreeNode(19, "forget_v", set(), set(), 2, [18]),
    }
    ok5, _ = build_proof_on_td(c_5, td_5, 19, {0: set(), 1: set(), 2: {5}, 3: {7}, 4: {11}, 5: {13}})
    assert ok5, "Adversarial TD 5 (|W| = 2 in intro_v) failed"

    # (6) 27/27 clause-path modes on 3-clause join with |elim_list| >= 2 and shared external literal 4 in d_{t0}^{ext}
    td_6 = {
        1: TreeNode(1, "leaf", set(), set(), None, []),
        2: TreeNode(2, "intro_c", set(), {0}, 0, [1]),
        3: TreeNode(3, "intro_c", set(), {0, 1}, 1, [2]),
        4: TreeNode(4, "intro_c", set(), {0, 1, 2}, 2, [3]),
        5: TreeNode(5, "intro_v", {1}, {0, 1, 2}, 1, [4]),
        6: TreeNode(6, "intro_c", {1}, {0, 1, 2, 3}, 3, [5]),
        7: TreeNode(7, "forget_c", {1}, {0, 1, 2}, 3, [6]),
        8: TreeNode(8, "intro_v", {1, 3}, {0, 1, 2}, 3, [7]),
        9: TreeNode(9, "intro_c", {1, 3}, {0, 1, 2, 5}, 5, [8]),
        10: TreeNode(10, "forget_c", {1, 3}, {0, 1, 2}, 5, [9]),
        11: TreeNode(11, "forget_v", {1}, {0, 1, 2}, 3, [10]),
        12: TreeNode(12, "forget_v", set(), {0, 1, 2}, 1, [11]),  # t1: Var={1,3}
        21: TreeNode(21, "leaf", set(), set(), None, []),
        22: TreeNode(22, "intro_c", set(), {0}, 0, [21]),
        23: TreeNode(23, "intro_c", set(), {0, 1}, 1, [22]),
        24: TreeNode(24, "intro_c", set(), {0, 1, 2}, 2, [23]),
        25: TreeNode(25, "intro_v", {2}, {0, 1, 2}, 2, [24]),
        26: TreeNode(26, "intro_c", {2}, {0, 1, 2, 4}, 4, [25]),
        27: TreeNode(27, "forget_c", {2}, {0, 1, 2}, 4, [26]),
        28: TreeNode(28, "intro_v", {2, 5}, {0, 1, 2}, 5, [27]),
        29: TreeNode(29, "intro_c", {2, 5}, {0, 1, 2, 6}, 6, [28]),
        30: TreeNode(30, "forget_c", {2, 5}, {0, 1, 2}, 6, [29]),
        31: TreeNode(31, "forget_v", {2}, {0, 1, 2}, 5, [30]),
        32: TreeNode(32, "forget_v", set(), {0, 1, 2}, 2, [31]),  # t2: Var={2,5}
        40: TreeNode(40, "join", set(), {0, 1, 2}, None, [12, 32]),  # var 4 is strictly external!
        41: TreeNode(41, "intro_v", {4}, {0, 1, 2}, 4, [40]),
        42: TreeNode(42, "forget_c", {4}, {1, 2}, 0, [41]),
        43: TreeNode(43, "forget_c", {4}, {2}, 1, [42]),
        44: TreeNode(44, "forget_c", {4}, set(), 2, [43]),
        45: TreeNode(45, "intro_c", {4}, {7}, 7, [44]),
        46: TreeNode(46, "forget_c", {4}, set(), 7, [45]),
        47: TreeNode(47, "forget_v", set(), set(), 4, [46]),
    }
    p_choices = {
        0: {
            "t1": {41, 40, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2},
            "t2": {41, 40, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22},
            "off": set(),
        },
        1: {
            "t1": {42, 41, 40, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3},
            "t2": {42, 41, 40, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23},
            "off": set(),
        },
        2: {
            "t1": {43, 42, 41, 40, 12, 11, 10, 9, 8, 7, 6, 5, 4},
            "t2": {43, 42, 41, 40, 32, 31, 30, 29, 28, 27, 26, 25, 24},
            "off": set(),
        },
    }
    modes = ("t1", "t2", "off")
    cnt27 = 0
    for m0 in modes:
        for m1 in modes:
            for m2 in modes:
                p_cur = {0: p_choices[0][m0], 1: p_choices[1][m1], 2: p_choices[2][m2], 3: {6}, 4: {26}, 5: {9}, 6: {29}, 7: {45}}
                ok_m, _ = build_proof_on_td(c_4, td_6, 47, p_cur)
                assert ok_m, f"Failed 27-mode join test at ({m0}, {m1}, {m2})"
                cnt27 += 1
    assert cnt27 == 27
    print("AUDIT2_ADVERSARIAL_TDS: 5/5 + 27/27 join modes PASS")


def check_proof_md_issues() -> list[str]:
    failures: list[str] = []
    root = pathlib.Path(__file__).resolve().parents[3]
    target_md = (root / "targets" / "cai-2610.02047-plog-reg" / "TARGET.md").read_text(encoding="utf-8")
    proof_md = (root / "targets" / "cai-2610.02047-plog-reg" / "PROOF.md").read_text(encoding="utf-8")

    # 1. Verify TARGET.md verbatim against arXiv:2610.02047v1 Section 8
    tar_path = root / "tools" / ".arxiv_cache" / "eprint" / "2610.02047.src"
    if "Another question is whether every unsatisfiable CNF formula" not in target_md:
        failures.append("TARGET.md missing Section 8 open question verbatim text")
    if not tar_path.exists():
        print("[SKIP] local tools/.arxiv_cache not present; skipping TeX snippet check")
    else:
        with tarfile.open(tar_path, "r:*") as tf:
            main_tex = tf.extractfile("main.tex").read().decode("utf-8")
        if "Another question is whether every unsatisfiable CNF formula" not in main_tex:
            failures.append("Primary source main.tex missing expected Section 8 text")

    # 2. Check PROOF.md fixes for AUDIT.md Items 1-4 & Re-Audit 1 items
    if "S_{\\mathrm{sat}}" not in proof_md:
        failures.append("PROOF.md Case 3 missing S_sat unified elimination fix")
    if "Section 2 of `arXiv:2610.02047v1`" in proof_md:
        failures.append("PROOF.md L7 still cites Section 2 instead of Section 3 (Preliminaries)")
    if "if needed? No" in proof_md:
        failures.append("PROOF.md L136 contains scratch draft parenthetical ('if needed? No')")
    if "when tautological, which occurs iff $\\ell_j \\in G$ and $\\neg\\ell_u \\notin G$" in proof_md:
        failures.append("PROOF.md L153 contains false iff condition in Case 5")
    if "2^{w+2} + 1" not in proof_md and "2^{w+2}+1" not in proof_md:
        failures.append("PROOF.md L138/L193 missing geometric-series bound 2^{w+2} + 1")

    return failures


def main() -> int:
    assert test_concrete_counterexample_to_proof_l165()
    test_pigeonhole_and_neg_lit_cases()
    test_audit2_adversarial_tds()
    failures = check_proof_md_issues()
    if failures:
        for msg in failures:
            print(f"ERROR: {msg}")
        print("FAIL")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
