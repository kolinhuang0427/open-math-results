#!/usr/bin/env python3
"""Independent exact verifier for targets/gaevoy-2606.25895-src2-1/.

Written directly from arXiv:2606.25895v1 (static/definitions.tex, static/tseitin.tex,
static/open.tex, preamble.tex) and PROOF.md without reading verify.py.
Uses zero floating-point arithmetic (pure int and fractions.Fraction).
"""

from collections import deque
from fractions import Fraction
import math
import pathlib
import random
import re

ROOT = pathlib.Path(__file__).resolve().parents[3]
SRC_DIR = ROOT / "tools/.arxiv_cache/eprint/2606.25895"
TARGET_MD = ROOT / "targets/gaevoy-2606.25895-src2-1/TARGET.md"
PROOF_MD = ROOT / "targets/gaevoy-2606.25895-src2-1/PROOF.md"


# ---------------------------------------------------------------------------
# 1. Primary Source & Compiled Numbering Verification
# ---------------------------------------------------------------------------

def check_primary_source() -> None:
    if not SRC_DIR.exists():
        print("[SKIP] local tools/.arxiv_cache not present; skipping TeX snippet check")
        return
    open_tex = (SRC_DIR / "static/open.tex").read_text()
    defs_tex = (SRC_DIR / "static/definitions.tex").read_text()
    pre_tex = (SRC_DIR / "preamble.tex").read_text()
    target = TARGET_MD.read_text()
    proof = PROOF_MD.read_text()

    # Exact verbatim statements in static/open.tex & static/definitions.tex
    assert "We have shown that the systems $\\SRCI[3]$ and $\\SRI[6]$ are stronger than Resolution." in open_tex
    assert "The question of whether systems with smaller constraints are stronger than Resolution is open." in open_tex
    assert "It seems plausible that a separation exists even for $\\SRCII[1]$ and Resolution." in open_tex
    assert "The approach in this lemma cannot be extended to $\\SRCII[1]$" in defs_tex
    assert "Moreover, it is likely that $\\SRCII[1]$ is strictly stronger than Resolution." in defs_tex
    assert "{#1}\\text{-SRC-II}" in pre_tex

    assert "It seems plausible that a separation exists even for $\\SRCII[1]$ and Resolution." in target
    assert "It seems plausible that a separation exists even for $1\\text{-SRC-II}$ and Resolution." in proof

    # Compiled numbering verification in static.tex order
    files = [
        "introduction.tex",
        "definitions.tex",
        "binary-php.tex",
        "tseitin.tex",
        "triangular.tex",
        "types.tex",
        "open.tex",
    ]
    labels_num: dict[str, int] = {}
    env_count = 0
    sec_count = 0
    sec_map: dict[str, int] = {}
    for fn in files:
        txt = (SRC_DIR / "static" / fn).read_text()
        for m in re.finditer(r"\\section\{[^}]*\}\\label\{([^}]+)\}", txt):
            sec_count += 1
            sec_map[m.group(1)] = sec_count
        for m in re.finditer(r"\\begin\{(definition|lemma|theorem|corollary|remark|proposition)\}(?:\[[^\]]*\])?(?:\\label\{([^}]+)\})?", txt):
            env_count += 1
            if m.group(2):
                labels_num[m.group(2)] = env_count

    assert sec_map["sec:definitions"] == 2
    assert sec_map["sec:tseitin-formulas"] == 4
    assert sec_map["sec:open"] == 6
    assert labels_num["thrm:haastad"] == 22
    assert labels_num["cor:Rectangular4"] == 24

    print("[PASS] Primary source arXiv:2606.25895v1 verbatim quotes, macros, & compiled numbering verified.")


# ---------------------------------------------------------------------------
# 2. Lemma 1: Exact Arithmetic, Union Bound, & Concrete Expander Sampling
# ---------------------------------------------------------------------------

def edge_expansion_exact(n: int, edges: list[tuple[int, int]]) -> Fraction:
    """Compute exact min_{|U|<=n//2} |partial(U)|/|U| for simple graph on 0..n-1."""
    adj = [set() for _ in range(n)]
    for u, v in edges:
        assert u != v
        adj[u].add(v)
        adj[v].add(u)
    best: Fraction | None = None
    for mask in range(1, 1 << n):
        sz = mask.bit_count()
        if sz > n // 2:
            continue
        cut = 0
        for u in range(n):
            if (mask >> u) & 1:
                for w in adj[u]:
                    if not ((mask >> w) & 1):
                        cut += 1
        ratio = Fraction(cut, sz)
        if best is None or ratio < best:
            best = ratio
    assert best is not None
    return best


