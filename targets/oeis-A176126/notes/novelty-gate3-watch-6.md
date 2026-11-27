# Gate 3 Novelty Check (`watch-6`): `targets/oeis-A176126/`

- **Checked UTC:** `2026-11-27T11:34:38Z`
- **Target:** OEIS `A176126` (`rev. 18`, `2022-08-27T03:13:41-04:00`) — R. J. Mathar's Dec 12 2010 g.f. and 9-term recurrence ($n \ge 9$) for the numerator of `-A127276(n)/A001788(n)`.
- **Verdict:** **PASS** (<1h freshness confirmed; no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py A176126 176126 A183063 183063 A157002 157002` -> `0` hits for `A176126`/`176126`.
2. **Live OEIS JSON (`11:24:50Z`):**
   - `A176126` `rev: 18` (`2022-08-27T03:13:41-04:00`), Mathar's Dec 12 2010 recurrence and g.f. remain labeled `Conjecture:`.
3. **Zenodo API (`A176126`):** `hits.total: 0`.
4. **arXiv metadata API (`all:A176126`):** `total_results: 0`.
5. **GitHub search (`gh search repos/issues A176126`):** `[]`.

## Coverage Limits

- `A176126` live OEIS/Zenodo/arXiv/GitHub API checks ran `~10` minutes prior (`11:24:50Z`), with the `658`-file snapshot grep (including all newly indexed 2026 compendia) refreshed at `11:34:38Z`.
