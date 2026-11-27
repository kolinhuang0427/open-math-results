# Gate 3 Novelty Re-Check — `yip-2309.10950-rem3.1` (watch-5)

- **UTC Timestamp:** `2026-11-26T23:31:11Z`
- **Target:** `targets/yip-2309.10950-rem3.1/TARGET.md`
- **Verdict:** **PASS** (no public proof or settlement of the $d=2$ case of `thm:VLM` / Remark 3.3 for `GPS(q, 2)` when $q \ge 49$ is an odd square found across live arXiv, OpenAlex citing cache, Zenodo, Crossref, 356 snapshots, `aliromman/math`, `trureturing*`, or `KnowledgeSense/math`)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 356 files incl. `aliromman__math.json`, `trureturing*.json`, `KnowledgeSense__math.json`):**
   - `"2309.10950" "GPS(q,2)" "van Lint-MacWilliams" "S0008414X24000920"` -> `3` lines across `2/356` files (`watch/snapshots/arxiv/citing/yip-2309.10950-rem3.1.json` and `openalex_works_cache.json` only).

2. **GitHub Live Checks (`gh search` / `gh api`, read-only):**
   - `gh search code --repo aliromman/math "2309.10950 OR GPS ..."` and `gh search prs --repo aliromman/math "2309.10950 OR Yip OR Paley ..."` -> `0` matches.
   - `gh search code --repo KnowledgeSense/math "2309.10950 OR GPS ..."` and `repos/KnowledgeSense/math/contents/preprints` filter -> `0` matches (`NO_KS_MATCH`).
   - `gh search prs --repo the-omega-institute/trureturing "2309.10950 OR Yip ..."` -> `0` matches.
   - `gh search code --repo the-omega-institute/trureturing-tools "2309.10950 ..."` -> `0` matches.

3. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:2309.10950` -> `1` entry (`2309.10950v2`, `2023-09-19T22:19:25Z`, *Restricted sumsets in multiplicative subgroups*, sole/latest version).
   - `all:"GPS(q,2)"` -> `1` earlier entry (`2203.16081v3`, *On eigenfunctions and maximal cliques of generalised Paley graphs of square order*).

4. **OpenAlex Citing Cache (`watch/snapshots/arxiv/citing/yip-2309.10950-rem3.1.json`):**
   - Checked during 3h sweep at `2026-11-26T22:55:40Z` (`errors: []`): `citing_count: 0`, `citing_works: []`.

5. **Zenodo API (`https://zenodo.org/api/records`) & Crossref API (`https://api.crossref.org/works/10.4153/S0008414X24000920`):**
   - Zenodo `q=2309.10950` -> `0` hits.
   - Crossref DOI `10.4153/S0008414X24000920` -> `is-referenced-by-count: 2`, `update-to: None` (unchanged from Gate 2).

## Near Misses & Why They Do Not Settle the Exact Statement

- `arXiv:2203.16081v3` (2022, Yip): Studies cliques in generalized Paley graphs (difference graphs), predating `2309.10950v2` and not resolving Cayley sum graphs `GPS(q, 2)` ($q \ge 49$).
- `CONTESTED.md`: absent from `targets/yip-2309.10950-rem3.1/`.

## What Was Not Covered

- Semantic Scholar (`HTTP 429` unauthenticated) and closed-access/unindexed private manuscripts.
