---
source: https://oeis.org/A121750 (rev. 13)
status: reported
owner: scout-5
updated: 2026-11-27T09:44:30Z
identifiers: ["A121750", "R. J. Mathar", "D-finite", "deco polyominoes"]
---

# OEIS A121750 — Mathar (2022) D-Finite Recurrence Conjecture

## Exact Statement
From OEIS **A121750** (`NAME` and `FORMULA`, revision 13, offset `1,3`):
> **Name:** Number of columns of even length in all deco polyominoes of height n. A deco polyomino is a directed column-convex polyomino in which the height, measured along the diagonal, is attained only in the last column.
> **Formula:** `Recurrence relation: a(n) = n*a(n-1)+d(n-1)+(n-1)!*floor((n-1)/2) for n>=2, a(1)=0, where d(1)=1, d(2)=0, d(2n)=3!+5!+...+(2n-1)!, d(2n+1)=-d(2n).`
> **Formula (_R. J. Mathar_, Jul 26 2022):**
> `Conjecture D-finite with recurrence a(n) +(-n-2)*a(n-1) +(-n^2+4*n-2)*a(n-2) +(n^3-3*n^2-4*n+11)*a(n-3) -(n-1)*(n^2-11*n+26)*a(n-4) +(-n^3+5*n^2+7*n-43)*a(n-5) +(n-3)*(n-5)^2*a(n-6)=0.`

Explicitly, with $a(1) = 0$, $d(1) = 1$, $d(2) = 0$, $d(2m) = \sum_{j=1}^{m-1}(2j+1)!$ ($m \ge 2$), $d(2m+1) = -d(2m)$ ($m \ge 1$), and $a(n) = n\,a(n-1) + d(n-1) + (n-1)!\lfloor(n-1)/2\rfloor$ for $n \ge 2$, the conjecture asserts that for all integers $n \ge 7$ (where all indices $n-6, \dots, n$ lie in the offset domain $\ge 1$),
$$
\begin{aligned}
a(n) &+ (-n - 2) a(n-1) + (-n^2 + 4n - 2) a(n-2) + (n^3 - 3n^2 - 4n + 11) a(n-3) \\
&- (n-1)(n^2 - 11n + 26) a(n-4) + (-n^3 + 5n^2 + 7n - 43) a(n-5) + (n-3)(n-5)^2 a(n-6) = 0,
\end{aligned}
$$
and hence $a(n)$ is P-recursive (equivalently, its exponential generating function $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$ is D-finite).

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-27T09:30:00Z – 2026-11-27T09:44:30Z
- **Sources Checked:**
  - `tools/novelty_grep.py A121750`: 0 hits across 608 files.
  - `tools/arxiv_fetch.py query 'all:"A121747" OR all:"A121750"'`: 0 hits.
  - Zenodo API (`curl` `https://zenodo.org/api/records?q=A121750`): 0 hits.
  - Crossref API (`https://api.crossref.org/works?query=A121750`): 0 hits.
  - GitHub (`gh search issues "A121750"`): 0 hits.
  - Web search (`"A121747" OR "A121750" "D-finite" OR "Mathar" OR "recurrence"`): 0 proofs found; OEIS A121750 rev. 13 still lists Mathar's recurrence as `Conjecture`.
- **Verdict:** Open and unclaimed.
