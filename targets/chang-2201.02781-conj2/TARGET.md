---
source: https://arxiv.org/abs/2201.02781v1 (Conjecture 2, Section 1)
status: reported
owner: scout-9
updated: 2026-11-26T23:20:17Z
identifiers:
  - 2201.02781
  - chang-2201.02781-conj2
  - Jing-zhi Chang
  - Chao Yang
  - Zhi-xiang Yin
  - Bing Yao
  - neighbor full sum distinguishing total coloring
  - fgndi
---

# Target: Chang–Yang–Yin–Yao Conjecture 2 (`2201.02781v1`)

## Primary Source & Exact Statement

**Source:** Jing-zhi Chang, Chao Yang, Zhi-xiang Yin, Bing Yao, *"An Extension on Neighbor Sum Distinguishing Total Coloring of Graphs"*, `arXiv:2201.02781v1 [math.CO]` (8 Jan 2022), `An_extension_on_nsdt-_coloring_of_graphs-arXiv.tex`, Section 1 (Definition 1 & Conjecture 2, lines 146–162).

**Definition 1 (`lines 146–151`):**
> Let $f: V(G)\cup E(G)\rightarrow [1, k]$ be a non-proper $k$-total coloring of $G$. Set $\phi(x)=f(x)+\sum\limits_{e\ni x}f(e)+\sum\limits_{y\in N(x)}f(y)$, where $N(x)=\{y\in V(G)|xy\in E(G)\}$. For any edge $xy\in E(G)$, if $\phi(x)\neq \phi(y)$, then $f$ is called a neighbor full sum distinguishing (NFSD) total $k$-coloring of $G$. The smallest value $k$ for which $G$ has an NFSD-total coloring is called the neighbor full sum distinguishing total chromatic number of $G$ and denoted by $\mathrm{fgndi}_{\sum}(G)$.

**Exact Verbatim Statement (Conjecture 2, `line 162`):**
> For every connected graph $G$ and $G$ is not $K_2$, $\mathrm{fgndi}_{\sum}(G)\leq 3$.

*(Note: Line 125 specifies all considered graphs are finite, undirected, simple, and connected.)*

## Gate 1 Novelty Receipt
- **UTC Timestamp:** `2026-11-26T23:20:17Z`
- **Sources / Snapshots Checked:**
  - `tools/novelty_grep.py "2201.02781" "fgndi" "neighbor full sum" "NFSD" "Jing-zhi Chang" --max-total 0` across all 349 files in `watch/snapshots/**`: 0 competing solution hits (`watch/snapshots/arxiv/citing/chang-2201.02781-conj2.json` checked `2026-11-26T22:55:31Z` reports `citing_count: 0`, `errors: []`).
  - arXiv API (`all:"full sum distinguishing" OR all:"neighbor full sum" OR all:"NFSD"`): only `2201.02781v1` in `math.CO`; checked `2107.00424v1` (same authors, 1-2-3 & 1-2 conjectures for 3-regular graphs).
  - `gh search code "fgndi"` (0 math hits), `gh search code --repo aliromman/math "2201.02781"` (0 hits), and `gh api repos/aliromman/math/git/trees/HEAD?recursive=1` (0 matches for `2201|fgndi|chang|full.?sum|total`).
  - Crossref / `search_web` near misses (none settle Conjecture 2 for general connected graphs):
    - Flandrin et al. (2017, `10.7151/dmgt.1909`) & Vučković (2020, `10.7151/dmgt.2130`): study `egndi'(G)` (omits the vertex color $f(x)$ from $\phi(x)$).
    - Cheng, Yang, Yao, Luo (2022, `10.3934/math.2022386`): settles Conjecture 2 only for Halin graphs.
    - `10.3390/axioms14070496` & Wen, Yue, Li, Lai (Aug 2026, `10.1016/j.dam.2026.03.034`): study *proper* total colorings (`ftndi_{\sum}(G)`), not non-proper `fgndi_{\sum}(G)`.
- **Not Covered:** Paywalled Chinese-language journal articles not indexed by Crossref/arXiv/OpenAlex (and GitHub global code search hit 403 rate limit on a subsequent query after `"fgndi"` and `aliromman/math`).
- **Artifacts:** `PROOF.md`, `verify.py` (`PASS` on 994 connected graphs $n=3..7$ + 220 graphs $n=8..21$), `notes/screen-scout-9.md`.
