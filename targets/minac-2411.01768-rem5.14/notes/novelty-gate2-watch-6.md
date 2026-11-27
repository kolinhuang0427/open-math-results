# Gate 2 Novelty Check — `targets/minac-2411.01768-rem5.14/`

- **Checked at:** `2026-11-27T10:31:57Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior refutation found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py 2411.01768 Minac "rem:same_degree" "So's conjecture"` -> `32` lines across `11/619` files:
     - `trureturing` `D5/S3/ArithUnits/MinacNguyenTanQuestion35.lean` (verified via `gh api`: formalizes `arXiv:2607.00404v1`, sums of units in finite rings/Cayley graphs — unrelated to Remark 5.14).
     - `arxiv_submissions` `2611.15026v2` (gcd-graphs over matrix rings $M_n(\mathbb{F}_q)$, not distinct-degree $\mathbb{F}_q[x]$).
     - Remaining hits are unrelated `"determinacy"` substring matches (`"rem"`/`"determinacy"`). `0` hits on Remark 5.14 or distinct-degree polynomials in $\mathbb{F}_q[x]$.
2. **GitHub search (`gh search repos`):**
   - `gh search repos "2411.01768"` -> `[]`.
   - `gh search issues "2411.01768"` -> `HTTP 403` GitHub Search API rate limit (`10:30:26Z`).
3. **arXiv live query (`id_list=2411.01768`):**
   - `arXiv:2411.01768v2` (`2026-08-03T02:49:58Z`) remains latest version.
4. **Zenodo API (`q=2411.01768`):**
   - `0` hits.
5. **Web search (`search_web`):**
   - Query `"2411.01768" OR ("Minac" "Nguyen" "Remark 5.14" OR "So's conjecture")` -> surfaces only `arXiv:2411.01768` and Wasin So's original paper; no refutation of Remark 5.14 found.

## Coverage Limits
- `gh search issues` hit `HTTP 403` rate limit at `10:30:26Z` and GitHub code search was skipped during cooldown; local snapshots (`619` files), `gh search repos`, `gh api` on `MinacNguyenTanQuestion35.md`, live arXiv, Zenodo API, and web search ran cleanly through `10:31:57Z`.
