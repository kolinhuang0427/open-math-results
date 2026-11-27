# Proof of Zhi-Wei Sun's Supercongruence Conjectures for OEIS A190969

## 1. Exact Statement and Main Theorem

**Primary Source:** OEIS `A190969` (fetched live, `revision: 48`, `2025-11-05`):
- **Name:** `a(n) = 5*a(n-1) - 8*a(n-2), with a(0)=0, a(1)=1.`
- **Comment (Zhi-Wei Sun, Mar 13 2013):**
  > `Let S(p):=Sum_{k=0..p-1} a(4k)*binomial(2k,k)^3/(-4096)^k. Zhi-Wei Sun conjectured that S(p) == 0 (mod p^2) for every odd prime p, and also S(p) == 0 (mod p^3) for any odd prime p == 1,2,4 (mod 7).`

**Formalization Source:** `google-deepmind/formal-conjectures`, `FormalConjectures/OEIS/190969.lean`:
- `def a : ℕ → ℤ | 0 => 0 | 1 => 1 | n + 2 => 5 * a (n + 1) - 8 * a n`
- `def sMod (p m : ℕ) : ZMod (p ^ m) := ∑ k ∈ Finset.range p, (a (4 * k) : ZMod (p ^ m)) * ((2 * k).choose k : ZMod (p ^ m)) ^ 3 * ((-4096 : ZMod (p ^ m)) ^ k)⁻¹`
- **`conjecture_1`:** For every odd prime $p$, `sMod p 2 = 0`.
- **`conjecture_2`:** For every odd prime $p$ with $p \bmod 7 \in \{1, 2, 4\}$, `sMod p 3 = 0`.

Since $-4096 = -2^{12}$ is coprime to every odd prime $p$, the rational number
$$S(p) := \sum_{k=0}^{p-1} \frac{a(4k)\binom{2k}{k}^3}{(-4096)^k}$$
lies in the local ring $\mathbb{Z}_{(p)} = \mathbb{Q} \cap \mathbb{Z}_p$, and its image under the canonical reduction $\mathbb{Z}_{(p)} \to \mathbb{Z}/p^m\mathbb{Z}$ is precisely `sMod p m`.

**Theorem.** *Both conjectures hold:*
1. *For every odd prime $p$, $S(p) \equiv 0 \pmod{p^2}$ in $\mathbb{Z}_{(p)}$.*
2. *For every odd prime $p \equiv 1, 2, 4 \pmod 7$, $S(p) \equiv 0 \pmod{p^3}$ in $\mathbb{Z}_{(p)}$.*

---

## 2. Algebraic Decomposition in $\mathbb{Q}(\sqrt{-7})$

Let $K = \mathbb{Q}(s)$ where $s^2 = -7$, with ring of integers $\mathcal{O}_K = \mathbb{Z}[\omega]$, $\omega := \frac{1+s}{2}$ (satisfying $\omega^2 - \omega + 2 = 0$). Fix the complex embedding $K \hookrightarrow \mathbb{C}$ mapping $s \mapsto i\sqrt{7}$ (with $\sqrt{7} > 0$).

The characteristic polynomial $X^2 - 5X + 8 = 0$ of the recurrence $a(n) = 5a(n-1) - 8a(n-2)$ has roots
$$\alpha := \frac{5 + s}{2}, \qquad \beta := \frac{5 - s}{2} \in \mathcal{O}_K,$$
satisfying $\alpha + \beta = 5$, $\alpha\beta = 8$, and $\alpha - \beta = s$. Since $\frac{\alpha^0 - \beta^0}{s} = 0 = a(0)$ and $\frac{\alpha^1 - \beta^1}{s} = 1 = a(1)$, Binet's formula gives
$$a(n) = \frac{\alpha^n - \beta^n}{s} \qquad \text{for all } n \ge 0.$$

Direct computation in $K$ yields $\alpha^2 = \frac{9 + 5s}{2}$ and
$$\alpha^4 = \frac{-47 + 45s}{2}, \qquad \beta^4 = \frac{-47 - 45s}{2}.$$
Define
$$t_1 := \frac{\beta^4}{-4096} = \frac{47 + 45s}{8192}, \qquad t_2 := \frac{\alpha^4}{-4096} = \frac{47 - 45s}{8192} = \overline{t_1} \in \mathcal{O}_K\!\left[\tfrac{1}{2}\right].$$
For any prime $p$, define the truncated hypergeometric polynomial
$$F_p(t) := \sum_{k=0}^{p-1} \binom{2k}{k}^3 t^k \in \mathbb{Z}[t].$$
Substituting $a(4k) = (\alpha^{4k} - \beta^{4k})/s$ into the definition of $S(p)$ gives the exact identity in $K$:
$$S(p) = \frac{F_p(t_2) - F_p(t_1)}{s}. \tag{2.1}$$

Observe further that $t_1 + t_2 = \frac{47}{4096}$ and $t_1 t_2 = \frac{47^2 + 7 \cdot 45^2}{8192^2} = \frac{16384}{67108864} = \frac{1}{4096}$, so $t_1$ and $t_2$ are the roots of $4096t^2 - 47t + 1 = 0$. In $\mathbb{Q}[t]$ we have the factorization
$$(16t - 1)^3 - 15^3 t^2 = 4096 t^3 - 4143 t^2 + 48 t - 1 = (t - 1)(4096 t^2 - 47 t + 1), \tag{2.2}$$
whose three distinct roots in $\mathbb{C}$ are $1$, $t_1$, and $t_2$.

