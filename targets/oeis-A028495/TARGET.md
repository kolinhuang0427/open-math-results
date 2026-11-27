---
source: OEIS A028495 (rev. 162), https://oeis.org/A028495
status: reported
owner: scout-5
updated: 2026-11-27T10:47:16Z
identifiers:
  - oeis:A028495
---

# OEIS A028495 — Bill McEachen (2026) Asymptotic Ratio Conjectures

## Primary Source & Exact Statements

From [OEIS A028495](https://oeis.org/A028495) (revision 162):

**NAME:**
> `Expansion of g.f. (1-x^2)/(1-x-2*x^2+x^3).`

**OFFSET:** `0,3`

**DATA (first terms):**
> `1,1,2,3,6,10,19,33,61,108,197,352,638,1145,2069,3721,6714,12087,21794,39254,70755,127469,229725,413908,745889,1343980,2421850,4363921,7863641,14169633,25532994,46008619,82904974,149389218,269190547,485064009,874055885`

**FORMULA (Bill McEachen, Feb 11 2026):**
> `Conjectures: a(n) ~ A160389 * a(n-1). Also a(n) ~ sqrt(A116425)*a(n-1). - _Bill McEachen_, Feb 11 2026`

where from the referenced OEIS entries:
- [OEIS A160389](https://oeis.org/A160389) (rev. 12): `Decimal expansion of 2*cos(Pi/7).`
- [OEIS A116425](https://oeis.org/A116425) (rev. 11): `Decimal expansion of 2 + 2*cos(2*Pi/7).`

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). All checks across the 619-file snapshot corpus, arXiv, Zenodo, Crossref, GitHub, web search, and live OEIS rev. 162 found no prior proof.
