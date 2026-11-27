# Target: `jensen-2605.27941-ques2`

- **Source:** Alathea Jensen, *Mixed thresholds in the Lonely Runner Conjecture*, `arXiv:2605.27941v1` [math.NT], May 27, 2026 (`main.tex`, Section 5 "Open questions and future work", lines 1138–1140, Question 2).
- **Status:** reported
- **Owner:** scout-10
- **Started:** 2026-11-27T16:42:47Z
- **Updated:** 2026-11-27T17:09:00Z
- **Identifiers:** `arXiv:2605.27941v1`, `MLPS_k`, `MLPS_3`, `Question 2`

## Gate 1 Novelty Receipt (`2026-11-27T16:42Z`)
- `ls targets/`: 0 matches (`jensen-2605.27941-ques2` absent).
- `.venv/bin/python tools/novelty_grep.py "2605.27941" "MLPS" "Mixed thresholds in the Lonely Runner"`: 0 hits across 742 snapshot files.
- `gh search {issues,prs,code} --repo the-omega-institute/trureturing "2605.27941"`: 0 matches.
- Global `gh search`: `2605.27941` gives 0 issues, 0 PRs, 36 code hits (all literature lists / reading notes in `eliottcassidy2000/math`, `ChinSookLing/together-mailbox`, `kavanaghpatrick/aristotle-math-problems`, `tradingartofwar/the-lonely-runner-conjecture`, `veenrek/openwiki`, `maximilianbehr/OpenTorus`, `mountain/process-geometry`; none resolving Question 2); `"Alathea Jensen"` gives 0 PRs, 1 unrelated Sage issue `#28256`, 28 code hits (faculty lists / citations); `"MLPS_k"` / `"7/20" "13/90"` gave 0/timeout/rate-limit.
- Zenodo API (`2605.27941` and `"Mixed thresholds in the Lonely Runner Conjecture"`): `total: 0`.
- arXiv `2605.27941`: single version `v1` (27 May 2026).
- Web search (`"2605.27941" OR "Mixed thresholds in the Lonely Runner Conjecture" "Alathea Jensen"` and `"13/90" "7/20" "MLPS"`): only Jensen's `2605.27941v1` preprint and mirror; Question 2 remains OPEN.

## Verbatim Problem Statement
From `main.tex`, Section 2 (`\label{sec:mixed-loneliness}`, lines 191–223) and Section 5 (`\label{sec:future-work}`, lines 1134–1140):

> **Definition (Mixed Lonely Runner Conjecture).** For $\mathbf d=(d_1,\ldots,d_k)\in(0,1/2]^k$, we write $\mathsf{MLRC}(\mathbf d)$ for the following statement:
> For every tuple of distinct positive integer speeds $(s_1,\ldots,s_k)$, there exists a time $t\in\mathbb{R}$ such that
> $$\|s_i t\|\geq d_i \qquad\text{for each }i=1,\ldots,k,$$
> where $\|x\|:=\min_{m\in\mathbb{Z}}|x-m|$.
>
> **Definition (Mixed Loneliness Parameter Space).** For each $k\geq 1$, define
> $$\mathsf{MLPS}_k := \left\{\mathbf d\in(0,1/2]^k : \mathsf{MLRC}(\mathbf d)\text{ holds}\right\}.$$
>
> **Context (lines 1134–1137):** Nevertheless, it is still possible that after exclusion of points in the coordinate planes, $\mathsf{MLPS}_3$ could be convex, or a union of convex sets. The author has not yet found any counterexamples.
> A possible counterexample to convexity of $\mathsf{MLPS}_3$ might be the following. The author has computational evidence, but not a complete proof, that $\left(\frac{7}{20},\frac{1}{5},\frac{13}{90}\right)$ and $\left(\frac{1}{20},\frac{1}{3},\frac{3}{10}\right)$ are likely in $\mathsf{MLPS}_3$. Their midpoint, $\left(\frac{1}{5},\frac{4}{15},\frac{2}{9}\right)$, however, is not in $\mathsf{MLPS}_3$, which can be shown using the speed set $(2,1,3)$.
>
> **Question 2 (lines 1138–1140):**
> For $k\geq 3$, off of the coordinate planes, is $\mathsf{MLPS}_k$ convex, or a finite union of convex sets?
