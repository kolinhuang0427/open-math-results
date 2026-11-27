# Novelty Receipt — Gate 2 (`watch-5`)

- **Target:** `targets/oeis-A157003/` (`OEIS:A157003` rev. 37, R. J. Mathar Nov 19 2014 6-term recurrence)
- **Timestamp (UTC):** `2026-11-27T11:33Z`
- **Verdict:** **PASS** (no settled prior art found)

## Exact Queries & Results

1. **`watch/snapshots/` (`tools/novelty_grep.py`):**
   - Query: `.venv/bin/python tools/novelty_grep.py A157003`
   - Result: `0` lines across `0/658` files.
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - Query: `all:A157003` -> `0` entries.
3. **OEIS Live JSON (`https://oeis.org/search?q=id:A157003&fmt=json`):**
   - `A157003` rev. `37` (`2025-11-05`) still marks Mathar's Nov 19 2014 recurrence as `Conjecture:`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A157003%22`):**
   - `0` hits.
5. **`mylesparslow-collab.github.io`, `gh search issues`, & `search_web`:**
   - `mylesparslow` conjecture ledger: `False`; `gh search issues "A157003"`: `0` hits; `search_web` returned only OEIS/combinatorial pattern-avoidance links, no proof of Mathar's recurrence.

## Coverage Limits

- `gh search code` skipped after earlier GitHub 429 cooldown; local `658`-file snapshot corpus and `gh search issues` are clear.
