# Proof of Hare–Hichri (arXiv:2603.19554v1) Conjecture 3.3 (`conj:1`)

**Conjecture (Hare–Hichri, arXiv:2603.19554v1, Section 3.1, Conjecture 3.3 / `conj:1`).**
Let $\beta_d > 1$ be the Perron root of $P_d(x) = x^d - x - 1$. Then for all $d \geq 4$ and all $k \geq 1$, $\beta_d^k$ is non-Parry.

**Classification:** Written proof + exact integer-interval verification of $4 \le d \le 499$ (`verify.py`). (Not peer-reviewed; not Lean-checked.)

---

## 1. Preliminaries: Irreducibility, Perron Property, and Criteria

1. **Irreducibility and degree of $\beta_d^k$.**
   By Selmer (1956, Theorem 1), $P_d(x) = x^d - x - 1$ is irreducible over $\mathbb{Q}$ for all $d \geq 2$. Since $P_d(1) = -1 < 0$ and $P_d'(x) = d x^{d-1} - 1 > 0$ for all $x \geq 1$, $P_d$ has a unique real root $\beta_d > 1$. For any root $\gamma \neq \beta_d$ of $P_d$, $|\gamma|^d = |\gamma + 1| \le |\gamma| + 1$; if $|\gamma| \ge \beta_d > 1$, then $|\gamma|^d - |\gamma| - 1 \ge \beta_d^d - \beta_d - 1 = 0$, forcing equality throughout and hence $|\gamma + 1| = |\gamma| + 1$, so $\gamma \in \mathbb{R}_{>0}$, contradicting uniqueness of $\beta_d$. Thus $|\gamma| < \beta_d$ for every conjugate $\gamma \neq \beta_d$, so $\beta_d$ is a Perron number of degree $d$. For every $k \geq 1$, no conjugate $\gamma \neq \beta_d$ satisfies $\gamma^k = \beta_d^k$ (as $|\gamma|^k < \beta_d^k$), so $\beta_d^k$ also has degree $d$ over $\mathbb{Q}$, is a Perron number, and its Galois conjugates are $\gamma^k$ as $\gamma$ ranges over the conjugates of $\beta_d$.

2. **Solomyak's golden-ratio bound.**
   By Solomyak (1994, *Proc. London Math. Soc.* (3) 68, 477–498; cited in `arXiv:2603.19554v1` Section 1 and Lemma 2.4), every Galois conjugate $\alpha$ of a Parry number satisfies $|\alpha| \le \theta_0 := \frac{1+\sqrt{5}}{2}$. Consequently, if $\gamma$ is a conjugate of $\beta_d$ ($\gamma \neq \beta_d$) and $|\gamma|^k > \theta_0$, then $\beta_d^k$ is non-Parry.

3. **Akiyama's divergence criterion.**
   Let $q = \beta_d^k$ and let $\sigma: \mathbb{Q}(\beta_d) \to \mathbb{Q}(\gamma)$ be the field isomorphism $\beta_d \mapsto \gamma$ for some conjugate $\gamma \neq \beta_d$ with $|\gamma| > 1$, setting $c := \sigma(q) = \gamma^k$ (so $|c| > 1$). Recall that $q$ is a Parry number if and only if the greedy $\beta$-expansion $d_q(1)$ is finite (ending in $0^\infty$) or eventually periodic, equivalently the orbit $\{x_m := T_q^m(1) : m \ge 0\}$ under $T_q(x) = qx - \lfloor qx \rfloor$ is finite, where $x_0 = 1$ and $x_{m+1} = q x_m - c_{m+1}$ with $c_{m+1} = \lfloor q x_m \rfloor \in \{0, 1, \dots, \lfloor q \rfloor\}$. Applying $\sigma$ gives $\sigma(x_{m+1}) = c\,\sigma(x_m) - c_{m+1}$ for all $m \ge 0$. If there exists $n \ge 1$ such that
   $$|\sigma(x_n)| > \frac{\lfloor q \rfloor}{|c| - 1},$$
   then by induction for all $m \ge n$, $|\sigma(x_{m+1})| \ge |c|\,|\sigma(x_m)| - \lfloor q \rfloor > |\sigma(x_m)|$, so $\{|\sigma(x_m)| : m \ge 0\}$ is strictly increasing from $n$ onward and hence infinite, contradicting finiteness of $\{x_m\}$. Thus $q$ is non-Parry.

