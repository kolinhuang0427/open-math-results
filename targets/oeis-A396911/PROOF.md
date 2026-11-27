# Proof of Sean A. Irvine's Bound on OEIS A396911 (Vogel Phyllotaxis Walk)

## Primary Source and Exact Statement

**Primary source:** OEIS **A396911** (author: Witold Tatkiewicz, Jun 09 2026; revision 48, `2026-06-22T17:16:16-04:00`, offset `0,3`), together with OEIS **A131988** (golden angle $\theta = (4 - 2\phi)\pi = \pi(3 - \sqrt{5}) = 2\pi \phi^{-2}$, revision 20).

For $k \in \mathbb{Z}_{\ge 0}$, define the points of Vogel's phyllotaxis spiral lattice by
$$p_k := \bigl(\sqrt{k}\cos(k\theta),\ \sqrt{k}\sin(k\theta)\bigr) \in \mathbb{R}^2, \qquad \theta := \pi(3 - \sqrt{5}) = 2\pi(2 - \phi) = 2\pi\phi^{-2},$$
where $\phi := \frac{1 + \sqrt{5}}{2}$. Starting at $p_0 = (0, 0)$ (so $a(0) = 0$), at each step $n \ge 1$ move from $p_{a(n-1)}$ to a closest unvisited point $p_j$ ($j \in \mathbb{Z}_{\ge 0} \setminus \{a(0), \dots, a(n-1)\}$) in Euclidean distance, and let $a(n) := j$.

> **Conjecture (OEIS A396911, Sean A. Irvine, Jun 21 2026):**
> $$a(n) \le \frac{3}{2} n^2 \qquad \text{for all } n \ge 0.$$

We prove this conjecture for all $n \ge 0$ (Theorem 1 below), unconditionally under any tie-breaking rule. In the course of the proof we also resolve Pontus von Brömssen's monotonicity and Fibonacci-difference questions on OEIS A396911: $a(n)$ is strictly increasing for all $n \ge 0$, every first difference $a(n+1) - a(n)$ is a Fibonacci number advancing monotonically through $F_2, F_4, F_5, F_6, \dots$, and $\limsup_{n \to \infty} a(n)/n^2 = \pi/\sqrt{5} \approx 1.40496 < 3/2$.

---

## Notation and Exact Distance Formulas

Let $F_0 = 0, F_1 = 1, F_{m+1} = F_m + F_{m-1}$ be the Fibonacci sequence, so Binet's formula gives $F_m = \frac{\phi^m - (-\phi)^{-m}}{\sqrt{5}}$. Recall $\phi^2 = \phi + 1$, $\phi^{-1} = \phi - 1$, $\phi^{-2} = 2 - \phi$, and $\phi + \phi^{-1} = \sqrt{5}$. Define
$$c := \frac{\phi}{4\sqrt{5}\pi}, \qquad K_m := c\,\phi^{2m} = \frac{\phi^{2m+1}}{4\sqrt{5}\pi}.$$
Note that $K_{m-1} = \phi^{-2} K_m$, $\frac{\phi^{2m}}{20 K_m} = \frac{\pi}{\sqrt{5}\,\phi}$, and $4\pi^2 K_m \phi^{-2m} = \frac{\pi\phi}{\sqrt{5}}$.

For real $k > 0$ and integer $d$ with $k + d \ge 0$, define
$$D^2(k, k+d) := (\sqrt{k+d} - \sqrt{k})^2 + 4\sqrt{k(k+d)}\sin^2\!\left(\frac{d\theta}{2}\right) = 2k + d - 2\sqrt{k(k+d)}\cos(d\theta).$$
For $k, j \in \mathbb{Z}_{\ge 0}$, $D^2(k, j) = \|p_j - p_k\|_2^2$. Set $R_+(k, d) := (\sqrt{k+d} - \sqrt{k})^2$ for $d > 0$ and $R_-(k, d) := (\sqrt{k} - \sqrt{k-d})^2$ for $0 < d \le k$. Notice that for $0 < d \le k$,
$$R_-(k, d) = \frac{d^2}{(\sqrt{k} + \sqrt{k-d})^2} > \frac{d^2}{(\sqrt{k+d} + \sqrt{k})^2} = R_+(k, d).$$
For any $x \in \mathbb{R}$, let $\|x\|_{\mathbb{Z}} := \min_{q \in \mathbb{Z}} |x - q| \in [0, \frac{1}{2}]$. Since $\frac{d\theta}{2} = \pi d \phi^{-2}$, we have $|\sin(d\theta/2)| = \sin(\pi \|d\phi^{-2}\|_{\mathbb{Z}})$ for every $d \in \mathbb{Z}$.

---

## Lemmas

### Lemma 1 (Exact Fibonacci Angles and Best-Approximation Gap)
1. For every integer $m \ge 2$,
   $$F_m \phi^{-2} - F_{m-2} = (-1)^m \phi^{-m},$$
   and hence $\|F_m \phi^{-2}\|_{\mathbb{Z}} = \phi^{-m}$ and $|\sin(F_m\theta/2)| = \sin(\pi \phi^{-m})$.
2. For every integer $m \ge 3$ and every integer $d$ satisfying $1 \le d < F_{m+1}$ and $d \notin \{F_{m-1}, F_m\}$,
   $$\|d \phi^{-2}\|_{\mathbb{Z}} \ge \phi^{-(m-2)}.$$

