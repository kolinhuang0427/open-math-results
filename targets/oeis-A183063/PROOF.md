# Proof of OEIS A183063 Cotangent Limit Conjecture

## Theorem

For each integer $n \ge 1$, let $a(n) = A183063(n)$ denote the number of positive even divisors of $n$. Define
$$f(u) := \sin(u) \sum_{k=1}^{\infty} \left(\frac{1}{2k}\cot\!\left(\frac{u}{2k}\right) - \frac{1}{u}\right).$$
Then for every $x \in \mathbb{R} \setminus 2\mathbb{Z}$ (and $x \ne 0$) the series defining $f(\pi x)$ converges absolutely, and for every integer $n \ge 1$,
$$\lim_{x \to n} f(\pi x) = a(n).$$

---

## Proof

For $x \in \mathbb{R} \setminus 2\mathbb{Z}$ and $k \in \mathbb{Z}_{\ge 1}$, we have $\frac{x}{2k} \notin \mathbb{Z}$ (hence $\frac{\pi x}{2k} \notin \pi\mathbb{Z}$), so each summand
$$g_k(x) := \frac{1}{2k}\cot\!\left(\frac{\pi x}{2k}\right) - \frac{1}{\pi x}$$
is finite and smooth in a neighborhood of $x$.

### 1. Uniform convergence of the tail via Mittag–Leffler partial fractions

Recall the standard Mittag–Leffler partial-fraction expansion of $\cot u$, valid for all $u \in \mathbb{R} \setminus \pi\mathbb{Z}$:
$$\cot u - \frac{1}{u} = -\sum_{m=1}^{\infty} \frac{2u}{m^2\pi^2 - u^2}.$$
Fix an integer $n \ge 1$, and restrict $x$ to the compact interval $J_n := \bigl[n - \tfrac{1}{2},\, n + \tfrac{1}{2}\bigr]$ (with $x \ne n$ in the limit). Note that $0 < n - \frac{1}{2} \le x \le n + \frac{1}{2}$.

For every $k \ge n + 1$ and every $x \in J_n$, setting $u := \frac{\pi x}{2k}$ gives
$$0 < u \le \frac{\pi\bigl(n + \frac{1}{2}\bigr)}{2(n+1)} < \frac{\pi}{2}.$$
In particular, $\frac{\pi x}{2k} \notin \pi\mathbb{Z}$ so $g_k$ is smooth on $J_n$, and for every $m \ge 1$,
$$m^2\pi^2 - u^2 \ge \pi^2\left(m^2 - \frac{1}{4}\right) \ge \frac{3}{4} m^2 \pi^2.$$
Therefore, uniformly for all $x \in J_n$ and all $k \ge n + 1$,
$$|g_k(x)| = \frac{1}{2k}\left|\cot u - \frac{1}{u}\right| \le \frac{1}{2k} \sum_{m=1}^{\infty} \frac{2u}{m^2\pi^2 - u^2} \le \frac{1}{2k} \sum_{m=1}^{\infty} \frac{2 \cdot \frac{\pi(n + 1/2)}{2k}}{\frac{3}{4}m^2\pi^2} = \frac{2n+1}{3\pi\, k^2}\sum_{m=1}^{\infty} \frac{1}{m^2} = \frac{(2n+1)\pi}{18\, k^2}.$$
(For any fixed $x \in \mathbb{R} \setminus (2\mathbb{Z} \cup \{0\})$, the same estimate holds for all $k > |x|$, proving absolute convergence of $\sum_{k=1}^{\infty} g_k(x)$ everywhere on $\mathbb{R} \setminus 2\mathbb{Z}$.)

Because $\sum_{k=n+1}^{\infty} \frac{1}{k^2} < \infty$, the Weierstrass M-test implies that the tail series
$$R_n(x) := \sum_{k=n+1}^{\infty} g_k(x)$$
converges uniformly on $J_n = [n - \tfrac{1}{2}, n + \tfrac{1}{2}]$ to a continuous function $R_n : J_n \to \mathbb{R}$. Since $\sin(\pi n) = 0$,
$$\lim_{x \to n} \sin(\pi x)\, R_n(x) = \sin(\pi n)\, R_n(n) = 0.$$

---

### 2. Evaluation of the finite head ($1 \le k \le n$)

Write $f(\pi x) = \sum_{k=1}^{n} \sin(\pi x)\, g_k(x) + \sin(\pi x)\, R_n(x)$ for $x \in J_n \setminus \{n\}$. For each $k \in \{1, 2, \dots, n\}$, there are two cases:

1. **$2k \nmid n$:** Then $\frac{n}{2k} \notin \mathbb{Z}$, so $\frac{\pi n}{2k} \notin \pi\mathbb{Z}$ and $g_k(x)$ is continuous at $x = n$. Because $\sin(\pi n) = 0$,
   $$\lim_{x \to n} \sin(\pi x)\, g_k(x) = \sin(\pi n)\, g_k(n) = 0.$$

2. **$2k \mid n$:** Write $n = 2km$ for some integer $m \ge 1$. In particular $n$ is even, so $(-1)^n = 1$. Setting $h := x - n$ ($h \to 0,\ h \ne 0$) gives
   $$\sin(\pi x) = \sin(\pi n + \pi h) = (-1)^n \sin(\pi h) = \sin(\pi h),$$
   $$\cot\!\left(\frac{\pi x}{2k}\right) = \cot\!\left(m\pi + \frac{\pi h}{2k}\right) = \cot\!\left(\frac{\pi h}{2k}\right),$$
   by $\pi$-periodicity of $\cot$. Thus,
   $$\sin(\pi x)\, g_k(x) = \frac{\sin(\pi h)}{2k}\cot\!\left(\frac{\pi h}{2k}\right) - \frac{\sin(\pi h)}{\pi(n+h)} = \frac{\sin(\pi h)}{\pi h}\cdot\frac{\frac{\pi h}{2k}}{\sin\!\left(\frac{\pi h}{2k}\right)}\cdot\cos\!\left(\frac{\pi h}{2k}\right) - \frac{\sin(\pi h)}{\pi(n+h)}.$$
   Using $\lim_{u \to 0} \frac{\sin u}{u} = 1$, $\lim_{u \to 0} \cos u = 1$, and $n \ge 1$, we obtain
   $$\lim_{x \to n} \sin(\pi x)\, g_k(x) = 1 \cdot 1 \cdot 1 - 0 = 1.$$

---

### 3. Conclusion

Summing the limits over $1 \le k \le n$ and adding the tail limit $\lim_{x \to n} \sin(\pi x)\, R_n(x) = 0$ gives
$$\lim_{x \to n} f(\pi x) = \sum_{\substack{1 \le k \le n \\ 2k \mid n}} 1 = \#\{k \in \mathbb{Z}_{\ge 1} : 2k \mid n\} = \#\{d \in \mathbb{Z}_{\ge 1} : 2 \mid d \text{ and } d \mid n\} = a(n). \qquad \blacksquare$$