4. **Closed-form Akiyama block for $q \in (1, 2)$.**
   Suppose $1 < q < 2$ (so $\lfloor q \rfloor = 1$). Let $m_0 \ge 2$ be the unique integer such that
   $$q^{m_0 - 2}(q - 1) < 1 \le q^{m_0 - 1}(q - 1)$$
   (when $q(q-1) \ge 1$, $m_0 = 2$ and $q^0(q-1) = q - 1 < 1$). Suppose we show that
   $$|c^{2m_0 - 2}(1 - c^{-1} - c^{-m_0})| > \frac{1}{|c| - 1}.$$
   Then in particular $c^{m_0} - c^{m_0 - 1} - 1 \neq 0$, and since $q$ and $c$ are Galois conjugates, $q^{m_0} - q^{m_0 - 1} - 1 \neq 0$, so $q^{m_0 - 1}(q - 1) > 1$ strictly. Because $q^{m_0 - 2}(q - 1) < 1$, we also have $q^{m_0 - 1}(q - 1) < q < 2$. Tracking the greedy orbit of $1$:
   - $c_1 = \lfloor q \rfloor = 1$ and $x_1 = q - 1 \in (0, 1)$.
   - For $2 \le j \le m_0 - 1$, $q x_{j-1} = q^{j-1}(q - 1) \le q^{m_0 - 2}(q - 1) < 1$, so $c_j = 0$ and $x_j = q^{j-1}(q - 1)$.
   - At $j = m_0$, $q x_{m_0 - 1} = q^{m_0 - 1}(q - 1) \in (1, 2)$, so $c_{m_0} = 1$ and $x_{m_0} = q^{m_0 - 1}(q - 1) - 1 = q^{m_0}(1 - q^{-1} - q^{-m_0}) \in (0, q - 1)$.
   - If $m_0 = 2$, then $2m_0 - 2 = 2 = m_0$, so $x_{2m_0 - 2} = x_2 = q^2(1 - q^{-1} - q^{-2})$. If $m_0 \ge 3$, then for $1 \le t \le m_0 - 2$, $q^t x_{m_0} < q^{m_0 - 2}(q - 1) < 1$, so $c_{m_0 + 1} = \dots = c_{2m_0 - 2} = 0$ and $x_{2m_0 - 2} = q^{m_0 - 2} x_{m_0} = q^{2m_0 - 2}(1 - q^{-1} - q^{-m_0})$.

   Therefore $\sigma(x_{2m_0 - 2}) = c^{2m_0 - 2}(1 - c^{-1} - c^{-m_0})$, so by the Akiyama divergence criterion $q = \beta_d^k$ is non-Parry.

---

## 2. Exact Verification for $4 \le d \le 499$

For every $d \in \{4, 5, \dots, 499\}$, the companion script `verify.py` uses **pure 128-bit fixed-point integer interval arithmetic** (zero floating-point operations in any verification check) to:
1. Bracket $\beta_d \in (b_{\mathrm{lo}}, b_{\mathrm{hi}})$ via $P_d(b_{\mathrm{lo}}) < 0 < P_d(b_{\mathrm{hi}})$.
2. Certify a complex root $\gamma_d$ in the open upper half-plane via Rouché's theorem on a disk $|z - z_*| < 2^{-60}$ around an integer-scaled center $z_*$, verifying $|P_d'(z_*)| \cdot r > |P_d(z_*)| + \frac{d(d-1)}{2} r^2 (|z_*| + r)^{d-2}$ and $\mathrm{Im}(z_*) > r$.
3. Increment $k = 1, 2, \dots$ until $|\gamma_d|^{2k} > \frac{3+\sqrt{5}}{2} = \theta_0^2$ (checked strictly via $2s - 3 > 0$ and $(2s - 3)^2 > 5$), which disposes of all larger $k$ by Solomyak's bound (since $|\gamma_d| > 1$).
4. For each $k$ prior to that threshold:
   - For $d \in \{4, 5\}$, certify the exact greedy digits of $T_q^j(1)$ and verify $|\sigma(T_q^n(1))| > \frac{\lfloor q \rfloor}{|c| - 1}$ at an explicit $n \le 35$.
   - For $6 \le d \le 499$, certify $q \in (1, 2)$, determine $m_0$ strictly via $q^{m_0 - 2}(q - 1) < 1 < q^{m_0 - 1}(q - 1)$, and verify $|c^{2m_0 - 2}(1 - c^{-1} - c^{-m_0})|^2 (|c| - 1)^2 > 1$.

