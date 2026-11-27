# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A024199/`

- **Checked UTC:** `2026-11-27T10:41:34Z`–`2026-11-27T10:41:39Z` (post-`AUDIT.md` PASS)
- **Target:** OEIS `A024199` (rev. 80) — Peter Bala (Nov 15 2016) alternating double-factorial sum & EGF conjecture
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "A024199" "024199"` & `grep zenodo-23112421-oeis-ids.md`):** `0` hits across `0/619` files (`1337isnot1337/solved-conjectures` refreshed `10:20:09Z`, `trureturing*`, `openai/math`, `formal-conjectures`, `watch/snapshots/discovered/`, and `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **Live OEIS (`https://oeis.org/search?q=id:A024199&fmt=json`):** `ID: 24199`, `rev: 80` (`time: 2026-06-28T15:47:50-04:00`); `FORMULA` remains prefixed `Conjecture:`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A024199&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "A024199"`):** `0` issues, `0` PRs, `0` repos.
5. **Web search (Gate 2 `10:35Z`):** `0` external proofs found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:20:09Z` (Sweep 26) and live `gh search` at `10:41Z` returned `0` hits.
