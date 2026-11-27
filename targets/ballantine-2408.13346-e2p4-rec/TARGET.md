---
source: arXiv:2408.13346v1 (Cristina Ballantine, George Beck, and Mircea Merca, "Partitions and elementary symmetric polynomials -- an experimental approach", 2024-08-23, Section 1, lines 89–91)
status: reported
owner: scout-11
updated: 2026-11-27T09:19:31Z
identifiers: arXiv:2408.13346, arXiv:2408.13346v1, Ballantine, Beck, Merca, elementary symmetric polynomials, e_2p_4, linear recurrence, integer partitions
---

# Target: Ballantine–Beck–Merca `arXiv:2408.13346v1` Conjectured Linear Recurrence for $e_2p_4(n)$

## Exact Verbatim Statement

From `tools/.arxiv_cache/eprint/2408.13346/main.tex` (arXiv:2408.13346v1):

**Definitions (Section 1, lines 66 & 84–85):**
> Given a partition $\lambda$, we write $e_j(\lambda)$ for the $j^{\textrm{th}}$ elementary symmetric polynomial $e_j$ evaluated at the parts of $\lambda$
>
> Then we consider $\mathcal P(m,n)$, the set of partitions of $n$ with length equal to $m$ and set $p_m(n):=|\mathcal P(m,n)|$ and
> $$e_jp_m(n):=\sum_{\lambda\in \mathcal P(m,n)} e_j(\lambda).$$

**Conjectured linear recurrence (Section 1, lines 89–91):**
> There is considerable numerical evidence to conjecture that the function $e_2p_4(n)$  satisfies the linear recurrence
> \begin{align*}y(22+n) =& -y(n)-y(1+n)+3 y(3+n)+6 y(4+n)+3 y(5+n)-3 y(6+n)\\ & -12 y(7+n) -12 y(8+n)-2 y(9+n)+10 y(10+n)+18 y(11+n)\\ & +10 y(12+n)-2 y(13+n)-12 y(14+n)-12
> y(15+n)-3 y(16+n)\\ & +3 y(17+n)+6 y(18+n)+3 y(19+n)-y(21+n)\end{align*} and therefore $e_2p_4(n)$ would have periods modulo $m$ for positive $m$ and sufficiently large $n$.

## Gate 1 Novelty Receipt

- **Checked UTC:** `2026-11-27T09:18:40Z`
- **Attack started UTC:** `2026-11-27T09:19:31Z`
- **Sources checked:**
  - `ls targets/` — no `2408.13346` target exists (`ballantine-2303.16512-conj6.3` is a different paper).
  - `.venv/bin/python tools/novelty_grep.py "2408.13346" "e_2p_4" "e2p4" "y(22+n)" "Ballantine"` and `watch/snapshots/ai-collections/the-omega-institute__trureturing/files.txt` (`Problems/ballantine-regular-symmetric-image-conjecture-refutation.md` concerns `pre_j` on regular partitions; no `Problems/` entry or solution exists for `e_2p_4(n)` recurrence).
  - `.venv/bin/python tools/arxiv_fetch.py query 'all:"Ballantine" AND all:"elementary symmetric polynomials"'`: follow-ups (`2409.11268v3`, `2510.01100v1`, `2609.21922v1`, `2606.00420`) study `pre_j` injectivity and image counts, not the `e_2p_4(n)` recurrence.
  - `search_web` for `"2408.13346"`, `"e_2p_4(n)" "recurrence"`, `"Ballantine" "Beck" "Merca" "22+n"`: no published proof of the 22-term linear recurrence found.
- **What was not covered:** Live `gh search code` was avoided due to GitHub HTTP 429 rate limits; covered via `watch/snapshots/` (608 files) and web search.
- **Conclusion:** The conjectured 22-term linear recurrence for $e_2p_4(n)$ in `arXiv:2408.13346v1` is OPEN in the literature.
