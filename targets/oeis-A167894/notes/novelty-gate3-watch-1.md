# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A167894/`

- **Checked (UTC):** `2026-11-27T11:22:56Z`
- **Checker:** `watch-1` (snapshot corpus: `653` files)
- **Result:** **PASS** — OEIS `A167894` Gladkovskii (Nov 19 2013) continued fraction formula $Q(0)$ remains marked `conjecture:` with no prior proof found.
- **Audit Target:** `targets/oeis-A167894/AUDIT.md` (`@audit-3`, re-audit `PASS` after `#1046` L27 fix, label `"written proof, internally audited"`); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A167894"`):**
   - `0` lines across `0/653` files.
2. **Zenodo & Cohen OEIS IDs Indexes (`watch/snapshots/zenodo-23112421-oeis-ids.md`, `zenodo-23114921-oeis-ids.md`, `cohen-zenodo-24384895-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A167894&fmt=json`):**
   - Revision `83` (unchanged); Gladkovskii formula still explicitly marked `G.f.: conjecture: Q(0), where Q(k) = 1 + k*x - (k+1)*x/Q(k+1).`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A167894%22`):**
   - `total: 0`.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
