# Gate 2 Novelty Receipt — targets/bartnicki-2303.08771-conj3 (watch-5)

- **Checked UTC:** 2026-11-27T09:28:32Z – 2026-11-27T09:28:49Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2303.08771 Bartnicki Grytczuk`):** `7` hits across `3/608` files (unrelated Grytczuk papers on shuffle squares / AP / fractional coloring); `0` hits for `2303.08771` or strong arboricity.
2. **arXiv API (`tools/arxiv_fetch.py query`):** `2303.08771v1` (`2023-03-15`) is the sole version; `abs:"2303.08771"` = `0` entries.
3. **Live OpenAlex, Semantic Scholar & Zenodo (`2303.08771`):** OpenAlex `cited_by=0`; Semantic Scholar `0` citations; Zenodo `0` hits.
4. **Web search (`search_web` `"2303.08771" OR "Bartnicki" "Grytczuk" "zeta" OR "coloring number" "counterexample"`):** returns only `Strong arboricity of graphs`; `0` refutations found.

## Coverage Limits
- Non-indexed private repos or papers not citing `2303.08771` in indexed metadata/abstracts are not covered.
