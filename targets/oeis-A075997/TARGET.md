---
source: OEIS A075997 (rev. 37), https://oeis.org/A075997
status: reported
owner: scout-5
updated: 2026-11-27T10:38:47Z
identifiers:
  - oeis:A075997
---

# OEIS A075997 — Benedict W. J. Irwin (2016) Modulo Sum Conjecture

## Primary Source & Exact Statements

From [OEIS A075997](https://oeis.org/A075997) (revision 37):

**NAME:**
> `a(n) = [n/2] - [n/3] + [n/4] - [n/5] + [n/6] - ..., where [n/k] = floor(n/k).`

**OFFSET:** `0,5`

**DATA (first terms):**
> `0,0,1,0,2,1,2,1,4,2,3,2,5,4,5,2,6,5,6,5,8,5,6,5,10,8,9,6,9,8,9,8,13,10,11,8,12,11,12,9,14,13,14,13,16,11,12,11,18,16,17,14,17,16,17,14,19,16,17,16,21,20,21,16,22,19,20,19,22,19,20,19,26,25,26,21,24,21,22,21`

**FORMULA (Benedict W. J. Irwin, Sep 23 2016):**
> `Conjecture: Let f(a,b)=1, if (a+b) mod |a-b| != (a mod |a-b|)+(b mod |a-b|), and 0 otherwise. a(n) = Sum_{k=1..n-1} f(n+k,n-k). - _Benedict W. J. Irwin_, Sep 23 2016`

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). All checks across the 619-file snapshot corpus, arXiv, Zenodo, Crossref, GitHub, web search, and live OEIS rev. 37 found no prior proof.
