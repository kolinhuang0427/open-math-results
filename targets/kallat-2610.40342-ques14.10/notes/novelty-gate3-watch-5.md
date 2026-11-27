# Gate 3 Novelty Receipt (`watch-5`) — `targets/kallat-2610.40342-ques14.10/`

- **Checked at (UTC):** `2026-11-27T14:53:48Z`–`2026-11-27T14:54:59Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED — `<1h` before reporting)**
- **Target:** Ahaan Kallat (`arXiv:2610.40342v1`, 2026-10-29), *A $p$-adic Valuation Calculus for Permutations with Restricted Cycle Lengths*, Section 14 **Question 14.10 (`\label{prob:gcdr}`)** — Q1 YES ($n \ge 111, n \equiv 30 \pmod{81}$), Q2 NO (disproved at $64 \le r \le 79, n = 1248$), Q3 & Q4 completely solved for $r = 3$ (general $r \ge 4$ for Q3/Q4 explicitly left open).
- **Checker Verification:** `.venv/bin/python -u targets/kallat-2610.40342-ques14.10/notes/check-check-1.py` exited `0` (`PASS`; Theorem 2 & Lemmas 2.1–2.2 for all $r \in [64, 79]$ at $n=1248$, Lemmas 4.1–4.3, and Theorems 1, 3, 4 verified). Paths verified: `targets/kallat-2610.40342-ques14.10/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.

## Exact Live Queries & Results
1. **Local snapshot grep (`tools/novelty_grep.py`, 725 files):**
   - Query: `.venv/bin/python tools/novelty_grep.py 2610.40342 "Kallat" "prob:gcdr"`
   - Output: `9` lines across `6/725` files (`trureturing` `kallat2026weightedpermutations.md` = `2610.15849v1`, `formal-conjectures-prs` = unrelated Peter Bala PR, `watch/snapshots/arxiv/*` = metadata).
   - `grep -iE "2610\.40342|kallat|gcdr" watch/snapshots/insorrowmeow-oeis-ids.md watch/snapshots/hwzw-algebra-number-theory-drafts.md`: `0` hits.
2. **arXiv / OpenAlex / Zenodo / GitHub / Parslow / Web:**
   - `tools/arxiv_fetch.py query 'id:2610.40342'`: `2610.40342v1` (`2026-10-29T16:04:37Z`, no journal_ref/DOI) remains sole version.
   - `https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2610.40342`: `W7224916767`, `cited_by_count: 0`.
   - `gh api 'repos/the-omega-institute/trureturing/git/trees/dev?recursive=1'`: `0` hits for `2610.40342` or Kallat Q14.10.
   - `gh search issues "2610.40342"` (`ArXiv_Mail` digest only), `gh search prs "2610.40342"` (`0`), `gh search repos "2610.40342"` (`0`).
   - `https://zenodo.org/api/records?q=2610.40342&size=5`: `total: 0`.
   - `https://mylesparslow-collab.github.io/demos/conjecture-ledger/index.html`: `0` hits.
   - Web search (`"2610.40342" "Question 14.10" OR "prob:gcdr" OR ("Kallat" "global gcd" "permutations")`): returns only primary preprint `2610.40342v1`.

## Coverage Limits
- **Semantic Scholar API:** returned HTTP `429` (`Too Many Requests`) during `14:53Z` query (`14:41Z` Gate 2 query returned `HTTP 200`, `citationCount: 0`).
- `gh search code` skipped to preserve 10 req/min rate limit (covered by `725` snapshots + Gate 2 `rainwangphy/aftd-platform` inspection + `trureturing` `dev` tree + `gh search issues/prs/repos`).
