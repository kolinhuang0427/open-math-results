# Proof of OEIS A124380 Logarithmic Asymptotic Conjecture

We prove Vaclav Kotesovec's Sep 18, 2024 conjecture on [OEIS A124380](https://oeis.org/A124380) (rev. 39):
$$\log a(n) = \frac{n \log n}{2} - \frac{1 + \log 2}{2} n + O\!\left(n^{3/4}\log n\right) \qquad (n \to \infty),$$
and in particular $\log a(n) \sim \frac{n \log n}{2} - \frac{1 + \log 2}{2} n$ (with $\lim_{n\to\infty}\frac{\log a(n) - \frac{n}{2}\log n}{n} = -\frac{1+\log 2}{2}$ as well).

## 1. Elementary Symmetric Polynomial Representation

From the generating function $A(x) = \sum_{n=0}^{\infty} a(n) x^n = \sum_{m=0}^{\infty} x^m \prod_{j=0}^{m}(1 + j x)$, expanding each finite product gives
$$\prod_{j=0}^{m}(1 + j x) = \prod_{j=1}^{m}(1 + j x) = \sum_{r=0}^{m} e_r(1, 2, \dots, m)\, x^r,$$
where $e_r(1, 2, \dots, m) := \sum_{1 \le i_1 < \dots < i_r \le m} i_1 \cdots i_r$ denotes the $r$-th elementary symmetric polynomial (with $e_0 = 1$). Extracting $[x^n] A(x)$ via $m + r = n$ ($0 \le r \le m = n - r$, i.e., $0 \le r \le \lfloor n/2 \rfloor$) yields
$$a(n) = \sum_{r=0}^{\lfloor n/2 \rfloor} e_r(1, 2, \dots, n - r) \qquad (n \ge 0).$$

## 2. Explicit Factorial Bounds for $a(n)$

**Lemma 1.** *Let $n \ge 4$ and $k := \lfloor n/2 \rfloor \ge 2$. Then*
$$k! \le a(n) \le (k + 1)\,(2k + 1)^{3 e (2k + 1)^{3/4} + 2}\, k!.$$

*Proof.*
1. **Lower bound:** Retain only the single $r = k$ summand of $a(n)$:
   - If $n = 2k$, then $n - k = k$ and $e_k(1, \dots, k) = k!$.
   - If $n = 2k + 1$, then $n - k = k + 1$ and $e_k(1, \dots, k+1) = \sum_{j=1}^{k+1}\frac{(k+1)!}{j} > k!$.
   Hence $a(n) \ge k!$ for every $n \ge 2$.

