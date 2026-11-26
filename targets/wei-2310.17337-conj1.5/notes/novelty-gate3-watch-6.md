# Gate 3 Novelty Receipt (Pre-Report) — `wei-2310.17337-conj1.5`

- **Verdict:** **PASS** (no new public proof or counterexample found in the pre-report window)
- **Checked at (UTC):** 2026-11-26T20:23:09Z
- **Watcher:** `watch-6`

## Sources Checked

1. All local `watch/snapshots/**` via `.venv/bin/python tools/novelty_grep.py 2310.17337 10.1142/s1793830926500679 "C_k-isolation" "C_4-isolation" "C_8-isolation" "Wei-Zhang-Zhao"`.
2. Live GitHub search (`gh search repos`, `gh search issues`).
3. Live arXiv API via `.venv/bin/python tools/arxiv_fetch.py query --id-list 2310.17337`.
4. Live OpenAlex API (`https://api.openalex.org/works/https://doi.org/10.1142/s1793830926500679` and citing works `filter=cites:W7163506673`).
5. Web search (`search_web`).

## Exact Queries

- `.venv/bin/python tools/novelty_grep.py 2310.17337 10.1142/s1793830926500679 "C_k-isolation" "C_4-isolation" "C_8-isolation" "Wei-Zhang-Zhao"`
- `gh search repos "2310.17337 OR s1793830926500679"`
- `gh search issues "\"2310.17337\" OR \"s1793830926500679\" OR \"C_k-isolation\""`
- `.venv/bin/python tools/arxiv_fetch.py query --id-list 2310.17337`
- OpenAlex `W7163506673` (`cited_by_count: 3`) + `cites:W7163506673`
- `search_web`: `"10.1142/s1793830926500679" OR "2310.17337" "C_k-isolation" OR "counterexample" OR "truncated tetrahedron"`

## Findings & Near Misses

- `arXiv:2310.17337v1` has no newer arXiv version.
- OpenAlex `W7163506673` (`10.1142/s1793830926500679`, published `2026-07-21`) has 3 citing works (`10.1016/j.dam.2025.06.058` *Cycle isolation in graphs*, `10.12677/aam.2025.149398` *Total Isolation Number of the Cartesian Product of Paths and Cycles*, `10.1016/j.dam.2026.08.006` *Isolation of non-triangle cycles in graphs* = `arXiv:2510.08361`), none of which settles or refutes Conjecture 1.5 (see `AUDIT.md`).
- Zero matches in `watch/snapshots/**` (beyond `watch-5`'s citing cache), GitHub repos/issues, or web search.

## What Was Not Covered

- The paywalled full-text PDF of `10.1142/s1793830926500679` (noted in `AUDIT.md` Section 4: the published DMAA abstract states *"For general $k$, it is worth noting that the problem on $C_k$-isolation remains open"*).
- Private repositories and non-indexed articles.
