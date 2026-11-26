# Proof of Conjecture 5.1 of arXiv:2202.08116v1 (`dris-2202.08116-conj5.1`)

**Status:** Written proof, verified on small cases and exact periodic moment identities (`verify.py PASS`); pending independent check and adversarial audit.

## Statement

Let $\sigma(n) = \sum_{d \mid n} d$ denote the sum-of-divisors function, and let
$$A = \left\{ m \in \mathbb{Z}_{\ge 1} : \gcd(m, \sigma(m^2)) = \gcd(m^2, \sigma(m^2)) \right\}.$$
We prove that $A$ has asymptotic density $0$, i.e.,
$$\lim_{X \to \infty} \frac{|A \cap \{1, 2, \dots, X\}|}{X} = 0.$$

## Proof

### Lemma 1 (Prime-power divisibility criterion)
Let $p \equiv 1 \pmod 6$ be a prime. Then:
1. The congruence $u^2 + u + 1 \equiv 0 \pmod p$ has exactly two distinct solutions $r_p, s_p \in \{2, \dots, p-2\}$.
2. Let $\mathcal{Q}_p = \{ q \text{ prime} : q \equiv r_p \pmod p \text{ or } q \equiv s_p \pmod p \}$. Note that $p \notin \mathcal{Q}_p$.
3. If $m \in \mathbb{Z}_{\ge 1}$ satisfies $p \parallel m$ (meaning $p \mid m$ and $p^2 \nmid m$) and there exist at least two distinct primes $q_1, q_2 \in \mathcal{Q}_p$ such that $q_1 \parallel m$ and $q_2 \parallel m$, then $m \notin A$.

*Proof.*
(1) Since $p \equiv 1 \pmod 6$, we have $p \ge 7$ and $3 \mid (p - 1)$. Because $(\mathbb{Z}/p\mathbb{Z})^\times$ is cyclic of order $p - 1$, there are exactly two elements $r_p, s_p \in (\mathbb{Z}/p\mathbb{Z})^\times$ of order $3$, which are the roots of $\frac{u^3 - 1}{u - 1} = u^2 + u + 1 \equiv 0 \pmod p$. Neither root is $0$ or $1 \pmod p$ (since $0^2 + 0 + 1 = 1 \not\equiv 0$ and $1^2 + 1 + 1 = 3 \not\equiv 0 \pmod p$ as $p \ge 7$), and they are distinct modulo $p$ because $u^3 - 1$ is separable over $\mathbb{F}_p$ (as $p \neq 3$). Hence $r_p, s_p \in \{2, \dots, p-2\}$.
(2) Any $q \in \mathcal{Q}_p$ satisfies $q \equiv r_p$ or $s_p \not\equiv 0 \pmod p$, so $q \neq p$.
(3) Since $q_1, q_2$ are distinct primes with $q_1 \parallel m$ and $q_2 \parallel m$, we have $q_1^2 \parallel m^2$ and $q_2^2 \parallel m^2$ with $\gcd(q_1^2, q_2^2) = 1$. By the multiplicativity of $\sigma$,
$$\sigma(q_1^2) \sigma(q_2^2) \mid \sigma(m^2).$$
For $j \in \{1, 2\}$, $\sigma(q_j^2) = q_j^2 + q_j + 1 \equiv 0 \pmod p$ because $q_j \in \mathcal{Q}_p$. Therefore $p^2 \mid \sigma(q_1^2) \sigma(q_2^2) \mid \sigma(m^2)$, so $v_p(\sigma(m^2)) \ge 2$ (where $v_p$ denotes the $p$-adic valuation). Since $p \parallel m$, we have $v_p(m) = 1$ and $v_p(m^2) = 2$. Consequently,
$$v_p(\gcd(m, \sigma(m^2))) = \min(1, v_p(\sigma(m^2))) = 1 < 2 = \min(2, v_p(\sigma(m^2))) = v_p(\gcd(m^2, \sigma(m^2))),$$
which implies $\gcd(m, \sigma(m^2)) \neq \gcd(m^2, \sigma(m^2))$, so $m \notin A$. $\square$

