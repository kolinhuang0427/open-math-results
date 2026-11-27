# Proof of Otmani Remark 3.1 (arXiv:2608.14453v2)

## Theorem
Let $p > 3$ be a prime, and let $(\mathcal{P}_k)_{k \ge 0}$ be the Catalan–Larcombe–French numbers, given by $\mathcal{P}_0 = 1$, $\mathcal{P}_1 = 8$, and equivalently by
$$\mathcal{P}_k = \sum_{j=0}^{k} \frac{\binom{2j}{j}^2 \binom{2k-2j}{k-j}^2}{\binom{k}{j}} = 2^k \sum_{m=0}^{\lfloor k/2 \rfloor} \binom{k}{2m} \binom{2m}{m}^2 4^{k-2m} \qquad (k \ge 0),$$
and satisfying the recurrence $k^2 \mathcal{P}_k = 8(3k^2-3k+1)\mathcal{P}_{k-1} - 128(k-1)^2 \mathcal{P}_{k-2}$ for all $k \ge 2$. Then
$$\sum_{k=0}^{p-1} \frac{\mathcal{P}_k^2}{128^k} \equiv \left(\frac{-1}{p}\right) \sum_{k=0}^{p-1} \binom{2k}{k}^4 \frac{1}{256^k} \pmod{p^3}.$$

---

## Proof

Fix a prime $p > 3$, and set
$$n := \frac{p-1}{2} \ge 2, \qquad \varepsilon := \left(\frac{-1}{p}\right) = (-1)^n \in \{1, -1\}.$$
All congruences are taken in the localization $\mathbb{Z}_{(p)}$ of rationals with denominator coprime to $p$. Define
$$c_m := \frac{\binom{2m}{m}^2}{16^m} \quad (m \ge 0), \qquad v_i := \frac{\mathcal{P}_i}{16^i} \quad (i \ge 0),$$
$$B_m := \sum_{i=2m}^{p-1} v_i \binom{i}{2m} \quad (0 \le m \le n), \qquad E_p(m) := c_m - \varepsilon B_m \quad (0 \le m \le n).$$

### Lemma 1 (Reduction to $E_p(m)$ and symmetry of $c_m$)
1. $\sum_{k=0}^{p-1} \frac{\mathcal{P}_k^2}{128^k} = \sum_{m=0}^n c_m B_m$.
2. $\sum_{k=0}^{p-1} \frac{\binom{2k}{k}^4}{256^k} \equiv \sum_{m=0}^n c_m^2 \pmod{p^4}$.
3. Remark 3.1 is equivalent to $\sum_{m=0}^n c_m E_p(m) \equiv 0 \pmod{p^3}$.
4. For $0 \le m \le n$, $c_m \equiv \binom{n}{m}^2 \pmod{p}$, and hence $c_m \equiv c_{n-m} \pmod{p}$ and $c_n \equiv 1 \pmod{p}$.

**Proof.**
For (1), rewrite $\mathcal{P}_k = 8^k \sum_{m=0}^{\lfloor k/2 \rfloor} \binom{k}{2m} c_m$. Since $\frac{8^k}{128^k} = \frac{1}{16^k}$ and $\lfloor (p-1)/2 \rfloor = n$, swapping sums gives
$$\sum_{k=0}^{p-1} \frac{\mathcal{P}_k^2}{128^k} = \sum_{k=0}^{p-1} v_k \sum_{m=0}^{\lfloor k/2 \rfloor} \binom{k}{2m} c_m = \sum_{m=0}^n c_m \sum_{k=2m}^{p-1} v_k \binom{k}{2m} = \sum_{m=0}^n c_m B_m.$$
For (2), if $n < k \le p-1$, then $p < 2k < 2p$, so $p \mid \binom{2k}{k}$ and $p^4 \mid \binom{2k}{k}^4$, while $p \nmid 256^k$. Truncating at $k = n$ leaves $\sum_{m=0}^n c_m^2 \pmod{p^4}$.
Part (3) follows from (1), (2), and $\sum_{m=0}^n c_m(c_m - \varepsilon B_m) = \sum_{m=0}^n c_m E_p(m)$.
For (4), since $2n \equiv -1 \pmod{p}$, we have for $0 \le m \le n$:
$$\frac{\binom{2m}{m}}{(-4)^m} = \binom{-1/2}{m} = \frac{\prod_{j=0}^{m-1}(-1/2 - j)}{m!} \equiv \frac{\prod_{j=0}^{m-1}(n - j)}{m!} = \binom{n}{m} \pmod{p}.$$
Squaring and using $(-4)^{2m} = 16^m$ yields $c_m \equiv \binom{n}{m}^2 \pmod{p}$, whence $c_m \equiv c_{n-m} \pmod{p}$ and $c_n \equiv \binom{n}{n}^2 = 1 \pmod{p}$. $\square$

