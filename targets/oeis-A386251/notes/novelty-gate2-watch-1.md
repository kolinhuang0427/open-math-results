# Gate 2 Novelty Receipt — `oeis-A386251`

- **UTC Time:** 2026-11-26T22:22:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 5 (`2026-11-26T22:07:29Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py A006255 Padhi A386251 2512.24346 Linusson` -> 0 hits for `A386251`.
2. **Live `the-omega-institute/trureturing` & GitHub (`gh api`, read-only):**
   - `search/issues?q=repo:the-omega-institute/trureturing+"A386251"` -> `#27151` (preregistration to refute Charles L. Hohn's OEIS `A386671` bilateral-symmetry conjecture, distinct sequence/statement).
   - Global `search/issues?q="A386251"` -> `#27151` and unrelated git SHA (`Unipg-Racing-Team/Provone#2`).
   - Global `search/code?q=A386251` -> 489 items (random hash/hex substring noise).
3. **Live OEIS, arXiv & Zenodo:**
   - `https://oeis.org/search?q=id:A386251&fmt=json` -> revision `22` (`2025-08-06T00:07:55-04:00`), unchanged.
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A006255" OR all:"A386251"'` -> `total_results: 0`.
   - `https://zenodo.org/api/records?q=A386251&size=5` -> `total: 0`.

## Near Misses

- `trureturing#27151` targets Charles L. Hohn's `A386671` (distinct conjecture); `A385525` is Hohn's equal-length sibling sequence.

## What Was Not Covered

- Closed-access publications and private repositories.
