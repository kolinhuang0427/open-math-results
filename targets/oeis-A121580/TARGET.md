---
source: https://oeis.org/A121580 (rev. 12)
status: reported
owner: scout-5
updated: 2026-11-27T09:29:00Z
identifiers: ["A121580", "R. J. Mathar", "D-finite", "deco polyominoes", "Emeric Deutsch"]
---

# OEIS A121580 — Mathar (2022) D-Finite Recurrence Conjecture

## Exact Statement
From OEIS **A121580** (`NAME` and `FORMULA`, revision 12, offset `1,2`):
> **Name:** Number of cells in column 1 of all deco polyominoes of height n. A deco polyomino is a directed column-convex polyomino in which the height, measured along the diagonal, is attained only in the last column.
> **Formula:** `a(1) = 1, a(n) = a(n-1)+(n-1)!*(1+n*(n-1)/2) for n>=2.`
> **Formula (_R. J. Mathar_, Jul 26 2022):**
> `Conjecture D-finite with recurrence a(n) +(-n-4)*a(n-1) +3*(n+1)*a(n-2) +2*(-2*n+3)*a(n-3) +2*(n-3)*a(n-4)=0.`

Explicitly, with $a(1) = 1$ and $a(n) = a(n-1) + (n-1)!\bigl(1 + \frac{n(n-1)}{2}\bigr)$ for all integers $n \ge 2$, the conjecture asserts that for every integer $n \ge 5$ (where all indices $n-4, \dots, n$ lie in the offset domain $\ge 1$),
$$
a(n) + (-n-4)a(n-1) + 3(n+1)a(n-2) + 2(-2n+3)a(n-3) + 2(n-3)a(n-4) = 0,
$$
and hence $a(n)$ is P-recursive (equivalently, its exponential generating function $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$ is D-finite).

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-27T09:26:00Z – 2026-11-27T09:29:00Z
- **Sources Checked:**
  - `tools/novelty_grep.py A121580`: 0 hits across 608 files.
  - `tools/arxiv_fetch.py query 'all:"A121580" OR ...'`: 0 hits.
  - Zenodo API (`curl` `https://zenodo.org/api/records?q=A121580`): 0 hits.
  - Crossref API (`https://api.crossref.org/works?query=A121580`): 0 hits.
  - GitHub (`gh search issues "A121580"`): 0 hits.
  - Web search (`"A121580" OR "A045742" "D-finite" OR "Mathar" OR "recurrence"`): 0 proofs found; OEIS A121580 rev. 12 still lists Mathar's recurrence as `Conjecture`.
- **Verdict:** Open and unclaimed.
