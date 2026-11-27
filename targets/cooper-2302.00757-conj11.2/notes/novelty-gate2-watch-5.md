# Gate 2 Novelty Check — `cooper-2302.00757-conj11.2` (watch-5)

- **UTC Timestamp:** `2026-11-27T00:08:52Z`
- **Target:** `targets/cooper-2302.00757-conj11.2/TARGET.md`
- **Verdict:** **PASS** (no public proof of Cooper `arXiv:2302.00757v2` Conjecture 11.2 on $T_{11}(3n) \pmod 9$ and $T_{11}(5n) \pmod{25}$ found across arXiv, Zenodo, Crossref, web search, 357 snapshots, `aliromman/math`, `trureturing`, or `KnowledgeSense/math`)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 357 files incl. `aliromman__math.json`, `trureturing*.json`, `KnowledgeSense__math.json`):**
   - `"2302.00757" "T_{11}" "5581" "Shaun Cooper"` -> `17` lines across `7/357` files (numeric `5581` substring collisions in SHA hashes/`A005581`; `0` hits on `2302.00757` or Shaun Cooper).

2. **GitHub Live Checks (`gh search`, read-only):**
   - `gh search code --repo aliromman/math "... 2302.00757 ..."` -> `0` matches.
   - `gh search code --repo the-omega-institute/trureturing "... 2302.00757 ..."` -> `0` matches.
   - `gh search code --repo KnowledgeSense/math "... 2302.00757 ..."` -> `0` matches.

3. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:2302.00757` -> `1` entry (`2302.00757v2`, `2023-02-01T21:03:06Z`, updated `2024-05-08`, sole/latest version).
   - `au:Cooper AND all:"2302.00757"` -> `0` follow-up entries.

4. **Zenodo API (`https://zenodo.org/api/records`), Crossref (`https://api.crossref.org/works`), & Web Search (`search_web`):**
   - Zenodo `q=2302.00757` -> `0` hits.
   - Crossref `query="2302.00757"` -> unrelated numeric substring collisions (`00757`).
   - `search_web`: `"2302.00757" OR ("Cooper" "Conjecture 11.2" "2302.00757") OR ("T_11(3n)" "mod 9")` -> returns only `arXiv:2302.00757` itself.

## Near Misses & Why They Do Not Settle the Exact Statement

- Cooper `arXiv:2302.00757v2` Section 5 (general mod-$p$ Lucas congruences) and Conjecture 11.1 ($p \in \{2, 59, 5581\}$) are distinct conjectures left open in the primary paper; `arXiv:2312.07134` cites Section 11 supercongruences as open.
- `CONTESTED.md`: absent from `targets/cooper-2302.00757-conj11.2/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live for citing works of `2302.00757`.
- Closed-access journals and unindexed private notes.
