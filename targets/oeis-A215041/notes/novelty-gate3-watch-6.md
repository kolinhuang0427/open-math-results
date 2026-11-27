# Gate 3 Novelty Check (`watch-6`): `targets/oeis-A215041/`

- **Checked UTC:** `2026-11-27T11:30:00Z`
- **Target:** OEIS `A215041` (`rev. 10`, `2023-12-25T18:06:42-05:00`) / `arXiv:1210.1018v2` Open Problem #1 — conjectured formula for $a(n) = n^{\delta(n)} / |\mathrm{Disc}(C(n, x))|$.
- **Verdict:** **PASS** (<1h freshness confirmed; no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (657 files incl. Su `24366920`/`23760779`, `mylesparslow-collab`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, 2026 Zenodo compendia):**
   - `.venv/bin/python -u tools/novelty_grep.py A215041 215041` -> `# 0 lines across 0/653 files in 0.31s`, and `0` matches in `mylesparslow-conjecture-ledger.md`, `su-zenodo-24366920-oeis-ids.md`, `su-zenodo-23760779-oeis-ids.md`, and `zenodo-2026-oeis-compendia-ids.md`.
2. **Live OEIS JSON (`https://oeis.org/search?q=id:A215041&fmt=json`):**
   - `rev: 10`, `time: 2023-12-25T18:06:42-05:00`; conjectured status unchanged.
3. **arXiv metadata API (`.venv/bin/python -u tools/arxiv_fetch.py query "all:A215041"`):**
   - `total_results: 0`.
4. **Zenodo API (`https://zenodo.org/api/records?q=A215041`):**
   - `hits.total: 0`.
5. **GitHub search (`gh search repos A215041 --limit 5`, `gh search issues A215041 --limit 5`):**
   - `[]` (repos) and `[]` (issues).
6. **Web search (`search_web` for `"A215041" recurrence cyclotomic proof`):**
   - Returned only OEIS `A215041` (and proved sibling `A193679` / Ribenboim classical cyclotomic discriminant); `A215041` remains conjectured.

## Coverage Limits

- arXiv API searches metadata rather than PDF full text; offline or unindexed manuscripts are outside direct visibility.
