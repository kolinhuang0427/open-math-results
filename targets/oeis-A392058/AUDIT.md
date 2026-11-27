# Independent Blind Audit — `oeis-A392058`

- **Auditor:** `audit-3` (`auto`)
- **Verdict:** **PASS**
- **Charter Label:** `written proof, internally audited`

## 1. Blindness & Scope

Audited strictly from primary sources (live OEIS `A392058` rev. 6 and `A233335` rev. 20, verified via live OEIS JSON and `oeis/oeisdata` mirror), `targets/oeis-A392058/TARGET.md`, `targets/oeis-A392058/PROOF.md`, and the independent checker's artifacts `targets/oeis-A392058/notes/check-check-1.{md,py}`. Author `verify.py` and author scratch notes were not read.

## 2. Primary Source Fidelity

- **OEIS `A392058` (`rev. 6`, Mikhail Kurkov, Dec 29 2025, offset `0,3`):**
  - `%N`: `Array read by downward antidiagonals: A(n,k) = A(n-1,k+1) + Sum_{j=0..k} binomial(k+1,j)*A(n-1,j)*A(k-j,0) with A(0,k) = 1.`
  - `%F`: `Conjecture: A(n,0) = A233335(n+1).`
- **OEIS `A233335` (`rev. 20`, Paul D. Hanna, Dec 07 2013, offset `0,3`):**
  - `%N`: `E.g.f. A(x) satisfies A( Integral 1/A(x) dx ) = exp(x).`
  - `%e` confirms $A(x) = 1 + x + 2x^2/2! + 7x^3/3! + \dots$ ($A(0) = 1$) and zero-constant integral $\int_0^x dt/A(t) = x - x^2/2! - \dots$, matching the formal power series formulation $E(\int_0^x dt/E(t)) = e^x$ with $E(0) = 1$.
