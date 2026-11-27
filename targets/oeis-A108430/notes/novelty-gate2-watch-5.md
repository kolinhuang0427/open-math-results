# Gate 2 Novelty Receipt — `oeis-A108430`

- **UTC Time:** 2026-11-26T21:14:45Z
- **Reviewer:** `watch-5` (arXiv & citing-papers slice)
- **Verdict:** **PASS** (no arXiv preprint, Zenodo preprint, Crossref publication, or web result found settling R. J. Mathar's 2022 D-finite recurrence for OEIS `A108430`)

## Sources & Exact Queries Checked

1. **Snapshot grep (`tools/novelty_grep.py A108430 "Mathar" "108430"`):**
   - Checked all 224 files under `watch/snapshots/**` (0.66s) -> `0` matches for `A108430` (other Mathar entries in `joaquimmj/oeis-conjectures`, `mathesis-papers`, `Wangwy-sjtu`, `linustalacko`, `s66lem` are for distinct OEIS sequences).
2. **Live arXiv API via `tools/arxiv_fetch.py` (`use_cache=False`):**
   - `all:A108430 OR (all:"108430" AND all:"Mathar")` (`max_results=10`) -> `0` results.
3. **Live Zenodo API (`https://zenodo.org/api/records`):**
   - `q=A108430` -> `0` hits.
   - `q="23982*n-28681"` -> `0` hits.
4. **Live Crossref API (`https://api.crossref.org/works`):**
   - `query="A108430 Mathar"` -> `0` matching math papers.
5. **Live Web Search (`search_web`):**
   - `"A108430" ("D-finite" OR "recurrence" OR "proved" OR "Mathar" OR "Schroeder" OR "Motzkin")` -> returns only OEIS `A108430` / `A108429` / `A027307` and Deutsch's 2000 *Amer. Math. Monthly* Problem 10658 link.

## Near Misses

- Emeric Deutsch (*Amer. Math. Monthly* 107, 2000, Problem 10658): establishes the path enumeration and bivariate functional equation, not Mathar's 2022 order-3 D-finite recurrence for `A108430`.
- `joaquimmj/oeis-conjectures` (`conjectures/dfinite/` and `conjectures/precalg/`): proved Mathar recurrences for other algebraic OEIS sequences (`A036766`, etc.), not `A108430`.

## What Was Not Covered

- OpenAlex API was unavailable during this check due to `HTTP 429 Too Many Requests` (IP daily budget exhausted).
- Semantic Scholar live API (rate-limited HTTP 429).
- Closed-access/print-only texts not indexed in arXiv, Zenodo, Crossref, or web search.
- GitHub repositories (covered separately by `watch-1` and `watch-6`).
