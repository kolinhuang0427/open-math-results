# Gate 2 Novelty Receipt — targets/mbirika-2204.12626-ques6.1 (watch-5)

- **Checked UTC:** 2026-11-27T09:32:04Z – 2026-11-27T09:32:54Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... 2204.12626 Mbirika`):** `8` hits across `2/608` files (`the-omega-institute/trureturing`); inspected `Problems/mbirika-spilker-gibonacci-power-gcd-normalization.md` (addresses Question 6.2 $d^e$ scaling, not Question 6.1 $\mathcal{F}^3(k)$ / $\mathcal{L}^3(k)$) and `Library/ArithUnits/fiebigmbirikaspilker2025lucas.md` (addresses `arXiv:2408.14632v2` Conjecture 5.2).
2. **arXiv API (`tools/arxiv_fetch.py query`):** `2204.12626v2` (`2023-01-13`, *Fibonacci Quarterly* 60(5)) is the latest version; `abs:"2204.12626"` = `0` entries; inspected later Mbirika papers (`2511.10797v2`, `2408.14632v2`, `2301.05758v3`) — none resolves Question 6.1 cubes.
3. **Live OpenAlex & Zenodo (`2204.12626`):** OpenAlex `cited_by=1`; Zenodo `0` hits (Semantic Scholar returned HTTP 429).
4. **Web search (`search_web` `"2204.12626" OR ("Mbirika" "Fibonacci" "Lucas" "Question 6.1")`):` returns only `2204.12626`; `0` refutations of Question 6.1 found.

## Coverage Limits
- Semantic Scholar API returned HTTP 429; non-indexed private repos or paywalled papers not mentioning `2204.12626` are not covered.
