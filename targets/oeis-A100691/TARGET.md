---
source: https://oeis.org/A100691 (OEIS A100691, revision 11, 2022-07-22) and https://oeis.org/A193641 (OEIS A193641, revision 48, 2026-09-16)
status: reported
owner: scout-6
updated: 2026-11-26T21:44:00Z
identifiers: ["A100691", "A193641", "R. J. Mathar", "triangular lattice", "strip Z x {0,1}", "self-avoiding paths"]
---

# OEIS A100691 — R. J. Mathar (2022) Conjecture Linking A100691 and A193641

## Exact Statements from Primary Sources

From OEIS **A100691** (revision 11, 2022-07-22):
- **Name:**
  > "Number of self-avoiding paths with n steps on a triangular lattice in the strip Z x {0,1}."
- **Data (`offset 0,2`):**
  > `1,4,12,30,70,158,352,780,1724,3806,8398,18526,40864,...`
- **Formula section:**
  > `G.f.: (1+z^2)(1+z+z^2)/[(1-z)(1-2z-z^3)]= 1+2*(2+z^2)/((z-1)*(z^2+2*z-1)).`
  > `a(n) = 2*a(n-1) + a(n-3) + 6 for n >= 4.`
  > `a(n) = A008998(n+2) - A052980(n+1) - 3. - _Ralf Stephan_, May 15 2007`
  > `Conjecture: a(n) = A193641(n+2)-3, n>0 - _R. J. Mathar_, Jul 22 2022`

From OEIS **A193641** (revision 48, 2026-09-16):
- **Name:**
  > "Number of arrays of -1..1 integers x(1..n) with every x(i) in a subsequence of length 1 or 2 with sum zero."
- **Data (`offset 0,3`):**
  > `1,1,3,7,15,33,73,161,355,783,1727,3809,8401,...`
- **Formula section:**
  > `Empirical: a(n) = 2*a(n-1) + a(n-3).`
  > `Empirical: G.f.: -x*(1+x+x^2) / ( -1+2*x+x^3 ); a(n) = A008998(n-3) + A008998(n-2) + A008998(n-1). - _R. J. Mathar_, Feb 19 2015`

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-26T19:59:07Z – 2026-11-26T20:10:00Z
- **Sources Checked:**
  - `watch/snapshots/` (grep for `A100691`, `A193641`) — 0 matches.
  - `joaquimmj/oeis-conjectures` (full tree + `REPORT.md` + `README.md`) — `A100691` is unsettled (listed in `conjectures/crawl/ranked.json`).
  - Live OEIS entries `A100691` (rev 11), `A193641` (rev 48), `A100692`, `A100693`, `A038577`.
  - `arXiv` API query (`tools/arxiv_fetch.py`): `all:"A193641" OR all:"A100691"` -> 0 results; `ti:"Intervals in a family of Fibonacci lattices"` -> `arXiv:2411.17628v1` (Baril & Hassler, 2024), checked `main.tex` line 564 (only compares boolean intervals in `\FF_n^3` to `A193641`, does not prove `A193641`'s `-1..1` array recurrence or address `A100691`).
  - Web search queries:
    - `"A100691" "A193641" OR "A193641" proof recurrence`
    - `"A100691" "self-avoiding paths" "triangular lattice" "Z x {0,1}"`
    - `"Paths in the Cartesian, triangular and hexagonal lattices" Labelle 1996`
    - `"Intervals in a family of Fibonacci lattices" "A193641" OR "193641"`
    - `"Counting maximal matchings in linear polymers" "A193641" OR "2a(n-1)" OR "193641"`
    - `"Number of arrays of -1..1 integers" "subsequence of length 1 or 2 with sum zero"`
- **Near Misses:** Baril & Hassler (`arXiv:2411.17628v1`, 2024) and Došlić & Zubac (2016) study other combinatorial objects counted by the same sequence `A193641`; neither proves the `-1..1` array recurrence of `A193641` nor relates it to `A100691`.
- **Not Covered:** Print-only text of J. Labelle, *Paths in the Cartesian, triangular and hexagonal lattices*, Bull. ICA 17 (1996), 47–61 (not digitized online), and Došlić & Zubac (2016) full PDF.
