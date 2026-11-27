# Proof of Wolfdieter Lang's Discriminant Quotient Conjecture (OEIS A215041)

## 1. Definitions and Statement

For each integer $n \ge 1$, let $\rho(n) := 2\cos(\pi/n) = \zeta_{2n} + \zeta_{2n}^{-1}$ ($\zeta_{2n} = e^{i\pi/n}$), let $C(n, x) \in \mathbb{Z}[x]$ be the monic minimal polynomial of $\rho(n)$ over $\mathbb{Q}$ (OEIS `A187360`), and let $\delta(n) := \deg C(n, x)$ (`A055034`). Explicitly:
- $C(1, x) = x + 2$, $\delta(1) = 1$, $\mathrm{Disc}(C(1, x)) = 1$, and $a(1) = 1^1 / 1 = 1$.
- For $n \ge 2$, the roots of the $(2n)$-th cyclotomic polynomial $\Phi_{2n}(z)$ are the $\varphi(2n)$ primitive $(2n)$-th roots of unity $\zeta_{2n}^k$ ($\gcd(k, 2n) = 1$). Because $\zeta_{2n}^k + \zeta_{2n}^{-k} = 2\cos(\pi k/n)$ pairs distinct inverse roots (since $2n \ge 4$ so $\zeta_{2n}^k \neq \pm 1$), the conjugates of $\rho(n)$ over $\mathbb{Q}$ are precisely the $d := \delta(n) = \varphi(2n)/2$ distinct real numbers
  $$x_i = 2\cos\!\left(\frac{\pi k_i}{n}\right) \in (-2, 2) \qquad (1 \le k_1 < \dots < k_d < n,\ \gcd(k_i, 2n) = 1).$$
  Consequently, $\Phi_{2n}(z)$ and $C(n, x)$ satisfy the exact polynomial identity
  $$\Phi_{2n}(z) = z^{\delta(n)} \, C\!\left(n,\, z + z^{-1}\right) \qquad (\forall n \ge 2).$$

We prove that $a(n) := \frac{n^{\delta(n)}}{\mathrm{Disc}(C(n, x))}$ satisfies for all $n \ge 2$:
1. $a(2^k) = 2$ for every $k \ge 1$;
2. $a(p^k) = p^{(p^{k-1}+1)/2}$ for every odd prime $p$ and $k \ge 1$;
3. $a(n) = \prod_{\substack{p \mid n \\ p \text{ odd prime}}} p^{\delta(n)/(p-1)}$ otherwise.

---

## 2. Self-Contained Cyclotomic Discriminant Formula

**Lemma 1 (Discriminant of $\Phi_m(z)$).** *For every integer $m \ge 2$,*
$$|\mathrm{Disc}(\Phi_m)| = \frac{m^{\varphi(m)}}{\displaystyle\prod_{q \mid m \text{ prime}} q^{\varphi(m)/(q-1)}}.$$

