# Gate 3 Novelty Receipt (`watch-5`) — `targets/oeis-A190969/`

- **Checked UTC:** `2026-11-27T09:00Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/oeis-A190969/`)
- **Target Scope:** OEIS `A190969` (rev `48`, `2025-11-05T15:22:20-05:00`) & `FormalConjectures/OEIS/190969.lean`: Zhi-Wei Sun supercongruences for $a(n) = 5a(n-1) - 8a(n-2)$, $S(p) \equiv 0 \pmod{p^2}$ (odd prime $p$) and $\pmod{p^3}$ ($p \equiv 1,2,4 \pmod 7$).

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 601 files):**
   - `.venv/bin/python tools/novelty_grep.py A190969 190969 "5*a(n-1)" --max-per-file 3 --max-total 15`: `8` lines across `4/601` files (`FormalConjectures/OEIS/190969.lean`, `BoltonBailey/formal-conjectures-ai-review` audit spec, `epoch-research/LeanOpenProblems`, and `epoch-research/LeanOpenProblems-results` where `scores.json` shows `sorryAx` failure — verified at Gate 2).
2. **arXiv 7-category snapshot (1,000 entries) & live arXiv API (`tools/arxiv_fetch.py`):**
   - Live query `all:A190969 OR abs:"2411.00721"` (`max_age=300`): `total: 0`.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A190969&fmt=json`):**
   - Revision `48`, timestamp `2025-11-05T15:22:20-05:00` (unchanged; conjectures remain open).
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A190969&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by OEIS, arXiv, Zenodo, or `watch/snapshots/**`.
