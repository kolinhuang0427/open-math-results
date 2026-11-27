#!/usr/bin/env python3
"""
Exact pure-integer verification for:
  Dochtermann, Huang, Mawhinney, Oh, Xu (2026), arXiv:2609.13361v1,
  Section 7, Conjecture 7.5 (conj:C>=3 ind) & Conjecture 7.4 (conj:unique).

Zero floats, zero '/' divisions (enforced via AST self-audit in Check 0).
Prints PASS on exit 0, FAIL on any discrepancy.
"""

import ast
import itertools
import sys
import time
import networkx as nx


# ============================================================================
# Check 0: AST Self-Audit (zero floats, zero '/' divisions)
# ============================================================================
def check_zero_floats_and_divs():
    src = open(__file__, "r", encoding="utf-8").read()
    tree = ast.parse(src, filename=__file__)
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            raise AssertionError(f"Float constant found at line {node.lineno}: {node.value}")
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            raise AssertionError(f"True division '/' found at line {node.lineno}")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "float":
            raise AssertionError(f"float() call found at line {node.lineno}")
    print("[OK] Check 0: Zero-float / zero-division AST self-audit passed.")


# ============================================================================
# Exact F_2 Binary Matroid Primitives (pure integer bitmasks)
# ============================================================================
def f2_rank_cols(cols):
    """Exact rank over F_2 of a list of integer column bitmasks."""
    basis = []
    for c in cols:
        x = c
        for b in basis:
            lb = b & -b
            if x & lb:
                x ^= b
        if x:
            basis.append(x)
            basis.sort(key=lambda v: v & -v)
    return len(basis)


def f2_rank_subset(cols, mask):
    """Exact F_2 rank of column subset given by bitmask `mask`."""
    sub = []
    m = mask
    while m:
        lb = m & -m
        sub.append(cols[lb.bit_length() - 1])
        m ^= lb
    return f2_rank_cols(sub)


def f2_is_dep(cols, mask):
    return f2_rank_subset(cols, mask) < mask.bit_count()


def f2_nullspace_basis(cols):
    """Return an F_2-basis of ker(H) as bitmasks over range(len(cols))."""
    m = len(cols)
    # Row-reduce matrix where column j is cols[j], tracking row-ops?
    # Simpler: transpose to m x r rows? Better: standard RREF on r x m!
    if m == 0:
        return []
    r = max((c.bit_length() for c in cols), default=0)
    rows = []
    for i in range(r):
        row = 0
        for j in range(m):
            if (cols[j] >> i) & 1:
                row |= 1 << j
        rows.append(row)
    pivots = []
    cur = 0
    for j in range(m):
        piv = -1
        for i in range(cur, len(rows)):
            if (rows[i] >> j) & 1:
                piv = i
                break
        if piv == -1:
            continue
        rows[cur], rows[piv] = rows[piv], rows[cur]
        for i in range(len(rows)):
            if i != cur and ((rows[i] >> j) & 1):
                rows[i] ^= rows[cur]
        pivots.append((cur, j))
        cur += 1
    piv_cols = {j for _, j in pivots}
    basis = []
    for free in range(m):
        if free in piv_cols:
            continue
        vec = 1 << free
        for i, pj in pivots:
            if (rows[i] >> free) & 1:
                vec |= 1 << pj
        basis.append(vec)
    return basis


def f2_circuits_from_nullspace(null_basis):
    """All inclusion-minimal nonempty elements of span(null_basis)."""
    g = len(null_basis)
    span = [0] * (1 << g)
    for idx in range(g):
        bit = 1 << idx
        v = null_basis[idx]
        for s in range(bit):
            span[s | bit] = span[s] ^ v
    nonempty = sorted(set(span[1:]), key=lambda x: (x.bit_count(), x))
    circs = []
    for x in nonempty:
        if not any((c & x) == c for c in circs):
            circs.append(x)
    return circs


def matroid_components_from_circuits(m, circs):
    """Connected components of matroid on [0..m-1] via circuit connectivity."""
    parent = list(range(m))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for c in circs:
        if c == 0:
            continue
        first = (c & -c).bit_length() - 1
        rem = c ^ (1 << first)
        while rem:
            lb = rem & -rem
            union(first, lb.bit_length() - 1)
            rem ^= lb
    groups = {}
    for e in range(m):
        groups.setdefault(find(e), 0)
        groups[find(e)] |= 1 << e
    return list(groups.values())


