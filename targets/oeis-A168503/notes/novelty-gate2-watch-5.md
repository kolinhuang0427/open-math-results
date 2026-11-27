# Novelty Receipt — Gate 2 (`watch-5`)

- **Target:** `targets/oeis-A168503/` (`OEIS:A168503` rev. 20, R. J. Mathar Feb 10 2015 4-term recurrence)
- **Timestamp (UTC):** `2026-11-27T11:36Z`
- **Verdict:** **PASS** (no settled prior art found)

## Exact Queries & Results

1. **`watch/snapshots/` (`tools/novelty_grep.py`):**
   - Query: `.venv/bin/python tools/novelty_grep.py A168503`
   - Result: `0` lines across `0/658` files.
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - Query: `all:A168503` -> `0` entries.
3. **OEIS Live JSON (`https://oeis.org/search?q=id:A168503&fmt=json`):**
   - `A168503` rev. `20` (`2025-02-07`) still marks Mathar's Feb 10 2015 recurrence as `Conjecture:`.
4. **Zenodo, `mylesparslow`, `gh search issues`, & `search_web`:**
   - Zenodo live API (`"A168503"`): `0` hits; `mylesparslow-collab.github.io`: `False`; `gh search issues "A168503 OR A168505"`: `0` hits; `search_web`: `0` proof hits.

## Coverage Limits

- `gh search code` skipped under earlier GitHub 429 cooldown; local `658`-file snapshot corpus and `gh search issues` are clear. No cited arXiv preprint for OpenAlex/S2 citing-paper traversal.
