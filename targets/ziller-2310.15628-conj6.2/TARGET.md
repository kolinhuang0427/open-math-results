---
source: arXiv:2310.15628v2 (math.NT, Mario Ziller, v1 2023-10-24, v2 2026-04-15), Section 6 "Concluding remarks", Conjecture 6.2
status: reported
owner: scout-11
updated: 2026-11-27T02:56:00Z
identifiers: arXiv:2310.15628v2, Euler totient, varphi(x)/x^2, injectivity
---

# Target: Ziller `arXiv:2310.15628v2` Conjecture 6.2 ($\varphi(x)/x^2$ Distinct Values)

## Exact Verbatim Statement

From `tools/.arxiv_cache/eprint/2310.15628/Conclusions.tex` (Section 6 "Concluding remarks", lines 89–91; numbered via `\newtheorem{conj}[defi]{Conjecture}` with `\newtheorem{defi}{Definition}[section]` in `Ziller_2023_v2.tex` lines 28–30 after `\stepcounter{section}` increments section from 5 to 6 and resets `defi` to 0):

> **Conjecture 6.2.**
> All function values of ${\displaystyle\frac{\varphi(x)}{x^2}}$ for $x\in\mathbb{N}$ are pairwise distinct.

Where `Ziller_2023_v2.tex` line 116 defines:
> Henceforth, we denote the set of integral numbers by $\mathbb{Z}$ and the set of natural numbers, i.e. positive integers, by $\mathbb{N}$.

And `Examples.tex` line 296 defines $\varphi(x) = \bigl|\{k \in \mathbb{N} \le x : k \perp x\}\bigr| = x \prod_{p \mid x} (1 - \frac{1}{p})$. (Line 98 of `Conclusions.tex` also notes the equivalent reciprocal claim for $x^2/\varphi(x)$.)

## Gate 1 Novelty Receipt

- **Checked UTC:** `2026-11-27T02:35:00Z` – `2026-11-27T02:54:00Z`
- **Sources checked:**
  - Primary paper `arXiv:2310.15628v2` (updated `2026-04-15T17:18:47Z`), `Examples.tex` lines 327–345 and `Conclusions.tex` lines 32, 79, 89–91, 98: author proves only the coprime/squarefree special case and explicitly leaves the general conjecture open as Conjecture 6.2 in v2.
  - `.venv/bin/python tools/novelty_grep.py 2310.15628 "varphi(x)/x^2" "phi(x)/x^2" "Ziller"` across 413 snapshot files: 16 hits all concerning an unrelated `Gerbicz u(n), Ziller` table for Erdős Problem 854.
  - `.venv/bin/python tools/arxiv_fetch.py query '(ti:Ziller OR all:2310.15628) OR ...'` and `'(all:"phi(n)/n^2" OR all:"varphi(x)/x^2" OR all:"varphi(n)/n^2") OR (all:"totient" AND all:"distinct" AND all:"x^2")'`: no matches resolving injectivity of $\varphi(x)/x^2$.
  - Zenodo API (`https://zenodo.org/api/records?q=2310.15628`): 0 hits.
  - Crossref API (`https://api.crossref.org/works?query="2310.15628"` and `"phi(n)/n^2 injective"`): no mathematical matches (unrelated 15628/$\phi$X174 hits; `Ziller` / `varphi` queries returned HTTP 429).
  - Read-only GitHub (`gh search code` on `aliromman/math`, `KnowledgeSense/math`, `the-omega-institute/trureturing`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, plus global `gh search code/issues/prs`): `the-omega-institute/trureturing#24177` only cites `2310.15628` as a citing paper of Mohan Lal (1969) in an OEIS A349824 check, with no mention of $\varphi(x)/x^2$; all other repos have 0 hits.
  - `search_web` queries for `2310.15628`, `"Mario Ziller"`, `"varphi(x)/x^2"`, `"phi(n)/n^2 injective"`, and `MathOverflow`/`MathStackExchange`: no proof or disproof found.
- **What was not covered:** Offline/paywalled problem books not indexed by web search, arXiv full-text TeX of arbitrary unrelated papers not containing `phi(n)/n^2` / `varphi(x)/x^2` / `2310.15628` in metadata.
