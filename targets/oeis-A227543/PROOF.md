# Proof of Mikhail Kurkov's Continued-Fraction Triangle Conjecture (OEIS A227543)

## 1. Theorem Statement

Let $R$ be any commutative ring with $1$ (in particular, the universal polynomial ring $R = \mathbb{Z}[f_0, f_1, f_2, \dots]$ or the row-polynomial ring $\mathbb{Z}[q]$ via $f_m \mapsto q^m$), and let $(f(m))_{m \ge 0}$ be any sequence in $R$.

Define the formal Stieltjes continued fraction $B(x) = B_0(x) = \sum_{n \ge 0} b(n) x^n \in 1 + x R[[x]]$ via the unique family of formal power series $(B_m(x))_{m \ge 0}$ in $1 + x R[[x]]$ satisfying
$$B_m(x) = \frac{1}{1 - f(m)\, x \, B_{m+1}(x)} \qquad \forall m \ge 0$$
(equivalently, the finite truncation $B_0^{(N)}(x)$ obtained by setting $B_{N+1}^{(N)}(x) = 1$ stabilizes modulo $x^{N+2}$ because each step shifts $x$-adic valuation by $1$).

Define the array $(P(n, k))_{n, k \ge 0}$ in $R$ by
$$P(n, 0) = 1 \quad (n \ge 0), \qquad P(n, k) = 0 \quad (k > n),$$
$$P(n, k) = P(n-1, k) + f(n-k) P(n, k-1) \qquad (0 < k \le n).$$
Then for **every** $n \ge 0$:
$$b(n) = P(n, n).$$
In particular, specializing $R = \mathbb{Z}[q]$ and $f(m) = q^m$ gives $A(x, q) = B_0(x)$ satisfying $A(x, q) = 1 + x A(qx, q) A(x, q)$ and $[x^n] A(x, q) = P(n, n)$ for all $n \ge 0$.

---

## 2. Proof

**Step 1 (Well-definedness of $B_m(x)$ in $R[[x]]$).**
Define the $N$-th finite continued-fraction approximant recursively backward from $B_{N+1}^{(N)}(x) := 1$ by
$$B_m^{(N)}(x) := \frac{1}{1 - f(m)\, x \, B_{m+1}^{(N)}(x)} = \sum_{j \ge 0} \bigl(f(m) x B_{m+1}^{(N)}(x)\bigr)^j \in 1 + x R[[x]] \qquad (0 \le m \le N).$$
Note every $1 - f(m) x B_{m+1}^{(N)}(x)$ has constant term $1$, so it is an exact unit in $R[[x]]$. By finite induction downward from $m = N+1$ to $m = 0$, if $B_{m+1}^{(N+1)}(x) \equiv B_{m+1}^{(N)}(x) \pmod{x^{r}}$, then $f(m) x B_{m+1}^{(N+1)}(x) \equiv f(m) x B_{m+1}^{(N)}(x) \pmod{x^{r+1}}$, hence $B_m^{(N+1)}(x) \equiv B_m^{(N)}(x) \pmod{x^{r+1}}$. Starting from $B_{N+1}^{(N+1)}(x) \equiv 1 = B_{N+1}^{(N)}(x) \pmod{x}$, induction gives
$$B_m^{(N+1)}(x) \equiv B_m^{(N)}(x) \pmod{x^{N - m + 2}} \qquad (0 \le m \le N + 1).$$
Thus $B_m(x) := \lim_{N \to \infty} B_m^{(N)}(x)$ exists $x$-adically in $1 + x R[[x]]$ for every $m \ge 0$, agrees with $B_m^{(N)}(x)$ through degree $N - m + 1$, and satisfies the exact formal identity in $R[[x]]$:
$$B_m(x) = \frac{1}{1 - f(m)\, x \, B_{m+1}(x)} \iff B_m(x) - 1 = f(m)\, x \, B_m(x)\, B_{m+1}(x) \qquad \forall m \ge 0.$$

**Step 2 (Product generating functions along diagonals $d = n - k$).**
For each $d \ge -1$, define $\widetilde{R}_d(x) \in 1 + x R[[x]]$ by the empty product $\widetilde{R}_{-1}(x) := 1$ and
$$\widetilde{R}_d(x) := \prod_{j=0}^{d} B_j(x) \qquad (d \ge 0).$$
For every $d \ge 0$, multiplying the relation $B_d(x) - 1 = f(d) x B_d(x) B_{d+1}(x)$ by $\widetilde{R}_{d-1}(x) = \prod_{j=0}^{d-1} B_j(x)$ immediately yields the exact identity in $R[[x]]$:
$$\widetilde{R}_d(x) - \widetilde{R}_{d-1}(x) = f(d)\, x \, \widetilde{R}_{d+1}(x) \qquad \forall d \ge 0.$$

