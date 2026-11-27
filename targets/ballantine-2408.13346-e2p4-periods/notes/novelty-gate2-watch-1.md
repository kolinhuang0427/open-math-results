# Gate 2 Novelty Receipt (`watch-1`): `targets/ballantine-2408.13346-e2p4-periods/`

- **Checked UTC:** `2026-11-27T09:24Z`
- **Target:** Cristina Ballantine, George Beck, and Mircea Merca, *"Partitions and elementary symmetric polynomials -- an experimental approach"*, `arXiv:2408.13346v1` (`2024-08-23`), Section 1, conjectural table of minimal periods for $e_2p_4(n) \pmod m$
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... 2408.13346 Ballantine ...`):** `0` hits for `2408.13346` across `608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`). `Ballantine` hits in `trureturing` and `atlas-lean#10666` concern `arXiv:2409.11268v3` / Merca part-sum identities, not $e_2p_4(n)$ periods.
2. **Live GitHub (`gh search issues "2408.13346"`):** Only hit is `the-omega-institute/trureturing#8751` (`arXiv:2409.11268v3` §5), unrelated.
3. **Live arXiv (`tools/arxiv_fetch.py query --id-list 2408.13346,2208.14707`):** `2408.13346v1` (`2024-08-23T19:41:53Z`) remains the sole arXiv version.
4. **Live Zenodo API (`https://zenodo.org/api/records?q=2408.13346&size=5`):** `0` hits.
5. **Web search (`"2408.13346" OR ("Ballantine" "Beck" "Merca" "e_2p_4")`):** `0` corrections/refutations of the minimal-period table ($m=10, 18$, etc.) found.
