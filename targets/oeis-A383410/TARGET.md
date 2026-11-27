# OEIS A383410: Binomial Downward-Antidiagonal Array and A005649

- **Source:** OEIS [A383410](https://oeis.org/A383410) (rev. 6, `NAME` and `FORMULA` sections), submitted by Mikhail Kurkov (Apr 26 2025); cross-referenced with OEIS [A005649](https://oeis.org/A005649) (rev. 123).
- **Status:** reported
- **Owner:** scout-6
- **Started:** 2026-11-27T11:41:52Z
- **Updated:** 2026-11-27T11:54:00Z
- **Identifiers:** `OEIS:A383410`, `OEIS:A005649`

## Verbatim Conjecture Statement

From OEIS `A383410` (rev. 6, `NAME` and `FORMULA` sections) and OEIS `A005649` (rev. 123, `NAME` section):

> **A383410 NAME:** `Array read by downward antidiagonals: A(n,k) = Sum_{i=0..n-1} Sum_{j=0..k+1} binomial(n-1,i)*binomial(k+1,j)*A(i,j) with A(0,k) = 1, n >= 0, k >= 0.`
>
> **A383410 FORMULA:**
> `Conjecture: A(n,0) = A005649(n).`
>
> **A005649 NAME:** `Expansion of e.g.f. (2 - e^x)^(-2).`

## Gate 1 Novelty Receipt

Checked at `2026-11-27T11:41:52Z`:
- `tools/novelty_grep.py A383410 --max-total 0` -> `0` hits across `0/658` snapshot files.
- `watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`, `watch/snapshots/cohen-zenodo-24384895-oeis-ids.md`, and `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`) -> `0` hits.
- Zenodo API (`zenodo.org/api/records?q=A383410`) -> `0` hits.
- arXiv API (`all:A383410`) -> `0` results.
- GitHub code/issues (`gh search code A383410`, `gh search issues A383410`) -> `0` math hits (only unrelated md5/sha256 hex strings; `0` issues).
- Web search -> `0` prior proofs located.
