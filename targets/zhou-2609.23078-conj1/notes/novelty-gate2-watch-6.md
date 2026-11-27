# Gate 2 Novelty Receipt (`watch-6`) — `targets/zhou-2609.23078-conj1/`

- **Checked UTC:** `2026-11-27T14:45:13Z`–`2026-11-27T14:45:26Z`
- **Target:** You Zhou, *Maximal proper extremal subset in the crystal basis of a finite-dimensional irreducible module*, `arXiv:2609.23078v1` (2026-09-19), Section 1 **Conjecture 1** / Section 3 **Conjecture 3.1** (`\label{conj:main1-all-types}`, all finite simple Lie types).
- **Verdict:** **OPEN / PASS**

## Exact Queries & Results

1. **Local Snapshot Grep (`.venv/bin/python tools/novelty_grep.py` across `721` snapshots):**
   - `2609.23078`, `You Zhou`, `conj:main1-all-types`, `maximal proper extremal subset` -> **`0` hits** (`0/721`).
2. **Live GitHub (`gh` CLI) & `trureturing` `dev`:**
   - `gh search repos "2609.23078"`, `gh search issues "2609.23078"`, `gh search prs "2609.23078"`, `gh search code '"conj:main1-all-types"'` -> `[]`.
   - `gh search code 2609.23078` & `"maximal proper extremal subset"` -> solely automated arXiv RSS/digest mirrors (`LeeMath-lzu/daily-arXiv-ai-enhanced-QA`, `ehijano/rss_fetch`, `koutya0akari/arxiv-plug-in-for-mixi2`), `0` proofs.
   - `gh api repos/the-omega-institute/trureturing/git/trees/dev?recursive=1` -> `0_HITS` for `2609|23078|zhou|crystal.*extremal`.
3. **Live arXiv, Zenodo & Web Search:**
   - `export.arxiv.org/api/query?id_list=2609.23078` -> sole version `2609.23078v1` (`2026-09-19T15:20:17Z`).
   - `all:"extremal subset"+AND+all:crystal` -> solely `2609.23078v1` and older `2310.14584v1` (Armon).
   - `zenodo.org/api/records?q=2609.23078` -> `0`; `q="maximal proper extremal subset"` -> `0`.
   - `search_web` -> returns only `arXiv:2609.23078`.

## Coverage Limits

- Unindexed private repositories, closed-access journals, or unscraped author webpages remain out of live query scope; all checked public sources confirm Conjecture 1 / Conjecture 3.1 (`conj:main1-all-types`) remains open outside type $A$.
