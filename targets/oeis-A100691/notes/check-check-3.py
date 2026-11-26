"""Independent exact verifier for targets/oeis-A100691/.

Written strictly from the OEIS A100691 / A193641 primary definitions and PROOF.md,
without reading the author's verify.py.
Uses exact integer / rational / symbolic arithmetic (SymPy).
"""

from __future__ import annotations

from itertools import product
import sympy as sp


# Exact OEIS DATA lists from A100691 (rev 11) and A193641 (rev 48)
OEIS_A100691 = [
    1, 4, 12, 30, 70, 158, 352, 780, 1724, 3806, 8398, 18526, 40864, 90132, 198796,
]
OEIS_A193641 = [
    1, 1, 3, 7, 15, 33, 73, 161, 355, 783, 1727, 3809, 8401, 18529, 40867, 90135, 198799,
]


def check_part1_a193641() -> None:
    """Verify A193641 brute-force counts, U/V/W transitions, and equivalence with a_OEIS."""
    U_counts = []
    V_counts = []
    W_counts = []
    b_counts = []

    for n in range(0, 11):
        u_cnt = v_cnt = w_cnt = 0
        for arr in product((-1, 0, 1), repeat=n):
            covered = [False] * n
            for i in range(n):
                if arr[i] == 0:
                    covered[i] = True
                if i + 1 < n and arr[i] + arr[i + 1] == 0:
                    covered[i] = True
                    covered[i + 1] = True
            if all(covered):
                if n == 0 or arr[-1] == 0:
                    u_cnt += 1
                else:
                    v_cnt += 1
            elif n >= 1 and all(covered[:-1]) and arr[-1] in (-1, 1):
                w_cnt += 1
        U_counts.append(u_cnt)
        V_counts.append(v_cnt)
        W_counts.append(w_cnt)
        b_counts.append(u_cnt + v_cnt)

    # Check against OEIS A193641 data
    assert b_counts == OEIS_A193641[:11], f"A193641 mismatch: {b_counts}"

    # Check U, V, W transitions from PROOF.md
    assert (U_counts[0], V_counts[0], W_counts[0]) == (1, 0, 0)
    assert (U_counts[1], V_counts[1], W_counts[1]) == (1, 0, 2)
    for n in range(10):
        assert U_counts[n + 1] == U_counts[n] + V_counts[n] == b_counts[n]
        assert W_counts[n + 1] == 2 * U_counts[n] + V_counts[n]
        assert V_counts[n + 1] == V_counts[n] + W_counts[n]
    for m in range(3, 11):
        assert b_counts[m] == 2 * b_counts[m - 1] + b_counts[m - 3]

    # Symbolic verification of G_OEIS(z) vs A193641(n+2)-3
    z = sp.Symbol("z")
    G_oeis = sp.simplify((1 + z**2) * (1 + z + z**2) / ((1 - z) * (1 - 2 * z - z**3)))
    G_alt = sp.simplify(1 + 2 * (2 + z**2) / ((z - 1) * (z**2 + 2 * z - 1)))
    assert sp.simplify(G_oeis - G_alt) != 0  # Typo noted in PROOF.md line 17

    # Check (1 - 2z - z^3) * G_oeis(z)
    lhs = sp.series((1 - 2 * z - z**3) * G_oeis, z, 0, 16)
    rhs = sp.series(1 + 2 * z + 4 * z**2 + 5 * z**3 + 6 * z**4 / (1 - z), z, 0, 16)
    assert sp.simplify(lhs.removeO() - rhs.removeO()) == 0
    assert sp.simplify((1 - 2 * z - z**3) * G_oeis - (1 + 2 * z + 4 * z**2 + 5 * z**3 + 6 * z**4 / (1 - z))) == 0

    coeffs_oeis = [int(G_oeis.series(z, 0, 15).coeff(z, k)) for k in range(15)]
    assert coeffs_oeis == OEIS_A100691
    for n in range(1, 15):
        assert coeffs_oeis[n] == OEIS_A193641[n + 2] - 3

    print("Part 1 PASS: A193641 brute-force (n<=10), U/V/W transitions, and a_OEIS(n)=A193641(n+2)-3 verified.")


