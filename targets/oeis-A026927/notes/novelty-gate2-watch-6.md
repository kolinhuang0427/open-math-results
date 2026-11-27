# Gate 2 Novelty Check (`watch-6`): `targets/oeis-A026927/`

- **Checked UTC:** `2026-11-27T11:40:42Z`
- **Target:** OEIS `A026927` (`rev. 23`) — Colin Barker's Sep 01 2019 conjectured g.f. `x^4*(1 + x^2 - x^3 + x^4) / ((1 - x)^3*(1 + x)^2*(1 - x + x^2)*(1 + x^2)*(1 + x + x^2))` and 11-term recurrence (`n > 11`).
- **Verdict:** **PASS** (no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py A026923 026923 A026927 026927` -> `# 2 lines across 2/658 files` — both false-positive hex SHA-256 digests (`...026927...` in `trureturing-source-theories`).
2. **OEIS (`oeis/oeisdata` `seq/A026/A026927.seq`):**
   - Barker's Sep 01 2019 g.f. and 11-term recurrence remain inside `Conjectures from _Colin Barker_, Sep 01 2019: (Start) ... (End)`.
3. **arXiv metadata API (`all:A026923 OR all:A026927`):** `total_results: 0`.
4. **Zenodo API (`A026923+OR+A026927`):** `hits.total: 1` (`6081413`: *Afrobethylus swazi Ramos & Azevedo, sp. nov.*, unrelated biology paper).
5. **GitHub (`gh search repos/issues A026927`):** `[]`.
6. **Web search (`search_web` for `"A026923" OR "A026927" Barker recurrence generating function proof`):** no proof surfaced.

## Coverage Limits

- `oeis.org/search` transiently rate-limited, mitigated by `raw.githubusercontent.com/oeis/oeisdata/main/seq/A026/A026927.seq`; arXiv query covers metadata rather than PDF full text.
