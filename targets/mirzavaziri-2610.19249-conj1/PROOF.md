# Complete Proof of Guo–Krattenthaler Conjecture 7.4 and Mirzavaziri–Yaqubi Conjecture 4.4

## 1. Exact Statements and Main Theorem

**Primary Sources:**
1. V. J. W. Guo and C. Krattenthaler, *Some divisibility properties of binomial and $q$-binomial coefficients*, J. Number Theory **135** (2014), 167–184 (`arXiv:1301.7651v3`, Section 7, Conjecture 7.4, `\label{conj:330n88n}`).
2. M. Mirzavaziri and D. Yaqubi, *Graph binomial coefficients and a positivity conjecture of Guo and Krattenthaler*, `arXiv:2610.19249v1` (Oct 13, 2026; Section 1 Conjecture 1.1 `\label{conj:GK}` and Section 4 Conjecture 4.4 `\label{conj:general}`).

Let $[n]_q = \frac{1-q^n}{1-q} = 1 + q + \dots + q^{n-1}$ and let $\begin{bmatrix} N \\ k \end{bmatrix}_q = \prod_{i=0}^{k-1}\frac{1-q^{N-i}}{1-q^{i+1}}$ denote the Gaussian polynomial ($q$-binomial coefficient). For an integer $m \ge 1$, set $a = 2m - 1$, $b = 3m - 1$, $G_m(q) = \begin{bmatrix} 6m \\ m \end{bmatrix}_q$, and
$$P^{(m)}(q) := \frac{(1-q)^2}{(1-q^{2m-1})(1-q^{3m-1})} \begin{bmatrix} 6m \\ m \end{bmatrix}_q = \frac{G_m(q)}{[a]_q [b]_q}.$$

**Conjecture 4.4 (`conj:general`, `arXiv:2610.19249v1`, Section 4):**
> Let $m \ge 9$ (or $m = 5$) with $m \not\equiv 2, 3 \pmod 5$. Then the polynomial
> $$P^{(m)}(q) = \frac{(1-q)^2}{(1-q^{2m-1})(1-q^{3m-1})} \begin{bmatrix} 6m \\ m \end{bmatrix}_q$$
> has non-negative coefficients, except for the coefficients of $q^1$ and $q^{5m^2 - 5m + 3}$, which are equal to $-1$.

**Conjecture 1.1 (`conj:GK` = Guo–Krattenthaler Conjecture 7.4, `arXiv:1301.7651v3`, Section 7):**
> For all positive integers $n$ and all $0 \le k \le 125n^2 - 25n + 4$, the coefficient of $q^k$ in the polynomial
> $$P_n(q) = \frac{(1-q)^2}{(1-q^{10n-1})(1-q^{15n-1})} \begin{bmatrix} 30n \\ 5n \end{bmatrix}_q$$
> is non-negative, except for $k = 1$ and $k = 125n^2 - 25n + 3$, where the coefficient equals $-1$.

**Theorem (Main Result).** *Conjecture 4.4 (`conj:general`) holds for every integer $m \in \{5\} \cup \{m \ge 9 : m \not\equiv 2, 3 \pmod 5\}$. Specializing to $m = 5n$ ($n \ge 1$), Guo–Krattenthaler Conjecture 7.4 (`conj:GK`, Conjecture 1.1) holds for every positive integer $n$.*

**Scope Note.** Conjecture 4.5 (`conj:almost`, Section 4 of `arXiv:2610.19249v1`, predicting weak monotonicity of $U_m(q) = \begin{bmatrix} 6m \\ m \end{bmatrix}_q/[2m-1]_q$ from $q^1$ to its middle coefficient) is **not** claimed here and remains open for $m > 300$.

**Proof Architecture.**
- **Section 2 (Polynomiality, Reciprocity, and Boundary Coefficients $0 \le t \le 5m$):** Self-contained cyclotomic proof that $P^{(m)}$ is a reciprocal polynomial of even degree $D_m = 5m^2 - 5m + 4$ whenever $m \not\equiv 2,3 \pmod 5$, together with the partition injection proving $[q^0] P^{(m)} = 1$, $[q^1] P^{(m)} = -1$, and $[q^t] P^{(m)} \ge 0$ for all $2 \le t \le 5m$ when $m \ge 9$. By reciprocity, it remains only to prove $p_t := [q^t] P^{(m)} > 0$ for all $5m < t \le T_m := D_m / 2$.
- **Section 3 (Finite Range $m \le 100$):** Exact arbitrary-precision Python integer verification (`verify.py`, Part A) for all $57$ admissible integers $m \in \{5\} \cup \{9 \le m \le 100 : m \not\equiv 2, 3 \pmod 5\}$ (which covers $1 \le n \le 20$ in `conj:GK`), taking $11.5\text{ s}$.
- **Sections 4–7 (Uniform Analytic + Certified Interval-Arithmetic Proof for all $m \ge 101$):** We sharpen the double contour integral of Mirzavaziri–Yaqubi by replacing crude third-order worst-case bounds with a 4th-order Edgeworth major-arc expansion exploiting odd-cubic cancellation (Lemma 4), a 6-line Exact Trigonometric Splitting bound on the near minor arcs (Lemma 5), Poisson summation on $\gamma = \theta m \ge 3.7$ (Lemma 6), and direct $L^1$-midpoint interval Fourier quadrature plus unimodal layer-cake and Parseval bounds on $0 < \gamma \le 3.7$ (Lemma 7). Every analytic constant inequality is rigorously certified in zero-float directed-rounding interval arithmetic (`mpmath.iv` at $25$ decimal digits; `verify.py`, Part B, taking $6.3\text{ s}$), yielding a strictly positive net margin $\ge +0.154579$ uniformly over all $m \ge 101$ and all $5m < t \le T_m$.

---

## 2. Polynomiality, Reciprocity, and Boundary Coefficients $0 \le t \le 5m$

For completeness we include self-contained proofs of the combinatorial and cyclotomic results of `arXiv:2610.19249v1` (Sections 2–4).

### Proposition 1 (Polynomiality and Reciprocity)
*For $m \ge 1$, $P^{(m)}(q)$ is a polynomial if and only if $m \not\equiv 2, 3 \pmod 5$. In that case, $P^{(m)}(q)$ is a reciprocal polynomial of even degree $D_m = 5m^2 - 5m + 4$ (so $p_{D_m - t} = p_t$ for all $0 \le t \le D_m$).*

**Proof.** Writing $q^n - 1 = \prod_{d \mid n} \Phi_d(q)$ in terms of cyclotomic polynomials $\Phi_d$, we have $P^{(m)}(q) = \prod_{d \ge 2} \Phi_d(q)^{e_d}$, where
$$e_d = -\mathbf{1}_{d \mid (2m-1)} - \mathbf{1}_{d \mid (3m-1)} + \left\lfloor \frac{6m}{d} \right\rfloor - \left\lfloor \frac{m}{d} \right\rfloor - \left\lfloor \frac{5m}{d} \right\rfloor.$$
Since $(3m-1) - (2m-1) = m$ and $\gcd(2m-1, m) = 1$, we have $\gcd(2m-1, 3m-1) = 1$, so at most one indicator is $1$. Write $m = Qd + x$ with $0 \le x < d$ and $X = x/d \in [0, 1)$. Then $\lfloor 6m/d \rfloor - \lfloor m/d \rfloor - \lfloor 5m/d \rfloor = \lfloor 6X \rfloor - \lfloor 5X \rfloor \ge 0$.
- **Case $d \mid 2m - 1$:** Then $d \mid 2x - 1$. Since $-1 \le 2x - 1 < 2d$ and $d \ge 2$, we must have $2x - 1 = d$, so $d$ is odd and $X = \frac{d+1}{2d}$. Hence $\lfloor 6X \rfloor - \lfloor 5X \rfloor = \lfloor 3 + 3/d \rfloor - \lfloor 5/2 + 5/(2d) \rfloor$, which equals $1$ for $d = 3$ and every odd $d \ge 7$, and equals $0$ for $d = 5$ (giving $e_5 = -1 \iff 5 \mid 2m - 1 \iff m \equiv 3 \pmod 5$).
- **Case $d \mid 3m - 1$:** Then $3x - 1 \in \{d, 2d\}$.
  - If $3x - 1 = d$, then $d \equiv 2 \pmod 3$ ($d \ne 4$) and $X = \frac{d+1}{3d}$, so $\lfloor 6X \rfloor - \lfloor 5X \rfloor = \lfloor 2 + 2/d \rfloor - \lfloor 5/3 + 5/(3d) \rfloor$, which equals $1$ for $d = 2$ and every $d \ge 8$, and equals $0$ for $d = 5$ (giving $e_5 = -1 \iff 5 \mid 3m-1 \iff m \equiv 2 \pmod 5$).
  - If $3x - 1 = 2d$, then $d \ge 4$ ($d \equiv 1 \pmod 3$) and $X = \frac{2d+1}{3d}$, so $\lfloor 6X \rfloor - \lfloor 5X \rfloor = \lfloor 4 + 2/d \rfloor - \lfloor 10/3 + 5/(3d) \rfloor = 4 - 3 = 1$.