**Proof.**
1. Induct on $m \ge 2$. For $m = 2$, $F_2 \phi^{-2} - F_0 = \phi^{-2} = (-1)^2 \phi^{-2}$. For $m = 3$, $F_3 \phi^{-2} - F_1 = 2(2 - \phi) - 1 = 3 - 2\phi = -\phi^{-3} = (-1)^3 \phi^{-3}$ (since $\phi^{-3} = \phi^{-1} - \phi^{-2} = (\phi - 1) - (2 - \phi) = 2\phi - 3$). For $m \ge 3$,
   $$F_{m+1}\phi^{-2} - F_{m-1} = (F_m\phi^{-2} - F_{m-2}) + (F_{m-1}\phi^{-2} - F_{m-3}) = (-1)^m \phi^{-m} + (-1)^{m-1} \phi^{-(m-1)} = (-1)^m \phi^{-m}(1 - \phi) = (-1)^{m+1} \phi^{-(m+1)},$$
   using $\phi - 1 = \phi^{-1}$. Since $\phi^{-m} \le \phi^{-2} < \frac{1}{2}$, $\|F_m \phi^{-2}\|_{\mathbb{Z}} = \phi^{-m}$ and $|\sin(F_m \theta/2)| = \sin(\pi \phi^{-m})$.

2. First note that $F_m F_{m-3} - F_{m-1} F_{m-2} = (-1)^m$ for all $m \ge 3$: at $m = 3$ this is $2\cdot 0 - 1\cdot 1 = -1$, and inductively $F_{m+1}F_{m-2} - F_m F_{m-1} = (F_m + F_{m-1})F_{m-2} - F_m(F_{m-2} + F_{m-3}) = -(F_m F_{m-3} - F_{m-1}F_{m-2})$.

   Now let $1 \le d < F_{m+1}$ with $d \notin \{F_{m-1}, F_m\}$, and let $q \in \mathbb{Z}$ be a nearest integer to $d\phi^{-2}$, so $|d\phi^{-2} - q| = \|d\phi^{-2}\|_{\mathbb{Z}}$. Since $\det \begin{pmatrix} F_m & F_{m-1} \\ F_{m-2} & F_{m-3} \end{pmatrix} = (-1)^m \in \{\pm 1\}$, there exist unique integers $a, b \in \mathbb{Z}$ such that
   $$d = a F_m + b F_{m-1}, \qquad q = a F_{m-2} + b F_{m-3}.$$
   By part (1),
   $$d\phi^{-2} - q = a(-1)^m \phi^{-m} + b(-1)^{m-1}\phi^{-(m-1)} = (-1)^m \phi^{-m}(a - b\phi),$$
   so $\|d\phi^{-2}\|_{\mathbb{Z}} = |a - b\phi|\phi^{-m}$. Consider all cases for $(a, b) \in \mathbb{Z}^2$:
   - If $b = 0$: $d = a F_m$ with $a \ge 1$. Since $m \ge 3$, $F_{m-1} < F_m$, so $F_{m+1} = F_m + F_{m-1} < 2 F_m$, forcing $a = 1$ and $d = F_m$, excluded.
   - If $a = 0$: $d = b F_{m-1}$ with $b \ge 1$. Since $d \neq F_{m-1}$, we have $b \ge 2$, whence $|a - b\phi| = b\phi \ge 2\phi > \phi^2$ (as $2 > \phi$), giving $\|d\phi^{-2}\|_{\mathbb{Z}} > \phi^{-(m-2)}$.
   - If $a \ge 1$ and $b \ge 1$: then $d = a F_m + b F_{m-1} \ge F_m + F_{m-1} = F_{m+1}$, impossible.
   - If $a \le -1$ and $b \le -1$: then $d < 0$, impossible.
   - If $ab < 0$: then $|a - b\phi| = |a| + |b|\phi \ge 1 + \phi = \phi^2$, giving $\|d\phi^{-2}\|_{\mathbb{Z}} \ge \phi^{-(m-2)}$. $\square$

---

### Lemma 2 (Elementary Bounds and Transition Thresholds $k^*_m$ for $m \ge 16$)
1. For every $x \in (0, 1)$,
   $$1 + \frac{x}{2} - \frac{x^2}{8} < \sqrt{1+x} < 1 + \frac{x}{2}, \qquad 1 - \frac{x}{2} < \frac{4}{(1+\sqrt{1+x})^2} < 1 - \frac{x}{2} + \frac{x^2}{2}, \qquad \sqrt{1+x} + \sqrt{1-x} < 2\left(1 - \frac{x^2}{8}\right).$$
   For every $t \in (0, 1)$, $t^2(1 - t^2/3) < \sin^2 t < t^2$.
2. For every integer $m \ge 16$, define $f_m(k) := D^2(k, k + F_m) - D^2(k, k + F_{m+1})$ for $k > 0$. Then $f'_m(k) > 0$ for all $k \ge F_{m+1}$, and $f_m$ has a unique zero $k^*_m$ in $[F_{m+1}, \infty)$, which satisfies
   $$\bigl(1 - 6\phi^{-m}\bigr) K_m < k^*_m < K_m.$$

**Proof.**
1. For $x \in (0, 1)$: $(1 + x/2)^2 = 1 + x + x^2/4 > 1 + x$, and $(1 + x/2 - x^2/8)^2 = 1 + x - \frac{x^3}{8}(1 - x/8) < 1 + x$, proving the first pair of inequalities. Using these, $(1 + \sqrt{1+x})^2 = 2 + x + 2\sqrt{1+x} < 4(1 + x/2)$, so $\frac{4}{(1+\sqrt{1+x})^2} > \frac{1}{1+x/2} > 1 - \frac{x}{2}$ (as $1 - x^2/4 < 1$); conversely $(1 + \sqrt{1+x})^2 > 4(1 + \frac{x}{2} - \frac{x^2}{16})$, and $(1 + \frac{x}{2} - \frac{x^2}{16})(1 - \frac{x}{2} + \frac{x^2}{2}) = 1 + \frac{3}{16}x^2 + \frac{9}{32}x^3 - \frac{1}{32}x^4 > 1$, proving the second pair. For the third inequality, $(\sqrt{1+x} + \sqrt{1-x})^2 = 2 + 2\sqrt{1-x^2} = 4 - \frac{2x^2}{1+\sqrt{1-x^2}} < 4 - x^2 < 4(1 - x^2/8)^2$. Finally, for $t \in (0, 1)$, $0 < t - t^3/6 < \sin t < t$ gives $\sin^2 t > t^2(1 - t^2/6)^2 > t^2(1 - t^2/3)$.

