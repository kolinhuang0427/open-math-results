---
source: https://oeis.org/A361430 (rev. 41, Jul 05 2026) & https://oeis.org/A298826 (rev. 125, Jun 10 2025)
status: reported
owner: scout-6
updated: 2026-11-27T10:49:30Z
identifiers: [A361430, A298826, A298825, A298674, Vaclav Kotesovec, Werner Schulte, Ridouane Oudra]
---

# Target: OEIS A361430 (`a(n) = abs(A298826(n))`)

## Verbatim Statement
From OEIS **A361430** (`rev. 41`, Jul 05 2026):

> `%N` Multiplicative with a(p^e) = e - 1.
> `%F` Conjecture: a(n) = abs(A298826(n)).

And from OEIS **A298826** (`rev. 125`, Jun 10 2025):

> `%N` a(n) = A298825(n)/n.
> `%F` a(n) = Sum_{k=1..n} (A298674(k, n))/n = A298825(n)/n.
> `%F` Conjecture: a(n) = (-1)^(n+1) * Sum_{d|n} mu(d)*tau(d)*tau(n/d). - _Ridouane Oudra_, Nov 19 2019
> `%F` Conjecture: abs(a(n)) = A361430(n). - _Vaclav Kotesovec_, Mar 12 2023
> `%F` Conjecture: a(n) is multiplicative with a(p^e) = (-1)^p * (e-1) for prime p and e > 0. That conforms to the conjectured Dirichlet generating function (compare Steven Foster Clark, Sep 12 2022). - _Werner Schulte_, Jun 09 2025

*(Data in `%S` of `A361430`: `1,0,0,1,0,0,0,2,1,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,1,0,2,0,0,0,0,4,0,0`; data in `%S/%T/%U` of `A298826`: `1,0,0,1,0,0,0,2,-1,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,-1,0,-2,0,0,0,0,4,0,0,0,-1,...`)*

## Gate 1 Novelty Receipt
- Checked at: `2026-11-27T10:44:30Z` – `2026-11-27T10:47:45Z`
- `watch/snapshots/` (`tools/novelty_grep.py A361430 A298826 A298825 A306653`): `0` hits across 619 files.
- Live GitHub (`gh search repos/issues` on `A361430`, `A298826`, `A298825`; `gh search code "A361430"`): `0` proofs (`joeis`, `joeis-lite`, `Radcliffe/OEIS-Python`, `loda-programs` contain only computational sequence definitions).
- Live Zenodo API (`zenodo.org/api/records?q=A361430`, `A298826`, `A298825`): `0` hits.
- `search_web` (`"A298826" "A361430"`, `"A298826" "multiplicative"`): `0` proofs (only MSE background on the twin-prime Mangoldt sum).
- Live OEIS `A361430` (`rev. 41`) & `A298826` (`rev. 125`): all three identities remain explicitly marked `Conjecture`.

## Attack Log
- Start UTC: `2026-11-27T10:48:04Z`
- End UTC: `2026-11-27T10:49:30Z` (proved directly from the primary matrix definition of `A298826` via CRT summation, establishing Werner Schulte's multiplicative formula, Vaclav Kotesovec's `abs(A298826(n)) = A361430(n)`, and Ridouane Oudra's divisor formula for all $n \ge 1$).
