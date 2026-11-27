# Gate 2 Novelty Receipt — `oeis-A006255`

- **UTC Time:** 2026-11-26T22:21:00Z
- **Reviewer:** `watch-5` (arXiv & citing-papers slice)
- **Verdict:** **PASS** (no arXiv preprint, Zenodo preprint, Crossref publication, or web result found settling Padhi's June 2026 conjecture on OEIS `A006255`)

## Sources & Exact Queries Checked

1. **Snapshot grep (`tools/novelty_grep.py A006255 Padhi A386251 "8434" "b(n)"`):**
   - Checked all 266 files under `watch/snapshots/**` (1.74s) -> `0` matches for `A006255` (Padhi hit in `1337` is unrelated Zeilberger-challenges paper).
2. **Live arXiv API via `tools/arxiv_fetch.py` (`use_cache=False`):**
   - `all:A006255 OR (all:"Padhi" AND all:"square") OR (all:"Granville" AND all:"Selfridge" AND all:"2001")` -> returned `2608.11290v2` (checked abstract: Chomp / Spahn–Zeilberger / SSYT / Geode / Kauers–Zeilberger, unrelated to `A006255`).
   - `all:"A006255"` -> `0` results.
3. **Live Zenodo API (`https://zenodo.org/api/records`):**
   - `q=A006255` -> `0` hits; `q='"Padhi" "A006255"'` -> `0` relevant hits.
4. **Live Crossref & OEIS JSON:**
   - Crossref `query=A006255` -> `0` math hits.
   - Live OEIS `A006255` (`https://oeis.org/search?q=id:A006255&fmt=json`) -> remains at `revision 106` (`2026-06-19T00:16:16-04:00`), unchanged.
5. **Live Web Search (`search_web`):**
   - `"A006255" ("Padhi" OR "b(n)" OR "2, 3, 10, 171" OR "proved" OR "Selfridge") 2026` -> returns only OEIS `A006255` itself.

## Near Misses

- **Erdős & Selfridge (1992, *Amer. Math. Monthly* 99, pp. 791–794) & Adenwalla (`arXiv:2504.19196`):** proves `P(n) > sqrt(2n) + 1 => a(n) = n + P(n)`, leaving the boundary `sqrt(2n) <= P(n) <= sqrt(2n) + 1` (including `n = 171`) open.
- **Granville & Selfridge (2001):** gives a $2\sqrt{z}$ interval bound (used in `PROOF.md`), does not settle the sharper $\sqrt{2z}$ threshold of Padhi's conjecture.
- **Jaideep Sai Padhi (`arXiv:2608.11290v2`):** unrelated combinatorics challenge problems.

## What Was Not Covered

- OpenAlex and Semantic Scholar live APIs (`HTTP 429 Too Many Requests`).
- Closed-access/print-only texts not indexed in arXiv, Zenodo, Crossref, or web search.
- GitHub repositories (covered separately by `watch-1` and `watch-6`).
