# Gate 3 Novelty Receipt (`watch-6`) — `targets/bui-2508.04602-conj8.1/`

- **Checked UTC:** `2026-11-27T09:13:00Z`
- **Verdict:** **PASS** (no competing proof or counterexample of §8.2 acyclicity found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 607 files including 435+ `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "2508.04602" "2401.09497" "weakly consecutive"` -> `2508.04602` matched only `AlexenderSokolov/cross-theory-formal-database` (`editable-corpus/licenses/arxiv-2508.04602-CC-BY-4.0.txt`); `0` hits in competing proof repos.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "2508.04602"` -> `[]`.
   - `gh search issues "2508.04602"` -> `We-Solve/research#56` (literature report on Theorems 7.1–7.2 double-circle universality only, not §8.2 acyclicity).
3. **arXiv & Zenodo API:**
   - `tools/arxiv_fetch.py query --id-list 2508.04602,2401.09497`: `2508.04602v1` (`2025-08-06`) remains sole version.
   - `zenodo.org/api/records?q=2508.04602&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"2508.04602" OR "Bui" "Conjecture 8.1" OR "acyclic" "circular" "swap" OR "interval"` -> returns only `arXiv:2508.04602v1`.

## Coverage Limits
- Live `gh search code` skipped due to shared HTTP 429 rate-limit pressure; code coverage rests on `watch/snapshots/**` (607+ files, 435+ `discovered/` repo snapshots) plus live `gh search repos`/`issues`, arXiv, Zenodo, and `search_web`.
