# OEIS A274272: Partitions of $5^n$ into at most Four Parts

- **Source:** OEIS [A274272](https://oeis.org/A274272) (rev. 12, `NAME` and `FORMULA` sections), submitted by Colin Barker (Jun 17 2016).
- **Status:** reported
- **Owner:** scout-6
- **Started:** 2026-11-27T11:35:19Z
- **Updated:** 2026-11-27T11:41:00Z
- **Identifiers:** `OEIS:A274272`

## Verbatim Conjecture Statement

From OEIS `A274272` (rev. 12, `NAME` and `FORMULA` sections):

> **NAME:** `Number of partitions of 5^n into at most four parts.`
>
> **FORMULA:**
> `Coefficient of x^(5^n) in 1/((1-x)*(1-x^2)*(1-x^3)*(1-x^4)).`
> `Conjectures (Start)`
> `a(n) = (57+8*(-1)^n+63*5^n+3*5^(1+2*n)+125^n)/144.`
> `a(n) = 155*a(n-1)-3874*a(n-2)+15470*a(n-3)+3875*a(n-4)-15625*a(n-5) for n>4.`
> `G.f.: (1-149*x+3129*x^2-5655*x^3-6750*x^4) / ((1-x)*(1+x)*(1-5*x)*(1-25*x)*(1-125*x)).`
> `(End)`

## Gate 1 Novelty Receipt

Checked at `2026-11-27T11:35:19Z`:
- `tools/novelty_grep.py A274272 --max-total 0` -> `0` hits across `0/653` snapshot files.
- `watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`, `watch/snapshots/cohen-zenodo-24384895-oeis-ids.md`, `mylesparslow-collab/mylesparslow-collab.github.io` -> `0` hits.
- Zenodo API (`zenodo.org/api/records?q=A274272`) -> `0` hits.
- arXiv API (`all:A274272`) -> `0` results.
- GitHub code/issues (`gh search code A274272`, `gh search code "A274272 sequencelib"`, `gh search code "A274272 conjecture"`, `gh search issues A274272`) -> only OEIS mirrors (`joeis`, `loda-programs`, `OEIS-Spider`) and unrelated hex/URLs; `0` proofs or issues.
- Web search -> confirms open OEIS entry with no published proof of Barker's $5^n$ closed form, recurrence, or rational g.f.
