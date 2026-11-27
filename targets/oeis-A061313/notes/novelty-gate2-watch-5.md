# Gate 2 Novelty Check — `oeis-A061313` (watch-5)

- **UTC Timestamp:** `2026-11-26T23:31:11Z`
- **Target:** `targets/oeis-A061313/TARGET.md`
- **Verdict:** **PASS** (no public proof of Zabolotskii's 2020 `A061313` Hirzebruch continued fraction conjecture found across live OEIS, arXiv, Zenodo, Crossref, web search, 356 local snapshots, `aliromman/math`, `trureturing*`, or `KnowledgeSense/math`)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 356 files incl. `aliromman__math.json`, `trureturing*.json`, `KnowledgeSense__math.json`):**
   - `"A061313" "061313" "Zabolotskii" "Stern-Brocot"` -> `0 lines across 0/356 files`.

2. **GitHub Live Checks (`gh search` / `gh api`, read-only):**
   - `gh search code/prs --repo aliromman/math "... A061313 OR Zabolotskii ..."` -> `0` matches.
   - `gh search code --repo KnowledgeSense/math "... A061313 OR Zabolotskii ..."` and `preprints` filter -> `0` matches.
   - `gh search prs --repo the-omega-institute/trureturing "... A061313 OR Zabolotskii"` and `trureturing-tools` -> `0` matches.
   - `gh search issues/prs "A061313"` -> `0` results.
   - `gh search code "A061313"` -> `joeis`, `loda-programs`, competitive programming solutions (`eolymp/388-transformation.py`), and hex/ID collisions only; no proof.

3. **Live OEIS JSON (`https://oeis.org/search?q=id:A061313&fmt=json`):**
   - Confirmed `revision: 58` (`2026-11-01T16:49:49-05:00`); comment still reads: `"Conjecture: a(n)+2 is the sum of the terms of the Hirzebruch (negative) continued fraction for the Stern-Brocot tree fraction A007305(n)/A007306(n). - _Andrei Zabolotskii_, Apr 17 2020"`.

4. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:A061313` -> `0` entries.
   - `au:Zabolotskii` -> `10` entries (e.g., `2608.13199v2` continued fraction convergence, `2607.06767v1` Y-friezes, `2312.12953v3` frieze patterns and Farey complexes); none prove the `A061313` stopping-time / Hirzebruch CF sum identity.

5. **Zenodo API (`https://zenodo.org/api/records`) & Crossref API (`https://api.crossref.org/works`):**
   - Zenodo `q=A061313` -> `0` hits; `q=Zabolotskii` -> `3` unrelated hits (`Sum-Free Partitions`, `Orthocladius`, `A288537`).
   - Crossref `query=A061313` -> `0` results.

6. **Web Search (`search_web`):**
   - `"A061313" OR ("Zabolotskii" "Stern-Brocot" "A061313") OR ("A061313" "conjecture" proved)` -> returns OEIS `A061313`, Math.SE stopping-time threads, and Zabolotskii's frieze/Stern–Brocot papers; no proof of `A061313` found.

## Near Misses & Why They Do Not Settle the Exact Statement

- `arXiv:2312.12953v3` (*Frieze patterns and Farey complexes*) and `2607.06767v1` (*All Y-friezes come from $\mathrm{SL}_2$-friezes*) by Zabolotskii: Study Farey/Stern–Brocot combinatorics and friezes, not the `A061313` doubling-minus-one stopping count identity.
- `CONTESTED.md`: absent from `targets/oeis-A061313/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live.
- Closed-access journals and unindexed private notes.
