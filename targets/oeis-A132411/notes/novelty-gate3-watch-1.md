# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A132411/`

- **Checked UTC:** `2026-11-27T10:35:15Z`–`2026-11-27T10:35:24Z` (post-`AUDIT.md` PASS)
- **Target:** OEIS `A132411` (rev. 80) — Peter Bala (May 10 2025) $q$-series conjecture $F(q) = \sum_{n \ge 0} q^{2n} \prod_{k \ge 2n+2} (1 - (-q)^k) = 1 + \sum_{m \ge 2} q^{m^2-1}$ in $\mathbb{Z}[[q]]$
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "A132411" "132411"` & `grep zenodo-23112421-oeis-ids.md`):** `0` hits across `0/619` files (`1337isnot1337/solved-conjectures` refreshed `10:20:09Z`, `trureturing*`, `openai/math`, `formal-conjectures`, `watch/snapshots/discovered/`, and `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **Live OEIS (`https://oeis.org/search?q=id:A132411&fmt=json`):** `ID: 132411`, `rev: 80` (`time: 2026-01-22T07:45:32-05:00`); `COMMENT` remains `Conjecture:`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A132411&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search prs "A132411"`):** `0` PRs (`gh search repos` hit HTTP 403 rate limit at `10:35:24Z`; Gate 2 check at `10:27Z` showed `0` repos and only unrelated `nbbrd/sdmx-upptime #28139`).
5. **Web search (Gate 2 `10:27Z`):** `0` external proofs found.

## Coverage Limits
- `gh search repos "A132411"` hit GitHub HTTP 403 search rate limit at `2026-11-27T10:35:24Z` (`gh search prs`, local `619`-file snapshot corpus incl. `1337isnot1337` at `10:20Z` and `zenodo-23112421-oeis-ids.md`, live OEIS rev 80, Zenodo, and Gate 2 `10:27Z` repo/issue checks all returned no math/OEIS matches).
