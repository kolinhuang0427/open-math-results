---
source: https://oeis.org/A121751 (rev. 5)
status: reported
owner: scout-5
updated: 2026-11-27T09:37:00Z
identifiers: ["A121751", "R. J. Mathar", "D-finite", "deco polyominoes"]
---

# OEIS A121751 — Mathar (2022) D-Finite Recurrence Conjecture

## Exact Statement
From OEIS **A121751** (`NAME` and `FORMULA`, revision 5, offset `1,3`):
> **Name:** Number of deco polyominoes of height n in which all columns end at an even level. A deco polyomino is a directed column-convex polyomino in which the height, measured along the diagonal, is attained only in the last column.
> **Formula:** `Recurrence relation: a(n)=2floor((n-1)/2)a(n-1)-[floor((n-1)/2)floor((n-2)/2)-1]a(n-2) for n>=3, a(1)=0, a(2)=1.`
> **Formula (_R. J. Mathar_, Jul 26 2022):**
> `Conjecture D-finite with recurrence +256*a(n) -384*a(n-1) +16*(-8*n^2+40*n-67)*a(n-2) +16*(8*n^2-54*n+87)*a(n-3) +4*(4*n^4-56*n^3+242*n^2-304*n-21)*a(n-4) +4*(-2*n^4+38*n^3-249*n^2+647*n-554)*a(n-5) +(n-4)*(n-8)*(n^2-12*n+31)*a(n-6)=0.`

Explicitly, with $a(1) = 0$, $a(2) = 1$, and $a(n) = 2\lfloor\frac{n-1}{2}\rfloor a(n-1) - \bigl(\lfloor\frac{n-1}{2}\rfloor\lfloor\frac{n-2}{2}\rfloor - 1\bigr) a(n-2)$ for $n \ge 3$, the conjecture asserts that for all integers $n \ge 7$ (where all indices $n-6, \dots, n$ lie in the offset domain $\ge 1$),
$$
\begin{aligned}
256\, a(n) &- 384\, a(n-1) + 16(-8n^2 + 40n - 67) a(n-2) + 16(8n^2 - 54n + 87) a(n-3) \\
&+ 4(4n^4 - 56n^3 + 242n^2 - 304n - 21) a(n-4) \\
&+ 4(-2n^4 + 38n^3 - 249n^2 + 647n - 554) a(n-5) \\
&+ (n-4)(n-8)(n^2 - 12n + 31) a(n-6) = 0,
\end{aligned}
$$
and hence $a(n)$ is P-recursive (equivalently, its exponential generating function $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$ is D-finite).

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-27T09:30:00Z – 2026-11-27T09:37:00Z
- **Sources Checked:**
  - `tools/novelty_grep.py A121751`: 0 hits across 608 files.
  - `tools/arxiv_fetch.py query 'all:"A121751"'`: 0 hits.
  - Zenodo API (`curl` `https://zenodo.org/api/records?q=A121751`): 0 hits.
  - Crossref API (`https://api.crossref.org/works?query=A121751`): 0 hits.
  - GitHub (`gh search issues "A121751"`): 0 hits.
  - Web search (`"A121751" "D-finite" OR "Mathar" OR "recurrence"`): 0 proofs found; OEIS A121751 rev. 5 still lists Mathar's recurrence as `Conjecture`.
- **Verdict:** Open and unclaimed.
