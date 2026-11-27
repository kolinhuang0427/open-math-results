# Gate 3 Novelty Receipt (`watch-5`) — `targets/zhou-2609.23078-conj1/`

- **Checked at (UTC):** `2026-11-27T15:07:04Z`–`2026-11-27T15:07:16Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED — `<1h` before reporting)**
- **Target:** You Zhou (`arXiv:2609.23078v1`, 2026-09-19), *Maximal proper extremal subset in the crystal basis of a finite-dimensional irreducible module*, Section 1 **Conjecture 1** / Section 4 **Conjecture 4.1 (`\label{conj:main1-all-types}`)** — proved across all finite-dimensional simple Lie types $A, B, C, D, E, F, G$ and all $\lambda \in P^+$.
- **Checker Verification:** `.venv/bin/python -u targets/zhou-2609.23078-conj1/notes/check-check-2.py` exited `0` (`PASS`; primary source match, Step 2 Parts 1–3, Lemma 4(2) `Pitman = e_max` across 31 crystals, Theorem 1 tensor monotonicity 11,643 comparisons, Lemma 1 folding, Lemma 2(3) gauge identity in $\mathbb{Q}[t]/(t^{11})$). Paths verified: `targets/zhou-2609.23078-conj1/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`.

## Exact Live Queries & Results
1. **Local snapshot grep (`tools/novelty_grep.py`, 729 files):**
   - Query: `.venv/bin/python tools/novelty_grep.py 2609.23078 "You Zhou" "conj:main1-all-types" "maximal proper extremal subset"`
   - Output: `4` lines across `2/729` files — strictly `watch/snapshots/arxiv/citing_papers.{json,md}` (`OpenAlex cited_by=0`, `S2=0`).
   - `grep -iE "2609\.23078|extremal" watch/snapshots/insorrowmeow-oeis-ids.md watch/snapshots/hwzw-algebra-number-theory-drafts.md`: `0` hits.
2. **arXiv / OpenAlex / Zenodo / GitHub / Parslow / HexagonMath / Web:**
   - `tools/arxiv_fetch.py query 'id:2609.23078'`: `2609.23078v1` (`2026-09-19T15:20:17Z`, no journal_ref/DOI) remains sole version.
   - `https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2609.23078`: `W7214037538`, `cited_by_count: 0`.
   - `gh api 'repos/the-omega-institute/trureturing/git/trees/dev?recursive=1'`: `0` hits.
   - `gh search issues "2609.23078"`, `gh search prs "2609.23078"`, `gh search repos "2609.23078"`: `0` hits.
   - `https://zenodo.org/api/records?q=2609.23078&size=5`: `total: 0`.
   - `https://mylesparslow-collab.github.io/demos/conjecture-ledger/index.html`: `0` hits.
   - `https://hexagonmath.org/`: `0` hits for `2609.23078|you zhou|extremal subset`.
   - Web search (`"2609.23078" "conj:main1-all-types" OR ("You Zhou" "extremal subset" "crystal")`): returns only primary preprint `2609.23078v1`.

## Coverage Limits
- Semantic Scholar API not re-queried in this `15:07Z` pass (`watch/snapshots/arxiv/citing_papers.json` & `watch5_sweep.py` at `15:05Z` observed `S2 HTTP 200`, `0` citations).
- `gh search code` skipped to preserve 10 req/min rate limit (covered by `729` snapshots + `trureturing` `dev` tree + `gh search issues/prs/repos`).
