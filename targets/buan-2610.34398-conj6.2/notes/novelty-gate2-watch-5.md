# Novelty Receipt — Gate 2 (`watch-5`)

- **Target:** `targets/buan-2610.34398-conj6.2/` (`arXiv:2610.34398v1` §7.1 Conjecture 7.2 `conj:TFordered`)
- **Timestamp (UTC):** `2026-11-27T11:34Z`
- **Verdict:** **PASS** (no settled prior art found)

## Exact Queries & Results

1. **`watch/snapshots/` (`tools/novelty_grep.py`):**
   - Query: `.venv/bin/python tools/novelty_grep.py 2610.34398`
   - Result: `0` lines across `0/658` files.
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - Query: `id:2610.34398` -> `2610.34398v1` (`2026-10-25`) remains sole/latest version.
3. **Citing-Paper Check (`Semantic Scholar`):**
   - `https://api.semanticscholar.org/graph/v1/paper/arXiv:2610.34398/citations` -> `0` citations.
4. **Zenodo, `mylesparslow`, `gh search issues`, & `search_web`:**
   - Zenodo live API (`"2610.34398"`): `0` hits.
   - `mylesparslow-collab.github.io` conjecture ledger: `False`.
   - `gh search issues "2610.34398"`: `0` hits.
   - `search_web` (`"2610.34398" OR ("Buan" "Hanson" "Marsh" "TF-ordered" OR "Conjecture 7.2")`): returns only `2610.34398v1` itself and background papers; no resolution of Conjecture 7.2.

## Coverage Limits

- OpenAlex returned HTTP 429 on `2610.34398`; Semantic Scholar (`0` citations), arXiv, Zenodo, `gh search issues`, snapshots, and web search are clear.
