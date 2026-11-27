# Gate 2 Novelty Check — `targets/schwob-2606.12129-conj8.7/`

- **Checked at:** `2026-11-27T10:40:59Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py 2606.12129 Schwob "cnj:Dtype" "Dtype"` -> `citing_papers.{json,md}` (`OpenAlex cited_by=0; S2=0`); remaining matches were unrelated `"Type"` substring hits across `619` files. `0` hits on Conjecture 8.7 (`cnj:Dtype`) or `D_n` middle orders.
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "2606.12129"` -> `[]`
   - `gh search issues "2606.12129"` -> only closed `the-omega-institute/trureturing#22269` (Liang–Sagan Question 8.6(a) on `Pin_n(\sigma)`, unrelated).
3. **arXiv live query (`id_list=2606.12129`):**
   - `arXiv:2606.12129v1` (`2026-06-10T14:22:22Z`) remains sole version.
4. **Zenodo API (`q=2606.12129`):**
   - `0` hits.
5. **Web search (`search_web`):**
   - Query `"2606.12129" OR ("Schwob" "8.7" OR "cnj:Dtype" OR "Young-Fibonacci" "2606.12129")` -> returns only `arXiv:2606.12129` itself; no prior proof found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`619` files), `gh search repos/issues`, live arXiv, Zenodo API, and web search ran at `2026-11-27T10:40:59Z`.
