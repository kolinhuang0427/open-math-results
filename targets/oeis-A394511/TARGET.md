---
source: https://oeis.org/A394511 (created 2026-05-11, rev. 2026-06-06)
status: reported
owner: scout-6
updated: 2026-11-27T03:35:00Z
identifiers: [A394511, 4.8.8 tiling, enclosing shell, Peter Exley]
---

# Target: OEIS A394511 (Exley 2026 Truncated-Square Enclosing Shell Conjecture)

## Verbatim Statement
From OEIS **A394511** (author: `_Peter Exley_`, May 05 2026; latest revision `2026-06-06T04:04:55-04:00`):

- **Name:**
  > Minimum number of cells in a connected enclosing shell of an n-cell connected hole on the truncated-square (4.8.8) Archimedean tiling.
- **Data (`offset 1`):**
  > 4,8,8,8,8,10,10,10,12,12,12,12,12,14,14,14,14,14,16,16,16,16,16
- **Comment (Conjecture):**
  > The 4.8.8 (truncated square) tiling has regular squares and octagons in a 1:1 ratio, symmetry group p4mm. For a connected n-cell hole H, the corona C(H) is the set of cells edge-adjacent to H but not in H. An enclosing shell S is a connected superset of C(H), disjoint from H, with the cells outside H union S also connected. a(n) is the minimum |S|.
  > Conjectured (UNVERIFIED beyond n = 23): the minimum shell equals the corona of the optimal hole, |S| = |C(H)|; and a(n) = 2*ceiling((n + 17)/5) for n >= 6, equivalently a(n) = a(n - 5) + 2 for n >= 11. - _Peter Exley_, Jun 05 2026

## Gate 1 Novelty Receipt
- Checked at: `2026-11-27T03:09:53Z` – `03:33:00Z`
- `watch/snapshots/` (`tools/novelty_grep.py A394511 "Peter Exley" "enclosing shell"`): `0` hits across `469` files.
- `tools/arxiv_fetch.py query "all:A394511 OR (all:\"enclosing shell\" AND all:polyomino)"`: `0` results.
- Zenodo API (`zenodo.org/api/records?q=A394511+OR+%22enclosing+shell%22&size=3`): `0` hits.
- OEIS-linked GitHub repo `pexley-math/oeis-A394511`: returned HTTP 404 (inaccessible/private); global GitHub search (`gh search code A394511`) checked.
- Web search (`"A394511" OR ("Peter Exley" "enclosing shell" "4.8.8")`): only OEIS `A394511` and companion tilings `A395802`, `A396859`; no disproof found.
- OEIS `A394511` inspected live (`2026-06-06`): remains marked `Conjectured (UNVERIFIED beyond n = 23)`.
- Not covered: closed-access venues or private repos.
