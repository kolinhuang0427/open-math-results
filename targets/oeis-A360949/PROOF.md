# Proof of OEIS A360949 (Paul D. Hanna Mod-4 Thue–Morse Conjecture)

## Theorem
Let $A(x) = \sum_{n \ge 0} a(n) x^n$ be the unique formal power series satisfying
$$1 = \sum_{n=0}^{\infty} \left(-\frac{x}{2}\right)^n \bigl(A(x)^n + (-1)^n\bigr)^n.$$
Let $(t_n)_{n \ge 0}$ be the Thue–Morse sequence (`A010060`: $t_0 = 0$, $t_{2n} = t_n$, $t_{2n+1} = 1 - t_n$), and let $\mathrm{A161674} = \{m \ge 0 : t_m + t_{m+2} = 1\}$ (indexed as $\mathrm{A161674}(k)$ for $k \ge 1$). Then:
1. $a(0) = 1$ and $a(n) \in 2\mathbb{Z}$ for all $n \ge 1$.
2. For every $n \ge 1$,
   $$a(n) \equiv \begin{cases} 2 \pmod 4 & \text{if } n = 2m + 1 \text{ with } t_m + t_{m+2} = 1 \text{ (i.e., } n = 2\,\mathrm{A161674}(k) + 1\text{)}, \\ 0 \pmod 4 & \text{otherwise.} \end{cases}$$

---

## Proof

### Step 1: Existence, Uniqueness, and Integrality of $B(x) = \frac{A(x) - 1}{2}$
Extracting the $n = 0$ term ($= 1$) and the $[x^1]$ coefficient ($-\frac{1}{2}(a(0) - 1) = 0$) gives $a(0) = 1$, and the functional equation becomes
$$0 = \sum_{n=1}^{\infty} \left(-\frac{x}{2}\right)^n \bigl(A(x)^n + (-1)^n\bigr)^n.$$
Write $A(x) = 1 + 2 B(x)$ where $B(x) = \sum_{k \ge 1} b_k x^k \in x \mathbb{Q}[[x]]$. For each $n \ge 1$:
- When $n = 1$:
  $$\left(-\frac{x}{2}\right)^1 (A(x) - 1) = -x B(x).$$
- When $n = 2m$ ($m \ge 1$):
  $$\frac{A(x)^{2m} + 1}{2} = \frac{(1 + 2 B(x))^{2m} + 1}{2} = 1 + \sum_{r=1}^{2m} \binom{2m}{r} 2^{r-1} B(x)^r =: P_{2m}(B(x)) \in \mathbb{Z}[B(x)],$$
  so the $n = 2m$ term equals $x^{2m} P_{2m}(B(x))^{2m}$.
- When $n = 2m + 1$ ($m \ge 1$):
  $$\frac{A(x)^{2m+1} - 1}{2} = \frac{(1 + 2 B(x))^{2m+1} - 1}{2} = \sum_{r=1}^{2m+1} \binom{2m+1}{r} 2^{r-1} B(x)^r =: Q_{2m+1}(B(x)) \in \mathbb{Z}[B(x)],$$
  so the $n = 2m + 1$ term equals $-x^{2m+1} Q_{2m+1}(B(x))^{2m+1}$.

Equating the coefficient of $x^{k+1}$ ($k \ge 1$) to $0$:
- The $n = 1$ term contributes $-b_k$.
- Every $n \ge 2$ term has prefactor $x^n$ multiplying a polynomial in $B(x) \in x\mathbb{Q}[[x]]$, so its $[x^{k+1}]$ coefficient is a polynomial with integer coefficients in $b_1, \dots, b_{k+1-n}$ (where $k + 1 - n \le k - 1$).

By strong induction on $k \ge 1$, $b_k \in \mathbb{Z}$ is uniquely determined for every $k \ge 1$. Hence $B(x) \in x \mathbb{Z}[[x]]$, $a(k) = 2 b_k \in 2\mathbb{Z}$, and for every $k \ge 1$:
$$a(k) \equiv 2 \pmod 4 \iff b_k \equiv 1 \pmod 2.$$

### Step 2: Reduction of $B(x)$ Modulo $2$
Reduce the functional equation for $B(x) \in x\mathbb{Z}[[x]]$ modulo $2$ in $\mathbb{F}_2[[x]]$:
- For every $m \ge 1$, in $P_{2m}(B(x)) = 1 + 2m B(x) + \sum_{r=2}^{2m} \binom{2m}{r} 2^{r-1} B(x)^r$, every term with $r \ge 1$ has an even coefficient, so $P_{2m}(B(x)) \equiv 1 \pmod 2$ and $x^{2m} P_{2m}(B(x))^{2m} \equiv x^{2m} \pmod 2$.
- For every $m \ge 1$, in $Q_{2m+1}(B(x)) = (2m+1)B(x) + \sum_{r=2}^{2m+1} \binom{2m+1}{r} 2^{r-1} B(x)^r$, every term with $r \ge 2$ has an even coefficient, so $Q_{2m+1}(B(x)) \equiv B(x) \pmod 2$ and $-x^{2m+1} Q_{2m+1}(B(x))^{2m+1} \equiv x^{2m+1} B(x)^{2m+1} \pmod 2$.
- For $n = 1$, $-x B(x) \equiv x^1 B(x)^1 \pmod 2$ also matches $x^{2m+1} B(x)^{2m+1}$ at $m = 0$.

