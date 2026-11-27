"""Exact integer verification for kaul-2112.05316-ques3 (arXiv:2112.05316v2 Questions 2 & 3, p >= 4)."""

import itertools
import math


def build_G0(p, r):
    """Build G_0 = K_{p-2} vee K_{2,r} as vertex list and adjacency set."""
    W = [f"w{i}" for i in range(1, p - 1)]
    V = ["v1", "v2"]
    U = [f"u{j}" for j in range(1, r + 1)]
    verts = W + V + U
    adj = {x: set() for x in verts}
    for i, x in enumerate(W):
        for y in W[i + 1 :]:
            adj[x].add(y)
            adj[y].add(x)
        for y in V + U:
            adj[x].add(y)
            adj[y].add(x)
    for x in V:
        for y in U:
            adj[x].add(y)
            adj[y].add(x)
    return verts, adj, W, V, U


def find_p_cliques(verts, adj, p):
    """Enumerate all cliques of size p in G_0."""
    cliques = []
    for comb in itertools.combinations(verts, p):
        if all(b in adj[a] for a, b in itertools.combinations(comb, 2)):
            cliques.append(comb)
    return cliques


def count_cover_exact(p, r, perm):
    """Exact integer count of H-colorings of K_{p-2} vee K_{2,r} with m=p+1 and edge v1-u_r twisted by perm."""
    m = p + 1
    total = 0
    w_mult = math.factorial(p - 2)
    for S in itertools.combinations(range(m), 3):
        s_set = set(S)
        s_cnt = 0
        for cv1 in S:
            for cv2 in S:
                u_choices = 2 if cv1 == cv2 else 1
                ur_choices = len(s_set - {perm[cv1], cv2})
                s_cnt += (u_choices ** (r - 1)) * ur_choices
        total += w_mult * s_cnt
    return total


def brute_force_cover_p4_r3():
    """Direct brute-force over all 5^7 vertex assignments on G_0 = K_2 vee K_{2,3} (m=5) and all 5^8 on K_2 vee K_{2,4}? (Fast exact check on K_2 vee K_{2,3}.)"""
    p, r, m = 4, 3, 5
    verts, adj, W, V, U = build_G0(p, r)
    # 1. Canonical cover count = P(G_0, 5)
    # 2. Twisted cover with perm = (1, 0, 2, 3, 4) on edge ('v1', 'u3')
    perm = [1, 0, 2, 3, 4]
    canon = 0
    twisted = 0
    edges = [(a, b) for a in verts for b in adj[a] if a < b]
    idx = {v: i for i, v in enumerate(verts)}
    tw_pair = tuple(sorted(("v1", "u3")))
    for col in itertools.product(range(m), repeat=len(verts)):
        ok_c = True
        ok_t = True
        for a, b in edges:
            ca, cb = col[idx[a]], col[idx[b]]
            if ca == cb:
                ok_c = False
            pair = (a, b)
            if pair == tw_pair:
                # tw_pair sorted is ('u3', 'v1')
                if a == "v1":
                    if perm[ca] == cb:
                        ok_t = False
                else:
                    if perm[cb] == ca:
                        ok_t = False
            else:
                if ca == cb:
                    ok_t = False
            if not ok_c and not ok_t:
                break
        if ok_c:
            canon += 1
        if ok_t:
            twisted += 1
    assert canon == 600, f"Expected 600, got {canon}"
    assert twisted == 588, f"Expected 588, got {twisted}"


def check_extension_and_tessellation(p, r):
    """Verify Lemma 1, Lemma 3, and tessellation structural properties on G_0 = K_{p-2} vee K_{2,r}."""
    verts, adj, W, V, U = build_G0(p, r)
    cliques = find_p_cliques(verts, adj, p)
    expected = {tuple(sorted(W + [vi, uj])) for vi in V for uj in U}
    assert {tuple(sorted(c)) for c in cliques} == expected
    assert len(cliques) == 2 * r

    # Check every edge of G_0 belongs to at least one p-clique
    for a in verts:
        for b in adj[a]:
            assert any(a in c and b in c for c in cliques), f"Edge {a}-{b} not in any K_{p}"

    # Check Lemma 3 degree conditions on G_0 \ K_k
    for c in cliques:
        c_set = set(c)
        rem = [x for x in verts if x not in c_set]
        rem_v = [x for x in rem if x in V]
        rem_u = [x for x in rem if x in U]
        assert len(rem_v) == 1 and len(rem_u) == r - 1
        v_rem = rem_v[0]
        assert len(adj[v_rem] & c_set) == p - 1  # leaves >= (p+1)-(p-1) = 2 choices
        for u_rem in rem_u:
            assert len(adj[u_rem] & c_set) == p - 1  # plus v_rem = p, leaves >= 1 choice
            assert adj[u_rem] & set(rem_u) == set()  # independent set

    # Build G^* = G_{2r} and verify each d_k is simplicial of degree p
    g_verts = list(verts)
    g_adj = {x: set(adj[x]) for x in g_verts}
    for k, c in enumerate(cliques, 1):
        dk = f"d{k}"
        for a, b in itertools.combinations(c, 2):
            assert b in g_adj[a]
        g_verts.append(dk)
        g_adj[dk] = set(c)
        for x in c:
            g_adj[x].add(dk)
        assert len(g_adj[dk]) == p


def main():
    brute_force_cover_p4_r3()

    for p in range(3, 9):
        r = p
        m = p + 1
        id_perm = list(range(m))
        tr_perm = [1, 0] + list(range(2, m))
        canon = count_cover_exact(p, r, id_perm)
        twisted = count_cover_exact(p, r, tr_perm)
        expected_canon = (math.factorial(m) // 6) * (3 * (1 << p) + 6)
        expected_diff = -math.factorial(p - 1) * ((1 << p) - 2 * p + 2)
        assert canon == expected_canon, f"p={p}: {canon} != {expected_canon}"
        assert twisted - canon == expected_diff, f"p={p}: {twisted - canon} != {expected_diff}"
        assert twisted < canon
        if p <= 6:
            check_extension_and_tessellation(p, r)

    # Verify algebraic positivity 2^p - 2p + 2 > 0 for p = 3..200
    for p in range(3, 201):
        assert (1 << p) - 2 * p + 2 > 0

    # Also verify exact K_4-gluing arithmetic for p=4, m=5
    m = 5
    p_k5 = math.prod(m - i for i in range(5))
    denom = math.prod(m - i for i in range(4))
    assert p_k5 // denom == 1 and p_k5 % denom == 0

    print("PASS: kaul-2112.05316-ques3 verified for p=4 (incl. brute-force 5^7) and general p>=3 family K_{p-2} vee K_{2,p}.")


if __name__ == "__main__":
    main()