---

## 3. Split Primes $p \equiv 1, 2, 4 \pmod 7$ (`conjecture_2`)

For $\tau \in \mathcal{H} := \{\tau \in \mathbb{C} : \mathrm{Im}(\tau) > 0\}$ and $q := e^{2\pi i\tau}$, let $\eta(\tau) = q^{1/24} \prod_{n=1}^\infty (1 - q^n)$ be the Dedekind eta function, and set
$$t(\tau) := \left(\frac{\eta(\tau)\eta(4\tau)}{\eta(2\tau)^2}\right)^{24}, \qquad \Theta(\tau) := \frac{\eta(2\tau)^{20}}{\eta(\tau)^8 \eta(4\tau)^8}.$$
As recorded in Beukers [1, Remark 1.14(2) and Appendix C, *Hypergeometric $F(1/2, 1/2, 1/2; 1, 1 \mid 64t)$*], the pair $(t(\tau), \Theta(\tau))$ satisfies Assumption (II) of [1] with level $N = 4$, Atkin–Lehner extension $\Gamma = \Gamma_0(4) + \langle w_4 \rangle$, $\eta$-product weight-$2$ modular form $\Theta(\tau) = 1 + O(q)$ (whose unique zero modulo $\Gamma$ has order $r = 1$ at the cusp $[1/2]$, the pole of $t$), Hauptmodul $t(\tau) = q + O(q^2)$, and generating series
$$F(t(\tau)) = \Theta(\tau), \qquad \text{where } F(t) = \sum_{k=0}^\infty \binom{2k}{k}^3 t^k.$$

### Lemma 3.1 (Modular equation and CM evaluations)
*For all $\tau \in \mathcal{H}$,*
$$(16 t(\tau) - 1)^3 + j(2\tau)\, t(\tau)^2 = 0, \tag{3.1}$$
*where $j$ is the elliptic modular $j$-invariant. At the CM points $\tau_1 := \frac{1 + s}{4} \in \mathcal{H}$ and $\tau_2 := \frac{-1 + s}{4} \in \mathcal{H}$, we have*
$$t(\tau_1) = t_1 = \frac{47 + 45s}{8192}, \qquad t(\tau_2) = t_2 = \frac{47 - 45s}{8192}.$$

*Proof.* Write $z := 2\tau \in \mathcal{H}$, so $e^{\pi i z} = e^{2\pi i\tau} = q$. Using the standard $\eta$-product representations of the Jacobi theta functions $\theta_2(z) = 2\frac{\eta(2z)^2}{\eta(z)}$, $\theta_3(z) = \frac{\eta(z)^5}{\eta(z/2)^2\eta(2z)^2}$, and $\theta_4(z) = \frac{\eta(z/2)^2}{\eta(z)}$ together with Jacobi's identity $\theta_3(z)^4 = \theta_2(z)^4 + \theta_4(z)^4$, the modular lambda function $\lambda(z) = \theta_2(z)^4 / \theta_3(z)^4$ satisfies
$$\lambda(2\tau) = 16\,\frac{\eta(\tau)^8 \eta(4\tau)^{16}}{\eta(2\tau)^{24}}, \qquad 1 - \lambda(2\tau) = \frac{\theta_4(2\tau)^4}{\theta_3(2\tau)^4} = \frac{\eta(\tau)^{16} \eta(4\tau)^8}{\eta(2\tau)^{24}}.$$
Multiplying these two identities yields $\lambda(2\tau)(1 - \lambda(2\tau)) = 16 \bigl(\frac{\eta(\tau)\eta(4\tau)}{\eta(2\tau)^2}\bigr)^{24} = 16 t(\tau)$. Substituting into the classical identity $j(z) = 256\frac{(1 - \lambda(z)(1-\lambda(z)))^3}{(\lambda(z)(1-\lambda(z)))^2}$ gives
$$j(2\tau) = 256\,\frac{(1 - 16 t(\tau))^3}{(16 t(\tau))^2} = \frac{(1 - 16 t(\tau))^3}{t(\tau)^2},$$
which rearranges to (3.1).

At $\tau_1$ and $\tau_2$, we have $2\tau_1 = \frac{1 + i\sqrt{7}}{2}$ and $2\tau_2 = 2\tau_1 - 1$, so by translation invariance of $j$ and the classical class-number-one value $j\bigl(\frac{1 + \sqrt{-7}}{2}\bigr) = -15^3 = -3375$ [2, (12.20)], we obtain $j(2\tau_1) = j(2\tau_2) = -15^3$. By (3.1) and (2.2), both $t(\tau_1)$ and $t(\tau_2)$ belong to $\{1, t_1, t_2\}$.

