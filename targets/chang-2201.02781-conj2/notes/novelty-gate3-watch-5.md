# Gate 3 Novelty Re-Check — `chang-2201.02781-conj2` (watch-5)

- **UTC Timestamp:** `2026-11-27T01:43:22Z`
- **Target:** `targets/chang-2201.02781-conj2/TARGET.md`
- **Verdict:** **PASS** (no public proof or refutation of Chang–Yang–Yin–Yao `arXiv:2201.02781v1` Conjecture 2 for general connected $G \neq K_2$ found across live arXiv, OpenAlex citing cache, Zenodo, 369 snapshots, or all 8 inspected competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 369 files):**
   - `"2201.02781" "fgndi" ...` -> only `watch/snapshots/arxiv/citing/chang-2201.02781-conj2.json` and `openalex_works_cache.json`.

2. **GitHub Live Checks (`gh search`, read-only):**
   - Checked `"2201.02781 OR fgndi ..."` across all 8 requested repos: `aliromman/math`, `the-omega-institute/trureturing`, `the-omega-institute/trureturing-tools`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, and `JENW1N/complete-math-solutions` -> `0` matching code results in all 8 repos (`trureturing` PR search `0` matches).

3. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:2201.02781` -> `1` entry (`2201.02781v1`, `2022-01-08T07:01:27Z`, sole/latest version).

4. **OpenAlex Citing Cache & Zenodo API:**
   - `watch/snapshots/arxiv/citing/chang-2201.02781-conj2.json` (`2026-11-26T22:55:31Z`): `citing_count: 0`, `errors: []`.
   - Zenodo `q=2201.02781` -> `0` hits.

## Near Misses & Why They Do Not Settle the Exact Statement

- `CONTESTED.md`: absent from `targets/chang-2201.02781-conj2/`.
- See `targets/chang-2201.02781-conj2/notes/novelty-gate2-watch-5.md` (`2026-11-27T00:08:52Z`) and `notes/audit-helper-chang.md` for Halin-graph / proper `ftndi` / regular-graph (`2602.06659v2`) near misses.

## What Was Not Covered

- Semantic Scholar (`HTTP 429` unauthenticated) and closed-access/unindexed private manuscripts.
