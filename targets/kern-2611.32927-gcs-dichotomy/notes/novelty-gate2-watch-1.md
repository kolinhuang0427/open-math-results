# Gate 2 Novelty Receipt — `targets/kern-2611.32927-gcs-dichotomy/` (`watch-1`)

- **Target:** `targets/kern-2611.32927-gcs-dichotomy/` (*Algorithms and Complexity of Connectivity Switching in Graphs*, Christoph Kern, Alexander Firbas, Manuel Sorge, `arXiv:2611.32927v1` [`cs.DS`, `cs.CC`, `cs.DM`], §4 `GCS` matroid-switch complexity dichotomy)
- **Checked At (UTC):** `2026-11-27T21:03:34Z`–`2026-11-27T21:04:14Z`
- **Verdict:** **PASS** (novel; `0` prior counterexamples or resolutions to the `GCS` matroid-switch dichotomy found)

## Exact Checks Run & Observed Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2611.32927" "Connectivity Switching" "matroid-switch" "matroid switch"`
   - Result: `7` lines across `3/854` files, all in `watch/snapshots/arxiv/{arxiv_submissions.json,arxiv_submissions.md,state.json}` announcing `2611.32927v1` itself (`0` settlements or counterexamples).
2. **GitHub PRs / Issues / Code Search:**
   - `gh search prs "2611.32927"` -> `[]`; `gh search issues "2611.32927"` -> `[]`; `gh search code '"2611.32927"'` -> `1` daily feed entry (`rainwangphy/TCSScholar/site/daily/2026-11-24.json`).
   - `gh search prs '"Connectivity Switching in Graphs"'` -> `[]`; `gh search issues '"Connectivity Switching in Graphs"'` -> `[]`; `gh search code '"Global-Con Switching" OR "matroid switches"'` -> `[]`.
3. **Live `1337isnot1337/solved-conjectures` HEADs (`2026-11-27T21:03:34Z`):**
   - `main`: `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (unchanged since Sweep 47).
   - `research`: `17de17696aa5c0f19d4f7626a7cf3aee8a6e14ab` (*"Generalize rainbow preservation to regular palettes and any finite arity"*) — unrelated.
4. **arXiv / Zenodo / Crossref / ECCC / Web Search:**
   - arXiv API (`id_list=2611.32927`): sole version `2611.32927v1` (`2026-11-24T16:37:07Z`).
   - Zenodo API (`q=2611.32927`): `0` hits.
   - Crossref (`query=2611.32927`, `query.title=Algorithms+and+Complexity+of+Connectivity+Switching+in+Graphs`): `0` matching DOIs (`5` unrelated items).
   - `search_web` on `eccc.weizmann.ac.il` (`"Kern"` + `"switch" OR "GCS" OR "matroid"`): `0` matching ECCC reports.
   - `search_web` (`"2611.32927"`, `"Algorithms and Complexity of Connectivity Switching in Graphs"`, `"Global-Con Switching" OR "matroid switches" "Kern" OR "Firbas" OR "Sorge"`): returns only `arXiv:2611.32927` / TU Wien publications & thesis (`LATIN 2026` full version); `0` disproofs or counterexamples to the `GCS` matroid-switch dichotomy.
