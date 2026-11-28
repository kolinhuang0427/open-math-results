# Gate 3 Novelty Receipt — `targets/kern-2611.32927-gcs-dichotomy/` (`watch-1`)

- **Target:** `targets/kern-2611.32927-gcs-dichotomy/` (*Algorithms and Complexity of Connectivity Switching in Graphs*, Christoph Kern, Alexander Firbas, Manuel Sorge, `arXiv:2611.32927v1` [`cs.DS`, `cs.CC`, `cs.DM`], §4 `sections/gcon.tex` L116 `GCS` matroid-switch dichotomy)
- **Checked At (UTC):** `2026-11-27T21:14:00Z`–`2026-11-27T21:14:39Z` (extending Gate 2 at `21:03:34Z`)
- **Verdict:** **PASS** (novel; `0` prior counterexamples or resolutions found)

## Exact Checks Run & Observed Results

1. **Snapshot grep (from Gate 2, unchanged `854` files):** `7` lines across `3/854` files in `watch/snapshots/arxiv/` announcing `2611.32927v1` only (`0` settlements).
2. **GitHub PRs / Issues / Code Search (`21:12:01Z`–`21:14:36Z`):**
   - `gh search prs "2611.32927"` -> `[]`; `gh search issues "2611.32927"` -> `[]`
   - `gh search code '"Global-Con Switching"'` -> `[]`
3. **Live `1337isnot1337/solved-conjectures` HEADs (`21:14:00Z`):**
   - `main`: `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (unchanged).
   - `research`: `bd6cc41b170d8aa184f8d6fb699db9d9d8fe2eeb` (*"Show the ZFC counterexample still has rainbows of every countable order type"*) — unrelated.
4. **arXiv / Zenodo / ECCC / Web Search (`21:12:01Z`–`21:14:39Z`):**
   - arXiv API (`id_list=2611.32927`): sole version `2611.32927v1` (`2026-11-24T16:37:07Z`).
   - Zenodo API (`q=2611.32927`): `0` hits.
   - `search_web` (`site:eccc.weizmann.ac.il "Connectivity Switching" OR "matroid switches" OR "Kern" "Firbas"`): `0` matching ECCC reports.
   - `search_web` (`"2611.32927" "matroid switches" OR "Global-Con Switching" "dichotomy"`): returns only `arXiv:2611.32927v1`, `airr.science`, and `themoonlight.io` digests of `2611.32927v1`; `0` counterexamples to the `GCS` matroid-switch dichotomy.
5. **Independent Check Execution (`#2019`):**
   - Command: `.venv/bin/python -u targets/kern-2611.32927-gcs-dichotomy/notes/check-check-1.py`
   - Exit status: `0`
   - Stdout:
     - `Non-matroid axioms and GCS equivalences (Pi_1, Pi_2, Pi_3): PASS`
     - `PASS`
