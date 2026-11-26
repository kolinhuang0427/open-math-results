# Gate 3 Novelty Receipt — `ferrero-2511.16335-conj1.8`

- **UTC Time:** 2026-11-26T20:21:30Z
- **Reviewer:** `watch-5` (arXiv & citing-papers slice)
- **Verdict:** **PASS** (fresh live pre-report check confirms no new arXiv preprint, version update, OpenAlex citation, or web publication settles Conjecture 1.8 of `arXiv:2511.16335v1`)

## Fresh Live Sources & Exact Queries Checked

1. **Snapshot grep (`tools/novelty_grep.py 2511.16335 ferrero "standard fast join"`):**
   - Checked all 201 files under `watch/snapshots/**` (0.48s) -> 7 lines in 3 files (`1337` issue #323 on unrelated Boyer–Brimkov–English–Ferrero conjecture; `formal/last_sweep.json` referencing sibling `ferrero-2511.16335-conj1.7`). Zero matches for Conjecture 1.8.
2. **Live arXiv API via `tools/arxiv_fetch.py` (`use_cache=False`):**
   - `id_list=["2511.16335"]` -> still `2511.16335v1` (`2025-11-20T13:15:25Z`), no `v2` or comment update.
   - `cat:math.CO` (`max_results=15`, `sort_by="submittedDate"`) -> top ID `2611.34855v1`; 0 matches for `forcing`, `propagation`, `fast join`, `ferrero`, `hogben`.
   - `all:"zero forcing" AND (all:"fast join" OR all:"propagation time" OR all:"2511.16335")` (`max_results=10`, `sort_by="submittedDate"`) -> newest remains `2609.35522v1`, `2602.16300v1`, `2512.01429v1`, `2511.16335v1`.
3. **Live OpenAlex API (`https://api.openalex.org/works/W4416550551`):**
   - `W4416550551` (*"Zero forcing propagation time intervals and graphs with fixed propagation time"*) still has **`cited_by_count: 0`** (updated `2026-11-24T14:10:38`).
   - `search="standard fast join zero forcing"` (`sort="publication_date:desc"`) -> 0 relevant matches.
4. **Live Web Search (`search_web`):**
   - `"2511.16335" OR "standard fast join" "zero forcing" OR ("Zero forcing propagation time intervals" "counterexample")` -> returns only the primary paper (`arXiv:2511.16335` / *Australasian J. Combin.* 96, 2026) and its discussion of Warnberg's 2015 interval conjecture; no refutation of Conjecture 1.8.

## Near Misses

- `1337isnot1337/solved-conjectures` issue #323: Boyer–Brimkov–English–Ferrero–Keller–Kirsch–Phillips–Reinhart conjecture (different Ferrero paper).
- `arXiv:2609.35522v1` (McKay, Ray, Valliere, Sep 2026): discrepancy between min and max propagation times of minimum zero forcing sets, does not classify $\overline{\mathrm{pt}}(G) = 1$ or standard fast joins.

## What Was Not Covered

- Semantic Scholar live API (rate-limited HTTP 429).
- Closed-access/unpublished manuscripts not indexed on arXiv, OpenAlex, or web search.
- GitHub repositories (checked separately by `watch-1` and `watch-6`).
