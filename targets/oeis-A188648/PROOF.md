# Proof of OEIS A188648 Hypergeometric Conjecture

We prove Velin Yanev's Oct 31, 2019 conjecture on [OEIS A188648](https://oeis.org/A188648) (rev. 46).

## Theorem

For every integer $n \ge 0$,
$$a(n) := \sum_{j=0}^{n} \binom{2n-j}{j}^2 = {}_4F_3\left(\begin{matrix}-n, -n, n+1, n+1 \\ 1/2, 1/2, 1\end{matrix}; \frac{1}{16}\right).$$

## Proof

Because the top parameter $-n \le 0$ is a nonpositive integer, the rising factorial $(-n)_k$ vanishes for all $k > n$. Hence the generalized hypergeometric series terminates at $k = n$:
$${}_4F_3\left(\begin{matrix}-n, -n, n+1, n+1 \\ 1/2, 1/2, 1\end{matrix}; \frac{1}{16}\right) = \sum_{k=0}^{n} \frac{(-n)_k^2 \, (n+1)_k^2}{(1/2)_k^2 \, (1)_k \, k!} \left(\frac{1}{16}\right)^k,$$
where $(x)_0 := 1$ and $(x)_k := \prod_{i=0}^{k-1}(x+i)$ for $k \ge 1$.

Fix $n \ge 0$ and any $k \in \{0, 1, \dots, n\}$. We simplify the numerator and denominator factors:

1. **Numerator:** Since $(-n)_k = (-1)^k n(n-1)\cdots(n-k+1) = (-1)^k \frac{n!}{(n-k)!}$ and $(n+1)_k = (n+1)(n+2)\cdots(n+k) = \frac{(n+k)!}{n!}$, their product is
   $$(-n)_k (n+1)_k = (-1)^k \frac{(n+k)!}{(n-k)!}.$$
   (This holds at $k = 0$ as well, giving $1 = \frac{n!}{n!}$.)

2. **Denominator:** Since $(1/2)_k = \prod_{i=0}^{k-1}\frac{2i+1}{2} = \frac{(2k-1)!!}{2^k}$ (with $(-1)!! := 1$ at $k=0$), $(1)_k = k!$, and $4^k = 2^k \cdot 2^k$, we have
   $$(1/2)_k \, k! \, 4^k = \frac{(2k-1)!!}{2^k} \cdot k! \cdot 2^k \cdot 2^k = (2k-1)!! \cdot (2k)!! = (2k)!.$$

3. **Termwise match:** Squaring the quotient and noting $(1)_k = k!$ and $4^{2k} = 16^k$, the $k$-th summand of the ${}_4F_3$ series equals
   $$\frac{(-n)_k^2 \, (n+1)_k^2}{(1/2)_k^2 \, (1)_k \, k! \, 16^k} = \left(\frac{(-n)_k (n+1)_k}{(1/2)_k \, k! \, 4^k}\right)^2 = \left(\frac{(-1)^k (n+k)!}{(n-k)! \, (2k)!}\right)^2 = \binom{n+k}{2k}^2 = \binom{n+k}{n-k}^2.$$

Finally, reindexing the sum by $j = n - k$ (so $k = n - j$ runs over $0 \le j \le n$, and $n + k = 2n - j$, $n - k = j$) yields
$${}_4F_3\left(\begin{matrix}-n, -n, n+1, n+1 \\ 1/2, 1/2, 1\end{matrix}; \frac{1}{16}\right) = \sum_{j=0}^{n} \binom{2n-j}{j}^2 = a(n). \qquad \square$$
