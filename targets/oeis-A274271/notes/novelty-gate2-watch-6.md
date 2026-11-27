# Gate 2 Novelty Check (`watch-6`): `targets/oeis-A274271/`

- **Checked UTC:** `2026-11-27T11:34:38Z`
- **Target:** OEIS `A274271` (`rev. 12`, `2016-06-21T09:29:05-04:00`) — Colin Barker's Jun 17 2016 conjectured closed form `((3+3^n)^2*(9+3^n))/144` ($n > 1$), 4-term recurrence ($n > 4$), and rational g.f. for partitions of `3^n` into at most 4 parts.
- **Verdict:** **PASS** (no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py A274271 274271` -> `# 0 lines across 0/658 files in 0.38s`.
2. **Live OEIS JSON (`https://oeis.org/search?q=id:A274271&fmt=json`):**
   - `rev: 12`, `time: 2016-06-21T09:29:05-04:00`; Barker's three formulas remain inside `Conjectures (Start) ... (End)`.
3. **arXiv metadata API (`.venv/bin/python -u tools/arxiv_fetch.py query "all:A274271"`):**
   - `total_results: 0`.
4. **Zenodo API (`https://zenodo.org/api/records?q=A274271`):**
   - `hits.total: 0`.
5. **GitHub search (`gh search repos A274271 --limit 5`, `gh search issues A274271 --limit 5`):**
   - `[]` (repos) and `[]` (issues).
6. **Web search (`search_web` for `"A274271" Barker recurrence generating function proof`):**
   - Returned only OEIS `A274271`; no published proof of Barker's 3-way formula/recurrence/g.f. conjecture surfaced.

## Coverage Limits

- arXiv API searches metadata rather than PDF full text; offline or unindexed manuscripts are outside direct visibility.
