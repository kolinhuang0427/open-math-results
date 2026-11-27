---
source: https://oeis.org/A350963 (rev. 2025-11-05)
status: reported
owner: attack-4
updated: 2026-11-27T02:43:00Z
identifiers: [A350963, A351966, A351967, XXOXX tiling, coordination sequence, N. J. A. Sloane]
---

# Target: OEIS A350963 (XXOXX Tiling Coordination Sequence Conjectured G.F.)

## Verbatim Statement
From OEIS **A350963** (author: `_N. J. A. Sloane_`, Feb 25 2022; latest revision `2025-11-05T15:22:48-05:00`):

- **Name:**
  > Coordination sequence for the XXOXX tiling with respect to a tile of type R.
- **Data (`offset 0`):**
  > 1,9,29,42,63,75,97,106,131,139,165,170,199,203,233,234,267,267,301,298,335,331,369,362,403,395,437,426,471,459,505,490,539,523,573,554,607,587,641,618,675,651,709,682,743,715,777,746,811,779,845,810,879,843
- **Formula (Conjecture):**
  > Conjectured g.f.: -(2*t^7-6*t^6-24*t^5-33*t^4-33*t^3-28*t^2-9*t-1)/((1-t^2)*(1-t^4)). Given the decomposition of this structure into eight sectors (see Sigrist's illustration of the first 100 generations), it should be possible to establish this g.f. and those of the other two coordination sequences by using the coloring book method. - _N. J. A. Sloane_, Feb 26 2022
- **Graph definition:** Given explicitly in Rémy Sigrist's OEIS-linked `a350963.gp.txt` (6 tiles per fundamental domain with translations `DX = 4 - i`, `DY = 6i`, root `T[4]` or `T[1]` of type R, degree 9).

## Gate 1 Novelty Receipt
- Checked at: `2026-11-27T00:33:00Z` – `00:45:16Z`
- `watch/snapshots/` (`tools/novelty_grep.py A350963 XXOXX A351966 A351967`): `0` hits.
- `tools/arxiv_fetch.py query "all:A350963 OR all:XXOXX"`: `0` results.
- Zenodo API (`zenodo.org/api/records?q=A350963+OR+XXOXX&size=3`): `0` hits.
- GitHub code search (`gh search code A350963`): `joeis` (`GeneratingFunctionSequence implements Conjectural`), `loda-programs`, `joeis-lite`, `0` matches in `aliromman/math`, `trureturing`, `joaquimmj/oeis-conjectures`, `1337isnot1337/solved-conjectures`.
- Web search (`"A350963" OR "XXOXX tiling" "coordination sequence"`): no published proof found.
- OEIS `A350963` inspected live (`rev 2025-11-05`): formula remains marked `Conjectured g.f.`.
- Not covered: closed-access venues not indexed by arXiv/Zenodo/web.
