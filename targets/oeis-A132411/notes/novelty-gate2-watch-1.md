# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A132411/`

- **Checked UTC:** `2026-11-27T10:27:28Z`–`2026-11-27T10:27:36Z`
- **Target:** OEIS `A132411` (rev. 80) — Peter Bala (May 10 2025) $q$-series expansion conjecture: $\sum_{n \ge 0} q^{2n} \prod_{k \ge 2n+2} (1 - (-q)^k) = 1 + q^3 + q^8 + q^{15} + q^{24} + \dots$
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "A132411" "132411" "m^2-1"` & `grep zenodo-23112421-oeis-ids.md`):** `0` hits for `A132411`/`132411` across `618` files (`m^2-1` matched only an unrelated tensor lower bound in `0thernes-research-archive`), and absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`.
2. **Live OEIS (`https://oeis.org/search?q=id:A132411&fmt=json`):** `ID: 132411`, `rev: 80` (`time: 2026-01-22T07:45:32-05:00`); `COMMENT` still reads `Conjecture: the sequence terms are the exponents in the expansion of the q-series... - _Peter Bala_, May 10 2025`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A132411&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "A132411"`):** Only unrelated `nbbrd/sdmx-upptime #28139`; `0` PRs and `0` repos.
5. **Web search (`"A132411" "Bala" OR "Gauss" OR "theta" OR "conjecture"`):** `0` external proofs found (points only to OEIS `A132411`).

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:20:09Z` (Sweep 26) and live `gh search issues/prs/repos` at `10:27Z` found no math/OEIS matches.
