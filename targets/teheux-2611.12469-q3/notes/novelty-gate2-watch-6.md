# Gate 2 Novelty Receipt (`watch-6`) — `targets/teheux-2611.12469-q3/`

- **Checked UTC:** `2026-11-27T14:12:24Z`–`2026-11-27T14:12:49Z`
- **Target:** Bruno Teheux, *Dualities and completions of median algebras and semilattices: a universal-algebraic approach*, `arXiv:2611.12469v1` (2026-11-09), Section 8, **Question 8.4** (`\label{q:correspondence}`) **item (3)**.
- **Verdict:** **OPEN / PASS**

## Exact Queries & Results

1. **Local Snapshot Grep (`.venv/bin/python tools/novelty_grep.py` across `721` snapshots):**
   - `2611.12469`, `Teheux`, `median algebra` -> `watch/snapshots/arxiv/` indices (`OpenAlex cited_by=0; S2=0`) only.
   - `q:correspondence` -> **`0` hits** (`0/721`).
2. **Live GitHub (`gh` CLI) & `trureturing` `dev`:**
   - `gh search repos "2611.12469"`, `gh search prs "2611.12469"` -> `[]`.
   - `gh search issues "2611.12469"` -> solely `the-omega-institute/trureturing#29092` (`state: open`, `comments: 0`, explicitly scoped to Question 8.4(2) `ST(\sigma)` and explicitly stating *"does not solve the other parts of Question 8.4"*).
   - `gh search code 2611.12469` -> `ehijano/rss_fetch`, `koutya0akari/arxiv-plug-in-for-mixi2` (arXiv RSS/bot logs) plus numeric CSV noise.
   - `gh api repos/the-omega-institute/trureturing/git/trees/dev?recursive=1` -> `HereditaryFlip/Median.{md,scribe.cs,lean}` only (`0` hits for `2611.12469` or `Teheux`).
3. **Live arXiv, Zenodo & Web Search:**
   - `export.arxiv.org/api/query?id_list=2611.12469` -> sole latest version `2611.12469v1` (`2026-11-09T14:19:48Z`); `au:Teheux` shows no newer papers.
   - `zenodo.org/api/records?q=2611.12469` -> `0` hits; `q="median algebras"+profinite` -> `5` unrelated results.
   - `search_web` (`"2611.12469" OR ("Teheux" "profinite completion" "median algebra")`) -> returns only `arXiv:2611.12469v1`.

## Coverage Limits

- Unindexed private repositories, closed-access journals, or unscraped author webpages remain out of live query scope; all checked public sources confirm Question 8.4 item (3) remains open.
