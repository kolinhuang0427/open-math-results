# Target: mora-2112.08768-conj

- **Source:** Mercè Mora, María José Souto-Salorio, and Ana Dorotea Tarrío-Tobar, *Resolving sets tolerant to failures in three-dimensional grids*, `arXiv:2112.08768v1` (published in *Mediterr. J. Math.* **19** (2022), art. 188, `DOI:10.1007/s00009-022-02096-1`), Section 3 (Conjecture 21).
- **Status:** reported
- **Owner:** scout-9
- **Started (UTC):** 2026-11-27T18:36:15Z
- **Updated:** 2026-11-27T18:47:00Z
- **Identifiers:** `arXiv:2112.08768v1`, `DOI:10.1007/s00009-022-02096-1`, Section 3 Conjecture 21 (final Conjecture of the paper, lines 901–911 of `FaultTolerantMD-3DGrids-arxiv.tex`).

## Exact Quoted Statement

From `2112.08768.src` (`FaultTolerantMD-3DGrids-arxiv.tex`), Section 1 & Section 3 (`\alpha_m, \alpha_M` and Conjecture 21 at lines 635, 642, 901–911):

> Note that the set obtained after the removal of any $k$ vertices of a resolving set $S$ remains resolving if and only if every pair of vertices of the graph is resolved by at least $k+1$ distinct vertices of $S$. ... a set $S$ of vertices of a graph is a *$k$-resolving set* if for every pair of vertices $x$ and $y$, the vectors $r(x|S)$ and $r(y|S)$ have at least $k$ different coordinates. ... Whenever a graph $G$ has at least one $k$-resolving set, a $k$-resolving set of minimum cardinality is a *$k$-metric basis*, and its cardinality is the *$k$-metric dimension* of $G$, denoted by $\dim_k(G)$.
> ...
> $$\alpha_m(n_1,n_2,n_3) = 2(n_1+n_2+n_3)-8,$$
> $$\alpha_M(n_1,n_2,n_3) = \min \{ n_1(n_2+n_3-2), n_2(n_1+n_3-2), n_3(n_1+n_2-2) \}.$$
> ...
> \begin{conj} 
> If  $\alpha_m(n_1,n_2,n_3)\le k< \alpha_M(n_1,n_2,n_3)$, then 
> \begin{align*}
> &\dim_{k+1}(P_{n_1}\Box P_{n_2}\Box P_{n_3})=\\
> &=\min\{  4k-2\alpha_m(n_1,n_2,n_3)+4,n_1n_2n_3-(n_1-2)(n_2-2)(n_3-2) \}.
> \end{align*}	
> \end{conj}

## Gate 1 Novelty Receipt (`2026-11-27T18:36:05Z`)

- `ls targets/`: no folder matching `2112.08768`, `mora`, `resolving`, `grid`, `metric`.
- `tools/novelty_grep.py`: 0 matches across 760 snapshots for `2112.08768`, `three-dimensional grids`, `tolerant to failures`, `dim_{k+1}`.
- `gh search prs/issues/code`: 0 PRs, 0 issues, 0 matching math repositories.
- `Zenodo`: `0`; `OpenAlex`: `0`; `Crossref`: 4 citations for `10.1007/s00009-022-02096-1`; `arXiv:2112.08768v1` sole version.
- Web search: no follow-up proof or counterexample found.
