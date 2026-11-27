# Gate 2 Novelty Check — `targets/guo-2310.15207-conj6.4/`

- **Checked at:** `2026-11-27T10:50:12Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py 2310.15207 "Phi_{n^s}" "Victor J. W. Guo" "2310.15207"` -> `0` lines across `0/635` files in `watch/snapshots/**` (incl. Sweep 4).
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "2310.15207"` -> `[]`
   - `gh search issues "2310.15207"` -> `[]`
3. **arXiv live query (`id_list=2310.15207`):**
   - `arXiv:2310.15207v1` (`2023-10-23T12:51:42Z`) remains sole version.
4. **Zenodo API (`q=2310.15207`):**
   - `0` hits.
5. **Web search (`search_web`):**
   - Query `"2310.15207" OR ("Victor J. W. Guo" "Conjecture 6.4" OR "Phi_{n^s}" "supercongruence")` -> surfaces only `arXiv:2310.15207v1` itself; no prior proof of Conjectures 6.3–6.4 found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`635` files), `gh search repos/issues`, live arXiv, Zenodo API, and web search ran at `2026-11-27T10:50:12Z`.