---

## 3. Analytic Proof for All $d \ge 500$

Assume $d \ge 500$.

### Lemma 3.1 (Bounds on $\beta_d$)
We have
$$2^{1/d} < \beta_d < 1 + \frac{\ln 2}{d} + \frac{1}{d^2}, \qquad \frac{\ln 2}{d} < \ln \beta_d < \frac{\ln 2}{d} + \frac{1}{d^2}.$$

*Proof.* Since $\beta_d > 1$, $\beta_d^d = 1 + \beta_d > 2$, giving the lower bounds. For the upper bound, set $u = \frac{\ln 2}{d} + \frac{1}{d^2} < 0.0014$ and $x_+ = 1 + u$. Since $\ln(1 + u) \ge u - u^2/2$,
$$d \ln(1 + u) \ge \ln 2 + \frac{1}{d} - \frac{(\ln 2 + 1/d)^2}{2d} > \ln 2 + \frac{1 - 0.242}{d} > \ln 2 + \frac{0.75}{d}.$$
Hence $(1+u)^d > 2 e^{0.75/d} > 2(1 + \frac{0.75}{d}) = 2 + \frac{1.5}{d} > 1 + x_+$, so $P_d(x_+) > 0$ and $\beta_d < x_+$. Also $\ln \beta_d < \ln(1+u) < u$. $\square$

### Lemma 3.2 (Existence and bounds on $\gamma_d$)
Let $z_0 = \exp\left(\frac{\ln 2 + 2\pi i}{d}\right)$, so $|z_0| = 2^{1/d}$ and $z_0^d = 2$. For all $d \ge 500$, $P_d$ has a unique root $\gamma_d$ in the disk $|z - z_0| < \frac{5}{d^2}$. Moreover $\mathrm{Im}(\gamma_d) > 0$ (so $\gamma_d \neq \beta_d$),
$$\ln |\gamma_d| \ge \frac{\ln 2}{d} - \frac{5.01}{d^2}, \qquad \text{and} \qquad \left|\arg(\gamma_d) - \frac{2\pi}{d}\right| < \frac{5.01}{d^2}.$$

*Proof.* On $|w| = \rho_d := \frac{5}{d^2}$, write $P_d(z_0 + w) = \frac{2d}{z_0} w + E(w)$, where
$$E(w) = (1 - z_0) - w + \sum_{j=2}^d \binom{d}{j} z_0^{d-j} w^j.$$
For $d \ge 500$:
- $|z_0| = 2^{1/d} < 1.0014$, so $\left|\frac{2d}{z_0} w\right| = \frac{10}{|z_0| d} > \frac{9.98}{d}$.
- With $\zeta = \frac{\ln 2 + 2\pi i}{d}$, $|\zeta| = \frac{\sqrt{(\ln 2)^2 + 4\pi^2}}{d} < \frac{6.322}{d} < 0.0127$, so $|1 - z_0| = |e^\zeta - 1| \le |\zeta| e^{|\zeta|} < \frac{6.41}{d}$.
- $|w| = \frac{5}{d^2} \le \frac{0.01}{d}$.
- $\left|\sum_{j=2}^d \binom{d}{j} z_0^{d-j} w^j\right| \le 2\left(\left(1 + \frac{5}{2^{1/d} d^2}\right)^d - 1 - \frac{5}{2^{1/d} d}\right) < 2\left(e^{5/d} - 1 - \frac{5}{d}\right) < \frac{0.06}{d}$ (since $5/d \le 0.01$ and $e^y - 1 - y \le y^2$ on $[0, 0.01]$).