def contract_cols(cols, x):
    """Exact F_2 representation of M / x for non-loop x (element indices remapped by removing x)."""
    v = cols[x]
    assert v != 0, "Cannot contract a loop via contract_cols"
    piv_bit = v & -v
    piv_idx = piv_bit.bit_length() - 1
    new_cols = []
    for j, c in enumerate(cols):
        if j == x:
            continue
        if c & piv_bit:
            c ^= v
        # Remove piv_idx bit
        low = c & (piv_bit - 1)
        high = c >> (piv_idx + 1)
        new_cols.append(low | (high << piv_idx))
    return new_cols


def delete_cols(cols, x):
    return [c for j, c in enumerate(cols) if j != x]


def drop_bit(mask, x):
    low = mask & ((1 << x) - 1)
    high = mask >> (x + 1)
    return low | (high << x)


def unique_union(sets):
    ex1 = 0
    ge2 = 0
    for c in sets:
        ex1, ge2 = (ex1 & ~c) | (c & ~(ex1 | ge2)), ge2 | (ex1 & c)
    return ex1


def mult_ge3_mask(m, sets):
    ge3 = 0
    for e in range(m):
        cnt = sum((c >> e) & 1 for c in sets)
        if cnt >= 3:
            ge3 |= 1 << e
    return ge3


def is_cycle_system_f2(cols, sets):
    m = len(cols)
    g = m - f2_rank_cols(cols)
    if len(sets) != g:
        return False
    # Check each set is in ker(H) (i.e. a cycle)
    for c in sets:
        xor_v = 0
        tmp = c
        while tmp:
            lb = tmp & -tmp
            xor_v ^= cols[lb.bit_length() - 1]
            tmp ^= lb
        if xor_v != 0 or c == 0:
            return False
    # Check every nonempty subset has dependent unique union
    states = [(0, 0)]
    for c in sets:
        prev = len(states)
        for s in range(prev):
            ex1, ge2 = states[s]
            nx1 = (ex1 & ~c) | (c & ~(ex1 | ge2))
            ng2 = ge2 | (ex1 & c)
            if not f2_is_dep(cols, nx1):
                return False
            states.append((nx1, ng2))
    return True


