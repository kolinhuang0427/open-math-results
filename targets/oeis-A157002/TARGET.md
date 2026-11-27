---
source: OEIS A157002 (rev. 15), https://oeis.org/A157002
status: reported
owner: scout-5
updated: 2026-11-27T11:36:00Z
identifiers:
  - oeis:A157002
---

# Target: OEIS A157002 — Mathar's D-Finite Recurrence

## Verbatim Statement

From OEIS [A157002](https://oeis.org/A157002) (rev. 15), offset `0,4`:

> `NAME: Transform of Catalan numbers whose Hankel transform gives the Somos-4 sequence.`
>
> `FORMULA:`
> `G.f.: (1 - sqrt(1-4*x*(1-x^2)))/(2*x*(1+x)).`
> `a(n) = Sum_{k=0..n} (-1)^floor((n-k+1)/2)*C(k,floor((n-k)/2))*A000108(k).`
> `Conjecture: (n+1)*a(n) +3*(-n+1)*a(n-1) +2*(-2*n+1)*a(n-2) +2*(2*n-7)*a(n-3) +2*(2*n-7)*a(n-4)=0. - _R. J. Mathar_, Nov 19 2014`
>
> `COMMENT: Image of the Catalan numbers A000108 by the Riordan array (1-x,x(1-x^2)).`

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). Summary:
- `tools/novelty_grep.py A157002` across all `653` snapshot files (plus live `mylesparslow-collab` ledger and Zenodo `24366920`/`23760779`): `0` hits.
- `A157002` (`rev. 15`) leaves Mathar's Nov 19 2014 recurrence marked `Conjecture:`, and linked paper Guoce Xin (`arXiv:0712.0933` / *Adv. Appl. Math.* 42, 2009) studies only the Somos-4 Hankel determinant, with `0` mentions of Mathar or any linear recurrence.
- arXiv API, Zenodo API, Crossref API, GitHub (`gh search`), and web search: `0` proofs found.
