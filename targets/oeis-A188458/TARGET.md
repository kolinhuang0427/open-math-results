---
source: OEIS A188458 (rev. 54), https://oeis.org/A188458
status: reported
owner: scout-5
updated: 2026-11-27T10:51:50Z
identifiers:
  - oeis:A188458
---

# OEIS A188458 — Sergei N. Gladkovskii (2013) Continued Fraction Conjecture

## Primary Source & Exact Statements

From [OEIS A188458](https://oeis.org/A188458) (revision 54):

**NAME:**
> `Expansion of e.g.f. exp(x)/cosh(2*x).`

**OFFSET:** `0,3`

**DATA (first terms):**
> `1,1,-3,-11,57,361,-2763,-24611,250737,2873041,-36581523,-512343611,7828053417,129570724921,-2309644635483,-44110959165011,898621108880097,19450718635716001,-445777636063460643,-10784052561125704811,274613643571568682777`

**FORMULA (Sergei N. Gladkovskii, Nov 12 2013):**
> `G.f.: conjecture T(0)/(1-x), where T(k) = 1 - 4*x^2*(k+1)^2/(4*x^2*(k+1)^2 + (1-x)^2/T(k+1) ); (continued fraction). - _Sergei N. Gladkovskii_, Nov 12 2013`

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). All checks across the 635-file snapshot corpus, arXiv, Zenodo, Crossref, GitHub, web search, and live OEIS rev. 54 found no prior proof.
