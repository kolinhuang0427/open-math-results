# Gate 3 Novelty Receipt — `yip-2309.10950-rem3.1`

- **UTC Time:** 2026-11-26T23:32:30Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Live Pre-Report Re-Checks Performed

1. **Local watch snapshots (`watch/`):**
   - Sweep 7 (`2026-11-26T23:05:56Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py 2309.10950 "GPS(q,2)" ...` -> 0 hits beyond our own target citation cache (`citing/yip-2309.10950-rem3.1.json`, `openalex_works_cache.json`).
2. **Live `1337isnot1337/solved-conjectures`, `trureturing`, `trureturing-tools` (`gh api`, read-only):**
   - `1337isnot1337/solved-conjectures` `commits/main` (`3f55d55b2c`, `2026-11-26T22:58:27Z`) & recent PRs/issues -> unrelated.
   - `the-omega-institute/trureturing-tools` (`SCREENED-OUT.md`, `SCREENED-OUT-R52.md`, `SCREENED-OUT-R71.md` + `search/issues`) -> 0 hits for `2309.10950` or `Yip`.
3. **Live `aliromman/math` & `KnowledgeSense/math` (`gh api`, read-only):**
   - `aliromman/math` (all PRs/issues and 102 tree files) -> 0 hits for `2309.10950`, `Yip`, `Paley`, `Peisert`.
   - `KnowledgeSense/math` (all 5,377 tree files and 56 `preprints/` directories, last commit `2026-10-14T07:35:51Z`) -> 0 hits for `2309.10950` / `Yip` / `Paley` / `Peisert` (`Ordinary-and-Restricted-Sumset-Sizes-Beyond-a-Polynomial-Threshold` treats $h$-fold integer sumsets, unrelated).
4. **Live Zenodo API:**
   - `https://zenodo.org/api/records?q=2309.10950&size=5` -> `total: 0`.

## What Was Not Covered

- Live arXiv/Crossref/OpenAlex re-query (covered by `@watch-5`) and private repositories.