2. Fix $m \ge 16$. Differentiating $D^2(k, k+d) = 2k + d - 2\sqrt{k(k+d)}\cos(d\theta)$ with respect to $k > 0$ yields
   $$\frac{d}{dk} D^2(k, k+d) = 2 - \frac{2k+d}{\sqrt{k(k+d)}}\cos(d\theta) = 4\sin^2\!\left(\frac{d\theta}{2}\right) - \frac{d^2 \cos(d\theta)}{\sqrt{k(k+d)}\bigl(\sqrt{k+d} + \sqrt{k}\bigr)^2},$$
   using $\frac{2k+d}{\sqrt{k(k+d)}} - 2 = \frac{(\sqrt{k+d} - \sqrt{k})^2}{\sqrt{k(k+d)}} = \frac{d^2}{\sqrt{k(k+d)}(\sqrt{k+d}+\sqrt{k})^2}$. Therefore,
   $$f'_m(k) = 4\bigl(\sin^2(\pi\phi^{-m}) - \sin^2(\pi\phi^{-(m+1)})\bigr) + \frac{F_{m+1}^2 \cos(F_{m+1}\theta)}{\sqrt{k(k+F_{m+1})}(\sqrt{k+F_{m+1}}+\sqrt{k})^2} - \frac{F_m^2 \cos(F_m\theta)}{\sqrt{k(k+F_m)}(\sqrt{k+F_m}+\sqrt{k})^2}.$$
   Since $0 < \pi\phi^{-(m+1)} < \pi\phi^{-m} < \frac{\pi}{4}$, we have $\sin^2(\pi\phi^{-m}) > \sin^2(\pi\phi^{-(m+1)})$ and $\cos(F_{m+1}\theta) = 1 - 2\sin^2(\pi\phi^{-(m+1)}) > 1 - 2\sin^2(\pi\phi^{-m}) = \cos(F_m\theta) > 0$. For all $k \ge F_{m+1} > F_m$,
   $$\sqrt{\frac{k+F_{m+1}}{k+F_m}} \left(\frac{\sqrt{k+F_{m+1}}+\sqrt{k}}{\sqrt{k+F_m}+\sqrt{k}}\right)^2 < \sqrt{2}\left(\frac{\sqrt{2}+1}{2}\right)^2 = \frac{4 + 3\sqrt{2}}{4} < 2.07 < 2.61 < \left(\frac{F_{m+1}}{F_m}\right)^2,$$
   where $F_{m+1}/F_m \ge F_{18}/F_{17} = 2584/1597 > 1.618$ for all $m \ge 16$ (and $F_{17}/F_{16} = 1597/987 > 1.618$). Hence both the angular and radial differences in $f'_m(k)$ are strictly positive, so $f'_m(k) > 0$ on $[F_{m+1}, \infty)$.

   We next record basic Binet and trigonometric bounds valid for all $r \ge 16$ (note $\phi^{16} = 2207 - \phi^{-16} > 2206$ and $\phi^{-32} < 2.1 \times 10^{-7}$):
   $$\left|\frac{\sqrt{5}\,F_r}{\phi^r} - 1\right| = \phi^{-2r} < 10^{-6}, \qquad \left|\frac{5 F_r^2}{\phi^{2r}} - 1\right| = \bigl|2(-1)^{r+1}\phi^{-2r} + \phi^{-4r}\bigr| < 3\phi^{-2r},$$
   and $\pi^2 \phi^{-2r}(1 - 4\phi^{-2r}) < \sin^2(\pi\phi^{-r}) < \pi^2 \phi^{-2r}$ (since $\frac{\pi^2}{3} < 4$). Let $x_m := F_m / K_m$ and $x_{m+1} := F_{m+1} / K_m$. Since $\frac{4\pi}{\phi} \in (7.766, 7.767)$ and $4\pi \in (12.566, 12.567)$, Binet's bound yields
   $$7.76\,\phi^{-m} < x_m < 7.77\,\phi^{-m}, \qquad 12.56\,\phi^{-m} < x_{m+1} < 12.57\,\phi^{-m}.$$
   In particular, $x_m < x_{m+1} < 12.57 \phi^{-16} < 0.0057 < 1$, and $(1 - 6\phi^{-m}) K_m > 0.997 K_m > F_{m+1}$.

   *Proof that $f_m(K_m) > 0$:* Writing $R_+(K_m, d) = \frac{d^2}{4K_m}\cdot\frac{4}{(1+\sqrt{1+d/K_m})^2}$ and applying part (1) (noting $1 - x_{m+1}/2 + x_{m+1}^2/2 < 1$ and $1 + x_m/2 < 5/4$), we obtain in units of $\frac{\pi}{\sqrt{5}}$:
   $$\frac{R_+(K_m, F_m) - R_+(K_m, F_{m+1})}{\pi/\sqrt{5}} > \phi^{-1}(1 - 3\phi^{-2m})\!\left(1 - \frac{x_m}{2}\right) - \phi(1 + 3\phi^{-2m-2})\!\left(1 - \frac{x_{m+1}}{2} + \frac{x_{m+1}^2}{2}\right)$$
   $$> (\phi^{-1} - \phi) + \frac{\phi x_{m+1} - \phi^{-1} x_m}{2} - \frac{\phi}{2} x_{m+1}^2 - 6\phi^{-1}\phi^{-2m},$$
   and
   $$\frac{4\sqrt{K_m(K_m+F_m)}\sin^2(\pi\phi^{-m}) - 4\sqrt{K_m(K_m+F_{m+1})}\sin^2(\pi\phi^{-(m+1)})}{\pi/\sqrt{5}}$$
   $$> \phi(1 - 4\phi^{-2m})\!\left(1 + \frac{x_m}{2} - \frac{x_m^2}{8}\right) - \phi^{-1}\!\left(1 + \frac{x_{m+1}}{2}\right) > (\phi - \phi^{-1}) + \frac{\phi x_m - \phi^{-1} x_{m+1}}{2} - \frac{\phi}{8} x_m^2 - 5\phi\,\phi^{-2m}.$$
   Adding these two bounds and using $\phi - \phi^{-1} = 1$,
   $$\frac{f_m(K_m)}{\pi/\sqrt{5}} > \frac{x_m + x_{m+1}}{2} - \frac{\phi}{2} x_{m+1}^2 - \frac{\phi}{8} x_m^2 - (6\phi^{-1} + 5\phi)\phi^{-2m} > 10.16\,\phi^{-m} - 153\,\phi^{-2m} > 0,$$
   since $\phi^m \ge \phi^{16} > 2206 > 153/10.16$.

   *Proof that $f_m((1 - 6\phi^{-m}) K_m) < 0$:* Set $u := 1 - 6\phi^{-m} \in (0.997, 1)$, $y_m := x_m/u < 7.80\,\phi^{-m}$, and $y_{m+1} := x_{m+1}/u < 12.61\,\phi^{-m}$. Applying part (1) symmetrically gives
   $$\frac{R_+(u K_m, F_m) - R_+(u K_m, F_{m+1})}{\pi/\sqrt{5}} < \frac{\phi^{-1}(1 + 3\phi^{-2m})}{u}\!\left(1 - \frac{y_m}{2} + \frac{y_m^2}{2}\right) - \frac{\phi(1 - 3\phi^{-2m-2})}{u}\!\left(1 - \frac{y_{m+1}}{2}\right)$$
   $$< -\frac{1}{u} + \frac{\phi y_{m+1} - \phi^{-1} y_m}{2u} + \frac{\phi^{-1}}{2u} y_m^2 + \frac{6\phi^{-1}}{u}\phi^{-2m},$$
   and
   $$\frac{4\sqrt{uK_m(uK_m+F_m)}\sin^2(\pi\phi^{-m}) - 4\sqrt{uK_m(uK_m+F_{m+1})}\sin^2(\pi\phi^{-(m+1)})}{\pi/\sqrt{5}}$$
   $$< \phi u\!\left(1 + \frac{y_m}{2}\right) - \phi^{-1} u(1 - 4\phi^{-2m-2})\!\left(1 + \frac{y_{m+1}}{2} - \frac{y_{m+1}^2}{8}\right) < u + \frac{\phi x_m - \phi^{-1} x_{m+1}}{2} + \frac{\phi^{-1}}{8} y_{m+1}^2 + 5\phi^{-3}\phi^{-2m}.$$
   Since $\frac{\phi y_{m+1} - \phi^{-1} y_m}{2u} = \frac{\phi x_{m+1} - \phi^{-1} x_m}{2} + \frac{1 - u^2}{2u^2}(\phi x_{m+1} - \phi^{-1} x_m)$ with $\frac{1 - u^2}{2u^2} < \frac{6\phi^{-m}}{0.994} < 6.04\,\phi^{-m}$ and $\phi x_{m+1} - \phi^{-1} x_m < 21\,\phi^{-m}$ (so their product is $< 128\,\phi^{-2m}$), and $u - \frac{1}{u} = -\frac{6\phi^{-m}(2 - 6\phi^{-m})}{1 - 6\phi^{-m}} < -12\phi^{-m}$, summing yields
   $$\frac{f_m(u K_m)}{\pi/\sqrt{5}} < -12\phi^{-m} + \frac{x_m + x_{m+1}}{2} + (128 + 19 + 4 + 13 + 2)\phi^{-2m} < -1.83\,\phi^{-m} + 166\,\phi^{-2m} < 0,$$
   as $\phi^m \ge \phi^{16} > 2206 > 166/1.83$. By continuity and strict monotonicity of $f_m$ on $[F_{m+1}, \infty)$, $k^*_m$ exists, is unique, and satisfies $(1 - 6\phi^{-m})K_m < k^*_m < K_m$. $\square$

