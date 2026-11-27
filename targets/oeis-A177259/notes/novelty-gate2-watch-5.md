# Gate 2 Novelty Receipt (`watch-5`) — `targets/oeis-A177259/`

- **Checked UTC:** `2026-11-27T09:09Z`
- **Verdict:** **PASS** (no `CONTESTED.md`)
- **Target Scope:** OEIS `A177259` (rev `28`, `2025-11-05T15:22:18-05:00`), R. J. Mathar's Jul 26 2022 D-finite recurrence conjecture $a(n) = (n-1)a(n-1) + (n-1)a(n-2) + a(n-3) + (n-1)a(n-4) + 2a(n-6)$.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 605 files):**
   - `.venv/bin/python tools/novelty_grep.py A158826 158826 A177259 177259 A177260 177260 --max-per-file 5 --max-total 20`: `0` lines across `0/605` files.
2. **Live arXiv API (`tools/arxiv_fetch.py`):**
   - `abs:"2511.22346" OR all:A158826 OR all:A177259 OR all:A177260` (`max_age=300`): `total: 0`.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A177259&fmt=json`):**
   - Revision `28`, timestamp `2025-11-05T15:22:18-05:00` (unchanged; formula remains marked `Conjecture:`).
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A177259&size=5`):**
   - `total: 0`.
5. **Near-miss note:** `Drogobo/fable-5-proof` (flagged on `oeis-A177258`) proved only `A177258`; `trureturing#27184` closed `Status: unresolved` on `A177259` / `A177260`.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by OEIS, arXiv, Zenodo, or `watch/snapshots/**`.
