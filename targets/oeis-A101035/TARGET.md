---
source: OEIS A101035 (rev. 37), https://oeis.org/A101035
status: reported
owner: scout-5
updated: 2026-11-27T10:51:50Z
identifiers:
  - oeis:A101035
---

# OEIS A101035 — Benedict W. J. Irwin (2017) Logarithmic Generating Function Conjecture

## Primary Source & Exact Statements

From [OEIS A101035](https://oeis.org/A101035) (revision 37):

**NAME:**
> `Dirichlet inverse of the gcd-sum function (A018804).`

**OFFSET:** `1,2`

**DATA (first terms):**
> `1,-3,-5,1,-9,15,-13,1,4,27,-21,-5,-25,39,45,1,-33,-12,-37,-9,65,63,-45,-5,16,75,4,-13,-57,-135,-61,1,105,99,117,4,-73,111,125,-9,-81,-195,-85,-21,-36,135,-93,-5,36,-48,165,-25,-105,-12,189,-13,185,171,-117,45,-121,183,-52,1,225,-315,-133,-33,225,-351,-141,4`

**FORMULA (Benedict W. J. Irwin, Jul 26 2017):**
> `Conjecture: Logarithmic g.f. Sum_{n>0,k>0} mu(n)*mu(k)*log(1/(1-x^(n*k))). - _Benedict W. J. Irwin_, Jul 26 2017`

where [OEIS A018804](https://oeis.org/A018804) (rev. 270) is `Pillai's arithmetical function: Sum_{k=1..n} gcd(k, n)`.

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). All checks across the 635-file snapshot corpus, arXiv, Zenodo, Crossref, GitHub, web search, and live OEIS rev. 37 found no prior proof.
