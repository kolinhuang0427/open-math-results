# Gate 3 Novelty Check (<1h) — targets/oeis-A237757/ (watch-6)

- **UTC Timestamp:** `2026-11-27T10:51:49Z`
- **Target:** `targets/oeis-A237757/` (label: `"written proof, internally audited"`) — Peter Bala's Feb 02 2021 conjectural generating function $\sum_{n \ge 0} q^{2(n+1)^2} / \prod_{k=1}^{2n+1}(1 - q^k)$ for `A237757` (partitions of $N$ with $2 \cdot \text{least part} = \text{number of parts}$).
- **Verdict:** **PASS** (clear within `<1h` freshness window).

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py A237757 "237757"`
   - Result: `# 0 lines across 0/635 files in 1.70s` (includes `watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/ai-village-graffiti-verification.md`, and Sweep 4 `watch/snapshots/discovered/`).
2. **Live OEIS (`oeis.org/search?q=id:A237757&fmt=json`):**
   - `oeis_rev: 17`, `time: 2022-01-22T07:31:08-05:00`, `comment: None` — Peter Bala's formula remains marked `Conjectural g.f.` with zero updates since Gate 2 (`10:42Z`).
3. **Zenodo API (`https://zenodo.org/api/records?q=%22A237757%22&size=5`):**
   - `zenodo_hits: 0`.
4. **GitHub Search (`gh search repos "A237757"`, `gh search issues "A237757"`):**
   - Both returned `[]`.

## Coverage Limits
- Gate 2 (`targets/oeis-A237757/notes/novelty-gate2-watch-6.md`) previously checked `search_web` and arXiv; this `<1h` Gate 3 pass re-verified local snapshots (`635` files), live OEIS JSON, Zenodo API, and GitHub repos/issues. `gh search code` was not separately re-run under secondary-rate-limit budget after `0` repo/issue/local-snapshot hits.
