---
source: google-deepmind/formal-conjectures FormalConjectures/OEIS/208425.lean (Zhi-Wei Sun, OEIS A208425)
status: reported
owner: attack-5
updated: 2026-11-27T05:32:00Z
identifiers: OEIS-A208425, FormalConjectures/OEIS/208425.lean, arXiv:2012.05121v3
---

# Target: OEIS A208425 — Zhi-Wei Sun's Supercongruence Conjecture (ii), Part 1 (`conjecture_2`)

## Primary Source Statement (Exact Verbatim Quote)

From **OEIS A208425** (revision 60, `2025-11-05T15:22:21-05:00`, <https://oeis.org/A208425>), comment by **Zhi-Wei Sun** (Nov 12, 2016):

> From _Zhi-Wei Sun_, Nov 12 2016: (Start)
> Conjecture: (i) For any prime p > 3 and positive integer n, the number (a(p*n)-a(n))/(p*n)^3 is always a p-adic integer.
> (ii) For any prime p == 1 (mod 3), we have Sum_{k=0..p-1}a(k) == C(2(p-1)/3,(p-1)/3) (mod p^2). For any prime p == 2 (mod 3), we have Sum_{k=0..p-1}a(k) == 2p/C(2(p+1)/3,(p+1)/3) (mod p^2).
> We have proved part (i) of this conjecture for n = 1. (End)

Here $a(n) = [x^n] \sum_{m \ge 0} \frac{(3m)!}{m!^3} \frac{x^{2m}}{(1-x)^{3m+1}} = \sum_{k=0}^n \binom{n}{k}\binom{n-k}{k}\binom{n+k}{k}$.

Formalized in `google-deepmind/formal-conjectures` (`FormalConjectures/OEIS/208425.lean`, blob `6692a6604859e2615fd452aa1f41cade8b6f8dcc`, `@[category research open, AMS 11]`):
- `conjecture_1`: `3 < p → 0 < n → 0 ≤ padicValRat p (((a (p * n) : ℚ) - (a n : ℚ)) / ((p * n : ℚ) ^ 3))` *(already proved in print — see Gate 1 below)*
- `conjecture_2`: `p.Prime → p % 3 = 1 → (∑ k ∈ Finset.range p, a k) % (p ^ 2) = ((2 * (p - 1) / 3).choose ((p - 1) / 3)) % (p ^ 2)` *(OPEN target)*
- `conjecture_3`: `p.Prime → p % 3 = 2 → ((∑ k ∈ Finset.range p, (a k : ℚ)) - (2 * p : ℚ) / ((2 * (p + 1) / 3).choose ((p + 1) / 3) : ℚ)).num % (p ^ 2 : ℤ) = 0` *(already proved & Lean-formalized — see Gate 1 below)*

## Gate 1 Novelty Receipt

- **Checked at (UTC):** `2026-11-26T23:07Z` – `2026-11-26T23:25Z`
- **Sources / snapshots checked:**
  - `watch/snapshots/**` via `.venv/bin/python tools/novelty_grep.py 208425 A208425`: only `FormalConjectures/OEIS/208425.lean` (open).
  - Live OEIS JSON (`https://oeis.org/search?q=id:A208425&fmt=json`, revision 60, `2025-11-05T15:22:21-05:00`): Conjectures (i) and (ii) still listed.
  - arXiv via `tools/arxiv_fetch.py`:
    - `arXiv:2012.05121v3` (Hao Pan & Zhi-Wei Sun, *Supercongruences for central trinomial coefficients*, *Frontiers in Combinatorics and Number Theory* 2 (2026), 55–62): **Theorem 1.2 settles `conjecture_1` completely**, and does **not** address Part (ii) (`conjecture_2`, `conjecture_3`).
    - `query 'all:"208425" OR (all:"2(p-1)/3" AND all:"supercongruence")'`: 0 results.
  - GitHub (`gh search code` + `gh api`) & web search (`search_web`):
    - `epoch-research/LeanOpenProblems-results`: 4 runs on `oeis_208425_conjecture_0` all failed (`sorryAx`).
    - **`Varun-Dudipala/sun-conjectures-lean` (`SunConjectures/A208425/Solution.lean`, `README.md`)**: **settles and Lean-formalizes `conjecture_3`** ($p \equiv 2 \pmod 3$), and explicitly states: *"The companion statements, part (i) and the case $p \equiv 1 \pmod 3$, are not proved here."*
    - **`conjecture_2` ($p \equiv 1 \pmod 3$)**: no published or Lean proof found anywhere.
- **What was not covered:** Offline/unindexed manuscripts after Nov 2026 or papers proving `conjecture_2` without citing A208425 or matching the checked queries.
