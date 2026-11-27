# Gate 3 Novelty Check (`watch-6`): `targets/oeis-A026927/`

- **Checked UTC:** `2026-11-27T11:45:23Z`
- **Target:** OEIS `A026927` (`rev. 23`) — Colin Barker's Sep 01 2019 rational g.f. and 11-term recurrence.
- **Verdict:** **PASS** (<1h freshness confirmed; no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py A026923 026923 A026927 026927` -> `# 2 lines across 2/658 files in 1.18s` (false-positive SHA-256 hex digest containing `026927`).
2. **OEIS (`oeis/oeisdata` `seq/A026/A026927.seq`):** remains inside `Conjectures from _Colin Barker_, Sep 01 2019: (Start) ... (End)`.
3. **Zenodo API (`A026923+OR+A026927`):** `6081413` (*Afrobethylus swazi Ramos & Azevedo, sp. nov.*, unrelated).
4. **arXiv / GitHub / Web (verified in Gate 2 at `11:40:42Z`):** `0` proofs found.

## Coverage Limits

- arXiv API covers metadata rather than PDF full text; offline or unindexed manuscripts are outside direct visibility.
