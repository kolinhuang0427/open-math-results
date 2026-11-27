# Gate 2 Novelty Check — `cassaigne-2602.21895-conjC4` (watch-5)

- **UTC Timestamp:** `2026-11-27T04:26:22Z`
- **Target:** `targets/cassaigne-2602.21895-conjC4/TARGET.md`
- **Verdict:** **PASS** (no public proof of Dekking Conjecture $(C_4)$ for factor lengths $|w| \ge 2$ or reversal invariance in $\mathbf{t}'$ / $\mathbf{t}_{3/2}$ of `arXiv:2602.21895v1` found across arXiv, Zenodo, Crossref, web search, `470` snapshots, or 14 competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `470` files):**
   - `"... 2602.21895 t_{3/2} A357448 ..."` -> only `watch/snapshots/formal/last_sweep.json` (`cassaigne-2602.21895-conjC4` entry) and unrelated `3/2` Schatten norm hits in `ArtificialZeng__AI-Has-Taste`.

2. **GitHub Live Checks (`gh api` trees + `gh search`, read-only):**
   - Checked `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds` (`2602` packet/PR hits unrelated), `linustalacko/small-true-things`, `chy4pro/automath` -> `0` relevant hits.
   - `gh search issues` & `the-omega-institute/trureturing` PR search -> `0` matches.

3. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `id_list=['2602.21895']` -> `2602.21895v1` (`2026-02-25T13:24:47Z`, sole/latest version).

4. **Zenodo API (`https://zenodo.org/api/records`), Crossref (`https://api.crossref.org/works`), & Web Search (`search_web`):**
   - Zenodo `q=2602.21895` -> `0` hits; Crossref `query="2602.21895"` -> unrelated numeric collisions (`21895`).
   - `search_web`: `... OR ("2602.21895" "Dekking" "C_4") OR ...` -> returns only `arXiv:2602.21895`.

## Near Misses & Why They Do Not Settle the Exact Statement

- `the-omega-institute/trureturing/Problems/dekking-keane-2022-two-block-thue-morse-frequency.md` (noted in Gate 1): Settles single-letter frequency $1/2$ for a different 2-block substitution (`arXiv:2202.13548v1`).
- `CONTESTED.md`: absent from `targets/cassaigne-2602.21895-conjC4/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live.
- Closed-access journals and unindexed private notes.
