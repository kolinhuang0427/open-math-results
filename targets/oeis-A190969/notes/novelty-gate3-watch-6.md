# Gate 3 Novelty Receipt (`watch-6`) — `targets/oeis-A190969/`

- **Checked UTC:** `2026-11-27T09:01:00Z`
- **Verdict:** **PASS** (no competing proof or refutation found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 601 files including 430 `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "A190969" "190969" "4096"` -> `A190969` / `190969` matched only `FormalConjectures/OEIS/190969.lean` (`formal/`), `epoch-research/LeanOpenProblems-results` (`discovered/`, failed `sorryAx` runs), and unrelated `trureturing` SHA256/issue IDs.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "A190969 OR 2411.00721"` -> `[]`.
   - `gh search issues "A190969 OR 2411.00721"` -> `[]`.
3. **Live OEIS JSON & Zenodo API:**
   - `oeis.org/search?q=id:A190969&fmt=json`: revision `48` (`2025-11-05`) unchanged; both supercongruences remain marked `conjectured`.
   - `zenodo.org/api/records?q=A190969&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"A190969" "5*a(n-1)-8*a(n-2)" OR "a(4k)*binomial(2k,k)^3" OR "4096" supercongruence` -> no proof found.

## Near Misses
- `epoch-research/LeanOpenProblems-results` runs for `oeis_a190969` failed SafeVerify (`sorryAx`).
- `FormalConjectures/OEIS/190969.lean` is statement-only (`category research open`).

## Coverage Limits
- Live `gh search code "A190969"` hit GitHub's shared secondary/rate limit (`HTTP 429`); code coverage rests on `watch/snapshots/**` (601 files, 430 `discovered/` repo snapshots) plus live `gh search repos`/`issues`, live OEIS, Zenodo, and `search_web`.