Thus $|E(w)| < \frac{6.48}{d} < \frac{9.98}{d} < \left|\frac{2d}{z_0} w\right|$, so by Rouché's theorem $P_d$ has a unique root $\gamma_d$ in $|z - z_0| < \frac{5}{d^2}$. Since $\mathrm{Im}(z_0) = 2^{1/d}\sin(2\pi/d) > \frac{6.28}{d} > \frac{5}{d^2}$, we have $\mathrm{Im}(\gamma_d) > 0$. Writing $x = \frac{5}{2^{1/d} d^2} \le 2\cdot 10^{-5}$,
$$|\gamma_d| \ge 2^{1/d}(1 - x), \qquad \ln|\gamma_d| \ge \frac{\ln 2}{d} + \ln(1 - x) \ge \frac{\ln 2}{d} - x - x^2 > \frac{\ln 2}{d} - \frac{5.01}{d^2},$$
and $|\sin(\arg(\gamma_d) - \frac{2\pi}{d})| \le x$, hence $|\arg(\gamma_d) - \frac{2\pi}{d}| \le \arcsin(x) < \frac{5.01}{d^2}$. $\square$

### Completion of Proof for $d \ge 500$

Fix $k \ge 1$. If $|\gamma_d|^k > \theta_0$, then $\beta_d^k$ is non-Parry by Solomyak's bound. Assume therefore that $|\gamma_d|^k \le \theta_0$, and set $q = \beta_d^k$, $c = \gamma_d^k$, and $t = k/d$.

By Lemma 3.2, $\ln |\gamma_d| \ge \frac{\ln 2 - 5.01/500}{d} > \frac{0.683}{d}$, so
$$t = \frac{k}{d} \le \frac{\ln \theta_0}{0.683} < 0.705.$$
By Lemma 3.1, $\ln q = k \ln \beta_d < 0.705(\ln 2 + \frac{1}{500}) < 0.491 < \ln 2$, so $1 < q < e^{0.491} < 1.635 < 2$, hence $\lfloor q \rfloor = 1$. Also $1 < |c| < q$ (from Perron property and $|\gamma_d| > 1$), and
$$0 < \ln q - \ln |c| = k(\ln \beta_d - \ln |\gamma_d|) < \frac{6.01 k}{d^2}.$$
Using $q - |c| = q(1 - e^{-(\ln q - \ln|c|)}) \le q(\ln q - \ln |c|)$ and $q - 1 > \ln q > \frac{k \ln 2}{d}$,
$$\frac{|c| - 1}{q - 1} = 1 - \frac{q - |c|}{q - 1} \ge 1 - \left(1 + \frac{1}{q - 1}\right)(\ln q - \ln |c|) > 1 - \left(\frac{6.01 k}{d^2} + \frac{6.01}{d \ln 2}\right) > 1 - 0.0259 = 0.9741.$$

Let $m_0 \ge 2$ be minimal with $q^{m_0 - 1}(q - 1) \ge 1$, and define
$$F(c) := (|c| - 1) |c^{2m_0 - 2}(1 - c^{-1} - c^{-m_0})| = (|c| - 1)|c|^{m_0 - 2}|c^{m_0 - 1}(c - 1) - 1|.$$
By Section 1.4, it suffices to prove $F(c) > 1$. Using the reverse triangle inequality and $|c| \le \theta_0$,
$$F(c) \ge (|c| - 1) |c|^{m_0 - 2}\left(|c|^{m_0 - 1}|c - 1| - 1\right) \ge \frac{|c| - 1}{q - 1} \cdot \frac{1}{\theta_0} \cdot \left(\frac{|c|}{q}\right)^{m_0 - 1} \left(\left(\frac{|c|}{q}\right)^{m_0 - 1}\frac{|c - 1|}{q - 1} - 1\right)$$
since $q^{m_0 - 1}(q - 1) \ge 1$. Let $\phi = k \arg(\gamma_d) \in [t(2\pi - 0.01002),\; t(2\pi + 0.01002)]$.

