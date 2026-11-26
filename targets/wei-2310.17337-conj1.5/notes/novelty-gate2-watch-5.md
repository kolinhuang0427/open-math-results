# Gate 2 Novelty Receipt — `wei-2310.17337-conj1.5`

- **UTC Time:** 2026-11-26T20:02:00Z
- **Reviewer:** `watch-5` (arXiv & citing-papers slice)
- **Verdict:** **PASS** (no arXiv preprint, journal paper, or OpenAlex citing work found settling Wei–Zhang–Zhao Conjecture 1.5 for general $k \ge 5$)

## Sources & Exact Queries Checked

1. **Local arXiv snapshot (`watch/snapshots/arxiv/recent_arxiv.json`, 440 recent papers across `math.CO`, `math.NT`, `cs.DM`, `math.GR`):**
   - Keyword scan for `2310.17337`, `isolation`, `c_k-isolation`, `c_4-isolation`, `xiaohua wei`, `gang zhang`, `biao zhao`.
   - Matches: `2611.19361v1` (*Distance-2 isolation of connected graphs*), `2611.17489v1` (*Isolation of k-cliques in uniform hypergraphs*) — neither settles $C_k$-isolation.
2. **Live arXiv API via `tools/arxiv_fetch.py` (`use_cache=False`):**
   - `id_list=["2310.17337"]` -> remains `2310.17337v1` (`2023-10-26T12:05:14Z`), no `v2` or erratum/refutation comment.
   - `all:2310.17337 OR all:"C_4-isolation" OR all:"C_k-isolation" OR all:"C4-isolation" OR all:"Ck-isolation"` (`max_results=20`) -> returned only `2310.17337v1`.
   - `cat:math.CO AND all:isolation AND all:cycle` (`max_results=25`, `sort_by="submittedDate"`) -> returned 25 papers (most recent `2611.29409v1`, `2611.24477v2`, `2611.19361v1`, etc.); none address $C_k$-isolation for $k \ge 5$ or refute Conjecture 1.5.
3. **OpenAlex live API (`https://api.openalex.org/works`):**
   - `search="2310.17337"` -> `0` results (`citing/wei-2310.17337-conj1.5.json` also `0`).
   - `search="On the C_4-isolation number of a graph"` -> `0` relevant graph-theory hits.
   - `search="C4-isolation number of a graph"` -> matched the published journal version **`W7163506673`** (*"On the C4-isolation number of a graph"*, `2026-07-21`, DOI `https://doi.org/10.1142/s1793830926500679`, `cited_by_count=3`).
   - `filter=cites:W7163506673` (all 3 citing works):
     1. `10.1016/j.dam.2026.08.006` (Peter Borg & Dayle Scicluna, `2026-08-21`, *"Isolation of non-triangle cycles in graphs"*)
     2. `10.1016/j.dam.2025.06.058` (Yanfang Liang & Baoyindureng Wu, `2025-07-15`, *"Cycle isolation in graphs"*)
     3. `10.12677/aam.2025.149398` (`2025-01-01`, *"Total Isolation Number of the Cartesian Product of Paths and Cycles"*)
   - `search="C_k-isolation"` and `search="isolation number cycle"` -> checked top results (`W4391604362`, `W4401221723`, `W4406915096`, `W4387641696`, `W4414069928`).
4. **Web search (`search_web`):**
   - `"C_4-isolation" OR "C4-isolation" OR "C_k-isolation" OR "Ck-isolation" "Wei" "Zhang" "Zhao" OR "m+1" "k+2"`
   - `"iota(G, C_k)" OR "C_k-isolating" OR "cycle isolation" "truncated tetrahedron" OR "(m+1)/(k+2)" OR "disprove" OR "counterexample"`
   - `"Cycle isolation in graphs" "10.1016/j.dam.2025.06.058" OR "Discrete Applied Mathematics" "Cycle isolation" 2025 OR 2026`
   - `("Wei, Zhang, and Zhao" OR "Wei, Zhang and Zhao" OR "2310.17337") ("Conjecture 1.5" OR "counterexample" OR "refute" OR "disprove" OR "false" OR "C_5" OR "C_8")`
   - `("C_8-isolation" OR "C_5-isolation" OR "C_6-isolation" OR "C_7-isolation" OR "C8-isolation" OR "C5-isolation") graph "m+1"`

## Near Misses (Why They Do Not Settle Conjecture 1.5)

- **Borg & Scicluna (`10.1016/j.dam.2026.08.006` / `arXiv:2510.08361`):** Proves $\iota(G, \mathcal{C}') \le (m+1)/6$ where $\mathcal{C}' = \{C_k : k \ge 4\}$ (isolating *all* non-triangle cycles simultaneously), which implies the $k=4$ case $\iota(G, C_4) \le (m+1)/6$ of Wei–Zhang–Zhao, and does not prove or refute $\iota(G, C_k) \le (m+1)/(k+2)$ for individual $k \ge 5$.
- **Liang & Wu (`10.1016/j.dam.2025.06.058`, *Discrete Appl. Math.* 378, 2026, *"Cycle isolation in graphs"*):** Proves $\iota_c(G) \le (m+1)/5$ for isolating *all* cycles in connected $G \ncong C_3$, and conjectures $\iota_c(G) \le (m+1)/(g+2)$ where $g$ is the girth of $G$ (a girth-restricted all-cycle bound, not individual $C_k$-isolation in arbitrary connected graphs that may contain triangles like the truncated tetrahedron).
- **Total isolation of $P_m \square C_n$ (`10.12677/aam.2025.149398`):** Studies total isolation number on Cartesian products of paths and cycles, not $C_k$-isolation.
- **Borg & Kaemawichanurat (`arXiv:2611.19361v1`) and Li, Zhang, Qu (`arXiv:2611.24477v2`):** Study distance-2 isolation and uniform hypertree / triangle-block cycle isolation by order $n$, not size-based $C_k$-isolation for $k \ge 5$.

## What Was Not Covered

- Semantic Scholar live API (unauthenticated rate-limited HTTP 429).
- Closed-access full text of *Discrete Applied Mathematics* / *Discrete Mathematics* articles whose abstracts were not indexed in OpenAlex (`10.1016/j.dam.2025.01.037`, `10.1007/s40840-024-01655-x`), though web search found no mention of refuting Wei–Zhang–Zhao Conjecture 1.5 or using the truncated tetrahedron.
- GitHub / competing conjecture repositories (covered separately by `watch-1` and `watch-6`).
