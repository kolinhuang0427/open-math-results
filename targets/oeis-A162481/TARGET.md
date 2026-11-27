---
source: OEIS A162481 (rev. 23), https://oeis.org/A162481
status: reported
owner: scout-5
updated: 2026-11-27T11:38:00Z
identifiers:
  - oeis:A162481
---

# Target: OEIS A162481 — Mathar's D-Finite Recurrence

## Verbatim Statement

From OEIS [A162481](https://oeis.org/A162481) (rev. 23), offset `0,2`:

> `NAME: Expansion of (1/(1-x)^3)*c(x/(1-x)^3), c(x) the g.f. of A000108.`
>
> `FORMULA:`
> `a(n) = Sum_{k=0..n} C(n+2k+2,n-k)*A000108(k).`
> `Conjecture: (n+1)*a(n) + 2*(1-4*n)*a(n-1) + 2*(5*n-3)*a(n-2) + 4*(2-n)*a(n-3) + (n-3)*a(n-4) = 0. - _R. J. Mathar_, Dec 11 2011`
> `G.f. A(x) satisfies: A(x) = 1/(1 - x)^3 + x * A(x)^2. - _Ilya Gutkovskiy_, Jun 30 2020`
> `a(n) = binomial(n+2,2) + Sum_{k=0..n-1} a(k) * a(n-k-1). - _Seiichi Manyama_, Jan 23 2023`
> `G.f.: (1 - sqrt(1 - 4*x/(1-x)^3))/(2*x). - _Vaclav Kotesovec_, Jan 24 2023`

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). Summary:
- `tools/novelty_grep.py A162481` across all `653` snapshot files (plus live `mylesparslow-collab` ledger and Zenodo `24366920`/`23760779`): `0` hits.
- `A162481` (`rev. 23`) has only `b162481.txt` in `LINK` and leaves Mathar's Dec 11 2011 recurrence marked `Conjecture:`.
- arXiv API, Zenodo API, Crossref API, GitHub (`gh search`), and web search: `0` proofs found.
