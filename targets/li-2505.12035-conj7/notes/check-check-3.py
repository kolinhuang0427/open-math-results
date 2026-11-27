"""Independent exact-arithmetic verifier for targets/li-2505.12035-conj7/."""

import itertools
import signal

signal.alarm(50)


def has_hamiltonian_berge_cycle(n: int, edges: list[frozenset[int]]) -> bool:
    """Exhaustively test existence of n distinct vertices & n distinct hyperedges forming a Berge cycle."""
    if len(edges) < n:
        return False
    pair_to_edges: dict[tuple[int, int], list[int]] = {}
    for idx, e in enumerate(edges):
        for u in e:
            for v in e:
                if u < v:
                    pair_to_edges.setdefault((u, v), []).append(idx)

    for perm in itertools.permutations(range(1, n)):
        cyc = (0,) + perm
        cand_lists = []
        ok = True
        for i in range(n):
            u, v = cyc[i], cyc[(i + 1) % n]
            key = (u, v) if u < v else (v, u)
            cands = pair_to_edges.get(key, [])
            if not cands:
                ok = False
                break
            cand_lists.append(cands)
        if not ok:
            continue

        used = [False] * len(edges)

        def backtrack(step: int) -> bool:
            if step == n:
                return True
            for eidx in cand_lists[step]:
                if not used[eidx]:
                    used[eidx] = True
                    if backtrack(step + 1):
                        return True
                    used[eidx] = False
            return False

        if backtrack(0):
            return True
    return False


def verify_witness(name: str, n: int, raw_edges: list[set[int]], expect_linear: bool = False) -> None:
    assert n >= 6
    vertices = set(range(n))
    edges = [frozenset(e) for e in raw_edges]
    assert len(set(edges)) == len(edges), f"{name}: duplicate hyperedges"
    for e in edges:
        assert 1 <= len(e) <= 3, f"{name}: edge {e} has size outside [3]"
        assert e <= vertices, f"{name}: edge {e} outside V"

    if expect_linear:
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                assert len(edges[i] & edges[j]) <= 1, f"{name}: non-linear pair {edges[i]}, {edges[j]}"

    # 2-shadow simple graph
    adj: dict[int, set[int]] = {v: set() for v in range(n)}
    for e in edges:
        for u, v in itertools.combinations(sorted(e), 2):
            adj[u].add(v)
            adj[v].add(u)

    degs = [len(adj[v]) for v in range(n)]
    non_adj = [
        (u, v)
        for u in range(n)
        for v in range(u + 1, n)
        if v not in adj[u]
    ]
    assert len(non_adj) >= 1, f"{name}: expected non-adjacent pair"
    min_sum = min(degs[u] + degs[v] for u, v in non_adj)
    assert min_sum >= n + 1, f"{name}: Ore sum {min_sum} < {n + 1}"

    assert len(edges) < n, f"{name}: expected |E| < n"
    assert not has_hamiltonian_berge_cycle(n, edges), f"{name}: found Hamiltonian Berge cycle"

    print(
        f"{name} PASS: n={n}, |E|={len(edges)} < {n}, "
        f"shadow_degs={degs}, non_adj={non_adj}, min_non_adj_sum={min_sum} >= {n+1}, "
        f"hamiltonian_berge_cycle=False"
    )


def main() -> None:
    w1_edges = [{0, 1, 2}, {0, 1, 3}, {0, 2, 4}, {1, 2, 5}, {3, 4, 5}]
    verify_witness("Witness 1", 6, w1_edges, expect_linear=False)
    # Check shadow of Witness 1 is K_{2,2,2} (complement is matching of size 3)
    adj1 = {v: set() for v in range(6)}
    for e in w1_edges:
        for u, v in itertools.combinations(sorted(e), 2):
            adj1[u].add(v)
            adj1[v].add(u)
    comp_edges1 = {frozenset((u, v)) for u in range(6) for v in range(u + 1, 6) if v not in adj1[u]}
    assert comp_edges1 == {frozenset((0, 5)), frozenset((1, 4)), frozenset((2, 3))}

    w2_edges = [{0, 3, 4}, {0, 5, 6}, {1, 3, 5}, {1, 4, 6}, {2, 3, 6}, {2, 4, 5}]
    verify_witness("Witness 2", 7, w2_edges, expect_linear=True)
    print("PASS")


if __name__ == "__main__":
    main()
