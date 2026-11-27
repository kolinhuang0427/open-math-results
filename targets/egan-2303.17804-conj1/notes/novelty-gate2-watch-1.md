# Gate 2 Novelty Receipt (`watch-1`): `targets/egan-2303.17804-conj1/`

- **Checked UTC:** `2026-11-27T10:44:26Z`–`2026-11-27T10:44:54Z`
- **Target:** Benjamin Egan and Yuri Nikolayevsky, *"On triangular biregular degree sequences"*, `arXiv:2303.17804v1` (`2023-03-31`, *Discrete Math.* 347(2) 2024 Art. 113778), Section 1 Conjecture (every graphical sequence with $d_{\min} \ge 4$ admits a simple triangular realisation)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "2303.17804" "113778" "triangular realisation" "triangular realization" "Nikolayevsky"`):** `9` lines across `6/619` files — `watch/snapshots/arxiv/{citing_papers.json,citing_papers.md,last_sweep_report.json}` indexing `2303.17804` (`OpenAlex cited_by=1; S2=1`, citing `arXiv:2311.00110` *Degree Sequences of Triangular Multigraphs*, DOI `10.37236/12518`, multigraphs only), `1337/closed_issues.md:158` citing unrelated `Annor–Nikolayevsky–Payne` (`2412.19560`), and a SHA-256 `113778` substring. `0` hits settling the simple-graph conjecture across `619` files.
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list "2303.17804"`):** Sole version remains `2303.17804v1` (`2023-03-31T05:26:45Z`).
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2303.17804&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "2303.17804"`):** `0` issues, `0` PRs, `0` repos.
5. **Web search (`"2303.17804" OR "10.1016/j.disc.2023.113778" OR ("Egan" "triangular" "degree sequence" "4" "proved")`): `0` simple-graph resolutions found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:20:09Z` (Sweep 26) and live `gh search` at `10:44Z` returned `0` hits.
