# Gate 2 Novelty Receipt (`watch-1`) — `targets/oeis-A158826/`

- **Checked UTC:** `2026-11-27T09:02Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 604 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 23 (`2026-11-27T08:49:42Z`): `0` hits for `A158826`, `158826`.
   - `.venv/bin/python tools/novelty_grep.py A158826 158826` -> `0` lines across `0/604` files (covers `1337-solved-conjectures`, `joaquimmj/oeis-conjectures`, `trureturing*`, `mathesis-papers*`, `openai-math`, `discovered/`, `arxiv/`, `formal/`).
2. **Live OEIS, Zenodo, and GitHub Issues (`2026-11-27T09:02Z`):**
   - `https://oeis.org/search?q=id:A158826&fmt=json` -> revision `54` (`2026-05-25T10:12:49-04:00`), Mathar's Aug 30 2021 recurrence still marked `Conjecture`.
   - `https://zenodo.org/api/records?q=A158826&size=5` -> `total: 0`.
   - `gh search issues "A158826"` -> `0` issues.

## Coverage Limits
- `gh search code` was recently rate-limited (HTTP 429); closed-access venues and private repositories not covered.
