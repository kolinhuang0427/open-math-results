# Gate 2 Novelty Check — targets/oeis-A374602/ (watch-6)

- **UTC Timestamp:** `2026-11-27T11:07:27Z`
- **Target:** `targets/oeis-A374602/` (`status: candidate`, `owner: scout-6`) — Charles L. Hohn's conjectures in OEIS `A374602` (`rev. 31`), `A377290` (`rev. 11`), `A377291` (`rev. 7`) on subsequence periodicity, geometric growth factor, and algorithmic generation for nearly regular Pythagorean hyperrectangles.
- **Verdict:** **PASS** (no settled proof or counterexample found).

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py A374602 "374602" A377290 A377291`
   - Result: `# 0 lines across 0/651 files in 2.47s` (incl. `zenodo-23112421-oeis-ids.md`, `zenodo-23114921-oeis-ids.md`, Sweep 5 `discovered/`).
2. **Live OEIS (`A374602` rev `31`, `2024-11-15T23:31:14-05:00`):**
   - Comments still state "it is conjectured that this is the case for all n... but these are not proven" and "not known if there is an algorithm".
3. **Zenodo API (`https://zenodo.org/api/records?q=%22A374602%22&size=5`):** `zenodo_hits: 0`.
4. **GitHub Search (`gh search repos "A374602"`):** `[]`.
5. **Web Search (`search_web`):** Clear; only references OEIS `A374602`/`A377290`/`A377291` themselves.

## Coverage Limits
- `gh search issues`/`code` and arXiv API omitted here on OEIS-only ID after `0/651` local, `0` Zenodo, `[]` GitHub repos, and `search_web` clear (`TARGET.md` Gate 1 also checked `gh search code`/`issues` = `0`).
