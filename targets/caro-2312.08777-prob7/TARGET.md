# Target: caro-2312.08777-prob7

- **Source:** Yair Caro, Josef Lauri, Xandru Mifsud, Raphael Yuster, and Christina Zarb, *Flip colouring of graphs*, `arXiv:2312.08777v1` (2023-12-14; published in *Graphs and Combinatorics* 40 (106), 2024, `DOI:10.1007/s00373-024-02838-w`), Section 6 & Section 7 (final Problem).
- **Status:** reported
- **Owner:** scout-9
- **Started (UTC):** 2026-11-27T17:56:00Z
- **Updated (UTC):** 2026-11-27T18:08:00Z
- **Identifiers:** `arXiv:2312.08777v1`, `DOI:10.1007/s00373-024-02838-w`, Section 7 Problem 7 ($b(t)$ for $t$-neighbourhood flip graphs).

## Exact Quoted Statement

From `sections/section6.tex` (`arXiv:2312.08777v1`):

> We now extend our general flip colouring problem to $t$-neighbourhoods: Given a graph $G = (V, E)$, and $k, t \in \mathbb{N}$ such that $k \geq 2$, does there exist an edge-colouring $f \colon E(G) \to \{1, \dots, k\}$ such that for every vertex $v$
> - $\deg_j (v) > \deg_i (v)$ for $1 \leq i < j \leq k$ (forcing global majority $e_j (G) > e_i (G)$),
> - for $1 \leq s \leq t$, $e_{j,s} [v] < e_{i,s} [v]$ for $1 \leq i < j \leq k$ (forcing opposite majority order up to a distance $t$ from $v$, with respect to the global $e_j (G)$ and the local $\deg_j (v)$).
> ...
> As before, we shall mostly consider a more restricted version of this problem, where for every $j \in \{1, \dots, k\}$, the edge set $E(j)$ spans a regular subgraph of degree $a_j$, where $a_1 < a_2 < \dots < a_k$ and resulting in a $([t], (a_1, \dots, a_k))$-flip graph.

From `sections/section7.tex` (`arXiv:2312.08777v1`):

> Lastly, Section 6 dealt with the extension of the flip problem to the $t^\mathrm{th}$ neighbourhood. In particular we illustrated two distinct constructions for the case of two colours. Problems 1-5 naturally extend to this generalisation and remain to be studied. In particular, define $b(t) = \min\left\{ b \colon ([t], (b, r))\mathrm{-flip} \ \mathrm{graph} \ \mathrm{exists}\right\}$. Observe that for $t \geq 2$, the proof of Theorem \ref{CayleyTFlip} gives $b(t) \leq 2^{t+1} - 1$.
>
> \begin{problem*}
> For $t \in \mathbb{N}, t \geq 2$ determine $b(t)$.
> \end{problem*}

## Gate 1 Novelty Receipt (`2026-11-27T17:55:00Z`)

- `ls targets/`: no folder matching `caro`, `2312.08777`, `flip`, `mifsud`.
- `tools/novelty_grep.py`: 0 matches across 760 snapshot files for `b(t)` flip / `CayleyTFlip` / `PackingTFlip` / `2312.08777` / `t-neighbourhood flip`.
- `gh search prs/issues/code` for `CayleyTFlip OR PackingTFlip OR "b(t)" flip`: 0 matching PRs, issues, or code; `gh search code "2312.08777"` shows only `xmif1/geng_rc_graphs` and `10m-u/open-problems-catalog` (`Open`).
- `trureturing` (`dev` tree): no matching flip-graph files.
- `Zenodo`: `0` hits; `Crossref` (`10.1007/s00373-024-02838-w`): `0` citations; `arXiv:2312.08777v1` is sole version.
- Follow-up papers inspected directly via eprint (`arXiv:2401.02315` *Flip colouring of graphs II*, `arXiv:2507.14473` *Graphs With the Same Edge Count in Each Neighborhood*, `arXiv:2602.23517` *Regular $K_3$-regular graphs*): they address $h(b,r)$, $q(k)$, $m(k)$, $c$ in $a_3 \ge c a_1^2$, `spec(r)`, and NP-completeness of `2-FLIP`, and do **not** address $t$-neighbourhood flip graphs or $b(t)$.
- Web search: no resolution of $b(t)$ found.
