# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A028495/`

- **Checked UTC:** `2026-11-27T10:49:27Z`–`2026-11-27T10:49:40Z`
- **Target:** OEIS `A028495` (rev. 162) — Bill McEachen (Feb 11 2026) asymptotic ratio conjectures: $a(n)/a(n-1) \to 2\cos(\pi/7) = \sqrt{2 + 2\cos(2\pi/7)}$
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... "A028495" "028495" "McEachen"` & `grep zenodo-23112421-oeis-ids.md`):** `0` hits for `A028495` across `635` files (`McEachen` hits in `IvanGrigin`, `senamakel`, `umaia1234` are `A362086`, `McEachenDensity/Stock`, and `A135508`; `028495` was a SHA-256 hex substring), and absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`.
2. **Live OEIS (`https://oeis.org/search?q=id:A028495&fmt=json`):** `ID: 28495`, `rev: 162` (`time: 2026-10-28T21:52:26-04:00`); `FORMULA` remains `Conjectures: a(n) ~ A160389 * a(n-1). Also a(n) ~ sqrt(A116425)*a(n-1).`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A028495&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "A028495"`):** `0` issues, `0` PRs, `0` repos.
5. **Web search (`... OR ("A028495" "McEachen") OR ("A028495" "2*cos(Pi/7)")`):** `0` external proofs of McEachen's `A028495` asymptotic conjectures found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:20:09Z` (Sweep 26; Sweep 27 running concurrently) and live `gh search` at `10:49Z` returned `0` hits.
