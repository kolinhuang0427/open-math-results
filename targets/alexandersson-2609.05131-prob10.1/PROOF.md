# Proof of Alexandersson (2026), Problem 10.1 (`prob:consecutiveChowInterlacing`)

- **Primary source:** Per Alexandersson, *Real-rootedness and interlacing for parking functions and Chow polynomials*, `arXiv:2609.05131v2` (2026-09-23), Section 10 (*Further questions*), **Problem 10.1** (`\label{prob:consecutiveChowInterlacing}`, `parking-functions.tex` lines 1879–1881).
- **Exact problem statement:**
  > Do $H_{\mathrm{NC}_{n+1}}(t)$ and $H_{\mathrm{NC}_{n+2}}(t)$ interlace for every $n$?
- **Result:** **YES.** For every $n \ge 1$ (and trivially $n = 0$), the noncrossing Chow polynomials $C_n(t) := H_{\mathrm{NC}_{n+1}}(t)$ and $C_{n+1}(t) = H_{\mathrm{NC}_{n+2}}(t)$ interlace ($C_n \ll C_{n+1}$). Moreover, for every $n \ge 2$, all zeros of $C_n(t)$ and $C_{n+1}(t)$ are real, negative, simple, and **strictly interlace**:
  $$\beta_n < \alpha_{n-1} < \beta_{n-1} < \dotsb < \alpha_1 < \beta_1 < 0.$$
