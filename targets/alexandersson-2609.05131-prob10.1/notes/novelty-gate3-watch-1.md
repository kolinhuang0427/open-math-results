# Gate 3 Novelty Receipt — `targets/alexandersson-2609.05131-prob10.1/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T12:06Z`
- **Target:** Per Alexandersson, `arXiv:2609.05131v2` (*Real-rootedness and interlacing for parking functions and Chow polynomials*, `2026-09-23`), Section 10 **Problem 10.1** (`\label{prob:consecutiveChowInterlacing}` — $H_{\mathrm{NC}_{n+1}}(t) \ll H_{\mathrm{NC}_{n+2}}(t)$).
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`709` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 29, `insorrowmeow/oeis-sequence-proofs`, Zenodo compendia, `mylesparslow`, & Sweep 7 newly indexed repos):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2609.05131" "consecutiveChowInterlacing"` (`12:06Z`) -> `7` lines across `4/709` files: only `closed_issues.md:246`, `citing_papers.{json,md}` (`2611.07267v1`, Ferreri–Martinez lucky-set enumeration), and `last_sweep_report.json`.
2. **Live arXiv & Zenodo APIs (`12:06Z`):**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2609.05131` -> `2609.05131v2` (`2026-09-23T12:23:46Z`) remains latest.
   - `curl -s "https://zenodo.org/api/records?q=2609.05131&size=3"` -> `0` hits.
3. **Live GitHub & Web Search (`12:06Z`):**
   - `gh search issues '"2609.05131"'` -> only `PerAlexandersson/RealRooted#665` (`closed`, Theorem 3.1 Smirnov transfer only); `gh search prs '"2609.05131"'` -> `0`.
   - `search_web` -> returns only `arXiv:2609.05131`; no proof of Problem 10.1 found.

## Near-Misses & Coverage Limits
- **Near-misses:** `arXiv:2611.07267v1` (Ferreri–Martinez, lucky sets) and `PerAlexandersson/RealRooted#665` (Theorem 3.1 only).
- **Coverage limits:** Private repositories and works without `2609.05131` or `consecutiveChowInterlacing` identifiers are not covered.
