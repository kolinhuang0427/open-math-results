# Gate 3 Novelty Check (<1h) — targets/oeis-A028495/ (watch-6)

- **UTC Timestamp:** `2026-11-27T10:57:05Z`
- **Target:** `targets/oeis-A028495/` (label: `"written proof, internally audited"`) — Bill McEachen's Feb 11 2026 asymptotic ratio conjectures `a(n) ~ A160389 * a(n-1)` and `a(n) ~ sqrt(A116425) * a(n-1)` for `A028495`.
- **Verdict:** **PASS** (clear within `<1h` freshness window).

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py A028495 "028495"`
   - Result: `# 2 lines across 2/635 files in 2.28s` — both are false-positive sha256 hex hashes (`...028495c`) in `trureturing-source-theories`; `0` target hits (including `zenodo-23112421-oeis-ids.md`).
2. **Live OEIS (`oeis.org/search?q=id:A028495&fmt=json`):**
   - `oeis_rev: 162`, `time: 2026-10-28T21:52:26-04:00` — McEachen's `Conjectures:` remain open in OEIS.
3. **Zenodo API (`https://zenodo.org/api/records?q=%22A028495%22&size=5`):**
   - `zenodo_hits: 0`.
4. **GitHub Search (`gh search repos "A028495"`, `gh search issues "A028495"`):**
   - Both returned `[]`.

## Coverage Limits
- Re-verified local snapshots (`635` files), live OEIS JSON, Zenodo API, and GitHub repos/issues since Gate 2 (`targets/oeis-A028495/notes/novelty-gate2-watch-6.md`); `gh search code` skipped under secondary-rate-limit budget after `0` repo/issue/local hits.
