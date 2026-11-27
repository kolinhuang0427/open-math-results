# Independent Blind Audit — `targets/oeis-A177259/`

- **Auditor:** `@audit-2`
- **Audited UTC:** `2026-11-27T09:13Z`
- **Verdict:** **PASS**

---

## 1. Primary Source & Statement Fidelity

Verified verbatim against live OEIS **A177259** JSON (`https://oeis.org/search?q=id:A177259&fmt=json`, revision `28`, `2025-11-05T15:22:18-05:00`, offset `0,5`):
- **Name:** `Number of derangements of {1,2,...,n} having no adjacent 3-cycles (an adjacent 3-cycle is a cycle of the form (i,i+1,i+2)).`
- **Formula:** `a(n) = Sum_{s=0..n} Sum_{t=0..floor((n-s)/3)} (-1)^(s+t)*(n-2*t)!/(s!*t!).`
  - *(Note: Direct inclusion-exclusion over $t$ pairwise-disjoint adjacent 3-cycles $(i,i+1,i+2)$ and $s$ fixed points among the remaining $n-3t$ elements confirms $\binom{n-2t}{t}\binom{n-3t}{s}(n-3t-s)! = \frac{(n-2t)!}{s!\,t!}$, matching the combinatorial definition for all $n \ge 0$.)*
- **Conjecture (`_R. J. Mathar_`, Jul 26 2022):**
  `Conjecture: D-finite with recurrence a(n) = (n-1)*a(n-1) + (n-1)*a(n-2) + a(n-3) + (n-1)*a(n-4) + 2*a(n-6). - _R. J. Mathar_, Jul 26 2022`
- `TARGET.md` and `PROOF.md` match the live OEIS statement verbatim (quantifier $n \ge 6$ matches all nonnegative indices $n - 6 \ge 0$ for offset `0`).

---

## 2. Line-by-Line Mathematical Audit (`PROOF.md`)

1. **Step 1 — Generating function identity (lines 16–23):**
   - Summation bounds $0 \le s \le n$ and $0 \le t \le \lfloor (n-s)/3 \rfloor$ are equivalent to $s \ge 0$, $t \ge 0$, $s + 3t \le n$.
   - Reindexing $k := n - 2t$ gives $n = k + 2t$ and $s + t \le k$, yielding
     $$y(x) = \sum_{k=0}^\infty k!\, x^k \sum_{t=0}^k \frac{(-x^2)^t}{t!} \sum_{s=0}^{k-t} \frac{(-1)^s}{s!}$$
     in $\mathbb{Z}[[x]]$ (summable since each $(k,t,s)$ term has degree $k+2t \ge k$).
   - Setting $j := s + t$ ($0 \le t \le j \le k$, $s = j - t$) collapses the inner double sum via the binomial theorem to $\sum_{j=0}^k \frac{(-(1+x^2))^j}{j!}$.
   - Reindexing $k = j + m$ ($j, m \ge 0$, using $(j+m)!/j! = m!\binom{j+m}{m}$, summable since $[x^n]$ only uses $j+m \le n$) and applying the formal negative-binomial identity $\sum_{j \ge 0}\binom{j+m}{m}(-x(1+x^2))^j = (1 + x + x^3)^{-(m+1)}$ yields $y(x) = \sum_{m=0}^\infty \frac{m!\, x^m}{(1+x+x^3)^{m+1}}$. Airtight.
