source: https://arxiv.org/abs/2508.04602v1 (Hong Duc Bui, "On existence of a compatible triangulation with the double circle order type", Section 8.2 "Matching Problem and Acyclicity of State Graph", lines 1188–1217)
status: reported
label: Lean-checked
lean: lean/OpenMath/Bui250804602Conj81.lean
owner: scout2-5
updated: 2026-11-27T11:01:00Z
identifiers: ["2508.04602", "2508.04602v1", "Hong Duc Bui", "double circle order type", "compatible triangulation", "acyclicity of state graph"]

# Hong Duc Bui (2025) — Acyclicity of Triangle-Matching Flip Graph (`conjecture` in §8.2)

- **Started:** 2026-11-27T09:01:45Z

## Exact Statement
From `tools/.arxiv_cache/eprint/2508.04602/article.tex`, Section 8.2 (*Matching Problem and Acyclicity of State Graph*, lines 1188–1212):

Let $Q$ be a planar point set in general position with $|Q|=2n$ and $|\mathrm{CH}(Q)|=n$, with convex hull vertices $Q_1,\dots,Q_n$ in cyclic order (indices modulo $n$) and interior points $B_1,\dots,B_n$.
Represent a matching where hull edge $Q_i Q_{i+1}$ is matched to interior point $B_{\pi_i}$ by a permutation $\pi = (\pi_1,\dots,\pi_n)$ of $(1,\dots,n)$. Define the directed graph $G$ as follows:
- The vertices are all $n!$ permutations of $(1,\dots,n)$;
- For two permutations $\pi$ and $\rho$, there is a directed edge from $\pi$ to $\rho$ if and only if there are two indices $i \neq j$ such that $\pi_i = \rho_j$, $\pi_j = \rho_i$, $\pi_k = \rho_k$ for all $k \in \{1,\dots,n\}\setminus\{i,j\}$, and triangles $Q_i B_{\pi_i} Q_{i+1}$ and $Q_j B_{\pi_j} Q_{j+1}$ intersect.

> **Conjecture (Section 8.2, lines 1194–1196, 1211).**
> The algorithm described above always terminates; equivalently, the directed graph $G$ is acyclic for all order types $Q$ in general position (with $|Q|=2n$ and $|\mathrm{CH}(Q)|=n$).

*(Verified by the author for $n \le 5$, i.e. $2n \le 10$; open for $n \ge 6$.)*

## Gate 1 Novelty Receipt
- **Checked UTC:** 2026-11-27T09:03:00Z
- **`tools/novelty_grep.py`:** `.venv/bin/python tools/novelty_grep.py "2508.04602" "Hong Duc Bui" "double circle order type" "triangles intersect"` returned 1 hit across 601 files in `watch/snapshots/**`, solely the arXiv license metadata file `AlexenderSokolov__cross-theory-formal-database` (`arxiv-2508.04602-CC-BY-4.0.txt`).
- **`search_web`:** Returned `arXiv:2508.04602v1` itself; `site:github.com "2508.04602" OR ("Hong Duc Bui" "acyclic" "compatible triangulation")` returned 0 solutions/repos addressing the §8.2 acyclicity conjecture.
- **arXiv API (`arxiv_fetch.py`):** `query --id-list 2508.04602` confirms `2508.04602v1` (2025-08-06) is the sole version; `query 'abs:"2508.04602"'` returned 0 citing preprints.
- **What was not covered:** `gh search code` was rate-limited (HTTP 429; 37s cooldown at 09:04:42Z — Gate 2 `@watch-1` to complete live `gh search code` check) and unindexed preprints/repos.
- **Verdict:** Open (passes Gate 1). Complete proof written in `PROOF.md` with exact-integer verification (`PASS`, 68 instances $n=3..7$, 180,598 edges) in `verify.py`.
