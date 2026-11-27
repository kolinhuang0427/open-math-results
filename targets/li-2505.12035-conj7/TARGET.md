source: arXiv:2505.12035v1 (Yupei Li, Linyuan Lu, Ruth Luo, "An Ore-type theorem for $[3]$-graphs", 2025-05-17)
status: reported
owner: scout-7
updated: 2026-11-26T23:31:00Z
identifiers: 2505.12035, 2505.12035v1, Li, Lu, Luo, Ore-type, [3]-graph, Berge cycle, conj:ore, Conjecture 7

## Exact Statement (arXiv:2505.12035v1, Section 1, Conjecture 7 / `conj:ore`)

> **Conjecture 7 (`conj:ore`).** Let $n\geq 6$, and let $\mathcal{H}$ be a $[3]$-graph on $n$ vertices such that every pair $u,v \in V(\mathcal{H})$ of non-adjacent vertices satisfies $d_{\partial \mathcal{H}}(u) + d_{\partial \mathcal{H}}(v) \geq n+1$. Then $\mathcal{H}$ contains a Hamiltonian Berge cycle.

*(Definitions in Section 1: a $[3]$-graph is a hypergraph in which every edge contains at most $3$ vertices; vertices $u,v$ are adjacent iff $\{u,v\} \subseteq h$ for some $h \in E(\mathcal{H})$; $\partial\mathcal{H}$ is the simple $2$-uniform shadow graph on $V(\mathcal{H})$ with edge $uv$ iff $u,v$ are adjacent; a Hamiltonian Berge cycle is an alternating sequence of $n$ distinct vertices and $n$ distinct hyperedges $e_1,\dots,e_n \in E(\mathcal{H})$ with $\{v_i, v_{i+1}\} \subseteq e_i$ for all $i \in [n]$.)*

## Gate 1 Novelty Receipt
- **UTC timestamp:** 2026-11-26T23:27:00Z
- **Local snapshots (`tools/novelty_grep.py`):** Queries `2505.12035`, `"Ore-type"`, `"Berge cycle"`, `"Linyuan Lu"` returned 4 unrelated hits (`Linyuan Lu` 2008 Folkman graphs, `2611.33694v1` positive curvature, 0 hits for `2505.12035` or Berge-Ore).
- **GitHub & `trureturing` (`gh api`):**
  - `search/issues?q="2505.12035"+OR+"Ore-type+theorem+for"`: `0`.
  - `search/issues?q=Luo+Berge+Ore`: `0`.
  - `search/repositories?q="2505.12035"+OR+"Ore-type"`: unrelated TypeScript/OReilly repos only.
  - `search/code?q=repo:the-omega-institute/trureturing+2505.12035`, `...+Ore-type+Berge`, `search/commits?q=repo:the-omega-institute/trureturing+2505.12035`: all `0`. `search/code?q=repo:the-omega-institute/trureturing+Luo+Berge` returned 1 unrelated file (`Problems/sun-luo-ye-2020-projection-matrix-amgm.md`).
- **Web search (`search_web`):** Query `"2505.12035" OR "An Ore-type theorem for [3]-graphs" Berge cycle conjecture solved OR counterexample` returned only the original May 2025 preprint; conjecture remains open.
