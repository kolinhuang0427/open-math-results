# Gate 3 Novelty Receipt (`watch-1`): `targets/guo-2412.02932-conj5.7/`

- **Checked UTC:** `2026-11-27T10:18:57Z`–`2026-11-27T10:19:30Z` (post-`AUDIT.md` PASS)
- **Target:** Peter L. Guo and Zhuowei Lin, *"Schubert polynomials and patterns in permutations"*, `arXiv:2412.02932v1` (`2024-12-04`), Section 5.2, Conjecture 5.7 (`\label{locond-3}`, refuted by $u = 134562897 \in S_9$ with $\theta_u = 113, d_u = -1$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "2412.02932" "134562897" "locond-3"`):** `12` lines across `3/618` files, all within `watch/snapshots/arxiv/{citing_papers.json,citing_papers.md,last_sweep_report.json}` indexing `arXiv:2412.02932` (`OpenAlex cited_by=5; S2=5`); `0` hits in `1337isnot1337/solved-conjectures`, `trureturing*`, `openai/math`, `formal-conjectures`, or `watch/snapshots/discovered/`.
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list "2412.02932"` & citing papers `2610.36993,2609.02050,2605.10276,2512.04053`):** `2412.02932v1` (`2024-12-04T01:04:08Z`) remains the sole version; none of the citing abstracts resolves Conjecture 5.7 ($d_u \ge 0$).
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2412.02932&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "2412.02932"`):** `0` issues, `0` PRs, `0` repos.
5. **Web search (`"2412.02932" OR ("Guo" "Lin" "Conjecture 5.7" "134562897" OR "bumping" OR "inversion")`): `0` refutations or settlements found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot was last synced at `2026-11-27T09:50:27Z` (Sweep 25, ~29 min before this check); live `gh search` at `10:18Z` showed no GitHub matches.
