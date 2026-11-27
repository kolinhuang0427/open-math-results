# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A123145/`

- **Checked UTC:** `2026-11-27T10:45:31Z`–`2026-11-27T10:45:42Z`
- **Target:** OEIS `A123145` (rev. 31) — Sergei N. Gladkovskii (Nov 26 2012) 5-step continued fraction EGF conjecture: $E(x) = \frac{d}{dx} G(0)$
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "A123145" "123145" "Gladkovskii"` & `grep zenodo-23112421-oeis-ids.md`):** `0` hits for `A123145`/`123145` across `619` files (`insorrowmeow__oeis-sequence-proofs.json:240` `Gladkovskii` match is `A048625` only), and absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`.
2. **Live OEIS (`https://oeis.org/search?q=id:A123145&fmt=json`):** `ID: 123145`, `rev: 31` (`time: 2023-07-16T16:56:53-04:00`); `FORMULA` remains prefixed `Conjecture:`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A123145&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "A123145"`):** `0` issues, `0` PRs, `0` repos.
5. **Web search (`"A123145" "Gladkovskii" OR "continued fraction" OR "conjecture"`):** `0` external proofs of `A123145` found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:20:09Z` (Sweep 26) and live `gh search` at `10:45Z` returned `0` hits.
