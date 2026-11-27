# Gate 3 Novelty Receipt (`watch-6`) — `targets/oeis-A168452/`

- **Checked UTC:** `2026-11-27T09:26:26Z` (`<1h` before submission)
- **Target:** OEIS `A168452` — R. J. Mathar's Nov 22 2024 conjectured 4th-order D-finite recurrence ($n \ge 4$)
- **Verdict:** **PASS**

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "A168452"`: `0` lines across `0/608` snapshot files.
- `gh search repos "A168452" --limit 5 --json fullName,url`: `[]`
- `gh search issues "A168452" --limit 10 --json repository,number,title,state,url`: `[]`
- `gh search code "A168452" --limit 5 --json repository,path,url`: hits only `archmageirvine/joeis`, `loda-lang/loda-programs`, `africamonkey/OEIS-Spider`, and `AdguardTeam/FiltersRegistry` (`0` proofs).
- Live OEIS JSON (`https://oeis.org/search?q=id:A168452&fmt=json`): still marked `Conjecture D-finite with recurrence ...` (`audit-3` verified rev. 14).
- Zenodo API (`https://zenodo.org/api/records?q=A168452&size=5`): `0` records.
- `search_web` (`09:22Z`) & arXiv API (`09:22Z`): `0` proofs found.

## Coverage Limits
- Closed-access venues or private repositories not indexed by arXiv, GitHub, OEIS, Zenodo, or `search_web` are not covered.