*Proof.* By Möbius inversion on $z^m - 1 = \prod_{e \mid m} \Phi_e(z)$, we have $\Phi_m(z) = \prod_{e \mid m} (z^e - 1)^{\mu(m/e)}$. Separating the $e = m$ factor ($\mu(1) = 1$) and writing $k = m/e$ gives the rational-function identity
$$\frac{\Phi_m(z)}{z^m - 1} = \prod_{\substack{k \mid m \\ k > 1}} \bigl(z^{m/k} - 1\bigr)^{\mu(k)}.$$
Let $\zeta$ be any root of $\Phi_m(z)$ (a primitive $m$-th root of unity). Since $m/k < m$ for every divisor $k > 1$, $\zeta^{m/k} \neq 1$. Taking the limit $z \to \zeta$ on both sides yields
$$\frac{\Phi_m'(\zeta)}{m \zeta^{m-1}} = \prod_{\substack{k \mid m \\ k > 1}} \bigl(\zeta^{m/k} - 1\bigr)^{\mu(k)}.$$
Take the product over all $\varphi(m)$ primitive $m$-th roots $\zeta$ of unity. On the left, $\prod_{\zeta} \Phi_m'(\zeta) = \pm \mathrm{Disc}(\Phi_m)$ (as $\Phi_m$ is monic) and $\left|\prod_{\zeta} m \zeta^{m-1}\right| = m^{\varphi(m)}$.

On the right, for each divisor $k > 1$ of $m$, as $\zeta$ ranges over $(\mathbb{Z}/m\mathbb{Z})^\times$ (via $\zeta = e^{2\pi i r / m}$), $\eta = \zeta^{m/k} = e^{2\pi i r / k}$ is the image of $r$ under the canonical reduction homomorphism $(\mathbb{Z}/m\mathbb{Z})^\times \to (\mathbb{Z}/k\mathbb{Z})^\times$. By the Chinese Remainder Theorem (surjectivity on prime-power components), this homomorphism is surjective with uniform fiber size $\varphi(m)/\varphi(k)$. Hence
$$\prod_{\Phi_m(\zeta) = 0} \bigl(\zeta^{m/k} - 1\bigr) = \left( \prod_{\Phi_k(\eta) = 0} (\eta - 1) \right)^{\varphi(m)/\varphi(k)} = \bigl((-1)^{\varphi(k)} \Phi_k(1)\bigr)^{\varphi(m)/\varphi(k)}.$$
Recall that for $k > 1$, $\Phi_k(1) = q$ if $k = q^a$ is a prime power ($a \ge 1$) and $\Phi_k(1) = 1$ otherwise (proof: evaluating $\frac{z^k - 1}{z - 1} = \prod_{d \mid k,\, d > 1} \Phi_d(z)$ at $z = 1$ gives $k = \prod_{d \mid k,\, d > 1} \Phi_d(1)$, so induction on $k$ yields $\Phi_{q^a}(1) = q$ and $\Phi_k(1) = 1$ when $k$ has $\ge 2$ distinct prime factors). Since $\mu(k) = 0$ for all prime powers $k = q^a$ with $a \ge 2$, and $\mu(q) = -1$ for primes $q$, taking absolute values gives
$$\frac{|\mathrm{Disc}(\Phi_m)|}{m^{\varphi(m)}} = \prod_{\substack{k \mid m \\ k > 1}} |\Phi_k(1)|^{\mu(k)\varphi(m)/\varphi(k)} = \prod_{q \mid m \text{ prime}} q^{-\varphi(m)/(q-1)}. \quad \square$$

---

## 3. Exact Bridge from $\mathrm{Disc}(\Phi_{2n})$ to $\mathrm{Disc}(C(n, x))$

**Lemma 2 (Discriminant bridge).** *For every integer $n \ge 2$,*
$$\mathrm{Disc}(C(n, x))^2 = \frac{|\mathrm{Disc}(\Phi_{2n})|}{|C(n, 2)\, C(n, -2)|}.$$

*Proof.* Set $d := \delta(n) = \varphi(2n)/2$. Differentiating $\Phi_{2n}(z) = z^d \, C(n, z + z^{-1})$ with respect to $z$ gives
$$\Phi_{2n}'(z) = d z^{d-1} C(n, z + z^{-1}) + z^d (1 - z^{-2}) C'(n, z + z^{-1}).$$
At every root $\zeta$ of $\Phi_{2n}(z)$, we have $C(n, \zeta + \zeta^{-1}) = 0$, so
$$\Phi_{2n}'(\zeta) = \zeta^{d-1} (\zeta - \zeta^{-1})\, C'(n, \zeta + \zeta^{-1}).$$
Take the product over all $2d$ roots $\zeta$ of $\Phi_{2n}(z)$, grouped into the $d$ reciprocal pairs $\{\zeta_i, \zeta_i^{-1}\}$ ($1 \le i \le d$) corresponding to $x_i = \zeta_i + \zeta_i^{-1}$:
- $\prod_{i=1}^d (\zeta_i \zeta_i^{-1})^{d-1} = 1$;
- $\prod_{i=1}^d (\zeta_i - \zeta_i^{-1})(\zeta_i^{-1} - \zeta_i) = \prod_{i=1}^d -\bigl((\zeta_i + \zeta_i^{-1})^2 - 4\bigr) = \prod_{i=1}^d (4 - x_i^2) = (-1)^d C(n, 2)\, C(n, -2)$ (since $C(n, x) = \prod_{i=1}^d (x - x_i)$ is monic);
- $\prod_{i=1}^d C'(\zeta_i + \zeta_i^{-1}) C'(\zeta_i^{-1} + \zeta_i) = \prod_{i=1}^d C'(n, x_i)^2 = \mathrm{Disc}(C(n, x))^2$.

Since $\left|\prod_{\Phi_{2n}(\zeta)=0} \Phi_{2n}'(\zeta)\right| = |\mathrm{Disc}(\Phi_{2n})|$ and $C(n, \pm 2) \neq 0$ (all $x_i \in (-2, 2)$), taking absolute values yields
$$|\mathrm{Disc}(\Phi_{2n})| = |C(n, 2)\, C(n, -2)| \cdot \mathrm{Disc}(C(n, x))^2. \quad \square$$

**Lemma 3 (Evaluation of $|C(n, 2)\, C(n, -2)|$).** *For every $n \ge 2$,*
$$|C(n, 2)\, C(n, -2)| = \begin{cases} 4 & \text{if } n = 2^k \ (k \ge 1), \\ p & \text{if } n = p^k \ (p \text{ odd prime},\ k \ge 1), \\ 1 & \text{otherwise}. \end{cases}$$

*Proof.* Evaluating $\Phi_{2n}(z) = z^d C(n, z + z^{-1})$ at $z = 1$ and $z = -1$ gives $C(n, 2) = \Phi_{2n}(1)$ and $|C(n, -2)| = |\Phi_{2n}(-1)|$, so $|C(n, 2) C(n, -2)| = |\Phi_{2n}(1) \Phi_{2n}(-1)|$.
- **Case (i): $n = 2^k$ ($k \ge 1$).** Here $2n = 2^{k+1} \ge 4$, so $\Phi_{2^{k+1}}(z) = z^{2^k} + 1$. Thus $\Phi_{2n}(1) = 2$ and $\Phi_{2n}(-1) = 2$, giving product $4$.
- **Case (ii): $n = p^k$ ($p$ odd prime, $k \ge 1$).** Here $2n = 2p^k$ has two distinct prime factors, so $\Phi_{2n}(1) = 1$. Since $p^k$ is odd, $\zeta$ is a primitive $(2p^k)$-th root of unity iff $-\zeta$ is a primitive $p^k$-th root of unity, so $\Phi_{2p^k}(-z) = \Phi_{p^k}(z)$. Hence $\Phi_{2n}(-1) = \Phi_{p^k}(1) = p$, giving product $1 \cdot p = p$.
- **Case (iii): Otherwise.** Either $n \ge 3$ is odd with $\ge 2$ distinct prime factors, or $n = 2^a m$ ($a \ge 1$, $m \ge 3$ odd).
  - If $n$ is odd with $\ge 2$ odd prime factors, then both $2n$ and $n$ have $\ge 2$ distinct prime factors, and $\Phi_{2n}(-z) = \Phi_n(z)$, so $\Phi_{2n}(1) = 1$ and $\Phi_{2n}(-1) = \Phi_n(1) = 1$.
  - If $n = 2^a m$ ($a \ge 1$, $m \ge 3$ odd), then $2n = 2^{a+1} m$ has $\ge 2$ distinct prime factors ($2$ and a prime dividing $m$), so $\Phi_{2n}(1) = 1$. Because $4 \mid 2n$, negation $\zeta \mapsto -\zeta$ preserves exact order $2n$, so $\Phi_{2n}(-z) = \Phi_{2n}(z)$ and $\Phi_{2n}(-1) = \Phi_{2n}(1) = 1$.
  In both subcases, $|C(n, 2) C(n, -2)| = 1$. $\square$

---

## 4. Completion of the Proof

Let $n \ge 2$, and set $d = \delta(n) = \varphi(2n)/2$, so $\varphi(2n) = 2d$. Applying Lemma 1 with $m = 2n$ gives
$$|\mathrm{Disc}(\Phi_{2n})| = \frac{(2n)^{2d}}{\displaystyle\prod_{q \mid 2n \text{ prime}} q^{2d/(q-1)}} = \frac{2^{2d} \, n^{2d}}{2^{2d/(2-1)} \displaystyle\prod_{\substack{p \mid n \\ p \text{ odd prime}}} p^{2d/(p-1)}} = \frac{n^{2d}}{\displaystyle\prod_{\substack{p \mid n \\ p \text{ odd prime}}} p^{2d/(p-1)}},$$
where the factor $2^{2d}$ cancels identically in numerator and denominator because $q = 2$ always divides $2n$.

Now note that $\mathrm{Disc}(C(n, x)) = \prod_{1 \le i < j \le d} (x_i - x_j)^2 > 0$ because all $d$ roots $x_i$ of $C(n, x)$ are distinct real numbers; hence $a(n) = n^d / \mathrm{Disc}(C(n, x)) > 0$. By Lemma 2,
$$a(n)^2 = \frac{n^{2d}}{\mathrm{Disc}(C(n, x))^2} = |C(n, 2)\, C(n, -2)| \prod_{\substack{p \mid n \\ p \text{ odd prime}}} p^{2d/(p-1)}.$$
Applying Lemma 3 and taking positive square roots yields all three conjectured cases:
- **Case (i) ($n = 2^k$, $k \ge 1$):** No odd prime divides $n$, so $a(2^k)^2 = 4 \cdot 1 = 4$, whence $a(2^k) = 2$.
- **Case (ii) ($n = p^k$, $p$ odd prime, $k \ge 1$):** Here $d = \delta(p^k) = \frac{\varphi(2p^k)}{2} = \frac{p^{k-1}(p-1)}{2}$, so $\frac{2d}{p-1} = p^{k-1}$. By Lemma 3, $a(p^k)^2 = p \cdot p^{p^{k-1}} = p^{p^{k-1} + 1}$, whence
  $$a(p^k) = p^{(p^{k-1} + 1)/2}.$$
- **Case (iii) (all other $n \ge 2$):** By Lemma 3, $|C(n, 2) C(n, -2)| = 1$, so
  $$a(n)^2 = \prod_{\substack{p \mid n \\ p \text{ odd prime}}} p^{2\delta(n)/(p-1)} \implies a(n) = \prod_{\substack{p \mid n \\ p \text{ odd prime}}} p^{\delta(n)/(p-1)}. \quad \blacksquare$$
