# Gate 2 Novelty Receipt — `targets/dochtermann-2609.13361-conj7.5/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T12:01Z`
- **Target:** Anton Dochtermann, Evan Huang, Kai Mawhinney, Suho Oh, Yuchen Xu (`arXiv:2609.13361v1`, `2026-09-11`), Section 7 **Conjecture 7.5** (`\label{conj:C>=3 ind}`, implying Conjecture 7.4 `\label{conj:unique}`).
- **Verdict:** **PASS** (`0` prior proofs found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`690` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 29, `insorrowmeow/oeis-sequence-proofs`, Zenodo compendia, & `mylesparslow` ledger):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2609.13361" "2509.11460" "2609.17446" "Dochtermann" "circuit system" "conj:C>=3 ind"` -> `6` lines across `2/690` files:
     - `watch/snapshots/1337-solved-conjectures/open_issues_claims.md:606` (`#336` [open] Stanley's pure $O$-sequence conjecture, citing `2509.11460` and `2609.17446` as background only).
     - `watch/snapshots/discovered/tamnd__arxiv.json` (arXiv metadata/census index for `2609.13361v1` only).
2. **Live arXiv API (`12:00Z`):**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2609.13361,2509.11460,2609.17446`:
     - `2609.13361v1` (`2026-09-11`) and `2509.11460v1` (`2025-09-14`) remain sole versions.
     - `2609.17446v2` (SuHo Oh, *Relaxed coparking functions and Stanley's conjecture for matroid $h$-vectors*, `2026-09-19`) studies relaxed coparking / fibre systems for Stanley's conjecture; does not address `conj:C>=3 ind` or `conj:unique`.
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"circuit system" AND all:"matroid"'` -> `total_results: 0`.
3. **Live Zenodo, GitHub, & Web Search:**
   - `curl -s "https://zenodo.org/api/records?q=2609.13361&size=3"` -> `0` hits (broad `circuit+system+matroid` hits are unquoted keyword matches).
   - `gh search issues`/`prs` for `"2609.13361"` and `"circuit system" matroid` -> `0` hits each.
   - `search_web` (`"2609.13361" OR "Matroids with cycle systems are regular" "Conjecture 7.5" OR "Conjecture 7.4" OR "circuit system" proof`) -> returns only `2609.13361v1` itself; no settlement of Conjecture 7.4 or 7.5 found.

## Near-Misses & Coverage Limits
- **Near-misses:** `arXiv:2609.17446v2` (SuHo Oh, relaxed coparking functions for Stanley's conjecture) and `1337isnot1337/solved-conjectures#336` (open Stanley pure $O$-sequence issue).
- **Coverage limits:** Private repositories and works without `2609.13361`, `Dochtermann`, or `circuit system` identifiers are not covered.
