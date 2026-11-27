---
source: OEIS A165204 (rev. 15), https://oeis.org/A165204
status: reported
owner: scout-5
updated: 2026-11-27T11:46:00Z
identifiers:
  - oeis:A165204
  - oeis:A165203
---

# Target: OEIS A165204 — Barker's Generating Function and Recurrence for Hankel Transform of A165203

## Verbatim Statement

From OEIS [A165204](https://oeis.org/A165204) (rev. 15), offset `0,2`:

> `NAME: Hankel transform of A165203.`
>
> `FORMULA:`
> `Conjectures from _Colin Barker_, Feb 10 2018: (Start)`
> `G.f.: (1 - 8*x + 2*x^2 - x^3) / (1 - 3*x + 8*x^2 - 3*x^3 + x^4).`
> `a(n) = 3*a(n-1) - 8*a(n-2) + 3*a(n-3) - a(n-4) for n>3.`
> `(End)`

Primary definition of `A165203` from OEIS [A165203](https://oeis.org/A165203) (rev. 28), offset `0,2`:

> `NAME: Expansion of (1+x)*c(x)^3/(1-x*c(x)^3), c(x) the g.f. of A000108.`

(Here the Hankel transform of $F_0(x) = \sum_{m=0}^{\infty} b_m x^m$ is $a(n) = \det(b_{i+j})_{0 \le i,j \le n}$ for $n \ge 0$, matching `DATA: 1,-5,-21,-21,89,377,377,-1597,-6765,-6765,...`.)

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). Summary:
- `tools/novelty_grep.py A165204` across all `653` snapshot files: `0` hits.
- `A165204` (`rev. 15`) has `LINK: None` and leaves Colin Barker's Feb 10 2018 G.f. and 4-term recurrence marked `Conjectures from _Colin Barker_`.
- arXiv API, Zenodo API, Crossref API, GitHub (`gh search`), and web search: `0` proofs found.
