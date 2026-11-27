# Adversarial Audit Report: `targets/oeis-A125790/`

- **Auditor:** `audit-1`
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`
- **Gate 3 Status:** Gate 3 Clear (`notes/novelty-gate3-watch-{1,5,6}.md`, all PASS; no `CONTESTED.md`)

---

## 1. Strict Isolation Record

Inspected ONLY:
- Live primary source: OEIS `A125790` (`https://oeis.org/search?q=id:A125790&fmt=json`, rev `47`, `2026-03-22T15:37:03-04:00`), plus related OEIS entries `A078121` (rev `62`), `A125800` (rev `27`), MathOverflow threads `492030` (answer `492359` & comments), `504757`, `504910` (answer `505968`), `506710` (answer `506732`), and `the-omega-institute/trureturing#29156`.
- `targets/oeis-A125790/TARGET.md`
- `targets/oeis-A125790/PROOF.md`
- `targets/oeis-A125790/notes/check-check-1.md`
- `targets/oeis-A125790/notes/check-check-1.py`
- Gate 2 receipts `notes/novelty-gate2-watch-{1,2,5,6}.md` (and confirmed absence of `CONTESTED.md`).

Did **not** inspect `verify.py` or any author scratch `notes/`.

---

## 2. Primary-Source Statement Fidelity

- **Live OEIS `A125790` (rev `47`, `2026-03-22`):**
  - Established recurrence (Paul D. Hanna, Dec 10 2006): `T(n,k) = T(n,k-1) + T(n-1,2*k) for n>0, k>0, with T(0,n)=T(n,0)=1 for n>=0.`
  - *(Definition cross-check against OEIS Name `column k equals row sums of matrix power A078121^k`: since the lower triangular matrix $M = \mathrm{A078121}$ has $M(j,0)=1$ and lower-right shift submatrix $S(M) = M^2$, we have $M^k = \begin{pmatrix}1 & 0 \\ v_k & M^{2k}\end{pmatrix}$ and $T(n,k) = (M^{k+1})_{n,0} = (M^k)_{n,0} + \sum_{j=0}^{n-1}(M^{2k})_{n-1,j} = T(n,k-1) + T(n-1,2k)$ with $T(0,k)=T(n,0)=1$, confirming exact equivalence.)*
  - Verbatim conjecture (`_Mikhail Kurkov_`, May 03 2025): `Conjecture: g.f. for n-th row is (Sum_{i=0..n-1} x^i Sum_{j=0..i} binomial(n+1,j)*T(n,i-j)*(-1)^j)/(1-x)^(n+1) for n > 0.`
- **Match:** `TARGET.md` and `PROOF.md` match OEIS `A125790` verbatim for every integer $n \ge 1$ with zero domain, quantifier, or index drift.

---

## 3. Adversarial Line-by-Line Mathematical Audit

- **Step 1 (Polynomiality & boundary vanishing $P_n(-1) = 0$):**
  - Base case $n = 0$: $P_0(t) := 1 \in \mathbb{Q}[t]$ has $\deg P_0 = 0 \le 0$ and $P_0(k) = 1 = T(0, k)$ for all $k \ge 0$.
  - Inductive step ($n \ge 1$): $V_n = \{f \in \mathbb{Q}[t] : \deg f \le n,\, f(0) = 0\}$ has basis $\{t, \ldots, t^n\}$ ($\dim_{\mathbb{Q}} V_n = n$), and $W_{n-1} = \{g \in \mathbb{Q}[t] : \deg g \le n - 1\}$ has basis $\{1, \ldots, t^{n-1}\}$ ($\dim_{\mathbb{Q}} W_{n-1} = n$). The backward difference $(\nabla f)(t) = f(t) - f(t-1)$ maps $V_n$ linearly into $W_{n-1}$ with trivial kernel (any $f \in \ker \nabla$ satisfies $f(m) = f(0) = 0$ for all $m \ge 0$, so $f \equiv 0$), hence is an isomorphism.
  - Since $P_{n-1}(2t) \in W_{n-1}$, there is a unique $P_n(t) \in \mathbb{Q}[t]$ of degree $\le n$ with $P_n(0) = 1$ and $P_n(t) - P_n(t-1) = P_{n-1}(2t)$.
  - Induction on $k \ge 0$ gives $P_n(k) = T(n, k)$ for all $k \ge 0$, and evaluating at $t = 0$ gives $P_n(-1) = P_n(0) - P_{n-1}(0) = 1 - 1 = 0$.
  - *(Note: Combinatorially $T(n, k)$ counts partitions of $k \cdot 2^n$ into powers $1, 2, \ldots, 2^n$, i.e. the Ehrhart polynomial of the lattice simplex $\{y \in \mathbb{R}_{\ge 0}^n : \sum_{j=1}^n 2^j y_j \le 2^n\}$ which has no interior lattice points, independently explaining $P_n(-1) = 0$ via Ehrhart–Macdonald reciprocity.)*
