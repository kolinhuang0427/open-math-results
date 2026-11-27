# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A237757/`

- **Checked UTC:** `2026-11-27T10:51:48Z`–`2026-11-27T10:51:55Z` (post-`AUDIT.md` PASS)
- **Target:** OEIS `A237757` (rev. 17) — Peter Bala (Feb 02 2021) conjectured g.f. $\sum_{n \ge 0} q^{2(n+1)^2}/\prod_{k=1}^{2n+1}(1 - q^k)$
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "A237757" "237757"` & `grep zenodo-23112421-oeis-ids.md`):** `0` hits across `0/635` files (`1337isnot1337/solved-conjectures` refreshed `10:50:03Z` in Sweep 27, `trureturing*`, `openai/math`, `formal-conjectures`, `watch/snapshots/discovered/`, and `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **Live OEIS (`https://oeis.org/search?q=id:A237757&fmt=json`):** `ID: 237757`, `rev: 17` (`time: 2022-01-22T07:31:08-05:00`); `FORMULA` remains `Conjectural g.f.: ...`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A237757&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "A237757"`):** `0` issues, `0` repos, and only unrelated PR `neams-th-coe/cardinal #834`.
5. **Web search (Gate 2 `10:47Z`):** `0` external proofs found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:50:03Z` (Sweep 27) and live `gh search` at `10:51Z` returned no math/OEIS matches.
