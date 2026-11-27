# Gate 2 Novelty Receipt (`watch-6`) — `targets/reyes-2310.16929-conj3.2/`

- **Checked UTC:** `2026-11-27T10:01:29Z`
- **Target:** Reyes–Dalfó–Fiol, `arXiv:2310.16929v1` / *Bol. Soc. Mat. Mex.* 30 (2024), Art. 11 (`DOI: 10.1007/s40590-023-00583-3`), Section 3, Conjecture 3.2 (`conjec-creix-alfa`)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2310.16929" "Reyes"`: `trureturing` has `reyes2023tokenspectra.md` / `NewLayerMaximaRefutation.lean` (refuting Conjecture 3.3 $\rho_k$ maxima only, explicitly excluding Conjecture 3.2 $\alpha_k$ minima); `0` hits settling Conjecture 3.2 across `618` snapshot files.
- `gh search repos "2310.16929" --limit 5`: `[]`
- `gh search issues "2310.16929" --limit 10`: `[]`
- `.venv/bin/python tools/arxiv_fetch.py query --id-list 2310.16929`: `2310.16929v1` (`2023-10-25`) remains sole arXiv version.
- Zenodo API (`https://zenodo.org/api/records?q=%222310.16929%22&size=5`): `0` records.
- `search_web` (`"2310.16929" OR ("Reyes" ...)`): returns only `2310.16929v1`, no refutation of Conjecture 3.2 found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`618` snapshot files) plus live `gh search repos` and `gh search issues`.
