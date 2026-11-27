---
source: OEIS A168503 (rev. 20), https://oeis.org/A168503
status: reported
owner: scout-5
updated: 2026-11-27T11:48:00Z
identifiers:
  - oeis:A168503
---

# Target: OEIS A168503 — Mathar's D-Finite Recurrence

## Verbatim Statement

From OEIS [A168503](https://oeis.org/A168503) (rev. 20), offset `0,3`:

> `NAME: Expansion of 1/(1-x/(1-2x/(1-3x/(1-x/(1-2x/(1-3x/(1-... (continued fraction).`
>
> `FORMULA:`
> `G.f.: (1-sqrt(1-12*x+36*x^2-24*x^3))/(6*x*(1-x)).`
> `Conjecture: (n+1)*a(n) +(-13*n+5)*a(n-1) +6*(8*n-13)*a(n-2) +12*(-5*n+13)*a(n-3) +12*(2*n-7)*a(n-4)=0. - _R. J. Mathar_, Feb 10 2015`

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). Summary:
- `tools/novelty_grep.py A168503` across all `658` snapshot files (plus live `mylesparslow-collab` ledger): `0` hits.
- `A168503` (`rev. 20`) has `LINK: None` and leaves Mathar's Feb 10 2015 recurrence marked `Conjecture:`.
- arXiv API, Zenodo API, Crossref API, GitHub (`gh search`), and web search: `0` proofs found.
