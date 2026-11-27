---
source: OEIS A157003 (rev. 37), https://oeis.org/A157003
status: reported
owner: scout-5
updated: 2026-11-27T11:48:00Z
identifiers:
  - oeis:A157003
---

# Target: OEIS A157003 — Mathar's 6-Term D-Finite Recurrence

## Verbatim Statement

From OEIS [A157003](https://oeis.org/A157003) (rev. 37), offset `0,3`:

> `NAME: Transform of Catalan numbers whose Hankel transform gives the Somos-4 sequence.`
>
> `FORMULA:`
> `G.f.: c(x*(1-x^2)) where c(x) is the g.f. of A000108;`
> `a(n) = Sum_{k=0..n} (-1)^((n-k)/2)*(1+(-1)^(n-k))*C(k,floor((n-k)/2))*A000108(k)/2.`
> `Conjecture: (n+1)*a(n) +(n+2)*a(n-1) +(-21*n+29)*a(n-2) +(3*n-16)*a(n-3) +40*(n-3)*a(n-4) +2*(-2*n+7)*a(n-5) +10*(-2*n+9)*a(n-6)=0. - _R. J. Mathar_, Nov 19 2014`
> `Recurrence: (n+1)*a(n) = 2*(2*n-1)*a(n-1) + (n+1)*a(n-2) - 8*(n-2)*a(n-3) + 2*(2*n-7)*a(n-5). - _Vaclav Kotesovec_, Feb 01 2015`

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). Summary:
- `tools/novelty_grep.py A157003` across all `653` snapshot files (plus live `mylesparslow-collab` ledger): `0` hits.
- `A157003` (`rev. 37`) leaves Mathar's Nov 19 2014 6-term recurrence marked `Conjecture:`, and all four linked preprints/PDFs (`arXiv:1410.2847`, `arXiv:2306.05025`, Baril et al. `bacorasisito.pdf`, Xin `arXiv:0712.0933`) contain `0` mentions of Mathar or his linear recurrence.
- arXiv API, Zenodo API, Crossref API, GitHub (`gh search`), and web search: `0` proofs found.
