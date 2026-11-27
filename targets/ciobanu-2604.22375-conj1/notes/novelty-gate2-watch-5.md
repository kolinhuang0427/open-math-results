# Gate 2 Novelty Receipt — targets/ciobanu-2604.22375-conj1 (watch-5)

- **Checked UTC:** 2026-11-27T09:49:40Z – 2026-11-27T09:50:06Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2604.22375 Ciobanu "VPL"`):** `2604.22375` matched only `watch/snapshots/arxiv/citing_papers.json` (own sweep entry `cited_by=0`); `0` solution hits across `608` files (`VPL` matched only unrelated substring `SupNormEpsDerivPlusIntegral`/`DevPlatform`).
2. **arXiv API (`tools/arxiv_fetch.py query`):** `2604.22375v1` (`2026-04-24`, DLT 2026) is the sole version; `abs:"2604.22375"` = `0` entries.
3. **Live OpenAlex, Semantic Scholar & Zenodo (`2604.22375`):** OpenAlex `cited_by=0`; Semantic Scholar `0` citations; Zenodo `0` hits.
4. **Web search (`search_web` `"2604.22375" OR ("Ciobanu" "VPL" "REG") ...`):** returns only `2604.22375v1`; `0` resolutions of Conjecture 1 found.

## Coverage Limits
- Non-indexed private repositories or papers not citing `2604.22375` in indexed metadata/abstracts are not covered.
