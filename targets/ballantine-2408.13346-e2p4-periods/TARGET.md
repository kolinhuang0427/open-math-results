---
source: arXiv:2408.13346v1 (Cristina Ballantine, George Beck, and Mircea Merca, "Partitions and elementary symmetric polynomials -- an experimental approach", 2024-08-23, Section 1, lines 93–97)
status: reported
owner: scout-11
updated: 2026-11-27T09:19:31Z
identifiers: arXiv:2408.13346, arXiv:2408.13346v1, Ballantine, Beck, Merca, elementary symmetric polynomials, e_2p_4, minimal period, counterexample
---

# Target: Ballantine–Beck–Merca `arXiv:2408.13346v1` Conjectural Table of Minimal Periods for $e_2p_4(n) \pmod m$

## Exact Verbatim Statement

From `tools/.arxiv_cache/eprint/2408.13346/main.tex` (arXiv:2408.13346v1):

**Definitions (Section 1, lines 66 & 84–85):**
> Given a partition $\lambda$, we write $e_j(\lambda)$ for the $j^{\textrm{th}}$ elementary symmetric polynomial $e_j$ evaluated at the parts of $\lambda$
>
> Then we consider $\mathcal P(m,n)$, the set of partitions of $n$ with length equal to $m$ and set $p_m(n):=|\mathcal P(m,n)|$ and
> $$e_jp_m(n):=\sum_{\lambda\in \mathcal P(m,n)} e_j(\lambda).$$

**Conjectural Table of Minimal Periods (Section 1, lines 93–97):**
> Below we give a conjectural table of minimal periods for certain values of $m$. 
> $$\begin{array}{c|cccccccccccccc}m & 2& 3& 4& 5 & 6& 7& 8 & 9&10&11&12&13&14     \\ \hline \text{period} & 48 & 54& 96& 300 & 432& 84& 192& 324& 1150& 132& 864 & 156& 336
> \end{array}$$
> $$\begin{array}{c|ccccccccccccc}m &16 &  17& 18& 19& 21& 22& 23& 26& 27& 28& 29& 31& 37 \\ \hline \text{period} & 384& 204& 1246 & 228& 756 & 528 & 276 & 624 & 972 & 672 & 348 & 372 & 444
> \end{array}$$

## Gate 1 Novelty Receipt

- **Checked UTC:** `2026-11-27T09:18:40Z`
- **Attack started UTC:** `2026-11-27T09:19:31Z`
- **Sources checked:**
  - `ls targets/` — no `2408.13346` target exists.
  - `.venv/bin/python tools/novelty_grep.py "2408.13346" "e_2p_4" "48 & 54" "1150" "1246"` and `watch/snapshots/ai-collections/the-omega-institute__trureturing/files.txt`: 0 matches for the `e_2p_4(n)` period table or its errors.
  - `.venv/bin/python tools/arxiv_fetch.py query 'all:"Ballantine" AND all:"elementary symmetric polynomials"'`: follow-ups study `pre_j` injectivity and image counts, not `e_2p_4(n)` minimal periods.
  - `search_web` for `"2408.13346"` with `"1150"`, `"1246"`, `"minimal periods"`, and `"e_2p_4(n)"`: no published correction or refutation of the `m=10` or `m=18` table entries found (the paper proves only `m=2, 3, 4` in Theorem 2 `\label{Th0}`).
- **What was not covered:** Live `gh search code` was avoided due to GitHub HTTP 429 rate limits; covered via `watch/snapshots/` (608 files) and web search.
- **Conclusion:** The conjectural table of minimal periods for $e_2p_4(n) \pmod m$ ($m \notin \{2,3,4\}$) in `arXiv:2408.13346v1` is OPEN in the literature.
