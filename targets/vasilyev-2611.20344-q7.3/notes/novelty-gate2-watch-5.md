# Gate 2 Novelty Receipt (`watch-5`) — `targets/vasilyev-2611.20344-q7.3/`

- **Checked at (UTC):** `2026-11-27T13:56:28Z`–`2026-11-27T13:57:03Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)**
- **Target:** Oleg Vasilyev (`arXiv:2611.20344v2`, 2026-11-18), *Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph*, Section 7 **Question 7.3 (`\label{q:types}`)** — existence of a Collatz-type map $T_S$ with infinitely many cycles and a divergent orbit (`Remark 4.4`, `rem:types`).

## Exact Queries & Results
1. **Local snapshot grep (`tools/novelty_grep.py`, 720 files):**
   - Query: `.venv/bin/python tools/novelty_grep.py 2611.20344 "Vasilyev" "q:types" "rem:types" "orbit type"`
   - Output: `28` lines across `9/720` files — **all** non-target hits address distinct questions:
     - `the-omega-institute/trureturing`: `VasilyevForceDivergenceRefutation.{md,lean}` & issue `#32194` — inspected verbatim via `gh api`: explicitly refutes **Question 7.7** (`#S7.Thmtheorem7`, force-divergent set without an all-up tail), NOT Question 7.3.
     - `OjasMor/arxiv-conjectures`: README explicitly lists Question 7.1 (`updown-cycle-ratio/`) and Question 7.7 (`updown-forcing/`) only.
     - `s66lem/conjectures`: `results/vasilyev-up-down-cycles/README.md` inspected verbatim via `gh api`: disproves **Question 7.1** ($2^\ell < 3^{a+1}$ via cycle $\ell=382$) only (`Zenodo 24567319`).
     - `andrheabacor/open-conjecture-results`: `docs/VasilyevCycle.md` inspected verbatim via `gh api`: disproves **Question 7.1** ($\ell=233$) only.
     - `watch/snapshots/arxiv/*`: metadata for `2611.20344v2` (`2026-11-18`) and separate `2611.10311v1`.
   - `Hwzw/algebra-number-theory-drafts` & `insorrowmeow-oeis-ids.md`: `0` hits.
2. **arXiv API (`tools/arxiv_fetch.py query 'id:2611.20344'`):**
   - `2611.20344v2` (`2026-11-18T03:50:40Z`, no journal_ref/DOI) remains latest version.
3. **GitHub live checks:**
   - `gh api 'repos/Mira-Cult/math/git/trees/main?recursive=1' | grep -iE "vasilyev|2611|collatz|updown"`: only unrelated Collatz density/tilings notes (`0` hits for `2611.20344` or Question 7.3).
   - `gh search issues "2611.20344"`: `trureturing#32194` (Question 7.7) only.
   - `gh search prs "2611.20344"` & `gh search repos "2611.20344"`: `0` hits.
4. **Zenodo / OpenAlex / Parslow / Web:**
   - `https://zenodo.org/api/records?q=2611.20344&size=10`: `total: 0`.
   - `https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2611.20344`: `W7234897498`, `cited_by_count: 1` (`cites:W7234897498` returned `[]`).
   - `https://mylesparslow-collab.github.io/demos/conjecture-ledger/index.html`: `0` hits.
   - Web search (`"2611.20344" OR ("Vasilyev" "orbit type" "Question 7.3" OR "q:types")`): returns only primary preprint `2611.20344v2`.

## Coverage Limits
- **Semantic Scholar API:** returned HTTP `429` (`Too Many Requests`) during `13:56Z` query.
- **OpenAlex `W7234897498`:** shows `cited_by_count: 1` metadata counter while `filter=cites:W7234897498` returned `[]` (no citing arXiv/Zenodo/GitHub artifact resolved `q:types`).
- `gh search code` skipped to preserve 10 req/min rate limit (covered by `720` snapshots + live `gh api` inspections of `trureturing`, `s66lem`, `andrheabacor`, `Mira-Cult`, and `OjasMor` README).
