# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A119262/`

- **Checked UTC:** `2026-11-27T10:26:10Z`–`2026-11-27T10:26:26Z`
- **Target:** OEIS `A119262` (rev. 55) — Benedict W. J. Irwin (Apr 19 2017) Hessenberg determinant conjecture: $a(n+1) = \det(M_n)$ for all $n \ge 1$
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "A119262" "119262"` & `grep zenodo-23112421-oeis-ids.md`):** `0` hits across `0/618` files (`1337isnot1337/solved-conjectures` refreshed `10:20:09Z`, `trureturing*`, `openai/math`, `formal-conjectures`, `watch/snapshots/discovered/`, and `watch/snapshots/zenodo-23112421-oeis-ids.md`). (Separate `Hessenberg` / `Irwin` sweep hits in `facebookresearch/atlas-lean` are ternary Fuss–Catalan / general Hessenberg files, unrelated to `A119262`.)
2. **Live OEIS (`https://oeis.org/search?q=id:A119262&fmt=json`):** `ID: 119262`, `rev: 55` (`time: 2026-02-23T22:55:40-05:00`); `FORMULA` still prefixes Irwin's formula with `Conjecture:`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A119262&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "A119262"`):** Only unrelated `DigitalKhatt/visualmeta... #3`; `0` PRs and `0` repos.
5. **Web search (`"A119262" "Irwin" OR "Hessenberg" OR "determinant" OR "conjecture"`):** `0` proofs of Irwin's `A119262` determinant conjecture found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:20:09Z` (Sweep 26) and live `gh search issues/prs/repos` at `10:26Z` returned no math/OEIS matches.
