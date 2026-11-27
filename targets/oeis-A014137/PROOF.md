# Proof of OEIS A014137 Continued Fraction Conjecture

We prove Sergei N. Gladkovskii's May 14, 2013 continued fraction conjecture on [OEIS A014137](https://oeis.org/A014137) (rev. 180), both in $\mathbb{Q}[[x]]$ ($x$-adically) and analytically on $\{x \in \mathbb{C} : |x| < 1/4\}$.

## 1. The Shifted Catalan Generating Functions $Q(k)$

Let $C_n := \frac{1}{n+1}\binom{2n}{n}$ ($n \ge 0$) be the Catalan numbers (OEIS A000108), with ordinary generating function $C(x) := \sum_{n=0}^{\infty} C_n x^n = \frac{1 - \sqrt{1 - 4x}}{2x}$. Then $a(n) = \sum_{j=0}^{n} C_j$ has ordinary generating function
$$A(x) = \sum_{n=0}^{\infty} a(n) x^n = \frac{C(x)}{1 - x}.$$

For every integer $k \ge 0$, define the normalized even-shifted Catalan generating function
$$Q(k) := \sum_{n=0}^{\infty} \frac{C_{n+2k}}{C_{2k}} x^n = \frac{1}{C_{2k} x^{2k}} \left(C(x) - \sum_{m=0}^{2k-1} C_m x^m\right) \in \mathbb{Q}[[x]].$$
Note that $Q(0) = C(x)$, so $A(x) = \frac{Q(0)}{1 - x}$, and $Q(k) = 1 + O(x)$ is a unit in $\mathbb{Q}[[x]]$ for every $k \ge 0$.

**Lemma 1 (Two-step Catalan ratios).** *For every integer $k \ge 0$,*
$$r_1(k) := \frac{C_{2k+1}}{C_{2k}} = \frac{4k + 1}{k + 1}, \qquad r_2(k) := \frac{C_{2k+2}}{C_{2k+1}} = \frac{2(4k + 3)}{2k + 3}.$$

*Proof.* Using the elementary Catalan ratio $\frac{C_{m+1}}{C_m} = \frac{2(2m+1)}{m+2}$:
- At $m = 2k$: $\frac{C_{2k+1}}{C_{2k}} = \frac{2(4k+1)}{2k+2} = \frac{4k+1}{k+1}$.
- At $m = 2k+1$: $\frac{C_{2k+2}}{C_{2k+1}} = \frac{2(4k+3)}{2k+3}$. $\square$

**Lemma 2 (Shift identity for $Q(k)$).** *For every integer $k \ge 0$,*
$$Q(k) = 1 + r_1(k)\, x + r_1(k)\, r_2(k)\, x^2\, Q(k + 1).$$

*Proof.* Separating the $n = 0$ and $n = 1$ terms of $Q(k)$ and reindexing $n = m + 2$ gives
$$Q(k) = 1 + \frac{C_{2k+1}}{C_{2k}} x + \frac{C_{2k+2}}{C_{2k}} x^2 \sum_{m=0}^{\infty} \frac{C_{m+2k+2}}{C_{2k+2}} x^m = 1 + r_1(k)\, x + r_1(k)\, r_2(k)\, x^2\, Q(k + 1). \qquad \square$$

## 2. Proof of the Continued Fraction Recurrence and Convergence

