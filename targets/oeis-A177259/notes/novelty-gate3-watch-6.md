# Gate 3 Novelty Receipt (`watch-6`) — `targets/oeis-A177259/`

- **Checked UTC:** `2026-11-27T09:15:15Z`
- **Verdict:** **PASS** (no competing proof or refutation found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 608 files including 436+ `discovered/` repo snapshots & `Drogobo/fable-5-proof`):**
   - Query: `.venv/bin/python tools/novelty_grep.py "A177259" "177259" "A108449" "108449"` -> `0` hits for `A177259` / `177259` across all 608 files (`Drogobo/fable-5-proof` proves sibling `A177258` only).
2. **Live GitHub search (`gh search`):**
   - `gh search repos "A177259"` -> `[]`.
   - `gh search issues "A177259"` -> `the-omega-institute/trureturing#27184` (already inspected via `gh api`: closed `Status: unresolved`, definitions only), plus unrelated `#28230` & `#28091`.
3. **Live OEIS JSON & Zenodo API:**
   - `oeis.org/search?q=id:A177259&fmt=json`: revision `28` (`2025-11-05T15:22:18-05:00`) unchanged; Mathar's 2022 recurrence remains marked `Conjecture: D-finite with recurrence`.
   - `zenodo.org/api/records?q=A177259&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"A177259" "R. J. Mathar" OR "adjacent 3-cycles" "(n-1)*a(n-1)" proved OR proof` -> no proof found.

## Coverage Limits
- Live `gh search code` skipped due to shared HTTP 429 rate-limit pressure; code coverage rests on `watch/snapshots/**` (608 files, 436+ `discovered/` repo snapshots) plus live `gh search repos`/`issues`, live OEIS, Zenodo, and `search_web`.
