#!/usr/bin/env python3
"""Exact finite verification for targets/kern-2611.32927-oolcs-11connected."""
import itertools


def edge(u, v):
    return (u, v) if u < v else (v, u)


def is_connected_ab(n_verts, edges, a, b):
    adj = [[] for _ in range(n_verts)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    vis = {a}
    stack = [a]
    while stack:
        u = stack.pop()
        if u == b:
            return True
        for w in adj[u]:
            if w not in vis:
                vis.add(w)
                stack.append(w)
    return b in vis


def min_weight_perfect_matching_exact(n_aux, aux_edges):
    """Exact integer recursive search for min-weight perfect matching on sparse G* (no floats)."""
    if n_aux % 2 != 0:
        return None
    adj = [[] for _ in range(n_aux)]
    for u, v, wt in aux_edges:
        adj[u].append((v, wt))
        adj[v].append((u, wt))

    # For half-edges and class vertices, degree is 2-3; MRV heuristic makes exact search instant!
    used = [False] * n_aux
    best = None

    def dfs(rem_count, cur_wt):
        nonlocal best
        if best is not None and cur_wt >= best:
            return
        if rem_count == 0:
            best = cur_wt
            return
        # Pick unmatched vertex with fewest available neighbors (MRV)
        u = -1
        u_opts = None
        for i in range(n_aux):
            if not used[i]:
                opts = [(v, wt) for (v, wt) in adj[i] if not used[v]]
                if not opts:
                    return
                if u == -1 or len(opts) < len(u_opts):
                    u = i
                    u_opts = opts
                    if len(u_opts) == 1:
                        break
        used[u] = True
        for v, wt in sorted(u_opts, key=lambda x: x[1]):
            used[v] = True
            dfs(rem_count - 2, cur_wt + wt)
            used[v] = False
        used[u] = False

    dfs(n_aux, 0)
    return best


def solve_via_matching(n_orig, a, b, switches_with_weights):
    """Build G* (with integer doubled edge weights) and compute min-weight perfect matching."""
    # switches_with_weights: list of (positions_list, weights_list), each |pos| <= 1 and connected union
    shift = 0
    edge_records = []  # list of (u, v, cost_int, sw_id)
    for sw_id, (pos_list, wts) in enumerate(switches_with_weights):
        m_s = min(wts)
        shift += m_s
        sh_wts = [w - m_s for w in wts]
        # Verify {1,1}-bounded & connected
        assert len(pos_list) in (1, 2)
        all_e = set().union(*pos_list)
        assert 1 <= len(all_e) <= 2
        if len(pos_list) == 1 or pos_list[0] == pos_list[1]:
            e = next(iter(pos_list[0]))
            edge_records.append((e[0], e[1], 0, sw_id))
        elif any(len(p) == 0 for p in pos_list):
            idx_e = 0 if len(pos_list[0]) == 1 else 1
            e = next(iter(pos_list[idx_e]))
            edge_records.append((e[0], e[1], sh_wts[idx_e], sw_id))
        else:
            e0 = next(iter(pos_list[0]))
            e1 = next(iter(pos_list[1]))
            assert len(set(e0) & set(e1)) >= 1, "Not connected switch!"
            edge_records.append((e0[0], e0[1], sh_wts[0], sw_id))
            edge_records.append((e1[0], e1[1], sh_wts[1], sw_id))

    # Build incident classes per vertex
    classes_at = {v: {} for v in range(n_orig)}
    for eid, (u, v, cost, sw_id) in enumerate(edge_records):
        classes_at[u].setdefault(sw_id, []).append((eid, u, cost))
        classes_at[v].setdefault(sw_id, []).append((eid, v, cost))

    if not classes_at[a] or not classes_at[b]:
        return None

    next_id = 0
    def new_v():
        nonlocal next_id
        vid = next_id
        next_id += 1
        return vid

    aux_edges = []
    half_verts = {}
    for eid, (u, v, cost, sw_id) in enumerate(edge_records):
        hu, hv = new_v(), new_v()
        half_verts[(eid, u)] = hu
        half_verts[(eid, v)] = hv
        aux_edges.append((hu, hv, 0))

    for v in range(n_orig):
        if not classes_at[v]:
            continue
        if v in (a, b):
            hubs = [new_v()]
        else:
            h1, h2 = new_v(), new_v()
            hubs = [h1, h2]
            aux_edges.append((h1, h2, 0))
        for sw_id, items in classes_at[v].items():
            cv, cpv = new_v(), new_v()
            aux_edges.append((cv, cpv, 0))
            for h in hubs:
                aux_edges.append((h, cpv, 0))
            for eid, _, cost in items:
                aux_edges.append((half_verts[(eid, v)], cv, cost))  # 1*cost on each end -> 2*cost total!

    pm_wt = min_weight_perfect_matching_exact(next_id, aux_edges)
    if pm_wt is None:
        return None
    assert pm_wt % 2 == 0
    return shift + pm_wt // 2


def solve_brute_force(n_orig, a, b, switches_with_weights):
    best = None
    choices = [range(len(sw[0])) for sw in switches_with_weights]
    for cfg in itertools.product(*choices):
        edges = set()
        wt = 0
        for i, pos_idx in enumerate(cfg):
            edges |= switches_with_weights[i][0][pos_idx]
            wt += switches_with_weights[i][1][pos_idx]
        if is_connected_ab(n_orig, edges, a, b):
            if best is None or wt < best:
                best = wt
    return best


def verify_all():
    # 1. Non-simple-walk trap:
    # a=0 -> w=1 -> b=2, where s0=({0-1}, {1-2}) forbids 0-1-2 at weight 0!
    # Triangle on w=1, x=3, y=4 of static edges (cost 0) lets a WALK go 0-1-3-4-1-2,
    # while ANY SIMPLE path CANNOT use both edges of s0! Plus an expensive direct backup s1=(empty, {0-2}) of cost 1!
    trap = [
        ([frozenset({edge(0, 1)}), frozenset({edge(1, 2)})], [0, 1]),  # P_3 switch centered at 1
        ([frozenset({edge(1, 3)})], [0]),
        ([frozenset({edge(3, 4)})], [0]),
        ([frozenset({edge(4, 1)})], [0]),
        ([frozenset(), frozenset({edge(0, 2)})], [0, 1]),  # direct pay-1 edge
    ]
    bf1 = solve_brute_force(5, 0, 2, trap)
    mp1 = solve_via_matching(5, 0, 2, trap)
    assert bf1 == mp1 == 1, f"Trap failed: bf={bf1}, mp={mp1}"
    print(f"PASS: Non-simple-walk trap (exact min cost={mp1})")

    # 2. Pure trap without backup -> infeasible (None)!
    trap_infeasible = trap[:-1]
    bf2 = solve_brute_force(5, 0, 2, trap_infeasible)
    mp2 = solve_via_matching(5, 0, 2, trap_infeasible)
    assert bf2 is None and mp2 is None
    print("PASS: Infeasible non-simple-walk trap correctly rejected (None)")

    # 3. Parallel multigraph edges + negative/arbitrary weights + disconnected 0-weight cycle!
    # Vertices 0..5 (a=0, b=3). Disconnected 0-cycle (4-5 via two static edges),
    # plus parallel edges between 1 and 2 from two distinct switches, plus negative weights!
    arb = [
        ([frozenset({edge(0, 1)}), frozenset({edge(1, 2)})], [-3, 5]),   # min=-3 -> cost(0-1)=0, cost(1-2)=8
        ([frozenset({edge(1, 2)}), frozenset({edge(2, 3)})], [2, 4]),    # min=2 -> cost(1-2)=0, cost(2-3)=2
        ([frozenset({edge(2, 3)}), frozenset({edge(1, 3)})], [10, 7]),   # min=7 -> cost(2-3)=3, cost(1-3)=0
        ([frozenset({edge(4, 5)})], [-10]),
        ([frozenset({edge(4, 5)})], [0]),
    ]
    # Note: 0-1 (cost 0 in s0), 1-3 (cost 0 in s2): total shifted = 0, total shift = -3 + 2 + 7 - 10 + 0 = -4!
    bf3 = solve_brute_force(6, 0, 3, arb)
    mp3 = solve_via_matching(6, 0, 3, arb)
    assert bf3 == mp3 == -4, f"Arbitrary weights failed: bf={bf3}, mp={mp3}"
    print(f"PASS: Arbitrary negative weights + parallel multiedges + 0-cycle (opt={mp3})")

    # 4. Random OOLCS stress test (20 instances on 5-6 vertices, 4-5 connected {1,1} switches)
    import random
    rng = random.Random(20261127)
    for t in range(20):
        n = 5
        sws = []
        for _ in range(4):
            kind = rng.randint(0, 3)
            u, v, w = rng.sample(range(n), 3)
            if kind == 0:
                sws.append(([frozenset({edge(u, v)}), frozenset({edge(v, w)})], [0, 1]))
            elif kind == 1:
                sws.append(([frozenset(), frozenset({edge(u, v)})], [0, 1]))
            elif kind == 2:
                sws.append(([frozenset({edge(u, v)}), frozenset()], [0, 1]))
            else:
                sws.append(([frozenset({edge(u, v)}), frozenset({edge(u, v)})], [0, 1]))
        bf = solve_brute_force(n, 0, n - 1, sws)
        mp = solve_via_matching(n, 0, n - 1, sws)
        assert bf == mp, f"Random mismatch on trial {t}: bf={bf}, mp={mp}"
    print("PASS: 20/20 random {1,1}-bounded connected OOLCS instances match brute force")
    return True


if __name__ == "__main__":
    assert verify_all()
    print("OVERALL: PASS")
