# Gate 2 Novelty Receipt (`watch-6`) — `targets/lau-2208.14707-conj2/`

- **Checked UTC:** `2026-11-27T09:14:15Z`
- **Verdict:** **PASS** (open; no refutation or proof found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 608 files including 436+ `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "2208.14707" "dml.2022.149" "local antimagic"` -> `1` hit (`kyleglsn22-spec/open-problems-lab`, unrelated Bača et al. 2022 tree leaf conjecture); `0` hits for `2208.14707` or `dml.2022.149`.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "2208.14707"` -> `[]`.
   - `gh search issues "2208.14707"` -> `[]`.
   - `gh search code "2208.14707"` -> `[]`.
3. **arXiv & Zenodo API:**
   - `tools/arxiv_fetch.py query --id-list 2208.14707`: `2208.14707v1` (`2022-08-31`) remains sole version.
   - `zenodo.org/api/records?q=2208.14707&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"2208.14707" OR "Lau" "lexicographic" "linear arboricity" OR "local antimagic" counterexample OR proved` -> returns only `arXiv:2208.14707` / *DML* 11 (2023); no refutation found.

## Coverage Limits
- Closed-access venues or private repositories not indexed by arXiv, GitHub, Zenodo, or `search_web` are not covered.
