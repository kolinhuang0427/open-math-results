# Gate 2 Novelty Check — `targets/hardt-2412.06976-conj7.5/`

- **Checked at:** `2026-11-27T10:29:08Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py 2412.06976 Hardt Wallach "2412.06976"` -> `54` lines across `18/618` files (all false/unrelated matches: `Pickhardt`, `hardt-trivialization`, `Casselman--Wallach`, `gourwallach2010fourqubits`). `0` hits on `2412.06976` or back-stable key polynomials.
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "2412.06976"` -> `[]`
   - `gh search issues "2412.06976"` -> `[]`
3. **arXiv live query (`id_list=2412.06976`):**
   - `arXiv:2412.06976v2` (`updated 2025-01-24T18:29:51Z`) remains latest version.
4. **Zenodo API (`q=2412.06976`):**
   - `0` hits.
5. **Web search (`search_web`):**
   - Query `"2412.06976" OR ("Hardt" "Wallach" "Conjecture 7.5" OR "key polynomials")` -> surfaces only `arXiv:2412.06976v2` itself; no prior proof of Conjecture 7.5 found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`618` files), `gh search repos/issues`, live arXiv, Zenodo API, and web search ran at `2026-11-27T10:29:08Z`.
