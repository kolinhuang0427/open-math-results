# Gate 2 Novelty Check — `targets/kallat-2610.40342-ques14.8/`

- **Checked at:** `2026-11-27T10:15:56Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof/counterexample found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py 2610.40342 Kallat "prob:composite"` -> `3` lines across `3/618` files (`trureturing` `Library/FiniteGroups/kallat2026weightedpermutations.md` library note + `formal-conjectures#8038` citing Kallat's $p$-local method for `A012780`). `0` hits on Question 14.8 (`prob:composite`) or type II least periods.
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "2610.40342"` -> `[]`
   - `gh search issues "2610.40342"` -> only automated `bguanmath/ArXiv_MathNT#437–439` paper listings.
3. **arXiv live query (`id_list=2610.40342`):**
   - `arXiv:2610.40342v1` (`2026-10-29T16:04:37Z`) remains sole version.
4. **Zenodo API (`q=2610.40342`):**
   - `0` hits.
5. **Web search (`search_web`):**
   - Query `"2610.40342" OR ("Kallat" "composite" "Question 14.8" OR "prob:composite")` -> surfaces only `arXiv:2610.40342v1` itself; no prior resolution found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`618` files), `gh search repos/issues`, live arXiv, Zenodo API, and web search ran at `2026-11-27T10:15:56Z`.