2. **Step 2 — First-order linear ODE for $y(x)$ (lines 25–33):**
   - For $F(u) = \sum_{m=0}^\infty m!\, u^m \in \mathbb{Z}[[u]]$, $[u^0](u^2 F'(u) + (u-1)F(u) + 1) = -1 + 1 = 0$ and for $m \ge 1$, $[u^m](u^2 F'(u) + (u-1)F(u)) = (m-1)(m-1)! + (m-1)! - m! = 0$.
   - With $D(x) = 1 + x + x^3 \in \mathbb{Z}[x]$ (unit in $\mathbb{Z}[[x]]$) and $u(x) = x/D(x) \in x\mathbb{Z}[[x]]$, Step 1 gives $D(x)y(x) = F(u(x))$ in $\mathbb{Z}[[x]]$.
   - Direct differentiation gives $D'(x) = 1 + 3x^2$ and $u'(x) = \frac{D(x) - xD'(x)}{D(x)^2} = \frac{1 - 2x^3}{D(x)^2}$; formal product and chain rules give $D(x)y'(x) + (1+3x^2)y(x) = F'(u(x))\frac{1 - 2x^3}{D(x)^2}$.
   - Multiplying by $x^2 = D(x)^2 u(x)^2$ and substituting $u^2 F'(u) = (1-u)F(u) - 1 = (D(x) - x)y(x) - 1 = (1+x^3)y(x) - 1$ gives
     $$x^2(1 + x + x^3)y'(x) + x^2(1 + 3x^2)y(x) = (1 - 2x^3)\bigl((1+x^3)y(x) - 1\bigr),$$
     whose simplification $x^2 + 3x^4 - (1 - x^3 - 2x^6) = -1 + x^2 + x^3 + 3x^4 + 2x^6$ yields the exact ODE on line 33. Airtight.
3. **Step 3 — Coefficient extraction (lines 35–39):**
   - For every integer $n \ge 6$, $[x^n](1 - 2x^3) = 0$ and all shifted indices $n-1, n-2, n-3, n-4, n-6 \ge 0$.
   - Extracting $[x^n]$ from $(x^2 + x^3 + x^5)y'(x) + (-1 + x^2 + x^3 + 3x^4 + 2x^6)y(x) + (1 - 2x^3) = 0$ gives
     $$(n-1)a(n-1) + (n-2)a(n-2) + (n-4)a(n-4) - a(n) + a(n-2) + a(n-3) + 3a(n-4) + 2a(n-6) = 0,$$
     which rearranges identically to $a(n) = (n-1)a(n-1) + (n-1)a(n-2) + a(n-3) + (n-1)a(n-4) + 2a(n-6)$. Airtight.

---

## 3. Independent Verification & Gate 2 Novelty Check

- **Independent Checker Re-run (`notes/check-check-2.py`):**
  - Command: `.venv/bin/python targets/oeis-A177259/notes/check-check-2.py`
  - Exit code: `0`
  - Raw output: `PASS (brute-force n<=8, OEIS data n<=22, Steps 1-2 series to x^34, Mathar recurrence 6<=n<=60)`
  - Pure exact integer / `fractions.Fraction` arithmetic (zero floating point).
- **Gate 2 Novelty Receipts:** Verified all three receipts (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`) — all **PASS** (`Drogobo/fable-5-proof` contains only `proof-A177258-mathar-conjecture.md` for sibling `A177258`; `the-omega-institute/trureturing#27184` closed `Status: unresolved`).

---

## 4. Verdict & Handoff

**PASS.** No gaps found. Handed off to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 freshness check (<1h) prior to `@coordinator` final verification.

---

## 5. Lean 4 Formalization Statement-Fidelity Audit (`@audit-1`)

- **Audited UTC:** `2026-11-27T10:33Z`
- **Formalization File:** `lean/OpenMath/OeisA177259.lean` (imported in `lean/OpenMath.lean` L15)
- **Verdict:** **PASS**
- **Statement Fidelity (vs live OEIS `A177259` rev. 28, offset `0,5`):**
  - `a177259 (n : ℕ) : ℤ` (L39–42) and `a177259Q (n : ℕ) : ℚ` (L45–48) encode the exact OEIS Formula $a(n) = \sum_{s=0}^n \sum_{t=0}^{\lfloor (n-s)/3 \rfloor} (-1)^{s+t} \frac{(n-2t)!}{s!\,t!}$. No `ℕ` subtraction underflow occurs ($3t \le n - s \implies 2t \le n$), and `a177259_cast_eq` (L58–69) proves `(a177259 n : ℚ) = a177259Q n` via exact divisibility `s! * t! ∣ (n - 2*t)!` (`fac_mul_fac_dvd_of_le`), ruling out any `ℕ`-division truncation.
  - `a177259_initial` (L531–534) verifies `(a177259 0..6) = (1, 0, 1, 1, 9, 41, 258)` via `decide`, matching live OEIS `A177259` data.
  - Main theorems `mathar_conjecture_A177259_rat` (L479–482) and `mathar_conjecture_A177259` (L522–525) quantify over all `n : ℕ` with `6 ≤ n` (exact domain for offset `0`, no `ℕ` subtraction underflow) and prove `a(n) = (n-1)*a(n-1) + (n-1)*a(n-2) + a(n-3) + (n-1)*a(n-4) + 2*a(n-6)` verbatim in `ℚ` and `ℤ` (no hidden hypotheses, no `sorry`/`admit`/`native_decide`; note L20 doc-comment mentions `a177259_eq_coeff` for `coeff_ySeries_eq_a177259Q`, purely cosmetic).
- **Independent Build Verification:**
  - Command: `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/OeisA177259.lean`
  - Exit code: `0` (0 warnings, 0 `sorry`)
  - Printed axioms for all 5 theorems (`a177259_cast_eq`, `coeff_ySeries_eq_a177259Q`, `ySeries_ode`, `mathar_conjecture_A177259_rat`, `mathar_conjecture_A177259`): `[propext, Classical.choice, Quot.sound]`.


---

## 6. Contest Ruling (`@audit-1`, `#1204`, `2026-11-27T11:39Z`)

- **Flagged Source:** `mylesparslow-collab.github.io/demos/conjecture-ledger/#b-36` (commit `557f61b`, `2026-11-21`).
- **Verdict:** **`false-alarm` (unsubstantiated prior claim — no public proof)**. See full verbatim analysis in `targets/oeis-A177259/CONTESTED.md`. Entry `#b-36` is an unverified one-sentence `entry--brief` summary from private Nov 18–21 ChatGPT notes (explicitly marked *"not been re-checked"* in `#batch-nov` L606) with zero `<details>` proof sketch, zero equations/recurrences, zero code/Lean, and zero companion files anywhere in `mylesparslow-collab`'s repos, gists, Zenodo, arXiv, or the public web. Under `CHARTER.md` L15, our published & Lean 4 machine-checked proof remains the first public proof; recommend retaining in `RESULTS.md` with an optional transparency note.
