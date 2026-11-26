"""Independent exact-arithmetic verifier for Conjecture 1.8 of arXiv:2511.16335v1.

Strictly derived from Definition 1.2, Definition 1.5, Conjecture 1.8, and the
CCR-Z propagation rules in NewFixedPropTime.tex (arXiv:2511.16335v1, Section 1),
checked against the explicit construction in COUNTEREXAMPLE.md.
"""

from __future__ import annotations

import signal
import sys
import time


class TimeoutError(Exception):
    pass


def _alarm_handler(signum, frame):
    raise TimeoutError("Verification exceeded built-in time limit")


def is_connected(n: int, adj: list[set[int]]) -> bool:
    if n == 0:
        return False
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == n


def complement_adj(n: int, adj: list[set[int]]) -> list[set[int]]:
    all_v = set(range(n))
    return [all_v - adj[u] - {u} for u in range(n)]


def is_complete_graph(n: int, adj: list[set[int]]) -> bool:
    return all(len(adj[u]) == n - 1 for u in range(n))


def is_standard_fast_join(n: int, adj: list[set[int]]) -> bool:
    """Check Definition 1.5 of arXiv:2511.16335v1.

    A graph G of order n >= 2 is a standard fast join iff G is K_n or
    G = join_{i=1}^t G_i (t >= 2) where each G_i is n_i K_1 or K_{n_i} U K_{m_i} (n_i, m_i >= 2).
    In particular, any nontrivial join (t >= 2 nonempty parts) has disconnected complement.
    We check the exact complement decomposition directly.
    """
    if n < 2:
        return False
    if is_complete_graph(n, adj):
        return True
    c_adj = complement_adj(n, adj)
    # Find connected components of complement(G)
    unvisited = set(range(n))
    comps: list[list[int]] = []
    while unvisited:
        start = min(unvisited)
        comp = []
        stack = [start]
        unvisited.remove(start)
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in c_adj[u]:
                if v in unvisited:
                    unvisited.remove(v)
                    stack.append(v)
        comps.append(comp)
    if len(comps) < 2:
        return False
    # Each component of complement(G) must be K_{n_i} or K_{n_i, m_i} with n_i, m_i >= 2
    for comp in comps:
        k = len(comp)
        comp_set = set(comp)
        degs = [len(c_adj[u] & comp_set) for u in comp]
        if all(d == k - 1 for d in degs):
            # Complement is K_k -> G_i is k K_1
            continue
        # Otherwise check if complement is complete bipartite K_{a, b} with a, b >= 2
        u0 = comp[0]
        part_b = c_adj[u0] & comp_set
        part_a = comp_set - part_b
        if len(part_a) < 2 or len(part_b) < 2:
            return False
        ok = all((c_adj[u] & comp_set) == part_b for u in part_a) and all(
            (c_adj[v] & comp_set) == part_a for v in part_b
        )
        if not ok:
            return False
    return True


def propagate_standard(n: int, adj_masks: list[int], initial_mask: int) -> tuple[bool, int]:
    """Run CCR-Z exactly per Section 1 (lines 312, 319-326) of arXiv:2511.16335v1.

    Returns (is_forcing_set, propagation_time).
    """
    full_mask = (1 << n) - 1
    blue = initial_mask
    rounds = 0
    while True:
        white = full_mask ^ blue
        if white == 0:
            return True, rounds
        newly_forced = 0
        # Simultaneous forces by all currently blue vertices
        temp = blue
        while temp:
            lsb = temp & -temp
            u = lsb.bit_length() - 1
            temp ^= lsb
            white_nbrs = adj_masks[u] & white
            if white_nbrs != 0 and (white_nbrs & (white_nbrs - 1)) == 0:
                newly_forced |= white_nbrs
        if newly_forced == 0:
            return False, -1
        rounds += 1
        blue |= newly_forced


def exhaustive_pt_analysis(n: int, adj: list[set[int]]) -> dict:
    adj_masks = [0] * n
    for u in range(n):
        m = 0
        for v in adj[u]:
            m |= 1 << v
        adj_masks[u] = m

    forcing_pts: dict[int, int] = {}
    proper_forcing_pts: list[int] = []
    full_mask = (1 << n) - 1
    for mask in range(1 << n):
        ok, pt = propagate_standard(n, adj_masks, mask)
        if ok:
            forcing_pts[mask] = pt
            if mask != full_mask:
                proper_forcing_pts.append(pt)

    # Filter to minimal forcing sets (no proper subset is forcing)
    minimal_masks: list[int] = []
    by_size: dict[int, list[int]] = {}
    for mask in forcing_pts:
        by_size.setdefault(mask.bit_count(), []).append(mask)

    all_forcing_sorted = sorted(forcing_pts.keys(), key=lambda m: m.bit_count())
    for mask in all_forcing_sorted:
        is_minimal = True
        for prev in minimal_masks:
            if (prev & mask) == prev:
                is_minimal = False
                break
        if is_minimal:
            minimal_masks.append(mask)

    minimal_sizes = [m.bit_count() for m in minimal_masks]
    minimal_pts = [forcing_pts[m] for m in minimal_masks]

    return {
        "n": n,
        "num_forcing": len(forcing_pts),
        "num_minimal": len(minimal_masks),
        "Z": min(minimal_sizes),
        "Zbar": max(minimal_sizes),
        "pt_ul": min(minimal_pts),
        "pt_bar": max(minimal_pts),
        "proper_forcing_pts": set(proper_forcing_pts),
    }


