"""Independent exact-arithmetic verifier for targets/kern-2611.32927-oolcs-11connected."""

from __future__ import annotations

import itertools
import pathlib
import random
import re
import tarfile
from collections import deque


def is_connected_ab(num_vertices: int, edges: list[tuple[int, int]], a: int, b: int) -> bool:
    if a == b:
        return True
    adj: list[list[int]] = [[] for _ in range(num_vertices)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = [False] * num_vertices
    seen[a] = True
    q = deque([a])
    while q:
        cur = q.popleft()
        if cur == b:
            return True
        for nxt in adj[cur]:
            if not seen[nxt]:
                seen[nxt] = True
                q.append(nxt)
    return False


def is_connected_graph(edges: list[tuple[int, int]]) -> bool:
    if not edges:
        return False
    verts = sorted({u for e in edges for u in e})
    adj: dict[int, list[int]] = {v: [] for v in verts}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = {verts[0]}
    q = deque([verts[0]])
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return len(seen) == len(verts)


def solve_wlcs_bruteforce(
    num_vertices: int,
    switches: list[list[list[tuple[int, int]]]],
    weights: list[list[int]],
    a: int,
    b: int,
) -> int | None:
    """Exact minimum total weight of a connecting configuration (None if impossible)."""
    best: int | None = None
    ranges = [range(len(sw)) for sw in switches]
    for cfg in itertools.product(*ranges):
        edges: list[tuple[int, int]] = []
        w_sum = 0
        for sw, wt, idx in zip(switches, weights, cfg):
            edges.extend(sw[idx])
            w_sum += wt[idx]
        if is_connected_ab(num_vertices, edges, a, b):
            if best is None or w_sum < best:
                best = w_sum
    return best


def build_auxiliary_g_star(
    num_vertices: int,
    switches: list[list[list[tuple[int, int]]]],
    weights: list[list[int]],
    a: int,
    b: int,
) -> tuple[int, int, list[list[tuple[int, int]]], int] | None:
    """Construct G* with doubled integer edge weights; return (shift_sum, n_star, adj, edge_count) or None."""
    shift_sum = 0
    multigraph_edges: list[tuple[int, int, int, int]] = []  # (u, v, sw_id, cost)

    for s_id, (sw, wt) in enumerate(zip(switches, weights)):
        assert 1 <= len(sw) <= 2
        assert all(len(pos) <= 1 for pos in sw)
        all_edges = [tuple(sorted(pos[0])) for pos in sw if len(pos) == 1]
        assert is_connected_graph(all_edges), f"Switch {s_id} is not connected: {sw}"

        m_s = min(wt)
        shift_sum += m_s
        shifted = [x - m_s for x in wt]
        distinct = sorted(set(all_edges))

        if len(distinct) == 1:
            e = distinct[0]
            min_e_cost = min(
                shifted[i] for i, pos in enumerate(sw) if len(pos) == 1 and tuple(sorted(pos[0])) == e
            )
            multigraph_edges.append((e[0], e[1], s_id, min_e_cost))
        elif len(distinct) == 2:
            assert len(sw) == 2
            e0 = tuple(sorted(sw[0][0]))
            e1 = tuple(sorted(sw[1][0]))
            assert len(set(e0) & set(e1)) == 1
            multigraph_edges.append((e0[0], e0[1], s_id, shifted[0]))
            multigraph_edges.append((e1[0], e1[1], s_id, shifted[1]))
        else:
            raise AssertionError("Unreachable for {1,1}-bounded switches")

    # Check active vertices
    incident_by_v_s: dict[tuple[int, int], list[int]] = {}
    active_verts = set()
    for e_idx, (u, v, s_id, _) in enumerate(multigraph_edges):
        active_verts.add(u)
        active_verts.add(v)
        incident_by_v_s.setdefault((u, s_id), []).append(e_idx)
        incident_by_v_s.setdefault((v, s_id), []).append(e_idx)

    if a not in active_verts or b not in active_verts:
        return None

    classes_at_v: dict[int, list[int]] = {v: [] for v in active_verts}
    for v, s_id in sorted(incident_by_v_s):
        classes_at_v[v].append(s_id)

    adj: list[list[tuple[int, int]]] = []

    def new_node() -> int:
        adj.append([])
        return len(adj) - 1

    edge_count = 0

    def add_edge(x: int, y: int, w: int) -> None:
        nonlocal edge_count
        adj[x].append((y, w))
        adj[y].append((x, w))
        edge_count += 1

    half_nodes: dict[tuple[int, int], int] = {}
    for e_idx, (u, v, _, _) in enumerate(multigraph_edges):
        hu = new_node()
        hv = new_node()
        half_nodes[(e_idx, u)] = hu
        half_nodes[(e_idx, v)] = hv
        add_edge(hu, hv, 0)

    for v in sorted(active_verts):
        if v in (a, b):
            hubs = [new_node()]
        else:
            h1, h2 = new_node(), new_node()
            add_edge(h1, h2, 0)
            hubs = [h1, h2]

        for s_id in classes_at_v[v]:
            c_node = new_node()
            c_prime = new_node()
            add_edge(c_node, c_prime, 0)
            for h in hubs:
                add_edge(h, c_prime, 0)
            for e_idx in incident_by_v_s[(v, s_id)]:
                cost = multigraph_edges[e_idx][3]
                add_edge(half_nodes[(e_idx, v)], c_node, cost)

    return shift_sum, len(adj), adj, edge_count


def exact_mwpm_small(n_star: int, adj: list[list[tuple[int, int]]]) -> int | None:
    """Exact minimum-weight perfect matching via memoized bitmask DP."""
    assert n_star % 2 == 0
    full_mask = (1 << n_star) - 1
    memo: dict[int, int | None] = {full_mask: 0}

    def solve(mask: int) -> int | None:
        if mask in memo:
            return memo[mask]
        # Pick lowest unmatched vertex (or min-degree unmatched vertex to prune)
        best_u = -1
        best_deg = 10**9
        rem = (~mask) & full_mask
        tmp = rem
        while tmp:
            lsb = tmp & -tmp
            u = lsb.bit_length() - 1
            deg = sum(1 for v, _ in adj[u] if not (mask & (1 << v)))
            if deg == 0:
                memo[mask] = None
                return None
            if deg < best_deg:
                best_deg = deg
                best_u = u
                if deg == 1:
                    break
            tmp ^= lsb

        ans: int | None = None
        m_u = mask | (1 << best_u)
        for v, w in adj[best_u]:
            if m_u & (1 << v):
                continue
            sub = solve(m_u | (1 << v))
            if sub is not None:
                cand = w + sub
                if ans is None or cand < ans:
                    ans = cand
        memo[mask] = ans
        return ans

    return solve(0)


def verify_adversarial_and_random() -> list[str]:
    failures: list[str] = []

    # 1. Explicit size-bound test: a-x and x-b as two single-edge switches (n=3, m=2)
    sw_size = [[[(0, 1)]], [[(1, 2)]]]
    wt_size = [[0], [0]]
    built_sz = build_auxiliary_g_star(3, sw_size, wt_size, 0, 2)
    assert built_sz is not None
    _, v_star_sz, _, e_star_sz = built_sz
    print(f"SIZE_WITNESS (n=3, m=2): |V*|={v_star_sz}, |E*|={e_star_sz}")

    # 2. Non-simple-walk trap (a=0, x=1, y=2, z=3, b=4):
    # Static 0-1 (cost 0), P3 at 1: {1-2 (cost 0), 1-3 (cost 0)}?
    # Better: P3 center at 1 forbids 0-1 -> 1-4; 0-weight triangle 1-2-3 lets a non-simple walk loop 0-1-2-3-1-4,
    # whereas simple path needs cost-1 edge 0-4!
    trap_sw = [
        [[(0, 1)], [(1, 4)]],  # P3 center 1, weights 0, 0
        [[(1, 2)]],            # static cost 0
        [[(2, 3)]],            # static cost 0
        [[(3, 1)]],            # static cost 0
        [[], [(0, 4)]],        # optional edge cost 5
    ]
    trap_wt = [[0, 0], [0], [0], [0], [0, 5]]
    bf_trap = solve_wlcs_bruteforce(5, trap_sw, trap_wt, 0, 4)
    built_trap = build_auxiliary_g_star(5, trap_sw, trap_wt, 0, 4)
    assert built_trap is not None
    sh_trap, n_trap, adj_trap, _ = built_trap
    mw_trap = exact_mwpm_small(n_trap, adj_trap)
    assert mw_trap is not None and mw_trap % 2 == 0
    gstar_trap = sh_trap + (mw_trap // 2)
    if bf_trap != 5 or gstar_trap != 5:
        failures.append(f"Non-simple-walk trap mismatch: bf={bf_trap}, gstar={gstar_trap}, expected=5")

    # 3. Random suite of {1,1}-bounded connected switches with negative/positive weights,
    # parallel multigraph edges, redundant positions, empty positions, and disconnected components
    rng = random.Random(261132927)
    checked = 0
    yes_cases = 0
    no_cases = 0
    for trial in range(40):
        n = rng.randint(4, 6)
        m_sw = rng.randint(2, 4)
        switches: list[list[list[tuple[int, int]]]] = []
        weights: list[list[int]] = []
        for _ in range(m_sw):
            kind = rng.randint(0, 3)
            if kind == 0:
                # Static single edge
                u, v = rng.sample(range(n), 2)
                switches.append([[(u, v)]])
                weights.append([rng.randint(-3, 5)])
            elif kind == 1:
                # Single edge or empty
                u, v = rng.sample(range(n), 2)
                switches.append([[], [(u, v)]])
                weights.append([rng.randint(-2, 4), rng.randint(-2, 4)])
            elif kind == 2:
                # Redundant duplicate edge
                u, v = rng.sample(range(n), 2)
                switches.append([[(u, v)], [(u, v)]])
                weights.append([rng.randint(-3, 4), rng.randint(-3, 4)])
            else:
                # P3 switch
                z, u, v = rng.sample(range(n), 3)
                switches.append([[(u, z)], [(z, v)]])
                weights.append([rng.randint(-3, 5), rng.randint(-3, 5)])

        a, b = rng.sample(range(n), 2)
        bf = solve_wlcs_bruteforce(n, switches, weights, a, b)
        built = build_auxiliary_g_star(n, switches, weights, a, b)
        if built is None:
            gstar = None
        else:
            sh, n_star, adj, _ = built
            mw = exact_mwpm_small(n_star, adj)
            if mw is None:
                gstar = None
            else:
                assert mw % 2 == 0
                gstar = sh + (mw // 2)
        if bf != gstar:
            failures.append(f"Trial {trial}: bf={bf} != gstar={gstar}")
        if bf is None:
            no_cases += 1
        else:
            yes_cases += 1
        checked += 1

    print(f"WLCS_11CONNECTED_EXACT: checked={checked}, yes={yes_cases}, no={no_cases}, trap={gstar_trap}")
    return failures


def verify_docs() -> list[str]:
    failures: list[str] = []
    root = pathlib.Path(__file__).resolve().parents[3]
    tar_path = root / "tools" / ".arxiv_cache" / "eprint" / "2611.32927.src"
    target_md = (
        root / "targets" / "kern-2611.32927-oolcs-11connected" / "TARGET.md"
    ).read_text(encoding="utf-8")
    proof_md = (
        root / "targets" / "kern-2611.32927-oolcs-11connected" / "PROOF.md"
    ).read_text(encoding="utf-8")

    if not tar_path.exists():
        print("[SKIP] local tools/.arxiv_cache not present; skipping TeX numbering check")
    else:
        with tarfile.open(tar_path, "r:*") as tf:
            main_tex = tf.extractfile("main-arxiv.tex").read().decode("utf-8")
            inputs = re.findall(r"\\input\{(sections/[^}]+)\}", main_tex)
            section_files = [
                rel for rel in inputs
                if re.search(r"\\section\{", tf.extractfile(rel).read().decode("utf-8"))
            ]
        conclusion_idx = section_files.index("sections/conclusion.tex") + 1
        if f"Section {conclusion_idx}" not in target_md:
            failures.append(
                f"TARGET.md section mismatch: sections/conclusion.tex is Section {conclusion_idx} "
                f"(sections={section_files}), but TARGET.md cites Section 6"
            )

    # Check Theorem 1 size bounds in PROOF.md L7 & L54 match |V*| <= 2n + 6m, |E*| <= 9m + n
    if "2n + 4m" in proof_md or "5m + n" in proof_md:
        failures.append(
            "PROOF.md still states outdated bounds 2n + 4m / 5m + n"
        )
    if "2n + 6m" not in proof_md or "9m + n" not in proof_md:
        failures.append(
            "PROOF.md missing corrected size bounds 2n + 6m and 9m + n"
        )

    if "Wait: note that" in proof_md:
        failures.append("PROOF.md L25 contains conversational draft text ('Wait: note that')")

    if r"W^*(e_v c_{v,s}) = \frac{1}{2} c(e)" not in proof_md:
        failures.append(
            "PROOF.md L41 missing half-edge weight W^*(e_v c_{v,s}) = \\frac{1}{2} c(e)"
        )

    return failures


def main() -> int:
    failures = verify_adversarial_and_random() + verify_docs()
    if failures:
        for msg in failures:
            print(f"ERROR: {msg}")
        print("FAIL")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
