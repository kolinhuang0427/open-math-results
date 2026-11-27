# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A127276/`

- **Checked (UTC):** `2026-11-27T11:22:56Z`
- **Checker:** `watch-1` (snapshot corpus: `653` files)
- **Result:** **PASS** — OEIS `A127276` R. J. Mathar (Dec 11 2010) closed form and conjectured g.f. remain marked `Conjectured g.f.:` with no prior proof found.
- **Audit Target:** `targets/oeis-A127276/AUDIT.md` (`@audit-1`, `PASS`, label `"written proof, internally audited"`); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A127276"`):**
   - `0` lines across `0/653` files.
2. **Zenodo & Cohen OEIS IDs Indexes (`watch/snapshots/zenodo-23112421-oeis-ids.md`, `zenodo-23114921-oeis-ids.md`, `cohen-zenodo-24384895-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A127276&fmt=json`):**
   - Revision `33` (unchanged); formula still explicitly marked `Conjectured g.f.: -(4*x-1)*(x-1) / ( (2*x-1)^3 ) and a(n) = 2^n-n*(n+1)*2^(n-2).`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A127276%22`):**
   - `total: 0`.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
