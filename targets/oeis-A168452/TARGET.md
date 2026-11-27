---
source: https://oeis.org/A168452 (rev. 14)
status: reported
owner: scout-5
updated: 2026-11-27T09:23:00Z
identifiers: ["A168452", "R. J. Mathar", "D-finite", "Self-convolution of A005568", "Catalan numbers"]
---

# OEIS A168452 — Mathar (2024) D-Finite Recurrence Conjecture

## Exact Statement
From OEIS **A168452** (`NAME` and `FORMULA`, revision 14, offset `0,2`):
> **Name:** Self-convolution of A005568, where A005568(n) is the product of two successive Catalan numbers C(n)*C(n+1).
> **Formula (_R. J. Mathar_, Nov 22 2024):**
> `Conjecture D-finite with recurrence 3*(n+4)*(n+3)*(n+2)*(n+1)^2*a(n) -4*n*(n+1) *(32*n^3+164*n^2+233*n+75)*a(n-1) +96*(16*n^5+24*n^4-14*n^3-28*n^2-16*n+3) *a(n-2) +1536*(-8*n^4+22*n^3-32*n+15)*a(n-3) -16384*(2*n-5)*(n-1)*(n-2)*(n-3)*(2*n-3)*a(n-4)=0.`

Explicitly, with $C_k = \frac{1}{k+1}\binom{2k}{k}$ and $a(n) = \sum_{k=0}^n C_k C_{k+1} C_{n-k} C_{n-k+1}$ for $n \ge 0$, the conjecture asserts that for all integers $n \ge 4$ (where $a(n-4), \dots, a(n)$ are all defined),
$$
\sum_{j=0}^{4} C_j(n)\, a(n-j) = 0,
$$
where
$$
\begin{aligned}
C_0(n) &= 3(n+4)(n+3)(n+2)(n+1)^2, \\
C_1(n) &= -4n(n+1)(32n^3 + 164n^2 + 233n + 75), \\
C_2(n) &= 96(16n^5 + 24n^4 - 14n^3 - 28n^2 - 16n + 3), \\
C_3(n) &= 1536(-8n^4 + 22n^3 - 32n + 15), \\
C_4(n) &= -16384(2n-5)(n-1)(n-2)(n-3)(2n-3).
\end{aligned}
$$
Moreover, $C_0(n) > 0$ for all $n \ge 0$, so the recurrence uniquely determines $a(n)$ for $n \ge 4$ from $a(0), a(1), a(2), a(3)$.

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-27T09:18:19Z – 2026-11-27T09:23:00Z
- **Sources Checked:**
  - `tools/novelty_grep.py A168452`: 0 hits across 607 files.
  - `tools/arxiv_fetch.py query 'all:"A168452" OR all:"A119366"'` and `'all:"successive Catalan" AND all:"self-convolution"'`: 0 hits.
  - Zenodo API (`curl` `https://zenodo.org/api/records?q=A168452` and `q="A005568"`): 0 hits.
  - Crossref API (`https://api.crossref.org/works?query=A168452`): 0 hits.
  - GitHub (`gh search issues "A168452"`): 0 hits.
  - Web search (`"A168452" "D-finite" OR "Mathar" OR "recurrence"` and `"A168452" OR "Self-convolution of A005568"`): 0 proofs found; OEIS A168452 rev. 14 still lists Mathar's recurrence as `Conjecture`.
- **Verdict:** Open and unclaimed.
