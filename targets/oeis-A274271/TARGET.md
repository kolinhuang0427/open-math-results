# OEIS A274271: Partitions of $3^n$ into at most Four Parts

- **Source:** OEIS [A274271](https://oeis.org/A274271) (rev. 12, `NAME` and `FORMULA` sections), submitted by Colin Barker (Jun 17 2016).
- **Status:** reported
- **Owner:** scout-6
- **Started:** 2026-11-27T11:31:56Z
- **Updated:** 2026-11-27T11:54:00Z
- **Identifiers:** `OEIS:A274271`

## Verbatim Conjecture Statement

From OEIS `A274271` (rev. 12, `NAME` and `FORMULA` sections):

> **NAME:** `Number of partitions of 3^n into at most four parts.`
>
> **FORMULA:**
> `Coefficient of x^(3^n) in 1/((1-x)*(1-x^2)*(1-x^3)*(1-x^4)).`
> `Conjectures (Start)`
> `a(n) = ((3+3^n)^2*(9+3^n))/144 for n>1.`
> `a(n) = 40*a(n-1)-390*a(n-2)+1080*a(n-3)-729*a(n-4) for n>4.`
> `G.f.: (1-37*x+288*x^2-405*x^3-81*x^4) / ((1-x)*(1-3*x)*(1-9*x)*(1-27*x)).`
> `(End)`

## Gate 1 Novelty Receipt

Checked at `2026-11-27T11:31:56Z`:
- `tools/novelty_grep.py A274271` -> `0` hits across `0/653` snapshot files.
- `watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`, `watch/snapshots/cohen-zenodo-24384895-oeis-ids.md`, and `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`) -> `0` hits.
- Zenodo API (`zenodo.org/api/records?q=A274271`) -> `0` hits.
- arXiv API (`all:A274271`) -> `0` results.
- GitHub code/issues (`gh search code A274271`, `gh search issues A274271`) -> only routine OEIS database mirrors (`joeis`, `loda-programs`, `OEIS-Spider`); `0` proof repos or issues.
- Web search -> confirms open OEIS entry; standard quasipolynomial formulas for $p(m, \le 4)$ do not appear in a published proof of Colin Barker's $3^n$ specialization and rational g.f.
