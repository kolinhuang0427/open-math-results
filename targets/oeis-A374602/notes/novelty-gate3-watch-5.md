# Novelty Receipt — Gate 3 (`watch-5`)

- **Target:** `targets/oeis-A374602/` (`OEIS:A374602` rev. 31, `OEIS:A377290` rev. 7, `OEIS:A377291` rev. 7)
- **Timestamp (UTC):** `2026-11-27T11:28Z`
- **Verdict:** **PASS**

## Live Checks (<1h)

1. `tools/novelty_grep.py A374602 A377290 A377291`: `0` lines across `0/653` snapshot files (incl. Cohen `24384895` & Zenodo `23112421`/`23114921`).
2. `tools/arxiv_fetch.py query 'all:A374602 OR all:A377290 OR all:A377291'`: `0` entries.
3. Live OEIS JSON: `A374602` rev. `31`, `A377290` rev. `7`, `A377291` rev. `7` unchanged (`2024-11-15`).
4. Zenodo live API (`"A374602"`, `"A377290"`, `"A377291"`): `0` hits.
5. Verified required files present: `targets/oeis-A374602/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`.
