# Gate 2 Novelty Receipt (`watch-5`) — `targets/fioravanti-2602.04034-conj59/`

- **Checked at (UTC):** `2026-11-27T13:42:07Z`–`2026-11-27T13:42:30Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)**
- **Target:** Fioravanti, Kompatscher, Rossi (`arXiv:2602.04034v1`, 2026-02-03), *Clonoids over vector spaces* — Section 7 **Conjecture 59 (`conjecture:strong`)** for all finite abelian $p$-groups and implied Section 1 **Conjecture 1 (`conjecture:main`)** for all finite modules.

## Exact Queries & Results
1. **Local snapshot grep (`tools/novelty_grep.py`, 717 files):**
   - Query: `.venv/bin/python tools/novelty_grep.py 2602.04034 "Fioravanti" "Kompatscher" "clonoid" "conjecture:strong"`
   - Output: `18` lines across `8/717` files:
     - `watch/snapshots/arxiv/{arxiv_submissions.*,citing_papers.*,last_sweep_report.json}`: metadata only (`OpenAlex cited_by=0`, `S2=0`, plus unrelated Boolean clonoid paper).
     - `AlexenderSokolov__cross-theory-formal-database`: CC-BY-4.0 license mirror only.
     - `Hwzw/algebra-number-theory-drafts` (`papers/P32-mixed-exponent-clonoids/manuscript.md`): **inspected §6 verbatim via `gh api`**. `P32` settles only $\mathbb{Z}/p^2\mathbb{Z} \oplus (\mathbb{Z}/p\mathbb{Z})^s$ (`Question 60`) and explicitly states: *"For sources with more than one cyclic $p^2$ factor... Groups of higher exponent also require additional congruence layers. Neither case is settled here, and the general finite-module conjecture remains outside the scope of this paper."* Leaves Conjecture 59 and Conjecture 1 open.
   - `grep -iE "2602\.04034|fioravanti|clonoid" watch/snapshots/insorrowmeow-oeis-ids.md`: `0` hits.
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - `query 'id:2602.04034'`: `2602.04034v1` (`2026-02-03T21:55:59Z`, no journal_ref/DOI) remains sole version.
   - `query 'all:clonoid OR all:clonoids'` (`--max-results 10`): `2611.33066v1` (Boolean clones/clonoids), `2608.18917v1` (Patrick Wynne, *Structure and Complexity of 2-Nilpotent Mal'cev Algebras*, 2026-08-19 — squarefree order 2-step nilpotent algebras only), `2602.04034v1`, Lehtonen Boolean papers, Fioravanti `2009.08256v2`. **0** papers solving Conjecture 59 or Conjecture 1.
3. **GitHub / OpenAlex / Zenodo / Parslow / Web:**
   - `gh api 'repos/the-omega-institute/trureturing/git/trees/dev?recursive=1' | grep -iE "2602|04034|fioravanti|kompatscher|clonoid"`: `0` hits.
   - `gh search issues "2602.04034"` & `gh search prs "2602.04034"`: `0` hits.
   - `https://zenodo.org/api/records?q=2602.04034&size=5`: `total: 0`.
   - `https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2602.04034`: `W7128086082`, `cited_by_count: 0`.
   - `https://mylesparslow-collab.github.io/demos/conjecture-ledger/index.html`: `0` hits.
   - Web search (`"2602.04034" OR ("Fioravanti" "Kompatscher" "Rossi" "clonoids" "conjecture")`): returns only primary preprint `2602.04034v1`.

## Coverage Limits
- **Semantic Scholar API:** returned HTTP `429` (`Too Many Requests`) during `13:42Z` live query (`fiora-lit` at `13:14Z` & `citing_papers.json` both observed `citationCount=0`).
- `gh search code` skipped to preserve 10 req/min rate limit (covered by `717` snapshots + live `Hwzw/algebra-number-theory-drafts` `P32` §6 inspection + `trureturing` `dev` tree + `gh search issues/prs`).
