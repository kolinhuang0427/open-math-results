# Gate 2 Novelty Check — targets/oeis-A101035/ (watch-6)

- **UTC Timestamp:** `2026-11-27T10:55:21Z`
- **Target:** `targets/oeis-A101035/` (`status: candidate`, `owner: scout-5`) — Benedict W. J. Irwin (Jul 26 2017) logarithmic generating function conjecture $\sum_{n,k>0} \mu(n)\mu(k)\log(1/(1-x^{nk}))$ for the Dirichlet inverse of Pillai's gcd-sum function (`A018804`).
- **Verdict:** **PASS** (no settled proof or counterexample found).

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py A101035 "101035"` (plus `A018804`, `"Irwin"`)
   - Result: `# 0 lines across 0/635 files in 0.90s` on `A101035`/`101035`; `A018804` had `0` hits, and `"Irwin"` hits in `atlas-lean` (`IrwinSeries*.lean` base-10 digit series) and `erdosproblems` (`Kirwin`) are unrelated.
2. **Live OEIS (`A101035` rev `37`, `2022-12-06T07:56:55-05:00`):**
   - `Conjecture: Logarithmic g.f. Sum_{n>0,k>0} mu(n)*mu(k)*log(1/(1-x^(n*k))). - _Benedict W. J. Irwin_, Jul 26 2017` remains unproved in OEIS.
3. **Zenodo API (`https://zenodo.org/api/records?q=%22A101035%22&size=5`):** `zenodo_hits: 0`.
4. **arXiv API (`all:A101035`):** `<opensearch:totalResults>0</opensearch:totalResults>`.
5. **GitHub Search (`gh search repos "A101035"`, `gh search issues "A101035"`):** Both returned `[]`.
6. **Web Search (`search_web`):** Clear; no paper proves Irwin's logarithmic g.f. identity for `A101035`.

## Coverage Limits
- `gh search code` not run after `0` repo/issue/local-snapshot hits under rate-limit budget; `arXiv` searched via literal OEIS ID `A101035`.
