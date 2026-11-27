# Gate 2 Novelty Receipt (`watch-6`) — `targets/oeis-A177259/`

- **Checked UTC:** `2026-11-27T09:09:30Z`
- **Verdict:** **PASS** (open; no proof or refutation found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 606 files including 435 `discovered/` repo snapshots, incl. newly snapshotted `Drogobo/fable-5-proof`):**
   - Query: `.venv/bin/python tools/novelty_grep.py "A177259" "177259" "A177260" "177260"` -> `0` hits across all 606 files.
   - Inspected `Drogobo/fable-5-proof` (`2026-07-01T22:09:51Z`, `1` file: `proof-A177258-mathar-conjecture.md`): proves sibling `A177258` only, not `A177259`.
2. **Live GitHub search (`gh search` & `gh api`):**
   - `gh search repos "A177259"` -> `[]`.
   - `gh search issues "A177259"` -> `the-omega-institute/trureturing#27184` (`2026-11-06`, plus unrelated `#28230`, `#28091`). Inspected `#27184` directly via `gh api`: closed out with `Status: unresolved` (definitions only, no proof or refutation).
3. **Live OEIS JSON & Zenodo API:**
   - `oeis.org/search?q=id:A177259&fmt=json`: revision `28` (`2025-11-05T15:22:18-05:00`) unchanged; Mathar's 2022 recurrence remains marked `Conjecture: D-finite with recurrence`.
   - `zenodo.org/api/records?q=A177259&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"A177259" "R. J. Mathar" OR "D-finite" OR "adjacent 3-cycles" OR "Drogobo"` -> no proof found.

## Near Misses
- `Drogobo/fable-5-proof/proof-A177258-mathar-conjecture.md`: settles sibling `A177258` only.
- `the-omega-institute/trureturing#27184`: threshold-0 probe on `A177259`, terminal `Status: unresolved`.

## Coverage Limits
- Live `gh search code` skipped due to shared HTTP 429 rate-limit pressure; code coverage rests on `watch/snapshots/**` (606 files, 435 `discovered/` repo snapshots) plus live `gh search repos`/`issues`, live OEIS, Zenodo, and `search_web`.
