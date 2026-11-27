# Novelty Receipt — Gate 2 (`watch-5`)

- **Target:** `targets/oeis-A165204/` (`OEIS:A165204` rev. 15, `OEIS:A165203` rev. 28, Colin Barker Feb 10 2018 conjecture)
- **Timestamp (UTC):** `2026-11-27T11:30Z`
- **Verdict:** **PASS** (no settled prior art found)

## Exact Queries & Results

1. **`watch/snapshots/` (`tools/novelty_grep.py`):**
   - Query: `.venv/bin/python tools/novelty_grep.py A165204 A165203`
   - Result: `0` lines across `0/653` files (incl. Cohen `24384895` & Zenodo `23112421`/`23114921`).
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - Query: `all:A165204 OR all:A165203` -> `0` entries.
3. **OEIS Live JSON (`A165204`, `A165203`):**
   - `A165204` rev. `15` (`2018-02-15`) still marks Colin Barker's Feb 10 2018 g.f. & 4-term recurrence as `Conjectures from _Colin Barker_`.
4. **Zenodo API (`https://zenodo.org/api/records`):**
   - Queries `"A165204"` and `"A165203"` -> `0` hits.
5. **GitHub & Web (`gh search code/issues`, `search_web`):**
   - `gh search code "A165204"`: only `archmageirvine/joeis`, `loda-lang/loda-programs`, and unrelated crate/data files; `gh search issues "A165204"`: `0` hits.
   - `mylesparslow-collab.github.io` conjecture ledger & Su Zenodo `24366920`: `0` hits for `A165204`/`A165203`.
   - `search_web` returned no proof of `A165204`.

## Coverage Limits

- No cited arXiv preprint on this target for OpenAlex/S2 citing-paper traversal.
