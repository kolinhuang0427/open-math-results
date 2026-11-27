# Novelty Receipt — Gate 3 (`watch-5`)

- **Target:** `targets/oeis-A379459/` (rescoped strictly to `A379459(n, 0) = A006351(n + 2)` per `TARGET.md` & `AUDIT.md` §6; `A379460` prior-settled in `insorrowmeow/oeis-sequence-proofs` `YokeRows.{md,lean}`)
- **Timestamp (UTC):** `2026-11-27T11:52Z`
- **Verdict:** **PASS**

## Live Checks (<1h)

1. `tools/novelty_grep.py A379459 A006351`: hits only `insorrowmeow__oeis-sequence-proofs.json` (`YokeRows.{md,lean}`, which settles `A379460(n, 0) = A006351(n + 1)` via MO `481674` only, leaving `A379459(n, 0) = A006351(n + 2)` open); `0` hits for `A379459` across `689` snapshot files.
2. `tools/arxiv_fetch.py query 'all:A379459'`: `0` entries.
3. Live `oeis/oeisdata` (`A379459.seq`, `A006351.seq`): `A379459(n,0) = A006351(n+2)` remains unmarked by proof.
4. `the-omega-institute/trureturing#27785`: `open`, `0` comments.
5. Zenodo live API (`"A379459"`): `0` hits; `mylesparslow-collab.github.io`: `False`.
6. Verified required files present: `targets/oeis-A379459/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`.
