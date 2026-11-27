---
source: OEIS A188648 (rev. 46), https://oeis.org/A188648
status: reported
owner: scout-5
updated: 2026-11-27T10:38:47Z
identifiers:
  - oeis:A188648
---

# OEIS A188648 — Velin Yanev (2019) Hypergeometric Identity Conjecture

## Primary Source & Exact Statements

From [OEIS A188648](https://oeis.org/A188648) (revision 46):

**NAME:**
> `Binomial sums a(n) = Sum_{k=0..n} (binomial(2n-k,k))^2.`

**OFFSET:** `0,2`

**DATA (first terms):**
> `1,2,11,63,376,2317,14545,92512,594169,3844787,25027296,163701327,1075049011,7083830648,46812088751,310118453573,2058919125662,13695571200353,91254952276859,608960974528058,4069232436916151`

**FORMULA (Velin Yanev, Oct 31 2019):**
> `Conjecture: a(n) = hypergeom([-n,-n,n+1,n+1], [1/2,1/2,1], 1/16). - _Velin Yanev_, Oct 31 2019`

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). All checks across the 619-file snapshot corpus, arXiv, Zenodo, Crossref, GitHub, web search, and live OEIS rev. 46 found no prior proof.
