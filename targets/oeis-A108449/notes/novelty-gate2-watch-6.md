# Gate 2 Novelty Receipt (`watch-6`) — `targets/oeis-A108449/`

- **Checked UTC:** `2026-11-27T09:15:15Z`
- **Verdict:** **PASS** (open; no proof or refutation found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 608 files including 436+ `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "A177259" "177259" "A108449" "108449"` -> `108449` matched only a `trureturing-source-theories` SHA256 hex digest (`09bf...108449cb...`); `0` hits for `A108449`.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "A108449"` -> `[]`.
   - `gh search issues "A108449"` -> `[]`.
3. **Live OEIS JSON & Zenodo API:**
   - `oeis.org/search?q=id:A108449&fmt=json`: revision `13` (`2025-11-05T15:35:31-05:00`) unchanged; Mathar's 2022 9-term recurrence remains marked `Conjecture D-finite with recurrence`.
   - `zenodo.org/api/records?q=A108449&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"A108449" "R. J. Mathar" OR "D-finite" OR "117*a(n-2)" OR "9-term" recurrence` -> surfaces only OEIS `A108449`; no proof found.

## Coverage Limits
- Live `gh search code` skipped due to shared HTTP 429 rate-limit pressure; code coverage rests on `watch/snapshots/**` (608 files, 436+ `discovered/` repo snapshots) plus live `gh search repos`/`issues`, live OEIS, Zenodo, and `search_web`.
