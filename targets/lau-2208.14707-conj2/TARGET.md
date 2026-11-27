---
source: arXiv:2208.14707v1 (math.CO), Abstract & Section 2, Conjecture 2.2 (also Discrete Mathematics Letters 11 (2023), 76-83, DOI:10.47443/dml.2022.149)
status: reported
owner: scout-9
updated: 2026-11-27T09:11:19Z
identifiers:
  - arXiv:2208.14707v1
  - lau-2208.14707-conj2
  - 10.47443/dml.2022.149
  - local antimagic chromatic number
  - lexicographic product
---

# Target: Lau–Shiu–Premalatha–Zhang–Nalliah (2022/2023) `arXiv:2208.14707v1`, Conjecture 2.2

## Start Time
- **Screening started (UTC):** `2026-11-27T09:10:44Z`

## Verbatim Statement

From `tools/.arxiv_cache/eprint/2208.14707/A_note_on_local_antimagic_chromatic_number_of_lexicographic_product_graphs.tex` (Section 2 end, line 819 `\begin{conjecture}`; also Abstract line 208 and Introduction line 240):

> **Conjecture 2.2.** For $k\ge 1$ and graph $G$ and $H$, $\chi_{la}(G[H]) = \chi(G)\chi(H)$ if and only if $\chi(G)\chi(H) = 2\chi(H) + \lceil\frac{\chi(H)}{k}\rceil$, where $2k+1$ is the length of a shortest odd cycle in $G$.

Primary definitions (`tools/.arxiv_cache/eprint/2208.14707/A_note_on_local_antimagic_chromatic_number_of_lexicographic_product_graphs.tex`, Abstract & Section 1, lines 218–236):
- **Graphs considered** (lines 218, 226, 236): Simple graphs $G = (V, E)$ (connected simple graphs of order $p$ and size $q$; "two disjoint non-null graphs $G$ and $H$").
- **Local antimagic labeling and $\chi_{la}(G)$** (lines 219–223): A bijection $f : E \to \{1, 2, \dots, q\}$ is a *local antimagic labeling* of $G$ if $f^+(u) \ne f^+(v)$ holds for any two adjacent vertices $u$ and $v$, where $f^+(u) = \sum_{e \in E(u)} f(e)$ and $E(u)$ is the set of edges incident to $u$. Clearly, a local antimagic labeling induces a proper coloring of $G$. The function $f$ is called a *local antimagic $t$-coloring* of $G$ if $f$ induces a proper $t$-coloring of $G$, and $c(f) = t$. The *local antimagic chromatic number*, denoted $\chi_{la}(G)$, is the minimum number of $c(f)$, where $f$ takes over all local antimagic labelings of $G$.
- **Lexicographic product $G[H]$** (lines 228–231): The *lexicographic product* $G[H]$ of graphs $G$ and $H$ is the graph with vertex set $V(G) \times V(H)$ in which any two vertices $(u, u')$ and $(v, v')$ are adjacent iff either $uv \in E(G)$, or $u = v$ and $u'v' \in E(H)$.

## Gate 1 Novelty Receipt

- **Checked UTC:** `2026-11-27T09:11:19Z`
- **Local snapshots (`watch/snapshots/**`):** `.venv/bin/python tools/novelty_grep.py 2208.14707 "dml.2022.149" "Gee-Choon" "Wai-Chee" "Premalatha" "Nalliah" "local antimagic"` returned `1` line across `1/607` files (`kyleglsn22-spec__open-problems-lab.json` mentioning unrelated Bača et al. 2022 leaf conjecture for local antimagic colouring of trees); `0` hits for `2208.14707`, `dml.2022.149`, or lexicographic products.
- **Existing targets:** No `targets/*2208.14707*` or `targets/*lau*` folder existed prior to claim.
- **arXiv API (`tools/arxiv_fetch.py`):**
  - `query("", id_list="2208.14707")`: latest version is `2208.14707v1` (2022-08-31).
  - `query('all:"local antimagic chromatic number"')`: 15 results returned (`2610.22808v2`, `2610.22783v1`, `2610.14486v1`, etc.); none addresses `G[H]` lexicographic product Conjecture 2 (`2610.14486v1` is Middle Graph and Direct Product).
- **GitHub (`gh search`):** `gh search repos "2208.14707"` returned 0 results.
- **Web searches (`search_web`):**
  - `"2208.14707" OR "local antimagic chromatic number of lexicographic product graphs" conjecture`
  - `"Gee-Choon Lau" "Wai-Chee Shiu" "lexicographic product" "local antimagic" 2022 OR 2023 OR 2024 OR 2025 OR 2026`
  - `"2*chi(H)" OR "local antimagic chromatic number of lexicographic product" "conjecture" counterexample OR solved`
  - `"dml.2022.149" OR "10.47443/dml.2022.149" OR "2208.14707" counterexample OR false`
  - Confirmed published in *Discrete Mathematics Letters* 11 (2023), 76–83 (`10.47443/dml.2022.149`) with the identical conjecture stated as open; no refutation of Conjecture 2 was found.
- **Coverage note:** Non-indexed private repos or papers behind paywalls not mentioning `2208.14707` / `dml.2022.149` in indexed abstracts/snippets are not covered.
