---
source: OEIS A026927 (rev. 23), https://oeis.org/A026927
status: reported
owner: scout-5
updated: 2026-11-27T11:51:00Z
identifiers:
  - oeis:A026927
  - oeis:A026923
---

# Target: OEIS A026927 — Barker's Generating Function and Linear Recurrence

## Verbatim Statement

From OEIS [A026927](https://oeis.org/A026927) (rev. 23), offset `1,6`:

> `NAME: Number of partitions of n into an even number of parts, the greatest being 3; also, a(n+5) = number of partitions of n+2 into an odd number of parts, each <= 3.`
>
> `FORMULA:`
> `Conjectures from _Colin Barker_, Sep 01 2019: (Start)`
> `G.f.: x^4*(1 + x^2 - x^3 + x^4) / ((1 - x)^3*(1 + x)^2*(1 - x + x^2)*(1 + x^2)*(1 + x + x^2)).`
> `a(n) = a(n-1) + a(n-4) - a(n-5) + a(n-6) - a(n-7) - a(n-10) + a(n-11) for n>11.`
> `(End)`

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). Summary:
- `tools/novelty_grep.py A026927` across all `658` snapshot files (plus live `mylesparslow-collab` ledger): `0` hits.
- `A026927` (`rev. 23`) has `LINK: None` and leaves Colin Barker's Sep 01 2019 G.f. and 11-term recurrence marked `Conjectures from _Colin Barker_`.
- arXiv API, Zenodo API, Crossref API, GitHub (`gh search`), and web search: `0` proofs found.
