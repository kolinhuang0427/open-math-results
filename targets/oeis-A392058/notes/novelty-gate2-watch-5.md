# Novelty Receipt — Gate 2 (`watch-5`)

- **Target:** `targets/oeis-A392058/` (`OEIS:A392058` rev. 6, `OEIS:A233335` rev. 20, Mikhail Kurkov Dec 29 2025 conjecture)
- **Timestamp (UTC):** `2026-11-27T11:44Z`
- **Verdict:** **PASS** (no settled prior art found)

## Exact Queries & Results

1. **`watch/snapshots/` (`tools/novelty_grep.py`):**
   - Query: `.venv/bin/python tools/novelty_grep.py A392058 A233335` -> `0` lines across `0/658` files.
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - Query: `all:A392058` -> `0` entries.
3. **OEIS (`oeis/oeisdata` `A392058.seq`):**
   - `%F A392058 Conjecture: A(n,0) = A233335(n+1).` unchanged.
4. **Zenodo, `mylesparslow`, `gh search issues`, & `search_web`:**
   - Zenodo live API (`"A392058"`): `0` hits; `mylesparslow-collab.github.io`: `False`; `gh search issues "A383410 OR A392058"`: `0` hits; `search_web`: `0` proof hits.
