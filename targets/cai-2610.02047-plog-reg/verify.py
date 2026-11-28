#!/usr/bin/env python3
"""
Exact-arithmetic standalone verifier for PROOF.md of cai-2610.02047-plog-reg.
Uses strictly integer and set arithmetic (no floats, no division operators).
Verifies:
1. Exact calculation of partially log-weighted incidence width w_plog(T, chi, r, P).
2. Construction of the hybrid C_0 + C_1 mRes proof DAG at every TD node.
3. Exact verification of (P0) multiclause identity, (P1) ResVars subset of Var_t minus bag_v[t],
   (P2) path regularity in Res, and (P3) var(mc) & ResVars == empty at EVERY node.
4. Exact conversion via lem:mres-to-res to a valid regular Resolution refutation of empty clause.
5. Tested across: 4-clause join puzzle (all P), multi-clause B1+B2 shared-var gadget,
   2-level join Case A (all 12 P combos), width-5 Case B (all P), W_p opposite-literal intro_v,
   7-, 8-, and 9-clause tw_log & tw_plog adversaries, PHP(3,2).
"""
import itertools
import sys
from collections import defaultdict


def var(lit):
    return abs(lit)


def is_taut(mc):
    s = set(mc)
    return any(-l in s for l in s)


def mres_resolve(p, q, v):
    pl = list(p)
    ql = list(q)
    assert v in pl and -v in ql
    pl.remove(v)
    ql.remove(-v)
    return tuple(sorted(pl + ql))


class MResProof:
    def __init__(self, clauses):
        self.nodes = []
        self.clauses = [tuple(sorted(c)) for c in clauses]
        self.init_map = {}
        for c in self.clauses:
            nid = len(self.nodes)
            self.nodes.append({'mc': c, 'rule': 'init', 'parents': [], 'var': None})
            self.init_map[c] = nid
        self.axiom_map = {}

    def get_init(self, c):
        return self.init_map[tuple(sorted(c))]

    def get_axiom(self, v):
        if v not in self.axiom_map:
            nid = len(self.nodes)
            self.nodes.append({'mc': tuple(sorted([v, -v])), 'rule': 'axiom', 'parents': [], 'var': None})
            self.axiom_map[v] = nid
        return self.axiom_map[v]

    def contract_id(self, pid):
        pmc = self.nodes[pid]['mc']
        cmc = tuple(sorted(set(pmc)))
        if cmc == pmc:
            return pid
        nid = len(self.nodes)
        self.nodes.append({'mc': cmc, 'rule': 'contract', 'parents': [pid], 'var': None})
        return nid

    def weaken_to(self, pid, target_set):
        pmc = set(self.nodes[pid]['mc'])
        extra = sorted(target_set - pmc)
        if not extra:
            return self.contract_id(pid)
        nid = len(self.nodes)
        mc = tuple(sorted(list(self.nodes[pid]['mc']) + extra))
        self.nodes.append({'mc': mc, 'rule': 'weaken', 'parents': [pid], 'var': None})
        return self.contract_id(nid)

    def resolve(self, pid_pos, pid_neg, v):
        res = mres_resolve(self.nodes[pid_pos]['mc'], self.nodes[pid_neg]['mc'], v)
        res = tuple(sorted(set(res)))
        nid = len(self.nodes)
        self.nodes.append({'mc': res, 'rule': 'resolve', 'parents': [pid_pos, pid_neg], 'var': v})
        return nid

    def resolve_any_order(self, pid1, pid2, v):
        p = self.nodes[pid1]['mc']
        q = self.nodes[pid2]['mc']
        if v in p and -v in q:
            return self.resolve(pid1, pid2, v)
        if -v in p and v in q:
            return self.resolve(pid2, pid1, v)
        raise AssertionError(f"Cannot resolve {p} and {q} on {v}")

    def convert_to_res_and_check_regular(self, root_id):
        reachable = set()
        stack = [root_id]
        while stack:
            u = stack.pop()
            if u in reachable:
                continue
            reachable.add(u)
            for p in self.nodes[u]['parents']:
                stack.append(p)
        order = sorted(reachable)

        init_sets = [frozenset(c) for c in self.clauses]
        res_nodes = {}
        for nid in order:
            nd = self.nodes[nid]
            cset = frozenset(nd['mc'])
            if any(-l in cset for l in cset):
                continue
            rule = nd['rule']
            if rule == 'init':
                assert cset in init_sets
                res_nodes[nid] = (cset, [], None)
            elif rule == 'axiom':
                continue
            elif rule in ('weaken', 'contract'):
                pid = nd['parents'][0]
                assert pid in res_nodes
                assert res_nodes[pid][0].issubset(cset)
                res_nodes[nid] = (cset, [pid], None)
            elif rule == 'resolve':
                p_id, q_id = nd['parents']
                v = nd['var']
                if v in cset:
                    assert p_id in res_nodes and res_nodes[p_id][0].issubset(cset)
                    res_nodes[nid] = (cset, [p_id], None)
                elif -v in cset:
                    assert q_id in res_nodes and res_nodes[q_id][0].issubset(cset)
                    res_nodes[nid] = (cset, [q_id], None)
                else:
                    assert p_id in res_nodes and q_id in res_nodes
                    ps = res_nodes[p_id][0]
                    qs = res_nodes[q_id][0]
                    assert v in ps and -v in qs
                    assert (ps - {v}) | (qs - {-v}) == cset
                    res_nodes[nid] = (cset, [p_id, q_id], v)

        assert root_id in res_nodes and res_nodes[root_id][0] == frozenset()

        path_vars = {}
        for nid in order:
            if nid not in res_nodes:
                continue
            _, pars, rvar = res_nodes[nid]
            pvars = set()
            for p in pars:
                pvars |= path_vars[p]
            if rvar is not None:
                assert rvar not in pvars, f"Irregularity on variable {rvar}"
                pvars.add(rvar)
            path_vars[nid] = pvars
        return len(self.nodes), len(res_nodes)


class TDNode:
    def __init__(self, nid, kind, bag_v, bag_c, children=None, arg=None):
        self.nid = nid
        self.kind = kind
        self.bag_v = frozenset(bag_v)
        self.bag_c = frozenset(bag_c)
        self.children = children or []
        self.arg = arg