### Lemma 2 (Covering $A$ for a finite truncation)
Let $p_1 < p_2 < \dots$ be the primes congruent to $1 \pmod 6$. Fix an integer $k \ge 1$ and define:
$$E_k = \left\{ m \in \mathbb{Z}_{\ge 1} : \forall i \in \{1, \dots, k\},\ p_i \nparallel m \right\},$$
$$B_i = \left\{ m \in \mathbb{Z}_{\ge 1} : \#\{ q \in \mathcal{Q}_{p_i} : q \parallel m \} \le 1 \right\} \quad (1 \le i \le k).$$
Then:
1. $A \subseteq E_k \cup \bigcup_{i=1}^k B_i$.
2. $E_k$ has asymptotic density
$$d(E_k) = \prod_{i=1}^k \left(1 - \frac{p_i - 1}{p_i^2}\right).$$

*Proof.*
(1) If $m \notin E_k \cup \bigcup_{i=1}^k B_i$, then there exists $i \in \{1, \dots, k\}$ such that $p_i \parallel m$ and $m \notin B_i$ (so $m$ has at least two distinct prime factors $q_1, q_2 \in \mathcal{Q}_{p_i}$ with $q_1 \parallel m$ and $q_2 \parallel m$). By Lemma 1, $m \notin A$.
(2) For each $i$, the condition $p_i \nparallel m$ holds if and only if $m \bmod p_i^2 \notin \{p_i, 2p_i, \dots, (p_i - 1)p_i\}$, which leaves $p_i^2 - (p_i - 1)$ admissible residue classes modulo $p_i^2$. Since $p_1^2, \dots, p_k^2$ are pairwise coprime, by the Chinese Remainder Theorem, $E_k$ is a union of $\prod_{i=1}^k (p_i^2 - p_i + 1)$ residue classes modulo $M_k = \prod_{i=1}^k p_i^2$. Hence for every $X \ge 1$,
$$\left| |E_k \cap [1, X]| - X \prod_{i=1}^k \left(1 - \frac{p_i - 1}{p_i^2}\right) \right| \le M_k.$$
Dividing by $X$ and taking $X \to \infty$ gives $d(E_k) = \prod_{i=1}^k \left(1 - \frac{p_i - 1}{p_i^2}\right)$. $\square$

### Lemma 3 (Each bad set $B_i$ has density $0$)
For every $i \ge 1$, the set $B_i$ has asymptotic density $0$ (in particular, $\overline{d}(B_i) = 0$).

*Proof.*
Fix $i \ge 1$, and write $p = p_i$ and $\mathcal{Q} = \mathcal{Q}_{p_i}$. Since $\gcd(r_p, p) = 1$, Dirichlet's theorem on primes in arithmetic progressions guarantees that $\sum_{q \equiv r_p \pmod p} \frac{1}{q} = \infty$. Because $1 - \frac{1}{q} \ge \frac{1}{2}$ for every prime $q$, the series
$$\sum_{q \in \mathcal{Q}} \frac{1}{q}\left(1 - \frac{1}{q}\right)$$
diverges to $+\infty$.

For any real cutoff $P \ge 2$, let $\mathcal{Q}(P) = \{q \in \mathcal{Q} : q \le P\}$ (a finite set of primes), and define
$$f_P(m) = \sum_{q \in \mathcal{Q}(P)} \mathbf{1}_{q \parallel m}, \qquad S(P) = \sum_{q \in \mathcal{Q}(P)} \frac{1}{q}\left(1 - \frac{1}{q}\right).$$
Choose $P$ large enough that $S(P) \ge 2$. Also define the finite-cutoff superset
$$\tilde{B}_{i, P} = \{ m \in \mathbb{Z}_{\ge 1} : f_P(m) \le 1 \}.$$
Clearly $B_i \subseteq \tilde{B}_{i, P}$, because $f_P(m) \le \#\{q \in \mathcal{Q} : q \parallel m\} \le 1$ for every $m \in B_i$.

Set $N_P = \prod_{q \in \mathcal{Q}(P)} q^2$. Since each indicator $\mathbf{1}_{q \parallel m}$ depends only on $m \bmod q^2$, both $f_P(m)$ and the membership $m \in \tilde{B}_{i, P}$ are periodic in $m$ with period $N_P$. Thus $\tilde{B}_{i, P}$ has exact asymptotic density
$$d(\tilde{B}_{i, P}) = \frac{|\tilde{B}_{i, P} \cap \{1, \dots, N_P\}|}{N_P} = \mathbb{P}_{m \sim \mathrm{Unif}(\{1, \dots, N_P\})}\!\left(f_P(m) \le 1\right).$$
By the Chinese Remainder Theorem, under the uniform distribution on $\{1, \dots, N_P\} \cong \prod_{q \in \mathcal{Q}(P)} \mathbb{Z}/q^2\mathbb{Z}$, the random variables $X_q(m) = \mathbf{1}_{q \parallel m}$ for $q \in \mathcal{Q}(P)$ are mutually independent Bernoulli random variables with success probability
$$\alpha_q = \mathbb{P}(q \parallel m) = \frac{q - 1}{q^2} = \frac{1}{q}\left(1 - \frac{1}{q}\right).$$
Therefore,
$$\mathbb{E}[f_P] = \sum_{q \in \mathcal{Q}(P)} \alpha_q = S(P),$$
$$\mathrm{Var}(f_P) = \sum_{q \in \mathcal{Q}(P)} \alpha_q(1 - \alpha_q) \le \sum_{q \in \mathcal{Q}(P)} \alpha_q = S(P).$$
Since $f_P(m) \le 1$ implies $|f_P(m) - S(P)| \ge S(P) - 1 > 0$, Chebyshev's inequality yields
$$\overline{d}(B_i) \le d(\tilde{B}_{i, P}) = \mathbb{P}(f_P(m) \le 1) \le \mathbb{P}(|f_P(m) - S(P)| \ge S(P) - 1) \le \frac{\mathrm{Var}(f_P)}{(S(P) - 1)^2} \le \frac{S(P)}{(S(P) - 1)^2}.$$
Letting $P \to \infty$, we have $S(P) \to \infty$, so $\frac{S(P)}{(S(P)-1)^2} \to 0$. Hence $\overline{d}(B_i) = 0$, so $d(B_i) = 0$. $\square$

### Conclusion
By Lemma 2 and Lemma 3, for every $k \ge 1$, subadditivity of upper asymptotic density gives
$$\overline{d}(A) \le d(E_k) + \sum_{i=1}^k \overline{d}(B_i) = \prod_{i=1}^k \left(1 - \frac{p_i - 1}{p_i^2}\right).$$
Using the elementary inequality $1 - x \le e^{-x}$ for $x \in \mathbb{R}$ and $\frac{p_i - 1}{p_i^2} \ge \frac{1}{2 p_i}$ (since $p_i \ge 7$),
$$0 \le \overline{d}(A) \le \exp\left( - \sum_{i=1}^k \frac{p_i - 1}{p_i^2} \right) \le \exp\left( - \frac{1}{2} \sum_{i=1}^k \frac{1}{p_i} \right).$$
By Dirichlet's theorem on primes in arithmetic progressions ($\gcd(1, 6) = 1$), $\sum_{i=1}^\infty \frac{1}{p_i} = \infty$. Letting $k \to \infty$ gives $\overline{d}(A) = 0$. Since $0 \le \underline{d}(A) \le \overline{d}(A) = 0$, the asymptotic density of $A$ exists and equals $0$. $\blacksquare$
