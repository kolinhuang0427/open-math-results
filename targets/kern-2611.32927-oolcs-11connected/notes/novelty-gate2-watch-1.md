# Gate 2 Novelty Receipt — `targets/kern-2611.32927-oolcs-11connected/` (`watch-1`)

- **Target:** `targets/kern-2611.32927-oolcs-11connected/` (*Algorithms and Complexity of Connectivity Switching in Graphs*, Christoph Kern, Alexander Firbas, Manuel Sorge, `arXiv:2611.32927v1` [`cs.DS`, `cs.CC`, `cs.DM`], `sections/conclusion.tex` L5 `OOLCS` restricted to `{1,1}`-bounded connected switches)
- **Checked At (UTC):** `2026-11-27T21:07:39Z`–`2026-11-27T21:08:02Z`
- **Verdict:** **PASS** (novel; `0` prior resolutions of `{1,1}`-bounded connected `OOLCS` / `WLCS` found)

## Exact Checks Run & Observed Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2611.32927" "OOLCS" "One-or-Other" "connected switches"`
   - Result: `6` lines across `3/854` files, all in `watch/snapshots/arxiv/{arxiv_submissions.json,arxiv_submissions.md,state.json}` announcing `2611.32927v1` itself (`0` settlements or proofs).
2. **GitHub PRs / Issues / Code Search:**
   - `gh search prs/issues '"OOLCS"'`: unrelated OCaml/surfsim/etc. hits only (`0` graph-switching hits).
   - `gh search code '"OOLCS" "switch"'` -> `[]`; `gh search code '"On-Off Local-Con Switching"'` -> `[]`.
3. **Live `1337isnot1337/solved-conjectures` HEADs (`2026-11-27T21:07:39Z`):**
   - `main`: `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (unchanged).
   - `research`: `eb68ebe0df18c6fd0632c673400c47c980fb3d75` (*"Audit Zhang’s exact question against pair, higher-dimensional and recent rainbow results"*) — unrelated.
4. **arXiv / Zenodo / Crossref / Web Search:**
   - arXiv API (`id_list=2611.32927`): sole version `2611.32927v1` (`2026-11-24T16:37:07Z`).
   - Zenodo API (`q=2611.32927`): `0` hits.
   - Crossref (`query.title=Algorithms+and+Complexity+of+Connectivity+Switching+in+Graphs`): `0` matching DOIs (`3` unrelated items).
   - `search_web` (`"OOLCS" "switch" OR "1,1" "Connectivity Switching" "Kern"` and `"On-Off Local-Con Switching" OR "On-Off Global-Con" "1,1" OR "11-bounded"`): returns only `arXiv:2611.32927v1`, TU Wien / LATIN 2026 mentions, and automated digests (`airr.science`, `themoonlight.io`) of `2611.32927v1`; `0` follow-up resolutions.
   - Coverage limit: `search_web` query `site:eccc.weizmann.ac.il "OOLCS" OR "One-or-Other" "switch"` returned `no summary returned`; earlier `site:eccc.weizmann.ac.il` checks for `Kern` / `Connectivity Switching` / `switch graph` returned `0` matching reports.
