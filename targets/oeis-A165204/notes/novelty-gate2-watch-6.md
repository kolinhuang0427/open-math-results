# Gate 2 Novelty Check (`watch-6`): `targets/oeis-A165204/`

- **Checked UTC:** `2026-11-27T11:30:00Z`
- **Target:** OEIS `A165204` (`rev. 15`, `2018-02-15T20:46:11-05:00`) — Colin Barker's Feb 10 2018 conjectured g.f. `(1 - 8*x + 2*x^2 - x^3) / (1 - 3*x + 8*x^2 - 3*x^3 + x^4)` and 4-term recurrence (`n > 3`) for Hankel transform of `A165203`.
- **Verdict:** **PASS** (no prior settlement found)

## Exact Queries & Results

1. **Snapshot grep (657 files incl. Su `24366920`/`23760779`, `mylesparslow-collab`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, 2026 Zenodo compendia):**
   - `.venv/bin/python -u tools/novelty_grep.py A165204 165204` -> `# 0 lines across 0/653 files in 0.51s`, and `0` hits in `mylesparslow-conjecture-ledger.md`, `su-zenodo-24366920-oeis-ids.md`, `su-zenodo-23760779-oeis-ids.md`, and `zenodo-2026-oeis-compendia-ids.md`.
2. **Live OEIS JSON (`https://oeis.org/search?q=id:A165204&fmt=json`):**
   - `rev: 15`, `time: 2018-02-15T20:46:11-05:00`; Barker's g.f. and 4-term recurrence remain labeled `Conjectures from _Colin Barker_, Feb 10 2018`.
3. **arXiv metadata API (`.venv/bin/python -u tools/arxiv_fetch.py query "all:A165204"`):**
   - `total_results: 0`.
4. **Zenodo API (`https://zenodo.org/api/records?q=A165204`):**
   - `hits.total: 0`.
5. **GitHub search (`gh search repos A165204 --limit 5`, `gh search issues A165204 --limit 5`):**
   - `[]` (repos) and `[]` (issues).
6. **Web search (`search_web` for `"A165204" Barker Hankel proof`):**
   - Grounding cited Zenodo `24414721` (Ma & Zhang, `2026-11-21`, *"Explicit proofs of Mathar's recurrence and Barker's Hankel formulas from Mathar's and Cigler's theorems"*); inspected `24414721` via Zenodo API directly — it settles `A128056` and `A128057` only, NOT `A165204` (`A165203`).

## Near-Misses

- Ma & Zhang Zenodo `24414721` proves Colin Barker's Hankel formula for `A128056`/`A128057`, unrelated to `A165203`/`A165204`.

## Coverage Limits

- arXiv query covers metadata rather than PDF full text; offline or unindexed manuscripts are outside direct visibility.
