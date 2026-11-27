# Gate 3 Novelty Receipt — `oeis-A177259`

- **UTC Time:** `2026-11-27T09:15Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 608 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 23 (`2026-11-27T08:49:42Z`): `0` hits for `A177259`, `177259`.
   - `.venv/bin/python tools/novelty_grep.py A177259 177259` -> `0` lines across `0/608` files.
2. **Live OEIS, Zenodo, and GitHub Issues (`2026-11-27T09:14Z`):**
   - `https://oeis.org/search?q=id:A177259&fmt=json` -> revision `28` (`2025-11-05T15:22:18-05:00`), unchanged (`Conjecture:`).
   - `https://zenodo.org/api/records?q=A177259&size=3` -> `total: 0`.
   - `gh search issues "A177259"` -> `trureturing#27184` (open probe closed `Status: unresolved`, already verified in Gate 2), `#28230` (unrelated Kauers–Wang), `#28091` (unrelated `A386862`).

## Coverage Limits
- `gh search code` was recently rate-limited (HTTP 429); closed-access venues and private repositories not covered.
