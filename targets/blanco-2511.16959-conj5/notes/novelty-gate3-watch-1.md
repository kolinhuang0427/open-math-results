# Gate 3 Novelty Receipt — `blanco-2511.16959-conj5`

- **UTC Time:** 2026-11-27T04:10:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 14 (`2026-11-27T03:21:32Z`) `watch/snapshots/1337-solved-conjectures/` -> `0` hits for `2511.16959` or prefix reversals.
2. **Live competing repos (`gh api`, read-only):**
   - Issue searches for `2511.16959` in `1337isnot1337/solved-conjectures` (`0`), `facebookresearch/atlas-lean` (`0`), and `the-omega-institute/trureturing` (`#20814` open preregistration, `#22875` Conj 1, `#7558`/`#7577` Conj 4 — none settling Conj 5).
   - Full file trees of `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform` (Conj 1–4 traces only), `valyuAI/research`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `trureturing-tools`, `DomTheDeveloper/open-math-agents`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath` -> `0` matches for `con:F_k(n)`.
3. **Live arXiv & Zenodo API:**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list ...,2511.16959,...` -> `2511.16959v3` (*DMTCS* vol. 28:1, Sep 24, 2026) latest version.
   - `https://zenodo.org/api/records?q=2511.16959&size=5` -> `total: 0`.

## What Was Not Covered

- Closed-access venues and private repositories; `atlas-lean` & `CrocSwap` root trees were `truncated=True`, checked additionally via `search/issues`.
