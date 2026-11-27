# Gate 3 Novelty Receipt (`watch-6`) — `targets/chervov-2509.19162-conj9/`

- **Checked UTC:** `2026-11-27T09:05:15Z`
- **Verdict:** **PASS** (no competing proof or refutation of Conjecture 9 found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 605 files including 434 `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "A091524" "091524" "2509.19162" "CayleyPy" "unitriangular"` -> `2509.19162` matched only `watch/snapshots/arxiv/` citing cache (`citing_papers.{json,md}`, `last_sweep_report.json`); `CayleyPy` / `unitriangular` hits in `trureturing` (`CayleyPyConjectureOneRefutation.md`, `NikolovSegal/TypeA/Unitriangular`), `1337-solved-conjectures` (`valiant-extended/LOCAL_LAW.md`), and `facebookresearch/atlas-lean` (`Kourovka18Problem86`) are unrelated to Conjecture 9 / `U(n, Z/2Z)` / `OEIS A136184`.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "2509.19162"` -> `[]`.
   - `gh search issues "2509.19162"` -> 1 unrelated hit: `the-omega-institute/trureturing#10230` (Chervov et al. `arXiv:2603.22195` Conjecture 16, $k=3$).
3. **arXiv & Zenodo API:**
   - `tools/arxiv_fetch.py query --id-list 2509.19162`: `2509.19162v2` (`2026-04-01`) remains latest.
   - `zenodo.org/api/records?q=2509.19162&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"2509.19162" "Conjecture 9" OR "unitriangular" "CayleyPy" counterexample OR proved` -> returns only `arXiv:2509.19162`; no prior refutation found.

## Near Misses
- `the-omega-institute/trureturing` (`CayleyPyConjectureOneRefutation`, `#10230`): address Conjecture 1 (`2509.19162`) and Conjecture 16 (`2603.22195`), not Conjecture 9 (`U(n, Z/2Z)` vs `A136184`).

## Coverage Limits
- Live `gh search code` skipped due to shared HTTP 429 rate-limit pressure; code coverage rests on `watch/snapshots/**` (605 files, 434 `discovered/` repo snapshots) plus live `gh search repos`/`issues`, arXiv, Zenodo, and `search_web`.
