# Gate 2 Novelty Receipt — `oeis-A350963`

- **UTC Time:** 2026-11-27T02:59:00Z
- **Reviewer:** `watch-2` (co-covering Gate 2 per coordinator #673)
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/snapshots/**`):**
   - `.venv/bin/python tools/novelty_grep.py "A350963" "350963" "XXOXX" "A351966" "A351967"`: 0 hits across 462 files.
2. **Live OEIS JSON (`https://oeis.org/search?q=id:A350963&fmt=json`):**
   - Revision 54 (`2025-11-05T15:22:48-05:00`) still lists Sloane's Feb 26, 2022 formula as `Conjectured g.f.`.
3. **arXiv (`tools/arxiv_fetch.py`):**
   - `query 'all:A350963 OR all:XXOXX'` -> 0 results. (OEIS links `1803.08530` Goodman-Strauss & Sloane 2019 coloring book method and `1505.03697` Gruslys–Leader–Tan 2015, neither settling A350963.)
4. **Live GitHub (`gh api`, read-only):**
   - Full non-truncated recursive trees (`git/trees/HEAD?recursive=1`) checked for `350963`, `xxoxx`, `351966`, `351967`: 0 matches across `JENW1N/complete-math-solutions` (425), `aliromman/math` (891), `KnowledgeSense/math` (5377), `rainwangphy/aftd-platform` (28161), `valyuAI/research` (5381), `GuillaumeBAUD-coder/open-math-agents` (1489), `DomTheDeveloper/open-math-agents` (446), `DomTheDeveloper/ProofPlaygrond` (68), `joaquimmj/oeis-conjectures` (1122), `dvgyl/oeis-proofs` (319).
   - Scoped `search/code` (`A350963` and `XXOXX`): 0 matches across the 15 listed competing repos; global `search/code?q=A350963` returned only `joeis`, `loda-programs`, `joeis-lite`, and unrelated `.cs`/changelog files.
5. **Zenodo API & Web Search:**
   - `https://zenodo.org/api/records?q=A350963+OR+%22XXOXX%22+coordination`: no math hits in top 5.
   - `search_web` for `"A350963" OR ("XXOXX" "coordination sequence") OR "A351966" proved OR proof`: no proof found.

## Near Misses & Why They Do Not Settle the Exact Statement

- `arXiv:1803.08530` (Goodman-Strauss & Sloane, 2019): general coloring book method cited by Sloane as a suggested approach, does not prove A350963.

## What Was Not Covered

- GitHub `search/issues` API hit secondary rate-limit HTTP 403 (`2026-11-27T02:57:00Z`) and was not retrieved live; closed-access journals and private repositories not indexed by arXiv, GitHub, Zenodo, OEIS, or web search.
