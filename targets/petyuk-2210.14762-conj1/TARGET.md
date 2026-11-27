---
source: https://arxiv.org/abs/2210.14762v2 (Conjecture 1, Section 4)
status: reported
owner: scout-9
updated: 2026-11-27T01:00:28Z
identifiers:
  - 2210.14762
  - petyuk-2210.14762-conj1
  - Anthony V. Petyuk
  - simplified de Bruijn graph
  - word-representable graph
---

# Target: Petyuk Conjecture (`2210.14762v2`)

## Primary Source & Exact Statement

**Source:** Anthony V. Petyuk, *"On word-representability of simplified de Bruijn graphs"*, `arXiv:2210.14762v2 [math.CO]` (v1 20 Oct 2022, v2 12 Jul 2023), `simplified_de_Bruijn_graphs__4_.tex`, Section 1.2 & Section 4 (lines 65–68, 123).

**Definition (`Section 1.2, lines 65–67`):**
> Let $A=\{0,1,\ldots,k-1\}$ be a $k$-letter alphabet and $A^n$ be the set of all words over $A$ of length $n$. A *de Bruijn graph* $B(n,k)$ consists of $k^n$ vertices labeled by words in $A^n$ and its directed edges are $x_1x_2\cdots x_n\rightarrow x_2\cdots x_nx_{n+1}$ where $x_i\in A$ for $i\in\{1,2,\ldots,n+1\}$. ...
> The *simplified de Bruijn graph* $S(n,k)$ is a simple graph obtained from $B(n,k)$ by removing orientations and loops and replacing multiple edges between a pair of vertices by a single edge.

**Exact Verbatim Statement (`Section 4, Conjecture 1, line 123`):**
> $S(n,k)$ is non-word-rerpesentable for $n\geq 4$ and $k\geq 3$.

*(Note: "non-word-rerpesentable" is a literal typo for "non-word-representable" in the primary source.)*

## Gate 1 Novelty Receipt
- **UTC Timestamp:** `2026-11-27T01:00:28Z`
- **Sources / Snapshots Checked:**
  - `tools/novelty_grep.py "2210.14762" "Petyuk" "simplified de Bruijn"`: 0 lines across 0/357 files in `watch/snapshots/**`.
  - arXiv API (`all:"simplified de Bruijn" OR all:"word-representability of simplified"`): returned `2210.14762v2` (Petyuk), `2312.10377v1` (Huang–Kitaev–Pyatkin, *Discrete Appl. Math.*, proves results only on distance-restricted $S_m(n,k)$ and explicitly states Petyuk's Conjecture as open), and `2605.02268v2` (Roy–Hariharasubramanian, May 2026, proves shift graphs $G(n,k)$ are word-representable and cites only Petyuk 2022 and Huang–Kitaev–Pyatkin 2024 for $S(n,k)$).
  - `gh api 'repos/aliromman/math/git/trees/HEAD?recursive=1'` tree grep for `2210|petyuk|bruijn|word.?rep`: 0 matches.
  - `search_web`: only references `2210.14762` and `2312.10377` (no resolution of $S(n,k)$ for $n\ge 4, k\ge 3$).
  - Crossref API (`simplified+de+Bruijn`): 0 mathematical resolutions (second query hit HTTP 429).
- **Not Covered:** Unindexed 2025–2026 papers not on arXiv or in `search_web` summaries.
- **Artifacts:** `COUNTEREXAMPLE.md`, `verify.py` (`PASS`), `notes/screen-scout-9.md`.
