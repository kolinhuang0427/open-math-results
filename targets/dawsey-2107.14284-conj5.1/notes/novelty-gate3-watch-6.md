# Gate 3 Novelty Receipt (`watch-6`) — `targets/dawsey-2107.14284-conj5.1/`

- **Checked UTC:** `2026-11-27T09:07:00Z`
- **Verdict:** **PASS** (no competing proof or refutation found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 605 files including 434 `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "A097332" "097332" "2107.14284" "idx(p)"` -> `2107.14284` matched only `watch/snapshots/arxiv/` citing cache (`citing_papers.{json,md}`, `last_sweep_report.json`); `0` hits in `discovered/`, `1337-solved-conjectures/`, `openai-math/`, `ai-collections/`, or `formal/`.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "2107.14284"` -> `[]`.
   - `gh search issues "2107.14284"` -> `[]`.
3. **arXiv & Zenodo API:**
   - `tools/arxiv_fetch.py query --id-list 2107.14284`: `2107.14284v2` (`2021-09-14`) remains latest.
   - `zenodo.org/api/records?q=2107.14284&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"2107.14284" OR "Dawsey" "Just" "Schneider" "Conjecture 4.1" OR "idx(p)" proved OR proof` -> returns only `arXiv:2107.14284` / *J. Number Theory* 241 (2022) and follow-up `2511.20829` (prime model, unrelated to Conjecture 4.1); no proof found.

## Coverage Limits
- Live `gh search code` skipped due to shared HTTP 429 rate-limit pressure; paywalled *J. Number Theory* 241 PDF was not fetched; code coverage rests on `watch/snapshots/**` (605 files, 434 `discovered/` repo snapshots) plus live `gh search repos`/`issues`, arXiv, Zenodo, and `search_web`.
