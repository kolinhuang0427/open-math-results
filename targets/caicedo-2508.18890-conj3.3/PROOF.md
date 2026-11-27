# Proof of Caicedo–Juhnke–Poullot Conjecture 3.4 (`arXiv:2508.18890v4`)

**Conjecture 3.4 (`arXiv:2508.18890v4`, `Ehrhart_non_positivity.tex` lines 109–111; folder slug `conj3.3`):**
For every integer $n \ge 5$, if the $\mathbf{s}$-lecture hall simplex $\mathcal{P}_n^{(a,\dots,a,a+1)}$ is Ehrhart non-positive for some $a \in \mathbb{N}_{\ge 1}$, then for all integers $b \ge a$, $\mathcal{P}_n^{(b,\dots,b,b+1)}$ is also Ehrhart non-positive.

We prove this unconditionally for all $n \ge 5$ and all $a \le b \in \mathbb{N}_{\ge 1}$.

---

## 1. Exact Ehrhart Polynomial and Generating Function

Let $\mathcal{L}_n(t, a) := \mathcal{L}_{\mathcal{P}_n^{(a,\dots,a,a+1)}}(t)$ for integers $n \ge 1, a \ge 1$.

**Lemma 1.** For all integers $n \ge 1$ and $a \ge 1$,
$$\mathcal{L}_n(t, a) = \binom{at + n}{n} + \sum_{\ell=0}^{t-1} \binom{a\ell + n - 1}{n - 1}. \tag{1}$$
Consequently, for every integer $k \ge 1$, the generating function of $[t^k]\mathcal{L}_n(t, a)$ over $n \ge k$ is
$$\sum_{n \ge k} \Bigl([t^k] \mathcal{L}_n(t, a)\Bigr) x^n = \frac{(a u(x))^k}{k!} \, F_a(x), \tag{2}$$
where $u(x) := -\ln(1 - x) = \sum_{m \ge 1} \frac{x^m}{m}$ and
$$F_a(x) := \frac{1}{1 - x} + \frac{x(1 - x)^{a-1}}{1 - (1 - x)^a} = 1 + \frac{1}{1 - x} - \frac{1}{a} \sum_{m=1}^{a-1} \frac{1}{1 - x / x_m}, \qquad x_m := 1 - e^{2\pi i m / a}. \tag{3}$$

*Proof.* By Caicedo–Juhnke–Poullot (`Ehrhart_non_positivity.tex`, Eq. (384)–(402) and lines 81–85), letting $\mathbf{a}^{(m)} = (a, \dots, a)$ of length $m$, Proposition 3.1 gives $h_{\mathcal{P}_n^{(a,\dots,a,a+1)}}^*(t) = h_{\mathcal{P}_n^{\mathbf{a}^{(n)}}}^*(t) + t\, h_{\mathcal{P}_{n-1}^{\mathbf{a}^{(n-1)}}}^*(t)$. Applying Beck–Robins' $h^*$-to-Ehrhart identity yields
$$\mathcal{L}_n(t, a) = \binom{at+n}{n} + \sum_{i=0}^{n-1} h_i^*(\mathbf{a}^{(n-1)}) \binom{t + n - 1 - i}{n}.$$
Using $\binom{t+n-1-i}{n} = \sum_{\ell=0}^{t-1} \binom{\ell + n - 1 - i}{n - 1}$ (summation of binomial coefficients) and $\sum_{i=0}^{n-1} h_i^*(\mathbf{a}^{(n-1)}) \binom{\ell + n - 1 - i}{n - 1} = \mathcal{L}_{\mathcal{P}_{n-1}^{\mathbf{a}^{(n-1)}}}(\ell) = \binom{a\ell + n - 1}{n - 1}$ proves (1). (This also follows from the pyramid decomposition in lines 81–85; note line 88 of the preprint has a harmless misprint $\binom{a\ell+n}{n}$ inside the sum, whereas Example 3.3 and lines 399–402 use the true formula (1).)

