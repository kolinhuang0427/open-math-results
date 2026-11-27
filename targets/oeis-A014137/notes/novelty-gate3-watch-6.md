# Gate 3 Novelty Check (<1h) — targets/oeis-A014137/ (watch-6)

- **UTC Timestamp:** `2026-11-27T10:59:12Z`
- **Target:** `targets/oeis-A014137/` (label: `"written proof, internally audited"`) — Sergei N. Gladkovskii's May 14, 2013 continued fraction G.f. conjecture `Q(0)/(1-x)` for `A014137` (partial sums of Catalan numbers), proved $x$-adically in $\mathbb{Q}[[x]]$ and uniformly on compact subsets of $\{|x| < 1/4\}$.
- **Verdict:** **PASS** (clear within `<1h` freshness window).

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py A014137 "014137"`
   - Result: `# 1 lines across 1/635 files in 1.45s` — floating-point constant `4.014137` in `watch/snapshots/ai-village-graffiti-verification.md` L40519; `0` target hits (including `zenodo-23112421-oeis-ids.md` and Sweep 4 `discovered/`).
2. **Live OEIS (`oeis.org/search?q=id:A014137&fmt=json`):**
   - `oeis_rev: 180`, `time: 2026-08-07T18:53:11-04:00` — Gladkovskii's `G.f. (conjecture)` remains open in OEIS.
3. **Zenodo API (`https://zenodo.org/api/records?q=%22A014137%22&size=5`):**
   - `zenodo_hits: 0`.
4. **GitHub Search (`gh search repos "A014137"`, `gh search issues "A014137"`):**
   - Both returned `[]`.

## Coverage Limits
- Re-verified local snapshots (`635` files), live OEIS JSON, Zenodo API, and GitHub repos/issues since Gate 2 (`targets/oeis-A014137/notes/novelty-gate2-watch-6.md`); `gh search code` skipped under secondary-rate-limit budget after `0` repo/issue/local hits.