---

### Lemma 3 (Backward-Step Comparison Bounds)
1. For every integer $r \ge 16$ and every integer $k$ satisfying $F_r < k \le 0.99\,\phi^{-1} K_r$,
   $$D^2(k, k - F_r) > D^2(k, k + F_r).$$
2. For every integer $m \ge 17$ and every integer $k \ge k^*_{m-1} + F_m$,
   $$D^2(k, k - F_{m-1}) > D^2(k, k + F_m).$$

**Proof.**
1. Set $d := F_r$ and $x := d/k \in (0, 1)$. Using $\sqrt{k(k+d)} - \sqrt{k(k-d)} = \frac{2d}{\sqrt{1+x} + \sqrt{1-x}}$,
   $$D^2(k, k-d) - D^2(k, k+d) = 2\cos(d\theta)\bigl(\sqrt{k(k+d)} - \sqrt{k(k-d)}\bigr) - 2d = 2d\left(\frac{2\cos(d\theta)}{\sqrt{1+x} + \sqrt{1-x}} - 1\right).$$
   By Lemma 2(1), $\sqrt{1+x} + \sqrt{1-x} < 2(1 - x^2/8)$, while $\cos(F_r\theta) = 1 - 2\sin^2(\pi\phi^{-r}) > 1 - 2\pi^2\phi^{-2r}$. Since $k \le 0.99\,\phi^{-1} K_r$ and $F_r > (1 - 10^{-6})\phi^r/\sqrt{5}$, we have
   $$x = \frac{F_r}{k} > \frac{(1 - 10^{-6})\phi^r/\sqrt{5}}{0.99\,\phi^{2r}/(4\sqrt{5}\pi)} = \frac{1 - 10^{-6}}{0.99}\,4\pi\phi^{-r} > 4\pi\phi^{-r},$$
   whence $x^2/8 > 2\pi^2 \phi^{-2r}$, giving $2\cos(F_r\theta) > 2(1 - 2\pi^2\phi^{-2r}) > 2(1 - x^2/8) > \sqrt{1+x} + \sqrt{1-x}$, and thus $D^2(k, k - F_r) > D^2(k, k + F_r)$.