def verify_inductive_step_and_cographic(cols, chosen, check_all_x=True):
    """
    Verify on a connected binary matroid (cols) with circuit system `chosen` and D = C_{[g]} a circuit:
      1. C_{>=3} == empty (Main Theorem).
      2. For every x in D (when g >= 2), verify Case 1 (M/x connected -> C'' is a circuit system
         with D\\{x} a circuit and C''_{>=3} = empty) OR Case 2 (M/x disconnected -> every component
         has g(W_j) >= 1, D cap C_1 = {x}, D ^ C_1 is a circuit of M\\x, C_1 cap C_{>=3} = empty,
         and C\\{C_1} is a circuit system on M\\x with total unique union D ^ C_1).
      3. Corollary 2: Reconstruct graph G on {0..g} from {D, C_1, ..., C_g} and verify
         span_F2(delta_G(1..g)) == ker_F2(cols) (i.e. M == M(G)^*).
    """
    m = len(cols)
    r = f2_rank_cols(cols)
    g = m - r
    assert len(chosen) == g
    D = unique_union(chosen)
    ge3 = mult_ge3_mask(m, chosen)
    assert ge3 == 0, f"Main Theorem violated: ge3={bin(ge3)}"

    # Corollary 2: build G on {0..g} from [D] + chosen
    sets_all = [D] + list(chosen)
    adj = [0] * (g + 1)
    for e in range(m):
        inc = [i for i, c in enumerate(sets_all) if (c >> e) & 1]
        assert len(inc) == 2, f"Element {e} has incidence {inc} != 2"
        u, v = inc
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    # Check G is connected
    vis = 1
    q = [0]
    while q:
        u = q.pop()
        nxt = adj[u] & ~vis
        while nxt:
            lb = nxt & -nxt
            v = lb.bit_length() - 1
            vis |= lb
            q.append(v)
            nxt ^= lb
    assert vis == (1 << (g + 1)) - 1, "Reconstructed graph G is disconnected"
    # Verify M == M(G)^* by checking chosen spans ker(cols)
    assert f2_rank_cols(chosen) == g, "chosen not F_2-independent"
    for c in chosen:
        xor_v = 0
        tmp = c
        while tmp:
            lb = tmp & -tmp
            xor_v ^= cols[lb.bit_length() - 1]
            tmp ^= lb
        assert xor_v == 0, "Circuit not in ker(cols)"

    if g <= 1 or not check_all_x:
        return (0, 0)

    c1_hits = 0
    c2_hits = 0
    tmp_d = D
    while tmp_d:
        lb = tmp_d & -tmp_d
        x = lb.bit_length() - 1
        tmp_d ^= lb
        # Unique C_1 containing x
        idx1 = [i for i, c in enumerate(chosen) if (c >> x) & 1]
        assert len(idx1) == 1
        i1 = idx1[0]
        C1 = chosen[i1]
        # Contract x
        cols_con = contract_cols(cols, x)
        nb_con = f2_nullspace_basis(cols_con)
        circs_con = f2_circuits_from_nullspace(nb_con)
        circs_con_set = set(circs_con)
        comps = matroid_components_from_circuits(m - 1, circs_con)
        c_con = [drop_bit(c & ~(1 << x), x) for c in chosen]
        d_con = drop_bit(D & ~(1 << x), x)
        assert d_con in circs_con_set
        assert unique_union(c_con) == d_con
        if len(comps) == 1:
            # Case 1: M/x connected -> every element of C'' is a circuit of M/x
            c1_hits += 1
            for cc in c_con:
                assert cc in circs_con_set, "Lemma 2.21 failed on connected M/x"
        else:
            # Case 2: M/x disconnected
            c2_hits += 1
            # Step 2a: every component has g(W_j) >= 1
            for cm in comps:
                g_comp = cm.bit_count() - f2_rank_subset(cols_con, cm)
                assert g_comp >= 1, "Found coloop component in M/x"
            # Step 2b/2c: D cap C1 == {x}
            assert (D & C1) == (1 << x), f"D cap C1 != {{x}}: D={bin(D)}, C1={bin(C1)}"
            # Check D\{x} and C1\{x} lie in DIFFERENT components of M/x
            c1_con = drop_bit(C1 & ~(1 << x), x)
            comp_d = [cm for cm in comps if (cm & d_con) == d_con]
            comp_c1 = [cm for cm in comps if (cm & c1_con) == c1_con]
            assert len(comp_d) == 1 and len(comp_c1) == 1 and comp_d[0] != comp_c1[0]
            # Step 2d: D ^ C1 is a circuit of M \ x
            cols_del = delete_cols(cols, x)
            nb_del = f2_nullspace_basis(cols_del)
            circs_del_set = set(f2_circuits_from_nullspace(nb_del))
            dc1_del = drop_bit(D ^ C1, x)
            assert dc1_del in circs_del_set, "Lemma 3 failed: D ^ C1 not a circuit of M\\x"
            # Step 2e: C' = C \ {C1} is a circuit system on M\x with total UU = D ^ C1
            c_del = [drop_bit(c, x) for i, c in enumerate(chosen) if i != i1]
            assert unique_union(c_del) == dc1_del
            assert mult_ge3_mask(m - 1, c_del) == 0
            assert all(c in circs_del_set for c in c_del)
    return (c1_hits, c2_hits)


def verify_conj_unique_for_cs(circ_set, chosen):
    """Verify Conjecture 7.4 (conj:unique): every circuit D has a UNIQUE S subseteq [g] with C_S = D."""
    g = len(chosen)
    states = [(0, 0)]
    for c in chosen:
        prev = len(states)
        for s in range(prev):
            ex1, ge2 = states[s]
            nx1 = (ex1 & ~c) | (c & ~(ex1 | ge2))
            ng2 = ge2 | (ex1 & c)
            states.append((nx1, ng2))
    counts = {}
    for S in range(1, 1 << g):
        uu = states[S][0]
        if uu in circ_set:
            counts[uu] = counts.get(uu, 0) + 1
    assert len(counts) == len(circ_set), "Some circuit missing from unique unions"
    for d, cnt in counts.items():
        assert cnt == 1, f"Conjecture 7.4 violated: circuit {bin(d)} has {cnt} unique-union reps!"


def graph_incidence_cols(n, edges):
    """Standard F_2 vertex-edge incidence columns for graphic matroid M(G)."""
    return [(1 << u) | (1 << v) for (u, v) in edges]


