# Proof of OEIS A127276 Formula and Generating Function

## Theorem

Let $(b_m)_{m \ge 0}$ be OEIS [A127275](https://oeis.org/A127275), defined by
$$\sum_{m=0}^{\infty} b_m x^m = \frac{\sqrt{1 - 4x} - x}{1 - 4x},$$
and let $a(n) = A127276(n)$ ($n \ge 0$) be its Hankel transform:
$$a(n) := \det\bigl(b_{i+j}\bigr)_{0 \le i,j \le n}.$$
Then for every integer $n \ge 0$,
$$a(n) = 2^n - n(n+1)\, 2^{n-2},$$
and the ordinary generating function of $(a(n))_{n \ge 0}$ is
$$\sum_{n=0}^{\infty} a(n) x^n = -\frac{(4x - 1)(x - 1)}{(2x - 1)^3}.$$

---

## Proof

### 1. Explicit coefficients of $A127275$ and rank-2 decomposition of the Hankel matrix

Simplifying the generating function of $(b_m)_{m \ge 0}$ gives
$$\frac{\sqrt{1 - 4x} - x}{1 - 4x} = \frac{1}{\sqrt{1 - 4x}} - \frac{x}{1 - 4x} = \sum_{m=0}^{\infty} \binom{2m}{m} x^m - \sum_{m=1}^{\infty} 4^{m-1} x^m.$$
Hence $b_0 = 1$, and for every $m \ge 1$,
$$b_m = \binom{2m}{m} - 4^{m-1}.$$

Fix an integer $n \ge 0$, and let $M_n := \bigl(b_{i+j}\bigr)_{0 \le i,j \le n} \in \mathbb{Q}^{(n+1)\times(n+1)}$ and $C_n := \bigl(\binom{2(i+j)}{i+j}\bigr)_{0 \le i,j \le n} \in \mathbb{Q}^{(n+1)\times(n+1)}$. Define column vectors $v := (1, 4, 4^2, \dots, 4^n)^T \in \mathbb{Q}^{n+1}$ and $e_0 := (1, 0, \dots, 0)^T \in \mathbb{Q}^{n+1}$. Since $i + j \ge 1$ for all $(i, j) \ne (0, 0)$ while $4^{0-1} = \tfrac{1}{4}$ at $(i, j) = (0, 0)$, entrywise inspection yields
$$M_n = C_n - \frac{1}{4} v v^T + \frac{1}{4} e_0 e_0^T = C_n + U V^T,$$
where $U := \bigl[-\tfrac{1}{4} v,\ \tfrac{1}{4} e_0\bigr] \in \mathbb{Q}^{(n+1)\times 2}$ and $V := [v,\ e_0] \in \mathbb{Q}^{(n+1)\times 2}$.

---

### 2. Exact diagonalization of $C_n$ via Laurent–Chebyshev polynomials

Define monic polynomials $P_k(t) = \sum_{i=0}^{k} p_{k,i} t^i \in \mathbb{Z}[t]$ ($k \ge 0$) by
$$P_0(t) := 1, \qquad P_1(t) := t - 2, \qquad P_2(t) := (t - 2) P_1(t) - 2 P_0(t) = t^2 - 4t + 2,$$
and for $k \ge 3$,
$$P_k(t) := (t - 2) P_{k-1}(t) - P_{k-2}(t).$$

**Lemma 1 (Laurent identity).** *In the Laurent polynomial ring $\mathbb{Z}[z, z^{-1}]$, set $t(z) := z + 2 + z^{-1} = \frac{(1+z)^2}{z}$. Then:*
1. *For all $m \ge 0$, $[z^0]\bigl(t(z)^m\bigr) = \binom{2m}{m}$.*
2. *For all $k \ge 1$, $P_k(t(z)) = z^k + z^{-k}$.*
3. *$P_0(4) = 1$, $P_k(4) = 2$ for $k \ge 1$; and $P_0(0) = 1$, $P_k(0) = 2(-1)^k$ for $k \ge 1$.*

*Proof.*
1. $t(z)^m = \frac{(1+z)^{2m}}{z^m}$, so $[z^0]\bigl(t(z)^m\bigr) = [z^m](1+z)^{2m} = \binom{2m}{m}$.
2. We check by induction on $k \ge 1$: for $k = 1$, $P_1(t(z)) = z + z^{-1}$; for $k = 2$, $(z + z^{-1})^2 - 2 = z^2 + z^{-2}$; for $k \ge 3$,
   $$P_k(t(z)) = (z + z^{-1})(z^{k-1} + z^{-(k-1)}) - (z^{k-2} + z^{-(k-2)}) = z^k + z^{-k}.$$
3. Substituting $z = 1$ ($t(1) = 4$) gives $P_0(4) = 1$ and $P_k(4) = 1^k + 1^{-k} = 2$ ($k \ge 1$). Substituting $z = -1$ ($t(-1) = 0$) gives $P_0(0) = 1$ and $P_k(0) = (-1)^k + (-1)^{-k} = 2(-1)^k$ ($k \ge 1$). $\blacksquare$

Let $P \in \mathbb{Z}^{(n+1)\times(n+1)}$ be the unit lower-triangular matrix with $(P)_{k,i} = p_{k,i}$ for $0 \le i \le k \le n$ (and $0$ for $i > k$). Then for all $0 \le k, \ell \le n$,
$$(P C_n P^T)_{k,\ell} = \sum_{i=0}^{k} \sum_{j=0}^{\ell} p_{k,i} \binom{2(i+j)}{i+j} p_{\ell,j} = [z^0]\bigl(P_k(t(z))\, P_\ell(t(z))\bigr).$$
Using Lemma 1(2):
- $[z^0](1 \cdot 1) = 1$;
- for $k \ge 1$, $[z^0]\bigl(1 \cdot (z^k + z^{-k})\bigr) = 0$;
- for $k, \ell \ge 1$, $[z^0]\bigl((z^k + z^{-k})(z^\ell + z^{-\ell})\bigr) = [z^0]\bigl(z^{k+\ell} + z^{-k-\ell} + z^{k-\ell} + z^{\ell-k}\bigr) = 2\,\delta_{k,\ell}$.

Hence
$$P C_n P^T = D := \mathrm{diag}(d_0, d_1, \dots, d_n), \qquad d_0 = 1,\quad d_k = 2\ (1 \le k \le n).$$
Since $P$ is unit lower-triangular ($\det P = 1$), $C_n$ is invertible,
$$\det(C_n) = \det(D) = 1 \cdot 2^n = 2^n, \qquad \text{and} \qquad C_n^{-1} = P^T D^{-1} P.$$

---

### 3. Determinant via Weinstein–Aronszajn identity

Since $M_n = C_n (I_{n+1} + C_n^{-1} U V^T)$, the Weinstein–Aronszajn determinant identity $\det(I_{n+1} + A B) = \det(I_2 + B A)$ (with $A = C_n^{-1} U$ and $B = V^T$) gives
$$a(n) = \det(M_n) = \det(C_n)\,\det\bigl(I_2 + V^T C_n^{-1} U\bigr) = 2^n\,\det\bigl(I_2 + V^T C_n^{-1} U\bigr).$$
Note that $(P v)_k = \sum_{i=0}^{k} p_{k,i} 4^i = P_k(4)$ and $(P e_0)_k = p_{k,0} = P_k(0)$. Using $C_n^{-1} = P^T D^{-1} P$ and Lemma 1(3):
- $v^T C_n^{-1} v = \sum_{k=0}^{n} \frac{P_k(4)^2}{d_k} = \frac{1^2}{1} + \sum_{k=1}^{n} \frac{2^2}{2} = 2n + 1$,
- $e_0^T C_n^{-1} e_0 = \sum_{k=0}^{n} \frac{P_k(0)^2}{d_k} = \frac{1^2}{1} + \sum_{k=1}^{n} \frac{(2(-1)^k)^2}{2} = 2n + 1$,
- $v^T C_n^{-1} e_0 = e_0^T C_n^{-1} v = \sum_{k=0}^{n} \frac{P_k(4) P_k(0)}{d_k} = \frac{1}{1} + \sum_{k=1}^{n} \frac{2 \cdot 2(-1)^k}{2} = 1 + 2\sum_{k=1}^{n}(-1)^k = (-1)^n$.

Therefore
$$I_2 + V^T C_n^{-1} U = I_2 + \frac{1}{4}\begin{pmatrix} -v^T C_n^{-1} v & v^T C_n^{-1} e_0 \\ -e_0^T C_n^{-1} v & e_0^T C_n^{-1} e_0 \end{pmatrix} = \begin{pmatrix} 1 - \frac{2n+1}{4} & \frac{(-1)^n}{4} \\ -\frac{(-1)^n}{4} & 1 + \frac{2n+1}{4} \end{pmatrix},$$
whose determinant is
$$\left(1 - \frac{2n+1}{4}\right)\left(1 + \frac{2n+1}{4}\right) + \frac{(-1)^{2n}}{16} = 1 - \frac{(2n+1)^2 - 1}{16} = 1 - \frac{4n(n+1)}{16} = 1 - \frac{n(n+1)}{4}.$$
Multiplying by $\det(C_n) = 2^n$ yields
$$a(n) = 2^n\left(1 - \frac{n(n+1)}{4}\right) = 2^n - n(n+1)\,2^{n-2}$$
for all integers $n \ge 0$ (with $n(n+1)\,2^{n-2} = 0$ at $n = 0$).

---

### 4. Ordinary generating function

Using $\sum_{n=0}^{\infty} \binom{n+1}{2} y^n = \frac{y}{(1-y)^3}$ at $y = 2x$ (noting $n(n+1)\,2^{n-2} = \binom{n+1}{2}\,2^{n-1}$):
$$\sum_{n=0}^{\infty} a(n) x^n = \sum_{n=0}^{\infty} 2^n x^n - \frac{1}{2}\sum_{n=0}^{\infty} \binom{n+1}{2} (2x)^n = \frac{1}{1 - 2x} - \frac{x}{(1 - 2x)^3} = \frac{(1 - 2x)^2 - x}{(1 - 2x)^3} = \frac{1 - 5x + 4x^2}{(1 - 2x)^3}.$$
Since $(1 - 4x)(1 - x) = 1 - 5x + 4x^2$ and $(1 - 2x)^3 = -(2x - 1)^3$, we obtain
$$\sum_{n=0}^{\infty} a(n) x^n = -\frac{(4x - 1)(x - 1)}{(2x - 1)^3}. \qquad \blacksquare$$