- **Case A ($0 < t \le 0.5$).**
  If $m_0 \ge 3$, then $q^{m_0 - 2}(q - 1) < 1$ and $q - 1 > \ln q > \frac{k \ln 2}{d}$, so
  $$m_0 - 1 < 1 + \frac{\ln(1/(q-1))}{\ln q} < 1 + \frac{d}{k \ln 2}\ln\left(\frac{d}{\ln 2}\right),$$
  whence $(m_0 - 1)(\ln q - \ln |c|) < \frac{6.01 k}{d^2} + \frac{6.01 \ln(d/\ln 2)}{d \ln 2} < 0.1227$ for $d \ge 500$ (which also trivially holds if $m_0 = 2$). Thus $(|c|/q)^{m_0 - 1} > e^{-0.1227} > 0.8845$.
  Next, $0 < \frac{\phi}{2} \le \frac{\pi}{2} + 0.00251 < \pi$. By concavity of $\sin$ on $[0, \pi]$, $\sin(\phi/2) \ge \frac{\cos(0.00251)}{\pi/2 + 0.00251} \cdot \frac{\phi}{2} > 0.635 \cdot \frac{\phi}{2}$, so
  $$|c - 1| = \sqrt{(|c| - 1)^2 + 4|c|\sin^2(\phi/2)} > 2\sin(\phi/2) > 0.635\,\phi \ge 0.635(2\pi - 0.01002)t > 3.98 t.$$
  Meanwhile $\ln q < 0.6952 t \le 0.3476$, so $q - 1 = e^{\ln q} - 1 \le (\ln q) e^{\ln q} < 0.6952 t \cdot e^{0.3476} < 0.985 t$. Thus $\frac{|c - 1|}{q - 1} > \frac{3.98}{0.985} > 4.04$, and
  $$F(c) > 0.9741 \cdot \frac{1}{\theta_0} \cdot 0.8845 \cdot (0.8845 \cdot 4.04 - 1) > 1.36 > 1.$$

- **Case B ($0.5 < t \le 0.705$).**
  Here $q > 2^t > \sqrt{2}$, so $q^3(q - 1) > 2\sqrt{2}(\sqrt{2} - 1) = 4 - 2\sqrt{2} > 1.17 > 1$, forcing $m_0 \le 4$. Hence $(m_0 - 1)(\ln q - \ln |c|) \le 3 \cdot \frac{6.01 \cdot 0.705}{500} < 0.0255$, so $(|c|/q)^{m_0 - 1} > e^{-0.0255} > 0.9748$.
  Also $|c| > e^{0.5 \cdot 0.683} > 1.407$ and $\phi \in [3.1365, 4.4368]$, on which $\cos \phi \le \cos 4.4368 < -0.272$. Therefore
  $$|c - 1| = \sqrt{|c|^2 + 1 - 2|c|\cos\phi} > \sqrt{1.407^2 + 1 + 2(1.407)(0.272)} > 1.935.$$
  Since $q - 1 < e^{0.491} - 1 < 0.634$, we have $\frac{|c - 1|}{q - 1} > \frac{1.935}{0.634} > 3.05$, and
  $$F(c) > 0.9741 \cdot \frac{1}{\theta_0} \cdot 0.9748 \cdot (0.9748 \cdot 3.05 - 1) > 1.15 > 1.$$

In both cases $F(c) > 1$, completing the proof for all $d \ge 500$ and all $k \ge 1$. Combined with the exact verification for $4 \le d \le 499$, $\beta_d^k$ is non-Parry for all $d \ge 4$ and all $k \ge 1$. $\blacksquare$