**Theorem.** *For every integer $k \ge 0$, $Q(k)$ satisfies Gladkovskii's continued fraction recurrence*
$$Q(k) = 1 + \cfrac{(4k + 1) x}{k + 1 - \cfrac{2x(k + 1)(4k + 3)}{2x(4k + 3) + \frac{2k + 3}{Q(k + 1)}}}$$
*in $\mathbb{Q}[[x]]$ (with all denominators units in $\mathbb{Q}[[x]]$). Moreover, finite truncations $Q^{(K)}(0)$ converge to $Q(0) = C(x)$ $x$-adically in $\mathbb{Q}[[x]]$ (with error $O(x^{2K+3})$ for any unit seed $1 + O(x)$); and for the standard truncation $q_{K+1}^{(K)} = 1$ (or any uniformly bounded sequence of seeds on compact subsets of $\{x \in \mathbb{C} : |x| < 1/4\}$ avoiding denominator zeros), the standard truncations $Q^{(K)}(0)$ have nonvanishing intermediate denominators $q_{k+1}^{(K)}(x), D_2(x), D_1(x)$ throughout $\{x \in \mathbb{C} : |x| < 1/4\}$ and converge uniformly on compact subsets of $\{x \in \mathbb{C} : |x| < 1/4\}$ to $Q(0) = C(x)$. Hence $\frac{Q(0)}{1-x} = \frac{C(x)}{1-x} = \sum_{n=0}^{\infty} a(n) x^n$.*

*Proof.* Fix $k \ge 0$ and write $q := Q(k+1) = 1 + O(x) \in \mathbb{Q}[[x]]^\times$, $r_1 := r_1(k) = \frac{4k+1}{k+1}$, and $r_2 := r_2(k) = \frac{2(4k+3)}{2k+3}$. Note that $2x(4k+3) = (2k+3) r_2 x$ and $2x(k+1)(4k+3) = (k+1)(2k+3) r_2 x$. Evaluating the continued fraction denominators from bottom to top in $\mathbb{Q}[[x]]$:

1. Inner denominator:
   $$D_2 := 2x(4k + 3) + \frac{2k + 3}{q} = (2k + 3)\left(r_2 x + \frac{1}{q}\right) = (2k + 3)\frac{1 + r_2 x\, q}{q} = (2k + 3) + O(x) \in \mathbb{Q}[[x]]^\times.$$

2. Outer denominator:
   $$D_1 := (k + 1) - \frac{2x(k + 1)(4k + 3)}{D_2} = (k + 1) - \frac{(k + 1)(2k + 3) r_2 x\, q}{(2k + 3)(1 + r_2 x\, q)} = (k + 1)\left(1 - \frac{r_2 x\, q}{1 + r_2 x\, q}\right) = \frac{k + 1}{1 + r_2 x\, q} = (k + 1) + O(x) \in \mathbb{Q}[[x]]^\times.$$

3. Top level:
   $$1 + \frac{(4k + 1)x}{D_1} = 1 + \frac{4k + 1}{k + 1} x\,(1 + r_2 x\, q) = 1 + r_1 x + r_1 r_2 x^2\, Q(k + 1) = Q(k)$$
   by Lemma 2.

For convergence of finite truncations, define the operator $T_k(q) := 1 + \frac{(4k+1)x}{k+1 - \frac{2x(k+1)(4k+3)}{2x(4k+3) + (2k+3)/q}} = 1 + r_1(k) x + \frac{C_{2k+2}}{C_{2k}} x^2 q$. For any two series $q_1, q_2 \in \mathbb{Q}[[x]]^\times$,
$$T_k(q_1) - T_k(q_2) = \frac{C_{2k+2}}{C_{2k}} x^2 (q_1 - q_2).$$
Given any depth $K \ge 0$ and any seed $q_{K+1}^{(K)} = 1 + O(x) \in \mathbb{Q}[[x]]^\times$ (for instance $q_{K+1}^{(K)} = 1$), iterating $T_k$ from $k = K$ down to $k = 0$ produces $Q^{(K)}(0)$ satisfying
$$Q^{(K)}(0) - Q(0) = \left(\prod_{k=0}^{K}\frac{C_{2k+2}}{C_{2k}}\right) x^{2K+2}\bigl(q_{K+1}^{(K)} - Q(K+1)\bigr) = C_{2K+2}\, x^{2K+2}\bigl(q_{K+1}^{(K)} - Q(K+1)\bigr).$$
Because $q_{K+1}^{(K)} - Q(K+1) = O(x)$, we have $Q^{(K)}(0) - Q(0) \in x^{2K+3}\mathbb{Q}[[x]]$, so $Q^{(K)}(0) \to Q(0) = C(x)$ $x$-adically as $K \to \infty$.

