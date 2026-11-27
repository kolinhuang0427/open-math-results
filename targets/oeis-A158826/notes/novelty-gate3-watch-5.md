# Gate 3 Novelty Receipt (`watch-5`) — `targets/oeis-A158826/`

- **Checked UTC:** `2026-11-27T09:09Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/oeis-A158826/`)
- **Target Scope:** OEIS `A158826` (rev `54`, `2026-05-25T10:12:49-04:00`), R. J. Mathar's Aug 30 2021 D-finite recurrence conjecture for the 3rd iteration of $x C(x)$.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 605 files):**
   - `.venv/bin/python tools/novelty_grep.py A158826 158826 A177259 177259 A177260 177260 --max-per-file 5 --max-total 20`: `0` lines across `0/605` files.
2. **Live arXiv API (`tools/arxiv_fetch.py`):**
   - `abs:"2511.22346" OR all:A158826 OR all:A177259 OR all:A177260` (`max_age=300`): `total: 0`.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A158826&fmt=json`):**
   - Revision `54`, timestamp `2026-05-25T10:12:49-04:00` (unchanged; formula remains marked `Conjecture`).
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A158826&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by OEIS, arXiv, Zenodo, or `watch/snapshots/**`.