2. Fix $m \ge 17$ and $k \ge k^*_{m-1} + F_m$. Write
   $$D^2(k, k - F_{m-1}) - D^2(k, k + F_m) = f_{m-1}(k) - B_{m-1}(k), \qquad B_{m-1}(k) := D^2(k, k + F_{m-1}) - D^2(k, k - F_{m-1}).$$
   Since $\sqrt{1+x} + \sqrt{1-x} < 2$ for $x = F_{m-1}/k \in (0, 1)$, we have $\sqrt{k(k+F_{m-1})} - \sqrt{k(k-F_{m-1})} > F_{m-1}$; as $\cos(F_{m-1}\theta) > 0$,
   $$B_{m-1}(k) = 2F_{m-1} - 2\cos(F_{m-1}\theta)\bigl(\sqrt{k(k+F_{m-1})} - \sqrt{k(k-F_{m-1})}\bigr) < 2F_{m-1}\bigl(1 - \cos(F_{m-1}\theta)\bigr)$$
   $$= 4F_{m-1}\sin^2(\pi\phi^{-(m-1)}) < 4\pi^2(1 + 10^{-6})\frac{\phi^{m-1}}{\sqrt{5}}\phi^{-2m+2} < 1.00001\,\frac{4\pi^2}{\sqrt{5}}\phi^{1-m}.$$
   On the other hand, by Lemma 2(2), $f_{m-1}(k^*_{m-1}) = 0$ and $f'_{m-1} > 0$ on $[k^*_{m-1}, \infty)$, so
   $$f_{m-1}(k) \ge f_{m-1}(k^*_{m-1} + F_m) = \int_{k^*_{m-1}}^{k^*_{m-1} + F_m} f'_{m-1}(t)\,dt.$$
   For $t \in [k^*_{m-1}, k^*_{m-1} + F_m]$ (where $m \ge 17$), Lemma 2(2) gives $0.997 K_{m-1} < (1 - 6\phi^{-(m-1)})K_{m-1} < k^*_{m-1} \le t < K_{m-1} + F_m < 1.0057 K_{m-1}$ (as $F_m / K_{m-1} \le F_{17} / K_{16} < 0.0057$) and $F_m / t < 0.00572$. Using the derivative formula from Lemma 2(2):
   - Angular term: $4(\sin^2(\pi\phi^{-(m-1)}) - \sin^2(\pi\phi^{-m})) > 4\pi^2(\phi^{2}(1 - 4\phi^{-32}) - 1)\phi^{-2m} > 0.9999 \cdot 4\pi^2 \phi\,\phi^{-2m}$ (since $\phi^2 - 1 = \phi$).
   - Positive radial term: since $\sqrt{t(t+F_m)}(\sqrt{t+F_m}+\sqrt{t})^2 < 4t^2(1 + F_m/t)^{3/2} < 4(1.0057)^2(1.00572)^{3/2} K_{m-1}^2 < 4 \cdot 1.021\,K_{m-1}^2$, $\cos(F_m\theta) > 1 - 2\pi^2\phi^{-34} > 0.99999$, $F_m^2 > (1 - 10^{-5})\phi^{2m}/5$, and $\frac{\phi^{2m}/5}{4 K_{m-1}^2} = 4\pi^2\phi^2\phi^{-2m}$, this term exceeds $\frac{0.99998}{1.021} \cdot 4\pi^2\phi^2\phi^{-2m} > 0.979 \cdot 4\pi^2\phi^2\phi^{-2m}$.
   - Subtracted radial term: since $\sqrt{t(t+F_{m-1})}(\sqrt{t+F_{m-1}}+\sqrt{t})^2 > 4t^2 > 4(0.997)^2 K_{m-1}^2 > 4 \cdot 0.994\,K_{m-1}^2$, $\cos(F_{m-1}\theta) < 1$, $F_{m-1}^2 < (1 + 10^{-5})\phi^{2m-2}/5$, and $\frac{\phi^{2m-2}/5}{4 K_{m-1}^2} = 4\pi^2\phi^{-2m}$, this term is less than $\frac{1.00001}{0.994} \cdot 4\pi^2\phi^{-2m} < 1.007 \cdot 4\pi^2\phi^{-2m}$.

   Combining all three pieces,
   $$f'_{m-1}(t) > 4\pi^2\bigl(0.9999\,\phi + 0.979\,\phi^2 - 1.007\bigr)\phi^{-2m} > 3.16 \cdot 4\pi^2 \phi^{-2m}.$$
   Since $F_m > 0.99999\,\phi^m/\sqrt{5}$, integrating over $[k^*_{m-1}, k^*_{m-1} + F_m]$ yields
   $$f_{m-1}(k) > 3.16 \cdot 0.99999\,\frac{4\pi^2}{\sqrt{5}}\phi^{-m} = (3.16 \cdot 0.99999\,\phi^{-1})\,\frac{4\pi^2}{\sqrt{5}}\phi^{1-m} > 1.95\,\frac{4\pi^2}{\sqrt{5}}\phi^{1-m}.$$
   Therefore $D^2(k, k - F_{m-1}) - D^2(k, k + F_m) = f_{m-1}(k) - B_{m-1}(k) > 0.94\,\frac{4\pi^2}{\sqrt{5}}\phi^{1-m} > 0$. $\square$

---

### Lemma 4 (Dominance of Fibonacci Steps on Plateau $m \ge 17$)
Let $m \ge 17$, and let $k \in \mathbb{Z}$ satisfy $k^*_{m-1} \le k \le k^*_m$.
1. For every integer $j \ge 0$ with $d := |j - k| \notin \{0, F_{m-1}, F_m, F_{m+1}\}$,
   $$D^2(k, j) > D^2(k, k + F_m).$$
