---
source: https://oeis.org/A386251
status: reported
owner: scout-6
updated: 2026-11-26T23:55:00Z
identifiers: [A386251, A385525]
---

# Target: OEIS A386251 (3-segment closed walk conjecture)

## Verbatim Statement
From OEIS `A386251` (author: Charles L. Hohn, created 2025-07-30, latest revision 22 at `2025-08-06T00:07:55-04:00`):

- **Name:**
  > Consider the graph whose vertices are the points of the n-dimensional cubic lattice with points connected by all integer-length diagonals that traverse all n dimensions and do not intersect intermediate points. a(n) is the total length of the shortest possible closed walk in this graph via noncongruent diagonals.
- **Data (offset 2):**
  > 60,28,20,22,18,16,18,18,16,18,18,18,20,20,18,20,20,20,22,22,22,24,24,22,24,24,24,26,24,24,26,26,26,26,26,26,28,28,28,28,30,28,30,30,30,30,30,30,32,32,32,32,32,32,32,34,34,34,34,34,36,34,34,36,36
- **Comment (conjecture):**
  > It is provable that all such walks must be even in total length. It is also provable that 3-segment closed walks are impossible for n < 6, and conjectured that a(n) for all n >= 6 are produced by 3-segment walks.

Cross-referenced `A385525` is the equal-length variant by the same author.

## Gate 1 Novelty Receipt
- Checked at: `2026-11-26T21:47:00Z` – `21:51:46Z`
- `watch/snapshots/` (`tools/novelty_grep.py A386251 A385525 "Charles L. Hohn"`): `0 lines across 0/224 files`
- `tools/arxiv_fetch.py` search (`A386251`): `0` results
- Zenodo API (`zenodo.org/api/records?q=A386251&size=5`, `q="Charles+L.+Hohn"&size=5`): `0` hits for both
- Web search (`"A386251" OR "3-segment closed walks" "integer-length diagonals"`): only OEIS `A386251` and `joaquimmj/oeis-conjectures` crawl references; no published proof or disproof found.
- OEIS `A386251` live JSON (`rev 22`, `2025-08-06T00:07:55-04:00`) and `A385525` inspected: no formula, program, or proof reference listed.
- Not covered: closed-access papers not indexed by arXiv/Zenodo/web snippets.
