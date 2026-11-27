---
source: google-deepmind/formal-conjectures (FormalConjectures/OEIS/190969.lean) & OEIS A190969
status: reported
owner: attack-2
updated: 2026-11-27T07:56:00Z
identifiers: OEIS A190969, FormalConjectures/OEIS/190969.lean
---

# Target: OEIS A190969 (Zhi-Wei Sun supercongruences for $a(n) = 5a(n-1) - 8a(n-2)$)

## Verbatim Statement

**Primary Source:** OEIS `A190969` (Zhi-Wei Sun, Mar 13 2013; fetched live via `oeis.org/search?q=id:A190969&fmt=json`, `revision: 48`, `time: 2025-11-05T15:22:20-05:00`):
- Name: `a(n) = 5*a(n-1) - 8*a(n-2), with a(0)=0, a(1)=1.`
- Comment: `Let S(p):=Sum_{k=0..p-1} a(4k)*binomial(2k,k)^3/(-4096)^k. Zhi-Wei Sun conjectured that S(p) == 0 (mod p^2) for every odd prime p, and also S(p) == 0 (mod p^3) for any odd prime p == 1,2,4 (mod 7). - _Zhi-Wei Sun_, Mar 13 2013`

**Formalization Source:** `google-deepmind/formal-conjectures` (`FormalConjectures/OEIS/190969.lean`):
```lean
def a : ℕ → ℤ
  | 0 => 0
  | 1 => 1
  | n + 2 => 5 * a (n + 1) - 8 * a n

def sMod (p m : ℕ) : ZMod (p ^ m) :=
  ∑ k ∈ Finset.range p,
    (a (4 * k) : ZMod (p ^ m)) * ((2 * k).choose k : ZMod (p ^ m)) ^ 3 *
      ((-4096 : ZMod (p ^ m)) ^ k)⁻¹

theorem conjecture_1 (p : ℕ) (hp : p.Prime) (hp2 : p ≠ 2) :
    sMod p 2 = 0

theorem conjecture_2 (p : ℕ) (hp : p.Prime) (hp2 : p ≠ 2)
    (h7 : p % 7 ∈ ({1, 2, 4} : Finset ℕ)) :
    sMod p 3 = 0
```

## Gate 1 Novelty Receipt
- **Checked UTC:** `2026-11-27T03:19:34Z`
- **Sources / Snapshots Checked:**
  - `tools/novelty_grep.py 190969` across all local workspace files and `watch/snapshots/**`: only `FormalConjectures/OEIS/190969.lean` in `formal-conjectures-files.tsv` (0 hits in `discovered/`, `1337-solved-conjectures`, `ai-collections`, `arxiv`, `openai-math`).
  - Live OEIS API (`id:A190969`, rev `48`, `2025-11-05`): both conjectures still stated as open conjectures by Zhi-Wei Sun (Mar 13 2013), with no proof link.
  - `tools/arxiv_fetch.py query` for `all:"A190969" OR all:"190969"` and `all:"4096" AND all:"supercongruence"`: `0` hits; `arXiv:1211.1588` fetched locally (no mention of `190969` or `4096`).
  - `search_web` for `"A190969"`, `"5a(n-1)-8a(n-2)"`, and `"sum_{k=0}^{p-1}" "a(4k)" "4096"`: no proof or counterexample found.
- **Not Covered:** Exhaustive GitHub code search (`gh search code` previously rate-limited HTTP 403).
- **Status Rationale:** Both `conjecture_1` ($\bmod p^2$ for all odd primes $p$) and `conjecture_2` ($\bmod p^3$ for $p \equiv 1,2,4 \pmod 7$) appear genuinely open.
