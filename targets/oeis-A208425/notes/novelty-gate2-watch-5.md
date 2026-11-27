# Gate 2 Novelty Check — `oeis-A208425` (watch-5)

- **UTC Timestamp:** `2026-11-27T01:26:04Z`
- **Target:** `targets/oeis-A208425/TARGET.md`
- **Verdict:** **PASS** (no public proof of Zhi-Wei Sun's 2016 `A208425` Conjecture (ii) Part 1 `conjecture_2` for $p \equiv 1 \pmod 3$ found across live OEIS, arXiv, Zenodo, Crossref, web search, 357 snapshots, or major competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 357 files):**
   - `"A208425" "208425" "2012.05121" "sun-conjectures-lean"` -> `5` lines across `2/357` files (only `FormalConjectures/OEIS/208425.lean` and `last_sweep.json`, listed open).

2. **GitHub Live Checks (`gh search`, read-only):**
   - `gh search code` (`"2505.12035 OR Berge OR A208425"`) across `the-omega-institute/trureturing`, `the-omega-institute/trureturing-tools`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, and `Varun-Dudipala/sun-conjectures-lean` -> `0` matches for `A208425`. (Note: `Varun-Dudipala/sun-conjectures-lean` solves `conjecture_3`, $p \equiv 2 \pmod 3$, via `SunConjectures/A208425/Solution.lean` and explicitly leaves `conjecture_2`, $p \equiv 1 \pmod 3$, unsolved, per `TARGET.md`.)
   - `gh search issues "A208425"` and `gh search prs "A208425"` -> `0` results.

3. **Live OEIS JSON (`https://oeis.org/search?q=id:A208425&fmt=json`):**
   - Confirmed `revision: 60` (`2025-11-05T15:22:21-05:00`) unchanged; Sun's Nov 12, 2016 Conjecture (ii) remains unproved for $p \equiv 1 \pmod 3$.

4. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:A208425` -> `0` entries.
   - `all:2012.05121` -> `1` entry (`2012.05121v3`, Pan–Sun, settles `conjecture_1` only).

5. **Zenodo API (`https://zenodo.org/api/records`), Crossref (`https://api.crossref.org/works`), & Web Search (`search_web`):**
   - Zenodo `q=A208425` -> `0` hits; `q=2012.05121` -> `0` hits.
   - Crossref `query=A208425` -> `0` results.
   - `search_web`: `"A208425" "conjecture_2" OR ("A208425" "p = 1 (mod 3)" "2(p-1)/3") OR ("2012.05121" "A208425")` -> returns OEIS `A208425` and Pan–Sun `2012.05121`, no settlement of `conjecture_2`.

## Near Misses & Why They Do Not Settle the Exact Statement

- Hao Pan & Zhi-Wei Sun (`arXiv:2012.05121v3`, *Front. Comb. Number Theory* 2 (2026)): Proves `conjecture_1` only; does not treat Part (ii) (`conjecture_2`).
- `Varun-Dudipala/sun-conjectures-lean`: Proves `conjecture_3` ($p \equiv 2 \pmod 3$) only; explicitly states $p \equiv 1 \pmod 3$ (`conjecture_2`) is not proved there.
- Mao (`arXiv:2003.09810v4`, *JCTA* 2021): Proves the auxiliary congruence $\sum_{k=0}^{2(p-1)/3} \binom{2k}{k} \equiv 1 \pmod{p^2}$ (noted in `notes/lit-a208425.md`), not `conjecture_2` itself.
- `CONTESTED.md`: absent from `targets/oeis-A208425/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live.
- Closed-access journals and unindexed private notes.
