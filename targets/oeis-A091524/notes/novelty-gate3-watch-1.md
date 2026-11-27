# Gate 3 Novelty Receipt — `oeis-A091524`

- **UTC Time:** `2026-11-27T09:05Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 605 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 23 (`2026-11-27T08:49:42Z`): `0` hits for `A091524`, `091524`, `"A001521"`.
   - `.venv/bin/python tools/novelty_grep.py A091524 091524 "A001521"` -> `4` lines across `3/605` files, all concerning Erdős Problem #482 in `erdosproblems/`, unrelated to Kurkov's `A091524` formula.
2. **Live OEIS, Zenodo, and GitHub Issues (`2026-11-27T09:04Z`):**
   - `https://oeis.org/search?q=id:A091524&fmt=json` -> revision `27` (`2025-02-16T08:32:52-05:00`), unchanged (`Conjecture:`).
   - `https://zenodo.org/api/records?q=A091524&size=5` -> `total: 0`.
   - `gh search issues "A091524"` -> `0` issues.

## Coverage Limits
- `gh search code` was recently rate-limited (HTTP 429); closed-access venues and private repositories not covered.
