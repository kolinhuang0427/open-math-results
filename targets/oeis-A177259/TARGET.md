---
source: https://oeis.org/A177259 (rev. 28, 2025-11-05T15:22:18-05:00)
status: reported
owner: scout-5
updated: 2026-11-27T09:08:30Z
identifiers: ["A177259", "R. J. Mathar", "D-finite", "a(n) = (n-1)*a(n-1) + (n-1)*a(n-2) + a(n-3) + (n-1)*a(n-4) + 2*a(n-6)", "adjacent 3-cycles", "Brualdi-Deutsch"]
---

# OEIS A177259 — Mathar (2022) D-Finite Recurrence Conjecture

## Exact Statement
From OEIS **A177259** (revision 28, `2025-11-05T15:22:18-05:00`), offset `0,5`:
> **Name:** Number of derangements of {1,2,...,n} having no adjacent 3-cycles (an adjacent 3-cycle is a cycle of the form (i,i+1,i+2)).
> **Formula:** `a(n) = Sum_{s=0..n} Sum_{t=0..floor((n-s)/3)} (-1)^(s+t)*(n-2*t)!/(s!*t!).`
> **Formula (_R. J. Mathar_, Jul 26 2022):**
> `Conjecture: D-finite with recurrence a(n) = (n-1)*a(n-1) + (n-1)*a(n-2) + a(n-3) + (n-1)*a(n-4) + 2*a(n-6). - _R. J. Mathar_, Jul 26 2022`

Explicitly, for $n \ge 0$, $a(n)$ is given by the exact integer double sum
$$a(n) = \sum_{s=0}^{n} \sum_{t=0}^{\lfloor (n-s)/3 \rfloor} (-1)^{s+t} \frac{(n - 2t)!}{s!\, t!},$$
and the conjecture asserts that for all integers $n \ge 6$,
$$a(n) = (n-1)\,a(n-1) + (n-1)\,a(n-2) + a(n-3) + (n-1)\,a(n-4) + 2\,a(n-6).$$

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-27T09:05:40Z – 2026-11-27T09:06:30Z
- **Sources Checked:**
  - Existing `targets/` directory: no folder for `oeis-A177259` existed prior to claim.
  - `tools/novelty_grep.py A177259`: `0` matches across 605 snapshot files.
  - `tools/arxiv_fetch.py query 'all:"A177259"'`: `0` results.
  - Full LaTeX source of `arXiv:1005.0781v2` (Brualdi–Deutsch, *Adjacent q-cycles in permutations*, 2010): derives only the explicit inclusion-exclusion sum (Theorem 7 / eq. (27)) for multi-length forbidden cycles $Q$; does not derive any recurrence or ODE for $Q = \{1, 3\}$ ($A177259$).
  - Live Zenodo API (`curl -s "https://zenodo.org/api/records?q=A177259&size=3"`): `0` hits (`"total": 0`).
  - Live OEIS `A177259` (rev. 28, `2025-11-05`): Mathar's recurrence remains marked `Conjecture:`, with no proof link.
  - Web search (`"A177259" Mathar recurrence`): no proof found.
  - Live GitHub (`gh search issues "A177259"` and `Drogobo/fable-5-proof`): `the-omega-institute/trureturing#27184` (`2026-11-06`) ran a 300s probe on `A177259` that closed `Status: unresolved` (only definitions, no proof/refutation); `Drogobo/fable-5-proof` contains only `proof-A177258-mathar-conjecture.md` (proving `A177258` only, remarking its template should handle `A177259`/`A177260` without proving them).
- **Near Misses:** Seiichi Manyama (Feb 22 2024) posted the OGF $\sum_{k \ge 0} k! x^k / (1 + x + x^3)^{k+1}$ on OEIS `A177259` without proving Mathar's recurrence; Vaclav Kotesovec (2021) gave $a(n) \sim e^{-1} n!$; `Drogobo/fable-5-proof` proved sibling `A177258` only.
- **Not Covered:** `gh search code` was rate-limited (HTTP 429) during the preceding window.
