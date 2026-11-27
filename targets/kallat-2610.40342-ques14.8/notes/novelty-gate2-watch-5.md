# Gate 2 Novelty Receipt — targets/kallat-2610.40342-ques14.8 (watch-5)

- **Checked UTC:** 2026-11-27T10:16:01Z – 2026-11-27T10:16:23Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2610.40342 Kallat "prob:composite"`):** `0` hits for `2610.40342` or `prob:composite` across `618` files; verified `the-omega-institute/trureturing` `Library/FiniteGroups/kallat2026weightedpermutations.md` via `gh api` concerns `arXiv:2610.15849v1` (A378495), not `2610.40342` Question 14.8.
2. **arXiv API (`tools/arxiv_fetch.py query`):** `2610.40342v1` (`2026-10-29`) is the sole version; `abs:"2610.40342"` = `0` entries.
3. **Live OpenAlex & Zenodo (`2610.40342`):** OpenAlex `cited_by=0`; Zenodo `0` hits (Semantic Scholar API returned HTTP 429).
4. **Web search (`search_web` `"2610.40342" OR ("Kallat" "2610.40342") OR "prob:composite"`):** `0` refutations found.

## Coverage Limits
- Semantic Scholar API returned HTTP 429; non-indexed private repos or paywalled papers not mentioning `2610.40342` are not covered.
