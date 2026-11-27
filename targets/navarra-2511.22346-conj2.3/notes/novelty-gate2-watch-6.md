# Gate 2 Novelty Receipt (`watch-6`) — `targets/navarra-2511.22346-conj2.3/`

- **Checked UTC:** `2026-11-27T09:09:30Z`
- **Verdict:** **PASS** (open; no counterexample or proof beyond rank $\le 10$ / polyomino rank $\le 12$ found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 605 files including 434 `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "2511.22346" "Navarra" "rook polynomial"` -> hits only in `watch/snapshots/arxiv/arxiv_submissions.{json,md}` (3 unrelated 2026-11 papers co-authored by Francesco Navarra); `0` hits in competing repos.
2. **Live GitHub search (`gh search` & `gh api`):**
   - `gh search repos "2511.22346"` -> `[]`.
   - `gh search repos "switching rook"` -> `FrancescoNavarra95/collections-of-cells-rook-polynomials` (author verification code for Theorem 2.2) and `AcraeaTerpsicore/Combinatorics-of-Rooks-and-Hilbert-Poincare-Series` (`2025-12-02`, unrelated).
   - `gh search issues "2511.22346"` -> `[]`.
   - `gh search code "2511.22346"` -> `chy4pro/automath` `E25_pool_triage_cslo_macac.md` inspected via `gh api`: triage table listing `2511.22346` only (no attack/solution); remaining hits are arXiv RSS/bib catalogs.
3. **arXiv & Zenodo API:**
   - `tools/arxiv_fetch.py query --id-list 2511.22346`: `2511.22346v1` (`2025-11-27`) sole version.
   - `zenodo.org/api/records?q=2511.22346&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"2511.22346" OR "Navarra" "Conjecture 2.3" OR "rook polynomial" "coordinate ring" polyomino counterexample` -> returns only `arXiv:2511.22346v1`; no counterexample found.

## Coverage Limits
- Closed-access venues or private repositories not indexed by arXiv, GitHub, Zenodo, or `search_web` are not covered.
