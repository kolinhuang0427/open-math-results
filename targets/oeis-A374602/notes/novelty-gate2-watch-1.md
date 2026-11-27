# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A374602/`

- **Checked (UTC):** `2026-11-27T11:05:43Z`
- **Checker:** `watch-1` (snapshot corpus: `651` files)
- **Result:** **PASS** — OEIS `A374602` (Hohn, rev. 31) subsequence periodicity and growth-factor algorithm conjectures (`A377290`, `A377291`) remain marked `conjectured ... not proven` with no prior proof found.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A374602" "A377290" "A377291"`):**
   - `0` lines across `0/651` files (`1.64s`).
2. **Zenodo OEIS IDs Indexes (`watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`):**
   - `0` matches for `A374602`, `A377290`, `A377291`.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A374602&fmt=json`):**
   - Revision `31`; comment still explicitly states *"it is conjectured that this is the case for all n, and that all solutions conform as such and that there are no solutions that do not, but these are not proven."* and *"It is also not known if there is an algorithm for generating values for all rows..."*.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A374602%22`):**
   - `total: 0`.
5. **GitHub (`gh search issues/prs "A374602"`):**
   - `0` issues, `0` PRs.
6. **Web Search (`search_web`):**
   - `"A374602" OR "A377290" OR "A377291" conjecture proof OR Pell` — references only the OEIS entries; no prior universal proof or algorithm found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