def dfs_saw_counts(max_n: int, start=(0, 0)) -> list[int]:
    """Pure brute-force DFS counting n-step self-avoiding walks on Z x {0, 1}."""
    counts = [0] * (max_n + 1)

    def neighbors(x: int, y: int):
        if y == 0:
            return ((x - 1, 0), (x + 1, 0), (x, 1), (x - 1, 1))
        return ((x - 1, 1), (x + 1, 1), (x, 0), (x + 1, 0))

    visited = {start}

    def dfs(vx: int, vy: int, steps: int) -> None:
        counts[steps] += 1
        if steps == max_n:
            return
        for nx, ny in neighbors(vx, vy):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                dfs(nx, ny, steps + 1)
                visited.remove((nx, ny))

    dfs(start[0], start[1], 0)
    return counts


def transfer_matrix_saw_gf():
    """Independent column transfer automaton over Q(z) for simple paths starting at (0,0).

    Across cut x (between column x-1 and column x), cut edges are:
      0: (x-1, 0) -- (x, 0)
      1: (x-1, 1) -- (x, 0)
      2: (x-1, 1) -- (x, 1)

    State before processing column x:
      (phase, end_count, pairs, singles)
      - phase in {'pre', 'post'} where 'pre' means x <= 0 (origin (0,0) not yet passed),
        'post' means x > 0 (origin (0,0) already passed).
      - end_count in {0, 1, 2}: number of path endpoints strictly to the left of column x.
      - pairs: tuple of sorted 2-tuples of cut-edge indices (connected to each other to the left).
      - singles: sorted tuple of cut-edge indices (each connected to an endpoint to the left).
    Note: Since only simple path subgraphs with endpoints {s, t} (s != t) are valid,
    when end_count == 2 and pairs == () and singles == (), the path is complete!
    """
    # Let's represent cut state as canonical tuple:
    # (end_count, pairs, singles)
    # where all elements of pairs and singles are distinct subsets/indices in {0, 1, 2}.
    def step_column(state, is_origin_col: bool):
        """Return dict mapping (next_state, added_edges_count) -> multiplicity (1)."""
        end_count, pairs, singles = state
        # If path already finished (2 endpoints left of cut, no active cut edges),
        # can only stay empty in all subsequent columns without adding edges.
        if end_count == 2 and not pairs and not singles:
            if is_origin_col:
                return []
            return [((2, (), ()), 0)]

        # Left cut edges touching (x, 0) are {0, 1}; touching (x, 1) is {2}.
        # Internal vertical edge v: {(x,0), (x,1)}.
        # Right cut edges: R0 = {(x,0), (x+1,0)}, R1 = {(x,1), (x+1,0)}, R2 = {(x,1), (x+1,1)}.
        # In the state AFTER column x, R0 has index 0, R1 has index 1, R2 has index 2.
        results = []

        for use_v in (0, 1):
            for r0 in (0, 1):
                for r1 in (0, 1):
                    for r2 in (0, 1):
                        # Degree of (x,0) and (x,1) in column x:
                        # Left incidences: (x,0) gets L0, L1; (x,1) gets L2
                        left_used = set(singles)
                        for a, b in pairs:
                            left_used.add(a)
                            left_used.add(b)
                        l0 = 1 if 0 in left_used else 0
                        l1 = 1 if 1 in left_used else 0
                        l2 = 1 if 2 in left_used else 0

                        deg0 = l0 + l1 + use_v + r0
                        deg1 = l2 + use_v + r1 + r2

                        # Determine valid endpoint placement at (x,0) and (x,1)
                        # Origin column requires (0,0) to be an endpoint (degree 1).
                        if deg0 > 2 or deg1 > 2:
                            continue
                        if is_origin_col and deg0 != 1:
                            continue

                        # Endpoints in column x:
                        # For (x,0): degree 1 means endpoint, degree 2 means internal, degree 0 means unused.
                        # For (x,1): degree 1 means endpoint, degree 2 means internal, degree 0 means unused.
                        new_ends = (1 if deg0 == 1 else 0) + (1 if deg1 == 1 else 0)
                        total_ends = end_count + new_ends
                        if total_ends > 2:
                            continue

                        # Build graph on nodes: L0, L1, L2, V0, V1, R0, R1, R2
                        # Wait: track connected components of the union of left-side components and column x edges!
                        # Nodes: 'L0', 'L1', 'L2', 'V0', 'V1', 'R0', 'R1', 'R2'
                        adj_loc = {}
                        active_nodes = set()
                        if 0 in left_used:
                            active_nodes.add("L0")
                        if 1 in left_used:
                            active_nodes.add("L1")
                        if 2 in left_used:
                            active_nodes.add("L2")
                        if deg0 > 0:
                            active_nodes.add("V0")
                        if deg1 > 0:
                            active_nodes.add("V1")
                        if r0:
                            active_nodes.add("R0")
                        if r1:
                            active_nodes.add("R1")
                        if r2:
                            active_nodes.add("R2")

                        for nd in active_nodes:
                            adj_loc[nd] = set()

                        def add_loc_edge(u, w):
                            adj_loc[u].add(w)
                            adj_loc[w].add(u)

                        if l0:
                            add_loc_edge("L0", "V0")
                        if l1:
                            add_loc_edge("L1", "V0")
                        if l2:
                            add_loc_edge("L2", "V1")
                        if use_v:
                            add_loc_edge("V0", "V1")
                        if r0:
                            add_loc_edge("V0", "R0")
                        if r1:
                            add_loc_edge("V1", "R1")
                        if r2:
                            add_loc_edge("V1", "R2")

                        # Also add left-side pairings between L_a and L_b!
                        for a, b in pairs:
                            add_loc_edge(f"L{a}", f"L{b}")

                        # Check for cycles! In the merged multigraph (each L_i has degree 1 on left if in pairs,
                        # or connects to an endpoint on left if in singles), a cycle occurs iff
                        # traversing components hits a cycle among active_nodes.
                        # Note: singles are attached to distinct endpoints on the left, NOT to each other.
                        visited_nd = set()
                        has_cycle = False
                        bad_component = False
                        closed_2_end = False
                        new_pairs = []
                        new_singles = []

                        for nd in sorted(active_nodes):
                            if nd in visited_nd:
                                continue
                            # BFS/DFS to find component
                            comp = []
                            stack = [(nd, None)]
                            visited_nd.add(nd)
                            while stack:
                                cur, par = stack.pop()
                                comp.append(cur)
                                for nxt in adj_loc[cur]:
                                    if nxt == par:
                                        continue
                                    if nxt in visited_nd:
                                        has_cycle = True
                                    else:
                                        visited_nd.add(nxt)
                                        stack.append((nxt, cur))
                            if has_cycle:
                                break

                            # Determine component's right-cut exits and endpoint status
                            r_exits = sorted(int(x[1]) for x in comp if x.startswith("R"))
                            col_ends = (1 if ("V0" in comp and deg0 == 1) else 0) + (
                                1 if ("V1" in comp and deg1 == 1) else 0
                            )
                            left_end_cnt = sum(1 for s in singles if f"L{s}" in comp)
                            comp_ends = left_end_cnt + col_ends

                            if len(r_exits) == 0:
                                # Closed off to the left! Must be the ENTIRE path (2 endpoints)
                                if comp_ends != 2 or total_ends != 2:
                                    bad_component = True
                                    break
                                closed_2_end = True
                            elif len(r_exits) == 1:
                                if comp_ends != 1:
                                    bad_component = True
                                    break
                                new_singles.append(r_exits[0])
                            elif len(r_exits) == 2:
                                if comp_ends != 0:
                                    bad_component = True
                                    break
                                new_pairs.append((r_exits[0], r_exits[1]))
                            else:
                                bad_component = True
                                break

                        if has_cycle or bad_component:
                            continue

                        if closed_2_end and (new_pairs or new_singles):
                            continue

                        if not new_pairs and not new_singles and total_ends not in (0, 2):
                            continue

                        next_st = (total_ends, tuple(sorted(new_pairs)), tuple(sorted(new_singles)))
                        added_edges = use_v + r0 + r1 + r2
                        results.append((next_st, added_edges))

        return results

    # Discover reachable pre-origin states (excluding completed/empty-after-start)
    init_state = (0, (), ())
    pre_states = {init_state}
    frontier = [init_state]
    while frontier:
        st = frontier.pop()
        for nxt, _ in step_column(st, is_origin_col=False):
            # In pre-origin columns, completed state (2, (), ()) cannot occur because
            # s=(0,0) hasn't been reached yet!
            if nxt[0] == 2:
                continue
            if nxt not in pre_states:
                pre_states.add(nxt)
                frontier.append(nxt)

    pre_list = sorted(pre_states)
    pre_idx = {s: i for i, s in enumerate(pre_list)}

    # Post-origin states reachable from pre_states via column x=0
    post_states = set()
    post_frontier = []
    for st in pre_list:
        for nxt, _ in step_column(st, is_origin_col=True):
            if nxt not in post_states:
                post_states.add(nxt)
                post_frontier.append(nxt)

    while post_frontier:
        st = post_frontier.pop()
        for nxt, _ in step_column(st, is_origin_col=False):
            if nxt not in post_states:
                post_states.add(nxt)
                post_frontier.append(nxt)

    # Note: (2, (), ()) is the absorbing accepting state; remove self-loop from M_R so
    # (I - M_R)^{-1} counts each path exactly once when it FIRST hits (2, (), ())!
    accept_state = (2, (), ())
    assert accept_state in post_states
    post_list = sorted(post_states)
    post_idx = {s: i for i, s in enumerate(post_list)}

    z = sp.Symbol("z")
    n_pre = len(pre_list)
    n_post = len(post_list)

    M_L = sp.zeros(n_pre, n_pre)
    for st in pre_list:
        j = pre_idx[st]
        for nxt, w in step_column(st, is_origin_col=False):
            if nxt in pre_idx and not (st == init_state and nxt == init_state):
                M_L[pre_idx[nxt], j] += z**w

    M_0 = sp.zeros(n_post, n_pre)
    for st in pre_list:
        j = pre_idx[st]
        for nxt, w in step_column(st, is_origin_col=True):
            M_0[post_idx[nxt], j] += z**w

    M_R = sp.zeros(n_post, n_post)
    for st in post_list:
        if st == accept_state:
            continue  # absorbing
        j = post_idx[st]
        for nxt, w in step_column(st, is_origin_col=False):
            M_R[post_idx[nxt], j] += z**w

    e_init = sp.zeros(n_pre, 1)
    e_init[pre_idx[init_state], 0] = 1

    v_L = (sp.eye(n_pre) - M_L).LUsolve(e_init)
    v_R = (sp.eye(n_post) - M_R).LUsolve(M_0 * v_L)

    # Total generating function including n=0 (s(0)=1)
    F_saw = sp.factor(1 + v_R[post_idx[accept_state], 0])
    return F_saw, n_pre, n_post


