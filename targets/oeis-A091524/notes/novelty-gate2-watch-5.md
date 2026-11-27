# Gate 2 Novelty Receipt (`watch-5`) — `targets/oeis-A091524/`

- **Checked UTC:** `2026-11-27T08:48Z` – `2026-11-27T08:52Z`
- **Verdict:** **PASS** (no `CONTESTED.md`)
- **Target Scope:** OEIS `A091524` (rev `27`, `2025-02-16`), Mikhail Kurkov's Apr 25 2024 conjecture $a(n) = \sqrt{\mathrm{A028982}(n)/\mathrm{A006337}(n)}$.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, rebuilt 2026-11-27T08:41Z–08:47Z):**
   - `.venv/bin/python tools/novelty_grep.py A091524 A028982 'Graham-Pollak' --max-per-file 3 --max-total 15`: `2` lines across `2/587` files (only `erdosproblems/{problems.yaml,pulls.json}` on Erdős Problem #482 / Trevor Morris formalization of Graham–Pollak and Stoll's theorem; `0` hits on `A091524` or Kurkov's formula).
2. **arXiv 7-category snapshot (1,000 entries) & live arXiv API (`tools/arxiv_fetch.py`):**
   - `0` matches in 1,000 recent arXiv entries.
   - Live query `all:A092920 OR all:A394511 OR all:A190969 OR all:A091524`: `total: 0`.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A091524&fmt=json`):**
   - Revision `27`, timestamp `2025-02-16T08:32:52-05:00` (unchanged; formula remains marked `Conjecture:`).
4. **Web search (`search_web`):**
   - `"A091524" "Kurkov"`: returns only OEIS `A091524`, no proof found.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by OEIS, arXiv, web search, or `watch/snapshots/**`.
