# Gate 2 Novelty Receipt — `li-2505.12035-conj7`

- **UTC Time:** 2026-11-26T23:59:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 8 (`2026-11-26T23:43:05Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py ... 2505.12035 "Li–Lu–Luo"` -> 0 hits across `watch/snapshots/**`.
2. **Live `1337isnot1337/solved-conjectures`, `trureturing`, `trureturing-tools`, `aliromman/math`, `KnowledgeSense/math` (`gh api`, read-only):**
   - `search/issues?q=repo:1337isnot1337/solved-conjectures+"2505.12035"` -> 0; `search/issues?q=repo:the-omega-institute/trureturing+"2505.12035"` -> 0.
   - Global `search/issues?q="2505.12035"` -> 0; global `search/code?q=2505.12035` -> 8 items (RSS metadata and unrelated CSVs only).
   - `aliromman/math` (all PRs): 0 matches for `2505.12035` / `Berge`.
   - `KnowledgeSense/math` (5,377 tree files): only unrelated `Zeros-of-the-Independence-Polynomials-of-Uniform-Linear-Hypercombs`.
3. **Live arXiv, Zenodo API & web search:**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2509.16034,2505.12035` -> `2505.12035v1` sole entry.
   - `https://zenodo.org/api/records?q=2505.12035&size=5` -> `total: 0`.
   - `search_web` for `"2505.12035" ("Conjecture 7" OR "disproved")` -> no refutation or resolution found.

## What Was Not Covered

- Private repositories and non-indexed post-2025 manuscripts.
