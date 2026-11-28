# Gate 3 Novelty Receipt — `targets/kern-2611.32927-oolcs-11connected/` (`watch-1`)

- **Target:** `targets/kern-2611.32927-oolcs-11connected/` (*Algorithms and Complexity of Connectivity Switching in Graphs*, Christoph Kern, Alexander Firbas, Manuel Sorge, `arXiv:2611.32927v1` [`cs.DS`, `cs.CC`, `cs.DM`], `sections/conclusion.tex` L5 `OOLCS` restricted to `{1,1}`-bounded connected switches)
- **Checked At (UTC):** `2026-11-27T21:14:00Z`–`2026-11-27T21:14:22Z` (extending Gate 2 at `21:07:39Z`)
- **Verdict:** **PASS** (novel; `0` prior resolutions found)

## Exact Checks Run & Observed Results

1. **Snapshot grep (from Gate 2, unchanged `854` files):** `6` lines across `3/854` files in `watch/snapshots/arxiv/` announcing `2611.32927v1` only (`0` settlements).
2. **GitHub PRs / Issues / Code Search (`21:14:00Z`):**
   - `gh search prs "2611.32927"` -> `[]`
   - `gh search issues "2611.32927"` -> `[]`
   - `gh search code '"On-Off Local-Con Switching"'` -> `[]`
3. **Live `1337isnot1337/solved-conjectures` HEADs (`21:14:00Z`):**
   - `main`: `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (unchanged).
   - `research`: `bd6cc41b170d8aa184f8d6fb699db9d9d8fe2eeb` (*"Show the ZFC counterexample still has rainbows of every countable order type"*) — unrelated.
4. **arXiv / Zenodo / Web Search (`21:14:00Z`–`21:14:07Z`):**
   - arXiv API (`id_list=2611.32927`): sole version `2611.32927v1` (`2026-11-24T16:37:07Z`).
   - Zenodo API (`q=2611.32927`): `0` hits.
   - `search_web` (`"On-Off Local-Con Switching" OR "OOLCS" "1,1" "polynomial time" OR "matching"`): returns only `arXiv:2611.32927v1` and `themoonlight.io` digest; `0` follow-up resolutions.
   - Coverage limit: `search_web` query `site:eccc.weizmann.ac.il "On-Off Local-Con" OR "OOLCS" OR "2611.32927"` returned `no summary returned`; earlier `site:eccc.weizmann.ac.il` checks (`21:03Z`–`21:12Z`) for `Kern`, `Connectivity Switching`, `switch graph`, `matroid switches` returned `0` matching ECCC reports.
5. **Independent Check Execution (`#2018`):**
   - Command: `.venv/bin/python -u targets/kern-2611.32927-oolcs-11connected/notes/check-check-1.py`
   - Exit status: `0`
   - Stdout:
     - `SIZE_WITNESS (n=3, m=2): |V*|=16, |E*|=17`
     - `WLCS_11CONNECTED_EXACT: checked=40, yes=16, no=24, trap=5`
     - `PASS`
