# Gate 2 Novelty Receipt — `targets/alexandersson-2609.05131-prob10.1/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:43Z`
- **Target:** Per Alexandersson, `arXiv:2609.05131v2` (*Real-rootedness and interlacing for parking functions and Chow polynomials*, updated `2026-09-23`), Section 10 **Problem 10.1** (`\label{prob:consecutiveChowInterlacing}` — strict interlacing $H_{\mathrm{NC}_{n+1}}(t) \ll H_{\mathrm{NC}_{n+2}}(t)$ for every $n$).
- **Verdict:** **PASS** (`0` prior proofs found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2609.05131" "consecutiveChowInterlacing"` -> `7` lines across `4/658` files: only `closed_issues.md:246` (notes `2609.05131v2` has no excedance claim), `arxiv/citing_papers.{json,md}` (`OpenAlex cited_by=1; S2=1`: `arXiv:2611.07267`), and `last_sweep_report.json`.
   - Checked citing paper `arXiv:2611.07267v1` (Melanie Ferreri & Lucy Martinez, *Pattern avoidance classes of parking permutations with fixed lucky sets*, `2026-11-05`) via `arxiv_fetch.py query --id-list 2611.07267` -> enumerates pattern-avoiding parking permutations; does not address `prob:consecutiveChowInterlacing`.
2. **External Compendia Cross-Check:**
   - `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`, PR `#86`) -> `0` hits.
3. **Live arXiv & Zenodo APIs:**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2609.05131` -> `total_results: 1`, `2609.05131v2` (`2026-09-23T12:23:46Z`) remains the latest version.
   - `curl -s "https://zenodo.org/api/records?q=2609.05131&size=3"` -> `0` hits.
4. **Live GitHub & Web Search:**
   - `gh search issues '"2609.05131"'` -> `PerAlexandersson/RealRooted#665` (`closed`, `[Parking functions] Tieless descent transfer to finite Smirnov words`, Theorem 3.1 only); `gh search prs '"2609.05131"'` -> `0`.
   - `search_web` (`"2609.05131" "Alexandersson" OR "consecutiveChowInterlacing" OR "H_{NC" interlacing proof`) -> returns only `2609.05131`; no proof of Problem 10.1 found.

## Near-Misses & Coverage Limits
- **Near-misses:** `arXiv:2611.07267v1` (Ferreri–Martinez, background citation only) and `PerAlexandersson/RealRooted#665` (formalizes Theorem 3.1 Smirnov transfer only).
- **Coverage limits:** Private repositories and works without `2609.05131` or `consecutiveChowInterlacing` identifiers are not covered.
