# Gate 2 Novelty Receipt (`watch-5`) — `targets/kallat-2610.40342-ques14.10/`

- **Checked at (UTC):** `2026-11-27T14:40:56Z`–`2026-11-27T14:41:17Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)**
- **Target:** Ahaan Kallat (`arXiv:2610.40342v1`, 2026-10-29), *A $p$-adic Valuation Calculus for Permutations with Restricted Cycle Lengths*, Section 14 **Question 14.10 (`\label{prob:gcdr}`)** (Q1 YES `n >= 111, n = 30 mod 81`; Q2 NO disproved at `64 <= r <= 79, n = 1248`; Q3–Q4 completely solved for `r = 3`, explicitly scoping general `r >= 4` for Q3/Q4 open).

## Exact Queries & Results
1. **Local snapshot grep (`tools/novelty_grep.py`, 721 files):**
   - Query: `.venv/bin/python tools/novelty_grep.py 2610.40342 "Kallat" "prob:gcdr" "OP-746"`
   - Output: `9` lines across `6/721` files:
     - `the-omega-institute/trureturing`: `Library/FiniteGroups/kallat2026weightedpermutations.md` — **inspected verbatim via `gh api`**: covers Kallat's earlier `arXiv:2610.15849v1` (`A378495`), NOT `2610.40342v1` Question 14.10.
     - `watch/snapshots/formal/formal-conjectures-prs.{json,tsv}`: cites Kallat's $p$-local method in an unrelated Peter Bala conjecture PR.
     - `watch/snapshots/arxiv/*`: metadata for `2610.40342v1` (`OpenAlex cited_by=0`, `S2=0`).
   - `grep -iE "2610\.40342|kallat|gcdr" watch/snapshots/insorrowmeow-oeis-ids.md watch/snapshots/hwzw-algebra-number-theory-drafts.md`: `0` hits.
2. **GitHub live inspection (`rainwangphy/aftd-platform` & global searches):**
   - `gh search code --repo rainwangphy/aftd-platform "2610.40342"` returned `RestrictedCycleGlobalGcd.lean` & `RestrictedCycleOneParamGcd.lean` (`Question 14.10`) — **inspected both verbatim via `gh api`**: pure `def` statements only (`15` lines each), no theorem or resolution of Question 14.10.
   - `gh api 'repos/the-omega-institute/trureturing/git/trees/dev?recursive=1' | grep -iE "2610\.40342|kallat|gcdr"`: `0` hits.
   - `gh search issues "2610.40342"`: only automated `bguanmath/ArXiv_Mail` digest (`#437`–`#439`).
   - `gh search prs "2610.40342"` & `gh search repos "2610.40342"`: `0` hits.
3. **arXiv / OpenAlex / Semantic Scholar / Zenodo / Parslow / Web:**
   - `tools/arxiv_fetch.py query 'id:2610.40342'`: `2610.40342v1` (`2026-10-29T16:04:37Z`, no journal_ref/DOI) remains sole version.
   - `https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2610.40342`: `W7224916767`, `cited_by_count: 0`.
   - `https://api.semanticscholar.org/graph/v1/paper/arXiv:2610.40342?fields=title,citationCount`: `HTTP 200`, `citationCount: 0`.
   - `https://zenodo.org/api/records?q=2610.40342&size=5`: `total: 0`.
   - `https://mylesparslow-collab.github.io/demos/conjecture-ledger/index.html`: `0` hits.
   - Web search (`"2610.40342" OR ("Ahaan Kallat" "Valuation Calculus" "Permutations")`): returns only primary preprint `2610.40342v1`.

## Coverage Limits
- Global `gh search code` skipped to preserve 10 req/min rate limit (covered by `721` snapshots + repo-scoped `gh search code` on `rainwangphy/aftd-platform` + live `trureturing` `dev` tree + global `gh search issues/prs/repos`).
