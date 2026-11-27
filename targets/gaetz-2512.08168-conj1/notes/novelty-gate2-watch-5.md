# Gate 2 Novelty Check — `gaetz-2512.08168-conj1` (watch-5)

- **UTC Timestamp:** `2026-11-26T23:26:05Z`
- **Target:** `targets/gaetz-2512.08168-conj1/TARGET.md`
- **Verdict:** **PASS** (no public proof or counterexample to Conjecture 1.3 `conj:union-intersection` found across arXiv, OpenAlex citing check, Zenodo, Crossref, web search, or 356 local snapshot files)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 356 files incl. `aliromman__math.json`, `trureturing-tools.json`, `trureturing.json`):**
   - `"2512.08168" "conj:union-intersection" "BP(w)" "Billey--Postnikov" "Billey-Postnikov"` -> `4` lines across `3/356` files:
     - `watch/snapshots/arxiv/citing/gaetz-2512.08168-conj1.json` and `openalex_works_cache.json` (local sweep cache).
     - `watch/snapshots/discovered/the-omega-institute__trureturing-tools.json:1484`: notes only `arXiv:2512.08168` **Conjecture 1.9** (explicitly distinct from Conjecture 1.3 `conj:union-intersection`, refuted by Theorem 6.2 of the paper itself).

2. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:2512.08168` -> `1` entry (`2512.08168v2`, `2025-12-09T01:51:50Z`, latest version).
   - `au:Gaetz AND all:Coxeter` (`9` entries) and `au:Gaetz AND all:Bruhat` (`10` entries, up to `2611.33572v1` *Reflection subgroups and the Lookup Conjecture*, 2026-11-25) -> none prove `conj:union-intersection` for arbitrary Coxeter groups.
   - `all:"Billey-Postnikov"` -> `8` entries (latest is `2512.08168v2` itself; prior papers are 2013–2024).
   - `all:"union-intersection" AND all:Coxeter` -> `0` entries.

3. **OpenAlex Citing Check (`watch/snapshots/arxiv/citing/gaetz-2512.08168-conj1.json`):**
   - Checked at `2026-11-26T22:55:34Z` during 3h sweep (`errors: []`): `citing_count: 0`, `citing_works: []`.

4. **Zenodo API (`https://zenodo.org/api/records`), Crossref, & Web Search (`search_web`):**
   - Zenodo `q=2512.08168` and `q="2512.08168"` -> `0` hits; `q="Christian Gaetz" Coxeter` -> unrelated matches (`level-2 Coxeter graphs`, etc.).
   - Crossref `query="2512.08168"` -> unrelated DOI substring hits (`08168`).
   - `search_web`: `"2512.08168" OR ("Gaetz" "union-intersection" "Coxeter") OR ("Billey-Postnikov" "Gaetz" "1.3" proved)` -> returns only `arXiv:2512.08168` (finite Weyl & rank $\le 3$ partial results).

## Near Misses & Why They Do Not Settle the Exact Statement

- `the-omega-institute__trureturing-tools.json:1484`: Explicitly flags `arXiv:2512.08168` **Conjecture 1.9** (already refuted in Theorem 6.2 of `2512.08168v2` itself), not Conjecture 1.3 (`conj:union-intersection`).
- `arXiv:2611.33572v1` (Gaetz–Gao, 2026-11-25, *Reflection subgroups and the Lookup Conjecture*): Different conjecture on reflection subgroups / Lookup Conjecture.
- `CONTESTED.md`: absent from `targets/gaetz-2512.08168-conj1/`.

## What Was Not Covered

- Semantic Scholar (`HTTP 429` unauthenticated) and closed-access/unindexed private manuscripts.