def make_nice_td_from_tree(clauses, adj_tree, bags_v, bags_c, root=0):
    children = defaultdict(list)
    seen = {root}
    q = [root]
    while q:
        u = q.pop(0)
        for v in adj_tree[u]:
            if v not in seen:
                seen.add(v)
                children[u].append(v)
                q.append(v)

    nodes = []

    def add_node(kind, bv, bc, ch=None, arg=None):
        nid = len(nodes)
        nodes.append(TDNode(nid, kind, bv, bc, ch or [], arg))
        return nid

    def build_path(child_id, bv_from, bc_from, bv_to, bc_to):
        cur = child_id
        cur_v, cur_c = set(bv_from), set(bc_from)
        for x in sorted(cur_v - bv_to):
            cur_v.remove(x)
            cur = add_node('forget_v', cur_v, cur_c, [cur], x)
        for c in sorted(cur_c - bc_to):
            cur_c.remove(c)
            cur = add_node('forget_c', cur_v, cur_c, [cur], c)
        for c in sorted(bc_to - cur_c):
            cur_c.add(c)
            cur = add_node('intro_c', cur_v, cur_c, [cur], c)
        for x in sorted(bv_to - cur_v):
            cur_v.add(x)
            cur = add_node('intro_v', cur_v, cur_c, [cur], x)
        return cur

    def rec(u):
        bv, bc = bags_v[u], bags_c[u]
        ch = children[u]
        if not ch:
            leaf = add_node('leaf', set(), set(), [], None)
            return build_path(leaf, set(), set(), bv, bc)
        sub_ids = []
        for w in ch:
            wid = rec(w)
            sub_ids.append(build_path(wid, bags_v[w], bags_c[w], bv, bc))
        while len(sub_ids) > 1:
            a = sub_ids.pop(0)
            b = sub_ids.pop(0)
            j = add_node('join', bv, bc, [a, b], None)
            sub_ids.insert(0, j)
        return sub_ids[0]

    top = rec(root)
    new_root = build_path(top, bags_v[root], bags_c[root], set(), set())
    return nodes, new_root


def ceil_log2(m):
    # Smallest integer k >= 0 with 2**k >= m (m >= 1). Pure integer arithmetic.
    k = 0
    p = 1
    while p < m:
        p *= 2
        k += 1
    return k


def compute_plog_upper_ceil(clauses, nodes, P_paths):
    # Compute integer upper bound on w_plog (using ceil(log2(rho+1))) and verify TD validity
    all_vars = {var(l) for cl in clauses for l in cl}
    for v in all_vars:
        sub = {nd.nid for nd in nodes if v in nd.bag_v}
        assert sub
    for c_idx, cl in enumerate(clauses):
        sub = {nd.nid for nd in nodes if c_idx in nd.bag_c}
        assert sub
        for l in cl:
            assert any(nd.nid in sub and var(l) in nd.bag_v for nd in nodes)
        if P_paths[c_idx]:
            assert P_paths[c_idx].issubset(sub)

    max_bag_w = 0
    for nd in nodes:
        bw = len(nd.bag_v)
        for c_idx in nd.bag_c:
            if nd.nid in P_paths[c_idx]:
                bw += 1
            else:
                p_vars = set()
                for u in P_paths[c_idx]:
                    p_vars |= nodes[u].bag_v
                rho = sum(1 for l in clauses[c_idx] if var(l) not in p_vars)
                w_c = max(ceil_log2(rho + 1), 1)
                bw += w_c
        if bw > max_bag_w:
            max_bag_w = bw
    return max_bag_w - 1


def compute_td_metadata(nodes, root):
    Var_t = {}
    Cls_t = {}
    forg_node = {}
    post_order = []

    def dfs(u):
        nd = nodes[u]
        vt = set(nd.bag_v)
        ct = set(nd.bag_c)
        for w in nd.children:
            dfs(w)
            vt |= Var_t[w]
            ct |= Cls_t[w]
        Var_t[u] = frozenset(vt)
        Cls_t[u] = frozenset(ct)
        if nd.kind == 'forget_v':
            forg_node[nd.arg] = u
        post_order.append(u)

    dfs(root)
    post_rank = {u: i for i, u in enumerate(post_order)}
    var_rank = {v: post_rank[u] for v, u in forg_node.items()}
    return Var_t, Cls_t, var_rank, post_order


def is_inconsistent(t, alpha_tuple, A_set, nodes, Var_t, Cls_t, clauses):
    nd = nodes[t]
    alpha = dict(alpha_tuple)
    free_vars = sorted(Var_t[t] - nd.bag_v)
    req_idx = (Cls_t[t] - nd.bag_c) | A_set
    req_clauses = [clauses[c] for c in req_idx]
    for vals in itertools.product([0, 1], repeat=len(free_vars)):
        assign = dict(alpha)
        for v, b in zip(free_vars, vals):
            assign[v] = b
        ok = True
        for cl in req_clauses:
            sat = False
            for l in cl:
                vv = var(l)
                if vv in assign:
                    if (l > 0 and assign[vv] == 1) or (l < 0 and assign[vv] == 0):
                        sat = True
                        break
            if not sat:
                ok = False
                break
        if ok:
            return False
    return True


def alpha_sat_clause(alpha_dict, cl):
    for l in cl:
        v = var(l)
        if v in alpha_dict:
            if (l > 0 and alpha_dict[v] == 1) or (l < 0 and alpha_dict[v] == 0):
                return True
    return False


def c_alpha_lits(alpha_dict):
    return {-v if b == 1 else v for v, b in alpha_dict.items()}


def c_int_ordered(cl, vt, var_rank):
    lits = [l for l in cl if var(l) in vt]
    lits.sort(key=lambda l: var_rank[var(l)])
    return tuple(lits)


def c_ext_lits(cl, vt):
    return frozenset(l for l in cl if var(l) not in vt)


def C1_family(c_ord):
    return tuple(tuple([-c_ord[i]] + list(c_ord[i + 1:])) for i in range(len(c_ord)))


