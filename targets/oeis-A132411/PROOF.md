# Proof of OEIS A132411 Peter Bala (2025) $q$-Series Expansion Conjecture

## Theorem
In the formal power series ring $\mathbb{Z}[[q]]$,
$$
F(q) := \sum_{n \ge 0} q^{2n} \prod_{k \ge 2n+2} \bigl(1 - (-q)^k\bigr) = 1 + \sum_{m \ge 2} q^{m^2 - 1} = 1 + q^3 + q^8 + q^{15} + q^{24} + \cdots.
$$
Consequently, every exponent appearing in $F(q)$ is a term of `A132411` ($a(0)=0, a(1)=1, a(m)=m^2-1$ for $m \ge 2$), and every term of `A132411` except $a(1) = 1$ occurs as an exponent in $F(q)$ (each with coefficient $1$), matching the displayed expansion $1 + q^3 + q^8 + q^{15} + q^{24} + \dots$.

## Proof

### Step 1: Reduction via Euler's identity
Substitute $x := -q$, so $x^{2n} = q^{2n}$ and $(-q)^k = x^k$. Using the standard $q$-Pochhammer notation $(u; x)_r := \prod_{j=0}^{r-1} (1 - u x^j)$ and $(u; x)_\infty := \prod_{j \ge 0} (1 - u x^j)$, every $(1 - x^k)$ ($k \ge 1$) is a unit in $\mathbb{Z}[[x]]$, so
$$
F(q) = \sum_{n \ge 0} x^{2n} \prod_{k \ge 2n+2} (1 - x^k) = (x; x)_\infty \sum_{n \ge 0} \frac{x^{2n}}{(x; x)_{2n+1}} \quad \text{in } \mathbb{Z}[[x]].
$$
Multiplying by $x$ gives
$$
x\, F(q) = (x; x)_\infty \sum_{n \ge 0} \frac{x^{2n+1}}{(x; x)_{2n+1}}.
$$
Consider $E(t) := \sum_{r \ge 0} \frac{t^r}{(x; x)_r} \in \mathbb{Q}[[x]][[t]]$. Since
$$
E(t) - E(tx) = \sum_{r \ge 1} \frac{t^r (1 - x^r)}{(x; x)_r} = t \sum_{r \ge 1} \frac{t^{r-1}}{(x; x)_{r-1}} = t\, E(t),
$$
we have $(1 - t) E(t) = E(tx)$, and iterating $N$ times gives $E(t) = \frac{E(tx^N)}{(t; x)_N}$. Since $E(0) = 1$ and $tx^N \to 0$ $(x, t)$-adically, $E(t) = \frac{1}{(t; x)_\infty}$ in $\mathbb{Q}[[x, t]]$. Specializing $t = x$ and $t = -x$ (both in $x\mathbb{Z}[[x]]$) and subtracting cancels all even-$r$ terms:
$$
\sum_{n \ge 0} \frac{x^{2n+1}}{(x; x)_{2n+1}} = \frac{E(x) - E(-x)}{2} = \frac{1}{2}\left(\frac{1}{(x; x)_\infty} - \frac{1}{(-x; x)_\infty}\right),
$$
hence in $\mathbb{Q}[[x]]$ (and $\mathbb{Z}[[x]]$):
$$
x\, F(q) = \frac{1}{2}\left(1 - \frac{(x; x)_\infty}{(-x; x)_\infty}\right).
$$

### Step 2: Elementary finite proof of Gauss's theta identity
For each integer $N \ge 1$, define the Laurent polynomial in $z$ with coefficients in $\mathbb{Z}[x]$:
$$
P_N(z) := \prod_{k=1}^{N} \bigl(1 + z x^{2k-1}\bigr)\bigl(1 + z^{-1} x^{2k-1}\bigr) = \sum_{m=-N}^{N} c_{N, m}(x)\, z^m.
$$
Replacing $z$ by $z x^2$ shifts the product to give
$$
(x^{2N} + z x)\, P_N(z x^2) = (1 + z x^{2N+1})\, P_N(z).
$$
Comparing coefficients of $z^m$ on both sides yields $x^{2N + 2m} c_{N, m} + x^{2m-1} c_{N, m-1} = c_{N, m} + x^{2N+1} c_{N, m-1}$, i.e.,
$$
(1 - x^{2N + 2m}) c_{N, m} = x^{2m-1} (1 - x^{2N - 2m + 2}) c_{N, m-1} \qquad (-N < m \le N).
$$
Since the highest $z$-term of $P_N(z)$ is $\prod_{k=1}^N z x^{2k-1} = z^N x^{N^2}$, we have $c_{N, N} = x^{N^2}$, and backward induction on $m$ gives for all $-N \le m \le N$:
$$
c_{N, m} = \frac{(x^2; x^2)_{2N}}{(x^2; x^2)_{N+m}\, (x^2; x^2)_{N-m}}\, x^{m^2}.
$$
Multiplying $P_N(-1)$ by $(x^2; x^2)_N$ yields the finite polynomial identity
$$
\prod_{k=1}^{N} (1 - x^{2k})(1 - x^{2k-1})^2 = \sum_{m=-N}^{N} \frac{(x^2; x^2)_N\, (x^2; x^2)_{2N}}{(x^2; x^2)_{N+m}\, (x^2; x^2)_{N-m}}\, (-1)^m x^{m^2}.
$$
For any fixed integer $m$ and $N \ge |m|$, both quotients $\frac{(x^2; x^2)_{2N}}{(x^2; x^2)_{N+m}}$ and $\frac{(x^2; x^2)_N}{(x^2; x^2)_{N-m}}$ lie in $1 + x^{2(N - |m| + 1)}\mathbb{Z}[[x]]$, so letting $N \to \infty$ in the $x$-adic topology of $\mathbb{Z}[[x]]$ gives
$$
\prod_{k=1}^{\infty} (1 - x^{2k})(1 - x^{2k-1})^2 = \sum_{m=-\infty}^{\infty} (-1)^m x^{m^2} = 1 + 2\sum_{m \ge 1} (-1)^m x^{m^2}.
$$
On the other hand, using $(x^2; x^2)_\infty = (x; x)_\infty (-x; x)_\infty$ and $(x; x)_\infty = \prod_{k \ge 1} (1 - x^{2k})(1 - x^{2k-1})$, the left-hand side equals
$$
\prod_{k \ge 1} (1 - x^{2k})(1 - x^{2k-1}) \cdot \frac{(x; x)_\infty}{(x^2; x^2)_\infty} = \frac{(x; x)_\infty}{(-x; x)_\infty}.
$$

### Step 3: Exact evaluation of $F(q)$
Substituting $\frac{(x; x)_\infty}{(-x; x)_\infty} = 1 + 2\sum_{m \ge 1} (-1)^m x^{m^2}$ into Step 1 gives
$$
x\, F(q) = \frac{1}{2}\left(1 - \Bigl(1 + 2\sum_{m \ge 1} (-1)^m x^{m^2}\Bigr)\right) = \sum_{m \ge 1} (-1)^{m-1} x^{m^2}.
$$
Dividing by $x = -q$ and noting $(-1)^{m-1} (-1)^{m^2-1} = (-1)^{m(m+1)} = +1$ for all $m \ge 1$ yields
$$
F(q) = \sum_{m \ge 1} (-1)^{m-1} (-q)^{m^2 - 1} = \sum_{m \ge 1} q^{m^2 - 1} = 1 + \sum_{m \ge 2} q^{m^2 - 1} = 1 + q^3 + q^8 + q^{15} + q^{24} + \cdots
$$
in $\mathbb{Z}[[q]]$. $\blacksquare$
