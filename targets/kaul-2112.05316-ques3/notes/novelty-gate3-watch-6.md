# Gate 3 Novelty Check — `targets/kaul-2112.05316-ques3/`

- **Checked at:** `2026-11-27T10:31:23Z`
- **Checker:** `watch-6`
- **Audit reviewed:** `AUDIT.md` (re-audit PASS by `audit-2`; cmd `.venv/bin/python -u targets/kaul-2112.05316-ques3/notes/check-check-2.py`; paths `targets/kaul-2112.05316-ques3/{TARGET.md,COUNTEREXAMPLE.md,AUDIT.md,notes/check-check-2.py}`)
- **Result:** **PASS (no settling prior resolution found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py 2112.05316 "ques: easier" "ques: classify"` -> `0` lines across `0/619` files in `watch/snapshots/**`.
2. **arXiv live query (`id_list=2112.05316`):**
   - `arXiv:2112.05316v2` (`updated 2023-08-14T15:43:58Z`, published *Enumerative Combinatorics and Applications* 4 (2024)) remains latest version.
3. **Zenodo API (`q=2112.05316`):**
   - `0` hits.
4. **GitHub (`gh search repos/issues`):**
   - Checked fresh in Gate 2 (`10:23:19Z`: `[]`); live `gh search` skipped at `10:31:23Z` during transient GitHub API TLS/rate-limit window.

## Coverage Limits
- GitHub code search and live GitHub search at `10:31Z` were skipped due to rate-limit/TLS timeout (Gate 2 `gh search repos/issues` ran clear at `10:23:19Z`); local snapshots (`619` files), live arXiv, and Zenodo API queries ran at `10:31:23Z`.