def cographic_cols(n, edges):
    """F_2 representation of cographic matroid M(G)^* via cycle-space basis of G."""
    g_cols = graph_incidence_cols(n, edges)
    # Rows of H_{M*} are a basis of ker(H_M) = cycle space of G
    cyc_basis = f2_nullspace_basis(g_cols)
    m = len(edges)
    cols = []
    for e in range(m):
        col = 0
        for row_i, cyc in enumerate(cyc_basis):
            if (cyc >> e) & 1:
                col |= 1 << row_i
        cols.append(col)
    return cols


# ============================================================================
# Check 1: Explicit Necklace Case-2 Stress Test (all x in D give disconnected M/x)
# ============================================================================
def check_necklace_case2():
    # Vertices: 0, 1, 2 (inner triangle D = {01, 12, 20}), ears through 3, 4, 5
    edges = [
        (0, 1),  # 0: x
        (1, 2),  # 1: y
        (2, 0),  # 2: z
        (0, 3), (3, 1),  # 3, 4: e1, e2
        (1, 4), (4, 2),  # 5, 6: f1, f2
        (2, 5), (5, 0),  # 7, 8: h1, h2
    ]
    cols = graph_incidence_cols(6, edges)
    C1 = (1 << 0) | (1 << 3) | (1 << 4)
    C2 = (1 << 1) | (1 << 5) | (1 << 6)
    C3 = (1 << 2) | (1 << 7) | (1 << 8)
    C4 = (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7) | (1 << 8)
    chosen = [C1, C2, C3, C4]
    assert is_cycle_system_f2(cols, chosen)
    D = unique_union(chosen)
    assert D == ((1 << 0) | (1 << 1) | (1 << 2))
    c1_hits, c2_hits = verify_inductive_step_and_cographic(cols, chosen, check_all_x=True)
    assert c1_hits == 0 and c2_hits == 3, f"Expected all 3 x in D to trigger Case 2, got ({c1_hits}, {c2_hits})"
    # Also verify C4 splits in M/x (not a single circuit in M/0)
    cols_con0 = contract_cols(cols, 0)
    circs_con0 = set(f2_circuits_from_nullspace(f2_nullspace_basis(cols_con0)))
    assert drop_bit(C4, 0) not in circs_con0, "Expected C4 to split in M/x"
    # Verify Conjecture 7.4 on necklace
    circs_neck = set(f2_circuits_from_nullspace(f2_nullspace_basis(cols)))
    verify_conj_unique_for_cs(circs_neck, chosen)
    print(f"[OK] Check 1: Necklace Case-2 stress test passed (Case 1={c1_hits}, Case 2={c2_hits}/3, C4 splits in M/x, conj:unique PASS).")


# ============================================================================
# Check 2: Exhaustive Graphic Matroids (n <= 6, g <= 5, plus K_5)
# ============================================================================
def enumerate_circuit_systems_graphic(n, edges, verify_ind=False, verify_unique=False):
    cols = graph_incidence_cols(n, edges)
    m = len(edges)
    g = m - f2_rank_cols(cols)
    nb = f2_nullspace_basis(cols)
    circs = f2_circuits_from_nullspace(nb)
    circ_set = set(circs)

    def is_dep_graph(mask):
        parent = list(range(n))
        tmp = mask
        while tmp:
            lb = tmp & -tmp
            e = lb.bit_length() - 1
            tmp ^= lb
            u, v = edges[e]
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            while parent[v] != v:
                parent[v] = parent[parent[v]]
                v = parent[v]
            if u == v:
                return True
            parent[u] = v
        return False

    chosen = []
    states = [(0, 0)]
    basis = []
    tot_cs = 0
    tot_circ = 0
    tot_c1 = 0
    tot_c2 = 0

    def f2_indep(x):
        for b in basis:
            if x & (b & -b):
                x ^= b
        return x != 0

    def bt(start):
        nonlocal tot_cs, tot_circ, tot_c1, tot_c2
        if len(chosen) == g:
            tot_cs += 1
            if verify_unique:
                verify_conj_unique_for_cs(circ_set, chosen)
            uu = states[-1][0]
            if uu in circ_set:
                tot_circ += 1
                assert mult_ge3_mask(m, chosen) == 0
                if verify_ind:
                    c1h, c2h = verify_inductive_step_and_cographic(cols, chosen, check_all_x=True)
                    tot_c1 += c1h
                    tot_c2 += c2h
            return
        for idx in range(start, len(circs)):
            c = circs[idx]
            if not f2_indep(c):
                continue
            prev = len(states)
            ok = True
            for s in range(prev):
                ex1, ge2 = states[s]
                nx1 = (ex1 & ~c) | (c & ~(ex1 | ge2))
                ng2 = ge2 | (ex1 & c)
                if not is_dep_graph(nx1):
                    ok = False
                    break
                states.append((nx1, ng2))
            if ok:
                chosen.append(c)
                x = c
                for b in basis:
                    if x & (b & -b):
                        x ^= b
                basis.append(x)
                bt(idx + 1)
                basis.pop()
                chosen.pop()
            del states[prev:]

    bt(0)
    return tot_cs, tot_circ, tot_c1, tot_c2