2. Moreover, $D^2(k, k - F_{m+1}) > D^2(k, k + F_{m+1}) \ge D^2(k, k + F_m)$.
3. If $k < k^*_m$, then $D^2(k, k + F_m) < D^2(k, k + F_{m+1})$; if $k > k^*_{m-1}$, then $D^2(k, k + F_m) < D^2(k, k + F_{m-1})$.

**Proof.**
Write $u := k / K_m$. By Lemma 2(2), $0.997\,\phi^{-2} < (1 - 6\phi^{-(m-1)})\phi^{-2} < k^*_{m-1}/K_m \le u \le k^*_m/K_m < 1$. Since $m \ge 17$, we have $F_m/k < 0.00572$, $F_{m+1}/k < 0.00926 < 0.01$, and $F_{m+2}/k < 0.0150 < 0.016$.

*Upper bound on $D^2(k, k + F_m)$:* Using $R_+(k, F_m) < F_m^2/(4k)$, $\sqrt{k(k+F_m)} < k(1 + F_m/(2k)) < 1.003 k$, $\sin^2(\pi\phi^{-m}) < \pi^2\phi^{-2m}$, and $F_m^2 < (1 + 10^{-5})\phi^{2m}/5$,
$$D^2(k, k + F_m) < 1.003\,\frac{\pi}{\sqrt{5}}\!\left(\frac{\phi^{-1}}{u} + \phi u\right).$$
Since $u \mapsto \phi^{-1}/u + \phi u$ is convex on $(0, \infty)$, its maximum on $[0.997\phi^{-2}, 1]$ occurs at an endpoint: at $u = 1$ it equals $\phi^{-1} + \phi = \sqrt{5}$, and at $u = 0.997\phi^{-2}$ it equals $\frac{\phi}{0.997} + 0.997\phi^{-1} < 1.0023\sqrt{5}$. Hence
$$D^2(k, k + F_m) < 1.003 \cdot 1.0023\,\pi < 3.161.$$

Now let $j \ge 0$ with $d = |j - k| \notin \{0, F_{m-1}, F_m, F_{m+1}\}$. We check three exhaustive cases:
- *Case A ($d \ge F_{m+2}$):* Using $R_-(k, d) > R_+(k, d)$ (when $j < k$), $R_+(k, d) \ge R_+(k, F_{m+2}) > \frac{F_{m+2}^2}{4k(1 + F_{m+2}/(2k))}$, $F_{m+2}/(2k) < 0.008$, and $u < 1$,
  $$D^2(k, j) \ge R_+(k, F_{m+2}) > \frac{1 - 10^{-5}}{1.008}\,\frac{\pi}{\sqrt{5}}\,\frac{\phi^3}{u} > 0.992\,\frac{\pi}{\sqrt{5}}\,\phi^3 > 5.90 > 3.161.$$
- *Case B ($1 \le d < F_{m+1}$ and $d \notin \{F_{m-1}, F_m\}$):* By Lemma 1(2), $\|d\phi^{-2}\|_{\mathbb{Z}} \ge \phi^{-(m-2)}$. Because $\sin(\pi t)$ is increasing on $[0, \frac{1}{2}]$ and $\phi^{-(m-2)} \le \phi^{-15} < 0.00074 < \frac{1}{2}$, Lemma 2(1) gives $\sin^2(\pi\|d\phi^{-2}\|_{\mathbb{Z}}) \ge \sin^2(\pi\phi^{-(m-2)}) > 0.99999\,\pi^2\phi^{-2m+4}$. Also $\sqrt{kj} \ge \sqrt{k(k - F_{m+1})} > k(1 - F_{m+1}/k) > 0.99 k$. Thus
  $$D^2(k, j) \ge 4\sqrt{kj}\sin^2(\pi\|d\phi^{-2}\|_{\mathbb{Z}}) > 0.989\,\frac{\pi}{\sqrt{5}}\,\phi^5 u > 0.989 \cdot 0.997\,\frac{\pi}{\sqrt{5}}\,\phi^3 > 5.86 > 3.161.$$
- *Case C ($F_{m+1} < d < F_{m+2}$):* Applying Lemma 1(2) with $m + 1$ in place of $m$ gives $\|d\phi^{-2}\|_{\mathbb{Z}} \ge \phi^{-(m-1)}$, so $\sin^2(\pi\|d\phi^{-2}\|_{\mathbb{Z}}) > 0.99999\,\pi^2\phi^{-2m+2}$. Moreover $\sqrt{kj} > k(1 - F_{m+2}/k) > 0.984 k$ and $R_\pm(k, d) \ge R_+(k, F_{m+1}) > \frac{F_{m+1}^2}{4k(1 + F_{m+1}/(2k))} > 0.995\,\frac{\pi}{\sqrt{5}}\,\frac{\phi}{u}$. Combining radial and angular terms and applying AM–GM ($\frac{\phi}{u} + \phi^3 u \ge 2\phi^2$),
  $$D^2(k, j) > 0.983\,\frac{\pi}{\sqrt{5}}\!\left(\frac{\phi}{u} + \phi^3 u\right) \ge 0.983\,\frac{\pi}{\sqrt{5}}\cdot 2\phi^2 > 7.23 > 3.161.$$

This proves (1). Part (2) follows from Lemma 3(1) with $r = m + 1$, since $F_{m+1} < k < K_m < 0.99\,\phi K_m = 0.99\,\phi^{-1} K_{m+1}$, together with $f_m(k) \le 0$ for $k \le k^*_m$ (Lemma 2(2)). Part (3) is immediate from $f_m(k^*_m) = 0$, $f_{m-1}(k^*_{m-1}) = 0$, and the strict monotonicity of $f_m$ and $f_{m-1}$ on $[F_{m+1}, \infty)$ established in Lemma 2(2). $\square$

