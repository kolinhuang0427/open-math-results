---
source: OEIS A179525 (rev. 74), https://oeis.org/A179525
status: reported
owner: scout-5
updated: 2026-11-27T10:58:15Z
identifiers:
  - oeis:A179525
---

# OEIS A179525 — Gladkovskii (2013) CF and Peter Bala (2017) Even-Product Generating Function

## Primary Source & Exact Statements

From [OEIS A179525](https://oeis.org/A179525) (revision 74):

**NAME:**
> `G.f.: A(x) = Sum_{n>=0} Product_{k=1..n} ((1+x)^k - 1).`

**OFFSET:** `0,3`

**DATA (first terms):**
> `1,1,2,7,33,197,1419,11966,115575,1257718,15223822,202860828,2950665011,46516215168,790009447590,14379745626739,279256447482090,5763290215111558,125960271446527241,2906289188751628643,70594767279197608011,1800695322331687800336,48122711251655255426539,1344617808976210991187090,39206731897407002624384182,1190905492485213830900901986`

**FORMULA (Sergei N. Gladkovskii, May 13 2013):**
> `G.f.: Q(0), where Q(k)= 1 - (1-(1+x)^(2*k+1))/(1 - (1-(1+x)^(2*k+2))/(1 - (1+x)^(2*k+2) - 1/Q(k+1))); (continued fraction). Conjecture. - _Sergei N. Gladkovskii_, May 13 2013`

**FORMULA (Peter Bala, May 16 2017):**
> `Conjectural g.f.: Sum_{n >= 0} (1 + x)^(2*n+1)*Product_{k = 1..2*n} (1 - (1 + x)^k). Cf. A158690, which has e.g.f. A(exp(x) - 1).`

*(Scope note: Bala's preceding May 16, 2017 line `Conjectural g.f.: Sum_{n >= 0} 1/(1 + x)^(n+1)*Product_{k = 1..n} (1 - 1/(1 + x)^(2*k)).`, which is the asymptotic $x$-adic series associated to OEIS A003475 / Zagier Example 1, is not claimed here and remains open in this folder.)*

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). All checks across the 635-file snapshot corpus, arXiv, Zenodo, Crossref, GitHub, web search, and live OEIS rev. 74 found no prior proof of either statement.
