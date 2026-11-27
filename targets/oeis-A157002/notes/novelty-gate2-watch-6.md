# Gate 2 Novelty Check (`watch-6`): `targets/oeis-A157002/`

- **Checked UTC:** `2026-11-27T11:32:31Z`
- **Target:** OEIS `A157002` (`rev. 15`, `2025-09-22T16:00:57-04:00`) — R. J. Mathar's Nov 19 2014 conjectured 4-term recurrence `(n+1)*a(n) +3*(-n+1)*a(n-1) +2*(-2*n+1)*a(n-2) +2*(2*n-7)*a(n-3) +2*(2*n-7)*a(n-4)=0`.
- **Verdict:** **PASS** (no prior settlement found)

## Exact Queries & Results

1. **Snapshot grep (657 files incl. Su `24366920`/`23760779`, `mylesparslow-collab`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, 2026 Zenodo compendia):**
   - `.venv/bin/python -u tools/novelty_grep.py A162481 162481 A157002 157002` -> `# 0 lines across 0/657 files in 0.85s`.
2. **Live OEIS JSON (`https://oeis.org/search?q=id:A157002&fmt=json`):**
   - `rev: 15`, `time: 2025-09-22T16:00:57-04:00`; Mathar's Nov 19 2014 recurrence remains marked `Conjecture:`.
3. **arXiv metadata API (`.venv/bin/python -u tools/arxiv_fetch.py query "all:A162481 OR all:A157002"`):**
   - `total_results: 0`.
4. **Zenodo API (`https://zenodo.org/api/records?q=A162481+OR+A157002`):**
   - `hits.total: 0`.
5. **GitHub search (`gh search repos A157002 --limit 5`):**
   - `[]`.
6. **Web search (`search_web` for `"A162481" OR "A157002" Mathar recurrence proof`):**
   - Returned no published proof of Mathar's `A157002` recurrence (Guoce Xin `arXiv:0712.0933` covers only the Somos-4 Hankel determinant).

## Coverage Limits

- `gh search issues` / `gh search code` were omitted on `A157002` (`gh search repos` + `novelty_grep` across 657 files clear); arXiv query covers metadata rather than full PDF text.
