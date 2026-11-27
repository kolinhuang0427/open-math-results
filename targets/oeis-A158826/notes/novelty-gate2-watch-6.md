# Gate 2 Novelty Receipt (`watch-6`) — `targets/oeis-A158826/`

- **Checked UTC:** `2026-11-27T09:03:30Z`
- **Verdict:** **PASS** (open; no proof or refutation found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 604 files including 433 `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "A158826" "158826" "2407.20048" "Benfield"` -> `0` hits for `A158826` / `158826`.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "A158826 OR 158826 OR 2407.20048"` -> `[]`.
   - `gh search issues "A158826 OR 2407.20048"` -> `[]`.
3. **Live OEIS JSON & Zenodo API:**
   - `oeis.org/search?q=id:A158826&fmt=json`: revision `54` (`2026-05-25T10:12:49-04:00`) unchanged; Mathar's 2021 recurrence remains marked `Conjecture D-finite with recurrence`.
   - `zenodo.org/api/records?q=A158826&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"A158826" "R. J. Mathar" OR "D-finite" OR "117*a(n-4)"` -> surfaces only OEIS `A158826`; no proof found.

## Coverage Limits
- Live `gh search code` was skipped due to shared HTTP 429 rate-limit pressure; code coverage rests on `watch/snapshots/**` (604 files, 433 `discovered/` repo snapshots) plus live `gh search repos`/`issues`, live OEIS, Zenodo, and `search_web`.