---

### Lemma 2 (Wolstenholme $H_n^{(2)}$ and Morley's congruence)
Let $H_n := \sum_{k=1}^n \frac{1}{k}$ and $H_n^{(2)} := \sum_{k=1}^n \frac{1}{k^2}$. Then:
1. $H_n^{(2)} \equiv 0 \pmod{p}$.
2. $\binom{p-1}{n} = \binom{2n}{n} \equiv \varepsilon 4^{p-1} \pmod{p^3}$.

**Proof.**
For (1), since $p > 3$, $4 \not\equiv 1 \pmod{p}$. As $k \mapsto 2k \pmod{p}$ permutes $\{1, \dots, p-1\}$, we have $\sum_{k=1}^{p-1} k^{-2} \equiv \sum_{k=1}^{p-1} (2k)^{-2} = \frac{1}{4}\sum_{k=1}^{p-1} k^{-2} \pmod{p}$, so $\sum_{k=1}^{p-1} k^{-2} \equiv 0 \pmod{p}$. Pairing $k$ with $p-k$ gives $2 H_n^{(2)} \equiv \sum_{k=1}^{p-1} k^{-2} \equiv 0 \pmod{p}$, hence $H_n^{(2)} \equiv 0 \pmod{p}$.

For (2), set $X := p H_n$ and $Y := 2^{p-1} - 1$; note $p \mid X$ and $p \mid Y$ by Fermat's Little Theorem. Expanding two exact expressions for $\binom{p-1}{n} = \binom{2n}{n}$ modulo $p^3$ using $H_n^{(2)} \equiv 0 \pmod{p}$:
- First,
  $$\binom{p-1}{n} = \frac{\prod_{k=1}^n (p-k)}{n!} = (-1)^n \prod_{k=1}^n \left(1 - \frac{p}{k}\right) \equiv \varepsilon \left(1 - X + \frac{X^2 - p^2 H_n^{(2)}}{2}\right) \equiv \varepsilon\left(1 - X + \frac{1}{2}X^2\right) \pmod{p^3}.$$
- Second, $\{p - 2k : 1 \le k \le n\} = \{1, 3, \dots, 2n-1\}$, so
  $$\binom{2n}{n} = \frac{(2n)!}{(n!)^2} = \frac{2^n}{n!} \prod_{k=1}^n (2k-1) = \frac{2^n}{n!} \prod_{k=1}^n (p - 2k) = (-1)^n 4^n \prod_{k=1}^n \left(1 - \frac{p}{2k}\right) \equiv \varepsilon (1+Y)\left(1 - \frac{1}{2}X + \frac{1}{8}X^2\right) \pmod{p^3}.$$

Equating these two congruences modulo $p^2$ gives $1 - X \equiv 1 + Y - \frac{1}{2}X \pmod{p^2}$, so $X \equiv -2Y \pmod{p^2}$. Therefore $X^2 \equiv 4Y^2 \pmod{p^3}$ and $XY \equiv -2Y^2 \pmod{p^3}$. Substituting these into the equality modulo $p^3$ gives
$$1 - X + 2Y^2 \equiv 1 + Y - \frac{1}{2}X - \frac{1}{2}XY + \frac{1}{8}X^2 \equiv 1 + Y - \frac{1}{2}X + \frac{3}{2}Y^2 \pmod{p^3},$$
so $\frac{1}{2}X \equiv -Y + \frac{1}{2}Y^2 \pmod{p^3}$, i.e., $X \equiv -2Y + Y^2 \pmod{p^3}$. Plugging this back into the first congruence yields
$$\binom{p-1}{n} \equiv \varepsilon\big(1 - (-2Y + Y^2) + 2Y^2\big) = \varepsilon (1+Y)^2 = \varepsilon 4^{p-1} \pmod{p^3}. \quad \square$$

---

### Lemma 3 (Tail binomial congruence, $v_p$, $v_{p-1}$, and $E_p(n) \pmod{p^3}$)
1. $v_p \equiv \frac{1}{2} \pmod{p}$.
2. For every $j \in \{n+1, \dots, p-1\}$, putting $r = p - j \in \{1, \dots, n\}$, we have
   $$\frac{1}{p}\binom{2j}{j} \equiv -\frac{2}{r \binom{2r}{r}} \pmod{p}.$$
