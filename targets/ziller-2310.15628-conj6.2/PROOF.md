# Proof of Ziller `arXiv:2310.15628v2` Conjecture 6.2

**Theorem (Conjecture 6.2 of [Ziller, arXiv:2310.15628v2]).**
*The function $f \colon \mathbb{N} \to \mathbb{Q}$ defined by $f(x) = \dfrac{\varphi(x)}{x^2}$ (where $\mathbb{N} = \{1, 2, 3, \dots\}$ and $\varphi$ is Euler's totient function) is injective: for all $x, y \in \mathbb{N}$, if $\dfrac{\varphi(x)}{x^2} = \dfrac{\varphi(y)}{y^2}$, then $x = y$.*

*(Consequently, the reciprocal function $x \mapsto \dfrac{x^2}{\varphi(x)}$ is also injective on $\mathbb{N}$.)*

## Proof

Recall that for any $n \in \mathbb{N}$ with prime factorization $n = \prod_{q} q^{e_q}$ (finite product over primes $q \mid n$ with $e_q = v_q(n) \ge 1$), Euler's totient function satisfies
$$
\varphi(n) = \prod_{q \mid n} q^{e_q - 1}(q - 1),
$$
and therefore
$$
f(n) = \frac{\varphi(n)}{n^2} = \prod_{q \mid n} \frac{q^{e_q - 1}(q - 1)}{q^{2e_q}} = \prod_{q \mid n} \frac{q - 1}{q^{e_q + 1}}.
$$
Note that for any prime $p$, the $p$-adic valuation $v_p \colon \mathbb{Q}_{>0} \to \mathbb{Z}$ is a group homomorphism, so
$$
v_p(f(n)) = \sum_{q \mid n} \Bigl( v_p(q - 1) - (e_q + 1)\, v_p(q) \Bigr).
$$

Now suppose for contradiction that there exist distinct positive integers $x, y \in \mathbb{N}$ ($x \neq y$) such that $f(x) = f(y)$. Without loss of generality, choose such a pair $(x, y)$ minimizing $x y$ (or simply define $p$ to be the largest prime at which $v_p(x) \neq v_p(y)$, or proceed by induction on $\max(x,y)$; we give the minimal-counterexample argument below).

Since $x \neq y$, at least one of $x, y$ is greater than $1$, so $\mathrm{lcm}(x, y) > 1$. Let $p$ be the **largest prime factor** of $x y$.

For every prime $q$ dividing $x$ or $y$, we have $q \le p$, and hence $1 \le q - 1 < p$. Because $p$ is prime and strictly larger than $q - 1 \ge 1$, it follows that
$$
p \nmid (q - 1), \quad \text{so} \quad v_p(q - 1) = 0 \quad \text{for every prime } q \mid xy.
$$
On the other hand, $v_p(q) = 1$ if $q = p$ and $v_p(q) = 0$ if $q \neq p$. Writing $e = v_p(x) \ge 0$ and $f' = v_p(y) \ge 0$, the valuation formula above gives:
$$
v_p(f(x)) = \begin{cases} 0, & \text{if } e = 0 \text{ (i.e., } p \nmid x\text{)}, \\ -(e + 1), & \text{if } e \ge 1, \end{cases}
\qquad
v_p(f(y)) = \begin{cases} 0, & \text{if } f' = 0 \text{ (i.e., } p \nmid y\text{)}, \\ -(f' + 1), & \text{if } f' \ge 1. \end{cases}
$$

Since $p \mid xy$, at least one of $e, f'$ is at least $1$, so at least one of $v_p(f(x)), v_p(f(y))$ is strictly negative (in fact $\le -2$). Because $f(x) = f(y)$, we have $v_p(f(x)) = v_p(f(y))$, which forces:
1. Both $e \ge 1$ and $f' \ge 1$ (since $0 \neq -(m+1)$ for all $m \ge 1$).
2. $-(e + 1) = -(f' + 1)$, so $e = f' \ge 1$.

Now write $x = p^e x_0$ and $y = p^e y_0$ with $p \nmid x_0$ and $p \nmid y_0$. Since $\gcd(p^e, x_0) = \gcd(p^e, y_0) = 1$ and $\varphi$ is multiplicative, $f$ is also multiplicative on coprime arguments, giving
$$
f(x) = f(p^e) f(x_0) \quad \text{and} \quad f(y) = f(p^e) f(y_0).
$$
Since $f(p^e) = \frac{p-1}{p^{e+1}} > 0$ and $f(x) = f(y)$, dividing both sides by $f(p^e)$ yields
$$
f(x_0) = f(y_0).
$$
However, $x \neq y$ implies $x_0 \neq y_0$, while $x_0 y_0 = \frac{xy}{p^{2e}} < xy$, contradicting the minimality of $xy$.

Therefore, no distinct $x, y \in \mathbb{N}$ can satisfy $\frac{\varphi(x)}{x^2} = \frac{\varphi(y)}{y^2}$, proving Conjecture 6.2. $\blacksquare$
