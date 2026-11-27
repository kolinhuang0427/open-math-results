# Gate 3 Novelty Receipt — `cassaigne-2602.21895-conjC4`

- **UTC Time:** `2026-11-27T08:50Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (prior `CONTESTED.md` ruled `STILL-OPEN` in `notes/contest-ruling-audit-2.md`, `2026-11-27T08:09Z`; no new competing settlement)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 586 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 22 (`2026-11-27T08:41:11Z`): `0` hits for `2602.21895`, `Cassaigne`, `Espinoza`, `Stipulanti`, `A357448`, `2301.13563`.
   - `.venv/bin/python tools/novelty_grep.py 2602.21895 "Cassaigne" "Espinoza" "Stipulanti" "A357448" "2301.13563"` -> hits only in:
     - `the-omega-institute/trureturing` (`CassaigneIndexTransport` / `CassaigneRecurrenceTransport` / `CassaigneSturmianCharacterization`, unrelated to base-3/2 Thue–Morse);
     - `AlexenderSokolov/cross-theory-formal-database` (`arxiv-2602.21895-CC-BY-4.0.txt`, license mirror only);
     - `watch/snapshots/arxiv/citing_papers.md` (`arXiv:2611.06878v1` *"The full Kolakoski shift is topologically transitive"*, checked via `arxiv_fetch.py query --id-list 2611.06878`: concerns the Kolakoski shift over `{1,2}`, not base-3/2 Thue–Morse Conjecture `(C_4)`).
2. **Live GitHub (`gh search`) & Zenodo (`2026-11-27T08:48Z`):**
   - `gh search issues "2602.21895"` -> `trureturing#14986` (`2202.13548v1` single-letter frequency) and `trureturing#24159` (`2406.09302` reflection complexity) only; no new issue on `(C_4)`. (Existing `trureturing#24005`/`#29075` already ruled `STILL-OPEN` for full `(C_4)` in `notes/contest-ruling-audit-2.md`.)
   - `gh search code "2602.21895"` -> `cross-theory-formal-database` license, `trureturing/Problems/dekking-keane-2022-two-block-thue-morse-frequency.md` (`2202.13548v1`), `Develata.github.io`, `Lyken17/arXiv-stats`.
   - `https://zenodo.org/api/records?q=2602.21895&size=1` -> `total: 0`.

## Coverage Limits
- Closed-access venues, private repositories (including unpushed `trureturing` branch `lane/math/op-dekking2301` noted in `contest-ruling-audit-2.md`), and unindexed papers.
