# Independent Blind Audit — `oeis-A383410`

- **Auditor:** `audit-3` (`auto`)
- **Verdict:** **PASS**
- **Charter Label:** `written proof, internally audited`

## 1. Blindness & Scope

Audited strictly from primary sources (live OEIS `A383410` rev. 6 and `A005649` rev. 123, verified via live OEIS JSON and `oeis/oeisdata` mirror), `targets/oeis-A383410/TARGET.md`, `targets/oeis-A383410/PROOF.md`, and the independent checker's artifacts `targets/oeis-A383410/notes/check-check-1.{md,py}`. Author `verify.py` and author scratch notes were not read.

## 2. Primary Source Fidelity

- **OEIS `A383410` (`rev. 6`, Mikhail Kurkov, Apr 26 2025, offset `0,3`):**
  - `%N`: `Array read by downward antidiagonals: A(n,k) = Sum_{i=0..n-1} Sum_{j=0..k+1} binomial(n-1,i)*binomial(k+1,j)*A(i,j) with A(0,k) = 1, n >= 0, k >= 0.`
  - `%F`: `Conjecture: A(n,0) = A005649(n).`
- **OEIS `A005649` (`rev. 123`, offset `0,2`):**
  - `%N`: `Expansion of e.g.f. (2 - e^x)^(-2).`
- `TARGET.md` L3, L12–19 and `PROOF.md` L5–10 match the primary OEIS definitions, revisions, indexing (`n >= 0`, `k >= 0`, offset `0`), and conjecture verbatim.
- Well-definedness: for $n \ge 1, k \ge 0$, every RHS term $A(i, j)$ has $0 \le i \le n - 1$, so induction on $n$ (and likewise antidiagonal order $(n+k, n)$ since $i+j \le n+k$ and $i < n$) uniquely defines $A(n, k)$ from $A(0, k) = 1$.

## 3. Line-by-Line Mathematical Audit (`PROOF.md`)

1. **Row EGF and PDE (§1, L14–28):**
   - $F_n(y) = \sum_{k \ge 0} A(n, k) y^k / k! \in \mathbb{Q}[[y]]$ has $F_0(y) = e^y$.
   - Binomial convolution $e^y F_i(y) = \sum_{m \ge 0} (\sum_{j=0}^m \binom{m}{j} A(i,j)) y^m/m!$ and differentiation $\partial_y(e^y F_i(y))$ shifting $m \mapsto k+1$ are exact.
   - Summing the defining recurrence against $y^k/k!$ yields $F_n(y) = \sum_{i=0}^{n-1}\binom{n-1}{i}\partial_y(e^y F_i(y))$ ($n \ge 1$); summing against $x^{n-1}/(n-1)!$ yields $\partial_x F(x, y) = e^x \partial_y(e^y F(x, y))$ in $\mathbb{Q}[[x, y]]$. Verified with no convergence or interchange gaps.
2. **Closed-form solution and uniqueness (§2, L32–48):**
   - $U(x, y) := e^y F(x, y)$ satisfies $\partial_x U = e^{x+y}\partial_y U$ with $U(0, y) = e^{2y}$. Extracting $[x^n/n!]$ gives $U_{n+1}(y) = e^y \sum_{i=0}^n \binom{n}{i} \partial_y U_i(y)$ ($n \ge 0$), proving uniqueness in $\mathbb{Q}[[x, y]]$.
   - $D(x, y) := 1 + e^{-y} - e^x$ has constant term $D(0,0) = 1 \neq 0$, so $\widetilde{U} = D^{-2} \in \mathbb{Q}[[x, y]]$ is well-defined.
   - At $x=0$, $D(0, y) = e^{-y} \implies \widetilde{U}(0, y) = e^{2y} = U(0, y)$.
   - Formal derivatives: $\partial_x \widetilde{U} = 2e^x D^{-3}$ and $\partial_y \widetilde{U} = 2e^{-y} D^{-3}$, so $e^{x+y}\partial_y \widetilde{U} = 2e^x D^{-3} = \partial_x \widetilde{U}$. By uniqueness, $U = \widetilde{U}$ and $F(x, y) = e^{-y}(1 + e^{-y} - e^x)^{-2}$.
3. **Conclusion (§3, L52–56):**
   - Evaluating at $y = 0$ (continuous ring homomorphism $\mathbb{Q}[[x, y]] \to \mathbb{Q}[[x]]$) gives $\sum_{n \ge 0} A(n, 0) x^n/n! = F(x, 0) = (2 - e^x)^{-2}$, the defining EGF of `A005649` (offset `0`), so $A(n, 0) = \mathrm{A005649}(n)$ for all $n \ge 0$.

## 4. Independent Mechanical & Exactness Check

- Audited `targets/oeis-A383410/notes/check-check-1.py` (AST check: `floats: []`; all divisions are SymPy exact rationals/expressions) and executed `.venv/bin/python -u targets/oeis-A383410/notes/check-check-1.py`: exited `0` (`PASS`), confirming symbolic PDE and specialization, all `55` live OEIS `A383410` `%S` antidiagonal terms, all `20` live OEIS `A005649` `%S` terms, $A(n,0) = \mathrm{A005649}(n)$ for $0 \le n \le 20$, and bivariate EGF agreement up to total degree $10$.
- Local snapshot check (`grep -rn "A383410" watch/snapshots/`): `0` hits across all snapshot files.
