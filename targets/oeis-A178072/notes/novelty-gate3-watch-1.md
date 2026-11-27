# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A178072/`

- **Checked (UTC):** `2026-11-27T11:24:25Z`
- **Checker:** `watch-1` (snapshot corpus: `653` files)
- **Result:** **PASS** — OEIS `A178072` R. J. Mathar (Jun 14 2016) 7-term linear recurrence remains marked `Conjecture:` with no prior proof found.
- **Audit Target:** `targets/oeis-A178072/AUDIT.md` (`@audit-1`, `PASS`, label `"written proof, internally audited"`); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A178072"`):**
   - `0` lines across `0/653` files.
2. **Zenodo & Cohen OEIS IDs Indexes (`watch/snapshots/zenodo-23112421-oeis-ids.md`, `zenodo-23114921-oeis-ids.md`, `cohen-zenodo-24384895-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A178072&fmt=json`):**
   - Revision `35` (unchanged); R. J. Mathar (Jun 14 2016) formula still explicitly marked `Conjecture: 2*n*(n+1)*a(n) +2*n*(n+1)*a(n-1) ... +(5*n-1)*(n-6)*a(n-7)=0.`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A178072%22`):**
   - `total: 0`.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
