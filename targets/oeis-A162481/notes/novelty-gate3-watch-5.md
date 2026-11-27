# Novelty Receipt — Gate 3 (`watch-5`)

- **Target:** `targets/oeis-A162481/` (`OEIS:A162481` rev. 23, R. J. Mathar Dec 11 2011 4-term recurrence)
- **Timestamp (UTC):** `2026-11-27T11:37Z`
- **Verdict:** **PASS**

## Live Checks (<1h)

1. `tools/novelty_grep.py A162481`: `0` lines across `0/658` snapshot files.
2. `tools/arxiv_fetch.py query 'all:A162481'`: `0` entries.
3. Live OEIS JSON: `A162481` rev. `23` (`2025-10-09`) unchanged, Mathar's recurrence marked `Conjecture:`.
4. Zenodo live API (`"A162481"`): `0` hits; `mylesparslow-collab.github.io`: `False`.
5. Verified required files present: `targets/oeis-A162481/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`.
