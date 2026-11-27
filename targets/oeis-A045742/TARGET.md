---
source: https://oeis.org/A045742 (rev. 20)
status: reported
owner: scout-5
updated: 2026-11-27T09:32:00Z
identifiers: ["A045742", "R. J. Mathar", "D-finite", "noncrossing connected graphs", "interior faces"]
---

# OEIS A045742 — Mathar (2022) D-Finite Recurrence Conjecture

## Exact Statement
From OEIS **A045742** (`NAME` and `FORMULA`, revision 20, offset `2,3`):
> **Name:** Number of interior faces in all noncrossing connected graphs on n nodes on a circle.
> **Formula:** `a(n) = Sum_{k=1..n-2} k*binomial(n+k-2, k)*binomial(3*n-3, n-2-k)/(n-1).`
> **Formula (_R. J. Mathar_, Jul 26 2022):**
> `Conjecture D-finite with recurrence n*(n-1)*(523*n-1993)*a(n) -6*(n-1)*(759*n^2-6019*n+12790)*a(n-1) -12*(n-2)*(4707*n^2-17937*n+6260)*a(n-2) +72*(3*n-10)*(759*n-2224)*(3*n-11)*a(n-3)=0.`

Explicitly, with $a(2) = 0$ and
$$a(n) = \frac{1}{n-1}\sum_{k=1}^{n-2} k \binom{n+k-2}{k}\binom{3n-3}{n-2-k} \qquad (n \ge 3),$$
the conjecture asserts that for all integers $n \ge 5$ (where all indices $n-3, \dots, n$ lie within the offset domain $n \ge 2$),
$$\sum_{j=0}^{3} C_j(n)\, a(n-j) = 0,$$
where
$$
\begin{aligned}
C_0(n) &= n(n-1)(523n - 1993), \\
C_1(n) &= -6(n-1)(759n^2 - 6019n + 12790), \\
C_2(n) &= -12(n-2)(4707n^2 - 17937n + 6260), \\
C_3(n) &= 72(3n-10)(759n - 2224)(3n-11).
\end{aligned}
$$
Moreover, $C_0(n) > 0$ for all $n \ge 4$, so the recurrence uniquely determines $a(n)$ for $n \ge 5$ from $a(2), a(3), a(4)$.

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-27T09:26:00Z – 2026-11-27T09:32:00Z
- **Sources Checked:**
  - `tools/novelty_grep.py A045742`: 0 hits across 608 files.
  - `tools/arxiv_fetch.py query 'all:"A121580" OR ... OR all:"A045742"'` and `'all:"interior faces" AND all:"noncrossing connected graphs"'`: 0 hits.
  - Zenodo API (`curl` `https://zenodo.org/api/records?q=A045742` and `q="interior+faces+in+all+noncrossing"`): 0 hits.
  - Crossref API (`https://api.crossref.org/works?query=A045742`): 0 hits.
  - GitHub (`gh search issues "A045742"`): 0 hits.
  - Web search (`"A045742" Mathar OR "interior faces in all noncrossing connected graphs"`): 0 proofs found; OEIS A045742 rev. 20 still lists Mathar's recurrence as `Conjecture`.
- **Verdict:** Open and unclaimed.
