# Adversarial Audit Report: `targets/oeis-A379818/`

- **Auditor:** `audit-1`
- **Date (UTC):** 2026-11-26T23:09Z
- **Verdict:** **`PASS`**
- **Charter Label:** `"written proof, internally audited"` (with exact-arithmetic verification of `A025480`, `A379818`, the shift lemma, all 10,000 $(m, k)$ instances with $2^m(2k+1) \le 10{,}000$, and Pascal identities). Note: per `CHARTER.md`, internal auditing and exact computation are not external peer review.
- **Independent Verifier:** `targets/oeis-A379818/notes/check-check-1.py` (authored by `check-1` strictly from live OEIS `A379818`/`A025480` and `PROOF.md`, independently audited and re-executed with exit code `0` and output `PASS`).

---

## 1. Isolation & Reviewed Inputs

Strictly following `CHARTER.md` isolation rules, this audit inspected **only**:
- Primary sources (live OEIS JSON API, fetched directly): `A379818` (revision 8, `2026-02-26T16:45:49-05:00`), `A025480` (revision 235, `2025-11-05T15:21:50-05:00`), and sibling Kurkov sequences `A329369`, `A341392`, `A347205`, `A379819`.
- `targets/oeis-A379818/TARGET.md`
- `targets/oeis-A379818/PROOF.md`
- `targets/oeis-A379818/notes/check-check-1.md` and `notes/check-check-1.py`
- Gate 2 novelty receipts (`notes/novelty-gate2-watch-{1,5,6}.md`), plus direct inspection of `VladimirReshetnikov/ProveIt` (`article.tex`), `aliromman/math`, `KnowledgeSense/math`, and MathOverflow/MathSE web searches.

The author's `verify.py` was **not** read (and no author scratch notes exist in `notes/`).

---

## 2. Primary-Source Fidelity & Definition Audit

Verified word-for-word against live OEIS `A379818` (rev 8, Mikhail Kurkov, created 2025-01-03, rev 2026-02-26) and `A025480` (rev 235):
- **Name (`A379818`):** `a(2n+1) = a(n) for n >= 0, a(2n) = a(n) + a(n - 2^f(n)) + a(2n - 2^f(n)) + a(A025480(n-1)) for n > 0 with a(0) = 1 where f(n) = A007814(n).` (`offset: 0,3`)
- **Formula (`A379818`):** `Conjecture: a(2^m*(2k+1)) = Sum_{j=0..m} (binomial(m+2, j+1) - binomial(m, j))*a(2^j*k) for m >= 0, k >= 0 with a(0) = 1.`
- **PARI program (`A379818`):** Confirmed exact agreement with the recurrence (at even $i = 2n$, $A = 2^{v_2(n)}$ and $i \backslash (4A) = \lfloor (2k+1)/2 \rfloor = k = \mathrm{A025480}(n-1)$).
- **Name (`A025480`):** `a(2n) = n, a(2n+1) = a(n).` (`offset: 0,5`)
- **Well-definedness:** Every recursive index on the RHS is strictly smaller than the LHS index ($n < 2n+1$ for odd indices; for even $2n$ with $n \ge 1$, $1 \le 2^{v_2(n)} \le n$ gives $0 \le n - 2^{v_2(n)} < n \le 2n - 2^{v_2(n)} < 2n$ and $0 \le \mathrm{A025480}(n-1) \le (n-1)/2 < 2n$).
- Zero quantifier, offset, boundary, or definition drift between OEIS, `TARGET.md`, `PROOF.md`, and `notes/check-check-1.py`.

---

## 3. Adversarial Audit of `PROOF.md`

### 3.1 Lemma (`A025480` Shift Identity)
- Claims $b(2^r(2k+1) - 1) = k$ for all integers $r \ge 0, k \ge 0$.
- Base $r = 0$: $2^0(2k+1) - 1 = 2k \implies b(2k) = k$.
- Step $r \ge 1$: $q := 2^{r-1}(2k+1) - 1 \ge 0$ (since $2^{r-1} \ge 1$ and $2k+1 \ge 1$), and $2^r(2k+1) - 1 = 2q + 1$, so $b(2q+1) = b(q) = k$ by the induction hypothesis. Completely airtight (and matches the standard identity recorded in `A025480`).

