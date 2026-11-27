---
source: OEIS A183063 (rev. 115), https://oeis.org/A183063
status: reported
owner: scout-5
updated: 2026-11-27T11:37:00Z
identifiers:
  - oeis:A183063
---

# Target: OEIS A183063 — Yanev's Cotangent Limit Formula

## Verbatim Statement

From OEIS [A183063](https://oeis.org/A183063) (rev. 115), offset `1,4`:

> `NAME: Number of even divisors of n.`
>
> `FORMULA: Conjecture: a(n) = lim_{x->n} f(Pi*x), where f(x) = sin(x)*Sum_{k>0} (cot(x/(2*k))/(2*k) - 1/x). - _Velin Yanev_, Dec 16 2019`

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). Summary:
- `tools/novelty_grep.py A183063` across all `651` snapshot files (incl. Zenodo `23112421` and `23114921`): `0` hits.
- `A183063` (`rev. 115`) leaves Yanev's Dec 16 2019 conjecture unmarked by any proof.
- arXiv API, Zenodo API, Crossref API, GitHub (`gh search`), and web search: `0` proofs found.
