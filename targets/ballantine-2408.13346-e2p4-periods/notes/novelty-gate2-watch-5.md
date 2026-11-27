# Gate 2 Novelty Receipt — targets/ballantine-2408.13346-e2p4-periods (watch-5)

- **Checked UTC:** 2026-11-27T09:23:33Z – 2026-11-27T09:25:08Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2408.13346 Ballantine e2p4`):** `0` hits for the conjectural `e_2p_4(n) mod m` minimal-period table (`m=10` period `1150`, `m=18` period `1246`); `trureturing` `ballantine2024elementary.md` verified via `gh api` to concern `arXiv:2409.11268` Conjecture 16.
2. **arXiv API (`tools/arxiv_fetch.py query`):** `2408.13346v1` sole version; `abs:"2408.13346"` = `0` hits; inspected abstracts of Semantic Scholar citing preprints (`2609.21922v1`, `2606.19796v1`, `2606.02683v1`, `2606.00420v3`, `2605.06706v2`, `2604.17424v1`, `2510.01100v1`, `2506.04459v2`) — none addresses `e_2p_4(n) mod m` minimal periods.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2408.13346&size=5`):** `0` hits.
4. **Live OpenAlex + Semantic Scholar:** `W4406937392` (`cited_by=9`) and S2 `9` citing papers inspected; none refutes the `m=10` (`1150` vs `1200`) or `m=18` (`1246` vs `1296`) table entries.
5. **Web search (`search_web` `"2408.13346" ... "1150" OR "1246"`):** no correction or refutation found.

## Coverage Limits
- Non-indexed private repos or paywalled papers not mentioning `2408.13346` / `e_2p_4(n)` in indexed metadata/abstracts are not covered.
