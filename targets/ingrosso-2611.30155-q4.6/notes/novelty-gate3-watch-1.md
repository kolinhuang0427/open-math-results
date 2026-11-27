# Gate 3 Novelty Check — `ingrosso-2611.30155-q4.6` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T16:37:30Z`–`2026-11-27T16:37:49Z`
- **Target:** `targets/ingrosso-2611.30155-q4.6/` — E. Ingrosso, M. Trombetti, A. Zitouni, *"Groups with dual classes of subgroups"* (`arXiv:2611.30155v1`, `2026-11-23`), §4 Question 4.6 (`pronormali_arxiv.tex` L784–786, referring to Theorem 4.5 `\label{sip}`, smallest possible subnormal defect = `2`)
- **Claimed label (`AUDIT.md`):** `written proof, internally audited`
- **Check cmd:** `.venv/bin/python -u targets/ingrosso-2611.30155-q4.6/notes/check-check-1.py`
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2611.30155" "Ingrosso" "Groups with dual classes of subgroups"`):**
   - `7` lines across `3/742` files, all solely from `watch/snapshots/arxiv/{arxiv_submissions.*,state.json}` indexing `2611.30155v1` itself; `0` settlement hits in `1337isnot1337/solved-conjectures` or other snapshots.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T16:37:49Z`):**
   - `main` = `f5f094d3fddd49f00f568832844d87d1edab93a6` (`2026-11-27T16:35:40Z`, `#1057` `docs/research-results/stanley-tree-subdivisions/`) — unrelated.
   - `research` = `fd7decb3a72fa2c2b43f31be20a840aa7eae5c4a` (`2026-11-27T16:35:02Z`, `lean/Conjectures/CircularInsertionDegree54.lean`) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2611.30155"` -> `0` hits.
   - `gh search issues "2611.30155"` -> `0` hits.
   - `gh search code "2611.30155"` -> `6` hits (`ehijano/rss_fetch` RSS XML + `5` unrelated CSV/pickle numeric collisions).
   - `gh search code '"Groups with dual classes of subgroups"'` -> `0` hits.
4. **Zenodo / Crossref / arXiv / Web:**
   - Zenodo API (`q=2611.30155`) -> `0` hits.
   - Crossref (`10.1017/s1446788726101682`) -> `is-referenced-by-count: 0`, `published: 2026-09-23`.
   - arXiv API (`id_list=2611.30155`) -> sole version `2611.30155v1` (`2026-11-23T07:03:10Z`).
   - Web search -> no settlement of Question 4.6 found.

## Coverage Limits
- Covers `watch/snapshots` (`742` files), live `1337isnot1337/solved-conjectures` (`main`/`research` HEAD), public GitHub PR/issue/code search, Zenodo, Crossref, arXiv API, and public web search as of `2026-11-27T16:37:49Z`; private repositories and non-indexed preprints remain unobservable.
