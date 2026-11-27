# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A108449/`

- **Checked UTC:** `2026-11-27T09:18Z`
- **Target:** OEIS `A108449` — R. J. Mathar (Jul 26, 2022) D-finite recurrence conjecture ($\sum_{j=0}^8 C_j(n)\,a(n-j)=0$ for $n \ge 8$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A108449 108449`):** `2` lines across `2/608` files (`watch/snapshots/ai-collections/the-omega-institute__trureturing-source-theories/files.txt:6158` and `watch/snapshots/discovered/the-omega-institute__trureturing-source-theories.json:6177`), both purely inside SHA256 digest `09bf203cb38203dbb25fbe5ad6dbf32108449cb49b48dfea84d7c860c8c94801`; `0` matches for `A108449` across all `608` snapshot files (including `1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live OEIS (`https://oeis.org/search?q=id:A108449&fmt=json`):** `1` result (`number: 108449`, updated `2025-11-05T15:35:31-05:00`, rev. 13), matching `TARGET.md`; Mathar's Jul 26, 2022 recurrence remains listed as `Conjecture` with no proof reference.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A108449&size=10` and `q="A108449"+OR+"no+pyramids"&size=10`):** `0` hits (`A108449` returned `total: 0`).
4. **Live GitHub (`gh search issues "A108449"`):** `0` hits (`[]`).
5. **Web search (`"A108449" "Mathar" OR "D-finite" OR "no pyramids"`):** `0` proofs of Mathar's `A108449` recurrence found (only neighboring `A108447` surfaced).

## Coverage Limits
- `gh search prs "A108449"` hit GitHub Search API HTTP 403 rate limit during the parallel batch; mitigated by full `608`-file `watch/snapshots/**` grep (covering `1337isnot1337/solved-conjectures` PRs/issues/results rebuilt at `08:49Z` and `trureturing` file trees) plus live `gh search issues "A108449"` (`0` hits) and live OEIS/Zenodo checks.
