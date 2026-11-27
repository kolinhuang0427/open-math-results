---
source: https://oeis.org/A177260 (rev. 27, 2025-11-05T15:22:18-05:00)
status: reported
owner: scout-5
updated: 2026-11-27T09:08:30Z
identifiers: ["A177260", "R. J. Mathar", "D-finite", "a(n) = (n-1)*a(n-1) + (n-1)*a(n-2) + 2*a(n-4) + (n-1)*a(n-5) + 3*a(n-8)", "adjacent 4-cycles", "Brualdi-Deutsch"]
---

# OEIS A177260 — Mathar (2022) D-Finite Recurrence Conjecture

## Exact Statement
From OEIS **A177260** (revision 27, `2025-11-05T15:22:18-05:00`), offset `0,4`:
> **Name:** Number of derangements of {1,2,...,n} having no adjacent 4-cycles (an adjacent 4-cycle is a cycle of the form (i,i+1,i+2,i+3)).
> **Formula:** `a(n) = Sum_{s=0..n} Sum_{t=0..floor((n-s)/4)} (-1)^(s+t)*(n-3*t)!/(s!*t!).`
> **Formula (_R. J. Mathar_, Jul 26 2022):**
> `Conjecture: D-finite with recurrence a(n) = (n-1)*a(n-1) + (n-1)*a(n-2) + 2*a(n-4) + (n-1)*a(n-5) + 3*a(n-8). - _R. J. Mathar_, Jul 26 2022`

Explicitly, for $n \ge 0$, $a(n)$ is given by the exact integer double sum
$$a(n) = \sum_{s=0}^{n} \sum_{t=0}^{\lfloor (n-s)/4 \rfloor} (-1)^{s+t} \frac{(n - 3t)!}{s!\, t!},$$
and the conjecture asserts that for all integers $n \ge 8$,
$$a(n) = (n-1)\,a(n-1) + (n-1)\,a(n-2) + 2\,a(n-4) + (n-1)\,a(n-5) + 3\,a(n-8).$$

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-27T09:05:40Z – 2026-11-27T09:06:30Z
- **Sources Checked:**
  - Existing `targets/` directory: no folder for `oeis-A177260` existed prior to claim.
  - `tools/novelty_grep.py A177260`: `0` matches across 605 snapshot files.
  - `tools/arxiv_fetch.py query 'all:"A177260"'`: `0` results.
  - Full LaTeX source of `arXiv:1005.0781v2` (Brualdi–Deutsch, *Adjacent q-cycles in permutations*, 2010): derives only the explicit inclusion-exclusion sum (Theorem 7 / eq. (27)) for multi-length forbidden cycles $Q$; does not derive any recurrence or ODE for $Q = \{1, 4\}$ ($A177260$).
  - Live Zenodo API (`curl -s "https://zenodo.org/api/records?q=A177260&size=3"`): `0` hits (`"total": 0`).
  - Live OEIS `A177260` (rev. 27, `2025-11-05`): Mathar's recurrence remains marked `Conjecture:`, with no proof link.
  - Web search (`"A177260" Mathar recurrence`): no proof found.
  - Live GitHub (`gh search issues "A177260"` and `Drogobo/fable-5-proof`): only hit is `trureturing#27184` mentioning `A177260` as an unproved sibling; `Drogobo/fable-5-proof` contains only `proof-A177258-mathar-conjecture.md` (proving `A177258` only).
- **Near Misses:** Seiichi Manyama (Feb 22 2024) posted the OGF $\sum_{k \ge 0} k! x^k / (1 + x + x^4)^{k+1}$ on OEIS `A177260` without proving Mathar's recurrence; Vaclav Kotesovec (2021) gave $a(n) \sim e^{-1} n!$; `Drogobo/fable-5-proof` proved sibling `A177258` only.
- **Not Covered:** `gh search code` was rate-limited (HTTP 429) during the preceding window.
