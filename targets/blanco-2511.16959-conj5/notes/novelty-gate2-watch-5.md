# Gate 2 Novelty Check — `blanco-2511.16959-conj5` (watch-5)

- **UTC Timestamp:** `2026-11-27T01:35:44Z`
- **Target:** `targets/blanco-2511.16959-conj5/TARGET.md`
- **Verdict:** **PASS** (no public proof or disproof of Blanco et al. `arXiv:2511.16959v3` Conjecture 5 `con:F_k(n)` found across arXiv, Zenodo, Crossref, web search, 369 snapshots, `the-omega-institute/trureturing#20814`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, or `facebookresearch/atlas-lean`)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 369 files):**
   - `"2511.16959" "con:F_k(n)" "F_k(n)" "2610.30892" "Golubyatnikov"` -> `6` unrelated lines (`f_k(n)` in Erdős Problem 979, rollercoasters, `FormalConjectures` #588/#670); `0` hits on `2511.16959`, `2610.30892`, or prefix reversals.

2. **GitHub Live Checks (`gh search` / `gh issue view`, read-only):**
   - `gh issue view 20814 --repo the-omega-institute/trureturing` -> `OPEN`, `comments: []` (*Preregister: whole arXiv2511.16959 Conjecture 5 maximum generating middle-prefix count*).
   - `gh search prs --repo the-omega-institute/trureturing "2511.16959 OR 20814 OR F_k"` -> `0` PRs.
   - `gh search code` (`"2511.16959 OR Blanco OR prefix_reversal"`) across `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, and `facebookresearch/atlas-lean` -> `0` matching code results in all 5 repos.

3. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:2511.16959` -> `1` entry (`2511.16959v3`, `2025-11-21T05:20:27Z`, revised 2026-09-22, DMTCS 28:1).
   - `all:2610.30892` -> `1` entry (`2610.30892v1`, `2026-10-22T08:09:29Z`, Lei–Zhao–Zhu–Wu, proves Conjectures 2–4 only, not Conjecture 5).
   - `all:"prefix reversal" AND all:"symmetric group"` -> `7` entries (none resolving `con:F_k(n)`).

4. **Zenodo API (`https://zenodo.org/api/records`), Crossref (`https://api.crossref.org/works`), & Web Search (`search_web`):**
   - Zenodo `q=2511.16959` -> `0` hits; `q=2610.30892` -> `0` hits.
   - Crossref `query="2511.16959"` -> unrelated numeric substring collisions (`16959`).
   - `search_web`: `"2511.16959" "Conjecture 5" OR ("F_k(n)" "prefix reversal" "2511.16959") OR ("2610.30892" "Conjecture 5")` -> surfaces only `arXiv:2511.16959`.

## Near Misses & Why They Do Not Settle the Exact Statement

- Lei–Zhao–Zhu–Wu (`arXiv:2610.30892v1`, Oct 2026): Settles Conjectures 2, 3, and 4 (`conj:mod4`, `conj:mod2`, `conj:km_sum`) of `2511.16959v3`; explicitly leaves Conjectures 1 and 5 (`con:F_k(n)`) open.
- `the-omega-institute/trureturing#20814`: Open empty preregistration issue (`0` comments, `0` PRs).
- `CONTESTED.md`: absent from `targets/blanco-2511.16959-conj5/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live for citing works of `2511.16959`.
- Closed-access journals and unindexed private notes.