Summing over all $n \ge 1$ in $\mathbb{F}_2[[x]]$ (noting $1 + x^2 B(x)^2$ is a unit in $\mathbb{F}_2[[x]]$ since $B(0) = 0$) gives
$$0 = \sum_{m=1}^{\infty} x^{2m} + \sum_{m=0}^{\infty} x^{2m+1} B(x)^{2m+1} = \frac{x^2}{1 + x^2} + \frac{x B(x)}{1 + x^2 B(x)^2} \qquad \text{in } \mathbb{F}_2[[x]].$$
Clearing denominators and dividing by $x$:
$$x(1 + x^2 B(x)^2) + (1 + x^2) B(x) = 0 \implies (1 + x^2) B(x) = x + x^3 B(x)^2 \qquad \text{in } \mathbb{F}_2[[x]].$$

Split $B(x) \bmod 2 = B_0(x^2) + x B_1(x^2)$ into even and odd powers of $x$. Because $B(x)^2 = B_0(x^4) + x^2 B_1(x^4)$ contains only even powers of $x$, the right-hand side $x + x^3 B(x)^2$ contains only odd powers of $x$.
- Equating even parts in $\mathbb{F}_2[[x]]$ yields $(1 + x^2) B_0(x^2) = 0$, hence $B_0(x^2) = 0$. Thus $b_{2k} \equiv 0 \pmod 2$, i.e., $a(2k) \equiv 0 \pmod 4$, for all $k \ge 1$.
- Equating odd parts, setting $y := x^2$ and $C(y) := B_1(y) \in \mathbb{F}_2[[y]]$, and dividing by $x$ yields
  $$(1 + y) C(y) = 1 + y^2 C(y)^2 \implies y^2 C(y)^2 + (1 + y) C(y) + 1 = 0 \qquad \text{in } \mathbb{F}_2[[y]].$$
Notice that this equation uniquely determines $C(y) \in \mathbb{F}_2[[y]]$, since $C(y) = \frac{1 + y^2 C(y)^2}{1 + y}$ expresses $[y^m] C(y)$ recursively in terms of $[y^j] C(y)$ with $j < m$.

### Step 3: Identification with Thue–Morse (`A161674`)
Let $T(y) = \sum_{m \ge 0} t_m y^m \in \mathbb{F}_2[[y]]$ be the Thue–Morse generating function modulo $2$. From $t_0 = 0$, $t_{2m} = t_m$, and $t_{2m+1} \equiv 1 + t_m \pmod 2$, and the Frobenius identity $T(y^2) = T(y)^2$ in $\mathbb{F}_2[[y]]$:
$$T(y) = T(y^2) + y \left(\frac{1}{1 + y^2} + T(y^2)\right) = (1 + y) T(y)^2 + \frac{y}{(1 + y)^2}.$$
Multiplying by $(1 + y)^2 = 1 + y^2$ gives
$$(1 + y)^3 T(y)^2 + (1 + y)^2 T(y) + y = 0 \qquad \text{in } \mathbb{F}_2[[y]].$$

Now consider the indicator series of $\{m \ge 0 : t_m + t_{m+2} = 1\} = \mathrm{A161674}$:
$$\widetilde{C}(y) := \sum_{m=0}^{\infty} (t_m + t_{m+2}) y^m \in \mathbb{F}_2[[y]].$$
Since $t_0 = 0$ and $t_1 = 1$, we have $\sum_{m \ge 0} t_{m+2} y^m = \frac{T(y) - y}{y^2} = \frac{T(y) + y}{y^2}$ in $\mathbb{F}_2[[y]]$, so
$$\widetilde{C}(y) = T(y) + \frac{T(y) + y}{y^2} = \frac{(1 + y)^2 T(y) + y}{y^2},$$
i.e., $(1 + y)^2 T(y) = y + y^2 \widetilde{C}(y)$, and squaring gives $(1 + y)^4 T(y)^2 = y^2 + y^4 \widetilde{C}(y)^2$.
Multiplying $(1 + y)^3 T(y)^2 + (1 + y)^2 T(y) + y = 0$ by $(1 + y)$ and substituting these expressions:
$$0 = (1 + y)^4 T(y)^2 + (1 + y)^3 T(y) + y(1 + y) = (y^2 + y^4 \widetilde{C}(y)^2) + (1 + y)(y + y^2 \widetilde{C}(y)) + y(1 + y) = y^4 \widetilde{C}(y)^2 + y^2(1 + y)\widetilde{C}(y) + y^2.$$
Dividing by $y^2$ gives
$$y^2 \widetilde{C}(y)^2 + (1 + y) \widetilde{C}(y) + 1 = 0 \qquad \text{in } \mathbb{F}_2[[y]].$$

By uniqueness of the solution in $\mathbb{F}_2[[y]]$, $C(y) = \widetilde{C}(y)$, meaning $b_{2m+1} \equiv t_m + t_{m+2} \pmod 2$ for all $m \ge 0$. Hence $a(2m+1) = 2 b_{2m+1} \equiv 2 \pmod 4$ if and only if $t_m + t_{m+2} = 1$ (i.e., $m \in \mathrm{A161674}$), and $a(n) \equiv 0 \pmod 4$ for all other $n \ge 1$. $\square$
