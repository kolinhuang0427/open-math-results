---
source: https://oeis.org/A400812 (rev. 50, Nov 10 2026)
status: reported
owner: scout-6
updated: 2026-11-27T10:28:15Z
identifiers: [A400812, A057080, A099919, Boris K. Horvat, Spectre tiling, star triples]
---

# Target: OEIS A400812 (Star Triples in Level-$n$ Spectre Supertile)

## Verbatim Statement
From OEIS **A400812** (`rev. 50`, Nov 10 2026; author: `_Boris K. Horvat_`, Oct 08 2026):

> `%N` Number of star triples in the level-n supertile of the Spectre tiling.
> `%C` A star triple is a set of three Spectre tiles related by a rotation through 120 degrees about a common point of their boundaries. Up to orientation, there are exactly two such configurations, the major and the minor star triple (A400813, A400814), which differ in their circumradius. ...
> `%C` The recurrence and formulas were derived from the growth rules of the cluster families and megaobjects, which were found empirically from direct counts in the supertiles of levels 3 to 7; they are not proved.
> `%F` Conjecture: a(n) = 13*a(n-1) - 44*a(n-2) + 28*a(n-3) + 5*a(n-4) - a(n-5) for n >= 5.
> `%F` Conjecture: G.f.: 4*x^3*(7 + 2*x)/((1 - x)*(1 - 8*x + x^2)*(1 - 4*x - x^2)).
> `%F` Conjecture: a(n) = A057080(n-1) - (A000045(3*n+2) - 3)/2 = A057080(n-1) - A099919(n) + 1 for n >= 1.
> `%F` Conjecture: Limit_{n->oo} a(n)/A057080(n) = 4 - sqrt(15) = 0.1270166537... (one star triple for every 4 + sqrt(15) = 7.8729833462... tiles).

*(Data in `%S`: `0,0,0,28,372,3604,31268,258464,2086984,16651528,132032296,1043449220` for $n=0,\dots,11$.)*

## Gate 1 Novelty Receipt
- Checked at: `2026-11-27T09:54:00Z` – `2026-11-27T09:56:00Z`
- `watch/snapshots/` (`tools/novelty_grep.py A400812 400812 A400813 A400814 "star triples" "2609.07592" "Horvat"` across 618 files): `0` relevant hits.
- Live GitHub (`gh search repos "A400812"`, `gh search issues "A400812"`): `0` math hits (`georchestra/cadastrapp` unrelated).
- Live Zenodo API (`zenodo.org/api/records?q=A400812`): `0` hits (Horvat's background record `18421797`, *Anatomy of the Spectre Tiling*, 2026-01-29 is cited directly by OEIS `A400812`, which states the formulas are empirical from levels 3–7 and not proved).
- Live arXiv (`2609.07592`, Imperor-Clerc–Sadoc–Tatham, Sep 2026): inspects global rotational symmetry centers of the infinite tiling and does not prove the `A400812` level-$n$ supertile counts or linear recurrence.
- Live OEIS `A400812` (`rev. 50`, `2026-11-10`): explicitly marked empirical and not proved.
- Not covered: `gh search code` (avoided due to rate limit), PDF-only contents of `18421797` (`Anatomy-of-the-Spectre-Tiling.pdf`) and `a400812_2.pdf`.

## Attack Log
- Start UTC: `2026-11-27T09:55:42Z`
