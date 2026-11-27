# Novelty Receipt — Gate 2 (`watch-5`)

- **Target:** `targets/oeis-A026923/` (`OEIS:A026923` rev. 27, Colin Barker Sep 01 2019 g.f. & 11-term recurrence)
- **Timestamp (UTC):** `2026-11-27T11:41Z`
- **Verdict:** **PASS** (no settled prior art found)

## Exact Queries & Results

1. **`watch/snapshots/` (`tools/novelty_grep.py`):**
   - Query: `.venv/bin/python tools/novelty_grep.py A026923 A026927`
   - Result: `0` lines across `0/658` files.
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - Query: `all:A026923 OR all:A026927` -> `0` entries.
3. **OEIS (`oeis/oeisdata` `A026923.seq`):**
   - Still contains `%F A026923 Conjectures from _Colin Barker_, Sep 01 2019: (Start)`.
4. **Zenodo, `mylesparslow`, `gh search issues`, & `search_web`:**
   - Zenodo live API (`"A026923"`): 1 unrelated entomology record (`6081413`, *Afrobethylus swazi Ramos & Azevedo, sp. nov.*); `0` math hits.
   - `mylesparslow-collab.github.io` conjecture ledger: `False`; `gh search issues "A026923 OR A026927"`: `0` hits; `search_web`: `0` proofs.
