# Gate 2 Novelty Receipt (`watch-5`) — `targets/zhou-2609.23078-conj1/`

- **Checked at (UTC):** `2026-11-27T14:45:07Z`–`2026-11-27T14:45:34Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)**
- **Target:** You Zhou (`arXiv:2609.23078v1`, 2026-09-19), *Maximal proper extremal subset in the crystal basis of a finite-dimensional irreducible module*, Section 1 **Conjecture 1** / Section 3 **Conjecture 3.1 (`\label{conj:main1-all-types}`)** — proved across all finite-dimensional simple Lie types $A, B, C, D, E, F, G$ and all $\lambda \in P^+$.

## Exact Queries & Results
1. **Local snapshot grep (`tools/novelty_grep.py`, 721 files):**
   - Query: `.venv/bin/python tools/novelty_grep.py 2609.23078 "You Zhou" "conj:main1-all-types" "maximal proper extremal subset"`
   - Output: `0` lines across `0/721` files.
   - `grep -iE "2609\.23078|extremal" watch/snapshots/insorrowmeow-oeis-ids.md watch/snapshots/hwzw-algebra-number-theory-drafts.md`: `0` hits.
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - `query 'id:2609.23078'`: `2609.23078v1` (`2026-09-19T15:20:17Z`, no journal_ref/DOI) remains sole version.
   - `query 'all:"extremal subset" AND all:crystal'`: returns only `2609.23078v1` and prior Sam Armon `2310.14584v1` (2023).
3. **GitHub / OpenAlex / Zenodo / Parslow / Web:**
   - `gh api 'repos/the-omega-institute/trureturing/git/trees/dev?recursive=1' | grep -iE "2609\.23078|you.?zhou|extremal.?subset"`: `0` hits.
   - `gh search issues "2609.23078"`, `gh search prs "2609.23078"`, `gh search repos "2609.23078"`: `0` hits.
   - `https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2609.23078`: `W7214037538`, `cited_by_count: 0`.
   - `https://zenodo.org/api/records?q=2609.23078&size=5`: `total: 0`.
   - `https://mylesparslow-collab.github.io/demos/conjecture-ledger/index.html`: `0` hits.
   - Web search (`"2609.23078" OR ("You Zhou" "extremal subset" "crystal basis")`): returns only primary preprint `2609.23078v1`.

## Coverage Limits
- **Semantic Scholar API:** returned HTTP `429` (`Too Many Requests`) during `14:45Z` query.
- `gh search code` skipped to preserve 10 req/min rate limit (covered by `721` snapshots + `trureturing` `dev` tree + `gh search issues/prs/repos`, plus `zhou-lit` live `gh search code` check at `14:15Z`).
