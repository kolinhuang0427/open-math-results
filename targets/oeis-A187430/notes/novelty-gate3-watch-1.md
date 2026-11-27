# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A187430/`

- **Checked UTC:** `2026-11-27T10:17:06Z`–`2026-11-27T10:17:18Z` (post-`AUDIT.md` PASS)
- **Target:** OEIS `A187430` (rev. 55) — Benedict W. J. Irwin (Jan 13 2017) Catalan g.f. transform conjecture: $1 + \sum_{n\ge 0} a(n)(-1)^n x^{n+1}/(1-x)^{2n+2} = C(x)$ (`A000108`)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "A187430" ...` & `grep zenodo-23112421-oeis-ids.md`):** `0` hits for `A187430` across `618` snapshot files (`1337isnot1337/solved-conjectures`, `trureturing*`, `openai/math`, `formal-conjectures`, `watch/snapshots/discovered/`, and `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **Live OEIS (`https://oeis.org/search?q=id:A187430&fmt=json`):** `ID: 187430`, `rev: 55` (`time: 2024-01-17T09:35:29-05:00`); `FORMULA` still lists `Conjecture: 1 + Sum_{n>=0} a(n)*(-1)^n x^(n+1)/(1-x)^(2*n+2) = C(x)... - _Benedict W. J. Irwin_, Jan 13 2017` with no proof note.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A187430&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "A187430"`):** `0` issues, `0` PRs, `0` repos.
5. **Web search (Gate 2 `10:13Z`):** `"A187430" "Irwin" OR "Catalan" OR "proved"` returned only OEIS `A187430` (`Conjecture`) and `arXiv:1609.06473`.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot was last synced at `2026-11-27T09:50:27Z` (Sweep 25, ~27 min before this check); live `gh search` at `10:17Z` found no GitHub hits.
