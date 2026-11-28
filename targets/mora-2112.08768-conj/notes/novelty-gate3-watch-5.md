# Gate 3 Novelty & Pre-Report Verification — `mora-2112.08768-conj` (`watch-5`)

- **Target:** `targets/mora-2112.08768-conj/` — Mercè Mora, María José Souto-Salorio, and Ana Dorotea Tarrío-Tobar, *"Resolving sets tolerant to failures in three-dimensional grids"*, `arXiv:2112.08768v1` / *Mediterr. J. Math.* 19 (2022), art. 188 (`DOI:10.1007/s00009-022-02096-1`), Section 3 Conjecture 21 (**FALSE**, $\dim_{14}(P_3\Box P_3\Box P_4) \le 30 < 32$).
- **Checked UTC:** `2026-11-27T18:45:37Z`–`2026-11-27T18:45:50Z`
- **Gate 3 Verdict:** **PASS (UNCONTESTED + CHECKER PASS)** — fresh (<1h) live novelty checks confirm open/uncontested status and independent checker passes cleanly.

## Fresh Live Novelty Queries (`18:45Z`)
1. **Local snapshots (`watch/snapshots/**`, 762 files):**
   - `.venv/bin/python tools/novelty_grep.py "2112.08768" "s00009-022-02096-1" "three-dimensional grids" --max-per-file 10 --max-total 40`: `0` lines across `0/762` files.
2. **Live GitHub (`gh`):**
   - `gh search issues "2112.08768"` & `gh search prs "2112.08768"`: `0` hits.
   - `the-omega-institute/trureturing` recent PRs up to `#34947`: `0` overlapping PRs.
3. **Live Preprint & Citation APIs (`18:45:48Z`):**
   - `arXiv` API (`id_list=2112.08768`): `2112.08768v1` (`2021-12-16T10:26:03Z`) sole version.
   - `OpenAlex` (`W4285008974`): `cited_by_count: 5` unchanged from Gate 2 (`18:40Z`), where all citing papers (`2410.03656`, `2610.13374`, `2307.13403`, `math13040560`, `s00010-024-01062-4`, `ICDCECE68961.2026.11645934`) were verified non-settling.
   - `Zenodo` (`q=2112.08768`): `0` hits.

## Independent Checker Verification
- Command: `.venv/bin/python -u targets/mora-2112.08768-conj/notes/check-check-3.py`
- Exit code: `0` (`BFS == L1 distance on P_3 x P_3 x P_4: OK`, `(3,3,4,13): OK`, `(3,3,5,15): OK`, `(3,4,4,15): OK`, `(4,4,4,17): OK`, `PASS`).
- Verified files present: `targets/mora-2112.08768-conj/{TARGET.md,COUNTEREXAMPLE.md,AUDIT.md,notes/check-check-3.py}`.

## Near-Misses & Coverage Limits
- **Near-misses:** `2410.03656` and `2610.13374` study general/outerplanar fault-tolerant metric dimension, not 3D grids.
- **Coverage limits:** Private/unindexed drafts posted after `2026-11-27T18:45:50Z` are not covered.
