# Gate 2 Novelty Check — `kern-2611.32927-oolcs-11connected` (`watch-5`)

- **Timestamp:** `2026-11-27T21:07:40Z`
- **Verdict:** **PASS — `OPEN / UNCONTESTED`**
- **Target:** Christoph Kern, Alexander Firbas, and Manuel Sorge, *"Algorithms and Complexity of Connectivity Switching in Graphs"*, `arXiv:2611.32927v1` (`2026-11-24T16:37:07Z`, full version of LATIN 2026), Section 5/6 (`sections/conclusion.tex` L5) — whether `On-Off Local-Con Switching` (`OOLCS`) restricted to $\{1,1\}$-bounded connected switches is solvable in polynomial time (or FPT w.r.t. solution weight).

## Verification Receipts

1. **`watch/snapshots/` (`novelty_grep.py "2611.32927" "OOLCS" "One-or-Other" "1,1-bounded" "connected switches"` across `854` files):**
   - `6` lines across `3/854` files (`arxiv_submissions.{json,md}`, `state.json` entries for `2611.32927v1` only). `0` settlements.
2. **Live GitHub (`gh search` & `trureturing`):**
   - `gh search code "One-or-Other Local-Con"`: `0` hits; `gh search code "OOLCS"`: unrelated `boolcs`/`ThreadPoolCS` substrings; `gh search issues/prs/repos "2611.32927"`: `0` hits; `trureturing` PRs up to `#34981` clear.
3. **arXiv / OpenAlex / OpenCitations / Zenodo:**
   - `2611.32927v1` (`2026-11-24T16:37:07Z`) sole version; OpenAlex `W7239759747` `cited_by_count: 0`; OpenCitations `200 []`; Zenodo `0` hits.
4. **ECCC & Conference Web Search (`search_web`):**
   - Query for `"OOLCS" / "One-or-Other Local-Con" / "{1,1}-bounded connected switches"` with `"Kern" / "2611.32927" / "LATIN 2026" / "ECCC"` returned only LATIN 2026 / `arXiv:2611.32927` (`0` follow-up settlements).