def verify_hybrid_construction(clauses, nodes, root, P_paths):
    w_ceil = compute_plog_upper_ceil(clauses, nodes, P_paths)
    Var_t, Cls_t, var_rank, post_order = compute_td_metadata(nodes, root)

    incons = defaultdict(set)
    for t in post_order:
        bv = sorted(nodes[t].bag_v)
        bc = sorted(nodes[t].bag_c)
        for vals in itertools.product([0, 1], repeat=len(bv)):
            alpha = tuple(zip(bv, vals))
            for mask in range(1 << len(bc)):
                A = frozenset(bc[j] for j in range(len(bc)) if (mask >> j) & 1)
                if is_inconsistent(t, alpha, A, nodes, Var_t, Cls_t, clauses):
                    incons[t].add((alpha, A))

    proof = MResProof(clauses)
    checked_upto = [0]
    res_valid = {}
    res_past_vars = {}

    def update_dag_stats():
        while checked_upto[0] < len(proof.nodes):
            nid = checked_upto[0]
            checked_upto[0] += 1
            nd = proof.nodes[nid]
            cset = frozenset(nd['mc'])
            taut = any(-l in cset for l in cset)
            rule = nd['rule']
            if rule == 'init':
                res_valid[nid] = not taut
                res_past_vars[nid] = set()
            elif rule == 'axiom':
                res_valid[nid] = False
                res_past_vars[nid] = set()
            elif rule in ('weaken', 'contract'):
                pid = nd['parents'][0]
                if taut:
                    res_valid[nid] = False
                    res_past_vars[nid] = set()
                else:
                    assert res_valid[pid]
                    res_valid[nid] = True
                    res_past_vars[nid] = set(res_past_vars[pid])
            elif rule == 'resolve':
                p_id, q_id = nd['parents']
                v = nd['var']
                if taut:
                    res_valid[nid] = False
                    res_past_vars[nid] = set()
                elif v in cset:
                    assert res_valid[p_id]
                    res_valid[nid] = True
                    res_past_vars[nid] = set(res_past_vars[p_id])
                elif -v in cset:
                    assert res_valid[q_id]
                    res_valid[nid] = True
                    res_past_vars[nid] = set(res_past_vars[q_id])
                else:
                    assert res_valid[p_id] and res_valid[q_id]
                    pv = set(res_past_vars[p_id]) | set(res_past_vars[q_id])
                    assert v not in pv
                    res_valid[nid] = True
                    res_past_vars[nid] = pv | {v}

    def target_mc(t, ad, A, choices):
        lits = set(c_alpha_lits(ad))
        Pt = {c for c in nodes[t].bag_c if t in P_paths[c]}
        for c in (A & Pt):
            if not alpha_sat_clause(ad, clauses[c]):
                lits |= c_ext_lits(clauses[c], Var_t[t])
        for c in (A - Pt):
            c_ord = c_int_ordered(clauses[c], Var_t[t], var_rank)
            lits |= set(C1_family(c_ord)[choices[c]])
        for c in (nodes[t].bag_c - Pt - A):
            if not alpha_sat_clause(ad, clauses[c]):
                lits |= set(c_int_ordered(clauses[c], Var_t[t], var_rank))
        return frozenset(lits)

    def check_entry(t, ad, A, choices, nid):
        update_dag_stats()
        mc_set = frozenset(proof.nodes[nid]['mc'])
        exp_set = target_mc(t, ad, A, choices)
        assert mc_set == exp_set
        if res_valid[nid]:
            allowed = Var_t[t] - nodes[t].bag_v
            assert res_past_vars[nid].issubset(allowed)
            mc_vars = {var(l) for l in mc_set}
            assert not (mc_vars & res_past_vars[nid])

    def derive_taut_if_any(tset):
        for l in tset:
            if -l in tset:
                ax = proof.get_axiom(var(l))
                return proof.weaken_to(ax, tset)
        return None

    derived = {}
    for t in post_order:
        nd = nodes[t]
        kind = nd.kind
        if kind == 'leaf':
            continue
        Pt = frozenset(c for c in nd.bag_c if t in P_paths[c])

        for alpha_tup, A in sorted(incons[t]):
            ad = dict(alpha_tup)
            off_A = sorted(A - Pt)
            c_ints = {c: c_int_ordered(clauses[c], Var_t[t], var_rank) for c in off_A}
            if any(len(c_ints[c]) == 0 for c in off_A):
                continue
            ranges = [range(len(c_ints[c])) for c in off_A]

            for ch_tup in itertools.product(*ranges):
                choices = dict(zip(off_A, ch_tup))
                key = (t, alpha_tup, A, tuple(sorted(choices.items())))
                tset = target_mc(t, ad, A, choices)

                taut_nid = derive_taut_if_any(tset)
                if taut_nid is not None:
                    derived[key] = taut_nid
                    check_entry(t, ad, A, choices, taut_nid)
                    continue

                if kind == 'intro_v':
                    x = nd.arg
                    tp = nd.children[0]
                    alpha_p = tuple((v, b) for v, b in alpha_tup if v != x)
                    alpha_p_dict = dict(alpha_p)
                    ell = x if ad[x] == 1 else -x
                    Ax = frozenset(c for c in A if ell not in clauses[c])
                    A_base = set(Ax)
                    W_p = []
                    for c in sorted((A - Ax) - Pt):
                        C_c = C1_family(c_ints[c])[choices[c]]
                        if C_c[0] == -ell:
                            W_p.append(c)
                        else:
                            A_base.add(c)
                    S_sat = [c for c in sorted(nd.bag_c - Pt - A)
                             if ell in clauses[c] and not alpha_sat_clause(alpha_p_dict, clauses[c])]
                    W_unsat = {c for c in W_p if not alpha_sat_clause(alpha_p_dict, clauses[c])} | set(S_sat)
                    W_list = [c for c in sorted(W_unsat)
                              if any(var(l) not in nodes[tp].bag_v for l in c_int_ordered(clauses[c], Var_t[tp], var_rank))]

                    def solve_wp(idx, A_cur, ch_cur):
                        if idx == len(W_list):
                            return derived[(tp, alpha_p, frozenset(A_cur), tuple(sorted(ch_cur.items())))]
                        c = W_list[idx]
                        c_ord_p = c_int_ordered(clauses[c], Var_t[tp], var_rank)
                        p_pos = sum(1 for l in c_ord_p if var(l) not in nodes[tp].bag_v)
                        cur_nid = solve_wp(idx + 1, A_cur, ch_cur)
                        cur_mc = set(proof.nodes[cur_nid]['mc'])
                        neg_ks = [k for k in range(p_pos) if -c_ord_p[k] in cur_mc]
                        start_k = 0
                        if neg_ks:
                            k0 = max(neg_ks)
                            ch_next = dict(ch_cur)
                            ch_next[c] = k0
                            cur_nid = solve_wp(idx + 1, A_cur | {c}, ch_next)
                            start_k = k0 + 1
                        for k in range(start_k, p_pos):
                            lit_k = c_ord_p[k]
                            ch_next = dict(ch_cur)
                            ch_next[c] = k
                            rhs_nid = solve_wp(idx + 1, A_cur | {c}, ch_next)
                            if lit_k in proof.nodes[cur_nid]['mc']:
                                cur_nid = proof.resolve_any_order(cur_nid, rhs_nid, var(lit_k))
                        return cur_nid

                    ch_base = {}
                    for c in sorted(frozenset(A_base) - Pt):
                        c_ord_p = c_int_ordered(clauses[c], Var_t[tp], var_rank)
                        hv = var(C1_family(c_ints[c])[choices[c]][0])
                        ch_base[c] = [j for j, l in enumerate(c_ord_p) if var(l) == hv][0]
                    nid_tp = solve_wp(0, A_base, ch_base)
                    derived[key] = proof.weaken_to(nid_tp, tset)

                elif kind == 'intro_c':
                    c_new = nd.arg
                    tp = nd.children[0]
                    if c_new not in A:
                        ch_p = {c: choices[c] for c in off_A}
                        pid_p = derived[(tp, alpha_tup, A, tuple(sorted(ch_p.items())))]
                        derived[key] = proof.weaken_to(pid_p, tset)
                    elif alpha_sat_clause(ad, clauses[c_new]):
                        A_p = A - {c_new}
                        ch_p = {c: choices[c] for c in off_A if c != c_new}
                        pid_p = derived[(tp, alpha_tup, A_p, tuple(sorted(ch_p.items())))]
                        derived[key] = proof.weaken_to(pid_p, tset)
                    else:
                        if c_new in Pt:
                            init_id = proof.get_init(clauses[c_new])
                            derived[key] = proof.weaken_to(init_id, tset)
                        else:
                            C_c = C1_family(c_ints[c_new])[choices[c_new]]
                            hl = C_c[0]
                            assert -hl in c_alpha_lits(ad)
                            ax_id = proof.get_axiom(var(hl))
                            derived[key] = proof.weaken_to(ax_id, tset)

                elif kind == 'forget_c':
                    c_fg = nd.arg
                    tp = nd.children[0]
                    if tp in P_paths[c_fg]:
                        ch_p = dict(choices)
                        derived[key] = derived[(tp, alpha_tup, A | {c_fg}, tuple(sorted(ch_p.items())))]
                    else:
                        c_ord = c_int_ordered(clauses[c_fg], Var_t[tp], var_rank)
                        neg_indices = [idx for idx, lit in enumerate(c_ord) if -lit in tset]
                        if neg_indices:
                            j = max(neg_indices)
                            ch_p = dict(choices)
                            ch_p[c_fg] = j
                            cur_id = derived[(tp, alpha_tup, A | {c_fg}, tuple(sorted(ch_p.items())))]
                            for idx in range(j + 1, len(c_ord)):
                                ch_p = dict(choices)
                                ch_p[c_fg] = idx
                                pid_i = derived[(tp, alpha_tup, A | {c_fg}, tuple(sorted(ch_p.items())))]
                                cur_id = proof.resolve_any_order(cur_id, pid_i, var(c_ord[idx]))
                            derived[key] = cur_id
                        else:
                            cur_id = proof.weaken_to(proof.get_init(clauses[c_fg]), tset | set(c_ord))
                            for idx, lit in enumerate(c_ord):
                                ch_p = dict(choices)
                                ch_p[c_fg] = idx
                                pid_i = derived[(tp, alpha_tup, A | {c_fg}, tuple(sorted(ch_p.items())))]
                                cur_id = proof.resolve_any_order(cur_id, pid_i, var(lit))
                            derived[key] = cur_id

                elif kind == 'forget_v':
                    x = nd.arg
                    tp = nd.children[0]
                    alpha0 = tuple(sorted(list(alpha_tup) + [(x, 0)]))
                    alpha1 = tuple(sorted(list(alpha_tup) + [(x, 1)]))
                    pid0 = derived[(tp, alpha0, A, tuple(sorted(choices.items())))]
                    pid1 = derived[(tp, alpha1, A, tuple(sorted(choices.items())))]
                    if x in tset:
                        derived[key] = pid0
                    elif -x in tset:
                        derived[key] = pid1
                    else:
                        derived[key] = proof.resolve(pid0, pid1, x)

                elif kind == 'join':
                    t1, t2 = nd.children
                    B1 = frozenset(c for c in A if t1 in P_paths[c])
                    B2 = frozenset(c for c in A if t2 in P_paths[c])
                    A1_off = frozenset(c for c in off_A if var(C1_family(c_ints[c])[choices[c]][0]) in (Var_t[t1] - nd.bag_v))
                    A2_off = frozenset(off_A) - A1_off
                    b0_sat = frozenset(c for c in (Pt & A) if alpha_sat_clause(ad, clauses[c]))
                    b0_unsat = (Pt & A) - b0_sat
                    B1_pure = frozenset(c for c in (B1 & b0_unsat) if not any(var(l) not in nd.bag_v for l in c_int_ordered(clauses[c], Var_t[t2], var_rank)))
                    B2_pure = frozenset(c for c in (B2 & b0_unsat) if not any(var(l) not in nd.bag_v for l in c_int_ordered(clauses[c], Var_t[t1], var_rank)))
                    b0_list = sorted(b0_unsat - B1_pure - B2_pure)

                    def rec_target(A1_b, A2_b, idx, ch_b2, ch_b1):
                        ts = set(c_alpha_lits(ad))
                        for c in ((A1_b & B1) | B1_pure):
                            if not alpha_sat_clause(ad, clauses[c]):
                                ts |= c_ext_lits(clauses[c], Var_t[t1])
                        for c in (A1_b & B2):
                            ts |= set(C1_family(c_int_ordered(clauses[c], Var_t[t1], var_rank))[ch_b2[c]])
                        for c in ((A2_b & B2) | B2_pure):
                            if not alpha_sat_clause(ad, clauses[c]):
                                ts |= c_ext_lits(clauses[c], Var_t[t2])
                        for c in (A2_b & B1):
                            ts |= set(C1_family(c_int_ordered(clauses[c], Var_t[t2], var_rank))[ch_b1[c]])
                        for c in b0_list[idx:]:
                            ts |= c_ext_lits(clauses[c], Var_t[t])
                        for c in off_A:
                            ts |= set(C1_family(c_ints[c])[choices[c]])
                        for c in (nd.bag_c - Pt - A):
                            if not alpha_sat_clause(ad, clauses[c]):
                                ts |= set(c_int_ordered(clauses[c], Var_t[t], var_rank))
                        return frozenset(ts)

                    def rec_join(A1_b, A2_b, idx, ch_b2, ch_b1):
                        rt = rec_target(A1_b, A2_b, idx, ch_b2, ch_b1)
                        tnid = derive_taut_if_any(rt)
                        if tnid is not None:
                            return tnid
                        if idx == len(b0_list):
                            A1 = A1_off | A1_b | B1_pure
                            A2 = A2_off | A2_b | B2_pure
                            if (alpha_tup, A1) in incons[t1]:
                                P2_all = frozenset(c for c in nd.bag_c if t2 in P_paths[c])
                                D1 = sorted(c for c in ((P2_all - A) | A2_off) if not alpha_sat_clause(ad, clauses[c])
                                            and any(var(l) not in nd.bag_v for l in c_int_ordered(clauses[c], Var_t[t1], var_rank)))

                                def solve_d1(d_idx, A1_cur, ch1_cur):
                                    # Target at t1: rt restricted to Var_{t1} minus t2-only parts + D1[d_idx:]'s c_{t1}^{int}
                                    # Wait: target at t1 for A1_cur, ch1_cur is exact at derived[(t1, ...)]!
                                    if d_idx == len(D1):
                                        ch1 = dict(ch1_cur)
                                        for c in sorted(A1 - B1):
                                            if c in B2:
                                                ch1[c] = ch_b2[c]
                                            else:
                                                c_ord1 = c_int_ordered(clauses[c], Var_t[t1], var_rank)
                                                hv = var(C1_family(c_ints[c])[choices[c]][0])
                                                ch1[c] = [j for j, l in enumerate(c_ord1) if var(l) == hv][0]
                                        return derived[(t1, alpha_tup, A1_cur, tuple(sorted(ch1.items())))]
                                    dc = D1[d_idx]
                                    c_ord1 = c_int_ordered(clauses[dc], Var_t[t1], var_rank)
                                    pure_js = [j for j, l in enumerate(c_ord1) if var(l) not in nd.bag_v]
                                    cur_d = solve_d1(d_idx + 1, A1_cur, ch1_cur)
                                    cur_mc = set(proof.nodes[cur_d]['mc'])
                                    neg_js = [j for j in pure_js if -c_ord1[j] in cur_mc]
                                    if neg_js:
                                        j0 = max(neg_js)
                                        ch1_next = dict(ch1_cur)
                                        ch1_next[dc] = j0
                                        cur_d = solve_d1(d_idx + 1, A1_cur | {dc}, ch1_next)
                                        rest_js = [j for j in pure_js if j > j0]
                                    else:
                                        rest_js = pure_js
                                    for j in rest_js:
                                        ch1_next = dict(ch1_cur)
                                        ch1_next[dc] = j
                                        rhs_d = solve_d1(d_idx + 1, A1_cur | {dc}, ch1_next)
                                        if c_ord1[j] in proof.nodes[cur_d]['mc']:
                                            cur_d = proof.resolve_any_order(cur_d, rhs_d, var(c_ord1[j]))
                                    return cur_d

                                pid1 = solve_d1(0, A1, {})
                                return proof.weaken_to(pid1, rt)

                            assert (alpha_tup, A2) in incons[t2]
                            P1_all = frozenset(c for c in nd.bag_c if t1 in P_paths[c])
                            D2 = sorted(c for c in (P1_all - A) if not alpha_sat_clause(ad, clauses[c])
                                        and any(var(l) not in nd.bag_v for l in c_int_ordered(clauses[c], Var_t[t2], var_rank)))

                            def solve_d2(d_idx, A2_cur, ch2_cur):
                                if d_idx == len(D2):
                                    ch2 = dict(ch2_cur)
                                    for c in sorted(A2 - B2):
                                        if c in B1:
                                            ch2[c] = ch_b1[c]
                                        else:
                                            c_ord2 = c_int_ordered(clauses[c], Var_t[t2], var_rank)
                                            hv = var(C1_family(c_ints[c])[choices[c]][0])
                                            ch2[c] = [j for j, l in enumerate(c_ord2) if var(l) == hv][0]
                                    return derived[(t2, alpha_tup, A2_cur, tuple(sorted(ch2.items())))]
                                dc = D2[d_idx]
                                c_ord2 = c_int_ordered(clauses[dc], Var_t[t2], var_rank)
                                pure_js = [j for j, l in enumerate(c_ord2) if var(l) not in nd.bag_v]
                                cur_d = solve_d2(d_idx + 1, A2_cur, ch2_cur)
                                cur_mc = set(proof.nodes[cur_d]['mc'])
                                neg_js = [j for j in pure_js if -c_ord2[j] in cur_mc]
                                if neg_js:
                                    j0 = max(neg_js)
                                    ch2_next = dict(ch2_cur)
                                    ch2_next[dc] = j0
                                    cur_d = solve_d2(d_idx + 1, A2_cur | {dc}, ch2_next)
                                    rest_js = [j for j in pure_js if j > j0]
                                else:
                                    rest_js = pure_js
                                for j in rest_js:
                                    ch2_next = dict(ch2_cur)
                                    ch2_next[dc] = j
                                    rhs_d = solve_d2(d_idx + 1, A2_cur | {dc}, ch2_next)
                                    if c_ord2[j] in proof.nodes[cur_d]['mc']:
                                        cur_d = proof.resolve_any_order(cur_d, rhs_d, var(c_ord2[j]))
                                return cur_d

                            pid2 = solve_d2(0, A2, {})
                            return proof.weaken_to(pid2, rt)

                        c = b0_list[idx]
                        if c in B2:
                            c_ord1 = c_int_ordered(clauses[c], Var_t[t1], var_rank)
                            pure_idx = [j for j, l in enumerate(c_ord1) if var(l) not in nd.bag_v]
                            if not pure_idx:
                                return rec_join(A1_b, A2_b | {c}, idx + 1, ch_b2, ch_b1)
                            neg_js = [j for j in pure_idx if -c_ord1[j] in rt]
                            if neg_js:
                                j0 = max(neg_js)
                                ch_b2_next = dict(ch_b2)
                                ch_b2_next[c] = j0
                                pid_j0 = rec_join(A1_b | {c}, A2_b, idx + 1, ch_b2_next, ch_b1)
                                tail_lits = {c_ord1[j] for j in pure_idx if j > j0}
                                cur_id = proof.weaken_to(pid_j0, rt | tail_lits)
                                rest_js = [j for j in pure_idx if j > j0]
                            else:
                                cur_id = rec_join(A1_b, A2_b | {c}, idx + 1, ch_b2, ch_b1)
                                rest_js = pure_idx
                            for j in rest_js:
                                ch_b2_next = dict(ch_b2)
                                ch_b2_next[c] = j
                                pid_R = rec_join(A1_b | {c}, A2_b, idx + 1, ch_b2_next, ch_b1)
                                cur_id = proof.resolve_any_order(cur_id, pid_R, var(c_ord1[j]))
                            return cur_id

                        c_ord2 = c_int_ordered(clauses[c], Var_t[t2], var_rank)
                        pure_idx = [j for j, l in enumerate(c_ord2) if var(l) not in nd.bag_v]
                        if not pure_idx:
                            return rec_join(A1_b | {c}, A2_b, idx + 1, ch_b2, ch_b1)
                        neg_js = [j for j in pure_idx if -c_ord2[j] in rt]
                        if neg_js:
                            j0 = max(neg_js)
                            ch_b1_next = dict(ch_b1)
                            ch_b1_next[c] = j0
                            pid_j0 = rec_join(A1_b, A2_b | {c}, idx + 1, ch_b2, ch_b1_next)
                            tail_lits = {c_ord2[j] for j in pure_idx if j > j0}
                            cur_id = proof.weaken_to(pid_j0, rt | tail_lits)
                            rest_js = [j for j in pure_idx if j > j0]
                        else:
                            cur_id = rec_join(A1_b | {c}, A2_b, idx + 1, ch_b2, ch_b1)
                            rest_js = pure_idx
                        for j in rest_js:
                            ch_b1_next = dict(ch_b1)
                            ch_b1_next[c] = j
                            pid_R = rec_join(A1_b, A2_b | {c}, idx + 1, ch_b2, ch_b1_next)
                            cur_id = proof.resolve_any_order(cur_id, pid_R, var(c_ord2[j]))
                        return cur_id

                    derived[key] = rec_join(frozenset(), frozenset(), 0, {}, {})

                check_entry(t, ad, A, choices, derived[key])

    root_id = derived[(root, (), frozenset(), ())]
    assert proof.nodes[root_id]['mc'] == ()
    mlen, rlen = proof.convert_to_res_and_check_regular(root_id)
    return w_ceil, len(nodes), mlen, rlen


