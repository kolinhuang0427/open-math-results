---
source: https://oeis.org/A121747 (rev. 15)
status: reported
owner: scout-5
updated: 2026-11-27T09:44:00Z
identifiers: ["A121747", "R. J. Mathar", "D-finite", "deco polyominoes"]
---

# OEIS A121747 — Mathar (2022) D-Finite Recurrence Conjecture

## Exact Statement
From OEIS **A121747** (`NAME` and `FORMULA`, revision 15, offset `1,2`):
> **Name:** Number of columns of odd length in all deco polyominoes of height n. A deco polyomino is a directed column-convex polyomino in which the height, measured along the diagonal, is attained only in the last column.
> **Formula:** `Recurrence relation: a(n)=n*a[n-1]-d(n-1)+(n-1)!*floor(n/2) for n>=2, a(1)=1, where d(1)=1, d(2)=0, d(2n)=3!+5!+...+(2n-1)!, d(2n+1)=-d(2n).`
> **Formula (_R. J. Mathar_, Jul 26 2022):**
> `Conjecture D-finite with recurrence (-9*n+38)*a(n) +3*(3*n^2-19*n+27)*a(n-1) +(9*n^3-37*n^2-24*n+127)*a(n-2) +(-9*n^4+102*n^3-392*n^2+525*n-85)*a(n-3) -(n-3)*(28*n^3-223*n^2+510*n-237)*a(n-4) -(19*n-15)*(n-3)*(n-4)^2*a(n-5)=0.`

Explicitly, with $a(1) = 1$, $d(1) = 1$, $d(2) = 0$, $d(2m) = \sum_{j=1}^{m-1} (2j+1)!$ ($m \ge 2$), $d(2m+1) = -d(2m)$ ($m \ge 1$), and $a(n) = n\, a(n-1) - d(n-1) + (n-1)!\lfloor n/2\rfloor$ for $n \ge 2$, the conjecture asserts that for all integers $n \ge 6$ (where all indices $n-5, \dots, n$ lie in the offset domain $\ge 1$),
$$
\begin{aligned}
(-9n + 38) a(n) &+ 3(3n^2 - 19n + 27) a(n-1) + (9n^3 - 37n^2 - 24n + 127) a(n-2) \\
&+ (-9n^4 + 102n^3 - 392n^2 + 525n - 85) a(n-3) \\
&- (n-3)(28n^3 - 223n^2 + 510n - 237) a(n-4) \\
&- (19n - 15)(n-3)(n-4)^2 a(n-5) = 0,
\end{aligned}
$$
and hence $a(n)$ is P-recursive (equivalently, its exponential generating function $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$ is D-finite).

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-27T09:30:00Z – 2026-11-27T09:44:00Z
- **Sources Checked:**
  - `tools/novelty_grep.py A121747`: 0 hits across 608 files.
  - `tools/arxiv_fetch.py query 'all:"A121747" OR all:"A121750"'`: 0 hits.
  - Zenodo API (`curl` `https://zenodo.org/api/records?q=A121747`): 0 hits.
  - Crossref API (`https://api.crossref.org/works?query=A121747`): 0 hits.
  - GitHub (`gh search issues "A121747"`): 0 hits.
  - Web search (`"A121747" OR "A121750" "D-finite" OR "Mathar" OR "recurrence"`): 0 proofs found; OEIS A121747 rev. 15 still lists Mathar's recurrence as `Conjecture`.
- **Verdict:** Open and unclaimed.