**Step 3 (Coefficient extraction and identification with $P(n, k)$).**
Write $\widetilde{Q}(d, k) := [x^k] \widetilde{R}_d(x) \in R$ for $d \ge -1$ and $k \ge 0$. Since $\widetilde{R}_{-1}(x) = 1$ and every $\widetilde{R}_d(x)$ has constant term $1$:
- $\widetilde{Q}(d, 0) = 1$ for all $d \ge -1$;
- $\widetilde{Q}(-1, k) = 0$ for all $k \ge 1$;
- Extracting $[x^k]$ ($k \ge 1$) from $\widetilde{R}_d(x) - \widetilde{R}_{d-1}(x) = f(d)\, x \, \widetilde{R}_{d+1}(x)$ gives
  $$\widetilde{Q}(d, k) = \widetilde{Q}(d - 1, k) + f(d)\, \widetilde{Q}(d + 1, k - 1) \qquad (d \ge 0,\ k \ge 1).$$

Now define $\widetilde{P}(n, k)$ for all $n, k \ge 0$ by
$$\widetilde{P}(n, k) := \begin{cases} \widetilde{Q}(n - k, k) & \text{if } 0 \le k \le n, \\ 0 & \text{if } k > n. \end{cases}$$
Let us check Kurkov's boundary conditions and recurrence on $\widetilde{P}(n, k)$:
1. For $n \ge 0$: $\widetilde{P}(n, 0) = \widetilde{Q}(n, 0) = 1$.
2. For $k > n$: $\widetilde{P}(n, k) = 0$ by definition.
3. For $0 < k \le n$, set $d = n - k \ge 0$. Notice that:
   - if $k < n$ ($d \ge 1$), then $\widetilde{P}(n-1, k) = \widetilde{Q}((n-1)-k, k) = \widetilde{Q}(d-1, k)$;
   - if $k = n$ ($d = 0$), then $\widetilde{P}(n-1, n) = 0 = \widetilde{Q}(-1, k) = \widetilde{Q}(d-1, k)$ (since $k \ge 1$);
   - moreover, $(n - k) \ge 0 \implies k - 1 \le n$, and $n - (k - 1) = d + 1 \ge 1$, so $\widetilde{P}(n, k - 1) = \widetilde{Q}(d + 1, k - 1)$.
   Therefore, for **every** $0 < k \le n$:
   $$\widetilde{P}(n, k) = \widetilde{Q}(d, k) = \widetilde{Q}(d - 1, k) + f(d)\, \widetilde{Q}(d + 1, k - 1) = \widetilde{P}(n - 1, k) + f(n - k)\, \widetilde{P}(n, k - 1).$$

Since $(P(n, k))_{n, k \ge 0}$ and $(\widetilde{P}(n, k))_{n, k \ge 0}$ satisfy the exact same boundary values ($k = 0$ and $k > n$) and the same recurrence advancing $k$ (and $n$ at fixed $k$), unique induction on $k \ge 0$ and, for each fixed $k$, on $n \ge k$ proves
$$P(n, k) = \widetilde{P}(n, k) \qquad \forall n, k \ge 0.$$

Setting $k = n$ ($d = 0$) gives
$$P(n, n) = \widetilde{P}(n, n) = \widetilde{Q}(0, n) = [x^n] \widetilde{R}_0(x) = [x^n] B_0(x) = b(n) \qquad \forall n \ge 0.$$

**Step 4 (Specialization to OEIS A227543).**
When $R = \mathbb{Z}[q]$ and $f(m) = q^m$ ($m \ge 0$), uniqueness of the $x$-adic fixed point $A(x, q) \in 1 + x \mathbb{Z}[q][[x]]$ of
$$A(x, q) = 1 + x A(q x, q) A(x, q) \iff A(x, q) = \frac{1}{1 - x A(q x, q)}$$
implies by induction on $m \ge 0$ (and $x$-adic uniqueness) that $B_m(x) = A(q^m x, q)$, since $A(q^m x, q) = \frac{1}{1 - q^m x A(q^{m+1} x, q)}$ satisfies the exact defining continued-fraction recurrence of $B_m(x)$. Hence $[x^n] A(x, q) = b(n) = P(n, n)$ for all $n \ge 0$. $\blacksquare$
