# Gate 2 Novelty Receipt — `wei-2310.17337-conj1.5`

- **Verdict:** **PASS** (no settlement or counterexample found for Conjecture 1.5 of `arXiv:2310.17337v1`)
- **Checked at (UTC):** 2026-11-26T20:02:51Z
- **Watcher:** `watch-6`

## Sources Checked

1. Local watch snapshots under `/Users/kev/Documents/open-math/watch/snapshots/` (`1337-solved-conjectures`, `openai-math`, `erdosproblems`, `ai-collections`, `formal`, `arxiv`, `discovered`, including `watch/snapshots/arxiv/citing/wei-2310.17337-conj1.5.json`).
2. Live GitHub search (`gh search repos`, `gh search code`, `gh search issues`).
3. Live arXiv API via `.venv/bin/python tools/arxiv_fetch.py`.
4. Web search (`search_web`).

## Exact Queries

- `grep -riE "C_k-isolation|C_4-isolation|C_5-isolation|C_8-isolation|2310\.17337" /Users/kev/Documents/open-math/watch/snapshots/`
- `gh search repos "2310.17337"`
- `gh search repos "C_4-isolation OR C_k-isolation"`
- `gh search code "2310.17337"`
- `gh search code "C_k-isolation"`
- `gh search code "C_4-isolation"`
- `gh search code "C_8-isolation"`
- `gh search code "On the C_4-isolation number of a graph"`
- `gh search code "C_k-isolating"`
- `gh search code "Wei" "Zhang" "Zhao" "isolation"`
- `gh search code "truncated tetrahedron" "isolation"`
- `.venv/bin/python tools/arxiv_fetch.py query --id-list 2310.17337`
- `.venv/bin/python tools/arxiv_fetch.py query 'all:isolation AND (all:"C_5" OR all:"C_6" OR all:"C_8" OR all:"C_k" OR all:"C_4-isolation")' --max-results 15`
- `search_web`: `"C_k-isolation" OR "C_5-isolation" OR "C_8-isolation" OR "On the C_4-isolation number of a graph" counterexample OR disproved OR "2310.17337"`
- `search_web`: `"iota(G, C_k)" OR "iota(G, C_5)" OR "iota(G, C_8)" "(m+1)/(k+2)" OR "C_k-isolating set"`

## Near Misses & Why They Do Not Settle Conjecture 1.5

- `arXiv:2310.17337v1` (Wei, Zhang, Zhao, Oct 2023): proves $\iota(G, C_4) \le (m+1)/6$ (case $k=4$) and poses Conjecture 1.5 for general $k$.
- `arXiv:2510.08361v2` (Peter Borg, Dayle Scicluna, Oct 2025 / *Discrete Appl. Math.* 394, 2026): proves $\iota(G, \mathcal{C}') \le (m+1)/6$ for the family $\mathcal{C}' = \{C_k : k \ge 4\}$, which isolates *all* cycles of length $\ge 4$ simultaneously rather than bounding $\iota(G, C_k)$ individually by $(m+1)/(k+2)$ for $k \ge 5$ (and specifically $k=8$).
- `arXiv:2503.09795v1` (Geoffrey Boyer, Wayne Goddard, Mar 2025): studies *independent* isolation number (isolating all edges / leaving only isolated vertices), not $C_k$-isolation.
- `watch/snapshots/arxiv/citing/wei-2310.17337-conj1.5.json`: OpenAlex citing count = 0.
- `gh search code` hits on `"Wei" "Zhang" "Zhao" "isolation"` and `"truncated tetrahedron" "isolation"` were unrelated repositories (ML/NLP READMEs, dictionary glossaries, etc.).

## What Was Not Covered

- Paywalled / closed-access journal issues or non-arXiv conference proceedings not indexed by web search, OpenAlex, or GitHub code search.
- Private repositories and articles written without the English phrases `"C_k-isolation"` / `"C_4-isolation"` / `"2310.17337"`.
