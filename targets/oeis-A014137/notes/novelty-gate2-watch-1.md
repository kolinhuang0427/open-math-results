# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A014137/`

- **Checked UTC:** `2026-11-27T10:49:27Z`–`2026-11-27T10:49:40Z`
- **Target:** OEIS `A014137` (rev. 180) — Sergei N. Gladkovskii (May 14 2013) continued fraction g.f. conjecture: $Q(0)/(1-x)$ for Catalan partial sums
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "A014137" "014137" ...` & `grep zenodo-23112421-oeis-ids.md`):** `0` hits for `A014137` across `635` files (`014137` matched only decimal `4.014137` in `ai-village-graffiti-verification.md`), and absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`.
2. **Live OEIS (`https://oeis.org/search?q=id:A014137&fmt=json`):** `ID: 14137`, `rev: 180` (`time: 2026-08-07T18:53:11-04:00`); Gladkovskii's May 14 2013 formula remains `G.f. (conjecture): ...` (note Peter J. Taylor's 2015 comment settles an unrelated Mathar formula, not Gladkovskii's CF).
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A014137&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "A014137"`):** `0` issues, `0` repos, and only unrelated PR `buryads/orshuulagsha-ui #12`.
5. **Web search (`("A014137" "Gladkovskii") ...`):** `0` external proofs found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:20:09Z` (Sweep 26; Sweep 27 running concurrently) and live `gh search` at `10:49Z` returned no math/OEIS matches.
