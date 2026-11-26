# Gate 3 Novelty Receipt — `oeis-A100691`

- **UTC Time:** 2026-11-26T21:14:45Z
- **Reviewer:** `watch-5` (arXiv & citing-papers slice)
- **Verdict:** **PASS** (fresh live pre-report check confirms no new arXiv preprint, Zenodo preprint, Crossref publication, OEIS update, or web result settles Mathar's 2022 conjecture or the `s(5)=160` triangular-strip SAW erratum)

## Fresh Live Sources & Exact Queries Checked

1. **Snapshot grep (`tools/novelty_grep.py A100691 A193641`):**
   - Checked all 224 files under `watch/snapshots/**` (0.49s) -> `0` matches.
2. **Live arXiv API via `tools/arxiv_fetch.py` (`use_cache=False`):**
   - `all:A100691 OR all:A193641 OR (all:"self-avoiding" AND all:"triangular lattice" AND all:"strip")` (`max_results=10`) -> `0` results.
   - `cat:math.CO` (`max_results=15`, `sort_by="submittedDate"`) -> top ID `2611.34855v1`; `0` matches for `a100691`, `a193641`, `self-avoiding`, `mathar`.
3. **Live Zenodo API (`https://zenodo.org/api/records`):**
   - `q=A100691` -> `0` hits.
   - `q=A193641` -> `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A100691&fmt=json`):**
   - Confirmed `A100691` remains at `revision 11` (`2022-07-22T09:50:24-04:00`), unchanged.
5. **Live Crossref API (`https://api.crossref.org/works`):**
   - `query=A100691` and `query=A193641` -> `0` math matches (only unrelated biology/urban planning DOI `10.1068/a100691`).
6. **Live Web Search (`search_web`):**
   - `"A100691" ("A193641" OR "160" OR "158" OR "erratum" OR "proved" OR "counterexample")` -> no new settling results.

## Near Misses

- Previously verified at Gate 2 (`notes/novelty-gate2-watch-5.md`): Ramírez & Sirvent (2015, $k$-Narayana substitution), Došlić & Zubac (2015, maximal matchings in linear polymers), Baril & Hassler (`arXiv:2411.17628`, Fibonacci lattice intervals) — none prove the `A193641` `{-1,0,1}` array recurrence or link to `A100691`.

## What Was Not Covered

- Live OpenAlex API returned `HTTP 429 Too Many Requests` (unauthenticated IP daily budget exhausted across shared swarm queries; Gate 2 OpenAlex queries at `2026-11-26T20:18Z` showed 0 settling citing works).
- Live OEIS JSON for `A193641` returned `HTTP 429` on back-to-back request (checked at Gate 2 at rev 48).
- Print-only text of J. Labelle (1996, Bull. ICA 17).
- GitHub repositories (covered separately by `watch-1` and `watch-6`).
