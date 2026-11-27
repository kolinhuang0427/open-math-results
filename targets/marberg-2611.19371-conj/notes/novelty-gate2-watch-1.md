# Gate 2 Novelty Receipt (`watch-1`): `targets/marberg-2611.19371-conj/`

- **Checked (UTC):** `2026-11-27T11:04:38Z`
- **Checker:** `watch-1` (snapshot corpus: `651` files)
- **Result:** **PASS** — no prior proof or resolution of Marberg–Morales–Yu `arXiv:2611.19371v1` §3.3 Conjecture 3.8 (`\label{iG-conj}`) found.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "2611.19371" "iG-conj" "kInvBPD"`):**
   - `13` lines across `5/651` files (`1.84s`): `watch/snapshots/arxiv/{arxiv_submissions.json,arxiv_submissions.md,last_sweep_report.json,state.json}` (indexing `2611.19371v1` itself) plus unrelated `mt0-svg__adversarial-bco.json` (`config-conj1...`). `0` settlement hits.
2. **arXiv API (`tools/arxiv_fetch.py query --id-list ...2611.19371...`):**
   - `2611.19371v1` (`2026-11-14T12:23:48Z`) remains the sole and latest arXiv version.
3. **Zenodo API (`https://zenodo.org/api/records?q=%222611.19371%22`):**
   - `total: 0`.
4. **GitHub (`gh search issues/prs "2611.19371"`):**
   - `0` issues, `0` PRs.
5. **Web Search (`search_web`):**
   - `"2611.19371" OR "Marberg" "Conjecture 3.8" OR "iG-conj" proof` — references only `arXiv:2611.19371v1` itself; no prior proof found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in arXiv/Zenodo/GitHub/web search are outside direct coverage.