3. $v_{p-1} \equiv \varepsilon \pmod{p}$, $p^2 \mid E_p(n)$, and
   $$\tilde{E}_n := \varepsilon \frac{E_p(n)}{p^2} \equiv -\frac{1}{2}\varepsilon \sum_{t=1}^n \frac{(-1)^t}{t^2} \pmod{p}.$$

**Proof.**
For (1), $\mathcal{P}_p = 8^p \sum_{k=0}^n \binom{p}{2k} c_k$. Since $p \mid \binom{p}{2k}$ for $1 \le k \le n$ and $c_0 = 1$, $\mathcal{P}_p \equiv 8^p \pmod{p}$, so $v_p = \frac{\mathcal{P}_p}{16^p} \equiv \frac{1}{2^p} \equiv \frac{1}{2} \pmod{p}$.

For (2), with $j = p - r$ and $2j - p = p - 2r \ge 1$,
$$\frac{1}{p}\binom{2j}{j} = \frac{(p-1)! \prod_{i=1}^{p-2r}(p+i)}{(j!)^2} \equiv \frac{(p-1)! \, (p-2r)!}{(j!)^2} \pmod{p}.$$
Using $(p-1)! \equiv -1 \pmod{p}$, $j! = \frac{(p-1)!}{\prod_{s=1}^{r-1}(p-s)} \equiv \frac{(-1)^r}{(r-1)!} \pmod{p}$, and $(p-2r)! = \frac{(p-1)!}{\prod_{s=1}^{2r-1}(p-s)} \equiv \frac{1}{(2r-1)!} \pmod{p}$, we obtain
$$\frac{1}{p}\binom{2j}{j} \equiv -\frac{((r-1)!)^2}{(2r-1)!} = -\frac{2(r!)^2}{r (2r)!} = -\frac{2}{r \binom{2r}{r}} \pmod{p}.$$

For (3), use the definition $\mathcal{P}_{p-1} = \sum_{j=0}^{p-1} \frac{\binom{2j}{j}^2 \binom{2(p-1-j)}{p-1-j}^2}{\binom{p-1}{j}}$ and divide by $16^{p-1} = 16^{2n}$. Pairing $j \leftrightarrow p-1-j$ around $j = n$ writes $v_{p-1} = T_{\mathrm{mid}} + T_{\mathrm{tail}}$, where
$$T_{\mathrm{mid}} = \frac{c_n^2}{\binom{p-1}{n}}, \qquad T_{\mathrm{tail}} = 2 \sum_{j=n+1}^{p-1} \frac{\binom{2j}{j}^2 \binom{2m}{m}^2}{\binom{p-1}{m} 16^{p-1}} \quad (m := p-1-j \in \{0,\dots,n-1\}).$$
Since $c_n = \frac{\binom{p-1}{n}^2}{16^n}$ and $16^n = 4^{p-1}$, Lemma 2(2) implies
$$c_n - \varepsilon T_{\mathrm{mid}} = c_n\left(1 - \varepsilon \frac{\binom{p-1}{n}}{4^{p-1}}\right) \equiv 0 \pmod{p^3}.$$
For each $j \in \{n+1,\dots,p-1\}$ with $m = p-1-j$ and $r = p-j = m+1$, we have $\binom{2r}{r} = \binom{2m+2}{m+1} = \frac{2(2m+1)}{m+1}\binom{2m}{m}$, so part (2) yields
$$\frac{1}{p}\binom{2j}{j}\binom{2m}{m} \equiv -\frac{2\binom{2m}{m}}{(m+1)\binom{2m+2}{m+1}} = -\frac{1}{2m+1} \pmod{p}.$$
Squaring, and using $\binom{p-1}{m} \equiv (-1)^m \pmod{p}$ and $16^{p-1} \equiv 1 \pmod{p}$, shows $p^2 \mid T_{\mathrm{tail}}$ and
$$\frac{T_{\mathrm{tail}}}{p^2} \equiv 2 \sum_{m=0}^{n-1} \frac{(-1)^m}{(2m+1)^2} \pmod{p}.$$
Reindexing via $t = n - m \in \{1, \dots, n\}$ gives $2m + 1 = p - 2t \equiv -2t \pmod{p}$ and $(-1)^m = \varepsilon (-1)^t$, so
$$\frac{T_{\mathrm{tail}}}{p^2} \equiv 2 \sum_{t=1}^n \frac{\varepsilon (-1)^t}{4t^2} = \frac{1}{2}\varepsilon \sum_{t=1}^n \frac{(-1)^t}{t^2} \pmod{p}.$$
Since $E_p(n) = c_n - \varepsilon v_{p-1} = (c_n - \varepsilon T_{\mathrm{mid}}) - \varepsilon T_{\mathrm{tail}}$, it follows that $p^2 \mid E_p(n)$, $v_{p-1} \equiv \varepsilon c_n \equiv \varepsilon \pmod{p}$ (by Lemma 1(4)), and $\tilde{E}_n = \varepsilon \frac{E_p(n)}{p^2} \equiv -\frac{T_{\mathrm{tail}}}{p^2} \equiv -\frac{1}{2}\varepsilon \sum_{t=1}^n \frac{(-1)^t}{t^2} \pmod{p}$. $\square$