def check_lemma_1() -> None:
    # Exact inequality from PROOF.md L72-73
    assert 3**5 < 2**8
    assert 3**128 < 27 * (2**200) < 2**205
    assert 157464 * (9**64) * (2**8) < 2**247

    # Exact rational union bound sum_{u=1}^{floor(n/2)} p_u < 1 for 2 <= n <= 40
    for n in range(2, 41):
        total_prob = Fraction(0)
        for u in range(1, n // 2 + 1):
            s = u // 8
            t = u + s
            assert t < n
            ratio = Fraction(math.comb(t, u), math.comb(n, u))
            assert ratio <= Fraction(9 * u, 8 * n) ** u
            p_u = Fraction(math.comb(n, u) * math.comb(n - u, s)) * (ratio ** 8)
            assert p_u < Fraction(1, 1 << u)
            total_prob += p_u
        assert total_prob < 1

    # Sample concrete 8-permutation graphs for n = 10, 14, 18 and verify Lemma 1 properties
    rng = random.Random(2606)
    for n in (10, 14, 18):
        found = False
        for _ in range(50):
            edge_set: set[tuple[int, int]] = set()
            verts = list(range(n))
            for _ in range(8):
                perm = list(verts)
                rng.shuffle(perm)
                for v in range(n):
                    w = perm[v]
                    if v != w:
                        a, b = (v, w) if v < w else (w, v)
                        edge_set.add((a, b))
            edges = sorted(edge_set)
            deg = [0] * n
            for a, b in edges:
                deg[a] += 1
                deg[b] += 1
            assert max(deg) <= 16
            exp = edge_expansion_exact(n, edges)
            if exp > Fraction(1, 8):
                assert n <= 2 * len(edges) <= 16 * n
                found = True
                break
        assert found, f"Failed to sample expander at n={n}"

    # Verify arithmetic in Main Theorem L202-203
    assert 48 * 17 == 816
    assert (48**2) * 64 == 147456

    print("[PASS] Lemma 1 exact integer/rational bounds (2<=n<=40) & concrete expanders verified.")


# ---------------------------------------------------------------------------
# 3. Strict Cook-Reckhow 1-SRC-II & Pure Resolution Verifiers
# ---------------------------------------------------------------------------

# Literal representation: nonzero int, positive = var id (1..N), negative = negated var id.
# Clause representation: frozenset[int] without complementary literals.

def clause_from(lits) -> frozenset[int]:
    c = frozenset(lits)
    for x in c:
        assert -x not in c, f"Tautological clause {c}"
    return c


def apply_1sym(clause: frozenset[int], flip_var: int | None) -> frozenset[int]:
    if flip_var is None:
        return clause
    return frozenset((-lit if abs(lit) == flip_var else lit) for lit in clause)


def verify_pure_resolution(phi: set[frozenset[int]], proof: list[tuple[str, object]]) -> None:
    """Strict pure Resolution verifier.

    Each entry is ("input", clause) or ("res", clause, idx1, idx2, pivot_var).
    """
    derived: list[frozenset[int]] = []
    for step in proof:
        kind = step[0]
        if kind == "input":
            _, c = step
            assert isinstance(c, frozenset) and c in phi
            derived.append(c)
        elif kind == "res":
            _, c, i1, i2, piv = step
            assert 0 <= i1 < len(derived) and 0 <= i2 < len(derived)
            assert piv > 0
            c1, c2 = derived[i1], derived[i2]
            if piv in c1 and -piv in c2:
                expected = (c1 - {piv}) | (c2 - {-piv})
            elif -piv in c1 and piv in c2:
                expected = (c1 - {-piv}) | (c2 - {piv})
            else:
                raise AssertionError(f"Invalid pivot {piv} for {c1} and {c2}")
            for lit in expected:
                assert -lit not in expected, "Tautological resolvent"
            assert c == expected
            derived.append(c)
        else:
            raise AssertionError(f"Unknown pure Res step {kind}")
    assert derived and derived[-1] == frozenset(), "Did not derive empty clause"


def verify_1src2(phi: set[frozenset[int]], proof: list[tuple]) -> None:
    """Strict Cook-Reckhow verifier for 1-SRC-II (Gaevoy Definitions 1, 2, 4, 8).

    Step formats:
      ("input", clause)
      ("res", clause, idx1, idx2, pivot_var)
      ("sym", clause, j, flip_var_or_None)
    """
    derived: list[frozenset[int]] = []
    premises: list[frozenset[frozenset[int]]] = []  # L(i) subseteq phi
    derived_set: set[frozenset[int]] = set()

    for step in proof:
        kind = step[0]
        if kind == "input":
            _, c = step
            assert isinstance(c, frozenset) and c in phi
            derived.append(c)
            premises.append(frozenset({c}))
            derived_set.add(c)
        elif kind == "res":
            _, c, i1, i2, piv = step
            assert 0 <= i1 < len(derived) and 0 <= i2 < len(derived)
            assert piv > 0
            c1, c2 = derived[i1], derived[i2]
            if piv in c1 and -piv in c2:
                expected = (c1 - {piv}) | (c2 - {-piv})
            elif -piv in c1 and piv in c2:
                expected = (c1 - {-piv}) | (c2 - {piv})
            else:
                raise AssertionError(f"Invalid pivot {piv} for {c1} and {c2}")
            for lit in expected:
                assert -lit not in expected
            assert c == expected
            derived.append(c)
            premises.append(premises[i1] | premises[i2])
            derived_set.add(c)
        elif kind == "sym":
            _, c, j, flip_var = step
            assert 0 <= j < len(derived)
            if flip_var is not None:
                assert isinstance(flip_var, int) and flip_var > 0
            lj = premises[j]
            assert lj.issubset(phi)
            mapped_lj = frozenset(apply_1sym(b, flip_var) for b in lj)
            # Gaevoy Def 4: all B_i and all phi(B_i) are in phi, and phi(B_i) already derived before this line
            assert mapped_lj.issubset(phi), "Mapped premises not all in input formula Phi"
            assert mapped_lj.issubset(derived_set), "Mapped premises not all previously derived"
            expected = apply_1sym(derived[j], flip_var)
            assert c == expected
            derived.append(c)
            premises.append(mapped_lj)
            derived_set.add(c)
        else:
            raise AssertionError(f"Unknown 1-SRC-II rule {kind}")

    assert derived and derived[-1] == frozenset(), "Did not derive empty clause"


def unfold_1src2_to_res(proof: list[tuple]) -> list[tuple[str, object]]:
    """Independently unfold a 1-SRC-II proof into a pure Resolution proof by replaying derivations."""
    out: list[tuple[str, object]] = []
    # For each step i in proof, store its replayable pure-Res tree as a map from proof index
    # Better: record a recursive derivation node per step i, then emit pure Res with a flip mask!
    nodes: list[tuple] = []
    for step in proof:
        if step[0] == "input":
            nodes.append(("input", step[1]))
        elif step[0] == "res":
            nodes.append(("res", step[1], step[2], step[3], step[4]))
        elif step[0] == "sym":
            nodes.append(("sym", step[2], step[3]))

    memo: dict[tuple[int, frozenset[int]], int] = {}

    def emit(idx: int, flipped: frozenset[int]) -> int:
        key = (idx, flipped)
        if key in memo:
            return memo[key]
        node = nodes[idx]
        if node[0] == "input":
            c = node[1]
            for v in flipped:
                c = apply_1sym(c, v)
            out_idx = len(out)
            out.append(("input", c))
            memo[key] = out_idx
            return out_idx
        elif node[0] == "res":
            _, _, i1, i2, piv = node
            r1 = emit(i1, flipped)
            r2 = emit(i2, flipped)
            c1 = out[r1][1]
            c2 = out[r2][1]
            assert isinstance(c1, frozenset) and isinstance(c2, frozenset)
            c = (c1 - {piv, -piv}) | (c2 - {piv, -piv})
            out_idx = len(out)
            out.append(("res", c, r1, r2, piv))
            memo[key] = out_idx
            return out_idx
        else:
            _, j, fv = node
            new_flipped = flipped ^ ({fv} if fv is not None else frozenset())
            res_idx = emit(j, frozenset(new_flipped))
            memo[key] = res_idx
            return res_idx

    emit(len(nodes) - 1, frozenset())
    return out


def lemma2_restrict_res(pure_proof: list[tuple[str, object]], guard_var: int) -> list[tuple[str, object]]:
    """Implement Lemma 2 restriction rho = {guard_var -> 1} on a pure Resolution refutation."""
    out: list[tuple[str, object]] = []
    # Map original index -> index in restricted proof (if guard_var not in C_i)
    kept: dict[int, int] = {}

    for idx, step in enumerate(pure_proof):
        if step[0] == "input":
            _, c = step
            assert isinstance(c, frozenset)
            if guard_var in c:
                continue
            c_sub = c - {-guard_var}
            kept[idx] = len(out)
            out.append(("input", c_sub))
        else:
            _, c, i1, i2, piv = step
            assert isinstance(c, frozenset)
            if guard_var in c:
                continue
            if piv == guard_var:
                c1 = pure_proof[i1][1]
                c2 = pure_proof[i2][1]
                assert isinstance(c1, frozenset) and isinstance(c2, frozenset)
                if -guard_var in c2:
                    assert i2 in kept
                    kept[idx] = kept[i2]
                else:
                    assert -guard_var in c1 and i1 in kept
                    kept[idx] = kept[i1]
            else:
                assert i1 in kept and i2 in kept
                k1, k2 = kept[i1], kept[i2]
                c1p = out[k1][1]
                c2p = out[k2][1]
                assert isinstance(c1p, frozenset) and isinstance(c2p, frozenset)
                if piv not in c1p and -piv not in c1p:
                    kept[idx] = k1
                elif piv not in c2p and -piv not in c2p:
                    kept[idx] = k2
                else:
                    if piv in c1p and -piv in c2p:
                        new_c = (c1p - {piv}) | (c2p - {-piv})
                    else:
                        new_c = (c1p - {-piv}) | (c2p - {piv})
                    kept[idx] = len(out)
                    out.append(("res", new_c, k1, k2, piv))

    assert out and len(out) <= len(pure_proof)
    return out


# ---------------------------------------------------------------------------
# 4. Theorem 5 Guarded Tseitin Formula & Explicit 1-SRC-II Proof Generator
# ---------------------------------------------------------------------------

def build_guarded_tseitin(n: int, edges: list[tuple[int, int]], alpha: list[int]):
    """Build Ts(G, alpha), All(G), and guarded Ts~(G, alpha).

    Edge variables are 1..m; guard variable g is m + 1.
    """
    m = len(edges)
    g_var = m + 1
    inc: list[list[int]] = [[] for _ in range(n)]
    for eid, (u, v) in enumerate(edges, start=1):
        inc[u].append(eid)
        inc[v].append(eid)

    ts_by_v: list[set[frozenset[int]]] = [set() for _ in range(n)]
    all_by_v: list[set[frozenset[int]]] = [set() for _ in range(n)]
    for v in range(n):
        evars = inc[v]
        d = len(evars)
        for mask in range(1 << d):
            parity = mask.bit_count() & 1
            lits = [(-evars[i] if ((mask >> i) & 1) else evars[i]) for i in range(d)]
            c = clause_from(lits)
            all_by_v[v].add(c)
            if parity != (alpha[v] & 1):
                ts_by_v[v].add(c)

    ts_all = set().union(*ts_by_v)
    phi = set()
    for v in range(n):
        for c in ts_by_v[v]:
            phi.add(c | {-g_var})
        for d_cl in all_by_v[v]:
            phi.add(d_cl | {g_var})
    return g_var, inc, ts_all, phi


def clause_for_assignment(edge_vars: list[int], sigma: dict[int, int], extra_lits=()) -> frozenset[int]:
    lits = [(-e if sigma[e] == 1 else e) for e in edge_vars]
    lits.extend(extra_lits)
    return clause_from(lits)


def construct_theorem5_proof(n: int, edges: list[tuple[int, int]], alpha: list[int]):
    """Construct the exact Theorem 5 1-SRC-II refutation and verify every step."""
    assert sum(alpha) % 2 == 1
    g_var, inc, ts_all, phi = build_guarded_tseitin(n, edges, alpha)
    m = len(edges)
    adj_tree: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    adj_all: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for eid, (u, v) in enumerate(edges, start=1):
        adj_all[u].append((v, eid))
        adj_all[v].append((u, eid))

    # BFS spanning tree rooted at vertex 0
    seen = [False] * n
    seen[0] = True
    q = deque([0])
    order = [0]
    tree_parent: dict[int, tuple[int, int]] = {}
    while q:
        u = q.popleft()
        for w, eid in adj_all[u]:
            if not seen[w]:
                seen[w] = True
                q.append(w)
                order.append(w)
                adj_tree[u].append((w, eid))
                adj_tree[w].append((u, eid))
                tree_parent[w] = (u, eid)
    assert len(order) == n

    proof: list[tuple] = []
    clause_to_idx: dict[frozenset[int], int] = {}

    def add_input(c: frozenset[int]) -> int:
        if c in clause_to_idx:
            return clause_to_idx[c]
        idx = len(proof)
        proof.append(("input", c))
        clause_to_idx[c] = idx
        return idx

    def add_res(c1_idx: int, c2_idx: int, piv: int) -> int:
        c1 = proof[c1_idx][1]
        c2 = proof[c2_idx][1]
        c = (c1 - {piv, -piv}) | (c2 - {piv, -piv})
        idx = len(proof)
        proof.append(("res", c, c1_idx, c2_idx, piv))
        clause_to_idx[c] = idx
        return idx

    def add_sym(j_idx: int, flip_var: int | None) -> int:
        c = apply_1sym(proof[j_idx][1], flip_var)
        idx = len(proof)
        proof.append(("sym", c, j_idx, flip_var))
        clause_to_idx[c] = idx
        return idx

    # Phase 0: input clauses
    for c in sorted(phi, key=lambda cl: (len(cl), sorted(cl))):
        add_input(c)
    phase0_count = len(proof)
    sum_bound_input = sum(3 * (1 << (len(inc[v]) - 1)) for v in range(n))
    assert phase0_count <= sum_bound_input

    def simulate_flip(clause_idx: int, flip_edges: list[int]) -> int:
        if not flip_edges:
            return clause_idx
        cur = add_sym(clause_idx, g_var)
        for f_e in flip_edges:
            cur = add_sym(cur, f_e)
        cur = add_sym(cur, g_var)
        return cur

    def tree_path_edges(u_set: set[int], start: int, goal: int) -> list[int]:
        """Unique path in T[U] between start and goal."""
        par: dict[int, tuple[int, int] | None] = {start: None}
        dq = deque([start])
        while dq:
            cur = dq.popleft()
            if cur == goal:
                break
            for nxt, eid in adj_tree[cur]:
                if nxt in u_set and nxt not in par:
                    par[nxt] = (cur, eid)
                    dq.append(nxt)
        path = []
        cur = goal
        while par[cur] is not None:
            prev, eid = par[cur]  # type: ignore[misc]
            path.append(eid)
            cur = prev
        return path

    # Phase 1: spanning-tree induction
    u_set = {order[0]}
    cut_edges = list(inc[order[0]])
    alpha_u = alpha[order[0]] & 1
    sigma_prev = {e: 0 for e in cut_edges}
    if (sum(sigma_prev.values()) & 1) == alpha_u:
        sigma_prev[cut_edges[0]] ^= 1
    b_idx = clause_to_idx[clause_for_assignment(cut_edges, sigma_prev, (-g_var,))]

    for t_step in range(1, n):
        vt = order[t_step]
        e_t = [e for e in inc[vt] if e in cut_edges]
        ep_t = [e for e in inc[vt] if e not in cut_edges]
        cut_minus = [e for e in cut_edges if e not in e_t]
        new_cut = cut_minus + ep_t
        new_alpha_u = alpha_u ^ (alpha[vt] & 1)

        if new_cut:
            sigma_t = {e: 0 for e in new_cut}
            if (sum(sigma_t.values()) & 1) == new_alpha_u:
                sigma_t[new_cut[0]] ^= 1
        else:
            sigma_t = {}
            assert new_alpha_u == 1  # at t = n, sum(alpha) == 1

        # Build the 2^{|e_t|} clauses for all tau on e_t
        r_t = len(e_t)
        leaves: dict[tuple[int, ...], int] = {}
        for mask in range(1 << r_t):
            tau = {e_t[i]: ((mask >> i) & 1) for i in range(r_t)}
            # Check parity of (sigma_{t,1}, tau) on old cut
            tilde_tau = {e: sigma_t[e] for e in cut_minus}
            tilde_tau.update(tau)
            par_old = sum(tilde_tau.values()) & 1
            if par_old != alpha_u:
                # Case A: simulate flip from sigma_prev -> tilde_tau
                S = [e for e in cut_edges if tilde_tau[e] != sigma_prev[e]]
                assert len(S) % 2 == 0
                deg_s = {u: 0 for u in u_set}
                for e in S:
                    eu, ev = edges[e - 1]
                    if eu in u_set:
                        deg_s[eu] ^= 1
                    if ev in u_set:
                        deg_s[ev] ^= 1
                W = [u for u, d in deg_s.items() if d == 1]
                assert len(W) % 2 == 0
                f1_xor: set[int] = set()
                for i in range(0, len(W), 2):
                    p_edges = tree_path_edges(u_set, W[i], W[i + 1])
                    f1_xor.symmetric_difference_update(p_edges)
                F = S + sorted(f1_xor)
                c_idx = simulate_flip(b_idx, F)
            else:
                # Case B: input clause at vt
                sig_vt = {e: tau[e] for e in e_t}
                for e in ep_t:
                    sig_vt[e] = sigma_t[e]
                c_idx = clause_to_idx[clause_for_assignment(inc[vt], sig_vt, (-g_var,))]
            tau_key = tuple(tau[e] for e in e_t)
            leaves[tau_key] = c_idx

        # Complete binary resolution tree on pivots e_t[0]..e_t[r_t - 1]
        cur_layer = leaves
        for pos in range(r_t):
            piv = e_t[pos]
            next_layer = {}
            for tail_bits in sorted({k[1:] for k in cur_layer}):
                idx0 = cur_layer[(0,) + tail_bits]
                idx1 = cur_layer[(1,) + tail_bits]
                next_layer[tail_bits] = add_res(idx0, idx1, piv)
            cur_layer = next_layer
        assert () in cur_layer
        b_idx = cur_layer[()]
        u_set.add(vt)
        cut_edges = new_cut
        alpha_u = new_alpha_u
        sigma_prev = sigma_t

    assert proof[b_idx][1] == frozenset({-g_var})

    # Phase 2: derive g from All(v_1) | g and resolve with -g
    v0_edges = inc[order[0]]
    d0 = len(v0_edges)
    g_layer = {
        tuple((mask >> i) & 1 for i in range(d0)): clause_to_idx[
            clause_for_assignment(v0_edges, {v0_edges[i]: (mask >> i) & 1 for i in range(d0)}, (g_var,))
        ]
        for mask in range(1 << d0)
    }
    for pos in range(d0):
        piv = v0_edges[pos]
        next_g = {}
        for tail_bits in sorted({k[1:] for k in g_layer}):
            next_g[tail_bits] = add_res(g_layer[(0,) + tail_bits], g_layer[(1,) + tail_bits], piv)
        g_layer = next_g
    g_unit_idx = g_layer[()]
    assert proof[g_unit_idx][1] == frozenset({g_var})
    add_res(g_unit_idx, b_idx, g_var)

    delta = max(len(inc[v]) for v in range(n))
    thm5_bound = (
        sum(3 * (1 << (len(inc[v]) - 1)) for v in range(n))
        + (n - 1) * ((1 << (delta - 1)) * (m + 4) - 1)
        + (1 << delta)
    )
    assert len(proof) <= thm5_bound, f"Proof len {len(proof)} > Theorem 5 bound {thm5_bound}"
    return g_var, ts_all, phi, proof


def check_theorem5_and_lemmas() -> None:
    # Diverse test graphs including K_2 (n=2 edge case!), K_4, K_{3,3}, irregular n=7, Petersen, 3x3 torus, Mobius ladder M_{20}
    graphs = []
    # 1. K_2 (n=2 minimum case)
    graphs.append(("K2", 2, [(0, 1)], [1, 0]))
    # 2. K_4 (n=4, 3-regular)
    graphs.append(("K4", 4, [(i, j) for i in range(4) for j in range(i + 1, 4)], [1, 0, 0, 0]))
    # 3. K_{3,3} (n=6, 3-regular)
    graphs.append(("K3,3", 6, [(i, j) for i in range(3) for j in range(3, 6)], [1, 1, 1, 0, 0, 0]))
    # 4. Irregular graph on n=7 (degrees 1, 2, 3, 4)
    graphs.append(("Irreg7", 7, [(0, 1), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (4, 5), (5, 6), (2, 5), (0, 6)], [0, 0, 1, 0, 0, 0, 0]))
    # 5. Petersen graph (n=10, 3-regular)
    pet_edges = [(i, (i + 1) % 5) for i in range(5)] + [(5 + i, 5 + (i + 2) % 5) for i in range(5)] + [(i, 5 + i) for i in range(5)]
    graphs.append(("Petersen", 10, pet_edges, [1] + [0] * 9))
    # 6. 3x3 toroidal grid H_3 (n=9, 4-regular, all-1 charge)
    h3_edges = []
    for r in range(3):
        for c in range(3):
            u = 3 * r + c
            h3_edges.append((u, 3 * r + (c + 1) % 3))
            h3_edges.append((u, 3 * ((r + 1) % 3) + c))
    graphs.append(("Torus3x3", 9, h3_edges, [1] * 9))
    # 7. Mobius ladder M_{20} (n=20, 3-regular)
    m20_edges = [(i, (i + 1) % 20) for i in range(20)] + [(i, i + 10) for i in range(10)]
    graphs.append(("M20", 20, m20_edges, [1] + [0] * 19))

    for name, n, edges, alpha in graphs:
        g_var, ts_all, phi, proof = construct_theorem5_proof(n, edges, alpha)
        verify_1src2(phi, proof)
        # Unfold + Lemma 2 restriction check on K2, K4, K3,3, Irreg7
        if n <= 7:
            pure = unfold_1src2_to_res(proof)
            verify_pure_resolution(phi, pure)
            res_ts = lemma2_restrict_res(pure, g_var)
            verify_pure_resolution(ts_all, res_ts)

    # Verify Corollary: simulating a global 4-symmetry (4-cycle edge flip) on Torus 3x3 H_3 via 6 local 1-symmetries
    g_var_h3, inc_h3, ts_h3, phi_h3 = build_guarded_tseitin(9, h3_edges, [1] * 9)
    # Pick a 4-cycle on vertices (0,0)-(0,1)-(1,1)-(1,0): find its 4 edge ids
    cycle_pairs = [(0, 1), (1, 4), (4, 3), (3, 0)]
    cycle_eids = []
    for a, b in cycle_pairs:
        for eid, (u, v) in enumerate(h3_edges, start=1):
            if (u, v) == (a, b) or (u, v) == (b, a):
                cycle_eids.append(eid)
                break
    assert len(cycle_eids) == 4
    # Take any clause C | -g in Ts~(H_3), apply phi_g -> phi_e1 -> ... -> phi_e4 -> phi_g, verify every intermediate L(j) in phi_h3
    sample_c = next(iter(ts_h3)) | {-g_var_h3}
    sim_proof = [("input", c) for c in sorted(phi_h3, key=lambda cl: (len(cl), sorted(cl)))]
    idx_map = {step[1]: i for i, step in enumerate(sim_proof)}
    cur_idx = idx_map[sample_c]
    for fv in [g_var_h3] + cycle_eids + [g_var_h3]:
        # Derive negated clause or add dummy resolve? Wait: we just verify every intermediate mapped clause is in phi_h3!
        nxt_c = apply_1sym(sim_proof[cur_idx][1], fv)
        assert nxt_c in phi_h3
        sim_proof.append(("sym", nxt_c, cur_idx, fv))
        cur_idx = len(sim_proof) - 1
    assert cur_idx == len(sim_proof) - 1

    # Verify exact Lemma 3 edge expansion ratios on K4, K3,3, Petersen
    assert edge_expansion_exact(4, graphs[1][2]) == Fraction(2, 1)
    assert edge_expansion_exact(6, graphs[2][2]) == Fraction(5, 3)
    assert edge_expansion_exact(10, graphs[4][2]) == Fraction(1, 1)

    print("[PASS] Strict 1-SRC-II Cook-Reckhow checker, Theorem 5 proofs (K2..M20), Res unfolding + Lemma 2 restriction, H3 4-cycle simulation, & Lemma 3 expansion verified.")


if __name__ == "__main__":
    check_primary_source()
    check_lemma_1()
    check_theorem5_and_lemmas()
    print("PASS")
