# Gate 3 Novelty Check (`watch-6`): `targets/mirzavaziri-2610.19249-conj1/`

- **Checked UTC:** `2026-11-27T11:47:50Z`
- **Target:** M. Mirzavaziri & D. Yaqubi, `arXiv:2610.19249v1` §1 Conjecture 1.1 (`conj:GK` = Guo–Krattenthaler `arXiv:1301.7651v3` §7 Conjecture 7.4 `conj:330n88n`) and §4 Conjecture 4.4 (`conj:general`).
- **Verdict:** **PASS** (<1h freshness confirmed; no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files, refreshed through Sweep 6):**
   - `.venv/bin/python -u tools/novelty_grep.py 2610.19249 1301.7651 Mirzavaziri` -> `41` lines across `11/658` files — `trureturing#21322` / `MirzavaziriYaqubiMonotonicityRefutation.lean` (Problem 7.2 monotonicity refutation only), `trureturing#34438` / Zenodo `24552279` / `s66lem` (`Yaqubi–Mirzavaziri` Conjecture 6.2 / PDO, unrelated), `OjasMor` / `andrheabacor` (Conjecture 8, unrelated), and cached `citing_papers.md` (`arXiv:2610.26878` Prellberg–Stanton). Zero settlement hits on Conjecture 1.1 / 4.4 / 7.4.
2. **Live arXiv (`.venv/bin/python -u tools/arxiv_fetch.py abs 2610.19249` & `1301.7651`):** `2610.19249v1` and `1301.7651v3` remain the latest versions.
3. **Zenodo API (`2610.19249+OR+1301.7651`):** `hits.total: 0`.
4. **GitHub (`gh search repos/issues 2610.19249`, `1301.7651`):** `repos` `[]`; `issues` only `trureturing#21322` (Problem 7.2) and `trureturing#12062` (Basu-Mallick `1503.08231`).
5. **Web search (`search_web` for `"2610.19249" OR "1301.7651" Mirzavaziri Guo Krattenthaler proof`):** returned only `2610.19249v1` ($n \ge 2 \cdot 10^{29}$ asymptotic proof) and `1301.7651v3`.

## Coverage Limits

- arXiv API covers metadata rather than PDF full text; offline or unindexed manuscripts are outside direct visibility.
