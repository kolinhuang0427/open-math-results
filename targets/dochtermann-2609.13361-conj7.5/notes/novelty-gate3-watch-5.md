# Gate 3 Novelty Receipt (`watch-5`) — `targets/dochtermann-2609.13361-conj7.5/`

- **Checked at (UTC):** `2026-11-27T12:08:59Z`–`2026-11-27T12:09:14Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED — `<1h` before reporting)**
- **Target:** Dochtermann, Huang, Mawhinney, Oh, Xu (`arXiv:2609.13361v1`, 2026-09-11), *Matroids with cycle systems are regular*, Section 7 Conjecture 7.5 (`\label{conj:C>=3 ind}`), plus implied Conjecture 7.4 (`conj:unique`) and cographic vertex-star characterization.
- **Checker Verification:** `.venv/bin/python -u targets/dochtermann-2609.13361-conj7.5/notes/check-check-1.py` exited `0` (`PASS`; `test_necklace_stress` & `test_cographic_and_graphic_families`: 39 circuit-system proofs, $K_5$ cone Cor 1, disconnected+coloops, Ex 6.8 verified). Paths verified: `targets/dochtermann-2609.13361-conj7.5/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.

## Exact Live Queries & Results
1. **Local snapshot grep (`tools/novelty_grep.py`, 709 files — post-Sweep-7):**
   - Query: `.venv/bin/python tools/novelty_grep.py 2609.13361 2609.17446 2509.11460 "circuit system" Dochtermann "conj:C>=3"`
   - Output: `7` lines across `3/709` files:
     - `watch/snapshots/1337-solved-conjectures/open_issues_claims.md:606` (`#336 [open]` Stanley's pure O-sequence conjecture — cites `2509.11460` & `2609.17446` only).
     - `watch/snapshots/discovered/tamnd__arxiv.json` (metadata/census index only).
     - `watch/snapshots/discovered/cmu-l3__reuF2F.json:150` (`lean/reuF2F/dochtermann2026matroids.lean`): **inspected verbatim via `gh api`** (`38` lines total) — defines `uniqueUnion` & `IsCircuitSystem` and states `theorem conjecture_7_5 ... := by sorry` (open-conjecture Lean 4 stub only, no proof).
   - `grep -iE "2609\.13361|dochtermann" watch/snapshots/insorrowmeow-oeis-ids.md`: `0` hits.
2. **arXiv API (`tools/arxiv_fetch.py query 'id:2609.13361 OR id:2609.17446 OR id:2509.11460'`):**
   - `2609.13361v1` (`2026-09-11T17:52:05Z`, no journal_ref/DOI) and `2509.11460v1` (`2025-09-14`) remain sole versions; `2609.17446v2` (`2026-09-19`) unchanged (already verified `0` mentions of `circuit system` or `conj:C>=3 ind`).
3. **GitHub live checks:**
   - `gh api 'repos/cmu-l3/reuF2F/contents/lean/reuF2F/dochtermann2026matroids.lean'`: confirmed `by sorry` stub only.
   - `gh api 'repos/the-omega-institute/trureturing/git/trees/dev?recursive=1' | grep -iE "2609|dochtermann|circuit.?sys|cycle.?sys"`: `0` hits.
   - `gh search issues "2609.13361"`: `0` hits.
4. **Zenodo / Parslow Ledger / Web search:**
   - `https://zenodo.org/api/records?q=2609.13361&size=5`: `total: 0`.
   - `https://mylesparslow-collab.github.io/demos/conjecture-ledger/index.html`: `0` hits for `2609.13361|dochtermann|circuit.system`.
   - Web search (`"2609.13361" OR ("Dochtermann" "circuit system" "conj:C>=3")`): returns only primary preprint `arXiv:2609.13361`.

## Coverage Limits
- OpenAlex & Semantic Scholar were not re-queried in this `12:09Z` pass (prior Gate 2 check at `12:01Z` returned OpenAlex `[]` and S2 HTTP `429`).
- `gh search code` skipped to preserve 10 req/min rate limit (covered by `709` local snapshots including Sweep 7 `529` repo snapshots + live `cmu-l3/reuF2F` file read + `trureturing` `dev` tree + `gh search issues`).