Thus $e_d \ge 0$ for all $d \ge 2$ iff $m \not\equiv 2,3 \pmod 5$. Its degree is $5m^2 - (2m - 2) - (3m - 2) = 5m^2 - 5m + 4 = D_m$, which is even since $m(m-1)$ is even. Because $G_m(q)$, $[2m-1]_q$, and $[3m-1]_q$ are reciprocal, so is $P^{(m)}(q)$. $\square$

### Proposition 2 (Boundary Coefficients $0 \le t \le 5m$ for $m \ge 9$)
*Let $m \ge 9$ with $m \not\equiv 2, 3 \pmod 5$. Then $p_0 = 1$, $p_1 = -1$, and $p_t \ge 0$ for all $2 \le t \le 5m$. By reciprocity, $p_{D_m} = 1$, $p_{D_m - 1} = -1$, and $p_t \ge 0$ for all $D_m - 5m \le t \le D_m - 2$.*

**Proof.** For $k \ge 9$, let $\mathcal{P}(n)$ be the set of partitions of $n$ into parts from $\{2, 3, \dots, k\}$, $h_k(n) = |\mathcal{P}(n)|$ ($h_k(n) = 0$ for $n < 0$), and $d_k(n) = h_k(n) - h_k(n-1)$, so that $\sum_{n \ge 0} d_k(n) q^n = \frac{(1-q)^2}{(q;q)_k}$, where $(q;q)_k = \prod_{j=1}^k (1 - q^j)$.

We first show $d_k(n) \ge 0$ for all $n \ge 2$ and $d_k(n) \ge 1$ for all $n \ge 8$. Define $\iota : \mathcal{P}(n-1) \to \mathcal{P}(n)$ for $n \ge 2$ (vacuously for $n=2$ since $\mathcal{P}(1) = \emptyset$). Given $\lambda \in \mathcal{P}(n-1)$:
1. If $\lambda$ contains a part $2$, replace one part $2$ by $3$.
2. Otherwise, let $r \ge 0$ be the multiplicity of $3$ in $\lambda$, and let $\nu$ be $\lambda$ with all parts $3$ removed (so every part of $\nu$ lies in $\{4, \dots, k\}$):
   - (2a) If $r$ is odd, set $\iota(\lambda) = \nu \cup 2^{(3r+1)/2}$.
   - (2b) If $r \ge 2$ is even, set $\iota(\lambda) = \nu \cup \{5\} \cup 2^{(3r-4)/2}$.
   - (2c) If $r = 0$ and the largest part $\lambda_1 < k$, increase one copy of $\lambda_1$ by $1$.
   - (2d) If $r = 0$ and $\lambda_1 = k$, replace one part $k$ by $k-5, 2, 2, 2$ (valid since $k - 5 \ge 4$).

In every case the parts lie in $\{2, \dots, k\}$ and the weight increases by $1$. Let $j$ be the multiplicity of $2$ in $\mu = \iota(\lambda)$: images of (1) contain a $3$, while images of (2a)–(2d) contain no $3$ and satisfy $j \equiv 2 \pmod 3$ in (2a), $j \equiv 1 \pmod 3$ in (2b), $j = 0$ in (2c), and $j = 3$ in (2d). Thus the five images are pairwise disjoint, and each branch is visibly injective (in (2c), the largest part of $\mu$ is unique; in (2d), $k-5$ is fixed). Hence $d_k(n) \ge 0$ for all $n \ge 2$. For $n \ge 8$, write $n - 2$ as a sum of elements of $\{4, 6, 7, 8, 9\} \subseteq \{4, \dots, k\}$ (base cases $6, 7, 8, 9$; induction via $(N - 4) + 4$ for $N \ge 10$) to obtain $\rho \vdash n - 2$; then $\mu = \rho \cup \{2\} \in \mathcal{P}(n)$ has no $3$, no $5$, and $j = 1$, so $\mu \notin \mathrm{im}(\iota)$ and $d_k(n) \ge 1$.

Now set $a = 2m - 1 \ge 17$, $b = 3m - 1 \ge 26$, and write $\frac{1}{(1-q^a)(1-q^b)} = \sum_{n \ge 0} N(n) q^n$, where $N(n) = |\{(i, j) \in \mathbb{N}^2 : ia + jb = n\}|$ ($N(n) = 0$ for $n < 0$). Since $\begin{bmatrix} 6m \\ m \end{bmatrix}_q = \frac{\prod_{j=1}^m (1 - q^{5m+j})}{(q;q)_m} \equiv \frac{1}{(q;q)_m} \pmod{q^{5m+1}}$, we have for all $0 \le t \le 5m$:
$$p_t = [q^t] \frac{(1-q)^2}{(1-q^a)(1-q^b)(q;q)_m} = \sum_{n=0}^{t} N(n)\, d_m(t - n).$$
For $t = 0, 1$ this gives $p_0 = 1$, $p_1 = -1$. For $2 \le t \le 5m$, the only negative summand is $n = t - 1$, contributing $-N(t - 1)$. Since $a \ne b$ and $a + 1, b + 1 \ge 8$, the two distinct indices $n_1 = t - 1 - a$ and $n_2 = t - 1 - b$ (when $\ge 0$) satisfy $d_m(t - n_1) \ge 1$ and $d_m(t - n_2) \ge 1$. Every solution $(i, j) \in \mathbb{N}^2$ of $ia + jb = t - 1 \ge 1$ has $i \ge 1$ or $j \ge 1$, yielding either $(i-1, j)$ for $t - 1 - a$ or $(i, j-1)$ for $t - 1 - b$, so $N(t - 1) \le N(t - 1 - a) + N(t - 1 - b)$. Hence $p_t \ge 0$ for all $2 \le t \le 5m$. $\square$

Since $D_m$ is even, $T_m := D_m / 2 = \frac{5m^2 - 5m}{2} + 2$ is an integer, and $t \mapsto D_m - t$ maps $(T_m, D_m - 5m)$ bijectively onto $(5m, T_m)$. Therefore, for every admissible $m \ge 9$, Conjecture 4.4 follows from
$$p_t > 0 \qquad \text{for all } 5m < t \le T_m. \tag{1}$$

---

## 3. Exact Verification of the Finite Range $m \le 100$

Part A of `verify.py` verifies all $57$ admissible values $m \in \{5\} \cup \{9 \le m \le 100 : m \not\equiv 2, 3 \pmod 5\}$ directly in exact arbitrary-precision Python `int` arithmetic:
1. Build $G_m(q) \bmod q^{T_m + 1}$ iteratively via $G_{6m, i+1}(q) = G_{6m, i}(q) \cdot \frac{1 - q^{6m - i}}{1 - q^{i+1}}$ ($i = 0, \dots, m-1$), multiplying by $1 - q^{6m-i}$ and applying the exact recurrence $x_j = y_j + x_{j-(i+1)}$ for division by $1 - q^{i+1}$.
2. Multiply by $1 - q$ and divide by $1 - q^{2m-1}$ $\bmod q^{T_m + 1}$, then multiply by $1 - q$ and divide by $1 - q^{3m-1}$ $\bmod q^{T_m + 1}$, obtaining the exact integer coefficients $p_0, p_1, \dots, p_{T_m}$ of $P^{(m)}(q)$.
3. Confirm $p_0 = 1$, $p_1 = -1$, and $p_k \ge 0$ for all $2 \le k \le T_m$. By Proposition 1 (reciprocity), this establishes Conjecture 4.4 for all $57$ values (and `conj:GK`, Conjecture 1.1, for all $1 \le n \le 20$). As an additional cross-check, Part A also runs full-degree ($0 \le k \le D_m$) exact division with explicit zero-remainder and reciprocity assertions on $m \in \{5, 9, 10, 11, 14, 15, 20\}$.

All $57$ cases pass with zero failures in $11.51\text{ s}$. Henceforth we fix an admissible integer $m \ge m_0 := 101$ and an integer $t$ with $5m < t \le T_m$, and prove (1).

---

## 4. Cauchy Double Integral, Saddle Point, Moments, and $K$-Bounds ($m \ge 101$)