For analytic convergence of the standard truncation $q_{K+1}^{(K)} := 1$ on $\{x \in \mathbb{C} : |x| < 1/4\}$:
1. **Nonvanishing of all intermediate denominators:** Inducting downward from $k = K$ to $k = 0$ via $T_k(q) = 1 + r_1(k)x + r_1(k)r_2(k)x^2 q = 1 + \frac{C_{2k+1}}{C_{2k}}x + \frac{C_{2k+2}}{C_{2k}}x^2 q$ shows that $q_k^{(K)}(x) = \sum_{n=0}^{2(K-k+1)} \frac{C_{n+2k}}{C_{2k}} x^n$ and $1 + r_2(k) x\, q_{k+1}^{(K)}(x) = \sum_{n=0}^{2(K-k)+1} \frac{C_{n+2k+1}}{C_{2k+1}} x^n$. Every such normalized Catalan partial sum $S_{m,M}(x) := \sum_{n=0}^M \frac{C_{n+m}}{C_m} x^n$ ($m, M \ge 0$) has coefficients $b_n := \frac{C_{n+m}}{4^n C_m}$ satisfying $1 = b_0 > b_1 > \dots > b_M > 0$ (since $\frac{b_{n+1}}{b_n} = \frac{4(n+m)+2}{4(n+m)+8} < 1$). Writing $w := 4x$ ($|w| < 1$), telescoping $(1 - w) S_{m,M}(x) = 1 - \sum_{n=1}^M (b_{n-1} - b_n) w^n - b_M w^{M+1}$ gives
   $$\left|\sum_{n=1}^M (b_{n-1} - b_n) w^n + b_M w^{M+1}\right| \le \sum_{n=1}^M (b_{n-1} - b_n)|w|^n + b_M |w|^{M+1} < \sum_{n=1}^M (b_{n-1} - b_n) + b_M = b_0 = 1$$
   (strict inequality when $M \ge 1$ since $|w| < 1$ and $b_0 - b_1, b_M > 0$; and trivially $S_{m,0}(x) = 1 \ne 0$ when $M=0$). Hence $S_{m,M}(x) \ne 0$ on $\{|x| < 1/4\}$. In particular, $q_{k+1}^{(K)}(x) \ne 0$ and $1 + r_2(k) x\, q_{k+1}^{(K)}(x) \ne 0$ for all $0 \le k \le K$, so $D_2(x) = (2k+3)\frac{1 + r_2(k)x\,q_{k+1}^{(K)}(x)}{q_{k+1}^{(K)}(x)}$ and $D_1(x) = \frac{k+1}{1 + r_2(k)x\,q_{k+1}^{(K)}(x)}$ are finite and nonzero everywhere on $\{|x| < 1/4\}$.
2. **Uniform convergence on compact disks $|x| \le \rho < 1/4$:** Since $\frac{C_{n+m}}{C_m} = \prod_{i=m}^{n+m-1}\frac{2(2i+1)}{i+2} \le 4^n$ for all $m, n \ge 0$, on $|x| \le \rho < 1/4$ we have $|Q(K+1)(x)| \le \sum_{n=0}^{\infty}(4\rho)^n = \frac{1}{1 - 4\rho}$, and since $q_{K+1}^{(K)}(x) = 1$,
   $$\bigl|Q^{(K)}(0)(x) - Q(0)(x)\bigr| = C_{2K+2} |x|^{2K+2} \bigl|1 - Q(K+1)(x)\bigr| \le \frac{(4\rho)^{2K+2}}{2K + 3}\left(1 + \frac{1}{1 - 4\rho}\right) \xrightarrow[K \to \infty]{} 0$$
   uniformly on $|x| \le \rho$ (the same bound holds for any uniformly bounded family of analytic seeds on $|x| \le \rho$). Dividing by $1 - x$ gives $\frac{Q(0)}{1-x} = \frac{C(x)}{1-x} = \sum_{n=0}^{\infty} a(n)x^n$. $\square$
