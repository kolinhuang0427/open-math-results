# Target: `jensen-2605.27941-ques4`

- **Source:** Alathea Jensen, *Mixed thresholds in the Lonely Runner Conjecture*, `arXiv:2605.27941v1` [math.NT], May 27, 2026 (`main.tex`, Section 5 "Open questions and future work", lines 1158–1163, Question 4).
- **Status:** reported
- **Owner:** scout-10
- **Started:** 2026-11-27T17:09:02Z
- **Updated:** 2026-11-27T17:25:00Z
- **Identifiers:** `arXiv:2605.27941v1`, `MLPS_k`, `MLPS_2`, `Question 4`

## Gate 1 Novelty Receipt (`2026-11-27T17:09Z`)
- `ls targets/`: only `jensen-2605.27941-ques2` exists (`jensen-2605.27941-ques4` absent; Question 4 is a distinct open question not claimed elsewhere).
- `.venv/bin/python tools/novelty_grep.py "2605.27941" "MLPS" "finitely many speed sets" "Alathea Jensen"`: `0` hits across `744` snapshot files.
- `gh search {issues,prs,code} --repo the-omega-institute/trureturing` for `"2605.27941"`, `"Alathea Jensen"`, `"MLPS"`: `0` matches.
- Global `gh search`: `0` issues and `0` PRs for `"2605.27941"`; code hits are background/reading notes (`eliottcassidy2000/math`, `maximilianbehr/OpenTorus`, `ChinSookLing/together-mailbox`), none resolving Question 4.
- Zenodo API (`https://zenodo.org/api/records?q=2605.27941`): `total: 0`.
- arXiv `2605.27941`: single version `v1` (27 May 2026).
- Web search (`"Alathea Jensen" "Mixed thresholds in the Lonely Runner Conjecture" OR "2605.27941"`): only Jensen's `2605.27941v1` preprint and summaries; Question 4 remains OPEN.

## Verbatim Problem Statement
From `main.tex`, Section 2 (`\label{sec:mixed-loneliness}`, lines 191–223) and Section 5 (`\label{sec:future-work}`, lines 1158–1163):

> **Definition 1 (Mixed Lonely Runner Conjecture).** For $\mathbf d=(d_1,\ldots,d_k)\in(0,1/2]^k$, we write $\mathsf{MLRC}(\mathbf d)$ for the following statement:
> For every tuple of distinct positive integer speeds $(s_1,\ldots,s_k)$, there exists a time $t\in\mathbb{R}$ such that
> $$\|s_i t\|\geq d_i \qquad\text{for each }i=1,\ldots,k,$$
> where $\|x\|:=\min_{m\in\mathbb{Z}}|x-m|$.
>
> **Definition 2 (Mixed Loneliness Parameter Space).** For each $k\geq 1$, define
> $$\mathsf{MLPS}_k := \left\{\mathbf d\in(0,1/2]^k : \mathsf{MLRC}(\mathbf d)\text{ holds}\right\}.$$
>
> **Context (lines 1158–1159):** Another question concerns the obstructions that define these spaces. In dimension two, the whole space is constrained by the two ordered speed pairs $(1,2)$ and $(2,1)$. It would be useful to know whether higher-dimensional spaces are similarly governed by a finite number of speed sets. If true, this would also imply that the parameter spaces are finite unions of convex sets.
>
> **Question 4 (lines 1161–1163):**
> For fixed $k$, is $\mathsf{MLPS}_k$ determined by finitely many speed sets?
