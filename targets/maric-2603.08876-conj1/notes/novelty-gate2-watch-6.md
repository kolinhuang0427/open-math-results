# Gate 2 Novelty Check — `targets/maric-2603.08876-conj1/`

- **Checked at:** `2026-11-27T10:21:48Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py 2603.08876 Maric "Maric"` -> `17` lines across `7/618` files (`citing_papers.{json,md}` OpenAlex `cited_by=0; S2=0`, unrelated `C. R. Marić` irrationality series in `plasma-ai__erdos`, and `Mathlib/NumberTheory/MaricaSchoenheim.lean`). `0` hits for Nevena Marić's Max-Cut geometric edge weights conjecture.
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "2603.08876"` -> `[]`
   - `gh search issues "2603.08876"` -> `[]`
3. **arXiv live query (`id_list=2603.08876`):**
   - `arXiv:2603.08876v1` (`2026-03-09T19:41:42Z`) remains sole version.
4. **Zenodo API (`q=2603.08876`):**
   - `0` hits.
5. **Web search (`search_web`):**
   - Query `"2603.08876" OR ("Maric" "Conjecture 5.1" "hyperelliptic" OR "2603.08876")` -> returns only `arXiv:2603.08876` itself; no prior resolution found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`618` files), `gh search repos/issues`, live arXiv, Zenodo API, and web search ran at `2026-11-27T10:21:48Z`.