Summing (1) against $x^n$ over $n \ge 0$ (using $\sum_{n \ge 0} \binom{M + n}{n} x^n = (1-x)^{-(M+1)}$ and adjusting the $n=0$ term for the second sum, which vanishes for $t \ge 1$ at $n=0$):
$$\sum_{n \ge 0} \mathcal{L}_n(t, a) x^n = (1 - x)^{-at - 1} + \sum_{\ell=0}^{t-1} x (1 - x)^{-a\ell - 1} = e^{(at + 1) u(x)} + (e^{u(x)} - 1) \frac{e^{at u(x)} - 1}{e^{a u(x)} - 1}.$$
For any $k \ge 1$, extracting $[t^k]$ replaces $e^{at u(x)}$ by $\frac{(a u(x))^k}{k!}$ and drops the $-1$ constant, giving
$$\sum_{n \ge k} \Bigl([t^k] \mathcal{L}_n(t, a)\Bigr) x^n = \frac{(a u(x))^k}{k!} \left( e^{u(x)} + \frac{e^{u(x)} - 1}{e^{a u(x)} - 1} \right) = \frac{(a u(x))^k}{k!} F_a(x),$$
since $e^{-u(x)} = 1 - x$. For the partial fraction identity (3) when $a \ge 2$, notice $F_a(x) \to 1$ as $x \to \infty$ (since $\frac{x(1-x)^{a-1}}{1 - (1-x)^a} \to 1$), $F_a$ has only simple poles at $x = 1$ (residue $-1$, as $x(1-x)^{a-1}$ vanishes at $x=1$) and $x = x_m = 1 - \zeta^m$ ($1 \le m \le a - 1$, $\zeta = e^{2\pi i / a}$), where
$$\mathrm{Res}_{x = x_m} \frac{x(1-x)^{a-1}}{1 - (1-x)^a} = \frac{x_m \zeta^{m(a-1)}}{a \zeta^{m(a-1)}} = \frac{x_m}{a} \implies \frac{x_m/a}{x - x_m} = -\frac{1}{a} \frac{1}{1 - x/x_m}. \quad \square$$

---

## 2. Ehrhart Positivity for $1 \le a \le 6$

**Lemma 2.** For every $a \in \{1, 2, 3, 4, 5, 6\}$ and every $n \ge 1$, the simplex $\mathcal{P}_n^{(a,\dots,a,a+1)}$ is Ehrhart positive.

*Proof.* Write $F_a(x) = \sum_{n \ge 0} f_{a,n} x^n$. Since $u(x) = \sum_{m \ge 1} \frac{x^m}{m}$ has non-negative Taylor coefficients, $[x^m] \frac{(au)^k}{k!} \ge 0$ for all $m, k \ge 0$ (and $> 0$ for $m \ge k$). By (2), it suffices to show $f_{a,n} > 0$ for all $n \ge 0$.

- For $a = 1$, $F_1(x) = 1 + \frac{1}{1-x} = 2 + \sum_{n \ge 1} x^n$, so $f_{1,n} \ge 1 > 0$.
- For $2 \le a \le 6$, $f_{a,0} = F_a(0) = 1 + \frac{1}{a} > 0$. By (3), for all $n \ge 1$:
  $$f_{a,n} = 1 - \frac{1}{a} \sum_{m=1}^{a-1} x_m^{-n}.$$
  Since $|x_m| = |1 - e^{2\pi i m/a}| = 2\sin\!\left(\frac{\pi m}{a}\right) \ge 2\sin\!\left(\frac{\pi}{a}\right) \ge 2\sin\!\left(\frac{\pi}{6}\right) = 1$ for all $1 \le m \le a - 1$, we have $|x_m|^{-n} \le |x_m|^{-1}$ for every $n \ge 1$. Thus
  $$f_{a,n} \ge 1 - \frac{1}{a} \sum_{m=1}^{a-1} \frac{1}{2\sin(\pi m / a)}.$$
  Explicitly:
  - $a = 2$: $\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4} < 1$;
  - $a = 3$: $\frac{1}{3} \cdot \frac{2}{\sqrt{3}} < 0.39 < 1$;
  - $a = 4$: $\frac{1}{4}\left(\frac{2}{\sqrt{2}} + \frac{1}{2}\right) < 0.48 < 1$;
  - $a = 5$: $\frac{1}{5}\left(\frac{2}{2\sin(\pi/5)} + \frac{2}{2\sin(2\pi/5)}\right) < 0.56 < 1$;
  - $a = 6$: $\frac{1}{6}\left(2\cdot 1 + \frac{2}{\sqrt{3}} + \frac{1}{2}\right) < 0.61 < 1$.
  Hence $f_{a,n} > 0$ for all $n \ge 0$, proving $[t^k] \mathcal{L}_n(t,a) > 0$ for all $1 \le k \le n$. $\square$

---

## 3. Exact Verification for $5 \le n \le 32$

