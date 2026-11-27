# Gate 2 Novelty Receipt (`watch-6`) — `targets/oeis-A177260/`

- **Checked UTC:** `2026-11-27T09:09:30Z`
- **Verdict:** **PASS** (open; no proof or refutation found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 606 files including 435 `discovered/` repo snapshots, incl. newly snapshotted `Drogobo/fable-5-proof`):**
   - Query: `.venv/bin/python tools/novelty_grep.py "A177259" "177259" "A177260" "177260"` -> `0` hits across all 606 files.
   - Inspected `Drogobo/fable-5-proof` (`2026-07-01T22:09:51Z`, `1` file: `proof-A177258-mathar-conjecture.md`): proves sibling `A177258` only, not `A177260`.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "A177260"` -> `[]`.
   - `gh search issues "A177260"` -> `the-omega-institute/trureturing#27184` (`2026-11-06`, unresolved probe on sibling `A177259`); `0` proofs of `A177260`.
3. **Live OEIS JSON & Zenodo API:**
   - `oeis.org/search?q=id:A177260&fmt=json`: revision `27` (`2025-11-05T15:22:18-05:00`) unchanged; Mathar's 2022 recurrence remains marked `Conjecture: D-finite with recurrence`.
   - `zenodo.org/api/records?q=A177260&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"A177260" "R. J. Mathar" OR "D-finite" OR "adjacent 4-cycles" OR "Drogobo"` -> surfaces only OEIS `A177260`; no proof found.

## Near Misses
- `Drogobo/fable-5-proof/proof-A177258-mathar-conjecture.md`: settles sibling `A177258` only.

## Coverage Limits
- Live `gh search code` skipped due to shared HTTP 429 rate-limit pressure; code coverage rests on `watch/snapshots/**` (606 files, 435 `discovered/` repo snapshots) plus live `gh search repos`/`issues`, live OEIS, Zenodo, and `search_web`.
