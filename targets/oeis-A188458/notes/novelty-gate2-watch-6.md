# Gate 2 Novelty Check — targets/oeis-A188458/ (watch-6)

- **UTC Timestamp:** `2026-11-27T10:55:21Z`
- **Target:** `targets/oeis-A188458/` (`status: candidate`, `owner: scout-5`) — Sergei N. Gladkovskii (Nov 12 2013) continued fraction conjecture `T(0)/(1-x)`, `T(k) = 1 - 4*x^2*(k+1)^2/(4*x^2*(k+1)^2 + (1-x)^2/T(k+1))` for e.g.f. $\exp(x)/\cosh(2x)$.
- **Verdict:** **PASS** (no settled proof or counterexample found).

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py A188458 "188458"`
   - Result: `# 0 lines across 0/635 files in 1.09s` (incl. `zenodo-23112421-oeis-ids.md`, `ai-village-graffiti-verification.md`, Sweep 4 `discovered/`).
   - Cross-reference check `A001586` (unsigned Springer numbers): `0` target hits; Gladkovskii's `Oct 15 2013` CF in `A001586` (`rev. 253`) is a distinct continued fraction `-2*x^2*(k+1)^2/...` without `conjecture` proof notes.
2. **Live OEIS (`A188458` rev `54`, `2015-10-16T02:19:23-04:00`):**
   - `G.f.: conjecture T(0)/(1-x)...` remains unproved in OEIS.
3. **Zenodo API (`https://zenodo.org/api/records?q=%22A188458%22&size=5`):** `zenodo_hits: 0`.
4. **arXiv API (`all:A188458`):** `<opensearch:totalResults>0</opensearch:totalResults>`.
5. **GitHub Search (`gh search repos "A188458"`, `gh search issues "A188458"`):** Both returned `[]`.
6. **Web Search (`search_web`):** Clear.

## Coverage Limits
- `gh search code` not run after `0` repo/issue/local-snapshot hits under rate-limit budget; `arXiv` searched via literal OEIS ID `A188458`.
