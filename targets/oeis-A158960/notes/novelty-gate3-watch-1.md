# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A158960/`

- **Checked UTC:** `2026-11-27T10:20:09Z`–`2026-11-27T10:20:57Z` (post-`AUDIT.md` PASS)
- **Target:** OEIS `A158960` (rev. 28) — M. F. Hasler (Feb 16 2014) denominator $5^n$ conjecture for $\mathrm{Hermite}(n, 1/5)$
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... "A158960" "158960" "Hermite(n, 1/5)"` after Sweep 26 refresh):** `0` hits across `0/618` files (`1337isnot1337/solved-conjectures`, `trureturing*`, `openai/math`, `formal-conjectures`, `watch/snapshots/discovered/`, and `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **Live OEIS (`https://oeis.org/search?q=id:A158960&fmt=json`):** `ID: 158960`, `rev: 28` (`time: 2022-09-08T08:45:43-04:00`); `COMMENT` remains `(conjectured)`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A158960&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs "A158960"`):** Only unrelated `sharpemu/sharpemu #618`; `0` PRs.
5. **Web search (Gate 2 `10:17Z`):** `0` external proofs found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:20Z` (Sweep 26) and live `gh search issues/prs` at `10:20Z` returned no math/OEIS matches.
