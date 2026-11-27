---
source: arXiv:2603.04876v1
status: reported
owner: attack-5
updated: 2026-11-27T05:47:00Z
identifiers:
  - arXiv:2603.04876v1
  - 2603.04876
  - Biswas
  - Mandal
  - Saha
  - Conjecture 5.5
  - RV_chordal
  - v-number
---

# Conjecture 5.5 of Biswas–Mandal–Saha (arXiv:2603.04876v1)

**Primary Source:** Prativa Biswas, Mousumi Mandal, and Kamalesh Saha, *"Lattice points arising from regularity and $\mathrm{v}$-number of Graphs: Whisker and Cameron-Walker"*, `arXiv:2603.04876v1` (submitted 5 Mar 2026, `math.AC` / `math.CO`), Section 5 (`Arxiv.tex` lines 980–983).

## Exact Verbatim Conjecture Statement (`Arxiv.tex` lines 980–983)

> **Conjecture 5.5:** For the class of connected chordal graphs on $n\geq 3$ vertices, we have
> $$\mathcal{RV}_{\mathrm{chordal}}(n)=\left\{(r,v)\in \mathbb{N}^{2} \mid 1\leq r<\frac{n}{2}, 1\leq v\leq r-\left\lceil\frac{r}{n-2r}\right\rceil+1\right\}.$$

## Definitions (`lines 250–346`)

- $\mathcal{RV}(n) = \{(\mathrm{reg}(R/I(G)), \mathrm{v}(I(G))) : G \text{ connected on } n \text{ vertices}\}$, and $\mathcal{RV}_{\mathrm{chordal}}(n)$ restricts to connected chordal graphs.
- For any chordal graph $G$, $\mathrm{reg}(G) = \mathrm{im}(G)$ (induced matching number, Theorem 2.11 / Hà–Van Tuyl).
- $\mathrm{v}(G) = \min\{|A| : A \subseteq V(G) \text{ independent and } N_G(A) \text{ is a vertex cover of } G\}$ (Definition 2.4 / Jaramillo–Villarreal).
- Note: Theorem 3.5 (`thm:RV(n)`) already proves the right-hand set $A(n) \subseteq \mathcal{RV}_{\mathrm{chordal}}(n)$, so the conjecture asserts the reverse inclusion: every connected chordal graph $G$ on $n \ge 3$ vertices satisfies $\mathrm{v}(G) \le r - \lceil r / (n - 2r) \rceil + 1$ where $r = \mathrm{im}(G)$.

## Gate 1 Novelty Receipt

- **Checked at:** `2026-11-26T16:10:24Z`–`16:14:20Z` (`2026-11-27T00:10Z`–`00:14Z` UTC)
- **Local snapshots (`watch/snapshots/**`):** `.venv/bin/python tools/novelty_grep.py 2603.04876 Biswas "RV(n)" "RV_{chordal}" "v-number" "Cameron-Walker"` -> 0 hits for Biswas / `RV(n)` / `RV_{chordal}` (only unrelated `ArtificialZeng` v-number under integral closure items).
- **arXiv:** `.venv/bin/python tools/arxiv_fetch.py query 'all:2603.04876 OR all:"Lattice points arising from regularity and"'` -> only `2603.04876v1`.
- **Zenodo API:** `https://zenodo.org/api/records?q=%222603.04876%22+OR+%22Lattice+points+arising+from+regularity%22` -> 0 hits.
- **GitHub (`gh search` & `gh api`):** `gh search repos "2603.04876"` (0), `gh search code "2603.04876"` (only BibTeX/RSS/index mirrors and unrelated numeric data), `aliromman/math/contents/conjectures` (no match).
- **Web (`search_web`):** Query `"2603.04876" OR "Lattice points arising from regularity and v-number of Graphs" OR ("RV_chordal" "v-number")` -> returned only `arXiv:2603.04876`.
- **Not covered:** Off-arXiv manuscripts or private repos.
