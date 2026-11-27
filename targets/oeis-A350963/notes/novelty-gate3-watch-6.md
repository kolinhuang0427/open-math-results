# Gate 3 Novelty Receipt (`watch-6`) — `targets/oeis-A350963/`

- **Checked UTC:** `2026-11-27T08:56:00Z`
- **Verdict:** **PASS** (no competing proof found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 601 files including 430 `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "A350963" "350963" "A092243"` -> `0` hits for `A350963` / `350963` anywhere (`A092243` matched only `mrigankswork/oeis-a092243-lean` prime-gap tug of war, unrelated).
2. **Live GitHub search (`gh search`):**
   - `gh search repos "2411.00721 OR A190969 OR 2605.25743 OR 2107.14284 OR A350963 OR A286044"` -> `[]`.
   - `gh search issues "2411.00721 OR A190969 OR 2605.25743 OR 2107.14284 OR A350963 OR A286044"` -> `[]`.
3. **Web search (`search_web`):**
   - Query: `"A350963" OR "XXOXX tiling" "coordination sequence"` -> no published proof of Sloane's conjectured generating function found.

## Coverage Limits
- Live `gh search code` returned `HTTP 429` (shared rate limit); code coverage rests on `watch/snapshots/**` (601 files, 430 `discovered/` repo snapshots) plus live `gh search repos`/`issues` and `search_web`.
