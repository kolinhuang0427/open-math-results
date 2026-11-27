# Gate 2 Novelty Receipt (`watch-5`) — `targets/riener-2605.25743-conjHermite/`

- **Checked UTC:** `2026-11-27T08:48Z` – `2026-11-27T08:52Z`
- **Verdict:** **PASS** (no `CONTESTED.md`)
- **Target Scope:** Cordian Riener and Boris Shapiro, `arXiv:2605.25743v3` (`2026-10-21`), Conjectures 1.1 (`conj:sos`) & 5.6 (`conj:hermite`) on derivative discriminants / Hermite-matrix SOS.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, rebuilt 2026-11-27T08:41Z–08:47Z):**
   - `.venv/bin/python tools/novelty_grep.py 2605.25743 Riener Shapiro 'Hermite-matrix' --max-per-file 3 --max-total 15`: `15` lines across `9/124` files (`0` hits for `2605.25743`, `Riener`, or `Hermite-matrix`; `Shapiro` hits are unrelated Erdős #951, Forsgard–Shapiro AMR21 Problem 0015, Rudin–Shapiro words, SupportForestMoments, cluster algebras).
2. **arXiv 7-category snapshot (1,000 entries) & OpenAlex citing sweep (`watch/snapshots/arxiv/`):**
   - `0` matches in 1,000 recent arXiv entries; OpenAlex `cited_by_count = 0`.
3. **Live arXiv API (`tools/arxiv_fetch.py`):**
   - `id_list=['2605.25743']`: confirms `2605.25743v3` (`2026-10-21T05:38:56Z`) remains latest version.
   - `abs:"2605.25743" OR ...`: `total: 0`.
4. **Web search (`search_web`):**
   - `"2605.25743" "Riener"`: returns only `2605.25743` itself.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by arXiv, OpenAlex, web search, or `watch/snapshots/**`.
