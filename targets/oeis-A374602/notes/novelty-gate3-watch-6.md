# Gate 3 Novelty Check (`watch-6`): `targets/oeis-A374602/`

- **Checked UTC:** `2026-11-27T11:28:17Z` (cross-checked against `657` snapshots at `11:32Z`)
- **Target:** OEIS `A374602` (`rev. 31`, `2024-11-15T23:31:14-05:00`) / `A377290` (`rev. 7`) / `A377291` (`rev. 7`) — Kurkov's conjecture on periodicity and closed-form linear recurrence of rows of `A374602`.
- **Verdict:** **PASS** (<1h freshness confirmed; no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (657 files incl. Su `24366920`/`23760779`, `mylesparslow-collab`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, 2026 Zenodo compendia):**
   - `.venv/bin/python -u tools/novelty_grep.py A374602 374602 A377290 377290 A377291 377291` -> `# 0 lines across 0/653 files in 1.68s`, and `0` hits in the newly indexed `mylesparslow-conjecture-ledger.md`, `su-zenodo-24366920-oeis-ids.md`, `su-zenodo-23760779-oeis-ids.md`, and `zenodo-2026-oeis-compendia-ids.md`.
2. **Live OEIS JSON (`https://oeis.org/search?q=id:A374602&fmt=json`):**
   - `rev: 31`, `time: 2024-11-15T23:31:14-05:00`; status unchanged.
3. **Zenodo API (`https://zenodo.org/api/records?q=A374602`):**
   - `hits.total: 0`.
4. **arXiv metadata API (`.venv/bin/python -u tools/arxiv_fetch.py query "all:A374602"`):**
   - `total_results: 0`.
5. **GitHub search (`gh search repos A374602 --limit 5`, `gh search issues A374602 --limit 5`):**
   - `[]` (repos) and `[]` (issues).

## Coverage Limits

- arXiv query covers metadata rather than PDF full text; offline or unindexed manuscripts are outside direct visibility.
