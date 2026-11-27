# Gate 3 Novelty Receipt (`watch-5`) — `targets/vasilyev-2611.20344-q7.3/`

- **Checked at (UTC):** `2026-11-27T14:02:02Z`–`2026-11-27T14:02:14Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED — `<1h` before reporting)**
- **Target:** Oleg Vasilyev (`arXiv:2611.20344v2`, 2026-11-18), *Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph*, Section 7 **Question 7.3 (`q:types`)** / Remark 4.4 (`rem:types`).
- **Checker Verification:** `.venv/bin/python -u targets/vasilyev-2611.20344-q7.3/notes/check-check-2.py` exited `0` (`PASS`; verified primary source, trap inequalities $B \le 600$, Lemma 3 across $H \in [5, 10000]$, 15-stage construction, 4 disjoint cycles, and exhaustive orbit classification on $[1, 1182213]$). Paths verified: `targets/vasilyev-2611.20344-q7.3/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`.

## Exact Live Queries & Results
1. **Local snapshot grep (`tools/novelty_grep.py`, 721 files):**
   - Query: `.venv/bin/python tools/novelty_grep.py 2611.20344 "Vasilyev" "q:types" "rem:types" "orbit type"`
   - Output: `28` lines across `9/721` files (`trureturing` `VasilyevForceDivergenceRefutation` / `#32194` = Q7.7 only; `s66lem`, `OjasMor`, `andrheabacor`, Zenodo `24567319` = Q7.1/Q7.7 only; `watch/snapshots/arxiv/*` metadata).
   - `grep -iE "2611\.20344|vasilyev" watch/snapshots/insorrowmeow-oeis-ids.md watch/snapshots/hwzw-algebra-number-theory-drafts.md`: `0` hits.
2. **arXiv / OpenAlex / Zenodo / GitHub / Parslow / Web:**
   - `tools/arxiv_fetch.py query 'id:2611.20344'`: `2611.20344v2` (`2026-11-18T03:50:40Z`, no journal_ref/DOI) remains latest version.
   - `https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2611.20344`: `W7234897498`, `cited_by_count: 1` (verified `filter=cites:W7234897498` returned `[]` at `13:56Z`).
   - `gh api 'repos/the-omega-institute/trureturing/git/trees/dev?recursive=1'`: only `VasilyevForceDivergenceRefutation` (Q7.7).
   - `gh search issues "2611.20344"` (`trureturing#32194` Q7.7 only), `gh search prs "2611.20344"` (`0`), `gh search repos "2611.20344"` (`0`).
   - `https://zenodo.org/api/records?q=2611.20344&size=5`: `total: 0`.
   - `https://mylesparslow-collab.github.io/demos/conjecture-ledger/index.html`: `0` hits.
   - Web search (`"2611.20344" "q:types" OR "infinitely many cycles and a divergent orbit" "Vasilyev"`): returns only primary preprint `2611.20344v2`.

## Coverage Limits
- Semantic Scholar API not re-queried after `13:56Z` HTTP `429`.
- `gh search code` skipped to preserve 10 req/min rate limit (covered by `721` snapshots + live `trureturing` `dev` tree + `gh search issues/prs/repos`).
