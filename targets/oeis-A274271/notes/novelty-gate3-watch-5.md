# Novelty Receipt — Gate 3 (`watch-5`)

- **Target:** `targets/oeis-A274271/` (`OEIS:A274271` rev. 12, Colin Barker Jun 17 2016)
- **Timestamp (UTC):** `2026-11-27T11:49Z`
- **Verdict:** **PASS**

## Live Checks (<1h)

1. `tools/novelty_grep.py A274271`: `0` lines across `0/689` snapshot files (incl. `insorrowmeow/oeis-sequence-proofs`, `mylesparslow-conjecture-ledger.md`, Cohen `24384895`, Su `24366920`/`23760779`, Zenodo `23112421`/`23114921`).
2. `tools/arxiv_fetch.py query 'all:A274271'`: `0` entries.
3. Live `oeis/oeisdata` (`A274271.seq`): `%F A274271 Conjectures (Start)` unchanged.
4. Zenodo live API (`"A274271"`): `0` hits; `mylesparslow-collab.github.io`: `False`.
5. Verified required files present: `targets/oeis-A274271/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`.
