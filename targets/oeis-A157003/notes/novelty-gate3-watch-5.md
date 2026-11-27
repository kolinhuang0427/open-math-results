# Novelty Receipt — Gate 3 (`watch-5`)

- **Target:** `targets/oeis-A157003/` (`OEIS:A157003` rev. 37, R. J. Mathar Nov 19 2014 6-term recurrence)
- **Timestamp (UTC):** `2026-11-27T11:41Z`
- **Verdict:** **PASS**

## Live Checks (<1h)

1. `tools/novelty_grep.py A157003`: `0` lines across `0/658` snapshot files.
2. `tools/arxiv_fetch.py query 'all:A157003'`: `0` entries.
3. OEIS (`oeis/oeisdata` `A157003.seq`): Mathar's 6-term recurrence still marked `Conjecture:`.
4. Zenodo live API (`"A157003"`): `0` hits; `mylesparslow-collab.github.io`: `False`.
5. Verified required files present: `targets/oeis-A157003/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`.