### 3.2 Main Theorem (Induction on $m \ge 0$, universally for all $k \ge 0$)
Set $c(m, j) := \binom{m+2}{j+1} - \binom{m}{j}$ for $m \ge 0, 0 \le j \le m$. Note $c(m, 0) = c(m, m) = m + 1$ for all $m \ge 0$ (including $m = 0$, where $c(0, 0) = 2 - 1 = 1$).
- **Base case $m = 0$:** For all $k \ge 0$, LHS $= a(2k+1) = a(k)$ by the odd recurrence, and RHS $= c(0, 0) a(k) = a(k)$. Checked edge case $k = 0$: $a(1) = a(0) = 1$.
- **Inductive step ($m \ge 1$):** Assume true at $m - 1$ for all $k' \ge 0$. Fix $k \ge 0$ and set $n = 2^{m-1}(2k+1)$.
  - Since $m \ge 1, k \ge 0$, $n \ge 1$ (valid input to the even recurrence) and $v_2(n) = m - 1$ (since $2k+1$ is odd), so $2^{f(n)} = 2^{m-1}$.
  - Checking each of the four RHS arguments of $a(2n) = a(2^m(2k+1))$:
    1. $n = 2^{m-1}(2k+1)$;
    2. $n - 2^{m-1} = 2^{m-1}(2k) = 2^m k$;
    3. $2n - 2^{m-1} = 2^{m-1}(4k + 1) = 2^{m-1}(2(2k) + 1)$;
    4. $b(n - 1) = b(2^{m-1}(2k+1) - 1) = k$ by the Lemma (valid since $m - 1 \ge 0, k \ge 0$).
  - Applying the induction hypothesis at $m - 1$ to $k' = k \ge 0$ and $k' = 2k \ge 0$ and reindexing $j = i + 1$ in the second sum gives:
    $$a(2^m(2k+1)) = \sum_{j=0}^{m-1} c(m-1, j) a(2^j k) + a(2^m k) + \sum_{j=1}^{m} c(m-1, j-1) a(2^j k) + a(k).$$
  - Checking $m = 1$ explicitly (where the interior range $1 \le j \le m - 1$ is empty): the four terms yield $(c(0,0) + 1)a(k) + (1 + c(0,0))a(2k) = 2a(k) + 2a(2k) = c(1,0)a(k) + c(1,1)a(2k)$.
  - Checking $m \ge 2$:
    - $j = 0$: $c(m-1, 0) + 1 = m + 1 = c(m, 0)$;
    - $1 \le j \le m - 1$: $c(m-1, j) + c(m-1, j-1) = (\binom{m+1}{j+1} + \binom{m+1}{j}) - (\binom{m-1}{j} + \binom{m-1}{j-1}) = \binom{m+2}{j+1} - \binom{m}{j} = c(m, j)$ by Pascal's identity (all indices strictly inside $0 \le r \le N$);
    - $j = m$: $1 + c(m-1, m-1) = 1 + m = c(m, m)$.
  - Checking $k = 0$: $2^j \cdot 0 = 0$ for all $j$, so every term is a multiple of $a(0)$ with the exact same coefficient arithmetic (incidentally yielding $a(2^m) = (3 \cdot 2^m - 2)a(0)$).
- Every step is completely elementary, self-contained, and airtight with zero gaps.

### 3.3 Independent Verifier Re-run
Re-executed `.venv/bin/python /Users/kev/Documents/open-math/targets/oeis-A379818/notes/check-check-1.py` (exit code `0`):
```text
A025480 data (84 terms) & Lemma (755 pairs): OK
A379818 data (62 terms) & Kurkov formula (10000 (m,k) pairs up to n=10000): OK
Pascal boundary & interior identities (1<=m<=30): OK
PASS
```

---

## 4. Novelty Assessment (Gate 3 Clear)

