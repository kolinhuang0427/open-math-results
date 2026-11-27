# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A188458/`

- **Checked (UTC):** `2026-11-27T11:12:32Z`
- **Checker:** `watch-1` (snapshot corpus: `651` files)
- **Result:** **PASS** — OEIS `A188458` Gladkovskii (Nov 12 2013) continued fraction formula $T(0)/(1-x)$ remains marked `conjecture` with no prior proof found.
- **Audit Target:** `targets/oeis-A188458/AUDIT.md` (`@audit-3`, `PASS`, label `"written proof, internally audited"`); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A188458"`):**
   - `0` lines across `0/651` files (`1.59s` combined query).
2. **Zenodo OEIS IDs Indexes (`watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A188458&fmt=json`):**
   - Revision `54` (unchanged); Sergei N. Gladkovskii (Nov 12 2013) formula still explicitly marked `G.f.: conjecture T(0)/(1-x)...`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A188458%22`):**
   - `total: 0`.
5. **GitHub (`gh search issues/prs "A188458"`):**
   - `0` issues, `0` PRs.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
