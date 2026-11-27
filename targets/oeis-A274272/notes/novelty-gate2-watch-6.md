# Gate 2 Novelty Check (`watch-6`): `targets/oeis-A274272/`

- **Checked UTC:** `2026-11-27T11:37:13Z`
- **Target:** OEIS `A274272` (`rev. 12`, `2016-06-23T10:05:23-04:00`) — Colin Barker's Jun 17 2016 conjectured closed form `(57+8*(-1)^n+63*5^n+3*5^(1+2*n)+125^n)/144`, 5-term recurrence (`n > 4`), and rational g.f. for partitions of `5^n` into at most 4 parts.
- **Verdict:** **PASS** (no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py A274272 274272` -> `# 0 lines across 0/658 files in 0.47s`.
2. **Live OEIS JSON (`https://oeis.org/search?q=id:A274272&fmt=json`):**
   - `rev: 12`, `time: 2016-06-23T10:05:23-04:00`; Barker's three formulas remain inside `Conjectures (Start) ... (End)`.
3. **arXiv metadata API (`.venv/bin/python -u tools/arxiv_fetch.py query "all:A274272"`):** `total_results: 0`.
4. **Zenodo API (`https://zenodo.org/api/records?q=A274272`):** `hits.total: 0`.
5. **GitHub search (`gh search repos A274272 --limit 5`, `gh search issues A274272 --limit 5`):** `[]`.
6. **Web search (`search_web` for `"A274272" Barker recurrence generating function proof`):**
   - Returned only OEIS `A274272`; no published proof of Barker's 3-way conjecture surfaced.

## Coverage Limits

- arXiv query covers metadata rather than PDF full text; offline or unindexed manuscripts are outside direct visibility.
