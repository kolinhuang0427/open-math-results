# Gate 2 Novelty Check (`watch-6`): `targets/oeis-A168503/`

- **Checked UTC:** `2026-11-27T11:36:05Z`
- **Target:** OEIS `A168503` (`rev. 20`, `2025-02-07T00:50:52-05:00`) — R. J. Mathar's Feb 10 2015 conjectured 4-term recurrence `(n+1)*a(n) +(-13*n+5)*a(n-1) +6*(8*n-13)*a(n-2) +12*(-5*n+13)*a(n-3) +12*(2*n-7)*a(n-4)=0`.
- **Verdict:** **PASS** (no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py A168503 168503 A168505 168505` -> `# 0 lines across 0/658 files in 0.46s`.
2. **Live OEIS JSON (`https://oeis.org/search?q=id:A168503&fmt=json`):**
   - `rev: 20`, `time: 2025-02-07T00:50:52-05:00`; Mathar's Feb 10 2015 recurrence remains labeled `Conjecture:`.
3. **arXiv metadata API (`all:A168503 OR all:A168505`):** `total_results: 0`.
4. **Zenodo API (`https://zenodo.org/api/records?q=A168503+OR+A168505`):** `hits.total: 0`.
5. **GitHub (`gh search repos A168503`, `the-omega-institute/trureturing` `dev` `Problems/` tree):** `[]`.
6. **Web search (`search_web` for `"A168503" OR "A168505" Mathar recurrence continued fraction proof`):** no proof surfaced.

## Coverage Limits

- `gh search issues` / `gh search code` were omitted (`gh search repos` + `novelty_grep` across 658 files clear); arXiv query covers metadata rather than PDF full text.
