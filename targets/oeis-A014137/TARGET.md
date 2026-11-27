---
source: OEIS A014137 (rev. 180), https://oeis.org/A014137
status: reported
owner: scout-5
updated: 2026-11-27T10:47:16Z
identifiers:
  - oeis:A014137
---

# OEIS A014137 — Sergei N. Gladkovskii (2013) Continued Fraction Conjecture

## Primary Source & Exact Statements

From [OEIS A014137](https://oeis.org/A014137) (revision 180):

**NAME:**
> `Partial sums of Catalan numbers (A000108).`

**OFFSET:** `0,2`

**DATA (first terms):**
> `1,2,4,9,23,65,197,626,2056,6918,23714,82500,290512,1033412,3707852,13402697,48760367,178405157,656043857,2423307047,8987427467,33453694487,124936258127,467995871777,1757900019101,6619846420553,24987199492705,94520750408709,358268702159069`

**FORMULA:**
> `G.f.: (1 - (1 - 4*x)^(1/2))/(2*x*(1 - x)).`
> `a(n) = Sum_{k=0..n} (2k)!/(k!)^2/(k+1). - _Alexander Adamchuk_, Jul 11 2006`
> `G.f. (conjecture): Q(0)/(1-x), where Q(k)= 1 + (4*k + 1)*x/(k + 1 - 2*x*(k + 1)*(4*k + 3)/(2*x*(4*k + 3) + (2*k + 3)/Q(k+1))); (continued fraction). - _Sergei N. Gladkovskii_, May 14 2013`

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). All checks across the 619-file snapshot corpus, arXiv, Zenodo, Crossref, GitHub, web search, and live OEIS rev. 180 found no prior proof of Gladkovskii's continued fraction conjecture.
