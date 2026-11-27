# Gate 2 Novelty Check — targets/oeis-A347063/ (watch-6)

- **UTC Timestamp:** `2026-11-27T11:09:28Z`
- **Target:** `targets/oeis-A347063/` (`status: candidate`, `owner: scout-6`) — Refutation of Ivan N. Ianakiev's Oct 01 2024 conjecture in OEIS `A347063` (`rev. 51`) that $18k+12$ is Double Zumkeller for all $k \ge 1$ (minimal counterexample $k=192$, $n=3468 = 12 \cdot 17^2$; infinite family $n=12p^2$).
- **Verdict:** **PASS** (no settled proof or counterexample found).

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py A347063 "347063"`
   - Result: `# 0 lines across 0/651 files in 0.99s` (incl. `zenodo-23112421-oeis-ids.md`, `zenodo-23114921-oeis-ids.md`, Sweep 5 `discovered/`).
2. **Live OEIS (`A347063` rev `51`, `2026-07-24T17:37:53-04:00`):**
   - Ianakiev's comment (`18k+12` verified for `k in [1, 45]`) remains unrefuted/unproved in OEIS.
3. **Zenodo API (`https://zenodo.org/api/records?q=%22A347063%22&size=5`):** `zenodo_hits: 0`.
4. **GitHub Search (`gh search repos "A347063"`, `gh search issues "A347063"`):** Both returned `[]`.
5. **Web Search (`search_web`):** Only references Zumkeller (`A083207`) `18k+6`/`18k+12` results, NOT Double Zumkeller (`A347063`) `18k+12`.

## Coverage Limits
- `gh search code` not re-run after `TARGET.md` Gate 1 checked `0` code results under rate-limit budget.