2. **Termwise upper bound:** Fix any $r \in \{0, 1, \dots, k\}$, and write $t := k - r \in \{0, 1, \dots, k\}$ and $m := n - r$. Since $2k \le n \le 2k + 1$, we have $k + t \le m \le k + 1 + t$ and $m - r = n - 2r \ge 2k - 2(k - t) = 2t$.

   Each $r$-element subset $S \subseteq \{1, \dots, m\}$ satisfies $\prod_{i \in S} i \le \prod_{i = m - r + 1}^m i = \frac{m!}{(m-r)!}$, and there are $\binom{m}{r}$ such subsets, so
   $$e_r(1, \dots, m) \le \binom{m}{r}\frac{m!}{(m-r)!} = \frac{(m!)^2}{r!\,((m-r)!)^2} \le \frac{((k + 1 + t)!)^2}{(k - t)!\,((2t)!)^2}.$$
   - At $t = 0$: $\frac{((k+1)!)^2}{k!\, (0!)^2} = (k + 1)^2 k! \le (2k + 1)^2 k!$.
   - For $1 \le t \le k$: since $k + 1 + t \le 2k + 1$, we have $\frac{(k + 1 + t)!}{k!} \le (2k + 1)^{t+1}$ and $\frac{(k + 1 + t)!}{(k - t)!} \le (2k + 1)^{2t+1}$, so
     $$\frac{((k + 1 + t)!)^2}{(k - t)!\, k!} \le (2k + 1)^{3t + 2}.$$
     On the other hand, for every integer $M \ge 1$, the series $e^M = \sum_{j=0}^{\infty} \frac{M^j}{j!} > \frac{M^M}{M!}$ gives $M! > (M/e)^M$; applying this to $M = 2t$ yields $((2t)!)^2 > \left(\frac{2t}{e}\right)^{4t}$. Hence
     $$\frac{e_r(1, \dots, m)}{k!} \le (2k + 1)^2 \left(\frac{(2k + 1)^3 e^4}{16\, t^4}\right)^t.$$
     Set $T := e (2k + 1)^{3/4}$. If $t \ge T$, then $16 t^4 \ge 16 e^4 (2k + 1)^3 > (2k + 1)^3 e^4$, so the parenthesized base is $< 1$ and $\frac{e_r(1, \dots, m)}{k!} \le (2k + 1)^2$. If $1 \le t < T$, then dropping $((2t)!)^2 \ge 1$ directly gives $\frac{e_r(1, \dots, m)}{k!} \le (2k + 1)^{3t + 2} < (2k + 1)^{3T + 2}$.

   Because $T > 0$, every one of the $k + 1$ terms $r \in \{0, \dots, k\}$ satisfies $e_r(1, \dots, n - r) \le (2k + 1)^{3T + 2} k!$. Summing over all $k + 1$ terms yields
   $$a(n) \le (k + 1)(2k + 1)^{3 e (2k + 1)^{3/4} + 2}\, k!. \qquad \square$$

## 3. Asymptotics of $\log a(n)$

**Theorem.** *As $n \to \infty$,*
$$\log a(n) = \frac{n \log n}{2} - \frac{1 + \log 2}{2} n + O\!\left(n^{3/4}\log n\right),$$
*so $\log a(n) \sim \frac{n \log n}{2} - \frac{1 + \log 2}{2} n$.*

*Proof.* For $k = \lfloor n/2 \rfloor \ge 2$, since $x \mapsto \log x$ is strictly increasing on $[1, \infty)$, comparing $\sum_{j=2}^k \log j$ with $\int \log x\,dx = x\log x - x$ gives
$$k \log k - k + 1 = \int_1^k \log x\, dx \le \sum_{j=2}^k \log j = \log(k!) \le \int_1^{k+1} \log x\, dx = (k + 1)\log(k + 1) - k.$$
Writing $k = \frac{n}{2} - \theta_n$ with $\theta_n \in \{0, 1/2\}$, we have $\log k = \log(n/2) + \log(1 - 2\theta_n/n) = \log n - \log 2 + O(1/n)$ and $(k+1)\log(k+1) - k\log k = O(\log n)$, whence
$$\log(k!) = \left(\frac{n}{2} - \theta_n\right)\bigl(\log n - \log 2 + O(1/n)\bigr) - \frac{n}{2} + O(\log n) = \frac{n \log n}{2} - \frac{1 + \log 2}{2} n + O(\log n).$$
Taking logarithms in Lemma 1 shows
$$0 \le \log a(n) - \log(k!) \le \log(k + 1) + \bigl(3 e (2k + 1)^{3/4} + 2\bigr)\log(2k + 1) = O\!\left(n^{3/4}\log n\right).$$
Therefore
$$\log a(n) = \frac{n \log n}{2} - \frac{1 + \log 2}{2} n + O\!\left(n^{3/4}\log n\right).$$
Dividing by $\frac{n \log n}{2} - \frac{1 + \log 2}{2} n$ gives $\lim_{n\to\infty} \frac{\log a(n)}{\frac{n \log n}{2} - \frac{1 + \log 2}{2} n} = 1$, i.e., $\log a(n) \sim \frac{n \log n}{2} - \frac{1 + \log 2}{2} n$ (and likewise $\lim_{n\to\infty}\frac{\log a(n) - \frac{n}{2}\log n}{n} = -\frac{1+\log 2}{2}$). $\square$
