# Gate 2 Novelty Receipt — `cooper-2302.00757-conj11.2`

- **UTC Time:** 2026-11-27T00:48:00Z
- **Reviewer:** `watch-2` (co-covering Gate 2 per coordinator #508)
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/snapshots/**`):**
   - `.venv/bin/python tools/novelty_grep.py "2302.00757" "Cooper" "T_11"`: hits only `1337-solved-conjectures` Cooper–Hollars Conjecture 1.1 (`arXiv:2607.15486`, Erdős #611, unrelated); 0 hits in `openai-math`, `erdosproblems`, `ai-collections`, `formal`, `arxiv`, `discovered`.
2. **arXiv (`tools/arxiv_fetch.py`):**
   - `query --id-list 2302.00757` -> `2302.00757v2` (updated `2024-05-08T00:29:10Z`, no journal-ref/DOI) remains the latest version.
3. **Live GitHub (`gh api`, read-only):**
   - Checked `pushed_at` of `1337isnot1337/solved-conjectures` (`2026-11-27T00:37:08Z`), `the-omega-institute/trureturing` (`2026-11-27T00:36:21Z`), `the-omega-institute/trureturing-tools` (`2026-11-27T00:37:13Z`), `aliromman/math` (`2026-11-27T00:36:54Z`), `KnowledgeSense/math` (`2026-10-14T07:35:52Z`).
   - Live recursive trees of `aliromman/math` (515 paths), `trureturing-tools` (1764 paths), `KnowledgeSense/math` (5377 paths): 0 matches for `2302`, `cooper`, `T_11`.
   - `search/code?q=2302.00757` (129 total, top 10 inspected) and `search/issues?q=2302.00757` (0 hits).
   - Repo-scoped `search/code` & `search/issues` for `2302.00757` and `Cooper` across the 5 competing repos: `trureturing` hits only Presburger Cooper; `1337` hits only Erdős #611 (Cooper–Hollars).
4. **Zenodo API & Web Search:**
   - `https://zenodo.org/api/records?q=2302.00757+OR+%22Shaun+Cooper%22+supercongruence&size=10` (43 hits inspected top 5 — none address `T_{11}` mod 9 / mod 25).
   - `search_web` for `"2302.00757" "supercongruence" OR "T_{11}" OR "T_11" Cooper`: returns only `2302.00757` itself.

## Near Misses & Why They Do Not Settle the Exact Statement

- `rbajaj5/a183068-supercongruence` (`related-results/CooperLevel11RarePrimes.md`, dated 2026-07-26): discusses Cooper's level-11 sequence $T(n)$ and notes Beukers–Tsai–Ye proved the mod-$p$ Lucas congruence $T(pn) \equiv T(n) \pmod p$ for all primes $p$, while explicitly stating the modulo-$p^2$ law remains unproved (`the first-order law remains unproved, 2026-07-26`). Does not settle Conjecture 11.2 (mod $3^2$ and mod $5^2$).

## What Was Not Covered

- Only top 10 global GitHub code-search results for `2302.00757` were inspected individually; closed-access journals and private repositories not indexed by arXiv, GitHub, Zenodo, or web search.
- Also checked live `rainwangphy/aftd-platform` (28,161 tree paths), `valyuAI/research` tree, and `facebookresearch/atlas-lean` issues: 0 matches for `2302.00757` / `T_11`.
