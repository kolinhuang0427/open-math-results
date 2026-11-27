# Gate 2 Novelty Receipt — `ferrero-2511.16335-conj1.8`

- **Verdict:** **PASS** (no prior proof or counterexample found for Conjecture 1.8 of `arXiv:2511.16335v1`)
- **Checked at (UTC):** 2026-11-26T20:06:15Z
- **Watcher:** `watch-6`

## Sources Checked

1. Local watch snapshots under `/Users/kev/Documents/open-math/watch/snapshots/` (`1337-solved-conjectures`, `openai-math`, `erdosproblems`, `ai-collections`, `formal`, `arxiv`, `discovered`).
2. Live GitHub search (`gh search repos`, `gh search code`, `gh search issues`) and live API inspection of `the-omega-institute/trureturing/issues/8371`.
3. Live arXiv API via `.venv/bin/python tools/arxiv_fetch.py`.
4. Web search (`search_web`).

## Exact Queries

- `grep -riE "2511\.16335|ferrero" /Users/kev/Documents/open-math/watch/snapshots/`
- `gh search repos "2511.16335"`
- `gh search code "2511.16335"`
- `gh search code "Ferrero" "1.8" "Circ"`
- `gh search code "standard fast join"`
- `gh search code "fixed propagation time"`
- `gh search issues "2511.16335"`
- `gh search issues "standard fast join"`
- `gh api "repos/the-omega-institute/trureturing/issues/8371"` and `.../comments`
- `.venv/bin/python tools/arxiv_fetch.py query --id-list 2511.16335`
- `.venv/bin/python tools/arxiv_fetch.py query 'all:"propagation time" AND all:"zero forcing"' --max-results 10`
- `search_web`: `"2511.16335" OR "Ferrero" "Conjecture 1.8" OR "Circ(12,{1,5})" counterexample OR disproved OR proved`
- `search_web`: `"2511.16335" "Ferrero" graph conjecture`

## Near Misses & Why They Do Not Settle Conjecture 1.8

- `the-omega-institute/trureturing/issues/8371` (*"Research: fixed standard zero forcing time (Conjecture 1.8)"*, closed `2026-09-16T23:35:45Z`): Explicitly ended as `terminal OPEN` with no proof, no counterexample, no finite scan, and no project files changed.
- `1337isnot1337/solved-conjectures/issues/323`: Open claim on the Boyer–Brimkov–English–Ferrero–Keller–Kirsch–Phillips–Reinhart path-extremal zero-forcing conjecture $z(G;k) \le z(P_n;k)$ — a completely different conjecture.
- `arXiv:2511.16335v1` itself (Theorem 5.10, Corollary 5.12): Proves Conjecture 1.8 only when $G$ is already a join of two graphs or $\mathbb{Z}(G) \ge n-2$; leaves the general connected case (where $\overline{G}$ is connected and $\mathbb{Z}(G) = n-4$, as in $C_6[2K_1]$) open.
- `arXiv:2609.35522v1` (McKay, Ray, Valliere, Sep 2026): Studies discrepancy between max and min propagation times of minimum zero forcing sets; does not characterize $\overline{\mathrm{PT}}(G) = 1$ or refute Conjecture 1.8.

## What Was Not Covered

- *Australasian Journal of Combinatorics* (where `trureturing#8371` noted the paper was listed as accepted/to appear) beyond public web search; private repositories; and papers not indexed on arXiv or GitHub code search.