---

### Lemma 4 (Polynomial ODE recurrence and $p^2 \mid E_p(m)$ for all $m$)
For all $0 \le m \le n$, $p^2 \mid E_p(m)$. Setting $\tilde{E}_m := \varepsilon \frac{E_p(m)}{p^2} \bmod p$, we have
$$4m^2 \tilde{E}_m - (2m-1)^2 \tilde{E}_{m-1} \equiv 1 \pmod{p} \qquad (1 \le m \le n).$$

**Proof.**
Define $G(x) := \sum_{i=0}^{p-1} v_i (1+x)^i = \sum_{j=0}^{p-1} G_j x^j$, so $G_{2m} = B_m$ for $0 \le m \le n$. Put $y = 1+x$, $D = \frac{d}{dx} = \frac{d}{dy}$, $\theta_y = y D$, and $\theta_x = x D$. Define the differential operators
$$\mathcal{L}_G := 2\theta_y^2 - y(3\theta_y^2 + 3\theta_y + 1) + y^2(\theta_y + 1)^2, \qquad \mathcal{L}_A := \theta_x^2 - x^2(\theta_x + 1)^2.$$
Since $\mathcal{L}_G(y^i) = 2i^2 y^i - (3i^2+3i+1)y^{i+1} + (i+1)^2 y^{i+2}$, applying $\mathcal{L}_G$ to $G(x) = \sum_{i=0}^{p-1} v_i y^i$ gives
$$\mathcal{L}_G(G)(x) = (2v_1 - v_0)y + \sum_{k=2}^{p-1} \big(2k^2 v_k - (3k^2-3k+1)v_{k-1} + (k-1)^2 v_{k-2}\big) y^k + \big(-(3p^2-3p+1)v_{p-1} + (p-1)^2 v_{p-2}\big) y^p + p^2 v_{p-1} y^{p+1}.$$
Dividing the defining recurrence $k^2 \mathcal{P}_k = 8(3k^2-3k+1)\mathcal{P}_{k-1} - 128(k-1)^2 \mathcal{P}_{k-2}$ by $8 \cdot 16^{k-1} = \frac{1}{2} \cdot 16^k$ gives $2k^2 v_k - (3k^2-3k+1)v_{k-1} + (k-1)^2 v_{k-2} = 0$ for all $k \ge 2$, and $2v_1 - v_0 = 2(\frac{8}{16}) - 1 = 0$. Using the $k = p$ recurrence for the $y^p$ coefficient yields the exact polynomial identity
$$\mathcal{L}_G(G)(x) = p^2 (1+x)^p \big(-2v_p + v_{p-1}(1+x)\big).$$
Next, expanding $\theta_y^2 = y^2 D^2 + y D$ and $(\theta_y+1)^2 = y^2 D^2 + 3y D + 1$ in $y = 1+x$, we find
$$\mathcal{L}_G = y^2(2 - 3y + y^2) D^2 + y(2 - 6y + 3y^2) D + y(y-1) = (1+x)^2 x(x-1) D^2 + (1+x)(3x^2-1) D + x(1+x).$$
On the other hand, $\mathcal{L}_A = x^2(1-x^2)D^2 + x(1-3x^2)D - x^2$, so comparing coefficients of $D^2, D, 1$ immediately gives the exact operator identity
$$(1+x)\mathcal{L}_A = -x \mathcal{L}_G.$$
Therefore, in $\mathbb{Z}_{(p)}[x]$,
$$(1+x)\mathcal{L}_A(G)(x) = p^2 x (1+x)^p \big(2v_p - v_{p-1}(1+x)\big).$$
By Lemma 3(1) and 3(3), $2v_p \equiv 1 \pmod{p}$ and $v_{p-1} \equiv \varepsilon \pmod{p}$, so
$$(1+x)\mathcal{L}_A(G)(x) \equiv p^2 (1+x)\big(x(1+x)^{p-1} - \varepsilon x(1+x)^p\big) \pmod{p^3}.$$
Since $(1+x)$ is monic in $\mathbb{Z}_{(p)}[x]$, cancelling $(1+x)$ sequentially modulo $p$, $p^2$, and $p^3$ (as $\mathbb{F}_p[x]$ is a domain) gives
$$\mathcal{L}_A(G)(x) \equiv p^2\big(x(1+x)^{p-1} - \varepsilon x(1+x)^p\big) \pmod{p^3}.$$
In $\mathbb{F}_p[x]$, $(1+x)^p \equiv 1 + x^p$ and $(1+x)^{p-1} \equiv \sum_{j=0}^{p-1} (-1)^j x^j$. For any $1 \le m \le n$, we have $2 \le 2m \le p-1$, so the coefficient of $x^{2m}$ in $x(1+x)^p \equiv x + x^{p+1}$ is $0 \pmod{p}$, while the coefficient of $x^{2m}$ in $x(1+x)^{p-1}$ is $(-1)^{2m-1} = -1 \pmod{p}$. On the left-hand side, $\mathcal{L}_A(G)(x) = \sum_{j=0}^{p-1} j^2 G_j x^j - \sum_{j=0}^{p-1} (j+1)^2 G_j x^{j+2}$ has $x^{2m}$ coefficient $(2m)^2 G_{2m} - (2m-1)^2 G_{2m-2} = 4m^2 B_m - (2m-1)^2 B_{m-1}$. Thus
$$4m^2 B_m - (2m-1)^2 B_{m-1} \equiv -p^2 \pmod{p^3} \qquad (1 \le m \le n).$$
Since $4m^2 c_m - (2m-1)^2 c_{m-1} = 4m^2 \frac{\binom{2m}{m}^2}{16^m} - (2m-1)^2 \frac{\binom{2m-2}{m-1}^2}{16^{m-1}} = 0$, subtracting $\varepsilon$ times the $B$-congruence yields
$$4m^2 E_p(m) - (2m-1)^2 E_p(m-1) \equiv \varepsilon p^2 \pmod{p^3} \qquad (1 \le m \le n).$$
Because $p^2 \mid E_p(n)$ (Lemma 3(3)) and $p \nmid (2m-1)$ for $1 \le m \le n$, downward induction from $m = n$ to $m = 0$ shows $p^2 \mid E_p(m)$ for all $0 \le m \le n$. Dividing by $p^2$ and multiplying by $\varepsilon$ gives $4m^2 \tilde{E}_m - (2m-1)^2 \tilde{E}_{m-1} \equiv 1 \pmod{p}$. $\square$

