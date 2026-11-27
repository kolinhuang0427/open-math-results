# Gate 2 Novelty Check — `targets/mirzavaziri-2610.19249-conj1/`

- **Checked at:** `2026-11-27T10:31:57Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof of `conj:GK` / `conj:general` found; near-miss disclosure noted)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py 2610.19249 Mirzavaziri "conj:GK" "conj:general"` -> `38` lines across `11/619` files:
     - **Near miss (`trureturing`):** `D5/S3/Combinatorics/GaussianQuotient/MirzavaziriYaqubiMonotonicityRefutation.lean` (inspected `Blueprint/.../MirzavaziriYaqubiMonotonicityRefutation.md` via `gh api`): refutes **Problem 7.2** / `conj:almost` monotonicity sufficiency in `2610.19249v1` (*"Is $\binom{N}{k}_q/[a]_q$ weakly increasing from $q^1$ sufficient for $\binom{N}{k}_q/([a]_q[b]_q)$ to have only two $-1$ coefficients?"*), which is distinct from `conj:GK` and `conj:general` (and `attack-4` explicitly left `conj:almost` open!).
     - Other matches (`andrheabacor__open-conjecture-results.json` `MirzavaziriYaqubi8`, `s66lem__conjectures.json` `YaqubiMirzavaziriPDO`, `trureturing#34438`) concern unrelated papers (`arXiv:2611.18194` / PDO / odd designated summands).
2. **arXiv live query (`id_list=2610.19249`):**
   - `arXiv:2610.19249v1` (`2026-10-13T22:05:49Z`) remains sole version.
3. **Zenodo API (`q=2610.19249`):**
   - `0` hits.
4. **Web search (`search_web`):**
   - Query `"2610.19249" OR ("Mirzavaziri" "Krattenthaler" "conj:GK")` -> surfaces only `arXiv:2610.19249v1` and `arXiv:1301.7651`; no proof closing `[301, 10^{30})` for `conj:GK` / `conj:general` found.

## Coverage Limits
- `gh search repos/issues` hit transient GitHub TLS timeout/rate-limit at `10:30:26Z` and code search was skipped during cooldown; local snapshots (`619` files), `gh api` inspection of `MirzavaziriYaqubiMonotonicityRefutation.md`, live arXiv, Zenodo API, and web search ran through `10:31:57Z`.
