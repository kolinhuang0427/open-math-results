---
source: https://arxiv.org/abs/2604.12864v1 (Ethan Ackelsberg and Florian K. Richter, "An inverse theorem for sumsets of sets of positive density in the integers", April 2026, Section 16.1, Question 16.4)
status: reported
owner: scout-10
updated: 2026-11-27T11:03:30Z
identifiers:
  - arXiv:2604.12864v1
  - Ethan Ackelsberg
  - Florian K. Richter
  - Question 16.4
  - Kneser's theorem in N^2
  - H_{a,b,c}
---

# Ackelsberg & Richter (2026), Question 16.4 (`Kneser's theorem in \N^2`)

- **Started:** 2026-11-27T11:02:09Z

## Exact Statement

Primary source: `arXiv:2604.12864v1`, extracted TeX `InverseProblemDensity_arXiv_v1.tex`, Section 1 (`\N = \{1, 2, 3, \ldots\}`, line 398) and Section 16 (`\section{Further explorations}`, `\subsection{More on direct theorems for sumsets in the integers}`, lines 5759–5777; `\newtheorem{Question}[Theorem]{Question}` at line 129 with `\counterwithin{Theorem}{section}` at line 162 gives number **Question 16.4**, following Question 16.1 `q_logarithmic_density_Kneser` at line 5724, Example 16.2 at line 5732, and Question 16.3 at line 5747):

> We define
> \[
> \liminf_{n,m\to\infty} a_{n,m}= \lim_{N\to\infty}\Bigg(\inf_{\substack{n\geq N\\m\geq N}} a_{n,m}\Bigg).
> \]
> The *lower density* of a set $A\subset \mathbb{N}^2$ is given by
> \[
> \underline{d}(A)=\liminf_{n,m\to\infty} \frac{|A\cap ([n]\times [m])|}{nm}.
> \]
> Note that all finite-index subgroups of $\mathbb{Z}^2$ are of the form $H_{a,b,c}=\{(an+bm,cm): m,n\in\mathbb{Z}\}$ for some $a,c\in\mathbb{N}$ and $b\in\{0,1,\ldots,a-1\}$.
>
> **Question 16.4 (Kneser's theorem in $\mathbb{N}^2$).**
> If $A, B \subseteq \mathbb{N}^2$ are non-empty sets then either
> \[
> \underline{d}(A+B)\geq \underline{d}(A)+\underline{d}(B),
> \]
> or there exists $H=H_{a,b,c}\cap (\mathbb{N}\times \mathbb{N})$ for some $a,c\in\mathbb{N}$ and $b\in\{0,1,\ldots,a-1\}$ such that $A+B$ equals, up to finitely many elements, a finite union of translates of $H$ and $\underline{d}(A+B)=d(A+H)+d(A+H)-d(H)$.

*(Note: `[N] = \{1,\ldots,N\}` by line 405, and $\mathbb{N} = \{1,2,3,\ldots\}$ by line 398. Also, as in Theorem `thm_Kneser_for_integers` line 421, the last display contains `d(A+H)+d(A+H)-d(H)` in place of `d(A+H)+d(B+H)-d(H)`; choosing $A = B$ makes both expressions identical, and the counterexample breaks the preceding structural condition "equals, up to finitely many elements, a finite union of translates of $H$" directly.)*

## Gate 1 Novelty Receipt

- **Checked UTC:** 2026-11-27T11:02:42Z
- **`tools/novelty_grep.py`:** `.venv/bin/python tools/novelty_grep.py "2604.12864" "H_{a,b,c}" "Kneser's theorem in" "Ackelsberg"` -> 10 lines across 5/635 files (`watch/snapshots/ai-collections/plasma-ai__erdos/...` referencing the main Erdős #335 inverse theorem, and `watch/snapshots/formal/formal-conjectures-prs.{json,tsv}` PR #8236 addressing **Question 16.9** on $d$-essential components only; `0` hits on Question 16.4 / $H_{a,b,c}$ / $\mathbb{N}^2$ Kneser).
- **arXiv API (`tools/arxiv_fetch.py`):** `query --id-list 2604.12864` confirms `2604.12864v1` (2026-04-14) is the sole version; `query 'all:"2604.12864"'` returned only `2604.12864v1` (`0` citing preprints).
- **GitHub (`gh search`):** `gh search code "2604.12864"` returned 39 hits (all Erdős #335 repositories, `plasma-ai/erdos`, `latexml-oxide` parser tests — none on Question 16.4); `gh search issues "2604.12864"` returned `no issues`; `gh search code '"Question 16.4" "2604.12864"'` returned `no code results`; `gh search issues '"Kneser'\''s theorem in" "2604.12864"'` returned `no issues`.
- **Zenodo API & Web Search:** `https://zenodo.org/api/records?q=2604.12864` returned `total: 0`; web search returned only `arXiv:2604.12864v1` itself and Erdős #335 summaries.
- **Verdict:** Open (passes Gate 1).
