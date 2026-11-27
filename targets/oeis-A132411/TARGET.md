---
source: OEIS A132411 (rev. 80), https://oeis.org/A132411
status: reported
owner: scout-5
updated: 2026-11-27T10:27Z
identifiers:
  - oeis:A132411
  - bala-2025
---

# OEIS A132411: Peter Bala (2025) $q$-Series Expansion Conjecture

## Exact Quoted Statement

From OEIS `A132411` (NAME and COMMENTS, rev. 80):

> **NAME:** a(0) = 0, a(1) = 1 and a(n) = n^2 - 1 with n >= 2.
>
> **COMMENTS:** Conjecture: the sequence terms are the exponents in the expansion of the q-series Sum_{n >= 0} q^(2*n) * Product_{k >= 2*n+2} 1 - (-q)^k = 1 + q^3 + q^8 + q^15 + q^24 + .... - _Peter Bala_, May 10 2025

## Gate 1 Novelty Receipt

Checked `2026-11-27T10:22Z`–`10:27Z`:
- `tools/novelty_grep.py A132411`: 0 lines across 0/618 files in `watch/snapshots/**`.
- Zenodo API (`https://zenodo.org/api/records?q=A132411&size=3`): `0` hits (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).
- arXiv API (`tools/arxiv_fetch.py search "A132411" 3`): `0` hits.
- Crossref API (`https://api.crossref.org/works?query=A132411&rows=3`): `0` hits.
- GitHub (`gh search issues A132411` only unrelated `nbbrd/sdmx-upptime#28139`; `gh search prs A132411`, `gh search repos A132411`: `0` matches).
- `search_web` (`"A132411" "Bala" OR "1 - (-q)^k" "1 + q^3 + q^8"`): only points to OEIS `A132411`.
- Live OEIS `A132411` rev. 80: Bala's May 10 2025 comment remains prefixed with `Conjecture:` with no confirmation note.
- Full check log in `notes/gate1-novelty.md`.
