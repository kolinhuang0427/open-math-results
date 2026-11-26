# Gate 3 Novelty Receipt — `oeis-A250917`

- **UTC Time:** 2026-11-26T21:56:30Z
- **Reviewer:** `watch-5` (arXiv & citing-papers slice)
- **Verdict:** **PASS** (fresh live pre-report check confirms no new arXiv preprint, Zenodo preprint, or web result settles R. J. Mathar's 2020 order-5 D-finite recurrence for OEIS `A250917`)

## Fresh Live Sources & Exact Queries Checked

1. **Snapshot grep (`tools/novelty_grep.py 2512.18169 Takemura "APD_m" A341743 A108430 A250917`):**
   - Checked all 224 files under `watch/snapshots/**` (0.71s) -> `0` matches for `A250917`.
2. **Live arXiv API via `tools/arxiv_fetch.py` (`use_cache=False`):**
   - `all:A341743 OR all:A108430 OR all:A250917 OR (all:"Eulerian graphs" AND all:"A062199")` -> `0` results.
   - `cat:math.CO` (`max_results=15`, `sort_by="submittedDate"`) -> top ID `2611.34855v1`; `0` matches for `a250917`.
3. **Live Zenodo API (`https://zenodo.org/api/records`):**
   - `q=A250917` -> `0` hits.
4. **Live Web Search (`search_web`):**
   - `"A250917" "Catalan" "recurrence" OR "exp(x*C(x)^3)" 2026` -> returns only OEIS `A250917` context.

## Near Misses

- `gfis/OEIS-mat` / `archmageirvine/joeis` Maple `sumrecursion` output and general D-finite closure of $\exp(\text{algebraic})$ (do not prove Mathar's explicit order-5 recurrence).

## What Was Not Covered

- Crossref live query for `A250917` hit `HTTP 429 Too Many Requests`; OpenAlex and Semantic Scholar also at `HTTP 429`.
- GitHub repositories (covered separately by `watch-1` and `watch-6`).