**Lemma 3.** For every integer $5 \le n \le 32$, there exists an integer $m_n \ge 7$ such that $\mathcal{P}_n^{(a,\dots,a,a+1)}$ is Ehrhart positive for $1 \le a < m_n$ and Ehrhart non-positive for all integers $a \ge m_n$.

*Proof.* From (1), using $(at+1)(at+2)\cdots(at+n) = \sum_{k=0}^n \left[{n+1 \atop k+1}\right] (at)^k$ and Faulhaber's formula $\sum_{\ell=0}^{t-1} \ell^j = \frac{B_{j+1}(t) - B_{j+1}(0)}{j+1}$ (with $B_1^- = -\frac{1}{2}$), each coefficient $[t^k] \mathcal{L}_n(t, a)$ ($1 \le k \le n$) is an explicit polynomial in $\mathbb{Q}[a]$ of degree $\le n$:
$$[t^k] \mathcal{L}_n(t, a) = \frac{\left[{n+1 \atop k+1}\right]}{n!} a^k + \sum_{j=k-1}^{n-1} \frac{\left[{n \atop j+1}\right] \binom{j}{k-1}}{(n-1)!\, k} B_{j+1-k}^- \, a^j. \tag{4}$$
For each $5 \le n \le 32$ and $1 \le k \le n$, `verify.py` performs exact rational Sturm/root interval isolation (`sympy.Poly.intervals()`) on each polynomial in (4), obtaining the exact finite union of intervals on $[1, \infty)$ where $[t^k]\mathcal{L}_n(t,a) < 0$. In every case $5 \le n \le 32$, the set of integers $a \ge 1$ where at least one coefficient is strictly negative is precisely $[m_n, \infty) \cap \mathbb{N}$ (with $m_n \in [7, 18]$). $\square$

---

## 4. Non-Positivity for $a \ge 2 n^{4/3}$

**Lemma 4.** For every $n \ge 5$ and every integer $a \ge 2 n^{4/3}$, we have $[t^{n-4}] \mathcal{L}_n(t, a) < 0$.

*Proof.* Setting $k = n - 4$ in (4), only $j \in \{n-5, n-4, n-3, n-2, n-1\}$ appear in the sum, with $B_3^- = 0$ eliminating $j = n - 2$. Using the closed forms for $\left[{n \atop n-m}\right]$ ($0 \le m \le 4$):
$$\frac{720 (n-4)!}{a^{n-5}} [t^{n-4}]\mathcal{L}_n(t,a) = -a^4 + \left(\frac{15}{2}n^2 - \frac{5}{2}n\right) a^2 + \left(\frac{15}{8}n^4 - \frac{15}{4}n^3 + \frac{65}{8}n^2 - \frac{9}{4}n - 1\right)a + \frac{15}{8}n^4 - \frac{15}{4}n^3 + \frac{5}{8}n^2 + \frac{1}{4}n.$$
(Verified symbolically in `verify.py`.) For $n \ge 5$ and $a \ge 2n^{4/3}$, we have $a > 17$:
- $\left(\frac{15}{2}n^2 - \frac{5}{2}n\right) a^2 < \frac{15}{2} n^2 a^2 \le \frac{15}{8} n^{-2/3} a^4 < 0.65\, a^4$;
- $-\frac{15}{4}n^3 + \frac{65}{8}n^2 - \frac{9}{4}n - 1 < 0$ for all $n \ge 5$, and $-\frac{15}{4}n^3 + \frac{5}{8}n^2 + \frac{1}{4}n < 0$ for all $n \ge 5$, so the $a^1$ and $a^0$ terms together are bounded by $\frac{15}{8} n^4 (a + 1) \le \frac{15}{8} \cdot \frac{a^3}{8} (a + 1) = \frac{15}{64} a^4 (1 + 1/a) < 0.25\, a^4$.
Since $0.65 + 0.25 = 0.90 < 1$, the right-hand side is strictly negative. $\square$

---

## 5. Non-Positivity for $n \ge 33$ and $8 \le a < 2 n^{4/3}$

**Lemma 5.** For every integer $n \ge 33$ and every integer $8 \le a < 2 n^{4/3}$, at least one coefficient $[t^k]\mathcal{L}_n(t, a)$ with $k \in \{1, 2, 3, 4\}$ is strictly negative.