To determine which root is $t(\tau_1)$, rewrite the infinite product for $t(\tau)$ (valid for $|q| < 1$): since
$$\prod_{n=1}^\infty (1 + q^{2n-1}) = \frac{\prod_{n=1}^\infty (1 + q^n)}{\prod_{n=1}^\infty (1 + q^{2n})} = \frac{\prod_{n=1}^\infty \frac{1 - q^{2n}}{1 - q^n}}{\prod_{n=1}^\infty \frac{1 - q^{4n}}{1 - q^{2n}}} = \prod_{n=1}^\infty \frac{(1 - q^{2n})^2}{(1 - q^n)(1 - q^{4n})},$$
taking reciprocals, multiplying by $q^{1/24}$, and raising to the $24$-th power yields
$$t(\tau) = \frac{q}{\prod_{n=1}^\infty (1 + q^{2n-1})^{24}}. \tag{3.2}$$
At $\tau_1 = \frac{1 + i\sqrt{7}}{4}$, we have $q = e^{2\pi i\tau_1} = i\rho$ where $\rho := e^{-\pi\sqrt{7}/2}$. Since $2.6^2 = 6.76 < 7$ implies $\sqrt{7} > 2.6$, and $\pi > 3.14$, we have $\frac{\pi\sqrt{7}}{2} > 3.14 \times 1.3 = 4.082 > 4$. As $e > 2.7$ and $2.7^4 = 53.1441 > 50$, it follows that $0 < \rho < e^{-4} < \frac{1}{50}$.

For every integer $n \ge 1$, the term $q^{2n-1} = (-1)^{n-1} i \rho^{2n-1}$ is purely imaginary, so $|1 + q^{2n-1}| = \sqrt{1 + \rho^{4n-2}} > 1$. Hence (3.2) immediately implies
$$|t(\tau_1)| = \frac{\rho}{\prod_{n=1}^\infty (1 + \rho^{4n-2})^{12}} < \rho < \frac{1}{50} < 1,$$
which rules out $t(\tau_1) = 1$. Writing $1 + q^{2n-1} = \sqrt{1 + \rho^{4n-2}}\,e^{i\theta_n}$ with $\theta_n := (-1)^{n-1}\arctan(\rho^{2n-1}) \in (-\frac{\pi}{2}, \frac{\pi}{2})$, we have $|\theta_n| < \rho^{2n-1}$ and therefore
$$\sum_{n=1}^\infty |\theta_n| < \sum_{n=1}^\infty \rho^{2n-1} = \frac{\rho}{1 - \rho^2} < \frac{1/50}{1 - 1/2500} = \frac{50}{2499} < \frac{1}{49}.$$
Thus $t(\tau_1) = |t(\tau_1)| e^{i\phi}$ with $\phi := \frac{\pi}{2} - 24\sum_{n=1}^\infty \theta_n$ satisfying $|\phi - \frac{\pi}{2}| < \frac{24}{49} < \frac{1}{2} < \frac{\pi}{2}$. Consequently $\phi \in (0, \pi)$, so $\mathrm{Im}(t(\tau_1)) = |t(\tau_1)|\sin\phi > 0$. Since $\mathrm{Im}(t_1) = \frac{45\sqrt{7}}{8192} > 0 > \mathrm{Im}(t_2)$, we conclude $t(\tau_1) = t_1$.

Finally, at $\tau_2 = \frac{-1 + i\sqrt{7}}{4}$ we have $e^{2\pi i\tau_2} = -i\rho = \overline{i\rho}$; conjugating (3.2) yields $t(\tau_2) = \overline{t(\tau_1)} = \overline{t_1} = t_2$. $\square$

### Lemma 3.2 (Representation by $x^2 + 7y^2$)
*Every odd prime $p \equiv 1, 2, 4 \pmod 7$ can be written as $p = x^2 + 7y^2$ with $x, y \in \mathbb{Z}$.*

*Proof.* For any $\xi \in K$, choosing $b \in \mathbb{Z}$ with $|\mathrm{Im}(\xi) - b\frac{\sqrt{7}}{2}| \le \frac{\sqrt{7}}{4}$ and then $a \in \mathbb{Z}$ with $|\mathrm{Re}(\xi - b\omega) - a| \le \frac{1}{2}$ gives $N_{K/\mathbb{Q}}(\xi - (a + b\omega)) \le \frac{1}{4} + \frac{7}{16} = \frac{11}{16} < 1$, so $\mathcal{O}_K = \mathbb{Z}[\omega]$ is norm-Euclidean, hence a unique factorization domain. Since $p \equiv 1, 2, 4 \pmod 7$ is a nonzero square modulo $7$ and $p$ is odd, quadratic reciprocity gives $\bigl(\frac{-7}{p}\bigr) = \bigl(\frac{-1}{p}\bigr)\bigl(\frac{7}{p}\bigr) = \bigl(\frac{p}{7}\bigr) = 1$, so there exists $r \in \mathbb{Z}$ with $r^2 \equiv -7 \pmod p$. Thus $p \mid (r - s)(r + s)$ in $\mathcal{O}_K$, whereas $p \nmid (r \pm s) = (r \mp 1) \pm 2\omega$ in $\mathcal{O}_K$ because $p$ is odd. Hence $p$ is reducible in $\mathcal{O}_K$, so $p = N_{K/\mathbb{Q}}(u + v\omega) = u^2 + uv + 2v^2$ for some $u, v \in \mathbb{Z}$. If $v$ were odd, then $u(u + v)$ would be even and hence $u^2 + uv + 2v^2$ would be even, contradicting that $p$ is odd. Therefore $v = 2y$ is even, and setting $x := u + y \in \mathbb{Z}$ yields $p = x^2 + 7y^2$. $\square$

