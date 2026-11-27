# Proof of OEIS A028495 Asymptotic Ratio Conjectures

We prove Bill McEachen's Feb 11, 2026 conjectures on [OEIS A028495](https://oeis.org/A028495) (rev. 162):
$$\lim_{n \to \infty} \frac{a(n)}{a(n-1)} = 2\cos(\pi/7) = \sqrt{2 + 2\cos(2\pi/7)},$$
i.e., $a(n) \sim \alpha \cdot a(n-1)$ with $\alpha = 2\cos(\pi/7)$ (whose decimal expansion is A160389) and $\alpha = \sqrt{2 + 2\cos(2\pi/7)}$ (where $2 + 2\cos(2\pi/7)$ is A116425).

## 1. Characteristic Polynomial and Its Roots

Let $A(x) = \sum_{n=0}^{\infty} a(n) x^n = \frac{1 - x^2}{1 - x - 2x^2 + x^3}$. Its reciprocal denominator polynomial is
$$P(r) := r^3 - r^2 - 2r + 1 = x^{-3}(1 - x - 2x^2 + x^3)\big|_{x = 1/r}.$$

**Lemma 1 (Exact trigonometric roots and strict dominance).** *The three roots of $P(r) = 0$ are the distinct real numbers*
$$r_1 = 2\cos(\pi/7), \qquad r_2 = 2\cos(3\pi/7), \qquad r_3 = 2\cos(5\pi/7),$$
*and they satisfy*
$$r_1 \in \left(\frac{3}{2}, 2\right), \qquad r_2 \in \left(0, \frac{1}{2}\right), \qquad r_3 \in \left(-\frac{3}{2}, -1\right),$$
*so $r_1 > |r_3| > r_2 > 0$. Moreover, $2\cos(\pi/7) = \sqrt{2 + 2\cos(2\pi/7)}$.*

*Proof.* For each $k \in \{1, 3, 5\}$, let $\zeta = e^{i k \pi / 7}$ and $r = \zeta + \zeta^{-1} = 2\cos(k\pi/7)$. Since $\zeta^7 = e^{i k \pi} = -1$ and $\zeta \ne -1$, we have $\frac{\zeta^7 + 1}{\zeta + 1} = \zeta^6 - \zeta^5 + \zeta^4 - \zeta^3 + \zeta^2 - \zeta + 1 = 0$. Dividing by $\zeta^3$ gives
$$(\zeta^3 + \zeta^{-3}) - (\zeta^2 + \zeta^{-2}) + (\zeta + \zeta^{-1}) - 1 = 0.$$
Using $\zeta^2 + \zeta^{-2} = r^2 - 2$ and $\zeta^3 + \zeta^{-3} = r^3 - 3r$, this simplifies to
$$(r^3 - 3r) - (r^2 - 2) + r - 1 = r^3 - r^2 - 2r + 1 = P(r) = 0.$$
Because $\cos$ is strictly decreasing on $[0, \pi]$, the three values $r_1 > r_2 > r_3$ are distinct and hence exhaust all roots of the cubic $P(r)$.

Evaluating $P(r)$ at rational endpoints:
$$P\!\left(-\frac{3}{2}\right) = -\frac{13}{8} < 0 < 1 = P(-1), \qquad P(0) = 1 > 0 > -\frac{1}{8} = P\!\left(\frac{1}{2}\right), \qquad P\!\left(\frac{3}{2}\right) = -\frac{7}{8} < 0 < 1 = P(2).$$
By the Intermediate Value Theorem and the ordering $r_3 < r_2 < r_1$, we have $r_3 \in (-3/2, -1)$, $r_2 \in (0, 1/2)$, and $r_1 \in (3/2, 2)$, whence $r_1 > \frac{3}{2} > |r_3| > 1 > \frac{1}{2} > r_2 > 0$. Finally, since $\cos(\pi/7) > 0$, the half-angle identity $(2\cos(\pi/7))^2 = 4\cos^2(\pi/7) = 2 + 2\cos(2\pi/7)$ gives $2\cos(\pi/7) = \sqrt{2 + 2\cos(2\pi/7)}$. $\square$

## 2. Partial Fractions and Exact Asymptotic Formula

**Theorem.** *For all $n \ge 0$,*
$$a(n) = \sum_{j=1}^{3} c_j r_j^n, \qquad\text{where}\quad c_j := \frac{r_j^2 - 1}{P'(r_j)} \quad (j = 1, 2, 3),$$
*with $c_1 > 0$. Consequently, $\lim_{n \to \infty} \frac{a(n)}{a(n-1)} = r_1 = 2\cos(\pi/7) = \sqrt{2 + 2\cos(2\pi/7)}$.*

*Proof.* Factor $1 - x - 2x^2 + x^3 = \prod_{j=1}^{3}(1 - r_j x)$. Because $r_1, r_2, r_3$ are distinct, partial fraction decomposition gives
$$\frac{1 - x^2}{1 - x - 2x^2 + x^3} = \sum_{j=1}^{3} \frac{c_j}{1 - r_j x},$$
where $c_j = \lim_{x \to 1/r_j} \frac{(1 - r_j x)(1 - x^2)}{\prod_{i=1}^3(1 - r_i x)} = \frac{1 - r_j^{-2}}{\prod_{i \ne j}(1 - r_i/r_j)} = \frac{r_j^2 - 1}{\prod_{i \ne j}(r_j - r_i)} = \frac{r_j^2 - 1}{P'(r_j)}$.
Expanding $(1 - r_j x)^{-1} = \sum_{n=0}^{\infty} r_j^n x^n$ yields $a(n) = \sum_{j=1}^{3} c_j r_j^n$ for all $n \ge 0$.

By Lemma 1, $r_1 > 3/2$ and $r_1 > r_2 > r_3$, so $r_1^2 - 1 > 5/4 > 0$ and $P'(r_1) = (r_1 - r_2)(r_1 - r_3) > 0$, hence $c_1 > 0$. In particular, for all sufficiently large $n$ we have $a(n) \ne 0$ and
$$a(n) = c_1 r_1^n \left(1 + \frac{c_2}{c_1}\left(\frac{r_2}{r_1}\right)^n + \frac{c_3}{c_1}\left(\frac{r_3}{r_1}\right)^n\right).$$
Since $|r_2 / r_1| < \frac{1/2}{3/2} = \frac{1}{3} < 1$ and $|r_3 / r_1| < \frac{3/2}{3/2} = 1$ (in fact $P(-3/2) < 0$ gives $|r_3| < 3/2 < r_1$, so $|r_3 / r_1| < 1$), both $(r_2 / r_1)^n \to 0$ and $(r_3 / r_1)^n \to 0$ as $n \to \infty$. Therefore $a(n) \sim c_1 r_1^n$, so
$$\lim_{n \to \infty} \frac{a(n)}{a(n-1)} = r_1 = 2\cos(\pi/7) = \sqrt{2 + 2\cos(2\pi/7)}. \qquad \square$$
