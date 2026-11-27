# Gate 2 Novelty Receipt (`watch-5`) — `targets/iverson-2506.20778-conjPaley/`

- **Checked UTC:** `2026-11-27T06:35:03Z` – `2026-11-27T06:49:04Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/iverson-2506.20778-conjPaley/`)
- **Target Scope:** Joseph W. Iverson and Dustin G. Mixon, `arXiv:2506.20778v1` (*Asymmetric SICs over finite fields*, `2025-06-25`), Section 4, Conjecture `conj:Paley` (parts (a) and (b) for prime powers $q > 11, q \equiv 3 \bmod 4$).

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 522 files):**
   - `.venv/bin/python tools/novelty_grep.py "2506.20778" "Iverson" "Mixon" "Asymmetric SIC" "conj:Paley"`
   - Result: 7 lines across 5 files: only `citing/iverson-2506.20778-conjPaley.json`, `openalex_works_cache.json`, and unrelated Alexeev–Mixon Sidon-set hits (`E0707`, `E0844`).
2. **arXiv (`tools/arxiv_fetch.py`):**
   - `id_list=["2506.20778"]` & `all:2506.20778`: `2506.20778v1` (`2025-06-25T19:09:29Z`) is the sole version.
   - `all:"Asymmetric SICs"`: 2 hits (`2506.20778v1` and unrelated 5G engineering `2011.01511v1`).
   - `au:Iverson AND au:Mixon`: 15 total (top 10 checked, newest `2603.23643v1` *Approximation theorems in bilipschitz invariant theory*); none settle `conj:Paley`.
   - `all:"conj:Paley"`: `0` results.
3. **OpenAlex citing snapshot (`watch/snapshots/arxiv/citing/iverson-2506.20778-conjPaley.json`):**
   - Checked `2026-11-27T05:01:49Z`: `citing_count: 0`, `errors: []`.
4. **Zenodo & Crossref:**
   - `https://zenodo.org/api/records?q=2506.20778&size=5`: `total=0` (`"Asymmetric SICs"` returned unrelated networking/ophthalmology hits).
   - `https://api.crossref.org/works?query=2506.20778&rows=5`: 5 unrelated `20778` DOIs; `"Asymmetric SICs over finite fields"`: 5 unrelated finite-field textbook chapters.
5. **Web Search (`search_web`):**
   - `"2506.20778" OR ("Iverson" "Mixon" "Asymmetric SICs") OR "conj:Paley"`: only `arXiv:2506.20778` itself.
6. **GitHub Read-Only Checks (`gh api` trees + `gh search`):**
   - Recursive tree grep (`2506\.20778|iverson|mixon|asymmetric.?sic`) across all 15 competing repos: `0` matches.
   - `gh search issues/prs --repo the-omega-institute/trureturing "2506.20778"` and `"Asymmetric SIC"`: `0` hits (`trureturing#16342` closed is unrelated `arXiv:2012.13642` Greaves–Iverson–Jasper–Mixon Example 5.8).

## What Was Not Covered
- Closed-access venues or private repositories not indexed by arXiv, OpenAlex, Zenodo, Crossref, GitHub, or web search.
