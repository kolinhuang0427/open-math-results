# Novelty Receipt — Gate 3 (`watch-5`)

- **Target:** `targets/oeis-A026923/` (`OEIS:A026923` rev. 27, Colin Barker Sep 01 2019)
- **Timestamp (UTC):** `2026-11-27T11:46Z`
- **Verdict:** **PASS**

## Live Checks (<1h)

1. `tools/novelty_grep.py A026923 A026927`: `0` lines across `0/658` snapshot files.
2. `tools/arxiv_fetch.py query 'all:A026923 OR all:A026927'`: `0` entries.
3. Live `oeis/oeisdata` (`A026923.seq`): `%F A026923 Conjectures from _Colin Barker_, Sep 01 2019: (Start)` unchanged.
4. Zenodo live API (`"A026923"`): only unrelated biology record `6081413` (*Afrobethylus swazi Ramos & Azevedo, sp. nov.*); `mylesparslow-collab.github.io`: `False`.
5. Verified required files present: `targets/oeis-A026923/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.
