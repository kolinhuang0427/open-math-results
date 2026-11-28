# Gate 2 Novelty Check — `kern-2611.32927-gcs-dichotomy` (`watch-5`)

- **Timestamp:** `2026-11-27T21:04:19Z`
- **Verdict:** **PASS — `OPEN / UNCONTESTED`**
- **Target:** Christoph Kern, Alexander Firbas, and Manuel Sorge, *"Algorithms and Complexity of Connectivity Switching in Graphs"*, `arXiv:2611.32927v1` (`2026-11-24T16:37:07Z`, full version of LATIN 2026), Section 4 (`sections/gcon.tex` L19–22, L116) — `Global-Con Switching` matroid-switch dichotomy conjecture.

## Verification Receipts

1. **`watch/snapshots/` (`novelty_grep.py "2611.32927" "Christoph Kern" "Firbas" "Manuel Sorge" "Global-Con" "Connectivity Switching"` across `854` files):**
   - `24` lines across `7/854` files: `2611.32927v1` in `arxiv_submissions.{json,md}` and `state.json`, `2611.27956v1` (Cluster Editing by Firbas–Sorge), and unrelated `"global-continuous"` / `"global-convergence"` / `"global-configuration-switching"` substrings (`THM-2687-slope-seven-global-configuration-switching-positive-thirteenfold-no-go.md`). `0` settlements.
2. **Live GitHub (`gh search` & `trureturing`):**
   - `gh search issues/prs/repos "2611.32927"`: `0` hits each.
   - `gh search code "2611.32927"`: `20` hits (`qiao-925/news-digest`, `ehijano/rss_fetch`, `rainwangphy/TCSScholar` daily digest + unrelated numeric CSVs).
   - `gh search code "matroid switches"`: `1` hit (`tavisrudd/othello`, unrelated design `t`-trades).
   - `the-omega-institute/trureturing` PRs up to `#34981`: `0` hits.
3. **arXiv API (`export.arxiv.org`):**
   - `id_list=2611.32927`: `2611.32927v1` (`2026-11-24T16:37:07Z`, LATIN 2026 full version) sole version.
   - `all:"Connectivity Switching" OR all:"Global-Con Switching" OR (au:Sorge AND all:switch)`: returns only `2611.32927v1` and unrelated multi-agent switching papers.
4. **Citations & Preprints (OpenAlex / OpenCitations / Zenodo / Crossref):**
   - OpenAlex `W7239759747` (`10.48550/arXiv.2611.32927`): `cited_by_count: 0`.
   - OpenCitations (`10.48550/arXiv.2611.32927`): `200 []`.
   - Zenodo (`2611.32927` and title): `0` hits. (Crossref `404`.)
5. **ECCC & Conference Web Search (`search_web`):**
   - Queries for `"2611.32927"`, `"Algorithms and Complexity of Connectivity Switching in Graphs"`, `"matroid switches" "Global-Con"`, and LATIN 2026 / ECCC / STOC / FOCS / SODA / ICALP / STACS follow-ups returned only `arXiv:2611.32927` / LATIN 2026 itself (`0` follow-up settlements).
