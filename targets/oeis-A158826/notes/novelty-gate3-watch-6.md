# Gate 3 Novelty Receipt (`watch-6`) — `targets/oeis-A158826/`

- **Checked UTC:** `2026-11-27T09:09:30Z`
- **Verdict:** **PASS** (no competing proof or refutation found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 605 files including 434 `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "A158826" "158826"` -> `0` hits across all 605 files.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "A158826"` -> `[]`.
   - `gh search issues "A158826"` -> `[]`.
3. **Live OEIS JSON & Zenodo API:**
   - `oeis.org/search?q=id:A158826&fmt=json`: revision `54` (`2026-05-25T10:12:49-04:00`) unchanged; Mathar's 2021 recurrence remains marked `Conjecture D-finite with recurrence`.
   - `zenodo.org/api/records?q=A158826&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"A158826" "R. J. Mathar" OR "1053*n" OR "Third iteration of x*C(x)" proved OR proof` -> surfaces only OEIS `A158826` and `A158825`; no proof found.

## Coverage Limits
- Live `gh search code "A158826"` hit GitHub's shared rate limit (`HTTP 429`, ~23s remaining); code coverage rests on `watch/snapshots/**` (605 files, 434 `discovered/` repo snapshots) plus live `gh search repos`/`issues`, live OEIS, Zenodo, and `search_web`.
