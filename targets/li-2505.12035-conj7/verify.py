from itertools import combinations, permutations


def verify_counterexample(name, n, edges, min_required_sum):
    assert n >= 6
    # Validate hyperedges: distinct subsets of size <= 3 (in fact == 3)
    edge_sets = [frozenset(e) for e in edges]
    assert len(set(edge_sets)) == len(edges), f"{name}: duplicate edges"
    for e in edge_sets:
        assert 1 <= len(e) <= 3, f"{name}: invalid edge size {e}"
        assert all(0 <= v < n for v in e), f"{name}: vertex out of range"

    # Build 2-shadow graph
    adj = [set() for _ in range(n)]
    for e in edge_sets:
        for u, v in combinations(e, 2):
            adj[u].add(v)
            adj[v].add(u)

    degs = [len(adj[v]) for v in range(n)]
    non_adj_sums = []
    for u in range(n):
        for v in range(u + 1, n):
            if v not in adj[u]:
                s = degs[u] + degs[v]
                non_adj_sums.append(((u, v), s))
                assert s >= min_required_sum, f"{name}: pair {(u,v)} has sum {s} < {min_required_sum}"

    assert len(non_adj_sums) > 0, f"{name}: expected non-covering graph"

    # Exhaustive check: no Hamiltonian Berge cycle exists
    assert len(edge_sets) < n, f"{name}: expected |E| < n"
    # Even directly check all cyclic permutations (fixing v0 = 0):
    for perm in permutations(range(1, n)):
        cyc = (0,) + perm
        # Each consecutive pair must lie in some hyperedge, and all n hyperedges must be distinct
        # Impossible since |E| < n, and we check pair-edge incidence explicitly anyway:
        cand_lists = []
        ok = True
        for i in range(n):
            pair = frozenset((cyc[i], cyc[(i + 1) % n]))
            hits = [idx for idx, e in enumerate(edge_sets) if pair <= e]
            if not hits:
                ok = False
                break
            cand_lists.append(hits)
        if ok:
            # Try finding distinct representatives
            used = set()
            def bt(i):
                if i == n:
                    return True
                for idx in cand_lists[i]:
                    if idx not in used:
                        used.add(idx)
                        if bt(i + 1):
                            return True
                        used.remove(idx)
                return False
            assert not bt(0), f"{name}: unexpectedly found Hamiltonian Berge cycle!"

    print(
        f"{name}: n={n}, |E|={len(edges)} < {n}, degs={degs}, "
        f"min_nonadj_sum={min(s for _, s in non_adj_sums)} (required >= {min_required_sum}), "
        f"hamiltonian_berge_cycle=False"
    )


def main():
    h1_edges = [
        (0, 1, 2),
        (0, 1, 3),
        (0, 2, 4),
        (1, 2, 5),
        (3, 4, 5),
    ]
    verify_counterexample("Witness 1 (n=6, |E|=5)", 6, h1_edges, 7)

    # Also confirm Witness 1 satisfies n+2 = 8
    verify_counterexample("Witness 1 (n=6, d0=2 check)", 6, h1_edges, 8)

    # Witness 2: Fano plane minus {0,1,2}
    h2_edges = [
        (0, 3, 4),
        (0, 5, 6),
        (1, 3, 5),
        (1, 4, 6),
        (2, 3, 6),
        (2, 4, 5),
    ]
    verify_counterexample("Witness 2 (n=7, Fano-1, linear)", 7, h2_edges, 8)
    print("PASS")


if __name__ == "__main__":
    main()
