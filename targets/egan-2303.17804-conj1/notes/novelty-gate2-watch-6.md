# Gate 2 Novelty Check — `targets/egan-2303.17804-conj1/`

- **Checked at:** `2026-11-27T10:44:56Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py 2303.17804 Egan "113778" "edge-triangle"` -> `63` lines across `28/619` files (all false substring hits `"egan"` inside `"elegant"`, Hadamard `Egan-Kotsireas-London-O Cathain` `2610.27175`, and `Leo66Gao/solved-conjectures` `29-fractional-planks/edge-triangles.md` fractional planks). `0` hits on `2303.17804` or triangular degree-sequence realisations.
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "2303.17804"` -> `[]`
   - `gh search issues "2303.17804"` -> `[]`
3. **arXiv live query (`id_list=2303.17804`):**
   - `arXiv:2303.17804v1` (`2023-03-31T05:26:45Z`, *Discrete Mathematics* 347(2), 2024, Art. 113778) remains sole version.
4. **Zenodo API (`q=2303.17804`):**
   - `0` hits.
5. **Web search (`search_web`):**
   - Query `"2303.17804" OR "113778" ("Egan" "triangle" OR "degree sequence" "every edge")` -> surfaces only `arXiv:2303.17804v1` / *Discrete Mathematics* Art. 113778; no proof for simple graphs with $d_{\min} \ge 4$ found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`619` files), `gh search repos/issues`, live arXiv, Zenodo API, and web search ran at `2026-11-27T10:44:56Z`.