def check_part2_saw() -> None:
    z = sp.Symbol("z")
    F_saw, n_pre, n_post = transfer_matrix_saw_gf()
    expected_F = (1 + z**2 - z**3 + z**5) / ((1 - z) ** 2 * (1 - 2 * z - z**3))
    assert sp.simplify(F_saw - expected_F) == 0, f"GF mismatch: {F_saw} != {expected_F}"

    # Verify against pure brute-force DFS for n = 0..14
    dfs_0 = dfs_saw_counts(14, start=(0, 0))
    dfs_1 = dfs_saw_counts(10, start=(0, 1))
    assert dfs_0[:11] == dfs_1, f"Start-row asymmetry: {dfs_0[:11]} vs {dfs_1}"

    ser = sp.series(F_saw, z, 0, 15)
    gf_coeffs = [int(ser.coeff(z, k)) for k in range(15)]
    assert gf_coeffs == dfs_0, f"GF vs DFS mismatch: {gf_coeffs} vs {dfs_0}"

    # Compare against G_oeis(z)
    G_oeis = (1 + z**2) * (1 + z + z**2) / ((1 - z) * (1 - 2 * z - z**3))
    diff_gf = sp.factor(F_saw - G_oeis)
    expected_diff = 2 * z**5 / ((1 - z) ** 2 * (1 - 2 * z - z**3))
    assert sp.simplify(diff_gf - expected_diff) == 0, f"Diff GF mismatch: {diff_gf}"

    # Verify positivity of 1/((1-z)^2 (1-2z-z^3)) explicitly:
    # 1/(1-2z-z^3) satisfies t_0 = 1, t_1 = 2, t_2 = 4, t_m = 2*t_{m-1} + t_{m-3} >= 1
    # Multiplying by 1/(1-z)^2 = sum (k+1) z^k yields strictly positive coefficients for all k >= 0.
    diff_coeffs = [int(sp.series(diff_gf, z, 0, 15).coeff(z, k)) for k in range(15)]
    assert diff_coeffs[:5] == [0, 0, 0, 0, 0]
    assert diff_coeffs[5:10] == [2, 8, 22, 54, 126]
    assert dfs_0[5] == 160 and OEIS_A100691[5] == 158 and OEIS_A193641[7] - 3 == 158

    print(
        f"Part 2 PASS: Transfer matrix (pre={n_pre}, post={n_post}) matches DFS (n<=14): "
        f"s(0..7)={dfs_0[:8]}, s(5)=160 != 158=A193641(7)-3."
    )


def main() -> None:
    check_part1_a193641()
    check_part2_saw()
    print("PASS")


if __name__ == "__main__":
    main()