- **Verification:** Standalone zero-float verification script [`verify.py`](file:///Users/kolinhuang/Documents/open-math/targets/alexandersson-2609.05131-prob10.1/verify.py) (pure exact integer arithmetic for $1 \le n \le 80$ + 35-digit outward-rounded `mpmath.iv` interval arithmetic for all $n \ge 80$), run via:
  ```bash
  .venv/bin/python -u targets/alexandersson-2609.05131-prob10.1/verify.py
  ```
  (prints `PASS`, exit code `0`, zero Python `float`s used anywhere).

---

## 1. Preliminaries, Rational Generating Function, and Base Cases

By Theorem 1.1, eq. `(1)` (`eq:introSmirnovTransfer`), and Proposition 4.1 (`eq:lastLetterRecurrence`) of `arXiv:2609.05131v2`, the noncrossing Chow polynomial for $n \ge 1$ is
$$C_n(t) := H_{\mathrm{NC}_{n+1}}(t) = \frac{1}{n+1} \sum_{\substack{w \in [n+1]^n \\ w_i \ne w_{i+1}\ (1 \le i < n)}} t^{\mathrm{des}(w)} = \frac{1}{n+1}\sum_{j=1}^{n+1} F^{(n+1)}_{n, j}(t),$$
where for fixed alphabet size $m \ge 2$ the reversed last-letter table $F^{(m)}_{r, j}(t)$ ($r \ge 1$, $1 \le j \le m$) satisfies
$$F^{(m)}_{1, j}(t) = 1, \qquad F^{(m)}_{r+1, j}(t) = t \sum_{k < j} F^{(m)}_{r, k}(t) + \sum_{k > j} F^{(m)}_{r, k}(t). \tag{1.1}$$
Recall the interlacing convention of `arXiv:2609.05131v2` (§4, lines 499–508): for real-rooted polynomials $f, g$ with positive leading coefficients and roots $\alpha_1 \ge \dotsb \ge \alpha_r$ and $\beta_1 \ge \dotsb \ge \beta_s$, we write $f \ll g$ if $s \in \{r, r+1\}$ and $\beta_{r+1} \le \alpha_r \le \beta_r \le \dotsb \le \alpha_1 \le \beta_1$ (omitting $\beta_{r+1}$ when $s = r$; for $r = 0$, only $s \in \{0, 1\}$ is required).

**Base cases $n = 0$ and $n = 1$.** Since $H_{\mathrm{NC}_1}(t) = 1$, $C_1(t) = H_{\mathrm{NC}_2}(t) = 1$ (degree $0$), and $C_2(t) = H_{\mathrm{NC}_3}(t) = 1 + t$ (degree $1$, root $-1$), both $H_{\mathrm{NC}_1} \ll H_{\mathrm{NC}_2}$ ($r = s = 0$) and $C_1 \ll C_2$ ($r = 0, s = 1$) hold immediately. We henceforth consider $n \ge 1$ (and prove strict interlacing for all $n \ge 2$).

**Elementary properties of $C_n(t)$.** For every $n \ge 1$:
1. **Palindromicity and degree:** Reversing the alphabet ($w_i \mapsto n+2-w_i$) is an involution on Smirnov words in $[n+1]^n$ satisfying $\mathrm{des}(\bar w) = (n-1) - \mathrm{des}(w)$ (as adjacent letters are distinct). Hence $C_n(t) = t^{n-1} C_n(1/t)$. There are $\binom{n+1}{n} = n+1$ strictly increasing (resp. strictly decreasing) words in $[n+1]^n$, so $c_{n,0} = c_{n,n-1} = 1$, $\deg C_n = n-1$, and $c_{n,k} > 0$ for all $0 \le k \le n-1$. In particular $C_n(0) = 1 > 0$, and $C_n(-1) = (-1)^{n-1} C_n(-1)$ implies $C_n(-1) = 0$ whenever $n$ is even.
2. **Real-rootedness:** By Theorem 1.1 (`thm:mainChow`) of `arXiv:2609.05131v2`, $C_n(t)$ is real-rooted with all roots in $(-\infty, 0)$. (Note also that our proof below independently constructs all $n-1$ simple negative roots of $C_n(t)$ for every $n \ge 1$.)
3. **Root count in $(0, 1)$:** Write $K_n := \lfloor (n-1)/2 \rfloor$. By palindromicity, the zeros of $C_n(-s)$ on $(0, \infty) \setminus \{1\}$ occur in reciprocal pairs $\{s, 1/s\}$, so $C_n(-s)$ has at most $K_n$ distinct roots in $(0, 1)$ (with equality iff all roots of $C_n$ are simple, and $C_n(-1) = 0$ iff $n$ is even).

**Lemma 1.1 (Closed Rational Generating Function).** *For every integer $n \ge 1$, letting $m := n + 1$,*
$$C_n(t) = \frac{1}{m}[z^n]\frac{(1-t)(1+z)^m}{(1+zt)^m - t(1+z)^m} = \frac{1}{m}[z^n]\frac{(1+z)^m}{1 - \sum_{k=2}^m \binom{m}{k}(t + t^2 + \dotsb + t^{k-1}) z^k}. \tag{1.2}$$

*Proof.* Fix $m \ge 2$ and define $G_j(z) := \sum_{r \ge 1} F^{(m)}_{r, j}(t) z^r$ ($1 \le j \le m$) and $S(z) := \sum_{j=1}^m G_j(z)$. Multiplying (1.1) by $z^{r+1}$ and summing over $r \ge 1$ yields
$$G_j(z) = z + z t \sum_{k < j} G_k(z) + z \sum_{k > j} G_k(z).$$
Subtracting the $j$-th equation from the $(j+1)$-th gives $G_{j+1}(z) - G_j(z) = z t G_j(z) - z G_{j+1}(z)$, i.e. $(1+z)G_{j+1}(z) = (1+zt)G_j(z)$, so $G_j(z) = \left(\frac{1+zt}{1+z}\right)^{j-1} G_1(z)$. For $j = 1$, $G_1(z) = z + z(S(z) - G_1(z))$, so $(1+z)G_1(z) = z(1+S(z))$. Summing the geometric series gives
$$S(z) = G_1(z)\frac{(1+zt)^m - (1+z)^m}{(1+z)^{m-1} z(t-1)} = (1+S(z))\frac{(1+zt)^m - (1+z)^m}{(t-1)(1+z)^m}.$$
Solving for $1 + S(z)$ gives $1 + S(z) = \frac{(1-t)(1+z)^m}{(1+zt)^m - t(1+z)^m}$. Setting $m = n+1$ and taking $\frac{1}{m}[z^n]$ yields the first equality in (1.2). Expanding $(1+zt)^m - t(1+z)^m = (1-t) + \sum_{k=2}^m \binom{m}{k}(t^k - t)z^k$ and canceling $(1-t)$ gives the second equality. $\square$

---

## 2. Part 1: Exact Integer Sturm–Cauchy Proof for $1 \le n \le 80$

Because $C_n(t)$ is palindromic of degree $n-1$, it expands uniquely in the $\gamma$-basis:
$$C_n(t) = \sum_{j=0}^{d_n} \gamma_{n, j}\, t^j (1+t)^{n-1-2j} = (1+t)^{n-1}\Gamma_n\!\left(\frac{t}{(1+t)^2}\right), \qquad \Gamma_n(u) := \sum_{j=0}^{d_n} \gamma_{n, j} u^j, \quad d_n := K_n = \left\lfloor\frac{n-1}{2}\right\rfloor,$$
with $\gamma_{n, 0} = c_{n, 0} = 1$.

**Proposition 2.1 ($\Gamma$-Equivalence and Sturm–Cauchy Criterion).** *Suppose $n \ge 2$, $\deg \Gamma_n = d_n$, $\deg \Gamma_{n+1} = d_{n+1} \in \{d_n, d_n+1\}$, and $\Gamma_n(0), \Gamma_{n+1}(0), \mathrm{lc}(\Gamma_n), \mathrm{lc}(\Gamma_{n+1}) > 0$. If the Cauchy index satisfies*
$$I_{-\infty}^0\!\left(\frac{\Gamma_n}{\Gamma_{n+1}}\right) = d_{n+1}, \tag{2.1}$$
*then $C_n$ and $C_{n+1}$ have all simple negative roots and strictly interlace ($C_n \ll C_{n+1}$).*

*Proof.* Every pole of $\Gamma_n/\Gamma_{n+1}$ in $(-\infty, 0)$ contributes at most $+1$ to $I_{-\infty}^0(\Gamma_n/\Gamma_{n+1})$, and $\Gamma_{n+1}$ has at most $d_{n+1}$ distinct roots in $(-\infty, 0)$. Hence (2.1) forces $\Gamma_{n+1}$ to have exactly $d_{n+1}$ simple roots $v_{d_{n+1}} < \dotsb < v_1 < 0$ in $(-\infty, 0)$, with $\Gamma_n(v_j) \ne 0$ and $\Gamma_n/\Gamma_{n+1}$ jumping from $-\infty$ to $+\infty$ at every $v_j$. Since $\Gamma_{n+1}(0) > 0$, we have $(-1)^{j-1} \Gamma_{n+1}'(v_j) > 0$, forcing $(-1)^{j-1}\Gamma_n(v_j) > 0$ for $1 \le j \le d_{n+1}$. By the Intermediate Value Theorem, $\Gamma_n$ has a root in each of the $d_{n+1}-1$ open intervals $(v_{j+1}, v_j)$.
- If $n = 2q$ is even ($d_n = q-1, d_{n+1} = q$), these $q-1$ roots exhaust $\deg \Gamma_n$, giving $v_q < u_{q-1} < v_{q-1} < \dotsb < u_1 < v_1 < 0$.
- If $n = 2q+1$ is odd ($d_n = d_{n+1} = q$), then $(-1)^{q-1}\Gamma_n(v_q) > 0$ while $\mathrm{lc}(\Gamma_n) > 0$ gives $\mathrm{sgn}\Gamma_n(-\infty) = (-1)^q$, forcing a $q$-th root $u_q < v_q$, giving $u_q < v_q < \dotsb < u_1 < v_1 < 0$.

Now $s \mapsto u(s) := \frac{-s}{(1-s)^2}$ has derivative $-\frac{1+s}{(1-s)^3} < 0$ and maps $(0, 1)$ strictly decreasingly and bijectively onto $(-\infty, 0)$. Pulling back the roots $u_i, v_j$ to $s_i, \tau_j \in (0, 1)$ yields
- for $n = 2q$: $0 < \tau_1 < s_1 < \tau_2 < \dotsb < s_{q-1} < \tau_q < 1$ (with $C_n(-1) = 0$, $C_{n+1}(-1) \ne 0$);
- for $n = 2q+1$: $0 < \tau_1 < s_1 < \dotsb < \tau_q < s_q < 1$ (with $C_n(-1) \ne 0$, $C_{n+1}(-1) = 0$).

Adjoining the reciprocal roots $1/s_i, 1/\tau_j \in (1, \infty)$ and negating ($t = -s$) shows that all $n-1$ roots of $C_n$ and all $n$ roots of $C_{n+1}$ are simple, negative, and strictly interlacing. $\square$

**Exact Integer Computation ($1 \le n \le 80$).** In `verify.py` (Part 0 & Part 1):
1. The second formula of (1.2) is evaluated in exact Python integers in $O(n^3)$ time per polynomial (using prefix sums for multiplication by $t + \dotsb + t^{k-1}$) and cross-checked identically against the direct Smirnov recurrence (1.1) for $1 \le n \le 15$ (plus row sums $C_n(1) = n^{n-1}$).
2. For all $1 \le n \le 81$, `to_gamma(C_n)` extracts $\Gamma_n(u)$ in exact integers and asserts exact zero remainder (certifying palindromicity), $\Gamma_n(0) = 1$, $\deg\Gamma_n = d_n$, and $\mathrm{lc}(\Gamma_n) > 0$.
3. For every $1 \le n \le 80$, we form the signed primitive pseudo-remainder sequence $p_0 = \Gamma_{n+1}$, $p_1 = \Gamma_n$, $c_i p_{i-1} = q_i p_i - p_{i+1}$ with strictly positive integer multipliers $c_i = |\mathrm{lc}(p_i)|^{\deg p_{i-1} - \deg p_i + 1} > 0$ (dividing out positive content at each step), verify termination at a nonzero constant ($\gcd(\Gamma_n, \Gamma_{n+1}) = 1$), and verify by Sturm's theorem for the Cauchy index (Gantmacher, *The Theory of Matrices*, Vol. 2, Ch. XV, Thm. 2) that $I_{-\infty}^0(\Gamma_n/\Gamma_{n+1}) = V(-\infty) - V(0) = d_{n+1}$.

All $80$ pairs $1 \le n \le 80$ **PASS**. Thus it remains to prove strict interlacing for all $n \ge n_0 := 80$.

---

## 3. Two Exact Analytic Identities for $C_n(-s)$ ($s \in (0, 1]$)

Setting $t = -s$ ($s \in (0, 1]$) and $m := n+1$ in (1.2) gives
$$\frac{C_n(-s)}{1+s} = \frac{1}{m}[z^n]\frac{(1+z)^m}{(1-sz)^m + s(1+z)^m}. \tag{3.1}$$

### Lemma 3.1 (Identity A: Alternating Fuss–Catalan Series)
*For every $n \ge 1$ and every $s \in (0, 1)$, letting $m = n+1$,*
$$\frac{C_n(-s)}{1+s} = \sum_{k=0}^\infty (-1)^k u_k(n, s), \qquad u_k(n, s) := s^k a_k(n, s) > 0, \tag{3.2}$$
*where $a_k(n, s) = a_k^{(0)}(n)\big(1 + E_k(n, s)\big)$ with*
$$a_k^{(0)}(n) := \frac{1}{m}\binom{(k+1)m}{n}, \qquad a_k(n, s) := \frac{1}{m}[z^n]\left(\frac{1+z}{1-sz}\right)^{(k+1)m} = \frac{1}{m}\sum_{j=0}^n \binom{(k+1)m}{n-j}\binom{(k+1)m+j-1}{j} s^j. \tag{3.3}$$
*Moreover, for all $N \ge 1$ and $s > 0$,*
$$0 < E_0(N, s) \le e^{N(N+1)s/2} - 1, \qquad 0 < E_k(N, s) \le e^{2Ns} - 1 \quad (\forall\, k \ge 1). \tag{3.4}$$

*Proof.* Fix $s \in (0, 1)$. Because $|s((1+z)/(1-sz))^m| = s < 1$ at $z = 0$, there exists $r_0 > 0$ such that $|s((1+z)/(1-sz))^m| < 1$ uniformly on $|z| = r_0$. Expanding $\frac{((1+z)/(1-sz))^m}{1 + s((1+z)/(1-sz))^m} = \sum_{k=0}^\infty (-1)^k s^k ((1+z)/(1-sz))^{(k+1)m}$ and interchanging $\frac{1}{2\pi i}\oint_{|z|=r_0} (\cdot)\, z^{-n-1} dz$ with the uniformly convergent sum yields (3.2)–(3.3).

Write $E_k(N, s) = \sum_{j=1}^N t_j$ with $M := (k+1)(N+1)$ and $t_j := \frac{\binom{M}{N-j}\binom{M+j-1}{j}}{\binom{M}{N}} s^j > 0$ ($t_0 = 1$). For $1 \le j \le N$,
$$\frac{t_j}{t_{j-1}} = \frac{(N-j+1)(M+j-1)}{j(M-N+j)} s.$$
- When $k = 0$ ($M = N+1$), $M - N + j = j + 1 \ge 2$ and $(N-j+1)(N+j) = N(N+1) - j(j-1) \le N(N+1)$, so $\frac{t_j}{t_{j-1}} \le \frac{N(N+1)s}{2j}$. By induction $t_j \le \frac{1}{j!}(N(N+1)s/2)^j$, giving $0 < E_0(N, s) \le e^{N(N+1)s/2} - 1$.
- When $k \ge 1$ ($M \ge 2N+2$), $2(M-N+j) - (M+j-1) = M - 2N + j + 1 \ge 4 > 0$, so $\frac{M+j-1}{M-N+j} < 2$ and hence $\frac{t_j}{t_{j-1}} < \frac{2Ns}{j}$. By induction $t_j < \frac{1}{j!}(2Ns)^j$, giving $0 < E_k(N, s) \le e^{2Ns} - 1$. $\square$

### Lemma 3.2 (Identity B: Partial-Fraction $w$-Sum and Exact $s = 1$ Sign)
*For every $n \ge 2$ ($m = n+1$) and every $s \in (0, 1]$, set $\rho := s^{1/m} = e^{-y}$ ($y := \frac{-\ln s}{m} \ge 0$), $c_n := s^{n/m} = e^{-ny} \in (0, 1]$, $\theta := \frac{\pi}{m}$, and $\theta_k := (2k-1)\theta$ ($1 \le k \le m$). With $w_k := \rho e^{i\theta_k}$ and $T_k(n, s) := \frac{w_k(w_k+s)^{n-1}}{(1-w_k)^{n+1}}$, we have*
$$-\frac{m^2 s}{(1+s)^2} C_n(-s) = \sum_{k=1}^m T_k(n, s) = 2|T_1(n, s)|\cos\Phi_n(s) + \sum_{k=2}^{\lceil m/2 \rceil} c_k |T_k(n, s)|\cos\Phi_{n, k}(s), \tag{3.5}$$
*where $c_k = 2$ if $2k-1 < m$ and $c_k = 1$ if $2k-1 = m$, and for $1 \le k \le \lceil m/2 \rceil$ (writing $\Phi_n := \Phi_{n, 1}$),*
$$\Phi_{n, k}(s) = A_{n, k}(s) + B_{n, k}(s), \qquad A_{n, k}(s) := m\arctan\!\left(\frac{e^{-y}\sin\theta_k}{1 - e^{-y}\cos\theta_k}\right), \qquad B_{n, k}(s) := n\theta_k - (n-1)\arctan\!\left(\frac{c_n\sin\theta_k}{1 + c_n\cos\theta_k}\right). \tag{3.6}$$
*Furthermore:*
1. *For every odd $n = 2q+1$ ($q \ge 0$),*
   $$(-1)^q C_{2q+1}(-1) = \frac{1}{(2q+2)^2}\sum_{k=1}^{2q+2} \frac{\cot^{2q}(\theta_k/2)}{\sin^2(\theta_k/2)} > 0. \tag{3.7}$$
2. *For every $s \in (0, 1]$ and $2 \le k \le \lceil m/2 \rceil$,*
   $$\frac{|T_k(n, s)|}{|T_1(n, s)|} < \left(1 + \frac{\sin^2(\theta_k/2) - \sin^2(\theta_1/2)}{\sinh^2(y/2) + \sin^2(\theta_1/2)}\right)^{-m/2}. \tag{3.8}$$

*Proof.* Consider the meromorphic $1$-form $\omega(z) := \frac{(1+z)^m}{(1-sz)^m + s(1+z)^m} \frac{dz}{z^{n+1}}$ on $\widehat{\mathbb{C}}$, which has $\mathrm{Res}_{z=0}\omega = \frac{m}{1+s} C_n(-s)$ by (3.1). Applying the Möbius biholomorphism $w = \frac{1-sz}{1+z}$ ($z = \frac{1-w}{w+s}$, $dz = -\frac{1+s}{(w+s)^2}dw$, mapping $z=0$ to $w=1$) preserves residues and transforms $\omega$ to
$$\omega(w) = -(1+s)\frac{(w+s)^{n-1}}{(w^m + s)(1-w)^{n+1}}\, dw.$$
As $w \to \infty$, the integrand is $O(w^{-m-2}) = O(w^{-n-3})$, so $\mathrm{Res}_{w=\infty}\omega = 0$. The remaining poles of $\omega$ are at $w = 1$ and the $m$ distinct simple roots $w_k = \rho e^{i\theta_k}$ ($1 \le k \le m$) of $w^m + s = 0$ (when $s=1$ and $m$ is odd, $w_{(m+1)/2} = -1$ is a removable singularity since $n-1 \ge 1$, giving $T_{(m+1)/2}(n,1) = 0$). Because $\frac{d}{dw}(w^m+s)\big|_{w=w_k} = m w_k^{m-1} = -\frac{ms}{w_k}$,
$$\mathrm{Res}_{w=w_k}\omega = -(1+s)\frac{(w_k+s)^{n-1}}{(1-w_k)^{n+1}}\cdot \frac{w_k}{-ms} = \frac{1+s}{ms} T_k(n, s).$$
By the residue theorem on $\widehat{\mathbb{C}}$, $\frac{m}{1+s} C_n(-s) = \mathrm{Res}_{w=1}\omega = -\sum_{k=1}^m \mathrm{Res}_{w=w_k}\omega = -\frac{1+s}{ms}\sum_{k=1}^m T_k(n, s)$, giving the first equality of (3.5). Pairing conjugate roots $w_{m+1-k} = \overline{w_k}$ gives the second equality.

Writing $T_k(n, s) = \frac{\rho^n e^{i n\theta_k} (1 + c_n e^{-i\theta_k})^{n-1}}{(1 - \rho e^{i\theta_k})^m}$, both $\mathrm{Re}(1 - \rho e^{i\theta_k}) = 1 - \rho\cos\theta_k > 0$ (since $\cos\theta_k < 1$) and $\mathrm{Re}(1 + c_n e^{-i\theta_k}) = 1 + c_n\cos\theta_k > 0$ for $\theta_k < \pi$ (and $= 1-c_n \ge 0$ at $\theta_k = \pi$, where $\sin\theta_k = 0$), yielding (3.6). At $s=1$ and $n = 2q+1$ ($m=2q+2$ even), $\theta_k \ne \pi$, $\frac{w_k}{(1-w_k)^2} = -\frac{1}{4\sin^2(\theta_k/2)}$, and $\frac{w_k+1}{1-w_k} = i\cot(\theta_k/2)$, so $T_k(2q+1, 1) = \frac{(-1)^{q+1}\cot^{2q}(\theta_k/2)}{4\sin^2(\theta_k/2)}$, which yields (3.7) upon substitution into (3.5).

Finally, for $2 \le k \le \lceil m/2 \rceil$, we have $0 < \theta_1 < \theta_k \le \pi$, so $\cos\theta_k < \cos\theta_1$ and hence $|1 + c_n e^{-i\theta_k}|^2 = 1 + c_n^2 + 2c_n\cos\theta_k < |1 + c_n e^{-i\theta_1}|^2$. Meanwhile $|1 - w_k|^2 = 4\rho(\sinh^2(y/2) + \sin^2(\theta_k/2))$, giving (3.8). $\square$

---

## 4. Phase Analysis and Regime B ($n \ge 80$)

For $n \ge n_0 := 80$ ($m = n+1 \ge m_0 := 81$, $\sqrt{m_0} = 9$), define the variables
$$\lambda := \frac{-\ln s}{\pi} = \frac{y}{\theta} > 0, \qquad Y := \frac{-\ln s}{\sqrt{m}} = y\sqrt{m} = \frac{\pi\lambda}{\sqrt{m}} > 0, \qquad u(s) := \arctan\!\left(\frac{1}{\lambda}\right) \in \left(0, \frac{\pi}{2}\right),$$
and set the regime cutoff and Regime B parameters
$$c_{K_A} := \frac{22}{10} = 2.2, \qquad K_A(n) := \left\lfloor \frac{\sqrt{m}}{c_{K_A}} \right\rfloor \ge 4, \qquad Y_{\max} := \frac{23}{10} = 2.3.$$

### Lemma 4.1 (Strict Monotonicity of $\Phi_n$)
*For every $n \ge 14$, $\rho \mapsto \Phi_n(\rho^m)$ is strictly increasing on $(0, 1]$, mapping $s \in (0, 1]$ bijectively onto $\left(\frac{n}{n+1}\pi, \frac{n+1}{2}\pi\right]$.*

*Proof.* Differentiating (3.6) for $k=1$ ($\theta = \pi/m$, $c_n = \rho^n$) with respect to $\rho \in (0, 1]$ gives
$$\frac{d\Phi_n}{d\rho} = \sin\theta \left(\frac{n+1}{1 - 2\rho\cos\theta + \rho^2} - \frac{n(n-1)\rho^{n-1}}{1 + 2\rho^n\cos\theta + \rho^{2n}}\right).$$
Since $\cos\theta > 0$ for $n \ge 2$, we have $1 + 2\rho^n\cos\theta + \rho^{2n} > 1$ and $1 - 2\rho\cos\theta + \rho^2 = (1-\rho)^2 + 4\rho\sin^2(\theta/2) \le (1-\rho)^2 + \rho\theta^2$. On $[0, 1]$, $\rho^{n-1}(1-\rho)^2$ is maximized at $\rho = \frac{n-1}{n+1}$, where its value is $\frac{4}{(n+1)^2}(\frac{n-1}{n+1})^{n-1} < \frac{4}{(n+1)^2}$. Hence for all $\rho \in (0, 1]$ and $n \ge 14$,
$$n(n-1)\rho^{n-1}\frac{1-2\rho\cos\theta+\rho^2}{1+2\rho^n\cos\theta+\rho^{2n}} < \frac{n(n-1)}{(n+1)^2}(4 + \pi^2) < 4 + \pi^2 < 14 < n+1,$$
proving $\frac{d\Phi_n}{d\rho} > 0$. As $s \to 0^+$, $A_{n,1}(s) \to 0$ and $B_{n,1}(s) \to \frac{n}{n+1}\pi$; at $s = 1$, $A_{n,1}(1) = m\frac{\pi-\theta}{2} = \frac{n}{2}\pi$ and $B_{n,1}(1) = n\theta - (n-1)\frac{\theta}{2} = \frac{\pi}{2}$, so $\Phi_n(1) = \frac{n+1}{2}\pi$. $\square$

### Lemma 4.2 (Euler-Product Expansion, Phase Shift $\Delta\Phi$, and $u$-Derivative)
*For every $m = n+1 \ge 2$, $1 \le k \le \lceil m/2 \rceil$ ($r := 2k-1 \le m$), and $s \in (0, 1)$:*
1. *(Exact Euler product)*
   $$A_{n, k}(s) = m\arctan\!\left(\frac{r}{\lambda}\right) - \frac{r\pi}{2} + E_{A, k}(m, \lambda), \qquad E_{A, k}(m, \lambda) := m\sum_{p=1}^\infty \arctan\!\left(\frac{2r\lambda}{4p^2 m^2 + \lambda^2 - r^2}\right). \tag{4.1}$$
   *Writing $E_A(m, \lambda) := E_{A, 1}(m, \lambda)$, we have for all $s \in (0, 1)$:*
   $$0 < E_A(m, \lambda) < \frac{\pi^2\lambda}{12 m(1 - \frac{1}{4m^2})} = \frac{\pi Y}{12\sqrt{m}(1 - \frac{1}{4m^2})}, \qquad \frac{\Phi_n(s)}{\pi} < \frac{\sqrt{m}}{Y} + \frac{1}{2} + \frac{Y}{12\sqrt{m}(1 - \frac{1}{4m^2})}. \tag{4.2}$$
2. *(Phase shift $\Delta\Phi(s) := \Phi_{n+1}(s) - \Phi_n(s)$ and $u$-derivative on $0 < Y \le Y_{\max}$, $m \ge m_0 = 81$, $\theta_0 := \pi/m_0$)*
   *Since $\lambda^2 + 1 \le \frac{Y_{\max}^2 m}{\pi^2} + 1 < 4 m^2$ holds on all of $0 < Y \le Y_{\max}$, $m \ge m_0$:*
   $$0 < E_A(m, \lambda) - E_A(m+1, \lambda) < \frac{\pi Y(1 + \frac{1}{4m^2})}{12 m^{3/2}(1 - \frac{1}{4m^2})^2}, \tag{4.3}$$
   $$-\frac{\pi^3}{24 m^2 \cos\theta_0} \le B_{n+1}(s) - B_n(s) \le \frac{\pi}{m(m+1)} + \frac{\pi}{e(m-1)(m+1)} + \frac{\pi^3}{24 m^2 \cos\theta_0}, \tag{4.4}$$
   *so $u(s) - \mathrm{err}_{\mathrm{lo}}(m) \le \Delta\Phi(s) \le u(s) + \mathrm{err}_{\mathrm{hi}}(m)$ where*
   $$\mathrm{err}_{\mathrm{lo}}(m) := \frac{\pi Y_{\max}(1 + \frac{1}{4m^2})}{12 m^{3/2}(1 - \frac{1}{4m^2})^2} + \frac{\pi^3}{24 m^2 \cos\theta_0}, \qquad \mathrm{err}_{\mathrm{hi}}(m) := \frac{\pi}{m(m+1)} + \frac{\pi}{e(m-1)(m+1)} + \frac{\pi^3}{24 m^2 \cos\theta_0}.$$
   *Moreover, $\frac{d\Phi_n}{du} \ge D_\Phi := m_0 - \frac{Y_{\max}^2 + \pi^2/m_0}{12(1 - \frac{1}{4m_0^2})^2} - \pi^2 > 10$.*

*Proof.*
**(1)** Write $w_k = e^{-(y - i r\theta)}$ and use Euler's product $1 - e^{-\zeta} = e^{-\zeta/2}\cdot \zeta \prod_{p=1}^\infty (1 + \frac{\zeta^2}{4\pi^2 p^2})$ with $\zeta = y - i r\theta$. Since $r\theta \le \pi$ and $p \ge 1$, the real part of $4\pi^2 p^2 + \zeta^2$ is $4\pi^2 p^2 + y^2 - r^2\theta^2 \ge 3\pi^2 + y^2 > 0$, while its imaginary part is $-2ry\theta \le 0$. Taking $-\arg$ of each factor and substituting $y = \lambda\theta$, $\theta = \pi/m$ (canceling $\theta^2$) gives $\frac{1}{m}A_{n, k}(s) = \arctan(r/\lambda) - \frac{r\theta}{2} + \sum_{p=1}^\infty \arctan\!\left(\frac{2r\lambda}{4p^2 m^2 + \lambda^2 - r^2}\right) + 2\pi\ell$ for an integer $\ell$ independent of $y > 0$ by continuity. As $y \to \infty$, $\frac{1}{m}A_{n, k} \to 0$, $\arctan(r/\lambda) \to 0$, and the sum converges as a Riemann sum to $\int_0^\infty \frac{2r\theta}{4\pi^2 x^2 + 1}\, dx = \frac{r\theta}{2}$, forcing $\ell = 0$ and proving (4.1). Using $\arctan x < x$ ($x > 0$), $4p^2 m^2 + \lambda^2 - 1 \ge 4p^2 m^2(1 - \frac{1}{4m^2})$, and $\sum_{p=1}^\infty p^{-2} = \frac{\pi^2}{6}$ gives the bound on $E_A$ in (4.2); combining with $\arctan(1/\lambda) < 1/\lambda = \frac{\pi}{Y\sqrt{m}}$ and $-\frac{\pi}{2} + B_n(s) < -\frac{\pi}{2} + \frac{n}{n+1}\pi < \frac{\pi}{2}$ gives the upper bound on $\Phi_n(s)/\pi$ in (4.2).

**(2)** Set $g_p(v) := v\arctan\!\left(\frac{2\lambda}{Q}\right)$ with $Q := 4p^2 v^2 + \lambda^2 - 1 > 0$ for $v \in [m, m+1]$. Differentiating gives
$$g_p'(v) = \arctan\!\left(\frac{2\lambda}{Q}\right) - \frac{16 p^2 v^2 \lambda}{Q^2 + 4\lambda^2}.$$
Because $\frac{x}{1+x^2} < \arctan x < x$ for all $x > 0$ (check $\frac{d}{dx}(\arctan x - \frac{x}{1+x^2}) = \frac{2x^2}{(1+x^2)^2} > 0$), substituting $x = 2\lambda/Q$ gives:
- $g_p'(v) < \frac{2\lambda(Q^2 + 4\lambda^2 - 8p^2 v^2 Q)}{Q(Q^2+4\lambda^2)} = \frac{2\lambda((\lambda^2+1)^2 - 16p^4 v^4)}{Q(Q^2+4\lambda^2)} < 0$ since $\lambda^2 + 1 < 4m^2 \le 4p^2 v^2$;
- $-g_p'(v) < \frac{16 p^2 v^2 \lambda - 2\lambda Q}{Q^2+4\lambda^2} = \frac{2\lambda(4p^2 v^2 + 1 - \lambda^2)}{Q^2+4\lambda^2} \le \frac{2\lambda(1 + \frac{1}{4v^2})}{4p^2 v^2 (1 - \frac{1}{4v^2})^2}$.

Integrating over $v \in [m, m+1]$ and summing over $p \ge 1$ proves (4.3).

For $B_{n+1}(s) - B_n(s)$, let $g_c(\phi) := \arctan\!\left(\frac{c\sin\phi}{1+c\cos\phi}\right)$. For $c \in [0, 1]$ and $\phi \in [0, \theta_0]$ ($\cos\phi \ge \cos\theta_0 > 0$),
$$0 \le \frac{c}{1+c} - g_c'(\phi) = \frac{c(1-c)(1-\cos\phi)}{(1+c)(1+2c\cos\phi+c^2)} \le \frac{c(1-c)}{(1+c)^3\cos\theta_0}\cdot \frac{\phi^2}{2} \le \frac{\phi^2}{8\cos\theta_0}$$
(since $1+2c\cos\phi+c^2 - (1+c)^2\cos\phi = (1+c^2)(1-\cos\phi) \ge 0$ and $c(1-c) \le 1/4$). Integrating from $0$ to $\phi$ yields $g_c(\phi) = \frac{c}{1+c}\phi - R_c(\phi)$ with $0 \le R_c(\phi) \le \frac{\phi^3}{24\cos\theta_0}$. Writing
$$B_{n+1}(s) - B_n(s) = \frac{\pi}{m(m+1)} + \big[(n-1)g_{c_n}(\theta_n) - n g_{c_n}(\theta_{n+1})\big] + n\big[g_{c_n}(\theta_{n+1}) - g_{c_{n+1}}(\theta_{n+1})\big],$$
the first two terms combine via $n\theta_{n+1} - (n-1)\theta_n = \frac{2\pi}{m(m+1)}$ to give $\frac{1-c_n}{1+c_n}\frac{\pi}{m(m+1)} - (n-1)R_{c_n}(\theta_n) + n R_{c_n}(\theta_{n+1}) \in \left[-\frac{\pi^3}{24 m^2\cos\theta_0},\ \frac{\pi}{m(m+1)} + \frac{\pi^3}{24 m^2\cos\theta_0}\right]$. For the third term, $0 \le \frac{\partial g_c(\theta_{n+1})}{\partial c} = \frac{\sin\theta_{n+1}}{1+2c\cos\theta_{n+1}+c^2} < \theta_{n+1}$, and with $x := -\ln s \ge 0$, $a := 1-\frac{1}{m}$, $b := 1-\frac{1}{m+1}$ ($b-a = \frac{1}{m(m+1)}$),
$$0 \le c_n - c_{n+1} = e^{-ax}(1 - e^{-(b-a)x}) \le (b-a)x e^{-ax} \le \frac{b-a}{e a} = \frac{1}{e(m-1)(m+1)},$$
so $0 \le n(g_{c_n}(\theta_{n+1}) - g_{c_{n+1}}(\theta_{n+1})) < \frac{\pi}{e(m-1)(m+1)}$. Summing proves (4.4).

Finally, for $\frac{d\Phi_n}{du} = m + \frac{d E_A}{du} + \frac{d B_n}{du}$ (using $\frac{d\lambda}{du} = -(1+\lambda^2)$):
- $\frac{\partial}{\partial\lambda}\arctan(\frac{2\lambda}{Q}) = \frac{2(4p^2 m^2 - 1 - \lambda^2)}{Q^2 + 4\lambda^2} \in \left(0, \frac{2}{4p^2 m^2(1-\frac{1}{4m^2})^2}\right)$, so $0 < -\frac{d E_A}{du} \le \frac{\pi^2(1+\lambda^2)}{12m(1-\frac{1}{4m^2})^2} \le \frac{Y_{\max}^2 + \pi^2/m_0}{12(1-\frac{1}{4m_0^2})^2}$;
- $0 < -\frac{d B_n}{du} = (n-1)\pi(1-\frac{1}{m})\frac{\sin\theta_n}{1+2c_n\cos\theta_n+c_n^2}(1+\lambda^2)c_n < \pi^2(1+\lambda^2)e^{-\pi(1-1/m_0)\lambda} \le \pi^2$, because for any $a > 1$ (here $a = \pi(1-1/m_0) > 3$), $\frac{d}{d\lambda}[(1+\lambda^2)e^{-a\lambda}] = (-a\lambda^2 + 2\lambda - a)e^{-a\lambda} < 0$ on $\lambda \ge 0$ (discriminant $4(1-a^2) < 0$).

This proves $\frac{d\Phi_n}{du} \ge D_\Phi$. $\square$

### Lemma 4.3 (Harmonic Phase Deviation and Power-Law Tail Bound)
*For every $m = n+1 \ge m_0$, $2 \le k \le \lceil m/2 \rceil$ ($r = 2k-1 \le m$), and $s \in (0, 1)$, let $\eta_k(m, s) := |\Phi_{n, k}(s) - r\Phi_n(s)|$. Then:*
1. $\eta_k(m, s) \le \frac{r^3-r}{3}\frac{\pi^3}{Y^3\sqrt{m}} + \frac{\pi^3 r(r^2-1) Y}{540 m^{5/2}(1-\frac{1}{4m^2})} + \frac{8\pi^3 r^3 Y^3}{76545 m^{7/2}} + r\pi e^{-Y\sqrt{m}(1-1/m)}$. *(4.5)*
2. *For every $B > 0$ and $x \ge 1$, $1 + B x^2 \ge (1 + B) x^{2B/(1+B)}$.* *(4.6)*

*Proof.*
**(1)** By (4.1) and (3.6), $\Phi_{n,k}(s) - r\Phi_n(s) = m(\arctan(r/\lambda) - r\arctan(1/\lambda)) + (E_{A,k} - r E_A) + (B_{n,k} - r B_n)$.
- **First term:** For all $x = 1/\lambda > 0$ and $r \ge 1$,
  $$0 \le r\arctan(x) - \arctan(rx) = r(r^2-1)\int_0^x \frac{t^2}{(1+t^2)(1+r^2t^2)}\, dt < \frac{r^3-r}{3}x^3,$$
  so $m|r\arctan(1/\lambda) - \arctan(r/\lambda)| < \frac{r^3-r}{3}\frac{m}{\lambda^3} = \frac{r^3-r}{3}\frac{\pi^3}{Y^3\sqrt{m}}$.
- **Second term:** Let $a_p := \frac{2r\lambda}{4p^2 m^2 + \lambda^2 - r^2}$ and $b_p := \frac{2\lambda}{4p^2 m^2 + \lambda^2 - 1}$. Because $a_p \ge r b_p > 0$, $r \ge 1$, and $0 \le x - \arctan x \le x^3/3$ ($x \ge 0$), we have $|\arctan a_p - r\arctan b_p| \le (a_p - r b_p) + \frac{1}{3} a_p^3$ (as $\arctan a_p - r\arctan b_p \le a_p - r b_p + \frac{r}{3}b_p^3 \le (a_p - r b_p) + \frac{1}{3}a_p^3$, and $r\arctan b_p - \arctan a_p \le r b_p - a_p + \frac{1}{3}a_p^3 \le \frac{1}{3}a_p^3$). Since $r \le m$ and $p \ge 1$, $4p^2 m^2 + \lambda^2 - r^2 \ge (4p^2-1)m^2 \ge 3p^2 m^2$, so
  $$a_p - r b_p = \frac{2r(r^2-1)\lambda}{(4p^2 m^2 + \lambda^2 - r^2)(4p^2 m^2 + \lambda^2 - 1)} \le \frac{2r(r^2-1)\lambda}{12 p^4 m^4 (1 - \frac{1}{4m^2})}, \qquad \frac{a_p^3}{3} \le \frac{8r^3\lambda^3}{81 p^6 m^6}.$$
  Multiplying by $m$, summing using $\sum_{p=1}^\infty p^{-4} = \frac{\pi^4}{90}$ and $\sum_{p=1}^\infty p^{-6} = \frac{\pi^6}{945}$, and substituting $\lambda = Y\sqrt{m}/\pi$ yields the second and third terms of (4.5).
- **Third term:** For any $c \in [0, 1]$ and $\phi \in [0, \pi]$, we claim $0 \le g_c(\phi) \le c\phi$: on $[0, \pi/2]$, $\cos\phi \ge 0$ so $g_c(\phi) \le \frac{c\sin\phi}{1+c\cos\phi} \le c\sin\phi \le c\phi$; on $[\pi/2, \pi]$, $g_c(\phi) \le \max_{\psi\in[0,\pi]} g_c(\psi) = \arcsin c \le \frac{\pi}{2} c \le c\phi$. Hence both $g_{c_n}(r\theta)$ and $r g_{c_n}(\theta)$ lie in $[0, c_n r\theta]$, so $|B_{n, k} - r B_n| = (n-1)|g_{c_n}(r\theta) - r g_{c_n}(\theta)| \le (n-1)c_n r\theta < r\pi c_n = r\pi e^{-Y\sqrt{m}(1-1/m)}$.

**(2)** Set $h(t) := \ln(1 + B e^t) - \ln(1+B) - \frac{B}{1+B} t$ for $t \ge 0$. Then $h(0) = 0$ and $h'(t) = \frac{B(e^t-1)}{(1+B e^t)(1+B)} \ge 0$, so $h(2\ln x) \ge 0$ for all $x \ge 1$. $\square$

### Proposition 4.4 (Regime B Brackets and Sign Certification for $n \ge 80$)
*For each $j \in \{K_A(n)+1, \dots, K_n\}$, define $s_j^* \in (0, 1)$ by $\Phi_n(s_j^*) = (j+\frac12)\pi$, set $\delta_j := \frac14 u(s_j^*) \in (0, \frac{\pi}{8})$, and define $0 < a_j < s_j^* < b_j < 1$ by $\Phi_n(a_j) = (j+\frac12)\pi - \delta_j$ and $\Phi_n(b_j) = (j+\frac12)\pi + \delta_j$. Then for every $n \ge 80$:*
1. *(Well-definedness, disjointness, and Seam-B)* The intervals $[a_j, b_j]$ ($K_A+1 \le j \le K_n$) are well-defined, pairwise disjoint, contained in $(0, 1)$, and satisfy $\Phi_n(a_{K_A+1}) > (K_A+1)\pi$ and $Y(s) \le Y(a_{K_A+1}) < Y_{\max} = 2.3$ for all $s \in [a_j, b_j]$.
2. *(Sign certification)* For every $j \in \{K_A+1, \dots, K_n\}$:
   $$(-1)^{j-1} C_n(-a_j) > 0, \qquad (-1)^j C_n(-b_j) > 0, \qquad (-1)^j C_{n+1}(-s) > 0 \quad (\forall\, s \in [a_j, b_j]). \tag{4.7}$$

*Proof.*
**(1)** By Lemma 4.1, $\Phi_n$ maps $(0, 1]$ bijectively onto $(\frac{n}{n+1}\pi, \frac{n+1}{2}\pi]$. Since $0 < \delta_j < \frac{\pi}{8}$, we have:
- $\Phi_n(a_{K_A+1}) = (K_A + \frac32)\pi - \delta_{K_A+1} > (K_A + \frac{11}{8})\pi > (K_A+1)\pi > \frac{n}{n+1}\pi$;
- $\Phi_n(b_j) = (j+\frac12)\pi + \delta_j < (j+\frac58)\pi < (j+\frac{11}{8})\pi < \Phi_n(a_{j+1})$ (disjointness);
- $\Phi_n(b_{K_n}) < (K_n + \frac58)\pi < \frac{n+1}{2}\pi = \Phi_n(1)$ (checking both $n=2q+1$, $K_n=q$, $(q+\frac58) < q+1$, and $n=2q$, $K_n=q-1$, $(q-\frac38) < q+\frac12$).

Since $K_A > \frac{\sqrt{m}}{c_{K_A}} - 1$, $\frac{\Phi_n(a_{K_A+1})}{\pi} > \frac{\sqrt{m}}{c_{K_A}} + \frac{3}{8}$. By (4.2), if $Y(a_{K_A+1}) \ge Y_{\max}$ then by monotonicity $\frac{\sqrt{m}}{c_{K_A}} + \frac{3}{8} < \frac{\sqrt{m}}{Y_{\max}} + \frac{1}{2} + \frac{Y_{\max}}{12\sqrt{m}(1-\frac{1}{4m^2})}$, contradicting the inequality $\sqrt{m}\left(\frac{1}{c_{K_A}} - \frac{1}{Y_{\max}}\right) > \frac{1}{8} + \frac{Y_{\max}}{12\sqrt{m}(1-\frac{1}{4m^2})}$, whose LHS increases and RHS decreases in $m \ge m_0 = 81$ and which holds at $m_0 = 81$ with margin $\ge 0.0315685$ (`[SEAM-B]` in `verify.py`). Thus $Y(s) \le Y(a_{K_A+1}) < Y_{\max}$ throughout Regime B.

**(2)** Fix $j \in \{K_A+1, \dots, K_n\}$ and $s \in [a_j, b_j]$. By Lemma 4.2(2) and the Mean Value Theorem, $|u(s) - u(s_j^*)| \le \frac{\delta_j}{D_\Phi} = \rho_u u(s_j^*)$ where $\rho_u := \frac{1}{4 D_\Phi}$, so $\frac{u(s)}{1+\rho_u} \le u(s_j^*) \le \frac{u(s)}{1-\rho_u}$. Moreover, since $Y \le Y_{\max}$, $u(s) = \arctan(\frac{\pi}{Y\sqrt{m}}) \ge \arctan(\frac{\pi}{Y_{\max}\sqrt{m}}) \ge a_{f,0}\frac{\pi}{Y_{\max}\sqrt{m}}$ where $a_{f,0} := \frac{\arctan x_0}{x_0}$ ($x_0 := \frac{\pi}{Y_{\max}\sqrt{m_0}}$). Dividing $\mathrm{err}_{\mathrm{lo}}(m)$ and $\mathrm{err}_{\mathrm{hi}}(m)$ by $a_{f,0}\frac{\pi}{Y_{\max}\sqrt{m}}$ yields expressions strictly decreasing in $m \ge m_0$ (scaling as $O(m^{-1})$ and $O(m^{-3/2})$), hence maximized at $m_0 = 81$, giving $\mathrm{rel}_{\mathrm{lo}} := \frac{\mathrm{err}_{\mathrm{lo}}(m_0)}{u_{\mathrm{lb}}(m_0)}$ and $\mathrm{rel}_{\mathrm{hi}} := \frac{\mathrm{err}_{\mathrm{hi}}(m_0)}{u_{\mathrm{lb}}(m_0)}$. Setting
$$c_{\min, n} := \frac{1}{4(1+\rho_u)}, \quad c_{\max, n} := \frac{1}{4(1-\rho_u)}, \quad c_{\min, n+1} := (1-\mathrm{rel}_{\mathrm{lo}}) - \frac{1}{4(1-\rho_u)}, \quad c_{\max, n+1} := (1+\mathrm{rel}_{\mathrm{hi}}) + \frac{1}{4(1-\rho_u)},$$
we have $0 < c_{\min, N} u(s) \le |\Phi_N(s) - (j+\frac12)\pi| \le c_{\max, N} u(s) < \pi$ (for $N = n$ at $s \in \{a_j, b_j\}$ with sign $\mp$, and for $N = n+1$ on all of $[a_j, b_j]$ with sign $+$). Since $\frac{\sin\phi}{\phi}$ is decreasing on $(0, \pi]$, writing $s_{\mathrm{fac}, N} := \frac{\sin(c_{\max, N}\pi/2)}{c_{\max, N}\pi/2} > 0$ gives $|\cos\Phi_N(s)| = \sin|\Phi_N(s) - (j+\frac12)\pi| \ge c_{\min, N} s_{\mathrm{fac}, N} u(s)$.

Meanwhile, because $\cos((2k-1)(j+\frac12)\pi) = 0$ for every odd $r = 2k-1$,
$$|\cos\Phi_{N, k}(s)| \le |\Phi_{N, k}(s) - r(j+\tfrac12)\pi| \le r|\Phi_N(s) - (j+\tfrac12)\pi| + \eta_k(M, s) \le r c_{\max, N} u(s) + \eta_k(M, s),$$
where $M := N+1 \in \{m, m+1\}$ and $Y_N(s) := \frac{-\ln s}{\sqrt{M}} \le Y(s) < Y_{\max}$ (note $M \ge m_0$ and $Y_N(s) \in (0, Y_{\max})$ for BOTH $N = n$ and $N = n+1$, with the exact same $\lambda(s)$ and $u(s)$!). By (3.5), (4.7) holds provided
$$E_B(N, s) := \sum_{k=2}^{\lceil M/2 \rceil} \frac{|T_k(N, s)|}{|T_1(N, s)|} \frac{|\cos\Phi_{N, k}(s)|}{|\cos\Phi_N(s)|} < 1, \tag{4.8}$$
since $\cos((j+\frac12)\pi - \delta_j) = (-1)^j\sin\delta_j$ and $\cos((j+\frac12)\pi + \phi) = (-1)^{j+1}\sin\phi$ for $\phi \in (0, \pi)$, and the leading factor $-\frac{M^2 s}{(1+s)^2}$ in (3.5) is strictly negative.

To bound $|T_k|/|T_1|$ via (3.8), let $S_{\mathrm{sh}} := \frac{\sinh(y_{\max}/2)}{y_{\max}/2}$ ($y_{\max} := Y_{\max}/\sqrt{m_0}$), so $\sinh^2(y/2) + \sin^2(\theta/2) \le \frac{1}{4M^2}(M S_{\mathrm{sh}}^2 Y_N^2 + \pi^2)$. For the numerator $M^2(\sin^2(\theta_k/2) - \sin^2(\theta_1/2)) \ge \nu_k$:
- $k = 2$: $\sin^2(3\theta/2)-\sin^2(\theta/2) = 2\sin^2\theta\cos\theta \ge \frac{2\pi^2 c_3}{M^2}$ with $c_3 := (1-\theta_0^2/6)^2(1-\theta_0^2/2)$, so $\nu_2 := 2\pi^2 c_3$;
- $k = 3$: $\sin^2(5\theta/2)-\sin^2(\theta/2) \ge \frac{25 c_5 - 1}{4}\frac{\pi^2}{M^2}$ with $c_5 := (1-(5\theta_0/2)^2/6)^2$, so $\nu_3 := \frac{25 c_5 - 1}{4}\pi^2$;
- $k \ge 4$: Jordan's inequality $\sin(\frac{r\pi}{2M}) \ge \frac{r}{M}$ and $\sin(\frac{\pi}{2M}) \le \frac{\pi}{2M}$ give $\nu_k := r^2 - \frac{\pi^2}{4}$.

Note that for any $A, B, C > 0$, $M \mapsto (1 + \frac{A}{BM+C})^{-M/2}$ is strictly decreasing in $M$ (since $\frac{d}{dM}[M\ln(1+\frac{A}{BM+C})] > \frac{A}{BM+C+A} - \frac{ABM}{(BM+C)(BM+C+A)} = \frac{AC}{(BM+C)(BM+C+A)} > 0$), and $M \mapsto (1 + \frac{D}{M})^{-M/2}$ is strictly decreasing in $M$ (since $\ln(1+u) > \frac{u}{1+u}$). We certify $E_B(N, s) < 1$ across the exhaustive partition of $(M, Y_N) \in [m_0, \infty) \times (0, Y_{\max})$ for BOTH $N = n$ and $N = n+1$:
- **(B3) $\lambda < 1$:** Here $u(s) > \frac{\pi}{4}$ and $M S_{\mathrm{sh}}^2 Y_N^2 + \pi^2 < (S_{\mathrm{sh}}^2 + 1)\pi^2$. Using $|\cos\Phi_{N, k}| \le 1$ and (4.6) at $r_0 = 7$ ($k \ge 4$) with $p(M) = \frac{M B}{1+B} \ge p(m_0)$ and $\sum_{j \ge 0}(1+\frac{2j}{7})^{-p} \le 1 + \frac{7}{2(p-1)}$, `verify.py` certifies $E_B \le 2.934 \times 10^{-28}$ ($C_n$) and $\le 2.058 \times 10^{-28}$ ($C_{n+1}$).
- **(B4) $\lambda \ge 1$ and $Y_N \le \frac{1}{2}$ ($Z := Y_N^{-2} \ge 4$):** Here $\pi^2 \le M Y_N^2$ so $|T_k|/|T_1| \le (1 + C_k Z/M)^{-M/2}$ with $C_k := \frac{4\nu_k}{S_{\mathrm{sh}}^2+1}$, and $u(s) \ge \frac{\pi}{4}\frac{1}{\lambda} = \frac{\pi^2}{4 Y_N \sqrt{M}}$. For $k \in \{2, 3, 4\}$, `verify.py` verifies $\frac{m_0}{C_k(m_0/2 - 1)} < 4$, so $Z(1 + C_k Z/M)^{-M/2}$ is strictly decreasing in $Z \ge 4$ and in $M \ge m_0$, hence maximized at $(Z, M) = (4, m_0)$. Bounding $k \ge 4$ via (4.6) at $r_0 = 7$ (power $p_4(M) = \frac{4C_4}{1+4C_4/M} \ge p_4(m_0)$ and $(r/7)^3$ dominating all $r, r^3$ terms via $\sum_{j \ge 0}(1+\frac{2j}{7})^{3-p_4} \le 1 + \frac{7}{2(p_4-4)}$), `verify.py` certifies $E_B \le 1.745 \times 10^{-16}$ ($C_n$) and $\le 1.233 \times 10^{-16}$ ($C_{n+1}$).
- **(B5) $\frac{1}{2} \le Y_N \le Y_{\max} = \frac{23}{10}$:** Partition $[\frac{1}{2}, \frac{23}{10}]$ into $18$ subintervals $[Y_a, Y_b]$ of width $\frac{1}{10}$. On each bin, $x = \frac{\pi}{Y_N\sqrt{M}} \le x_{\mathrm{hi}} := \frac{\pi}{Y_a\sqrt{m_0}}$ gives $u(s) \ge a_f \frac{\pi}{Y_N\sqrt{M}}$ ($a_f := \frac{\arctan x_{\mathrm{hi}}}{x_{\mathrm{hi}}}$), $Y_N\sqrt{M} e^{-Y_N\sqrt{M}(1-1/M)}$ decreases in both $Y_N$ and $M$ (as $Y_a\sqrt{m_0}(1-1/m_0) > 1$), and the $k \ge 10$ ($r \ge 19$) tail is bounded via (4.6) with exponent $p(M, Y_N) = \frac{4\nu_{10}}{S_{\mathrm{sh}}^2 Y_N^2 + (\pi^2+4\nu_{10})/M} \ge p_{\mathrm{tail}} := p(m_0, Y_{\max}) \ge 61.96$ and multiplier $1 + \frac{19}{2(p_{\mathrm{tail}}-4)} \le 1.1639$. Across all $18$ bins, `verify.py` certifies $E_B \le 0.090792 < 1$ ($C_n$) and $\le 0.074801 < 1$ ($C_{n+1}$). $\square$

---

## 5. Binomial Asymptotics, Regime A ($1 \le k \le K_A$, $n \ge 80$), and Seam

For $N \ge 1$ ($M := N+1$) and $j \ge 1$, define the Fuss–Catalan leading-term ratios
$$R_j(N) := \frac{a_j^{(0)}(N)}{a_{j-1}^{(0)}(N)} = \frac{\binom{(j+1)M}{N}}{\binom{jM}{N}}, \qquad Q_k(n) := \frac{R_k(n+1)}{R_k(n)}. \tag{5.1}$$
For $j \ge 2$, define the exact constants
$$\beta_j := (j+1)\ln(j+1) - 2j\ln j + (j-1)\ln(j-1), \qquad c_j := -\frac{3}{2}\ln\!\left(\frac{j}{j-1}\right) + \frac{1}{2}\ln\!\left(\frac{j+1}{j}\right). \tag{5.2}$$

### Lemma 5.1 (Monotonicity, Robbins–Stirling Bounds, and Integral Identities)
*For all integers $N \ge 1$ ($M = N+1$):*
1. *(Strict monotonicity)* $R_1(N) > R_2(N) > R_3(N) > \dotsb > 1$. Moreover, $R_1(N) = \frac{1}{M+1}\binom{2M}{M} \ge \frac{4^M}{(M+1)(2M+1)}$ and $Q_1(n) = \frac{2(2n+3)}{n+3}$.
2. *(Stirling decomposition)* For all $j \ge 2$ and $M \ge 2$, $\ln R_j(N) = M\beta_j + c_j + \delta_j(M)$ with
   $$0 < \delta_j(M) < \frac{13}{12 M j(j-1)}, \tag{5.3}$$
   *and for all $j \ge 2$ and $M \ge 24$,*
   $$-\frac{5}{24 M j(j-1)} < \ln Q_j(n) - \beta_j < \frac{1}{6 M j(j-1)}. \tag{5.4}$$
3. *(Integral identities and convexity)* For all $j \ge 2$ and $1 \le i \le k - 2$ ($k \ge 3$):
   $$\frac{1}{j} < \beta_j = \int_{-1}^1 \frac{1-|u|}{j+u}\, du < \frac{1}{j} + \frac{1}{6j(j^2-1)}, \qquad -\frac{3}{2(j-1)} < c_j < 0, \tag{5.5}$$
   $$\beta_k - \beta_{k+i} > \frac{i}{k(k+i)}, \qquad \beta_{k-i} - \beta_k > \frac{i}{k(k-i)}, \qquad 0 < \beta_{k-i} + \beta_{k+i} - 2\beta_k \le \frac{2i^2}{(k-1)((k-1)^2-i^2)}, \tag{5.6}$$
   $$0 < c_{k+i} - c_k \le \frac{i(k+2)}{k(k^2-1)}, \qquad 0 < c_k - c_{k-i} \le \frac{i(k-i+2)}{(k-i)((k-i)^2-1)}. \tag{5.7}$$

*Proof.*
**(1)** For every $j \ge 1$, $\frac{R_{j+1}(N)}{R_j(N)} = \prod_{i=0}^{N-1}\frac{((j+2)M-i)(jM-i)}{((j+1)M-i)^2} = \prod_{i=0}^{N-1}\left(1 - \frac{M^2}{((j+1)M-i)^2}\right) < 1$. For $j = 1$, $R_1(N) = \frac{1}{M}\binom{2M}{M-1} = \frac{1}{M+1}\binom{2M}{M} = \mathrm{Cat}_M$, giving $Q_1(n) = \frac{\mathrm{Cat}_{n+2}}{\mathrm{Cat}_{n+1}} = \frac{2(2n+3)}{n+3}$ and $\binom{2M}{M} \ge \frac{4^M}{2M+1}$ (largest of $2M+1$ terms summing to $4^M$).

**(2)** Since $\binom{jM}{M-1} = \frac{M}{(j-1)M+1}\binom{jM}{M}$, we have $R_j(N) = \frac{(j-1)M+1}{jM+1}\frac{((j+1)M)!((j-1)M)!}{((jM)!)^2}$. Substituting Robbins's Stirling bound $\ln(X!) = X\ln X - X + \frac{1}{2}\ln(2\pi X) + \theta(X)$ with $\frac{1}{12X+1} < \theta(X) < \frac{1}{12X}$ ($X \ge 1$) gives $\ln R_j(N) = M\beta_j + c_j + \delta_j(M)$ with
$$\delta_j(M) = \ln\!\left(\frac{1+\frac{1}{(j-1)M}}{1+\frac{1}{jM}}\right) + \underbrace{\big[\theta((j+1)M) + \theta((j-1)M) - 2\theta(jM)\big]}_{=: \Delta_2\theta_j(M)}.$$
Here $\ln(\frac{1+1/((j-1)M)}{1+1/(jM)}) = \ln(1 + \frac{1}{M j(j-1) + j-1}) \in \left(\frac{1}{2 M j(j-1)},\ \frac{1}{M j(j-1)}\right)$ (for $M \ge 2$), while Robbins's bound yields:
- $\Delta_2\theta_j(M) < \frac{1}{12(j+1)M} + \frac{1}{12(j-1)M} - \frac{2}{12jM+1} = \frac{1}{6Mj(j^2-1)} + \frac{2}{12jM(12jM+1)} < \frac{1}{12Mj(j-1)}$ (since $\frac{2}{j+1} + \frac{j-1}{6Mj} \le \frac{2}{3} + \frac{1}{12} < 1$);
- $\Delta_2\theta_j(M) > \frac{1}{6Mj(j^2-1)} - \frac{1}{12(j+1)M(12(j+1)M+1)} - \frac{1}{12(j-1)M(12(j-1)M+1)} > -\frac{1}{72 M^2 (j-1)^2} \ge -\frac{1}{36 M^2 j(j-1)}$.

Summing yields $\delta_j(M) > \frac{1}{2Mj(j-1)} - \frac{1}{36M^2 j(j-1)} > 0$ and $\delta_j(M) < \frac{13}{12Mj(j-1)}$, proving (5.3). Next, $\ln Q_j(n) - \beta_j = \delta_j(M+1) - \delta_j(M) = \ln\!\left(1 - \frac{1}{(jM+j+1)((j-1)M+1)}\right) + \Delta_2\theta_j(M+1) - \Delta_2\theta_j(M)$. The first term lies in $(-\frac{1}{M^2 j(j-1)}, 0)$ and $|\Delta_2\theta_j(M+1) - \Delta_2\theta_j(M)| < \frac{1}{12Mj(j-1)} + \frac{1}{36M^2 j(j-1)}$; for $M \ge 24$, $\frac{1}{12} + \frac{37}{36 \cdot 24} = \frac{109}{864} < \frac{5}{24}$ and $\frac{1}{12} + \frac{1}{36 \cdot 24} < \frac{1}{6}$, proving (5.4).

**(3)** Since $\frac{d^2}{dx^2}(x\ln x) = \frac{1}{x}$, Taylor's theorem gives $\beta_j = \int_{-1}^1 \frac{1-|u|}{j+u}\, du = \int_0^1 \frac{2j(1-u)}{j^2-u^2}\, du = \frac{1}{j} + \frac{2}{j}\int_0^1 \frac{u^2(1-u)}{j^2-u^2}\, du \in (\frac{1}{j}, \frac{1}{j} + \frac{1}{6j(j^2-1)})$ (as $\int_0^1 u^2(1-u)\, du = \frac{1}{12}$). Since $u \mapsto \frac{1}{(k+u)(k+i+u)}$ is strictly convex on $[-1, 1]$ (product of two positive decreasing convex functions) and $(1-|u|)du$ is a symmetric probability measure on $[-1, 1]$, Jensen's inequality gives $\beta_k - \beta_{k+i} = i\int_{-1}^1 \frac{1-|u|}{(k+u)(k+i+u)}\, du > \frac{i}{k(k+i)}$ and similarly $\beta_{k-i} - \beta_k > \frac{i}{k(k-i)}$. Likewise, $\beta_{k-i} + \beta_{k+i} - 2\beta_k = \int_{-1}^1 \frac{2i^2(1-|u|)}{(k+u)((k+u)^2-i^2)}\, du \le \frac{2i^2}{(k-1)((k-1)^2-i^2)}$. Finally, $c(x) := -\frac{3}{2}\ln\frac{x}{x-1} + \frac{1}{2}\ln\frac{x+1}{x}$ satisfies $c'(x) = \frac{x+2}{x(x^2-1)} > 0$ (strictly decreasing on $x > 1$) and $c(\infty) = 0$, giving $-\frac{3}{2(j-1)} < c_j < 0$ and (5.7) by the Mean Value Theorem. $\square$

### Proposition 5.2 (Regime A Brackets, Disjointness, Seam-A, and Sign Certification for $n \ge 80$)
*For each $k \in \{1, \dots, K_A(n)\}$, define the closed-form bracket endpoints*
$$a_k := s_k^- := \frac{Q_k(n)^{-1/3}}{R_k(n)}, \qquad b_k := s_k^+ := \frac{Q_k(n)^{+1/3}}{R_k(n)}. \tag{5.8}$$
*Then for every $n \ge 80$:*
1. *(Disjointness and Seam-A)* $0 < a_1 < b_1 < a_2 < b_2 < \dotsb < a_{K_A} < b_{K_A} < a_{K_A+1} < 1$, with $\Phi_n(b_{K_A}) < (K_A+1)\pi < \Phi_n(a_{K_A+1})$.
2. *(Sign certification)* For every $k \in \{1, \dots, K_A(n)\}$:
   $$(-1)^{k-1} C_n(-a_k) > 0, \qquad (-1)^k C_n(-b_k) > 0, \qquad (-1)^k C_{n+1}(-s) > 0 \quad (\forall\, s \in [a_k, b_k]). \tag{5.9}$$

*Proof.* Note $k_{\min} := K_A(80) = \lfloor 9 / 2.2 \rfloor = 4$, and for every $1 \le k \le K_A(n)$, $m \ge \max(m_0, c_{K_A}^2 k^2)$ with $m_0 = 81$.

**Global $s_{\max}$ bound.** By Lemma 5.1(1), $s \le b_{K_A} = s_{K_A}^+$ for all $s$ in Regime A. Using (5.3)–(5.5), $-\ln s_{K_A}^+ = \ln R_{K_A}(n) - \frac{1}{3}\ln Q_{K_A}(n) > m\beta_{K_A} + c_{K_A} - \frac{1}{3}(\beta_{K_A} + \frac{1}{6m K_A(K_A-1)}) \ge c_{K_A}\sqrt{m} - s_{\mathrm{loss}}$, where $s_{\mathrm{loss}} := \frac{3}{2(k_{\min}-1)} + \frac{1}{3}(\frac{1}{k_{\min}} + \frac{1}{6k_{\min}(k_{\min}^2-1)} + \frac{1}{6m_0 k_{\min}(k_{\min}-1)})$. Thus $s \le s_{\max}(m) := \exp(-(c_{K_A}\sqrt{m} - s_{\mathrm{loss}})) \le s_{\max}(m_0) \le 4.516 \times 10^{-9}$. Since $\sqrt{m} \ge 9 > 4/c_{K_A}$, both $\frac{(m+1)(m+2)}{2} s_{\max}(m)$ and $\frac{\sqrt{m}}{c_{K_A}} \cdot 2(m+1) s_{\max}(m)$ are strictly decreasing in $m \ge m_0$; by (3.4), uniformly for $N \in \{n, n+1\}$ and $s \le b_{K_A}$:
$$E_0(N, s) \le \varepsilon_{E_0} := e^{\frac{(m_0+1)(m_0+2)}{2} s_{\max}(m_0)} - 1 \le 1.537 \times 10^{-5}, \qquad E_j(N, s) \le \varepsilon_{E_1} := e^{2(m_0+1)s_{\max}(m_0)} - 1 \quad (j \ge 1),$$
and $k E_j(N, s) \le k_{\varepsilon} := \frac{\sqrt{m_0}}{c_{K_A}} \cdot 2(m_0+1) s_{\max}(m_0) e^{2(m_0+1)s_{\max}(m_0)} \le 3.03 \times 10^{-6}$ (using $e^x - 1 \le x e^x$).

**Disjointness and Seam-A.** By Lemma 5.1(1)–(2), for all $M \ge m_0$, $\frac{R_2(N)}{R_1(N)} \le (M+1)(2M+1)e^{c_2 + \frac{13}{24M}}(\frac{27}{64})^M$, which is strictly decreasing in $M \ge m_0$ (step ratio $< 1$ verified in `verify.py`), giving $R_2/R_1 \le R_{2/1, \mathrm{ub}}$.
- For $k = 1$: $s_1^+/s_2^- = (Q_1(n) Q_2(n))^{1/3} R_2(n)/R_1(n) \le 4.807 \times 10^{-27} < 1$.
- For $2 \le k < K_A$: $m \ge c_{K_A}^2 (k+1)^2$, so $\ln\frac{R_k(n)}{R_{k+1}(n)} = m(\beta_k-\beta_{k+1}) + (c_k-c_{k+1}) + (\delta_k-\delta_{k+1}) > c_{K_A}^2 - \frac{2}{3} - \frac{13}{72m_0}$, exceeding $\frac{1}{3}(\ln Q_k(n)+\ln Q_{k+1}(n)) < \frac{2}{3}(\beta_2 + \frac{1}{12m_0})$ by a gap $\ge 3.8216 > 0$ (`[DISJ-A]`).
- For Seam-A: with $L := -\ln b_{K_A}$, multiplying the lower bound on $L$ by $K_A$ gives $K_A L > m - M_{\mathrm{loss}}$ where $M_{\mathrm{loss}} := \frac{3}{2}\frac{k_{\min}}{k_{\min}-1} + \frac{1}{3}(1 + \frac{1}{6(k_{\min}^2-1)} + \frac{1}{6m_0(k_{\min}-1)})$, so $\frac{m}{L} < K_A + \frac{(\sqrt{m_0}/c_{K_A}) M_{\mathrm{loss}}}{m_0 - M_{\mathrm{loss}}}$. Also $\frac{L}{m} < y_{K_A, \mathrm{ub}} := \frac{1}{k_{\min}} + \frac{1}{6k_{\min}(k_{\min}^2-1)} + \frac{13}{12m_0^2 k_{\min}(k_{\min}-1)}$. By (4.2), $\frac{\Phi_n(b_{K_A})}{\pi} - K_A < \frac{(\sqrt{m_0}/c_{K_A})M_{\mathrm{loss}}}{m_0 - M_{\mathrm{loss}}} + \frac{1}{2} + \frac{y_{K_A,\mathrm{ub}}}{12(1-\frac{1}{4m_0^2})} \le 0.64262 < 1$ (`[SEAM-A]`), so $\Phi_n(b_{K_A}) < (K_A+1)\pi < \Phi_n(a_{K_A+1})$ and hence $b_{K_A} < a_{K_A+1}$.

**Symmetric pair-sum sign proof.** By Lemma 3.1, regrouping (3.2) symmetrically around index $k$ yields
$$(-1)^{k-1}\frac{C_N(-s)}{(1+s) u_k^{(0)}(N, s)} = \frac{u_{k-1} - u_k}{u_k^{(0)}} + \sum_{r=1}^\infty (-1)^r \frac{u_{k-1-r} - u_{k+r}}{u_k^{(0)}}, \tag{5.10}$$
with the convention $u_j := 0$ for $j < 0$. Define $\Delta_0 := \ln(u_{k-1}^{(0)}/u_k^{(0)}) = -\ln(s R_k(N))$. Across all four cases needed for (5.9), $\Delta_0 = -\gamma \ln Q_k(n)$ where:
- $N = n, s = a_k$: $\gamma = -\frac{1}{3}$ ($\Delta_0 > 0$, main term $e^{\Delta_0} - 1 > 0 \implies (-1)^{k-1} C_n(-a_k) > 0$);
- $N = n, s = b_k$: $\gamma = +\frac{1}{3}$ ($\Delta_0 < 0$, main term $-(1 - e^{\Delta_0}) < 0 \implies (-1)^k C_n(-b_k) > 0$);
- $N = n+1, s \in [a_k, b_k]$: since $s R_k(n+1) = s R_k(n) Q_k(n) \in [Q_k(n)^{2/3}, Q_k(n)^{4/3}]$, we have $\gamma \in [\frac{2}{3}, \frac{4}{3}]$ (split into $[\frac{2}{3}, 1]$ and $[1, \frac{4}{3}]$; $\Delta_0 < 0$, main term $-(1 - e^{\Delta_0}) < 0 \implies (-1)^k C_{n+1}(-s) > 0$).

In every case we certify $\frac{\text{tail + } E\text{-perturbation}}{|e^{\Delta_0} - 1|} < 1$:
- **$k = 1$:** Using $s R_2(N) \le Q_1(n)^{4/3} R_{2/1, \mathrm{ub}} < \frac{1}{2}$, Lemma 5.1(1) ($R_j$ decreasing), and $(Q_1^{1/3}+1)\varepsilon_{E_0}$ for $r=0$, `verify.py` certifies error $\le 1.086 \times 10^{-4} < 1$ (`[A-k=1]`).
- **$k = 2$:** Using $u_0^{(0)}/u_2^{(0)} \le Q_2(n)^{2/3} R_{2/1, \mathrm{ub}}$, $s R_3(N) \le Q_2(n)^{4/3}\exp(m_0(\beta_3-\beta_2) + c_3 - c_2 + \frac{13}{72m_0}) < \frac{1}{2}$, and $(Q_2^{1/3}+1)\varepsilon_{E_1}$, `verify.py` certifies error $\le 1.661 \times 10^{-5} < 1$ (`[A-k=2]`).
- **$3 \le k \le 25$:** For each paired term $1 \le r \le k - 2$, write $\ln(u_{k-1-r}^{(0)}/u_k^{(0)}) = A_r$ and $\ln(u_{k+r}^{(0)}/u_k^{(0)}) = B_r$, where
  $$A_r = -(r+1)\gamma\ln Q_k - M S_L(r) - C_L(r) + \sum_{i=1}^r(\delta_k - \delta_{k-i}), \qquad B_r = r\gamma\ln Q_k - M S_R(r) - C_R(r) + \sum_{i=1}^r(\delta_{k+i} - \delta_k),$$
  with $S_L(r) := \sum_{i=1}^r(\beta_{k-i}-\beta_k)$, $S_R(r) := \sum_{i=1}^r(\beta_k-\beta_{k+i})$, $C_L(r) := \sum_{i=1}^r(c_{k-i}-c_k)$, $C_R(r) := \sum_{i=1}^r(c_k-c_{k+i})$. By the elementary inequality $|e^A - e^B| \le e^{\max(A, B)}\min(1, |A-B|)$ and $S_L(r) > S_R(r) > 0$,
  $$|e^{A_r} - e^{B_r}| \le e^{\max(A_{0,r}, B_{0,r}) - M S_{\min}(r)} \min\!\big(1,\ d_{\mathrm{const}} + M(S_L(r) - S_R(r))\big).$$
  Because $(a + bM)e^{-cM}$ ($a, b \ge 0$, $c > 0$) has derivative $(b - ca - cbM)e^{-cM} < 0$ whenever $cM > 1$, asserting $M_{\min} S_{\min}(r) > 1$ (where $M_{\min} := \max(m_0, c_{K_A}^2 k^2)$) proves the maximum over ALL $M \ge M_{\min}$ is achieved at $M = M_{\min}$. Adding the geometric right tail ($r \ge k-1$, step ratio $q_R < \frac{1}{2}$), left term $u_0/u_k = (u_1/u_k)(u_0/u_1)$ (using $u_0^{(0)}/u_1^{(0)} \le e^{\Delta_0} R_{2/1, \mathrm{ub}}$), and $E$-perturbations, `verify.py` certifies worst error $\le 0.40099 < 1$ across all $3 \le k \le 25$ and all four $\gamma$-cases (`[A-k=3..25]`).
- **Uniform $k \ge k_0 := 26$ (all the way to $\infty$):** Here $M \ge c_{K_A}^2 k^2 \ge M_{0,\mathrm{big}} := c_{K_A}^2 k_0^2 = 3271.84$, and $\ln Q_k(n) \in [q_{\mathrm{lo}}/k, q_{\mathrm{hi}}/k]$ by (5.4)–(5.5), so $k|e^{\Delta_0}-1| \ge \mathrm{main}_{k,\mathrm{lb}} > 0$ is bounded below independently of $k$. We multiply both sides of (5.10) by $k$:
  - *Head pairs $1 \le r \le 6$:* By (5.6)–(5.7), $S_R(r) \ge \frac{a_{R,r}}{k^2}$ ($a_{R,r} := \sum_{i=1}^r \frac{i}{1+i/k_0}$), $S_L(r) - S_R(r) \le \frac{\mathrm{diff}_r}{k^3}$, and $|C_L|, |C_R| \le O(k^{-2})$. Setting $x := M/k^2 \ge c_{K_A}^2$, the monotonicity of $(a + bx)e^{-a_{R,r} x}$ (verified via $c_{K_A}^2 a_{R,r} > 1$) maximizes the bound at $x = c_{K_A}^2$, canceling $k$ completely!
  - *Middle pairs $7 \le r \le \lfloor k/2 \rfloor$ (Piece 1):* Here $k - r \ge k/2$ and $k + r \le \frac{3}{2}k$, so $M S_R(r) \ge \frac{c_{K_A}^2}{3} r(r+1)$ while the positive non-$M$ exponent is $\le C_{\mathrm{pos}} r(r+1)$ with $\alpha_1 := \frac{c_{K_A}^2}{3} - C_{\mathrm{pos}} > 1$, and $k|A_r - B_r| \le C_{\mathrm{poly}} r^3$. Summing via the geometric ratio $\rho_1 := (\frac{8}{7})^3 e^{-16\alpha_1} < \frac{1}{2}$ yields $p_1 \le 2.74 \times 10^{-36}$.
  - *Far tails $r \ge r_h := \lfloor k/2 \rfloor + 1$ (Piece 2):* Both $M S_R(r_h)$ and $M S_L(r_h)$ exceed $\alpha_2 k^2$ where $\alpha_2 := \frac{c_{K_A}^2}{8(\frac{3}{2} + \frac{1}{k_0})}$, while the right and left step ratios satisfy $\rho_{2R} < \frac{1}{2}$ and $\rho_{2L} < \frac{1}{2}$ by Lemma 5.1(1) and (5.6). Since $k e^{-\alpha_2 k^2}$ decreases for $k \ge k_0$ ($2\alpha_2 k_0^2 > 1$), summing both geometric tails gives $p_2 \le 1.78 \times 10^{-113}$.
  - Combining head pairs, Piece 1, Piece 2, and exact $E$-perturbation bounds, `verify.py` certifies worst error $\le 0.35001 < 1$ uniformly across all $k \ge 26$, all $M \ge c_{K_A}^2 k^2$, and all four $\gamma$-cases (`[A-k>=26]`). $\square$

---

## 6. Proof of the Main Theorem (Assembly for All $n \ge 1$)

**Theorem.** *For every $n \ge 1$ (and trivially $n = 0$), $H_{\mathrm{NC}_{n+1}}(t) \ll H_{\mathrm{NC}_{n+2}}(t)$. For every $n \ge 2$, the zeros of $C_n(t)$ and $C_{n+1}(t)$ are all real, negative, simple, and strictly interlace.*

*Proof.* The cases $n = 0, 1$ are immediate (§1), and all $1 \le n \le 80$ are proved by Proposition 2.1 and the exact integer Sturm–Cauchy computation in `verify.py` (§2).

Now let $n \ge 80$. By Propositions 4.4 and 5.2, the $K_n = \lfloor (n-1)/2 \rfloor$ closed intervals $[a_j, b_j]$ ($1 \le j \le K_A$ from (5.8) and $K_A+1 \le j \le K_n$ from Proposition 4.4) satisfy
$$0 < a_1 < b_1 < a_2 < b_2 < \dotsb < a_{K_n} < b_{K_n} < 1,$$
with $(-1)^{j-1} C_n(-a_j) > 0$ and $(-1)^j C_n(-b_j) > 0$ for every $1 \le j \le K_n$. By the Intermediate Value Theorem, $C_n(-s)$ has at least one root $r_j \in (a_j, b_j)$ for each $1 \le j \le K_n$. Since $C_n$ has degree $n-1$ and is palindromic (with $C_n(-1) = 0$ when $n$ is even), $C_n(-s)$ has at most $K_n$ roots in $(0, 1)$; therefore $0 < r_1 < r_2 < \dotsb < r_{K_n} < 1$ are **all** the roots of $C_n(-s)$ in $(0, 1)$ (all simple, and $s = 1$ is a simple root iff $n$ is even).

By Propositions 4.4(2) and 5.2(2), $(-1)^j C_{n+1}(-r_j) > 0$ for every $1 \le j \le K_n$, while $C_{n+1}(0) = 1 > 0$.
- **Case $n = 2q$ even ($K_n = q - 1$, $K_{n+1} = q$):** By Lemma 3.2(1), $(-1)^q C_{2q+1}(-1) = (-1)^{K_n+1} C_{n+1}(-1) > 0$. Thus $C_{n+1}(-s)$ alternates sign strictly along the $q+1$ points $0 < r_1 < \dotsb < r_{q-1} < 1$, forcing $q$ simple roots $\tau_1, \dots, \tau_q$ of $C_{n+1}(-s)$ with
  $$0 < \tau_1 < r_1 < \tau_2 < r_2 < \dotsb < r_{q-1} < \tau_q < 1$$
  (which exhaust all $K_{n+1} = q$ roots of $C_{n+1}(-s)$ in $(0, 1)$, while $C_n(-1) = 0$ and $C_{n+1}(-1) \ne 0$).
- **Case $n = 2q+1$ odd ($K_n = q$, $K_{n+1} = q$):** $C_{n+1}(-s)$ alternates sign strictly along the $q+1$ points $0 < r_1 < \dotsb < r_q < 1$, forcing $q$ simple roots $\tau_1, \dots, \tau_q$ of $C_{n+1}(-s)$ with
  $$0 < \tau_1 < r_1 < \tau_2 < r_2 < \dotsb < \tau_q < r_q < 1$$
  (plus the simple root at $s = 1$ of $C_{n+1}(-s)$, while $C_n(-1) \ne 0$).

In both parities, adjoining the reciprocal roots $1/r_j, 1/\tau_j \in (1, \infty)$ by palindromicity and substituting $t = -s$ yields the strict interlacing of all $n-1$ zeros of $C_n(t)$ and all $n$ zeros of $C_{n+1}(t)$:
$$-\frac{1}{\tau_1} < -\frac{1}{r_1} < \dotsb < (-1) < \dotsb < -r_1 < -\tau_1 < 0.$$
Hence $H_{\mathrm{NC}_{n+1}}(t) \ll H_{\mathrm{NC}_{n+2}}(t)$ holds for every $n$. $\square$

---

## 7. Certified Numerical Summary (`verify.py`)

All quantities below are certified by `.venv/bin/python -u targets/alexandersson-2609.05131-prob10.1/verify.py` (35-digit outward-rounded `mpmath.iv` interval arithmetic, zero Python floats, $n_0 = 80$, $m_0 = 81$, $c_{K_A} = 22/10$, $Y_{\max} = 23/10$):

| Check | Exact Statement Certified | Certified Bound | Requirement |
| :--- | :--- | :--- | :--- |
| `[Part 0]` | Direct Smirnov DP (1.1) == $O(n^3)$ GF (1.2) | Exact integer match, $1 \le n \le 15$ | Identity |
| `[Part 1]` | Exact $\gamma$-expansion & Sturm–Cauchy $I_{-\infty}^0(\Gamma_n/\Gamma_{n+1}) = d_{n+1}$ | Exact integer PASS, $1 \le n \le 80$ | $= d_{n+1}$ |
| `[SEAM-B]` | $\sqrt{m_0}(\frac{1}{c_{K_A}} - \frac{1}{Y_{\max}}) - (\frac{1}{8} + \frac{Y_{\max}}{12\sqrt{m_0}(1-\frac{1}{4m_0^2})})$ | $\ge 0.0315685$ | $> 0$ |
| `[REGIME B3]` | $\lambda < 1$ error $E_B$ ($C_n$ / $C_{n+1}$) | $\le 2.934 \times 10^{-28}$ / $\le 2.058 \times 10^{-28}$ | $< 1$ |
| `[REGIME B4]` | $\lambda \ge 1, Y \le 0.5$ error $E_B$ ($C_n$ / $C_{n+1}$) | $\le 1.745 \times 10^{-16}$ / $\le 1.233 \times 10^{-16}$ | $< 1$ |
| `[REGIME B5]` | $0.5 \le Y \le 2.3$ error $E_B$ ($C_n$ / $C_{n+1}$; $p_{\mathrm{tail}} \ge 61.96$) | $\le 0.090792$ / $\le 0.074801$ | $< 1$ |
| `[REGIME A0]` | Global $s_{\max}$, $\varepsilon_{E_0}$, $k\varepsilon_{E_1}$ | $\le 4.516 \times 10^{-9}$, $\le 1.537 \times 10^{-5}$, $\le 3.03 \times 10^{-6}$ | $< 10^{-2}$ |
| `[SEAM-A]` | $\Phi_n(b_{K_A})/\pi - K_A$ | $\le 0.64262$ | $< 1$ |
| `[DISJ-A]` | $k=1$ ratio $s_1^+/s_2^-$; $k \ge 2$ log-gap | $\le 4.807 \times 10^{-27}$; gap $\ge 3.8216$ | $< 1$; $> 0$ |
| `[A-k=1]` | Regime A relative error ($k=1$, all 4 cases) | $\le 1.086 \times 10^{-4}$ | $< 1$ |
| `[A-k=2]` | Regime A relative error ($k=2$, all 4 cases) | $\le 1.661 \times 10^{-5}$ | $< 1$ |
| `[A-k=3..25]` | Regime A relative error ($3 \le k \le 25$, all 4 cases) | $\le 0.40099$ | $< 1$ |
| `[A-k>=26]` | Regime A relative error (ALL $k \ge 26$ to $\infty$; $p_1 \le 2.74 \times 10^{-36}$, $p_2 \le 1.78 \times 10^{-113}$) | $\le 0.35001$ | $< 1$ |
