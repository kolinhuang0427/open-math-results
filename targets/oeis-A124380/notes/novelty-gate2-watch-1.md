# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A124380/`

- **Checked (UTC):** `2026-11-27T11:04:38Z`
- **Checker:** `watch-1` (snapshot corpus: `651` files)
- **Result:** **PASS** — OEIS `A124380` Kotesovec (Sep 18 2024) logarithmic asymptotic conjecture remains marked `Conjecture:` with no prior proof found.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A124380"`):**
   - `0` lines across `0/651` files (`0.93s`).
2. **Zenodo OEIS IDs Indexes (`watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A124380&fmt=json`):**
   - Revision `39`; Vaclav Kotesovec (Sep 18 2024) formula still explicitly marked `Conjecture: log(a(n)) ~ n*log(n)/2 - n*(1 + log(2))/2.`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A124380%22`):**
   - `total: 0`.
5. **GitHub (`gh search issues/prs "A124380"`):**
   - `0` issues, `0` PRs.
6. **Web Search (`search_web`):**
   - `"A124380" "Kotesovec" asymptotic OR proof` — no prior proof found for `A124380`.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
