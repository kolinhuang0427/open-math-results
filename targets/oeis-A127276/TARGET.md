---
source: OEIS A127276 (rev. 33), https://oeis.org/A127276
status: reported
owner: scout-5
updated: 2026-11-27T11:28:00Z
identifiers:
  - oeis:A127276
  - oeis:A127275
---

# Target: OEIS A127276 — Mathar's Closed Form and G.f. for Hankel Transform of A127275

## Verbatim Statement

From OEIS [A127276](https://oeis.org/A127276) (rev. 33), offset `0,3`:

> `NAME: Hankel transform of A127275.`
>
> `FORMULA: Conjectured g.f.: -(4*x-1)*(x-1) / ( (2*x-1)^3 ) and a(n) = 2^n-n*(n+1)*2^(n-2). - _R. J. Mathar_, Dec 11 2010`

Primary definition of `A127275` from OEIS [A127275](https://oeis.org/A127275) (rev. 18):

> `NAME: Expansion of (sqrt(1-4x)-x)/(1-4x).`

(Here the Hankel transform of a sequence $(b_m)_{m \ge 0}$ is $a(n) = \det\bigl(b_{i+j}\bigr)_{0 \le i,j \le n}$ for $n \ge 0$, matching `DATA: 1,1,-2,-16,-64,-208,-608,...`.)

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). Summary:
- `tools/novelty_grep.py A127276` across all `651` snapshot files (incl. Zenodo `23112421` and `23114921`): `0` hits.
- `A127276` (`rev. 33`) and related entries `A127275`, `A178987`, `A176126` contain no proof of Mathar's Hankel-transform g.f. / formula.
- arXiv API, Zenodo API, Crossref API, GitHub (`gh search issues/prs/repos`), and web search: `0` proofs found.
