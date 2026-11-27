# Gate 2 Novelty Check — `chervov-2509.19162-conj9` (watch-5)

- **UTC Timestamp:** `2026-11-27T03:48:56Z`
- **Target:** `targets/chervov-2509.19162-conj9/TARGET.md`
- **Verdict:** **PASS** (no public refutation or proof of Chervov et al. `arXiv:2509.19162v2` Conjecture 9 on $\mathrm{diam}(U(n,\mathbb{Z}/2\mathbb{Z})) = \text{A136184}(n)$ found across arXiv, OEIS `A136184`, Zenodo, Crossref, web search, `470` snapshots, or 13 competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `470` files):**
   - `"2509.19162" "Chervov" "U(n, Z/2Z)" "metacyclic"` -> `1` line (`watch/snapshots/arxiv/citing/blanco-2511.16959-conj5.json` citing `A. Chervov` on `2603.22195`); `0` hits on `2509.19162` or `U(n, Z/2Z)`.

2. **GitHub Live Checks (`gh api` trees + `gh search`, read-only):**
   - Checked `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds` (unrelated efficient1500 `2509` packet IDs only), and `linustalacko/small-true-things` -> `0` relevant hits.
   - `gh search issues "2509.19162 OR A136184"` and `gh search prs --repo the-omega-institute/trureturing "2509.19162 OR A136184 OR unitriangular"` -> `0` matches.

3. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`) & OEIS `A136184`:**
   - `2509.19162v2` (`2025-09-23T15:40:36Z`, sole/latest version).
   - Checked follow-up `arXiv:2603.22195v1` (*CayleyPy-4: AI-Holography*, eprint extracted at `tools/.arxiv_cache/eprint/2603.22195/`): `2509.19162` appears only in `biblio.bib`; no hits for `unitriangular` or `A136184` in any `.tex` file.
   - Live OEIS `A136184` JSON (`rev 31`, `2026-09-17T22:32:10-04:00`): no mention of `U(n, Z/2Z)` or `2509.19162`.

4. **Zenodo API (`https://zenodo.org/api/records`), Crossref (`https://api.crossref.org/works`), & Web Search (`search_web`):**
   - Zenodo `q=2509.19162` -> `0` hits; Crossref `query="2509.19162"` -> unrelated numeric DOI/ISBN collisions (`19162`).
   - `search_web`: `"2509.19162" OR ("Chervov" "U(n" "Z/2Z" "Conjecture 9") OR ("2509.19162" "diameter" "unitriangular")` -> surfaces only `arXiv:2509.19162`.

## Near Misses & Why They Do Not Settle the Exact Statement

- `arXiv:2603.22195v1` (*CayleyPy-4*): Cites `2509.19162` only as background in `biblio.bib`.
- `the-omega-institute/trureturing` (`CayleyPyConjectureOneRefutation.lean` & `NikolovSegal/TypeA/Unitriangular`, noted in Gate 1): Target Conjecture 1 and large odd primes respectively, not Conjecture 9 on $U(n, \mathbb{Z}/2\mathbb{Z})$.
- `CONTESTED.md`: absent from `targets/chervov-2509.19162-conj9/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`) for live queries (`chervov-2509.19162-conj9` not yet in sweep cache).
- Closed-access journals and unindexed private notes.
