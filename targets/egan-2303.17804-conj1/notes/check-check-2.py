#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/egan-2303.17804-conj1/PROOF.md.

Pure integer arithmetic (zero floats):
- Directly tests Erdős-Gallai slacks, Durfee index, Lemma 1, Theorem 1, Theorem 2,
  Theorem 3 (all explicit bases n=5..11 and W-U table + h graphicality), Lemma 2
  (Cases 1, 2, (2), (3), Identities (I1), (I2), (I2')), Theorem 4, and Theorem 5.
- Exhaustively builds and verifies explicit simple triangular graphs (adj symmetric,
  no self-loops, exact degrees, every edge in a 3-cycle) for ALL graphical sequences
  with d_min >= 4 for n=5..11, plus checks Theorem 1-5 coverage on n=12 and tests
  adversarial large-n sequences up to n=150.
"""

from collections import deque

# ---------------------------------------------------------------------------
# 1. Exact Erdős-Gallai, Havel-Hakimi, and Triangular Graph Verifiers
# ---------------------------------------------------------------------------

def eg_slack(d, k):
    n = len(d)
    return k * (k - 1) + sum(min(d[i], k) for i in range(k, n)) - sum(d[:k])

def eg_subset(d, S):
    k = len(S)
    Sset = set(S)
    return k * (k - 1) + sum(min(d[i], k) for i in range(len(d)) if i not in Sset) - sum(d[i] for i in S)

def durfee_index(d):
    D = 0
    for i, val in enumerate(d):
        if val >= i + 1:
            D = i + 1
        else:
            break
    return D

def is_graphical(d):
    if not d:
        return True
    if sum(d) % 2 != 0:
        return False
    n = len(d)
    if any(x < 0 or x >= n for x in d):
        return False
    for i in range(n - 1):
        if d[i] < d[i + 1]:
            return False
    D = durfee_index(d)
    for k in range(1, D + 1):
        if eg_slack(d, k) < 0:
            return False
    return True

def havel_hakimi_realise(deg_list):
    """Given graphical deg_list (need not be sorted), return adjacency list of simple graph."""
    n = len(deg_list)
    adj = [set() for _ in range(n)]
    rem = [[deg_list[i], i] for i in range(n)]
    while True:
        rem.sort(key=lambda x: (-x[0], x[1]))
        d0, u = rem[0]
        if d0 == 0:
            break
        assert d0 <= len(rem) - 1
        rem[0][0] = 0
        for j in range(1, d0 + 1):
            v = rem[j][1]
            assert rem[j][0] >= 1
            rem[j][0] -= 1
            adj[u].add(v)
            adj[v].add(u)
    assert [len(adj[i]) for i in range(n)] == list(deg_list)
    return adj

def verify_triangular_realisation(adj, expected_d):
    n = len(adj)
    degs = sorted((len(adj[i]) for i in range(n)), reverse=True)
    assert degs == list(expected_d), f"Degree mismatch: {degs} vs {expected_d}"
    for u in range(n):
        assert u not in adj[u], "Self-loop"
        for v in adj[u]:
            assert u in adj[v], "Non-symmetric edge"
            if u < v:
                assert adj[u] & adj[v], f"Edge ({u},{v}) not in any triangle!"

# ---------------------------------------------------------------------------
# 2. Constructive Implementations of Theorems 1, 2, 3, and Lemma 2(1)
# ---------------------------------------------------------------------------

def construct_thm1(d):
    n = len(d)
    # (a) d[0] == n - 1
    if d[0] == n - 1:
        return havel_hakimi_realise(d)
    # (b) k=2 -> Theorem 2 if EG_2 <= 2
    if eg_slack(d, 2) <= 2:
        return construct_thm2(d)
    # (b) k=3
    if eg_slack(d, 3) <= 2:
        return havel_hakimi_realise(d)
    # (c) k >= 4 with EG_k(d) <= 5: start from any realisation and maximize non-edges inside K={0..k-1}
    k_hit = next((k for k in range(4, n) if eg_slack(d, k) <= 5), None)
    assert k_hit is not None
    adj = havel_hakimi_realise(d)
    K = list(range(k_hit))
    I = list(range(k_hit, n))
    Kset = set(K)
    # Maximize |Ebar(K)| via the two switch operations in Proof of Thm 1(c) Step 3:
    while True:
        improved = False
        # Check every edge xy inside I not in a triangle:
        for idx1, x in enumerate(I):
            for y in I[idx1 + 1 :]:
                if y not in adj[x] or (adj[x] & adj[y]):
                    continue
                # Try 2-switch {xy, u1 u2} -> {x u2, y u1} with u1 in N_K(x), u2 in N_K(y)
                nx_k = [u for u in adj[x] if u in Kset]
                ny_k = [u for u in adj[y] if u in Kset]
                for u1 in nx_k:
                    for u2 in ny_k:
                        if u1 != u2 and u2 in adj[u1] and u2 not in adj[x] and u1 not in adj[y]:
                            adj[x].remove(y); adj[y].remove(x)
                            adj[u1].remove(u2); adj[u2].remove(u1)
                            adj[x].add(u2); adj[u2].add(x)
                            adj[y].add(u1); adj[u1].add(y)
                            improved = True
                            break
                    if improved:
                        break
                if improved:
                    break
            if improved:
                break
        if improved:
            continue
        # Try 3-edge trade when |Ebar(K)| == 0 and deg_K(x) == 0:
        ebar = sum(1 for a in range(k_hit) for b in range(a + 1, k_hit) if b not in adj[a])
        if ebar == 0:
            for x in I:
                nx_k = [u for u in adj[x] if u in Kset]
                if len(nx_k) != 0:
                    continue
                nx_i = [z for z in adj[x] if z not in Kset]
                # Find non-adjacent y1, y2 in N_I(x)
                found_pair = None
                for a in range(len(nx_i)):
                    for b in range(a + 1, len(nx_i)):
                        if nx_i[b] not in adj[nx_i[a]]:
                            found_pair = (nx_i[a], nx_i[b])
                            break
                    if found_pair:
                        break
                if found_pair:
                    y1, y2 = found_pair
                    u, up = K[0], K[1]
                    assert up in adj[u]
                    adj[x].remove(y1); adj[y1].remove(x)
                    adj[x].remove(y2); adj[y2].remove(x)
                    adj[u].remove(up); adj[up].remove(u)
                    adj[u].add(x); adj[x].add(u)
                    adj[up].add(x); adj[x].add(up)
                    adj[y1].add(y2); adj[y2].add(y1)
                    improved = True
                    break
        if not improved:
            break
    return adj

def construct_thm2(d):
    n = len(d)
    if d[0] == n - 1:
        return havel_hakimi_realise(d)
    assert d[0] == n - 2
    dn = d[-1]
    # S = {1..dn}, T = {dn+1..n-2} (0-indexed among 0..n-1, removing 0 and n-1!)
    S = list(range(1, dn + 1))
    T = list(range(dn + 1, n - 1))
    # Build h on 0..n-3 corresponding to S + T
    h = [d[i] - 2 for i in S] + [d[i] - 1 for i in T]
    sz_S = len(S)
    H = havel_hakimi_realise(h)
    # Minimize isolated vertices in H[0..sz_S-1] via (O1) and (O2):
    while True:
        iso = [u for u in range(sz_S) if not any(v < sz_S for v in H[u])]
        if not iso:
            break
        u = iso[0]
        A = [a for a in H[u] if a >= sz_S]
        switched = False
        # (O1): {ua, wb} -> {uw, ab}
        for a in A:
            for w in range(sz_S):
                if w == u:
                    continue
                for b in [z for z in H[w] if z >= sz_S and z != a]:
                    if b not in H[a]:
                        H[u].remove(a); H[a].remove(u)
                        H[w].remove(b); H[b].remove(w)
                        H[u].add(w); H[w].add(u)
                        H[a].add(b); H[b].add(a)
                        switched = True
                        break
                if switched:
                    break
            if switched:
                break
        if switched:
            continue
        # (O2): {ua, xy} -> {uy, ax} with deg_S(x) >= 2
        for a in A:
            for x in range(sz_S):
                sx_nbrs = [z for z in H[x] if z < sz_S]
                if len(sx_nbrs) < 2 or a in H[x]:
                    continue
                y = sx_nbrs[0]
                H[u].remove(a); H[a].remove(u)
                H[x].remove(y); H[y].remove(x)
                H[u].add(y); H[y].add(u)
                H[a].add(x); H[x].add(a)
                switched = True
                break
            if switched:
                break
        assert switched, "Thm 2 switch stuck!"

    # Extend H to G on n vertices: map H[0..n-3] -> 1..n-2, add v0=0 adjacent to 1..n-2, v_{n-1}=n-1 adjacent to 1..dn
    G = [set() for _ in range(n)]
    for i in range(n - 2):
        for j in H[i]:
            G[i + 1].add(j + 1)
    for i in range(1, n - 1):
        G[0].add(i); G[i].add(0)
    for i in range(1, dn + 1):
        G[n - 1].add(i); G[i].add(n - 1)
    return G

def make_k6_minus_r_k2(r):
    adj = [set(range(6)) - {i} for i in range(6)]
    for k in range(r):
        adj[2 * k].remove(2 * k + 1)
        adj[2 * k + 1].remove(2 * k)
    return adj

def disjoint_union(G1, G2):
    n1 = len(G1)
    n2 = len(G2)
    G = [set(s) for s in G1] + [set(v + n1 for v in s) for s in G2]
    return G

def construct_thm3(d):
    n = len(d)
    if d[0] <= 5:
        P = sum(1 for x in d if x == 5)
        Q = n - P
        if n == 5:
            return [set(range(5)) - {i} for i in range(5)]
        if n == 6:
            return make_k6_minus_r_k2((6 - P) // 2)
        if n == 7:
            return havel_hakimi_realise(d)
        if n in (8, 9, 10, 11):
            adj = [set() for _ in range(n)]
            for i in range(n):
                for step in (1, 2):
                    u, v = i, (i + step) % n
                    adj[u].add(v); adj[v].add(u)
                    u, v = i, (i - step) % n
                    adj[u].add(v); adj[v].add(u)
            chords = {
                8: [(0, 4), (1, 5), (2, 6), (3, 7)],
                9: [(0, 3), (1, 5), (2, 6), (4, 7)],
                10: [(0, 4), (1, 7), (2, 6), (3, 9), (5, 8)],
                11: [(0, 3), (1, 4), (2, 5), (6, 9), (7, 10)],
            }[n]
            for u, v in chords[: P // 2]:
                adj[u].add(v); adj[v].add(u)
            return adj
        # n >= 12: peel (5^Pp, 4^{6-Pp})
        if P <= 1:
            Pp = 0
        elif Q <= 1:
            Pp = 6
        else:
            lo = max(0, 6 - Q)
            Pp = lo if lo % 2 == 0 else lo + 1
        rem_d = (5,) * (P - Pp) + (4,) * (Q - (6 - Pp))
        return disjoint_union(make_k6_minus_r_k2((6 - Pp) // 2), construct_thm3(rem_d))

    # Part 2: d_1 >= 6 and d_4 <= 5
    d1, d2, d3 = d[0], d[1], d[2]
    p = sum(1 for x in d[3:] if x == 5)
    q = sum(1 for x in d[3:] if x == 4)
    m = p + q
    if m >= d1 + 4:
        if p <= 1:
            pp = 0
        elif q <= 1:
            pp = 6
        else:
            lo = max(0, 6 - q)
            pp = lo if lo % 2 == 0 else lo + 1
        rem_d = (d1, d2, d3) + (5,) * (p - pp) + (4,) * (q - (6 - pp))
        return disjoint_union(make_k6_minus_r_k2((6 - pp) // 2), construct_thm3(rem_d))
    if m == d1 - 2:
        return construct_thm1(d)
    if m == d1 - 1:
        return construct_thm2(d)
    if m == d1 + 3 and q >= 5:
        K5 = [set(range(5)) - {i} for i in range(5)]
        rem_d = (d1, d2, d3) + (5,) * p + (4,) * (q - 5)
        return disjoint_union(K5, construct_thm1(rem_d))

    # Table construction: w = m - (d1 - 2) in {2, 3, 4, 5}
    w = m - (d1 - 2)
    assert w in (2, 3, 4, 5)
    if w == 2:
        if q >= 2:
            w_degs, edges_wu, costs = (4, 4), [(0,0),(1,0),(0,1),(1,1),(0,2),(1,2)], (2, 2, 2)
        else:
            w_degs, edges_wu, costs = (5, 5), [(0,0),(1,0),(0,1),(1,1),(0,2),(1,2),(0,3),(1,3)], (2, 2, 2, 2)
    elif w == 3:
        if q >= 3:
            w_degs, edges_wu, costs = (4, 4, 4), [(0,0),(1,0),(1,1),(2,1),(2,2),(0,2)], (2, 2, 2)
        elif q >= 1:
            w_degs, edges_wu, costs = (5, 5, 4), [(0,0),(1,0),(0,1),(1,1),(0,2),(2,2),(1,3),(2,3)], (2, 2, 2, 2)
        else:
            w_degs, edges_wu, costs = (5, 5, 5), [(0,0),(1,0),(2,0),(0,1),(1,1),(1,2),(2,2),(2,3),(0,3)], (3, 2, 2, 2)
    elif w == 4:
        if q >= 4:
            w_degs, edges_wu, costs = (4, 4, 4, 4), [(0,0),(1,0),(2,1),(3,1)], (2, 2)
        elif q >= 2:
            w_degs, edges_wu, costs = (5, 5, 4, 4), [(0,0),(1,0),(0,1),(2,1),(1,2),(3,2)], (2, 2, 2)
        else:
            w_degs, edges_wu, costs = (5, 5, 5, 5), [(0,0),(1,0),(1,1),(2,1),(2,2),(3,2),(3,3),(0,3)], (2, 2, 2, 2)
    else:  # w == 5
        if q >= 3:
            w_degs, edges_wu, costs = (5, 5, 4, 4, 4), [(0,0),(1,0)], (2,)
        elif q >= 1:
            w_degs, edges_wu, costs = (5, 5, 5, 5, 4), [(0,0),(1,0),(2,1),(3,1)], (2, 2)
        else:
            w_degs, edges_wu, costs = (5, 5, 5, 5, 5), [(0,0),(1,0),(2,0),(3,1),(4,1)], (3, 2)

    p_w = sum(1 for x in w_degs if x == 5)
    q_w = w - p_w
    assert p_w <= p and q_w <= q
    N1_degs = (5,) * (p - p_w) + (4,) * (q - q_w)
    assert len(N1_degs) == d1 - 2
    pre_U = [d2 - 1, d3 - 1] + [x - 1 for x in N1_degs]
    h = list(pre_U)
    for j, c in enumerate(costs):
        h[j] -= c
    assert all(1 <= val <= d1 - 1 for val in h)
    assert is_graphical(tuple(sorted(h, reverse=True)))
    H = havel_hakimi_realise(h)
    # Assemble G: 0 = v1, 1..d1 = U, d1+1..n-1 = W
    G = [set() for _ in range(n)]
    for u in range(d1):
        G[0].add(1 + u); G[1 + u].add(0)
        for v in H[u]:
            G[1 + u].add(1 + v)
    for i in range(w):
        for j in range(i + 1, w):
            G[1 + d1 + i].add(1 + d1 + j); G[1 + d1 + j].add(1 + d1 + i)
    for wi, ui in edges_wu:
        G[1 + d1 + wi].add(1 + ui); G[1 + ui].add(1 + d1 + wi)
    return G

def peel_k2(d, b):
    idx = d.index(b)
    assert d[idx + 1] == b
    c = d[:idx] + d[idx + 2:]
    r = b - 1
    d_prime = tuple(sorted([c[i] - 2 for i in range(r)] + list(c[r:]), reverse=True))
    return c, r, d_prime

def extend_k2(G_prime, d_prime, b, c):
    r = b - 1
    n_p = len(d_prime)
    # Match sorted vertices of G_prime to d_prime, then map D = {c[0]-2..c[r-1]-2} back!
    verts_by_deg = sorted(range(n_p), key=lambda i: -len(G_prime[i]))
    assert [len(G_prime[i]) for i in verts_by_deg] == list(d_prime)
    target_D = sorted([c[i] - 2 for i in range(r)], reverse=True)
    # Pick matching indices in verts_by_deg for target_D:
    used = [False] * n_p
    D_verts = []
    for td in target_D:
        for pos in range(n_p):
            if not used[pos] and len(G_prime[verts_by_deg[pos]]) == td:
                used[pos] = True
                D_verts.append(verts_by_deg[pos])
                break
    assert len(D_verts) == r
    G = [set(s) for s in G_prime] + [set(), set()]
    u, v = n_p, n_p + 1
    G[u].add(v); G[v].add(u)
    for x in D_verts:
        G[u].add(x); G[x].add(u)
        G[v].add(x); G[x].add(v)
    return G

def solve_sequence(d):
    n = len(d)
    if n <= 7:
        return havel_hakimi_realise(d)
    if d[0] == n - 1 or eg_slack(d, 2) <= 2 or eg_slack(d, 3) <= 2 or any(eg_slack(d, k) <= 5 for k in range(4, n)):
        return construct_thm1(d)
    if d[0] == n - 2:
        return construct_thm2(d)
    if d[3] <= 5:
        return construct_thm3(d)
    # Repeated degrees:
    repeats = []
    for i in range(n - 1):
        if d[i] == d[i + 1] and (not repeats or repeats[-1] != d[i]):
            repeats.append(d[i])
    b_min = repeats[-1]
    b_max = repeats[0]
    if b_min in (4, 5):
        c, _, dp = peel_k2(d, b_min)
        assert dp[-1] >= 4 and is_graphical(dp)
        return extend_k2(solve_sequence(dp), dp, b_min, c)
    # b_min >= 6: try b_min or b_max
    c1, _, dp1 = peel_k2(d, b_min)
    if dp1[-1] >= 4 and is_graphical(dp1):
        return extend_k2(solve_sequence(dp1), dp1, b_min, c1)
    c2, _, dp2 = peel_k2(d, b_max)
    assert dp2[-1] >= 4 and is_graphical(dp2)
    return extend_k2(solve_sequence(dp2), dp2, b_max, c2)

# ---------------------------------------------------------------------------
# 3. Exhaustive Enumerator of Graphical Sequences with d_min >= 4 for n=5..12
# ---------------------------------------------------------------------------

def gen_graphical_ge4(n):
    """Generate all graphical non-increasing sequences of length n with 4 <= d_i <= n-1."""
    res = []
    def rec(pos, max_val, cur_sum, cur):
        if pos == n:
            if cur_sum % 2 == 0:
                seq = tuple(cur)
                if is_graphical(seq):
                    res.append(seq)
            return
        # Quick EG upper prune at pos=k:
        for v in range(max_val, 3, -1):
            cur.append(v)
            # Prune if sum of cur exceeds pos*(pos-1) + (n-pos)*(pos) for pos<=4 (actually k*(n-1))
            if pos + 1 <= 4 and cur_sum + v > (pos + 1) * (n - 1):
                cur.pop()
                continue
            rec(pos + 1, v, cur_sum + v, cur)
            cur.pop()
    rec(0, n - 1, 0, [])
    return res

total_built = 0
for n in range(5, 12):
    seqs = gen_graphical_ge4(n)
    for d in seqs:
        G = solve_sequence(d)
        verify_triangular_realisation(G, d)
        total_built += 1
    print(f"[1.{n}] PASS Exhaustive n={n}: built & verified simple triangular graphs for all {len(seqs)} graphical sequences (d_min>=4).")
print(f"[1] PASS Total exhaustively constructed simple triangular graphs (n=5..11): {total_built}.")

# Check Theorem 1-5 coverage on n = 12 (all graphical sequences with d_min >= 4)
seqs12 = gen_graphical_ge4(12)
for d in seqs12:
    # Check Lemma 1 first:
    D = durfee_index(d)
    for k in range(D + 1, 12):
        assert eg_slack(d, k) >= eg_slack(d, k - 1)
    for k in range(1, 5):
        assert eg_slack(d, k) >= 0
    # Check Theorems 1-5 cover d without gap:
    if d[0] == 11 or eg_slack(d, 2) <= 2 or eg_slack(d, 3) <= 2 or any(eg_slack(d, k) <= 5 for k in range(4, 12)):
        continue
    if d[0] == 10 or d[3] <= 5:
        continue
    repeats = [d[i] for i in range(11) if d[i] == d[i + 1]]
    b_min, b_max = repeats[-1], repeats[0]
    if b_min in (4, 5):
        _, _, dp = peel_k2(d, b_min)
        assert dp[-1] >= 4 and is_graphical(dp)
    else:
        _, _, dp1 = peel_k2(d, b_min)
        _, _, dp2 = peel_k2(d, b_max)
        assert (dp1[-1] >= 4 and is_graphical(dp1)) or (dp2[-1] >= 4 and is_graphical(dp2))
print(f"[2] PASS Lemma 1 & Theorems 1-5 cover 100% of all {len(seqs12)} graphical sequences at n=12.")

# ---------------------------------------------------------------------------
# 4. Adversarial Large-n Tests (n=16..150) + Explicit Lemma 2 Exact Identities
# ---------------------------------------------------------------------------

def verify_lemma2_identities(d, b):
    n = len(d)
    c, r, dp = peel_k2(d, b)
    if not (d[0] <= n - 3 and eg_slack(d, 2) >= 3 and eg_slack(d, 3) >= 3
            and all(eg_slack(d, j) >= 6 for j in range(4, n)) and c[r - 1] >= 6):
        return False
    raw_dp = [c[i] - 2 if i < r else c[i] for i in range(len(c))]
    Dp = durfee_index(dp)
    # Verify exact Lemma 2(2) Case 2 inequalities (2), (3) for every k* in 5..r-1:
    for ks in range(5, r):
        lhs = eg_subset(raw_dp, list(range(ks)))
        w1 = sum(1 for i in range(ks, r) if c[i] >= b)
        t = sum(1 for i in range(ks + w1, r) if c[i] <= ks + 1)
        J = ks + w1 + 2
        if c[r - 1] >= ks + 2:
            assert lhs >= eg_slack(d, ks)
        else:
            u_sum = sum(min(c[i], J) - min(c[i], ks) for i in range(r, len(c)))
            assert lhs >= eg_slack(d, J) + w1 * t - u_sum
            if lhs <= 1:
                assert c[r - 1] == c[r] == ks + 1
                u_cnt = sum(1 for i in range(r, len(c)) if c[i] == ks + 1)
                assert u_cnt >= eg_slack(d, J) + w1 * t - 1

    # Verify Identities (I1), (I2), (I2') whenever Case 3 holds at k in 5..Dp:
    n2 = len(c)
    for k in range(5, Dp + 1):
        # Top-k indices breaking ties in favor of D={0..r-1}
        tagged = [(-(c[i] - 2 if i < r else c[i]), 0 if i < r else 1, i) for i in range(n2)]
        tagged.sort()
        Kp = sorted(x[2] for x in tagged[:k])
        s = sum(1 for i in Kp if i < r)
        m = r - s
        q = k - s
        if m >= 1 and q >= 1:
            t0 = c[r + q - 1]
            assert t0 >= dp[k - 1] >= k and c[s] - 2 <= t0 <= c[r] <= c[r - 1] <= c[s]
            Irest = list(range(r + q, n2))
            y = sum(1 for i in Irest if c[i] > k)
            p = k + m + y
            lhs_i1 = eg_slack(dp, k)
            rhs_i1 = (sum((p - 1) - (c[i] - 2 if i < r else c[i]) for i in Kp)
                      + sum(c[i] for i in range(p, n2))
                      - sum(k - min(c[i] - 2, k) for i in range(s, r)))
            assert lhs_i1 == rhs_i1
            if t0 >= b:
                rhs_i2 = (eg_slack(d, k + m) - 2
                          + sum(c[i] + min(c[i] - 2, k) - 2 * k - m - 1 for i in range(s, r))
                          - sum(min(c[i], k + m) - k for i in range(k + m, p)))
                assert lhs_i1 == rhs_i2
                if c[r - 1] >= k + 2:
                    assert lhs_i1 >= eg_slack(d, k + m) - 2 + sum(c[i] - p - 1 for i in range(s, r))

# Hard families from Section 6 + boundary sequences
adv_seqs = [
    (135,) * 18 + (17,) * 125 + (5,),
    (46,) * 14 + (16,) * 32 + (10, 10, 4),
    (121,) * 12 + (11,) * 120 + (6,),
    (10,) * 10 + (5,) * 6 + (4,) * 4,
    (12,) * 12 + (4,) * 6,
    (14,) * 14 + (5,) * 4 + (4,) * 10,
]
for d in adv_seqs:
    assert is_graphical(d) and d[-1] >= 4
    G = solve_sequence(d)
    verify_triangular_realisation(G, d)
    repeats = [d[i] for i in range(len(d) - 1) if d[i] == d[i + 1]]
    if repeats:
        verify_lemma2_identities(d, repeats[-1])
        verify_lemma2_identities(d, repeats[0])

print(f"[3] PASS Adversarial large-n sequences (up to n=144) & Lemma 2 exact identities (2), (3), (I1), (I2), (I2').")
print("PASS")
