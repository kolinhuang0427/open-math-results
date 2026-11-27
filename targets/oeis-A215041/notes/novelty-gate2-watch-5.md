# Novelty Receipt — Gate 2 (`watch-5`)

- **Target:** `targets/oeis-A215041/` (`OEIS:A215041` rev. 10, `OEIS:A193681` rev. 24, `arXiv:1210.1018` Open Problem #1)
- **Timestamp (UTC):** `2026-11-27T11:22Z`
- **Verdict:** **PASS** (no settled prior art found)

## Exact Queries & Results

1. **`watch/snapshots/` (`tools/novelty_grep.py`):**
   - Query: `.venv/bin/python tools/novelty_grep.py A215041 A193681 1210.1018`
   - Result: `0` lines across `0/652` files (incl. Zenodo `23112421`/`23114921` and Cohen `24384895`).
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - Query: `all:A215041 OR all:1210.1018 OR (ti:"cos" AND ti:"Galois" AND au:"Lang")`
   - Result: `1210.1018v2` (`2017-03-07`) is sole/latest version; `0` other arXiv hits.
3. **OEIS Live JSON (`https://oeis.org/search?q=id:A215041&fmt=json`, `A193681`):**
   - `A215041` rev. `10` (`2023-12-25`) still states `Conjectures for a(n), n>=2:`; `A193681` rev. `24` (`2024-10-22`) shows no proof.
4. **Zenodo API (`https://zenodo.org/api/records`):**
   - Queries `"A215041"` and `"1210.1018"` -> `0` hits.
5. **Web Search & Crossref (`search_web`, `api.crossref.org`):**
   - Query `"A215041" OR "1210.1018" discriminant Lang proof OR conjecture` and `"The field Q(2cos(pi/n)), its Galois group"`: returned only OEIS and Lang's `1210.1018` itself; Crossref returned no citing proof paper.

## Coverage Limits

- Both OpenAlex and Semantic Scholar returned HTTP 429 on `1210.1018` citation endpoints during this window; web search, Crossref, arXiv, Zenodo, live OEIS, and local snapshots all show no prior proof.