def build_circulant(n: int, jumps: list[int]) -> list[set[int]]:
    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in jumps:
            u = (i + j) % n
            v = (i - j) % n
            if u != i:
                adj[i].add(u)
            if v != i:
                adj[i].add(v)
    return adj


def build_c6_blowup(sizes: list[int]) -> list[set[int]]:
    assert len(sizes) == 6
    parts: list[list[int]] = []
    cur = 0
    for r in sizes:
        assert r >= 1
        parts.append(list(range(cur, cur + r)))
        cur += r
    n = cur
    adj = [set() for _ in range(n)]
    for i in range(6):
        nxt = (i + 1) % 6
        for u in parts[i]:
            for v in parts[nxt]:
                adj[u].add(v)
                adj[v].add(u)
    return adj


def main() -> int:
    signal.signal(signal.SIGALRM, _alarm_handler)
    signal.alarm(30)
    t0 = time.monotonic()

    # 1. Explicit smallest witness: Circ(12, {1, 5}) and C_6[2K_1]
    g_circ = build_circulant(12, [1, 5])
    # Map A_i = {i, i+6} -> in build_c6_blowup([2]*6), part i is {2i, 2i+1}.
    # Check exact equality with explicit vertex labeling from COUNTEREXAMPLE.md:
    # A_i = {i, i+6} for i in Z/6Z
    g_lex_explicit = [set() for _ in range(12)]
    for i in range(6):
        ai = [i, i + 6]
        anext = [(i + 1) % 6, ((i + 1) % 6) + 6]
        for u in ai:
            for v in anext:
                g_lex_explicit[u].add(v)
                g_lex_explicit[v].add(u)

    if g_circ != g_lex_explicit:
        print("FAIL: Circ(12, {1, 5}) does not match explicit C_6[2K_1] edge set")
        return 1

    edge_count = sum(len(s) for s in g_circ) // 2
    assert edge_count == 24, f"Expected 24 edges, got {edge_count}"
    assert all(len(s) == 4 for s in g_circ), "Expected 4-regular"
    # Verify bipartiteness: evens vs odds
    for u in range(12):
        for v in g_circ[u]:
            assert (u % 2) != (v % 2), "Expected bipartite"

    if not is_connected(12, g_circ):
        print("FAIL: G is not connected")
        return 1

    if is_standard_fast_join(12, g_circ):
        print("FAIL: G IS a standard fast join")
        return 1

    c_adj = complement_adj(12, g_circ)
    if not is_connected(12, c_adj):
        print("FAIL: complement(G) is disconnected")
        return 1

    stats12 = exhaustive_pt_analysis(12, g_circ)
    print(f"Circ(12, {{1, 5}}): {stats12}")
    if stats12["pt_bar"] != 1 or stats12["pt_ul"] != 1:
        print("FAIL: PTbar != 1 on Circ(12, {1, 5})")
        return 1
    if stats12["Z"] != 8 or stats12["Zbar"] != 8 or stats12["num_minimal"] != 144:
        print("FAIL: Z, Zbar, or minimal count mismatch on Circ(12, {1, 5})")
        return 1
    if stats12["proper_forcing_pts"] != {1}:
        print("FAIL: Not all proper forcing sets have pt=1")
        return 1

    # 2. Exhaustive tests on several asymmetric blowups C_6[r_0 K_1, ..., r_5 K_1]
    test_tuples = [
        [2, 2, 2, 2, 2, 2],
        [3, 2, 2, 2, 2, 2],
        [2, 3, 2, 3, 2, 2],
        [3, 2, 3, 2, 2, 2],
        [4, 2, 2, 2, 2, 2],
        [3, 3, 2, 3, 2, 2],
    ]
    for sizes in test_tuples:
        n = sum(sizes)
        g = build_c6_blowup(sizes)
        assert is_connected(n, g), f"Not connected for {sizes}"
        assert not is_standard_fast_join(n, g), f"Fast join for {sizes}"
        assert is_connected(n, complement_adj(n, g)), f"Disconnected complement for {sizes}"
        st = exhaustive_pt_analysis(n, g)
        print(f"C_6{sizes} (n={n}): Z={st['Z']}, Zbar={st['Zbar']}, pt_ul={st['pt_ul']}, pt_bar={st['pt_bar']}, num_min={st['num_minimal']}")
        assert st["pt_bar"] == 1 and st["pt_ul"] == 1
        assert st["Z"] == n - 4 and st["Zbar"] == n - 4
        assert st["proper_forcing_pts"] == {1}

    elapsed = time.monotonic() - t0
    print(f"PASS (all checks passed in {elapsed:.3f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
