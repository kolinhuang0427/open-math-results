# bartnicki-2303.08771-conj3

- source: Tomasz Bartnicki, Sebastian Czerwiński, Jarosław Grytczuk, Zofia Miechowicz, "Strong arboricity of graphs", arXiv:2303.08771v1 [math.CO] (2023-03-15), Section 3 (Final remarks and open problems), Conjecture 3; also published in *Graphs and Combinatorics* 41 (2025), Art. 80 (DOI: 10.1007/s00373-025-02934-5, pp. 7–8)
- status: reported
- owner: scout-9
- updated: 2026-11-27T09:26:00Z
- started: 2026-11-27T09:21:51Z
- identifiers: arXiv:2303.08771v1, 10.1007/s00373-025-02934-5, math.CO

## Exact Statement

From `tools/.arxiv_cache/eprint/2303.08771/Zlamasy_III_11.tex`, Section 3 ("Final remarks and open problems", lines 248–252; also *Graphs and Combinatorics* 41 (2025), Art. 80, pp. 7–8):

> It is known that every graph $G$ with $\mathrm{arb}(G)=k$ is at most $(2k-1)$-degenerated. Recall that the *coloring number* $\mathrm{col}(G)$ is the least integer $r$ for which there is a vertex ordering with maximum back-degree equal to $r-1$. This leads to the following stronger conjecture.
>
> **Conjecture.** Every graph $G$ satisfies $\zeta(G)\leqslant \mathrm{col}(G)$.

### Primary Definitions (Section 1, lines 86–101; Section 3, line 248)

- A coloring of the edges of a simple graph $G$ is *woody* if every color class forms a forest (contains no monochromatic cycles).
- A subgraph $B$ of a simple graph $G$ is a *broken cycle* if $B = C - e$ for some cycle $C$ and some edge $e \in E(C)$.
- An edge coloring of $G$ is *strongly woody* if no broken cycle is monochromatic (equivalently, it is a woody coloring that remains woody in $G/e$ after contracting any single edge $e$).
- The *strong arboricity* $\zeta(G)$ is the least number of colors needed for a strongly woody edge coloring of $G$.
- The *coloring number* $\mathrm{col}(G)$ is the least integer $r$ for which there is a vertex ordering with maximum back-degree equal to $r-1$ (equivalently, $\mathrm{col}(G) = 1 + \max_{H \subseteq G} \delta(H)$, i.e., degeneracy plus $1$).

## Gate 1 Novelty Check

- `tools/novelty_grep.py "strong arboricity" "broken cycle" "Bartnicki" "Grytczuk" "2303.08771"`: 0 matching targets/files for `2303.08771` or strong arboricity (7 hits across 3 snapshot files for unrelated Grytczuk papers).
- `ls targets/`: no prior target for `bartnicki` or `2303.08771` other than our own `bartnicki-2303.08771-conj1` (parked).
- `gh search repos "2303.08771" --limit 5`: 0 matching repositories.
- `tools/arxiv_fetch.py query --id-list 2303.08771`: `2303.08771v1` only (published 2023-03-15, no newer version, no journal_ref/doi).
- Web search (`"Strong arboricity of graphs" Bartnicki OR "2303.08771"`, `"strong arboricity" planar OR "broken cycle" arboricity conjecture`, `"Strong arboricity" "Bartnicki" OR "Grytczuk" "zeta(G)" OR "broken cycle" 2024 OR 2025 OR 2026`): confirms published in *Graphs and Combinatorics* 41 (2025), Art. 80 (`DOI: 10.1007/s00373-025-02934-5`, OpenAlex `W4411944715`, `cited_by_count = 0`) with Conjecture 3 retained verbatim and still open.
