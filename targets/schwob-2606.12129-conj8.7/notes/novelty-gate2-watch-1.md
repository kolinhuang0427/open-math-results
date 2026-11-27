# Gate 2 Novelty Receipt (`watch-1`): `targets/schwob-2606.12129-conj8.7/`

- **Checked UTC:** `2026-11-27T10:40:10Z`–`2026-11-27T10:40:32Z`
- **Target:** Ludovic Schwob, *"Middle orders: all distributive lattices between weak and Bruhat"*, `arXiv:2606.12129v1` (`2026-06-10`), Section 8, Conjecture 8.7 (`\label{cnj:Dtype}`, all middle orders on $D_n$ are minuscule middle orders)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "2606.12129" "Schwob" "cnj:Dtype"`):** Only `watch/snapshots/arxiv/citing_papers.{json,md}` indexing this target (`OpenAlex cited_by=0; S2=0`); `0` settlement hits across `619` files (`1337isnot1337/solved-conjectures` refreshed `10:20:09Z`, `trureturing*`, `openai/math`, `formal-conjectures`, `watch/snapshots/discovered/`).
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list "2606.12129"`):** Sole version remains `2606.12129v1` (`2026-06-10T14:22:22Z`).
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2606.12129&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "2606.12129"`):** Only unrelated `the-omega-institute/trureturing#22269` (*Open problem: Lia...*); `0` PRs and `0` repos.
5. **Web search (`"2606.12129" OR ("Schwob" "Conjecture 8.7" OR "cnj:Dtype" OR "interval" "poset")`): `0` competing proofs found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:20:09Z` (Sweep 26) and live `gh search` at `10:40Z` returned no math matches on `cnj:Dtype`.
