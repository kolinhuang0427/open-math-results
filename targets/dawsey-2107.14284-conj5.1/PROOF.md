# Proof of Dawsey–Just–Schneider `arXiv:2107.14284v2` Conjecture 4.1 (`\label{conj1}`)

**Theorem (Conjecture 4.1, `\label{conj1}`, Section 4 `\label{sect5}` of [Dawsey–Just–Schneider, `arXiv:2107.14284v2`]).**
*Let $p_1 < p_2 < p_3 < \cdots$ denote the strictly increasing sequence of all primes $\mathbb{P}$ (with $\mathrm{idx}(p_k) = k$ for $k \ge 1$). Let $f \colon \mathbb{N} \to \mathbb{C}$ be any arithmetic function for which the Cesàro average*
$$L_f := \lim_{N \to \infty} \frac{1}{N} \sum_{k=1}^{N} f(k)$$
*exists as a finite complex limit. Then for every real $s > 1$, the ordered Dirichlet series $\sum_{p \in \mathbb{P}} f(\mathrm{idx}(p)) p^{-s} := \lim_{M \to \infty} \sum_{k=1}^{M} f(k) p_k^{-s}$ converges, and*
$$\lim_{s \to 1^+} \frac{\sum_{p \in \mathbb{P}} f(\mathrm{idx}(p)) p^{-s}}{\sum_{p \in \mathbb{P}} p^{-s}} = L_f.$$

## Proof

For $N \ge 1$, set $S_N := \sum_{k=1}^{N} f(k)$, and set $S_0 := 0$. Because $S_N / N \to L_f$ as $N \to \infty$, the sequence $(S_N / N)_{N \ge 1}$ is bounded: there exists a constant $C > 0$ such that
$$|S_k| \le C k \quad \text{for all } k \ge 1.$$
Write
$$P(s) := \sum_{p \in \mathbb{P}} p^{-s} = \sum_{k=1}^{\infty} p_k^{-s} \quad (s > 1).$$
Since $p_k \ge k$ for all $k \ge 1$ and $s > 1$, we have $0 < P(s) \le \zeta(s) < \infty$.

### Step 1: Convergence and Abel summation identity for $s > 1$

Fix any real $s > 1$. For any integers $1 \le N \le M$, summation by parts gives
$$\sum_{k=N}^{M} f(k) p_k^{-s} = S_M p_M^{-s} - S_{N-1} p_N^{-s} + \sum_{k=N}^{M-1} S_k \bigl(p_k^{-s} - p_{k+1}^{-s}\bigr).$$
Observe two bounds:
1. Since $p_M \ge M$ and $|S_M| \le C M$, we have $|S_M p_M^{-s}| \le C M^{1-s} \to 0$ as $M \to \infty$ (as $s > 1$).
2. Since $(p_k)_{k \ge 1}$ is strictly increasing, $p_k^{-s} - p_{k+1}^{-s} > 0$ for every $k \ge 1$. Telescoping gives, for every $M \ge 2$,
   $$\sum_{k=1}^{M-1} k \bigl(p_k^{-s} - p_{k+1}^{-s}\bigr) = \sum_{k=1}^{M-1} p_k^{-s} - (M - 1) p_M^{-s} \le \sum_{k=1}^{M-1} p_k^{-s} < P(s).$$
   Combining this with $|S_k| \le C k$ shows that $\sum_{k=1}^{\infty} |S_k| (p_k^{-s} - p_{k+1}^{-s}) \le C P(s) < \infty$, so $\sum_{k=1}^{\infty} S_k (p_k^{-s} - p_{k+1}^{-s})$ converges absolutely.

Taking $N = 1$ and letting $M \to \infty$, we conclude that $\sum_{k=1}^{\infty} f(k) p_k^{-s} = \lim_{M \to \infty} \sum_{k=1}^{M} f(k) p_k^{-s}$ converges for every real $s > 1$ and equals
$$\sum_{k=1}^{\infty} f(k) p_k^{-s} = \sum_{k=1}^{\infty} S_k \bigl(p_k^{-s} - p_{k+1}^{-s}\bigr).$$
In particular, applying the same identity to the constant function $f \equiv 1$ (for which $S_k = k$ and $L_1 = 1$) yields
$$P(s) = \sum_{k=1}^{\infty} k \bigl(p_k^{-s} - p_{k+1}^{-s}\bigr) \quad \text{for every } s > 1.$$

### Step 2: Limit as $s \to 1^+$

Define $\varepsilon_k := \frac{S_k}{k} - L_f$ for $k \ge 1$. By hypothesis, $\lim_{k \to \infty} \varepsilon_k = 0$. Subtracting $L_f P(s)$ from $\sum_{k=1}^{\infty} f(k) p_k^{-s}$ gives, for every $s > 1$,
$$\sum_{k=1}^{\infty} f(k) p_k^{-s} - L_f P(s) = \sum_{k=1}^{\infty} (S_k - L_f k)\bigl(p_k^{-s} - p_{k+1}^{-s}\bigr) = \sum_{k=1}^{\infty} \varepsilon_k \, k \bigl(p_k^{-s} - p_{k+1}^{-s}\bigr).$$
Let $\eta > 0$ be arbitrary. Choose $K \in \mathbb{N}$ such that $|\varepsilon_k| < \eta / 2$ for all $k > K$. Using $p_k^{-s} - p_{k+1}^{-s} > 0$, we obtain for every $s > 1$:
$$\begin{aligned}
\left| \frac{\sum_{k=1}^{\infty} f(k) p_k^{-s}}{P(s)} - L_f \right|
&\le \frac{1}{P(s)} \sum_{k=1}^{K} |\varepsilon_k| \, k \bigl(p_k^{-s} - p_{k+1}^{-s}\bigr)
   + \frac{\eta}{2 P(s)} \sum_{k=K+1}^{\infty} k \bigl(p_k^{-s} - p_{k+1}^{-s}\bigr) \\
&\le \frac{C_K}{P(s)} + \frac{\eta}{2},
\end{aligned}$$
where in the first sum we used $0 < p_k^{-s} - p_{k+1}^{-s} < p_k^{-s} < p_k^{-1}$ to bound it independently of $s > 1$ by the finite constant $C_K := \sum_{k=1}^{K} |\varepsilon_k| k p_k^{-1}$, and in the second sum we used
$$\sum_{k=K+1}^{\infty} k \bigl(p_k^{-s} - p_{k+1}^{-s}\bigr) \le \sum_{k=1}^{\infty} k \bigl(p_k^{-s} - p_{k+1}^{-s}\bigr) = P(s).$$

Finally, by Euler's theorem on the divergence of the prime harmonic series, $\sum_{k=1}^{\infty} p_k^{-1} = \infty$. For any $M \in \mathbb{N}$ and any $s > 1$, $P(s) > \sum_{k=1}^{M} p_k^{-s}$, so $\liminf_{s \to 1^+} P(s) \ge \sum_{k=1}^{M} p_k^{-1}$ for every $M$; hence $\lim_{s \to 1^+} P(s) = +\infty$. Thus there exists $\delta > 0$ such that for all $s \in (1, 1 + \delta)$, $\frac{C_K}{P(s)} < \frac{\eta}{2}$, and consequently
$$\left| \frac{\sum_{p \in \mathbb{P}} f(\mathrm{idx}(p)) p^{-s}}{\sum_{p \in \mathbb{P}} p^{-s}} - L_f \right| < \eta.$$
Since $\eta > 0$ was arbitrary, the limit equals $L_f$. $\blacksquare$
