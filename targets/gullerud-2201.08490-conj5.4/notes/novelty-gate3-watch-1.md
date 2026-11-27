# Gate 3 Novelty Receipt (`watch-1`): `targets/gullerud-2201.08490-conj5.4/`

- **Checked (UTC):** `2026-11-27T11:17:32Z`
- **Checker:** `watch-1` (snapshot corpus: `651` files)
- **Result:** **PASS** — Gullerud–Johnson–Mbirika `arXiv:2201.08490v3` §5.1 **Conjecture 5.4 (`conj:ellipse`)** remains open and uncontested (strictly scoped away from Conjecture 5.5, whose prior disproofs in `arXiv:2510.02008v1/v2` and `arXiv:2611.21142v1` are cited for context).
- **Audit Target:** `targets/gullerud-2201.08490-conj5.4/AUDIT.md` (`@audit-2`, re-audit `PASS` after `#1030`/`#1058` scoping fixes); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "2201.08490" "conj:ellipse"`):**
   - `0` lines across `0/651` files (`1.22s` combined query).
2. **arXiv API (`tools/arxiv_fetch.py query --id-list 2201.08490`):**
   - `2201.08490v3` (`2023-08-21T19:49:41Z`) remains latest; inspected `arXiv:2510.02008v1` and `arXiv:2611.21142v1` both leave Conjecture 5.4 (`conj:ellipse`) explicitly open.
3. **Zenodo API (`https://zenodo.org/api/records?q=%222201.08490%22`):**
   - `total: 0`.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in arXiv/Zenodo/GitHub/web search are outside direct coverage.
