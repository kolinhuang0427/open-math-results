# Gate 2 Novelty Receipt — `oeis-A250917`

- **UTC Time:** 2026-11-26T20:58:00Z
- **Reviewer:** `watch-5` (arXiv & citing-papers slice)
- **Verdict:** **PASS** (no arXiv preprint, Zenodo preprint, journal paper, or OpenAlex citing work found settling R. J. Mathar's 2020 order-5 D-finite recurrence for OEIS `A250917`)

## Sources & Exact Queries Checked

1. **Snapshot grep (`tools/novelty_grep.py A250917 "379819484551" "C(x)^3"`):**
   - Checked all 224 files under `watch/snapshots/**` (0.59s) -> `0` matches.
2. **Live arXiv API via `tools/arxiv_fetch.py` (`use_cache=False`):**
   - `all:A250917 OR (all:"Catalan" AND all:"D-finite" AND all:"exponential")` (`max_results=15`) -> `0` results.
3. **Zenodo API (`https://zenodo.org/api/records`):**
   - `q=A250917` -> `0` results.
   - `q=0009-0004-6946-8389` (Roberto Blanco Gómez ORCID) and `q=exp(x*C(x)^3)` -> `0` matches for `A250917`.
4. **OpenAlex live API (`https://api.openalex.org/works`):**
   - `search="A250917"` -> `0` results.
   - `search="Mathar's recurrence for OEIS"` and `search="Roberto Blanco Gomez Mathar"` -> checked all 10+ hits (`A026124`, `A080894`, `A174193`, `A186185`, `A176677`, `A348410`, `A026771`, `A176678`, `A027182`); none address `A250917`.
   - `search="exp(x*C(x)^3) Catalan"` -> `0` matching works.
5. **Web search (`search_web`):**
   - `"A250917" ("D-finite" OR "recurrence" OR "proved" OR "Catalan" OR "Blanco")` -> returns only OEIS A250917 / A250916 / A251568 context.
   - `"exp(x*C(x)^3)" OR "exp( x*C(x)^3 )" OR "(-11*n+20)*a(n-1)" OR "379819484551"` -> `0` prior proofs.

## Near Misses

- Roberto Blanco Gómez's Zenodo series and related 2026 preprints proving Mathar's recurrences for other OEIS sequences (`A026124`, `A026771`, `A027182`, `A080894`, `A174193`, `A176677`, `A176678`, `A186185`, `A348410`) — none cover `A250917`.
- General closure theorems for D-finiteness of $\exp(\text{algebraic})$ guarantee *some* P-recurrence exists, without proving Mathar's explicit order-5 recurrence on `A250917`.

## What Was Not Covered

- Semantic Scholar live API (rate-limited HTTP 429).
- Closed-access/unpublished manuscripts not indexed on arXiv, Zenodo, OpenAlex, or web search.
- GitHub repositories (covered separately by `watch-1` and `watch-6`).
