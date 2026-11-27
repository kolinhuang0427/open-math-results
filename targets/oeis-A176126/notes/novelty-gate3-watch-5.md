# Novelty Receipt — Gate 3 (`watch-5`)

- **Target:** `targets/oeis-A176126/` (`OEIS:A176126` rev. 18, `OEIS:A127276` rev. 33)
- **Timestamp (UTC):** `2026-11-27T11:34Z`
- **Verdict:** **PASS**

## Live Checks (<1h)

1. `tools/novelty_grep.py A176126`: `0` lines across `0/658` snapshot files.
2. `tools/arxiv_fetch.py query 'all:A176126'`: `0` entries.
3. Live OEIS JSON: `A176126` rev. `18` (`2022-08-27`) unchanged, Mathar's recurrence & g.f. marked `Conjecture:`.
4. Zenodo live API (`"A176126"`): `0` hits; `mylesparslow-collab.github.io`: `False`.
5. Verified required files present: `targets/oeis-A176126/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.
