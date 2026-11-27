# Gate 2 Novelty Check — `targets/kaul-2112.05316-ques3/`

- **Checked at:** `2026-11-27T10:23:19Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior refutation found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py 2112.05316 Kaul "ques: easier" "ques: classify"` -> `8` lines across `2/618` files (false substring match `"kaul"` inside `MiskaUlas` in `trureturing`). `0` hits on `2112.05316` or Kaul–Maxfield–Mudrock–Thomason.
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "2112.05316"` -> `[]`
   - `gh search issues "2112.05316"` -> `[]`
3. **arXiv live query (`id_list=2112.05316`):**
   - `arXiv:2112.05316v2` (`updated 2023-08-14T15:43:58Z`, published *Enumerative Combinatorics and Applications* 4 (2024)) remains latest version.
4. **Zenodo API (`q=2112.05316`):**
   - `0` hits.
5. **Web search (`search_web`):**
   - Query `"2112.05316" OR ("Kaul" "critical" "K_{2,p}" OR "2112.05316")` -> surfaces only `arXiv:2112.05316`; no prior refutation found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`618` files), `gh search repos/issues`, live arXiv, Zenodo API, and web search ran at `2026-11-27T10:23:19Z`.
