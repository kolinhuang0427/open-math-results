# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A400812/`

- **Checked (UTC):** `2026-11-27T11:12:32Z`
- **Checker:** `watch-1` (snapshot corpus: `651` files)
- **Result:** **PASS** — OEIS `A400812` / `A400813` / `A400814` (Boris K. Horvat) Spectre star-triple recurrence, generating function, `A057080`/`A099919` identity, and $4-\sqrt{15}$ asymptotic limit conjectures remain unproved (`Conjecture:` / `Conjectured g.f.:`).
- **Audit Target:** `targets/oeis-A400812/AUDIT.md` (`@audit-1`, re-audit `PASS` after `#975`/`#992` fixes); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A400812" "A400813" "A400814"`):**
   - `0` lines across `0/651` files (`1.59s` combined query).
2. **Zenodo OEIS IDs Indexes (`watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`A400812` rev. `50`, `A400813` rev. `19`, `A400814` rev. `19`):**
   - All four conjectures on `A400812` and the recurrence / conjectured g.f. entries on `A400813` and `A400814` remain explicitly marked `Conjecture:` / `Conjectured g.f.:` (`not proven`).
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A400812%22`):**
   - `total: 0`.
5. **GitHub (`gh search issues/prs "A400812"`):**
   - `0` PRs; `1` unrelated issue (`georchestra/cadastrapp#329`, ID substring match).
6. **Web Search (`search_web`):**
   - `"A400812" OR "A400813" OR "A400814" "Spectre" conjecture proof OR recurrence` — references only the OEIS pages (`A400812`–`A400814`) and `arXiv:2305.17743`; no prior proof found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
