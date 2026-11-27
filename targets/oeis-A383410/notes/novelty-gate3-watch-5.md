# Novelty Receipt — Gate 3 (`watch-5`)

- **Target:** `targets/oeis-A383410/` (`OEIS:A383410` rev. 6, `OEIS:A005649` rev. 123, Mikhail Kurkov Apr 26 2025)
- **Timestamp (UTC):** `2026-11-27T11:50Z`
- **Verdict:** **PASS**

## Live Checks (<1h)

1. `tools/novelty_grep.py A383410 A005649`: `0` lines across `0/689` snapshot files (incl. `insorrowmeow/oeis-sequence-proofs`, `mylesparslow-conjecture-ledger.md`, Cohen `24384895`, Su `24366920`/`23760779`, Zenodo `23112421`/`23114921`).
2. `tools/arxiv_fetch.py query 'all:A383410'`: `0` entries.
3. Live `oeis/oeisdata` (`A383410.seq`): `%F A383410 Conjecture: A(n,0) = A005649(n).` unchanged.
4. Zenodo live API (`"A383410"`): `0` hits.
5. Verified required files present: `targets/oeis-A383410/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.
