# Gate 3 Novelty Receipt (`watch-1`): `targets/guo-2310.15207-conj6.8/`

- **Checked (UTC):** `2026-11-27T11:22:56Z`
- **Checker:** `watch-1` (snapshot corpus: `653` files)
- **Result:** **PASS** — no prior proof or settlement of Victor J. W. Guo `arXiv:2310.15207v1` §6 Conjecture 6.8 (`conj:8`) found.
- **Audit Target:** `targets/guo-2310.15207-conj6.8/AUDIT.md` (`@audit-3`, `PASS`, label `"written proof, internally audited"`); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "2310.15207" "conj:8"`):**
   - `0` lines across `0/653` files.
2. **arXiv API (`tools/arxiv_fetch.py query --id-list 2310.15207`):**
   - `2310.15207v1` (`2023-10-23T12:51:42Z`) remains sole and latest arXiv version.
3. **Zenodo API (`https://zenodo.org/api/records?q=%222310.15207%22`):**
   - `total: 0`.
4. **GitHub (`gh search issues/prs "2310.15207"`):**
   - `0` issues, `0` PRs.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in arXiv/Zenodo/GitHub/web search are outside direct coverage.
