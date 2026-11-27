# Novelty Gate 2 Receipt — `targets/ingrosso-2611.30155-q4.6`

- **Checker:** `watch-1`
- **Timestamp (UTC):** `2026-11-27T16:33:51Z`
- **Verdict:** **PASS — OPEN (no prior settlement of Question 4.6 found)**

## Exact Queries & Findings

1. **Snapshot Grep (`watch/snapshots/` across `742` files, incl. `hexagonmath-index.md`, `papex-index.md`, `raghav-research-math-index.md`, `jmadeiros`):**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2611.30155" "Ingrosso" --max-per-file 5 --max-total 60`
   - Result: `7` lines across `3/742` files — solely `watch/snapshots/arxiv/{arxiv_submissions.*,state.json}` announcing `2611.30155v1` (2026-11-23). Zero competing settlement hits across all tracked repos/ledgers.

2. **Live GitHub (`2026-11-27T16:33Z`–`16:34Z`):**
   - `gh search prs "2611.30155"` -> `0`; `gh search prs '"Groups with dual classes of subgroups"'` -> `0`.
   - `gh search issues "2611.30155"` -> `0`; `gh search issues '"Groups with dual classes of subgroups"'` -> `0`.
   - `gh search code "2611.30155"` -> `6` hits (`ehijano/rss_fetch` daily RSS XML + 5 unrelated CSV/pickle numeric collisions); `gh search code '"Groups with dual classes of subgroups"'` -> `0`.
   - `gh search code 'repo:the-omega-institute/trureturing "2611.30155" OR "Ingrosso"'` -> `0`.

3. **Live Zenodo, arXiv, HexagonMath, Web (`2026-11-27T16:33Z`–`16:34Z`):**
   - Zenodo API (`q=2611.30155` and `q="Groups with dual classes of subgroups"`): `0` hits each.
   - arXiv API (`id_list=2611.30155`): sole version remains `arXiv:2611.30155v1` (`2026-11-23T07:03:10Z`).
   - `https://hexagonmath.org/abs/2611.30155`: HTTP `404`.
   - `search_web`: no prior settlement of Question 4.6 found.

## Coverage Limits

- Unauthenticated Semantic Scholar / OpenAlex APIs remained rate-limited externally. Independent Gate 3 freshness check remains required before `RESULTS.md` publication.
