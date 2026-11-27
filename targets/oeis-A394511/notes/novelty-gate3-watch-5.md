# Gate 3 Novelty Receipt (`watch-5`, refreshed) — `targets/oeis-A394511/`

- **Checked UTC:** `2026-11-27T08:48Z` – `2026-11-27T08:52Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/oeis-A394511/`)
- **Target Scope:** OEIS `A394511` (rev `47`, `2026-06-06T04:04:55-04:00`), Peter Exley's truncated-square (`4.8.8`) enclosing shell conjecture ($|S| = |C(H)|$, $a(n) = 2\lceil (n+17)/5\rceil$ for $n \ge 6$, $a(n) = a(n-5)+2$ for $n \ge 11$, disproved).

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, rebuilt 2026-11-27T08:41Z–08:47Z):**
   - `.venv/bin/python tools/novelty_grep.py A394511 Kurkov --max-per-file 3 --max-total 15`: `0` hits on `A394511` (all `15` lines across `7/368` files were unrelated `Kurkov` entries).
2. **arXiv 7-category snapshot (`watch/snapshots/arxiv/arxiv_submissions.json`, 1,000 entries) & live arXiv API (`tools/arxiv_fetch.py`):**
   - Sweep 1 (`math.CO`, `math.NT`, `cs.DM`, `math.GR`, `math.AC`, `math.RA`, `math.RT` + `lastUpdatedDate`): `0` matches to `oeis-A394511`.
   - Live query `all:A092920 OR all:A394511 OR all:A190969 OR all:A091524`: `total: 0`.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A394511&fmt=json`):**
   - Revision `47`, timestamp `2026-06-06T04:04:55-04:00` (unchanged; remains marked `Conjectured (UNVERIFIED beyond n = 23)`).

## What Was Not Covered
- Closed-access venues or private repositories not indexed by OEIS, arXiv, or `watch/snapshots/**`.
