# Novelty Receipt — Gate 3 (`watch-5`)

- **Target:** `targets/oeis-A168503/` (`OEIS:A168503` rev. 20, R. J. Mathar Feb 10 2015 4-term recurrence)
- **Timestamp (UTC):** `2026-11-27T11:41Z`
- **Verdict:** **PASS**

## Live Checks (<1h)

1. `tools/novelty_grep.py A168503`: `0` lines across `0/658` snapshot files.
2. `tools/arxiv_fetch.py query 'all:A168503'`: `0` entries.
3. OEIS (`oeis/oeisdata` `A168503.seq`): Mathar's 4-term recurrence still marked `Conjecture:`.
4. Zenodo live API (`"A168503"`): `0` hits; `mylesparslow-collab.github.io`: `False`.
5. Verified required files present: `targets/oeis-A168503/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.
