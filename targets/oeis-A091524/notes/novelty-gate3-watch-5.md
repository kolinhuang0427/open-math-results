# Gate 3 Novelty Receipt (`watch-5`) — `targets/oeis-A091524/`

- **Checked UTC:** `2026-11-27T09:04Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/oeis-A091524/`)
- **Target Scope:** OEIS `A091524` (rev `27`, `2025-02-16T08:32:52-05:00`), Mikhail Kurkov's Apr 25 2024 conjecture $a(n) = \sqrt{\mathrm{A028982}(n)/\mathrm{A006337}(n)}$.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 605 files):**
   - `.venv/bin/python tools/novelty_grep.py A091524 A028982 "Graham-Pollak" --max-per-file 5 --max-total 15`: `2` lines across `2/605` files (only `erdosproblems/{problems.yaml,pulls.json}` on Erdős Problem #482 / Stoll; `0` hits on `A091524` or Kurkov's formula).
2. **arXiv 7-category snapshot (1,000 entries) & live arXiv API (`tools/arxiv_fetch.py`):**
   - Live query `all:A091524 OR abs:"2509.19162"` (`max_age=300`): `total: 0`.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A091524&fmt=json`):**
   - Revision `27`, timestamp `2025-02-16T08:32:52-05:00` (unchanged; formula remains marked `Conjecture:`).
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A091524&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by OEIS, arXiv, Zenodo, or `watch/snapshots/**`.
