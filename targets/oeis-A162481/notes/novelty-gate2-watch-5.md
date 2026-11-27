# Novelty Receipt — Gate 2 (`watch-5`)

- **Target:** `targets/oeis-A162481/` (`OEIS:A162481` rev. 23, R. J. Mathar Dec 11 2011 4-term recurrence)
- **Timestamp (UTC):** `2026-11-27T11:32Z`
- **Verdict:** **PASS** (no settled prior art found)

## Exact Queries & Results

1. **`watch/snapshots/` (`tools/novelty_grep.py`):**
   - Query: `.venv/bin/python tools/novelty_grep.py A162481`
   - Result: `0` lines across `0/657` files (incl. Cohen `24384895`, Zenodo `23112421`/`23114921`, `mylesparslow`, Su `24366920`).
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - Query: `all:A162481` -> `0` entries.
3. **OEIS Live JSON (`https://oeis.org/search?q=id:A162481&fmt=json`):**
   - `A162481` rev. `23` (`2025-10-09`) still marks Mathar's Dec 11 2011 recurrence as `Conjecture:`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A162481%22`):**
   - `0` hits.
5. **`mylesparslow-collab.github.io` & `gh search issues` & `search_web`:**
   - `mylesparslow` conjecture ledger: `False`; `gh search issues "A162481 OR A157002"`: `0` hits; `search_web` returned no proof.

## Coverage Limits

- `gh search code "A162481 OR A157002"` hit GitHub HTTP 429 rate-limit; local `657`-file snapshot corpus (incl. newly indexed ledgers) and `gh search issues` are clear.
