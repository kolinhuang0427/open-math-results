---
source: https://oeis.org/A121584 (rev. 4)
status: reported
owner: scout-5
updated: 2026-11-27T09:34:00Z
identifiers: ["A121584", "R. J. Mathar", "D-finite", "deco polyominoes"]
---

# OEIS A121584 — Mathar (2022) D-Finite Recurrence Conjecture

## Exact Statement
From OEIS **A121584** (`NAME` and `FORMULA`, revision 4, offset `1,2`):
> **Name:** Number of cells in columns 1 and 2 of all deco polyominoes of height n. A deco polyomino is a directed column-convex polyomino in which the height, measured along the diagonal, is attained only in the last column.
> **Formula:** `a(1)=1, a(2)=4, a(n)=[(2n-3)a(n-1)-(n-1)a(n-2)]/(n-2) + (1/2)(2n^3-9n^2+17n-16)(n-1)!/(n-2) for n>=3.`
> **Formula (_R. J. Mathar_, Jul 26 2022):**
> `Conjecture D-finite with recurrence 14*(-n+1)*a(n) +(14*n^2+1731*n-6995)*a(n-1) +3*(-577*n^2+480*n+7243)*a(n-2) +2*(2781*n^2-11952*n+6004)*a(n-3) +(-5987*n^2+36181*n-54220)*a(n-4) +2*(1071*n-3433)*(n-4)*a(n-5)=0.`

Explicitly, with $a(1) = 1$, $a(2) = 4$, and $a(n) = \frac{(2n-3)a(n-1)-(n-1)a(n-2)}{n-2} + \frac{1}{2}(2n^3-9n^2+17n-16)\frac{(n-1)!}{n-2}$ for $n \ge 3$, the conjecture asserts that for every integer $n \ge 6$ (where all indices $n-5, \dots, n$ lie in the offset domain $\ge 1$),
$$
\begin{aligned}
14(-n+1)a(n) &+ (14n^2+1731n-6995)a(n-1) + 3(-577n^2+480n+7243)a(n-2) \\
&+ 2(2781n^2-11952n+6004)a(n-3) + (-5987n^2+36181n-54220)a(n-4) \\
&+ 2(1071n-3433)(n-4)a(n-5) = 0,
\end{aligned}
$$
and hence $a(n)$ is P-recursive (equivalently, its exponential generating function $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$ is D-finite).

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-27T09:26:00Z – 2026-11-27T09:34:00Z
- **Sources Checked:**
  - `tools/novelty_grep.py A121584`: 0 hits across 608 files.
  - `tools/arxiv_fetch.py query 'all:"A121580" OR all:"A121584" OR ...'`: 0 hits.
  - Zenodo API (`curl` `https://zenodo.org/api/records?q=A121584`): 0 hits.
  - Crossref API (`https://api.crossref.org/works?query=A121584`): 0 hits.
  - GitHub (`gh search issues "A121584"`): 0 hits.
  - Web search (`"A121584" "D-finite" OR "Mathar" OR "recurrence"`): 0 proofs found; OEIS A121584 rev. 4 still lists Mathar's recurrence as `Conjecture`.
- **Verdict:** Open and unclaimed.