- Live OEIS `A379818` (rev 8, `2026-02-26T16:45:49-05:00`) still explicitly labels the formula `Conjecture:`.
- Inspected sibling Kurkov OEIS entries (`A329369`, `A341392`, `A347205`, `A379819`): `A329369` (Ehrenborg–Steingrímsson 2000) and `A341392` have analogous formulas for 3-term and 2-term recurrences, but lack the fourth term $+ a(\mathrm{A025480}(n-1))$ that characterizes `A379818` and changes the kernel to $\binom{m+2}{j+1} - \binom{m}{j}$.
- Directly inspected `VladimirReshetnikov/ProveIt` (`Analysis/Transseries/docs/series-and-transseries/Factorial_Transseries_OEIS_A006014/article.tex`, lines 1043–1105): it only mentions the separate dyadic partial-sum conjecture for `A006014`, not Kurkov's `a(2^m(2k+1))` formula.
- Gate 2 receipts (`notes/novelty-gate2-watch-{1,5,6}.md`) all passed with no `CONTESTED.md`; direct auditor checks of `aliromman/math`, `KnowledgeSense/math`, `facebookresearch/atlas-lean`, `rainwangphy/aftd-platform`, and MathOverflow/MathSE found no prior proof.
- **Gate 3 live pre-report re-check (all PASS within 1 hour of report, no `CONTESTED.md`; `watch-3` relieved `watch-1` per board #494):**
  - `targets/oeis-A379818/notes/novelty-gate3-watch-3.md` (`2026-11-27T00:25:29Z`, PASS)
  - `targets/oeis-A379818/notes/novelty-gate3-watch-5.md` (`2026-11-27T00:08:52Z`, PASS)
  - `targets/oeis-A379818/notes/novelty-gate3-watch-6.md` (`2026-11-27T00:21:13Z`, PASS)

---

## 5. Lean 4 Statement-Fidelity Audit (`lean/OpenMath/OeisA379818.lean`)

- **Auditor:** `audit-1`
- **Date (UTC):** `2026-11-27T08:53Z`
- **Verdict:** **`PASS`** (upgrade eligible to `"Lean-checked"` once `@coordinator` verifies build/axioms directly)
- **Statement-Fidelity Checks against Live OEIS `A379818` (rev 8), `A025480` (rev 235), `A007814` (rev 549):**
  - `a007814` is proved identically equal to Mathlib's `n.factorization 2` (`a007814_eq_factorization`).
  - `a025480` is proved to satisfy `a025480 (2 * n) = n` and `a025480 (2 * n + 1) = a025480 n` for all `n : ℕ` (`a025480_even`, `a025480_odd`).
  - `a379818` is proved to satisfy `a379818 0 = 1`, `a379818 (2 * n + 1) = a379818 n`, and for `0 < n`, `a379818 (2 * n) = a379818 n + a379818 (n - 2 ^ a007814 n) + a379818 (2 * n - 2 ^ a007814 n) + a379818 (a025480 (n - 1))` (with all `ℕ` subtractions non-truncating since `2 ^ v_2(n) ≤ n` for `n > 0`).
  - `kurkov_conjecture_A379818` matches Kurkov's conjecture verbatim for all `(m k : ℕ)` (`Finset.range (m + 1)` = `0..m`, with `choose_le_choose_add_two` proving non-truncating `ℕ` subtraction); `kurkov_conjecture_A379818_int` gives the equivalent `ℤ`-valued statement; `kurkov_conjecture_A379818_of_recurrence` proves the axiomatic version for any `a : ℕ → ℕ` satisfying the OEIS `A379818` recurrence using Mathlib's `Nat.factorization`.
  - Audited all 346 lines of `lean/OpenMath/OeisA379818.lean`: zero `sorry`, zero custom `axiom`, zero `native_decide`, zero `unsafe`/`implemented_by`; `#print axioms` included for all three main theorems.
- **Verification Command for `@coordinator`:**
  `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake build OpenMath.OeisA379818 && lake env lean OpenMath/OeisA379818.lean`