*Proof.* Let $c_{r,k} := [x^r] \frac{u(x)^k}{k!} = \frac{\left[{r \atop k}\right]}{r!} \ge 0$. Notice two universal bounds:
1. $c_{r,k} = \frac{\left[{r \atop k}\right]}{r!} \le \frac{\sum_{j=1}^r \left[{r \atop j}\right]}{r!} = 1$ for all $r, k \ge 1$;
2. $\sum_{r=k}^n c_{r,k} \le \frac{1}{k!} \left(\sum_{r=1}^n \frac{1}{r}\right)^k = \frac{H_n^k}{k!}$.

Note also that since $x_1 = 1 - e^{2\pi i / a}$, we have $u(x_1) = -\ln(e^{2\pi i/a}) = -\frac{2\pi i}{a}$, so $\frac{(a u(x_1))^k}{k!} = \frac{(-2\pi i)^k}{k!} = \frac{(2\pi)^k}{k!} e^{-i k\pi/2}$, and similarly for $x_{a-1} = \overline{x_1}$. Letting $\theta_a := \arg(x_1) = -\frac{\pi}{2} + \frac{\pi}{a}$, the sum of the $m=1$ and $m=a-1$ pole contributions is
$$M_k(n, a) := -\frac{2}{a} \frac{(2\pi)^k}{k!} |x_1|^{-n} \cos\!\left(-n \theta_a - \frac{k\pi}{2}\right), \qquad |x_1| = 2\sin\!\left(\frac{\pi}{a}\right).$$
As $k$ varies over $\{1, 2, 3, 4\}$, $\cos(-n\theta_a - k\pi/2)$ sweeps $\{\pm\sin(n\theta_a), \pm\cos(n\theta_a)\}$, so for every $(n, a)$ there exists $k \in \{1, 2, 3, 4\}$ with $\cos(-n\theta_a - k\pi/2) \ge \frac{1}{\sqrt{2}}$, making $M_k(n, a) \le -\frac{\sqrt{2}}{a} \frac{(2\pi)^k}{k!} |x_1|^{-n} < 0$. We bound the remaining terms below $|M_k(n,a)|$ in two cases:

### Case 5a: $a \in \{8, 9, 10\}$, $n \ge 33$
By (3), $[t^k]\mathcal{L}_n(t,a) - M_k(n,a)$ equals
$$a^k \left(c_{n,k} + \sum_{r=k}^n c_{r,k}\right) + \frac{2 a^k}{a} \mathrm{Re}\!\left( x_1^{-n} \sum_{r=n+1}^\infty c_{r,k} x_1^r \right) - \frac{a^k}{a} \sum_{m=2}^{a-2} \sum_{r=k}^n c_{r,k} x_m^{r-n}.$$
Since $|x_1| < 1$ and $c_{r,k} \le 1$, the second term is bounded in modulus by $\frac{2 a^k}{a} \frac{|x_1|}{1 - |x_1|}$. Since $|x_m| \ge 2\sin(2\pi/10) > 1.175 > 1$ for all $2 \le m \le a - 2$ when $a \in \{8,9,10\}$, the third term is bounded in modulus by $a^{k-1} \sum_{m=2}^{a-2} \frac{1}{1 - |x_m|^{-1}}$. Using $c_{n,k} + \sum_{r=k}^n c_{r,k} \le 1 + \frac{H_n^k}{k!}$, the total error divided by $|M_k(n,a)|$ is bounded by
$$\frac{a^{k+1} k!}{\sqrt{2}(2\pi)^k} \left(1 + \frac{H_n^k}{k!} + \frac{2|x_1|}{a(1-|x_1|)} + \frac{1}{a}\sum_{m=2}^{a-2}\frac{1}{1 - |x_m|^{-1}}\right) |x_1|^n.$$
Since $H_n$ increases while $|x_1|^n$ decays geometrically, passing from $n$ to $n+1$ for any $n \ge 33$, $a \in \{8,9,10\}$, and $k \in \{1,2,3,4\}$ multiplies this upper bound by at most $\left(\frac{H_{n+1}}{H_n}\right)^4 |x_1| \le \left(1 + \frac{1}{34 H_{33}}\right)^4 \cdot 2\sin\!\left(\frac{\pi}{8}\right) < 0.79 < 1$, so the bound is strictly decreasing in $n \ge 33$. Evaluating at $n = 33$ in `verify.py` via exact interval arithmetic confirms it is strictly less than $1$ for every $a \in \{8, 9, 10\}$ and $k \in \{1, 2, 3, 4\}$.