---

## Finite Base Case and Proof of the Main Theorem

### Proposition 1 (Certified Base Case $0 \le n \le 460$)
Using certified interval arithmetic (`mpmath.iv` at 50 decimal digits with exact integer angular pruning; see `verify.py`), for every $1 \le n \le 460$ there is a unique strict nearest unvisited point $p_{a(n)}$ from $p_{a(n-1)}$ (minimum certified gap $\min_{j \neq a(n)} D^2(a(n-1), j) - D^2(a(n-1), a(n)) > 2.5 \times 10^{-3}$), and the resulting prefix satisfies:
1. $0 = a(0) < a(1) < \cdots < a(460) = 280{,}542$, with $a(459) = 279{,}555 = a(460) - F_{16}$.
2. Every first difference $a(n) - a(n-1)$ ($1 \le n \le 460$) is a Fibonacci number, running monotonically through $F_2, F_4, F_5, \dots, F_{16}$.
3. $a(n) \le \frac{3}{2} n^2$ for all $0 \le n \le 460$ (in fact $\max_{1 \le n \le 460} a(n)/n^2 = a(352)/352^2 = 173{,}946/123{,}904 < 1.404$).
4. $f_{16}(279{,}555) < 0 < f_{16}(280{,}542)$, so $k^*_{16} < a(460) < k^*_{16} + F_{16}$.
5. $460 > \frac{\phi^{18}}{4\pi} \approx 459.80$.

---

### Theorem 1 (Monotonicity, Plateau Structure, and Irvine's Conjecture)
Under any tie-breaking rule, the OEIS A396911 walk satisfies:
1. $a(n)$ is strictly increasing for all $n \ge 0$, every first difference $a(n+1) - a(n)$ is a Fibonacci number advancing monotonically through $F_2, F_4, F_5, F_6, \dots$, and there is an increasing sequence of plateau endpoints $460 = n_{16} < n_{17} < n_{18} < \cdots$ such that for every $m \ge 17$:
   - $a(n_{m-1} + j) = a(n_{m-1}) + j F_m$ for all $0 \le j \le L_m := n_m - n_{m-1}$,
   - $k^*_m \le a(n_m) \le k^*_m + F_m$, and $a(n_m - 1) = a(n_m) - F_m$.
2. For all $n \ge 0$,
   $$a(n) \le \frac{3}{2} n^2.$$
   Moreover, $a(n) < 1.43\,n^2$ for all $n \ge 460$ and $\limsup_{n \to \infty} a(n)/n^2 = \pi/\sqrt{5} < 3/2$.

**Proof.**
#### Part 1 (Inductive Plateau Structure for $m \ge 17$)
We prove by induction on $m \ge 17$ that if the walk reaches step $n_{m-1}$ at $k_0 := a(n_{m-1})$ with $k^*_{m-1} \le k_0 \le k^*_{m-1} + F_{m-1}$, $k_0 - F_{m-1}$ already visited, all previously visited indices contained in $[0, k_0]$, and (in the hypothetical case $k_0 = k^*_{m-1}$) the tie-breaking choice from $k_0$ taking $+F_m$:
then the walk takes $L_m \ge 1$ consecutive steps of $+F_m$ until reaching $a(n_m)$ satisfying the exact same inductive hypothesis for $m + 1$.

The base case $m = 17$ ($n_{16} = 460$, $k_0 = 280{,}542 > k^*_{16}$, $k_0 - F_{16} = a(459)$ visited, all visited indices in $[0, k_0]$) holds by Proposition 1.

Now fix $m \ge 17$ and consider step $r \ge 0$ of plateau $m$ from $k = k_0 + r F_m$ while $k \le k^*_m$ (note that all indices $> k$ are unvisited):
- *First step ($r = 0$, $k = k_0$):* Note $k_0 \le k^*_{m-1} + F_{m-1} < 1.004 K_{m-1} = 1.004\phi^{-2} K_m < 0.39 K_m < 0.99\phi^{-1} K_m$ and $k_0 > F_m$, so Lemma 3(1) gives $D^2(k_0, k_0 - F_m) > D^2(k_0, k_0 + F_m)$; moreover $k_0 - F_{m-1}$ is already visited. By Lemma 4(1)–(3) (and $k_0 < k^*_m$ since $1.004\phi^{-2} < 0.997 < k^*_m/K_m$):
  - If $k_0 > k^*_{m-1}$, then $D^2(k_0, k_0 + F_m) < D^2(k_0, k_0 + F_{m-1})$, so $k_0 + F_m$ is the unique strict nearest unvisited point.
  - If $k_0 = k^*_{m-1}$, then $k_0 + F_{m-1}$ and $k_0 + F_m$ tie strictly ahead of all other unvisited points, and by hypothesis the tie-breaking rule chooses $+F_m$, advancing to $k_1 = k_0 + F_m$.
- *Subsequent steps ($r \ge 1$, $k = k_0 + r F_m \le k^*_m$):* Here $k \ge k^*_{m-1} + F_m > k^*_{m-1}$, and $k - F_m = k_0 + (r - 1) F_m$ is already visited. By Lemma 3(2), $D^2(k, k - F_{m-1}) > D^2(k, k + F_m)$, and by Lemma 4(1)–(3), $D^2(k, k + F_m)$ strictly beats every other unvisited point except possibly $k + F_{m+1}$ when $k = k^*_m$.
  - If $k < k^*_m$, then $D^2(k, k + F_m) < D^2(k, k + F_{m+1})$, so $k + F_m$ is the unique strict nearest unvisited point.
  - Since $F_m > 0$, after finitely many steps $r \ge 1$ the walk first hits $k = k_0 + r F_m \ge k^*_m$.
    - If $k > k^*_m$, then $k^*_m < k \le k^*_m + F_m$ and $k - F_m$ is visited; set $n_m := n_{m-1} + r$.
    - If $k = k^*_m$, then $k + F_m$ and $k + F_{m+1}$ tie strictly ahead of all other unvisited points: if tie-breaking selects $+F_m$, the walk moves to $k + F_m = k^*_m + F_m$ (with $k^*_m$ visited) and we set $n_m := n_{m-1} + r + 1$; if tie-breaking selects $+F_{m+1}$, we set $n_m := n_{m-1} + r$ (so $a(n_m) = k^*_m$ with $k^*_m - F_m$ visited, and the tie-breaking choice from $k^*_m$ takes $+F_{m+1}$).