def check_graphic_exhaustive():
    atlas = nx.graph_atlas_g()
    graphs = [
        nx.convert_node_labels_to_integers(G)
        for G in atlas
        if 3 <= G.number_of_nodes() <= 6
        and nx.is_biconnected(G)
        and (G.number_of_edges() - G.number_of_nodes() + 1) <= 5
    ]
    tot_cs = tot_circ = tot_c1 = tot_c2 = 0
    for G in graphs:
        n = G.number_of_nodes()
        edges = list(G.edges())
        cs, circ, c1, c2 = enumerate_circuit_systems_graphic(n, edges, verify_ind=True, verify_unique=True)
        tot_cs += cs
        tot_circ += circ
        tot_c1 += c1
        tot_c2 += c2

    # Explicitly include K_5 (non-planar, g=6): 5 cone circuit systems, 0 with circuit total UU, all pass conj:unique
    k5_edges = list(itertools.combinations(range(5), 2))
    k5_cs, k5_circ, _, _ = enumerate_circuit_systems_graphic(5, k5_edges, verify_ind=True, verify_unique=True)
    assert k5_cs == 5 and k5_circ == 0, f"Unexpected K_5 counts: cs={k5_cs}, circ={k5_circ}"

    print(
        f"[OK] Check 2: Exhaustive graphic matroids passed "
        f"({len(graphs)} graphs n<=6 g<=5: {tot_cs} circuit systems, {tot_circ} with circuit C_[g], "
        f"all C_>=3=empty, inductive Case1={tot_c1} Case2={tot_c2}, all conj:unique PASS; "
        f"K_5: {k5_cs} CS / {k5_circ} circuit C_[g] / all conj:unique PASS)."
    )


# ============================================================================
# Check 3: Exhaustive Cographic Matroids M(G)^* (all 69 biconnected G, 4 <= n <= 6)
# ============================================================================
def is_connected_mask(n, adj_mask, subset_mask=None):
    if subset_mask is None:
        subset_mask = (1 << n) - 1
    if subset_mask == 0:
        return True
    start = (subset_mask & -subset_mask).bit_length() - 1
    vis = 1 << start
    q = [start]
    while q:
        u = q.pop()
        nxt = adj_mask[u] & subset_mask & ~vis
        while nxt:
            lb = nxt & -nxt
            v = lb.bit_length() - 1
            vis |= lb
            q.append(v)
            nxt ^= lb
    return vis == subset_mask


def get_bonds(n, edges):
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    full = (1 << n) - 1
    bonds = []
    for A in range(2, 1 << n, 2):
        if is_connected_mask(n, adj, A) and is_connected_mask(n, adj, full ^ A):
            em = 0
            for idx, (u, v) in enumerate(edges):
                if bool((A >> u) & 1) != bool((A >> v) & 1):
                    em |= 1 << idx
            bonds.append((A, em))
    return bonds


