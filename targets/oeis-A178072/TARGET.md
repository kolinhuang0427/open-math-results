---
source: OEIS A178072 (rev. 35), https://oeis.org/A178072
status: reported
owner: scout-5
updated: 2026-11-27T11:26:00Z
identifiers:
  - oeis:A178072
---

# Target: OEIS A178072 — Mathar's D-Finite Recurrence

## Verbatim Statement

From OEIS [A178072](https://oeis.org/A178072) (rev. 35), offset `0,8`:

> `NAME: Sequence with Hankel transform equal to the Somos-4 sequence A006769(n+2).`
>
> `FORMULA:`
> `a(n) = Sum_{k=0..floor(n/2)} (C(n-k,k)/(n-2*k+1))*Sum_{i=0..min(k,n-2*k)} C(k,i)*C(n-k-i-1,n-2*k-i)*2^(n-2*k-i)*(-1)^(k-i).`
> `From _Michael Somos_, Jun 13 2010: (Start)`
> `G.f. A(x) satisfies 0 = f(x, A(x)) where f(x, y) = (2*x + x^3) * y^2 - (1 + x)^2 * y + 1.`
> `G.f.: 2 / (1 + 2*x + x^2 + sqrt(1 - 4*x + 6*x^2 + x^4)). (End)`
> `Conjecture: 2*n*(n+1)*a(n) +2*n*(n+1)*a(n-1) -3*(3*n-1)*(3*n-4)*a(n-2) +(61*n^2-191*n+36)*a(n-3) +6*(-2*n^2+2*n-1)*a(n-4) +2*(5*n-1)*(4*n-15)*a(n-5) +n*(n-5)*a(n-6) +(5*n-1)*(n-6)*a(n-7)=0. - _R. J. Mathar_, Jun 14 2016`

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). Summary:
- `tools/novelty_grep.py A178072` across all `651` snapshot files (incl. Zenodo `23112421` and `23114921`): `0` hits.
- `A178072` (`rev. 35`) leaves Mathar's Jun 14 2016 7-term recurrence marked `Conjecture:`, and linked paper `arXiv:2306.05025` (`Elliptic_Curve.tex`) contains `0` mentions of `A178072` or Mathar.
- arXiv API, Zenodo API, Crossref API, GitHub (`gh search`), and web search: `0` proofs found.
