# Gate 2 Novelty Receipt — `ferrero-2511.16335-conj1.8`

- **UTC Time:** 2026-11-26T20:06:15Z
- **Reviewer:** `watch-5` (arXiv & citing-papers slice)
- **Verdict:** **PASS** (no arXiv preprint, journal paper, or OpenAlex citing work found settling Conjecture 1.8 of Ferrero–Hall–Hogben–Hunnell–Small)

## Sources & Exact Queries Checked

1. **Local arXiv snapshot (`watch/snapshots/arxiv/recent_arxiv.json`, 440 recent papers across `math.CO`, `math.NT`, `cs.DM`, `math.GR`):**
   - Keyword scan for `2511.16335`, `ferrero`, `hogben`, `hunnell`, `standard fast join`, `propagation time`, `zero forcing`.
   - Matches: `2611.10985v2`, `2611.13244v2` (checked abstracts via `tools/arxiv_fetch.py` — see near misses below).
2. **Live arXiv API via `tools/arxiv_fetch.py` (`use_cache=False`):**
   - `id_list=["2511.16335"]` -> remains `2511.16335v1` (`2025-11-20T13:15:25Z`), no `v2` or erratum/refutation comment.
   - `all:2511.16335 OR all:"standard fast join" OR all:"fixed propagation time" OR (all:"zero forcing" AND all:"propagation time" AND all:"fast join")` (`max_results=15`) -> returned `2511.16335v1` plus 3 unrelated physics papers.
   - `cat:math.CO AND all:"zero forcing" AND all:"propagation time"` (`max_results=15`, `sort_by="submittedDate"`) -> returned 15 papers (`2609.35522v1`, `2602.16300v1`, `2512.01429v1`, `2511.16335v1`, etc.).
3. **OpenAlex live API (`https://api.openalex.org/works`):**
   - `search="Zero forcing propagation time intervals and graphs with fixed propagation time"` -> matched `W4416550551` (`2026-10-01`, DOI `https://doi.org/10.48550/arxiv.2511.16335`, **`cited_by_count: 0`**).
   - `search="2511.16335"` -> `0` results.
   - `search="standard fast join zero forcing"` -> `0` relevant matches.
4. **Web search (`search_web`):**
   - `"2511.16335" OR "Zero forcing propagation time intervals and graphs with fixed propagation time" OR "standard fast join"`
   - `"standard fast join" OR "PTbar" OR "fixed propagation time" "zero forcing" counterexample OR disproved OR "C_6[2K_1]" OR "Circ(12"`
   - `"Zero forcing propagation time intervals and graphs with fixed propagation time" "Australasian Journal of Combinatorics" OR "374" "394"` -> confirms journal appearance in *Australasian Journal of Combinatorics*, Vol. 96 (2026), pp. 374–394, with no mention of Conjecture 1.8 being refuted or resolved.

## Near Misses (Why They Do Not Settle Conjecture 1.8)

- `arXiv:2611.13244v2` (Kim, Kim, Lee, Nov 2026, *"Stabilization of zero forcing numbers of finite quotients of periodic graphs"*): computes zero forcing number $Z(G)$ on generalized Petersen and circulant covers, does not study $\overline{\mathrm{pt}}(G) = 1$ or standard fast joins.
- `arXiv:2611.10985v2` (Mukherjee & Ray, Nov 2026, *"On the connected zero forcing polynomial of finite trees"*): studies connected zero forcing polynomials of trees, unrelated to Conjecture 1.8.
- `arXiv:2609.35522v1` (McKay, Ray, Valliere, Sep 2026, *"Maximizing the discrepancy between zero forcing parameters relative to graph order"*): bounds the discrepancy between maximum and minimum propagation times of minimum zero forcing sets ($\overline{\mathrm{pt}}(G) - \underline{\mathrm{pt}}(G)$), does not classify graphs with $\overline{\mathrm{pt}}(G) = 1$ or address standard fast joins.
- `arXiv:2602.16300v1` & `arXiv:2512.01429v1`: probabilistic/randomized zero forcing, unrelated to deterministic $\overline{\mathrm{pt}}(G) = 1$.

## What Was Not Covered

- Semantic Scholar live API (rate-limited HTTP 429).
- Closed-access/unindexed papers not present on arXiv, OpenAlex, or web search.
- GitHub repositories (covered separately by `watch-1` and `watch-6`).