### Case 5b: $11 \le a < 2 n^{4/3}$, $n \ge 33$
Write $F_a(x) = \frac{1}{1 - x} + G_a(x)$ with $G_a(x) := \frac{x(1-x)^{a-1}}{1 - (1-x)^a}$. Separating the $\frac{1}{1-x}$ term gives an error $E_1 \le a^k \frac{H_n^k}{k!}$. For the $G_a(x)$ term, set $R_a := 3\sin(\pi/a) = \frac{3}{2}|x_1| < 1$ (since $R_a \le 3\sin(\pi/11) < 0.846$). Because $R_a < 1$, the disk $|x| \le R_a$ avoids the branch cut $[1, \infty)$ of $u(x)$ and contains only the poles $x_1, \overline{x_1}$ of $G_a(x)$ (since $|x_2| = 2\sin(2\pi/a) = 4\cos(\pi/a)\sin(\pi/a) > 3\sin(\pi/a) = R_a$ for $a \ge 11$). By Cauchy's residue theorem,
$$[x^n]\left( G_a(x) \frac{(a u(x))^k}{k!} \right) = M_k(n, a) + \frac{1}{2\pi i} \oint_{|x| = R_a} \frac{G_a(x) (a u(x))^k}{k!\, x^{n+1}}\, dx.$$
On $|x| = R_a$:
1. $a |u(x)| \le a (-\ln(1 - R_a)) = (a R_a)\frac{-\ln(1-R_a)}{R_a} \le 3\pi \frac{-\ln(1 - 3\sin(\pi/11))}{3\sin(\pi/11)} < 21$;
2. Setting $z = 1 - x = r e^{i\phi}$, we have $|z - 1| = R_a$ and $a |x| \le 3\pi$. Observe that $|z^{a-1}/(1 - z^a)| \le |1 - z^a|^{-1}$ when $r \le 1$, whereas $|z^{a-1}/(1 - z^a)| = (r |1 - z^{-a}|)^{-1} < |1 - z^{-a}|^{-1}$ when $r > 1$, so it suffices to prove $|1 - z^{\pm a}| > 0.85$ uniformly for all $a \ge 11$:
   - $|\sin\phi| \le R_a = 3\sin(\pi/a)$ gives $|\phi| \le \arcsin(3\sin(\pi/a))$; since $g(u) := \arcsin(3\sin u)$ satisfies $g(0)=0$ and $g'(u) = 3/\sqrt{1 - 8\tan^2 u}$ is strictly increasing on $(0, \pi/11]$ (with $8\tan^2(\pi/11) < 0.7 < 1$), $g$ is strictly convex on $[0, \pi/11]$, so $g(u)/u$ increases on $(0, \pi/11]$. Hence $a|\phi| \le \pi \frac{g(\pi/a)}{\pi/a}$ decreases for $a \ge 11$, giving $a|\phi| \le 12\arcsin(3\sin(\pi/12)) < \frac{7\pi}{2}$ for $a \ge 12$ and $a|\phi| \le 11\arcsin(3\sin(\pi/11)) < 3.53\pi$ for $a = 11$;
   - Whenever $\cos(a\phi) \le 0$, $\mathrm{Re}(1 - z^{\pm a}) = 1 - r^{\pm a}\cos(a\phi) \ge 1$, so $|1 - z^{\pm a}| \ge 1$;
   - When $a|\phi| < \frac{\pi}{2}$ or $a|\phi| \in (\frac{3\pi}{2}, \frac{5\pi}{2})$ (so $a|\phi| \le \frac{5\pi}{2}$), $|r e^{i\phi} - 1|^2 = R_a^2$ yields $r^2 - 2r\cos\phi + (1 - R_a^2) = 0$, i.e., $r_\pm = \cos\phi \pm \sqrt{R_a^2 - \sin^2\phi}$. For all $a \ge 11$, concavity of $\sin$ gives $R_a = 3\sin(\pi/a) \ge \frac{c\pi}{a}$ with $c := \frac{3\sin(\pi/11)}{\pi/11} > 2.959$, while $|\sin\phi| \le |\phi| \le \frac{2.5\pi}{a}$, so $\sqrt{R_a^2 - \sin^2\phi} \ge \frac{\pi\sqrt{c^2 - 2.5^2}}{a} > \frac{4.975}{a}$. Also $1 - \cos\phi \le \frac{\phi^2}{2} \le \frac{25\pi^2}{8a^2} \le \frac{2.804}{a}$ for $a \ge 11$. Hence $1 - r_- \ge \sqrt{R_a^2 - \sin^2\phi} > \frac{4.975}{a}$, giving $r_-^a < (1 - \frac{4.975}{a})^a < e^{-4.975} < 0.007$, and $r_+ - 1 > \frac{4.975 - 2.804}{a} = \frac{2.171}{a}$, giving $r_+^{-a} < (1 + \frac{2.171}{a})^{-a} \le (1 + \frac{2.171}{11})^{-11} < 0.138$. Thus $|1 - z^a| \ge 1 - r_-^a > 0.993 > 0.85$ (when $r = r_- \le 1$) and $|1 - z^{-a}| \ge 1 - r_+^{-a} > 1 - 0.138 = 0.862 > 0.85$ (when $r = r_+ > 1$) for every $a \ge 11$;
   - At $a = 11$ for $a|\phi| \in (\frac{7\pi}{2}, 3.53\pi)$, the identity $|1 - R e^{i\theta}|^2 = (R - \cos\theta)^2 + \sin^2\theta \ge \sin^2\theta$ gives $|1 - z^{\pm 11}| \ge |\sin(11\phi)| > 0.99$.
   Hence $a |G_a(x)| \le \frac{3\pi}{0.85} < 11.1$ for all $a \ge 11$ and $|x| = R_a$.

