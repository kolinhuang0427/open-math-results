---
source: https://oeis.org/A108449 (rev. 13, 2025-11-05T15:35:31-05:00)
status: reported
owner: scout-5
updated: 2026-11-27T09:15:00Z
identifiers: ["A108449", "R. J. Mathar", "D-finite", "no pyramids", "Emeric Deutsch", "Vaclav Kotesovec"]
---

# OEIS A108449 — Mathar (2022) D-Finite Recurrence Conjecture

## Exact Statement
From OEIS **A108449** (`NAME` and `FORMULA`, revision 13, offset `0,3`):
> **Name:** Number of paths from (0,0) to (3n,0) that stay in the first quadrant (but may touch the horizontal axis), consisting of steps u=(2,1),U=(1,2), or d=(1,-1) and having no pyramids (a pyramid is a sequence u^pd^p or U^pd^(2p) for some positive integer p, starting at the x-axis).
> **Formula:** `G.f.=(1-z)/[1+z-z(1-z)A(1+A)], where A=1+zA^2+zA^3=(2/3)*sqrt((z+3)/z)*sin((1/3)*arcsin(sqrt(z)*(z+18)/(z+3)^(3/2)))-1/3 (the g.f. of A027307).`
> **Formula (_Vaclav Kotesovec_, Mar 18 2014):** `G.f. y(x) satisfies: -1 + 3*x - 3*x^2 + x^3 + y + 3*x*y - 9*x^2*y + 5*x^3*y - 5*x*y^2 - x^2*y^2 + 5*x^3*y^2 + x^4*y^2 - x*y^3 + 9*x^2*y^3 - 3*x^3*y^3 + 3*x^4*y^3 = 0.`
> **Formula (_R. J. Mathar_, Jul 26 2022):**
> `Conjecture D-finite with recurrence +n*(2*n+1)*(431*n-2895)*a(n) +2*(-9395*n^3+68622*n^2-64084*n+26109)*a(n-1) +2*(59288*n^3-508196*n^2+1044822*n-574587)*a(n-2) +2*(-94965*n^3+1070605*n^2-3607435*n+3485484)*a(n-3) +4*(29036*n^3-351474*n^2+1402336*n-1970505)*a(n-4) +6*(-6703*n^3+63052*n^2-99178*n-237177)*a(n-5) +6*(1012*n^3-14914*n^2+74580*n-127341)*a(n-6) +6*(1127*n^3-21429*n^2+135199*n-282762 )*a(n-7) +9*(29*n-165)*(2*n-15)*(n-8)*a(n-8)=0.`

Explicitly, for every integer $n \ge 8$ (the range where all indices $n-8, \dots, n$ are non-negative and the inhomogeneous boundary terms vanish), $a(n)$ satisfies
$$
\sum_{j=0}^{8} C_j(n)\, a(n-j) = 0,
$$
where
$$
\begin{aligned}
C_0(n) &= n(2n+1)(431n-2895), \\
C_1(n) &= 2(-9395n^3+68622n^2-64084n+26109), \\
C_2(n) &= 2(59288n^3-508196n^2+1044822n-574587), \\
C_3(n) &= 2(-94965n^3+1070605n^2-3607435n+3485484), \\
C_4(n) &= 4(29036n^3-351474n^2+1402336n-1970505), \\
C_5(n) &= 6(-6703n^3+63052n^2-99178n-237177), \\
C_6(n) &= 6(1012n^3-14914n^2+74580n-127341), \\
C_7(n) &= 6(1127n^3-21429n^2+135199n-282762), \\
C_8(n) &= 9(29n-165)(2n-15)(n-8).
\end{aligned}
$$
Moreover, since $C_0(n) > 0$ for all $n \ge 7$, the recurrence uniquely determines $a(n)$ for all $n \ge 8$ from $a(0), \dots, a(7)$.

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-27T09:09:45Z – 2026-11-27T09:12:00Z
- **Sources Checked:**
  - `tools/novelty_grep.py A108449 "no pyramids"`: 0 hits across 606 files.
  - `tools/arxiv_fetch.py query 'all:"A108449"'` and `'all:"no pyramids" AND all:"(2,1)"'`: 0 hits.
  - Zenodo API (`curl` `https://zenodo.org/api/records?q=A108449` and `q="no+pyramids"`): 0 hits.
  - Crossref API (`https://api.crossref.org/works?query=A108449`): 0 hits.
  - GitHub (`gh search issues "A108449"`): 0 hits.
  - Web search (`"A108449" "D-finite" OR "Mathar" OR "recurrence"`): 0 proofs found; OEIS A108449 rev. 13 (2025-11-05) still lists Mathar's recurrence as `Conjecture`.
- **Verdict:** Open and unclaimed.
