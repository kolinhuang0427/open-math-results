# Gate 3 Novelty Receipt (`watch-6`) — `targets/oeis-A119366/`

- **Checked UTC:** `2026-11-27T09:27:39Z` (`<1h` before submission)
- **Target:** OEIS `A119366` — R. J. Mathar's Feb 03 2025 conjectured 7th-order D-finite recurrence ($n \ge 7$)
- **Verdict:** **PASS**

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "A119366"`: `0` lines across `0/608` snapshot files.
- `gh search repos "A119366" --limit 5 --json fullName,url`: `[]`
- `gh search issues "A119366" --limit 10 --json repository,number,title,state,url`: `[]`
- `gh search code "A119366" --limit 5 --json repository,path,url`: hits `loda-lang/loda-programs`, `africamonkey/OEIS-Spider`, `AdguardTeam/FiltersRegistry`, and `Anon52MI4/oeis-alien/run1/exp134-chk/names.md` (inspected via `gh api`: plain OEIS ID + sequence name line only, `0` proofs).
- Live OEIS JSON (`https://oeis.org/search?q=id:A119366&fmt=json`): still marked `Conjecture D-finite with recurrence ...` (`audit-2` verified rev. 7).
- Zenodo API (`https://zenodo.org/api/records?q=A119366&size=5`): `0` records.
- `search_web` (`09:24Z`) & arXiv API (`09:24Z`): `0` proofs found.

## Coverage Limits
- Closed-access venues or private repositories not indexed by arXiv, GitHub, OEIS, Zenodo, or `search_web` are not covered.
