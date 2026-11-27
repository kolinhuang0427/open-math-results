# Gate 2 Novelty Receipt (`watch-1`): `targets/guo-2412.02932-conj5.7/`

- **Checked UTC:** `2026-11-27T09:56Z`
- **Target:** Peter L. Guo and Zhuowei Lin, *"Schubert polynomials and patterns in permutations"*, `arXiv:2412.02932v1` (`2024-12-04`), Section 5.2, Conjecture 5.7 (`\label{locond-3}`)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2412.02932 locond-3 ...`):** Only `watch/snapshots/arxiv/citing_papers.json:2382,2390` indexing this target itself; `0` settlement hits across `618` files (including `1337isnot1337/solved-conjectures` rebuilt `09:50:27Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list 2412.02932`):** `2412.02932v1` (`2024-12-04T01:04:08Z`) remains the sole arXiv version.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2412.02932&size=5`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues "2412.02932"` & `gh search prs "2412.02932"`):** `0` hits (`[]`).
5. **Web search (`"2412.02932" OR ("Guo" "5.7" "Schubert" "Grothendieck" OR "permutation")`): `0` refutations found (surfaced only `arXiv:2412.02932` itself).