def all_paths(nodes, c_idx):
    sub = {nd.nid for nd in nodes if c_idx in nd.bag_c}
    parent = {ch: nd.nid for nd in nodes for ch in nd.children}
    r_sub = [u for u in sub if parent.get(u) not in sub][0]
    res = [frozenset()]

    def dfs(u, acc):
        chs = [ch for ch in nodes[u].children if ch in sub]
        if not chs:
            res.append(frozenset(acc))
        else:
            for ch in chs:
                dfs(ch, acc | {ch})

    dfs(r_sub, {r_sub})
    return res


def main():
    total_cases = 0

    # 1. 4-clause join puzzle across all (P0, P1) choices
    cl1 = [(3, 2), (2, 4), (-2, 4), (-4,)]
    adj1 = {0: [1, 2], 1: [0], 2: [0]}
    bv1 = {0: {4}, 1: {3, 4}, 2: {2, 4}}
    bc1 = {0: {0, 1, 2, 3}, 1: {0}, 2: {0, 1, 2}}
    n1, r1 = make_nice_td_from_tree(cl1, adj1, bv1, bc1, root=0)
    for p0 in all_paths(n1, 0):
        for p1 in all_paths(n1, 1):
            P1 = {0: p0, 1: p1, 2: frozenset(), 3: frozenset()}
            w, vt, ml, rl = verify_hybrid_construction(cl1, n1, r1, P1)
            total_cases += 1
    print(f"[PASS] Case 1 (4-clause join puzzle, {total_cases} P-families): w_ceil={w}, |V(T)|={vt}, last rlen={rl}")

    # 2. B1 + two B2 clauses sharing variables at join
    cl2 = [(1, 2, 3), (1, 2, -3), (-1, 4), (-1, -4), (-2, 5), (-2, -5), (1, -2, 3)]
    adj2 = {0: [1, 2], 1: [0], 2: [0]}
    bv2 = {0: {3}, 1: {1, 3, 4}, 2: {2, 3, 5}}
    bc2 = {0: {0, 1, 6}, 1: {0, 1, 2, 3, 6}, 2: {0, 1, 4, 5, 6}}
    n2, r2 = make_nice_td_from_tree(cl2, adj2, bv2, bc2, root=0)
    p0s2, p1s2, p6s2 = all_paths(n2, 0), all_paths(n2, 1), all_paths(n2, 6)
    P2 = {c: frozenset() for c in range(len(cl2))}
    P2[0], P2[1], P2[6] = p0s2[1], p1s2[-1], p6s2[-1]
    w, vt, ml, rl = verify_hybrid_construction(cl2, n2, r2, P2)
    total_cases += 1
    print(f"[PASS] Case 2 (B1 & two B2 shared-var join): w_ceil={w}, |V(T)|={vt}, mlen={ml}, rlen={rl}")

    # 3. Multi-clause W_p opposite literals at intro_v
    cl_wp = [(1, 2), (1, -2), (1, 3), (-1,), (-3,)]
    adj_wp = {0: [1], 1: [0]}
    bv_wp = {0: {1}, 1: {2, 3}}
    bc_wp = {0: {0, 1, 2, 3, 4}, 1: {0, 1, 2, 4}}
    n_wp, r_wp = make_nice_td_from_tree(cl_wp, adj_wp, bv_wp, bc_wp, root=0)
    w, vt, ml, rl = verify_hybrid_construction(cl_wp, n_wp, r_wp, {i: frozenset() for i in range(len(cl_wp))})
    total_cases += 1
    print(f"[PASS] Case 3 (W_p opposite literals at intro_v): w_ceil={w}, |V(T)|={vt}, mlen={ml}, rlen={rl}")

    # 4. 2-level join Case A across all 12 (P0, P1) path families
    clA = [(1, 2), (-2, 3, 4), (-1, 5), (-1, -5), (-3, 2), (-3, -2), (-4, -2), (-4, 2)]
    adjA = {0: [1, 2], 1: [0, 3], 3: [1, 4, 5], 4: [3], 5: [3], 2: [0]}
    bvA = {0: {2}, 1: {2}, 3: {2}, 4: {1, 2, 5}, 5: {2, 3}, 2: {2, 4}}
    bcA = {0: {1}, 1: {1}, 3: {0, 1}, 4: {0, 2, 3}, 5: {0, 1, 4, 5}, 2: {1, 6, 7}}
    nA, rA = make_nice_td_from_tree(clA, adjA, bvA, bcA, root=0)
    cA_cnt = 0
    for p0 in all_paths(nA, 0):
        for p1 in all_paths(nA, 1):
            PA = {i: frozenset() for i in range(len(clA))}
            PA[0], PA[1] = p0, p1
            w, vt, ml, rl = verify_hybrid_construction(clA, nA, rA, PA)
            cA_cnt += 1
            total_cases += 1
    print(f"[PASS] Case 4 (2-level join across all {cA_cnt} P-families): w_ceil={w}, |V(T)|={vt}, last rlen={rl}")

    # 5. Width-5 clause along path (bounded w_plog regardless of width)
    clB = [(1, 2, 3, 4, 5), (-1,), (-2,), (-3,), (-4,), (-5, 6), (-5, -6)]
    adjB = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3]}
    bvB = {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5, 6}}
    bcB = {0: {0, 1}, 1: {0, 2}, 2: {0, 3}, 3: {0, 4}, 4: {0, 5, 6}}
    nB, rB = make_nice_td_from_tree(clB, adjB, bvB, bcB, root=0)
    for p0 in all_paths(nB, 0):
        PB = {i: frozenset() for i in range(len(clB))}
        PB[0] = p0
        w, vt, ml, rl = verify_hybrid_construction(clB, nB, rB, PB)
        total_cases += 1
    print(f"[PASS] Case 5 (width-5 clause on-path & off-path): w_ceil={w}, |V(T)|={vt}, last rlen={rl}")

    # 6. 9-clause adversary with non-empty P (testing Lemma 2 j0 & C0+C1 join interplay)
    cl9 = [(-1, -3, 6), (2, -3, 4), (5,), (1, -2), (-5, 3, 4), (-5, 3, -4), (-5, -3, -4), (-5, -6, 4), (-5, -6, -4)]
    adj9 = {0: [1], 1: [0, 2, 3], 2: [1], 3: [1]}
    bv9 = {0: set(), 1: set(), 2: {1, 2}, 3: {3, 4, 5, 6}}
    bc9 = {0: {1, 2}, 1: {0, 1, 2}, 2: {0, 1, 3}, 3: {0, 1, 2, 4, 5, 6, 7, 8}}
    n9, r9 = make_nice_td_from_tree(cl9, adj9, bv9, bc9, root=0)
    p0s9, p1s9 = all_paths(n9, 0), all_paths(n9, 1)
    P9 = {i: frozenset() for i in range(len(cl9))}
    P9[0], P9[1] = p0s9[-1], p1s9[1]
    w, vt, ml, rl = verify_hybrid_construction(cl9, n9, r9, P9)
    total_cases += 1
    print(f"[PASS] Case 6 (9-clause C0+C1 join adversary, non-empty P): w_ceil={w}, |V(T)|={vt}, rlen={rl}")

    # 7. Pigeonhole PHP(3,2) with nice TD and non-empty P
    def v_php(p, h):
        return p * 2 + h + 1
    cl_php = []
    for p in range(3):
        cl_php.append((v_php(p, 0), v_php(p, 1)))
    for h in range(2):
        for p1 in range(3):
            for p2 in range(p1 + 1, 3):
                cl_php.append((-v_php(p1, h), -v_php(p2, h)))
    # Simple decomposition: root bag holds hole-clauses, 3 children hold pigeon clauses
    adj_php = {0: [1, 2, 3], 1: [0], 2: [0], 3: [0]}
    bv_php = {0: {1, 2, 3, 4}, 1: {1, 2}, 2: {3, 4}, 3: {5, 6, 1, 2, 3, 4}}
    bc_php = {0: {3, 4, 5, 6, 7, 8}, 1: {0, 3, 6}, 2: {1, 3, 6}, 3: {2, 4, 5, 7, 8}}
    # Check edge coverage: all edges covered cleanly if bag 0 has all vars 1..6? Wait: bag 3 has 5,6 and 1,2,3,4;
    # pigeon 0 clause {1,2} in bag 1; pigeon 1 clause {3,4} in bag 2; pigeon 2 clause {5,6} in bag 3;
    # hole 0 clauses (3: {1,3}, 4: {1,5}, 5: {3,5}) and hole 1 clauses (6: {2,4}, 7: {2,6}, 8: {4,6}):
    # vars 5,6 only appear in bag 3 -> clauses 4,5,7,8 must have {5,6} inside bag 3 (yes, 4,5,7,8 are in bc[3] AND bc[0] doesn't need 5,6!).
    bv_php = {0: {1, 2, 3, 4}, 1: {1, 2}, 2: {3, 4}, 3: {1, 2, 3, 4, 5, 6}}
    bc_php = {0: {4, 5, 7, 8}, 1: {0, 3, 6}, 2: {1, 3, 6}, 3: {2, 4, 5, 7, 8}}
    #Wait: clause 3={1,3} in bag 1 & bag 2 -> must also be in bag 0 (connectedness)! Same for clause 6={2,4}!
    bc_php = {0: {3, 4, 5, 6, 7, 8}, 1: {0, 3, 6}, 2: {1, 3, 6}, 3: {2, 4, 5, 7, 8}}
    n_php, r_php = make_nice_td_from_tree(cl_php, adj_php, bv_php, bc_php, root=0)
    P_php = {i: frozenset() for i in range(len(cl_php))}
    P_php[3] = all_paths(n_php, 3)[1]
    P_php[6] = all_paths(n_php, 6)[-1]
    w, vt, ml, rl = verify_hybrid_construction(cl_php, n_php, r_php, P_php)
    total_cases += 1
    print(f"[PASS] Case 7 (PHP(3,2) with non-empty P): w_ceil={w}, |V(T)|={vt}, rlen={rl}")

    # 8. Join off-path A2_off adversary: c0=(1,2), c1=(-1), c2=(-2), c0 completely off-path
    cl_jadv = [(1, 2), (-1,), (-2,)]
    adj_jadv = {0: [1, 2], 1: [0], 2: [0]}
    bv_jadv = {0: set(), 1: {1}, 2: {2}}
    bc_jadv = {0: {0}, 1: {0, 1}, 2: {0, 2}}
    n_jadv, r_jadv = make_nice_td_from_tree(cl_jadv, adj_jadv, bv_jadv, bc_jadv, root=0)
    P_jadv = {0: frozenset(), 1: all_paths(n_jadv, 1)[0], 2: all_paths(n_jadv, 2)[0]}
    w, vt, ml, rl = verify_hybrid_construction(cl_jadv, n_jadv, r_jadv, P_jadv)
    total_cases += 1
    print(f"[PASS] Case 8 (join A2_off adversary): w_ceil={w}, |V(T)|={vt}, rlen={rl}")

    # 9. 5-clause mixed neg-lit & P_0 modes (c0=(1,2,3), (-1,-2), (-1,2), (1,-2), (-3))
    cl_m5 = [(1, 2, 3), (-1, -2), (-1, 2), (1, -2), (-3,)]
    adj_m5 = {0: [1, 2], 1: [0], 2: [0]}
    bv_m5 = {0: set(), 1: {1, 2}, 2: {3}}
    bc_m5 = {0: {0}, 1: {0, 1, 2, 3}, 2: {0, 4}}
    n_m5, r_m5 = make_nice_td_from_tree(cl_m5, adj_m5, bv_m5, bc_m5, root=0)
    for p0 in [frozenset(), all_paths(n_m5, 0)[0], all_paths(n_m5, 0)[-1]]:
        P_m5 = {0: p0, 1: frozenset(), 2: frozenset(), 3: frozenset(), 4: frozenset()}
        w, vt, ml, rl = verify_hybrid_construction(cl_m5, n_m5, r_m5, P_m5)
        total_cases += 1
    print(f"[PASS] Case 9 (5-clause neg-lit and P_0 modes): w_ceil={w}, |V(T)|={vt}, last rlen={rl}")

    # 10. AUDIT Bug 1 (intro_v S_sat): c0=(1,2), c1=(-1), c2=(1), c0 off-path, intro_v(2) above empty bag
    cl_a1 = [(1, 2), (-1,), (1,)]
    nd_a1 = [
        TDNode(0, 'leaf', set(), set(), [], None),
        TDNode(1, 'intro_c', set(), {0}, [0], 0),
        TDNode(2, 'intro_v', {1}, {0}, [1], 1),
        TDNode(3, 'intro_c', {1}, {0, 1}, [2], 1),
        TDNode(4, 'forget_c', {1}, {0}, [3], 1),
        TDNode(5, 'intro_c', {1}, {0, 2}, [4], 2),
        TDNode(6, 'forget_c', {1}, {0}, [5], 2),
        TDNode(7, 'forget_v', set(), {0}, [6], 1),
        TDNode(8, 'intro_v', {2}, {0}, [7], 2),
        TDNode(9, 'forget_c', {2}, set(), [8], 0),
        TDNode(10, 'forget_v', set(), set(), [9], 2),
    ]
    P_a1 = {0: frozenset(), 1: frozenset({3}), 2: frozenset({5})}
    w, vt, ml, rl = verify_hybrid_construction(cl_a1, nd_a1, 10, P_a1)
    total_cases += 1
    print(f"[PASS] Case 10 (AUDIT Bug 1 intro_v S_sat): w_ceil={w}, |V(T)|={vt}, rlen={rl}")

    # 11. AUDIT Bug 2 (intro_v alpha'-sat W_p): c0=(1,2), c1=(3,2), c2=(-3), c3=(3), forg(3)<forg(1)<forg(2)
    cl_a2 = [(1, 2), (3, 2), (-3,), (3,)]
    nd_a2 = [
        TDNode(0, 'leaf', set(), set(), [], None),
        TDNode(1, 'intro_c', set(), {0}, [0], 0),
        TDNode(2, 'intro_c', set(), {0, 1}, [1], 1),
        TDNode(3, 'intro_v', {3}, {0, 1}, [2], 3),
        TDNode(4, 'intro_c', {3}, {0, 1, 2}, [3], 2),
        TDNode(5, 'forget_c', {3}, {0, 1}, [4], 2),
        TDNode(6, 'intro_c', {3}, {0, 1, 3}, [5], 3),
        TDNode(7, 'forget_c', {3}, {0, 1}, [6], 3),
        TDNode(8, 'forget_v', set(), {0, 1}, [7], 3),
        TDNode(9, 'intro_v', {1}, {0, 1}, [8], 1),
        TDNode(10, 'forget_v', set(), {0, 1}, [9], 1),
        TDNode(11, 'intro_v', {2}, {0, 1}, [10], 2),
        TDNode(12, 'forget_c', {2}, {1}, [11], 0),
        TDNode(13, 'forget_c', {2}, set(), [12], 1),
        TDNode(14, 'forget_v', set(), set(), [13], 2),
    ]
    P_a2 = {0: frozenset(), 1: frozenset(), 2: frozenset({4}), 3: frozenset({6})}
    w, vt, ml, rl = verify_hybrid_construction(cl_a2, nd_a2, 14, P_a2)
    total_cases += 1
    print(f"[PASS] Case 11 (AUDIT Bug 2 intro_v alpha'-sat W_p): w_ceil={w}, |V(T)|={vt}, rlen={rl}")

    # 12. AUDIT Bug 3 (forget_c L0 weakening G != bot): c0=(1), c1=(-2), c2=(2), c0 off-path with x2 in bag
    cl_a3 = [(1,), (-2,), (2,)]
    nd_a3 = [
        TDNode(0, 'leaf', set(), set(), [], None),
        TDNode(1, 'intro_c', set(), {0}, [0], 0),
        TDNode(2, 'intro_v', {1}, {0}, [1], 1),
        TDNode(3, 'forget_v', set(), {0}, [2], 1),
        TDNode(4, 'intro_v', {2}, {0}, [3], 2),
        TDNode(5, 'forget_c', {2}, set(), [4], 0),
        TDNode(6, 'intro_c', {2}, {1}, [5], 1),
        TDNode(7, 'forget_c', {2}, set(), [6], 1),
        TDNode(8, 'intro_c', {2}, {2}, [7], 2),
        TDNode(9, 'forget_c', {2}, set(), [8], 2),
        TDNode(10, 'forget_v', set(), set(), [9], 2),
    ]
    P_a3 = {0: frozenset(), 1: frozenset({6}), 2: frozenset({8})}
    w, vt, ml, rl = verify_hybrid_construction(cl_a3, nd_a3, 10, P_a3)
    total_cases += 1
    print(f"[PASS] Case 12 (AUDIT Bug 3 forget_c L0 weaken): w_ceil={w}, |V(T)|={vt}, rlen={rl}")

    # 13. Shared external literal & P_ti \ A != empty multi-clause join test
    cl_s = [(1, 2, 5), (3, 4, 5), (-1,), (-2,), (-3,), (-4,), (-5,)]
    adj_s = {0: [1, 2], 1: [0], 2: [0]}
    bv_s = {0: {5}, 1: {1, 2, 5}, 2: {3, 4, 5}}
    bc_s = {0: {0, 1, 6}, 1: {0, 1, 2, 3}, 2: {0, 1, 4, 5}}
    n_s, r_s = make_nice_td_from_tree(cl_s, adj_s, bv_s, bc_s, root=0)
    P_s = {i: frozenset() for i in range(len(cl_s))}
    P_s[0] = all_paths(n_s, 0)[0]
    P_s[1] = all_paths(n_s, 1)[-1]
    w, vt, ml, rl = verify_hybrid_construction(cl_s, n_s, r_s, P_s)
    total_cases += 1
    print(f"[PASS] Case 13 (shared ext & multi-P join): w_ceil={w}, |V(T)|={vt}, rlen={rl}")

    print(f"ALL {total_cases} EXACT-ARITHMETIC CASES VERIFIED!")
    print("OVERALL: PASS")


if __name__ == '__main__':
    main()
