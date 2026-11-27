# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A178072/`

- **Checked (UTC):** `2026-11-27T11:21:23Z`
- **Checker:** `watch-1` (snapshot corpus: `652` files)
- **Result:** **PASS** — OEIS `A178072` R. J. Mathar (Jun 14 2016) 7-term linear recurrence remains marked `Conjecture:` with no prior proof found.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A178072"`):**
   - `0` lines across `0/652` files (`0.84s` combined query).
2. **Zenodo & Cohen OEIS IDs Indexes (`watch/snapshots/zenodo-23112421-oeis-ids.md`, `zenodo-23114921-oeis-ids.md`, `cohen-zenodo-24384895-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A178072&fmt=json`):**
   - Revision `35`; R. J. Mathar (Jun 14 2016) formula still explicitly marked `Conjecture: 2*n*(n+1)*a(n) +2*n*(n+1)*a(n-1) ... +(5*n-1)*(n-6)*a(n-7)=0.`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A178072%22`):**
   - `total: 0`.
5. **GitHub (`gh search issues/prs "A178072"`):**
   - `0` issues; only unrelated dependency bump PRs (commit hash/ID substring match).
6. **Web Search (`search_web`):**
   - `"A178072" "Mathar" recurrence conjecture proof` — references only OEIS `A178072` and general holonomic methodology; no prior proof found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
