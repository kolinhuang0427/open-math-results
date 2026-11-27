# Gate 2 Novelty Receipt (`watch-5`) — `targets/oeis-A045743/`

- **Checked UTC:** `2026-11-27T09:18Z`
- **Verdict:** **PASS** (no `CONTESTED.md`)
- **Target Scope:** OEIS `A045743` (rev `14`, `2022-07-26T14:31:19-04:00`), R. J. Mathar's Jul 26 2022 5-term D-finite recurrence conjecture for noncrossing connected graphs with no triangular faces.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 608 files):**
   - `.venv/bin/python tools/novelty_grep.py A045743 045743 --max-per-file 5 --max-total 15`: `0` lines across `0/608` files.
2. **arXiv 7-category snapshot (1,000 entries) & live arXiv API (`tools/arxiv_fetch.py`):**
   - `all:A045743 OR all:045743` (`max_age=300`): `total: 0`.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A045743&fmt=json`):**
   - Revision `14`, timestamp `2022-07-26T14:31:19-04:00` (unchanged; formula remains marked `Conjecture`).
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A045743&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by OEIS, arXiv, Zenodo, or `watch/snapshots/**`.
