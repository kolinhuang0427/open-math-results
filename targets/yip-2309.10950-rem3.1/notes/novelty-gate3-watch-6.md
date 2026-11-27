# Novelty Receipt — Gate 3 (`watch-6`)

- **Target:** `targets/yip-2309.10950-rem3.1/` (Chi Hoi Yip `arXiv:2309.10950v2` / *Canad. J. Math.* 78 (2026), 594–618, Remark 3.3 / `thm:VLM` for $d=2$, odd squares $q \ge 49$)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-26T23:27:07Z`
- **Requested by:** `@audit-3` (board #421)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`, 356 files incl. `aliromman__math.json`, `trureturing-tools`, `KnowledgeSense__math.json`):**
   - Command: `.venv/bin/python tools/novelty_grep.py 2309.10950 "GPS(q" "Paley sum"` -> `3` index/cache hits (`watch/snapshots/arxiv/citing/yip-2309.10950-rem3.1.json`, `openalex_works_cache.json`); `0` competing hits.
2. **Competing Repo Checks (`aliromman/math`, `the-omega-institute/trureturing*`, `KnowledgeSense/math`):**
   - Direct snapshot substring scan for `2309.10950`, `Paley sum`, `GPS(q`, `van Lint`, `Yip` returned `0` hits across `KnowledgeSense__math.json`, `aliromman__math.json`, and `the-omega-institute__trureturing-tools.json`.
3. **GitHub Live Search & arXiv (`gh`, `tools/arxiv_fetch.py`):**
   - `gh search code "2309.10950"` -> only RSS/arXiv index mirrors (`ehijano/rss_fetch`, `pritam-roy-99/axiovo`) and unrelated numeric matches (`COMPAS-Surrogate`, `SlopDotCash`).
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2309.10950` -> `2309.10950v2` (`Can. J. Math. 78 (2026) 594-618`, `10.4153/S0008414X24000920`) remains sole latest version.

## Near Misses
- `arXiv:2608.02568v3` (Cochrane–Yip–Yoo) and `arXiv:2611.28533v1` (Cochrane–Cochrane–Spencer) treat multiplicative subgroups over prime fields / $|A+A|$ lower bounds, not cliques in $GPS(q, 2)$ over odd squares $q \ge 49$.

## Not Covered
- Paywalled publications, private repositories, and offline manuscripts not referencing `2309.10950`.
