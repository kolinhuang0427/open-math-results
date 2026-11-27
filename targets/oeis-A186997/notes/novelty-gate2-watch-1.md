# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A186997/`

- **Checked UTC:** `2026-11-27T10:15:52Z`–`2026-11-27T10:16:33Z`
- **Target:** OEIS `A186997` (rev. 85) — Peter Bala (Aug 02 2016) 2-adic valuation conjectures: $v_2(a(2m+1)) = v_2(C_{2m+1}) = v_2(C_m)$ ($m \ge 0$) and $v_2(a(2m)) = 3 + v_2(C_{m-2})$ ($m \ge 2$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "A186997" "186997" "Peter Bala"`):** `0` hits for `A186997` across `618` snapshot files (all `Peter Bala` matches in `watch/snapshots/**` are for unrelated sequences `A212334`, `A211417`, `A172572`, `A183068`, `A363412`, `A363419`, `A372211–A372213`, `A351859`, `A339946`, `A361717`, `A003024`, `A188457`, `A248668`).
2. **Zenodo `23112421` OEIS index (`grep -n "A186997" watch/snapshots/zenodo-23112421-oeis-ids.md`):** No match.
3. **Live OEIS (`https://oeis.org/search?q=id:A186997&fmt=json`):** `number: 186997`, `revision: 85` (`time: 2026-08-30T09:47:33-04:00`), `COMMENTS` still state `Conjectures (both checked up to n = 100):` with no proof note.
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A186997&size=5`):** `0` hits (`total: 0`).
5. **Live GitHub (`gh search issues/prs/repos "A186997"`):** `0` issues, `0` PRs, `0` repos.
6. **Web search (`"A186997" "Bala" OR "2-adic" OR "conjecture"`, `"A186997" "Catalan" OR "2-adic"`):** `0` proofs of Bala's `A186997` valuation conjectures found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot was last synced at `2026-11-27T09:50:27Z` (Sweep 25, ~26 min before this check); live `gh search` at `10:15Z` found no GitHub hits.