In all cases, the inductive hypothesis holds for $m + 1$ with $k^*_m \le a(n_m) \le k^*_m + F_m$ and $a(n_m - 1) = a(n_m) - F_m$. This completes the proof of Part 1.

#### Part 2 (Effective Bound $a(n) \le \frac{3}{2} n^2$)
For $0 \le n \le 460$, $a(n) \le \frac{3}{2} n^2$ holds by Proposition 1(3). Now let $m \ge 17$. By Part 1 and Lemma 2(2),
$$a(n_m) - a(n_{m-1}) \ge k^*_m - (k^*_{m-1} + F_{m-1}) > (1 - 6\phi^{-m}) K_m - K_{m-1} - F_{m-1} = (\phi^{-1} - 6\phi^{-m}) K_m - F_{m-1}.$$
Dividing by $F_m < (1 + 10^{-6})\phi^m/\sqrt{5}$ and using $\frac{\phi^{-1} K_m}{\phi^m/\sqrt{5}} = \frac{\phi^m}{4\pi}$, $\frac{6\phi^{-m} K_m}{\phi^m/\sqrt{5}} = \frac{6\phi}{4\pi} < 0.773$, and $\frac{F_{m-1}}{F_m} < 0.62$,
$$L_m = \frac{a(n_m) - a(n_{m-1})}{F_m} > \frac{\phi^m}{4\pi(1 + 10^{-6})} - 0.773 - 0.62 > \frac{\phi^m}{4\pi}(1 - 10^{-6}) - 1.40.$$
Since $\frac{\phi^m}{4\pi} \ge \frac{\phi^{17}}{4\pi} > 284.1$ for $m \ge 17$, we have $1.40 < 0.005\,\frac{\phi^m}{4\pi}$, and therefore
$$L_m > 0.994\,\frac{\phi^m}{4\pi} \qquad \text{for all } m \ge 17.$$
Combining this with Proposition 1(5) ($n_{16} = 460 > \frac{\phi^{18}}{4\pi} > 0.994\,\frac{\phi^{18}}{4\pi}$) and the exact geometric identity $\phi^{18} + \sum_{r=17}^m \phi^r = \phi^{18} + \frac{\phi^{m+1} - \phi^{17}}{\phi - 1} = \phi^{m+2}$ yields
$$n_m = n_{16} + \sum_{r=17}^m L_r > 0.994\,\frac{\phi^{m+2}}{4\pi} \qquad \text{for all } m \ge 16.$$

Now consider any $n \ge 460$. Choose $m \ge 17$ and $0 \le j \le L_m$ such that $n = n_{m-1} + j$, so $a(n) = a(n_{m-1}) + j F_m$. Since $F_{m-1} / K_{m-1} \le F_{16} / K_{16} < 0.0036$ for $m \ge 17$, we have
$$a(n_{m-1}) \le K_{m-1} + F_{m-1} < A := 1.004\,\frac{\phi^{2m-1}}{4\sqrt{5}\pi}, \qquad F_m < B := 1.001\,\frac{\phi^m}{\sqrt{5}}, \qquad n_{m-1} > N := 0.994\,\frac{\phi^{m+1}}{4\pi}.$$
Observe that $B N = (1.001)(0.994)\frac{\phi^{2m+1}}{4\sqrt{5}\pi} > 0.9949\,\frac{\phi^{2m+1}}{4\sqrt{5}\pi}$, so
$$B N - A > (0.9949 - 1.004\,\phi^{-2})\,\frac{\phi^{2m+1}}{4\sqrt{5}\pi} > 0.6114\,\frac{\phi^{2m+1}}{4\sqrt{5}\pi} > 0.$$
For any positive reals $A, B, N$ with $BN > A$ and any $j \ge 0$, the identity
$$\frac{B^2}{4(BN - A)} - \frac{A + Bj}{(N + j)^2} = \frac{\bigl(Bj - (BN - 2A)\bigr)^2}{4(BN - A)(N + j)^2} \ge 0$$
implies
$$\frac{a(n)}{n^2} = \frac{a(n_{m-1}) + j F_m}{(n_{m-1} + j)^2} < \frac{A + Bj}{(N + j)^2} \le \frac{B^2}{4(BN - A)} < \frac{(1.001)^2}{0.6114\,\phi}\cdot\frac{\pi}{\sqrt{5}} < \frac{1.0021}{0.989}\cdot 1.405 < 1.43 < \frac{3}{2}.$$

Finally, the same two-sided bounds $L_m = \frac{\phi^m}{4\pi} + O(1)$, $n_m = \frac{\phi^{m+2}}{4\pi} + O(m)$, $a(n_{m-1}) = (1 + O(\phi^{-m}))K_{m-1}$, and $F_m = (1 + O(\phi^{-2m}))\phi^m/\sqrt{5}$ show that the maximum of $a(n)/n^2$ on plateau $m$ (attained near $j = \lfloor (BN - 2A)/B \rfloor \sim \frac{\phi^m}{4\pi}(1 - 2\phi^{-2}) \in (0, L_m)$) converges to $\frac{(\phi^m/\sqrt{5})^2}{4\phi^{-1} K_m} = \frac{\pi}{\sqrt{5}}$ as $m \to \infty$, giving $\limsup_{n\to\infty} a(n)/n^2 = \pi/\sqrt{5}$. $\square$
