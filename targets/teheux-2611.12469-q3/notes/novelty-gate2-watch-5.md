# Gate 2 Novelty Receipt (`watch-5`) — `targets/teheux-2611.12469-q3/`

- **Checked at (UTC):** `2026-11-27T14:12:26Z`–`2026-11-27T14:12:36Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)**
- **Target:** Bruno Teheux (`arXiv:2611.12469v1`, 2026-11-09), *Dualities and completions of median algebras and semilattices: a universal-algebraic approach*, Section 8 **Question 8.4 (`\label{q:correspondence}`) item (3)** — whether every universal sentence holding in a median algebra $\mathbf{A}$ holds in $\hat{\mathbf{A}}$ (equivalently, whether every finite subalgebra of $\hat{\mathbf{A}}$ embeds into $\mathbf{A}$).

## Exact Queries & Results
1. **Local snapshot grep (`tools/novelty_grep.py`, 721 files):**
   - Query: `.venv/bin/python tools/novelty_grep.py 2611.12469 "Teheux" "q:correspondence" "median algebra" "poc-set"`
   - Output: `16` lines across `6/721` files — strictly `watch/snapshots/arxiv/*` metadata (`OpenAlex cited_by=0`, `S2=0`).
   - `grep -iE "2611\.12469|teheux|median" watch/snapshots/insorrowmeow-oeis-ids.md watch/snapshots/hwzw-algebra-number-theory-drafts.md`: `0` hits.
2. **arXiv / OpenAlex / Zenodo / Parslow / Web:**
   - `tools/arxiv_fetch.py query 'id:2611.12469'`: `2611.12469v1` (`2026-11-09T14:19:48Z`, no journal_ref/DOI) remains sole version.
   - `https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2611.12469`: `W7225720536`, `cited_by_count: 0`.
   - `https://zenodo.org/api/records?q=2611.12469&size=5`: `total: 0`.
   - `https://mylesparslow-collab.github.io/demos/conjecture-ledger/index.html`: `0` hits.
   - Web search (`"2611.12469" OR ("Teheux" "Dualities and completions of median algebras")`): returns only primary preprint `2611.12469v1`.
3. **GitHub live checks:**
   - `gh search issues "2611.12469"`: returns only `the-omega-institute/trureturing#29092` (`OPEN`, 0 comments) — inspected verbatim via `gh issue view`: preregistration for Question 8.4**(2)** second sentence (`ST(\sigma)`), explicitly stating *"does not solve the other parts of Question 8.4"*.
   - `gh api 'repos/the-omega-institute/trureturing/git/trees/dev?recursive=1'`: only unrelated `HereditaryFlip/Median.{md,scribe.cs,lean}` (`0` hits for `2611.12469` or Teheux).
   - `gh search prs "2611.12469"` & `gh search repos "2611.12469"`: `0` hits.

## Coverage Limits
- **Semantic Scholar API:** returned HTTP `429` (`Too Many Requests`) during `14:12Z` live check (prior snapshot cached `S2=0`).
- `gh search code` skipped to preserve 10 req/min rate limit (covered by `721` snapshots + live `trureturing#29092` / `dev` tree inspection + `gh search issues/prs/repos`).
