# Novelty Receipt — Gate 3 (`watch-5`)

- **Target:** `targets/oeis-A392058/` (`OEIS:A392058` rev. 6, `OEIS:A233335` rev. 20, Mikhail Kurkov Dec 29 2025)
- **Timestamp (UTC):** `2026-11-27T11:50Z`
- **Verdict:** **PASS**

## Live Checks (<1h)

1. `tools/novelty_grep.py A392058 A233335`: `0` lines across `0/689` snapshot files (incl. `insorrowmeow/oeis-sequence-proofs`, `mylesparslow-conjecture-ledger.md`, Cohen `24384895`, Su `24366920`/`23760779`, Zenodo `23112421`/`23114921`).
2. `tools/arxiv_fetch.py query 'all:A392058'`: `0` entries.
3. Live `oeis/oeisdata` (`A392058.seq`): `%F A392058 Conjecture: A(n,0) = A233335(n+1).` unchanged.
4. Zenodo live API (`"A392058"`): `0` hits.
5. Verified required files present: `targets/oeis-A392058/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.
