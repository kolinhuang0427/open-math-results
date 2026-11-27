---
source: https://oeis.org/A121754 (rev. 4)
status: reported
owner: scout-5
updated: 2026-11-27T09:40:00Z
identifiers: ["A121754", "R. J. Mathar", "D-finite", "deco polyominoes"]
---

# OEIS A121754 — Mathar (2022) D-Finite Recurrence Conjecture

## Exact Statement
From OEIS **A121754** (`NAME` and `FORMULA`, revision 4, offset `1,3`):
> **Name:** Number of columns ending at an even level in all deco polyominoes of height n. A deco polyomino is a directed column-convex polyomino in which the height, measured along the diagonal, is attained only in the last column.
> **Formula:** `Recurrence relation: a(n)=(2n-3)a(n-1)-(n-1)(n-3)a(n-2)+(n-2)![n-2+(1/2)(1+(-1)^(n-1))(n-1)] for n>=3; a(1)=0, a(2)=1.`
> **Formula (_R. J. Mathar_, Jul 26 2022):**
> `Conjecture D-finite with recurrence 16*(n+1)*a(n) +(-16*n^2-178*n+531)*a(n-1) +(-16*n^3+178*n^2-393*n-510)*a(n-2) +(16*n^4+98*n^3-1439*n^2+4222*n-3623)*a(n-3) +(-146*n^4+1479*n^3-4483*n^2+3054*n+2841)*a(n-4) +(130*n-311)*(n-6)*(-4+n)^2*a(n-5)=0.`

Explicitly, with $a(1) = 0$, $a(2) = 1$, and $a(n) = (2n-3)a(n-1) - (n-1)(n-3)a(n-2) + (n-2)!\bigl(n - 2 + \frac{1 + (-1)^{n-1}}{2}(n-1)\bigr)$ for $n \ge 3$, the conjecture asserts that for all integers $n \ge 6$ (where all indices $n-5, \dots, n$ lie in the offset domain $\ge 1$),
$$
\begin{aligned}
16(n+1) a(n) &+ (-16n^2 - 178n + 531) a(n-1) + (-16n^3 + 178n^2 - 393n - 510) a(n-2) \\
&+ (16n^4 + 98n^3 - 1439n^2 + 4222n - 3623) a(n-3) \\
&+ (-146n^4 + 1479n^3 - 4483n^2 + 3054n + 2841) a(n-4) \\
&+ (130n - 311)(n-6)(n-4)^2 a(n-5) = 0,
\end{aligned}
$$
and hence $a(n)$ is P-recursive (equivalently, its exponential generating function $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$ is D-finite).

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-27T09:34:00Z – 2026-11-27T09:40:00Z
- **Sources Checked:**
  - `tools/novelty_grep.py A121754`: 0 hits across 608 files.
  - `tools/arxiv_fetch.py query 'all:"A121752" OR all:"A121754"'`: 0 hits.
  - Zenodo API (`curl` `https://zenodo.org/api/records?q=A121754`): 0 hits.
  - Crossref API (`https://api.crossref.org/works?query=A121754`): 1 unrelated medical paper (`10.1002/jor.23400`).
  - GitHub (`gh search issues "A121754"`): 0 hits.
  - Web search (`"A121754" OR "A121752" "D-finite" OR "Mathar" OR "recurrence"`): 0 proofs found; OEIS A121754 rev. 4 still lists Mathar's recurrence as `Conjecture`.
- **Verdict:** Open and unclaimed.
