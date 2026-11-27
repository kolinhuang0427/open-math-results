# Adversarial Audit Report (`audit-1`): `targets/oeis-A045742/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A045742` — R. J. Mathar's Jul 26 2022 D-finite recurrence conjecture
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-3.md`, `notes/check-check-3.py`, and live OEIS `A045742` (rev. 20, `2022-07-26T12:51:11-04:00`)
- **Verdict:** **PASS** (Label: `"written proof, internally audited"`)

---

## 1. Primary-Source Statement Fidelity

Fetched live OEIS JSON (`https://oeis.org/search?q=id:A045742&fmt=json`, rev. 20, `2022-07-26T12:51:11-04:00`, offset `2,3`):
- **Name:** `Number of interior faces in all noncrossing connected graphs on n nodes on a circle.`
- **Established Formula (`%F`):** `a(n) = Sum_{k=1..n-2} k*binomial(n+k-2, k)*binomial(3*n-3, n-2-k)/(n-1).` (Empty sum gives $a(2) = 0$.)
- **Conjecture (`%F`, _R. J. Mathar_, Jul 26 2022):**
  `Conjecture D-finite with recurrence n*(n-1)*(523*n-1993)*a(n) -6*(n-1)*(759*n^2-6019*n+12790)*a(n-1) -12*(n-2)*(4707*n^2-17937*n+6260)*a(n-2) +72*(3*n-10)*(759*n-2224)*(3*n-11)*a(n-3)=0.`
- **Data (19 terms, `a(2)..a(20)`):** `0,1,13,141,1456,14778,149031,...`

`TARGET.md` and `PROOF.md` match the primary OEIS entry verbatim, with exact domain $n \ge 5$ (matching offset $2$ since $n - 3 \ge 2$) and $C_0(n) = n(n-1)(523n - 1993) > 0$ for all $n \ge 4$.

---

## 2. Line-by-Line Mathematical Verification of `PROOF.md`

- **Step 1 (L16–52, Lagrange–Bürmann inversion & cubic algebraic equation):**
  - Reindexing $m = n - 1 \ge 2$ and applying $t\frac{d}{dt}$ to $(1-t)^{-m}$ gives $a(m+1) = [t^m]\bigl(\frac{t^2}{1-t}\Phi(t)^m\bigr)$ with $\Phi(t) = \frac{(1+t)^3}{1-t} \in 1 + t\mathbb{Z}[[t]]$ (and $[t^m] = 0$ for $m = 0, 1$, matching $a(2) = 0$). Exact.
  - For the unique $t(x) \in x\mathbb{Z}[[x]]$ with $t(x) = x\Phi(t(x))$, Lagrange–Bürmann gives $\sum_{m \ge 2} a(m+1)x^m = \frac{x t'(x)}{t(x)} \cdot \frac{t(x)^2}{1-t(x)}$; differentiating $t(1-t) = x(1+t)^3$ yields $\frac{x t'}{t(1-t)} = \frac{1+t}{1 - 4t + t^2}$ in $\mathbb{Z}[[x]]$ (since $(1-2t)(1+t) - 3t(1-t) = 1 - 4t + t^2 \in \mathbb{Z}[[x]]^\times$), hence $y(x) = \sum_{n \ge 2} a(n) x^n = \frac{x t^2(1+t)}{1 - 4t + t^2}$. Exact.
  - Both $E_1(x, t) = x(1+t)^3 - t(1-t) = 0$ and $E_2(x, y, t) = y(1-4t+t^2) - xt^2(1+t) = 0$ have degree $3$ in $t$, and their $6 \times 6$ Sylvester resultant satisfies $\mathrm{Res}_t(E_1, E_2) = 2x P(x, y)$ in $\mathbb{Z}[x, y]$; cancelling $2x \neq 0$ in the domain $\mathbb{Z}[[x]]$ gives $P(x, y(x)) = 0$. Exact.
- **Step 2 (L54–78, Order-$3$ formal ODE):**
  - Checked displayed partial derivative $P_y = (-27x^3 + 13x^2 - x) + (216x^2 - 2)y + (324x^2 - 3)y^2$ (L55) term-by-term against $P(x,y)$ (L50): exact. Since $y(x) = x^3 + O(x^4)$, $P_y(x, y(x)) = -x + O(x^2) \neq 0$ in $\mathbb{Z}[[x]]$.
  - Inductive polynomial numerators $N_1 = -P_x$, $N_{k+1} = (P_y \partial_x N_k + N_1 \partial_y N_k) P_y - (2k-1) N_k (P_y \partial_x P_y + N_1 \partial_y P_y)$ satisfy $P_y^{2k-1} y^{(k)} = N_k(x, y)$ in $\mathbb{Z}[[x]]$ ($k = 1, 2, 3$).
  - Exact $\mathbb{Z}[x,y]$ polynomial division $Q(x,y) = P(x,y) R(x,y)$ (zero remainder) and cancellation of $P_y(x, y(x))^5 \neq 0$ yield $2544x^3 + \sum_{k=0}^3 p_k(x) y^{(k)}(x) = 0$ in $\mathbb{Z}[[x]]$. Exact.
- **Step 3 (L80–91, Coefficient extraction):**
  - Checked all monomial degree shifts $d - k \in [0, 3]$ across $p_0, p_1, p_2, p_3$; for all $n \ge 5$, $[x^n](2544x^3) = 0$, every $m = n - j \ge 2$ lies in the OEIS domain (and at $m = 2, k = 3$ both the falling factorial and $a(2)$ vanish cleanly), and the resulting polynomials in $\mathbb{Z}[n]$ match Mathar's $C_0(n), \dots, C_3(n)$ identically. Exact.

---

## 3. Independent Mechanical Verification

Executed `@check-3`'s independent exact-arithmetic verifier (pure `int` and SymPy `ZZ`, zero floats):
- Command: `.venv/bin/python -u targets/oeis-A045742/notes/check-check-3.py`
- Raw output (exit code `0`):
  ```text
  [1/4] Closed-form sum matches all 19 live OEIS A045742 terms (n=2..20).
  [2/4] Step 1 series identity and 6x6 Sylvester resultant Res_t(E1,E2) = 2x P(x,y) verified.
  [3/4] Step 2 exact Z[x,y] division Q = P*R and order-3 ODE verified.
  [4/4] Step 3 symbolic Z[n] coefficient match and recurrence verified for 5 <= n <= 150.
  PASS
  ```

---

## 4. Verdict

**PASS.** Proof is complete, exact, and matches live OEIS `A045742` rev. 20 verbatim. Ready for Gate 3 novelty verification (`<1h`) once Gate 2 clears.