def check_cographic_exhaustive():
    atlas = nx.graph_atlas_g()
    graphs = [
        nx.convert_node_labels_to_integers(G)
        for G in atlas
        if 4 <= G.number_of_nodes() <= 6 and nx.is_biconnected(G)
    ]
    tot_cs = tot_circ = tot_c1 = tot_c2 = 0
    for G in graphs:
        n = G.number_of_nodes()
        g = n - 1
        edges = list(G.edges())
        m = len(edges)
        cols_dual = cographic_cols(n, edges)
        bonds = get_bonds(n, edges)
        bond_ems = set(em for _, em in bonds)

        def disconnects(cut_mask):
            rem = [0] * n
            for idx, (u, v) in enumerate(edges):
                if not ((cut_mask >> idx) & 1):
                    rem[u] |= 1 << v
                    rem[v] |= 1 << u
            return not is_connected_mask(n, rem)

        chosen = []
        states = [(0, 0)]
        basis = []

        def f2_indep(x):
            for b in basis:
                if x & (b & -b):
                    x ^= b
            return x != 0

        def bt(start):
            nonlocal tot_cs, tot_circ, tot_c1, tot_c2
            if len(chosen) == g:
                tot_cs += 1
                if n <= 5:
                    verify_conj_unique_for_cs(bond_ems, chosen)
                uu = states[-1][0]
                if uu in bond_ems:
                    tot_circ += 1
                    assert mult_ge3_mask(m, chosen) == 0
                    # Run full inductive + Corollary 2 check on n<=5 and on non-planar n=6 (K_{3,3}, K_6)
                    if n <= 5 or m in (9, 15):
                        c1h, c2h = verify_inductive_step_and_cographic(cols_dual, chosen, check_all_x=(n <= 5))
                        tot_c1 += c1h
                        tot_c2 += c2h
                return
            for idx in range(start, len(bonds)):
                A, em = bonds[idx]
                if not f2_indep(A):
                    continue
                prev = len(states)
                ok = True
                for s in range(prev):
                    ex1, ge2 = states[s]
                    nx1 = (ex1 & ~em) | (em & ~(ex1 | ge2))
                    ng2 = ge2 | (ex1 & em)
                    if not disconnects(nx1):
                        ok = False
                        break
                    states.append((nx1, ng2))
                if ok:
                    chosen.append(em)
                    x = A
                    for b in basis:
                        if x & (b & -b):
                            x ^= b
                    basis.append(x)
                    bt(idx + 1)
                    basis.pop()
                    chosen.pop()
                del states[prev:]

        bt(0)

    assert len(graphs) == 69 and tot_cs == 8408 and tot_circ == 2075
    print(
        f"[OK] Check 3: Exhaustive cographic matroids M(G)^* passed "
        f"({len(graphs)} biconnected graphs 4<=n<=6 incl. K5/K3,3/K6: "
        f"{tot_cs} CS, {tot_circ} with circuit C_[g], all C_>=3=empty, Case1={tot_c1} Case2={tot_c2})."
    )


