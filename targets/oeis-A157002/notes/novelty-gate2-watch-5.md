# Novelty Receipt — Gate 2 (`watch-5`)

- **Target:** `targets/oeis-A157002/` (`OEIS:A157002` rev. 15, R. J. Mathar Nov 19 2014 4-term recurrence)
- **Timestamp (UTC):** `2026-11-27T11:32Z`
- **Verdict:** **PASS** (no settled prior art found)

## Exact Queries & Results

1. **`watch/snapshots/` (`tools/novelty_grep.py`):**
   - Query: `.venv/bin/python tools/novelty_grep.py A157002`
   - Result: `0` lines across `0/657` files.
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - Query: `all:A157002` -> `0` entries.
3. **OEIS Live JSON (`https://oeis.org/search?q=id:A157002&fmt=json`):**
   - `A157002` rev. `15` (`2025-09-22`) still marks Mathar's Nov 19 2014 recurrence as `Conjecture:`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A157002%22`):**
   - `0` hits.
5. **`mylesparslow-collab.github.io` & `gh search issues` & `search_web`:**
   - `mylesparslow` conjecture ledger: `False`; `gh search issues "A162481 OR A157002"`: `0` hits; `search_web` returned only OEIS links.

## Coverage Limits

- `gh search code "A162481 OR A157002"` hit GitHub HTTP 429 rate-limit; local `657`-file snapshot corpus and `gh search issues` are clear.
