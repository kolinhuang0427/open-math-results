---
source: OEIS A176126 (rev. 18), https://oeis.org/A176126
status: reported
owner: scout-5
updated: 2026-11-27T11:37:00Z
identifiers:
  - oeis:A176126
  - oeis:A127276
  - oeis:A001788
---

# Target: OEIS A176126 — Mathar's Linear Recurrence and Generating Function

## Verbatim Statement

From OEIS [A176126](https://oeis.org/A176126) (rev. 18), offset `0,4`:

> `NAME: Numerator of -A127276(n)/A001788(n).`
>
> `FORMULA: Conjecture: a(n) = +3*a(n-1) -6*a(n-2) +10*a(n-3) -12*a(n-4) +12*a(n-5) -10*a(n-6) +6*a(n-7) -3*a(n-8) +a(n-9) with g.f. (x^4-x^3+3*x^2-x+1)*(x^4-x^3-2*x^2-x+1) / ( (x-1)^3*(x^2+1)^3 ). - _R. J. Mathar_, Dec 12 2010`
>
> `COMMENT: The sequence of fractions starts -1/0, -1/1, 1/3, 2/3, 4/5, 13/15, 19/21, 13/14, 17/18, 43/45, 53/55, 32/33, 38/39, ...`

Auxiliary primary definitions:
- `A127276` (`rev. 33`): `NAME: Hankel transform of A127275.` (where `A127275` is the expansion of `(\sqrt{1-4x}-x)/(1-4x)`).
- `A001788` (`rev. 270`): `NAME: a(n) = n*(n+1)*2^(n-2).` (with `a(0) = 0`).

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). Summary:
- `tools/novelty_grep.py A176126` across all `652` snapshot files (incl. Cohen Zenodo `24384895` and Blanco Gómez Zenodo `23112421`/`23114921`): `0` hits.
- `A176126` (`rev. 18`) leaves Mathar's Dec 12 2010 recurrence and g.f. marked `Conjecture:`.
- arXiv API, Zenodo API, Crossref API, GitHub (`gh search`), and web search: `0` proofs found.
