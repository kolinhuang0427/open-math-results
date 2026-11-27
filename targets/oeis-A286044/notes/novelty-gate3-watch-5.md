# Gate 3 Novelty Receipt (`watch-5`) — `targets/oeis-A286044/`

- **Checked UTC:** `2026-11-27T08:52Z` – `2026-11-27T08:53Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/oeis-A286044/`)
- **Target Scope:** OEIS `A286044` (rev `8`, `2026-02-19T22:02:10-05:00`), Velin Yanev's Feb 16 2026 conjecture $a(n) = b(b(n-2)) - b(b(n-3))$ ($n > 3$, $b = \mathrm{A003160}$).

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 586 files, rebuilt 2026-11-27T08:41Z–08:47Z):**
   - `.venv/bin/python tools/novelty_grep.py A286044 286044 --max-per-file 3 --max-total 15`: `1` line across `1/586` files (only `joaquimmj__oeis-conjectures/files.txt: conjectures/phase0/A286044.txt`, problem statement listing; `0` proofs).
2. **arXiv 7-category snapshot (`watch/snapshots/arxiv/arxiv_submissions.json`, 1,000 entries) & live arXiv API (`tools/arxiv_fetch.py`):**
   - `0` matches in 1,000 recent arXiv entries.
   - Live query `all:A350963 OR all:A286044`: `total: 0`.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A286044&fmt=json`):**
   - Revision `8`, timestamp `2026-02-19T22:02:10-05:00` (unchanged; formula remains marked `Conjecture:`).

## What Was Not Covered
- Closed-access venues or private repositories not indexed by OEIS, arXiv, or `watch/snapshots/**`.
