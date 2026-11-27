# Proof of Kotesovec's Conjecture $\mathrm{A361430}(n) = |\mathrm{A298826}(n)|$ and Schulte's Formula

## 1. Statement

Let $a(n) = \mathrm{A361430}(n)$ be the multiplicative arithmetic function defined on prime powers $p^e$ ($e \ge 1$) by $a(p^e) = e - 1$, with $a(1) = 1$. Let $c(n) = \mathrm{A298826}(n) = \mathrm{A298825}(n)/n$, defined from the primary matrix construction of `A298674` / `A298825` / `A298826`:
- $A(u, d) = \mathbf{1}_{d \mid u}$ and $B(d, v) = \mathbf{1}_{d \mid v}\,\mu(d)\,d$ for $u, d, v \ge 1$, where $\mu$ is the Möbius function;
- $T(u, v) = (AB)(u, v) = \sum_{d \mid \gcd(u, v)} \mu(d)\,d$;
- $c(n) = \frac{1}{n} \sum_{m=1}^{n} (T(\cdot, m) * T(\cdot, m + 2))(n) = \frac{1}{n} \sum_{m=1}^{n} \sum_{k \mid n} T(n/k, m)\,T(k, m+2)$.

We prove for all integers $n \ge 1$:
1. **(Werner Schulte's conjecture on `A298826`):** $c(n)$ is multiplicative with $c(p^e) = (-1)^p (e - 1)$ for all primes $p$ and exponents $e \ge 1$.
2. **(Vaclav Kotesovec's conjecture on `A361430` & `A298826`):** $\mathrm{A361430}(n) = |c(n)|$.
3. **(Ridouane Oudra's divisor conjecture on `A298826` & `A361430`):** $c(n) = (-1)^{n+1} \sum_{d \mid n} \mu(d)\,\tau(d)\,\tau(n/d)$, where $\tau(m) = \sum_{d \mid m} 1$ is the divisor-count function, and $|c(n)| = \left|\sum_{d \mid n} \mu(d)\,\tau(d)\,\tau(n/d)\right|$.

---

## 2. Proof via Chinese Remainder Reduction

Fix $n \ge 1$. Substituting $T(u, v) = \sum_{d \mid \gcd(u, v)} \mu(d)\,d$ into the defining formula for $c(n)$ gives
$$c(n) = \frac{1}{n} \sum_{k \mid n} \sum_{d_1 \mid (n/k)} \sum_{d_2 \mid k} \mu(d_1)\,d_1\,\mu(d_2)\,d_2 \sum_{\substack{1 \le m \le n \\ d_1 \mid m \\ d_2 \mid (m+2)}} 1.$$

For each pair $(d_1, d_2)$ in the sum, we have $d_1 \mid (n/k)$ and $d_2 \mid k$, so $d_1 d_2 \mid n$. In particular,
$$L := \mathrm{lcm}(d_1, d_2) = \frac{d_1 d_2}{\gcd(d_1, d_2)} \;\Big|\; n.$$
Consider the congruence system on $m$:
$$m \equiv 0 \pmod{d_1}, \qquad m \equiv -2 \pmod{d_2}.$$
By the Chinese Remainder Theorem, this system has a solution modulo $L$ if and only if $\gcd(d_1, d_2) \mid (0 - (-2)) = 2$, and when $\gcd(d_1, d_2) \mid 2$, there is a unique residue class modulo $L$. Since $L \mid n$, every residue class modulo $L$ occurs exactly $n / L$ times among $m \in \{1, \dots, n\}$. Hence
$$\sum_{\substack{1 \le m \le n \\ d_1 \mid m \\ d_2 \mid (m+2)}} 1 = \begin{cases} \dfrac{n\,\gcd(d_1, d_2)}{d_1 d_2}, & \text{if } \gcd(d_1, d_2) \mid 2, \\[8pt] 0, & \text{otherwise.} \end{cases}$$

Substituting this back and cancelling $n$ and $d_1 d_2$ yields
$$c(n) = \sum_{k \mid n} \sum_{\substack{d_1 \mid (n/k),\, d_2 \mid k \\ \gcd(d_1, d_2) \mid 2}} \mu(d_1)\,\mu(d_2)\,\gcd(d_1, d_2).$$

Now group by the product $j = d_1 d_2$. Given any pair $(d_1, d_2)$ with $d_1 d_2 = j \mid n$, the pairs $(k, n/k)$ satisfying $d_2 \mid k$ and $d_1 \mid (n/k)$ correspond bijectively via $k = d_2 r$ to divisors $r \mid (n / j)$, of which there are $\tau(n / j)$. Defining
$$b(j) := \sum_{\substack{d_1 d_2 = j \\ \gcd(d_1, d_2) \mid 2}} \mu(d_1)\,\mu(d_2)\,\gcd(d_1, d_2),$$
we obtain the exact Dirichlet convolution identity
$$c(n) = \sum_{j \mid n} \tau(n / j)\, b(j) = (\tau * b)(n) \qquad (\forall n \ge 1).$$

---

## 3. Multiplicativity and Prime-Power Evaluation

**Lemma.** *$b(j)$ is a multiplicative function of $j \ge 1$.*

*Proof.* Clearly $b(1) = 1$. Suppose $\gcd(u, v) = 1$ with $u, v \ge 1$. Every factorization $j = uv = d_1 d_2$ splits uniquely as $d_1 = d_1' d_1''$ and $d_2 = d_2' d_2''$ with $d_1' d_2' = u$ and $d_1'' d_2'' = v$, where $\gcd(d_1', d_1'') = \gcd(d_2', d_2'') = 1$ and $\gcd(d_1', d_2'') = \gcd(d_1'', d_2') = 1$. Thus $\mu(d_1)\mu(d_2) = \mu(d_1')\mu(d_2')\,\mu(d_1'')\mu(d_2'')$ and
$$\gcd(d_1, d_2) = \gcd(d_1', d_2')\,\gcd(d_1'', d_2'').$$
Because $2$ is prime, the divisibility condition $\gcd(d_1', d_2')\,\gcd(d_1'', d_2'') \mid 2$ on the coprime factors $g' = \gcd(d_1', d_2') \mid u$ and $g'' = \gcd(d_1'', d_2'') \mid v$ is equivalent to $g' \mid 2$ and $g'' \mid 2$. Hence the sum over $d_1 d_2 = uv$ factors into $b(u)\,b(v)$. $\square$

Since $\tau$ and $b$ are both multiplicative, their Dirichlet convolution $c = \tau * b$ is **multiplicative**. We evaluate $b(p^e)$ and $c(p^e)$ for every prime $p$ and $e \ge 1$:

- **Case 1: $p$ is an odd prime.**
  - For $e = 1$: the pairs $(d_1, d_2)$ with $d_1 d_2 = p$ are $(1, p)$ and $(p, 1)$, both with $\gcd(d_1, d_2) = 1 \mid 2$, so $b(p) = \mu(1)\mu(p)\cdot 1 + \mu(p)\mu(1)\cdot 1 = -2$.
  - For $e = 2$: among $(1, p^2), (p, p), (p^2, 1)$, we have $\mu(p^2) = 0$ while $\gcd(p, p) = p \nmid 2$, so $b(p^2) = 0$.
  - For $e \ge 3$: every pair $d_1 d_2 = p^e$ has $p^2 \mid d_1$ or $p^2 \mid d_2$, so $\mu(d_1)\mu(d_2) = 0$ and $b(p^e) = 0$.
  Therefore, for all $e \ge 1$,
  $$c(p^e) = \tau(p^e)\,b(1) + \tau(p^{e-1})\,b(p) = (e + 1)\cdot 1 + e\cdot (-2) = -(e - 1) = (-1)^p (e - 1).$$

- **Case 2: $p = 2$.**
  - For $e = 1$: $(1, 2)$ and $(2, 1)$ give $b(2) = -1 - 1 = -2$.
  - For $e = 2$: $(1, 4)$ and $(4, 1)$ have $\mu(4) = 0$, while $(d_1, d_2) = (2, 2)$ satisfies $\gcd(2, 2) = 2 \mid 2$ and contributes $\mu(2)\mu(2)\cdot 2 = +2$, so $b(4) = 2$.
  - For $e \ge 3$: every pair $d_1 d_2 = 2^e$ has $4 \mid d_1$ or $4 \mid d_2$, so $b(2^e) = 0$.
  Therefore:
  - for $e = 1$: $c(2) = \tau(2)\,b(1) + \tau(1)\,b(2) = 2\cdot 1 + 1\cdot (-2) = 0 = (-1)^2 (1 - 1)$;
  - for $e \ge 2$:
    $$c(2^e) = \tau(2^e)\,b(1) + \tau(2^{e-1})\,b(2) + \tau(2^{e-2})\,b(4) = (e+1)\cdot 1 + e\cdot(-2) + (e-1)\cdot 2 = e - 1 = (-1)^2(e - 1).$$

This proves Werner Schulte's conjecture: $c(n) = \mathrm{A298826}(n)$ is multiplicative with $c(p^e) = (-1)^p (e - 1)$ for all primes $p$ and $e \ge 1$.

---

## 4. Consequences for $\mathrm{A361430}(n)$ and Oudra's Formula

1. **Proof of $\mathrm{A361430}(n) = |\mathrm{A298826}(n)|$:**
   Since $c$ is multiplicative and $\mathrm{A361430}$ is defined to be multiplicative with $\mathrm{A361430}(p^e) = e - 1$, comparing prime-power values gives for every $n = \prod_{i} p_i^{e_i} \ge 1$:
   $$|c(n)| = \prod_{i} |c(p_i^{e_i})| = \prod_{i} \bigl|(-1)^{p_i}(e_i - 1)\bigr| = \prod_{i} (e_i - 1) = \mathrm{A361430}(n).$$

2. **Proof of Oudra's formula:**
   Let $g(n) := \sum_{d \mid n} \mu(d)\,\tau(d)\,\tau(n/d)$, which is multiplicative as a Dirichlet convolution of $\mu \cdot \tau$ and $\tau$. On any prime power $p^e$ ($e \ge 1$),
   $$g(p^e) = \mu(1)\tau(1)\tau(p^e) + \mu(p)\tau(p)\tau(p^{e-1}) = (e + 1) - 2e = -(e - 1).$$
   Meanwhile $(-1)^{n+1}$ is not multiplicative, **except** note that on $n = 2^a m$ ($m$ odd, $a \ge 0$):
   - If $n$ is not powerful (some prime $p$ divides $n$ with $v_p(n) = 1$), then $c(p) = g(p) = 0$ and multiplicativity gives $c(n) = 0 = (-1)^{n+1} g(n)$.
   - Whenever $n$ is powerful (every prime $p \mid n$ has $e_p = v_p(n) \ge 2$), comparing the sign factors gives:
     - $g(n) = \prod_{p \mid n} (-(e_p - 1)) = (-1)^{\omega(n)} \prod_{p \mid n} (e_p - 1)$, where $\omega(n)$ is the number of distinct prime factors of $n$;
     - $c(n) = \prod_{p \mid n} (-1)^p (e_p - 1) = (-1)^{\omega_{\text{odd}}(n)} \prod_{p \mid n} (e_p - 1)$, where $\omega_{\text{odd}}(n)$ is the number of distinct **odd** prime factors of $n$.
     Now if $n$ is **odd**, $\omega(n) = \omega_{\text{odd}}(n)$ and $(-1)^{n+1} = 1$, so $(-1)^{n+1} g(n) = c(n)$. If $n$ is **even** ($2 \mid n$), then $\omega(n) = \omega_{\text{odd}}(n) + 1$ and $(-1)^{n+1} = -1$, so $(-1)^{n+1} g(n) = -(-1)^{\omega_{\text{odd}}(n)+1} \prod (e_p - 1) = c(n)$. Thus $c(n) = (-1)^{n+1} \sum_{d \mid n} \mu(d)\tau(d)\tau(n/d)$ holds identically for all $n \ge 1$! $\blacksquare$
