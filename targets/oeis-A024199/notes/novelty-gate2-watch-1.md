# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A024199/`

- **Checked UTC:** `2026-11-27T10:35:15Z`–`2026-11-27T10:35:34Z`
- **Target:** OEIS `A024199` (rev. 80) — Peter Bala (Nov 15 2016) alternating double-factorial sum & EGF conjecture: $a(n) = \frac{1}{2}\sum_{k=0}^{2n-1} (-1)^{n-k+1} k!(2n-2k-3)!!$ ($n \ge 1$) and EGF $\frac{\arcsin(2x)}{2\sqrt{1-2x}}$
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "A024199" "024199"` & `grep zenodo-23112421-oeis-ids.md`):** `0` hits across `0/619` files (`1337isnot1337/solved-conjectures` refreshed `10:20:09Z`, `trureturing*`, `openai/math`, `formal-conjectures`, `watch/snapshots/discovered/`, and `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **Live OEIS (`https://oeis.org/search?q=id:A024199&fmt=json`):** `ID: 24199`, `rev: 80` (`time: 2026-06-28T15:47:50-04:00`); `FORMULA` still prefixes Bala's formula with `Conjecture:` and has no confirmation note.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A024199&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "A024199"`):** `0` issues, `0` PRs, `0` repos.
5. **Web search (`"A024199" "Bala" OR "arcsin" OR "conjecture"`):** `0` external proofs of Bala's `A024199` conjecture found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:20:09Z` (Sweep 26) and live `gh search` at `10:35Z` returned `0` hits.