---

### Lemma 5 (Symmetry reduction to $S_0 \equiv 0 \pmod{p}$)
Set $S_m := \tilde{E}_m + \tilde{E}_{n-m}$ for $0 \le m \le n$.
1. $4m^2 S_m \equiv (2m-1)^2 S_{m-1} \pmod{p}$ for all $1 \le m \le n$. Hence if $S_0 \equiv 0 \pmod{p}$, then $S_m \equiv 0 \pmod{p}$ for all $0 \le m \le n$, and Remark 3.1 holds.
2. $S_0 \equiv 2\tilde{E}_n - T_{n-1} \pmod{p}$, where $T_M := \sum_{k=0}^M \frac{1}{\binom{M}{k}^2}$.

**Proof.**
For (1), fix $1 \le m \le n$ and set $m' := n + 1 - m \in \{1, \dots, n\}$. Then $2m' = p + 1 - 2m \equiv -(2m-1) \pmod{p}$ and $2m' - 1 = p - 2m \equiv -2m \pmod{p}$. Writing Lemma 4 at $m$ and at $m'$:
- At $m$: $4m^2 \tilde{E}_m - (2m-1)^2 \tilde{E}_{m-1} \equiv 1 \pmod{p}$.
- At $m'$: $(2m')^2 \tilde{E}_{m'} - (2m'-1)^2 \tilde{E}_{m'-1} \equiv 1 \pmod{p}$, which modulo $p$ reads $(2m-1)^2 \tilde{E}_{n+1-m} - 4m^2 \tilde{E}_{n-m} \equiv 1 \pmod{p}$.
Subtracting the second congruence from the first cancels the constant $1$ and gives
$$4m^2(\tilde{E}_m + \tilde{E}_{n-m}) - (2m-1)^2 (\tilde{E}_{m-1} + \tilde{E}_{n+1-m}) \equiv 0 \pmod{p},$$
i.e., $4m^2 S_m \equiv (2m-1)^2 S_{m-1} \pmod{p}$. Since $p \nmid 4m^2$ for $1 \le m \le n$, $S_0 \equiv 0 \pmod{p}$ implies $S_m \equiv 0 \pmod{p}$ for all $m$. Using $c_m \equiv c_{n-m} \pmod{p}$ (Lemma 1(4)) and $p \ne 2$,
$$2 \sum_{m=0}^n c_m \tilde{E}_m \equiv \sum_{m=0}^n c_m (\tilde{E}_m + \tilde{E}_{n-m}) = \sum_{m=0}^n c_m S_m \equiv 0 \pmod{p},$$
so $\sum_{m=0}^n c_m E_p(m) \equiv 0 \pmod{p^3}$, proving Remark 3.1 by Lemma 1(3).

For (2), dividing $4m^2 \tilde{E}_m - (2m-1)^2 \tilde{E}_{m-1} \equiv 1 \pmod{p}$ by $4m^2 c_m = (2m-1)^2 c_{m-1}$ (which are units mod $p$ by Lemma 1(4)) gives
$$\frac{\tilde{E}_m}{c_m} - \frac{\tilde{E}_{m-1}}{c_{m-1}} \equiv \frac{1}{4m^2 c_m} \pmod{p} \qquad (1 \le m \le n).$$
Summing over $m = 1, \dots, n$ and using $c_0 = 1$, $c_n \equiv 1 \pmod{p}$, $c_m \equiv \binom{n}{m}^2 \pmod{p}$, $m\binom{n}{m} = n\binom{n-1}{m-1}$, and $4n^2 = (p-1)^2 \equiv 1 \pmod{p}$ gives
$$\tilde{E}_n - \tilde{E}_0 \equiv \sum_{m=1}^n \frac{1}{4m^2 \binom{n}{m}^2} = \sum_{m=1}^n \frac{1}{4n^2 \binom{n-1}{m-1}^2} \equiv \sum_{k=0}^{n-1} \frac{1}{\binom{n-1}{k}^2} = T_{n-1} \pmod{p}.$$
Hence $S_0 = \tilde{E}_0 + \tilde{E}_n \equiv 2\tilde{E}_n - T_{n-1} \pmod{p}$. $\square$

---

### Lemma 6 (Evaluation of $T_{n-1} \pmod{p}$ and completion of the proof)
$$T_{n-1} \equiv -\varepsilon \sum_{t=1}^n \frac{(-1)^t}{t^2} \pmod{p},$$
and therefore $S_0 \equiv 2\tilde{E}_n - T_{n-1} \equiv 0 \pmod{p}$.

**Proof.**
We establish four elementary steps:

1. **Exact Staver identity:** For every integer $M \ge 0$,
   $$\frac{2(2M+3)\binom{2M+2}{M+1}}{(M+1)^2} T_M = 6 \sum_{r=1}^{M+1} \frac{\binom{2r}{r}}{r}.$$
   *Proof of (1):* For $M \ge 1$ and $0 \le k \le M-1$, define $G(M, k) := \frac{M^2(2k - 3M - 3)}{\binom{M}{k}^2}$, and set $G(M, M) := \frac{M^2(2M-3M-3)}{\binom{M}{M}^2} = -M^2(M+3)$. Using $\frac{1}{\binom{M}{k+1}^2} = \frac{(k+1)^2}{(M-k)^2}\frac{1}{\binom{M}{k}^2}$ and the polynomial identity
   $$(2k - 3M - 1)(k+1)^2 - (2k - 3M - 3)(M-k)^2 = 2(2M+3)(M-k)^2 - (M+1)^3$$
   (both sides are quadratic in $k$ with $k^2$ coefficient $2(2M+3)$ and equal values at $k = 0$ and $k = M$), we have
   $$G(M, k+1) - G(M, k) = \frac{2M^2(2M+3)}{\binom{M}{k}^2} - \frac{M^2(M+1)^3}{(M-k)^2\binom{M}{k}^2} = \frac{2M^2(2M+3)}{\binom{M}{k}^2} - \frac{(M+1)^3}{\binom{M-1}{k}^2}.$$
   Summing over $k = 0, \dots, M-1$ gives $G(M, M) - G(M, 0) = 2M^3 = 2M^2(2M+3)(T_M - 1) - (M+1)^3 T_{M-1}$, so
   $$2M^2(2M+3)T_M - (M+1)^3 T_{M-1} = 6M^2(M+1).$$
   Multiplying by $\frac{\binom{2M+2}{M+1}}{M^2(M+1)^2}$ and using $\binom{2M+2}{M+1} = \frac{2(2M+1)}{M+1}\binom{2M}{M}$ telescopes to
   $$\frac{2(2M+3)\binom{2M+2}{M+1}}{(M+1)^2} T_M - \frac{2(2M+1)\binom{2M}{M}}{M^2} T_{M-1} = \frac{6\binom{2M+2}{M+1}}{M+1}.$$
   Summing over $M = 1, \dots, N$ and adding the $M = 0$ value $\frac{2\cdot 3 \cdot \binom{2}{1}}{1^2} T_0 = 12 = \frac{6\binom{2}{1}}{1}$ yields (1).

2. **Mod-$p^2$ vanishing and reflection:** Setting $M = p - 2$ in (1) gives
   $$6 \sum_{r=1}^{p-1} \frac{\binom{2r}{r}}{r} = \frac{2(2p-1)\binom{2p-2}{p-1}}{(p-1)^2} T_{p-2}.$$
   Here $p \mid \binom{2p-2}{p-1}$, and $\binom{p-2}{k} \equiv \binom{-2}{k} = (-1)^k (k+1) \pmod{p}$ implies $T_{p-2} \equiv \sum_{k=0}^{p-2} \frac{1}{(k+1)^2} = \sum_{j=1}^{p-1} \frac{1}{j^2} \equiv 0 \pmod{p}$ (as in Lemma 2(1)). Since $p > 3$, $p^2 \mid \sum_{r=1}^{p-1} \frac{\binom{2r}{r}}{r}$. Splitting at $n = (p-1)/2$ and applying Lemma 3(2) with $j = p - r \equiv -r \pmod{p}$ gives
   $$\sum_{r=1}^n \frac{\binom{2r}{r}}{r} \equiv -\sum_{j=n+1}^{p-1} \frac{\binom{2j}{j}}{j} \equiv -\sum_{r=1}^n \frac{-2p / (r\binom{2r}{r})}{-r} = -2p \sum_{r=1}^n \frac{1}{r^2\binom{2r}{r}} \pmod{p^2}.$$
   Comparing with (1) at $M = n - 1$ (where $2M+3 = 2n+1 = p$, $\binom{2n}{n} \equiv \varepsilon \pmod{p}$, and $4n^2 \equiv 1 \pmod{p}$),
   $$8\varepsilon p T_{n-1} \equiv \frac{2p\binom{2n}{n}}{n^2} T_{n-1} = 6 \sum_{r=1}^n \frac{\binom{2r}{r}}{r} \equiv -12p \sum_{r=1}^n \frac{1}{r^2\binom{2r}{r}} \pmod{p^2},$$
   whence
   $$3 \sum_{r=1}^n \frac{1}{r^2\binom{2r}{r}} \equiv -2\varepsilon T_{n-1} \pmod{p}.$$

3. **Apéry's identity (exact telescoping):** For every integer $m \ge 1$,
   $$\sum_{k=1}^m \frac{(-1)^k}{k^2 \binom{m}{k}\binom{m+k}{k}} = (-1)^{m-1} \left(3 \sum_{k=1}^m \frac{1}{k^2\binom{2k}{k}} + 2 \sum_{k=1}^m \frac{(-1)^k}{k^2}\right).$$
   *Proof of (3):* The $m = 1$ case reads $-\frac{1}{2} = 1\cdot(\frac{3}{2} - 2) = -\frac{1}{2}$. For $m \ge 2$, the increment $(-1)^{m-1}\sum_{k=1}^m \frac{(-1)^k}{k^2\binom{m}{k}\binom{m+k}{k}} - (-1)^{m-2}\sum_{k=1}^{m-1} \frac{(-1)^k}{k^2\binom{m-1}{k}\binom{m-1+k}{k}}$ equals $(-1)^{m-1}$ times
   $$\frac{(-1)^m}{m^2\binom{2m}{m}} + \sum_{k=1}^{m-1} \frac{(-1)^k}{k^2}\left(\frac{1}{\binom{m}{k}\binom{m+k}{k}} + \frac{1}{\binom{m-1}{k}\binom{m-1+k}{k}}\right) = \frac{(-1)^m}{m^2\binom{2m}{m}} + \sum_{k=1}^{m-1} \frac{2(-1)^k}{k^2 \binom{m-1}{k}\binom{m+k}{k}},$$
   since $\binom{m-1}{k}\binom{m-1+k}{k} = \frac{m-k}{m}\cdot\frac{m}{m+k}\binom{m}{k}\binom{m+k}{k}$, so $\frac{1}{\binom{m}{k}\binom{m+k}{k}} + \frac{1}{\binom{m-1}{k}\binom{m-1+k}{k}} = \frac{2m}{(m-k)\binom{m}{k}\binom{m+k}{k}} = \frac{2}{\binom{m-1}{k}\binom{m+k}{k}}$.
   Now define $F(m, k) := -\frac{2(-1)^k}{k^2 \binom{m}{k}\binom{m+k-1}{k}}$ for $1 \le k \le m$. For $1 \le k \le m-1$, using $\binom{m}{k+1} = \frac{m-k}{k+1}\binom{m}{k}$ and $\binom{m+k}{k+1} = \frac{m+k}{k+1}\binom{m+k-1}{k}$, we get
   $$F(m, k+1) - F(m, k) = \frac{2(-1)^k}{k^2 \binom{m}{k}\binom{m+k-1}{k}}\left(1 + \frac{k^2}{m^2 - k^2}\right) = \frac{2(-1)^k m^2}{k^2(m-k)(m+k)\binom{m}{k}\binom{m+k-1}{k}} = \frac{2(-1)^k}{k^2 \binom{m-1}{k}\binom{m+k}{k}}.$$
   Summing over $k = 1, \dots, m-1$ gives $F(m, m) - F(m, 1) = \frac{4(-1)^{m-1}}{m^2\binom{2m}{m}} - \frac{2}{m^2}$ (since $\binom{2m-1}{m} = \frac{1}{2}\binom{2m}{m}$). Adding $\frac{(-1)^m}{m^2\binom{2m}{m}}$ and multiplying by $(-1)^{m-1}$ yields $\frac{3}{m^2\binom{2m}{m}} + \frac{2(-1)^m}{m^2}$, completing the induction.

4. **Conclusion:** Reduce Apéry's identity at $m = n$ modulo $p$. For $1 \le k \le n$, $\binom{n+k}{k}(-1)^k = \binom{-n-1}{k} \equiv \binom{p-n-1}{k} = \binom{n}{k} \pmod{p}$, so the LHS becomes
   $$\sum_{k=1}^n \frac{1}{k^2\binom{n}{k}^2} = \frac{1}{n^2} \sum_{k=1}^n \frac{1}{\binom{n-1}{k-1}^2} \equiv 4 T_{n-1} \pmod{p}.$$
   Substituting $3\sum_{k=1}^n \frac{1}{k^2\binom{2k}{k}} \equiv -2\varepsilon T_{n-1} \pmod{p}$ from (2) into the RHS gives
   $$4 T_{n-1} \equiv -\varepsilon \left(-2\varepsilon T_{n-1} + 2\sum_{t=1}^n \frac{(-1)^t}{t^2}\right) = 2 T_{n-1} - 2\varepsilon \sum_{t=1}^n \frac{(-1)^t}{t^2} \pmod{p}.$$
   Hence $2 T_{n-1} \equiv -2\varepsilon \sum_{t=1}^n \frac{(-1)^t}{t^2} \pmod{p}$, i.e., $T_{n-1} \equiv -\varepsilon \sum_{t=1}^n \frac{(-1)^t}{t^2} \pmod{p}$. Combining this with Lemma 3(3) and Lemma 5(2) gives
   $$S_0 \equiv 2\tilde{E}_n - T_{n-1} \equiv -\varepsilon \sum_{t=1}^n \frac{(-1)^t}{t^2} - \left(-\varepsilon \sum_{t=1}^n \frac{(-1)^t}{t^2}\right) = 0 \pmod{p}.$$
   By Lemma 5(1), Remark 3.1 holds for every prime $p > 3$. $\blacksquare$
