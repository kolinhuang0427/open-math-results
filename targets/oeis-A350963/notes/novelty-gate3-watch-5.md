# Gate 3 Novelty Receipt (`watch-5`) — `targets/oeis-A350963/`

- **Checked UTC:** `2026-11-27T08:52Z` – `2026-11-27T08:53Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/oeis-A350963/`)
- **Target Scope:** OEIS `A350963` (rev `54`, `2025-11-05T15:22:48-05:00`), N. J. A. Sloane's conjectured generating function for the XXOXX tiling coordination sequence.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 586 files, rebuilt 2026-11-27T08:41Z–08:47Z):**
   - `.venv/bin/python tools/novelty_grep.py A350963 350963 --max-per-file 3 --max-total 15`: `2` lines across `2/586` files (`350963` only as a SHA-256 substring in `trureturing-source-theories`; `0` hits for `A350963`).
2. **arXiv 7-category snapshot (`watch/snapshots/arxiv/arxiv_submissions.json`, 1,000 entries) & live arXiv API (`tools/arxiv_fetch.py`):**
   - `0` matches in 1,000 recent arXiv entries.
   - Live query `all:A350963 OR all:A286044`: `total: 0`.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A350963&fmt=json`):**
   - Revision `54`, timestamp `2025-11-05T15:22:48-05:00` (unchanged; formula remains marked `Conjectured g.f.`).

## What Was Not Covered
- Closed-access venues or private repositories not indexed by OEIS, arXiv, or `watch/snapshots/**`.
