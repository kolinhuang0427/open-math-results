#!/usr/bin/env python3
"""Exact finite verification for targets/kern-2611.32927-wlcs-multipartite."""
import itertools


def edge(u, v):
    return (u, v) if u < v else (v, u)


def is_k22(edges, verts):
    """Check that (verts, edges) is isomorphic to K_{2,2}."""
    if len(verts) != 4 or len(edges) != 4:
        return False
    # In K_{2,2}, every vertex has degree 2 and graph is 4-cycle
    deg = {v: 0 for v in verts}
    for u, v in edges:
        if u == v or u not in deg or v not in deg:
            return False
        deg[u] += 1
        deg[v] += 1
    return all(d == 2 for d in deg.values())


def is_ab_connected(n_verts, edges, a, b):
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


def reduce_k2k2_to_k22(switches):
    """Apply Theorem 1 reduction to {1^*}-bounded (K_2+K_2)-shaped switches."""
    reduced = []
    for sw in switches:
        assert len(sw) == 2 and len(sw[0]) == 1 and len(sw[1]) == 1
        (u, v) = next(iter(sw[0]))
        (x, y) = next(iter(sw[1]))
        assert len({u, v, x, y}) == 4
        pos = [
            frozenset({edge(u, v)}),
            frozenset({edge(x, y)}),
            frozenset({edge(u, y)}),
            frozenset({edge(x, v)}),
        ]
        wts = [0, 0, 1, 1]
        union_edges = set().union(*pos)
        assert is_k22(union_edges, {u, v, x, y})
        assert all(len(p) == 1 for p in pos)
        reduced.append((pos, wts))
    return reduced


def verify_instances():
    # Instance 1 (NO for LCS(K_2+K_2), YES if weight-1 K_{2,2} cross-edges were allowed -> tests tight lambda=0!):
    # Vertices 0..7, a=0, b=7.
    # Switch 0: ({0,1}, {4,5}); Switch 1: ({1,4}, {5,7}) -- no path from 0 to 7 without using 2 edges of same switch?
    # Actually test Switch 0: ({0,1}, {2,3}), Switch 1: ({1,2}, {3,7})!
    # In LCS: 0->1 needs sw0=0, 1->2 needs sw1=0, 2->3 needs sw0=1 (CONFLICT with sw0=0!), 3->7 needs sw1=1!
    # With K_{2,2} cross-edges (at lambda=1): sw0 could pick {0,3}, sw1 picks {3,7} -> 0-3-7!
    no_inst = [
        (frozenset({edge(0, 1)}), frozenset({edge(2, 3)})),
        (frozenset({edge(1, 2)}), frozenset({edge(3, 7)})),
    ]
    # Instance 2 (YES for LCS(K_2+K_2)):
    # Switch 0: ({0,1}, {4,5}), Switch 1: ({1,7}, {2,3}) -> 0-1-7 using sw0=0, sw1=0!
    yes_inst = [
        (frozenset({edge(0, 1)}), frozenset({edge(4, 5)})),
        (frozenset({edge(1, 7)}), frozenset({edge(2, 3)})),
    ]
    # Instance 3 (3-switch chain NO vs YES)
    no_inst3 = [
        (frozenset({edge(0, 1)}), frozenset({edge(4, 5)})),
        (frozenset({edge(1, 4)}), frozenset({edge(5, 6)})),
        (frozenset({edge(6, 7)}), frozenset({edge(2, 3)})),
    ]

    for name, sws, expected in [
        ("conflict-NO", no_inst, False),
        ("chain-YES", yes_inst, True),
        ("3-switch-NO", no_inst3, False),
    ]:
        n = 8
        a, b = 0, 7
        lcs_ans = any(
            is_ab_connected(n, set().union(*(sws[i][cfg[i]] for i in range(len(sws)))), a, b)
            for cfg in itertools.product([0, 1], repeat=len(sws))
        )
        assert lcs_ans == expected

        red = reduce_k2k2_to_k22(sws)
        wlcs_ans = any(
            sum(red[i][1][cfg[i]] for i in range(len(red))) <= 0
            and is_ab_connected(n, set().union(*(red[i][0][cfg[i]] for i in range(len(red)))), a, b)
            for cfg in itertools.product(range(4), repeat=len(red))
        )
        assert wlcs_ans == lcs_ans, f"Mismatch on {name}: {wlcs_ans} vs {lcs_ans}"
        print(f"PASS: {name}: LCS={lcs_ans}, WLCS(K_{{2,2}}, lambda=0)={wlcs_ans}")

    return True


if __name__ == "__main__":
    assert verify_instances()
    print("OVERALL: PASS")
