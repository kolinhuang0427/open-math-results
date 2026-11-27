# Gate 2 Novelty Check — `campbell-2509.16034-conj1` (watch-5)

- **UTC Timestamp:** `2026-11-26T23:51:52Z`
- **Target:** `targets/campbell-2509.16034-conj1/TARGET.md`
- **Verdict:** **PASS** (no public settlement of the Section 3 open problems / `displayconjecture` of Campbell–Currie–Rampersad `arXiv:2509.16034v1` / *INTEGERS* 26 (2026) #A34 found across arXiv, Zenodo, Crossref, web search, 356 snapshots, `aliromman/math`, `trureturing`, or `KnowledgeSense/math`)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 356 files incl. `aliromman__math.json`, `trureturing*.json`, `KnowledgeSense__math.json`):**
   - `"2509.16034" "displayconjecture" "reduced abelian complexity"` -> `0 lines across 0/356 files`.
   - `"2509.16034" "displayconjecture" "Rampersad" "Currie" "reduced abelian complexity"` -> 20 lines (all other Currie papers, e.g. `currie-conjecture-19` on `arXiv:2507...`, `EJC 33(3)`).

2. **GitHub Live Checks (`gh search`, read-only):**
   - `gh search code --repo aliromman/math "... 2509.16034 ..."` -> `0` matches.
   - `gh search code --repo the-omega-institute/trureturing "... 2509.16034 ..."` -> `0` matches.
   - `gh search code --repo KnowledgeSense/math "... 2509.16034 ..."` -> `0` matches.

3. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:2509.16034` -> `1` entry (`2509.16034v1`, `2025-09-19T14:38:51Z`, sole/latest version).
   - `au:Rampersad AND all:"abelian complexity"` -> `7` entries (including `2610.03837v1` *An example of an automatic sequence with non-regular abelian complexity*, 2026-10-02, which studies ordinary abelian complexity of another automatic sequence rather than Thue–Morse reduced abelian complexity).

4. **Zenodo API (`https://zenodo.org/api/records`) & Crossref API (`https://api.crossref.org/works`):**
   - Zenodo `q=2509.16034` -> `0` hits; `q="reduced abelian complexity"` -> `0` hits.
   - Crossref `query="2509.16034"` -> unrelated numeric substring collisions (`16034`).

5. **Web Search (`search_web`):**
   - `"2509.16034" OR ("Campbell" "Currie" "Rampersad" "reduced abelian complexity")` -> returns only `arXiv:2509.16034` and *INTEGERS* 26 (2026) #A34 primary publication; no follow-up resolving Section 3.

## Near Misses & Why They Do Not Settle the Exact Statement

- `arXiv:2610.03837v1` (Rampersad, Oct 2026): Concerns non-regular ordinary abelian complexity of an automatic sequence, unrelated to $\rho^{\mathrm{ab},\mathrm{red}}_{\mathbf{t}}$ of Thue–Morse.
- `1337isnot1337/solved-conjectures` PR `#154` (`currie-conjecture-19`): Concerns Currie's *Electron. J. Combin.* 33(3) critical exponent conjecture, unrelated to `2509.16034`.
- `CONTESTED.md`: absent from `targets/campbell-2509.16034-conj1/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live for citing works of `2509.16034`.
- Closed-access journals and unindexed private notes.
