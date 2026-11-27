---
source: https://oeis.org/A092920 (rev. 56, Mar 14 2026)
status: reported
owner: scout-6
updated: 2026-11-27T05:27:00Z
identifiers: [A092920, A006789, strongly monotone partitions, Mikhail Kurkov]
---

# Target: OEIS A092920 (Kurkov 2023 Binary-Valuation / Binomial Sum Conjecture)

## Verbatim Statement
From OEIS **A092920** (author: `_Ralf Stephan_`, Apr 17 2004; latest revision `#56`, `2026-03-14T12:38:00-04:00`), offset `0,3`:

- **Name:**
  > Number of strongly monotone partitions of [n].
- **Data (`offset 0`):**
  > 1,1,2,4,9,22,58,164,496,1601,5502,20075,77531,315947,1354279,6087421,28611385,140239297,715116827,3785445032,20760746393,117759236340,689745339984,4165874930885,25911148634728,165775085602106,1089773992530717,7353740136527305
- **Formula (Conjecture):**
  > Conjecture: a(n) = Sum_{k=0..2^(n-1) - 1} b(k) for n > 0 with a(0) = 1 where b(2^m*(2n+1)) = Sum_{k=0..[m > 0]*(m-1)} binomial(m-1, k)*b(2^k*n) for m >= 0, n >= 0 with b(0) = 1. - _Mikhail Kurkov_, Apr 24 2023

## Gate 1 Novelty Receipt
- Checked at: `2026-11-27T05:21:50Z` – `05:26:00Z`
- `watch/snapshots/` (`tools/novelty_grep.py A092920 "strongly monotone partitions"`): `0` hits across `522` files.
- `tools/arxiv_fetch.py query 'all:A092920 OR all:"strongly monotone partitions"'`: `0` results.
- Zenodo API (`zenodo.org/api/records?q=A092920&size=5`): `0` hits.
- Crossref API (`api.crossref.org/works?query=A092920&rows=3`): `0` hits.
- GitHub (`gh search code A092920`): only `archmageirvine/joeis` (`A092920.java`), `africamonkey/OEIS-Spider` (`A092920.txt`), and unrelated non-math filename substrings; no proof found.
- Web search (`"A092920" "Mikhail Kurkov" OR "strongly monotone partitions" "binomial"`): no proof of Kurkov's Apr 2023 conjecture found.
- Live OEIS `A092920` (rev 56, `2026-03-14`): formula remains marked `Conjecture:`.
- Not covered: closed-access venues or private repos.