- `TARGET.md` L3, L12–19 and `PROOF.md` L5–10 match the primary OEIS definitions, revisions, indexing (`n >= 0`, `k >= 0`, `A233335` offset `0`), and conjecture verbatim.
- Well-definedness: for $n \ge 1, k \ge 0$, every RHS term has strictly smaller $(n'+k', n')$ in lexicographic order: $A(n-1, k+1)$ has sum $n+k$ and $n-1 < n$; $A(n-1, j)$ has sum $\le n+k-1$; $A(k-j, 0)$ has sum $k-j \le k = (n+k)-n \le n+k-1$. Thus $A(n, k)$ is uniquely defined from $A(0, k) = 1$.

## 3. Line-by-Line Mathematical Audit (`PROOF.md`)

1. **Row EGF and transport PDE (§1, L14–29):**
   - $H_n(y) = \sum_{k \ge 0} A(n, k) y^k/k!$ ($H_0(y) = e^y$), $G(x, y) = \sum_{n \ge 0} H_n(y) x^n/n!$, and $V(y) = 1 + \sum_{m \ge 1} A(m-1, 0) y^m/m! = 1 + \int_0^y G(t, 0)\,dt$ satisfy $V(0) = 1$ and $V'(y) = G(y, 0)$.
   - Dividing the recurrence by $k!$ uses $\frac{1}{k!}\binom{k+1}{j} = \frac{k+1}{j!(k+1-j)!}$. Since $[y^0](V(y)-1) = 0$ and $[y^r](V(y)-1) = A(r-1,0)/r!$ for $r \ge 1$, the Cauchy product coefficient $[y^{k+1}]((V(y)-1)H_{n-1}(y))$ equals $\sum_{j=0}^k \frac{A(n-1, j)}{j!}\frac{A(k-j, 0)}{(k+1-j)!}$ (the $j=k+1$ term vanishes). Multiplying by $y^k$ and summing over $k \ge 0$ gives $H_n(y) = \partial_y(V(y) H_{n-1}(y))$ for $n \ge 1$.
   - Setting $W(x, y) = V(y) G(x, y)$ gives $\partial_x G = \partial_y W$, hence $\partial_x W = V(y)\partial_y W$ with $W(0, y) = V(y) e^y$. For this fixed $V(y) \in \mathbb{Q}[[y]]$, comparing $[x^n/n!]$ gives $W_{n+1}(y) = V(y)\partial_y W_n(y)$, proving uniqueness in $\mathbb{Q}[[x, y]]$ with zero circularity.
2. **Method of characteristics in $\mathbb{Q}[[x, y]]$ (§2, L33–44):**
   - Since $V(0) = 1$, $1/V(t) \in \mathbb{Q}[[t]]$ has constant term $1$, so $\Phi(u) = \int_0^u dt/V(t) \in u\mathbb{Q}[[u]]$ has $\Phi(0) = 0, \Phi'(0) = 1$.
   - Hence $\Phi$ is compositionally invertible and $\eta(x, y) = \Phi^{-1}(\Phi(y) + x) \in \mathbb{Q}[[x, y]]$ is the unique formal series with $\eta(0,0) = 0$ satisfying $\Phi(\eta(x, y)) = \Phi(y) + x$ (and $\eta(0, y) = y$).
   - Formal chain-rule differentiation gives $\partial_x\eta/V(\eta) = 1$ and $\partial_y\eta/V(\eta) = 1/V(y)$, hence $\partial_x\eta = V(y)\partial_y\eta$.
   - $U(x, y) := V(\eta)e^\eta \in \mathbb{Q}[[x, y]]$ satisfies $\partial_x U = V(y)\partial_y U$ and $U(0, y) = V(y)e^y = W(0, y)$; by uniqueness, $W(x, y) = V(\eta(x, y)) e^{\eta(x, y)}$.
3. **Specialization and uniqueness identification with $E(x)$ (§3, L48–60):**
   - At $y = 0$, $u(x) := \eta(x, 0) = \Phi^{-1}(x)$ and $V(0) = 1$ give $V'(x) = G(x, 0) = W(x, 0) = V(u(x)) e^{u(x)}$.
   - Substituting $x = \Phi(u)$ (valid since $\Phi(0) = 0$) and applying the chain rule gives $\frac{d}{du}(V(\Phi(u))) = V'(\Phi(u))\Phi'(u) = (V(u)e^u)(1/V(u)) = e^u$. Since $V(\Phi(0)) = V(0) = 1 = e^0$, $V(\Phi(u)) = e^u$.
   - Uniqueness check (L57): differentiating $A(\Phi_A(u)) = e^u$ ($A(0) = 1$) gives $A'(\Phi_A(u)) = A(u)e^u$. At $m = 0$, $a_1 = 1$. For $m \ge 1$, expanding $A'(\Phi_A(u)) = \sum_{r \ge 0} \frac{a_{r+1}}{r!} \Phi_A(u)^r$ with $\Phi_A(u) = u + O(u^2)$: the $r=m$ term contributes $a_{m+1}/m!$ to $[u^m]$, $r=0$ contributes $0$, and each $1 \le r \le m-1$ uses $a_{r+1}$ ($r+1 \le m$) together with $[u^k]\Phi_A(u) = \frac{1}{k}[t^{k-1}](1/A(t))$ for $k \le m-r+1 \le m$, which depends only on $a_1, \dots, a_{m-1}$ (with $a_0 = 1$ fixed). The RHS $[u^m](A(u)e^u)$ depends only on $a_0, \dots, a_m$. Hence $a_{m+1}$ is uniquely determined by induction, so $V(x) = E(x)$.
   - Comparing $[x^n/n!]$ in $V'(x) = E'(x)$ yields $A(n, 0) = \mathrm{A233335}(n + 1)$ for all $n \ge 0$.

## 4. Independent Mechanical & Exactness Check

- Audited `targets/oeis-A392058/notes/check-check-1.py` (AST check: `floats: []`; divisions on L58 and L145 are `sp.Rational / int`) and executed `.venv/bin/python -u targets/oeis-A392058/notes/check-check-1.py`: exited `0` (`PASS`), confirming all `45` live OEIS `A392058` `%S` antidiagonal terms, all `22` live OEIS `A233335` `%S` terms via exact term-by-term inversion of $E(\int_0^x dt/E(t)) = e^x$, $A(n,0) = \mathrm{A233335}(n+1)$ for $0 \le n \le 21$, $H_n(y) = \partial_y(V(y)H_{n-1}(y))$ ($1 \le n \le 9$), the transport PDE up to total degree $9$, and $V(\Phi(u)) = e^u \bmod u^{22}$.
- Local snapshot check (`grep -rn "A392058" watch/snapshots/`): `0` hits across all snapshot files.
