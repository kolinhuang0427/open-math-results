# Gate 2 Novelty Check — `petyuk-2210.14762-conj1` (watch-5)

- **UTC Timestamp:** `2026-11-27T01:43:22Z`
- **Target:** `targets/petyuk-2210.14762-conj1/TARGET.md`
- **Verdict:** **PASS** (no public refutation or proof of Petyuk `arXiv:2210.14762v2` Conjecture 1 for $S(n,k)$ with $n \ge 4, k \ge 3$ found across arXiv, Zenodo, Crossref, web search, 369 snapshots, or competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 369 files):**
   - `"... 2210.14762 Petyuk S(4,3)"` -> `0` hits on `2210.14762`, `Petyuk`, or `S(4,3)`.

2. **GitHub Live Checks (`gh search`, read-only):**
   - Checked `"... 2210.14762 OR Petyuk"` across `aliromman/math`, `the-omega-institute/trureturing`, `the-omega-institute/trureturing-tools`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, and `JENW1N/complete-math-solutions` -> `0` matches in all 8 repos (`trureturing` PRs `0`; global `gh search issues` `0`).

3. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:2210.14762` -> `1` entry (`2210.14762v2`, `2022-10-20T07:50:43Z`, v2 2023-07-12, sole/latest version).
   - `au:Petyuk AND all:word` -> `1` entry (`2210.14762v2` only).
   - `all:"word-representable" AND all:"S(n,k)"` -> `1` entry (`2210.14762v2` only).

4. **Zenodo API (`https://zenodo.org/api/records`), Crossref (`https://api.crossref.org/works`), & Web Search (`search_web`):**
   - Zenodo `q=2210.14762` -> `0` hits.
   - Crossref `query="2210.14762"` -> unrelated numeric substring collisions (`14762`).
   - `search_web`: `"2210.14762" OR ("Petyuk" "word-representable" "S(n,k)" OR "S(4,3)")` -> surfaces only `arXiv:2210.14762` (and `2312.10377v1` / `2605.02268v2` noted in Gate 1, which leave Petyuk's conjecture open).

## Near Misses & Why They Do Not Settle the Exact Statement

- Huang–Kitaev–Pyatkin (`arXiv:2312.10377v1`) and Roy–Hariharasubramanian (`arXiv:2605.02268v2`): Study distance-restricted $S_m(n,k)$ and shift graphs $G(n,k)$ respectively; leave $S(n,k)$ ($n \ge 4, k \ge 3$) explicitly open.
- `CONTESTED.md`: absent from `targets/petyuk-2210.14762-conj1/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live for citing works of `2210.14762`.
- Closed-access journals and unindexed private notes.
