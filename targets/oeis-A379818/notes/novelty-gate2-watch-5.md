# Gate 2 Novelty Check — `oeis-A379818` (watch-5)

- **UTC Timestamp:** `2026-11-26T22:54:20Z`
- **Target:** `targets/oeis-A379818/TARGET.md`
- **Verdict:** **PASS** (no public proof or resolution of Mikhail Kurkov's `A379818` binomial formula conjecture found across local snapshots, arXiv, live OEIS, Zenodo, Crossref, or web search)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py`):**
   - `.venv/bin/python tools/novelty_grep.py A379818 "binomial(m+2"` -> `0 lines across 0/280 files`.
   - `.venv/bin/python tools/novelty_grep.py A379818 Kurkov A025480 "2^r(2k+1)-1"` -> 27 lines across 9/277 files (all other Kurkov OEIS sequences — see Near Misses).

2. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:A379818` -> `0` entries
   - `all:"Mikhail Kurkov"` -> `0` entries
   - `all:A025480 AND all:Kurkov` -> `0` entries
   - `all:"379818" AND all:OEIS` -> `0` entries

3. **Live OEIS JSON (`https://oeis.org/search?q=id:A379818&fmt=json`):**
   - Confirmed `revision: 8` (`2026-02-26T16:45:49-05:00`) still lists `Conjecture: a(2^m*(2k+1)) = Sum_{j=0..m} (binomial(m+2, j+1) - binomial(m, j))*a(2^j*k) for m >= 0, k >= 0 with a(0) = 1.` under `formula`, with `references: 2` (`xref: A007814, A025480, A329369, A341392, A347205`).

4. **Zenodo API (`https://zenodo.org/api/records`):**
   - `q=A379818` -> `0` hits
   - `q="Mikhail Kurkov"` -> `0` hits
   - `q=A025480 Kurkov` -> `12` hits (all unrelated records, e.g. engineering/modal triplet theory/other Kurkov authors)

5. **Crossref API (`https://api.crossref.org/works`):**
   - `query=A379818` -> `0` results
   - `query="Mikhail Kurkov"` -> top hits unrelated (`Management of destabilized deterministic systems`, `Andrej Kurkov`, etc.; earlier call hit transient HTTP 429 before retry succeeded)

6. **Web Search (`search_web`):**
   - Query: `"A379818" OR ("Mikhail Kurkov" "A025480") OR ("binomial(m+2, j+1) - binomial(m, j)" "a(2^j*k)")` -> returned only OEIS entries (`A379818`, `A025480`), no proofs or papers.

## Near Misses & Why They Do Not Settle the Exact Statement

- `watch/snapshots/discovered/CATALOG.md` and `watch/snapshots/ai-collections/joaquimmj__oeis-conjectures/`: list proofs/conjectures for *other* Mikhail Kurkov OEIS sequences (`A006068`, `A340991`, `A263634`, `A396563`, binary Stirling row edge) and `trureturing` files (`KurkovGrayInverseRecurrence.md`, `KurkovLowerBitRecurrence.md`, `KurkovRunAlternatingCount.md`); none touch `A379818` or `a(2^m*(2k+1))`.
- `CONTESTED.md`: absent from `targets/oeis-A379818/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried.
- Closed-access journals and unindexed private repositories.
