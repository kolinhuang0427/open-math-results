# Gate 2 Novelty Check (`watch-6`): `targets/oeis-A157003/`

- **Checked UTC:** `2026-11-27T11:33:48Z`
- **Target:** OEIS `A157003` (`rev. 37`, `2025-11-05T15:22:17-05:00`) — R. J. Mathar's Nov 19 2014 conjectured 6-term recurrence `(n+1)*a(n) +(n+2)*a(n-1) +(-21*n+29)*a(n-2) +(3*n-16)*a(n-3) +40*(n-3)*a(n-4) +2*(-2*n+7)*a(n-5) +10*(-2*n+9)*a(n-6)=0`.
- **Verdict:** **PASS** (no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, 2026 Zenodo compendia):**
   - `.venv/bin/python -u tools/novelty_grep.py A157003 157003` -> `# 0 lines across 0/658 files in 0.46s`.
2. **Live OEIS JSON (`https://oeis.org/search?q=id:A157003&fmt=json`):**
   - `rev: 37`, `time: 2025-11-05T15:22:17-05:00`; Mathar's Nov 19 2014 recurrence remains marked `Conjecture:`.
3. **arXiv metadata API (`.venv/bin/python -u tools/arxiv_fetch.py query "all:A157003"`):**
   - `total_results: 0`.
4. **Zenodo API (`https://zenodo.org/api/records?q=A157003`):**
   - `hits.total: 0`.
5. **GitHub search (`gh search repos A157003 --limit 5`, `gh search issues A157003 --limit 5`):**
   - `[]` (repos) and `[]` (issues).
6. **Web search (`search_web` for `"A157003" Mathar Kotesovec recurrence proof`):**
   - Returned only OEIS `A157003` and Baril et al. `bacorasisito.pdf` (no proof of Mathar's 6-term recurrence).

## Coverage Limits

- arXiv API searches metadata rather than full PDF text (beyond linked PDFs already checked in Gate 1); offline or unindexed manuscripts are outside direct visibility.
