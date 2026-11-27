# Gate 2 Novelty Receipt (`watch-5`) — `targets/haugland-2411.00721-ques2/`

- **Checked UTC:** `2026-11-27T08:48Z` – `2026-11-27T08:52Z`
- **Verdict:** **PASS** (no `CONTESTED.md`)
- **Target Scope:** Jan Kristian Haugland and Tron Omland, `arXiv:2411.00721v2` (`2026-11-01`), Section 2 Question / Section 4 Open Problem (iii): existence of proper liftings $f \colon \mathbb{F}_2^k \to \mathbb{F}_2$ of algebraic degree $2$.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, rebuilt 2026-11-27T08:41Z–08:47Z):**
   - `.venv/bin/python tools/novelty_grep.py 2411.00721 Haugland Omland 'proper lifting' --max-per-file 3 --max-total 15`: `15` lines across `7/168` files (`atlas-lean` / `plasma-ai__erdos` / `BoltonBailey` hits are Haugland 1996 on Erdős #36 minimum overlap; `watch/snapshots/arxiv/` lists `2411.00721` citing papers).
2. **Live arXiv & OpenAlex citing sweep (`watch/snapshots/arxiv/citing_papers.md`, `tools/arxiv_fetch.py`):**
   - `id_list=['2411.00721']`: confirms `2411.00721v2` (`2026-11-01T15:13:35Z`) remains latest version.
   - `abs:"2411.00721" OR ...`: `total: 0`.
   - OpenAlex (`cited_by=5`): inspected citing preprints `arXiv:2610.33131v2` (*"Locally eventually onto cellular automata"*, Haugland–Larsen–Omland–Rustad, updated `2026-11-19`) and `arXiv:2609.35921v1` (*"Finite-ring obstructions for quadratic binary radius-two cellular automata"*, Houqiao Fu, `2026-09-28`):
     - **Near-miss `2609.35921v1`:** Proves non-injectivity on periodic rings $4 \mid n, n \ge 8$ for 5-slot radius-two (diameter $\le 5$) quadratic binary rules; does **not** settle general diameter $k$ (Haugland–Omland `2411.00721v2` already checked $k \le 7$).
     - **Near-miss `2610.33131v2`:** Gives criteria for open and locally eventually onto cellular automata; does not resolve existence of degree-2 proper liftings.
3. **Web search (`search_web`):**
   - `"2411.00721" "Haugland" "proper lifting"`: returns only `arXiv:2411.00721` itself.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by arXiv, OpenAlex, web search, or `watch/snapshots/**`.