### Proposition 3.3 (Proof of `conjecture_2`)
*For every odd prime $p \equiv 1, 2, 4 \pmod 7$, $S(p) \equiv 0 \pmod{p^3}$ in $\mathbb{Z}_{(p)}$.*

*Proof.* By Lemma 3.2, write $p = x^2 + 7y^2$ with $x, y \in \mathbb{Z}$. Since $\bigl(\frac{-7}{p}\bigr) = 1$ and $p$ is odd, Hensel's lemma yields $\sigma_p \in \mathbb{Z}_p$ with $\sigma_p^2 = -7$, giving a field embedding $\iota: K \hookrightarrow \mathbb{Q}_p$ with $\iota(s) = \sigma_p$ and $\iota(\mathcal{O}_K) \subset \mathbb{Z}_p$. In $\mathbb{Z}_p$,
$$\iota(x + ys)\,\iota(x - ys) = x^2 + 7y^2 = p,$$
so the $p$-adic valuations of $\iota(x + ys)$ and $\iota(x - ys)$ are nonnegative integers summing to $1$. Replacing $y$ by $-y$ if necessary, we may assume $\iota(x + ys) \in \mathbb{Z}_p^\times$.

We now apply Beukers' Theorem 1.15 [1] (`\label{thm:CMpoints3}`) to $(t(\tau), \Theta(\tau))$ (level $N = 4$) at both $\tau_1 = \frac{1 + s}{4}$ and $\tau_2 = \frac{-1 + s}{4}$, using the **same** embedding $\iota: K \hookrightarrow \mathbb{Q}_p$. Every hypothesis of [1, Theorem 1.15] is satisfied:
- Assumption (II) holds for $(t(\tau), \Theta(\tau))$ with $N = 4$, and $p$ is odd, so $N \nmid p$ and $p$ splits in $K = \mathbb{Q}(\tau_1) = \mathbb{Q}(\tau_2)$.
- Both $\tau_1, \tau_2 \in K$ have positive imaginary part $\frac{\sqrt{7}}{4} > 0$, with $4|\tau_i|^2 = 4 \cdot \frac{1 + 7}{16} = 2 \in \mathbb{Z}$ and $4(\tau_i + \overline{\tau_i}) = \pm 2 \in \mathbb{Z}$.
- Set $(c_1, d_1) := (4y, x - y) \in \mathbb{Z}^2$ for $\tau_1$ and $(c_2, d_2) := (4y, x + y) \in \mathbb{Z}^2$ for $\tau_2$. Then $4 \mid c_1$, $4 \mid c_2$, and
  $$c_1 \tau_1 + d_1 = 4y \cdot \frac{1 + s}{4} + (x - y) = x + ys, \qquad c_2 \tau_2 + d_2 = 4y \cdot \frac{-1 + s}{4} + (x + y) = x + ys,$$
  so $|c_1 \tau_1 + d_1|^2 = |c_2 \tau_2 + d_2|^2 = x^2 + 7y^2 = p$ and $\iota(c_1 \tau_1 + d_1) = \iota(c_2 \tau_2 + d_2) = \iota(x + ys) \in \mathbb{Z}_p^\times$.
- By Lemma 3.1, $t(\tau_1) = t_1 = \frac{47 + 45s}{8192}$ and $t(\tau_2) = t_2 = \frac{47 - 45s}{8192}$; since $2 \in \mathbb{Z}_p^\times$ and $\iota(s) = \sigma_p \in \mathbb{Z}_p$, both $\iota(t(\tau_1))$ and $\iota(t(\tau_2))$ lie in $\mathbb{Z}_p$.

Therefore [1, Theorem 1.15] yields
$$F_p(\iota(t_1)) \equiv \iota(x + ys)^2 \pmod{p^3 \mathbb{Z}_p} \qquad \text{and} \qquad F_p(\iota(t_2)) \equiv \iota(x + ys)^2 \pmod{p^3 \mathbb{Z}_p}.$$
Subtracting these two congruences and applying $\iota$ to (2.1) gives
$$\sigma_p \cdot S(p) = F_p(\iota(t_2)) - F_p(\iota(t_1)) \equiv 0 \pmod{p^3 \mathbb{Z}_p}.$$
Since $p \neq 7$, we have $\sigma_p^2 = -7 \in \mathbb{Z}_p^\times$, so $\sigma_p \in \mathbb{Z}_p^\times$. Dividing by $\sigma_p$ gives $S(p) \equiv 0 \pmod{p^3 \mathbb{Z}_p}$, and hence $S(p) \equiv 0 \pmod{p^3}$ in $\mathbb{Z}_{(p)}$. $\square$

---

## 4. Inert Primes $p \equiv 3, 5, 6 \pmod 7$ (`conjecture_1`)

For each integer $m \ge 0$, define the $m$-th Legendre polynomial by
$$P_m(x) := \sum_{k=0}^m \binom{m}{k}\binom{m+k}{k}\left(\frac{x - 1}{2}\right)^k \in \mathbb{Q}[x].$$

