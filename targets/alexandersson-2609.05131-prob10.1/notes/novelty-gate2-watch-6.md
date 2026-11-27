# Gate 2 Novelty Check (`watch-6`): `targets/alexandersson-2609.05131-prob10.1/`

- **Checked UTC:** `2026-11-27T11:42:40Z`
- **Target:** Per Alexandersson, *"Real-rootedness and interlacing for parking functions and Chow polynomials"*, `arXiv:2609.05131v2` (`2026-09-23`), Section 10, **Problem 10.1** (`\label{prob:consecutiveChowInterlacing}`): $H_{\mathrm{NC}_{n+1}}(t) \ll H_{\mathrm{NC}_{n+2}}(t)$ for every $n$.
- **Verdict:** **PASS** (no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `1337-solved-conjectures`, `trureturing`, `mylesparslow-conjecture-ledger.md`, `zenodo-2026-oeis-compendia-ids.md`, `citing_papers.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py 2609.05131 consecutiveChowInterlacing --max-total 0` -> `7` lines across `4/658` files (`closed_issues.md:246` citing `2609.05131` for a different excedance conjecture, and our own `citing_papers.{json,md}` / `last_sweep_report.json` listing sole S2 cite `arXiv:2611.07267`).
   - Verified `arXiv:2611.07267` (*Pattern avoidance classes of parking permutations with fixed lucky sets*) is unrelated parking-permutation enumeration.
2. **Live arXiv (`.venv/bin/python -u tools/arxiv_fetch.py abs 2609.05131`):** `2609.05131v2` remains the latest version.
3. **Zenodo API (`https://zenodo.org/api/records?q=2609.05131`):** `hits.total: 0`.
4. **GitHub (`gh search repos 2609.05131`, `gh search issues 2609.05131`, `gh search issues "consecutiveChowInterlacing"`, `gh search issues "NC_{n+2}"`):**
   - `gh search repos 2609.05131`: `[]`.
   - `gh search issues 2609.05131`: only `PerAlexandersson/RealRooted#665` (Theorem 3.1 Smirnov transfer, unrelated to Problem 10.1).
   - `consecutiveChowInterlacing`: `[]`; `NC_{n+2}`: 5 unrelated bioinformatics/compiler hits.
5. **Web search (`search_web` for `"2609.05131" Alexandersson "Problem 10.1" OR "consecutiveChowInterlacing" OR "noncrossing partitions" interlacing proof`):**
   - Returned only `arXiv:2609.05131` and its cited Theorem 1.1 background (Chun–Hayashida–Partida–Wang / Leander), leaving Problem 10.1 open.

## Coverage Limits

- arXiv query covers metadata and inspected abstract of sole S2 cite `2611.07267` rather than full PDF texts of unrelated papers; offline or unindexed manuscripts are outside direct visibility.
