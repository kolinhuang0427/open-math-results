---
source: arXiv:2302.00757v2
status: reported
owner: scout-11
updated: 2026-11-27T03:56:00Z
identifiers: arXiv:2302.00757v2 Section 11.1 Conjecture 11.2
---

# Conjecture 11.2 of Cooper (arXiv:2302.00757v2)

## Verbatim Source Statement

From `/Users/kev/Documents/open-math/tools/.arxiv_cache/eprint/2302.00757/main.tex` (`arXiv:2302.00757v2`, Section 5 lines 1620–1632 and Section 11.1 lines 2557–2565):

Definition of $T_{11}(n)$ (Section 5, lines 1620–1632):
> ...the coefficients $T(n)$ in the expansion
> $$Z=\sum_{n=0}^\infty T(n)X^n$$
> satisfy the four-term recurrence relation
> \begin{align*}
> (n+1)^3T(n+1) &=2(2n+1)(5n^2+5n+2)T(n)  \\
> &\qquad -8n(7n^2+1)T(n-1)\\ 
> & \qquad\qquad +22n(2n-1)(n-1)T(n-2).
> \end{align*}
> The single initial condition $T(0)=1$ is enough to start the recurrence.
> It follows from the $q$-expansions for~$X$ and~$Z$ that $T(n)$ is always an integer.

where (lines 1611–1614):
> $$Z=\left(\sum_{j=-\infty}^\infty \sum_{k=-\infty}^\infty q^{j^2+jk+3k^2}\right)^2\quad\text{and}\quad X=\frac{\eta_1^2\eta_{11}^2}{Z}$$

Target Conjecture 11.2 (Section 11.1, lines 2557–2565; note `2302.00757/main.tex` uses `\newtheorem{conjecture}[theorem]{Conjecture}` with `\newtheorem{theorem}{Theorem}[section]`, and this is the second conjecture environment in Section 11):
> \begin{conjecture}
> $$
> T_{11}(3n) \equiv T_{11}(n) + 3n \pmod {3^2}
> $$
> and
> $$
> T_{11}(5n) \equiv T_{11}(n)  \pmod {5^2} \quad\mbox{if and only if $\;5|n$}.
> $$
> \end{conjecture}

*(Implicit quantifier from Section 11 preamble / lines 2539, 2555–2567: for all positive integers $n$; also note both congruences hold trivially at $n=0$ since $T_{11}(0)=1$.)*

## Gate 1 Novelty Receipt

- **Checked UTC:** 2026-11-26 22:50–23:18 UTC
- **Sources checked:**
  - `tools/novelty_grep.py "2302.00757" "Cooper" "5581" "LCM matrix" "2212.07726"` across all `watch/snapshots/**` (`1337-solved-conjectures`, `trureturing`, `openai-math`, `ai-collections`, `formal`, `discovered`, `arxiv`): 32 lines across 19/280 files, 0 hits for Shaun Cooper or `2302.00757`.
  - `tools/arxiv_fetch.py query 'abs:"2302.00757" OR (abs:"Cooper" AND abs:"four-term" AND abs:"supercongruence") OR abs:"5581"'`: returns `2302.00757v2` (updated 2024-05-08) and unrelated astro-ph/chem-ph papers; 0 follow-up papers settling Section 11. Also note `arXiv:2312.07134` line 108 explicitly cites Cooper's Section 11 supercongruences as open.
  - `search_web` for `"2302.00757" "proved" OR "counterexample" OR "5581" "Cooper"`: returns only `arXiv:2302.00757` itself.
  - Zenodo API (`https://zenodo.org/api/records?q=2302.00757`): `total: 0`.
  - Live `gh api`: `repos/aliromman/math/pulls?state=all` (pages 1–2) and `repos/aliromman/math/contents/conjectures` checked for `cooper|2302|00757|apery|5581|supercongruence` -> 0 matches.
- **Near misses:** Cooper's Section 5 conjecture on general mod-$p$ Lucas congruences (`T_{11}(n) \equiv \prod T_{11}(n_i) \pmod p`) and Conjecture 11.1 (`T_{11}(pn) \equiv T_{11}(n) \pmod{p^2}` for $p \in \{2, 59, 5581\}$) remain separate; we prove the mod-$3$ and mod-$5$ Lucas congruences unconditionally as lemmas en route to Conjecture 11.2.
- **Not covered:** Unindexed private preprints or paywalled journals not mirrored on arXiv, Zenodo, GitHub, or web search.
