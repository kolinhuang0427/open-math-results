---
source: https://oeis.org/A045743 (rev. 14)
status: reported
owner: scout-5
updated: 2026-11-27T09:19:00Z
identifiers: ["A045743", "R. J. Mathar", "D-finite", "noncrossing connected graphs", "no triangular faces", "Paul D. Hanna"]
---

# OEIS A045743 — Mathar (2022) D-Finite Recurrence Conjecture

## Exact Statement
From OEIS **A045743** (`NAME` and `FORMULA`, revision 14, offset `2,2`):
> **Name:** Number of noncrossing connected graphs on n nodes on a circle having no triangular faces.
> **Formula:** `a(n) = Sum_{i=0..floor((n-2)/2)} binomial(n-2+i, i)*binomial(3*n-3-i, n-2-2*i)/(n-1).`
> **Formula (_Paul D. Hanna_, Mar 09 2010):**
> `G.f. A(x): Let F(x) = 1 + A(x)/x = 1 + x + 3*x^2 + 13*x^3 + 66*x^4 +...`
> `then F(x) satisfies: x*F(x)^4 = (1 - F(x))*(1 - 3*F(x) + F(x)^2).`
> **Formula (_R. J. Mathar_, Jul 26 2022):**
> `Conjecture D-finite with recurrence 5*n*(n-1)*(n-2)*(1353818*n-3651663)*a(n) +16*(n-1)*(n-2)*(2236406*n^2-6864025*n+2014500)*a(n-1) -16*(n-2)*(46338048*n^3-326486432*n^2+734160494*n-506411475)*a(n-2) +8*(2*n-7)*(26592864*n^3-436441232*n^2+2071128458*n-3030735075)*a(n-3) +128*(94246*n-334675)*(4*n-19)*(2*n-9)*(4*n-17)*a(n-4)=0.`

Explicitly, for $n \ge 2$ with
$$a(n) = \frac{1}{n-1}\sum_{i=0}^{\lfloor (n-2)/2 \rfloor} \binom{n-2+i}{i}\binom{3n-3-i}{n-2-2i},$$
the conjecture asserts that for all integers $n \ge 6$ (where all terms $a(n-4), \dots, a(n)$ lie within the offset $n \ge 2$),
$$\sum_{j=0}^{4} C_j(n)\, a(n-j) = 0,$$
where
$$
\begin{aligned}
C_0(n) &= 5n(n-1)(n-2)(1353818n - 3651663), \\
C_1(n) &= 16(n-1)(n-2)(2236406n^2 - 6864025n + 2014500), \\
C_2(n) &= -16(n-2)(46338048n^3 - 326486432n^2 + 734160494n - 506411475), \\
C_3(n) &= 8(2n-7)(26592864n^3 - 436441232n^2 + 2071128458n - 3030735075), \\
C_4(n) &= 128(94246n - 334675)(4n-19)(2n-9)(4n-17).
\end{aligned}
$$
Moreover, $C_0(n) > 0$ for all $n \ge 6$, so the recurrence uniquely determines $a(n)$ for $n \ge 6$ from $a(2), a(3), a(4), a(5)$.

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-27T09:14:56Z – 2026-11-27T09:19:00Z
- **Sources Checked:**
  - `tools/novelty_grep.py A045743`: 0 hits across 607 files.
  - `tools/arxiv_fetch.py query 'all:"A045743"'` and `'all:"no triangular faces" AND all:"noncrossing"'`: 0 hits.
  - Zenodo API (`curl` `https://zenodo.org/api/records?q=A045743` and `q="no+triangular+faces"`): 0 hits.
  - Crossref API (`https://api.crossref.org/works?query=A045743`): 0 hits.
  - GitHub (`gh search issues "A045743"`): 0 hits.
  - Web search (`"A045743" Mathar`): 0 proofs found; OEIS A045743 rev. 14 still lists Mathar's recurrence as `Conjecture`.
- **Verdict:** Open and unclaimed.