- **Step 2 (Vanishing of $c_i$ for $i \ge n$):**
  - Multiplying $F_n(x) = \sum_{k \ge 0} T(n, k) x^k$ by $(1 - x)^{n+1}$ in $\mathbb{Q}[[x]]$ gives coefficients $c_i = \sum_{j=0}^{\min(i, n+1)} \binom{n+1}{j}(-1)^j T(n, i-j)$.
  - Because $\deg P_n \le n$, $(\nabla^{n+1} P_n)(i) = \sum_{j=0}^{n+1} \binom{n+1}{j}(-1)^j P_n(i-j) = 0$ for all $i \in \mathbb{Z}$.
  - For $i \ge n + 1$, every $i - j \ge 0$, so $c_i = (\nabla^{n+1} P_n)(i) = 0$.
  - For $i = n$, $n - j \ge 0$ for $0 \le j \le n$, while the $j = n + 1$ term is $(-1)^{n+1} P_n(-1) = 0$ by Step 1(2); thus $c_n = (\nabla^{n+1} P_n)(n) = 0$.
  - Hence $(1 - x)^{n+1} F_n(x) = \sum_{i=0}^{n-1} c_i x^i$, and dividing by the unit $(1 - x)^{n+1} \in \mathbb{Q}[[x]]^\times$ establishes Kurkov's conjecture for all $n \ge 1$. **No gaps.**

---

## 4. Independent Mechanical Verification & Novelty Status

- **Independent script re-execution:** Re-ran `.venv/bin/python -u /Users/kev/Documents/open-math/targets/oeis-A125790/notes/check-check-1.py`: exited with status `0`, outputting `PASS` (verified OEIS rows `0 <= n <= 8`, Step 1 polynomials $P_n(t)$ and $P_n(-1)=0$, $\nabla: V_n \to W_{n-1}$ exact matrix determinant $\neq 0$, and Kurkov's row g.f. expansion through $x^{40}$ for all $1 \le n \le 10$).
- **Direct MathOverflow / literature / prior-art checks:**
  - Inspected **MO Q492030** (posted May 3, 2025 by Mikhail Kurkov, where he also asked a variant of the row g.f. alongside two binary-partition signed-sum conjectures) and accepted **MO Answer 492359** + its comments: Answer `492359` explicitly addressed ONLY the signed-sum conjectures and confirmed in comments *"I did not address the generating function in this answer"*.
  - Inspected **MO Q504910 / A505968**, **MO Q506710 / A506732**, **MO Q504757 / A504889**, and **`the-omega-institute/trureturing#29156`** (open, 0 comments): all concern Kurkov's Jan 2026 *column* transforms (`A391910`), not the May 2025 *row* generating function conjecture.
  - Checked arXiv binary-partition/Ehrhart papers, web search, and all 4 Gate 2 receipts (`notes/novelty-gate2-watch-{1,2,5,6}.md`): clear; no `CONTESTED.md`.
- **Gate 3 receipts (all PASS, no `CONTESTED.md`):**
  - `targets/oeis-A125790/notes/novelty-gate3-watch-1.md` (`2026-11-27T05:35:00Z`, PASS): Sweep 17 snapshots, live OEIS `A125790` rev 47, Zenodo, and 14+ competing repos incl. `joaquimmj/oeis-conjectures` (`trureturing#29156` confirmed MO 506710 column transform only) clear.
  - `targets/oeis-A125790/notes/novelty-gate3-watch-5.md` (`2026-11-27T05:53:04Z`, PASS): 522 snapshots, live arXiv, OEIS rev 47, Zenodo, Crossref, web search, and 15 competing repos clear.
  - `targets/oeis-A125790/notes/novelty-gate3-watch-6.md` (`2026-11-27T05:06:41Z`, PASS): 616 discovered repo snapshots, live OEIS rev 47, and live `trureturing` clear.
- Ready for final report to `@coordinator` with label `"written proof, internally audited"`.

---

## 5. Independent Lean Statement-Fidelity Audit (`audit-2`, `2026-11-27T09:02Z`)

- **Auditor:** `audit-2`
- **File Audited:** `lean/OpenMath/OeisA125790.lean` (584 lines)
- **Verdict:** **`PASS`**

### Statement-Fidelity Verification Against Live Primary Source
Checked verbatim against live OEIS JSON (`A125790`, rev. 47) and `targets/oeis-A125790/TARGET.md`:
1. **`A125790` recurrence fidelity:** `a125790` defines `T(0, k) = 1`, `T(n, 0) = 1`, `T(n + 1, k + 1) = T(n + 1, k) + T(n, 2 * (k + 1))`, and `a125790_rec` matches the verbatim OEIS formula `T(n, k) = T(n, k - 1) + T(n - 1, 2 * k)` for `n > 0, k > 0`.
2. **Row generating function & numerator fidelity:** `rowGF n : PowerSeries ℚ` encodes $\sum_{k \ge 0} T(n, k) x^k \in \mathbb{Q}[[x]]$, and `kurkovNum n` matches `Sum_{i=0..n-1} x^i Sum_{j=0..i} binomial(n+1, j) * T(n, i-j) * (-1)^j` with exact `Finset.range n` ($0 \le i \le n - 1$) and `Finset.range (i + 1)` ($0 \le j \le i$) index bounds.
3. **Main theorems:** For every `n ≥ 1`, `kurkov_row_gf_mul` proves `(1 - X)^(n + 1) * rowGF n = kurkovNum n`, `kurkov_row_gf` proves `rowGF n = kurkovNum n * ((1 - X)^(n + 1))⁻¹` in `ℚ⟦X⟧`, and `kurkov_row_gf_of_recurrence` states the identical theorem universally for any `T : ℕ → ℕ → ℕ` satisfying the literal OEIS boundary and recurrence equations.
4. **Hygiene:** Zero `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, or `implemented_by`.

**Verification command for `@coordinator`:** `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake build OpenMath.OeisA125790 && lake env lean OpenMath/OeisA125790.lean`
