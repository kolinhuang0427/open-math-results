---
source: https://oeis.org/A121752 (rev. 4)
status: reported
owner: scout-5
updated: 2026-11-27T09:42:00Z
identifiers: ["A121752", "R. J. Mathar", "D-finite", "deco polyominoes"]
---

# OEIS A121752 — Mathar (2022) D-Finite Recurrence Conjecture

## Exact Statement
From OEIS **A121752** (`NAME` and `FORMULA`, revision 4, offset `1,2`):
> **Name:** Number of columns ending at an odd level in all deco polyominoes of height n. A deco polyomino is a directed column-convex polyomino in which the height, measured along the diagonal, is attained only in the last column.
> **Formula:** `Recurrence relation: a(n)=(2n-3)a(n-1)-(n-1)(n-3)a(n-2)+(n-2)!(n*floor(n/2)-(n-2)*floor((n-1)/2)-1); a[1]=1, a[2]=2.`
> **Formula (_R. J. Mathar_, Jul 26 2022):**
> `Conjecture D-finite with recurrence (-460*n+1223)*a(n) +(460*n^2+460*n-5569)*a(n-1) +(460*n^3-3826*n^2+7853*n+1313)*a(n-2) +(-460*n^4+1840*n^3+5501*n^2-31045*n+31726)*a(n-3) +(1223*n^4-13205*n^3+45787*n^2-51389*n+558)*a(n-4) -2*(426*n-1111)*(n-6)*(n-4)^2*a(n-5)=0.`

Explicitly, with $a(1) = 1$, $a(2) = 2$, and $a(n) = (2n-3)a(n-1) - (n-1)(n-3)a(n-2) + (n-2)!\bigl(n\lfloor n/2\rfloor - (n-2)\lfloor(n-1)/2\rfloor - 1\bigr)$ for $n \ge 3$, the conjecture asserts that for all integers $n \ge 6$ (where all indices $n-5, \dots, n$ lie in the offset domain $\ge 1$),
$$
\begin{aligned}
(-460n + 1223) a(n) &+ (460n^2 + 460n - 5569) a(n-1) + (460n^3 - 3826n^2 + 7853n + 1313) a(n-2) \\
&+ (-460n^4 + 1840n^3 + 5501n^2 - 31045n + 31726) a(n-3) \\
&+ (1223n^4 - 13205n^3 + 45787n^2 - 51389n + 558) a(n-4) \\
&- 2(426n - 1111)(n-6)(n-4)^2 a(n-5) = 0,
\end{aligned}
$$
and hence $a(n)$ is P-recursive (equivalently, its exponential generating function $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$ is D-finite).

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-27T09:34:00Z – 2026-11-27T09:42:00Z
- **Sources Checked:**
  - `tools/novelty_grep.py A121752`: 0 hits across 608 files.
  - `tools/arxiv_fetch.py query 'all:"A121752" OR all:"A121754"'`: 0 hits.
  - Zenodo API (`curl` `https://zenodo.org/api/records?q=A121752`): 0 hits.
  - Crossref API (`https://api.crossref.org/works?query=A121752`): 0 hits.
  - GitHub (`gh search issues "A121752"`): 0 hits.
  - Web search (`"A121754" OR "A121752" "D-finite" OR "Mathar" OR "recurrence"`): 0 proofs found; OEIS A121752 rev. 4 still lists Mathar's recurrence as `Conjecture`.
- **Verdict:** Open and unclaimed.
