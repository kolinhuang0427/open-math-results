---
source: https://oeis.org/A379818 (OEIS A379818, rev. 2026-02-26)
status: reported
owner: scout-6
updated: 2026-11-27T01:40:00Z
identifiers: [A379818, A025480, A007814, Mikhail Kurkov]
---

# Target: OEIS A379818 (Mikhail Kurkov 2025/2026 Binomial Formula Conjecture)

## Verbatim Statement
From OEIS **A379818** (author: `_Mikhail Kurkov_`, Jan 03 2025; latest revision `2026-02-26T16:45:49-05:00`):

- **Name:**
  > a(2n+1) = a(n) for n >= 0, a(2n) = a(n) + a(n - 2^f(n)) + a(2n - 2^f(n)) + a(A025480(n-1)) for n > 0 with a(0) = 1 where f(n) = A007814(n).
- **Data (`offset 0`):**
  > 1,1,4,1,10,4,10,1,22,10,28,4,49,10,22,1,46,22,64,10,118,28,64,4,190,49,118,10,190,22,46,1,94,46,136,22,256,64,148,10,424,118,292,28,478,64,136,4,661,190,478,49,796,118,256,10,1177,190,424,22,661,46
- **Formula (Conjecture):**
  > Conjecture: a(2^m*(2k+1)) = Sum_{j=0..m} (binomial(m+2, j+1) - binomial(m, j))*a(2^j*k) for m >= 0, k >= 0 with a(0) = 1.

Cross-referenced `A025480` has Name `a(2n) = n, a(2n+1) = a(n)` and `A007814` is the 2-adic valuation $v_2(n)$.

## Gate 1 Novelty Receipt
- Checked at: `2026-11-26T22:20:13Z` – `22:29:23Z`
- `watch/snapshots/` (`tools/novelty_grep.py A379818`): `0 lines`
- `tools/arxiv_fetch.py query "all:A379818"` and `query "all:A379818 OR (all:Kurkov AND all:A025480)"`: `0` results (and `query "au:Kurkov"` returned 35 physics papers by M. A. Kurkov, none on OEIS A379818).
- Zenodo API (`zenodo.org/api/records?q=%22Mikhail+Kurkov%22+OR+A379818&size=5`): `0` hits.
- GitHub code search (`gh search code A379818 --limit 10`): only `VladimirReshetnikov/ProveIt` (`Factorial_Transseries_OEIS_A006014/article.tex`, which asks about partial sums of `A379818` for `A006014`), no proof of Kurkov's `2^m*(2k+1)` conjecture.
- Web search (`"Mikhail Kurkov" "A379818" OR "binomial(m+2, j+1) - binomial(m, j)"`): only OEIS `A379818` itself; no proof found.
- OEIS `A379818`, `A025480`, `A329369`, `A341392`, `A347205` checked live: `A379818` formula remains marked `Conjecture:` as of `2026-02-26`.
- Not covered: closed-access journals or unindexed private repositories.
