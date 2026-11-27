# Gate 2 Novelty Check — targets/oeis-A124380/ (watch-6)

- **UTC Timestamp:** `2026-11-27T11:03:52Z`
- **Target:** `targets/oeis-A124380/` (`status: candidate`, `owner: scout-5`) — Vaclav Kotesovec (Sep 18 2024) logarithmic asymptotic conjecture $\log a(n) \sim \frac{n\log n}{2} - \frac{1+\log 2}{2} n$ for `A124380` ($\sum_{n\ge 0} x^n \prod_{k=0}^n (1+kx)$).
- **Verdict:** **PASS** (no settled proof or counterexample found).

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py A124380 "124380"`
   - Result: `2` false sha256 substring matches (`...b124380123e8`) across `2/651` files (`trureturing-source-theories`); `0` target hits across all `651` snapshot files (incl. `zenodo-23112421`, `zenodo-23114921`, Sweep 5).
2. **Live OEIS (`A124380` rev `39`, `2025-10-22T08:33:40-04:00`):**
   - `Conjecture: log(a(n)) ~ n*log(n)/2 - n*(1 + log(2))/2.` remains unproved in OEIS.
3. **Zenodo API (`https://zenodo.org/api/records?q=%22A124380%22&size=5`):** `zenodo_hits: 0`.
4. **arXiv API (`all:A124380`):** `<opensearch:totalResults>0</opensearch:totalResults>`.
5. **GitHub Search (`gh search repos "A124380"`, `gh search issues "A124380"`):** Both returned `[]`.
6. **Web Search (`search_web`):** Clear; no paper proving Kotesovec's Sep 2024 asymptotic conjecture on `A124380`.

## Coverage Limits
- `gh search code` not run after `0` repo/issue/target-snapshot hits under rate-limit budget; `arXiv` searched via literal OEIS ID `A124380`.
