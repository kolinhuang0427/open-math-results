# Gate 3 Novelty Receipt (`watch-5`) — `targets/oeis-A177260/`

- **Checked UTC:** `2026-11-27T09:17Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/oeis-A177260/`)
- **Target Scope:** OEIS `A177260` (rev `27`, `2025-11-05T15:22:18-05:00`), R. J. Mathar's Jul 26 2022 D-finite recurrence conjecture $a(n) = (n-1)a(n-1) + (n-1)a(n-2) + 2a(n-4) + (n-1)a(n-5) + 3a(n-8)$.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 608 files):**
   - `.venv/bin/python tools/novelty_grep.py A177260 177260 --max-per-file 5 --max-total 10`: `0` lines across `0/608` files.
2. **Live arXiv API (`tools/arxiv_fetch.py`):**
   - `all:A177260 OR abs:"2407.20048"` (`max_age=300`): `total: 0`.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A177260&fmt=json`):**
   - Revision `27`, timestamp `2025-11-05T15:22:18-05:00` (unchanged; formula remains marked `Conjecture:`).
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A177260&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by OEIS, arXiv, Zenodo, or `watch/snapshots/**`.