Thus the contour integral is bounded in modulus by $E_2 \le \frac{11.1}{a} \frac{21^k}{k!} R_a^{-n} = \frac{11.1}{a} \frac{21^k}{k!} (1.5)^{-n} |x_1|^{-n}$. Therefore, for all $n \ge 33$, $a \ge 11$, and $k \in \{1, 2, 3, 4\}$:
$$\frac{E_1 + E_2}{|M_k(n,a)|} \le \frac{1}{\sqrt{2}(2\pi)^k} a^{k+1} H_n^k \left(2\sin\frac{\pi}{a}\right)^n + \frac{11.1}{\sqrt{2}} \left(\frac{21}{2\pi}\right)^k (1.5)^{-n}.$$
For fixed $n \ge 33$ and $1 \le k \le 4$, $\frac{\partial}{\partial a}\ln\bigl(a^{k+1}(2\sin(\pi/a))^n\bigr) = \frac{1}{a}\bigl(k + 1 - n\frac{\pi/a}{\tan(\pi/a)}\bigr) \le \frac{1}{a}\bigl(5 - 33\frac{\pi/11}{\tan(\pi/11)}\bigr) < -27/a < 0$ for all $a \ge 11$ (since $u/\tan u$ is decreasing on $(0, \pi/2)$), so the first term is strictly decreasing in $a \ge 11$ and hence maximized at $a = 11$. Moreover, at $a = 11$, increasing $n \to n+1$ multiplies the first term by $\left(\frac{H_{n+1}}{H_n}\right)^k \cdot 2\sin(\pi/11) \le \left(1 + \frac{1}{34 H_{33}}\right)^4 \cdot 2\sin(\pi/11) < 0.58 < 1$, and multiplies the second term by $(1.5)^{-1} < 1$. Evaluating at $n = 33, a = 11$ in `verify.py` gives $< 0.002 < 1$ for every $k \in \{1, 2, 3, 4\}$, proving $\frac{E_1+E_2}{|M_k(n,a)|} < 1$ for **all** $n \ge 33$ and **all** $a \ge 11$. Therefore $[t^k]\mathcal{L}_n(t, a) < 0$. $\square$

---

## 6. Conclusion

Let $n \ge 5$ and suppose $\mathcal{P}_n^{(a,\dots,a,a+1)}$ is Ehrhart non-positive. Let $b \ge a$.
- If $5 \le n \le 32$, Lemma 3 implies $\mathcal{P}_n^{(b,\dots,b,b+1)}$ is Ehrhart non-positive for all $b \ge a$.
- If $n \ge 33$, Lemma 2 forces $a \ge 7$, so either $b = a$ (non-positive by hypothesis) or $b \ge 8$, in which case Lemmas 4 and 5 show $\mathcal{P}_n^{(b,\dots,b,b+1)}$ is Ehrhart non-positive.

This completes the proof of Conjecture 3.4 (`arXiv:2508.18890v4`, folder slug `conj3.3`) for all $n \ge 5$. $\blacksquare$
