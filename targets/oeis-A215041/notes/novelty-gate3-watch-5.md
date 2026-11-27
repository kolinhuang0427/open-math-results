# Novelty Receipt — Gate 3 (`watch-5`)

- **Target:** `targets/oeis-A215041/` (`OEIS:A215041` rev. 10, `OEIS:A193681` rev. 24, `arXiv:1210.1018v2` Open Problem #1)
- **Timestamp (UTC):** `2026-11-27T11:30Z`
- **Verdict:** **PASS**

## Live Checks (<1h)

1. `tools/novelty_grep.py A215041 A193681 A187360 A193679 1210.1018`: `0` lines across `0/653` snapshot files.
2. `tools/arxiv_fetch.py query 'id:1210.1018 OR all:A215041'`: `1210.1018v2` (`2017-03-07`) remains latest version, `0` other entries.
3. Live OEIS JSON: `A215041` rev. `10` (`2023-12-25`) and `A193681` rev. `24` (`2024-10-22`) unchanged.
4. Zenodo live API (`"A215041"`, `"1210.1018"`, `"A193681"`): `0` hits.
5. Newly discovered ledgers checked directly: `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`) `0` hits; Lien-Hung Su Zenodo `24366920` `0` hits; Alexander R. Cohen Zenodo `24384895` `0` hits.
6. Verified required files present: `targets/oeis-A215041/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`.
