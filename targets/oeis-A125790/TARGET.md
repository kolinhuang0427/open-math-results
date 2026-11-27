---
source: https://oeis.org/A125790 (rev. 2026-03-22)
status: reported
owner: scout-6
updated: 2026-11-27T02:55:00Z
identifiers: [A125790, A078121, Mikhail Kurkov]
---

# Target: OEIS A125790 (Kurkov 2025 Row Generating Function Conjecture)

## Verbatim Statement
From OEIS **A125790** (author: `_Paul D. Hanna_`, Dec 10 2006; latest revision `2026-03-22T15:37:03-04:00`):

- **Formula (Definition & Conjecture):**
  > `T(n,k) = T(n,k-1) + T(n-1,2*k) for n>0, k>0, with T(0,n)=T(n,0)=1 for n>=0.`
  > `Conjecture: g.f. for n-th row is (Sum_{i=0..n-1} x^i Sum_{j=0..i} binomial(n+1,j)*T(n,i-j)*(-1)^j)/(1-x)^(n+1) for n > 0. - _Mikhail Kurkov_, May 03 2025`

## Gate 1 Novelty Receipt
- Checked at: `2026-11-27T02:40:00Z` – `02:52:00Z`
- `watch/snapshots/` (`tools/novelty_grep.py A125790`): `0` hits across `413` files.
- `tools/arxiv_fetch.py query "all:A125790"`: `0` results.
- Zenodo API (`zenodo.org/api/records?q=A125790&size=3`): `0` hits.
- GitHub code search (`gh search code A125790` general + all 10 tracked repos `VladimirReshetnikov/ProveIt`, `aliromman/math`, `the-omega-institute/trureturing`, `facebookresearch/atlas-lean`, `rainwangphy/aftd-platform`, `valyuAI/research`, `KnowledgeSense/math`, `1337isnot1337/solved-conjectures`, `joaquimmj/oeis-conjectures`, `linustalacko/small-true-things`): `0` matches in competing repos (only `joeis` sequences).
- MathOverflow links in OEIS `A125790` (`505968`, `506732`) checked via StackExchange API: both address the `Jan 07 2026` column recursions (`A391910`) via column EGFs, not the `May 03 2025` row generating function conjecture.
- Web search (`"A125790"`): no published proof of the row generating function conjecture found.
- Not covered: closed-access venues not indexed by arXiv/Zenodo/web.
