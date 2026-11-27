---
source: https://oeis.org/A119366 (rev. 7)
status: reported
owner: scout-5
updated: 2026-11-27T09:26:00Z
identifiers: ["A119366", "R. J. Mathar", "D-finite", "Paul Barry", "rooted planar n-trees"]
---

# OEIS A119366 — Mathar (2025) D-Finite Recurrence Conjecture

## Exact Statement
From OEIS **A119366** (`NAME` and `FORMULA`, revision 7, offset `0,5`):
> **Name:** Number of rooted planar n-trees whose number of leaves is equal to 1 modulo 3.
> **Formula (_Paul Barry_, Jan 25 2007):** `a(0)=0, a(n)=sum{k=0..floor(n/3), (1/n)*C(n,3k+1)C(n,3k)},n>0;`
> **Formula (_R. J. Mathar_, Feb 03 2025):**
> `Conjecture D-finite with recurrence +n*(881*n-4580)*(n-2)*(n+1)*a(n) -3*n*(612*n^3-2827*n^2-2988*n+10135)*a(n-1) +3*(-3088*n^4+42803*n^3-190361*n^2+313702*n-167988)*a(n-2) +(43042*n^4-600920*n^3+2924411*n^2-5860777*n+4115562)*a(n-3) +3*(-38600*n^4+558681*n^3-2904370*n^2+6389913*n-4965528)*a(n-4) +3*(-14776*n^4+162695*n^3-434711*n^2-415064*n+1878084)*a(n-5) -9*(n-6)*(10835*n^3-106831*n^2+290611*n-173519)*a(n-6) +54*(n-6)*(n-7)*(593*n-1429)*(2*n-13)*a(n-7)=0.`

Explicitly, with $a(0) = 0$ and $a(n) = \frac{1}{n}\sum_{k=0}^{\lfloor n/3 \rfloor}\binom{n}{3k+1}\binom{n}{3k}$ for $n \ge 1$, the conjecture asserts that for all integers $n \ge 7$ (the range where all indices $n-7, \dots, n$ are non-negative),
$$
\sum_{j=0}^{7} C_j(n)\, a(n-j) = 0,
$$
where
$$
\begin{aligned}
C_0(n) &= n(881n-4580)(n-2)(n+1), \\
C_1(n) &= -3n(612n^3-2827n^2-2988n+10135), \\
C_2(n) &= 3(-3088n^4+42803n^3-190361n^2+313702n-167988), \\
C_3(n) &= 43042n^4-600920n^3+2924411n^2-5860777n+4115562, \\
C_4(n) &= 3(-38600n^4+558681n^3-2904370n^2+6389913n-4965528), \\
C_5(n) &= 3(-14776n^4+162695n^3-434711n^2-415064n+1878084), \\
C_6(n) &= -9(n-6)(10835n^3-106831n^2+290611n-173519), \\
C_7(n) &= 54(n-6)(n-7)(593n-1429)(2n-13).
\end{aligned}
$$
Moreover, $C_0(n) > 0$ for all $n \ge 6$, so the recurrence uniquely determines $a(n)$ for $n \ge 7$ from $a(0), \dots, a(6)$.

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-27T09:18:00Z – 2026-11-27T09:26:00Z
- **Sources Checked:**
  - `tools/novelty_grep.py A119366 "rooted planar"`: 0 hits across 608 files.
  - `tools/arxiv_fetch.py query 'all:"A168452" OR all:"A119366"'` and `'all:"rooted planar" AND all:"leaves" AND all:"modulo 3"'`: 0 hits.
  - Zenodo API (`curl` `https://zenodo.org/api/records?q=A119366` and `q="rooted+planar"+"modulo+3"`): 0 relevant hits.
  - Crossref API (`https://api.crossref.org/works?query=A119366`): 0 hits.
  - GitHub (`gh search issues "A119366"`): 0 hits.
  - Web search (`"A119366" "D-finite" OR "Mathar" OR "recurrence"`): 0 proofs found; OEIS A119366 rev. 7 still lists Mathar's recurrence as `Conjecture`.
- **Verdict:** Open and unclaimed.
