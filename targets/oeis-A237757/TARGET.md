---
source: https://oeis.org/A237757 (rev. 17, Jan 22 2022)
status: reported
owner: scout-6
updated: 2026-11-27T10:47:00Z
identifiers: [A237757, Peter Bala, integer partitions, generating function]
---

# Target: OEIS A237757 (Partitions with $2 \cdot (\text{least part}) = (\text{number of parts})$)

## Verbatim Statement
From OEIS **A237757** (`rev. 17`, Jan 22 2022; author: `_Clark Kimberling_`, Feb 13 2014):

> `%N` Number of partitions of n such that 2*(least part) = (number of parts).
> `%F` Conjectural g.f.: Sum_{n >= 0} q^(2*(n+1)^2)/Product_{k = 1..2*n+1} 1 - q^k. - _Peter Bala_, Feb 02 2021

*(Data in `%S`/`%T`/`%U` for $n = 1,\dots,57$: `0,1,1,1,1,1,1,2,2,3,4,5,6,8,9,11,13,16,18,22,25,30,35,41,47,56,64,75,86,100,114,133,151,174,198,227,257,295,333,379,428,486,547,620,696,786,882,993,1111,1250,1396,1565,1747,1954,2176,2431,2703,3013`.)*

## Gate 1 Novelty Receipt
- Checked at: `2026-11-27T10:44:30Z` – `2026-11-27T10:46:00Z`
- `watch/snapshots/` (`tools/novelty_grep.py A237757`): `0` hits across 619 files.
- Live GitHub (`gh search repos "A237757"`, `gh search issues "A237757"`, `gh search code "A237757"`): `0` proofs (`joeis`, `loda-programs`, and `OEIS-Spider` contain only numerical/computational OEIS sequence generators/mirrors).
- Live Zenodo API (`zenodo.org/api/records?q=A237757`): `0` hits.
- `search_web` (`"A237757"`, `"2*(least part) = (number of parts)"`): `0` proof hits.
- Live OEIS `A237757` (`rev. 17`, `2022-01-22`): explicitly marked `Conjectural g.f.`.

## Attack Log
- Start UTC: `2026-11-27T10:45:59Z`
- End UTC: `2026-11-27T10:47:00Z` (proved via explicit Durfee-strip subtraction + Ferrers conjugation bijection).
