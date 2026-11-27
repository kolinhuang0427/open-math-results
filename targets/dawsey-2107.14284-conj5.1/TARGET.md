---
source: arXiv:2107.14284v2 (math.NT; J. Number Theory 241 (2022), 120–141), Section 4 (`\label{sect5}`), Conjecture 4.1 (`\label{conj1}`)
status: reported
owner: scout-11
updated: 2026-11-27T09:04:44Z
identifiers: arXiv:2107.14284v2, supernormal partition statistic, Dawsey-Just-Schneider, prime zeta Abelian theorem
---

# Target: Dawsey–Just–Schneider `arXiv:2107.14284v2` Conjecture 4.1 (`\label{conj1}`)

*(Note: folder slug `dawsey-2107.14284-conj5.1` retains `conj5.1` from the TeX section label `\label{sect5}`; in `arXiv:2107.14284v2`, this is Section 4, Conjecture 4.1.)*

## Exact Verbatim Statement

From `tools/.arxiv_cache/eprint/2107.14284/main.tex` (Section 4 `"Supernormal" maps and Abelian-type conjectures` (`\label{sect5}`), lines 1083–1086; `\newtheorem{conjecture}{Conjecture}[section]`):

> **Conjecture 4.1 (`\label{conj1}`).**
> For $f(n)$ an arithmetic function, if the limit of the average value $L_f=\lim_{N\to \infty}\frac{1}{N}\sum_{k=1}^{N} f(k)$ exists, then 
> $$\lim_{s\to 1^+}\  \frac{\sum_{p\in \mathbb P} f\left(\mathrm{idx}(p)\right)p^{-s}}{\sum_{p\in \mathbb P} p^{-s}}\  \   =\  \  L_f.$$

With primary-source definitions (`main.tex` lines 113, 126, 1053):
- $\mathbb{N} = \{1, 2, 3, \dots\}$ and $\mathbb{P} = \{p_1 < p_2 < p_3 < \dots\}$ is the increasing sequence of prime numbers ($p_1=2, p_2=3, p_3=5, \dots$);
- $\mathrm{idx}(p_k) := k$ is the index of the $k$-th prime ($k \ge 1$);
- $f \colon \mathbb{N} \to \mathbb{C}$ is an arithmetic function whose Cesàro mean $L_f = \lim_{N \to \infty} \frac{1}{N} \sum_{k=1}^N f(k) \in \mathbb{C}$ exists.

## Gate 1 Novelty Receipt

- **Checked UTC:** `2026-11-27T06:10:00Z` – `2026-11-27T07:07:00Z`
- **Sources checked:**
  - `.venv/bin/python tools/novelty_grep.py 2107.14284 "supernormal" Dawsey Schneider "idx(p)"` across 522 snapshot files: 5 hits (`DawseyPartitionPolynomialDerivativeQuestionRefutation` in `the-omega-institute/trureturing`, which concerns `arXiv:2108.00943`, unrelated).
  - `.venv/bin/python tools/arxiv_fetch.py query` for `all:"supernormal"` (15 results), `au:Dawsey OR (au:Just AND au:Schneider)` (20 results): inspected `2308.15303v1` (Lagarias–Sun, reciprocal supernorm size asymptotics), `2501.00580v3` (Botkin–Dawsey–Hemmer–Just–Schneider, prime-gap model citing `2107.14284v1` only for the appendix), and `2011.08386` (Schneider, *Ramanujan J.* 2024, cited as `[Robert_abelian]` *prior* to `2107.14284` posing Conj 5.1). None settles Conjecture 5.1.
  - Zenodo API (`https://zenodo.org/api/records?q=2107.14284`): 0 hits (`"A supernormal partition statistic"` returned 0 relevant math hits).
  - Crossref API (`2107.14284`) and `search_web` for `"2107.14284"`, `"A 'supernormal' partition statistic"`, `"Dawsey" "Just" "Schneider" "Conjecture 5.1"`, `"Botkin" "Dawsey" "Hemmer" "Just" "Schneider"`: confirmed published in *J. Number Theory* 241 (2022), 120–141; no subsequent proof of Conjecture 5.1 found.
  - Read-only GitHub (`gh search code` globally for `2107.14284`, `"supernormal" "partition"`, plus per-repo checks on `aliromman/math`, `KnowledgeSense/math`, `the-omega-institute/trureturing`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `1337isnot1337/solved-conjectures`, `JENW1N/complete-math-solutions`, `linustalacko/small-true-things`, `chy4pro/automath`): `epoch-research/LeanOpenProblems-results` has `2107.14284` only in an unrelated `nt_ids.txt` bibliography file; `the-omega-institute/trureturing`'s `lagarias-sun-2024-supernorm-size-asymptotic.md` is about `2308.15303v1` Conjecture 3.5; `idx(p)` and `2107.14284` have 0 matches in all competing repos.
- **What was not covered:** Paywalled *J. Number Theory* 241 (2022) 120–141 PDF itself (only `2107.14284v2` arXiv TeX + abstract/citing summaries inspected).