Let $N = 6m$, $a = 2m - 1$, $b = 3m - 1$, $t' = t + \binom{m}{2}$, and
$$F(w, z) = \prod_{j=0}^{N-1} (1 + w z^j), \qquad K(z) = \frac{(1 - z)^2}{(1 - z^a)(1 - z^b)} = \frac{1}{[a]_z [b]_z}.$$
Since $[w^m] F(w, z) = z^{\binom{m}{2}} G_m(z)$ and $K$ is analytic in $|z| < 1$, Cauchy's integral formula gives for any $\lambda \in \mathbb{R}$ and $\theta > 0$ (putting $\rho = e^\lambda$, $r = e^{-\theta}$, $\mu = \lambda/\theta$, $s = 1/\theta$, $\gamma = \theta m = m/s$):
$$p_t = F(\rho, r) \rho^{-m} r^{-t'} K(r) \cdot I, \qquad I = \frac{1}{4\pi^2} \iint_{[-\pi, \pi)^2} \Phi(\psi, \varphi) e^{-i(m\psi + t'\varphi)} \frac{K(r e^{i\varphi})}{K(r)}\,d\psi\,d\varphi, \tag{2}$$
where the prefactor $F(\rho, r)\rho^{-m} r^{-t'} K(r)$ is strictly positive, and
$$p(u) := \frac{1}{1 + e^u}, \qquad v(u) := p(u)(1 - p(u)) = \frac{e^u}{(1 + e^u)^2}, \qquad p_j := p\bigl(\theta(j - \mu)\bigr), \qquad v_j := v\bigl(\theta(j - \mu)\bigr),$$
$$\Phi(\psi, \varphi) := \prod_{j=0}^{N-1} \bigl(1 - p_j + p_j e^{i(\psi + j\varphi)}\bigr).$$
Define the tilted moments
$$V := \sum_{j=0}^{N-1} v_j, \qquad \bar\jmath := \frac{1}{V}\sum_{j=0}^{N-1} j v_j, \qquad W := \sum_{j=0}^{N-1} v_j(j - \bar\jmath)^2, \qquad S_3 := \sum_{j=0}^{N-1} v_j(j - \bar\jmath)^3, \qquad M_r := \sum_{j=0}^{N-1} v_j|j - \bar\jmath|^r.$$
Changing variables to $\alpha \in [-\pi, \pi)$ with $\alpha \equiv \psi + \bar\jmath\varphi \pmod{2\pi}$ and setting $\tilde{s}_j := \alpha + (j - \bar\jmath)\varphi$ leaves $I$ unchanged, satisfies $\sum_j v_j \tilde{s}_j^2 = V\alpha^2 + W\varphi^2 =: Q$, and satisfies $\Phi(\psi, \varphi)e^{-i(m\psi + t'\varphi)} = \prod_{j=0}^{N-1} (1 - p_j + p_j e^{i\tilde{s}_j}) e^{-i p_j \tilde{s}_j}$ whenever $\sum_j p_j = m$ and $\sum_j j p_j = t'$. It suffices to prove $\tilde{I} := 2\pi\sqrt{VW} \mathrm{Re} I > 0$.

### Lemma 1 (Unique Saddle Point and Sharp Scale Bounds)
*For every $m \ge 101$ and $5m < t \le T_m$, there exists a unique $(\lambda, \theta) \in \mathbb{R} \times (0, \infty)$ such that $\sum_{j=0}^{6m-1} p_j = m$ and $\sum_{j=0}^{6m-1} j p_j = t'$. It satisfies*
$$\frac{4}{9 m^2} \le \theta < \frac{1}{c_s \sqrt{m}}, \qquad \text{equivalently} \qquad c_s \sqrt{m} < s \le \frac{9}{4} m^2, \qquad \text{with } c_s = 1.709.$$

**Proof.** Existence, uniqueness, and the lower bound $\theta \ge \frac{4}{9m^2}$ are immediate: for fixed $\theta \ge 0$, $\lambda \mapsto \sum_j p_j$ is a strictly increasing bijection $\mathbb{R} \to (0, 6m)$, defining $\lambda(\theta)$ with $\lambda'(\theta) = \bar\jmath$ and $E(\theta) := \sum_j j p_j$ satisfying $E'(\theta) = -W < 0$, $E(0) = \binom{m}{2} + \frac{5}{2}m^2$, and $\lim_{\theta \to \infty} E(\theta) = \binom{m}{2}$. Since $W \le \frac{1}{4}\sum_{j=0}^{6m-1}(j - \frac{6m-1}{2})^2 < \frac{(6m)^3}{48} = 4.5 m^3$ and $t \le \frac{5}{2}m^2 - \frac{5}{2}m + 2$, we get $4.5 m^3 \theta \ge E(0) - E(\theta) = \frac{5}{2}m^2 - t \ge \frac{5}{2}m - 2 \ge 2m$ (for $m \ge 4$), so $\theta \ge \frac{4}{9m^2}$.

For the upper bound, set $\tau(\theta) := E(\theta) - \binom{m}{2}$ (strictly decreasing, $\tau(\theta_{\mathrm{saddle}}) = t > 5m$) and $\theta_1 := \frac{1}{c_s \sqrt{m}}$. Using $\sum_{j=0}^{6m-1} p_j = m$, we have $\sum_{j=0}^{m-1}(1 - p_j) = \sum_{j=m}^{6m-1} p_j$. At $\theta = \theta_1$:
- If $\mu = m - \frac12$, the terms $1 - p_{m-1-k}$ and $p_{m+k}$ ($0 \le k \le m-1$) cancel identically, leaving $\sum_{j=0}^{6m-1} p_j = m + \sum_{j=2m}^{6m-1} p_j > m$, so $\mu < m - \frac12$.
- If $\mu = m - 1$, then $1 - p_{m-1} = \frac12$ while $1 - p_{m-1-k} = p_{m-1+k}$ ($1 \le k \le m-1$), leaving
  $$\sum_{j=0}^{6m-1} p_j = m - \frac{1}{2} + \sum_{k=m}^{5m} \frac{1}{1 + e^{\theta_1 k}} < m - \frac{1}{2} + \frac{e^{-\theta_1 m}}{1 - e^{-\theta_1}}.$$
  Using $1 - e^{-\theta_1} \ge \theta_1(1 - \theta_1/2)$, we have $\frac{e^{-\theta_1 m}}{1 - e^{-\theta_1}} \le \frac{c_s\sqrt{m}}{1 - 1/(2 c_s\sqrt{m})} e^{-\sqrt{m}/c_s}$, which is strictly decreasing for $\sqrt{m} > c_s$ and evaluates to $\le 0.049413 < \frac12$ at $m = 101$ (`verify.py`). Thus $\sum p_j < m$ at $\mu = m - 1$, forcing $m - 1 < \mu < m - \frac12$.

Now rewrite $\tau(\theta_1)$ using $\sum_{j \ge m} p_j - \sum_{j < m}(1 - p_j) = 0$:
$$\tau(\theta_1) = \sum_{j=m}^{6m-1} (j - m) p_j + \sum_{j=0}^{m-1} (m - j)(1 - p_j) = \frac{1}{\theta_1}\sum_{j=m}^{6m-1} g\bigl(\theta_1(j - \mu)\bigr) + \frac{1}{\theta_1}\sum_{j=0}^{m-1} g\bigl(\theta_1(\mu - j)\bigr),$$
where $g(u) := \frac{u}{1 + e^u}$ on $[0, \infty)$ and every argument is strictly positive because $m - 1 < \mu < m - \frac12$. Note that $g'(u) = \frac{1 + (1-u)e^u}{(1+e^u)^2}$ vanishes at the unique root $u_* > 0$ of $u_* - 1 = e^{-u_*}$, so $g$ is unimodal on $[0, \infty)$ with maximum $g(u_*) = e^{-u_*} = u_* - 1$. Since $u \mapsto u - 1 - e^{-u}$ is strictly increasing and positive at $u = 1.285$ (`verify.py`), we have $g_{\max} := g(u_*) < 0.285$. For any unimodal nonnegative function $g$ on $[0, \infty)$ and any step $h > 0$, $a \ge 0$, splitting at the grid point $k_1$ immediately below $u_*$ gives $h\sum_{k \ge 0} g(a + kh) \le \int_0^\infty g(u)\,du + h g_{\max}$ (each term except $k_1, k_1 + 1$ is bounded by an adjacent integral cell of width $h$, while $h\min(g_{k_1}, g_{k_1+1}) \le \int_{a+k_1 h}^{a+(k_1+1)h} g$ and $h\max(g_{k_1}, g_{k_1+1}) \le h g_{\max}$). Since $\int_0^\infty \frac{u}{1+e^u}\,du = \frac{\pi^2}{12}$, both sums together satisfy
$$\frac{\tau(\theta_1)}{m} \le \frac{1}{m}\left(\frac{\pi^2}{6\theta_1^2} + \frac{2 g_{\max}}{\theta_1}\right) = \frac{\pi^2}{6} c_s^2 + \frac{2 g_{\max} c_s}{\sqrt{m}} \le 4.90126 < 5 \qquad (\text{for all } m \ge 101).$$
Hence $\tau(\theta_1) < 5m < t = \tau(\theta_{\mathrm{saddle}})$, giving $\theta_{\mathrm{saddle}} < \theta_1$ and $s > c_s\sqrt{m}$. $\square$

### Lemma 2 ($L^1$ Midpoint Rule, Centered Parameterizations, and Moment Enclosures)
1. **($L^1$ Midpoint Rule).** *For any $f \in C^2([a, b])$ and uniform partition of $[a, b]$ into $n$ subintervals of width $h = (b - a)/n$ with midpoints $x_j = a + (j + \frac12)h$,*
   $$\left| h \sum_{j=0}^{n-1} f(x_j) - \int_a^b f(x)\,dx \right| \le \frac{h^2}{8} \int_a^b |f''(x)|\,dx.$$
   *Proof:* On each cell $[x_j - h/2, x_j + h/2]$, Taylor's formula with integral remainder gives $\int_{x_j-h/2}^{x_j+h/2} f(x)\,dx - h f(x_j) = \int_{x_j-h/2}^{x_j+h/2} \frac12 (\frac{h}{2} - |t - x_j|)^2 f''(t)\,dt$; the Peano kernel is nonnegative and bounded by $h^2/8$. Summing over $j$ proves the bound. $\square$
2. **(Global Derivative Bounds and $L^1$ Norms).** With $v' = v(2p - 1)$, $v'' = v(1 - 6v)$, $v''' = v'(1 - 12v)$, we have globally $|v| \le \frac14$, $|v'| \le \frac{1}{6\sqrt{3}} < 0.097$, $|v''| \le \frac18$, $|v'''| \le 0.14$, and $\int_{-\infty}^\infty |v'(u)|\,du = \frac12$. Exact interval integration on $[0, 22]$ plus the elementary exponential tail on $[22, \infty)$ (where $|v|, |v'|, |v''|, |v'''| \le e^{-u}$) certifies upper bounds $L_1(u^k v) = \int_{-\infty}^\infty |(u^k v(u))''|\,du$ ($0 \le k \le 4$) and $L_1(u^k v') = \int_{-\infty}^\infty |(u^k v'(u))''|\,du$ ($0 \le k \le 3$) in `verify.py`.
3. **(Exact Centered Parameterization of $A$).** Writing $y_j := \frac{j + 1/2}{m} \in (0, 6)$ and $A := -\theta(\mu + \frac12)$, we have $\theta(j - \mu) = A + \gamma y_j = A + \frac{j + 1/2}{s}$ and $B := A + 6\gamma$. Applying the $L^1$ midpoint rule with step $h = 1/m$ to $f(y) = p(A + \gamma y)$ (for which $\int_0^6 |f''(y)|\,dy = \gamma \int_A^B |v'(u)|\,du \le \gamma/2$) yields
   $$\rho := \int_0^6 p(A + \gamma y)\,dy \in \left[1 - \frac{\gamma}{16 m^2},\ 1 + \frac{\gamma}{16 m^2}\right].$$
   Evaluating the integral explicitly gives $\gamma_* := \gamma\rho = \log\frac{1 + e^{-A}}{1 + e^{-A-6\gamma}}$, hence
   $$e^A = \frac{1 - e^{(\rho - 6)\gamma}}{e^{\gamma_*} - 1}, \qquad e^{A + \gamma} = e^{(1 - \rho)\gamma}\frac{1 - e^{(\rho - 6)\gamma}}{1 - e^{-\gamma_*}}, \qquad e^{A + 3\gamma} = \frac{\mathrm{sinhc}\bigl((3 - \rho/2)\gamma\bigr)}{\mathrm{sinhc}\bigl((\rho/2)\gamma\bigr)} \cdot \frac{6 - \rho}{\rho},$$
   where $\mathrm{sinhc}(x) := \frac{\sinh x}{x}$ is even, positive, and strictly increasing on $[0, \infty)$. The second formula keeps $u(y) = (A + \gamma) + \gamma(y - 1)$ tight on $\gamma \ge \frac12$, and the third keeps $u(y) = (A + 3\gamma) + \gamma(y - 3)$ tight and singularity-free through $\gamma \to 0^+$.
4. **(Alternating Tail Bound and Exact Moment Shifts).** For all $u > 0$, setting $x = e^{-u} \in (0, 1)$, we have $(x - 2x^2 + 3x^3)(1 + x)^2 - x = 4x^4 + 3x^5 > 0$, hence $0 < |v'(u)| \le v(u) \le e^{-u} - 2e^{-2u} + 3e^{-3u}$, and $\int_a^\infty v(u)\,du = p(a)$ exactly. For any fixed center $c$ and $\delta := \bar\jmath - c$, writing $z_j = j - c$ and using $\sum v_j z_j = V\delta$, the exact shift identities
   $$W = W_c - V\delta^2, \qquad S_3 = S_{3,c} - 3\delta W_c + 2 V\delta^3, \qquad M_4 = M_{4,c} - 4\delta S_{3,c} + 6\delta^2 W_c - 3 V\delta^4 \le M_{4,c} + 4|\delta|\sqrt{W_c M_{4,c}} + 6\delta^2 W_c$$
   hold, and similarly $\bigl|\sum v'(u_j)(j - \bar\jmath)^r\bigr| \le \sum_{k=0}^r \binom{r}{k}|\delta|^{r-k}\bigl|\sum v'(u_j) z_j^k\bigr|$.
   In $s$-units ($\gamma \ge \gamma_{\mathrm{lo}} \ge 3.7$, $s \ge s_{\min}$), since $|\gamma_* - \gamma| \le \frac{1}{16 s^2} \le \frac{1}{16 s_{\min}^2} =: \Delta\gamma$, we have $|A| = -A \ge \log(e^{\gamma_{\mathrm{lo}} - \Delta\gamma} - 1) > 2.5$ and $B \ge -\log\frac{e^{-5\gamma_{\mathrm{lo}} + \Delta\gamma}}{1 - e^{-5\gamma_{\mathrm{lo}} + \Delta\gamma}} > 2.5$; comparing discrete sums $\sum_{j=0}^{N-1} u_j^k v(u_j)$ against the exact full-line integrals ($\int v = 1$, $\int u^2 v = \frac{\pi^2}{3}$, $\int u^4 v = \frac{7\pi^4}{15}$, $\int u v' = -1$, $\int u^3 v' = -\pi^2$) via the $L^1$ midpoint rule and tail truncation yields explicit uniform enclosures of $V/s, W/s^3, |S_3|/s^4, M_4/s^5$, and the cubic cumulant moments.
   In $y$-units ($0 < \gamma \le 3.7$), for each rational subinterval $[\gamma_a, \gamma_b]$, applying the $L^1$ midpoint rule with $n_y = 36$ panels on $[0, 6]$ (with step $h_y = 1/6$) and adding the discrete $L^1$ midpoint error $\frac{1}{8 m^2} \|f''\|_{L^1}$ yields explicit enclosures of $V/m$, $\bar{y}_{\mathrm{disc}} = \frac{\bar\jmath + 1/2}{m} \in y_0 \pm (dy_0 + dy_d)$, and hence (via a single shift by $\delta_{\mathrm{tot}} = dy_0 + dy_d$ from $y_0$) of $W/m^3$, $|S_3|/m^4$, $M_4/m^5$, and the cubic cumulant moments uniformly for all $m \ge m_0$.

### Lemma 3 (Bounds on $K(re^{i\varphi})/K(r)$)
*Let $z = r e^{i\varphi}$ with $r = e^{-\theta}$, $s = 1/\theta$, and $f(\varphi) := \log K(re^{i\varphi})$ continued continuously from $\varphi = 0$.*
1. *(First derivative):* $f'(0) = i\beta$, where $\beta = \frac{r K'(r)}{K(r)} = -\frac{2r}{1-r} + \frac{a r^a}{1-r^a} + \frac{b r^b}{1-r^b}$ satisfies $-\min(2s, \frac{5}{2}m) \le \beta \le 0$.
   *(Note: $\beta = -r\frac{d}{dr}(\log[a]_r + \log[b]_r)$ and for any $n \ge 1$ and $0 < r < 1$, $r\frac{[n]_r'}{[n]_r} = \frac{\sum_{k=0}^{n-1} k r^k}{\sum_{k=0}^{n-1} r^k} \le \frac{n-1}{2}$ by Chebyshev's sum inequality since $k$ is increasing and $r^k$ is decreasing; thus $|\beta| \le \frac{a-1}{2} + \frac{b-1}{2} = \frac{5m-4}{2} < \frac{5}{2}m$. Also $0 \le \frac{n r^n}{1-r^n} \le \frac{r}{1-r} \le s$ gives $|\beta| \le 2s$.)*
2. *(Second derivative):* $|f(\varphi) - f(0) - i\beta\varphi| \le \frac12 H \varphi^2$ on $|\varphi| \le \eta$, where:
   - for all $\theta > 0$ and $\varphi \in \mathbb{R}$,
     $$|f''(\varphi)| \le \frac{2}{4\sinh^2(\theta/2)} + \frac{a^2}{4\sinh^2(a\theta/2)} + \frac{b^2}{4\sinh^2(b\theta/2)} \le \begin{cases} s^2\Bigl(2 + \frac{(a\theta)^2}{4\sinh^2(a\theta/2)} + \frac{(b\theta)^2}{4\sinh^2(b\theta/2)}\Bigr), \\ m^2\Bigl(\frac{2}{\gamma^2} + \frac{1}{\sinh^2(a\gamma/(2m))} + \frac{9}{4\sinh^2(b\gamma/(2m))}\Bigr);\end{cases}$$
   - for $\gamma \le \frac12$ and $|\varphi| \le \eta$ with $3(\gamma + m\eta) < 2a\sin(\pi/a)$, writing $\log[n]_z = \sum_{k=1}^{n-1} \log(1 - z/\zeta_k)$ ($\zeta_k = e^{2\pi i k/n}$) and using $|1 - z| \le \theta + |\varphi| \le \frac{\gamma + m\eta}{m} < \frac{3(\gamma + m\eta)}{n}$, $|\zeta_1 - 1| = 2\sin(\pi/n) \ge \frac{c_1}{n}$ with $c_1 = 2a\sin(\pi/a)$ (since $x \mapsto \frac{\sin x}{x}$ is decreasing on $(0, \pi)$ and $a < b$), and $|\zeta_k - 1| \ge \frac{4k}{n}$ for $2 \le k \le n/2$:
     $$|f''(\varphi)| \le 2(a^2 + b^2)\left(\frac{1}{(c_1 - 3(\gamma + m\eta))^2} + \sum_{k=2}^\infty \frac{1}{(4k - 3(\gamma + m\eta))^2}\right) \le 26 m^2\left(\frac{1}{\mathrm{gap}_1^2} + \frac{1}{(8 - 3\vartheta)^2} + \frac{1}{4(8 - 3\vartheta)}\right),$$
     where $\vartheta = \gamma + m\eta$ and $\mathrm{gap}_1 = c_1 - 3\vartheta > 0$.
3. *(Pointwise and $L^1$ modulus bounds):*
   - *Universal bound:* $|1 - z^n| \ge 1 - r^n$ gives
     $$\frac{|K(re^{i\varphi})|}{K(r)} \le \frac{|1 - re^{i\varphi}|^2}{(1 - r)^2} = 1 + \frac{\sin^2(\varphi/2)}{\sinh^2(\theta/2)} \le 1 + \min(s^2\varphi^2, 4s^2), \qquad \frac{1}{2\pi}\int_{-\pi}^\pi \frac{|K(re^{i\varphi})|}{K(r)}\,d\varphi \le 1 + 2s^2.$$
   - *Small-$\varphi$ cosine bound ($1.5 m |\varphi| < \pi/2$, used on $m|\varphi| \le 0.70$):* $|[n]_{re^{i\varphi}}| = \bigl|\sum_{k=0}^{n-1} r^k e^{i(k - \frac{n-1}{2})\varphi}\bigr| \ge \cos\bigl(\frac{n-1}{2}\varphi\bigr) [n]_r$, so
     $$\frac{|K(re^{i\varphi})|}{K(r)} \le \frac{1}{\cos(m\varphi)\cos(\frac32 m\varphi)}.$$
   - *Moderate-$\varphi$ sine bound ($0.70 \le m|\varphi| \le 1.60$):* $|1 - re^{i\varphi}|^2 \le \theta^2 + \varphi^2$, $|1 - r^n e^{in\varphi}| \ge 2 r^{n/2}|\sin(n\varphi/2)|$, $r^{-(a+b)/2} < e^{2.5\gamma}$, and $K(r) = \frac{1}{[a]_r[b]_r} > \frac{1}{6m^2}$ yield
     $$\frac{|K(re^{i\varphi})|}{K(r)} \le \frac{(\gamma^2 + (m\varphi)^2) \cdot 6 e^{2.5\gamma}}{4 \sin(a|\varphi|/2)\sin(b|\varphi|/2)}.$$
     For any $\omega = m|\varphi| \in [0.70, \omega_b] \subseteq [0.70, 1.60]$ and all $m \ge m_0 = 101$, the arguments $a|\varphi|/2 = (1 - \frac{1}{2m})\omega \in [(1 - \frac{1}{2m_0})\cdot 0.70,\ \omega_b] \subset (0, \pi)$ and $b|\varphi|/2 = (\frac32 - \frac{1}{2m})\omega \in [(\frac32 - \frac{1}{2m_0})\cdot 0.70,\ \frac32\omega_b] \subset (0, \pi)$ (note $b|\varphi|/2$ exceeds $\pi/2$ for $\omega > 1.05$, where $\sin(b|\varphi|/2)$ is decreasing in $m$). By concavity of $\sin$ on $[0, \pi]$, the uniform-in-$(m \ge m_0, \omega \in [0.70, \omega_b])$ lower bounds $\sin(a|\varphi|/2) \ge \min\bigl(\sin((1-\frac{1}{2m_0})\cdot 0.70),\, \sin(\omega_b)\bigr)$ and $\sin(b|\varphi|/2) \ge \min\bigl(\sin((\frac32 - \frac{1}{2m_0})\cdot 0.70),\, \sin(\frac32\omega_b)\bigr)$ hold (implemented directly in `verify.py`, line 772).
   - *Parseval $L^1$ bound (used for $\gamma \le 0.5$):* By Cauchy–Schwarz and Parseval's identity on $\frac{1-z}{1-z^n} = \sum_{k \ge 0}(z^{kn} - z^{kn+1})$ ($n \ge 2$),
     $$\frac{1}{2\pi}\int_{-\pi}^\pi \left|\frac{1 - re^{i\varphi}}{1 - r^n e^{in\varphi}}\right|^2 d\varphi = \frac{1 + r^2}{1 - r^{2n}} \le \frac{2}{1 - r^n} \implies \frac{1}{2\pi}\int_{-\pi}^\pi \frac{|K(re^{i\varphi})|}{K(r)}\,d\varphi \le \frac{2\sqrt{[a]_r[b]_r}}{1 - r} \le 2\sqrt{6}\, m(s + 1).$$

---

## 5. Major Arc: 4th-Order Edgeworth Lower Bound

Fix $L = 3$ and define the elliptical major arc $\mathcal{B} := \{(\alpha, \varphi) : Q(\alpha, \varphi) = V\alpha^2 + W\varphi^2 \le L^2\}$. (In every regime, $L/\sqrt{V} < \pi$ and $L/\sqrt{W} < \pi$ are certified in `verify.py`, so $\mathcal{B} \subset [-\pi, \pi)^2$.)

### Lemma 4 (Major Arc)
*For each $j \in \{0, \dots, N-1\}$, set $g_j(x) = \log(1 - p_j + p_j e^{ix})$ and write $g_j(\tilde{s}_j) - i p_j \tilde{s}_j = -\frac12 v_j \tilde{s}_j^2 + \frac{i}{6} v'(u_j) \tilde{s}_j^3 + r_{4,j}(\tilde{s}_j)$. Define $C_3(\alpha, \varphi) := \frac16 \sum_j v'(u_j) \tilde{s}_j^3$, $R_4 := \sum_j r_{4,j}(\tilde{s}_j)$, and $R_K := f(\varphi) - f(0) - i\beta\varphi$.*
1. *(Zero-tail global $C_4$ bound):* With $w = 1 - p + p e^{ix}$, direct differentiation gives $|g^{(4)}(x)| = v \cdot \frac{|w^2 - 6 v e^{ix}|}{|w|^4}$. This ratio is invariant under $(p, x) \mapsto (1-p, -x)$ and $x \mapsto -x$. Writing $w^2 - 6v e^{ix} = (1-p)^2 - 4v e^{ix} + p^2 e^{2ix}$ gives $|w^2 - 6v e^{ix}| \le 1 + 2v$ and $|w| \ge 1 - 2q$ ($q = \min(p, 1-p)$), so whenever $|u_j| > \frac52$ (i.e. $q_j \le q_0 = \frac{1}{1+e^{5/2}}$) we have $|g_j^{(4)}(x)| \le C_{4,\mathrm{tail}} v_j$ for **all** $x \in \mathbb{R}$, with $C_{4,\mathrm{tail}} = \frac{1 + 2 q_0(1 - q_0)}{(1 - 2q_0)^4} \le 2.20201$. For $|u_j| \le \frac52$ and $(\alpha, \varphi) \in \mathcal{B}$, Cauchy–Schwarz gives $|\tilde{s}_j| \le L \sqrt{\frac{1}{V} + \frac{J_{\mathrm{lim}}^2}{W}} =: u_0$ (where $J_{\mathrm{lim}} \ge |j - \bar\jmath|$ for $|u_j| \le \frac52$), and interval evaluation on $[0, u_0] \times [0, \frac12]$ yields $C_{4,\mathrm{core}}(u_0)$. Putting $C_4 = \max(C_{4,\mathrm{tail}}, C_{4,\mathrm{core}}(u_0))$ gives $|R_4| \le \frac{C_4}{24}\sum_j v_j \tilde{s}_j^4$ on $\mathcal{B}$ with **no tail set**.
2. *(Exact real-part bound):* For every $x \in \mathbb{R}$, $\mathrm{Re} g_j(x) = \frac12 \log(1 - 2 v_j(1 - \cos x)) \le -v_j(1 - \cos x) \le -\frac12 v_j x^2 + \frac{1}{24} v_j x^4$, so $\mathrm{Re} R_4 \le \frac{1}{24} \sum_j v_j \tilde{s}_j^4$ (with no $C_4$ factor!). Setting $Z := R_4 + R_K$ and changing to polar coordinates $(X, Y) = (\sqrt{V}\alpha, \sqrt{W}\varphi) = (R\cos\vartheta, R\sin\vartheta)$ with $R \le L$, we get $\mathrm{Re} Z \le \frac{\lambda}{2} Q$ on $\mathcal{B}$, where
   $$\lambda := 2 \max_{\vartheta \in [0, \pi/2]} \left[\frac{L^2}{24}\left(\frac{\cos^4\vartheta + 6\cos^2\vartheta\sin^2\vartheta}{V} + 4|\cos\vartheta|\sin^3\vartheta\frac{|S_3|}{V^{1/2}W^{3/2}} + \sin^4\vartheta\frac{M_4}{W^2}\right) + \frac{H\sin^2\vartheta}{2 W}\right].$$
3. *(Major-arc lower bound):* Assuming $\lambda < 1$, let $X_0 = L^2/2$, $X = (1 - \lambda) X_0$, and $g_k(x) := 1 - e^{-x}\sum_{r=0}^k \frac{x^r}{r!}$. Then
   $$2\pi\sqrt{VW} \mathrm{Re} I_{\mathcal{B}} \ge e^{-\frac{\beta^2}{2W}} - e^{-X_0} - \frac12 g_3(X_0)\,\mathbb{E}[C_3^2] - \frac{|\beta|}{\sqrt{W}}\sqrt{g_1(X_0) g_3(X_0)\,\mathbb{E}[C_3^2]} - \frac{C_4}{24}\frac{g_2(X)}{(1-\lambda)^3}\left(\frac{9}{V} + \frac{3 M_4}{W^2}\right) - \frac{H}{2W}\frac{g_1(X)}{(1-\lambda)^2},$$
   where for $(X, Y) \sim \mathcal{N}(0, I_2)$ and $a_{r, 3-r} := V^{-r/2} W^{-(3-r)/2} \sum_j v'(u_j)(j - \bar\jmath)^{3-r}$,
   $$\mathbb{E}[C_3^2] = \frac{15 a_{30}^2 + 18 a_{30} a_{12} + 27 a_{21}^2 + 18 a_{21} a_{03} + 27 a_{12}^2 + 15 a_{03}^2}{36}.$$

**Proof.** On $\mathcal{B}$, the integrand is $e^{-\frac12 Q + i(\beta\varphi + C_3)} + e^{-\frac12 Q + i(\beta\varphi + C_3)}(e^Z - 1)$. For all real $x, y$, $\cos(x + y) = \cos x - \cos x(1 - \cos y) - \sin x \sin y \ge \cos x - \frac12 y^2 - |x||y|$. Integrating against $\frac{1}{2\pi} e^{-(X^2+Y^2)/2}\mathbf{1}_{R \le L}\,dX\,dY$ gives $e^{-\beta^2/(2W)}$ minus the tail $|\mathbb{E}[\mathbf{1}_{R > L}\cos(\beta\varphi)]| \le e^{-X_0}$, minus $\frac12 \mathbb{E}[\mathbf{1}_{R \le L} C_3^2] = \frac12 g_3(X_0)\mathbb{E}[C_3^2]$ (by degree-$6$ radial/angular independence), minus $\mathbb{E}[\mathbf{1}_{R \le L}|\beta\varphi||C_3|] \le \sqrt{\mathbb{E}[\mathbf{1}_{R \le L}(\beta\varphi)^2]\,\mathbb{E}[\mathbf{1}_{R \le L} C_3^2]} = \frac{|\beta|}{\sqrt{W}}\sqrt{g_1(X_0)g_3(X_0)\mathbb{E}[C_3^2]}$ (by Cauchy–Schwarz). For the remainder, $|e^Z - 1| \le |Z| e^{(\mathrm{Re} Z)_+} \le (|R_4| + |R_K|)e^{\frac{\lambda}{2} Q}$. Rescaling $(X', Y') = \sqrt{1 - \lambda}(X, Y)$ (Jacobian $(1-\lambda)^{-1}$, disk radius $\sqrt{2X}$) and using $\mathbb{E}[\sum_j v_j \tilde{s}_j^4] = \frac{9}{V} + \frac{3M_4}{W^2}$ (the $4 S_3 \alpha \varphi^3$ term integrates to $0$ by symmetry) yields the final two terms. $\square$

---

## 6. Minor Arcs: Uniform-in-$m$ Upper Bounds

On $[-\pi, \pi)^2 \setminus \mathcal{B}$, since $|1 - p_j + p_j e^{i\tilde{s}_j}|^2 = 1 - 2 v_j(1 - \cos\tilde{s}_j) \le e^{-2 v_j(1 - \cos\tilde{s}_j)}$, we have $|\Phi(\psi, \varphi)| \le e^{-\mathcal{E}(\alpha, \varphi)}$, where
$$\mathcal{E}(\alpha, \varphi) := \sum_{j=0}^{N-1} v_j \bigl(1 - \cos(\alpha + (j - \bar\jmath)\varphi)\bigr).$$
Writing $\sum_{j=0}^{N-1} v_j e^{i(j - \bar\jmath)\varphi} = S(\varphi) e^{i\delta(\varphi)}$ with $S(\varphi) = \bigl|\sum_j v_j e^{ij\varphi}\bigr| \ge 0$, we have for every $(\alpha, \varphi)$:
$$\mathcal{E}(\alpha, \varphi) = \bigl(V - S(\varphi)\bigr) + S(\varphi)\bigl(1 - \cos(\alpha + \delta(\varphi))\bigr). \tag{3}$$
For any $A > 0$, using $\sin(u/2) \ge u/\pi$ on $[0, \pi]$ gives the elementary 1D integral bound
$$\frac{1}{2\pi}\int_{-\pi}^\pi e^{-A(1 - \cos u)}\,du = \frac{1}{\pi}\int_0^\pi e^{-2A\sin^2(u/2)}\,du < \frac{1}{\pi}\int_0^\infty e^{-2A u^2/\pi^2}\,du = \sqrt{\frac{\pi}{8 A}}. \tag{4}$$
Set $\eta_{\mathrm{true}} := L / \sqrt{W} \le L / \sqrt{W_{\mathrm{lo}}} =: \eta$. We partition $[-\pi, \pi)^2 \setminus \mathcal{B}$ into Region **(A)** ($|\varphi| \le \eta_{\mathrm{true}}, Q > L^2$), Region **(B1)** ($\eta_{\mathrm{true}} < |\varphi| \le \phi_1$), Region **(B2)** ($\phi_1 < |\varphi| \le \phi_{\mathrm{lc}}$), and Region **(C)** ($\phi_{\mathrm{lc}} < |\varphi| \le \pi$).

### Lemma 5 (Exact Trigonometric Splitting for Regions (A) and (B1))
*Let $C(\varphi) = \sum_j v_j \cos((j - \bar\jmath)\varphi)$ and $B(\varphi) = \sum_j v_j \sin((j - \bar\jmath)\varphi)$. For any $\phi_{\max} > 0$ such that $C_{\min} := V - \frac12 W \phi_{\max}^2 > 0$ and all $|\varphi| \le \phi_{\max}$:*
1. $S(\varphi) \ge C(\varphi) \ge V - \frac12 W\varphi^2 \ge C_{\min} > 0$, and $\delta(\varphi) = \arctan(B(\varphi)/C(\varphi)) \in (-\frac\pi2, \frac\pi2)$ satisfies
   $$|\delta(\varphi)| \le \frac{|B(\varphi)|}{C(\varphi)} \le \frac{M_3 \phi_{\max}^2}{6 C_{\min}} |\varphi| =: d_\phi |\varphi|, \qquad M_3 \le \sqrt{W M_4}.$$
2. *Using $1 - \cos x \ge \frac{x^2}{2} - \frac{x^4}{24}$ and $S(\varphi) - C(\varphi) = \frac{B(\varphi)^2}{S(\varphi) + C(\varphi)} \le \frac{B(\varphi)^2}{2 C_{\min}}$,*
   $$V - S(\varphi) \ge \left(\frac{1}{2} - \frac{M_4 \phi_{\max}^2}{24 W} - \frac{M_3^2 \phi_{\max}^4}{72 C_{\min} W}\right) W\varphi^2 =: c_W^*(\phi_{\max})\, W\varphi^2.$$
3. *(Region A):* Take $\phi_{\max} = \eta_{\mathrm{true}}$ (so $C_{\min} \ge V_{\mathrm{lo}} - \frac12 L^2 =: C_\eta > 0$) and any $u_{\mathrm{cap}} \in (0, \pi)$ with $d_\phi \eta < \pi - u_{\mathrm{cap}}$. Setting $u \equiv \alpha + \delta(\varphi) \pmod{2\pi}$ in $[-\pi, \pi)$ preserves measure $d\alpha = du$; on $|u| \le u_{\mathrm{cap}}$, no $2\pi$-wraparound can occur since $|\alpha| \le \pi$, so $|\alpha| \le |u| + d_\phi|\varphi|$. Putting $b_{\mathrm{sh}} = d_\phi\sqrt{V/W}$ and $\rho_{\mathrm{sh}} = \lambda_{\max}\!\begin{pmatrix} 1 & b_{\mathrm{sh}} \\ b_{\mathrm{sh}} & 1+b_{\mathrm{sh}}^2 \end{pmatrix} = 1 + \frac{b_{\mathrm{sh}}^2 + b_{\mathrm{sh}}\sqrt{4+b_{\mathrm{sh}}^2}}{2}$, we get $V u^2 + W\varphi^2 > L^2/\rho_{\mathrm{sh}} =: L_{\mathrm{eff}}^2$. With $c_{\mathrm{ell}} := \min\bigl(c_W^*(\eta),\ \frac{C_\eta}{V}\frac{1 - \cos u_{\mathrm{cap}}}{u_{\mathrm{cap}}^2}\bigr)$ and $K_\eta = \sup_{|\varphi|\le\eta} |K(re^{i\varphi})|/K(r)$, splitting $|u| \le u_{\mathrm{cap}}$ and $|u| > u_{\mathrm{cap}}$ gives
   $$2\pi\sqrt{VW}\,|I_{\mathrm{A}}| \le K_\eta \frac{e^{-c_{\mathrm{ell}} L_{\mathrm{eff}}^2}}{2 c_{\mathrm{ell}}} + \sqrt{\frac{\pi}{c_W^*(\eta)}} \sqrt{V}\, K_\eta\, e^{-C_\eta(1 - \cos u_{\mathrm{cap}})}.$$
4. *(Region B1):* For any $\phi_1 \ge \eta$ with $C_1 := V_{\mathrm{lo}} - \frac12 W_{\mathrm{hi}} \phi_1^2 > 0$ and $c_{W,1} := c_W^*(\phi_1) > 0$, combining (3), (4), and $\int_{\eta_{\mathrm{true}}}^{\phi_1} e^{-c_{W,1} W \varphi^2}\,d\varphi \le \frac{e^{-c_{W,1} L^2}}{2 c_{W,1} \sqrt{W} L}$ yields
   $$2\pi\sqrt{VW}\,|I_{\mathrm{B1}}| \le \sqrt{\frac{\pi}{8}}\sqrt{\frac{V}{C_1}} K_{\phi_1} \frac{e^{-c_{W,1} L^2}}{c_{W,1} L}.$$

**Proof.** Parts 1–2 follow immediately from $\cos x \ge 1 - \frac{x^2}{2}$, $\cos x \le 1 - \frac{x^2}{2} + \frac{x^4}{24}$, $|\sin x - x| \le \frac{|x|^3}{6}$ (all valid for all $x \in \mathbb{R}$), $\sum_j v_j(j - \bar\jmath) = 0$, and $|\arctan t| \le |t|$. Parts 3–4 follow by direct polar integration on $\{Vu^2 + W\varphi^2 > L_{\mathrm{eff}}^2\}$ and 1D Gaussian integration over $\varphi \in \mathbb{R}$ (on $|u| > u_{\mathrm{cap}}$) and $\varphi \in (\eta_{\mathrm{true}}, \infty)$ (in B1). $\square$

### Lemma 6 (Poisson Summation for Regimes I & IIb: $\gamma \ge 3.7$)
*Since $\widehat{v}(\omega) = \int_{-\infty}^\infty \frac{e^{i\omega u}}{4\cosh^2(u/2)}\,du = \frac{\pi\omega}{\sinh(\pi\omega)}$, Poisson summation gives for all $|\varphi| \le \pi$:*
$$\sum_{j \in \mathbb{Z}} v_j e^{i(j - \mu)\varphi} = s\,\frac{\pi s\varphi}{\sinh(\pi s\varphi)} + \varepsilon_P(\varphi), \qquad |\varepsilon_P(\varphi)| \le 2s \sum_{n=1}^\infty \frac{(2n-1)\pi^2 s}{\sinh((2n-1)\pi^2 s)} \le 8\pi^2 s^2 e^{-\pi^2 s} \quad (s \ge 1).$$
*Putting $u \equiv \alpha + (\mu - \bar\jmath)\varphi \pmod{2\pi}$, subtracting the missing indices $j \notin [0, N)$ yields BOTH:*
1. *(Quadratic-tail form, using $1 - \cos(u + \delta) \le 2(1 - \cos u) + \delta^2$):*
   $$\mathcal{E}(\alpha, \varphi) \ge s\left(1 - \frac{\pi s\varphi}{\sinh(\pi s\varphi)}\right) - W_{\mathrm{tail},\mu}\varphi^2 + \left(s\frac{\pi s\varphi}{\sinh(\pi s\varphi)} - 2 V_{\mathrm{tail}}\right)(1 - \cos u) - 2|\varepsilon_P|_{\max}.$$
2. *(Global far-arc form, using $1 - \cos(\cdot) \le 2$):*
   $$\mathcal{E}(\alpha, \varphi) \ge s\left(1 - \frac{\pi s\varphi}{\sinh(\pi s\varphi)} - \frac{2 V_{\mathrm{tail}}}{s}\right) + \left(s\frac{\pi s\varphi}{\sinh(\pi s\varphi)} - 2 V_{\mathrm{tail}}\right)(1 - \cos u) - 2|\varepsilon_P|_{\max}.$$
*Here $V_{\mathrm{tail}}/s \le p(|A|) + p(B) + \frac{v(|A|) + v(B)}{s}$ (since $v$ is decreasing on $[0, \infty)$), and $W_{\mathrm{tail},\mu}/s^3 \le \int_{|A|}^\infty u^2 v(u)\,du + \int_B^\infty u^2 v(u)\,du + \frac{|A|^2 v(|A|) + B^2 v(B)}{s}$ whenever $|A|, B \ge 2.5$ (since $\frac{d}{du}(u^2 v(u)) = u v(u)(2 - u\tanh(u/2)) < 0$ on $[2.5, \infty)$ as $2.5\tanh(1.25) > 2$). Moreover, $x \mapsto \frac{1 - x/\sinh x}{x^2}$ is strictly decreasing on $(0, \infty)$ because its numerator derivative is $x^2\cosh x + x\sinh x - \cosh(2x) + 1 = \sum_{n \ge 3} \frac{4n^2 - 2^{2n}}{(2n)!} x^{2n} < 0$.*

Applying Lemma 5 and Lemma 6 (taking the sharper of the two on Region A and on B1 up to $u_m / s = 0.55/s$, and using the global far-arc form of Lemma 6 on $[0.55/s, 0.80/s]$, $[0.80/s, 1.40/s]$, $[1.40/s, 2.50/s]$, and $[2.50/s, \pi]$ together with Lemma 3(3)) bounds the entire minor arc in Regime I ($\gamma \ge 5.5$, $s \ge 1.709\sqrt{m_0}$) and Regime IIb ($3.7 \le \gamma \le 5.5$, partitioned into three slices $[3.7, 4.2], [4.2, 4.8], [4.8, 5.5]$ with $s \ge m_0 / \gamma_b$).

### Lemma 7 (Interval Fourier Quadrature and Layer-Cake Bound for Regimes IIa & III: $0 < \gamma \le 3.7$)
1. *(Direct Interval Fourier Lower Bound on $V - S(\omega/m)$ for Region B2):* Fix a frequency interval $\omega = m\varphi \in [\omega_a, \omega_b]$, and define
   $$R(\omega) := \frac{1}{m}\sum_{j=0}^{6m-1} v_j \cos\bigl(\omega(y_j - y_0)\bigr), \qquad J(\omega) := \frac{1}{m}\sum_{j=0}^{6m-1} v_j \sin\bigl(\omega(y_j - y_0)\bigr),$$
   so $S(\omega/m)/m = \sqrt{R(\omega)^2 + J(\omega)^2}$. Differentiating $g_\pm(y) = v(A+\gamma y)(1 \pm \cos(\omega(y-y_0)))$ and $g_{c,s}(y) = v(A+\gamma y)\{\cos, \sin\}(\omega(y-y_0))$ twice and using $\int_0^6 |\gamma^2 v''(A+\gamma y)|\,dy \le \gamma L_1(v_0)$, $\int_0^6 2\omega |\gamma v'(A+\gamma y)|\,dy \le \omega$, and $\int_0^6 \omega^2 v(A+\gamma y)\,dy \le \omega^2 V_{\mathrm{cont}}$ yields
   $$\|g_\pm''\|_{L^1([0,6])} \le 2\gamma L_1(v_0) + \omega + \omega^2 V_{\mathrm{cont}}, \qquad \|g_{c,s}''\|_{L^1([0,6])} \le \gamma L_1(v_0) + \omega + \omega^2 V_{\mathrm{cont}}.$$
   By Lemma 2(1) applied to both the $n_y$-panel midpoint rule ($h_y = 6/n_y$) and the $6m$-point discrete sum ($h = 1/m$), each discrete sum lies within $(\frac{h_y^2}{8} + \frac{1}{8m^2})\|g''\|_{L^1}$ of its $n_y$-panel interval quadrature. From these rigorous enclosures we obtain BOTH:
   - the cancellation-free identity $\frac{V - S}{m} = \frac{(V/m - R)(V/m + R) - J^2}{V/m + S/m} \ge \frac{\max\bigl(0,\ (V/m - R)_{\mathrm{lo}}(V/m + R)_{\mathrm{lo},+} - J_{\mathrm{hi}}^2\bigr)}{2 V_{\mathrm{hi},m}}$ (valid unconditionally, since $V/m + S/m \le 2 V_{\mathrm{hi},m}$ and the numerator is clamped at $0$);
   - the direct bound $\frac{V - S}{m} \ge V_{\mathrm{lo},m} - \sqrt{R_{\mathrm{hi}}^2 + J_{\mathrm{hi}}^2}$;
   - the lower bound $S(\omega/m)/m \ge \max(0, R_{\mathrm{lo}}, |J|_{\mathrm{lo}}, V_{\mathrm{lo},m} - \frac12 W_{\mathrm{hi},m} \omega_b^2)$ for the 1D $\alpha$-integral factor $\psi_{\mathrm{fac}} = \min\bigl(1, \sqrt{\frac{\pi}{8 S_{\mathrm{lo}}}}\bigr)$ via (4).
   (In addition, whenever $A < 0$ and $m/\gamma_b \ge 12$, Lemma 6(2) provides a complementary closed-form lower bound on $V - S(\omega/m)$.) Stepping geometrically ($\omega_{k+1} = \min(\phi_{\mathrm{lc},m}, 1.18\omega_k)$) across $[\phi_{1,m}, \phi_{\mathrm{lc},m}]$ (with exact breakpoint $0.70$ in Regime III where Lemma 3(3) switches from cosine to sine $K$-bound) gives a certified bound on $2\pi\sqrt{VW}|I_{\mathrm{B2}}|$.
2. *(Unimodal Layer-Cake Bound for Region C: $|\varphi| \ge \phi_{\mathrm{lc}} = \phi_{\mathrm{lc},m}/m$):* Since $j \mapsto v_j$ is unimodal with $0 \le v_j \le \frac14$, writing $v_j = \int_0^{1/4} \mathbf{1}_{\{v_j > \tau\}}\,d\tau$ expresses $\sum_{j=0}^{N-1} v_j e^{ij\varphi}$ as an integral of geometric sums over contiguous intervals of integers, each of modulus at most $\frac{1}{|\sin(\varphi/2)|}$. Hence
   $$S(\varphi) \le \frac{1}{4|\sin(\varphi/2)|} \implies V - S(\varphi) \ge V - \frac{1}{4\sin(\phi_{\mathrm{lc}}/2)} =: E_{\mathrm{lc}} \qquad (\phi_{\mathrm{lc}} \le |\varphi| \le \pi).$$
   Combining $e^{-E_{\mathrm{lc}}}$ with Lemma 3(3)'s $L^1$ average of $|K|/K(r)$ ($1 + 2s^2$ in Regime IIa with $\phi_{\mathrm{lc},m} = 3/V_{\mathrm{lo},m}$, and $2\sqrt{6}\,m(2.25 m^2 + 1)$ in Regime III with $\phi_{\mathrm{lc},m} = 1.60$) bounds $2\pi\sqrt{VW}|I_{\mathrm{C}}|$.

---

## 7. Monotonicity in $m \ge 101$ and Certified Interval-Arithmetic Summary

Every single inequality evaluated at $m_0 = 101$ in `verify.py` (Part B) holds uniformly for **all** $m \ge 101$:
- **Lemma 1:** $\frac{c_s\sqrt{m}}{1 - 1/(2c_s\sqrt{m})} e^{-\sqrt{m}/c_s}$ and $\frac{\pi^2}{6} c_s^2 + \frac{2g_{\max} c_s}{\sqrt{m}}$ are strictly decreasing for $m \ge 101$.
- **Moments & Major Arc:** Every $L^1$ midpoint discretization error $\frac{L_1}{8 s^2}$ or $\frac{L_1}{8 m^2}$, $\rho$-width $\frac{\gamma}{16 m^2}$, $\lambda$, $u_0$, $C_4$, $\mathbb{E}[C_3^2]$, $H/W$, and $|\beta|/\sqrt{W}$ is decreasing (and every lower bound $V_{\mathrm{lo}}, W_{\mathrm{lo}}$ is increasing) in $s \ge s_{\min}$ (Regimes I, IIb) and in $m \ge m_0$ (Regimes IIa, III).
- **Minor Arcs (Regions A & B1):** With $\phi_1 = u_1/s$ (fixed $u_1$ in Regimes I, IIb) or $\phi_1 = \phi_{1,m}/m$ (fixed $\phi_{1,m}$ in Regimes IIa, III), $c_W^*, C_\eta/V, C_1/V, c_{\mathrm{ell}}$ increase and $d_\phi, \rho_{\mathrm{sh}}, K_\eta$ decrease with $s$ or $m$. For the $|u| > u_{\mathrm{cap}}$ term $\propto \sqrt{s}\,e^{-C_\eta(1 - \cos u_{\mathrm{cap}})}$, the certified assertion $E_{a2} = C_\eta(1 - \cos u_{\mathrm{cap}}) > 1$ implies $V_{\mathrm{lo},s} s(1 - \cos u_{\mathrm{cap}}) > 1 > \frac12$, guaranteeing strict decrease for all $s \ge s_{\min}$ (and analogously in $m \ge m_0$).
- **Minor Arcs (Regions B2 & C):** Every fixed-frequency step has exponent $E = c \cdot s$ (or $c \cdot m$) with $c$ nondecreasing in $s$ (or $m$) and prefactor of polynomial degree $d$:
  - $d = 1$ for B2 / C1 / C2 in Regimes I, IIb (`far_gap * s_min > 1` and `> 2` asserted);
  - $d \le 1$ (in fact $d = \frac12$ when $\psi_{\mathrm{fac}} < 1$) for B2 in Regimes IIa, III (`best_E > 1` asserted on every step; for moderate $\omega \in [0.70, 1.60]$ in Regime III, the sine $K$-bound uses the full $m \ge m_0$ endpoint minima $\min(\sin((1-\frac{1}{2m_0})\cdot 0.70), \sin(\omega_b))$ and $\min(\sin((\frac32-\frac{1}{2m_0})\cdot 0.70), \sin(\frac32\omega_b))$ from Lemma 3(3), which are independent of $m$ and hence valid uniformly for all $m \ge m_0$ even where $b|\varphi|/2 > \pi/2$);
  - $d = 4$ for C3 in Regimes I, IIb (`far_gap(2.5) * s_min > 5 > 4` asserted) and Region C in Regime IIa (`E_lc > 5 > 4` asserted);
  - $d = 5$ for Region C in Regime III (`E_lc > 6 > 5` asserted, and $\frac{1}{4m\sin(0.8/m)}$ is strictly decreasing in $m$).
  Because $x^d e^{-cx}$ is strictly decreasing on $[x_0, \infty)$ whenever $c x_0 > d$, every minor-arc upper bound evaluated at $m_0 = 101$ is valid for all $m \ge 101$.

Running `.venv/bin/python targets/mirzavaziri-2610.19249-conj1/verify.py` (exact `int` arithmetic in Part A; `mpmath.iv` at `dps = 25` with zero Python `float` conversions in Part B) certifies an exhaustive rational cover of $\gamma = \theta m \in (0, \infty)$ at $m_0 = 101$, $L = 3$:

| Regime | $\gamma = \theta m$ range | Method | Certified $\text{Maj}_{\mathrm{lb}}$ | Certified $\text{Min}_{\mathrm{ub}}$ | Certified $\text{Net} = 2\pi\sqrt{VW}\mathrm{Re} I$ |
|---|---|---|---|---|---|
| **III** | $[0,\ 0.5]$ (5 blocks) | `sinhc` + Trig Split + Fourier + Layer-Cake | $\ge 0.90806$ | $\le 0.09352$ | $\ge \mathbf{+0.814548}$ |
| **IIa** | $[0.5,\ 3.7]$ (14 blocks) | Centered $y$-quad + Trig Split + Fourier + Layer-Cake | $\ge 0.50831$ | $\le 0.24757$ | $\ge \mathbf{+0.260738}$ |
| **IIb** | $[3.7,\ 5.5]$ (3 slices) | $s$-unit + Trig Split / Poisson | $\ge 0.53134$ | $\le 0.37676$ | $\ge \mathbf{+0.154579}$ |
| **I** | $[5.5,\ \infty)$ ($s \ge 1.709\sqrt{m}$) | $s$-unit + Trig Split / Poisson | $\ge 0.48476$ | $\le 0.27072$ | $\ge \mathbf{+0.214039}$ |

Hence $2\pi\sqrt{VW}\mathrm{Re} I \ge +0.154579 > 0$, so $p_t > 0$ for all $m \ge 101$ ($m \not\equiv 2,3 \pmod 5$) and all $5m < t \le T_m$. Combined with Proposition 2 and Section 3 ($m \le 100$), this completes the proof of Conjecture 4.4 (`conj:general`) and Guo–Krattenthaler Conjecture 7.4 (`conj:GK`, Conjecture 1.1). $\blacksquare$

---

## 8. Verification Command and Transparency Note

- **Exact self-contained verification command:**
  ```bash
  .venv/bin/python targets/mirzavaziri-2610.19249-conj1/verify.py
  ```
  Prints `PASS` (total runtime $\approx 18\text{ s}$: Part A exact integer check $m \le 100$ in $11.5\text{ s}$; Part B 25-digit zero-float `mpmath.iv` certification $m \ge 101$ in $6.3\text{ s}$).
- **Status label (pending independent check and audit):** Written proof with exact integer and directed-rounding interval-arithmetic verification (`verify.py`); not externally peer-reviewed. Conjecture 4.5 (`conj:almost`) is not established.
