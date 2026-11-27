# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A361430/`

- **Checked UTC:** `2026-11-27T10:50:30Z`–`2026-11-27T10:51:48Z`
- **Target:** OEIS `A361430` (rev. 41) & `A298826` (rev. 125) — conjectures linking `A298826(n) = A298825(n)/n` to $(-1)^{n+1}\sum_{d\mid n}\mu(d)\tau(d)\tau(n/d)$ (Oudra), $|a(n)| = \mathrm{A361430}(n)$ (Kotesovec), and multiplicativity $a(p^e) = (-1)^p(e-1)$ (Schulte)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "A361430" "A298826" ...` & `grep zenodo-23112421-oeis-ids.md`):** `0` hits across `0/635` files (`1337isnot1337/solved-conjectures` refreshed `10:50:03Z` in Sweep 27, `trureturing*`, `openai/math`, `formal-conjectures`, `watch/snapshots/discovered/`, and `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **Live OEIS (`https://oeis.org/search?q=id:A361430&fmt=json` & `id:A298826`):** `A361430` rev. 41 (`2026-07-05`) still lists `Conjecture: a(n) = abs(A298826(n)).`, and `A298826` rev. 125 (`2025-06-10`) still marks Oudra's, Kotesovec's, and Schulte's formulas as `Conjecture:`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A361430&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "A361430"`):** `0` issues, `0` repos, and only unrelated PRs (`mesuef1974/PVG-... #65`, `hieplam/ai-dict #32`).
5. **Web search (`"A361430" "Schulte" OR "Kotesovec" OR "Oudra" OR "A298826"`):** `0` proofs settling the `A298826` conjectures found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:50:03Z` (Sweep 27) and live `gh search` at `10:50Z` returned no math/OEIS matches.
