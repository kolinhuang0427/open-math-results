# Gate 2 Novelty Receipt (`watch-1`): `targets/guo-2310.15207-conj6.8/`

- **Checked (UTC):** `2026-11-27T11:01:08Z`
- **Checker:** `watch-1` (post-Sweep 27 snapshot corpus: `636` files)
- **Result:** **PASS** — no prior proof or resolution of Victor J. W. Guo `arXiv:2310.15207v1` §6 Conjecture 6.8 (`conj:8`) found.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "2310.15207" "conj:8" "Conjecture 6.8" "Dwork-type"`):**
   - `0` lines across `0/636` files (`1.39s`).
2. **arXiv API (`tools/arxiv_fetch.py query --id-list 2310.15207`):**
   - `2310.15207v1` (`2023-10-23T12:51:42Z`) remains the sole and latest arXiv version.
3. **Zenodo API (`https://zenodo.org/api/records?q=%222310.15207%22`):**
   - `total: 0`.
4. **GitHub (`gh search issues/prs "2310.15207"`):**
   - `0` issues, `0` PRs.
5. **Semantic Scholar (`https://api.semanticscholar.org/graph/v1/paper/arXiv:2310.15207?...`):**
   - Returned `HTTP 429` rate limit during this check; previously inspected by `watch-5` (`#899`) confirming all `3` S2 citing papers of `2310.15207v1` / `10.1007/s13398-025-01762-9` are distinct from `conj:4`/`conj:8`.
6. **Web Search (`search_web`):**
   - `"2310.15207" "Conjecture 6.8" OR "Victor J. W. Guo" "Dwork-type" supercongruences proof` — cites `arXiv:2310.15207v1` itself and Guo–Zudilin (2021); no subsequent proof of Conjecture 6.8 found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Live Semantic Scholar API returned `HTTP 429` during this check (`watch-5` `#899` already inspected the 3 citing works); paywalled journals not indexed in arXiv/Zenodo/GitHub/web search are outside direct coverage.
