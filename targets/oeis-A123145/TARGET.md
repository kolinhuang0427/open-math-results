---
source: OEIS A123145 (rev. 31), https://oeis.org/A123145
status: reported
owner: scout-5
updated: 2026-11-27T10:44:00Z
identifiers:
  - oeis:A123145
---

# OEIS A123145 — Sergei N. Gladkovskii (2012) 5-Step Continued Fraction EGF Conjecture

## Primary Source & Exact Statements

From [OEIS A123145](https://oeis.org/A123145) (revision 31):

**NAME:**
> `a(1) = 1, a(n) = a(n-1) if n == 1 (mod 4), otherwise a(n) = n * a(n-1) for n >= 2.`

**OFFSET:** `1,2`

**DATA (first terms):**
> `1,2,6,24,24,144,1008,8064,8064,80640,887040,10644480,10644480,149022720,2235340800,35765452800,35765452800,643778150400,12231784857600,244635697152000,244635697152000,5381985337344000,123785662758912000,2970855906213888000`

**FORMULA (Sergei N. Gladkovskii, Nov 26 2012):**
> `Conjecture: E.g.f.: E(x)=d(G(0))/dx where G(k) = 1 + x/(4*k+1 - x*(4*k+1)/(1 + x - x/(1 + x - x/(x + 1/G(k+1) )))), or shift on 1 left G(0); (continued fraction,5-step). - _Sergei N. Gladkovskii_, Nov 26 2012`

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). All checks across the 619-file snapshot corpus, arXiv, Zenodo, Crossref, GitHub, web search, and live OEIS rev. 31 found no prior proof.
