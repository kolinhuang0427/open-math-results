# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A127276/`

- **Checked (UTC):** `2026-11-27T11:17:32Z`
- **Checker:** `watch-1` (snapshot corpus: `651` files)
- **Result:** **PASS** — OEIS `A127276` R. J. Mathar (Dec 11 2010) conjectured g.f. `-(4*x-1)*(x-1)/((2*x-1)^3)` and closed form `a(n) = 2^n - n*(n+1)*2^(n-2)` remain marked `Conjectured g.f.:` with no prior proof found.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A127276"`):**
   - `0` lines across `0/651` files (`1.22s` combined query).
2. **Zenodo OEIS IDs Indexes (`watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A127276&fmt=json`):**
   - Revision `33`; R. J. Mathar (Dec 11 2010) formula still explicitly marked `Conjectured g.f.: -(4*x-1)*(x-1) / ( (2*x-1)^3 ) and a(n) = 2^n-n*(n+1)*2^(n-2).`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A127276%22`):**
   - `total: 0`.
5. **GitHub (`gh search issues/prs "A127276"`):**
   - `0` issues; `1` unrelated PR (`NavHur/slopsubs#63`, commit/ID substring match).
6. **Web Search (`search_web`):**
   - `"A127276" "Mathar" OR "2^n - n*(n+1)*2^(n-2)" conjecture proof` — no prior proof found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
