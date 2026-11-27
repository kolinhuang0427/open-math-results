# Novelty Receipt — Gate 2 (`watch-5`)

- **Target:** `targets/oeis-A379459/` (`OEIS:A379459` rev. 4, `OEIS:A379460` rev. 4, `OEIS:A006351` rev. 195)
- **Timestamp (UTC):** `2026-11-27T11:45Z`
- **Verdict:** **PASS** (no settled prior art found)

## Exact Queries & Results

1. **`watch/snapshots/` (`tools/novelty_grep.py`):**
   - Query: `.venv/bin/python tools/novelty_grep.py A379459 A379460 A006351` -> `0` lines across `0/658` files.
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - Query: `all:A379459 OR all:A379460` -> `0` entries.
3. **OEIS (`oeis/oeisdata` `A379459.seq`, `A379460.seq`, `A006351.seq`):**
   - All three conjectures (`Conjecture: A(n,0) = A006351(n+2)`, `A(n,0) = A006351(n+1)`, `a(n) = A379459(n-2,0) = A379460(n-1,0)`) remain unmarked by proof.
4. **Zenodo, `mylesparslow`, `gh search issues`, & `search_web`:**
   - Zenodo live API (`"A379459"`, `"A379460"`): `0` hits; `mylesparslow-collab.github.io`: `False`; `gh search issues`: `trureturing#27785` (`state: open`, `comments: 0`, `0` PRs); `search_web`: `0` proof hits.
