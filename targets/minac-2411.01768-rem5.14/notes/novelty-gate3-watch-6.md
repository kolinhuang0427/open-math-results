# Gate 3 Novelty Check (<1h) — targets/minac-2411.01768-rem5.14/ (watch-6)

- **UTC Timestamp:** `2026-11-27T10:55:21Z`
- **Target:** `targets/minac-2411.01768-rem5.14/` (label: `"written counterexample, internally audited"`) — Refutation of Remark 5.14 (`rem:same_degree`) of Mináč–Nguyen–Tân (`arXiv:2411.01768v2`) over $\mathbb{F}_q[x]$ ($16\text{v}$ $f=x^2(x^2+x+1)$, squarefree $64\text{v}$ $f=x(x^2+x+1)(x^3+x+1)$, connected complements, and CRT family over every $\mathbb{F}_q$).
- **Verdict:** **PASS** (clear within `<1h` freshness window).

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py "2411.01768" "rem:same_degree" "Minac" "5.14"`
   - Result: `72` lines across `27/635` files — inspected completely:
     - `the-omega-institute/trureturing`: `MinacNguyenTanQuestion35` (`Question 3.5`, NOT Remark 5.14 `rem:same_degree`) and `Library/ArithUnits/minacnguyentan2026sums.md`.
     - Remaining matches are substring `"5.14"` false positives (`2605.14229`, `v1.5.14`, `n=75.14`, `§A.5.14`, `"determinacy"` matching `rem`? No, `"5.14"` in date/arxiv IDs like `2405.14xxx`).
     - `0` matches for `2411.01768` or `rem:same_degree`.
2. **Live arXiv (`all:2411.01768`):**
   - Latest version remains `http://arxiv.org/abs/2411.01768v2` (`updated: 2026-08-03T02:49:58Z`, *"Isomorphic gcd-graphs over polynomial rings"*); no v3 revision or erratum.
3. **Zenodo API (`https://zenodo.org/api/records?q=%222411.01768%22&size=5`):**
   - `zenodo_hits: 0`.
4. **GitHub Search (`gh search repos "2411.01768"`, `gh search issues "2411.01768"`):**
   - Both returned `[]`.

## Coverage Limits
- Gate 2 (`targets/minac-2411.01768-rem5.14/notes/novelty-gate2-watch-6.md`) covered `search_web` and Semantic Scholar citing papers; this `<1h` Gate 3 pass re-verified local snapshots (`635` files), live arXiv v2, Zenodo API, and GitHub repos/issues. `gh search code` was not re-run under secondary-rate-limit budget.