# ============================================================================
# Check 4: Rank-2 Binary Matroids (parallel classes, |D|=2 Case 2),
#          Disconnected Matroids, Hypothesis-Necessity Examples, and M(K5) +_2 M(K5)*
# ============================================================================
def check_rank2_and_special():
    tot_cs = tot_circ = tot_c1 = tot_c2 = 0
    for na in range(1, 4):
        for nb in range(na, 4):
            for nc in range(nb, 4):
                m = na + nb + nc
                if not (4 <= m <= 7):
                    continue
                g = m - 2
                # F_2 columns: class 0 -> 01, class 1 -> 10, class 2 -> 11
                cols = [0b01] * na + [0b10] * nb + [0b11] * nc
                circs = f2_circuits_from_nullspace(f2_nullspace_basis(cols))
                circ_set = set(circs)
                chosen = []
                states = [(0, 0)]
                basis = []

                def f2_indep(x):
                    for b in basis:
                        if x & (b & -b):
                            x ^= b
                    return x != 0

                def bt(start):
                    nonlocal tot_cs, tot_circ, tot_c1, tot_c2
                    if len(chosen) == g:
                        tot_cs += 1
                        verify_conj_unique_for_cs(circ_set, chosen)
                        uu = states[-1][0]
                        if uu in circ_set:
                            tot_circ += 1
                            assert mult_ge3_mask(m, chosen) == 0
                            c1h, c2h = verify_inductive_step_and_cographic(cols, chosen, check_all_x=True)
                            tot_c1 += c1h
                            tot_c2 += c2h
                        return
                    for idx in range(start, len(circs)):
                        c = circs[idx]
                        if not f2_indep(c):
                            continue
                        prev = len(states)
                        ok = True
                        for s in range(prev):
                            ex1, ge2 = states[s]
                            nx1 = (ex1 & ~c) | (c & ~(ex1 | ge2))
                            ng2 = ge2 | (ex1 & c)
                            if not f2_is_dep(cols, nx1):
                                ok = False
                                break
                            states.append((nx1, ng2))
                        if ok:
                            chosen.append(c)
                            x = c
                            for b in basis:
                                if x & (b & -b):
                                    x ^= b
                            basis.append(x)
                            bt(idx + 1)
                            basis.pop()
                            chosen.pop()
                        del states[prev:]

                bt(0)

    # Disconnected matroid with coloops: M(K_4) (+) U_{2,2} (2 coloops)
    k4_edges = list(itertools.combinations(range(4), 2))
    k4_cols = graph_incidence_cols(4, k4_edges)
    # Add 2 coloops (new independent unit rows bits 4 and 5)
    disc_cols = k4_cols + [1 << 4, 1 << 5]
    # Faces of K_4 around outer triangle (0,1,2)
    # edges: 0:(0,1), 1:(0,2), 2:(0,3), 3:(1,2), 4:(1,3), 5:(2,3)
    C_k4 = [
        (1 << 0) | (1 << 2) | (1 << 4),  # (0,1,3)
        (1 << 1) | (1 << 2) | (1 << 5),  # (0,2,3)
        (1 << 3) | (1 << 4) | (1 << 5),  # (1,2,3)
    ]
    assert is_cycle_system_f2(disc_cols, C_k4)
    D_k4 = unique_union(C_k4)
    assert D_k4 == ((1 << 0) | (1 << 1) | (1 << 3))
    assert mult_ge3_mask(len(disc_cols), C_k4) == 0

    # Hypothesis-necessity check 1: Example 6.8 (U_{1,6}), C_{[5]} NOT a circuit, C_{>=3} dependent
    u16_cols = [1] * 6
    ex68 = [(1 << 0) | (1 << 1), (1 << 0) | (1 << 2), (1 << 0) | (1 << 3),
            (1 << 1) | (1 << 4), (1 << 1) | (1 << 5)]
    assert is_cycle_system_f2(u16_cols, ex68)
    uu_ex68 = unique_union(ex68)
    assert uu_ex68 == 0b111100 and uu_ex68 not in set(f2_circuits_from_nullspace(f2_nullspace_basis(u16_cols)))
    ge3_ex68 = mult_ge3_mask(6, ex68)
    assert ge3_ex68 == 0b000011 and f2_is_dep(u16_cols, ge3_ex68)

    # Hypothesis-necessity check 2: Figure 2 (disconnected cycle system, NOT a circuit system)
    # Triangle T={0,1,2} glued at vertex 0 to diamond K4-e {3,4,5,6,7} with diag 7
    fig2_edges = [(0, 1), (1, 2), (2, 0), (0, 3), (3, 4), (4, 5), (5, 0), (0, 4)]
    fig2_cols = graph_incidence_cols(6, fig2_edges)
    T = (1 << 0) | (1 << 1) | (1 << 2)
    U_tri = (1 << 3) | (1 << 4) | (1 << 7)
    L_tri = (1 << 5) | (1 << 6) | (1 << 7)
    fig2_cs = [T, T | U_tri, T | L_tri]
    assert is_cycle_system_f2(fig2_cols, fig2_cs)
    assert unique_union(fig2_cs) == ((1 << 3) | (1 << 4) | (1 << 5) | (1 << 6))  # outer 4-cycle
    assert mult_ge3_mask(8, fig2_cs) == T and f2_is_dep(fig2_cols, T)

    # Regular non-graphic, non-cographic 2-sum: M(K_5) +_2 M(K_5)*
    # M1 = M(K_5) on edges 0..9 (basepoint p = edge 0 = (0,1) in K_5; apex = vertex 4 -> edges (0,1),(0,2),(0,3),(1,2),(1,3),(2,3) in C_{[6]})
    k5_edges = list(itertools.combinations(range(5), 2))
    # Cone system of M(K_5) with apex 4: 6 triangles T_e for e in K_4 on {0,1,2,3}
    e_idx = {e: i for i, e in enumerate(k5_edges)}
    k5_cone = []
    for u, v in itertools.combinations(range(4), 2):
        k5_cone.append((1 << e_idx[(u, v)]) | (1 << e_idx[(u, 4)]) | (1 << e_idx[(v, 4)]))
    # Here p = e_idx[(0,1)] = 0 lies ONLY in k5_cone[0] = {(0,1),(0,4),(1,4)}!
    # M2 = M(K_5)* on 10 edges (0..9), with star system C2_i = delta(i) for i=0,1,2,3 (sink=4).
    # Choose basepoint p' = e_idx[(0,4)] = 3 in M2: p' appears in ONLY delta(0) (1 circuit of M2)!
    # 2-sum M = M1 +_2 M2 along p=0 in M1 (in C1_0 only) and p'=3 in M2 (in delta(0) only):
    # Elements of M: (E(M1)\{0}) = 9 elements (indices 0..8), (E(M2)\{3}) = 9 elements (indices 9..17), total 18 elements, g = 6+4-1 = 9.
    # Circuit space basis of 2-sum M:
    #   C1_1..C1_5 (5 circuits in E1\{p}),
    #   (C1_0 \ {p}) U (delta(0) \ {p'}) (1 glued circuit),
    #   delta(1), delta(2), delta(3) (3 circuits in E2\{p'}).
    def remap_drop(mask, p, offset):
        return drop_bit(mask & ~(1 << p), p) << offset

    m2_stars = []
    for v in range(4):
        st = 0
        for idx, (a, b) in enumerate(k5_edges):
            if a == v or b == v:
                st |= 1 << idx
        m2_stars.append(st)
    # Check p'=3 is edge (0,4): only in m2_stars[0]!
    assert k5_edges[3] == (0, 4)
    assert [i for i, s in enumerate(m2_stars) if (s >> 3) & 1] == [0]

    cs_2sum = [remap_drop(c, 0, 0) for c in k5_cone[1:]]
    cs_2sum.append(remap_drop(k5_cone[0], 0, 0) | remap_drop(m2_stars[0], 3, 9))
    cs_2sum.extend(remap_drop(s, 3, 9) for s in m2_stars[1:])
    assert len(cs_2sum) == 9
    # Construct parity-check / F_2 representation of M(K_5) +_2 M(K_5)* from its circuit space cs_2sum!
    # A binary matroid is uniquely determined by its circuit space Z (9-dim subspace of F_2^18):
    # columns of H are a basis of Z^\perp (dimension 18 - 9 = 9)!
    # Represent Z as 9 x 18 matrix whose rows are cs_2sum; nullspace of Z is a 9-dim basis of Z^\perp!
    z_cols = []
    for e in range(18):
        col = 0
        for r_i, c in enumerate(cs_2sum):
            if (c >> e) & 1:
                col |= 1 << r_i
        z_cols.append(col)
    h_rows = f2_nullspace_basis(z_cols)
    assert len(h_rows) == 9
    cols_2sum = []
    for e in range(18):
        col = 0
        for r_i, row in enumerate(h_rows):
            if (row >> e) & 1:
                col |= 1 << r_i
        cols_2sum.append(col)
    assert is_cycle_system_f2(cols_2sum, cs_2sum)
    # Verify C_{[9]} is NOT a circuit (contains a smaller circuit!)
    uu_2sum = unique_union(cs_2sum)
    # Specifically, the triangle (1,2),(2,3),(1,3) of K_5 is strictly contained in uu_2sum!
    tri_123 = remap_drop((1 << e_idx[(1, 2)]) | (1 << e_idx[(2, 3)]) | (1 << e_idx[(1, 3)]), 0, 0)
    assert (tri_123 & uu_2sum) == tri_123 and tri_123 != uu_2sum and f2_is_dep(cols_2sum, tri_123)

    print(
        f"[OK] Check 4: Rank-2 binary ({tot_cs} CS, {tot_circ} circuit C_[g], Case1={tot_c1} Case2={tot_c2}, "
        f"all C_>=3=empty, all conj:unique PASS), disconnected+coloop, Example 6.8, Figure 2, "
        f"and M(K_5) +_2 M(K_5)* (valid CS, C_[9] not a circuit) all passed."
    )


def main():
    t0 = time.monotonic_ns()
    check_zero_floats_and_divs()
    check_necklace_case2()
    check_graphic_exhaustive()
    check_cographic_exhaustive()
    check_rank2_and_special()
    elapsed_ms = (time.monotonic_ns() - t0) // 1000000
    print(f"PASS (all 5 checks passed in {elapsed_ms} ms)")


if __name__ == "__main__":
    main()
