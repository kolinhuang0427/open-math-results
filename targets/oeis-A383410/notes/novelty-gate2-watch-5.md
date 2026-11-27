# Novelty Receipt — Gate 2 (`watch-5`)

- **Target:** `targets/oeis-A383410/` (`OEIS:A383410` rev. 6, `OEIS:A005649` rev. 123, Mikhail Kurkov Apr 26 2025 conjecture)
- **Timestamp (UTC):** `2026-11-27T11:44Z`
- **Verdict:** **PASS** (no settled prior art found)

## Exact Queries & Results

1. **`watch/snapshots/` (`tools/novelty_grep.py`):**
   - Query: `.venv/bin/python tools/novelty_grep.py A383410 A005649` -> `0` lines across `0/658` files.
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - Query: `all:A383410` -> `0` entries.
3. **OEIS (`oeis/oeisdata` `A383410.seq`):**
   - `%F A383410 Conjecture: A(n,0) = A005649(n).` unchanged.
4. **Zenodo, `mylesparslow`, `gh search issues`, & `search_web`:**
   - Zenodo live API (`"A383410"`): `0` hits; `mylesparslow-collab.github.io`: `False`; `gh search issues "A383410 OR A392058"`: `0` hits; `search_web`: `0` proof hits.
