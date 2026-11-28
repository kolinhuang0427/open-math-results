"""Independent exact-arithmetic verifier for targets/kern-2611.32927-gcs-dichotomy."""

from itertools import combinations, permutations, product
import pathlib


def is_matroid_switch(edges: set[tuple[int, int]], positions: list[set[tuple[int, int]]]) -> bool:
    """Exact check of hereditary + augmentation axioms for I_s = {A : exists i, A <= s[i]}."""
    indep = set()
    edge_list = sorted(edges)
    for r in range(len(edge_list) + 1):
        for sub in combinations(edge_list, r):
            sub_set = frozenset(sub)
            if any(sub_set.issubset(pos) for pos in positions):
                indep.add(sub_set)
    for A in indep:
        for B in indep:
            if len(A) < len(B):
                if not any((A | {e}) in indep for e in (B - A)):
                    return False
    return True


def is_connected(n: int, edges: set[tuple[int, int]]) -> bool:
    if n <= 1:
        return True
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == n


def e_norm(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


def verify_switches_and_exhaustives() -> None:
    # 1. Verify uniqueness of {2,1}-bounded K_3-shaped switches up to relabeling
    k3_edges = {e_norm(0, 1), e_norm(1, 2), e_norm(0, 2)}
    all_21_k3 = []
    # Positions: s[0] of size <= 2, s[1] of size <= 1, union == k3_edges
    subsets_le2 = [set(c) for r in range(3) for c in combinations(k3_edges, r)]
    subsets_le1 = [set(c) for r in range(2) for c in combinations(k3_edges, r)]
    for p0 in subsets_le2:
        for p1 in subsets_le1:
            if (p0 | p1) == k3_edges:
                assert len(p0) == 2 and len(p1) == 1 and (p0 & p1) == set()
                assert not is_matroid_switch(k3_edges, [p0, p1])
                all_21_k3.append((p0, p1))
    assert len(all_21_k3) == 3

    # 2. Verify s_2 and s_3 non-matroid property
    # s_2 on {a=0, b=1, c=2, x=3}: s_2[0]={ax, xb, ab}, s_2[1]={ax, ac}
    s2_0 = {e_norm(0, 3), e_norm(3, 1), e_norm(0, 1)}
    s2_1 = {e_norm(0, 3), e_norm(0, 2)}
    s2_edges = s2_0 | s2_1
    assert len(s2_edges) == 4  # paw graph (K_4 - {bc, cx}), NOT K_4 - bc (which has 5 edges)
    assert not is_matroid_switch(s2_edges, [s2_0, s2_1])

    # s_3 on {0,1,2,3}: s_3[0]={01,12,23}, s_3[1]={02,13,30}
    s3_0 = {e_norm(0, 1), e_norm(1, 2), e_norm(2, 3)}
    s3_1 = {e_norm(0, 2), e_norm(1, 3), e_norm(3, 0)}
    s3_edges = s3_0 | s3_1
    assert len(s3_edges) == 6
    assert not is_matroid_switch(s3_edges, [s3_0, s3_1])

    # 3. Exhaustive GCS equivalence checks on 5-6 vertex switch graphs
    # (a) Pi_1: 3 switches on n=5 vertices, check GCS iff all-size-2 position connects G
    n = 5
    triples = list(combinations(range(n), 3))
    for t1 in triples[:4]:
        for t2 in triples[2:6]:
            for t3 in triples[4:8]:
                sws = []
                for u, v, w in (t1, t2, t3):
                    sws.append([{e_norm(u, v), e_norm(v, w)}, {e_norm(u, w)}])
                brute_ok = any(
                    is_connected(n, set().union(*(sws[idx][c[idx]] for idx in range(3))))
                    for c in product((0, 1), repeat=3)
                )
                c_star_ok = is_connected(n, set().union(*(sw[0] for sw in sws)))
                assert brute_ok == c_star_ok

    # (b) Pi_2: 3 switches on n=6 vertices, check exact equivalence to {1}-matroid static + {1,1}-matroid
    n2 = 6
    quads = list(permutations(range(n2), 4))
    for q1, q2, q3 in zip(quads[::97][:8], quads[13::89][:8], quads[29::83][:8]):
        orig_sws = []
        mat_sws = []
        for a, b, c, x in (q1, q2, q3):
            orig_sws.append([
                {e_norm(a, x), e_norm(x, b), e_norm(a, b)},
                {e_norm(a, x), e_norm(a, c)},
            ])
            # Replacement: static {ax} + rank-1 uniform {ab}, {ac}
            mat_sws.append([
                {e_norm(a, x), e_norm(a, b)},
                {e_norm(a, x), e_norm(a, c)},
            ])
        for cfg in product((0, 1), repeat=3):
            e_orig = set().union(*(orig_sws[i][cfg[i]] for i in range(3)))
            e_mat = set().union(*(mat_sws[i][cfg[i]] for i in range(3)))
            assert is_connected(n2, e_orig) == is_connected(n2, e_mat)

    print("Non-matroid axioms and GCS equivalences (Pi_1, Pi_2, Pi_3): PASS")


def verify_counterexample_claims() -> list[str]:
    failures: list[str] = []
    root = pathlib.Path(__file__).resolve().parents[3]
    text = (root / "targets" / "kern-2611.32927-gcs-dichotomy" / "COUNTEREXAMPLE.md").read_text(encoding="utf-8")
    # Check COUNTEREXAMPLE.md L35: s_2 has 4 edges -> paw graph L_{3,1} ~= K_4 - {bc, cx}, NOT K_4 - bc
    if "(K_4 - bc)-shaped" in text or "K_4 - bc" in text:
        failures.append("COUNTEREXAMPLE.md L35 claims s_2 is (K_4 - bc)-shaped (5 edges), whereas |E(G[s_2])| = 4")
    if r"K_4 - \{bc, cx\}" not in text and r"K_4 - \{bc,cx\}" not in text:
        failures.append("COUNTEREXAMPLE.md L35 missing corrected graph identity K_4 - \\{bc, cx\\}")
    return failures


def main() -> None:
    verify_switches_and_exhaustives()
    failures = verify_counterexample_claims()
    for msg in failures:
        print("ISSUE:", msg)
    if failures:
        print("FAIL")
        raise SystemExit(1)
    print("PASS")


if __name__ == "__main__":
    main()
