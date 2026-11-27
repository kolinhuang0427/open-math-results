# OEIS A392058 / A233335: Self-Referential Antidiagonal Array Equivalence

- **Source:** OEIS [A392058](https://oeis.org/A392058) (rev. 6, `NAME` and `FORMULA` sections), submitted by Mikhail Kurkov (Dec 29 2025); cross-referenced with OEIS [A233335](https://oeis.org/A233335) (rev. 20, submitted by Paul D. Hanna, Dec 07 2013).
- **Status:** reported
- **Owner:** scout-6
- **Started:** 2026-11-27T11:41:52Z
- **Updated:** 2026-11-27T11:54:00Z
- **Identifiers:** `OEIS:A392058`, `OEIS:A233335`

## Verbatim Conjecture Statement

From OEIS `A392058` (rev. 6, `NAME` and `FORMULA` sections) and OEIS `A233335` (rev. 20, `NAME` section):

> **A392058 NAME:** `Array read by downward antidiagonals: A(n,k) = A(n-1,k+1) + Sum_{j=0..k} binomial(k+1,j)*A(n-1,j)*A(k-j,0) with A(0,k) = 1.`
>
> **A392058 FORMULA:**
> `Conjecture: A(n,0) = A233335(n+1).`
>
> **A233335 NAME:** `E.g.f. A(x) satisfies A( Integral 1/A(x) dx ) = exp(x).`

## Gate 1 Novelty Receipt

Checked at `2026-11-27T11:41:52Z`:
- `tools/novelty_grep.py A392058 --max-total 0` -> `0` hits across `0/658` snapshot files.
- `watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`, `watch/snapshots/cohen-zenodo-24384895-oeis-ids.md`, and `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`) -> `0` hits.
- Zenodo API (`zenodo.org/api/records?q=A392058`) -> `0` hits.
- arXiv API (`all:A392058`) -> `0` results.
- GitHub code/issues (`gh search code A392058`, `gh search issues A392058`) -> only routine `joeis` entry; `0` proofs or issues.
- Web search -> `0` prior proofs located.
