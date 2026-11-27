# Gate 2 Novelty Receipt — `ingrosso-2611.30155-q4.6` (`watch-5`)

- **Target:** `targets/ingrosso-2611.30155-q4.6/` — E. Ingrosso, M. Trombetti, and A. Zitouni, *"Groups with dual classes of subgroups"*, `arXiv:2611.30155v1` / *J. Aust. Math. Soc.* DOI `10.1017/s1446788726101682`, Section 4 Question 4.6 (smallest possible subnormal defect in Theorem 4.5).
- **Checked UTC:** `2026-11-27T16:33:35Z`–`2026-11-27T16:34:34Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)** — no prior or competing determination of the sharp subnormal defect in Theorem 4.5 found.

## Exact Queries & Results
1. **Local snapshots (`watch/snapshots/**`, 742 files):**
   - `.venv/bin/python tools/novelty_grep.py "2611.30155" "Ingrosso" "Trombetti" "pronorm" "10.1017/s1446788726101682" --max-per-file 0 --max-total 0`:
     - Only hits for `2611.30155` are `arxiv_submissions.{json,md}` and `state.json`.
     - Near-miss hits checked directly: `facebookresearch/atlas-lean` (`Kourovka18Problem32`, `Kourovka19Problem109Wanted`, `Kourovka19Problem74Wanted` — distinct Kourovka pronormal problems) and `eliottcassidy2000/math` `THM-4728` (`01-canon/theorems/THM-4728-...md`, verified via `gh api` to concern `HYP-9340` odd-order permutation subgroups and tournament/graph twisted Burnside defects, unrelated to `arXiv:2611.30155`).
   - `hexagonmath-index.md`, `papex-index.md`, `hwzw-algebra-number-theory-drafts.md`, `raghav-research-math-index.md`: `0` hits.
2. **Live GitHub (`gh`):**
   - `gh search issues "2611.30155"`, `gh search prs "2611.30155"`, `gh search repos "2611.30155"`, `gh search issues "Ingrosso" "pronormal"`, `gh search issues "Trombetti" "pronormal"`, `gh search code "10.1017/s1446788726101682"`, `gh search prs/issues "pronormal" repo:the-omega-institute/trureturing`: `0` hits.
   - `gh search code "2611.30155"`: 6 hits — 1 arXiv RSS mirror (`ehijano/rss_fetch`) and 5 unrelated floating-point numbers.
3. **Live Preprint / Citation APIs & Web:**
   - **arXiv API (`id_list=2611.30155`):** `2611.30155v1` (`2026-11-23T07:03:10Z`) is sole version.
   - **OpenAlex (`doi.org/10.48550/arXiv.2611.30155` & `doi.org/10.1017/s1446788726101682`):** `publication_date: 2026-09-23`, `cited_by_count: 0`.
   - **Semantic Scholar (`ARXIV:2611.30155`):** `citationCount: 0`.
   - **Zenodo (`q=2611.30155`):** `0` hits; **Crossref (`query=2611.30155`):** `0` relevant hits.
   - **`search_web` (`"2611.30155" OR ("Ingrosso" "pronormal" "defect")`)**: returns only `arXiv:2611.30155` / JAMS article.

## Near-Misses & Coverage Limits
- **Near-misses:** `eliottcassidy2000/math` `THM-4728` and `atlas-lean` Kourovka pronormal files are distinct problems.
- **Coverage limits:** Private/unindexed drafts posted after `2026-11-27T16:34:34Z` are not covered.
