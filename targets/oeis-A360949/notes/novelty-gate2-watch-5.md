# Gate 2 Novelty Check — `oeis-A360949` (watch-5)

- **UTC Timestamp:** `2026-11-26T23:51:52Z`
- **Target:** `targets/oeis-A360949/TARGET.md`
- **Verdict:** **PASS** (no public proof of Paul D. Hanna's 2023 `A360949` mod-4 / `A161674` Thue–Morse conjecture found across live OEIS, arXiv, Zenodo, Crossref, web search, 356 snapshots, `aliromman/math`, `trureturing*`, or `KnowledgeSense/math`)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 356 files incl. `aliromman__math.json`, `trureturing*.json`, `KnowledgeSense__math.json`):**
   - `"A360949" "360949" "A161674"` -> `0 lines across 0/356 files`.
   - `"A360949" "360949" "A161674" "Paul D. Hanna"` -> `8` lines across `6/356` files (all other Hanna conjectures: `mathesis-papers/hanna-self-substitution-integrality`, `dvgyl/oeis-proofs`, `trureturing-tools` `SCREENED-OUT.md`, `formal-conjectures` PRs on `A158110` / other Hanna sequences; 0 hits on `A360949` or `A161674`).

2. **GitHub Live Checks (`gh search`, read-only):**
   - `gh search code --repo aliromman/math "A360949 OR ..."` -> `0` matches.
   - `gh search code --repo the-omega-institute/trureturing "A360949 OR ..."` -> `0` matches.
   - `gh search code --repo KnowledgeSense/math "A360949 OR ..."` -> `0` matches.

3. **Live OEIS JSON (`https://oeis.org/search?q=id:A360949&fmt=json`):**
   - Confirmed `revision: 15` (`2023-03-05T12:37:19-05:00`) unchanged; comment still reads: `Conjecture: a(0) = 1, a(2*A161674(k) + 1) == 2 (mod 4) for k >= 1, otherwise a(n) == 0 (mod 4). ...`.

4. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:A360949` -> `0` entries.

5. **Zenodo API (`https://zenodo.org/api/records`) & Crossref API (`https://api.crossref.org/works`):**
   - Zenodo `q=A360949` -> `0` hits.
   - Zenodo `q="Paul D. Hanna" A360949` -> `4` hits (`24484628`, `24013714`, `23282853`, `24433538`), all inspected directly and confirmed unrelated (`A350410`–`A350412`, self-referential exponential series, scattering coefficients; `A360949`/`A161674` absent from all descriptions).
   - Crossref `query=A360949` -> `0` results.

6. **Web Search (`search_web`):**
   - `"A360949" "Hanna" OR "A360949" "A161674"` -> no proof or published resolution found.

## Near Misses & Why They Do Not Settle the Exact Statement

- `dvgyl/oeis-proofs` / `mathesis-papers/hanna-self-substitution-integrality` / Zenodo `24484628`, `24013714`, `23282853`: Resolve other OEIS conjectures of Paul D. Hanna (`A350410`–`A350412`, self-referential exponential series), not `A360949`.
- `CONTESTED.md`: absent from `targets/oeis-A360949/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live.
- Closed-access journals and unindexed private notes.
