# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A158960/`

- **Checked UTC:** `2026-11-27T10:17:06Z`–`2026-11-27T10:17:18Z`
- **Target:** OEIS `A158960` (rev. 28) — M. F. Hasler (Feb 16 2014) conjecture that the reduced denominator of $\mathrm{Hermite}(n, 1/5)$ is $5^n = \mathrm{A000351}(n)$ for all $n \ge 0$
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "A158960" "158960" "Hasler" "Hermite(n, 1/5)"` & `grep zenodo-23112421-oeis-ids.md`):** `0` hits for `A158960`, `158960`, or `Hermite(n, 1/5)` across `618` snapshot files (`13` lines across `6` files were all unrelated M. F. Hasler entries: `hasler_2024_sums_distinct_powers_3_4`, `A260407`, `A359482`, `A267681`, `A377090`, `A300326`, `A133509`), and absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`.
2. **Live OEIS (`https://oeis.org/search?q=id:A158960&fmt=json`):** `ID: 158960`, `rev: 28` (`time: 2022-09-08T08:45:43-04:00`); `COMMENTS` still reads `The denominators are 5^n = A000351(n) (conjectured). - _M. F. Hasler_, Feb 16 2014`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A158960&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "A158960"`):** Only unrelated issue `sharpemu/sharpemu #618`; `0` PRs and `0` repos.
5. **Web search (`"A158960" "Hasler" OR "Hermite" OR "conjecture"`):** `0` proofs of Hasler's `A158960` denominator conjecture found (only unrelated legal docket `A158960` and unrelated Hasler papers).

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot was last synced at `2026-11-27T09:50:27Z` (Sweep 25, ~27 min before this check); live `gh search` at `10:17Z` found no math/OEIS hits.
