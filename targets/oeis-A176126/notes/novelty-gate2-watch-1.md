# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A176126/`

- **Checked (UTC):** `2026-11-27T11:24:25Z`
- **Checker:** `watch-1` (snapshot corpus: `653` files)
- **Result:** **PASS** — OEIS `A176126` R. J. Mathar (Dec 12 2010) linear recurrence and generating function remain marked `Conjecture:` with no prior proof found.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A176126"`):**
   - `0` lines across `0/653` files.
2. **Zenodo & Cohen OEIS IDs Indexes (`watch/snapshots/zenodo-23112421-oeis-ids.md`, `zenodo-23114921-oeis-ids.md`, `cohen-zenodo-24384895-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A176126&fmt=json`):**
   - Revision `18`; R. J. Mathar (Dec 12 2010) formula still explicitly marked `Conjecture: a(n) = +3*a(n-1) -6*a(n-2) ... with g.f. (x^4-x^3+3*x^2-x+1)*(x^4-x^3-2*x^2-x+1) / ( (x-1)^3*(x^2+1)^3 ).`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A176126%22`):**
   - `total: 0`.
5. **GitHub (`gh search issues/prs "A176126"`):**
   - `0` issues, `0` PRs.
6. **Web Search (`search_web`):**
   - `"A176126" "Mathar" recurrence OR "generating function" conjecture proof` — no prior proof found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