### Lemma 4.1 (Finite Clausen Identity)
*For every integer $m \ge 0$, the polynomial identity*
$$P_m(1 - 2u)^2 = \sum_{k=0}^m (-1)^k \binom{m + k}{2k} \binom{2k}{k}^2 \bigl(u(1 - u)\bigr)^k \tag{4.1}$$
*holds in $\mathbb{Q}[u]$.*

*Proof.* First observe that $P_m(1) = 1$ and $P_m(x)$ satisfies Legendre's differential equation $(1 - x^2)P_m''(x) - 2x P_m'(x) + m(m + 1)P_m(x) = 0$: indeed, writing $w = \frac{1 - x}{2}$ gives $P_m(1 - 2w) = \sum_{k=0}^m c_k w^k$ with $c_k = (-1)^k \binom{m}{k}\binom{m+k}{k}$, whose coefficients satisfy $(k+1)^2 c_{k+1} = (k(k+1) - m(m+1))c_k$ for all $k \ge 0$, equivalent to $w(1-w)\frac{d^2 P}{dw^2} + (1-2w)\frac{dP}{dw} + m(m+1)P = 0$; changing back via $x = 1 - 2w$ yields Legendre's equation.

Work in the formal power series ring $\mathbb{Q}\llbracket z \rrbracket$, where $x(z) := (1 - z)^{1/2} = \sum_{n=0}^\infty \binom{1/2}{n}(-z)^n \in 1 + z\mathbb{Q}\llbracket z \rrbracket$ satisfies $x^2 = 1 - z$ and $x' = -\frac{1}{2x}$ (denoting ${}' = \frac{d}{dz}$). Set $y(z) := P_m(x(z)) \in 1 + z\mathbb{Q}\llbracket z \rrbracket$ and $Y(z) := y(z)^2 \in 1 + z\mathbb{Q}\llbracket z \rrbracket$. By the chain rule, $P_m'(x) = -2x y'$ and $P_m''(x) = 4(1 - z)y'' - 2y'$, so Legendre's equation transforms into
$$z(1 - z)y'' + \left(1 - \frac{3}{2}z\right)y' + \frac{m(m+1)}{4}y = 0. \tag{4.2}$$
Define $A := z(1 - z)Y'' + \bigl(1 - \frac{3}{2}z\bigr)Y' + \frac{m(m+1)}{2}Y$. Substituting $Y = y^2$, $Y' = 2yy'$, $Y'' = 2yy'' + 2(y')^2$ and using (4.2) gives
$$A = 2z(1 - z)(y')^2. \tag{4.3}$$
Differentiating (4.3) and substituting $4z(1-z)y'' = -(4 - 6z)y' - m(m+1)y$ from (4.2) yields
$$A' = 2(1 - 2z)(y')^2 + 4z(1 - z)y' y'' = -2(1 - z)(y')^2 - \frac{m(m+1)}{2}Y'.$$
Multiplying by $z$ and using (4.3) to replace $2z(1 - z)(y')^2$ by $A$ gives
$$z A' + A + \frac{m(m+1)}{2} z Y' = 0. \tag{4.4}$$
Let $\theta := z\frac{d}{dz}$, so $z^2 Y'' = \theta(\theta - 1)Y$, $z(z A' + A) = \theta(z A)$, and $\theta(z f) = z(\theta + 1)f$. Multiplying the definition of $A$ by $z$ gives
$$z A = \theta^2 Y - z\left(\theta^2 + \frac{1}{2}\theta - \frac{m(m+1)}{2}\right)Y,$$
so multiplying (4.4) by $z$ yields
$$\theta^3 Y - z\left((\theta + 1)\left(\theta^2 + \frac{1}{2}\theta - \frac{m(m+1)}{2}\right) - \frac{m(m+1)}{2}\theta\right)Y = 0.$$
Since $(t + 1)\bigl(t^2 + \frac{1}{2}t - \frac{m(m+1)}{2}\bigr) - \frac{m(m+1)}{2}t = (t - m)(t + m + 1)\bigl(t + \frac{1}{2}\bigr)$ identically in $t$, we obtain
$$\theta^3 Y = z(\theta - m)(\theta + m + 1)\left(\theta + \frac{1}{2}\right)Y. \tag{4.5}$$
Expanding $Y(z) = \sum_{k=0}^\infty d_k z^k$ with $d_0 = Y(0) = P_m(1)^2 = 1$, comparing the coefficient of $z^k$ ($k \ge 1$) in (4.5) gives
$$k^3 d_k = (k - 1 - m)(k + m)\left(k - \frac{1}{2}\right) d_{k-1} \qquad (k \ge 1).$$
By induction, $d_k = 0$ for $k > m$, while for $0 \le k \le m$ (using Pochhammer symbols $(a)_k = a(a+1)\cdots(a+k-1)$):
$$d_k = \frac{(-m)_k (m+1)_k (1/2)_k}{(k!)^3} = \frac{(-1)^k (2k)!\binom{m+k}{2k} \cdot \frac{(2k)!}{4^k k!}}{(k!)^3} = \frac{(-1)^k}{4^k} \binom{m+k}{2k}\binom{2k}{k}^2.$$
Hence $P_m((1 - z)^{1/2})^2 = \sum_{k=0}^m (-1)^k \binom{m+k}{2k}\binom{2k}{k}^2 (z/4)^k$ in $\mathbb{Q}\llbracket z \rrbracket$. Finally, substitute $z = 4u(1 - u) \in u\mathbb{Q}\llbracket u \rrbracket$: since $1 - 4u(1-u) = (1 - 2u)^2$ and $1 - 2u \in 1 + u\mathbb{Q}\llbracket u \rrbracket$ is the unique formal square root of $1 - z$ with constant term $1$, we have $x(4u(1-u)) = 1 - 2u$, yielding (4.1) in $\mathbb{Q}\llbracket u \rrbracket$ and hence in $\mathbb{Q}[u]$. $\square$

*(Remark: Equivalent forms of (4.1) via Gould's identity appear in Z.-H. Sun [5, Lemma 3.2].)*

### Lemma 4.2 (Polynomial congruences modulo $p^2$ and $p$)
*Let $p$ be any odd prime and set $m := \frac{p-1}{2}$. Define $H_p(u) := \sum_{k=0}^m \binom{m}{k}^2 u^k \in \mathbb{Z}[u]$. Then:*
1. $F_p\!\left(\frac{u(1-u)}{16}\right) \equiv P_m(1 - 2u)^2 \pmod{p^2 \mathbb{Z}_p[u]}$.
2. $P_m(1 - 2u) \equiv H_p(u) \pmod{p \mathbb{Z}_p[u]}$.

*Proof.*
1. For $m < k \le p - 1$, we have $k < p < 2k$, so $p \nmid k!$ and $p \mid (2k)!$, hence $p \mid \binom{2k}{k}$ and $p^3 \mid \binom{2k}{k}^3$. Since $16 \in \mathbb{Z}_p^\times$, dropping the terms $k > m$ leaves
   $$F_p\!\left(\frac{u(1-u)}{16}\right) \equiv \sum_{k=0}^m \frac{\binom{2k}{k}}{16^k} \binom{2k}{k}^2 \bigl(u(1-u)\bigr)^k \pmod{p^3 \mathbb{Z}_p[u]}.$$
   For $0 \le k \le m$, we have $2k \le p - 1 < p$, so $(2k)! \in \mathbb{Z}_p^\times$, and using $m - j = \frac{p}{2} - (j + \frac{1}{2})$ and $m + 1 + j = \frac{p}{2} + (j + \frac{1}{2})$ we compute in $\mathbb{Z}_p$:
   $$(-1)^k \binom{m+k}{2k} = \frac{(-1)^k}{(2k)!} \prod_{j=0}^{k-1} (m - j)(m + 1 + j) = \frac{1}{(2k)!} \prod_{j=0}^{k-1} \left(\left(j + \frac{1}{2}\right)^2 - \frac{p^2}{4}\right) \equiv \frac{((1/2)_k)^2}{(2k)!} = \frac{\binom{2k}{k}}{16^k} \pmod{p^2 \mathbb{Z}_p},$$
   where the last equality uses $(1/2)_k = \frac{(2k)!}{4^k k!}$. Substituting this congruence into Lemma 4.1 gives (1).

2. Since $P_m(1 - 2u) = \sum_{k=0}^m (-1)^k \binom{m}{k}\binom{m+k}{k} u^k$, and for $0 \le k \le m$ we have $k! \in \mathbb{Z}_p^\times$ and $m + 1 + j = p - (m - j) \equiv -(m - j) \pmod p$ for $0 \le j \le k - 1$, it follows that
   $$(-1)^k \binom{m+k}{k} = \frac{(-1)^k}{k!} \prod_{j=0}^{k-1} (m + 1 + j) \equiv \frac{1}{k!} \prod_{j=0}^{k-1} (m - j) = \binom{m}{k} \pmod{p\mathbb{Z}_p},$$
   which gives $P_m(1 - 2u) \equiv \sum_{k=0}^m \binom{m}{k}^2 u^k = H_p(u) \pmod{p\mathbb{Z}_p[u]}$. $\square$

### Proposition 4.3 (Proof of `conjecture_1` for inert primes)
*For every odd prime $p \equiv 3, 5, 6 \pmod 7$, $S(p) \equiv 0 \pmod{p^2}$ in $\mathbb{Z}_{(p)}$.*

*Proof.* Since $p$ is odd and $p \equiv 3, 5, 6 \pmod 7$ is a quadratic nonresidue modulo $7$, quadratic reciprocity gives $\bigl(\frac{-7}{p}\bigr) = \bigl(\frac{p}{7}\bigr) = -1$, so $p$ is **inert** in $K = \mathbb{Q}(\sqrt{-7})$. Thus $\mathfrak{p} := p\mathcal{O}_K$ is a prime ideal of $\mathcal{O}_K$ with residue field $\mathcal{O}_K / \mathfrak{p} \cong \mathbb{F}_{p^2}$. Let $\mathcal{O}_{K,\mathfrak{p}}$ be the localization of $\mathcal{O}_K$ at $\mathfrak{p}$; since $p$ is odd, $\mathcal{O}_K[\frac{1}{2}] \subset \mathcal{O}_{K,\mathfrak{p}}$.

Define
$$u_1 := \frac{1 + 3s}{32} \in \mathcal{O}_K\!\left[\tfrac{1}{2}\right], \qquad 1 - u_1 = \frac{31 - 3s}{32} \in \mathcal{O}_K\!\left[\tfrac{1}{2}\right].$$
Direct computation in $K$ gives
$$u_1(1 - u_1) = \frac{(1 + 3s)(31 - 3s)}{1024} = \frac{31 + 90s + 63}{1024} = \frac{47 + 45s}{512} = 16\, t_1, \tag{4.6}$$
so $\frac{u_1(1 - u_1)}{16} = t_1$, and norms
$$N_{K/\mathbb{Q}}(u_1) = \frac{1^2 + 7 \cdot 3^2}{32^2} = \frac{64}{1024} = \frac{1}{16}, \qquad N_{K/\mathbb{Q}}(1 - u_1) = \frac{31^2 + 7 \cdot 3^2}{32^2} = \frac{1024}{1024} = 1.$$
Because $p$ is odd, both $N_{K/\mathbb{Q}}(u_1)$ and $N_{K/\mathbb{Q}}(1 - u_1)$ lie in $\mathbb{Z}_p^\times$, which forces $u_1, 1 - u_1 \in \mathcal{O}_{K,\mathfrak{p}}^\times$.

Consider the Legendre elliptic curve over $K$:
$$E_{u_1} : y^2 = x(x - 1)(x - u_1).$$
Its Weierstrass discriminant is $\Delta(E_{u_1}) = 16 u_1^2 (1 - u_1)^2 \in \mathcal{O}_{K,\mathfrak{p}}^\times$ (in fact $N_{K/\mathbb{Q}}(\Delta(E_{u_1})) = 2^8 \cdot 2^{-8} \cdot 1 = 1$), so $E_{u_1}$ has **good reduction** at $\mathfrak{p}$ for *every* odd inert prime $p$ (including $p = 3$ and $p = 5$), with smooth Legendre reduction $\widetilde{E}_{u_1} : y^2 = x(x - 1)(x - \bar u_1)$ over $\mathbb{F}_{p^2}$ ($\bar u_1 := u_1 \bmod \mathfrak{p} \notin \{0, 1\}$).

By the Legendre $j$-invariant formula [4, Ch. III, Proposition 1.7] together with (4.6) and (2.2),
$$j(E_{u_1}) = 256\,\frac{(u_1^2 - u_1 + 1)^3}{u_1^2(u_1 - 1)^2} = 256\,\frac{\bigl(1 - u_1(1 - u_1)\bigr)^3}{\bigl(u_1(1 - u_1)\bigr)^2} = \frac{(1 - 16 t_1)^3}{t_1^2} = -15^3 = -3375 = j\!\left(\frac{1 + \sqrt{-7}}{2}\right).$$
Therefore $E_{u_1} \cong_{\mathbb{C}} \mathbb{C}/\mathcal{O}_K$, so $E_{u_1}$ has complex multiplication by the maximal order $\mathcal{O}_K$ (moreover, since $K$ contains the CM field, all endomorphisms of $E_{u_1}$ are defined over $K$). Because $p$ is inert in $K$ and $E_{u_1}$ has good reduction at $\mathfrak{p}$, **Deuring's criterion** [3, Ch. 13, §4, Theorem 12] implies that the reduced curve $\widetilde{E}_{u_1}$ over $\mathbb{F}_{p^2}$ is **supersingular**.

By [4, Ch. V, Theorem 4.1] (valid in every odd characteristic $p \ge 3$), the Legendre curve $\widetilde{E}_{u_1}$ over $\mathbb{F}_{p^2}$ is supersingular if and only if the coefficient of $x^{p-1}$ in $\bigl(x(x - 1)(x - \bar u_1)\bigr)^m$ ($m = \frac{p-1}{2}$) vanishes. Expanding directly gives
$$[x^{2m}]\, x^m (x - 1)^m (x - \lambda)^m = [x^m]\,(x - 1)^m (x - \lambda)^m = \sum_{k=0}^m \binom{m}{k}(-1)^{m-k}\binom{m}{m-k}(-\lambda)^k = (-1)^m H_p(\lambda).$$
Hence $H_p(\bar u_1) = 0$ in $\mathcal{O}_K / \mathfrak{p}$, i.e., $H_p(u_1) \in p\mathcal{O}_{K,\mathfrak{p}}$.

Evaluating Lemma 4.2(2) at $u = u_1 \in \mathcal{O}_{K,\mathfrak{p}}$ yields $P_m(1 - 2u_1) \equiv H_p(u_1) \equiv 0 \pmod{p\mathcal{O}_{K,\mathfrak{p}}}$, so squaring gives $P_m(1 - 2u_1)^2 \in p^2 \mathcal{O}_{K,\mathfrak{p}}$. Evaluating Lemma 4.2(1) at $u = u_1$ and using $\frac{u_1(1 - u_1)}{16} = t_1$ then yields
$$F_p(t_1) = F_p\!\left(\frac{u_1(1 - u_1)}{16}\right) \equiv P_m(1 - 2u_1)^2 \equiv 0 \pmod{p^2 \mathcal{O}_{K,\mathfrak{p}}}.$$
Applying the nontrivial Galois automorphism $s \mapsto -s$ of $K/\mathbb{Q}$ (which preserves $\mathcal{O}_{K,\mathfrak{p}}$ and $p^2\mathcal{O}_{K,\mathfrak{p}}$ and sends $t_1 \mapsto t_2$) gives $F_p(t_2) \in p^2 \mathcal{O}_{K,\mathfrak{p}}$ as well. By (2.1),
$$s \cdot S(p) = F_p(t_2) - F_p(t_1) \in p^2 \mathcal{O}_{K,\mathfrak{p}}.$$
Since $p \neq 7$, we have $N_{K/\mathbb{Q}}(s) = 7 \in \mathbb{Z}_p^\times$, so $s \in \mathcal{O}_{K,\mathfrak{p}}^\times$, whence $S(p) \in p^2 \mathcal{O}_{K,\mathfrak{p}}$. Finally, because $S(p) \in \mathbb{Q}$ and $p^2 \mathcal{O}_{K,\mathfrak{p}} \cap \mathbb{Q} = p^2 \mathbb{Z}_{(p)}$ (as $\mathcal{O}_K = \mathbb{Z} \oplus \mathbb{Z}\omega$ implies $p\mathcal{O}_{K,\mathfrak{p}} \cap \mathbb{Z} = p\mathbb{Z}$), we conclude $S(p) \equiv 0 \pmod{p^2}$ in $\mathbb{Z}_{(p)}$. $\square$

---

## 5. Ramified Prime $p = 7$

For $p = 7$, we verify $S(7) \equiv 0 \pmod{49}$ directly. Since $-4096 \equiv 20 \pmod{49}$ and $20 \cdot 27 = 540 = 11 \cdot 49 + 1$, we have $(-4096)^{-1} \equiv 27 \pmod{49}$. Moreover, $\alpha^4 + \beta^4 = -47$ and $\alpha^4\beta^4 = 4096$, so $a(4k)$ satisfies $a(4(k+2)) = -47 a(4(k+1)) - 4096 a(4k)$ with $a(0) = 0$ and $a(4) = 45$. Computing the seven terms $T_k := a(4k)\binom{2k}{k}^3 (-4096)^{-k} \pmod{49}$:
- $k = 0$: $a(0) = 0 \implies T_0 \equiv 0 \pmod{49}$.
- $k = 1$: $a(4) = 45 \equiv -4$, $\binom{2}{1}^3 = 8$, $(-4096)^{-1} \equiv 27 \implies T_1 \equiv (-4) \cdot 8 \cdot 27 = -864 \equiv 18 \pmod{49}$.
- $k = 2$: $a(8) = -2115 \equiv 41 \equiv -8$, $\binom{4}{2}^3 = 216 \equiv 20$, $27^2 = 729 \equiv 43 \equiv -6 \implies T_2 \equiv (-8) \cdot 20 \cdot (-6) = 960 \equiv 29 \pmod{49}$.
- $k = 3$: $a(12) = -84915 \equiv 2$, $\binom{6}{3} = 20 \equiv -4096$, so $\binom{6}{3}^3 (-4096)^{-3} \equiv 1 \implies T_3 \equiv 2 \cdot 1 = 2 \pmod{49}$.
- $k = 4, 5, 6$: $\binom{8}{4} = 70$, $\binom{10}{5} = 252$, $\binom{12}{6} = 924$ are all divisible by $7$, so $7^3 \mid \binom{2k}{k}^3$ and hence $T_4 \equiv T_5 \equiv T_6 \equiv 0 \pmod{49}$.

Summing gives
$$S(7) \equiv 0 + 18 + 29 + 2 + 0 + 0 + 0 = 49 \equiv 0 \pmod{49}.$$
(Exact arithmetic further gives $S(7) \equiv 294 = 6 \cdot 7^2 \pmod{7^3}$, confirming that $p = 7$ satisfies `conjecture_1` and not the $\bmod p^3$ congruence.)

---

## 6. Completion of the Proof

Every odd prime $p$ falls into one of three exhaustive cases modulo $7$:
- $p \equiv 1, 2, 4 \pmod 7$: by Proposition 3.3, $S(p) \equiv 0 \pmod{p^3}$ (proving `conjecture_2` and a fortiori `conjecture_1`);
- $p \equiv 3, 5, 6 \pmod 7$: by Proposition 4.3, $S(p) \equiv 0 \pmod{p^2}$;
- $p = 7$: by Section 5, $S(7) \equiv 0 \pmod{7^2}$.

Thus both `conjecture_1` and `conjecture_2` of OEIS `A190969` are completely proved. $\blacksquare$

---

## References

1. F. Beukers, *Supercongruences using modular forms*, Algebra & Number Theory **20** (2026), no. 9, 1727–1768 (preprint `arXiv:2403.03301v3`; Theorem 1.15, Remark 1.14, and Appendix C).
2. D. A. Cox, *Primes of the Form $x^2 + ny^2$: Fermat, Class Field Theory, and Complex Multiplication*, 2nd ed., Wiley, 2013.
3. S. Lang, *Elliptic Functions*, 2nd ed., Graduate Texts in Mathematics **112**, Springer, 1987 (Ch. 13, §4, Theorem 12).
4. J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Graduate Texts in Mathematics **106**, Springer, 2009 (Ch. III, Proposition 1.7; Ch. V, Theorem 4.1).
5. Z.-H. Sun, *Congruences concerning Legendre polynomials II*, J. Number Theory **133** (2013), no. 6, 1950–1976 (`arXiv:1012.3898v2`).
