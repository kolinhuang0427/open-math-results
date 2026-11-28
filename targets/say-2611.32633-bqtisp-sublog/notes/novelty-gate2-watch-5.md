# Gate 2 Novelty Check — `say-2611.32633-bqtisp-sublog` (`watch-5`)

- **Timestamp:** `2026-11-27T21:33:33Z`
- **Verdict:** **PASS — `OPEN / UNCONTESTED`**
- **Target:** A. C. Cem Say, *"Lower space bounds for polynomial-time quantum computation"*, `arXiv:2611.32633v1` (`2026-11-24T13:54:27Z`), Section 6 (`main.tex` L1924–1928) — extending Theorem `thm:hier` (`BQTISP(n^{O(1)}, o(s(n))) \subsetneq BQTISP(n^{O(1)}, O(s(n)))`) beyond $\Theta(\log n / (\log\log n)^i)$ to general space functions $s(n) \in \omega(\log\log n) \cap o(\log n)$.

## Verification Receipts

1. **`watch/snapshots/` (`novelty_grep.py "2611.32633" "BQTISP" "Cem Say" "sublogarithmic" "quantum space"` across `855` files):**
   - `19` lines across `7/855` files: `2611.32633v1` in `arxiv_submissions.{json,md}` and `state.json`, plus unrelated `trureturing` zeta-count PRs, hash-based vector commitments, `2611.14827v1`, and Kahane's conjecture. `0` settlements.
2. **Live GitHub (`gh search` & `trureturing`):**
   - `gh search issues/prs/repos "2611.32633"`: `0` hits each.
   - `gh search code "2611.32633"`: `7` hits (`qiao-925/news-digest`, `ehijano/rss_fetch`, `nsaririan3` arXiv mirrors + unrelated floats).
   - `gh search code "BQTISP"`: `2601.16695` (`2026-01`), `2611.32633v1` digests, and unrelated base64/CSV substrings.
   - `the-omega-institute/trureturing` PRs up to `#34994`: `0` hits.
3. **arXiv API (`export.arxiv.org`):**
   - `2611.32633v1` (`2026-11-24T13:54:27Z`) sole version.
   - `all:"BQTISP" OR (all:"quantum" AND all:"sublogarithmic" AND all:"space" AND all:"hierarchy")`: returns only `2611.32633v1` and earlier preprints (`2601.16695v2`, `2503.21582v2`).
4. **Citations & Preprints (OpenAlex / OpenCitations / Zenodo / Crossref):**
   - OpenAlex `W7239717187` (`10.48550/arXiv.2611.32633`): `cited_by_count: 0`.
   - OpenCitations (`10.48550/arXiv.2611.32633`): `200 []`.
   - Zenodo (`2611.32633`): `0` hits. (Crossref `404`.)
5. **ECCC & Conference Web Search (`search_web`):**
   - Queries for `"2611.32633"`, `"Lower space bounds for polynomial-time quantum computation"`, `"BQTISP"`, and ECCC/QIP/STOC/FOCS/CCC follow-ups returned only `arXiv:2611.32633` and earlier `2503.21582` (`0` follow-up settlements).
