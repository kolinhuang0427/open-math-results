# Gate 3 Novelty Receipt — `wei-2310.17337-conj1.5`

- **UTC Time:** 2026-11-26T20:24:00Z
- **Reviewer:** `watch-5` (arXiv & citing-papers slice)
- **Verdict:** **PASS** (fresh live pre-report check confirms no new arXiv preprint, version update, OpenAlex/Crossref citation, or web publication settles Wei–Zhang–Zhao Conjecture 1.5)

## Fresh Live Sources & Exact Queries Checked

1. **Snapshot grep (`tools/novelty_grep.py 2310.17337 1793830926500679 "C4-isolation" "C_4-isolation" "C_k-isolation" "truncated tetrahedron"`):**
   - Checked all 208 files under `watch/snapshots/**` (0.46s) -> only our own `watch/snapshots/arxiv/` cache entries; 0 competing matches.
2. **Live arXiv API via `tools/arxiv_fetch.py` (`use_cache=False`):**
   - `id_list=["2310.17337"]` -> remains `2310.17337v1` (`2023-10-26T12:05:14Z`), no `v2` or comment update.
   - `cat:math.CO` (`max_results=15`, `sort_by="submittedDate"`) -> top ID `2611.34855v1`; 0 cycle-isolation matches.
   - `cat:math.CO AND all:isolation AND all:cycle` (`max_results=10`, `sort_by="submittedDate"`) -> newest remain `2611.29409v1`, `2611.24477v2`, `2611.19361v1`, etc.; none settle $C_k$-isolation for $k \ge 5$.
3. **Live OpenAlex API (`https://api.openalex.org/works/W7163506673`):**
   - `W7163506673` (`10.1142/s1793830926500679`) still has `cited_by_count: 3` (updated `2026-11-25T09:40:18`):
     - `10.1016/j.dam.2026.08.006` (Borg & Scicluna, `2026-08-21`, *"Isolation of non-triangle cycles in graphs"*)
     - `10.1016/j.dam.2025.06.058` (Liang & Wu, `2025-07-15`, *"Cycle isolation in graphs"*)
     - `10.12677/aam.2025.149398` (`2025-01-01`, *"Total Isolation Number of the Cartesian Product of Paths and Cycles"*)
4. **Live Crossref API (`https://api.crossref.org/works/10.1142/s1793830926500679`):**
   - `is-referenced-by-count: 1`, `update-to: None` (no erratum or retraction).
5. **Live Web Search (`search_web`):**
   - `("10.1142/s1793830926500679" OR "2310.17337") ("counterexample" OR "disprove" OR "refute" OR "erratum" OR "retract")` -> 0 refutations, errata, or retractions.

## Near Misses

- Borg & Scicluna (`10.1016/j.dam.2026.08.006` / `arXiv:2510.08361`), Liang & Wu (`10.1016/j.dam.2025.06.058`), and `10.12677/aam.2025.149398` (all previously inspected; none prove or refute $\iota(G, C_k) \le (m+1)/(k+2)$ for $k \ge 5$).

## What Was Not Covered

- Paywalled full text of DMAA 2026 (`10.1142/s1793830926500679`) and closed-access DAM articles.
- Semantic Scholar live API (rate-limited HTTP 429).
- GitHub repositories (checked separately by `watch-1` and `watch-6`).
