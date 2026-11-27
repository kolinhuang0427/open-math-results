# Gate 2 Novelty Check (`watch-6`): `targets/oeis-A162481/`

- **Checked UTC:** `2026-11-27T11:32:31Z`
- **Target:** OEIS `A162481` (`rev. 23`, `2025-10-09T23:21:43-04:00`) — R. J. Mathar's Dec 11 2011 conjectured 4-term D-finite recurrence `(n+1)*a(n) + 2*(1-4*n)*a(n-1) + 2*(5*n-3)*a(n-2) + 4*(2-n)*a(n-3) + (n-3)*a(n-4) = 0`.
- **Verdict:** **PASS** (no prior settlement found)

## Exact Queries & Results

1. **Snapshot grep (657 files incl. Su `24366920`/`23760779`, `mylesparslow-collab`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, 2026 Zenodo compendia):**
   - `.venv/bin/python -u tools/novelty_grep.py A162481 162481 A157002 157002` -> `# 0 lines across 0/657 files in 0.85s`.
2. **Live OEIS JSON (`https://oeis.org/search?q=id:A162481&fmt=json`):**
   - `rev: 23`, `time: 2025-10-09T23:21:43-04:00`; Mathar's Dec 11 2011 recurrence remains marked `Conjecture:`.
3. **arXiv metadata API (`.venv/bin/python -u tools/arxiv_fetch.py query "all:A162481 OR all:A157002"`):**
   - `total_results: 0`.
4. **Zenodo API (`https://zenodo.org/api/records?q=A162481+OR+A157002`):**
   - `hits.total: 0`.
5. **GitHub search (`gh search repos A162481 --limit 5`):**
   - `[]`.
6. **Web search (`search_web` for `"A162481" OR "A157002" Mathar recurrence proof`):**
   - Returned no published proof of Mathar's `A162481` recurrence.

## Coverage Limits

- `gh search issues` / `gh search code` were omitted on `A162481` (`gh search repos` + `novelty_grep` across 657 files clear); arXiv query covers metadata rather than full PDF text.
