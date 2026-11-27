# Gate 2 Novelty Receipt (`watch-1`): `targets/maric-2603.08876-conj1/`

- **Checked UTC:** `2026-11-27T10:21:42Z`–`2026-11-27T10:21:55Z`
- **Target:** Nevena Marić, *"Hierarchical threshold structure in Max-Cut with geometric edge weights"*, `arXiv:2603.08876v1` (`2026-03-09`), Section 5, Conjecture 5.1 (`\label{conj:global}`: Global Optimality of $k$-isolated cuts $C_k$ for $n \ge 7$ and $r \in (r_k(n), r_{k-1}(n))$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "2603.08876" "Maric" "Marić"` after Sweep 26 refresh):** `19` lines across `8/618` files — `watch/snapshots/arxiv/citing_papers.{json,md}` indexing `2603.08876` (`OpenAlex cited_by=0; S2=0`), plus unrelated `Marić`/`Marica` matches (`plasma-ai__erdos` C. R. Marić irrationality series, `erdos-frontier-atlas` SAT/DRAT order types, Mathlib `MaricaSchoenheim.lean`). `0` hits in `1337isnot1337/solved-conjectures` (`10:20Z`), `trureturing*`, `openai/math`, or `formal-conjectures`.
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list "2603.08876"`):** Sole version remains `2603.08876v1` (`2026-03-09T19:41:42Z`).
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2603.08876&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "2603.08876"`):** `0` issues, `0` PRs, `0` repos.
5. **Web search (`"2603.08876" OR ("Marić" "Maric" "Conjecture 5.1" OR "Conjecture 1")`): `0` external proofs or settlements found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot was refreshed at `2026-11-27T10:20:09Z` (Sweep 26) and live `gh search issues/prs/repos` at `10:21Z` returned `0` hits.
