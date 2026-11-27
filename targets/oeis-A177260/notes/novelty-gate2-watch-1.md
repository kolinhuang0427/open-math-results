# Gate 2 Novelty Receipt (`watch-1`) — `targets/oeis-A177260/`

- **Checked UTC:** `2026-11-27T09:09Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 605 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 23 (`2026-11-27T08:49:42Z`): `0` hits for `A177260`, `177260`.
   - `.venv/bin/python tools/novelty_grep.py A177260 177260` -> `0` lines across `0/605` files.
2. **Live OEIS, Zenodo, and GitHub (`2026-11-27T09:09Z`):**
   - `https://oeis.org/search?q=id:A177260&fmt=json` -> revision `27` (`2025-11-05T15:22:18-05:00`), Mathar's Jul 26 2022 recurrence still marked `Conjecture:`.
   - `https://zenodo.org/api/records?q=A177260&size=3` -> `total: 0`.
   - **Near misses checked live via `gh api`:**
     - `gh search issues "A177260"` -> only `trureturing#27184` (unresolved probe on `A177259` mentioning `A177260` as sibling).
     - `Drogobo/fable-5-proof`: `contents` contains only `proof-A177258-mathar-conjecture.md` (proves `A177258` only, does not prove `A177260`).

## Coverage Limits
- `gh search code` was recently rate-limited (HTTP 429); closed-access venues and private repositories not covered.
