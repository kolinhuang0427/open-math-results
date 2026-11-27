# Gate 3 Novelty Check (`watch-6`): `targets/maric-2603.08876-conj1/`

- **Checked UTC:** `2026-11-27T11:41:53Z`
- **Target:** Nevena Marić, *"Hierarchical threshold structure in Max-Cut with geometric edge weights"*, `arXiv:2603.08876v1` (`2026-03-09`), Section 5, **Conjecture 5.1** (`\label{conj:global}`) for $n \ge 7$.
- **Verdict:** **PASS** (<1h freshness confirmed; no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, `zenodo-2026-oeis-compendia-ids.md`, all discovered repos):**
   - `.venv/bin/python -u tools/novelty_grep.py 2603.08876 Maric` -> `17` lines across `7/658` files — our own `citing_papers.{json,md}` (`OpenAlex cited_by=0; S2=0`), unrelated `C. R. Maric` (`E0270` irrationality) and `MaricaSchoenheim.lean` in Mathlib. Zero settlement hits.
2. **Live arXiv (`.venv/bin/python -u tools/arxiv_fetch.py abs 2603.08876`):** `2603.08876v1` remains the sole and latest version.
3. **Zenodo API (`https://zenodo.org/api/records?q=2603.08876`):** `hits.total: 0`.
4. **GitHub (`gh search repos 2603.08876`, `gh search issues 2603.08876`, `trureturing/dev` tree):** `[]`.
5. **Web search (`search_web` for `"2603.08876" Maric Conjecture proof counterexample`):** returned only `arXiv:2603.08876v1`.

## Coverage Limits

- arXiv query did not re-fetch OpenAlex/S2 citations beyond the cached `citing_papers` (`cited_by=0`) and `search_web`; offline or unindexed manuscripts are outside direct visibility.
