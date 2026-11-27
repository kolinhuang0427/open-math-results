# Gate 2 Novelty Check — `ziller-2310.15628-conj6.2` (watch-5)

- **UTC Timestamp:** `2026-11-27T04:26:22Z`
- **Target:** `targets/ziller-2310.15628-conj6.2/TARGET.md`
- **Verdict:** **PASS** (no public proof or counterexample to Mario Ziller `arXiv:2310.15628v2` Conjecture 6.2 on injectivity of $\varphi(x)/x^2$ found across arXiv, Zenodo, Crossref, web search, `470` snapshots, or 14 competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `470` files):**
   - `"2310.15628" "varphi(x)/x^2" ...` -> only `watch/snapshots/formal/last_sweep.json` (`ziller-2310.15628-conj6.2` entry).
   - Earlier query with `"Ziller"` surfaced unrelated Erdős 854 table notes (`Gerbicz u(n), Ziller`).

2. **GitHub Live Checks (`gh api` trees + `gh search`, read-only):**
   - Checked `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds` (`check-2310` is an unrelated efficient1300 packet ID), `linustalacko/small-true-things`, `chy4pro/automath` -> `0` relevant hits.
   - `gh search issues "2310.15628 ..."` & `gh search prs --repo the-omega-institute/trureturing "2310.15628 ..."` -> `0` matches.

3. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `id_list=['2310.15628']` -> `2310.15628v2` (`2023-10-24T08:52:12Z`, revised `2026-04-15`, sole/latest version).
   - `au:Ziller AND all:totient` -> `0` entries.

4. **Zenodo API (`https://zenodo.org/api/records`), Crossref (`https://api.crossref.org/works`), & Web Search (`search_web`):**
   - Zenodo `q=2310.15628` -> `0` hits; Crossref `query="2310.15628"` -> unrelated numeric collisions (`15628`).
   - `search_web`: `("2310.15628" "injective") OR ...` -> returns only `arXiv:2310.15628`.

## Near Misses & Why They Do Not Settle the Exact Statement

- `the-omega-institute/trureturing#24177` (noted in Gate 1): Cites `2310.15628` only on OEIS `A349824` / Mohan Lal (1969), not Conjecture 6.2.
- `CONTESTED.md`: absent from `targets/ziller-2310.15628-conj6.2/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live.
- Closed-access journals and unindexed private notes.
