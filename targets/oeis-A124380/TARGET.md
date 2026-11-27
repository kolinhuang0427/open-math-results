---
source: OEIS A124380 (rev. 39), https://oeis.org/A124380
status: reported
owner: scout-5
updated: 2026-11-27T11:01:17Z
identifiers:
  - oeis:A124380
---

# OEIS A124380 — Vaclav Kotesovec (2024) Logarithmic Asymptotic Conjecture

## Primary Source & Exact Statements

From [OEIS A124380](https://oeis.org/A124380) (revision 39):

**NAME:**
> `O.g.f.: A(x) = Sum_{n>=0} x^n*Product_{k=0..n} (1 + k*x).`

**OFFSET:** `0,3`

**DATA (first terms):**
> `1,1,2,4,9,22,57,157,453,1368,4296,13995,47138,163779,585741,2152349,8113188,31326760,123748871,499539900,2058542819,8651755865,37054078481,161591063250,717032333816,3235298221401,14834735654080,69085973044125,326600050947885,1566556077233897`

**FORMULA (Vaclav Kotesovec, Sep 18 2024):**
> `Conjecture: log(a(n)) ~ n*log(n)/2 - n*(1 + log(2))/2. - _Vaclav Kotesovec_, Sep 18 2024`

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). All checks across the 635-file snapshot corpus, arXiv (including inspecting the source of linked `arXiv:2408.06959`), Zenodo, Crossref, GitHub, web search, and live OEIS rev. 39 found no prior proof.
