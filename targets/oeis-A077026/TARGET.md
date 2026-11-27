---
source: OEIS A077026 (rev. 14), https://oeis.org/A077026
status: reported
owner: scout-5
updated: 2026-11-27T10:38:47Z
identifiers:
  - oeis:A077026
---

# OEIS A077026 — Benedict W. J. Irwin (2016) Modulo Sum Conjecture (Refutation)

## Primary Source & Exact Statements

From [OEIS A077026](https://oeis.org/A077026) (revision 14):

**NAME:**
> `a(n) = Sum_{k=1..n} floor(n/k + 1)-floor(n/k + 1/2).`

**OFFSET:** `1,2`

**DATA (first terms):**
> `1,2,2,4,3,5,5,6,6,8,6,10,9,9,9,13,11,12,12,14,14,16,12,18,17,17,17,19,17,21,21,22,20,22,20,26,26,24,22,28,25,29,27,29,29,29,27,33,33,32,32,36,30,34,34,38,38,38,34,40,39,39,37,43,41,45,43,41,41,45,43,50,48`

**FORMULA (Benedict W. J. Irwin, Sep 22 2016):**
> `Conjecture: Let f(a,b)=1, if (a+b) mod |a-b| != (a mod |a-b|)+(b mod |a-b|), and 0 otherwise. a(n) = Sum_{k=1..n-1} 1-f(n,k). - _Benedict W. J. Irwin_, Sep 22 2016`

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). All checks across the 619-file snapshot corpus, arXiv, Zenodo, Crossref, GitHub, web search, and live OEIS rev. 14 found no prior refutation or correction.
