"""Independent exact-arithmetic verifier for targets/kern-2611.32927-wlcs-multipartite."""

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


def is_k2_plus_k2(edges: list[tuple[int, int]]) -> bool:
    norm = [tuple(sorted(e)) for e in edges]
    if len(norm) != 2 or norm[0] == norm[1]:
        return False
    return len({norm[0][0], norm[0][1], norm[1][0], norm[1][1]}) == 4


def is_k22(edges: list[tuple[int, int]]) -> bool:
    norm = {tuple(sorted(e)) for e in edges}
    if len(norm) != 4:
        return False
    verts = sorted({u for e in norm for u in e})
    if len(verts) != 4:
        return False
    for part_a in itertools.combinations(verts, 2):
        part_b = tuple(v for v in verts if v not in part_a)
        expected = {tuple(sorted((u, v))) for u in part_a for v in part_b}
        if norm == expected:
            return True
    return False


def reduce_lcs_to_wlcs(
    switches: list[list[list[tuple[int, int]]]],
) -> tuple[list[list[list[tuple[int, int]]]], list[list[int]]]:
    """Reduce {1^*}-bounded (K_2+K_2)-shaped LCS switches to K_{2,2}-shaped WLCS switches."""
    out_switches: list[list[list[tuple[int, int]]]] = []
    out_weights: list[list[int]] = []
    for sw in switches:
        distinct_edges: list[tuple[int, int]] = []
        seen_edges: set[tuple[int, int]] = set()
        for pos in sw:
            assert len(pos) <= 1, f"Switch position {pos} exceeds size 1"
            if len(pos) == 1:
                e = tuple(sorted(pos[0]))
                if e not in seen_edges:
                    seen_edges.add(e)
                    distinct_edges.append(e)
        assert is_k2_plus_k2(distinct_edges), f"Switch {sw} is not (K_2+K_2)-shaped"
        u, v = distinct_edges[0]
        x, y = distinct_edges[1]
        new_sw = [
            [(u, v)],
            [(x, y)],
            [(u, y)],
            [(x, v)],
        ]
        all_edges = [pos[0] for pos in new_sw]
        assert all(len(pos) == 1 for pos in new_sw)
        assert is_k22(all_edges)
        out_switches.append(new_sw)
        out_weights.append([0, 0, 1, 1])
    return out_switches, out_weights


def solve_lcs_exact(
    num_vertices: int,
    switches: list[list[list[tuple[int, int]]]],
    a: int,
    b: int,
) -> bool:
    ranges = [range(len(sw)) for sw in switches]
    for cfg in itertools.product(*ranges):
        edges: list[tuple[int, int]] = []
        for sw, idx in zip(switches, cfg):
            edges.extend(sw[idx])
        if is_connected_ab(num_vertices, edges, a, b):
            return True
    return False


def solve_wlcs_exact(
    num_vertices: int,
    switches: list[list[list[tuple[int, int]]]],
    weights: list[list[int]],
    lam: int,
    a: int,
    b: int,
) -> bool:
    ranges = [range(len(sw)) for sw in switches]
    for cfg in itertools.product(*ranges):
        total_w = sum(w[idx] for w, idx in zip(weights, cfg))
        if total_w > lam:
            continue
        edges: list[tuple[int, int]] = []
        for sw, idx in zip(switches, cfg):
            edges.extend(sw[idx])
        if is_connected_ab(num_vertices, edges, a, b):
            return True
    return False


def verify_reduction_exact() -> list[str]:
    failures: list[str] = []
    rng = random.Random(261132927)
    checked = 0
    saw_yes = 0
    saw_no = 0
    saw_false_positive_at_lam1 = 0

    for trial in range(120):
        n = rng.randint(5, 8)
        num_sw = rng.randint(1, 3)
        switches: list[list[list[tuple[int, int]]]] = []
        for _ in range(num_sw):
            v4 = rng.sample(range(n), 4)
            e1 = (v4[0], v4[1])
            e2 = (v4[2], v4[3])
            sw: list[list[tuple[int, int]]] = [[e1], [e2]]
            if trial % 3 == 0:
                sw.insert(0, [])
            if trial % 4 == 0:
                sw.append([e1])
            rng.shuffle(sw)
            switches.append(sw)

        a, b = rng.sample(range(n), 2)
        lcs_ans = solve_lcs_exact(n, switches, a, b)
        w_switches, weights = reduce_lcs_to_wlcs(switches)
        wlcs_lam0 = solve_wlcs_exact(n, w_switches, weights, 0, a, b)
        wlcs_lam1 = solve_wlcs_exact(n, w_switches, weights, 1, a, b)

        if lcs_ans != wlcs_lam0:
            failures.append(
                f"Trial {trial}: LCS={lcs_ans} != WLCS(lambda=0)={wlcs_lam0}"
            )
        if lcs_ans:
            saw_yes += 1
        else:
            saw_no += 1
            if wlcs_lam1:
                saw_false_positive_at_lam1 += 1
        checked += 1

    if saw_yes == 0 or saw_no == 0 or saw_false_positive_at_lam1 == 0:
        failures.append(
            f"Insufficient test coverage: yes={saw_yes}, no={saw_no}, lam1_fp={saw_false_positive_at_lam1}"
        )
    print(
        f"REDUCTION_EXACT: checked={checked}, yes={saw_yes}, no={saw_no}, lam1_false_positives={saw_false_positive_at_lam1}"
    )
    return failures


def verify_source_and_docs() -> list[str]:
    failures: list[str] = []
    root = pathlib.Path(__file__).resolve().parents[3]
    tar_path = root / "tools" / ".arxiv_cache" / "eprint" / "2611.32927.src"
    target_md = (
        root / "targets" / "kern-2611.32927-wlcs-multipartite" / "TARGET.md"
    ).read_text(encoding="utf-8")
    proof_md = (
        root / "targets" / "kern-2611.32927-wlcs-multipartite" / "PROOF.md"
    ).read_text(encoding="utf-8")

    if not tar_path.exists():
        print("[SKIP] local tools/.arxiv_cache not present; skipping TeX numbering check")
    else:
        with tarfile.open(tar_path, "r:*") as tf:
            main_tex = tf.extractfile("main-arxiv.tex").read().decode("utf-8")
            inputs = re.findall(r"\\input\{(sections/[^}]+)\}", main_tex)
            section_files: list[str] = []
            for rel_path in inputs:
                sec_tex = tf.extractfile(rel_path).read().decode("utf-8")
                if re.search(r"\\section\{", sec_tex):
                    section_files.append(rel_path)
        conclusion_idx = section_files.index("sections/conclusion.tex") + 1
        if f"Section {conclusion_idx}" not in target_md:
            failures.append(
                f"TARGET.md section mismatch: sections/conclusion.tex is Section {conclusion_idx} "
                f"(sections={section_files}), but TARGET.md cites Section 6"
            )

    if r"\tilde{s}[4]" in proof_md and r"c(s) = c'(\tilde{s})" in proof_md:
        failures.append(
            "PROOF.md index mismatch: L21 allows empty position at index 4 (\\tilde{s}[4]), "
            "which breaks exact index equality c(s) = c'(\\tilde{s}) in L28 if retained"
        )

    return failures


def main() -> int:
    failures = verify_reduction_exact() + verify_source_and_docs()
    if failures:
        for msg in failures:
            print(f"ERROR: {msg}")
        print("FAIL")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
