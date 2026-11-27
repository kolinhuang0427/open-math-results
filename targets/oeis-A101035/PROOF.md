# Proof of OEIS A101035 Logarithmic Generating Function Conjecture

We prove Benedict W. J. Irwin's Jul 26, 2017 logarithmic generating function conjecture on [OEIS A101035](https://oeis.org/A101035) (rev. 37) in $\mathbb{Q}[[x]]$.

## Theorem

Let $g(m) := \sum_{j=1}^{m} \gcd(j, m)$ ($m \ge 1$) be Pillai's gcd-sum function (OEIS A018804), and let $a := g^{-1}$ be its Dirichlet inverse, i.e., the unique arithmetic function satisfying $(a * g)(m) = \sum_{d \mid m} a(d)\,g(m/d) = \varepsilon(m)$ ($\varepsilon(1)=1$, $\varepsilon(m)=0$ for $m > 1$). Then in $\mathbb{Q}[[x]]$,
$$\sum_{n=1}^{\infty}\sum_{k=1}^{\infty} \mu(n)\mu(k)\log\left(\frac{1}{1 - x^{nk}}\right) = \sum_{m=1}^{\infty} a(m)\frac{x^m}{m},$$
where $\mu$ is the Möbius function.

## Proof

### Step 1: Dirichlet factorization of $g$ and $a = g^{-1}$
Recall the standard arithmetic functions $\mathrm{id}(m) = m$, $1(m) = 1$, and Euler's totient $\varphi(m)$. Grouping $j \in \{1, \dots, m\}$ by $d = \gcd(j, m)$ gives
$$g(m) = \sum_{j=1}^{m} \gcd(j, m) = \sum_{d \mid m} d \cdot \#\{1 \le j \le m : \gcd(j, m) = d\} = \sum_{d \mid m} d\, \varphi(m/d) = (\mathrm{id} * \varphi)(m).$$
Since $\varphi * 1 = \mathrm{id}$ (so $\varphi = \mathrm{id} * \mu$), we have $g = \mathrm{id} * \mathrm{id} * \mu$.

Moreover, $\mathrm{id}^{-1} = \mathrm{id}\cdot\mu$ because for every $m \ge 1$,
$$\bigl(\mathrm{id} * (\mathrm{id}\cdot\mu)\bigr)(m) = \sum_{d \mid m} d \cdot \frac{m}{d}\mu(m/d) = m\sum_{d \mid m}\mu(m/d) = m\,\varepsilon(m) = \varepsilon(m),$$
and $1^{-1} = \mu$ (so $\mu^{-1} = 1$). Because Dirichlet convolution is commutative and associative, the Dirichlet inverse of $g = \mathrm{id} * \mathrm{id} * \mu$ is
$$a = g^{-1} = (\mathrm{id}\cdot\mu) * (\mathrm{id}\cdot\mu) * 1,$$
meaning that for every integer $m \ge 1$,
$$a(m) = \sum_{\substack{n, k, r \ge 1 \\ n k r = m}} n\mu(n) \cdot k\mu(k).$$

### Step 2: Coefficient extraction of the logarithmic generating function
In $\mathbb{Q}[[x]]$, for every $n, k \ge 1$, $\log\!\left(\frac{1}{1 - x^{nk}}\right) = \sum_{r=1}^{\infty} \frac{x^{nkr}}{r} \in x^{nk}\mathbb{Q}[[x]]$. Since only finitely many pairs $(n, k) \in \mathbb{Z}_{\ge 1}^2$ satisfy $nk \le M$ for any given $M$, the double sum converges $x$-adically in $\mathbb{Q}[[x]]$. Collecting the coefficient of $x^m$ ($m \ge 1$):
$$\begin{aligned}
\sum_{n=1}^{\infty}\sum_{k=1}^{\infty} \mu(n)\mu(k)\log\left(\frac{1}{1 - x^{nk}}\right)
&= \sum_{n=1}^{\infty}\sum_{k=1}^{\infty}\sum_{r=1}^{\infty} \mu(n)\mu(k)\frac{x^{nkr}}{r} \\
&= \sum_{m=1}^{\infty} \left(\sum_{\substack{n,k,r \ge 1 \\ nkr = m}} \mu(n)\mu(k)\frac{m}{r}\right)\frac{x^m}{m} \\
&= \sum_{m=1}^{\infty} \left(\sum_{\substack{n,k,r \ge 1 \\ nkr = m}} n\mu(n)\cdot k\mu(k)\right)\frac{x^m}{m} \\
&= \sum_{m=1}^{\infty} a(m)\frac{x^m}{m}. \qquad \square
\end{aligned}$$
