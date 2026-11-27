# Gate 3 Novelty Receipt (`watch-5`) — `targets/alexandersson-2609.05131-prob10.1/`

- **Checked at (UTC):** `2026-11-27T12:06:23Z`–`2026-11-27T12:07:28Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED — `<1h` before reporting)**
- **Target:** Per Alexandersson (`arXiv:2609.05131v2`, 2026-09-23), Section 10 Problem 10.1 (`\label{prob:consecutiveChowInterlacing}`: consecutive Chow polynomials of noncrossing partition lattices $\mathrm{NC}_{n+1}$ interlace).
- **Checker Verification:** `.venv/bin/python -u targets/alexandersson-2609.05131-prob10.1/notes/check-check-3.py` exited `0` (`PASS`; `[1/4]`–`[4/4]` exact integer Sturm–Cauchy `n=1..80`, 40-digit `iv` bounds `B5 <= 0.0907922`, `A(3..25) <= 0.40099`, `A(>=26) <= 0.350014`). Paths verified: `targets/alexandersson-2609.05131-prob10.1/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`.

## Exact Live Queries & Results
1. **Local snapshot grep (`tools/novelty_grep.py`, 709 files — post-Sweep-7):**
   - Query: `.venv/bin/python tools/novelty_grep.py 2609.05131 "consecutiveChowInterlacing" "Alexandersson" "Chow polynomial"`
   - Output: `72` lines across `23/709` files — all hits are distinct conjectures or background:
     - `1337-solved-conjectures`: parking-function excedance, graphical `dist`, transportation polytopes, Fuss–Catalan, long-cycle (`#55`/`#81`), Catalan-word peaks (`#59`), ordered-set-partition (`#108`), and CFH Conjecture 7.3 dual Chow (`PR #360`/rank-5 non-real-rootedness). **0 hits** for `2609.05131`, `consecutiveChowInterlacing`, or consecutive Chow polynomial interlacing for $\mathrm{NC}_{n+1}$.
     - `the-omega-institute__trureturing` (`files.txt`): `AlexanderssonLeiteFundamentalLengthRefutation` (sink polynomials, unrelated).
     - `1khvled__ordered-set-partition-conjecture`: ordered big-block conjecture (unrelated).
     - `insorrowmeow-oeis-ids.md` (`proofs/research-batch-06/geometry/AlexanderssonRows.lean`, `alexandersson-row-recurrence.md`): OEIS `A395454`/`A201637` row polynomials (unrelated).
     - `watch/snapshots/arxiv/citing_papers.md`: lists only `arXiv:2611.07267` (Ferreri–Martinez, *Pattern avoidance classes of parking permutations with fixed lucky sets*, 2026-11-05; already inspected in Gate 2 `#1300` — background citation only, does not study Chow polynomials).
2. **arXiv API (`tools/arxiv_fetch.py query 'id:2609.05131 OR id:2611.07267'`):**
   - `2609.05131v2` (`2026-09-23T12:23:46Z`, no journal_ref/DOI) remains latest version; `2611.07267v1` (`2026-11-05`) unchanged.
3. **GitHub live checks (`trureturing` `dev` & `PerAlexandersson/RealRooted`):**
   - `gh api 'repos/the-omega-institute/trureturing/git/trees/dev?recursive=1' | grep -iE "2609|05131|alexandersson|chow|interlac"`: inspected `Blueprint/D5/S3/Zeros/SimplicialPosetChowRefutation.md` -> concerns Hoster–Stump (`2508.15538v1`, simplicial poset Chow counterexample), **0 hits** for `2609.05131`, `05131`, or `NC_{n+1}` consecutive Chow interlacing.
   - `gh search issues "2609.05131"`: returns only `PerAlexandersson/RealRooted#665` (`[Parking functions] Tieless descent transfer to finite Smirnov words`, `CLOSED`, updated `2026-09-14T10:12:08Z`, covering Theorem 3.3, NOT Problem 10.1).
   - `gh search issues --repo PerAlexandersson/RealRooted "consecutiveChowInterlacing"`: `0` hits.
4. **Zenodo / Parslow Ledger / OpenAlex / Web search:**
   - `https://zenodo.org/api/records?q=2609.05131&size=5`: `total: 0`.
   - `https://mylesparslow-collab.github.io/demos/conjecture-ledger/index.html`: `0` hits for `2609.05131|alexandersson|chow`.
   - `https://api.openalex.org/works?search=2609.05131+OR+Alexandersson+Chow+polynomials`: `0` hits (`watch/snapshots/arxiv/citing_papers.json` already recorded `cited_by=1` -> `2611.07267v1` only).
   - Web search (`"2609.05131" "consecutiveChowInterlacing" OR "real-rootedness" "Alexandersson" 2026`): returns only primary preprint `arXiv:2609.05131`.

## Coverage Limits
- **Semantic Scholar API:** returned HTTP `429` (`Too Many Requests`) on live query (`12:06Z`); prior snapshot cached `S2=1` (`2611.07267v1`).
- `gh search code` skipped to preserve 10 req/min rate limit (covered by `709` local snapshots including Sweep 7 `529` repo snapshots + live `trureturing` `dev` tree + `gh search issues`).
