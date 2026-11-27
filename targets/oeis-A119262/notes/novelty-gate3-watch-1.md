# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A119262/`

- **Checked UTC:** `2026-11-27T10:30:53Z`–`2026-11-27T10:31:15Z` (post-`AUDIT.md` PASS)
- **Target:** OEIS `A119262` (rev. 55) — Benedict W. J. Irwin (Apr 19 2017) Hessenberg determinant conjecture $\det(M_n) = a(n+1)$ for all $n \ge 1$
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "A119262" "119262"`):** `0` hits across `0/619` files (`1337isnot1337/solved-conjectures` refreshed `10:20:09Z`, `trureturing*`, `openai/math`, `formal-conjectures`, `watch/snapshots/discovered/`, `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **Live OEIS (`https://oeis.org/search?q=id:A119262&fmt=json`):** `ID: 119262`, `rev: 55` (`time: 2026-02-23T22:55:40-05:00`); `FORMULA` remains prefixed `Conjecture:`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A119262&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "A119262"`):** Only unrelated `DigitalKhatt/visualmeta... #3`; `0` PRs and `0` repos.
5. **Web search (Gate 2 `10:26Z`):** `0` external proofs found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:20:09Z` (Sweep 26) and live `gh search` at `10:31Z` returned no math/OEIS matches.
