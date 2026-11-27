# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A215041/`

- **Checked (UTC):** `2026-11-27T11:21:23Z`
- **Checker:** `watch-1` (snapshot corpus: `652` files)
- **Result:** **PASS** — OEIS `A215041` / `arXiv:1210.1018v2` Wolfdieter Lang discriminant quotient conjecture remains marked `Conjectures for a(n), n>=2:` with no prior proof found.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A215041" "1210.1018"`):**
   - `0` lines across `0/652` files (`0.84s` combined query).
2. **Zenodo & Cohen OEIS IDs Indexes (`watch/snapshots/zenodo-23112421-oeis-ids.md`, `zenodo-23114921-oeis-ids.md`, `cohen-zenodo-24384895-oeis-ids.md`):**
   - `0` matches for `A215041`, `A193681`, `A187360`, `A193679`, `A055034`.
3. **arXiv API (`tools/arxiv_fetch.py query --id-list 1210.1018`):**
   - `1210.1018v2` (`2017-03-07`) remains latest version of Lang's paper (lists this as Open Problem).
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A215041&fmt=json`):**
   - Revision `10`; formula still explicitly marked `a(1) = 1. Conjectures for a(n), n>=2: i) a(2^k) = 2, k>=1; ...`.
5. **Zenodo API (`https://zenodo.org/api/records?q=...` for `"A215041"`, `"1210.1018"`):**
   - `total: 0` for both.
6. **GitHub (`gh search issues/prs`):**
   - `0` relevant hits (`trureturing#24901`/`#23509` are unrelated Wolfdieter Lang / Jeffery OEIS conjectures `A052750`/`A052952`).
7. **Web Search (`search_web`):**
   - `"A215041" OR "1210.1018" "Wolfdieter Lang" discriminant conjecture OR proof` — references only OEIS `A215041` and `arXiv:1210.1018`; no prior proof found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
