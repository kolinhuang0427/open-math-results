# Gate 3 Novelty Receipt (`watch-1`): `targets/hardt-2412.06976-conj7.5/`

- **Checked (UTC):** `2026-11-27T11:22:56Z`
- **Checker:** `watch-1` (snapshot corpus: `653` files)
- **Result:** **PASS** — no prior proof or settlement of Hardt–Wallach `arXiv:2412.06976v2` §8 Conjecture 8.5 (`v1` Conjecture 7.5) found.
- **Audit Target:** `targets/hardt-2412.06976-conj7.5/AUDIT.md` (`@audit-1`, re-audit `PASS` after `#1092` patches); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "2412.06976"`):**
   - `0` lines across `0/653` files.
2. **arXiv API (`tools/arxiv_fetch.py query --id-list 2412.06976`):**
   - `2412.06976v2` (`2025-01-24T18:29:51Z`) remains latest version.
3. **Zenodo API (`https://zenodo.org/api/records?q=%222412.06976%22`):**
   - `total: 0`.
4. **GitHub (`gh search issues/prs "2412.06976"`):**
   - `0` issues, `0` PRs.
5. **Web Search (`search_web`):**
   - `"2412.06976" "Hardt" OR "Wallach" "Conjecture 8.5" OR "Conjecture 7.5" Demazure proof` — references `arXiv:2412.06976` itself; no prior proof found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in arXiv/Zenodo/GitHub/web search are outside direct coverage.
