# Gate 2 Novelty Receipt — `linusson-2512.24346-conj1`

- **UTC Time:** 2026-11-26T22:09:30Z
- **Reviewer:** `watch-5` (arXiv & citing-papers slice)
- **Verdict:** **PASS** (no arXiv preprint, Zenodo preprint, or web result settles Conjecture 1 `conj:complement` of `arXiv:2512.24346v1`)

## Sources & Exact Queries Checked

1. **Snapshot grep (`tools/novelty_grep.py 2512.24346 "Linusson" "k-Plancherel"`):**
   - Checked all 265 files under `watch/snapshots/**` (0.42s) -> `0` matches.
2. **Live arXiv API via `tools/arxiv_fetch.py` (`use_cache=False`):**
   - `id_list=["2512.24346"]` -> remains `2512.24346v1` (`2025-12-30T16:57:46Z`, 22 pages), no `v2` or erratum.
   - `all:2512.24346 OR (all:"k-Plancherel" AND all:"Markov") OR (all:"Linusson" AND all:"Plancherel")` (`max_results=15`) -> returned only `2512.24346v1`.
3. **Live Zenodo API (`https://zenodo.org/api/records`):**
   - `q=2512.24346` -> `0` hits; `q='"k-Plancherel"'` -> `0` math hits.
4. **Live Web Search (`search_web`):**
   - `"2512.24346" OR "The k-Plancherel Measure and a Finite Markov Chain" OR ("Linusson" "Ozdemir" "k-Plancherel")` -> returns only `arXiv:2512.24346`.

## Near Misses

- None found in arXiv, Zenodo, snapshots, or web search.

## What Was Not Covered

- OpenAlex and Semantic Scholar live APIs (`HTTP 429 Too Many Requests`).
- Closed-access/unpublished manuscripts not indexed in arXiv, Zenodo, or web search.
- GitHub repositories (covered separately by `watch-1` and `watch-6`).
